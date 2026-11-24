"""Original-u sparse affine and independent closed sine-series reference.

No primary DST or boundary-subflow function is imported.
"""
import math
import numpy as np
from scipy.sparse import bmat, csc_matrix, diags
from scipy.sparse.linalg import expm_multiply


def exact_continuum(x, t):
    equilibrium = np.cos(x-0.5)/math.cos(0.5)
    return equilibrium+0.1*math.exp((1-math.pi*math.pi)*t)*np.sin(math.pi*x)


def operators(n):
    dx = 1/(n+1)
    matrix = diags([np.ones(n-1)/dx**2, np.full(n, 1-2/dx**2), np.ones(n-1)/dx**2], [-1, 0, 1], format='csc')
    source = np.zeros(n)
    source[0] = source[-1] = 1/dx**2
    augmented = bmat([[matrix, csc_matrix(source[:, None])], [csc_matrix((1, n)), csc_matrix((1, 1))]], format='csc')
    return matrix, source, augmented


def sparse_action(n, times, save):
    matrix, source, augmented = operators(n)
    x = np.arange(1, n+1)/(n+1)
    initial = exact_continuum(x, 0.)
    vector = np.r_[initial, 1.]
    rows = []
    save('before-sparse-action', x=x, initial=initial, matrix_data=augmented.data,
         matrix_indices=augmented.indices, matrix_indptr=augmented.indptr)
    trace = float(augmented.diagonal().sum())
    for t in times:
        value = vector.copy() if t == 0 else expm_multiply(t*augmented, vector, traceA=t*trace)
        rows.append(value[:-1].copy())
        save('completed-sparse-action', x=x, times=np.asarray(times[:len(rows)]), states=np.array(rows), affine_last=np.array([value[-1]]))
    return x, np.array(rows), matrix, source


def sine_solution(n, times):
    dx = 1/(n+1)
    x = np.arange(1, n+1)*dx
    angle = 2*math.asin(dx/2)
    equilibrium = np.array([math.cos(angle*(j-(n+1)/2))/math.cos(angle*(n+1)/2) for j in range(1, n+1)])
    # Independently formed dense sine basis is reference-only, n<=127.
    basis = np.array([[math.sqrt(2/(n+1))*math.sin(math.pi*j*k/(n+1))
                       for k in range(1, n+1)] for j in range(1, n+1)])
    initial = exact_continuum(x, 0.)
    coefficients = np.einsum('jk,j->k', basis, initial-equilibrium, optimize=False)
    eigen = np.array([1-4*math.sin(math.pi*k/(2*(n+1)))**2/dx**2 for k in range(1, n+1)])
    states, rates = [], []
    for t in times:
        modes = coefficients*np.exp(t*eigen)
        states.append(equilibrium+np.einsum('jk,k->j', basis, modes, optimize=False))
        rates.append(np.einsum('jk,k->j', basis, eigen*modes, optimize=False))
    return np.array(states), np.array(rates)
