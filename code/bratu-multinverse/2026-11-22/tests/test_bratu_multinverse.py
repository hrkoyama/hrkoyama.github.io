"""Numerical contracts for the two-parameter Bratu inverse example."""
import json
from pathlib import Path
import numpy as np
import pytest
import numart.bratu_multinverse as m

INPUT=json.loads((Path(__file__).parents[1]/'inputs/synthetic-observations.json').read_text())
DATA=np.array(INPUT['reference_data'])


@pytest.mark.parametrize('theta',[[1.,-.5],[1.,.5],[2.8,-.5],[2.8,.5]])
def test_box_corners_have_converged_positive_coefficient_lower_states(theta):
    root=m.solve_state(31,theta)
    assert root.converged and np.linalg.norm(m.residual(root.x,theta))<=1e-10
    assert np.all(root.x>0)
    assert np.linalg.eigvalsh(m.derivatives(root.x,theta)[0])[0]>0


def test_full_residual_linearization_matches_state_and_parameter_differences():
    u=np.linspace(.02,.2,15);theta=np.array([2.,.2]);j,ft=m.derivatives(u,theta)
    v=np.linspace(-.7,.8,15);eps=1e-6
    fd=(m.residual(u+eps*v,theta)-m.residual(u-eps*v,theta))/(2*eps)
    np.testing.assert_allclose(fd,j@v,rtol=2e-9,atol=1e-8)
    for k in range(2):
        e=np.eye(2)[k]*eps
        np.testing.assert_allclose((m.residual(u,theta+e)-m.residual(u,theta-e))/(2*eps),ft[:,k],rtol=2e-8,atol=2e-8)


@pytest.mark.parametrize('theta',[[1.3,-.3],[2.1,.2],[2.6,.4]])
@pytest.mark.parametrize('gamma',[0.,3e-4])
def test_every_adjoint_component_matches_resolved_differences_and_tangent(theta,gamma):
    positions=np.array([.125,.25,.75]);data=DATA[[0,1,3]]
    weights=np.array([.2,.3,.5]);prior=np.array([1.7,-.1]);eps=1e-5
    value=m.evaluate(31,theta,data,positions,weights,gamma,prior)
    j,ft=m.derivatives(value['state'],theta);s=np.linalg.solve(j,-ft)
    direct=value['objective_state']@s+gamma*(np.array(theta)-prior)
    np.testing.assert_allclose(value['gradient'],direct,rtol=3e-13,atol=1e-15)
    fd=[]
    for e in eps*np.eye(2):
        plus=m.evaluate(31,np.array(theta)+e,data,positions,weights,gamma,prior,gradient=False)['objective']
        minus=m.evaluate(31,np.array(theta)-e,data,positions,weights,gamma,prior,gradient=False)['objective']
        fd.append((plus-minus)/(2*eps))
    np.testing.assert_allclose(value['gradient'],fd,rtol=2e-7,atol=2e-10)
    assert value['adjoint_residual_l2']<1e-12


@pytest.mark.parametrize('initial',INPUT['initial_guesses'])
def test_actual_projected_adjoint_updates_recover_same_discrete_data(initial):
    fit=m.fit_parameters(31,INPUT['same_grid_data'],initial)
    assert fit['converged']
    np.testing.assert_allclose(fit['parameters'],m.TRUTH,atol=5e-7,rtol=0)
    for before,after in zip(fit['history'],fit['history'][1:]):
        assert after['objective']<=before['armijo_rhs']
        assert after['objective']<=before['objective']
        proposed=np.clip(before['parameters']-before['accepted_step']*m.METRIC*before['gradient'],m.LOWER,m.UPPER)
        np.testing.assert_allclose(after['parameters'],proposed,atol=1e-15)
    last=fit['history'][-1]
    pg=np.linalg.norm(fit['parameters']-np.clip(fit['parameters']-fit['result']['gradient'],m.LOWER,m.UPPER),ord=np.inf)
    assert pg==last['projected_gradient_inf'] and pg<=1e-9


@pytest.mark.parametrize('gamma',[0.,1e-4,1e-3])
def test_noisy_penalized_fit_agrees_with_objective_only_reference(gamma):
    data=np.array(INPUT['noisy_data'])
    fit=m.fit_parameters(31,data,[2.,0.],gamma=gamma)
    ref=m.objective_reference(31,data,gamma=gamma)
    assert fit['converged'] and ref['simplex_diameter']<=1e-8
    np.testing.assert_allclose(fit['parameters'],ref['parameters'],atol=4e-6,rtol=0)
    assert fit['result']['data_rms']>1e-4
    assert fit['result']['objective']==fit['result']['data_objective']+fit['result']['penalty']


def test_reference_initial_simplex_is_nondegenerate_at_upper_box_corner():
    ref=m.objective_reference(15,DATA,initial=(2.8,.5))
    assert ref['iterations']>0 and ref['objective']<1e-8
    with pytest.raises(ValueError):m.objective_reference(15,DATA,diameter_tolerance=0)


def test_data_rank_is_separate_from_penalty_curvature_and_has_parameter_nullspace():
    full=m.sensitivity_diagnostic(31,m.TRUTH)
    center=m.sensitivity_diagnostic(31,m.TRUTH,positions=[.5],gamma=.01)
    zero=m.sensitivity_diagnostic(31,[2.2,0.],positions=[.5],gamma=.01)
    assert full['data_rank']==2 and full['data_condition_number']<11
    assert center['data_rank']==zero['data_rank']==1
    assert center['data_singular_values'].shape==(2,) and center['data_singular_values'][1]==0
    assert center['right_singular_vectors'].shape==(2,2)
    np.testing.assert_allclose(center['weighted_data_jacobian']@center['weakest_parameter_direction'],0,atol=1e-15)
    assert abs(zero['weighted_data_jacobian'][0,1])<1e-15
    assert center['augmented_singular_values'][1]>.0999
    same=m.sensitivity_diagnostic(31,m.TRUTH,gamma=.01)
    np.testing.assert_array_equal(full['data_singular_values'],same['data_singular_values'])


def test_reflection_makes_center_observation_globally_ambiguous_and_priors_select_mirrors():
    positive=m.evaluate(31,m.TRUTH,DATA)['state']
    negative=m.evaluate(31,[2.2,-.35],DATA)['state']
    np.testing.assert_allclose(positive,negative[::-1],atol=2e-14,rtol=0)
    fits=[m.fit_parameters(31,DATA[2:3],INPUT['central_initial'],positions=[.5],gamma=1e-4,prior=prior)
          for prior in INPUT['central_priors']]
    assert all(f['converged'] for f in fits)
    np.testing.assert_allclose(fits[0]['parameters'],fits[1]['parameters']*[1,-1],atol=1e-12)
    assert fits[0]['parameters'][1]>.39 and fits[1]['parameters'][1]<-.39
    np.testing.assert_allclose(fits[0]['result']['predicted'],fits[1]['result']['predicted'],atol=1e-13)
    assert all(m.sensitivity_diagnostic(31,f['parameters'],positions=[.5],gamma=1e-4)['data_rank']==1 for f in fits)


def test_regularization_reduces_this_perturbation_response_but_introduces_prior_bias():
    noise=np.array(INPUT['fixed_noise']);records=[]
    for gamma in [0.,1e-3]:
        clean=m.fit_parameters(31,DATA,[2.,0.],gamma=gamma)
        noisy=m.fit_parameters(31,DATA+noise,[2.,0.],gamma=gamma)
        assert clean['converged'] and noisy['converged']
        records.append((np.linalg.norm(clean['parameters']-m.TRUTH),np.linalg.norm(noisy['parameters']-clean['parameters'])))
    assert records[1][0]>records[0][0]+.1
    assert records[1][1]<records[0][1]/2


def test_independent_thomas_reference_matches_dense_state_and_has_refinement_floor():
    same=m.fine_reference(31,m.TRUTH)
    np.testing.assert_allclose(same['predicted'],m.evaluate(31,m.TRUTH,np.zeros(5))['predicted'],atol=1e-13)
    refs=[m.fine_reference(n,m.TRUTH) for n in [255,511,1023]]
    d1=np.linalg.norm(refs[0]['predicted']-refs[1]['predicted'])
    d2=np.linalg.norm(refs[1]['predicted']-refs[2]['predicted'])
    assert 3.9<d1/d2<4.1 and d2>0
    assert all(r['scaled_residual_inf']<2e-14 and r['final_correction_inf']<2e-13 for r in refs)
    np.testing.assert_allclose(refs[-1]['predicted'],DATA,atol=1e-13)


def test_fixed_reference_data_produce_decreasing_parameter_grid_bias():
    errors=[np.linalg.norm(m.fit_parameters(n,DATA,[2.,0.])['parameters']-m.TRUTH) for n in [15,31,63]]
    assert all(1.9<q<2.1 for q in np.log2(np.array(errors[:-1])/errors[1:]))


def test_active_bound_stationarity_does_not_require_zero_raw_gradient():
    data=m.evaluate(15,[2.6,.4],np.zeros(5))['predicted']
    fit=m.fit_parameters(15,data,[2.,0.],bounds=((1.,2.3),(-.3,.3)))
    assert fit['converged']
    assert np.max(abs(fit['result']['gradient']))>1e-4
    assert fit['history'][-1]['projected_gradient_inf']<=1e-9
    assert np.any(abs(fit['parameters']-[2.3,.3])<1e-12)


def test_failed_primal_and_iteration_limit_cannot_claim_convergence(monkeypatch):
    fit=m.fit_parameters(15,DATA,[1.3,-.4],maxiter=1)
    assert not fit['converged'] and fit['reason']=='optimization iteration limit'
    original=m.solve_state
    def failed(*args,**kwargs):
        result=original(*args,**kwargs);result.converged=False;return result
    monkeypatch.setattr(m,'solve_state',failed)
    with pytest.raises(RuntimeError,match='Primal solve failed'):m.evaluate(15,[2.,0.],DATA)


def test_boundary_data_have_no_information_even_when_prior_selects_parameters():
    diag=m.sensitivity_diagnostic(15,[2.,.1],positions=[0.,1.],gamma=.01)
    assert diag['data_rank']==0 and np.all(diag['data_singular_values']==0)
    assert np.all(diag['augmented_singular_values']>.0999)
    with pytest.raises(ValueError,match='no parameter information'):
        m.fit_parameters(15,[0.,0.],[2.,0.],positions=[0.,1.])
    fit=m.fit_parameters(15,[0.,0.],[2.2,.2],positions=[0.,1.],gamma=.01,prior=[2.,0.])
    assert fit['converged']
    np.testing.assert_allclose(fit['parameters'],[2.,0.],atol=2e-6)


@pytest.mark.parametrize('kwargs',[{'weights':[1,1,0,1,1]},{'gamma':-1},{'metric':[1,-1]},{'bounds':((.1,3.),(-.5,.5))}])
def test_invalid_physical_or_optimization_settings_rejected(kwargs):
    with pytest.raises(ValueError):m.fit_parameters(15,DATA,[2.,0.],**kwargs)
