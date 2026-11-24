"""Fixed real root problems. Residual scaling never changes the root test."""
import numpy as np


class DomainError(ArithmeticError):
    pass


def dot(a, b):
    return float(np.sum(np.asarray(a)*np.asarray(b)))


def norm(a):
    return float(np.sqrt(dot(a, a)))


def mv(a, x):
    return np.einsum('ij,j->i', a, x)


def residual(kind, x, lam=3.):
    x = np.asarray(x, dtype=float)
    if not np.all(np.isfinite(x)):
        raise DomainError('Nonfinite candidate')
    if kind == 'rosenbrock':
        if np.max(np.abs(x)) > 1e100:
            raise DomainError('Polynomial trial exceeds the declared guard')
        return np.array([10*(x[1]-x[0]*x[0]), 1-x[0]])
    if kind == 'stationary':
        if abs(x[0]) > 1e100:
            raise DomainError('Polynomial trial exceeds the declared guard')
        return np.array([x[0]*x[0]+1])
    if kind == 'bratu':
        if np.max(x) > 700 or np.min(x) < -700:
            raise DomainError('Reject before an unrepresentable exponential')
        z = np.r_[0., x, 0.]
        return (2*z[1:-1]-z[:-2]-z[2:])*(len(x)+1)**2-lam*np.exp(x)
    raise ValueError(kind)


def jacobian(kind, x, lam=3.):
    if kind == 'rosenbrock':
        return np.array([[-20*x[0], 10.], [-1., 0.]])
    if kind == 'stationary':
        return np.array([[2*x[0]]])
    if kind == 'bratu':
        n = len(x); a = np.zeros((n, n)); scale = (n+1)**2
        for i in range(n):
            a[i, i] = 2*scale-lam*np.exp(x[i])
            if i: a[i, i-1] = -scale
            if i+1 < n: a[i, i+1] = -scale
        return a
    raise ValueError(kind)
