"""Independent assembled-band/direct reference; primary actions are not used."""
import numpy as np
from scipy.linalg import solve_banded, eigh_tridiagonal


def solve(diagonal, lower, upper, rhs, transpose=False):
    if transpose:
        lower, upper = upper, lower
    ab = np.zeros((3, len(diagonal)))
    ab[0, 1:], ab[1], ab[2, :-1] = upper, diagonal, lower
    return solve_banded((1, 1), ab, rhs, check_finite=True)


def bratu(u, coefficient):
    n = len(u)
    scale = (n+1)**2
    return 2*scale-coefficient*np.exp(u), np.full(n-1, -scale), np.full(n-1, -scale)


def smallest(u, coefficient):
    diagonal, lower, _ = bratu(u, coefficient)
    eigenvalues = eigh_tridiagonal(diagonal, lower, eigvals_only=True, check_finite=True)
    return float(np.min(np.abs(eigenvalues))), float(eigenvalues[0])


def dense_hats(n, m):
    # Separately evaluated all-hat formula; allowed ONLY in this reference.
    x = np.arange(1, n+1, dtype=float)/(n+1)
    nodes = np.arange(m, dtype=float)/(m-1)
    return np.maximum(0.0, 1.0-np.abs(x[:, None]-nodes[None, :])*(m-1))


def full_sensitivity(u, coefficient, m):
    B = dense_hats(len(u), m)
    diagonal, lower, upper = bratu(u, coefficient)
    S = solve(diagonal, lower, upper, np.exp(u)[:, None]*B)
    return B, S
