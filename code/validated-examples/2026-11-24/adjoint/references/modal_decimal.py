"""Independent scalar high-precision modes; no primary operator imports."""
from decimal import Decimal as D, localcontext


def binary(value):
    return D.from_float(float(value))


def pi(precision):
    with localcontext() as c:
        c.prec = precision+20
        def atan_inverse(integer):
            x = D(1)/integer
            power, total = x, D(0)
            for k in range(200):
                total += power/D(2*k+1) if k % 2 == 0 else -power/D(2*k+1)
                power *= x*x
            return total
        value = 16*atan_inverse(5)-4*atan_inverse(239)
        c.prec = precision
        return +value


def sine(value, audit=None):
    # Fixed bounded Taylor series; tail criterion is truncation, not all rounding.
    term, total = value, value
    for k in range(1, 300):
        term *= -value*value/D((2*k)*(2*k+1))
        total += term
        if k > 8 and abs(term) < D('1e-95'):
            next_term = abs(term*value*value/D((2*k+2)*(2*k+3)))
            decreasing_ratio = abs(value*value/D((2*k+2)*(2*k+3)))
            if decreasing_ratio >= 1:
                raise ArithmeticError('Sine alternating tail not yet decreasing')
            if audit is not None:
                audit.append({'argument': value, 'last_index': k, 'next_term_bound': next_term,
                              'future_ratio_bound': decreasing_ratio})
            return total
    raise ArithmeticError('Independent sine series limit')


def pi_remainder():
    # Each alternating atan tail is bounded by its first omitted term.
    return 16/(D(401)*D(5)**401)+4/(D(401)*D(239)**401)


def expm1_series(value):
    """Independent factorial series for exp(x)-1, with absolute tail bound."""
    term, total = value, value
    for k in range(1, 300):
        next_term = term*value/D(k+1)
        ratio = abs(value)/D(k+2)
        if ratio < 1 and abs(next_term)/(1-ratio) <= D('1e-95'):
            return total, {'terms': k, 'remainder_bound': abs(next_term)/(1-ratio), 'argument': value}
        term = next_term; total += term
    raise ArithmeticError('Independent expm1 series limit')


def modes(n, steps, kappa, theta, T, precision=80):
    with localcontext() as context:
        context.prec = precision+20
        p = pi(precision+10)
        tails = []
        h = D(1)/(n+1)
        kappa, theta = binary(kappa), binary(theta)
        dt, duration = binary(float(T)/steps), binary(T)
        eigenvalues = [4*sine(D(l)*p*h/2, tails)**2/(h*h) for l in (1, 2, 3)]
        initial, beta, target = [D(1), binary(.2), D(0)], [D(1), D(0), binary(-.1)], [D('.5'), D(0), D(0)]
        a, sk, st = initial[:], [D(0)]*3, [D(0)]*3
        history = [a[:]]
        for _ in range(steps):
            nxt, nk, nt = [], [], []
            for j, lam in enumerate(eigenvalues):
                B = 1+dt*kappa*lam
                value = (a[j]+dt*theta*beta[j])/B
                nxt.append(value)
                nk.append((sk[j]-dt*lam*value)/B)
                nt.append((st[j]+dt*beta[j])/B)
            a, sk, st = nxt, nk, nt
            history.append(a[:])
        objective = sum((a[j]-target[j])**2 for j in range(3))/4 + D('.005')*kappa*kappa+D('.01')*theta*theta
        gradient = [sum((a[j]-target[j])*sk[j] for j in range(3))/2+D('.01')*kappa,
                    sum((a[j]-target[j])*st[j] for j in range(3))/2+D('.02')*theta]
        closed, closed_k, closed_t, exact, exact_series, series_tails = [], [], [], [], [], []
        for j, lam in enumerate(eigenvalues):
            q = kappa*lam
            r = 1/(1+dt*q)
            power = r**steps
            value = power*initial[j]+theta*beta[j]*(1-power)/q
            Rq = -D(steps)*dt*r**(steps+1)
            closed.append(value)
            closed_k.append(lam*(Rq*(initial[j]-theta*beta[j]/q)-theta*beta[j]*(1-power)/(q*q)))
            closed_t.append(beta[j]*(1-power)/q)
            exponential = (-q*duration).exp()
            exact.append(initial[j]*exponential+theta*beta[j]*(1-exponential)/q)
            em1, tail = expm1_series(-q*duration)
            exact_series.append(initial[j]*(1+em1)-theta*beta[j]*em1/q)
            series_tails.append(tail)
        closed_gradient = [sum((closed[j]-target[j])*closed_k[j] for j in range(3))/2+D('.01')*kappa,
                           sum((closed[j]-target[j])*closed_t[j] for j in range(3))/2+D('.02')*theta]
        basis = [[sine(D(l)*p*D(i)*h, tails) for l in (1, 2, 3)] for i in range(1, n+1)]
        field = [sum(basis[i][j]*a[j] for j in range(3)) for i in range(n)]
        exact_field = [sum(basis[i][j]*exact[j] for j in range(3)) for i in range(n)]
        return {'n': n, 'steps': steps, 'eigenvalues': eigenvalues, 'basis': basis,
                'coefficients': history, 'field': field, 'time_exact_field': exact_field,
                'objective': objective, 'gradient': gradient, 'closed': closed,
                'closed_gradient': closed_gradient, 'time_exact_coefficients': exact,
                'time_exact_series_coefficients': exact_series, 'expm1_series_tails': series_tails,
                'sine_tails': tails, 'pi_alternating_remainder_bound': pi_remainder(),
                'tail_scope': 'Analytic truncation bounds; Decimal rounding is separately checked by precision refinement,not interval-certified.'}


def strings(value):
    if isinstance(value, D):
        return str(value)
    if isinstance(value, dict):
        return {k: strings(v) for k, v in value.items()}
    if isinstance(value, list):
        return [strings(v) for v in value]
    return value
