"""Fixed main studies; accuracy goals are preserved separately from validation."""
import csv
import json
from pathlib import Path
import numpy as np
import pinn
import fno
import biology
from io_utils import Trace, finite, rms, outcome, summarize


def newcase(ident):
    return {'id': ident, 'passed': False, 'checks': {}, 'records': [], 'metrics': {}}


def optimizer_return_allowed(kind, status, success, nfev, nit, message):
    """Native convergence and normal fixed-budget termination are distinct."""
    if kind == 'PINN':
        return bool(status in [0, 1, 2, 3, 4] and success == (status > 0)
                    and (status != 0 or nfev == 300))
    reason = str(message).upper()
    normal_limit = ('LIMIT' in reason and ('ITERATION' in reason or 'EVALUATION' in reason)
                    and 'ABNORMAL' not in reason and (nit == 120 or nfev == 300))
    return bool((status == 0 and success) or (status == 1 and not success and normal_limit))


def convergence_goal(success):
    return {'measured': int(bool(success)), 'limit': 1, 'comparison': '==',
            'units': 'native optimizer success boolean', 'met': bool(success)}


def csv_records(path, rows):
    keys = sorted(set().union(*(r.keys() for r in rows)))
    with Path(path).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, keys); writer.writeheader(); writer.writerows(rows)


def complete(case, targets, acceptance_sha, output, checkpoint):
    summarize(case, targets, acceptance_sha)
    csv_records(output/(case['id']+'.csv'), case['records'])
    checkpoint()


def pinn_case(config, acceptance, output, budget, case, checkpoint, acceptance_sha):
    goals = {}; curves = {}; evaluation = (np.arange(257)+.5)/257
    for seed in config['seeds']:
        trace = Trace(output, 'pinn-'+str(seed))
        result, counts = pinn.train({'seed': seed, **config['optimizer']}, trace, budget)
        u, ux, uxx = pinn.fields(result.x, evaluation)
        np.savez_compressed(output/f'pinn-{seed}.npz', theta=result.x, x=evaluation,
                            u=u, exact=np.sin(np.pi*evaluation), pde_residual=-uxx-np.pi**2*np.sin(np.pi*evaluation))
        finite(u); finite(uxx); finite(result.x)
        error = float(np.max(np.abs(u-np.sin(np.pi*evaluation))))
        residual = rms((-uxx-np.pi**2*np.sin(np.pi*evaluation))/np.pi**2)
        boundary = float(np.max(np.abs(pinn.fields(result.x, np.array([0., 1.]))[0])))
        np.savez_compressed(output/f'pinn-{seed}.npz', theta=result.x, x=evaluation,
                            u=u, exact=np.sin(np.pi*evaluation), pde_residual=-uxx-np.pi**2*np.sin(np.pi*evaluation))
        row = {'kind': 'PINN', 'seed': seed, 'parameter_count': 49, 'solution_Linf': error,
            'PDE_normalized_RMS': residual, 'boundary_Linf': boundary,
            'training_loss': float(2*result.cost), 'status': int(result.status),
            'optimizer_success': int(result.success), 'nfev': int(result.nfev),
            'njev': int(result.njev), **counts}
        case['records'].append(row); checkpoint()
        case['checks'][f'seed-{seed}:finite-shape'] = bool(u.shape == (257,) and len(result.x) == 49)
        case['checks'][f'seed-{seed}:optimizer-return-status'] = optimizer_return_allowed(
            'PINN', result.status, bool(result.success), result.nfev, 0, result.message)
        goals[f'seed-{seed}:optimizer-converged'] = convergence_goal(result.success)
        case['checks'][f'seed-{seed}:actual-work'] = counts['fun_calls'] == result.nfev and counts['jac_calls'] == result.njev
        for name, value in [('solution_Linf', error), ('PDE_normalized_RMS', residual), ('boundary_Linf', boundary)]:
            goals[f'seed-{seed}:{name}'] = outcome(value, acceptance['pinn'][name])
    for n in config['fd_nodes']:
        x = np.arange(1, n+1)/(n+1); b = np.pi**2*np.sin(np.pi*x)/(n+1)**2
        diag = np.full(n, 2.); right = b.copy()
        for j in range(1, n):
            factor = -1/diag[j-1]; diag[j] += factor; right[j] -= factor*right[j-1]
        u = np.zeros(n); u[-1] = right[-1]/diag[-1]
        for j in range(n-2, -1, -1):
            u[j] = (right[j]+u[j+1])/diag[j]
        raw = (2*u-np.r_[0, u[:-1]]-np.r_[u[1:], 0])*(n+1)**2-np.pi**2*np.sin(np.pi*x)
        np.savez_compressed(output/f'fd-{n}.npz', x=x, u=u, exact=np.sin(np.pi*x), residual=raw)
        error = float(np.max(np.abs(u-np.sin(np.pi*x))))
        case['records'].append({'kind': 'FD2', 'nodes': n, 'solution_Linf': error,
                              'true_linear_residual': float(np.max(np.abs(raw)))})
        case['checks'][f'fd-{n}:true-residual'] = bool(np.max(np.abs(raw)) <= 1e-9)
        goals[f'fd-{n}:solution_Linf'] = outcome(error, acceptance['fd'][str(n)])
        checkpoint()
    case['metrics'] = {'training_seeds': len(config['seeds']), 'parameters': 49,
        'independent_grid_points': 257, 'FD_runs': 3}
    complete(case, goals, acceptance_sha, output, checkpoint)


def fno_case(config, acceptance, cache, output, budget, case, checkpoint, acceptance_sha):
    data = json.loads((cache/'heat-problems.json').read_text())
    archive = np.load(cache/'heat-data.npz', allow_pickle=False)
    train = [p for p in data if p['split'] == 'train']
    features = np.array([archive[f'i{p["id"]}_32'] for p in train])
    target = np.array([archive[f'y{p["id"]}_32'] for p in train])
    goals = {}; evaluations = []
    for seed in config['seeds']:
        trace = Trace(output, 'fno-'+str(seed))
        result, counts = fno.train({'seed': seed, **config['optimizer']}, features, target, trace, budget)
        np.savez_compressed(output/f'fno-{seed}-parameters.npz', theta=result.x, gradient=result.jac)
        case['records'].append({'seed': seed, 'parameters': 93, 'loss': float(result.fun),
            'status': int(result.status), 'optimizer_success': int(result.success),
            'iterations': int(result.nit), 'nfev': int(result.nfev), 'njev': int(result.njev), **counts})
        checkpoint()
        errors = {32: [], 64: []}; saved = {}
        for problem in data:
            grids = [32, 64] if problem['split'] == 'test' else [32 if problem['split'] in ['train', 'validation'] else 64]
            predictions = {}
            for n in grids:
                budget.check(); inp = archive[f'i{problem["id"]}_{n}']; exact = archive[f'y{problem["id"]}_{n}']
                u = fno.forward(result.x, inp[None])[0]
                np.savez_compressed(output/f'fno-{seed}-{problem["id"]}-{n}.npz',
                                    u=u, reference=exact, inputs=inp)
                finite(u)
                predictions[n] = u
                norm = rms(exact); absolute = rms(u-exact)
                applicable = norm > config['relative_norm_cutoff']
                relative = absolute/norm if applicable else ''
                evaluations.append({'seed': seed, 'problem_id': problem['id'], 'split': problem['split'],
                    'N': n, 'absolute_RMS': absolute, 'relative_L2': relative,
                    'relative_applicable': int(applicable), 'Linf': float(np.max(np.abs(u-exact)))})
                csv_records(output/'fno-evaluations.csv', evaluations)
                if problem['split'] == 'test':
                    errors[n].append(relative)
                if problem['id'] in [850300, 850400, 850500]:
                    saved[f'u{problem["id"]}_{n}'] = u; saved[f'y{problem["id"]}_{n}'] = exact
            if len(predictions) == 2:
                evaluations[-1]['restriction_discrepancy_RMS'] = rms(predictions[64][::2]-predictions[32])
        zero_errors = []
        for kind, scale in [('zero', 0.), ('near-zero', 1e-14)]:
            for n in [32, 64]:
                inp = archive[f'i850300_{n}'].copy(); inp[:, 0] *= scale; inp[:, 1] = .1
                exact = archive[f'y850300_{n}']*scale
                # Problem850300 has nu=.05: replace the nearzero truth by its
                # own qualified initial shape's nu=.1 output saved in the cache.
                exact = archive[f'norm_{kind}_{n}']
                u = fno.forward(result.x, inp[None])[0]
                np.savez_compressed(output/f'fno-{seed}-{kind}-{n}.npz', u=u, reference=exact, inputs=inp)
                finite(u)
                applicable = rms(exact) > config['relative_norm_cutoff']
                evaluations.append({'seed': seed, 'problem_id': kind, 'split': 'norm-control',
                    'N': n, 'absolute_RMS': rms(u-exact), 'relative_L2': '',
                    'relative_applicable': int(applicable), 'Linf': float(np.max(np.abs(u-exact)))})
                csv_records(output/'fno-evaluations.csv', evaluations)
                zero_errors.append(rms(u-exact))
                if applicable:
                    raise AssertionError('Known zero/nearzero must have relative NA')
        np.savez_compressed(output/f'fno-{seed}-profiles.npz', **saved)
        case['checks'][f'seed-{seed}:finite-parameters'] = bool(len(result.x) == 93 and np.isfinite(result.x).all())
        case['checks'][f'seed-{seed}:optimizer-return-status'] = optimizer_return_allowed(
            'FNO', result.status, bool(result.success), result.nfev, result.nit, result.message)
        goals[f'seed-{seed}:optimizer-converged'] = convergence_goal(result.success)
        case['checks'][f'seed-{seed}:actual-work'] = bool(counts['loss_calls'] == result.nfev == counts['gradient_calls'])
        case['checks'][f'seed-{seed}:relative-NA'] = all(r['relative_L2'] == '' for r in evaluations if r['seed'] == seed and r['split'] == 'norm-control')
        goals[f'seed-{seed}:ID-N32-relative'] = outcome(max(errors[32]), acceptance['fno']['ID_relative'])
        goals[f'seed-{seed}:ID-N64-relative'] = outcome(max(errors[64]), acceptance['fno']['N64_relative'])
        goals[f'seed-{seed}:norm-control-absolute'] = outcome(max(zero_errors), acceptance['fno']['zero_absolute_RMS'])
    csv_records(output/'fno-evaluations.csv', evaluations)
    case['checks']['disjoint-whole-problem-IDs'] = len({p['id'] for p in data}) == 46
    case['metrics'] = {'models': 2, 'parameters_per_model': 93, 'whole_problem_IDs': 46,
        'prediction_rows': len(evaluations), 'nonlinear_dealiasing': 'none',
        'restriction_discrepancy_scope': 'Native-grid nonlinear/alias sensitivity, not continuum error'}
    complete(case, goals, acceptance_sha, output, checkpoint)


def lookup(t, reference_t, reference_y):
    index = np.searchsorted(reference_t, t)
    if np.any(index >= len(reference_t)) or np.max(np.abs(reference_t[index]-t)) > 2e-14:
        raise ValueError('Requested times are not in the qualified finite cache')
    return reference_y[:, index].T


def biology_case(ident, config, acceptance, cache, output, budget, case, checkpoint, acceptance_sha):
    goals = {}
    if ident == 'enzyme-qssa':
        for total, label in [(.01, '01'), (.002, '002')]:
            ref = np.load(cache/f'enzyme-{label}-qualified.npz', allow_pickle=False)
            for rtol, atol in [(1e-6, 1e-10), (1e-8, 1e-12)]:
                rid = f'enzyme-{label}-r{rtol:g}'; trace = Trace(output, rid)
                t, y, ta, ya, trials, counts = biology.adaptive_enzyme(total, rtol, atol, trace, budget)
                np.savez_compressed(output/(rid+'.npz'), t=t, y=y, accepted_t=ta,
                    accepted_y=ya, trials=trials, reference=ref['y'].T, mm=ref['mm'])
                finite(y); error = float(np.max(np.abs(y-ref['y'].T)))
                mass = max(float(np.max(np.abs(ya[:, 1]+ya[:, 2]-total))), float(np.max(np.abs(ya[:, 0]+ya[:, 1]+ya[:, 3]-1))))
                window = t*total >= .02
                model_error = float(np.max(np.abs(ref['y'][0, window]-ref['mm'][window])))
                case['records'].append({'id': rid, 'Etotal': total, 'epsilon': total/1.2,
                    'rtol': rtol, 'atol': atol, 'integration_Linf': error,
                    'conservation_defect': mass, 'QSSA_window_model_error': model_error,
                    'QSSA_full_model_error': float(np.max(np.abs(ref['y'][0]-ref['mm']))),
                    'minimum_accepted': float(ya.min()), **counts})
                checkpoint()
                case['checks'][rid+':completed-work'] = counts['accepted_steps']+counts['rejected_steps'] == counts['attempted_steps']
                case['checks'][rid+':finite'] = bool(np.isfinite(y).all() and np.isfinite(trials).all())
                goals[rid+':integration'] = outcome(error, acceptance['biology']['state_Linf'])
                goals[rid+':mass'] = outcome(mass, acceptance['biology']['conservation'])
                goals[rid+':negative-part'] = outcome(max(0., -float(ya.min())), acceptance['biology']['negative_allowance'])
                goals[rid+':QSSA-model'] = outcome(model_error, acceptance['biology']['QSSA_free_S'])
        for n in [200, 400]:
            ref = np.load(cache/f'mm-{n}-qualified.npz', allow_pickle=False)
            t, y = biology.rk4(lambda z: -z/(.2+z), [1.], .5, n, Trace(output, f'mm-{n}'), budget)
            np.savez_compressed(output/f'mm-{n}.npz', t=t, y=y, reference=ref['y'])
            case['records'].append({'id': f'mm-{n}', 'steps': n, 'reduced_scalar_error': float(np.max(np.abs(y[:, 0]-ref['y'])))})
            case['checks'][f'mm-{n}:finite'] = bool(np.isfinite(y).all()); checkpoint()
    elif ident == 'lotka-volterra':
        ref = np.load(cache/'lv-qualified.npz', allow_pickle=False)
        for n in [400, 800, 1600]:
            rid = f'lv-{n}'; t, y = biology.rk4(biology.lv, [1.2, .8], 20., n, Trace(output, rid), budget)
            np.savez_compressed(output/(rid+'.npz'), t=t, y=y)
            finite(y)
            if np.min(y) <= 0:
                raise ValueError('Nonpositive LV state retained before logarithm')
            exact = lookup(t, ref['t'], ref['y'])
            invariant = np.sum(y-np.log(y), axis=1)
            drift = float(np.max(np.abs(invariant-invariant[0])))
            error = float(np.max(np.abs(y-exact)))
            np.savez_compressed(output/(rid+'.npz'), t=t, y=y, reference=exact, invariant=invariant)
            case['records'].append({'id': rid, 'steps': n, 'state_Linf': error, 'invariant_drift': drift, 'minimum_state': float(y.min())})
            case['checks'][rid+':actual-grid-finite'] = bool(len(t) == n+1 and np.isfinite(y).all()); checkpoint()
            goals[rid+':state'] = outcome(error, acceptance['biology']['state_Linf'])
            goals[rid+':invariant'] = outcome(drift, acceptance['biology']['LV_invariant'])
    else:
        for label, eta in [('1e-4', 1e-4), ('5e-5', 5e-5)]:
            ref = np.load(cache/f'seir-{label}-qualified.npz', allow_pickle=False)
            early = ref['t'] <= 1.
            model_error = float(np.max(np.abs(ref['y'][1:3, early]-ref['linear'][:, early])))
            for n in [400, 800, 1600]:
                rid = f'seir-{label}-{n}'
                t, y = biology.rk4(biology.seir, [1-2*eta, eta, eta, 0.], 20., n, Trace(output, rid), budget)
                np.savez_compressed(output/(rid+'.npz'), t=t, y=y)
                finite(y); exact = lookup(t, ref['t'], ref['y']); linear = lookup(t, ref['t'], ref['linear'])
                error = float(np.max(np.abs(y-exact))); mass = float(np.max(np.abs(y.sum(axis=1)-1)))
                np.savez_compressed(output/(rid+'.npz'), t=t, y=y, reference=exact, linear=linear,
                    early_t=ref['t'][early], early_reference=ref['y'][:, early].T, early_linear=ref['linear'][:, early].T)
                case['records'].append({'id': rid, 'eta': eta, 'steps': n, 'state_Linf': error,
                    'mass_defect': mass, 'minimum_state': float(y.min()),
                    'early_model_deviation': model_error, 'early_deviation_over_eta_squared': model_error/(eta*eta)})
                case['checks'][rid+':actual-grid-finite'] = bool(len(t) == n+1 and np.isfinite(y).all()); checkpoint()
                goals[rid+':integration'] = outcome(error, acceptance['biology']['state_Linf'])
                goals[rid+':mass'] = outcome(mass, acceptance['biology']['conservation'])
                goals[rid+':negative-part'] = outcome(max(0., -float(y.min())), acceptance['biology']['negative_allowance'])
            goals[f'seir-{label}:early-linearization'] = outcome(model_error/eta, acceptance['biology']['SEIR_early_relative'])
    case['metrics'] = {'actual_primary_records': len(case['records']),
        'reference_role': 'Qualified Radau/BDF full ODE; reduction/linearization errors are distinct modeling diagnostics'}
    complete(case, goals, acceptance_sha, output, checkpoint)

