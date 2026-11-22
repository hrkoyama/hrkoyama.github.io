import copy
import json
import math
from pathlib import Path
import numpy as np
import pytest
import reference
from splitting import (Budget, CASE_ID, compose, diffuse, initial_field, integrate,
                       kinetics, midpoint, norms, run_case, validate)
from run import run


@pytest.fixture(scope='module')
def config():
    return json.loads(Path('inputs.json').read_text())['cases'][CASE_ID]


@pytest.fixture(scope='module')
def measured(config):
    return run_case(config, Budget())


def test_diffusion_is_exact_for_the_fd_symbol_not_the_continuum_symbol(config):
    n = config['grid']; dx = config['length']/n; mode = 4; h = .03
    wave = np.cos(2*math.pi*mode*np.arange(n)/n)
    field = np.array([1+.1*wave, .9-.04*wave])
    result = diffuse(field, h, config)
    lam = -4*math.sin(math.pi*mode/n)**2/dx**2
    expected = np.array([1+.1*wave*math.exp(config['diffusion'][0]*lam*h),
                         .9-.04*wave*math.exp(config['diffusion'][1]*lam*h)])
    np.testing.assert_allclose(result, expected, atol=8e-16, rtol=8e-16)
    continuum = .9-.04*wave*np.exp(-config['diffusion'][1]*mode**2*h)
    assert np.max(np.abs(result[1]-continuum)) > 1e-5


def test_diffusion_mean_and_semigroup(config):
    field = initial_field(config)
    full = diffuse(field, .07, config)
    half_twice = diffuse(diffuse(field, .035, config), .035, config)
    np.testing.assert_allclose(full, half_twice, atol=2e-15, rtol=0)
    np.testing.assert_allclose(full.mean(axis=1), field.mean(axis=1), atol=3e-16, rtol=0)


def test_reaction_midpoint_residual_and_nonconservative_source_balance(config):
    field = initial_field(config); h = .0625
    # Exercise a nonzero source directly; the production IC has mean(u)=a+b.
    field[0] += .2
    result, mid, residual, _ = midpoint(field, h, config)
    u, v = mid
    independent_rhs = np.stack((config['a']-u+u*u*v, config['b']-u*u*v))
    np.testing.assert_allclose(result-field-h*independent_rhs, 0, atol=config['newton_tolerance'], rtol=0)
    assert residual <= config['newton_tolerance']
    assert abs((result-field).sum(axis=0).mean()-h*(config['a']+config['b']-mid[0].mean())) < 1e-15
    assert abs((result-field).sum(axis=0).mean()) > 1e-6


def test_homogeneous_equilibrium_stays_fixed_in_both_methods(config):
    uniform = copy.deepcopy(config)
    uniform['initial_cosine_coefficients'] = [[1.,0,0,0,0],[.9,0,0,0,0]]
    for method in ['lie-trotter', 'strang']:
        states, _ = integrate(uniform, 16, method, Budget())
        np.testing.assert_allclose(states, np.broadcast_to(initial_field(uniform), states.shape), atol=4e-15, rtol=0)


def test_composition_applies_operators_in_the_declared_order():
    drift = lambda u,h: np.array([u[0]+h*u[1], u[1]])
    kick = lambda u,h: np.array([u[0], u[1]-h*u[0]])
    u = np.array([1.,.3]); h = .1
    np.testing.assert_allclose(compose(u,h,drift,kick,'lie-trotter'), [1.03,.197], atol=1e-15)
    np.testing.assert_allclose(compose(u,h,drift,kick,'lie-reversed'), [1.02,.2], atol=1e-15)
    np.testing.assert_allclose(compose(u,h,drift,kick,'strang'), [1.024925,.1985], atol=1e-15)
    with pytest.raises(ValueError):compose(u,h,drift,kick,'unknown')


def test_commuting_exact_linear_reaction_does_not_expose_splitting_error(config):
    field = initial_field(config)
    diffusion = lambda u,h: diffuse(u,h,config)
    reaction = lambda u,h: np.exp(-.7*h)*u
    expected = np.exp(-.7*.1)*diffuse(field,.1,config)
    for method in ['lie-trotter','strang']:
        np.testing.assert_allclose(compose(field,.1,diffusion,reaction,method), expected, atol=1e-15, rtol=1e-15)


def test_unsplit_rhs_and_jacobian_independently_match_the_fd_equations(config):
    rhs, jac = reference.system(config, Budget())
    field = initial_field(config); dx = config['length']/config['grid']
    lap = (np.roll(field,1,axis=1)-2*field+np.roll(field,-1,axis=1))/dx**2
    np.testing.assert_allclose(rhs(0,field.ravel()).reshape(field.shape),
                               np.asarray(config['diffusion'])[:,None]*lap+kinetics(field,config['a'],config['b']), atol=2e-14, rtol=2e-13)
    direction = np.random.default_rng(713).normal(size=field.size)
    eps = 1e-6
    finite_difference = (rhs(0,field.ravel()+eps*direction)-rhs(0,field.ravel()-eps*direction))/(2*eps)
    np.testing.assert_allclose(jac(0,field.ravel())@direction, finite_difference, atol=1e-8, rtol=2e-9)
    np.testing.assert_allclose(initial_field(config),reference.initial_values(config),atol=4e-16,rtol=0)


def test_fixed_case_observes_first_and_second_order_and_resolves_references(config, measured):
    assert measured['passed'] and all(measured['checks'].values())
    assert [r['method'] for r in measured['reference_records']] == ['Radau','Radau','DOP853']
    assert measured['metrics']['reference_to_strang_error_ratio'] < .01
    assert measured['metrics']['reverse_order_l2_difference'] > 1e-7
    for method, order in [('lie-trotter',1),('strang',2)]:
        rows = [r for r in measured['records'] if r['method']==method]
        assert [r['steps'] for r in rows] == config['step_counts']
        assert all(abs(r['observed_order_l2']-order)<.2 for r in rows[1:])
        assert all(r['reaction_calls']==r['steps'] for r in rows)
        assert all(r['diffusion_calls']==r['steps']*(2 if method=='strang' else 1) for r in rows)
    assert 'SAME' in measured['reference_scope'] and 'No continuum' in measured['reference_scope']


def test_error_norms_are_worst_species_and_the_observation_set_is_shared(config, measured):
    assert norms(np.array([[1.,-1.],[2.,-2.]]))=={'l1':2.,'l2':2.,'linf':2.}
    for row in measured['records']:
        observations = [r for r in measured['time_records'] if r['method']==row['method'] and r['steps']==row['steps']]
        assert [r['time'] for r in observations]==config['snapshot_times']
        assert row['max_l2']==max(r['l2'] for r in observations[1:])


def test_nonconvergence_and_expired_budget_are_errors(config,monkeypatch):
    limited = {**config,'newton_iterations':1}
    with pytest.raises(RuntimeError,match='did not converge'):midpoint(initial_field(config),.0625,limited)
    budget=Budget(1)
    monkeypatch.setattr('splitting.time.perf_counter',lambda:budget.deadline+1)
    with pytest.raises(RuntimeError,match='budget'):budget.check()


@pytest.mark.parametrize('key,value',[('grid',128),('time',float('nan')),('step_counts',[16,32,64,65]),('snapshot_times',[0,.1,.5,.75,1]),('newton_iterations',30)])
def test_unbounded_or_misaligned_inputs_are_rejected(config,key,value):
    invalid=copy.deepcopy(config);invalid[key]=value
    with pytest.raises(ValueError):validate(invalid)


def test_cli_outputs_can_be_reproduced_without_overwriting_existing_results(tmp_path):
    output=tmp_path/'run'
    data=run('inputs.json',output)
    assert data['passed'] and data['termination']=='fixed_budget_completed'
    assert (output/(CASE_ID+'.csv')).is_file() and (output/'time-errors.csv').is_file()
    with pytest.raises(ValueError,match='empty output'):run('inputs.json',output)
