"""93-real-parameter, two-block Fourier neural operator; native-grid tanh."""
import numpy as np
from scipy.optimize import minimize


def structure(theta, derivatives=False):
    """Parameters in row-major order: lift, two W/b/R blocks, projection."""
    cursor = 0
    def take(shape):
        nonlocal cursor
        count = int(np.prod(shape))
        val = theta[cursor:cursor+count].reshape(shape)
        der = np.zeros(shape+(93,))
        for j in range(count):
            der.reshape(count, 93)[j, cursor+j] = 1
        cursor += count
        return val, der
    lift, dlift = take((2, 2)); lb, dlb = take((2,))
    blocks = []
    for _ in range(2):
        w, dw = take((2, 2)); b, db = take((2,)); dc, ddc = take((2, 2))
        parts, dparts = take((4, 2, 2, 2))
        r = np.concatenate((dc[None].astype(complex),
            parts[..., 0] + 1j*parts[..., 1]), axis=0)
        dr = np.concatenate((ddc[None].astype(complex),
            dparts[..., 0, :] + 1j*dparts[..., 1, :]), axis=0)
        blocks.append((w, b, r, dw, db, dr))
    q, dq = take((2,)); qb, dqb = take((1,))
    if cursor != 93:
        raise ValueError('FNO parameter layout mismatch')
    return lift, lb, blocks, q, qb[0], dlift, dlb, dq, dqb[0]


def forward(theta, inputs, jacobian=False, direct=False):
    lift, lb, blocks, q, qb, dlift, dlb, dq, dqb = structure(theta)
    n = inputs.shape[1]
    # Direct DFT is used only by independent component qualification.
    if direct:
        angle = 2*np.pi*np.arange(n)[:, None]*np.arange(n)[None, :]/n
        matrix = np.cos(angle)-1j*np.sin(angle)
        transform = lambda a: np.einsum('kn,bnc->bkc', matrix[:n//2+1], a, optimize=False)
        def inverse(a):
            full = np.concatenate((a, np.conj(a[:, 1:-1][:, ::-1])), axis=1)
            return np.einsum('nk,bkc->bnc', np.conj(matrix).T, full, optimize=False).real/n
    else:
        transform = lambda a: np.fft.rfft(a, axis=1)
        inverse = lambda a: np.fft.irfft(a, n=n, axis=1)
    v = np.einsum('bni,oi->bno', inputs, lift, optimize=False)+lb
    if jacobian:
        dv = np.einsum('bni,oip->bnop', inputs, dlift, optimize=False)+dlb
    for w, b, r, dw, db, dr in blocks:
        spectrum = transform(v)
        filtered = np.zeros_like(spectrum)
        filtered[:, :5] = np.einsum('koi,bki->bko', r, spectrum[:, :5], optimize=False)
        z = np.einsum('oi,bni->bno', w, v, optimize=False)+inverse(filtered)+b
        if jacobian:
            ds = np.fft.rfft(dv, axis=1)
            df = np.zeros_like(ds)
            df[:, :5] = (np.einsum('koip,bki->bkop', dr, spectrum[:, :5], optimize=False)
                + np.einsum('koi,bkip->bkop', r, ds[:, :5], optimize=False))
            dz = (np.einsum('oip,bni->bnop', dw, v, optimize=False)
                + np.einsum('oi,bnip->bnop', w, dv, optimize=False)
                + np.fft.irfft(df, n=n, axis=1)+db)
        v = np.tanh(z)
        if jacobian:
            dv = (1-v*v)[..., None]*dz
    output = np.einsum('o,bno->bn', q, v, optimize=False)+qb
    if jacobian:
        derivative = (np.einsum('op,bno->bnp', dq, v, optimize=False)
            + np.einsum('o,bnop->bnp', q, dv, optimize=False)+dqb)
        return output, derivative
    return output


def initial(seed):
    return np.random.Generator(np.random.PCG64(seed)).normal(0, .15, 93)


def train(config, inputs, target, trace, budget):
    counts = {'loss_calls': 0, 'gradient_calls': 0, 'returned_final_vectors': 0}
    def fun(theta):
        budget.check()
        if counts['loss_calls'] >= config['max_fun_calls']:
            raise RuntimeError('Actual FNO combined loss/gradient call cap exhausted')
        counts['loss_calls'] += 1; counts['gradient_calls'] += 1
        prediction, derivative = forward(theta, inputs, True)
        error = prediction-target
        loss = float(np.mean(error*error))
        gradient = 2*np.einsum('bn,bnp->p', error, derivative, optimize=False)/error.size
        trace.observe('optimizer', theta=theta, prediction=prediction,
                      gradient=gradient, loss=loss)
        return loss, gradient
    try:
        result = minimize(fun, initial(config['seed']), jac=True, method='L-BFGS-B',
            options={'maxiter': 120, 'maxfun': config['max_fun_calls'], 'maxcor': 5,
                     'maxls': 20, 'ftol': 1e-12, 'gtol': 1e-8})
        counts['returned_final_vectors'] = 1
        trace.observe('returned', theta=result.x, gradient=result.jac,
                      loss=result.fun, status=result.status)
        trace.flush()
        return result, counts
    except BaseException:
        trace.flush()
        raise

