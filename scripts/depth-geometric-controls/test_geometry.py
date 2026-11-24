"""32 fixed tests: small operators, negative controls, ownership and retention.

Small test trajectories precede main in the public verifier. Reference-first
ordering refers specifically to the separately counted44 main evolutions.
"""
import importlib.metadata
import json
import math
from pathlib import Path
from fractions import Fraction
import numpy as np
import pytest
import physics as p
import diagnostics as d
import run
from references import analytic as a
from references import discrete as f


def initial(theta=.7, omega=0.):
    return (math.sin(theta), -math.cos(theta)), (omega*math.cos(theta), omega*math.sin(theta))


def test_initial_constraint_and_units():
    q, v = initial(); assert abs(p.dot(q, q)-1) <= 4*d.EPS
    assert p.dot(v, v) == 0 and abs(q[1]+math.cos(.7)) <= d.EPS


def test_continuous_root_and_closed_scalar_oracle():
    q, v = initial(.3, .2); h = .02
    aa = (q[0]+h*v[0], q[1]+h*v[1]-h*h/2)
    new, eta, _, _, _ = p.position(aa, q, 1e-13)
    aq, qq, aa2 = p.dot(aa, q), p.dot(q, q), p.dot(aa, aa)
    oracle = (aa2-1)/(aq+math.sqrt(aq*aq-qq*(aa2-1)))
    assert abs(eta-oracle) <= 2e-13 and p.dot(q, new) > 0


def test_newton_branch_and_target():
    q, v = initial(); new, _, info, trace = p.rattle_step(q, v, .04, 1e-13)
    assert abs(info[3]) <= 1e-13 and info[4] <= 8
    assert len(trace) == info[4]+1 and p.dot(q, new) > 0


def test_rattle_final_tangent_impulse():
    q, v = initial(.3, .2); new, momentum, _, _ = p.rattle_step(q, v, .04, 1e-13)
    assert abs(p.dot(new, momentum)) <= 32*d.EPS


def test_omitted_velocity_impulse_negative_control():
    q, v = initial(.3, .2)
    new, omitted, _, _ = p.rattle_step(q, v, .04, 1e-13, omit_final=True)
    _, corrected, _, _ = p.rattle_step(q, v, .04, 1e-13)
    assert abs(p.dot(new, omitted)) > 1e-6
    assert abs(p.dot(new, corrected)) < abs(p.dot(new, omitted))*1e-6


def test_finite_C_centered_identity():
    q = np.array([[.6, -.8], [.61, -.795], [.62, -.79]])
    raw = dict(q=q, h=.02, times=np.array([0., .02, .04]))
    fields = d.pendulum_fields(raw, 'shake')
    assert np.max(abs(fields['tangent']-fields['finite_C_identity'])) <= 64*d.EPS/.02


def test_SHAKE_endpoint_ownership():
    raw = p.pendulum('shake', .02, 4, 1e-13)
    fields = d.pendulum_fields(raw, 'shake')
    assert 'p' not in raw and fields['p'].shape == (3, 2)
    assert np.array_equal(fields['times'], raw['times'][1:-1])
    assert raw['solves'].shape == (4, 4)


def test_reduced_map_two_delta_proxy():
    state = (.3, .2)
    js = [d.reduced_jacobian(p.rattle_step, state, .02, 1e-13, delta) for delta in [1e-5, 5e-6]]
    assert np.max(abs(js[0]-js[1])) <= 2e-6
    determinant = js[-1][0, 0]*js[-1][1, 1]-js[-1][0, 1]*js[-1][1, 0]
    assert abs(determinant-1) <= 2e-6


def test_position_failure_retains_candidate():
    with pytest.raises(p.EvolutionFailure) as caught:
        p.position((.8, -.8), (.6, -.8), 1e-30, cap=0)
    assert 'candidate' in caught.value.payload and caught.value.payload['history']


def test_absent_branch_rejected():
    with pytest.raises(p.EvolutionFailure):
        p.position((0., 0.), (1., 0.), 1e-13)


def test_RATTLE_one_step_reverse():
    q, v = initial(.3, .2); new, momentum, _, _ = p.rattle_step(q, v, .02, 1e-13)
    back, backp, _, _ = p.rattle_step(new, momentum, -.02, 1e-13)
    assert np.max(abs(np.r_[np.array(back)-q, np.array(backp)-v])) <= 2e-11


def test_SHAKE_position_pair_reverse():
    forward = p.pendulum('shake', .02, 8, 1e-13)
    backward = p.pendulum('shake', -.02, 7, 1e-13, pair=(forward['q'][-1], forward['q'][-2]))
    assert np.max(abs(backward['q'][-2:]-forward['q'][1::-1])) <= 2e-11


def test_input_nonmutation():
    q = np.array([.6, -.8]); v = np.array([.16, .12]); before = q.copy(), v.copy()
    p.rattle_step(q, v, .01, 1e-13)
    assert np.array_equal(q, before[0]) and np.array_equal(v, before[1])


def test_Kepler_initial_invariants():
    state = a.kepler([0.], .7); fields = d.kepler_fields(state)
    assert abs(fields['energy'][0]+.5) <= 5e-14
    assert abs(fields['angular'][0]-math.sqrt(.51)) <= 5e-14


def test_Kepler_bracket_and_cycle_boundaries():
    times = np.array([0., 2*math.pi-1e-12, 2*math.pi, 2*math.pi+1e-12])
    one, two = a.kepler(times, .7), a.kepler(times, .7, True)
    assert np.max(abs(one['p']-two['p'])) <= 2e-10
    assert np.max(abs(one['q'][0]-one['q'][2])) <= 2e-12


def test_analytic_velocity_matches_Newton_ODE():
    t, delta = .7, 1e-5
    before, after, center = a.kepler([t-delta], .7), a.kepler([t+delta], .7), a.kepler([t], .7)
    velocity_derivative = (after['p'][0]-before['p'][0])/(2*delta)
    assert np.max(abs(velocity_derivative-p.acceleration(center['q'][0]))) <= 5e-8


def test_gravity_sign_negative_control():
    q = (.3, .4); acceleration = p.acceleration(q)
    assert p.dot(q, acceleration) < 0
    assert p.dot(q, tuple(-x for x in acceleration)) > 0


def test_central_KDK_one_step_reverse():
    q, v = (.3, .4), (.5, -.2)
    new, newp = p.kepler_step(q, v, .001)
    back, backp = p.kepler_step(new, newp, -.001)
    assert np.max(abs(np.r_[np.array(back)-q, np.array(backp)-v])) <= 64*d.EPS


def test_central_angular_invariant():
    q, v = (.3, .4), (.5, -.2); new, newp = p.kepler_step(q, v, .001)
    assert abs(new[0]*newp[1]-new[1]*newp[0]-(q[0]*v[1]-q[1]*v[0])) <= 64*d.EPS


def test_variable_step_ownership_and_endpoint():
    raw = p.kepler(.1, periods=1, steps_per_period=64, variable=True, cap=512)
    expected = (2*math.pi/64)*np.sqrt(np.sum(raw['q'][:-1]**2, axis=1))
    assert np.allclose(raw['actual_h'][:-1], expected[:-1], rtol=16*d.EPS, atol=0)
    assert raw['actual_h'][-1] <= expected[-1] and abs(raw['times'][-1]-2*math.pi) <= 1e-12


def test_saved_schedule_vs_regenerated_label():
    raw = p.kepler(.1, periods=1, steps_per_period=64, variable=True, cap=512)
    replay = p.kepler(.1, periods=1, steps_per_period=64, schedule=-raw['actual_h'][::-1], backward=True,
                      initial=(raw['q'][-1], raw['p'][-1]))
    assert replay['steps_completed'] == raw['steps_completed']
    assert np.array_equal(replay['actual_h'], -raw['actual_h'][::-1])
    # A regenerated schedule has no replay/reversibility theorem in this work.
    settings = json.loads((Path(__file__).parent/'inputs.json').read_text())
    assert settings['kepler']['geometric_scope'].startswith('No measured canonical symplectic-defect')


def test_Hermite_periapsis_known_orbit():
    times = np.linspace(0., 2.2*math.pi, 2049); truth = a.kepler(times, .3)
    events = d.periapses(dict(times=times, **truth))
    assert len(events['times']) == 1 and abs(events['times'][0]-2*math.pi) <= 1e-6


def test_collision_and_nonfinite_guard():
    with pytest.raises(p.EvolutionFailure):p.acceleration((0., 0.))
    with pytest.raises(p.EvolutionFailure):p.acceleration((math.inf, 1.))


def test_coupled_modal_initial_invariants():
    values, vectors = a.modes(10); state = a.coupled([0., .1], 10)
    assert np.max(abs(state[0]-[1., .1, 0., 0.])) <= 64*d.EPS
    _, _, H = d.coupled_energy(state, 10)
    mode = d.modal_energy(state, values, vectors)
    assert np.max(abs(mode.sum(axis=1)-H)) <= 128*d.EPS


def test_coupling_is_not_dropped():
    with_coupling = a.coupled([.5], 10, 1.)
    without = a.coupled([.5], 10, 0.)
    assert np.max(abs(with_coupling-without)) > 1e-4


def test_scalar_stage_vs_independent_matrix():
    z = (1., .1, .2, -.3)
    for method in ['verlet', 'impulse']:
        c = p.coefficients(method, 10., 1., .02); actual, _ = p.coupled_step(z, method, c)
        reference = list(z)
        for matrix in f.stage_matrices(c, method):reference = f.mv(matrix, reference)
        assert np.max(abs(np.array(actual)-reference)) <= 128*d.EPS


def test_ideal_pi_rational_polynomial_and_Jordan():
    for h in [Fraction(1, 4), Fraction(1, 8)]:
        _, rank, polynomial = f.exact_pi_component(h)
        assert rank == 3 and polynomial
        assert f.exact_pi_component(h, Fraction(0))[1] == 2


def test_stored_float_trig_no_snapping():
    c = p.coefficients('impulse', 10., 1., math.pi/10.)
    assert c['sine'] == math.sin(c['h']*10.) and c['sine'] != 0.
    assert float.fromhex(c['sine'].hex()) == c['sine']


def test_near_degenerate_classification():
    cfg = json.loads((Path(__file__).parent/'inputs.json').read_text())
    assert cfg['coupled']['central_actual_classification'].startswith('unresolved_near_degeneracy')
    assert f.ideal_classification(10, 1., 80)[0] == 'defective_jordan'


def test_roundoff_bound_rejects_perturbed_action():
    c = p.coefficients('verlet', 10., 1., .02); raw = p.coupled('verlet', c, 4)
    reference = np.asarray(f.action(c, 'verlet', 4, 80), float)
    bound = f.roundoff_allowance(c, 'verlet', raw['stage_inputs'], reference)
    assert np.all(abs(raw['states']-reference) <= bound)
    perturbed = raw['states'].copy(); perturbed[-1, 0] += 1e-5
    assert not np.all(abs(perturbed-reference) <= bound)


def test_frozen_source_and_pins():
    source = Path(__file__).parent
    contract = json.loads((source/'pre-run-contract.json').read_text())
    assert all(run.sha(source/name) == expected for name, expected in contract['files_sha256'].items())
    assert {name: importlib.metadata.version(name) for name in ['numpy', 'scipy', 'pytest']} == {'numpy': '2.0.2', 'scipy': '1.14.1', 'pytest': '8.3.5'}


def test_raw_before_diagnostics_and_public_schema_regression(tmp_path, monkeypatch):
    source = Path(__file__).parent; cfg = json.loads((source/'inputs.json').read_text())
    matrix = [dict(case=run.CASE_IDS[0], id='retention-fixture', role='primary', method='rattle', h=.02, steps=2, target=1e-13)]
    protocol = run.Protocol(source, tmp_path, cfg, matrix, tmp_path)
    def fail_after_candidate(*args, **kwargs):raise ArithmeticError('Injected diagnostic failure')
    monkeypatch.setattr(run.exact, 'pendulum', fail_after_candidate)
    with pytest.raises(ArithmeticError, match='Injected'):protocol.pendulum()
    with np.load(tmp_path/'retention-fixture.npz', allow_pickle=False) as raw:
        assert raw['q'].shape == (3, 2) and raw['p'].shape == (3, 2)
    assert protocol.completed == 1
    with pytest.raises(ValueError):run.numeric_csv(tmp_path/'invalid.csv', ['x'], [[math.nan]])
