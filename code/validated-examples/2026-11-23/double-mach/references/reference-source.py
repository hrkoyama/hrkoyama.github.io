"""Independent finite-volume references for the 2D RKDG demonstration.

This module imports no RKDG code and shares no spatial operators with it.
The 1D reference uses component-wise conservative FV WENO5-JS reconstruction,
HLLC flux and SSPRK(3,3). The 2D Double Mach reference uses primitive-variable
MC/MUSCL reconstruction, HLL flux and SSPRK(2,2), without dimensional splitting.
Finite-resolution reference uncertainty is measured by separate finer grids;
these arrays are numerical references, not exact solutions.

References: Jiang & Shu (1996), doi:10.1006/jcph.1996.0130;
Shu & Osher (1989), doi:10.1016/0021-9991(89)90222-2;
Woodward & Colella (1984), doi:10.1016/0021-9991(84)90142-6.
"""
from dataclasses import dataclass
import argparse
import hashlib
import json
from pathlib import Path
import platform
import time as clock

import numpy as np

GAMMA = 1.4


def conserved(w):
    rho, u, v, pressure = np.moveaxis(np.asarray(w, dtype=float), -1, 0)
    return np.stack((rho, rho*u, rho*v,
                     pressure/(GAMMA-1) + .5*rho*(u*u+v*v)), axis=-1)


def primitive(q):
    q = np.asarray(q)
    rho = q[..., 0]
    u, v = q[..., 1]/rho, q[..., 2]/rho
    pressure = (GAMMA-1)*(q[..., 3] - .5*(q[..., 1]*u+q[..., 2]*v))
    if not np.all(np.isfinite(q)) or np.any(rho <= 0) or np.any(pressure <= 0):
        raise FloatingPointError('Independent FV reference became nonphysical')
    return np.stack((rho, u, v, pressure), axis=-1)


def flux(q, axis):
    w = primitive(q)
    velocity = w[..., 1+axis]
    f = q*velocity[..., None]
    f[..., 1+axis] += w[..., 3]
    f[..., 3] += w[..., 3]*velocity
    return f


def hll(left, right, axis=0, contact=False):
    wl, wr = primitive(left), primitive(right)
    rl, rr = wl[..., 0], wr[..., 0]
    ul, ur = wl[..., 1+axis], wr[..., 1+axis]
    pl, pr = wl[..., 3], wr[..., 3]
    al, ar = np.sqrt(GAMMA*pl/rl), np.sqrt(GAMMA*pr/rr)
    sl, sr = np.minimum(ul-al, ur-ar), np.maximum(ul+al, ur+ar)
    fl, fr = flux(left, axis), flux(right, axis)
    middle = ((sr[..., None]*fl-sl[..., None]*fr
               +(sl*sr)[..., None]*(right-left))/(sr-sl)[..., None])
    if contact:
        sm = ((pr-pl + rl*ul*(sl-ul)-rr*ur*(sr-ur))
              /(rl*(sl-ul)-rr*(sr-ur)))

        def star(q, w, speed):
            rho, vel, p = w[..., 0], w[..., 1+axis], w[..., 3]
            density = rho*(speed-vel)/(speed-sm)
            result = q*(density/rho)[..., None]
            result[..., 1+axis] = density*sm
            result[..., 3] = density*(q[..., 3]/rho
                  +(sm-vel)*(sm+p/(rho*(speed-vel))))
            return result

        fsl = fl+sl[..., None]*(star(left, wl, sl)-left)
        fsr = fr+sr[..., None]*(star(right, wr, sr)-right)
        middle = np.where((sm >= 0)[..., None], fsl, fsr)
    return np.where((sl >= 0)[..., None], fl,
                    np.where((sr <= 0)[..., None], fr, middle))


def _weno_left(q):
    a, b, c, d, e = (q[k:len(q)-4+k] for k in range(5))
    beta0 = 13/12*(a-2*b+c)**2 + .25*(a-4*b+3*c)**2
    beta1 = 13/12*(b-2*c+d)**2 + .25*(b-d)**2
    beta2 = 13/12*(c-2*d+e)**2 + .25*(3*c-4*d+e)**2
    alpha = np.stack((.1/(1e-6+beta0)**2, .6/(1e-6+beta1)**2,
                      .3/(1e-6+beta2)**2))
    polynomials = np.stack(((2*a-7*b+11*c)/6, (-b+5*c+2*d)/6,
                             (2*c+5*d-e)/6))
    return np.sum(alpha*polynomials, axis=0)/np.sum(alpha, axis=0)


def _safe_reconstruction(face, average):
    """Locally fall back to the owning average; never clip conserved states."""
    with np.errstate(divide='ignore', invalid='ignore'):
        pressure = (GAMMA-1)*(face[..., 3]
                    -.5*(face[..., 1]**2+face[..., 2]**2)/face[..., 0])
    bad = ((face[..., 0] <= 1e-12) | (pressure <= 1e-12)
           | ~np.all(np.isfinite(face), axis=-1))
    return np.where(bad[..., None], average, face), int(np.count_nonzero(bad))


def _rhs_1d(q, dx):
    g = np.pad(q, ((3, 3), (0, 0)), mode='edge')
    left = _weno_left(g)[:-1]
    right = _weno_left(g[::-1])[::-1][1:]
    left, a = _safe_reconstruction(left, g[2:-3])
    right, b = _safe_reconstruction(right, g[3:-2])
    f = hll(left, right, contact=True)
    return -(f[1:]-f[:-1])/dx, f[0]-f[-1], a+b


@dataclass
class FVResult:
    x_edges: np.ndarray
    q: np.ndarray
    time: float
    steps: int
    boundary_integral: np.ndarray
    initial_integral: np.ndarray
    diagnostics: dict
    y_edges: object = None


def initial_1d(problem, n):
    if problem == 'shu-osher':
        edges = np.linspace(-5., 5., n+1)
        center = .5*(edges[1:]+edges[:-1])
        # Analytic cell average of the sinusoid, not a point sample.
        density = 1 + .2*np.sinc(2.5*(edges[1]-edges[0])/np.pi)*np.sin(5*center)
        w = np.stack((density, np.zeros(n), np.zeros(n), np.ones(n)), axis=-1)
        w[center < -4] = (3.857143, 2.629369, 0., 10.33333)
    elif problem == 'sod':
        edges = np.linspace(0., 1., n+1)
        center = .5*(edges[1:]+edges[:-1])
        w = np.where((center < .5)[:, None], (1., 0., 0., 1.), (.125, 0., 0., .1))
    else:
        raise ValueError('Unknown 1D reference problem')
    return edges, conserved(w)


def solve_1d(problem='shu-osher', n=1600, final_time=None, cfl=.4):
    """Return a conservative 1D FV solution, embedded with zero transverse momentum."""
    if not isinstance(n, int) or n < 20 or n % 10 or not 0 < cfl <= .45:
        raise ValueError('Require n multiple of 10 >=20 and 0<CFL<=.45')
    if final_time is None:
        final_time = 1.8 if problem == 'shu-osher' else .2
    if not np.isfinite(final_time) or final_time < 0:
        raise ValueError('Invalid final time')
    edges, q = initial_1d(problem, n)
    dx = edges[1]-edges[0]
    initial = dx*q.sum(axis=0)
    boundary = np.zeros(4)
    t = 0.; steps = 0; fallbacks = 0; rejects = 0
    while t < final_time:
        w = primitive(q)
        dt = min(cfl*dx/np.max(abs(w[:, 1])+np.sqrt(GAMMA*w[:, 3]/w[:, 0])), final_time-t)
        while True:
            try:
                f0, b0, n0 = _rhs_1d(q, dx)
                u1 = q+dt*f0
                primitive(u1)
                f1, b1, n1 = _rhs_1d(u1, dx)
                u2 = .75*q+.25*(u1+dt*f1)
                primitive(u2)
                f2, b2, n2 = _rhs_1d(u2, dx)
                updated = q/3+2/3*(u2+dt*f2)
                primitive(updated)
                break
            except FloatingPointError:
                rejects += 1
                dt *= .5
                if dt < 1e-12:
                    raise
        q = updated
        boundary += dt*(b0/6+b1/6+2*b2/3)
        fallbacks += n0+n1+n2
        t += dt; steps += 1
    defect = dx*q.sum(axis=0)-initial-boundary
    return FVResult(edges, q, t, steps, boundary, initial,
         {'method':'FV conservative WENO5-JS/HLLC/SSPRK3',
          'reconstruction_fallbacks':fallbacks,'rejected_steps':rejects,
          'balance_residual':defect.tolist(), 'cfl':cfl})


def _minmod(a, b, c):
    same = (np.sign(a) == np.sign(b)) & (np.sign(a) == np.sign(c))
    return np.where(same, np.sign(a)*np.minimum(np.minimum(abs(a), abs(b)), abs(c)), 0.)


def double_mach_states():
    return conserved((8., 8.25*np.sqrt(3)/2, -4.125, 116.5)), conserved((1.4, 0., 0., 1.))


def _dmr_rhs(q, time, x, dx, dy):
    hot, cold = double_mach_states()
    g = np.pad(q, ((1, 1), (1, 1), (0, 0)), mode='edge')
    g[0, 1:-1] = hot
    g[1:-1, 0] = q[:, 0]
    g[1:-1, 0, 2] *= -1
    g[1:-1, 0] = np.where((x < 1/6)[:, None], hot, g[1:-1, 0])
    g[1:-1, -1] = np.where((x < 1/6+(1+20*time)/np.sqrt(3))[:, None], hot, cold)
    w = primitive(g)
    wc = w[1:-1, 1:-1]
    sx = _minmod(1.5*(wc-w[:-2, 1:-1]), .5*(w[2:, 1:-1]-w[:-2, 1:-1]),
                 1.5*(w[2:, 1:-1]-wc))
    sy = _minmod(1.5*(wc-w[1:-1, :-2]), .5*(w[1:-1, 2:]-w[1:-1, :-2]),
                 1.5*(w[1:-1, 2:]-wc))
    # MC-limited primitive rho,p stay positive at both face centers.
    xl, xr = conserved(wc-.5*sx), conserved(wc+.5*sx)
    yb, yt = conserved(wc-.5*sy), conserved(wc+.5*sy)
    fx = np.empty((len(x)+1, q.shape[1], 4))
    fy = np.empty((len(x), q.shape[1]+1, 4))
    fx[1:-1] = hll(xr[:-1], xl[1:], 0)
    fx[0] = hll(np.broadcast_to(hot, xl[0].shape), xl[0], 0)
    fx[-1] = flux(xr[-1], 0)
    fy[:, 1:-1] = hll(yt[:, :-1], yb[:, 1:], 1)
    reflected = yb[:, 0].copy(); reflected[:, 2] *= -1
    bottom = np.where((x < 1/6)[:, None], hot, reflected)
    fy[:, 0] = hll(bottom, yb[:, 0], 1)
    top = np.where((x < 1/6+(1+20*time)/np.sqrt(3))[:, None], hot, cold)
    fy[:, -1] = hll(yt[:, -1], top, 1)
    rhs = -(fx[1:]-fx[:-1])/dx-(fy[:, 1:]-fy[:, :-1])/dy
    inflow = dy*(fx[0].sum(axis=0)-fx[-1].sum(axis=0)) + dx*(fy[:, 0].sum(axis=0)-fy[:, -1].sum(axis=0))
    return rhs, inflow


def solve_double_mach(ny=64, final_time=.2, cfl=.3):
    """Independent 2D MUSCL/HLL reference; broad structures only at modest grids."""
    if not isinstance(ny, int) or ny < 8 or not 0 < cfl <= .4:
        raise ValueError('Require ny>=8, 0<CFL<=.4')
    if not np.isfinite(final_time) or final_time < 0:
        raise ValueError('Invalid final time')
    nx = 4*ny; dx = dy = 1/ny
    xe, ye = np.linspace(0, 4, nx+1), np.linspace(0, 1, ny+1)
    x, y = .5*(xe[1:]+xe[:-1]), .5*(ye[1:]+ye[:-1])
    # Match point-defined Woodward--Colella cell initialization, recorded as such.
    hot, cold = double_mach_states()
    q = np.where((x[:, None] < 1/6+y[None, :]/np.sqrt(3))[..., None], hot, cold)
    initial = dx*dy*q.sum(axis=(0, 1)); boundary = np.zeros(4)
    t = 0.; steps = 0; rejects = 0
    while t < final_time:
        w = primitive(q); sound = np.sqrt(GAMMA*w[..., 3]/w[..., 0])
        dt = min(cfl/(np.max(abs(w[..., 1])+sound)/dx
                     +np.max(abs(w[..., 2])+sound)/dy), final_time-t)
        while True:
            try:
                rhs0, b0 = _dmr_rhs(q, t, x, dx, dy)
                first = q+dt*rhs0
                primitive(first)
                rhs1, b1 = _dmr_rhs(first, t+dt, x, dx, dy)
                updated = .5*q+.5*(first+dt*rhs1)
                primitive(updated)
                break
            except FloatingPointError:
                dt *= .5; rejects += 1
                if dt < 1e-12:
                    raise
        q = updated; boundary += .5*dt*(b0+b1)
        t += dt; steps += 1
    return FVResult(xe, q, t, steps, boundary, initial,
         {'method':'unsplit FV primitive-MC MUSCL/HLL/SSPRK2',
          'initialization':'cell center hot/cold classification',
          'rejected_steps':rejects,'cfl':cfl,
          'balance_residual':(dx*dy*q.sum(axis=(0, 1))-initial-boundary).tolist()}, ye)


def save_reference(result, path, problem, wall_seconds):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    data = dict(x_edges=result.x_edges, q=result.q, time=result.time,
                initial_integral=result.initial_integral,
                boundary_integral=result.boundary_integral)
    if result.y_edges is not None:
        data['y_edges'] = result.y_edges
    np.savez_compressed(path, **data)
    source = Path(__file__)
    meta = {'problem':problem,'shape':list(result.q.shape),'time':result.time,
            'steps':result.steps,'wall_seconds':wall_seconds,
            'diagnostics':result.diagnostics,'gamma':GAMMA,
            'python':platform.python_version(),'numpy':np.__version__,
            'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'npz_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'independence':'No imports from numart or RKDG spatial/time implementation',
            'reference_scope':'finite resolution numerical comparison; no exact-solution claim'}
    path.with_suffix('.json').write_text(json.dumps(meta, indent=2)+'\n')
    return meta


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('problem', choices=('sod', 'shu-osher', 'double-mach'))
    parser.add_argument('--n', type=int, required=True, help='1D cells or DMR cells in y')
    parser.add_argument('--time', type=float)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    start = clock.perf_counter()
    if args.problem == 'double-mach':
        result = solve_double_mach(args.n, .2 if args.time is None else args.time)
    else:
        result = solve_1d(args.problem, args.n, args.time)
    print(json.dumps(save_reference(result, args.output, args.problem,
                                      clock.perf_counter()-start), indent=2))
