"""Independent explicit neural expressions and direct real heat-series truth."""
import numpy as np


def pinn_second(theta, x):
    # Exponential tanh representation and direct product-rule expression.
    w, b, a, out = theta[:16], theta[16:32], theta[32:48], theta[48]
    result = np.full(np.shape(x), -2*out, dtype=np.result_type(theta, float))
    for j in range(16):
        z = w[j]*x+b[j]
        v = np.exp(2*z)
        t = (v-1)/(v+1)
        d = 4*v/(v+1)**2
        dd = 8*v*(1-v)/(v+1)**3
        result += a[j]*(-2*t + 2*(1-2*x)*w[j]*d + x*(1-x)*w[j]**2*dd)
    return result


def pinn_first(theta, x):
    result = (1-2*x)*theta[48]
    for w, b, a in zip(theta[:16], theta[16:32], theta[32:48]):
        v = np.exp(2*(w*x+b))
        result = result+a*((1-2*x)*(v-1)/(v+1)+x*(1-x)*w*4*v/(v+1)**2)
    return result


def seir_linear(eta, times):
    # Full 2x2 exponential, including BOTH eigenvalues and transient coefficients.
    matrix = np.array([[-.3, .6], [.3, -.2]])
    half_trace = -.25
    delta = np.sqrt((-.3+.2)**2+4*.3*.6)/2
    centered = matrix-half_trace*np.eye(2)
    initial = np.array([eta, eta])
    return np.array([np.exp(half_trace*t)*(np.cosh(delta*t)*initial
        + np.sinh(delta*t)/delta*np.einsum('ij,j->i', centered, initial, optimize=False)) for t in times])


def mm_identity(theta):
    # Monotone scalar root; bracket follows S>=1-theta>=1/2 on this domain.
    from scipy.optimize import brentq
    return np.array([brentq(lambda s: s+.2*np.log(s)-1+t, .25, 1.,
                           xtol=5e-15, rtol=1e-14) for t in theta])

