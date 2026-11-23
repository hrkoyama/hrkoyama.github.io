"""Closed symmetric non-vacuum Euler double-rarefaction reference.

The Riemann invariants determine the middle pressure explicitly. This is a
separate evaluator, not the LF numerical interface flux. Only equal positive
outer density/pressure and opposite separating velocities are supported.
See citations.json / README.md for the derivation and limited source review.
"""
from functools import lru_cache

import numpy as np


def star_state(gamma=1.4, rho0=1., p0=.4, speed=2.):
    """Return the strictly positive symmetric central state and wave speeds."""
    if (not all(np.isfinite(v) for v in (gamma, rho0, p0, speed))
            or gamma <= 1 or min(rho0, p0) <= 0 or speed < 0):
        raise ValueError('Require gamma>1, rho0,p0>0 and separating speed>=0')
    c0 = float(np.sqrt(gamma*p0/rho0))
    ratio = 1-(gamma-1)*speed/(2*c0)
    if ratio <= 0:
        raise ValueError('Vacuum-generating data are outside this evaluator')
    cstar = c0*ratio
    return {'rho': rho0*ratio**(2/(gamma-1)), 'u': 0.,
            'p': p0*ratio**(2*gamma/(gamma-1)), 'c': cstar,
            'c0': c0, 'head_speed': speed+c0,
            'tail_speed': cstar, 'vacuum': False}


def speeds(gamma=1.4, rho0=1., p0=.4, speed=2.):
    s = star_state(gamma, rho0, p0, speed)
    return np.array([-s['head_speed'], -s['tail_speed'],
                     s['tail_speed'], s['head_speed']])


def primitive(x, t, origin=.5, gamma=1.4, rho0=1., p0=.4, speed=2.):
    """Evaluate rho,u,p at physical coordinates x and nonnegative time t."""
    s = star_state(gamma, rho0, p0, speed)
    x = np.asarray(x, dtype=float)
    if (not np.all(np.isfinite(x)) or not np.isfinite(t) or t < 0
            or not np.isfinite(origin)):
        raise ValueError('Require finite coordinates/origin and time>=0')
    if t == 0:
        return np.stack((np.full_like(x, rho0),
                         np.where(x < origin, -speed, speed),
                         np.full_like(x, p0)), axis=-1)
    xi = (x-origin)/t
    z = np.abs(xi)
    # In either fan, c is affine in |xi|. The formula is evaluated only
    # within its positive fan interval; no clipping of a physical state.
    fan = (z > s['tail_speed']) & (z < s['head_speed'])
    cf = (2*s['c0']-(gamma-1)*speed+(gamma-1)*z)/(gamma+1)
    ratio = np.where(fan, cf/s['c0'], 1.)
    rho = np.where(z <= s['tail_speed'], s['rho'], rho0)
    p = np.where(z <= s['tail_speed'], s['p'], p0)
    u = np.where(z <= s['tail_speed'], 0., np.sign(xi)*speed)
    rho = np.where(fan, rho0*ratio**(2/(gamma-1)), rho)
    p = np.where(fan, p0*ratio**(2*gamma/(gamma-1)), p)
    uf = 2/(gamma+1)*(z+speed*(gamma-1)/2-s['c0'])
    u = np.where(fan, np.sign(xi)*uf, u)
    return np.stack((rho, u, p), axis=-1)


def conserved(x, t, origin=.5, gamma=1.4, rho0=1., p0=.4, speed=2.):
    w = primitive(x, t, origin, gamma, rho0, p0, speed)
    rho, u, p = w[..., 0], w[..., 1], w[..., 2]
    return np.stack((rho, rho*u, p/(gamma-1)+.5*rho*u*u), axis=-1)


@lru_cache(maxsize=6)
def _gauss(order):
    return np.polynomial.legendre.leggauss(order)


def cell_averages(edges, t, origin=.5, order=8, gamma=1.4,
                  rho0=1., p0=.4, speed=2.):
    """Integrate conserved variables, splitting at all four fan boundaries.

    Pressure of the conserved mean is distinct from the mean pressure.
    At gamma=1.4 each fan's conserved field has degree at most seven in x;
    split Gauss8 is therefore exact in real arithmetic, with float64 error.
    """
    edges = np.asarray(edges, dtype=float)
    if (edges.ndim != 1 or edges.size < 2 or not np.all(np.isfinite(edges))
            or np.any(np.diff(edges) <= 0) or not isinstance(order, int) or order < 1):
        raise ValueError('Require finite increasing 1D edges and integer order>=1')
    if not np.isfinite(t) or t < 0:
        raise ValueError('Require finite time>=0')
    cuts = origin+t*speeds(gamma, rho0, p0, speed) if t else np.array([origin])
    nodes, weights = _gauss(order)
    out = np.zeros((len(edges)-1, 3))
    # At most five smooth pieces per cell. Repeated zero-strength boundaries
    # are discarded. Every interval contribution integrates conserved q.
    for i, (left, right) in enumerate(zip(edges[:-1], edges[1:])):
        breaks = np.unique(np.r_[left, cuts[(cuts > left) & (cuts < right)], right])
        for a, b in zip(breaks[:-1], breaks[1:]):
            points = .5*(a+b)+.5*(b-a)*nodes
            out[i] += .5*(b-a)*np.einsum(
                'i,ij->j', weights,
                conserved(points, t, origin, gamma, rho0, p0, speed))
        out[i] /= right-left
    return out
