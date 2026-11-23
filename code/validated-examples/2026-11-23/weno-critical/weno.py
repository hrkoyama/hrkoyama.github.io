"""Scalar finite-volume WENO5; arrays are cell averages, never point samples."""
import numpy as np

LINEAR = np.array([.1, .6, .3])


def reconstruct(stencil, method, epsilon):
    """Left trace at i+1/2, stencil[..., :] = means i-2,...,i+2.

    Return trace, normalized weights, Jiang--Shu indicators and candidates.
    WENO-Z uses power two, explicitly distinct from a power-one variant.
    """
    a = np.asarray(stencil, dtype=float)
    if a.shape[-1] != 5 or not np.all(np.isfinite(a)):
        raise ValueError('Require five finite cell means per stencil')
    if not np.isfinite(epsilon) or epsilon <= 0:
        raise ValueError('epsilon must be finite and positive')
    v, w, x, y, z = np.moveaxis(a, -1, 0)
    candidates = np.stack([(2*v-7*w+11*x)/6, (-w+5*x+2*y)/6,
                           (2*x+5*y-z)/6], axis=-1)
    beta = np.stack([13/12*(v-2*w+x)**2+.25*(v-4*w+3*x)**2,
                     13/12*(w-2*x+y)**2+.25*(w-y)**2,
                     13/12*(x-2*y+z)**2+.25*(3*x-4*y+z)**2], axis=-1)
    denominator = beta+epsilon
    if method == 'weno-js':
        # A common positive scale avoids enormous inverse powers at constants.
        alpha = LINEAR*(np.min(denominator, axis=-1, keepdims=True)/denominator)**2
    elif method == 'weno-z':
        tau = abs(beta[..., 0]-beta[..., 2])[..., None]
        alpha = LINEAR*(1+(tau/denominator)**2)
    else:
        raise ValueError('Unknown WENO method')
    weights = alpha/alpha.sum(axis=-1, keepdims=True)
    return np.sum(weights*candidates, axis=-1), weights, beta, candidates


def epsilon_value(policy, h):
    if policy == 'fixed-1e-40':return 1e-40
    if policy == 'fixed-1e-6':return 1e-6
    if policy == 'h-squared':return h*h
    raise ValueError('Unknown epsilon policy')


def periodic_rhs(q, h, method, epsilon):
    """Unit positive speed; a single shared left-upwind flux per periodic face."""
    q = np.asarray(q, dtype=float)
    if q.ndim != 1 or len(q) < 5 or h <= 0:
        raise ValueError('Require >=5 one-dimensional cell means and h>0')
    stencil = np.stack([np.roll(q, shift) for shift in [2, 1, 0, -1, -2]], axis=-1)
    flux, weights, beta, _ = reconstruct(stencil, method, epsilon)
    rhs = -(flux-np.roll(flux, 1))/h
    return rhs, weights, beta


def transport(initial, method, epsilon, final_time, courant, snapshot_times, max_steps):
    """Classical RK4 with fixed steps landing on requested times; no clipping."""
    q = np.asarray(initial, dtype=float).copy()
    h, time, steps = 1/len(q), 0., 0
    snapshots, history = [q.copy()], []
    for target in snapshot_times[1:]:
        count = int(np.ceil((target-time)/(courant*h)))
        dt, start = (target-time)/count, time
        for j in range(count):
            if steps >= max_steps:raise RuntimeError('fixed step budget exceeded')
            k1, _, _ = periodic_rhs(q, h, method, epsilon)
            stage2 = q+.5*dt*k1
            k2, _, _ = periodic_rhs(stage2, h, method, epsilon)
            stage3 = q+.5*dt*k2
            k3, _, _ = periodic_rhs(stage3, h, method, epsilon)
            stage4 = q+dt*k3
            k4, weights, _ = periodic_rhs(stage4, h, method, epsilon)
            new = q+dt/6*(k1+2*k2+2*k3+k4)
            stage = np.array([q, stage2, stage3, stage4, new])
            if not np.all(np.isfinite(stage)):raise ArithmeticError('nonfinite RK stage')
            steps += 1
            time = float(target) if j+1 == count else start+(j+1)*dt
            history.append([steps, time, dt/h, h*new.sum(), float(stage.min()),
                            float(stage.max()), float(np.max(abs(weights-LINEAR))),
                            float(max(abs(h*k.sum()) for k in [k1, k2, k3, k4])),
                            float(abs(h*(new-q).sum()))])
            q = new
        snapshots.append(q.copy())
    if time != final_time:raise ValueError('Snapshot targets must finish at final_time')
    return dict(q=q, q_history=np.array(snapshots), history=np.array(history),
                steps=steps, time=time, clip_count=0, retries=0)
