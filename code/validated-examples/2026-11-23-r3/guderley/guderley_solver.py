"""Spherical Euler finite volumes: HLL fluxes and physical-time Heun steps.

There is no similarity solution in this module. Initial conserved cell means
and the time-dependent outer boundary state are supplied by the caller.
"""
import numpy as np

GAMMA = 1.4
# Absolute nondimensional internal ENERGY DENSITY, with the fixed rho0=1
# and shock-radius/time normalization documented by inputs.json. This only
# classifies floating-point cancellation; no conserved state is changed.
INTERNAL_ENERGY_ABSOLUTE_TOLERANCE = 64 * np.finfo(float).eps


class InvalidStage(ValueError):
    """A raw failed stage, its context and completed history are retained."""


def geometry(n, radius):
    if int(n) != n or n < 8 or not np.isfinite(radius) or radius <= 0:
        raise ValueError('Invalid spherical mesh')
    edges = np.linspace(0., float(radius), int(n) + 1)
    return edges, 4*np.pi*edges**2, 4*np.pi*np.diff(edges**3)/3


def conserved(rho, velocity, pressure):
    rho, velocity, pressure = np.broadcast_arrays(rho, velocity, pressure)
    if (not np.all(np.isfinite(rho + velocity + pressure))
            or np.any(rho <= 0) or np.any(pressure < 0)):
        raise ValueError('Invalid primitive state')
    return np.column_stack([rho.ravel(), (rho*velocity).ravel(),
                            (pressure/(GAMMA-1) + .5*rho*velocity**2).ravel()])


def primitive(q):
    q = np.asarray(q)
    if q.ndim != 2 or q.shape[1] != 3 or not np.all(np.isfinite(q)):
        raise ValueError('Expected finite N by 3 conserved states')
    if np.any(q[:, 0] <= 0):
        raise ValueError('Nonpositive density')
    rho = q[:, 0]
    velocity = q[:, 1]/rho
    internal = q[:, 2] - .5*q[:, 1]*velocity
    if np.any(internal < -INTERNAL_ENERGY_ABSOLUTE_TOLERANCE):
        raise ValueError('Negative internal energy beyond fixed absolute roundoff tolerance')
    return rho, velocity, (GAMMA-1)*internal, internal


def sound_speed(rho, pressure, guard=None):
    # Only the square-root diagnostic treats the permitted cancellation band
    # as zero. Neither pressure nor a conserved component is repaired.
    if np.any(pressure < -(GAMMA-1)*INTERNAL_ENERGY_ABSOLUTE_TOLERANCE):
        raise ValueError('Sound speed received pressure outside cancellation band')
    negative = pressure < 0
    if guard is not None and np.any(negative):
        guard['evaluations'] += int(np.count_nonzero(negative))
        guard['minimum_pressure'] = min(guard['minimum_pressure'], float(pressure[negative].min()))
    return np.sqrt(np.maximum(GAMMA*pressure/rho, 0.))


def physical_flux(q):
    rho, velocity, pressure, _ = primitive(q)
    return np.column_stack([q[:, 1], q[:, 1]*velocity + pressure,
                            (q[:, 2] + pressure)*velocity])


def hll(left, right, guard=None):
    if left.shape != right.shape:
        raise ValueError('Incompatible face states')
    rl, ul, pl, _ = primitive(left)
    rr, ur, pr, _ = primitive(right)
    cl, cr = sound_speed(rl, pl, guard), sound_speed(rr, pr, guard)
    sl = np.minimum(np.minimum(ul-cl, ur-cr), 0.)
    sr = np.maximum(np.maximum(ul+cl, ur+cr), 0.)
    fl, fr = physical_flux(left), physical_flux(right)
    flux = np.empty_like(fl)
    positive, negative = sl >= 0, sr <= 0
    middle = ~(positive | negative)
    # Both speeds vanish in the exactly cold stationary upstream. The
    # physical flux is exactly zero and no 0/0 is ever evaluated.
    flux[positive] = fl[positive]
    flux[negative & ~positive] = fr[negative & ~positive]
    if np.any(middle):
        a, b = sl[middle, None], sr[middle, None]
        flux[middle] = (b*fl[middle] - a*fr[middle]
                        + a*b*(right[middle]-left[middle]))/(b-a)
    return flux


def rhs(q, time, areas, volumes, outer_state, guard=None):
    _, _, pressure, _ = primitive(q)
    boundary_q = np.asarray(outer_state(time), dtype=float)
    if boundary_q.shape != (3,):
        raise ValueError('Outer boundary must return one conserved state')
    primitive(boundary_q[None, :])
    left = np.vstack([q[0]*[1., -1., 1.], q])
    right = np.vstack([q, boundary_q])
    flux = hll(left, right, guard)
    derivative = -(areas[1:, None]*flux[1:]
                   - areas[:-1, None]*flux[:-1])/volumes[:, None]
    source = np.zeros_like(q)
    source[:, 1] = pressure*np.diff(areas)/volumes
    derivative += source
    boundary = areas[0]*flux[0] - areas[-1]*flux[-1]
    return derivative, boundary, np.sum(source*volumes[:, None], axis=0)


def cfl_step(speed, width, cfl, remaining):
    inverse_step = float(np.max(speed/width))
    if not np.isfinite(inverse_step) or inverse_step < 0:
        raise ValueError('Invalid inverse CFL step')
    if inverse_step <= cfl/remaining:
        return remaining
    return cfl/inverse_step


def solve(initial, edges, initial_time, final_time, cfl, outer_state,
          max_steps=10000, history_stride=10):
    if not (initial_time < final_time < 0 and 0 < cfl <= .4):
        raise ValueError('Use a strictly pre-collapse interval and CFL <= 0.4')
    if max_steps < 1 or history_stride < 1:
        raise ValueError('Invalid step/history budget')
    edges = np.asarray(edges, dtype=float)
    if (edges.ndim != 1 or edges[0] != 0 or np.any(np.diff(edges) <= 0)
            or not np.all(np.isfinite(edges))):
        raise ValueError('Invalid radial edges')
    q = np.asarray(initial, dtype=float).copy()
    if q.shape != (len(edges)-1, 3):
        raise ValueError('Initial means do not match the mesh')
    areas, volumes = 4*np.pi*edges**2, 4*np.pi*np.diff(edges**3)/3
    integral = lambda state: np.sum(state*volumes[:, None], axis=0)
    initial_integral = integral(q)
    boundary_integral, source_integral = np.zeros(3), np.zeros(3)
    time, steps, history, snapshots = float(initial_time), 0, [], []
    minimum_density, minimum_pressure, minimum_internal = np.inf, np.inf, np.inf
    minimum_dt, maximum_dt = np.inf, 0.
    sound_guard = {'evaluations': 0, 'minimum_pressure': 0.}

    def checked(state, label):
        nonlocal minimum_density, minimum_pressure, minimum_internal
        try:
            rho, _, pressure, internal = primitive(state)
        except ValueError as original:
            error = InvalidStage(str(original))
            error.failed_state = state.copy()
            error.failed_context = {'stage': label, 'step': steps, 'time': time}
            error.completed_history = list(history)
            raise error from original
        minimum_density = min(minimum_density, float(rho.min()))
        minimum_pressure = min(minimum_pressure, float(pressure.min()))
        minimum_internal = min(minimum_internal, float(internal.min()))

    def record(dt):
        rho, velocity, pressure, _ = primitive(q)
        history.append({'step': steps, 'time': time, 'dt': dt,
                        'minimum_density': float(rho.min()),
                        'minimum_pressure': float(pressure.min()),
                        'maximum_speed': float(abs(velocity).max()),
                        'integral': integral(q).tolist()})
        snapshots.append(q.copy())

    checked(q, 'initial')
    record(0.)
    while time < final_time:
        if steps >= max_steps:
            error = InvalidStage('Fixed step budget exhausted; no hidden retry')
            error.failed_state = q.copy()
            error.failed_context = {'stage': 'step-budget', 'step': steps, 'time': time}
            error.completed_history = list(history)
            raise error
        rho, velocity, pressure, _ = primitive(q)
        speed = abs(velocity) + sound_speed(rho, pressure, sound_guard)
        remaining = final_time - time
        dt = cfl_step(speed, volumes/(areas[:-1]+areas[1:]), cfl, remaining)
        if not np.isfinite(dt) or dt <= 0:
            raise ValueError('Invalid time step')
        stage_time = final_time if dt == remaining else time + dt
        k0, b0, s0 = rhs(q, time, areas, volumes, outer_state, guard=sound_guard)
        predictor = q + dt*k0
        checked(predictor, 'predictor')
        k1, b1, s1 = rhs(predictor, stage_time, areas, volumes, outer_state, guard=sound_guard)
        candidate = .5*q + .5*(predictor + dt*k1)
        checked(candidate, 'update')
        q = candidate
        boundary_integral += .5*dt*(b0+b1)
        source_integral += .5*dt*(s0+s1)
        time = stage_time
        steps += 1
        minimum_dt, maximum_dt = min(minimum_dt, dt), max(maximum_dt, dt)
        if steps % history_stride == 0 or time == final_time:
            record(dt)
    return {'q': q, 'edges': edges, 'volumes': volumes, 'time': time,
            'steps': steps, 'initial_integral': initial_integral,
            'final_integral': integral(q), 'boundary_net_integral': boundary_integral,
            'geometric_source_integral': source_integral, 'history': history,
            'snapshots': np.array(snapshots),
            'minimum_density_all_stages': minimum_density,
            'minimum_pressure_all_stages': minimum_pressure,
            'minimum_internal_energy_all_stages': minimum_internal,
            'sound_speed_roundoff_guard_evaluations': sound_guard['evaluations'],
            'minimum_pressure_at_sound_speed_guard': sound_guard['minimum_pressure'],
            'minimum_dt': minimum_dt, 'maximum_dt': maximum_dt,
            'state_floor_count': 0, 'rejected_steps': 0}
