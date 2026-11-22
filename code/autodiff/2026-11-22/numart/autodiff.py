"""Small real forward-mode AD and a shared Bratu verification problem.

Dual carries one tangent direction, so a Jacobian uses one evaluation per
input coordinate. This educational subset supports elementary arithmetic,
constant powers, exp, slicing, and matrix products; it is not a NumPy AD
replacement. No finite-difference approximation is used by AD.
"""
from dataclasses import dataclass
import numpy as np


def _matrix_product(left, right):
    # Match krylov.apply's explicit contraction for matrix-vector products.
    # This also avoids BLAS floating-status artifacts on some NumPy backends.
    if left.ndim == 2 and right.ndim == 1:
        return np.einsum('ij,j->i', left, right)
    return np.matmul(left, right)


@dataclass
class Dual:
    value: np.ndarray
    tangent: np.ndarray
    __array_priority__ = 1000

    def __post_init__(self):
        self.value = np.asarray(self.value, dtype=float)
        self.tangent = np.asarray(self.tangent, dtype=float)
        if self.value.shape != self.tangent.shape:
            raise ValueError("Value and tangent must have identical shapes")

    @staticmethod
    def constant(value):
        value = np.asarray(value, dtype=float)
        return Dual(value, np.zeros_like(value))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Dual) else Dual.constant(value)

    def __getitem__(self, key):
        return Dual(self.value[key], self.tangent[key])

    def __add__(self, other):
        other = self.coerce(other)
        return Dual(self.value + other.value, self.tangent + other.tangent)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, -self.tangent)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return Dual(self.value * other.value,
                    self.tangent * other.value + self.value * other.tangent)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        return Dual(self.value / other.value,
                    (self.tangent * other.value - self.value * other.tangent)
                    / other.value**2)

    def __rtruediv__(self, other):
        return self.coerce(other) / self

    def __pow__(self, exponent):
        if isinstance(exponent, Dual) or not np.isscalar(exponent):
            raise TypeError("This AD example supports constant scalar powers only")
        if exponent == 0:
            return Dual(np.ones_like(self.value), np.zeros_like(self.tangent))
        return Dual(self.value**exponent,
                    exponent * self.value**(exponent-1) * self.tangent)

    def __matmul__(self, other):
        other = self.coerce(other)
        return Dual(_matrix_product(self.value, other.value),
                    _matrix_product(self.tangent, other.value)
                    + _matrix_product(self.value, other.tangent))

    def __rmatmul__(self, other):
        return self.coerce(other) @ self

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        if method != '__call__' or kwargs:
            return NotImplemented
        if ufunc is np.exp:
            result = np.exp(self.value)
            return Dual(result, result * self.tangent)
        if ufunc is np.negative:
            return -self
        binary = {np.add: '__add__', np.subtract: '__sub__',
                  np.multiply: '__mul__', np.divide: '__truediv__',
                  np.matmul: '__matmul__'}
        if ufunc in binary:
            return getattr(self.coerce(inputs[0]), binary[ufunc])(inputs[1])
        if ufunc is np.power:
            return self.coerce(inputs[0]) ** inputs[1]
        return NotImplemented


def jvp(function, x, direction):
    """Evaluate f(x) and J(x) direction in one forward-mode traversal."""
    result = function(Dual(x, direction))
    if not isinstance(result, Dual):
        raise TypeError("Function must preserve Dual values")
    return result.value, result.tangent


def jacobian(function, x):
    """Dense Jacobian of a vector function, one forward seed per column."""
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or not len(x):
        raise ValueError("Jacobian example requires a nonempty input vector")
    return np.column_stack([jvp(function, x, seed)[1] for seed in np.eye(len(x))])


def finite_difference_jacobian(function, x, step, scheme='central'):
    """Absolute coordinate perturbations, with the scheme stated explicitly."""
    if not np.isfinite(step) or step <= 0 or scheme not in ('forward', 'central'):
        raise ValueError("Use a positive finite step and forward/central differences")
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or not len(x):
        raise ValueError("Finite differences require a nonempty input vector")
    base = function(x) if scheme == 'forward' else None
    columns = []
    for seed in np.eye(len(x)):
        plus = function(x + step*seed)
        columns.append((plus-base)/step if scheme == 'forward'
                       else (plus-function(x-step*seed))/(2*step))
    return np.column_stack(columns)


BRATU_LAMBDA = float(2 / np.cosh(.5)**2)


def bratu_matrix(n):
    """-d²/dx², n interior nodes, h=1/(n+1), homogeneous Dirichlet data."""
    if not isinstance(n, (int, np.integer)) or n < 1:
        raise ValueError("n must be a positive interior-node count")
    return (2*np.eye(n)-np.eye(n, k=1)-np.eye(n, k=-1)) * (n+1)**2


def bratu_residual(u, lam=BRATU_LAMBDA):
    """The same residual expression accepts ordinary or dual-valued states."""
    value = u.value if isinstance(u, Dual) else np.asarray(u, dtype=float)
    if value.ndim != 1:
        raise ValueError("Bratu state must be a vector")
    matrix = bratu_matrix(len(value))
    linear = matrix @ u if isinstance(u, Dual) else _matrix_product(matrix, value)
    return linear - lam*np.exp(u)


def bratu_jacobian(u, lam=BRATU_LAMBDA):
    u = np.asarray(u, dtype=float)
    return bratu_matrix(len(u)) - np.diag(lam*np.exp(u))


def bratu_reference(n):
    """Continuous small-branch solution for lambda=2/cosh(1/2)^2."""
    bratu_matrix(n)  # Validate the interior-node count.
    x = np.arange(1, n+1) / (n+1)
    return x, -2*np.log(np.cosh(x-.5)/np.cosh(.5))
