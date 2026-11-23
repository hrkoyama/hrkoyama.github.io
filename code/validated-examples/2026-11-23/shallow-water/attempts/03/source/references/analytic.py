"""New implementations of Bernoulli and Ritter formulas in SWASHES.

No solver functions are imported. Original SWASHES source code is not copied.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss


def bump(x):
    x = np.asarray(x)
    return np.where((x > 8) & (x < 12), .2-.05*(x-10)**2, 0.)


def subcritical(x, g=9.81, discharge=4.42, downstream_depth=2.):
    z = bump(x); q = discharge; hL = downstream_depth
    energy = hL+q*q/(2*g*hL*hL)
    lo = np.full_like(z, (q*q/g)**(1/3), dtype=float)
    hi = np.full_like(z, energy, dtype=float)
    if np.any(lo+z+q*q/(2*g*lo*lo) > energy):
        raise ValueError('No subcritical Bernoulli branch')
    for _ in range(60):
        mid = .5*(lo+hi)
        positive = mid+z+q*q/(2*g*mid*mid) > energy
        hi = np.where(positive, mid, hi); lo = np.where(positive, lo, mid)
    return np.stack((.5*(lo+hi), np.full_like(z, q)), axis=-1)


def ritter(x, t, g=9.81, left_depth=1., dam_position=0.):
    x = np.asarray(x); c = np.sqrt(g*left_depth)
    if t == 0:
        return np.stack((np.where(x < dam_position, left_depth, 0.), np.zeros_like(x)), axis=-1)
    s = (x-dam_position)/t
    h = np.where(s <= -c, left_depth, np.where(s < 2*c, (2*c-s)**2/(9*g), 0.))
    u = np.where((s > -c) & (s < 2*c), 2*(s+c)/3, 0.)
    return np.stack((h, h*u), axis=-1)


def means(edges, function, breaks=(), order=8):
    """Gauss means split exactly at every branch point; q is conservative hu."""
    nodes, weights = leggauss(order)
    rows = []
    for a, b in zip(edges[:-1], edges[1:]):
        cuts = [a]+[p for p in breaks if a < p < b]+[b]
        total = None
        for l, r in zip(cuts[:-1], cuts[1:]):
            val = np.asarray(function(.5*(l+r)+.5*(r-l)*nodes))
            integral = .5*(r-l)*np.tensordot(weights, val, axes=(0, 0))
            total = integral if total is None else total+integral
        rows.append(total/(b-a))
    return np.array(rows)


def ritter_means(edges, t, g=9.81, left_depth=1., dam_position=0., order=8):
    c = np.sqrt(g*left_depth)
    breaks = [dam_position] if t == 0 else [dam_position-c*t, dam_position+2*c*t]
    return means(edges, lambda x: ritter(x, t, g, left_depth, dam_position), breaks, order)


def qualify():
    """Independent quadrature, energy and PDE identity checks at fixed probes."""
    g = 9.81; x = np.linspace(0, 25, 101); s = subcritical(x)
    energy = s[:, 0]+bump(x)+s[:, 1]**2/(2*g*s[:, 0]**2)
    edges = np.linspace(-5, 5, 101)
    r8 = ritter_means(edges, .5, order=8); r16 = ritter_means(edges, .5, order=16)
    eps = 1e-5; probes = np.array([-.7, .2, 1.5]); t=.5
    dt = (ritter(probes,t+eps)-ritter(probes,t-eps))/(2*eps)
    def physical_flux(x):
        u=ritter(x,t); return np.stack((u[:,1],u[:,1]**2/u[:,0]+.5*g*u[:,0]**2),axis=-1)
    dx = (physical_flux(probes+eps)-physical_flux(probes-eps))/(2*eps)
    return dict(checks={
        'Bernoulli energy constant': bool(np.ptp(energy) < 3e-14),
        'subcritical branch': bool(np.all(s[:,0] > (4.42**2/g)**(1/3))),
        'Gauss8 vs Gauss16 conservative means': bool(np.max(abs(r8-r16)) < 2e-14),
        'Ritter total mass': bool(abs(.1*r8[:,0].sum()-5.) < 2e-14),
        'Ritter finite difference PDE residual': bool(np.max(abs(dt+dx)) < 2e-8),
        'exact dry branch': bool(np.array_equal(ritter(np.array([4.,5.]),.5),np.zeros((2,2))))},
        maximum_quadrature_gap=float(np.max(abs(r8-r16))),
        maximum_pde_residual=float(np.max(abs(dt+dx))),
        energy_span=float(np.ptp(energy)))
