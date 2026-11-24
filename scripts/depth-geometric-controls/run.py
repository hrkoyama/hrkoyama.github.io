"""Fixed44-evolution protocol. Every completed candidate precedes diagnostics."""
import argparse
import csv
from decimal import localcontext
import json
import math
from pathlib import Path
import time
import traceback
import numpy as np
import physics as primary
import diagnostics as diag
from io_utils import save_raw, sha, write_json
from references import analytic as exact
from references import discrete


CASE_IDS = ['shake-rattle-pendulum', 'kepler-eccentricity', 'multifrequency-resonance']
GATE_COUNTS = [74, 92, 116]


def numeric_csv(path, columns, values):
    array = np.asarray(values, dtype=float)
    if array.ndim != 2 or array.shape[1] != len(columns) or not len(array) or not np.isfinite(array).all():
        raise ValueError('Numeric CSV must be nonempty, finite and rectangular')
    with Path(path).open('w', newline='') as handle:
        writer = csv.writer(handle); writer.writerow(columns); writer.writerows(array)


def verify_reference(source, cfg_path, acceptance_path):
    root = source/'references/qualified'
    qpath = root/'qualification.json'; q = json.loads(qpath.read_text())
    if q['passed'] is not True or q['failure'] is not None or len(q['checks']) != 67 or not all(v is True for v in q['checks'].values()):
        raise ValueError('Independent67-check qualification must pass before main evolutions')
    if q['input_sha256'] != sha(cfg_path) or q['acceptance_sha256'] != sha(acceptance_path):
        raise ValueError('Reference input/criteria changed')
    for name, expected in q['source_sha256'].items():
        if sha(source/name) != expected:
            raise ValueError('Reference source changed: '+name)
    manifest = json.loads((root/'cache-manifest.json').read_text())
    for name, expected in manifest['files_sha256'].items():
        if sha(root/name) != expected:
            raise ValueError('Reference cache changed: '+name)
    return root, dict(checks=67, passed=True, qualification_sha256=sha(qpath),
                      scope='Qualified analytic and matrix-action algorithms and two separate angular reference evolutions. Author-platform frozen maps are retained as history, not reused as current-platform coefficient maps. Main evaluates current stored coefficients independently.')


class Protocol:
    def __init__(self, source, out, cfg, matrix, reference):
        self.source, self.out, self.cfg = source, out, cfg
        self.matrix, self.reference = matrix, reference
        self.cases = [dict(id=case, passed=False, checks={}, records=[], metrics={}) for case in CASE_IDS]
        self.raws = {}; self.completed = 0; self.map_actions = 0

    def gate(self, case, name, passed):
        if name in case['checks']:
            raise ValueError('Duplicate scientific gate '+name)
        case['checks'][name] = bool(passed)
        self.partial()

    def partial(self):
        write_json(self.out/'protocol.partial.json', dict(cases=self.cases, completed_evolutions=self.completed,
                   completed_reference_map_actions=self.map_actions))

    def evolve(self, row, function):
        tag = row['id']
        def checkpoint(fields):
            save_raw(self.out, tag+'-checkpoint', fields)
        try:
            raw = function(checkpoint)
        except primary.EvolutionFailure as error:
            save_raw(self.out, tag+'-failed', error.payload)
            raise
        # This must remain before ANY reference, derived observable or gate.
        save_raw(self.out, tag, raw)
        self.raws[tag] = raw; self.completed += 1
        self.partial()
        return raw

    def pendulum(self):
        case = self.cases[0]; settings = self.cfg['pendulum']; eps = diag.EPS
        for row in self.matrix:
            if row['case'] != case['id']:
                continue
            method, h, n = row['method'], row['h'], row['steps']
            target = row.get('target', settings['position_target'])
            kwargs = dict(cap=settings['newton_max_iterations'])
            if row['role'] == 'reversal':
                forward = self.raws[row['start_from']]
                if method == 'rattle':
                    kwargs['initial'] = (forward['q'][-1], forward['p'][-1])
                else:
                    kwargs['pair'] = (forward['q'][-1], forward['q'][-2])
            raw = self.evolve(row, lambda callback: primary.pendulum(method, h, n, target,
                               checkpoint=callback, **kwargs))
            if row['role'] == 'reversal':
                forward = self.raws[row['start_from']]
                if method == 'rattle':
                    defect = float(np.linalg.norm(np.r_[raw['q'][-1]-forward['q'][0], raw['p'][-1]-forward['p'][0]]))
                else:
                    defect = float(np.linalg.norm(np.r_[raw['q'][-2]-forward['q'][1], raw['q'][-1]-forward['q'][0]]))
                record = dict(id=row['id'], method=method, role='reversal', steps=n,
                              recovery_defect=defect, raw_file=row['id']+'.npz')
                case['records'].append(record)
                self.gate(case, row['id']+'-finite', np.isfinite(raw['q']).all())
                self.gate(case, row['id']+'-steps', raw['steps_completed'] == n)
                self.gate(case, row['id']+'-recovery', defect <= 2e-8)
                numeric_csv(self.out/(row['id']+'.csv'), ['time', 'qx', 'qy'], np.column_stack((raw['times'], raw['q'])))
                continue
            fields = diag.pendulum_fields(raw, method)
            reference = exact.pendulum(fields['times'])
            state_error = np.sqrt(np.sum((fields['q']-reference['q'])**2+(fields['p']-reference['p'])**2, axis=1))
            energy_error = abs(fields['energy']+math.cos(settings['theta0']))
            constraint, tangent = float(np.max(abs(fields['constraint']))), float(np.max(abs(fields['tangent'])))
            residual_index, iteration_index = (3, 4) if method == 'rattle' else (2, 3)
            solver_target = float(np.max(abs(raw['solves'][:, residual_index])))
            record = dict(id=row['id'], role='primary', method=method, h=h, steps=n,
                          target=target, constraint=constraint, tangent=tangent,
                          max_state_error=float(np.max(state_error)), max_energy_error=float(np.max(energy_error)),
                          max_solver_residual=solver_target, max_solver_updates=float(np.max(raw['solves'][:, iteration_index])),
                          raw_file=row['id']+'.npz', diagnostic_file=row['id']+'-diagnostics.npz',
                          momentum_scope='Full-time constrained momentum' if method == 'rattle' else 'Interior centered momentum; endpoint momentum is absent')
            save_raw(self.out, row['id']+'-diagnostics', dict(**fields, reference_q=reference['q'],
                     reference_p=reference['p'], state_error=state_error, energy_error=energy_error))
            case['records'].append(record)
            for suffix, passed in [('finite', all(np.isfinite(x).all() for x in [raw['q'], fields['p'], raw['solves']])),
                                   ('completed', raw['steps_completed'] == n),
                                   ('constraint', constraint <= target+8*eps),
                                   ('state', record['max_state_error'] <= 20*h*h),
                                   ('energy', record['max_energy_error'] <= 2*h*h+32*n*target),
                                   ('solver', solver_target <= target and record['max_solver_updates'] <= 8)]:
                self.gate(case, row['id']+'-'+suffix, passed)
            if method == 'rattle':
                self.gate(case, row['id']+'-tangent', tangent <= target+64*eps*(1+diag.maxnorm(fields['p'])))
            else:
                discrepancy = float(np.max(abs(fields['tangent']-fields['finite_C_identity'])))
                cjump = float(np.max(abs(fields['constraint'][2:]-fields['constraint'][:-2])))
                self.gate(case, row['id']+'-finite-C-identity', discrepancy <= 32*eps/h)
                self.gate(case, row['id']+'-centered-tangency', tangent <= 2*h*h+cjump/(2*h)+32*eps/h)
                record.update(centered_identity_discrepancy=discrepancy, finite_C_jump=cjump)
            numeric_csv(self.out/(row['id']+'.csv'), ['time', 'qx', 'qy', 'px', 'py'],
                        np.column_stack((fields['times'], fields['q'], fields['p'])))
        for method in settings['methods']:
            records = [r for r in case['records'] if r['role'] == 'primary' and r['method'] == method and r['target'] == settings['position_target']]
            observed = diag.orders([r['max_state_error'] for r in records], [r['h'] for r in records])
            case['metrics'][method+'_observed_orders'] = observed
            self.gate(case, method+'-state-order', min(observed) >= 1.7)
        probes = []
        for i, state in enumerate(settings['map_probes']):
            js = [diag.reduced_jacobian(primary.rattle_step, state, settings['map_h'],
                                       settings['position_target'], delta) for delta in settings['map_difference_steps']]
            save_raw(self.out, 'reduced-map-'+str(i), dict(state=np.asarray(state), jacobians=np.asarray(js)))
            defect = abs(float(js[-1][0, 0]*js[-1][1, 1]-js[-1][0, 1]*js[-1][1, 0])-1)
            consistency = float(np.max(abs(js[0]-js[1])))
            self.gate(case, 'reduced-map-'+str(i)+'-symplectic-proxy', defect <= 2e-6)
            self.gate(case, 'reduced-map-'+str(i)+'-FD-consistency', consistency <= 2e-6)
            probes.append(dict(state=state, symplectic_defect=defect, FD_difference=consistency))
        case['metrics'].update(reduced_map_probes=probes, evolution_count=10,
                               centered_SHAKE_not_RATTLE_tangent=True,
                               maximum_constraint=max(r['constraint'] for r in case['records'] if r['role'] == 'primary'))

    def kepler(self):
        case = self.cases[1]; settings = self.cfg['kepler']; eps = diag.EPS
        for row in self.matrix:
            if row['case'] != case['id']:
                continue
            e = row['eccentricity']; control = row.get('control', 'fixed')
            periods = row.get('periods', settings['long_periods'] if 'variable' in control else 1)
            nper = row.get('steps', settings['long_steps_per_period'])
            kwargs = dict(periods=periods, steps_per_period=nper,
                          variable=control in ('variable', 'variable-regenerated'),
                          cap=settings['variable_max_steps'])
            if row['role'] == 'reversal':
                forward = self.raws[row['start_from']]
                kwargs.update(initial=(forward['q'][-1], forward['p'][-1]), backward=True)
                if control in ('fixed', 'variable-replay'):
                    kwargs['schedule'] = -forward['actual_h'][::-1]
            raw = self.evolve(row, lambda callback: primary.kepler(e, checkpoint=callback, **kwargs))
            numeric_csv(self.out/(row['id']+'.csv'), ['time', 'qx', 'qy', 'px', 'py'],
                        np.column_stack((raw['times'], raw['q'], raw['p'])))
            numeric_csv(self.out/(row['id']+'-steps.csv'), ['step_size'], raw['actual_h'][:, None])
            if row['role'] == 'reversal':
                forward = self.raws[row['start_from']]
                initial = np.r_[forward['q'][0], forward['p'][0]]
                defect = float(np.linalg.norm(np.r_[raw['q'][-1], raw['p'][-1]]-initial))
                n = raw['steps_completed']; label = 'diagnostic_not_time_symmetric' if control == 'variable-regenerated' else 'saved_schedule_reversal'
                record = dict(id=row['id'], role='reversal', control=control, eccentricity=e,
                              recovery_defect=defect, steps=n, reversal_scope=label, raw_file=row['id']+'.npz')
                case['records'].append(record)
                self.gate(case, row['id']+'-finite', np.isfinite(raw['q']).all() and np.isfinite(raw['p']).all())
                count_ok = (n <= settings['variable_max_steps'] and abs(raw['times'][-1]) <= 1e-12*(1+2*math.pi*periods)) if control == 'variable-regenerated' else n == forward['steps_completed']
                self.gate(case, row['id']+'-schedule', count_ok)
                self.gate(case, row['id']+'-recovery-or-diagnostic-scope', label == 'diagnostic_not_time_symmetric' if control == 'variable-regenerated' else defect <= 200*eps*n*(1+float(np.linalg.norm(initial))))
                continue
            fields = diag.kepler_fields(raw); reference = exact.kepler(raw['times'], e)
            state_error = np.sqrt(np.sum((raw['q']-reference['q'])**2+(raw['p']-reference['p'])**2, axis=1))
            energy = float(np.max(abs(fields['energy']+.5)))
            angular = float(np.max(abs(fields['angular']-math.sqrt(1-e*e)))/(1+math.sqrt(1-e*e)))
            maximum_h = float(np.max(abs(raw['actual_h'])))
            record = dict(id=row['id'], role='primary', eccentricity=e, control=control,
                          periods=periods, steps=raw['steps_completed'], max_h=maximum_h,
                          max_state_error=float(np.max(state_error)), max_energy_error=energy,
                          angular_normalized_drift=angular, min_radius=float(np.min(fields['radius'])),
                          raw_file=row['id']+'.npz', diagnostic_file=row['id']+'-diagnostics.npz')
            save_raw(self.out, row['id']+'-diagnostics', dict(**fields, reference_q=reference['q'],
                     reference_p=reference['p'], state_error=state_error))
            case['records'].append(record)
            for suffix, passed in [('finite', np.isfinite(raw['q']).all() and np.isfinite(raw['p']).all()),
                                   ('time', abs(raw['times'][-1]-2*math.pi*periods) <= 1e-12*(1+2*math.pi*periods)),
                                   ('radius', record['min_radius'] >= .05),
                                   ('angular', angular <= 64*eps*raw['steps_completed']),
                                   ('energy', energy <= 200*maximum_h**2),
                                   ('reference', record['max_state_error'] <= 2.)]:
                self.gate(case, row['id']+'-'+suffix, passed)
            if periods == settings['long_periods']:
                events = diag.periapses(raw, settings['root_xtol'], settings['root_rtol'])
                save_raw(self.out, row['id']+'-periapses', events)
                event_error = abs(events['times']-2*math.pi*np.arange(1, len(events['times'])+1))
                record.update(periapsis_count=len(events['times']),
                              max_periapsis_time_error=float(np.max(event_error)) if len(event_error) else 2*math.pi*periods,
                              max_apsidal_angle_drift=float(np.max(abs(fields['apsidal_angle']-fields['apsidal_angle'][0]))))
                self.gate(case, row['id']+'-periapsis-count', len(events['times']) >= 8)
                self.gate(case, row['id']+'-periapsis-time', record['max_periapsis_time_error'] <= .5)
        for e in settings['eccentricities']:
            rows = [r for r in case['records'] if r['role'] == 'primary' and r['eccentricity'] == e and r['periods'] == 1]
            observed = diag.orders([r['max_state_error'] for r in rows], [r['max_h'] for r in rows])
            case['metrics']['e'+str(e)+'_orders'] = observed
            self.gate(case, 'e'+str(e)+'-fine-state', rows[-1]['max_state_error'] <= .03)
            self.gate(case, 'e'+str(e)+'-state-order', min(observed) >= 1.7)
            self.gate(case, 'e'+str(e)+'-fine-energy', rows[-1]['max_energy_error'] <= .02)
        case['metrics'].update(evolution_count=16, variable_map_symplecticity_measured=False,
                               max_state_error=max(r['max_state_error'] for r in case['records'] if r['role'] == 'primary'))

    def coupled(self):
        case = self.cases[2]; settings = self.cfg['coupled']; accuracy = {}
        for row in self.matrix:
            if row['case'] != case['id']:
                continue
            method, omega, n = row['method'], row['omega'], row['steps']
            value = row.get('coefficient')
            h = row['h'] if 'h' in row else (value/omega if method == 'verlet' else (float(value)*math.pi)/float(omega))
            coeff = primary.coefficients(method, omega, settings['alpha'], h)
            raw = self.evolve(row, lambda callback: primary.coupled(method, coeff, n,
                               settings['norm_cap'], checkpoint=callback))
            write_json(self.out/(row['id']+'-coefficients.json'), dict(values=coeff,
                       hexadecimal={key: float(x).hex() for key, x in coeff.items()},
                       theta_requested=(float(value)*math.pi if method == 'impulse' and value is not None else h*omega)))
            # The library sin/cos result can differ by an ulp across platforms.
            # Each oracle uses THIS run's already saved coefficient values/hex,
            # not the author's cached map from a potentially different libm.
            precision_results = []
            precisions = [80, 120] if row['role'] == 'probe' else [80]
            for precision in precisions:
                tag = row['id']+'-reference-D'+str(precision)
                write_json(self.out/(tag+'-active.json'), dict(step=0, initial=[1., 1./omega, 0., 0.], coefficient_file=row['id']+'-coefficients.json'))
                strings = discrete.action(coeff, method, n, precision,
                          raw_callback=lambda step, states: write_json(self.out/(tag+'-active.json'), dict(step=step, states=states)))
                write_json(self.out/(tag+'.json'), [[str(x) for x in state] for state in strings])
                precision_results.append(strings);self.map_actions += 1;self.partial()
            reference = np.asarray(precision_results[-1], dtype=float)
            precision_error = None
            if row['role'] == 'probe':
                with localcontext() as context:
                    context.prec = 140
                    precision_error = float(max(abs(x-y)/(1+abs(y))
                        for low, high in zip(*precision_results) for x, y in zip(low, high)))
            scale = np.asarray([1., 1./omega, 1., 1.])
            discrepancy = abs(raw['states']-reference)
            relative = float(np.max(np.sqrt(np.sum((discrepancy/scale)**2, axis=1))/(1+np.sqrt(np.sum((reference/scale)**2, axis=1)))))
            allowance = discrete.roundoff_allowance(coeff, method, raw['stage_inputs'], reference)
            within_roundoff = bool(np.all(discrepancy <= allowance))
            matrices = discrete.stage_matrices(coeff, method)
            matrix = discrete.mm(matrices[2], discrete.mm(matrices[1], matrices[0]))
            defect = diag.symplectic_defect(matrix)
            coordinate, coupling, energy = diag.coupled_energy(raw['states'], omega)
            record = dict(id=row['id'], role=row['role'], method=method, omega=omega, h=h,
                          steps=raw['steps_completed'], discrete_relative_error=relative,
                          roundoff_bound_satisfied=within_roundoff, normalized_symplectic_defect=defect,
                          max_energy_error=float(np.max(abs(energy-energy[0]))),
                          reference_action_precisions=precisions,
                          raw_file=row['id']+'.npz', diagnostic_file=row['id']+'-diagnostics.npz')
            case['records'].append(record)
            fields = dict(reference=reference, discrepancy=discrepancy, allowance=allowance,
                          coordinate_energy=coordinate, coupling_energy=coupling, total_energy=energy,
                          one_step_matrix=np.asarray(matrix))
            if row['role'] == 'probe':
                if method == 'impulse' and value == 1.:
                    label, ideal = settings['central_actual_classification'].split(';')[0], 'defective_jordan'
                    coherent = label == 'unresolved_near_degeneracy'
                elif method == 'impulse':
                    qualified = json.loads((self.reference/('ideal-class-'+str(omega)+'-'+str(value)+'.json')).read_text())
                    label, ideal = qualified['precision120_class'], qualified['precision120_class']
                    coherent = label in ('stable', 'unstable') and qualified['precision80_class'] == label
                else:
                    # Verlet stability of the true coupled modes, not the uncoupled omega alone.
                    eigenvalues, _ = exact.modes(omega)
                    label = 'stable' if h*h*max(eigenvalues) < 4 else 'unstable'
                    ideal, coherent = label, label in ('stable', 'unstable')
                spectral = np.linalg.eigvals(np.asarray(matrix))
                fields['eigenvalues'] = spectral
                record.update(reference_map_classification=label, ideal_map_classification=ideal,
                              actual_frozen_map_classification=('unresolved_near_degeneracy' if method == 'impulse' and value == 1. else 'raw_spectrum_reported_without_exact_stability_theorem'),
                              actual_frozen_map_spectral_radius=float(np.max(abs(spectral))),
                              classification_scope='Central actual float map unresolved; ideal mathematical pi structure is separate. Off-central classification is explicitly the qualified mathematical reference class. The actual frozen map spectrum and finite action are reported without turning near-unit floating eigenvalues into a theorem.',
                              finite_horizon_amplification=float(np.max(np.sqrt(np.sum((raw['states']/scale)**2, axis=1)))) )
                gates = [('finite-cap', np.isfinite(raw['states']).all() and diag.maxnorm(raw['states']) <= settings['norm_cap']),
                         ('completed', raw['steps_completed'] == 64 and len(raw['states']) == 65),
                         ('discrete-reference', relative <= 2e-10 and precision_error <= 1e-50), ('roundoff', within_roundoff),
                         ('symplectic', defect <= 1e-12), ('classification', coherent)]
                record['current_coefficient_precision_error'] = precision_error
            else:
                continuum = exact.coupled(raw['times'], omega)
                state_error = np.sqrt(np.sum(((raw['states']-continuum)/scale)**2, axis=1))
                eigenvalues, vectors = exact.modes(omega)
                modal = diag.modal_energy(raw['states'], eigenvalues, vectors)
                ref_coordinate, _, _ = diag.coupled_energy(continuum, omega)
                mode_identity = float(np.max(abs(modal.sum(axis=1)-energy)))
                record.update(max_scaled_state_error=float(np.max(state_error)),
                              relative_energy_envelope=record['max_energy_error']/(1+abs(float(energy[0]))),
                              max_coordinate_energy_error=float(np.max(abs(coordinate-ref_coordinate))),
                              modal_energy_identity_error=mode_identity)
                fields.update(continuum=continuum, state_error=state_error, modal_energy=modal,
                              reference_coordinate_energy=ref_coordinate)
                accuracy.setdefault(method, []).append(record)
                gates = [('finite', np.isfinite(raw['states']).all()),
                         ('completed', raw['steps_completed'] == n and abs(raw['times'][-1]-10.) <= 1e-12),
                         ('state', record['max_scaled_state_error'] <= 500*h*h),
                         ('energy', record['max_energy_error'] <= 100*h*h),
                         ('mode', mode_identity <= 256*diag.EPS*(1+float(np.max(abs(energy))))),
                         ('discrete-reference', relative <= 2e-10 and within_roundoff)]
            save_raw(self.out, row['id']+'-diagnostics', fields)
            numeric_csv(self.out/(row['id']+'.csv'), ['time', 'q1', 'q2', 'p1', 'p2'], np.column_stack((raw['times'], raw['states'])))
            for suffix, passed in gates:
                self.gate(case, row['id']+'-'+suffix, passed)
        for method, records in accuracy.items():
            observed = diag.orders([r['max_scaled_state_error'] for r in records], [r['h'] for r in records])
            case['metrics'][method+'_observed_orders'] = observed
            self.gate(case, method+'-state-order', min(observed) >= 1.7)
            self.gate(case, method+'-fine-state', records[-1]['max_scaled_state_error'] <= .02)
            self.gate(case, method+'-fine-relative-H', records[-1]['relative_energy_envelope'] <= .01)
            self.gate(case, method+'-fine-coordinate-energy', records[-1]['max_coordinate_energy_error'] <= .02)
        case['metrics'].update(evolution_count=18, probe_steps=64,
                              ideal_pi_separate_from_actual_float=True,
                              maximum_frozen_map_relative_error=max(r['discrete_relative_error'] for r in case['records']))

    def finish(self):
        for case, count in zip(self.cases, GATE_COUNTS):
            if len(case['checks']) != count or not case['records'] or not case['metrics']:
                raise RuntimeError('Fixed scientific decision inventory changed: '+case['id'])
            case['passed'] = bool(all(case['checks'].values()))
        if self.completed != 44 or self.map_actions != 30:
            raise RuntimeError('Expected44fixed evolutions and30current-coefficient reference actions')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args(); source = Path(__file__).resolve().parent
    if args.input.read_bytes() != (source/'inputs.json').read_bytes():
        raise ValueError('Only the exact frozen input bytes are accepted')
    contract = json.loads((source/'pre-run-contract.json').read_text())
    if any(sha(source/name) != expected for name, expected in contract['files_sha256'].items()):
        raise ValueError('Frozen source/input/reference cache changed')
    out = args.output.resolve(); out.mkdir(parents=True, exist_ok=True)
    if any(out.iterdir()):
        raise FileExistsError('Use a fresh output directory')
    started = time.monotonic(); protocol = None
    result = dict(schema_version=1, passed=False, input_sha256=sha(args.input),
                  checks={case: False for case in CASE_IDS}, cases=[], failure=None,
                  termination='not_completed')
    try:
        cfg = json.loads(args.input.read_text())
        reference, qualification = verify_reference(source, args.input, source/'acceptance.json')
        matrix = json.loads((source/'run-matrix.json').read_text())['main_evolutions']
        protocol = Protocol(source, out, cfg, matrix, reference)
        result['reference_qualification'] = qualification
        protocol.pendulum(); protocol.kepler(); protocol.coupled(); protocol.finish()
        result.update(cases=protocol.cases, checks={c['id']: c['passed'] for c in protocol.cases},
                      passed=bool(all(c['passed'] for c in protocol.cases)),
                      termination='completed_fixed_protocol', completed_evolutions=protocol.completed,
                      completed_reference_map_actions=protocol.map_actions,
                      numerical_gate_count=sum(len(c['checks']) for c in protocol.cases))
    except BaseException as error:
        result['failure'] = dict(type=type(error).__name__, message=str(error), traceback=traceback.format_exc())
        if protocol is not None:
            result.update(cases=protocol.cases, completed_evolutions=protocol.completed,
                          completed_reference_map_actions=protocol.map_actions)
    finally:
        result['duration_seconds'] = time.monotonic()-started
        write_json(out/'result.json', result)
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
