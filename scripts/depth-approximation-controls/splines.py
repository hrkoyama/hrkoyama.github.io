"""Small cubic B-spline collocation/de Boor and a separate PCHIP path."""
from functools import lru_cache
import numpy as np


def basis_vector(knots, degree, point, derivative=0):
    t = tuple(float(x) for x in knots)
    z = float(point)
    @lru_cache(None)
    def basis(i, p, d):
        if d > p:
            return 0.0
        if d:
            left = p/(t[i+p]-t[i])*basis(i, p-1, d-1) if t[i+p] != t[i] else 0.0
            right = p/(t[i+p+1]-t[i+1])*basis(i+1, p-1, d-1) if t[i+p+1] != t[i+1] else 0.0
            return left-right
        if p == 0:
            return float(t[i] <= z < t[i+1] or (z == t[-1] and t[i] < z == t[i+1]))
        left = (z-t[i])/(t[i+p]-t[i])*basis(i, p-1, 0) if t[i+p] != t[i] else 0.0
        right = (t[i+p+1]-z)/(t[i+p+1]-t[i+1])*basis(i+1, p-1, 0) if t[i+p+1] != t[i+1] else 0.0
        return left+right
    return np.array([basis(i, degree, derivative) for i in range(len(t)-degree-1)])


def fit(x, y, kind, endpoint_slopes, observe=None):
    x, y = np.array(x, dtype=float, copy=True), np.array(y, dtype=float, copy=True)
    if len(x) < 2 or len(x) != len(y) or np.any(np.diff(x) <= 0) or not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ValueError('Strictly increasing finite input required')
    knots = np.r_[np.repeat(x[0], 4), x[1:-1], np.repeat(x[-1], 4)]
    rows = [basis_vector(knots, 3, z) for z in x]
    order = 2 if kind == 'natural' else 1
    if kind not in ('natural', 'clamped'):
        raise ValueError('Unknown C2 boundary conditions')
    rows.extend([basis_vector(knots, 3, x[0], order), basis_vector(knots, 3, x[-1], order)])
    rhs = np.r_[y, [0.0, 0.0] if kind == 'natural' else endpoint_slopes]
    matrix = np.array(rows)
    if observe is not None:
        observe(x=x, y=y, knots=knots, matrix=matrix, rhs=rhs)
    coefficients = np.linalg.solve(matrix, rhs)
    return {'knots': knots, 'coefficients': coefficients, 'matrix': matrix, 'rhs': rhs}


def deboor(knots, coefficients, point, degree=3):
    t, c, z = np.asarray(knots), np.asarray(coefficients), float(point)
    if not t[degree] <= z <= t[len(c)]:
        raise ValueError('Extrapolation is outside this fixed experiment')
    span = len(c)-1 if z == t[len(c)] else int(np.searchsorted(t, z, side='right')-1)
    work = [float(c[span-degree+j]) for j in range(degree+1)]
    for r in range(1, degree+1):
        for j in range(degree, r-1, -1):
            i = span-degree+j
            denominator = float(t[i+degree-r+1]-t[i])
            alpha = (z-float(t[i]))/denominator if denominator else 0.0
            work[j] = (1.0-alpha)*work[j-1]+alpha*work[j]
    return work[degree]


def evaluate(model, points, derivative=0):
    t = np.array(model['knots'], copy=True)
    c = np.array(model['coefficients'], copy=True)
    degree = 3
    for _ in range(derivative):
        c = np.array([degree*(float(c[i+1])-float(c[i]))/float(t[i+degree+1]-t[i+1]) for i in range(len(c)-1)])
        t, degree = t[1:-1], degree-1
    return np.array([deboor(t, c, z, degree) for z in points])


def endpoint(h0, h1, m0, m1):
    d = ((2.0*h0+h1)*m0-h0*m1)/(h0+h1)
    if np.sign(d) != np.sign(m0):
        return 0.0
    if np.sign(m0) != np.sign(m1) and abs(d) > 3.0*abs(m0):
        return 3.0*m0
    return float(d)


def pchip_slopes(x, y):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    if len(x) != len(y) or len(x) < 2 or np.any(np.diff(x) <= 0) or not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ValueError('Strictly increasing finite data required')
    h, m = np.diff(x), np.diff(y)/np.diff(x)
    if len(x) == 2:
        return np.repeat(m[0], 2)
    d = np.zeros(len(x))
    for k in range(1, len(x)-1):
        if m[k-1]*m[k] > 0:
            w1, w2 = 2*h[k]+h[k-1], h[k]+2*h[k-1]
            d[k] = (w1+w2)/(w1/m[k-1]+w2/m[k])
    d[0] = endpoint(h[0], h[1], m[0], m[1])
    d[-1] = endpoint(h[-1], h[-2], m[-1], m[-2])
    return d


def hermite_coefficients(x, y, slopes):
    h = np.diff(x)
    secants = np.diff(y)/h
    # Ascending powers of (x-x_i), one row per interval.
    return np.stack((np.asarray(y[:-1]), slopes[:-1], (3*secants-2*slopes[:-1]-slopes[1:])/h,
                     (slopes[:-1]+slopes[1:]-2*secants)/(h*h)), axis=1)


def power_evaluate(x, coefficients, points, derivative=0):
    out = []
    for z in points:
        i = min(len(x)-2, max(0, int(np.searchsorted(x, z, side='right')-1)))
        s = float(z-x[i])
        a, b, c, d = coefficients[i]
        out.append(a+s*(b+s*(c+s*d)) if derivative == 0 else b+s*(2*c+3*s*d) if derivative == 1 else 2*c+6*s*d)
    return np.array(out)
