"""Original unsplit 2D Cartesian Euler FV code. No radial source or floors.

The only analytic input during evolution is the prescribed supersonic outer
inflow. Both momenta evolve on the complete square; no symmetry projection,
radial reduction, analytic interior replacement, or timestep retry is used.
"""
import math
import time as clock
import numpy as np

GAMMA = 5.0 / 3.0


def primitive(q):
    q = np.asarray(q, dtype=float)
    rho = q[..., 0]
    if q.shape[-1] != 4 or not np.isfinite(q).all() or np.any(rho <= 0):
        raise FloatingPointError('Require finite conserved states and positive density')
    ux, uy = q[..., 1]/rho, q[..., 2]/rho
    internal = q[..., 3] - .5*(q[..., 1]*ux + q[..., 2]*uy)
    scale = np.maximum(abs(q[..., 3]), np.finfo(float).tiny)
    if np.any(internal < -64*np.finfo(float).eps*scale):
        raise FloatingPointError('Negative internal energy beyond roundoff')
    pressure = (GAMMA-1)*internal
    # q, energy and pressure remain unchanged; only a square-root argument.
    sound = np.sqrt(np.maximum(GAMMA*pressure/rho, 0))
    return rho, ux, uy, pressure, sound


def flux(q, axis):
    if axis not in (0, 1):
        raise ValueError('Flux axis must be x=0 or y=1')
    rho, ux, uy, pressure, sound = primitive(q)
    u = ux if axis == 0 else uy
    f = q*u[..., None]
    f[..., 1+axis] += pressure
    f[..., 3] += pressure*u
    return f, abs(u)+sound


def rusanov(left, right, axis):
    fl, al = flux(left, axis)
    fr, ar = flux(right, axis)
    speed = np.maximum(al, ar)
    return .5*(fl+fr)-.5*speed[..., None]*(right-left), speed


def cold_state(x, y, time):
    radius = np.hypot(x, y)
    if np.any(radius == 0):
        raise ValueError('Do not sample the singular initial velocity at r=0')
    rho = 1+time/radius
    return np.stack((rho, -rho*x/radius, -rho*y/radius, .5*rho), axis=-1)


def cold_x_face_flux(x, y_edges, time):
    """Exact spatial mean of the prescribed cold flux at constant x != 0.

    Integrate rho=1+t/r, ux=-x/r, uy=-y/r. The flux is affine in
    time, so Heun also integrates its temporal contribution exactly.
    This routine does not evaluate an interior shock solution.
    """
    if not math.isfinite(x) or x == 0:
        raise ValueError('The outer face requires nonzero finite x')
    y = np.asarray(y_edges, dtype=float)
    a = abs(x)
    radius = np.hypot(x, y)
    mass = -x*np.arcsinh(y/a)-time*np.sign(x)*np.arctan(y/a)
    normal = a*np.arctan(y/a)+time*y/radius
    transverse = .5*x*np.log(x*x+y*y)-time*x/radius
    integral = np.stack((mass, normal, transverse, .5*mass), axis=-1)
    return np.diff(integral, axis=0)/np.diff(y)[:, None]


def operator(q, time, edges):
    """Shared x/y face fluxes in an unsplit Cartesian divergence."""
    n = len(edges)-1
    if q.shape != (n, n, 4):
        raise ValueError('Expected square Cartesian means with four components')
    dx = edges[1]-edges[0]
    if not np.allclose(np.diff(edges), dx, rtol=1e-13, atol=0):
        raise ValueError('Uniform Cartesian mesh required')
    centers = .5*(edges[:-1]+edges[1:])
    low, high = edges[0], edges[-1]
    xl = cold_state(np.full(n, low), centers, time)
    xr = cold_state(np.full(n, high), centers, time)
    yb = cold_state(centers, np.full(n, low), time)
    yt = cold_state(centers, np.full(n, high), time)
    fx, ax = rusanov(np.concatenate((xl[:, None], q), axis=1),
                     np.concatenate((q, xr[:, None]), axis=1), 0)
    fy, ay = rusanov(np.concatenate((yb[None], q), axis=0),
                     np.concatenate((q, yt[None]), axis=0), 1)
    fx[:, 0] = cold_x_face_flux(low, edges, time)
    fx[:, -1] = cold_x_face_flux(high, edges, time)
    fy[0] = cold_x_face_flux(low, edges, time)[:, [0, 2, 1, 3]]
    fy[-1] = cold_x_face_flux(high, edges, time)[:, [0, 2, 1, 3]]
    rhs = -(np.diff(fx, axis=1)+np.diff(fy, axis=0))/dx
    net = dx*(np.sum(fx[:, 0]-fx[:, -1], axis=0)+np.sum(fy[0]-fy[-1], axis=0))
    rate = (float(np.max(ax))+float(np.max(ay)))/dx
    return rhs, net, rate


def solve(n, radius=.5, final_time=.6, cfl=.35, maximum_seconds=45):
    if isinstance(n, bool) or int(n) != n or n < 8 or n % 2 or n > 256:
        raise ValueError('Require even integer n in [8,256]; fixed tests use at most128')
    if not all(math.isfinite(x) for x in [radius, final_time, cfl, maximum_seconds]):
        raise ValueError('Finite parameters required')
    if radius <= 0 or final_time <= 0 or final_time/3 >= radius or not 0 < cfl <= .4 or maximum_seconds <= 0:
        raise ValueError('Require positive domain/time, internal shock, CFL<=.4 and positive budget')
    edges = np.linspace(-radius, radius, n+1)
    centers = .5*(edges[:-1]+edges[1:])
    x, y = np.meshgrid(centers, centers)
    q = cold_state(x, y, 0)
    area = (2*radius/n)**2
    initial = np.sum(q, axis=(0, 1))*area
    boundary = np.zeros(4)
    time, steps = 0., 0
    started = clock.monotonic()
    history = []
    minimum_density, minimum_pressure = 1., 0.
    minimum_internal_roundoff_units = 0.
    def checked(state, stage):
        nonlocal minimum_density, minimum_pressure, minimum_internal_roundoff_units
        try:
            rho, ux, uy, p, _ = primitive(state)
        except FloatingPointError as error:
            error.failed_state = state.copy()
            error.failed_context = {'time': time, 'steps': steps, 'stage': stage}
            error.completed_history = history.copy()
            raise
        minimum_density = min(minimum_density, float(rho.min()))
        minimum_pressure = min(minimum_pressure, float(p.min()))
        units = p/(GAMMA-1)/np.maximum(abs(state[..., 3]), np.finfo(float).tiny)/np.finfo(float).eps
        minimum_internal_roundoff_units = min(minimum_internal_roundoff_units, float(units.min()))
    while time < final_time:
        if steps >= 10000 or clock.monotonic()-started > maximum_seconds:
            raise RuntimeError('Fixed computation budget exceeded')
        rhs0, net0, rate = operator(q, time, edges)
        dt = min(cfl/rate, final_time-time)
        if not math.isfinite(dt) or dt <= 0:
            raise FloatingPointError('Invalid timestep')
        stage = q+dt*rhs0
        checked(stage, 'Euler predictor')
        rhs1, net1, _ = operator(stage, time+dt, edges)
        next_q = .5*(q+stage+dt*rhs1)
        checked(next_q, 'Heun update')
        boundary += .5*dt*(net0+net1)
        q = next_q
        time += dt
        steps += 1
        history.append({'time': time, 'dt': dt, 'integral': (area*np.sum(q, axis=(0, 1))).tolist(),
                        'boundary_net_integral': boundary.tolist()})
    return {'q': q, 'edges': edges, 'time': time, 'steps': steps,
            'initial_integral': initial, 'final_integral': area*np.sum(q, axis=(0, 1)),
            'boundary_net_integral': boundary, 'history': history,
            'minimum_density': minimum_density, 'minimum_pressure': minimum_pressure,
            'minimum_internal_roundoff_units': minimum_internal_roundoff_units,
            'state_floor_count': 0}
