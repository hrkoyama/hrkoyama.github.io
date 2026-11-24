"""One-hidden-layer 49-real-parameter Poisson PINN; no training oracle import."""
import numpy as np
from scipy.optimize import least_squares


def unpack(theta):
    return theta[:16], theta[16:32], theta[32:48], theta[48]


def initial(seed):
    rng = np.random.Generator(np.random.PCG64(seed))
    return np.concatenate((rng.normal(0, 1, 16), rng.normal(0, .5, 16),
                           rng.normal(0, .25, 16), [0.]))


def fields(theta, x, jacobian=False):
    w, b, a, out = unpack(np.asarray(theta))
    x = np.asarray(x)
    xx = x[:, None]
    t = np.tanh(xx * w + b)
    t1 = 1 - t*t
    t2 = -2*t*t1
    t3 = -2*t1*(1-3*t*t)
    g, gp = x*(1-x), 1-2*x
    net = np.sum(a*t, axis=1) + out
    first = np.sum(a*w*t1, axis=1)
    second = np.sum(a*w*w*t2, axis=1)
    u = g*net
    ux = gp*net + g*first
    uxx = -2*net + 2*gp*first + g*second
    if not jacobian:
        return u, ux, uxx
    da = -2*t + 2*gp[:, None]*w*t1 + g[:, None]*w*w*t2
    db = a*(-2*t1 + 2*gp[:, None]*w*t2 + g[:, None]*w*w*t3)
    dw = a*(-2*t1*xx + 2*gp[:, None]*(t1+w*t2*xx)
            + g[:, None]*(2*w*t2+w*w*t3*xx))
    return u, ux, uxx, np.concatenate((dw, db, da,
        -2*np.ones((len(x), 1), dtype=uxx.dtype)), axis=1)


def residual(theta, x, jacobian=False):
    result = fields(theta, x, jacobian)
    r = (-result[2] - np.pi**2*np.sin(np.pi*x))/np.pi**2
    return (r, -result[3]/np.pi**2) if jacobian else r


def train(config, trace, budget):
    x = np.arange(1, 65)/65
    counters = {'fun_calls': 0, 'jac_calls': 0, 'returned_final_parameter_vectors': 0}
    def fun(theta):
        budget.check()
        if counters['fun_calls'] >= config['max_fun_calls']:
            raise RuntimeError('Actual PINN residual call cap exhausted')
        counters['fun_calls'] += 1
        r = residual(theta, x)
        trace.observe('optimizer_fun', theta=theta, residual=r)
        return r/8
    def jac(theta):
        budget.check()
        if counters['jac_calls'] >= config['max_jac_calls']:
            raise RuntimeError('Actual PINN Jacobian call cap exhausted')
        counters['jac_calls'] += 1
        r, j = residual(theta, x, True)
        trace.observe('optimizer_jac', theta=theta, residual=r, jacobian=j)
        return j/8
    try:
        result = least_squares(fun, initial(config['seed']), jac=jac, method='trf',
            x_scale=1., ftol=1e-10, xtol=1e-10, gtol=1e-10,
            max_nfev=config['max_fun_calls'])
        counters['returned_final_parameter_vectors'] = 1
        trace.observe('returned', theta=result.x, residual=result.fun,
                      gradient=result.grad, status=result.status)
        trace.flush()
        return result, counters
    except BaseException:
        trace.flush()
        raise

