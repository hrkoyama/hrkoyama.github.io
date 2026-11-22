"""Small educational models; numerical solvers do not import reference solvers."""
import numpy as np


def rk4(rhs, initial, end, steps):
    y = np.asarray(initial, dtype=float)
    history = [y.copy()]
    h = end / steps
    for i in range(steps):
        t = i * h
        a = rhs(t, y)
        b = rhs(t + h/2, y + h*a/2)
        c = rhs(t + h/2, y + h*b/2)
        d = rhs(t + h, y + h*c)
        y = y + h*(a + 2*b + 2*c + d)/6
        if not np.isfinite(y).all():
            raise ValueError('Non-finite state')
        history.append(y.copy())
    return np.linspace(0, end, steps+1), np.array(history)


def logistic(p, steps):
    return rk4(lambda t, y: p['rate']*y*(1-y/p['capacity']),
               [p['initial']], p['end'], steps)


def sir(p, steps):
    def rhs(t, y):
        s, i, r = y
        incidence = p['beta']*s*i
        recovery = p['gamma']*i
        return np.array([-incidence, incidence-recovery, recovery])
    return rk4(rhs, p['initial'], p['end'], steps)


def monte_carlo(p):
    # Fresh generators for independent replications; nested prefixes within a seed.
    samples = np.array([np.random.Generator(np.random.PCG64(seed)).uniform(size=max(p['samples']))
                        for seed in p['seeds']])**2
    rows = []
    for n in p['samples']:
        estimates = samples[:, :n].mean(axis=1)
        standard_errors = samples[:, :n].std(axis=1, ddof=1)/np.sqrt(n)
        rows.append((n, estimates, standard_errors))
    return rows


def gbm(p):
    # Aggregate the SAME fine increments for every discretization and exact endpoint.
    finest = max(p['steps'])
    rng = np.random.Generator(np.random.PCG64(p['seed']))
    increments = rng.normal(0, np.sqrt(p['end']/finest), (p['paths'], finest))
    wt = increments.sum(axis=1)
    exact = p['initial']*np.exp((p['mu']-p['sigma']**2/2)*p['end']+p['sigma']*wt)
    rows = []
    for n in p['steps']:
        if finest % n:
            raise ValueError('Nested time steps required')
        dw = increments.reshape(p['paths'], n, finest//n).sum(axis=2)
        numerical = p['initial']*np.prod(1+p['mu']*p['end']/n+p['sigma']*dw, axis=1)
        rows.append((n, numerical, exact))
    return rows
