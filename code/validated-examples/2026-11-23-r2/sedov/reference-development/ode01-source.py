"""Independent similarity-ODE reference for the uniform spherical Sedov blast.

Dimensionless fields are rho=rho0*G(xi), u=D*V(xi), p=rho0*D**2*P(xi),
xi=r/R(t), D=(2/5)*R/t. Integrate the continuous Euler similarity ODE
inward from the strong-shock jumps. No numerical FV solver is imported.
The tiny central core uses its leading regular asymptote, explicitly exposed
as cutoff/rtol options for sensitivity checks. Cell means use split quadrature,
and must not be described as closed-form exact cell averages.
"""
from functools import lru_cache
import numpy as np
from scipy.integrate import quad, solve_ivp

GAMMA = 5.0 / 3.0
ALPHA = 2.0 / 5.0
RHO0 = 1.0
ENERGY = 1.0
DEFAULT_CUTOFF = 1.e-3
DEFAULT_RTOL = 2.e-10


@lru_cache(maxsize=8)
def build_reference(cutoff=DEFAULT_CUTOFF, rtol=DEFAULT_RTOL):
    if not 0 < cutoff < .1 or not 0 < rtol < 1.e-5:
        raise ValueError('Unsupported reference resolution')

    def rhs(xi, state):
        logg, velocity, logp = state
        a = velocity - xi
        pg = np.exp(logp - logg)
        # Momentum and adiabatic-pressure equations determine V' and log(P)'.
        matrix = np.array([[a, pg], [GAMMA, a]])
        forcing = np.array([1.5 * velocity, 3. - 2. * GAMMA * velocity / xi])
        dv, dh = np.linalg.solve(matrix, forcing)
        dg = (-dv - 2. * velocity / xi) / a
        return [dg, dv, dh]

    solution = solve_ivp(rhs, (1., cutoff), [np.log(4.), .75, np.log(.75)],
                         method='DOP853', rtol=rtol, atol=rtol * .01,
                         dense_output=True)
    if not solution.success:
        raise ArithmeticError('Similarity ODE failed: ' + solution.message)
    lg, vc, lp = solution.sol(cutoff)
    gc, pc = float(np.exp(lg)), float(np.exp(lp))
    if not gc > 0 or not pc > 0 or not vc > 0:
        raise ArithmeticError('Invalid regular-center continuation')
    exponent = 3. / (GAMMA - 1.)

    def fields(xi):
        x = np.asarray(xi, dtype=float)
        regular = np.maximum(x, cutoff)
        states = solution.sol(regular.ravel())
        g = np.exp(states[0]).reshape(x.shape)
        v = states[1].reshape(x.shape)
        p = np.exp(states[2]).reshape(x.shape)
        core = x < cutoff
        g = np.where(core, gc * (x / cutoff) ** exponent, g)
        v = np.where(core, vc * x / cutoff, v)
        p = np.where(core, pc, p)
        return g, v, p

    def integrand(x):
        g, v, p = fields(x)
        return float((p / (GAMMA - 1.) + .5 * g * v*v) * x*x)

    core_energy = pc * cutoff**3 / (3. * (GAMMA - 1.))
    core_energy += .5 * gc * vc*vc * cutoff**3 / (exponent + 5.)
    integral, err = quad(integrand, cutoff, 1., epsabs=1.e-11, epsrel=1.e-11)
    integral += core_energy
    mass, mass_err = quad(lambda x: float(fields(x)[0] * x*x), cutoff, 1.,
                          epsabs=1.e-11, epsrel=1.e-11)
    mass += gc * cutoff**3 / (exponent + 3.)
    beta = (1. / (4. * np.pi * ALPHA**2 * integral)) ** .2
    info = {'gamma': GAMMA, 'geometry': 3, 'rho0': RHO0, 'energy': ENERGY,
            'alpha': ALPHA, 'beta': float(beta), 'core_cutoff_xi': cutoff,
            'ode_rtol': rtol, 'ode_nfev': solution.nfev,
            'energy_integral': float(integral), 'energy_quad_error_estimate': err,
            'swept_mass_dimensionless': float(mass), 'mass_quad_error_estimate': mass_err,
            'core_model': 'G proportional to xi^(9/2), V proportional to xi, P constant',
            'reference_kind': 'semi-analytic similarity ODE plus split Gauss cell quadrature'}
    return fields, info


def normalization(cutoff=DEFAULT_CUTOFF, rtol=DEFAULT_RTOL):
    return dict(build_reference(cutoff, rtol)[1])


def shock_radius(t, cutoff=DEFAULT_CUTOFF, rtol=DEFAULT_RTOL):
    if not np.isfinite(t) or t <= 0:
        raise ValueError('Point-blast similarity solution requires finite t>0')
    return normalization(cutoff, rtol)['beta'] * t**ALPHA


def point_state(radius, t, cutoff=DEFAULT_CUTOFF, rtol=DEFAULT_RTOL):
    r = np.asarray(radius, dtype=float)
    if np.any(~np.isfinite(r)) or np.any(r < 0):
        raise ValueError('Radii must be finite and nonnegative')
    fields, info = build_reference(cutoff, rtol)
    shock = shock_radius(t, cutoff, rtol)
    speed = ALPHA * shock / t
    xi = r / shock
    g, v, p = fields(np.minimum(xi, 1.))
    inside = xi <= 1.
    return (np.where(inside, RHO0*g, RHO0),
            np.where(inside, speed*v, 0.),
            np.where(inside, RHO0*speed**2*p, 0.))


def cell_means(edges, t, order=24, cutoff=DEFAULT_CUTOFF, rtol=DEFAULT_RTOL):
    edges = np.asarray(edges, dtype=float)
    if edges.ndim != 1 or len(edges) < 2 or edges[0] < 0 or np.any(np.diff(edges) <= 0):
        raise ValueError('Strictly increasing nonnegative radial edges required')
    if order < 4:
        raise ValueError('Quadrature order must be at least 4')
    left, right = edges[:-1], edges[1:]
    shock = shock_radius(t, cutoff, rtol)
    hot_right = np.maximum(left, np.minimum(right, shock))
    nodes, weights = np.polynomial.legendre.leggauss(order)
    radius = (left[:, None] + hot_right[:, None]) / 2.
    radius = radius + (hot_right - left)[:, None] / 2. * nodes
    rho, velocity, pressure = point_state(radius, t, cutoff, rtol)
    energy = pressure / (GAMMA - 1.) + .5*rho*velocity**2
    weight = weights * radius**2 * (hot_right - left)[:, None] / 2.
    conserved = np.stack((rho, rho*velocity, energy), axis=-1)
    integrated = np.sum(weight[..., None]*conserved, axis=1)
    cold_volume = (right**3 - np.maximum(left, np.minimum(right, shock))**3) / 3.
    integrated[:, 0] += RHO0 * cold_volume
    volumes = (right**3 - left**3) / 3.
    return integrated / volumes[:, None], np.sum(weight*pressure, axis=1) / volumes
