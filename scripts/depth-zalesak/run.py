#!/usr/bin/env python3
"""Run the fixed eight 2D scalar rotations and retain every stage diagnostic."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import rotation as solver
from references import geometry
from references.qualify_reference import qualify

ROOT = Path(__file__).resolve().parent
CASE = 'zalesak-rotation'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def check_frozen_sources(root=ROOT):
    root = Path(root)
    contract = json.loads((root/'pre-run-contract.json').read_text())
    for name, expected in contract['files_sha256'].items():
        if sha(root/name) != expected:
            raise ValueError('Changed frozen scientific source/input: '+name)
    return contract


def fixed_runs(cfg):
    rows = [dict(id=f'base-{method}-n{n}', family='refinement', n=n,
                 method=method, shift_cells=0., angle0=0.)
            for n in cfg['grids'] for method in cfg['methods']]
    rows += [dict(row, family=row['id']) for row in cfg['diagnostics']]
    return rows


def geometry_arguments(cfg, run):
    shift = run['shift_cells']/run['n']
    return dict(rotation_center=tuple(v+shift for v in cfg['rotation_center']),
                shape_center=tuple(v+shift for v in cfg['shape_center']),
                radius=cfg['radius'], slot_width=cfg['slot_width'],
                slot_top=cfg['slot_top']+shift)


def discrete_centroid(q, h):
    x = (np.arange(len(q))+.5)*h
    mass_sum = q.sum()
    if mass_sum <= 0:
        raise ArithmeticError('Require a positive represented mass')
    return np.array([(q*x[None, :]).sum(), (q*x[:, None]).sum()])/mass_sum


def slot_probe(edges, angle, args):
    """Exact rectangular overlap weights for an inner empty-slot probe.

    The reported mean is an area-weighted mean of piecewise-constant cell
    means over this probe, not a pointwise or subcell reconstruction value.
    """
    lo = (args['shape_center'][0]-args['slot_width']/4,
          args['shape_center'][1]-.1)
    hi = (args['shape_center'][0]+args['slot_width']/4,
          args['slot_top']-.025)
    n = len(edges)-1
    xl, yl = np.meshgrid(edges[:-1], edges[:-1])
    xr, yr = np.meshgrid(edges[1:], edges[1:])
    x = np.stack((xl, xr, xr, xl), axis=-1)
    y = np.stack((yl, yl, yr, yr), axis=-1)
    x0, y0 = geometry.inverse_points(x, y, angle, args['rotation_center'])
    vertices = np.stack((x0, y0), axis=-1)
    minimum, maximum = vertices.min(axis=-2), vertices.max(axis=-2)
    outside = ((maximum[..., 0] <= lo[0]) | (minimum[..., 0] >= hi[0])
               | (maximum[..., 1] <= lo[1]) | (minimum[..., 1] >= hi[1]))
    inside = ((minimum[..., 0] >= lo[0]) & (maximum[..., 0] <= hi[0])
              & (minimum[..., 1] >= lo[1]) & (maximum[..., 1] <= hi[1]))
    weights = np.zeros((n, n));weights[inside] = 1.
    for j, i in np.argwhere(~outside & ~inside):
        polygon = vertices[j, i]
        for normal, bound in [((-1., 0.), -lo[0]), ((1., 0.), hi[0]),
                              ((0., -1.), -lo[1]), ((0., 1.), hi[1])]:
            polygon = geometry.clip_halfplane(polygon, normal, bound)
        if len(polygon) >= 3:
            area = .5*abs(np.sum(polygon[:, 0]*np.roll(polygon[:, 1], -1)
                                    -polygon[:, 1]*np.roll(polygon[:, 0], -1)))
            weights[j, i] = area/((edges[i+1]-edges[i])*(edges[j+1]-edges[j]))
    if weights.sum() <= 0:
        raise ArithmeticError('Empty slot probe')
    return weights


def measure(out, references, edges, cfg, run, args):
    q, n = out['q'], run['n'];h = 1./n
    stages = {name: out['stage_data'][:, i]
              for i, name in enumerate(out['stage_columns'])}
    analytic_area = geometry.total_area(cfg['radius'], cfg['slot_width'],
                                       cfg['slot_top']-cfg['shape_center'][1])
    quarter_l1, centroid_distances, continuum_centroid_gaps = [], [], []
    for numerical, reference, stamp in zip(out['snapshots'], references, out['snapshot_times']):
        quarter_l1.append(float(h*h*np.sum(abs(numerical-reference))/analytic_area))
        centroid_distances.append(float(np.linalg.norm(discrete_centroid(numerical, h)
                                                       -discrete_centroid(reference, h))))
        exact_center = geometry.centroid(angle=run['angle0']+cfg['omega']*stamp, **args)
        continuum_centroid_gaps.append(float(np.linalg.norm(discrete_centroid(reference, h)-exact_center)))
    probe = slot_probe(edges, run['angle0']+cfg['omega']*out['time'], args)
    width = cfg['boundary_band_width']
    edge_weights = (np.minimum(h, np.maximum(0., width-edges[:-1]))
                    +np.minimum(h, np.maximum(0., edges[1:]-(1-width))))/h
    band = 1-(1-edge_weights[:, None])*(1-edge_weights[None, :])
    mass = out['initial_mass']
    row = {**run, 'time': out['time'], 'steps': out['steps'],
           'stages': len(out['stage_data']), 'snapshots': len(out['snapshot_times']),
           'relative_l1': quarter_l1[-1],
           'l1_absolute': float(h*h*np.sum(abs(q-references[-1]))),
           'linf': float(abs(q-references[-1]).max()),
           'relative_l2': float(np.sqrt(h*h*np.sum((q-references[-1])**2)/analytic_area)),
           'initial_mass': mass, 'final_mass': out['final_mass'],
           'mass_change': out['final_mass']-mass,
           'initial_area_error': abs(mass-analytic_area),
           'reference_area_error': max(abs(h*h*r.sum()-analytic_area) for r in references),
           'reference_return_maximum': float(abs(references[-1]-references[0]).max()),
           'minimum': min(float(stages[k].min()) for k in ['face_min', 'fe_min', 'rk_min']),
           'maximum': max(float(stages[k].max()) for k in ['face_max', 'fe_max', 'rk_max']),
           'maximum_courant': float(stages['courant'].max()),
           'maximum_mean_preservation_defect': float(stages['mean_preservation_defect'].max()),
           'maximum_fe_mass_defect': float(stages['fe_mass_defect'].max()),
           'maximum_rk_mass_defect': float(stages['rk_mass_defect'].max()),
           'maximum_discrete_divergence': out['divergence_max'],
           'slot_probe_mean': float(np.sum(probe*q)/probe.sum()),
           'slot_probe_reference_mean': float(np.sum(probe*references[-1])/probe.sum()),
           'slot_probe_excess': float(np.sum(probe*(q-references[-1]))/probe.sum()),
           'slot_probe_weight_sum': float(probe.sum()),
           'boundary_band_width': width,
           'boundary_band_mass_fraction': float(h*h*np.sum(q*band)/mass),
           'total_variation': float(h*(abs(np.roll(q, -1, 0)-q).sum()
                                       +abs(np.roll(q, -1, 1)-q).sum())),
           'state_clip_count': out['state_clip_count'], 'retries': out['retries'],
           'rejected_steps': out['rejected_steps'],
           'snapshot_times': out['snapshot_times'].tolist(),
           'snapshot_relative_l1': quarter_l1,
           'snapshot_discrete_centroid_distances': centroid_distances,
           'reference_discrete_to_continuum_centroid_distances': continuum_centroid_gaps,
           'all_saved_values_finite': bool(np.all(np.isfinite(out['snapshots']))
                                          and np.all(np.isfinite(out['stage_data'])))}
    return row, probe


def decisions(rows, reference, cfg, limits):
    checks = []
    def add(name, value, bound, passed):
        checks.append(dict(name=name, value=value, bound=bound, passed=bool(passed)))
    add('all eight fixed rotations completed', [r['id'] for r in rows],
        [r['id'] for r in fixed_runs(cfg)], [r['id'] for r in rows] == [r['id'] for r in fixed_runs(cfg)])
    tolerance = cfg['bounds_roundoff_tolerance']
    targets = np.linspace(0., cfg['final_time'], 5).tolist()
    for row in rows:
        p = row['id']+': '
        for name, value, bound, passed in [
                ('final time', row['time'], cfg['final_time'], row['time'] == cfg['final_time']),
                ('initial represented area', row['initial_area_error'], limits['reference_area'], row['initial_area_error'] <= limits['reference_area']),
                ('periodic mass conservation', abs(row['mass_change']), limits['mass_balance'], abs(row['mass_change']) <= limits['mass_balance']),
                ('three FE records per SSP step', row['stages'], 3*row['steps'], row['stages'] == 3*row['steps']),
                ('finite saved means and stage data', row['all_saved_values_finite'], True, row['all_saved_values_finite']),
                ('all stage lower bounds', row['minimum'], -tolerance, row['minimum'] >= -tolerance),
                ('all stage upper bounds', row['maximum'], 1+tolerance, row['maximum'] <= 1+tolerance),
                ('sufficient individual face Courant', row['maximum_courant'], cfg['sufficient_face_courant'], row['maximum_courant'] <= cfg['sufficient_face_courant']),
                ('four-face mean preserved', row['maximum_mean_preservation_defect'], limits['reconstruction_mean'], row['maximum_mean_preservation_defect'] <= limits['reconstruction_mean']),
                ('each FE shared-flux balance', row['maximum_fe_mass_defect'], limits['mass_balance'], row['maximum_fe_mass_defect'] <= limits['mass_balance']),
                ('each SSP convex-mean balance', row['maximum_rk_mass_defect'], limits['mass_balance'], row['maximum_rk_mass_defect'] <= limits['mass_balance']),
                ('all rotated reference areas', row['reference_area_error'], limits['reference_area'], row['reference_area_error'] <= limits['reference_area']),
                ('full-turn geometric return', row['reference_return_maximum'], 3e-12, row['reference_return_maximum'] <= 3e-12),
                ('zero clipping and retries', row['state_clip_count']+row['retries']+row['rejected_steps'], 0, row['state_clip_count']+row['retries']+row['rejected_steps'] == 0),
                ('exact discrete velocity divergence', row['maximum_discrete_divergence'], 0, row['maximum_discrete_divergence'] == 0),
                ('quarter-turn snapshots retained', row['snapshot_times'], targets, row['snapshot_times'] == targets)]:
            add(p+name, value, bound, passed)
    base = [r for r in rows if r['family'] == 'refinement']
    if len(base) == 6:
        finest = {}
        for method, key in [('donor-cell', 'finest_donor_relative_l1'), ('muscl-minmod', 'finest_muscl_relative_l1')]:
            seq = sorted([r for r in base if r['method'] == method], key=lambda r: r['n'])
            finest[method] = seq[-1]
            add(method+' finest relative L1', seq[-1]['relative_l1'], limits[key], seq[-1]['relative_l1'] <= limits[key])
            for index in [1, 2]:
                ratio = seq[index]['relative_l1']/seq[index-1]['relative_l1']
                add(method+' refinement ratio '+str(index), ratio, limits['consecutive_refinement_ratio'], ratio <= limits['consecutive_refinement_ratio'])
            for k in [1, 2, 3]:
                value = seq[-1]['snapshot_relative_l1'][k]
                bound = limits['finest_quarter_relative_l1']
                add(method+' intermediate relative L1 '+str(k), value, bound, value <= bound)
                value = seq[-1]['snapshot_discrete_centroid_distances'][k]
                bound = limits['finest_quarter_discrete_centroid_distance']
                add(method+' intermediate centroid distance '+str(k), value, bound, value <= bound)
        ratio = finest['muscl-minmod']['relative_l1']/finest['donor-cell']['relative_l1']
        add('finest MUSCL/donor relative L1', ratio, limits['finest_muscl_to_donor_l1'], ratio <= limits['finest_muscl_to_donor_l1'])
    for row in rows:
        if row['family'] != 'refinement':
            add(row['id']+' shape error', row['relative_l1'], limits['diagnostic_relative_l1'], row['relative_l1'] <= limits['diagnostic_relative_l1'])
    for name, passed in reference.get('checks', {}).items():
        add('independent geometry: '+name, passed, True, passed)
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=ROOT/'inputs.json')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    contract = check_frozen_sources()
    if sha(args.input) != contract['files_sha256']['inputs.json']:
        raise ValueError('Use the unchanged frozen input bytes')
    cfg = json.loads(args.input.read_text())['cases'][CASE]
    limits = json.loads((ROOT/'acceptance.json').read_text())['limits']
    if args.output.exists() and any(args.output.iterdir()):
        raise ValueError('Use a new or empty output directory')
    args.output.mkdir(parents=True, exist_ok=True)
    start, rows, files, failure, reference = time.monotonic(), [], {}, None, {}
    try:
        reference = qualify()
        if len(reference['checks']) != 8 or not all(reference['checks'].values()):
            raise ArithmeticError('Independent geometric qualification failed')
        for run in fixed_runs(cfg):
            n = run['n'];edges = np.linspace(0., 1., n+1)
            geo = geometry_arguments(cfg, run)
            initial = geometry.cell_averages(edges, angle=run['angle0'], **geo)
            out = solver.solve(initial, run['method'], geo['rotation_center'],
                               cfg['final_time'], cfg['omega'], cfg['face_courant'],
                               cfg['bounds_roundoff_tolerance'], cfg['max_steps'])
            refs = np.array([geometry.cell_averages(edges, angle=run['angle0']+cfg['omega']*t, **geo)
                             for t in out['snapshot_times']])
            row, probe = measure(out, refs, edges, cfg, run, geo)
            field, history = 'field-'+run['id']+'.npz', 'stages-'+run['id']+'.npz'
            np.savez_compressed(args.output/field, q=out['q'], q_initial=initial,
                                q_reference=refs[-1], q_history=out['snapshots'],
                                q_reference_history=refs, edges=edges,
                                snapshot_times=out['snapshot_times'], slot_probe_weights=probe)
            np.savez_compressed(args.output/history, values=out['stage_data'],
                                columns=np.array(out['stage_columns']))
            row.update(field=field, history=history,
                       geometric_roundoff=[geometry.cell_average_diagnostics(
                           edges, angle=run['angle0']+cfg['omega']*t, **geo)
                                          for t in out['snapshot_times']])
            files[field], files[history] = sha(args.output/field), sha(args.output/history)
            rows.append(row)
    except Exception as error:
        failure = {'type': type(error).__name__, 'message': str(error)}
        if hasattr(error, 'state'):
            np.savez_compressed(args.output/'failed-state.npz', q=error.state,
                                stage_data=np.array(error.history))
            failure['context'] = error.context
    checks = decisions(rows, reference, cfg, limits)
    passed = failure is None and len(checks) == 158 and all(c['passed'] for c in checks)
    columns = ['id', 'n', 'method', 'steps', 'relative_l1', 'linf', 'mass_change',
               'minimum', 'maximum', 'slot_probe_mean', 'boundary_band_mass_fraction']
    with (args.output/(CASE+'.csv')).open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction='ignore')
        writer.writeheader();writer.writerows(rows)
    finest_id = 'base-muscl-minmod-n'+str(cfg['grids'][-1])
    metrics = next((r for r in rows if r['id'] == finest_id), {})
    case = {'id': CASE, 'passed': passed, 'records': rows,
            'metrics': {k: v for k, v in metrics.items() if isinstance(v, (int, float))},
            'checks': {c['name']: c['passed'] for c in checks}, 'check_details': checks,
            'reference_qualification': reference}
    result = dict(schema_version=1, passed=passed, checks={CASE: passed}, cases=[case],
                  termination='calculation_failed' if failure else 'fixed_budget_completed',
                  input_sha256=sha(args.input), files_sha256=files,
                  source_sha256={name: sha(ROOT/name) for name in [*contract['files_sha256'], 'pre-run-contract.json']},
                  failure=failure, duration_seconds=time.monotonic()-start)
    save(args.output/'result.json', result)
    print(json.dumps({'passed': passed, 'runs': len(rows), 'gates': len(checks),
                      'failed': [c for c in checks if not c['passed']], 'failure': failure}), flush=True)
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
