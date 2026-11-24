"""Small directed Decimal intervals for fixed independent scalar references.

No primary quadrature is imported. Decimal transcendental outputs are rounded
to nearest; one adjacent decimal on each side encloses the rounded result.
Interval arithmetic, not an 80/120 comparison, supplies the enclosure.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from functools import lru_cache
from math import factorial


class Interval:
    def __init__(self, lo, hi=None, precision=80):
        self.lo = Decimal(lo)
        self.hi = self.lo if hi is None else Decimal(hi)
        self.precision = precision
        if not (self.lo.is_finite() and self.hi.is_finite() and self.lo <= self.hi):
            raise ValueError("Invalid finite interval")

    def coerce(self, value):
        return value if isinstance(value, Interval) else Interval(value, precision=self.precision)

    def directed(self, function, rounding):
        with localcontext() as context:
            context.prec = self.precision
            context.rounding = rounding
            return function()

    def __add__(self, other):
        other = self.coerce(other)
        return Interval(self.directed(lambda: self.lo + other.lo, ROUND_FLOOR),
                        self.directed(lambda: self.hi + other.hi, ROUND_CEILING),
                        self.precision)

    __radd__ = __add__

    def __neg__(self):
        # Decimal unary minus is context-sensitive; copy_negate is exact.
        return Interval(self.hi.copy_negate(), self.lo.copy_negate(), self.precision)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        pairs = [(a, b) for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        low = min(self.directed(lambda a=a, b=b: a*b, ROUND_FLOOR) for a, b in pairs)
        high = max(self.directed(lambda a=a, b=b: a*b, ROUND_CEILING) for a, b in pairs)
        return Interval(low, high, self.precision)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        if other.lo <= 0 <= other.hi:
            raise ValueError("Interval division by zero")
        inverse = Interval(self.directed(lambda: Decimal(1)/other.hi, ROUND_FLOOR),
                           self.directed(lambda: Decimal(1)/other.lo, ROUND_CEILING),
                           self.precision)
        return self * inverse

    def __rtruediv__(self, other):
        return self.coerce(other) / self

    def power(self, integer):
        if not isinstance(integer, int) or integer < 0:
            raise ValueError("Nonnegative integer power required")
        out = self.coerce(1)
        for _ in range(integer):
            out = out * self
        return out

    def monotone(self, name):
        if name in ("ln", "sqrt") and (self.lo < 0 or (name == "ln" and self.lo == 0)):
            raise ValueError("Invalid elementary-function domain")
        with localcontext() as context:
            context.prec = self.precision
            context.rounding = ROUND_HALF_EVEN
            low = getattr(self.lo, name)().next_minus(context)
            high = getattr(self.hi, name)().next_plus(context)
        return Interval(low, high, self.precision)

    def exp(self):
        return self.monotone("exp")

    def ln(self):
        return self.monotone("ln")

    def sqrt(self):
        return self.monotone("sqrt")

    def widen(self, radius):
        radius = self.coerce(radius)
        return self + Interval(radius.hi.copy_negate(), radius.hi, self.precision)

    def record(self):
        return {"lower": str(self.lo), "upper": str(self.hi), "precision": self.precision}


def atan_small(denominator, precision):
    """128 alternating terms; next term bounds the remainder for 1/d<1."""
    x = Interval(1, precision=precision) / denominator
    total = Interval(0, precision=precision)
    term = x
    square = x*x
    for k in range(128):
        total = total + term/(2*k+1) if k % 2 == 0 else total - term/(2*k+1)
        term = term*square
    return total.widen(term/257)


@lru_cache(maxsize=2)
def pi_interval(precision):
    # tan(4 atan(1/5)-atan(1/239))=1; angle lies in (0, pi/2).
    return 16*atan_small(5, precision)-4*atan_small(239, precision)


def sincos_integer(argument, precision):
    """Finite integer-radian arguments; reduction uncertainty stays in interval."""
    x = Interval(argument, precision=precision)
    pi = pi_interval(precision)
    with localcontext() as context:
        context.prec = precision
        context.rounding = ROUND_HALF_EVEN
        turns = int((Decimal(argument)/((pi.lo+pi.hi))).to_integral_value())
    reduced = x - 2*turns*pi
    if max(reduced.lo.copy_abs(), reduced.hi.copy_abs()) > pi.hi:
        raise ValueError("Unqualified trigonometric range reduction")
    sine = Interval(0, precision=precision)
    cosine = Interval(0, precision=precision)
    sine_term, cosine_term = reduced, Interval(1, precision=precision)
    square = reduced*reduced
    for k in range(80):
        sine = sine+sine_term if k % 2 == 0 else sine-sine_term
        cosine = cosine+cosine_term if k % 2 == 0 else cosine-cosine_term
        sine_term = sine_term*square/((2*k+2)*(2*k+3))
        cosine_term = cosine_term*square/((2*k+1)*(2*k+2))
    # Taylor's real Lagrange remainder uses |sin|,|cos|<=1.
    radius_s = Interval(pi.hi, precision=precision).power(161)/factorial(161)
    radius_c = Interval(pi.hi, precision=precision).power(160)/factorial(160)
    return sine.widen(radius_s), cosine.widen(radius_c)
