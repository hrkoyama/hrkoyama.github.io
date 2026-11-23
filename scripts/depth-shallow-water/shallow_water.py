"""First-order conservative Saint-Venant FV with hydrostatic reconstruction.

No positive water-depth floor, state clipping, retries or rejected steps.
The only max(0,...) is the mathematical hydrostatic face reconstruction.
"""
import numpy as np


class NumericalFailure(ArithmeticError):
    def __init__(self,message,state,history,context):
        super().__init__(message)
        self.state=np.array(state,copy=True);self.history=np.array(history)
        self.context=context


def velocity(state):
    state = np.asarray(state)
    if np.any(state[:, 0] < 0) or np.any((state[:, 0] == 0) & (state[:, 1] != 0)):
        raise ArithmeticError('Invalid dry state')
    out = np.zeros(len(state))
    np.divide(state[:, 1], state[:, 0], out=out, where=state[:, 0] > 0)
    return out


def flux(state, g):
    u = velocity(state)
    return np.column_stack((state[:, 1], state[:, 1]*u+.5*g*state[:, 0]**2))


def hll_parts(left, right, g):
    """HLL as nonnegative directional water-transfer rates plus pressure."""
    ul, ur = velocity(left), velocity(right)
    cl, cr = np.sqrt(g*left[:, 0]), np.sqrt(g*right[:, 0])
    sl, sr = np.minimum(ul-cl, ur-cr), np.maximum(ul+cl, ur+cr)
    rd, ld = right[:, 0] == 0, left[:, 0] == 0
    sl = np.where(rd, ul-cl, sl); sr = np.where(rd, ul+2*cl, sr)
    sl = np.where(ld, ur-2*cr, sl); sr = np.where(ld, ur+cr, sr)
    sl, sr = np.minimum(sl, 0.), np.maximum(sr, 0.)
    wl, wr = np.zeros_like(sl), np.zeros_like(sl)
    np.divide(sr,sr-sl,out=wl,where=sr>sl)
    np.divide(-sl,sr-sl,out=wr,where=sr>sl)
    al, ar = wl*(ul-sl), wr*(sr-ur)
    ml, mr = al*left[:,0], ar*right[:,0]
    pressure = .5*g*(wl*left[:,0]**2+wr*right[:,0]**2)
    value = np.column_stack((ml-mr,ml*ul-mr*ur+pressure))
    return value,float(np.max(np.maximum(-sl,sr))),al,ar,pressure


def hll(left, right, g):
    """HLL with enclosing gravity speeds and exact one-sided dry fan bounds."""
    return hll_parts(left,right,g)[:2]


def interfaces(state, bed, boundary, g, packet_data=False):
    if boundary['kind'] == 'reflecting':
        l, r = state[0].copy(), state[-1].copy(); l[1] *= -1; r[1] *= -1
    elif boundary['kind'] == 'transmissive':
        l, r = state[0], state[-1]
    elif boundary['kind'] == 'subcritical':
        # One imposed datum at each subcritical boundary; extrapolate the other.
        l = np.array([state[0, 0], boundary['discharge']])
        r = np.array([boundary['downstream_depth'], state[-1, 1]])
    else:
        raise ValueError('Unknown boundary')
    extended = np.vstack((l, state, r)); z = np.r_[bed[0], bed, bed[-1]]
    left, right = extended[:-1], extended[1:]
    zstar = np.maximum(z[:-1], z[1:])
    hl = np.maximum(0., left[:, 0]+z[:-1]-zstar)
    hr = np.maximum(0., right[:, 0]+z[1:]-zstar)
    ls = np.column_stack((hl, hl*velocity(left)))
    rs = np.column_stack((hr, hr*velocity(right)))
    common, speed, al, ar, pressure = hll_parts(ls, rs, g)
    left_flux, right_flux = common.copy(), common.copy()
    left_flux[:, 1] += .5*g*(left[:, 0]**2-hl**2)
    right_flux[:, 1] += .5*g*(right[:, 0]**2-hr**2)
    if packet_data:
        return left_flux,right_flux,common,speed,dict(al=al,ar=ar,hl=hl,hr=hr,
            ul=velocity(left),ur=velocity(right),pressure=pressure,
            left_correction=.5*g*(left[:,0]**2-hl**2),
            right_correction=.5*g*(right[:,0]**2-hr**2))
    return left_flux, right_flux, common, speed


def packet_update(state, data, dt_over_dx):
    """Same HR/HLL FE update factored into nonnegative water packets.

    Compute momentum advection from the already-rounded water packets. Thus
    subnormal water transfers that round to zero cannot create a nonzero dry
    momentum. No depth threshold or a posteriori projection is used.
    """
    h=state[:,0];u=velocity(state)
    ratio_right=np.zeros_like(h);ratio_left=np.zeros_like(h)
    np.divide(data['hl'][1:],h,out=ratio_right,where=h>0)
    np.divide(data['hr'][:-1],h,out=ratio_left,where=h>0)
    stay=1-dt_over_dx*(data['al'][1:]*ratio_right+data['ar'][:-1]*ratio_left)
    if np.any(stay<0):raise ArithmeticError('Negative staying coefficient: no repair performed')
    remaining=h*stay
    incoming_left=(dt_over_dx*data['al'][:-1])*data['hl'][:-1]
    incoming_right=(dt_over_dx*data['ar'][1:])*data['hr'][1:]
    new_h=remaining+incoming_left+incoming_right
    impulse=-dt_over_dx*(data['pressure'][1:]+data['left_correction'][1:]
                         -data['pressure'][:-1]-data['right_correction'][:-1])
    new_q=(remaining*u+incoming_left*data['ul'][:-1]
           +incoming_right*data['ur'][1:]+impulse)
    return np.column_stack((new_h,new_q)),float(stay.min())


def solve(initial, bed, dx, final_time, boundary, g=9.81, cfl=.4, max_steps=100000):
    state = np.array(initial, copy=True); velocity(state)
    if not 0 < cfl <= .5: raise ValueError('Require CFL <= .5')
    t, step = 0., 0
    times, history, records = [0.], [state.copy()], []
    targets = np.linspace(0., final_time, 5)
    budget = np.zeros(2)
    initial_total = dx*state.sum(axis=0)
    while t < final_time:
        if step >= max_steps:
            raise NumericalFailure('Step budget exhausted',state,records,dict(time=t,step=step))
        lf, rf, common, speed, data = interfaces(state, bed, boundary, g,packet_data=True)
        next_target = targets[len(times)]
        dt = min(cfl*dx/speed if speed else final_time-t, next_target-t)
        try:
            update,minimum_stay=packet_update(state,data,dt/dx)
        except ArithmeticError as error:
            raise NumericalFailure(str(error),state,records,dict(time=t,step=step,dt=dt)) from error
        if not np.isfinite(update).all() or np.any(update[:, 0] < 0):
            raise NumericalFailure('Nonfinite or negative depth: no repair performed',update,records,
                                   dict(time=t,step=step,dt=dt))
        try:
            velocity(update)
        except ArithmeticError as error:
            raise NumericalFailure(str(error),update,records,dict(time=t,step=step,dt=dt)) from error
        boundary_change = -dt*(common[-1]-common[0])
        # Interface correction difference is the discrete bed-source impulse.
        source_change = -dt*np.sum((lf[1:]-rf[:-1])-(common[1:]-common[:-1]), axis=0)
        predicted = boundary_change+source_change
        defect = dx*(update-state).sum(axis=0)-predicted
        budget += predicted
        total_defect = dx*update.sum(axis=0)-initial_total-budget
        t = next_target if dt == next_target-t else t+dt
        step += 1
        records.append([t, dt, update[:, 0].min(), update[:, 0].max(),
                        np.max(np.abs(velocity(update))), dt*speed/dx,
                        *boundary_change, *source_change, *defect, *total_defect,
                        np.count_nonzero(update[:, 0] == 0),minimum_stay])
        state = update
        if t == next_target:
            times.append(t); history.append(state.copy())
    return dict(state=state, snapshots=np.array(history), snapshot_times=np.array(times),
                steps=step, stages=np.array(records), budget=budget,
                state_clip_count=0, depth_floor_count=0, rejected_steps=0, retries=0)


STAGE_COLUMNS = ['time', 'dt', 'minimum_depth', 'maximum_depth', 'maximum_speed',
                 'face_courant', 'boundary_mass', 'boundary_momentum', 'bed_mass',
                 'bed_momentum', 'step_mass_defect', 'step_momentum_defect',
                 'total_mass_defect', 'total_momentum_defect', 'dry_cells',
                 'minimum_staying_coefficient']
