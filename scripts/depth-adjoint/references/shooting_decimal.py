"""Independent discrete shooting/fold and separate Decimal Thomas Newton."""
from decimal import Decimal as D, localcontext


def shoot(n, a, lam, audit=None):
    h2 = D(1)/D((n+1)**2)
    u, z, w, y, t = [D(0), a], [D(0), D(1)], [D(0), D(0)], [D(0), D(0)], [D(0), D(0)]
    for i in range(1, n+1):
        if audit is not None:
            audit.update(stage='shoot', n=n, a=a, lam=lam, index=i,
                         u=u[:], z=z[:], w=w[:], y=y[:], t=t[:])
        e = u[i].exp()
        C = 2-h2*lam*e
        u.append(2*u[i]-u[i-1]-h2*lam*e)
        z.append(C*z[i]-z[i-1])
        w.append(C*w[i]-w[i-1]-h2*e)
        y.append(C*y[i]-y[i-1]-h2*lam*e*z[i]*z[i])
        t.append(C*t[i]-t[i-1]-h2*e*z[i]-h2*lam*e*w[i]*z[i])
    return {'u': u, 'z': z, 'w': w, 'y': y, 't': t}


def fold(n, precision=80, audit=None):
    with localcontext() as c:
        c.prec = precision+20
        a, lam = (D('.8'), D(3)) if n == 1 else (D(4)/(n+1), D('3.5'))
        tolerance = D(10)**(-precision+10)
        history = []
        for iteration in range(17):
            out = shoot(n, a, lam, audit)
            R, Ra, Rl, Raa, Ral = (out[key][-1] for key in ('u', 'z', 'w', 'y', 't'))
            current = max(abs(R), abs(Ra))
            det = Ra*Ral-Rl*Raa
            history.append({'a': a, 'lambda': lam, 'R': R, 'Ra': Ra, 'determinant': det})
            if current <= tolerance:
                return {'a': a, 'lambda': lam, 'profile': out['u'], 'R': R, 'Ra': Ra,
                        'determinant': det, 'history': history}
            if iteration == 16 or det == 0:
                break
            da, dl = (-R*Ral+Rl*Ra)/det, (Raa*R-Ra*Ra)/det
            accepted = False
            for j in range(16):
                scale = D(2)**(-j)
                at, lt = a+scale*da, lam+scale*dl
                if not (0 < at < 2 and 2 < lt < 4):
                    continue
                if audit is not None:
                    audit.update(stage='fold-trial', trial_a=at, trial_lambda=lt,
                                 trial_line_index=j, fold_iteration=iteration)
                trial = shoot(n, at, lt, audit)
                if max(abs(trial['u'][-1]), abs(trial['z'][-1])) <= (1-D('.0001')*scale)*current:
                    a, lam, accepted = at, lt, True
                    break
            if not accepted:
                break
        raise ArithmeticError('Independent fold iteration/line search limit: '+str(history[-1]))


def lower_state(n, lam, fold_a, precision=80, audit=None):
    with localcontext() as c:
        c.prec = precision+20
        left, right = D(0), fold_a
        fl, fr = shoot(n, left, lam, audit)['u'][-1], shoot(n, right, lam, audit)['u'][-1]
        if not (fl < 0 < fr):
            raise ArithmeticError('Independent lower shooting bracket failed')
        a = (left+right)/2
        tolerance = D(10)**(-precision+10)
        history = []
        for iteration in range(120):
            out = shoot(n, a, lam, audit)
            value, derivative = out['u'][-1], out['z'][-1]
            history.append({'a': a, 'R': value, 'Ra': derivative})
            if abs(value) <= tolerance:
                da = -out['w'][-1]/derivative
                state = out['u'][1:-1]
                tangent = [out['w'][i]+out['z'][i]*da for i in range(1, n+1)]
                h = D(1)/(n+1)
                gradient = D('.05')*lam+h*sum(x*s for x, s in zip(state, tangent))
                return {'u': state, 'tangent': tangent, 'gradient': gradient,
                        'a': a, 'right_residual': value, 'shooting_derivative': derivative,
                        'history': history}
            if value < 0:
                left = a
            else:
                right = a
            proposed = a-value/derivative if derivative else (left+right)/2
            a = proposed if left < proposed < right else (left+right)/2
        raise ArithmeticError('Independent lower shooting iteration limit')


def thomas(lower, diagonal, upper, rhs):
    diagonal, rhs = diagonal[:], rhs[:]
    for i in range(1, len(rhs)):
        multiplier = lower[i-1]/diagonal[i-1]
        diagonal[i] -= multiplier*upper[i-1]
        rhs[i] -= multiplier*rhs[i-1]
    out = [D(0)]*len(rhs)
    for i in range(len(rhs)-1, -1, -1):
        out[i] = (rhs[i]-(upper[i]*out[i+1] if i+1 < len(rhs) else 0))/diagonal[i]
    return out


def discrete_residual(u, lam):
    scale = D((len(u)+1)**2)
    return [scale*(2*x-(u[i-1] if i else 0)-(u[i+1] if i+1 < len(u) else 0))-lam*x.exp()
            for i, x in enumerate(u)]


def independent_newton(n, lam, precision=80, audit=None):
    with localcontext() as c:
        c.prec = precision+20
        u = [D(0)]*n
        scale = D((n+1)**2)
        tolerance = D(10)**(-precision+10)
        for iteration in range(41):
            if audit is not None:
                audit.update(stage='independent-Thomas-Newton', n=n, lam=lam,
                             iteration=iteration, u=u[:])
            f = discrete_residual(u, lam)
            current = max(abs(x) for x in f)
            if current <= tolerance:
                return u
            if iteration == 40:
                break
            diagonal = [2*scale-lam*x.exp() for x in u]
            step = thomas([-scale]*(n-1), diagonal, [-scale]*(n-1), [-x for x in f])
            accepted = False
            for k in range(20):
                alpha = D(2)**(-k)
                trial = [x+alpha*y for x, y in zip(u, step)]
                if audit is not None:
                    audit.update(stage='independent-Thomas-trial', n=n, lam=lam,
                                 iteration=iteration, trial_line_index=k, trial=trial[:])
                if max(abs(x) for x in discrete_residual(trial, lam)) <= (1-D('.0001')*alpha)*current:
                    u, accepted = trial, True
                    break
            if not accepted:
                break
        raise ArithmeticError('Independent Decimal Thomas Newton limit')


def positive_pivots(u, lam):
    scale = D((len(u)+1)**2)
    previous = None
    for x in u:
        pivot = 2*scale-lam*x.exp()
        if previous is not None:
            pivot -= scale*scale/previous
        if pivot <= 0:
            return False
        previous = pivot
    return True
