"""Independent scalar/Fraction/Decimal components and loop-assembled audits."""
from decimal import Decimal, localcontext
from fractions import Fraction
import numpy as np
from scipy.linalg import solve


def dogleg_intersection(delta, precision=60):
    with localcontext() as c:
        c.prec = precision
        pu = [Decimal(-68)/65, Decimal(-17)/65]; pb = [Decimal(-1), Decimal(-1)]
        v = [pb[i]-pu[i] for i in range(2)]
        aa = sum(z*z for z in v); bb = 2*sum(pu[i]*v[i] for i in range(2))
        cc = sum(z*z for z in pu)-Decimal(str(delta))**2
        t = (-bb+(bb*bb-4*aa*cc).sqrt())/(2*aa)
        return np.array([float(pu[i]+t*v[i]) for i in range(2)])


def independent_residual(kind, x):
    if kind == 'rosenbrock': return np.array([10*x[1]-10*x[0]**2, 1-x[0]])
    if kind == 'stationary': return np.array([1+x[0]**2])
    n = len(x); result = []
    for i in range(n):
        left = x[i-1] if i else 0.; right = x[i+1] if i+1 < n else 0.
        result.append((n+1)**2*(2*x[i]-left-right)-3*np.exp(x[i]))
    return np.array(result)


def independent_correction(x):
    n = len(x); a = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j: a[i, j] = 2*(n+1)**2-3*np.exp(x[i])
            elif abs(i-j) == 1: a[i, j] = -(n+1)**2
    return solve(a, independent_residual('bratu', x), assume_a='gen', check_finite=True)


def fraction_cauchy():
    g = [Fraction(4), Fraction(1)]; numerator = sum(z*z for z in g)
    denominator = Fraction(8)**2+Fraction(1)**2
    return np.array([float(-numerator*z/denominator) for z in g])
