"""The complete small fixed protocol; every comparison uses saved candidate arrays."""
from fractions import Fraction
import json
import math
from pathlib import Path
import numpy as np
from scipy.interpolate import CubicSpline, PchipInterpolator
import interpolation as I
import splines as S
import haar as H
from references import polynomials as RP
from references import spline_rational as RS
from references import haar_matrix as RH


class Study:
    def __init__(self, ident, output):
        self.result = {'id': ident, 'passed': False, 'checks': {}, 'records': [], 'metrics': {}}
        self.output = Path(output)
        self.active = {}

    def check(self, name, condition):
        if name in self.result['checks']:
            raise ValueError('Repeated check '+name)
        self.result['checks'][name] = bool(condition)

    def candidate(self, **arrays):
        self.active = {k: np.array(v, copy=True) for k, v in arrays.items()}

    def save(self, name, **arrays):
        self.candidate(**arrays)
        if not all(np.isfinite(a).all() for a in self.active.values()):
            np.savez(self.output/(name+'-nonfinite-candidate.npz'), **self.active)
            raise ArithmeticError('Nonfinite saved candidate '+name)
        np.savez_compressed(self.output/(name+'.npz'), **self.active)

    def finish(self):
        self.result['passed'] = bool(self.result['checks']) and all(self.result['checks'].values())
        return self.result


def interpolation_study(cfg, limits, study):
    count = cfg['probe_count']
    probes = -1.0+(2*np.arange(count)+1)/count
    indices = cfg['certificate_probe_indices']
    node_defect = max(RP.cosine_node_defects(cfg['positive_cosine32_decimal']))
    study.check('reference:fixed-cosine-node-table', node_defect <= limits['node_cosine_abs_max'])
    errors, coefficient_sets = {}, 0
    for function in cfg['functions']:
        for degree in cfg['degrees']:
            for family in cfg['node_families']:
                key = f'{function}-{family}-{degree}'
                nodes, weights = I.nodes_weights(degree, family, cfg['positive_cosine32_decimal'])
                data = I.target(function, nodes)
                truth = np.array([float(RP.exact_function(function, x)) for x in probes])
                value, denominator = np.zeros(count), np.zeros(count)
                study.candidate(nodes=nodes, weights=weights, data=data, probes=probes, completed_values=value)
                value = study.active['completed_values']
                study.active['denominator'] = denominator
                for j, x in enumerate(probes):
                    study.active['current_probe_index'] = np.array(j)
                    value[j], denominator[j], _ = I.barycentric(nodes, data, weights, x)
                # Persist the completed primary field before any reference arithmetic.
                study.save(key+'-candidate', nodes=nodes, weights=weights, data=data, probes=probes, values=value, denominator=denominator, truth=truth)
                bary_ref, poly_ref, representation, cert_bound, cert_defect, guard, lebesgue = [], [], [], [], [], [], []
                bary_pass, normal = True, True
                exact_audit = {'barycentric': [], 'clenshaw': []}
                clenshaw_values, c_ref, c_representation, c_bound, c_defect = np.empty(0), [], [], [], []
                coefficients, table, clenshaw_pass = np.empty(0), np.empty((0, 0)), True
                for j in indices:
                    actual, _, trace = I.barycentric(nodes, data, weights, probes[j])
                    certificate = RP.barycentric_certificate(nodes, data, weights, probes[j], actual, trace)
                    bary_ref.append(float(certificate['reference']))
                    polynomial = RP.direct_lagrange(nodes, data, probes[j])
                    poly_ref.append(float(polynomial))
                    representation.append(float(abs(certificate['reference']-polynomial)))
                    cert_bound.append(float(certificate['bound']));cert_defect.append(float(certificate['defect']))
                    guard.append(float(certificate['guard_ratio']));lebesgue.append(float(certificate['lebesgue']))
                    bary_pass &= certificate['passed'];normal &= certificate['normal']
                    exact_audit['barycentric'].append({'probe_index': j, 'P_stored': str(polynomial),
                        **{k: str(v) if isinstance(v, Fraction) else bool(v) for k, v in certificate.items()}})
                    (study.output/(key+'-exact-certificate.json')).write_text(json.dumps(exact_audit, indent=2)+'\n')
                if family == 'lobatto':
                    coefficient_sets += 1
                    coefficients, table = I.chebyshev_coefficients(nodes, data)
                    clenshaw_values = np.array([I.clenshaw(coefficients, x)[0] for x in probes])
                    study.save(key+'-coefficient-candidate', coefficients=coefficients, table=table, values=clenshaw_values)
                    for j in indices:
                        actual, trace, final = I.clenshaw(coefficients, probes[j])
                        certificate = RP.clenshaw_certificate(coefficients, probes[j], actual, trace, final)
                        c_ref.append(float(certificate['reference']));c_bound.append(float(certificate['bound']));c_defect.append(float(certificate['defect']))
                        c_representation.append(float(abs(certificate['reference']-RP.direct_lagrange(nodes, data, probes[j]))))
                        clenshaw_pass &= certificate['passed'] and certificate['normal']
                        exact_audit['clenshaw'].append({'probe_index': j,
                            **{k: str(v) if isinstance(v, Fraction) else bool(v) for k, v in certificate.items()}})
                        (study.output/(key+'-exact-certificate.json')).write_text(json.dumps(exact_audit, indent=2)+'\n')
                    study.check(key+':clenshaw-operation-certificate', clenshaw_pass)
                error = float(np.max(np.abs(value-truth)))
                errors[(function, family, degree)] = error
                row = {'id': key, 'function': function, 'nodes': family, 'degree': degree,
                       'sampled_max_error': error, 'sampled_RMS_error': float(np.sqrt(np.mean((value-truth)**2))),
                       'max_closed_weight_representation_defect': max(representation),
                       'max_barycentric_roundoff_bound': max(cert_bound), 'max_barycentric_roundoff_defect': max(cert_defect),
                       'maximum_certificate_guard_ratio': max(guard), 'maximum_weighted_Lebesgue': max(lebesgue)}
                if family == 'lobatto':
                    row.update({'clenshaw_sampled_max_error': float(np.max(np.abs(clenshaw_values-truth))),
                                'max_coefficient_representation_defect': max(c_representation)})
                study.result['records'].append(row)
                study.save(key, nodes=nodes, weights=weights, data=data, probes=probes, values=value,
                           denominator=denominator, truth=truth, errors=value-truth,
                           certificate_indices=indices, R_closed=bary_ref, P_stored=poly_ref,
                           closed_weight_representation_defect=representation, barycentric_bound=cert_bound, barycentric_defect=cert_defect,
                           denominator_guard_ratio=guard, weighted_Lebesgue=lebesgue,
                           coefficients=coefficients, coefficient_basis_table=table,
                           clenshaw_values=clenshaw_values, C_stored=c_ref, coefficient_representation_defect=c_representation, clenshaw_bound=c_bound, clenshaw_defect=c_defect)
                study.check(key+':finite', np.isfinite(value).all() and np.isfinite(denominator).all())
                study.check(key+':node-hit-identity', all(I.barycentric(nodes, data, weights, x)[0] == y for x, y in zip(nodes, data)))
                study.check(key+':barycentric-operation-certificate', bary_pass and normal and max(guard) < 1)
    for family in cfg['node_families']:
        nodes, weights = I.nodes_weights(cfg['polynomial_control_degree'], family, cfg['positive_cosine32_decimal'])
        data = I.target('polynomial', nodes)
        control = np.array([I.barycentric(nodes, data, weights, x)[0] for x in probes])
        study.check('reference:polynomial-control-'+family, np.max(np.abs(control-I.target('polynomial', probes))) <= limits['polynomial_control_abs_max'])
    study.check('runge:equispaced-growth', errors[('runge', 'equispaced', 32)] > limits['equispaced_runge_growth_min']*errors[('runge', 'equispaced', 16)])
    study.check('runge:lobatto-refinement', errors[('runge', 'lobatto', 32)] < limits['lobatto_runge_refinement_max']*errors[('runge', 'lobatto', 16)])
    study.check('fixed-record-and-coefficient-count', len(study.result['records']) == limits['records'] and coefficient_sets == limits['coefficient_sets'])
    study.result['metrics'] = {'max_node_table_cosine_defect': node_defect, 'maximum_sampled_function_error': max(errors.values()),
                               'reference_certificate_probes_per_interpolant': len(indices), 'coefficient_sets': coefficient_sets}
    return study.finish()


def _jet(row, x, order):
    a, b, c, d = row
    return a+b*x+c*x*x+d*x*x*x if order == 0 else b+2*c*x+3*d*x*x if order == 1 else 2*c+6*d*x


def _shape(x, coefficients):
    minimum = math.inf
    for i, (a, b, c, d) in enumerate(coefficients):
        h = float(x[i+1]-x[i])
        secant = _jet(coefficients[i], h, 0)-a
        sign = np.sign(secant)
        points = [0.0, h]
        if d != 0 and 0 < -c/(3*d) < h:
            points.append(float(-c/(3*d)))
        for q in points:
            minimum = min(minimum, float(sign*_jet(coefficients[i], q, 1)))
    return minimum


def spline_study(cfg, limits, study):
    endpoint_records, endpoint_outputs, datasets, endpoint_ok = [], [], set(), True
    for row in cfg['endpoint_left_controls']:
        for side in ('left', 'right'):
            y = row['y'] if side == 'left' else row['y'][::-1]
            expected = Fraction(row['expected'])*(1 if side == 'left' else -1)
            slopes = S.pchip_slopes([0, 1, 2], y)
            actual = float(slopes[0 if side == 'left' else -1])
            endpoint_ok &= Fraction.from_float(actual) == expected
            endpoint_records.append({'id': row['id']+'-'+side, 'x': [0, 1, 2], 'y': y, 'side': side, 'actual': actual, 'expected': float(expected)})
            endpoint_outputs.append(actual);datasets.add(json.dumps([[0, 1, 2], y]))
    row = cfg['two_point_control'];actual = S.pchip_slopes(row['x'], row['y'])
    endpoint_ok &= all(Fraction.from_float(float(a)) == Fraction(b) for a, b in zip(actual, row['expected']))
    endpoint_records.append({'id': 'two-point', 'x': row['x'], 'y': row['y'], 'side': 'both', 'actual': actual.tolist(), 'expected': [float(Fraction(x)) for x in row['expected']]})
    endpoint_outputs.extend(actual.tolist());datasets.add(json.dumps([row['x'], row['y']]))
    (study.output/'endpoint-reference-records.json').write_text(json.dumps(endpoint_records, indent=2)+'\n')
    study.check('reference:endpoint-branch-values', endpoint_ok)
    study.check('reference:endpoint-record-count', len(endpoint_records) == limits['endpoint_records'])
    study.check('reference:endpoint-output-count', len(endpoint_outputs) == limits['endpoint_scalar_outputs'])
    study.check('reference:endpoint-distinct-datasets', len(datasets) == limits['endpoint_distinct_datasets'])
    plateau = cfg['datasets'][0]
    cert = RS.plateau_certificates(plateau['y'][0], plateau['y'][-1])
    (study.output/'plateau-exact-input-oracle.json').write_text(json.dumps({k: str(v) for k, v in cert.items()}, indent=2)+'\n')
    for kind in ('natural', 'clamped'):
        study.check('reference:negative-'+kind+'-witness', cert['witness_a'] and cert['witness_delta'] and cert[kind] < 0)
    continuity, polynomial_controls = True, {}
    for dataset in cfg['datasets']:
        x = np.array(dataset['x'], dtype=float)
        y = np.array(dataset['y'], dtype=float) if 'y' in dataset else x**3-2*x+1 if dataset['function'] == 'cubic' else 1+x/2
        grid = np.linspace(x[0], x[-1], cfg['probe_count'])
        for kind in cfg['methods']:
            key = dataset['id']+'-'+kind
            if kind == 'pchip':
                slopes = S.pchip_slopes(x, y);coeff = S.hermite_coefficients(x, y, slopes)
                values = np.array([S.power_evaluate(x, coeff, grid, order) for order in range(3)])
                model = {'knots': np.empty(0), 'coefficients': coeff, 'matrix': np.empty((0, 0)), 'rhs': np.empty(0)}
                study.save(key+'-candidate', x=x, y=y, probes=grid, values=values, **model)
                xr, cr, _ = RS.pchip_coefficients(x, y)
                companion = PchipInterpolator(x, y)
                nodal = S.power_evaluate(x, coeff, x)
                boundary_defect = max(0.0, -_shape(x, coeff))
            else:
                model = S.fit(x, y, kind, dataset['endpoint_slopes'], observe=study.candidate)
                values = np.array([S.evaluate(model, grid, order) for order in range(3)])
                study.save(key+'-candidate', x=x, y=y, probes=grid, values=values, **model)
                xr, cr, _ = RS.c2_coefficients(x, y, kind, dataset['endpoint_slopes'])
                bc = 'natural' if kind == 'natural' else ((1, dataset['endpoint_slopes'][0]), (1, dataset['endpoint_slopes'][1]))
                companion = CubicSpline(x, y, bc_type=bc)
                nodal = S.evaluate(model, x)
                boundary_defect = float(np.max(np.abs(S.evaluate(model, [x[0], x[-1]], 2)))) if kind == 'natural' else float(np.max(np.abs(S.evaluate(model, [x[0], x[-1]], 1)-dataset['endpoint_slopes'])))
            reference = np.array([[float(RS.evaluate(xr, cr, z, order)) for z in grid] for order in range(3)])
            companion_values = np.array([companion(grid, order) for order in range(3)])
            defect = np.max(np.abs(values-reference)/(1+np.abs(reference)), axis=1)
            companion_defect = float(np.max(np.abs(companion_values-reference)/(1+np.abs(reference))))
            for i in range(len(cr)-1):
                h = xr[i+1]-xr[i]
                for order in range(2 if kind == 'pchip' else 3):
                    continuity &= _jet(cr[i], h, order) == _jet(cr[i+1], Fraction(0), order)
            if dataset['id'] == 'linear' and kind in ('natural', 'clamped') or dataset['id'] == 'cubic' and kind == 'clamped':
                truth = grid**3-2*grid+1 if dataset['id'] == 'cubic' else 1+grid/2
                polynomial_controls[key] = float(np.max(np.abs(values[0]-truth)))
            if dataset['id'] == 'plateau' and kind == 'pchip':
                t = np.clip(grid-2, 0, 1)
                expected = float(y[0])+(float(y[-1])-float(y[0]))*(3*t*t-2*t*t*t)
                study.check('reference:pchip-actual-input-plateau', np.max(np.abs(values[0]-expected)) <= limits['value_scaled_max'])
            row = {'id': key, 'dataset': dataset['id'], 'method': kind, 'value_scaled_defect': float(defect[0]),
                   'derivative_scaled_defect': float(max(defect[1:])), 'companion_scaled_defect': companion_defect,
                   'minimum_value': float(np.min(values[0])), 'maximum_value': float(np.max(values[0])),
                   'nodal_maxabs': float(np.max(np.abs(nodal-y))), 'boundary_or_shape_defect': boundary_defect}
            study.result['records'].append(row)
            study.save(key, x=x, y=y, probes=grid, values=values, reference=reference, companion=companion_values,
                       reference_power_coefficients=np.array([[float(v) for v in a] for a in cr]), **model)
            study.check(key+':finite', np.isfinite(values).all())
            study.check(key+':value-reference', defect[0] <= limits['value_scaled_max'])
            study.check(key+':derivative-reference', max(defect[1:]) <= limits['derivative_scaled_max'] and companion_defect <= limits['derivative_scaled_max'])
            study.check(key+':nodal', row['nodal_maxabs'] <= limits['value_scaled_max']*(1+np.max(np.abs(y))))
            study.check(key+':boundary-or-shape', boundary_defect <= limits['shape_roundoff_max']*(1+np.max(np.abs(y))))
    study.check('reference:exact-piece-continuity', continuity)
    for name, value in polynomial_controls.items():study.check('reference:polynomial-'+name, value <= limits['value_scaled_max'])
    study.check('fixed-fit-count', len(study.result['records']) == limits['records'])
    study.result['metrics'] = {'maximum_value_scaled_reference_defect': max(r['value_scaled_defect'] for r in study.result['records']),
                               'maximum_derivative_scaled_reference_defect': max(r['derivative_scaled_defect'] for r in study.result['records']),
                               'endpoint_fixture_records': len(endpoint_records), 'endpoint_scalar_outputs': len(endpoint_outputs), 'endpoint_distinct_datasets': len(datasets)}
    return study.finish()


def haar_study(cfg, limits, study):
    saved, analyses = {}, 0
    goldens = [(np.array([1., 1., 0., 0.]), [1., 1., 0., 0.]), (np.array([1., -1., 1., -1.]), None)]
    for i, (signal, expected) in enumerate(goldens):
        primary = H.flatten(H.analyze(signal, 2, 'periodic'))
        reference, _ = RH.exact_coefficients(signal, 2, 'periodic')
        study.check('reference:golden-'+str(i), np.max(np.abs(primary-reference)) <= limits['dense_map_scaled_max'] and (expected is None or np.max(np.abs(primary-expected)) <= limits['dense_map_scaled_max']))
    for spec in cfg['signals']:
        n = spec['length'];j = np.arange(n)
        signal = np.sin(2*np.pi*j/n)+0.25*np.cos(6*np.pi*j/n) if spec['kind'] == 'smooth' else j/(n-1) if spec['kind'] == 'ramp' else (j >= n//2).astype(float)
        signal = np.roll(signal, spec['shift'])
        for mode in cfg['boundary_rules']:
            analyses += 1
            model = H.analyze(signal, cfg['levels'], mode)
            original_coeff = H.flatten(model)
            study.save(spec['id']+'-'+mode+'-candidate', signal=signal, coefficients=original_coeff, lengths=model['lengths'], pads=model['pads'], energy_ledger=model['energy_ledger'])
            analysis, synthesis = RH.matrices(n, cfg['levels'], mode)
            exact, exact_padding = RH.exact_coefficients(signal, cfg['levels'], mode)
            matrix_defect = float(np.max(np.abs(np.einsum('ij,jk->ik', synthesis, analysis)-np.eye(n))))
            oracle_coeff = np.einsum('ij,j->i', analysis, signal)
            scale = 1+float(np.max(np.abs(signal)))
            analysis_name = spec['id']+'-'+mode
            study.check(analysis_name+':independent-analysis', max(np.max(np.abs(original_coeff-oracle_coeff)), np.max(np.abs(original_coeff-exact))) <= limits['dense_map_scaled_max']*scale)
            study.check(analysis_name+':left-inverse', matrix_defect <= limits['dense_map_scaled_max'])
            study.check(analysis_name+':coefficient-count', len(original_coeff) == limits['coefficient_counts'][str(n)])
            ledger = model['energy_ledger']
            study.check(analysis_name+':padding-energy-ledger', np.max(np.abs(ledger[:, 2]-ledger[:, 0]-ledger[:, 1])) <= limits['energy_scaled_max']*(1+np.sum(signal*signal)) and abs(float(np.sum(model['pads']**2))-float(exact_padding)) <= limits['energy_scaled_max'])
            for threshold in cfg['thresholds']:
                changed = H.threshold(model, threshold['id'], threshold['tau'])
                coefficients = H.flatten(changed)
                reconstructed = H.synthesize(changed)
                key = analysis_name+'-'+threshold['id']
                study.save(key+'-candidate', signal=signal, reconstructed=reconstructed,
                           coefficients=coefficients, original_coefficients=original_coeff)
                independent = np.einsum('ij,j->i', synthesis, coefficients)
                error = reconstructed-signal
                squared_error = float(np.sum(error*error))
                coefficient_delta = float(np.sum((coefficients-original_coeff)**2))
                base_id = spec['id'].replace('-shift1', '')
                shift_defect = 0.0
                if spec['shift']:
                    shift_defect = float(np.sum((np.roll(reconstructed, -spec['shift'])-saved[(base_id, mode, threshold['id'])])**2))
                saved[(spec['id'], mode, threshold['id'])] = reconstructed.copy()
                detail_flat = np.concatenate(changed['details'])
                row = {'id': key, 'signal': spec['id'], 'length': n, 'boundary': mode, 'shift_samples': spec['shift'], 'threshold': threshold['id'], 'tau': threshold['tau'],
                       'reconstruction_l2_squared': squared_error, 'reconstruction_Linf': float(np.max(np.abs(error))),
                       'coefficient_delta_l2_squared': coefficient_delta, 'shift_back_equivariance_l2_squared': shift_defect,
                       'signal_l2_squared': float(np.sum(signal*signal)), 'padding_energy': float(np.sum(model['pads']**2)),
                       'retained_details': int(np.count_nonzero(detail_flat)), 'total_coefficients': len(coefficients)}
                study.result['records'].append(row)
                study.save(key, signal=signal, reconstructed=reconstructed, error=error, original_coefficients=original_coeff,
                           coefficients=coefficients, independent_reconstruction=independent, analysis=analysis, synthesis=synthesis,
                           lengths=model['lengths'], pads=model['pads'], energy_ledger=ledger)
                study.check(key+':finite-and-owned-shape', np.isfinite(reconstructed).all() and reconstructed.shape == signal.shape)
                study.check(key+':independent-synthesis', np.max(np.abs(reconstructed-independent)) <= limits['dense_map_scaled_max']*scale)
                if threshold['id'] == 'none':study.check(key+':perfect-reconstruction', np.max(np.abs(error)) <= limits['reconstruction_scaled_max']*scale)
                if n == 32:study.check(key+':critical-squared-error-identity', abs(squared_error-coefficient_delta) <= limits['energy_scaled_max']*(1+row['signal_l2_squared']))
    study.check('fixed-analysis-and-reconstruction-count', analyses == limits['analysis_records'] and len(study.result['records']) == limits['records'])
    study.result['metrics'] = {'analysis_records': analyses, 'maximum_reconstruction_l2_squared': max(r['reconstruction_l2_squared'] for r in study.result['records']),
                               'maximum_shift_back_equivariance_l2_squared': max(r['shift_back_equivariance_l2_squared'] for r in study.result['records'])}
    return study.finish()
