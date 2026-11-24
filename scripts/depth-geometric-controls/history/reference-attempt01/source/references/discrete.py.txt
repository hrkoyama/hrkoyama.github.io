"""Independent fixed-coefficient Decimal/Fraction matrix actions.

Shared float trig input is intentional for the frozen-coefficient oracle.
The ideal mathematical-angle oracle computes its own Decimal pi/trig.
"""
import math
from decimal import Decimal, localcontext
from fractions import Fraction
import numpy as np


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def mv(a, b):
    return [sum(x*y for x, y in zip(row, b)) for row in a]


def eye(number):
    return [[number(int(i == j)) for j in range(4)] for i in range(4)]


def stage_matrices(c, method, number=float):
    def n(x):
        if number is Decimal:
            return Decimal.from_float(float(x))
        if number is Fraction:
            return Fraction.from_float(float(x))
        return float(x)
    kick, flow = eye(number), eye(number)
    kick[2][0], kick[2][1] = -n(c['half']), -n(c['cross'])
    kick[3][0], kick[3][1] = -n(c['cross']), -n(c['stiff'])
    flow[0][2] = n(c['h'])
    if method == 'verlet':
        flow[1][3] = n(c['h'])
    else:
        flow[1][1] = flow[3][3] = n(c['cosine'])
        flow[1][3] = n(c['sine_over_omega'])
        flow[3][1] = -n(c['omega_sine'])
    return [kick, flow, kick]


def action(c, method, steps, precision=80, initial=None, raw_callback=None):
    with localcontext() as ctx:
        ctx.prec = precision
        z = [Decimal.from_float(float(x)) for x in
             ((1., 1./c['omega'], 0., 0.) if initial is None else initial)]
        matrices = stage_matrices(c, method, Decimal)
        states = [list(z)]
        for i in range(steps):
            for matrix in matrices:
                z = mv(matrix, z)
            states.append(list(z))
            if raw_callback is not None and (i+1) % 16 == 0:
                raw_callback(i+1, [[str(x) for x in row] for row in states])
        return states


def binary_coefficients(method, omega, alpha, h):
    """Independent construction, same explicitly declared libm convention."""
    h, omega, alpha = float(h), float(omega), float(alpha)
    theta = h*omega
    sine, cosine = math.sin(theta), math.cos(theta)
    return dict(h=h, omega=omega, alpha=alpha, half=h/2,
                cross=(h/2)*alpha,
                stiff=(h/2)*(omega*omega) if method == 'verlet' else 0.,
                cosine=cosine, sine_over_omega=sine/omega, omega_sine=omega*sine)


def roundoff_allowance(c, method, stage_inputs, reference):
    matrices = stage_matrices(c, method)
    eps = np.finfo(float).eps; gamma = 8*eps/(1-8*eps)
    error = [0., 0., 0., 0.]; result = [list(error)]
    for trial in stage_inputs:
        for matrix, actual in zip(matrices, trial):
            error = [sum(abs(matrix[i][j])*error[j] for j in range(4)) +
                     gamma*sum(abs(matrix[i][j])*abs(float(actual[j])) for j in range(4))
                     for i in range(4)]
        result.append(list(error))
    allowance = np.asarray(result)
    scale = np.asarray([1., 1./c['omega'], 1., 1.])
    return allowance+6*eps*(np.abs(reference)+scale)


def decimal_pi():
    def atan(x):
        term = x; total = term; square = x*x; k = 1
        while True:
            term *= -square
            add = term/Decimal(2*k+1)
            previous = total; total += add; k += 1
            if total == previous:
                return total
    return 16*atan(Decimal(1)/5)-4*atan(Decimal(1)/239)


def decimal_trig(x):
    sine, cosine = x, Decimal(1); st, ct = x, Decimal(1); k = 1
    while True:
        st *= -(x*x)/Decimal((2*k)*(2*k+1))
        ct *= -(x*x)/Decimal((2*k-1)*(2*k))
        old = (sine, cosine); sine += st; cosine += ct; k += 1
        if old == (sine, cosine):
            return sine, cosine


def ideal_matrix(omega, factor, precision=80):
    with localcontext() as ctx:
        ctx.prec = precision
        theta = Decimal(str(factor))*decimal_pi(); h = theta/Decimal(omega)
        sine, cosine = decimal_trig(theta)
        kick, flow = eye(Decimal), eye(Decimal)
        kick[2][0] = kick[2][1] = kick[3][0] = -h/2
        flow[0][2] = h; flow[1][1] = flow[3][3] = cosine
        flow[1][3] = sine/omega; flow[3][1] = -omega*sine
        return mm(kick, mm(flow, kick))


def ideal_classification(omega, factor, precision=80):
    if factor == 1.:
        return 'defective_jordan', Decimal(0)
    with localcontext() as ctx:
        ctx.prec = precision
        matrix = ideal_matrix(omega, factor, precision)
        trace = sum(matrix[i][i] for i in range(4)); square = mm(matrix, matrix)
        coefficient = (trace*trace-sum(square[i][i] for i in range(4)))/2
        discriminant = trace*trace-4*(coefficient-2)
        if discriminant < 0:
            return 'unstable', -discriminant
        root = discriminant.sqrt(); xs = [(trace+root)/2, (trace-root)/2]
        margin = min(abs(abs(x)-2) for x in xs)
        if margin < Decimal('1e-40'):
            return 'unresolved_near_degeneracy', margin
        return ('stable' if max(abs(x) for x in xs) < 2 else 'unstable'), margin


def fraction_rank(matrix):
    a = [list(row) for row in matrix]; pivot = 0
    for col in range(len(a[0])):
        row = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if row is None:
            continue
        a[pivot], a[row] = a[row], a[pivot]
        divisor = a[pivot][col]; a[pivot] = [v/divisor for v in a[pivot]]
        for i in range(len(a)):
            if i != pivot:
                divisor = a[i][col]
                a[i] = [x-divisor*y for x, y in zip(a[i], a[pivot])]
        pivot += 1
    return pivot


def exact_pi_component(h, alpha=Fraction(1)):
    """Exact rational test of the authored general-h ideal-pi identity."""
    zero = Fraction(0); one = Fraction(1)
    matrix = [[one-h*h/2, -h*h*alpha/2, h, zero],
              [zero, -one, zero, zero],
              [-h*(one-h*h/4), h*h*h*alpha/4, one-h*h/2, zero],
              [h*h*h*alpha/4, h*h*h*alpha*alpha/4, -h*h*alpha/2, -one]]
    identity = eye(Fraction); plus = [[matrix[i][j]+identity[i][j] for j in range(4)] for i in range(4)]
    square = mm(matrix, matrix)
    slow = [[square[i][j]-(2-h*h)*matrix[i][j]+identity[i][j]
             for j in range(4)] for i in range(4)]
    annihilator = mm(mm(plus, plus), slow)
    return matrix, fraction_rank(plus), all(x == 0 for row in annihilator for x in row)
