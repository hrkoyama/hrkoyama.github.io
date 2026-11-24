"""Near-discrete-fold sensitivity with fixed requested-target diagnostics."""
import numpy as np
from operators import dot, norm, residual, jac_action
from newton import state, derivative
from io_contract import save_npz
from references.linear_oracle import bratu, solve, smallest


def objective(u, lam):
    return .5*dot(u, u)/(len(u)+1)+.025*lam*lam


def identity(u, lam, b, q, direct_s, direct_p, s, p):
    """Finite direct references: retain BOTH their nonzero residuals."""
    J = lambda v: jac_action(u, lam, v)
    rd, rpd = b-J(direct_s), q-J(direct_p)
    r, rp = b-J(s), q-J(p)
    es, ep = direct_s-s, direct_p-p
    lhs = dot(q, es)-dot(direct_p, r)
    correction = -dot(direct_p, rd)+dot(rpd, es)
    adj_lhs = dot(b, ep)-dot(direct_s, rp)
    adj_correction = -dot(direct_s, rpd)+dot(rd, ep)
    approximate_lhs = dot(q, es)-dot(p, r)
    cross_correction = -dot(p, rd)+dot(rp, es)
    scale = max(1., abs(dot(q, es)), abs(dot(direct_p, r)), abs(correction),
                abs(dot(b, ep)), abs(dot(direct_s, rp)))
    bound = abs(dot(direct_p, r))+abs(dot(direct_p, rd))+abs(dot(rpd, es))
    return {'tangent_defect': abs(lhs-correction),
            'adjoint_defect': abs(adj_lhs-adj_correction),
            'approximate_cross_defect': abs(approximate_lhs-cross_correction),
            'scale': scale, 'tangent_error': abs(dot(q, es)), 'finite_reference_bound': bound,
            'direct_tangent_residual': norm(rd), 'direct_adjoint_residual': norm(rpd),
            'approximate_adjoint_cross_term': dot(rp, es)}


def record(n, lam, settings, cfg, partial, raw_path):
    arrays = {'lambda': np.array(lam)}
    states = []
    for tag, tolerance in zip(['loose', 'strict'], cfg['state_tolerances']):
        out = state(n, lam, tolerance, settings, partial)
        arrays['state_'+tag] = out['u'].copy(); states.append(out)
        save_npz(raw_path, arrays)
    u = arrays['state_strict']; b, q = np.exp(u), u/(n+1)
    linear = []
    for j, rtol in enumerate(cfg['linear_rtol']):
        tangent = derivative(u, lam, b, rtol, settings, partial)
        arrays[f'tangent_{j}'] = tangent['x']; arrays[f'tangent_history_{j}'] = tangent['residuals']
        save_npz(raw_path, arrays)
        adjoint = derivative(u, lam, q, rtol, settings, partial)
        arrays[f'adjoint_{j}'] = adjoint['x']; arrays[f'adjoint_history_{j}'] = adjoint['residuals']
        save_npz(raw_path, arrays)
        linear.append({'tangent': tangent, 'adjoint': adjoint})
    # Independent direct/condition diagnostics only after completed candidates saved.
    diag, lower, upper = bratu(u, lam)
    sd = solve(diag, lower, upper, b)
    arrays['direct_tangent'] = sd
    save_npz(raw_path, arrays)
    pd = solve(diag, lower, upper, q, True)
    arrays['direct_adjoint'] = pd
    save_npz(raw_path, arrays)
    sigma, minimum = smallest(u, lam)
    identities = [identity(u, lam, b, q, sd, pd, item['tangent']['x'], item['adjoint']['x']) for item in linear]
    fd, fd_states = [], []
    for step in cfg['FD_steps']:
        pair = []
        for sign in [-1, 1]:
            candidate = state(n, lam+sign*step, cfg['FD_state_tolerance'], settings, partial)
            pair.append(candidate)
            arrays[f'FD_{len(fd)}_{"minus" if sign < 0 else "plus"}'] = candidate['u']
            save_npz(raw_path, arrays)
        value = (objective(pair[1]['u'], lam+step)-objective(pair[0]['u'], lam-step))/(2*step)
        fd.append({'step': step, 'derivative': value, 'residual_minus': pair[0]['residual'],
                   'residual_plus': pair[1]['residual']})
        fd_states.extend(pair)
    # Loose-state derivative isolates state error from the strict-state linear tolerance study.
    dl, ll, ul = bratu(states[0]['u'], lam)
    loose_p = solve(dl, ll, ul, states[0]['u']/(n+1), True)
    loose_gradient = .05*lam+dot(loose_p, np.exp(states[0]['u']))
    arrays['loose_direct_adjoint'] = loose_p
    save_npz(raw_path, arrays)
    return {'arrays': arrays, 'states': states, 'linear': linear, 'FD': fd,
            'FD_states': fd_states, 'sigma_estimate': sigma, 'minimum_eigenvalue': minimum,
            'identities': identities, 'direct_gradient_tangent': .05*lam+dot(q, sd),
            'direct_gradient_adjoint': .05*lam+dot(pd, b),
            'gradient': .05*lam+dot(linear[-1]['adjoint']['x'], b),
            'loose_direct_gradient': loose_gradient}
