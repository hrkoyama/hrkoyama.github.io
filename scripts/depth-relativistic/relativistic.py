"""1D seven-component ideal RMHD finite volumes; c=4pi=1, fixed normal Bx.

U=(D,Sx,Sy,Sz,E,By,Bz); E includes rest mass. Full magnetic stress and
induction are evolved, including when the exact Alfvén wave is incompressible.
"""
import numpy as np


class PhysicsFailure(ValueError):
    """An unmodified failed candidate plus available stage diagnostics."""
    def __init__(self,message,**payload):
        super().__init__(message)
        self.payload=payload


def state(w, bx, gamma):
    rho = w[..., 0]; v = w[..., 1:4]; p = w[..., 4]
    B = np.concatenate([np.full(rho.shape+(1,), bx), w[..., 5:7]], axis=-1)
    v2 = np.sum(v*v, axis=-1); b2 = np.sum(B*B, axis=-1); vb = np.sum(v*B, axis=-1)
    if np.any(rho <= 0) or np.any(p <= 0) or np.any(v2 >= 1) or not np.all(np.isfinite(w)):
        raise ValueError('nonphysical primitive state; no floor/repair')
    W = 1/np.sqrt(1-v2); Z = (rho+gamma/(gamma-1)*p)*W*W
    S = (Z+b2)[..., None]*v-vb[..., None]*B
    E = Z-p+.5*(b2*(1+v2)-vb*vb)
    U = np.concatenate([(rho*W)[..., None], S, E[..., None], B[..., 1:]], axis=-1)
    pt = p+.5*(b2*(1-v2)+vb*vb)
    mom = S*v[..., 0, None]-bx*(B*(1-v2)[..., None]+vb[..., None]*v)
    mom[..., 0] += pt
    induction = v[..., 0, None]*B[..., 1:]-bx*v[..., 1:]
    F = np.concatenate([(rho*W*v[..., 0])[..., None], mom, S[..., 0, None], induction], axis=-1)
    return U, F


def recover(U, bx, gamma, tolerance=2e-13, maximum_iterations=80):
    """Bracketed scalar Z=rho*h*W² recovery, with safeguarded Newton steps.

    Inadmissible trial Z moves the lower root bracket; it never clips an evolved
    state. Square-root sentinels apply ONLY to invalid root trials, not physics.
    """
    D = U[..., 0]; S = U[..., 1:4]; E = U[..., 4]
    B = np.concatenate([np.full(D.shape+(1,), bx), U[..., 5:]], axis=-1)
    if np.any(D <= 0) or np.any(E <= 0) or not np.all(np.isfinite(U)):
        raise ValueError('nonpositive/nonfinite conserved state')
    b2 = np.sum(B*B, axis=-1); sb = np.sum(S*B, axis=-1)
    scale = np.maximum(1., abs(E)+np.sqrt(np.sum(S*S, axis=-1))+b2)
    a = (gamma-1)/gamma
    def evaluate(z):
        v = (S+(sb/z)[..., None]*B)/(z+b2)[..., None]
        v2 = np.sum(v*v, axis=-1); g = 1-v2
        sq = np.sqrt(np.where(g > 0, g, 1.))
        p = a*(z*g-D*sq)
        valid = (g > 0)&(p > 0)
        residual = z-p+.5*(b2*(1+v2)-(sb/z)**2)-E
        dv = -((sb/(z*z))[..., None]*B+v)/(z+b2)[..., None]
        v2d = 2*np.sum(v*dv, axis=-1)
        pd = a*(g-z*v2d+D*v2d/(2*sq))
        derivative = 1-pd+.5*b2*v2d+sb*sb/(z*z*z)
        return residual, derivative, valid, v, p, sq
    lo = D.copy(); hi = 2*(abs(E)+D+b2+np.sqrt(np.sum(S*S, axis=-1))+1)
    f, _, valid, _, _, _ = evaluate(hi)
    if not np.all(valid&(f > 0)):
        raise ValueError('failed physical upper recovery bracket')
    z = .5*(lo+hi); active = np.ones(D.shape, dtype=bool); fallbacks = 0
    for iteration in range(1, maximum_iterations+1):
        f, derivative, valid, v, p, sq = evaluate(z)
        active = ~((abs(f) <= tolerance*scale)&valid)
        if not np.any(active): break
        lower = (~valid)|(f < 0)
        lo = np.where(active&lower, z, lo); hi = np.where(active&~lower, z, hi)
        proposal = z-f/derivative
        safe = valid&np.isfinite(proposal)&(proposal > lo)&(proposal < hi)
        fallbacks += int(np.count_nonzero(active&~safe))
        z = np.where(active, np.where(safe, proposal, .5*(lo+hi)), z)
    else: raise ValueError('primitive recovery iteration cap; no state repair')
    w = np.concatenate([(D*sq)[..., None], v, p[..., None], U[..., 5:]], axis=-1)
    rebuilt, _ = state(w, bx, gamma)
    defect = float(np.max(abs(rebuilt-U)/np.maximum(1., abs(U))))
    return w, dict(iterations=iteration, root_residual=float(np.max(abs(f)/scale)),
                   roundtrip_residual=defect, safeguarded_root_steps=fallbacks)


def minmod(a, b):
    return np.where(a*b > 0, np.sign(a)*np.minimum(abs(a), abs(b)), 0.)


def operator(U, bx, gamma, dx, periodic):
    w, stats = recover(U, bx, gamma)
    ghost = np.pad(w, ((2, 2), (0, 0)), mode='wrap' if periodic else 'edge')
    slopes = minmod(ghost[1:-1]-ghost[:-2], ghost[2:]-ghost[1:-1])
    left = ghost[1:-2]+.5*slopes[:-1]
    right = ghost[2:-1]-.5*slopes[1:]
    try:
        ul, fl = state(left, bx, gamma); ur, fr = state(right, bx, gamma)
    except ValueError as error:
        raise PhysicsFailure(str(error),face_left=left.copy(),face_right=right.copy(),
                             face_primitives_available=True) from error
    # Exact causal bounds sL=-1,sR=+1; intentionally more diffusive than fast-wave estimates.
    flux = .5*(fl+fr-(ur-ul))
    rhs = -(flux[1:]-flux[:-1])/dx
    stats.update(minimum_density=float(w[:, 0].min()), minimum_pressure=float(w[:, 4].min()),
                 maximum_speed=float(np.sqrt(np.sum(w[:, 1:4]**2, axis=1)).max()),
                 face_minimum_density=float(min(left[:, 0].min(), right[:, 0].min())),
                 face_minimum_pressure=float(min(left[:, 4].min(), right[:, 4].min())),
                 face_maximum_speed=float(max(np.sqrt(np.sum(left[:, 1:4]**2, axis=1)).max(),np.sqrt(np.sum(right[:, 1:4]**2, axis=1)).max())))
    return rhs, flux[-1]-flux[0], stats


def solve(initial, bx, gamma, final_time, periodic, cfl=.35, snapshots=5):
    U = initial.copy(); n = len(U); dx = 1/n; t = 0.; step = 0
    targets = np.linspace(0, final_time, snapshots); saved = [U.copy()]; times = [0.]
    initial_total = dx*U.sum(axis=0); boundary_integral = np.zeros(7); history = []
    stage_rows = []; next_save = 1
    while t < final_time:
        dt = min(cfl*dx, targets[next_save]-t)
        last_valid=U.copy();stage=0;candidate=U;stage_time=t
        try:
            k0, b0, s0 = operator(candidate, bx, gamma, dx, periodic); a = U+dt*k0
            stage=1;candidate=a;stage_time=t+dt
            k1, b1, s1 = operator(candidate, bx, gamma, dx, periodic); b = .75*U+.25*(a+dt*k1)
            stage=2;candidate=b;stage_time=t+.5*dt
            k2, b2, s2 = operator(candidate, bx, gamma, dx, periodic)
            candidate=U/3+2*(b+dt*k2)/3;stage=3;stage_time=t+dt
            w, last = recover(candidate, bx, gamma)
            U=candidate
        except ValueError as error:
            payload=dict(getattr(error,'payload',{}))
            payload.update(candidate_U=candidate.copy(),last_valid_U=last_valid,
                           time=t,stage_time=stage_time,dt=dt,step=step+1,stage=stage,
                           bx=bx,gamma=gamma)
            payload.setdefault('face_left',np.empty((0,7)))
            payload.setdefault('face_right',np.empty((0,7)))
            payload.setdefault('face_primitives_available',False)
            raise PhysicsFailure(str(error),**payload) from error
        step += 1; t += dt
        boundary_integral += dt*(b0/6+b1/6+2*b2/3)
        residual = dx*U.sum(axis=0)-initial_total+boundary_integral
        for k, s in enumerate([s0, s1, s2, {**s2, **last,
              'minimum_density':float(w[:,0].min()),'minimum_pressure':float(w[:,4].min()),
              'maximum_speed':float(np.sqrt(np.sum(w[:,1:4]**2,axis=1)).max())}]):
            stage_rows.append([step,k,t,s['minimum_density'],s['minimum_pressure'],s['maximum_speed'],s['root_residual'],s['roundtrip_residual'],s['iterations'],s['safeguarded_root_steps'],s['face_minimum_density'],s['face_minimum_pressure'],s['face_maximum_speed']])
        history.append([t, *residual, *boundary_integral])
        if t >= targets[next_save]-2e-14:
            t = float(targets[next_save]); saved.append(U.copy()); times.append(t); next_save += 1
            if next_save == len(targets): break
    return dict(U=U, U_initial=initial, U_history=np.asarray(saved), snapshot_times=np.asarray(times),
                primitive=w, stages=np.asarray(stage_rows), conservation=np.asarray(history),
                x=(np.arange(n)+.5)/n, edges=np.linspace(0,1,n+1), steps=step, time=t,
                state_floor_count=0, retries=0, rejected_steps=0)
