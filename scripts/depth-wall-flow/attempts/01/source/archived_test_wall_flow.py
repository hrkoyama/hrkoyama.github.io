"""Twenty meaningful checks; tiny probes do not replay the main refinement batch."""
import hashlib
import json
from pathlib import Path
import numpy as np
import pytest
import wall_flow as s
import run as runner
from references.qualify_reference import ghia, polynomial_reference, qualify


def grid(n=9):
    x = np.linspace(0, 1, n)
    return np.meshgrid(x, x), 1/(n-1)


def test_01_dirichlet_poisson_discrete_eigenmode():
    (X, Y), h = grid()
    exact = np.sin(np.pi*X)*np.sin(2*np.pi*Y)
    boundary = np.zeros_like(X)
    rhs = (4*np.sin(np.pi*h/2)**2+4*np.sin(np.pi*h)**2)/h**2*exact[1:-1, 1:-1]
    assert np.max(abs(s.poisson_dirichlet(rhs, boundary, h)-exact)) < 2e-15


def test_02_nonzero_dirichlet_boundaries_are_actually_used():
    (X, Y), h = grid()
    exact = X*X+Y*Y+X*Y
    out = s.poisson_dirichlet(np.full((7, 7), -4.), exact, h)
    assert np.max(abs(out-exact)) < 2e-15


def test_03_poisson_interior_does_not_leak_boundary_array_interior():
    (X, Y), h = grid(); dirty = np.zeros_like(X); dirty[1:-1, 1:-1] = 123.
    assert np.max(abs(s.poisson_dirichlet(np.zeros((7, 7)), dirty, h))) == 0


def test_04_poisson_shape_rejected():
    with pytest.raises(ValueError): s.poisson_dirichlet(np.zeros((3, 4)), np.zeros((5, 5)), .25)


def test_05_cavity_lid_sign_and_stationary_corners():
    (X, _), h = grid(); _, _, w, u, v = s.stage(np.zeros((7, 7)), h, .01, 1., np.zeros((7, 7)))
    assert np.all(w[-1, 1:-1] == -2/h)
    assert np.all(u[-1, 1:-1] == 1) and np.all(u[-1, [0, -1]] == 0)
    assert np.max(abs(v)) == 0


def test_06_stationary_wall_closure_uses_adjacent_streamfunction():
    (X, Y), h = grid(); psi = 8*X**2*(1-X)**2*Y**2*(1-Y)**2
    w = s.thom_wall(np.zeros_like(X), psi, h, 0.)
    assert np.array_equal(w[0, 1:-1], -2*psi[1, 1:-1]/h**2)
    assert np.array_equal(w[1:-1, -1], -2*psi[1:-1, -2]/h**2)


def test_07_corners_do_not_enter_five_point_transport_stencil():
    (X, Y), h = grid(); q = X+Y; changed = q.copy(); changed[[0, -1], 0] = 1e9; changed[[0, -1], -1] = -1e9
    assert np.array_equal(s.laplacian(q, h), s.laplacian(changed, h))


def test_08_interior_velocity_orientation_matches_known_streamfunction():
    (X, Y), h = grid(); u, v = s.velocity(X*Y, h, 0.)
    assert np.max(abs(u[1:-1, 1:-1]-X[1:-1, 1:-1])) == 0
    assert np.max(abs(v[1:-1, 1:-1]+Y[1:-1, 1:-1])) == 0


def test_09_constructed_discrete_velocity_is_solenoidal():
    (X, Y), h = grid(); p = s.manufactured(X, Y)['psi']; u, v = s.velocity(p, h, 0.)
    div = (u[1:-1, 2:]-u[1:-1, :-2]+v[2:, 1:-1]-v[:-2, 1:-1])/(2*h)
    assert np.max(abs(div)) < 1e-15


def test_10_manufactured_fields_match_independent_polynomial_derivatives():
    (X, Y), _ = grid(); exact = polynomial_reference(X, Y, 8., .01); actual = s.manufactured(X, Y)
    for k in ['psi', 'u', 'v', 'omega', 'forcing']:
        assert np.max(abs(exact[k]-actual[k])) < 3e-11


def test_11_analytic_forcing_is_not_discrete_residual_injection():
    defects = []
    for n in [9, 17]:
        (X, Y), h = grid(n); a = s.manufactured(X, Y)
        rhs, _, _, _, _ = s.stage(a['omega'][1:-1, 1:-1], h, .01, 0., a['forcing'][1:-1, 1:-1])
        cut = n//4
        defects.append(np.max(abs(rhs[cut:-cut, cut:-cut])))
    assert defects[0] > 1e-4 and defects[1] < defects[0]


def test_12_thom_truncation_is_reported_as_first_order():
    errs = []
    for n in [17, 33]:
        (X, Y), h = grid(n); a = s.manufactured(X, Y); w = s.thom_wall(np.zeros_like(X), a['psi'], h, 0.)
        errs.append(np.max(abs(w[0, 1:-1]-a['omega'][0, 1:-1])))
    assert .9 < np.log2(errs[0]/errs[1]) < 1.1


def test_13_nonperiodic_gradient_exact_for_quadratic():
    (X, Y), h = grid(); px, py = s.gradient(X*X+Y*Y+X*Y, h)
    assert np.max(abs(px-2*X-Y)) == 0 and np.max(abs(py-2*Y-X)) == 0


def test_14_separate_pressure_gradient_converges():
    errors = []
    for n in [9, 17]:
        p = s.pressure_manufactured(n)
        errors.append(runner.rms(p['px']-p['px_exact']))
    assert errors[0]/errors[1] > 3


def test_15_zero_force_stationary_flow_stays_zero():
    out = s.solve(9, lid=0., maximum_time=.02, check_every=1)
    assert out['residual'] == 0 and np.max(abs(out['psi'])) == 0 and out['converged']


def test_16_short_real_cavity_develops_negative_streamfunction():
    out = s.solve(9, maximum_time=.02, check_every=1)
    assert out['psi'].min() < 0 and out['omega'][-1, 4] < 0
    assert out['state_clip_count'] == out['retries'] == 0


def test_17_bad_grid_and_viscosity_rejected():
    with pytest.raises(ValueError): s.solve(8)
    with pytest.raises(ValueError): s.solve(9, viscosity=-1.)


def test_18_primary_transcription_endpoint_and_extrema():
    t = ghia()
    assert t['u'].shape == t['v'].shape == (17, 2)
    assert np.min(t['u'][:, 1]) == -.21090 and np.min(t['v'][:, 1]) == -.24533
    assert t['u'][0, 1] == 1 and t['v'][0, 1] == 0


def test_19_independent_reference_qualification():
    assert qualify(s.manufactured)['passed']


def test_20_frozen_contract_and_three_dependency_pins():
    root = Path(__file__).resolve().parent
    contract = runner.verify_contract()
    assert contract['declared_before_first_pde_run'] is True
    assert set((root/'requirements.txt').read_text().splitlines()) == {'numpy==2.0.2', 'scipy==1.14.1', 'pytest==8.3.5'}
    assert hashlib.sha256((root/'inputs.json').read_bytes()).hexdigest() == contract['files_sha256']['inputs.json']
