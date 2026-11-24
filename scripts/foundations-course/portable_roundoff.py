"""Independent decimal oracle for the fixed sine cancellation demonstration.
This validates the arithmetic error envelope, not cross-platform bit equality.
No scientific acceptance threshold in inputs.json is changed.
"""
from decimal import Decimal, localcontext
import math

D = Decimal.from_float
ORACLE_REMAINDER = Decimal('1e-70')


def sincos_decimal(x):
    """80-digit Taylor oracle, restricted to this example's |x| <= 2.
    At most 80 terms; the next term is below 1e-75 and rounding is
    enclosed by the deliberately larger 1e-70 oracle remainder.
    """
    assert abs(x) <= 2
    with localcontext() as ctx:
        ctx.prec = 80
        x = D(x)
        sine = sine_term = x
        cosine = cosine_term = Decimal(1)
        for k in range(1, 80):
            sine_term *= -x*x / ((2*k)*(2*k+1))
            cosine_term *= -x*x / ((2*k-1)*(2*k))
            sine += sine_term
            cosine += cosine_term
            if max(abs(sine_term), abs(cosine_term)) < Decimal('1e-75'):
                return +sine, +cosine
        raise AssertionError('Taylor oracle did not converge')


def validate_derivative_row(row, x=1.0):
    """Require the row to lie in the independently derived libm envelope.
    One ULP for each sine evaluation, exact subtraction by Sterbenz for
    these positive close values, plus one ULP for division. The absolute
    error column must agree with the 80-digit cosine up to its rounding.
    """
    h, approximation, error = map(float, row)
    assert h > 0 and all(map(math.isfinite, [h, approximation, error])) and error >= 0
    plus_arg, minus_arg = x+h, x-h
    plus, _ = sincos_decimal(plus_arg)
    minus, _ = sincos_decimal(minus_arg)
    _, cosine = sincos_decimal(x)
    a, b = math.sin(plus_arg), math.sin(minus_arg)
    assert a > 0 and b > 0 and 0.5 <= a/b <= 2, 'Sterbenz scope'
    with localcontext() as ctx:
        ctx.prec = 80
        # Check the assumed one-ULP libm bounds on the executing platform.
        assert abs(D(a)-plus) <= D(math.ulp(a))+ORACLE_REMAINDER
        assert abs(D(b)-minus) <= D(math.ulp(b))+ORACLE_REMAINDER
        assert abs(D(math.cos(x))-cosine) <= D(math.ulp(math.cos(x)))+ORACLE_REMAINDER
        target = (plus-minus)/(2*D(h))
        sine_budget = (D(math.ulp(float(plus)))+D(math.ulp(float(minus)))+2*ORACLE_REMAINDER)/(2*D(h))
        bound = sine_budget+D(math.ulp(approximation))
        assert abs(D(approximation)-target) <= bound, ('derivative outside ULP envelope', h, approximation, str(bound))
        error_bound = D(math.ulp(float(cosine)))+D(math.ulp(error))+ORACLE_REMAINDER
        assert abs(D(error)-abs(D(approximation)-cosine)) <= error_bound, ('inconsistent absolute error', h)
    return float(bound)
