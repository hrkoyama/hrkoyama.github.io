#!/usr/bin/env python3
"""Run frozen WENO critical reconstruction and genuine periodic FV transport."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import shutil
import time
import numpy as np
import weno
from references import analytic

ROOT = Path(__file__).resolve().parent
CASE = 'weno-critical-epsilon'
HISTORY_COLUMNS = ['step', 'time', 'courant', 'mass', 'stage_minimum',
                   'stage_maximum', 'maximum_weight_deviation', 'rhs_mass_defect',
                   'step_mass_defect']


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def check_frozen_sources(root=ROOT):
    root = Path(root)
    contract = json.loads((root/'pre-run-contract.json').read_text())
    for name, digest in contract['files_sha256'].items():
        if sha(root/name) != digest:raise ValueError('Changed frozen scientific source/input: '+name)
    return contract


def fixed_runs(cfg):
    runs = [dict(id=f'{m}-{p}-n{n}', method=m, epsilon_policy=p, n=n,
                 family='refinement', courant=cfg['transport_courant'])
            for m in cfg['methods'] for p in cfg['epsilon_policies']
            for n in cfg['transport_grids']]
    runs += [dict(id=f'{m}-{p}-time-half', method=m, epsilon_policy=p,
                  n=cfg['transport_grids'][-1], family='time-probe',
                  courant=cfg['transport_courant']*cfg['time_probe_factor'])
             for m in cfg['methods'] for p in cfg['epsilon_policies']]
    return runs


def reconstruction_records(cfg):
    rows, arrays = [], {k: [] for k in ['means', 'weights', 'beta', 'candidates']}
    for profile in cfg['profiles']:
        coefficients = analytic.PROFILES[profile]
        for method in cfg['methods']:
            for policy in cfg['epsilon_policies']:
                for n in cfg['reconstruction_grids']:
                    h = 1/n;epsilon = weno.epsilon_value(policy, h)
                    means = analytic.polynomial_means(np.arange(-2, 3)*h, h, coefficients)
                    trace, weights, beta, candidates = weno.reconstruct(means, method, epsilon)
                    exact = float(analytic.polynomial_value(h/2, coefficients))
                    row = dict(profile=profile, method=method, epsilon_policy=policy,
                               n=n, h=h, epsilon=epsilon, trace=float(trace), reference=exact,
                               absolute_error=abs(float(trace)-exact),
                               weight_deviation=float(np.max(abs(weights-weno.LINEAR))),
                               weight_sum_defect=abs(float(weights.sum())-1),
                               minimum_weight=float(weights.min()), tau5=float(abs(beta[0]-beta[2])))
                    rows.append(row)
                    for key, value in zip(arrays, [means, weights, beta, candidates]):arrays[key].append(value)
    return rows, {k: np.array(v) for k, v in arrays.items()}


def decisions(local, rows, cfg, limits, qualification):
    checks = []
    def add(name, value, bound, passed):
        checks.append(dict(name=name, value=value, bound=bound, passed=bool(passed)))
    add('72 fixed local reconstructions', len(local), 72, len(local) == 72)
    add('24 fixed PDE runs completed', [r['id'] for r in rows],
        [r['id'] for r in fixed_runs(cfg)], [r['id'] for r in rows] == [r['id'] for r in fixed_runs(cfg)])
    add('independent analytic-cell quadrature', qualification.get('maximum_difference', 1),
        limits['reference_quadrature'], qualification.get('maximum_difference', 1) <= limits['reference_quadrature'])
    add('convex normalized local weights', max([r['weight_sum_defect'] for r in local], default=1),
        limits['weight_sum'], bool(local) and all(r['minimum_weight'] >= 0 and r['weight_sum_defect'] <= limits['weight_sum'] for r in local))
    # All three local regularity classes remain visible; only an explicitly
    # chosen first-critical class is assigned an asymptotic accuracy gate.
    for method in cfg['methods']:
        for policy in cfg['epsilon_policies']:
            seq = [r for r in local if r['profile'] == 'first-critical' and r['method'] == method and r['epsilon_policy'] == policy]
            for previous, current in zip(seq, seq[1:]):
                ratio = current['absolute_error']/previous['absolute_error']
                add(f'first-critical {method} {policy} refinement n{current["n"]}', ratio,
                    limits['local_refinement_ratio'], ratio <= limits['local_refinement_ratio'])
    def selected(method, policy):
        return [r for r in local if r['profile'] == 'first-critical' and r['method'] == method and r['epsilon_policy'] == policy]
    z, js = selected('weno-z', 'fixed-1e-40'), selected('weno-js', 'fixed-1e-40')
    ratio = z[-1]['absolute_error']/js[-1]['absolute_error']
    add('first-critical tiny-epsilon Z/JS error', ratio, limits['first_critical_z_js_error_ratio'], ratio <= limits['first_critical_z_js_error_ratio'])
    for method, policy, key in [('weno-z', 'fixed-1e-40', 'first_critical_z_last_order_minimum'),
                                 ('weno-js', 'h-squared', 'first_critical_scaled_js_last_order_minimum')]:
        seq = selected(method, policy)
        order = float(np.log2(seq[-2]['absolute_error']/seq[-1]['absolute_error']))
        add(f'first-critical last reconstruction order {method} {policy}', order, limits[key], order >= limits[key])
    for r in rows:
        for name, value, bound, passed in [
            ('finite saved arrays', r['all_finite'], True, r['all_finite']),
            ('time reached', r['time'], cfg['transport_final_time'], r['time'] == cfg['transport_final_time']),
            ('periodic mass', r['maximum_mass_change'], limits['periodic_mass'], r['maximum_mass_change'] <= limits['periodic_mass']),
            ('shared RHS flux balance', r['maximum_rhs_mass_defect'], limits['rhs_mass'], r['maximum_rhs_mass_defect'] <= limits['rhs_mass']),
            ('all requested snapshots', r['snapshot_times'], cfg['transport_snapshot_times'], r['snapshot_times'] == cfg['transport_snapshot_times']),
            ('four stage evaluations per step', r['rhs_evaluations'], 4*r['steps'], r['rhs_evaluations'] == 4*r['steps']),
            ('no clipping or retries', r['clip_count']+r['retries'], 0, r['clip_count']+r['retries'] == 0)]:
            add(r['id']+': '+name, value, bound, passed)
    for method in cfg['methods']:
        for policy in cfg['epsilon_policies']:
            seq = [r for r in rows if r['method'] == method and r['epsilon_policy'] == policy and r['family'] == 'refinement']
            if len(seq) != len(cfg['transport_grids']):continue
            for previous, current in zip(seq, seq[1:]):
                ratio = current['l1']/previous['l1']
                add(f'{method} {policy} PDE refinement n{current["n"]}', ratio, limits['transport_refinement_ratio'], ratio <= limits['transport_refinement_ratio'])
            add(f'{method} {policy} finest PDE L1', seq[-1]['l1'], limits['finest_transport_l1'], seq[-1]['l1'] <= limits['finest_transport_l1'])
            probe = next((r for r in rows if r['method'] == method and r['epsilon_policy'] == policy and r['family'] == 'time-probe'), None)
            if probe:
                fraction = probe['time_half_difference_l1']/seq[-1]['l1']
                add(f'{method} {policy} dt contamination fraction', fraction, limits['time_probe_error_fraction'], fraction <= limits['time_probe_error_fraction'])
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=ROOT/'inputs.json')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    contract = check_frozen_sources()
    if sha(args.input) != contract['files_sha256']['inputs.json']:raise ValueError('Use frozen input bytes')
    cfg = json.loads(args.input.read_text())['cases'][CASE]
    limits = json.loads((ROOT/'acceptance.json').read_text())['limits']
    if args.output.exists() and any(args.output.iterdir()):raise ValueError('Use fresh output directory')
    args.output.mkdir(parents=True, exist_ok=True)
    if shutil.disk_usage(args.output).free < 4*1024**3:raise RuntimeError('Require 4 GiB free before run')
    start, rows, files, failure, local, qualification = time.monotonic(), [], {}, None, [], {}
    try:
        local, arrays = reconstruction_records(cfg)
        np.savez_compressed(args.output/'reconstruction.npz', **arrays)
        files['reconstruction.npz'] = sha(args.output/'reconstruction.npz')
        differences = [float(np.max(abs(analytic.periodic_means(n, t)-analytic.quadrature_means(n, t))))
                       for n in cfg['transport_grids'] for t in cfg['transport_snapshot_times']]
        qualification = dict(algorithm='Fourier antiderivative versus independent Gauss12 point-function integration', maximum_difference=max(differences), differences=differences)
        base_fields = {}
        for spec in fixed_runs(cfg):
            if time.monotonic()-start >= 115:raise RuntimeError('shared 120s budget guard')
            if shutil.disk_usage(args.output).free < 2.5*1024**3:raise RuntimeError('2.5 GiB running disk guard')
            n = spec['n'];h = 1/n;epsilon = weno.epsilon_value(spec['epsilon_policy'], h)
            initial = analytic.periodic_means(n)
            out = weno.transport(initial, spec['method'], epsilon, cfg['transport_final_time'], spec['courant'], cfg['transport_snapshot_times'], cfg['max_steps'])
            references = np.array([analytic.periodic_means(n, t) for t in cfg['transport_snapshot_times']])
            error = out['q']-references[-1]
            times = np.array(cfg['transport_snapshot_times'])
            field = 'field-'+spec['id']+'.npz'
            np.savez_compressed(args.output/field, q=out['q'], q_initial=initial,
                                q_reference=references[-1], q_history=out['q_history'],
                                q_reference_history=references, snapshot_times=times,
                                edges=np.linspace(0, 1, n+1), history=out['history'],
                                history_columns=np.array(HISTORY_COLUMNS))
            files[field] = sha(args.output/field)
            row = {**spec, 'epsilon': epsilon, 'time': out['time'], 'steps': out['steps'],
                   'rhs_evaluations': 4*out['steps'], 'l1': float(np.mean(abs(error))),
                   'l2': float(np.sqrt(np.mean(error**2))), 'linf': float(np.max(abs(error))),
                   'maximum_mass_change': float(np.max(abs(out['history'][:, 3]-h*initial.sum()))),
                   'maximum_rhs_mass_defect': float(out['history'][:, 7].max()),
                   'minimum': float(out['history'][:, 4].min()), 'maximum': float(out['history'][:, 5].max()),
                   'snapshot_times': times.tolist(), 'snapshot_l1': np.mean(abs(out['q_history']-references), axis=1).tolist(),
                   'clip_count': out['clip_count'], 'retries': out['retries'], 'field': field,
                   'all_finite': bool(np.all(np.isfinite(out['history'])) and np.all(np.isfinite(out['q_history'])))}
            identity = (spec['method'], spec['epsilon_policy'])
            if spec['family'] == 'refinement':base_fields[identity] = out['q'].copy()
            else:row['time_half_difference_l1'] = float(np.mean(abs(out['q']-base_fields[identity])))
            rows.append(row)
    except Exception as error:
        failure = dict(type=type(error).__name__, message=str(error))
    checks = decisions(local, rows, cfg, limits, qualification) if local else []
    passed = failure is None and len(rows) == 24 and bool(checks) and all(c['passed'] for c in checks)
    for name, records in [(CASE+'.csv', rows), ('reconstruction.csv', local)]:
        if records:
            columns = list(dict.fromkeys(k for r in records for k in r if not isinstance(r[k], (list, dict))))
            with (args.output/name).open('w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=columns, extrasaction='ignore');writer.writeheader();writer.writerows(records)
            files[name] = sha(args.output/name)
    case = dict(id=CASE, passed=passed, records=rows,
                reconstruction_records=local, reference_qualification=qualification,
                metrics={'completed_pde_runs': len(rows), 'local_reconstructions': len(local),
                         'maximum_transport_mass_error': max([r['maximum_mass_change'] for r in rows], default=0)},
                checks={c['name']: c['passed'] for c in checks}, check_details=checks)
    result = dict(schema_version=1, passed=passed, cases=[case], checks={CASE: passed},
                  termination='calculation_failed' if failure else 'fixed_budget_completed', failure=failure,
                  input_sha256=sha(args.input), files_sha256=files,
                  source_sha256={name: sha(ROOT/name) for name in [*contract['files_sha256'], 'pre-run-contract.json']},
                  duration_seconds=time.monotonic()-start)
    save(args.output/'result.json', result)
    print(json.dumps(dict(passed=passed, pde_runs=len(rows), local_reconstructions=len(local), gates=len(checks),
                         failed=[c for c in checks if not c['passed']], failure=failure)), flush=True)
    return 0 if passed else 1


if __name__ == '__main__':raise SystemExit(main())
