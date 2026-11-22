"""Fixed matrix recipes; no algorithm under test is invoked here."""
import hashlib
import numpy as np


def array_sha256(value):
    return hashlib.sha256(np.ascontiguousarray(value, dtype='<f8').tobytes()).hexdigest()


def hadamard(n):
    if type(n) is not int or n < 1 or n > 64 or n & (n-1):
        raise ValueError('Power-of-two Hadamard size in [1,64] required')
    h = np.ones((1, 1))
    while len(h) < n:
        h = np.block([[h, h], [h, -h]])
    return h


def decomposition_fixture(exponent, perturbation=2.**-40):
    if type(exponent) is not int or exponent not in (0, 4, 8, 12):
        raise ValueError('Fixed dyadic spectrum exponent required')
    u = hadamard(16)[:, :4] / 4
    v = hadamard(4) / 2
    singular = np.exp2(-exponent*np.arange(4, dtype=float))
    matrix = np.einsum('ik,k,jk->ij', u, singular, v, optimize=False)
    b = u[:, 0].copy()
    perturbed = b + perturbation*u[:, -1]
    return matrix, b, perturbed, singular, u, v


def symmetric_fixture(n, gap):
    # Orthogonal construction is not the eigenvalue algorithm under test.
    index = np.arange(1, n+1, dtype=float)
    rotation = np.sqrt(2/(n+1))*np.sin(np.pi*np.outer(index, index)/(n+1))
    spectrum = np.r_[np.linspace(-1., 1., n-2), 5.-gap, 5.]
    matrix = np.einsum('ik,k,jk->ij', rotation, spectrum, rotation, optimize=False)
    return matrix, spectrum, rotation
