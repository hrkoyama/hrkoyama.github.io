"""Independent reference qualification only: no production trajectory imports."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import traceback
import numpy as np
from scipy.integrate import solve_ivp
from reference_models import system, observation_times
from boundary_reference import sparse_action, sine_solution, exact_continuum
from coefficient_exact import audit

DEPENDENCIES = ['inputs.json', 'acceptance.json', 'tableau.py', 'references/qualify.py',
                'references/reference_models.py', 'references/boundary_reference.py', 'references/coefficient_exact.py']


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dump(path, data):
    tmp = path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False)+'\n')
    tmp.replace(path)


def main():
    parser = argparse.ArgumentParser();parser.add_argument('--output', required=True, type=Path);args = parser.parse_args()
    source = Path(__file__).resolve().parents[1]
    if args.output.exists():raise FileExistsError('Fresh qualifier output required')
    args.output.mkdir(parents=True)
    result = {'passed': False, 'checks': {}, 'metrics': {}, 'source_sha256': {name: digest(source/name) for name in DEPENDENCIES},
              'input_sha256': digest(source/'inputs.json'), 'acceptance_sha256': digest(source/'acceptance.json')}
    def check(name, ok, value=None):
        if name in result['checks']:raise ValueError('Duplicate qualification check')
        result['checks'][name] = bool(ok)
        if value is not None:result['metrics'][name] = value
        dump(args.output/'qualification.json', result)
    try:
        for key in ('robertson', 'vdp-mu1', 'vdp-mu100'):
            rhs, jac, initial, weights, total = system(key)
            times = observation_times(key)
            points = np.array([[1.,0.,0.], [0.9,3e-5,0.09997], [0.5,1e-6,0.499999]]) if key == 'robertson' else np.array([[2.,0.], [0.3,-0.2], [-1.2,0.5]])
            analytic, complex_step = [], []
            for point in points:
                analytic.append(jac(0., point))
                columns = []
                for index in range(len(point)):
                    perturbed = point.astype(complex)
                    perturbed[index] += 1e-30j
                    columns.append(np.imag(rhs(0., perturbed))/1e-30)
                complex_step.append(np.array(columns).T)
            analytic, complex_step = np.array(analytic), np.array(complex_step)
            np.savez_compressed(args.output/(key+'-jacobian-controls.npz'), states=points, analytic=analytic, complex_step=complex_step)
            jac_error = float(np.max(np.abs(analytic-complex_step)/(1+np.abs(analytic))))
            check(key+':analytic-Jacobian-vs-complex-step', jac_error <= 3e-14, jac_error)
            if jac_error > 3e-14:raise ValueError('ReferenceJacobian qualification failed before model solves')
            values = []
            for ident, method, rtol, scale in [('Radau', 'Radau', 1e-11, 1e-13), ('Radau-tight', 'Radau', 2e-12, 2e-14), ('BDF', 'BDF', 2e-12, 2e-14)]:
                np.savez_compressed(args.output/(key+'-entered.npz'), initial=initial, times=times)
                # Last owned callback state is available on ordinary exceptions;
                # the monolithic SciPy accepted history is not exposed if it raises.
                last = {'phase': 'before-solve', 'time': np.array([0.]), 'state': initial.copy()}
                def observed_rhs(t, state):
                    last.clear();last.update(phase='before-rhs', time=np.array([t]), state=state.copy())
                    value = rhs(t, state)
                    last['rhs'] = value.copy()
                    return value
                def observed_jac(t, state):
                    last.clear();last.update(phase='before-jacobian', time=np.array([t]), state=state.copy())
                    value = jac(t, state)
                    last['jacobian'] = value.copy()
                    return value
                try:
                    sol = solve_ivp(observed_rhs, (0., total), initial.copy(), method=method, t_eval=times,
                                    rtol=rtol, atol=scale*weights, jac=observed_jac)
                except BaseException:
                    np.savez_compressed(args.output/(key+'-'+ident+'-last-callback.npz'),
                                        **{name: np.array(value, copy=True) for name,value in last.items()})
                    raise
                # Preserve the completed/partial raw candidate before status/diagnostics.
                np.savez_compressed(args.output/(key+'-'+ident+'.npz'), times=sol.t.copy(), states=sol.y.T.copy(),
                                    initial=initial, weights=weights, status=np.array([sol.status]),
                                    counters=np.array([sol.nfev, sol.njev, sol.nlu]))
                values.append({'solution': sol, 'states': sol.y.T.copy(), 'id': ident})
            completed = all(v['solution'].success and np.array_equal(v['solution'].t, times) for v in values)
            check(key+':all-reference-statuses', completed)
            if not completed:raise RuntimeError('Reference failed before prescribed observations')
            finite = all(np.isfinite(v['states']).all() for v in values)
            check(key+':finite-full-grid', finite)
            if not finite:raise FloatingPointError('Nonfinite reference')
            limit = 5e-8 if key == 'robertson' else 5e-9
            scale = weights if key == 'robertson' else np.ones(2)
            err_tight = float(np.max(np.abs(values[0]['states']-values[1]['states'])/scale))
            err_algorithm = float(np.max(np.abs(values[2]['states']-values[1]['states'])/scale))
            check(key+':Radau-refinement', err_tight <= limit, err_tight)
            check(key+':independent-BDF-agreement', err_algorithm <= limit, err_algorithm)
            check(key+':initial-state', all(np.array_equal(v['states'][0], initial) for v in values))
            if key == 'robertson':
                mass = max(float(np.max(np.abs(v['states'].sum(axis=1)-1))) for v in values)
                minimum = min(float(v['states'].min()) for v in values)
                check(key+':mass-invariant', mass <= 1e-11, mass)
                check(key+':nonnegative-fixed-reference', minimum >= -2e-13, minimum)
        for n in (31, 63, 127):
            times = np.array([0., 0.025, 0.05, 0.075, 0.1])
            def save(phase, **arrays):
                np.savez_compressed(args.output/('boundary-'+str(n)+'-active.npz'), **arrays)
            x, values, matrix, force = sparse_action(n, times, save)
            np.savez_compressed(args.output/('boundary-'+str(n)+'.npz'), x=x, times=times, states=values)
            check('boundary-'+str(n)+':finite-sparse', np.isfinite(values).all())
            other, rates = sine_solution(n, times)
            continuum = np.array([exact_continuum(x, t) for t in times])
            # Enrich only after sparse candidate has already been saved.
            np.savez_compressed(args.output/('boundary-'+str(n)+'.npz'), x=x, times=times,
                                states=values, sine_states=other, sine_rates=rates, continuum=continuum)
            err = float(np.max(np.abs(values-other)))
            residual = max(float(np.max(np.abs(rates[k]-(matrix@other[k]+force)))) for k in range(len(times)))
            check('boundary-'+str(n)+':sparse-vs-sine', err <= 3e-11, err)
            check('boundary-'+str(n)+':independent-equation-residual', residual <= 3e-9, residual)
            check('boundary-'+str(n)+':initial', float(np.max(np.abs(values[0]-continuum[0]))) <= 1e-13)
            check('boundary-'+str(n)+':physical-boundary', all(abs(float(exact_continuum(np.array([0.,1.]), t)[0])-1) <= 1e-14 and abs(float(exact_continuum(np.array([0.,1.]), t)[1])-1) <= 1e-14 for t in times))
            check('boundary-'+str(n)+':finite-continuum-control', np.isfinite(continuum).all() and float(np.max(np.abs(values-continuum))) <= 0.01)
        coefficient_checks, notes = audit(source/'tableau.py')
        dump(args.output/'coefficient-audit.json', notes)
        for name, passed in coefficient_checks.items():check('coefficient:'+name, passed)
        if len(result['checks']) != 52:raise AssertionError('Actual52 reference/check inventory required')
        result['passed'] = all(result['checks'].values())
    except BaseException as exc:
        result['failure'] = {'type': type(exc).__name__, 'message': str(exc), 'traceback': traceback.format_exc()}
    dump(args.output/'qualification.json', result)
    return 0 if result['passed'] else 1


if __name__ == '__main__':sys.exit(main())
