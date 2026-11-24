"""Independent exact small systems and power polynomials, never de Boor calls."""
from fractions import Fraction as F


def f(value):
    return F.from_float(float(value))


def eliminate(matrix, rhs):
    a = [list(row)+[value] for row, value in zip(matrix, rhs)]
    n = len(a)
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            raise ArithmeticError('Singular exact reference system')
        a[k], a[pivot] = a[pivot], a[k]
        scale = a[k][k]
        a[k] = [v/scale for v in a[k]]
        for i in range(n):
            if i != k:
                scale = a[i][k]
                a[i] = [u-scale*v for u, v in zip(a[i], a[k])]
    return [row[-1] for row in a]


def c2_coefficients(x, y, kind, slopes):
    x, y, slopes = [list(map(f, a)) for a in (x, y, slopes)]
    n = len(x)
    h = [x[i+1]-x[i] for i in range(n-1)]
    secants = [(y[i+1]-y[i])/h[i] for i in range(n-1)]
    matrix = [[F(0) for _ in x] for _ in x]
    rhs = [F(0) for _ in x]
    for i in range(1, n-1):
        matrix[i][i-1:i+2] = [h[i-1], 2*(h[i-1]+h[i]), h[i]]
        rhs[i] = 6*(secants[i]-secants[i-1])
    if kind == 'natural':
        matrix[0][0] = matrix[-1][-1] = F(1)
    else:
        matrix[0][:2] = [2*h[0], h[0]]
        matrix[-1][-2:] = [h[-1], 2*h[-1]]
        rhs[0] = 6*(secants[0]-slopes[0])
        rhs[-1] = 6*(slopes[-1]-secants[-1])
    second = eliminate(matrix, rhs)
    coeff = [[y[i], secants[i]-h[i]*(2*second[i]+second[i+1])/6,
              second[i]/2, (second[i+1]-second[i])/(6*h[i])] for i in range(n-1)]
    return x, coeff, second


def evaluate(x, coeff, point, derivative=0):
    z = f(point)
    i = min(len(x)-2, next((j for j in range(len(x)-1) if x[j] <= z < x[j+1]), len(x)-2))
    q = z-x[i]
    a, b, c, d = coeff[i]
    return a+b*q+c*q*q+d*q*q*q if derivative == 0 else b+2*c*q+3*d*q*q if derivative == 1 else 2*c+6*d*q


def _edge(h0, h1, m0, m1):
    raw = ((2*h0+h1)*m0-h0*m1)/(h0+h1)
    if raw*m0 <= 0:
        return F(0)
    if m0*m1 < 0 and abs(raw) > 3*abs(m0):
        return 3*m0
    return raw


def pchip_coefficients(x, y):
    x, y = list(map(f, x)), list(map(f, y))
    n = len(x)
    h = [x[i+1]-x[i] for i in range(n-1)]
    m = [(y[i+1]-y[i])/h[i] for i in range(n-1)]
    d = [F(0) for _ in x]
    if n == 2:
        d = [m[0], m[0]]
    else:
        for i in range(1, n-1):
            if m[i-1]*m[i] > 0:
                w1, w2 = 2*h[i]+h[i-1], h[i]+2*h[i-1]
                d[i] = (w1+w2)/(w1/m[i-1]+w2/m[i])
        d[0] = _edge(h[0], h[1], m[0], m[1])
        d[-1] = _edge(h[-1], h[-2], m[-1], m[-2])
    coeff = [[y[i], d[i], (3*m[i]-2*d[i]-d[i+1])/h[i],
              (d[i]+d[i+1]-2*m[i])/(h[i]*h[i])] for i in range(n-1)]
    return x, coeff, d


def plateau_certificates(a, b):
    a, b = f(a), f(b)
    delta = b-a
    return {'natural': a-9*delta/88, 'clamped': a-15*delta/152,
            'witness_a': a < F(1, 64), 'witness_delta': delta > F(1, 2),
            'a_exact': str(a), 'b_exact': str(b)}
