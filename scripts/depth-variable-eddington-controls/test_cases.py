"""Independent fixed numerical/component oracles; execute only from a source freeze.

These tests do not repeat the six main protocol rows. Higher angular integration,
scalar adaptive quadrature and explicit periodic stencil oracles are separate
from the primary FFT transport and conservative FD implementations.
"""
from pathlib import Path
import ast
import copy
import json
import math

# The guard itself imports only standard-library modules. No scientific module
# below is imported from an unfrozen, partially authored public source directory.
from run import check_freeze
check_freeze(Path(__file__).resolve().parent)

import numpy as np
import pytest
from scipy.integrate import quad

import primary
import run
from analytic_reference import reference_fields, mode_response, m1_tensor


HERE = Path(__file__).resolve().parent
DOCUMENT = json.loads((HERE/'inputs.json').read_text())
ACCEPTANCE = json.loads((HERE/'acceptance.json').read_text())
SETTINGS = DOCUMENT['settings']
ST, SS, SA = 4., 3., 1.


def _case(dimension):
    return copy.deepcopy(next(c for c in DOCUMENT['cases'] if c['dimension'] == dimension))


def _points(n, dimension):
    # Independent point-grid construction; no primary.coordinates call.
    axes = [np.arange(n, dtype=float)/n for _ in range(dimension)]
    return tuple(np.meshgrid(*axes, indexing='ij'))


def _quad_response(k):
    """Real adaptive integrations, not the closed arctangent implementation."""
    kernels = [lambda u: ST/(ST*ST+k*k*u*u),
               lambda u: k*u*u/(ST*ST+k*k*u*u),
               lambda u: ST*u*u/(ST*ST+k*k*u*u),
               lambda u: ST*(1-u*u)/(2*(ST*ST+k*k*u*u))]
    result = []
    for function in kernels:
        value, error = quad(function, -1., 1., epsabs=2e-13, epsrel=2e-13, limit=100)
        assert error/2 < 2e-12
        result.append(value/2)
    return tuple(result)


def _coefficient(field, waves, points):
    phase = sum(2*math.pi*k*x for k, x in zip(waves, points))
    return complex(2*np.mean(field*np.exp(-1j*phase)))


def _small_row(dimension, n=9):
    return {'id': 'fixed-component-row', 'shape': [n]*dimension,
            'mu_order': 32 if dimension == 1 else 12,
            **({'phi_order': 48} if dimension == 2 else {})}


def test_primary_source_has_no_reference_dependency_and_inputs_remain_fixed():
    tree = ast.parse((HERE/'primary.py').read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            assert all(x.name not in {'analytic_reference', 'run', 'test_cases'} for x in node.names)
        if isinstance(node, ast.ImportFrom):
            assert node.module not in {'analytic_reference', 'run', 'test_cases'}
    assert (ST, SS, SA) == (SETTINGS['st'], SETTINGS['ss'], SETTINGS['st']-SETTINGS['ss'])
    assert DOCUMENT['expected_primary_rows'] == 6 and DOCUMENT['expected_constant_rows'] == 2
    assert DOCUMENT['settings']['inner_maximum'] == 200
    assert DOCUMENT['settings']['outer_maximum'] == 40
    assert all(n % 2 == 1 for c in DOCUMENT['cases'] for row in c['rows'] for n in row['shape'])


@pytest.mark.parametrize('waves', [(1,), (1, 1)])
def test_analytic_response_matches_independent_adaptive_angular_integrals(waves):
    result = mode_response(list(waves), {'real': .3, 'imag': -.2}, st=ST, ss=SS)
    k = 2*math.pi*math.sqrt(sum(n*n for n in waves))
    independent = _quad_response(k)
    np.testing.assert_allclose([result[x] for x in ['R', 'B', 'C', 'T']], independent,
                               rtol=0, atol=2e-12)
    # The analytic tensor must retain all three angular directions.
    np.testing.assert_allclose(np.trace(result['K']), result['E'], rtol=0, atol=2e-14)


def test_reference_moments_match_independent_higher_sphere_rule_at_three_points():
    case = _case(2)
    points = (np.array([.07, .31, .83]), np.array([.19, .47, .61]))
    expected = reference_fields(case, points, st=ST, ss=SS)
    # This 24x96 rule is fixed and distinct from both primary rules.
    z, wz = np.polynomial.legendre.leggauss(24)
    phi = 2*math.pi*np.arange(96)/96
    directions = np.array([[math.sqrt(1-float(u*u))*math.cos(float(p)),
                            math.sqrt(1-float(u*u))*math.sin(float(p)), float(u)]
                           for u in z for p in phi])
    weights = np.repeat(wz/(2*96), 96)
    intensity = np.ones((len(weights), len(points[0])))
    for mode in case['source']['modes']:
        vector = np.array([2*math.pi*n for n in mode['wave_numbers']]+[0.])
        k = math.sqrt(math.fsum(float(v*v) for v in vector))
        R = _quad_response(k)[0]
        b = complex(mode['amplitude']['real'], mode['amplitude']['imag'])
        amplitude = b/(1-SS*R)
        projection = sum(directions[:, j]*vector[j] for j in range(3))
        phase = sum(vector[j]*points[j] for j in range(2))
        intensity += np.real(amplitude/(ST+1j*projection[:, None])*np.exp(1j*phase)[None, :])
    angular_E = np.sum(weights[:, None]*intensity, axis=0)
    angular_H = np.einsum('m,mp,mi->pi', weights, intensity, directions, optimize=False)
    angular_K = np.einsum('m,mp,mi,mj->pij', weights, intensity, directions, directions, optimize=False)
    # Qualification tolerance is predeclared, not inferred from primary errors.
    np.testing.assert_allclose(angular_E, expected['E'], rtol=0, atol=2e-9)
    np.testing.assert_allclose(angular_H, expected['H'], rtol=0, atol=2e-9)
    np.testing.assert_allclose(angular_K, expected['K'], rtol=0, atol=2e-9)


def test_sine_phase_and_factor_two_mode_normalization_have_independent_oracles():
    case = _case(2)
    points = _points(17, 2)
    q = primary.source_values(case, (17, 17))
    reference = reference_fields(case, points, st=ST, ss=SS)
    for mode in case['source']['modes']:
        waves = mode['wave_numbers']
        b = complex(mode['amplitude']['real'], mode['amplitude']['imag'])
        k = 2*math.pi*math.sqrt(sum(m*m for m in waves))
        R, B, _, _ = _quad_response(k)
        scalar = b*R/(1-SS*R)
        np.testing.assert_allclose(_coefficient(q, waves, points), b, rtol=0, atol=2e-14)
        np.testing.assert_allclose(_coefficient(reference['E'], waves, points), scalar, rtol=0, atol=2e-12)
        khat = np.array(waves+[0.])/math.sqrt(sum(m*m for m in waves))
        for axis in range(3):
            expected = -1j*b*B*khat[axis]/(1-SS*R)
            np.testing.assert_allclose(_coefficient(reference['H'][..., axis], waves, points),
                                       expected, rtol=0, atol=2e-12)
    assert _coefficient(q, [1, 1], points).imag < 0
    # Reversing the sine sign or using b rather than b/2 in both FFT modes fails.
    wanted = complex(0., -.2)
    assert abs(wanted.conjugate()-wanted)/abs(wanted) > .02
    assert abs(2*wanted-wanted)/abs(wanted) > .02


def test_primary_angular_measure_and_slab_transverse_moments_are_full_S2():
    angular = primary.quadrature(2, 12, 48)
    omega, weight = angular['omega'], angular['weights']
    assert np.all(weight > 0)
    np.testing.assert_allclose(np.sum(weight), 1., rtol=0, atol=5e-14)
    np.testing.assert_allclose(np.sum(omega*weight[:, None], axis=0), 0., rtol=0, atol=5e-14)
    second = np.einsum('m,mi,mj->ij', weight, omega, omega, optimize=False)
    np.testing.assert_allclose(second, np.eye(3)/3, rtol=0, atol=5e-14)
    slab = primary.quadrature(1, 32)
    mu, weight = slab['omega'][:, 0], slab['weights']
    np.testing.assert_allclose(np.sum(weight*mu*mu), 1/3, rtol=0, atol=5e-14)
    np.testing.assert_allclose(np.sum(weight*(1-mu*mu)/2), 1/3, rtol=0, atol=5e-14)
    assert slab['axisymmetric'] and np.all(slab['omega'][:, 1:] == 0)


@pytest.mark.parametrize('shape', [(8,), (9, 8), (9, 11)])
def test_even_or_unequal_point_grids_are_rejected_before_transform(shape):
    with pytest.raises(ValueError):
        primary.coordinates(shape)


@pytest.mark.parametrize('mu', [.37, -.61])
def test_formal_fft_ray_uses_actual_LO_feedback_and_correct_complex_sign(mu):
    n = 9
    x = np.arange(n)/n
    q = 1+.3*np.cos(2*math.pi*x)
    trial = 1+.04*np.sin(2*math.pi*x)
    angular = {'omega': np.array([[mu, 0., 0.]]), 'weights': np.ones(1), 'axisymmetric': True}
    result = primary.formal_transport(q, trial, angular, SETTINGS)
    source_amplitude = .3-.12j
    wanted = 1+np.real(source_amplitude/(ST+1j*mu*2*math.pi)*np.exp(2j*math.pi*x))
    np.testing.assert_allclose(result['I'][0], wanted, rtol=0, atol=2e-13)
    np.testing.assert_allclose(result['source'], q+SS*trial, rtol=0, atol=2e-14)
    frozen = primary.formal_transport(q, trial, angular, SETTINGS, feedback='frozen-initial')
    assert float(np.max(np.abs(frozen['I'][0]-wanted))) > 1e-3


def test_shared_face_fluxes_match_explicit_loop_oracle_and_full_nine_point_operator():
    n, h = 9, 1/9
    x, y = _points(n, 2)
    E = 1+.1*np.cos(2*math.pi*x)
    D = np.broadcast_to(np.eye(3)/3, E.shape+(3, 3)).copy()
    D[..., 0, 0] += .02*np.cos(2*math.pi*y)
    D[..., 1, 1] -= .01*np.cos(2*math.pi*y)
    D[..., 2, 2] -= .01*np.cos(2*math.pi*y)
    D[..., 0, 1] = D[..., 1, 0] = .015*np.sin(2*math.pi*(x+y))
    P = D*E[..., None, None]
    fx, fy, oracle = np.empty_like(E), np.empty_like(E), np.empty_like(E)
    cross = np.empty_like(E)
    for i in range(n):
        for j in range(n):
            ip, im, jp, jm = (i+1) % n, (i-1) % n, (j+1) % n, (j-1) % n
            fx[i, j] = -(P[ip, j, 0, 0]-P[i, j, 0, 0])/(h*ST)-(P[ip, jp, 0, 1]+P[i, jp, 0, 1]-P[ip, jm, 0, 1]-P[i, jm, 0, 1])/(4*h*ST)
            fy[i, j] = -(P[i, jp, 1, 1]-P[i, j, 1, 1])/(h*ST)-(P[ip, jp, 0, 1]+P[ip, j, 0, 1]-P[im, jp, 0, 1]-P[im, j, 0, 1])/(4*h*ST)
            dxx = (P[ip, j, 0, 0]-2*P[i, j, 0, 0]+P[im, j, 0, 0])/(h*h)
            dyy = (P[i, jp, 1, 1]-2*P[i, j, 1, 1]+P[i, jm, 1, 1])/(h*h)
            cross[i, j] = 2*(P[ip, jp, 0, 1]-P[ip, jm, 0, 1]-P[im, jp, 0, 1]+P[im, jm, 0, 1])/(4*h*h)
            oracle[i, j] = ST*SA*E[i, j]-dxx-dyy-cross[i, j]
    actual = primary.face_fluxes(E, D, ST)
    np.testing.assert_allclose(actual[0], fx, rtol=0, atol=2e-14)
    np.testing.assert_allclose(actual[1], fy, rtol=0, atol=2e-14)
    np.testing.assert_allclose(primary.moment_operator(E, D, ST, SA), oracle, rtol=0, atol=2e-12)
    local_budget = ST*(SA*E+primary.face_divergence((fx, fy)))
    np.testing.assert_allclose(local_budget, oracle, rtol=0, atol=2e-12)
    assert abs(float(np.mean(primary.face_divergence((fx, fy))))) < 2e-14
    assert float(np.max(np.abs(cross))) > 1e-3
    assert float(np.max(np.abs((oracle+cross)-oracle))) > 1e-3


def test_constant_tensor_preconditioner_is_the_declared_FD_operator_not_a_spectral_laplacian():
    n = 9
    x, y = _points(n, 2)
    mode = np.cos(2*math.pi*(x+y))
    target = 1+.1*mode
    D = np.broadcast_to(np.eye(3)/3, target.shape+(3, 3)).copy()
    symbol = ST*SA+8*n*n*math.sin(math.pi/n)**2/3
    oracle = ST*SA+.1*symbol*mode
    np.testing.assert_allclose(primary.moment_operator(target, D, ST, SA), oracle, rtol=0, atol=2e-12)
    computed, work = primary.solve_inner(oracle/ST, D, np.ones_like(target), SETTINGS)
    np.testing.assert_allclose(computed, target, rtol=0, atol=2e-12)
    assert work['iterations'] <= 2


@pytest.mark.parametrize('dimension', [1, 2])
def test_constant_control_has_absolute_errors_and_no_zero_flux_relative_division(dimension):
    case = _case(dimension)
    case['source'] = {'mean': 1., 'modes': []}
    row = _small_row(dimension)
    solution = primary.solve(case, row, SETTINGS)
    arrays = run.arrays_for_row(case, row, solution, SETTINGS)
    metrics = run.row_metrics(case, row, solution, arrays)
    limits = ACCEPTANCE['constant_control_absolute_checks']
    assert float(np.max(np.abs(solution['I']-1))) <= limits['I_E_max_error']
    assert metrics['E_absolute_max_error'] <= limits['I_E_max_error']
    assert metrics['face_H_absolute_max_error'] <= limits['H_face_max_error']
    assert metrics['D_component_max_abs_error'] <= limits['D_max_error']
    assert metrics['face_H_relative_rms_error'] is None
    assert metrics['maximum_source_mode_complex_relative_error'] is None


def test_isotropic_closure_negative_fails_the_same_independent_complex_mode_gate():
    case = _case(1)
    row = _small_row(1, 17)
    solution = primary.solve(case, row, SETTINGS, closure='isotropic')
    x = _points(17, 1)
    actual = _coefficient(solution['E_LO'], [1], x)
    R = _quad_response(2*math.pi)[0]
    wanted = .3*R/(1-SS*R)
    error = abs(actual-wanted)/abs(wanted)
    assert error > ACCEPTANCE['required_case_checks']['finest_complex_mode_relative_amplitude_error_max']


def test_frozen_scattering_feedback_negative_fails_the_same_mode_gate():
    case = _case(1)
    row = _small_row(1, 17)
    solution = primary.solve(case, row, SETTINGS, feedback='frozen-initial')
    actual = _coefficient(solution['E_LO'], [1], _points(17, 1))
    R = _quad_response(2*math.pi)[0]
    wanted = .3*R/(1-SS*R)
    assert abs(actual-wanted)/abs(wanted) > ACCEPTANCE['required_case_checks']['finest_complex_mode_relative_amplitude_error_max']


def test_physical_reference_cross_term_catches_zero_or_flipped_Dxy_even_if_PSD_survives():
    n = 17
    case = _case(2)
    points = _points(n, 2)
    ref = reference_fields(case, points, st=ST, ss=SS)
    D = ref['D']
    zero = D.copy()
    zero[..., 0, 1] = zero[..., 1, 0] = 0
    flipped = D.copy()
    flipped[..., 0, 1] *= -1
    flipped[..., 1, 0] *= -1
    full = primary.moment_operator(ref['E'], D, ST, SA)
    no_cross = primary.moment_operator(ref['E'], zero, ST, SA)
    wrong_sign = primary.moment_operator(ref['E'], flipped, ST, SA)
    source_mode = case['source']['modes'][1]
    k = 2*math.pi*math.sqrt(2)
    R, _, C, T = _quad_response(k)
    b = complex(source_mode['amplitude']['real'], source_mode['amplitude']['imag'])
    coefficient = b*(C-T)/(2*(1-SS*R))
    discrete_cross = 2*n*n*math.sin(2*math.pi/n)**2
    exact = np.real(discrete_cross*coefficient*np.exp(2j*math.pi*(points[0]+points[1])))
    np.testing.assert_allclose(full-no_cross, exact, rtol=0, atol=2e-12)
    np.testing.assert_allclose(wrong_sign-no_cross, -exact, rtol=0, atol=2e-12)
    assert float(np.max(np.abs(exact))) > 1e-3


def test_M1_is_only_a_diagnostic_and_does_not_replace_the_exact_variable_factor():
    case = _case(1)
    ref = reference_fields(case, (np.array([0., .25, .5]),), st=ST, ss=SS)
    M1 = m1_tensor(ref['E'], ref['H'])
    np.testing.assert_allclose(M1[0], np.eye(3)/3, rtol=0, atol=2e-14)
    assert ref['D'][0, 0, 0] < 1/3
    assert abs(float(ref['D'][0, 0, 0])-1/3) > 1e-3
    assert float(np.min(np.linalg.eigvalsh(ref['D']))) > 0
    reduced = ref['H']/ref['E'][..., None]
    covariance = ref['D']-reduced[..., :, None]*reduced[..., None, :]
    assert float(np.min(np.linalg.eigvalsh(covariance))) > -1e-12


def test_centered_LO_flux_owns_realizability_metric_at_the_same_energy_points():
    case = _case(1)
    case['source'] = {'mean': 1., 'modes': []}
    row = _small_row(1)
    E = np.ones(9)
    D = np.broadcast_to(np.eye(3)/3, (9, 3, 3)).copy()
    H = np.zeros((9, 3))
    faces = (np.full(9, .4),)
    arrays = {'x': np.arange(9)/9, 'E_LO': E, 'E_reference': E.copy(),
              'E_HO': E.copy(), 'H_HO': H.copy(), 'H_reference': H.copy(),
              'D': D, 'D_reference': D.copy(), 'H_LO_center': primary.centered_flux(faces),
              'Fx_face': faces[0], 'Hx_reference_face': np.zeros(9)}
    metrics = run.row_metrics(case, row, {'history': [{}], 'work': {}}, arrays)
    assert abs(metrics['LO_flux_realizability_excess']-(-.6)) < 1e-14
    assert metrics['HO_flux_realizability_excess'] == -1
    assert metrics['face_H_relative_rms_error'] is None


def test_failed_inner_candidate_is_owned_and_saved_before_failure_metadata(tmp_path):
    class StopAtCandidate(RuntimeError):
        pass
    saved = {}
    def stop(state):
        if state['phase'] == 'inner-candidate':
            saved.update(state)
            raise StopAtCandidate('fixed failure-ownership component control')
    with pytest.raises(StopAtCandidate):
        primary.solve(_case(1), _small_row(1), SETTINGS, deadline=stop)
    assert isinstance(saved['E_failed_candidate'], np.ndarray)
    assert isinstance(saved['E_accepted'], np.ndarray)
    assert not np.shares_memory(saved['E_failed_candidate'], saved['E_accepted'])
    receipt = run.save_failure_arrays(tmp_path, saved)
    with np.load(tmp_path/receipt['file'], allow_pickle=False) as archive:
        np.testing.assert_array_equal(archive['active__E_failed_candidate'], saved['E_failed_candidate'])
        np.testing.assert_array_equal(archive['active__E_accepted'], saved['E_accepted'])
