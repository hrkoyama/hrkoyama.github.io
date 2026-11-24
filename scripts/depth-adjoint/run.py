"""Fixed three-case runner. CLI accepts --input and fresh --output."""
import argparse
import json
from pathlib import Path
import signal
import shutil
import time
import numpy as np
from operators import norm, hnorm, dot
from io_contract import (fresh_directory, save_json, save_npz, finite_csv,
                         qualified_cache, digest, add, native)
import time_adjoint as time_case
import fold_study
import distributed
from references.linear_oracle import full_sensitivity, bratu, smallest

SOURCE = Path(__file__).resolve().parent
CASE_IDS = ['diffusion-discrete-adjoint', 'bratu-fold-sensitivity', 'bratu-distributed-vjp']


def status(item):
    return {k: v for k, v in item.items() if k not in ['x', 'residuals']}


def finite_arrays(arrays):
    return all(np.isfinite(a).all() for a in arrays.values())


def diffusion(case, cfg, limits, output, flush):
    checks, records = case['checks'], case['records']
    rows, errors = [], {}
    for n in cfg['n']:
        for N in cfg['steps']:
            key = f'n{n}-N{N}'; work = output/key
            # Separate ownership windows. Full arrays do not escape full_window.
            full = time_case.full_window(n, N, cfg['kappa'], cfg['theta'], cfg['T'], work)
            replay = time_case.checkpoint_window(n, N, cfg['kappa'], cfg['theta'], cfg['T'], cfg['checkpoint_block'], work)
            # Validation loads/NPZ assembly explicitly outside both measured windows.
            states = np.load(work/'full-states.npy', allow_pickle=False)
            tangent = time_case.tangent(n, N, cfg['kappa'], cfg['theta'], cfg['T'], output/(key+'-tangent-partial.npz'))
            save_npz(output/(key+'.npz'), states=states, tangent_kappa=tangent['sk'],
                     tangent_theta=tangent['st'], adjoint_gradient=full['gradient'],
                     tangent_gradient=tangent['gradient'], replay_gradient=replay['gradient'])
            reference = json.loads((SOURCE/'references/cache-time.json').read_text())['records'][key]
            field = np.array(reference['field'], dtype=float)
            reference_states = np.einsum('tj,ij->ti', np.array(reference['coefficients'], dtype=float), np.array(reference['basis'], dtype=float), optimize=False)
            exact = np.array(reference['time_exact_field'], dtype=float)
            gradient = np.array(reference['gradient'], dtype=float)
            scale = max(1., norm(gradient))
            errors[n, N] = hnorm(states[-1]-exact)
            values = {'state_error': max(hnorm(actual-ref) for actual, ref in zip(states, reference_states)), 'gradient_error': norm(np.array(full['gradient'])-gradient),
                      'tangent_error': norm(tangent['gradient']-gradient),
                      'replay_error': norm(np.array(full['gradient'])-replay['gradient']),
                      'time_error': errors[n, N], 'reference_scale': max(1., hnorm(exact)),
                      'full_ledger': full['ledger'], 'checkpoint_ledger': replay['ledger'],
                      'objective': full['objective'], 'full_primal_solves': full['primal_solves'],
                      'full_transpose_solves': full['transpose_solves'], 'replay_solves': replay['replay_solves'],
                      'checkpoint_primal_solves': replay['primal_solves'],
                      'checkpoint_transpose_solves': replay['transpose_solves'], 'tangent_RHS_solves': tangent['RHS_solves']}
            save_npz(output/(key+'.npz'), states=states, reference_states=reference_states, reference_terminal=field, time_exact_terminal=exact,
                     tangent_kappa=tangent['sk'], tangent_theta=tangent['st'],
                     adjoint_gradient=full['gradient'], reference_gradient=gradient,
                     tangent_gradient=tangent['gradient'], replay_gradient=replay['gradient'])
            tests = {'finite-boundary': bool(np.isfinite(states).all() and np.isfinite(full['gradient']).all() and np.isfinite(replay['gradient']).all() and finite_arrays({k: tangent[k] for k in ['sk', 'st', 'state']})),
                     'state-modal': values['state_error'] <= limits['field_scaled']*max(1., hnorm(field)),
                     'adjoint-modal': values['gradient_error'] <= limits['gradient_scaled']*scale,
                     'tangent-modal': values['tangent_error'] <= limits['gradient_scaled']*scale,
                     'adjoint-tangent': norm(np.array(full['gradient'])-tangent['gradient']) <= limits['adjoint_tangent_scaled']*scale,
                     'replay-state': time_case.compare_replay(work, states),
                     'replay-gradient': values['replay_error'] <= limits['replay_gradient_scaled']*scale,
                     'exact-work': full['primal_solves'] == full['transpose_solves'] == replay['primal_solves'] == replay['replay_solves'] == replay['transpose_solves'] == N and tangent['RHS_solves'] == 2*N}
            for tag, passed in tests.items(): add(checks, key+'-'+tag, passed)
            records.append({'n': n, 'steps': N, 'metrics': values, 'field_file': key+'.npz'})
            rows.append([n, N, values['state_error'], values['gradient_error'], values['tangent_error'],
                         values['time_error'], full['ledger']['peak_total_bytes'], replay['ledger']['peak_total_bytes'],
                         replay['ledger']['peak_state_elements']])
            flush()
        for coarse, fine in zip(cfg['steps'][:-1], cfg['steps'][1:]):
            denominator = errors[n, coarse]
            ratio = errors[n, fine]/denominator if denominator else 0.
            add(checks, f'n{n}-time-ratio-{coarse}-{fine}', denominator > limits['time_error_roundoff_scale'] and limits['time_ratio'][0] <= ratio <= limits['time_ratio'][1])
            case['metrics'].setdefault('time_ratios', []).append({'n': n, 'coarse': coarse, 'fine': fine, 'ratio': ratio, 'denominator': denominator})
        fine_record = records[-1]['metrics']
        add(checks, f'n{n}-N256-storage', fine_record['checkpoint_ledger']['peak_state_elements'] <= limits['checkpoint_peak_state_elements_factor']*n and fine_record['checkpoint_ledger']['peak_total_bytes'] < fine_record['full_ledger']['peak_total_bytes'])
    fd_cfg = cfg['FD']; base = next(r for r in records if r['n'] == fd_cfg['n'] and r['steps'] == fd_cfg['steps'])
    gradient = np.load(output/f"n{fd_cfg['n']}-N{fd_cfg['steps']}.npz", allow_pickle=False)['adjoint_gradient']
    fd_rows, fd_finite = [], True
    for i, direction in enumerate(fd_cfg['directions']):
        expected = dot(gradient, np.array(direction, dtype=float))
        for exponent in [10, 14, 18]:
            h = 2.**-exponent; pair = []
            for sign in [-1, 1]:
                J, state = time_case.forward_objective(fd_cfg['n'], fd_cfg['steps'], cfg['kappa']+sign*h*direction[0], cfg['theta']+sign*h*direction[1], cfg['T'], output/f'FD-direction{i}-{exponent}-{sign}-partial.npz')
                pair.append(J); save_npz(output/f'FD-direction{i}-{exponent}-{sign}.npz', state=state, objective=J)
                fd_finite &= bool(np.isfinite(state).all() and np.isfinite(J))
            actual = (pair[1]-pair[0])/(2*h)
            fd_rows.append([i, h, actual, expected, abs(actual-expected)])
        add(checks, f'FD-direction{i}', abs(actual-expected) <= limits['FD_finest_scaled']*max(1., abs(expected)))
    add(checks, 'FD-all-finite', fd_finite)
    add(checks, 'qualified-cache', True)
    finite_csv(output/'diffusion-discrete-adjoint.csv', ['n', 'steps', 'field_error', 'adjoint_error', 'tangent_error', 'time_error', 'full_bytes', 'checkpoint_bytes', 'checkpoint_state_elements'], rows)
    finite_csv(output/'diffusion-FD.csv', ['direction', 'step', 'FD', 'adjoint', 'error'], fd_rows)
    case['metrics'].update(principal_records=len(records), FD_forward_evolutions=18,
                           ownership_scope='Unique explicit scientific arrays; validation loaded after the separate ownership windows; serialization internals are not process RSS.')


def near_fold(case, cfg, limits, settings, output, flush):
    checks, rows, linear_rows, fd_rows = case['checks'], [], [], []
    for n in cfg['n']:
        for i, text in enumerate(cfg['lambda_decimal'][str(n)]):
            lam = float(text); key = f'n{n}-point{i}'
            out = fold_study.record(n, lam, settings, cfg, output/(key+'-partial.npz'), output/(key+'.npz'))
            # Cache access/diagnostics occur after each completed candidate was saved.
            cache = json.loads((SOURCE/'references/cache-fold.json').read_text())
            ref = cache['points'][key]; fold = cache['folds'][str(n)]
            if ref['lambda_hex'] != lam.hex(): raise ValueError('Reference parameter rounding mismatch')
            u = out['arrays']['state_strict']; ref_u = np.array(ref['u'], dtype=float)
            ref_g = float(ref['gradient']); state_error = float(np.max(np.abs(u-ref_u)))
            gradient_error = abs(out['gradient']-ref_g)
            identity_ok = all(max(r['tangent_defect'], r['adjoint_defect'], r['approximate_cross_defect']) <= limits['residual_identity_scaled']*r['scale'] and r['tangent_error'] <= r['finite_reference_bound']+limits['reference_error_bound_roundoff_scaled']*r['scale'] for r in out['identities'])
            statuses = [{'requested_rtol': rtol, 'tangent': status(item['tangent']), 'adjoint': status(item['adjoint'])} for rtol, item in zip(cfg['linear_rtol'], out['linear'])]
            target_ok = all(item[k]['finite_candidate'] and item[k]['raw_solver_passed'] == item[k]['target_met'] and item[k]['iterations'] <= settings['gmres']['max_iterations'] and (j == 2 or item[k]['target_met']) for j, item in enumerate(out['linear']) for k in ['tangent', 'adjoint'])
            all_state = out['states']+out['FD_states']
            positive = all(np.min(s['u']) > 0 and smallest(s['u'], lam)[1] > 0 for s in out['states'])
            fd_ok = all(s['passed'] and s['residual'] <= cfg['FD_state_tolerance'] and np.min(s['u']) > 0 and smallest(s['u'], lam+sign*step)[1] > 0 for s, (step, sign) in zip(out['FD_states'], [(step, sign) for step in cfg['FD_steps'] for sign in [-1, 1]]))
            tests = {'finite-state-branches': finite_arrays(out['arrays']) and positive and all(np.isfinite(s['u']).all() for s in all_state),
                     'strict-state-reference': state_error <= limits['strict_state_scaled']*max(1., float(np.max(np.abs(ref_u)))),
                     'state-residuals': all(s['passed'] and s['residual'] <= t for s, t in zip(out['states'], cfg['state_tolerances'])),
                     'below-discrete-fold': abs(float(fold['lambda'])-float(cfg['stored_discrete_anchor_decimal'][str(n)])) <= 1e-10 and lam < float(fold['lambda']) and out['minimum_eigenvalue'] > 0 and float(np.max(np.abs(u-u[::-1]))) <= limits['symmetry_scaled']*max(1., float(np.max(np.abs(u)))),
                     'strict-gradient-reference': gradient_error <= limits['gradient_reference_absolute']+limits['gradient_reference_relative']*abs(ref_g),
                     'direct-duality': abs(out['direct_gradient_tangent']-out['direct_gradient_adjoint']) <= limits['direct_duality_scaled']*max(1., abs(ref_g)),
                     'GMRES-fixed-targets': target_ok, 'residual-identities': identity_ok, 'FD-complete': fd_ok and len(out['FD']) == 3}
            for tag, passed in tests.items(): add(checks, key+'-'+tag, passed)
            arrays = {**out['arrays'], 'reference_state': ref_u, 'reference_gradient': np.array(ref_g)}
            save_npz(output/(key+'.npz'), arrays)
            metrics = {'lambda': lam, 'delta': float(cfg['delta_decimal'][i]), 'state_error': state_error,
                       'gradient': out['gradient'], 'reference_gradient': ref_g, 'gradient_error': gradient_error,
                       'loose_state_error': float(np.max(np.abs(out['arrays']['state_loose']-ref_u))),
                       'loose_direct_gradient': out['loose_direct_gradient'], 'sigma_estimate': out['sigma_estimate'],
                       'sigma_is_certified_bound': False, 'linear_statuses': statuses, 'identities': out['identities'], 'FD': out['FD'],
                       'newton_loose': out['states'][0]['newton'], 'newton_strict': out['states'][1]['newton']}
            case['records'].append({'n': n, 'point': i, 'metrics': metrics, 'field_file': key+'.npz'})
            rows.append([n, lam, float(cfg['delta_decimal'][i]), out['sigma_estimate'], state_error, gradient_error, out['gradient'], ref_g])
            for j, item in enumerate(out['linear']):
                for kind, code in [('tangent', 0), ('adjoint', 1)]:
                    s = item[kind]
                    linear_rows.append([n, i, code, cfg['linear_rtol'][j], s['requested_absolute_target'], s['actual_true_residual'], int(s['target_met']), s['iterations'], s['roundoff_scale_estimate']])
            for f in out['FD']: fd_rows.append([n, i, f['step'], f['derivative'], abs(f['derivative']-ref_g)])
            flush()
    add(checks, 'qualified-cache', True)
    finite_csv(output/'bratu-fold-sensitivity.csv', ['n', 'lambda', 'delta', 'sigma_estimate', 'state_error', 'gradient_error', 'gradient', 'reference_gradient'], rows)
    finite_csv(output/'fold-linear-status.csv', ['n', 'point', 'kind', 'rtol', 'target', 'actual_residual', 'target_met', 'iterations', 'roundoff_estimate'], linear_rows)
    finite_csv(output/'fold-FD.csv', ['n', 'point', 'step', 'FD', 'error'], fd_rows)
    case['metrics'].update(principal_records=len(case['records']), FD_state_solves=36,
                           tight_target_policy='1e-12 observational; exact returned candidate retained. Passing case does not imply target attained.')


def many_parameters(case, cfg, limits, settings, output, flush):
    rows = []
    for m in cfg['m']:
        n = cfg['n']; key = f'm{m}'
        out = distributed.run(n, m, settings, cfg, output/(key+'-partial.npz'), output/(key+'.npz'))
        arrays = out['arrays']; u, coefficient = arrays['u'], arrays['coefficient']
        # Dense reference only in this explicitly separate post-primary window.
        B, S = full_sensitivity(u, coefficient, m)
        qs = distributed.objective_q(u)
        reference = np.array([np.einsum('i,ij->j', q, S, optimize=False) for q in qs])
        errors = [norm(a-b) for a, b in zip(out['gradients'], reference)]
        expected_direction = np.array([dot(g, arrays['direction']) for g in out['gradients']])
        fd_error = np.abs(out['FD'][-1]['derivative']-expected_direction)
        dual = out['duality']
        tests = {'state-residual': out['state']['passed'] and out['state']['residual'] <= cfg['state_tolerance'],
                 'coefficient': np.min(coefficient) >= 1.7-1e-13 and np.max(coefficient) <= 2.3+1e-13,
                 'duality': dual['J_error'] <= limits['dot_product_scaled']*dual['J_scale'] and dual['B_error'] <= limits['dot_product_scaled']*dual['B_scale'],
                 'VJP-dense-reference': all(e <= limits['VJP_absolute']+limits['VJP_relative']*norm(r) for e, r in zip(errors, reference)) and all(c['target_met'] for c in out['one_candidates']+out['candidates']),
                 'FD-finest': bool(np.all(fd_error <= limits['FD_finest_scaled']*np.maximum(1., np.abs(expected_direction)))),
                 'objective-count': out['one_RHS'] == 1 and out['three_RHS'] == 3 and out['derivative_factor_builds'] == 1 and all(c['counts']['factor_builds'] == 0 for c in out['one_candidates']+out['candidates']) and np.array_equal(arrays['one_gradient'][0], out['gradients'][0]),
                 'allocation': all(tuple(r['shape']) not in [(n, m), (m, n)] for r in out['inventory']),
                 'finite-boundary': finite_arrays(arrays) and all(s['passed'] and np.isfinite(s['u']).all() for s in out['FD_states']) and len(out['FD_states']) == 6}
        for tag, passed in tests.items(): add(case['checks'], key+'-'+tag, passed)
        save_npz(output/(key+'.npz'), **arrays, reference_gradients=reference,
                 dense_reference_sensitivity=S, dense_reference_B=B,
                 FD_derivatives=np.array([f['derivative'] for f in out['FD']]))
        metrics = {'state_residual': out['state']['residual'], 'gradient_errors': errors, 'FD_finest_errors': fd_error,
                   'one_RHS': out['one_RHS'], 'three_RHS': out['three_RHS'], 'reference_RHS': m,
                   'state_counts': out['state']['counts'], 'derivative_factor_builds': out['derivative_factor_builds'], 'derivative_factor_solves': out['derivative_factor_solves'],
                   'duality': dual, 'primary_arrays': out['inventory'], 'Krylov_workspace': out['workspace'],
                   'reference_arrays': [{'name': 'S', 'shape': list(S.shape), 'bytes': S.nbytes}, {'name': 'B', 'shape': list(B.shape), 'bytes': B.nbytes}],
                   'linear_statuses': [status(item) for item in out['candidates']], 'FD': out['FD']}
        case['records'].append({'n': n, 'm': m, 'metrics': metrics, 'field_file': key+'.npz'})
        for j in range(3): rows.append([n, m, j, errors[j], float(fd_error[j]), out['one_RHS'], out['three_RHS'], m])
        flush()
    add(case['checks'], 'nonsymmetric-transpose', distributed.nonsymmetric_control())
    error, negative = distributed.affine_control(cfg['n'])
    add(case['checks'], 'affine-offset', error <= limits['affine_identity_scaled'] and negative > 1.)
    add(case['checks'], 'qualified-cache', True)
    case['metrics'].update(principal_records=len(case['records']), FD_state_solves=18,
                           affine_error=error, wrong_offset_error=negative,
                           primary_scope='Persistent named-array inventory and declared fixed Krylov workspace; not an RSS/peak-allocation measurement.')
    finite_csv(output/'bratu-distributed-vjp.csv', ['n', 'm', 'objective', 'VJP_error', 'FD_error', 'one_RHS', 'three_RHS', 'reference_RHS'], rows)


def run(input_path, output):
    output = fresh_directory(output); started = time.monotonic()
    config = json.loads(Path(input_path).read_text()); acceptance = json.loads((SOURCE/'acceptance.json').read_text())
    result = {'schema_version': 1, 'passed': False, 'termination': 'incomplete', 'failure': None,
              'checks': {}, 'cases': [], 'input_sha256': digest(input_path), 'source_sha256': {}, 'duration_seconds': 0.}
    def flush():
        for c in result['cases']: c['passed'] = bool(c['checks']) and all(c['checks'].values())
        result['checks'] = {c['id']: c['passed'] for c in result['cases']}
        result['duration_seconds'] = time.monotonic()-started
        save_json(output/'result.json', result)
    def stop(_sig, _frame): raise TimeoutError('Main terminated; partial scientific outputs retained')
    old = signal.signal(signal.SIGTERM, stop)
    flush()
    try:
        qualified_cache(SOURCE, input_path, SOURCE/'acceptance.json')
        contract = json.loads((SOURCE/'pre-run-contract.json').read_text())
        for path, expected in contract['files_sha256'].items():
            if digest(SOURCE/path) != expected: raise ValueError('Changed frozen source: '+path)
        result['source_sha256'] = {**contract['files_sha256'], 'pre-run-contract.json': digest(SOURCE/'pre-run-contract.json')}
        functions = [diffusion, near_fold, many_parameters]
        for case_id, function, number in zip(CASE_IDS, functions, ['62', '63', '64']):
            case = {'id': case_id, 'passed': False, 'checks': {}, 'records': [], 'metrics': {}}
            result['cases'].append(case); flush()
            directory = output/case_id; directory.mkdir()
            args = [case, config['cases'][case_id], acceptance['limits'][number]]
            if number != '62': args.append(config['solver'])
            function(*args, directory, flush)
            for csv_file in directory.glob('*.csv'):
                shutil.copyfile(csv_file, output/csv_file.name)
            expected = {r['id'] for r in acceptance['gates'] if r['case'] == case_id}
            if set(case['checks']) != expected: raise ValueError('Missing/unexpected gate IDs: '+case_id)
            flush()
        if sum(len(c['checks']) for c in result['cases']) != 141: raise ValueError('Exactly141 gates required')
        result['passed'] = all(result['checks'].values())
        result['termination'] = 'fixed_budget_completed'
    except BaseException as error:
        result['failure'] = {'type': type(error).__name__, 'message': str(error)}
        result['termination'] = 'exception'
    finally:
        signal.signal(signal.SIGTERM, old); flush()
    return result


def main():
    p = argparse.ArgumentParser(); p.add_argument('--input', type=Path, default=SOURCE/'inputs.json')
    p.add_argument('--output', type=Path, required=True); a = p.parse_args()
    result = run(a.input, a.output)
    print(json.dumps({'passed': result['passed'], 'gates': sum(len(c['checks']) for c in result['cases']), 'duration_seconds': result['duration_seconds']}))
    return 0 if result['passed'] else 1


if __name__ == '__main__': raise SystemExit(main())
