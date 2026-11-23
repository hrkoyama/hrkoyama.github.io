"""Twenty-seven limited-scope checks; fixed PDE refinements run separately."""
import numpy as np
import pytest
import euler_positivity as s
from references import double_rarefaction as exact
from references.numart_reference_riemann import RiemannSolution


def base():
    left, right = s.conserved(1., -2., .4), s.conserved(1., 2., .4)
    q = np.repeat(left[None], 8, axis=0); q[4:] = right
    return q, left, right


def test_01_pressure_roundtrip():
    assert np.allclose(s.pressure(s.conserved([1., 2.], [3., -2.], [.4, 2.])), [.4, 2.])


def test_02_equal_lf_flux_consistent():
    q = s.conserved(1., .2, .4)
    assert np.array_equal(s.global_lf(q, q, 4.), s.physical_flux(q))


def test_03_nonfinite_state_rejected():
    with pytest.raises(s.StageFailure): s.admissible([[1., np.nan, 3.]])


def test_04_negative_density_rejected():
    with pytest.raises(s.StageFailure): s.admissible([[-1., 0., 1.]])


def test_05_negative_pressure_rejected():
    with pytest.raises(s.StageFailure): s.admissible([[1., 2., 1.]])


def test_06_fixed_lf_speed_violation_rejected():
    q, l, r = base()
    with pytest.raises(s.StageFailure): s.global_lf(l, r, 1.)


def test_07_excessive_cfl_rejected():
    q, l, r = base()
    with pytest.raises(ValueError): s.forward_euler(q, l, r, .125, .02)


def test_08_raw_endpoint_mean_identity():
    q, l, r = base()
    assert np.array_equal(s.raw_endpoints(q, l, r).mean(axis=1), q)


def test_09_raw_pressure_negativity_exercised():
    q, l, r = base()
    assert s.pressure(s.raw_endpoints(q, l, r)).min() < 0


def test_10_scaling_preserves_conserved_means():
    q, l, r = base(); u, theta = s.scale_endpoints(q, s.raw_endpoints(q, l, r))
    assert np.max(abs(u.mean(axis=1)-q)) < 2e-15


def test_11_scaling_makes_both_endpoints_admissible():
    q, l, r = base(); u, theta = s.scale_endpoints(q, s.raw_endpoints(q, l, r))
    assert np.min(u[..., 0]) > 0 and np.min(s.pressure(u)) > 0


def test_12_theta_is_one_common_cell_factor():
    q, l, r = base(); raw = s.raw_endpoints(q, l, r); u, theta = s.scale_endpoints(q, raw)
    assert np.all((theta > 0)&(theta <= 1)) and np.any(theta < 1)
    assert np.array_equal(u, q[:, None]+theta[:, None, None]*(raw-q[:, None]))


def test_13_uniform_state_scaling_is_identity():
    q, l, r = base(); q[:] = l; raw = s.raw_endpoints(q, l, l)
    u, theta = s.scale_endpoints(q, raw)
    assert np.array_equal(u, raw) and np.all(theta == 1)


def test_14_invalid_reconstruction_target_rejected():
    q, l, r = base()
    with pytest.raises(ValueError): s.scale_endpoints(q, s.raw_endpoints(q, l, r), 0.)


def test_15_mean_below_target_cannot_be_repaired():
    q = np.array([s.conserved(1., 0., 1e-15)])
    with pytest.raises(s.StageFailure): s.scale_endpoints(q, np.repeat(q[:, None], 2, axis=1))


def test_16_nonfinite_reconstruction_rejected():
    q, l, r = base(); raw = s.raw_endpoints(q, l, r); raw[0, 0, 0] = np.nan
    with pytest.raises(ValueError): s.scale_endpoints(q, raw)


def test_17_lax_friedrichs_split_states_positive():
    q, l, r = base(); u, theta = s.scale_endpoints(q, s.raw_endpoints(q, l, r))
    for sign in [-1., 1.]: s.admissible(u+sign*s.physical_flux(u)/4.)


def test_18_fe_convex_decomposition_identity():
    q, l, r = base(); dt, dx, alpha = .01, .125, 4.
    u, theta = s.scale_endpoints(q, s.raw_endpoints(q, l, r))
    lm = np.concatenate((l[None], u[:-1, 1])); rp = np.concatenate((u[1:, 0], r[None]))
    z = dt*alpha/dx
    decomposition = (.5*(1-z)*(u[:, 0]+u[:, 1])
                     +.5*z*(lm+s.physical_flux(lm)/alpha)
                     +.5*z*(rp-s.physical_flux(rp)/alpha)
                     +.5*z*(s.physical_flux(u[:, 0])-s.physical_flux(u[:, 1]))/alpha)
    # Endpoint self-flux term is regrouped below into positive split states
    positive = (.5*(1-2*z)*(u[:, 0]+u[:, 1])
                +.5*z*(u[:, 0]+s.physical_flux(u[:, 0])/alpha)
                +.5*z*(u[:, 1]-s.physical_flux(u[:, 1])/alpha)
                +.5*z*(lm+s.physical_flux(lm)/alpha)
                +.5*z*(rp-s.physical_flux(rp)/alpha))
    updated, budget, stats = s.forward_euler(q, l, r, dx, dt, alpha)
    assert np.allclose(updated, positive, rtol=0, atol=1e-15)
    assert np.allclose(updated, decomposition, rtol=0, atol=1e-15)


def test_19_forward_euler_boundary_conservation():
    q, l, r = base(); updated, budget, stats = s.forward_euler(q, l, r, .125, .01)
    assert np.max(abs(.125*(updated-q).sum(axis=0)-budget)) < 1e-15


def test_20_all_three_actual_ssp_stages_recorded():
    out = s.solve(16, final_time=.005)
    assert len(out['stage_history']) == 3*out['steps']
    assert {r['stage'] for r in out['stage_history']} == {1, 2, 3}


def test_21_all_ssp_combination_means_positive():
    out = s.solve(16, final_time=.005)
    assert min(r['rk_mean_min_pressure'] for r in out['stage_history']) > 0
    assert min(r['rk_mean_min_density'] for r in out['stage_history']) > 0


def test_22_ssp_flux_weights_boundary_conservation():
    out = s.solve(16, final_time=.005)
    assert np.max(abs(out['final_integral']-out['initial_integral']-out['boundary_net_integral'])) < 2e-15
    assert out['state_floor_count'] == out['rejected_steps'] == out['retries'] == 0


def test_23_symmetric_reference_star_matches_independent_root():
    ref = RiemannSolution('euler', [1., -2., .4], [1., 2., .4], 1.4)
    center = exact.conserved(np.array([.5]), .15)[0]
    assert abs(s.pressure(center)-ref.star) < 2e-13
    assert center[0] > 0 and 0 < s.pressure(center) < .002


def test_24_reference_points_match_independent_riemann_evaluator():
    ref = RiemannSolution('euler', [1., -2., .4], [1., 2., .4], 1.4)
    x = np.linspace(0, 1, 97)
    assert np.max(abs(exact.conserved(x, .15)-ref.point(x, .15, origin=.5))) < 2e-12


def test_25_split_gauss_reference_cell_means_agree():
    edges = np.linspace(0., 1., 65)
    means = exact.cell_averages(edges, .15, order=8)
    assert np.max(abs(means-exact.cell_averages(edges, .15, order=16))) < 2e-12
    # Exact fan heads remain inside [0,1]. Initial integral [1,0,3]
    # plus .15 times the far-field flux difference [-4,0,-13.6].
    assert np.max(abs(np.sum(means*np.diff(edges)[:, None], axis=0)-[.4, 0., .96])) < 2e-13


def test_26_reference_and_numerical_reflection_symmetry():
    out = s.solve(16, final_time=.005); q = out['q']; mirror = q[::-1].copy(); mirror[:, 1] *= -1
    assert np.max(abs(q-mirror)) < 4e-15
    qref = exact.conserved(np.linspace(0, 1, 31), .15)
    mirror = qref[::-1].copy(); mirror[:, 1] *= -1
    assert np.max(abs(qref-mirror)) < 4e-15


def test_27_raw_zero_density_diagnostic_does_not_divide_by_zero():
    raw = np.array([[[0., 1., 2.], [2., -1., 2.]]])
    with np.errstate(all='raise'):
        diagnostic = s.raw_diagnostics(raw)
    assert diagnostic['raw_endpoint_nonpositive_density_count'] == 1
    assert np.isfinite(diagnostic['raw_endpoint_min_pressure'])
