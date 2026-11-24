"""Exact stored-input references and operation-graph rounding certificates."""
from fractions import Fraction as F
from decimal import Decimal, localcontext
import sys


def rational(value):
    return F.from_float(float(value))


def exact_function(name, point):
    x = rational(point)
    if name == 'runge':
        return 1/(1+25*x*x)
    if name == 'absolute':
        return abs(x)
    raise ValueError('Unknown exact target')


def direct_lagrange(nodes, values, point):
    x, y, z = list(map(rational, nodes)), list(map(rational, values)), rational(point)
    total = F(0)
    for j in range(len(x)):
        term = y[j]
        for k in range(len(x)):
            if j != k:
                term *= (z-x[k])/(x[j]-x[k])
        total += term
    return total


def weighted_rational(nodes, values, weights, point):
    x, y, w = [list(map(rational, a)) for a in (nodes, values, weights)]
    z = rational(point)
    if z in x:
        return y[x.index(z)]
    t = [b/(z-a) for a, b in zip(x, w)]
    return sum((a*b for a, b in zip(t, y)), F(0))/sum(t, F(0))


def normal_or_zero(values):
    return all(float(v) == 0.0 or abs(float(v)) >= sys.float_info.min for v in values)


def barycentric_certificate(nodes, values, weights, point, computed, trace):
    x, y, w = [list(map(rational, a)) for a in (nodes, values, weights)]
    z = rational(point)
    t = [b/(z-a) for a, b in zip(x, w)]
    denominator = sum(t, F(0))
    numerator = sum((a*b for a, b in zip(t, y)), F(0))
    p = numerator/denominator
    u, count = F(1, 2**53), len(x)
    gamma = (count-1)*u/(1-(count-1)*u)
    eps_t = (1+u)/(1-u)-1
    eps_d = (1+eps_t)*(1+gamma)-1
    eps_n = (1+eps_t)*(1+u)*(1+gamma)-1
    ed = eps_d*sum(map(abs, t), F(0))
    en = eps_n*sum((abs(a*b) for a, b in zip(t, y)), F(0))
    if ed >= abs(denominator):
        raise ArithmeticError('Exact rounding-certificate denominator guard failed')
    pre = (en+abs(p)*ed)/(abs(denominator)-ed)
    bound = (1+u)*pre+u*abs(p)
    defect = abs(rational(computed)-p)
    return {'reference': p, 'bound': bound, 'defect': defect,
            'guard_ratio': ed/abs(denominator), 'lebesgue': sum(map(abs, t), F(0))/abs(denominator),
            'normal': normal_or_zero([*trace.flatten(), computed]), 'passed': defect <= bound}


def direct_chebyshev(coefficients, point):
    z = rational(point)
    c = list(map(rational, coefficients))
    t0, t1 = F(1), z
    total = c[0]
    if len(c) > 1:
        total += c[1]*t1
    for k in range(2, len(c)):
        t0, t1 = t1, 2*z*t1-t0
        total += c[k]*t1
    return total


def clenshaw_certificate(coefficients, point, computed, trace, final):
    z, u = rational(point), F(1, 2**53)
    c = list(map(rational, coefficients))
    e1, e2 = F(0), F(0)
    for row in trace:
        k = int(row[0])
        _, b1, b2, product, middle, _ = [rational(v) for v in row]
        local = u*(abs(2*z*b1)+abs(product-b2)+abs(middle+c[k]))
        e = 2*abs(z)*e1+e2+local
        e2, e1 = e1, e
    b1, b2, product, middle, _ = map(rational, final)
    local = u*(abs(z*b1)+abs(product-b2)+abs(c[0]+middle))
    bound = abs(z)*e1+e2+local
    reference = direct_chebyshev(coefficients, point)
    defect = abs(rational(computed)-reference)
    return {'reference': reference, 'bound': bound, 'defect': defect,
            'normal': normal_or_zero([*trace[:, 1:].flatten(), *final]), 'passed': defect <= bound}


def _atan_inverse(number):
    z = Decimal(1)/number
    total, power = Decimal(0), z
    for k in range(200):
        term = power/(2*k+1)
        total += term if k % 2 == 0 else -term
        if abs(term) < Decimal('1e-105'):
            return total
        power *= z*z
    raise ArithmeticError('Bounded Machin series did not finish')


def cosine_node_defects(positive):
    """Independent 110-digit Machin/Taylor check; no primary trig calls."""
    with localcontext() as ctx:
        ctx.prec = 110
        pi = 16*_atan_inverse(Decimal(5))-4*_atan_inverse(Decimal(239))
        defects = []
        for j, value in enumerate(positive):
            angle = pi*j/32
            term, total = Decimal(1), Decimal(1)
            for k in range(1, 150):
                term *= -angle*angle/((2*k-1)*(2*k))
                total += term
                if abs(term) < Decimal('1e-105'):
                    break
            else:
                raise ArithmeticError('Bounded cosine series did not finish')
            defects.append(float(abs(Decimal.from_float(float(value))-total)))
        return defects
