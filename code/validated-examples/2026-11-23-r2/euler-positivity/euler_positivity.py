"""P1 conservative FV reconstruction, mean-preserving scaling and SSPRK(3,3).

Global Lax--Friedrichs splitting uses one fixed speed a. The endpoint
quadrature weights are 1/2, so dt*a/dx <= 1/2 is the sufficient FE mean
positivity restriction. Every actually used endpoint must also obey
|u|+c <= a. These are checked, never achieved by a hidden retry or clipping.
"""
import numpy as np

GAMMA = 1.4


class StageFailure(ArithmeticError):
    def __init__(self, message, q, context=None):
        super().__init__(message)
        self.failed_state = np.array(q, copy=True)
        self.failed_context = context or {}
        self.completed_history = []


def pressure(q, gamma=GAMMA):
    q = np.asarray(q, dtype=float)
    return (gamma-1)*(q[..., 2]-.5*q[..., 1]**2/q[..., 0])


def conserved(rho, velocity, p, gamma=GAMMA):
    rho, velocity, p = np.broadcast_arrays(rho, velocity, p)
    return np.stack((rho, rho*velocity, p/(gamma-1)+.5*rho*velocity**2), axis=-1)


def admissible(q, label='Euler state', epsilon=0.):
    q = np.asarray(q, dtype=float)
    if q.shape[-1] != 3 or not np.all(np.isfinite(q)) or np.any(q[..., 0] <= epsilon):
        raise StageFailure(label+' has nonfinite/nonpositive density', q)
    p = pressure(q)
    if not np.all(np.isfinite(p)) or np.any(p <= epsilon):
        raise StageFailure(label+' has nonfinite/nonpositive pressure', q)
    return q


def physical_flux(q):
    q = admissible(q)
    p = pressure(q)
    velocity = q[..., 1]/q[..., 0]
    return np.stack((q[..., 1], q[..., 1]*velocity+p,
                     velocity*(q[..., 2]+p)), axis=-1)


def spectral_radius(q):
    q = admissible(q)
    return abs(q[..., 1]/q[..., 0])+np.sqrt(GAMMA*pressure(q)/q[..., 0])


def global_lf(left, right, alpha):
    if not np.isfinite(alpha) or alpha <= 0:
        raise ValueError('Require a finite positive fixed LF splitting speed')
    left, right = admissible(left), admissible(right)
    if np.max(spectral_radius(left)) > alpha or np.max(spectral_radius(right)) > alpha:
        raise StageFailure('Fixed LF speed does not bound an actual face spectrum',
                           np.stack((left, right)))
    return .5*(physical_flux(left)+physical_flux(right)-alpha*(right-left))


def raw_endpoints(q, left, right):
    """Unlimited central conservative linear reconstruction, not TVD."""
    q = admissible(q)
    extended = np.concatenate((np.asarray(left)[None], q, np.asarray(right)[None]))
    half_slope = .25*(extended[2:]-extended[:-2])
    return np.stack((q-half_slope, q+half_slope), axis=1)


def raw_diagnostics(raw):
    """Pressure is undefined at nonpositive density; record that separately."""
    positive = raw[..., 0] > 0
    # Each raw endpoint pair averages to a positive-density mean, so at least
    # one endpoint has positive density. No invalid division is evaluated.
    minimum = float(pressure(raw[positive]).min()) if np.any(positive) else None
    return {'raw_endpoint_min_density': float(raw[..., 0].min()),
            'raw_endpoint_min_pressure': minimum,
            'raw_endpoint_nonpositive_density_count': int(np.count_nonzero(~positive))}


def scale_endpoints(q, endpoints, epsilon=1e-13):
    """One common affine theta per cell; means never changed or repaired.

    Density is bounded analytically, then pressure by concavity/bisection.
    The epsilon is a reconstruction admissibility target, not added mass or
    energy. A mean below this target causes a failure.
    """
    q = admissible(q, 'reconstruction mean')
    endpoints = np.asarray(endpoints, dtype=float)
    if endpoints.shape != q.shape[:-1]+(2, 3) or not np.all(np.isfinite(endpoints)):
        raise ValueError('Require two finite Euler endpoints per mean')
    if not np.isfinite(epsilon) or epsilon <= 0:
        raise ValueError('Require finite positive reconstruction epsilon')
    if np.any(q[:, 0] < epsilon) or np.any(pressure(q) < epsilon):
        raise StageFailure('A mean is below the reconstruction target', q)
    delta = endpoints-q[:, None]
    theta = np.ones(len(q))
    minimum = endpoints[..., 0].min(axis=1)
    active = minimum < epsilon
    theta[active] = (q[active, 0]-epsilon)/(q[active, 0]-minimum[active])
    theta[active] *= 1-64*np.finfo(float).eps
    candidate = q[:, None]+theta[:, None, None]*delta
    active_p = np.any(pressure(candidate) < epsilon, axis=1)
    if np.any(active_p):
        lo, hi = np.zeros(np.count_nonzero(active_p)), theta[active_p].copy()
        for _ in range(60):
            mid = .5*(lo+hi)
            trial = q[active_p, None]+mid[:, None, None]*delta[active_p]
            safe = np.all(pressure(trial) >= epsilon, axis=1)
            lo = np.where(safe, mid, lo)
            hi = np.where(safe, hi, mid)
        theta[active_p] = lo*(1-64*np.finfo(float).eps)
    limited = q[:, None]+theta[:, None, None]*delta
    admissible(limited, 'scaled endpoints')
    return limited, theta


def forward_euler(q, left, right, dx, dt, alpha=4., epsilon=1e-13):
    if not all(np.isfinite(v) and v > 0 for v in (dx, dt, alpha)):
        raise ValueError('Require finite positive dx, dt and alpha')
    courant = dt*alpha/dx
    if courant > .5:
        raise ValueError('Endpoint sufficient positivity CFL <= 1/2 exceeded')
    raw = raw_endpoints(q, left, right)
    endpoints, theta = scale_endpoints(q, raw, epsilon)
    lstate = np.concatenate((np.asarray(left)[None], endpoints[:, 1]))
    rstate = np.concatenate((endpoints[:, 0], np.asarray(right)[None]))
    flux = global_lf(lstate, rstate, alpha)
    updated = q-dt/dx*np.diff(flux, axis=0)
    admissible(updated, 'forward Euler mean')
    fe_balance = dx*(updated-q).sum(axis=0)-dt*(flux[0]-flux[-1])
    stats = {**raw_diagnostics(raw), 'endpoint_min_density': float(endpoints[..., 0].min()),
             'endpoint_min_pressure': float(pressure(endpoints).min()),
             'fe_mean_min_density': float(updated[:, 0].min()),
             'fe_mean_min_pressure': float(pressure(updated).min()),
             'minimum_theta': float(theta.min()),
             'scaled_cells': int(np.count_nonzero(theta < 1)),
             'maximum_face_spectral_radius': float(max(spectral_radius(lstate).max(),
                                                        spectral_radius(rstate).max())),
             'courant': float(courant),
             'maximum_mean_preservation_defect': float(abs(endpoints.mean(axis=1)-q).max()),
             'maximum_fe_boundary_balance_defect': float(abs(fe_balance).max())}
    return updated, dt*(flux[0]-flux[-1]), stats


def solve(n, final_time=.15, alpha=4., cfl=.4, epsilon=1e-13,
          max_steps=2000, history_stride=8):
    if not isinstance(n, int) or n < 8 or n % 2:
        raise ValueError('Require an even integer n>=8 aligned with x0=.5')
    if not np.isfinite(final_time) or final_time <= 0 or not 0 < cfl <= .5:
        raise ValueError('Require positive final time and CFL <= .5')
    edges = np.linspace(0., 1., n+1)
    dx = 1./n
    left, right = conserved(1., -2., .4), conserved(1., 2., .4)
    q = np.repeat(left[None], n, axis=0)
    q[n//2:] = right
    initial = q.copy()
    time, steps = 0., 0
    boundary = np.zeros(3)
    stages, history, snapshots = [], [{'time': 0., 'step': 0}], [q.copy()]
    try:
        while time < final_time:
            if steps >= max_steps:
                raise StageFailure('Fixed step budget exhausted', q)
            dt = min(cfl*dx/alpha, final_time-time)
            old = q.copy()
            first, b0, s0 = forward_euler(old, left, right, dx, dt, alpha, epsilon)
            second_fe, b1, s1 = forward_euler(first, left, right, dx, dt, alpha, epsilon)
            second = .75*old+.25*second_fe
            admissible(second, 'second SSP convex mean')
            third_fe, b2, s2 = forward_euler(second, left, right, dx, dt, alpha, epsilon)
            q = old/3+(2./3)*third_fe
            admissible(q, 'third SSP convex mean')
            combo_budgets = (b0, .25*(b0+b1), b0/6+b1/6+2*b2/3)
            for stage, (s, combined, fraction, combo_budget) in enumerate(zip(
                    (s0, s1, s2), (first, second, q), (0., 1., .5), combo_budgets), start=1):
                s.update(step=steps+1, stage=stage, stage_input_time=time+fraction*dt,
                         dt=dt, rk_mean_min_density=float(combined[:, 0].min()),
                         rk_mean_min_pressure=float(pressure(combined).min()),
                         maximum_rk_boundary_balance_defect=float(
                             abs(dx*(combined-old).sum(axis=0)-combo_budget).max()))
                stages.append(s)
            boundary += b0/6+b1/6+2*b2/3
            time = final_time if dt == final_time-time else time+dt
            steps += 1
            if steps % history_stride == 0 or time == final_time:
                history.append({'time': time, 'step': steps})
                snapshots.append(q.copy())
    except StageFailure as error:
        error.completed_history = stages
        raise
    return {'q': q, 'initial': initial, 'edges': edges, 'time': time, 'steps': steps,
            'initial_integral': dx*initial.sum(axis=0),
            'final_integral': dx*q.sum(axis=0), 'boundary_net_integral': boundary,
            'stage_history': stages, 'history': history, 'snapshots': np.array(snapshots),
            'state_floor_count': 0, 'rejected_steps': 0, 'retries': 0}
