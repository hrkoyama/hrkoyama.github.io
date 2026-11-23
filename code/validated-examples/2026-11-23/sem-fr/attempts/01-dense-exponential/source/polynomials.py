"""Modest-degree Legendre/GLL tabulation for the two educational examples."""
import numpy as np
from numpy.polynomial.legendre import Legendre, legvander


def degree(value, low=1, high=6):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)) or not low <= value <= high:
        raise ValueError('Require an integer degree in the documented small range')
    return int(value)


def gll(p):
    p = degree(p)
    polynomial = Legendre.basis(p)
    nodes = np.r_[-1., polynomial.deriv().roots(), 1.]
    nodes = (nodes-nodes[::-1])/2
    weights = 2/(p*(p+1)*polynomial(nodes)**2)
    return nodes, weights


def cardinal(nodes, points, derivative=False):
    """Evaluate Lagrange basis or its reference derivative, without finite differences."""
    nodes, points = np.asarray(nodes, dtype=float), np.asarray(points, dtype=float)
    if nodes.ndim != 1 or len(nodes) < 2 or len(np.unique(nodes)) != len(nodes) or not np.isfinite(nodes).all():
        raise ValueError('Require distinct finite nodes')
    p = len(nodes)-1
    values = np.stack([Legendre.basis(k).deriv()(points) for k in range(p+1)], axis=-1) if derivative else legvander(points, p)
    return np.linalg.solve(legvander(nodes, p).T, values.reshape(-1, p+1).T).T.reshape(values.shape)
