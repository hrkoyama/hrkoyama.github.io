"""Independent analytic interval targets, not a primary quadrature engine."""
from .interval import Interval, pi_interval, sincos_integer


def I(value, precision):
    return Interval(value, precision=precision)


def sine_integral(omega, endpoint, precision):
    sine, cosine = sincos_integer(omega*endpoint, precision)
    return (omega-I(-endpoint, precision).exp()*(sine+omega*cosine))/(1+omega*omega)


def transformed_endpoints(cutoff, precision):
    t = I(cutoff, precision)
    sinh = (t.exp()-(-t).exp())/2
    z = pi_interval(precision)*sinh
    # x(-T)=1/(1+exp(pi*sinh(T))); x(T)=1-x(-T), as intervals.
    a = 1/(1+z.exp())
    return a, 1-a


def primitive(kind, x, precision):
    if kind == "smooth-exponential":
        return x.exp()
    if kind == "algebraic-inverse-cuberoot":
        return I(3, precision)/2*((2*x.ln()/3).exp())
    if kind == "log-endpoint":
        return x*(1-x.ln())
    raise ValueError("Unknown analytic integrand")


def all_targets(precision, retain=None):
    out = {}

    def add(name, value):
        out[name] = value.record()
        if retain:
            retain(out)

    pi = pi_interval(precision)
    gaussian = pi.sqrt()
    gaussian_tail = I(-36, precision).exp()/6
    add("q78:gaussian-whole-line", gaussian)
    add("q78:gaussian-tail-bound", gaussian_tail)
    add("q78:gaussian-finite", Interval((gaussian-gaussian_tail).lo, gaussian.hi, precision))
    for omega in (40, 120):
        add("q78:finite-sine-"+str(omega), sine_integral(omega, 1, precision))
    add("q78:fourier-half-line", I(8, precision)/65)
    add("q78:fourier-finite", sine_integral(8, 24, precision))
    add("q78:fourier-tail-bound", I(-24, precision).exp()/I(65, precision).sqrt())
    add("q78:internal-root", 2*((I(3, precision)/8).sqrt()+(I(5, precision)/8).sqrt()))
    full = {"smooth-exponential": I(1, precision).exp()-1,
            "algebraic-inverse-cuberoot": I(3, precision)/2,
            "log-endpoint": I(1, precision)}
    for kind, value in full.items():
        add("q79:"+kind, value)
        for cutoff in (3, 4):
            a, b = transformed_endpoints(cutoff, precision)
            window = primitive(kind, b, precision)-primitive(kind, a, precision)
            add("q79:"+kind+":window:"+str(cutoff), window)
            add("q79:"+kind+":continuous-tail:"+str(cutoff), value-window)
    smooth = I(1, precision)
    for dimension, denominator in enumerate((1, 2, 4, 8), 1):
        a = I(1, precision)/denominator
        smooth = smooth*(a.exp()-1)/a
        if dimension >= 2:
            add("q80:smooth-product:"+str(dimension), smooth)
            add("q80:interaction-product:"+str(dimension), (I(1, precision)/12).power(dimension))
    return out
