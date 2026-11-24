"""Explicit scalar interpolation operations; stored inputs define the experiment."""
import math
import numpy as np


def nodes_weights(degree, family, positive32):
    n = int(degree)
    if n not in (8, 16, 32):
        raise ValueError('Fixed degrees are 8, 16 and 32')
    if family == 'equispaced':
        x = [-1.0 + 2.0*j/n for j in range(n+1)]
        w = [float((-1)**j*math.comb(n, j))*2.0**(-n) for j in range(n+1)]
    elif family == 'lobatto':
        half = [float(positive32[j*(32//n)]) for j in range(n//2+1)]
        x = half + [-v for v in half[-2::-1]]
        w = [(-1.0)**j*(0.5 if j in (0, n) else 1.0) for j in range(n+1)]
    else:
        raise ValueError('Unknown fixed node family')
    return np.array(x), np.array(w)


def barycentric(x, y, w, point):
    """Ordered binary64 subtraction, division, product and sequential additions."""
    x, y, w = [tuple(float(v) for v in a) for a in (x, y, w)]
    if not (len(x) == len(y) == len(w)) or len(set(x)) != len(x):
        raise ValueError('Distinct equally sized node/data/weight vectors required')
    if not all(math.isfinite(v) for a in (x, y, w) for v in a):
        raise ValueError('Finite inputs required')
    z = float(point)
    for a, b in zip(x, y):
        if z == a:
            return b, None, np.empty((0, 5))
    numerator, denominator = 0.0, 0.0
    trace = []
    for a, b, weight in zip(x, y, w):
        difference = z-a
        term = weight/difference
        product = term*b
        numerator = numerator+product
        denominator = denominator+term
        trace.append((difference, term, product, numerator, denominator))
    if denominator == 0.0:
        raise ArithmeticError('Zero barycentric denominator')
    value = numerator/denominator
    if not math.isfinite(value):
        raise ArithmeticError('Nonfinite barycentric value')
    return value, denominator, np.array(trace)


def chebyshev_coefficients(x, y):
    """Finite Lobatto-inspired transform on stored nodes, FULL coefficients.

    T_k(x_j) is formed by the declared binary64 recurrence. Rounded-node
    discrete orthogonality is not asserted to be exact.
    """
    n = len(x)-1
    table = np.zeros((n+1, n+1))
    table[0] = 1.0
    table[1] = x
    for k in range(1, n):
        for j in range(n+1):
            table[k+1, j] = 2.0*float(x[j])*float(table[k, j])-float(table[k-1, j])
    c = []
    for k in range(n+1):
        total = 0.0
        for j in range(n+1):
            term = (0.5 if j in (0, n) else 1.0)*float(y[j])*float(table[k, j])
            total = total+term
        c.append((2.0/n)*(0.5 if k in (0, n) else 1.0)*total)
    return np.array(c), table


def clenshaw(c, point):
    """Three rounded operations per stage; actual trace supports a certificate."""
    z = float(point)
    two_z = 2.0*z
    b1, b2 = 0.0, 0.0
    trace = []
    for k in range(len(c)-1, 0, -1):
        product = two_z*b1
        middle = product-b2
        value = middle+float(c[k])
        trace.append((k, b1, b2, product, middle, value))
        b2, b1 = b1, value
    product = z*b1
    middle = product-b2
    value = float(c[0])+middle
    return value, np.array(trace).reshape((-1, 6)), np.array((b1, b2, product, middle, value))


def target(name, x):
    if name == 'runge':
        return 1.0/(1.0+25.0*x*x)
    if name == 'absolute':
        return np.abs(x)
    if name == 'polynomial':
        return 1.0-2.0*x+3.0*x*x-x*x*x
    raise ValueError('Unknown fixed function')
