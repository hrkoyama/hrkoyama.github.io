#!/usr/bin/env python3
"""48 fixed reference qualification decisions; no main optimizer study."""
import argparse
import json
from pathlib import Path
import sys
import traceback

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy as np

from model import BratuModel, observe_legacy
from references.oracles import fit_context
from references.thomas import state_and_sensitivity
from support import DecisionBook, Retainer, digest, numeric_csv, relative_error, write_json

BOUND_SOURCES = ['support.py', 'model.py', 'references/thomas.py', 'references/oracles.py',
                 'references/qualify.py', 'references/__init__.py', 'legacy/__init__.py',
                 'legacy/numart/__init__.py', 'legacy/numart/autodiff.py',
                 'legacy/numart/bratu_inverse.py', 'legacy/numart/bratu_multinverse.py',
                 'legacy/numart/bratu_sensitivity.py', 'legacy/numart/krylov.py',
                 'legacy/input-observations.json']


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    cfg = json.loads(args.input.read_text())
    acceptance = json.loads((ROOT/'acceptance.json').read_text())
    limits, book = acceptance['limits'], DecisionBook()
    report = dict(schema_version=1, passed=False, checks=book.checks, details=book.details,
                  input_sha256=digest(args.input), acceptance_sha256=digest(ROOT/'acceptance.json'),
                  source_sha256={n: digest(ROOT/n) for n in BOUND_SOURCES},
                  reference_optimizer_fits=0, fixed_state_points=0, failure=None)
    arrays, rows = {}, []
    try:
        active_retainer = Retainer(output, 'active-data')
        active = state_and_sensitivity(31, [2.9, .35], cfg['bratu']['positions'], active_retainer)
        arrays['active_data'] = active['predicted']
        active_retainer.arrays('completed', **active)
        book.add('active-data-finite', np.all(np.isfinite(active['predicted'])), active['predicted'])
        book.add('active-data-state-residual', active['scaled_residual_inf'] <= limits['oracle_scaled_residual_inf'],
                 active['scaled_residual_inf'], limits['oracle_scaled_residual_inf'])
        for i, theta in enumerate(([2., 0.], [2.2, .35], [2.9, .35], [1.5, -.25])):
            raw = Retainer(output, 'state-point-'+str(i))
            reference = state_and_sensitivity(31, theta, cfg['bratu']['positions'], raw)
            with observe_legacy(raw):
                primary = BratuModel(31, cfg['legacy_data']['same_grid_data'], cfg['bratu']['positions'],
                                     cfg['bratu']['weights'], 0., cfg['bratu']['prior'], raw).at(theta)
            raw.arrays('completed-both-before-comparison', reference_state=reference['state'],
                       primary_state=primary['state'], reference_k=reference['data_jacobian'],
                       primary_k=primary['data_jacobian'])
            finite_difference = np.empty((5, 2))
            for j in range(2):
                step = np.zeros(2)
                step[j] = 1e-5
                plus = state_and_sensitivity(31, np.asarray(theta)+step, cfg['bratu']['positions'], raw)
                minus = state_and_sensitivity(31, np.asarray(theta)-step, cfg['bratu']['positions'], raw)
                finite_difference[:, j] = (plus['predicted']-minus['predicted'])/(2e-5)
            raw.arrays('finite-difference-before-comparison', finite_difference=finite_difference)
            book.add(f'point-{i}-residual', reference['scaled_residual_inf'] <= limits['oracle_scaled_residual_inf'],
                     reference['scaled_residual_inf'], limits['oracle_scaled_residual_inf'])
            for label, actual, expected, limit in [
                ('state', primary['state'], reference['state'], limits['dense_thomas_state_relative_inf']),
                ('jacobian', primary['data_jacobian'], reference['data_jacobian'], limits['dense_thomas_jacobian_relative_inf']),
                ('finite-difference', finite_difference, reference['data_jacobian'], limits['finite_difference_jacobian_relative'])]:
                defect = relative_error(actual, expected, np.inf if label != 'finite-difference' else None)
                book.add(f'point-{i}-{label}', defect <= limit, defect, limit)
            arrays[f'point_{i}_state'] = reference['state']
            arrays[f'point_{i}_jacobian'] = reference['data_jacobian']
            report['fixed_state_points'] += 1
        for i in range(4):
            raw = Retainer(output, 'context-'+str(i))
            result = fit_context(cfg, i, arrays['active_data'], raw)
            # Save all completed candidate fields before any acceptance diagnostic.
            arrays.update({f'context_{i}_{key}': result[key] for key in
                           ['parameters', 'state', 'data_jacobian', 'gradient', 'objective']})
            np.savez_compressed(output/'cache-fields.partial.npz', **arrays)
            lo, hi = np.asarray(cfg['bratu']['box']['lower']), np.asarray(cfg['bratu']['box']['upper'])
            book.add(f'context-{i}-complete', result['library_success'],
                     {'status': result['library_status'], 'message': result['library_message']})
            book.add(f'context-{i}-finite', np.all(np.isfinite(result['parameters'])) and np.isfinite(result['objective']), result['objective'])
            book.add(f'context-{i}-residual', result['scaled_residual_inf'] <= limits['oracle_scaled_residual_inf'],
                     result['scaled_residual_inf'], limits['oracle_scaled_residual_inf'])
            book.add(f'context-{i}-stationary', result['projected_gradient_inf'] <= limits['oracle_stationarity_inf'],
                     result['projected_gradient_inf'], limits['oracle_stationarity_inf'])
            book.add(f'context-{i}-feasible', np.all(result['parameters'] >= lo) and np.all(result['parameters'] <= hi), result['parameters'])
            book.add(f'context-{i}-nonincrease', result['objective'] <= result['initial_objective'],
                     result['objective'], result['initial_objective'])
            if i != 2:
                book.add(f'context-{i}-strictly-interior', np.all(result['parameters'] > lo) and np.all(result['parameters'] < hi), result['parameters'])
                gradient = float(np.linalg.norm(result['gradient'], ord=np.inf))
                book.add(f'context-{i}-unbounded-stationary', gradient <= limits['oracle_stationarity_inf'], gradient, limits['oracle_stationarity_inf'])
            rows.append([i, *result['parameters'], result['objective'], result['projected_gradient_inf'], result['nfev']])
            report['reference_optimizer_fits'] += 1
            write_json(output/'qualification.partial.json', report)
        if len(book.checks) != 48:
            raise ValueError('Reference decision inventory must be exactly48')
        np.savez_compressed(output/'cache-fields.npz', **arrays)
        report['fields_sha256'] = digest(output/'cache-fields.npz')
        report['gate_count'] = len(book.checks)
        report['passed'] = all(book.checks.values())
        numeric_csv(output/'reference-summary.csv', ['context_index', 'a', 'b', 'objective', 'projected_gradient_inf', 'nfev'], rows)
    except BaseException as error:
        report['passed'] = False
        if arrays:
            np.savez_compressed(output/'cache-fields.partial.npz', **arrays)
        report['failure'] = {'type': type(error).__name__, 'message': str(error), 'traceback': traceback.format_exc()}
        raise
    finally:
        write_json(output/'qualification.json', report)
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
