"""General binary64 Dirichlet difference-associated Jv; qualified on fixed vectors."""
import numpy as np


def laplace_difference(v):
    if v.ndim != 1 or len(v) < 1:
        raise ValueError('One nonempty interior vector required')
    left, right = np.empty_like(v), np.empty_like(v)
    left[0] = v[0]
    left[1:] = v[1:]-v[:-1]
    right[-1] = -v[-1]
    right[:-1] = v[1:]-v[:-1]
    return (left-right)*(len(v)+1)**2


def jac_action(u, coefficient, v):
    return laplace_difference(v)-coefficient*np.exp(u)*v
