"""Small actual Dirichlet operators and explicitly owned work arrays."""
import math
import numpy as np
from balanced_operator import jac_action as _difference_jac_action


def dot(x, y):
    return float(np.einsum('i,i->', x, y, optimize=False))


def norm(x):
    return math.sqrt(max(0.0, dot(x, x)))


def hnorm(x):
    return norm(x) / math.sqrt(len(x) + 1)


def laplace(x, out=None):
    """A_h=-Dxx on interior unknowns; missing neighbors are fixed zero."""
    if out is None:
        out = np.empty_like(x)
    np.multiply(x, 2.0, out=out)
    out[:-1] -= x[1:]
    out[1:] -= x[:-1]
    out *= (len(x) + 1)**2
    return out


def residual(u, coefficient):
    with np.errstate(over='raise', invalid='raise', divide='raise'):
        return laplace(u) - coefficient * np.exp(u)


def jac_action(u, coefficient, v):
    return _difference_jac_action(u, coefficient, v)


def tridiagonal_action(diagonal, lower, upper, v, transpose=False):
    if transpose:
        lower, upper = upper, lower
    out = diagonal * v
    out[1:] += lower * v[:-1]
    out[:-1] += upper * v[1:]
    return out


class TriFactor:
    """Thomas factorization; solve scratch/output supplied by the caller."""
    def __init__(self, lower, diagonal, upper):
        self.lower = np.array(lower, dtype=float, copy=True)
        self.diagonal = np.array(diagonal, dtype=float, copy=True)
        self.upper = np.array(upper, dtype=float, copy=True)
        self.pivot = self.diagonal.copy()
        self.cprime = self.upper.copy()
        n = len(self.pivot)
        if n < 1 or len(self.lower) != n-1 or len(self.upper) != n-1:
            raise ValueError('Tridiagonal dimensions')
        for k in range(n):
            if not math.isfinite(self.pivot[k]) or self.pivot[k] == 0:
                raise ArithmeticError('Zero/nonfinite Thomas pivot')
            if k < n-1:
                self.cprime[k] /= self.pivot[k]
                self.pivot[k+1] -= self.lower[k] * self.cprime[k]

    def solve(self, rhs, out=None, scratch=None):
        if out is None:
            out = np.empty_like(rhs)
        if scratch is None:
            scratch = np.empty_like(rhs)
        if np.shares_memory(rhs, out) or np.shares_memory(rhs, scratch) or np.shares_memory(out, scratch):
            raise ValueError('Thomas input/output/scratch must have distinct owners')
        scratch[0] = rhs[0] / self.pivot[0]
        for k in range(1, len(rhs)):
            scratch[k] = (rhs[k]-self.lower[k-1]*scratch[k-1]) / self.pivot[k]
        out[-1] = scratch[-1]
        for k in range(len(rhs)-2, -1, -1):
            out[k] = scratch[k]-self.cprime[k]*out[k+1]
        return out

    def transpose(self):
        return TriFactor(self.upper, self.diagonal, self.lower)

    def arrays(self, prefix):
        return {prefix+'.'+name: value for name, value in vars(self).items()}


def poisson_factor(n):
    scale = (n+1)**2
    return TriFactor(np.full(n-1, -scale), np.full(n, 2*scale), np.full(n-1, -scale))


class LocalHats:
    """Endpoint coefficients; two entries/node, never an n by m matrix."""
    def __init__(self, n, m):
        if n < 1 or m < 2:
            raise ValueError('Hat dimensions')
        self.n, self.m = n, m
        x = np.arange(1, n+1, dtype=float)/(n+1)
        coordinate = x*(m-1)
        left = np.minimum(np.floor(coordinate).astype(np.int64), m-2)
        fraction = coordinate-left
        self.index = np.column_stack((left, left+1))
        self.weight = np.column_stack((1-fraction, fraction))
        self.calls = {'B': 0, 'BT': 0}

    def forward(self, theta):
        if np.shape(theta) != (self.m,):
            raise ValueError('Hat parameter shape')
        self.calls['B'] += 1
        return self.weight[:, 0]*theta[self.index[:, 0]] + self.weight[:, 1]*theta[self.index[:, 1]]

    def transpose(self, w):
        if np.shape(w) != (self.n,):
            raise ValueError('Hat cotangent shape')
        self.calls['BT'] += 1
        out = np.zeros(self.m)
        np.add.at(out, self.index[:, 0], self.weight[:, 0]*w)
        np.add.at(out, self.index[:, 1], self.weight[:, 1]*w)
        return out


def owning_root(array):
    while isinstance(array.base, np.ndarray):
        array = array.base
    return array


class BufferLedger:
    """Explicit live scientific-array inventory, not a process RSS monitor."""
    def __init__(self):
        self.peak_state_elements = 0
        self.peak_total_bytes = 0
        self.observations = []

    def observe(self, state, other):
        roots, state_roots = {}, set()
        entries = []
        for category, arrays in [('state', state), ('factor-model-work', other)]:
            for name, array in arrays.items():
                if array is None:
                    continue
                root = owning_root(array)
                key = id(root)
                roots[key] = root
                if category == 'state':
                    state_roots.add(key)
                entries.append({'name': name, 'category': category, 'shape': list(array.shape),
                                'owner_shape': list(root.shape), 'owner_bytes': int(root.nbytes),
                                'alias_owner': next((e['name'] for e in entries if e['_id'] == key), name),
                                '_id': key})
        elements = sum(roots[key].size for key in state_roots)
        total = sum(array.nbytes for array in roots.values())
        if elements > self.peak_state_elements or total > self.peak_total_bytes:
            self.observations.append({'state_elements': int(elements), 'total_bytes': int(total),
                                      'arrays': [{k: v for k, v in e.items() if k != '_id'} for e in entries]})
        self.peak_state_elements = max(self.peak_state_elements, int(elements))
        self.peak_total_bytes = max(self.peak_total_bytes, int(total))

    def report(self):
        return {'peak_state_elements': self.peak_state_elements, 'peak_total_bytes': self.peak_total_bytes,
                'ownership': self.observations, 'scope': 'Explicit unique owned numeric buffers; not total process RSS.'}
