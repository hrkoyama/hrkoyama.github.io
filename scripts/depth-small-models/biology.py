"""Small mass-action systems; original RK4 and SDIRK2 trajectories."""
import math
import numpy as np


def enzyme(y, total=None):
    s, c, e, p = y
    binding, reverse, catalysis = 10*e*s, c, c
    return np.array([-binding+reverse, binding-reverse-catalysis,
                     -binding+reverse+catalysis, catalysis])


def enzyme_jac(y):
    s, c, e, p = y
    return np.array([[-10*e, 1, -10*s, 0], [10*e, -2, 10*s, 0],
                     [-10*e, 2, -10*s, 0], [0, 1, 0, 0]])


def lv(y):
    x, z = y
    return np.array([x*(1-z), z*(x-1)])


def seir(y):
    s, e, i, r = y
    incidence, progression, recovery = .6*s*i, .3*e, .2*i
    return np.array([-incidence, incidence-progression,
                     progression-recovery, recovery])


def rk4(rhs, initial, end, steps, trace, budget):
    y = np.array(initial, dtype=float, copy=True)
    states = [y.copy()]
    h = end/steps
    for k in range(steps):
        budget.check()
        trace.observe('rk4_before', state=y, index=k)
        a = rhs(y); b = rhs(y+h*a/2); c = rhs(y+h*b/2); d = rhs(y+h*c)
        y = y+h*(a+2*b+2*c+d)/6
        trace.observe('rk4_completed', state=y, index=k+1)
        states.append(y.copy())
        if not np.isfinite(y).all():
            raise FloatingPointError('Nonfinite RK4 candidate retained')
    trace.flush()
    return np.linspace(0, end, steps+1), np.array(states)


def stage(base, hgamma, start, rtol, atol, counts, trace, budget):
    y = start.copy()
    weights = atol+rtol*np.abs(start)
    for iteration in range(11):
        budget.check()
        trace.observe('newton_before', candidate=y, base=base, coefficient=hgamma)
        f = enzyme(y); counts['RHS_calls'] += 1
        residual = y-base-hgamma*f
        trace.observe('newton_residual', candidate=y, residual=residual)
        norm = float(np.max(np.abs(residual)/weights))
        if not np.isfinite(norm):
            raise FloatingPointError('Nonfinite SDIRK Newton residual')
        if norm <= 1e-3:
            return y
        if iteration == 10:
            raise RuntimeError('SDIRK Newton iteration cap')
        jac = enzyme_jac(y); counts['Jacobian_calls'] += 1
        matrix = np.eye(4)-hgamma*jac
        trace.observe('newton_linear', matrix=matrix, residual=residual, candidate=y)
        correction = np.linalg.solve(matrix, residual)
        counts['factor_builds'] += 1; counts['linear_solves'] += 1
        accepted = False
        for backtrack in range(9):
            trial = y-(.5**backtrack)*correction
            trace.observe('newton_trial', candidate=trial, base=base)
            trial_residual = trial-base-hgamma*enzyme(trial)
            counts['RHS_calls'] += 1
            if np.max(np.abs(trial_residual)/weights) <= (1-1e-4*.5**backtrack)*norm:
                y = trial; accepted = True
                counts['Newton_updates'] += 1
                break
            counts['backtracks'] += 1
        if not accepted:
            raise RuntimeError('SDIRK Armijo cap')
    raise AssertionError('Unreachable')


def sdirk_step(y, h, rtol, atol, counts, trace, budget):
    gamma = 1-1/math.sqrt(2)
    first = stage(y, h*gamma, y, rtol, atol, counts, trace, budget)
    f = enzyme(first); counts['RHS_calls'] += 1
    second = stage(y+h*(1-gamma)*f, h*gamma, first, rtol, atol, counts, trace, budget)
    trace.observe('completed_sdirk', first=first, second=second)
    return second


def enzyme_times(total):
    # Exact floating union; no tolerance snapping or extra adapted output times.
    return np.unique(np.concatenate((np.arange(101)/200/total,
                                     np.array([1., 5., 20.])/12)))


def adaptive_enzyme(total, rtol, atol, trace, budget):
    targets = enzyme_times(total)
    y = np.array([1., 0., total, 0.]); t = 0.; h = (1/12)/8
    counts = {k: 0 for k in ['attempted_steps', 'accepted_steps', 'rejected_steps',
        'clipped_output_steps', 'RHS_calls', 'Jacobian_calls', 'factor_builds',
        'linear_solves', 'Newton_updates', 'backtracks']}
    states = [y.copy()]; accepted_times = [t]; accepted_states = [y.copy()]
    trials = []; rejects = 0
    try:
        for target in targets[1:]:
            while t < target:
                budget.check()
                if counts['attempted_steps'] >= 20000:
                    raise RuntimeError('Enzyme attempted-step cap')
                proposed = min(h, .005/total)
                step = min(proposed, target-t)
                if step < proposed:
                    counts['clipped_output_steps'] += 1
                if step <= 0 or t+step == t:
                    raise RuntimeError('Enzyme step underflow')
                counts['attempted_steps'] += 1
                full = sdirk_step(y, step, rtol, atol, counts, trace, budget)
                half = sdirk_step(y, step/2, rtol, atol, counts, trace, budget)
                two = sdirk_step(half, step/2, rtol, atol, counts, trace, budget)
                error = (two-full)/3
                ratio = float(np.max(np.abs(error)/(atol+rtol*np.maximum(np.abs(y), np.abs(two)))))
                trace.observe('step_candidates', previous=y, full=full, two_half=two,
                              error=error, ratio=ratio, time=t, step=step)
                if not np.isfinite(ratio):
                    raise FloatingPointError('Nonfinite enzyme error ratio')
                ok = ratio <= 1
                trials.append((t, step, ratio, int(ok)))
                factor = 2. if ratio == 0 else min(2., max(.2, .8*ratio**(-1/3)))
                if ok:
                    t = target if step == target-t else t+step
                    y = two.copy(); rejects = 0
                    counts['accepted_steps'] += 1
                    accepted_times.append(t); accepted_states.append(y.copy())
                    trace.observe('accepted', state=y, time=t)
                else:
                    counts['rejected_steps'] += 1; rejects += 1
                    factor = min(1., factor)
                    if rejects > 30:
                        raise RuntimeError('Enzyme consecutive rejection cap')
                h = step*factor
            states.append(y.copy())
        trace.flush()
        return targets, np.array(states), np.array(accepted_times), np.array(accepted_states), np.array(trials), counts
    except BaseException:
        trace.flush()
        raise

