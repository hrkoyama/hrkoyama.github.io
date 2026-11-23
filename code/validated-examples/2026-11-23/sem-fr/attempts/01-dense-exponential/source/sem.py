"""Continuous tensor-product Legendre GLL SEM for a square Poisson problem.

Affine square elements, GLL stiffness/load quadrature, strong Dirichlet data.
This is a small assembled sparse solver, not a Nek5000/nekRS implementation.
"""
from dataclasses import dataclass
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve
from polynomials import cardinal, degree, gll


def exact(x, y):
    return np.sin(np.pi*x)*np.sin(np.pi*y)


def gradient(x, y):
    return np.pi*np.cos(np.pi*x)*np.sin(np.pi*y), np.pi*np.sin(np.pi*x)*np.cos(np.pi*y)


@dataclass
class Solution:
    elements: int
    degree: int
    nodes: np.ndarray
    values: np.ndarray
    stiffness: object
    rhs: np.ndarray
    free: np.ndarray
    residual: float


def solve(elements, p, forcing=None, boundary=None):
    p = degree(p)
    if type(elements) is not int or not 1 <= elements <= 16:
        raise ValueError('Require 1..16 elements per coordinate')
    forcing = forcing or (lambda x, y: 2*np.pi**2*exact(x, y))
    boundary = boundary or (lambda x, y: np.zeros_like(x+y))
    z, w = gll(p)
    d = cardinal(z, z, derivative=True)
    mass = np.diag(w)
    stiffness = d.T @ mass @ d
    # For a square, J_y/J_x=J_x/J_y=1. C order: y index varies fastest.
    local = np.kron(stiffness, mass)+np.kron(mass, stiffness)
    count = elements*p+1
    nodes = np.concatenate([(e+(z[:-1]+1)/2)/elements for e in range(elements)]+[np.array([1.])])
    rows, columns, entries = [], [], []
    rhs = np.zeros(count*count)
    for ex in range(elements):
        for ey in range(elements):
            ix, iy = ex*p+np.arange(p+1), ey*p+np.arange(p+1)
            ids = (ix[:, None]*count+iy[None, :]).ravel()
            x, y = np.meshgrid(nodes[ix], nodes[iy], indexing='ij')
            load = np.broadcast_to(forcing(x, y), x.shape)*np.outer(w, w)/(4*elements**2)
            if not np.isfinite(load).all():
                raise ValueError('Nonfinite load')
            rhs[ids] += load.ravel()
            rows.extend(np.repeat(ids, len(ids))); columns.extend(np.tile(ids, len(ids))); entries.extend(local.ravel())
    matrix = coo_matrix((entries, (rows, columns)), shape=(count**2, count**2)).tocsr()
    x, y = np.meshgrid(nodes, nodes, indexing='ij')
    fixed = np.flatnonzero(((x == 0) | (x == 1) | (y == 0) | (y == 1)).ravel())
    free = np.setdiff1d(np.arange(count**2), fixed)
    u = np.zeros(count**2)
    u[fixed] = np.broadcast_to(boundary(x.ravel()[fixed], y.ravel()[fixed]), fixed.shape)
    reduced_rhs = rhs[free]-matrix[free][:, fixed]@u[fixed]
    if len(free):
        u[free] = spsolve(matrix[free][:, free], reduced_rhs)
    residual = float(np.linalg.norm((matrix@u-rhs)[free])/max(np.linalg.norm(rhs[free]), np.finfo(float).tiny)) if len(free) else 0.
    if not np.isfinite(u).all():
        raise ArithmeticError('Nonfinite SEM solution')
    return Solution(elements, p, nodes, u.reshape(count, count), matrix, rhs, free, residual)


def errors(solution, value=exact, derivative=gradient, quadrature=None):
    """Continuous L2 and H1 seminorm with Gauss points independent of GLL nodes."""
    p, elements = solution.degree, solution.elements
    z, _ = gll(p)
    q, w = leggauss(quadrature or p+4)
    b, d = cardinal(z, q), cardinal(z, q, derivative=True)
    weights = np.outer(w, w)/(4*elements**2)
    l2, h1 = 0., 0.
    for ex in range(elements):
        for ey in range(elements):
            u = solution.values[ex*p:ex*p+p+1, ey*p:ey*p+p+1]
            x, y = np.meshgrid((ex+(q+1)/2)/elements, (ey+(q+1)/2)/elements, indexing='ij')
            gx, gy = derivative(x, y)
            l2 += float(np.sum(weights*(b@u@b.T-value(x, y))**2))
            h1 += float(np.sum(weights*((2*elements*d@u@b.T-gx)**2+(2*elements*b@u@d.T-gy)**2)))
    return float(np.sqrt(l2)), float(np.sqrt(h1))
