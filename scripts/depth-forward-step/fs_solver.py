"""Aligned forward-facing step: first-order 2D HLL + Heun, with face budgets.

Derived from the published Numart shock_cases.py baseline. States are indexed
[x,y,(rho,rho*u,rho*v,E)]. Solid cells are inactive storage, never fluid cells.
There is no corner entropy fix, floor, repair or hidden time-step retry.
"""
import numpy as np

GAMMA = 1.4
BOUNDARIES = ('inlet', 'outlet', 'bottom', 'top', 'vertical_step', 'horizontal_step')


class InvalidStage(ValueError):
    """A raw failed stage is attached for reproducible failure reporting."""


def conserved(w):
    rho,u,v,p = np.moveaxis(np.asarray(w,dtype=float),-1,0)
    return np.stack((rho,rho*u,rho*v,p/(GAMMA-1)+.5*rho*(u*u+v*v)),axis=-1)


def primitive(q):
    q = np.asarray(q)
    if not np.all(np.isfinite(q)) or np.any(q[...,0] <= 0):
        raise ValueError('Invalid density/nonfinite state')
    rho = q[...,0]; u = q[...,1]/rho; v = q[...,2]/rho
    p = (GAMMA-1)*(q[...,3]-.5*(q[...,1]*u+q[...,2]*v))
    if np.any(p <= 0) or not np.all(np.isfinite(p)):
        raise ValueError('Nonpositive pressure')
    return np.stack((rho,u,v,p),axis=-1)


def flux(q,axis,w=None):
    if axis not in (0,1): raise ValueError('Cartesian axis required')
    if w is None: w = primitive(q)
    normal = w[...,1+axis]
    f = q*normal[...,None]; f[...,1+axis] += w[...,3]
    f[...,3] = (q[...,3]+w[...,3])*normal
    return f


def hll(left,right,axis):
    a,b = primitive(left),primitive(right)
    al = np.sqrt(GAMMA*a[...,3]/a[...,0]); ar = np.sqrt(GAMMA*b[...,3]/b[...,0])
    sl = np.minimum(np.minimum(a[...,1+axis]-al,b[...,1+axis]-ar),0.)
    sr = np.maximum(np.maximum(a[...,1+axis]+al,b[...,1+axis]+ar),0.)
    fl,fr = flux(left,axis,a),flux(right,axis,b)
    return (sr[...,None]*fl-sl[...,None]*fr+(sl*sr)[...,None]*(right-left))/(sr-sl)[...,None]


def upstream():
    return conserved([1.4,3.,0.,1.])


def geometry(ny):
    if isinstance(ny,bool) or not isinstance(ny,int) or ny < 10 or ny % 5:
        raise ValueError('Ny must be an integer >=10 divisible by5, aligning both step faces')
    x = (np.arange(3*ny)+.5)/ny; y = (np.arange(ny)+.5)/ny
    fluid = ~((x[:,None] >= .6) & (y[None,:] < .2))
    return x,y,fluid


def initial(ny):
    x,y,fluid = geometry(ny)
    return x,y,fluid,np.broadcast_to(upstream(),(*fluid.shape,4)).copy()


def reflected(q,axis):
    r = q.copy(); r[...,1+axis] *= -1
    return r


def face_fluxes(q,fluid,inflow=None):
    """One shared numerical flux per face, including mirrored step-wall states."""
    if q.shape != (*fluid.shape,4): raise ValueError('State/mask shape mismatch')
    g = np.pad(q,((1,1),(1,1),(0,0)),mode='edge')
    g[0,1:-1] = upstream() if inflow is None else inflow
    g[1:-1,0] = reflected(q[:,0],1)
    g[1:-1,-1] = reflected(q[:,-1],1)
    active = np.pad(fluid,((1,1),(1,1)),mode='edge')
    result = []
    for axis in (0,1):
        left,right = (g[:-1,1:-1],g[1:,1:-1]) if axis == 0 else (g[1:-1,:-1],g[1:-1,1:])
        ml,mr = (active[:-1,1:-1],active[1:,1:-1]) if axis == 0 else (active[1:-1,:-1],active[1:-1,1:])
        f = hll(left,right,axis)
        outward = ml & ~mr; inward = ~ml & mr
        if np.any(outward): f[outward] = hll(left[outward],reflected(left[outward],axis),axis)
        if np.any(inward): f[inward] = hll(reflected(right[inward],axis),right[inward],axis)
        f[~(ml|mr)] = 0.
        result.append((f,ml,mr))
    return result


def rhs(q,fluid,spacing,inflow=None):
    (fx,mxl,mxr),(fy,myl,myr) = face_fluxes(q,fluid,inflow)
    derivative = -(fx[1:]-fx[:-1]+fy[:,1:]-fy[:,:-1])/spacing
    derivative[~fluid] = 0.
    boundary = spacing*np.stack((fx[0].sum(axis=0),-fx[-1].sum(axis=0),
        fy[:,0].sum(axis=0),-fy[:,-1].sum(axis=0),
        fx[~mxl & mxr].sum(axis=0)-fx[mxl & ~mxr].sum(axis=0),
        fy[~myl & myr].sum(axis=0)-fy[myl & ~myr].sum(axis=0)))
    return derivative,boundary


def solve(ny=40,final_time=4.,cfl=.4,max_steps=20000):
    if not np.isfinite(final_time) or final_time <= 0 or not 0 < cfl <= .4:
        raise ValueError('Positive finite time and0<CFL<=.4 required')
    if not isinstance(max_steps,int) or max_steps < 1: raise ValueError('Positive integer step budget required')
    x,y,fluid,q = initial(ny); spacing = 1/ny; area = spacing**2
    initial_integral = area*q[fluid].sum(axis=0); boundary = np.zeros((len(BOUNDARIES),4))
    time = 0.; steps = 0; history = []; minimum_density = float('inf'); minimum_pressure = float('inf')
    def checked(state,stage):
        nonlocal minimum_density,minimum_pressure
        try: w = primitive(state[fluid])
        except ValueError as original:
            error = InvalidStage(str(original)); error.failed_state = state.copy(); error.completed_history = list(history)
            error.failed_context = {'stage':stage,'step':steps,'time':time}; raise error
        minimum_density = min(minimum_density,float(w[...,0].min()))
        minimum_pressure = min(minimum_pressure,float(w[...,3].min()))
        return w
    checked(q,'initial')
    while time < final_time:
        if steps >= max_steps: raise ValueError('Declared step budget exceeded; no hidden retry')
        w = primitive(q[fluid]); sound = np.sqrt(GAMMA*w[...,3]/w[...,0])
        rate = (np.max(abs(w[...,1])+sound)+np.max(abs(w[...,2])+sound))/spacing
        dt = min(cfl/rate,final_time-time)
        if not np.isfinite(dt) or dt <= 0: raise ValueError('Invalid time step')
        f0,b0 = rhs(q,fluid,spacing); predictor = q+dt*f0; checked(predictor,'predictor')
        f1,b1 = rhs(predictor,fluid,spacing); updated = .5*q+.5*(predictor+dt*f1); checked(updated,'update')
        q = updated; boundary += .5*dt*(b0+b1); time += dt; steps += 1
        if steps % 50 == 0 or time >= final_time:
            history.append({'step':steps,'time':time,'dt':dt,'min_density':minimum_density,'min_pressure':minimum_pressure})
    return {'q':q,'x':x,'y':y,'fluid':fluid,'time':time,'steps':steps,'history':history,
        'initial_integral':initial_integral,'final_integral':area*q[fluid].sum(axis=0),
        'boundary_integrals':boundary,'boundary_net_integral':boundary.sum(axis=0),
        'minimum_density':minimum_density,'minimum_pressure':minimum_pressure,
        'state_floor_count':0,'rejected_steps':0}
