"""32 fixed tests: algorithms, independent algebra, failure retention and CLI."""
import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest

import least_squares
import model
import run
from model import BratuModel, canonical_box, observe_legacy
from public_contract import check_generated_csv, validate_result
from quasi_newton import (Objective, current_scaling, dense_retained_action, inverse_bfgs,
                          lbfgs_action, positive_curvature, strong_wolfe)
from references.thomas import state_and_sensitivity
from regularization import (fixed_gamma_covariance, fixed_noise, lcurve_chord_curvature,
                            scalar_2x2_statistics, select_discrepancy)
from support import Retainer, classify_library, digest, numeric_csv, relative_error

ROOT=Path(__file__).resolve().parent


@pytest.fixture
def cfg():
    return json.loads((ROOT/'inputs.json').read_text())


class LinearModel:
    def __init__(self,path,gamma=0.,target=(2.2,.1)):
        self.prior=np.array([2.,0.])
        self.gamma=gamma
        self.target=np.asarray(target)
        self.retainer=Retainer(path,'linear')

    def at(self,theta):
        theta=np.asarray(theta)
        misfit=theta-self.target
        gradient=misfit+self.gamma*(theta-self.prior)
        self.retainer.forward_calls+=1
        return dict(parameters=theta.copy(),gradient=gradient,
                    objective=float(.5*np.dot(misfit,misfit)+.5*self.gamma*np.dot(theta-self.prior,theta-self.prior)))

    def augmented(self,theta):
        value=self.at(theta)
        r=np.concatenate((np.asarray(theta)-self.target,np.sqrt(self.gamma)*(np.asarray(theta)-self.prior)))
        jac=np.vstack((np.eye(2),np.sqrt(self.gamma)*np.eye(2)))
        return r,jac,value


def pairs_fixture(count):
    a=np.diag([1.,2.,4.,8.])+np.ones((4,4))/16.
    pairs=[]
    for i in range(count):
        s=np.eye(4)[i]
        pairs.append((s,np.einsum('ij,j->i',a,s)))
    return pairs


def test_canonical_box_adapter(cfg):
    lo,hi,pairs=canonical_box(cfg['bratu']['box'])
    assert np.array_equal(pairs,[[1.,2.8],[-.5,.5]])
    assert np.array_equal(lo,[1.,-.5]) and np.array_equal(hi,[2.8,.5])


def test_invalid_box_rejection():
    with pytest.raises(ValueError):canonical_box({'lower':[1.,2.8],'upper':[-.5,.5]})


def test_weight_validation(tmp_path):
    with pytest.raises(ValueError):
        BratuModel(7,[0.,0.,0.],[.25,.5,.75],[1.,0.,1.],0.,[2.,0.],Retainer(tmp_path,'bad-weight'))


def test_coordinate_chain_rule():
    k=np.array([[1.,2.],[-1.,3.],[2.,1.]])
    weights=np.array([.2,.3,.5]);theta=np.array([2.1,.2]);prior=np.array([2.,0.]);misfit=np.array([.1,-.2,.3]);gamma=.01
    fake=SimpleNamespace(weights=weights,gamma=gamma,prior=prior,
                         at=lambda _:dict(misfit=misfit,data_jacobian=k))
    r,jac,_=BratuModel.augmented(fake,theta)
    d=np.array([1.,.1])
    physical=np.einsum('mi,m,m->i',k,weights,misfit)+gamma*(theta-prior)
    assert np.allclose(np.einsum('mi,m->i',jac*d[None,:],r),d*physical,rtol=1e-14,atol=1e-15)


def test_legacy_pg_adapter_real_route_with_mock(cfg,tmp_path,monkeypatch):
    seen={};theta=np.array([2.,0.]);value={'parameters':theta}
    def fake(*args,**kwargs):
        seen.update(kwargs)
        return dict(parameters=theta,converged=True,reason='mock',evaluations=1,
                    history=[{'parameters':theta,'objective':0.,'projected_gradient_inf':0.}])
    monkeypatch.setattr(model.legacy,'fit_parameters',fake)
    m=SimpleNamespace(n=31,data=np.zeros(5),positions=np.array(cfg['bratu']['positions']),
                      weights=np.array(cfg['bratu']['weights']),gamma=0.,prior=np.array([2.,0.]),
                      retainer=Retainer(tmp_path,'adapter'),at=lambda _:value)
    least_squares.legacy_projected(m,theta,cfg['bratu']['box'],cfg['case65']['legacy_pg_controls'])
    assert np.array_equal(seen['bounds'],[[1.,2.8],[-.5,.5]])
    assert seen['maxiter']==1000 and seen['initial_step']==10.


def test_observation_grid_points():
    h=model.legacy.observation_matrix(31,[.125,.25,.5,.75,.875])
    assert np.array_equal(np.argmax(h,axis=1),[3,7,15,23,27])
    assert np.array_equal(np.sum(h,axis=1),np.ones(5))


def test_dense_thomas_state_and_sensitivity(tmp_path):
    retainer=Retainer(tmp_path,'dense-thomas')
    ref=state_and_sensitivity(7,[2.2,.35],[.25,.5,.75],retainer)
    with observe_legacy(retainer):
        actual=BratuModel(7,[0.,0.,0.],[.25,.5,.75],[1/3]*3,0.,[2.,0.],retainer).at([2.2,.35])
    assert relative_error(actual['state'],ref['state'],np.inf)<=2e-10
    assert relative_error(actual['data_jacobian'],ref['data_jacobian'],np.inf)<=2e-8


def test_jacobian_finite_difference_control():
    theta=np.array([2.1,.2]);columns=[]
    ref=state_and_sensitivity(7,theta,[.25,.5,.75])
    for i in range(2):
        h=np.eye(2)[i]*1e-5
        columns.append((state_and_sensitivity(7,theta+h,[.25,.5,.75])['predicted']-
                        state_and_sensitivity(7,theta-h,[.25,.5,.75])['predicted'])/(2e-5))
    assert relative_error(np.column_stack(columns),ref['data_jacobian'])<=2e-6


def test_candidate_checkpoint_on_failure(tmp_path,monkeypatch):
    state=np.arange(7,dtype=float)/100.
    raw=Retainer(tmp_path,'completed-before-failure')
    monkeypatch.setattr(model.legacy,'evaluate',lambda *a,**k:dict(parameters=np.array([2.,0.]),state=state,objective=0.))
    def fail(*args):raise RuntimeError('forced later derivative failure')
    monkeypatch.setattr(model.legacy,'derivatives',fail)
    with observe_legacy(raw),pytest.raises(RuntimeError,match='later derivative'):
        BratuModel(7,[0.,0.,0.],[.25,.5,.75],[1/3]*3,0.,[2.,0.],raw).at([2.,0.])
    rows=[json.loads(s) for s in raw.path.read_text().splitlines()]
    saved=next(r for r in rows if r['stage']=='forward-completed-before-further-work')
    assert np.array_equal(saved['state'],state)


def test_augmented_residual_gradient(tmp_path):
    m=LinearModel(tmp_path,gamma=.03)
    r,jac,value=m.augmented([2.3,.1])
    assert np.allclose(np.einsum('ij,i->j',jac,r),value['gradient'],atol=1e-15)
    assert abs(.5*np.dot(r,r)-value['objective'])<1e-15


def test_gn_known_linear_step(cfg,tmp_path):
    m=LinearModel(tmp_path)
    answer=least_squares.own_least_squares(m,'gn',[2.,0.],[1.,1.],cfg['case65']['own_controls'])
    assert answer['converged'] and np.allclose(answer['parameters'],m.target,atol=1e-14)
    assert answer['linear_subproblem_solves']==1


def test_lm_mu_distinct_from_gamma(cfg,tmp_path):
    m=LinearModel(tmp_path,gamma=.1)
    answer=least_squares.own_least_squares(m,'lm',[2.,0.],[1.,1.],cfg['case65']['own_controls'])
    optimum=(m.target+.1*m.prior)/1.1
    assert answer['converged'] and np.allclose(answer['parameters'],optimum,atol=2e-9)
    assert m.gamma==.1 and answer['history'][0]['damping_mu']==.001


def test_lm_gain_ratio_decision(cfg,tmp_path):
    m=LinearModel(tmp_path)
    answer=least_squares.own_least_squares(m,'lm',[2.,0.],[1.,.1],cfg['case65']['own_controls'])
    assert answer['accepted_steps']
    assert all(abs(row['gain_ratio']-1.)<1e-6 for row in answer['accepted_steps'])


def test_unbounded_domain_reject_without_box_clip(cfg,tmp_path):
    m=LinearModel(tmp_path,target=[4.,0.]);controls=dict(cfg['case65']['own_controls'],maxiter=1)
    answer=least_squares.own_least_squares(m,'gn',[2.,0.],[1.,1.],controls)
    assert 2.8<answer['parameters'][0]<=3.3
    assert 'rejected-forward-domain' in m.retainer.path.read_text()


def test_lm_bounds_configuration_rejection():
    with pytest.raises(ValueError,match='unbounded LM'):
        least_squares.library_least_squares(None,'lm-with-bounds',None,None,None,None)


def test_library_failure_budget_classification():
    result=SimpleNamespace(success=False,status=0,message='max evaluations exceeded')
    assert classify_library(result,False)=='BUDGET_EXHAUSTED'
    result.status=2;result.message='precision loss'
    assert classify_library(result,False)=='LIBRARY_FAILURE'
    assert classify_library(result,True)=='EXTERNALLY_STATIONARY_LIBRARY_FAILURE_RETAINED'


def test_bfgs_secant_known_spd():
    a=np.array([[2.,.5],[.5,1.]]);s=np.array([1.,.2]);y=np.einsum('ij,j->i',a,s)
    h,antisymmetry=inverse_bfgs(np.eye(2),s,y)
    assert np.allclose(np.einsum('ij,j->i',h,y),s,rtol=1e-14,atol=1e-14)
    assert antisymmetry<=1e-12


def test_bfgs_spd_curvature():
    s=np.array([1.,2.]);y=np.array([3.,4.]);h,_=inverse_bfgs(np.eye(2),s,y)
    assert positive_curvature(s,y)[0] and np.linalg.eigvalsh(h)[0]>0


def test_negative_curvature_control():
    s=np.array([1.,0.]);y=-s
    assert not positive_curvature(s,y)[0]
    with pytest.raises(ValueError):inverse_bfgs(np.eye(2),s,y)
    with pytest.raises(ValueError):lbfgs_action(np.ones(2),[(s,y)])


def test_lbfgs_empty_history():
    g=np.array([1.,-2.,3.,4.])
    assert np.array_equal(lbfgs_action(g,[]),-g)
    assert np.array_equal(dense_retained_action(g,[]),-g)


def test_lbfgs_one_pair():
    pairs=pairs_fixture(1);g=np.arange(1.,5.)
    assert relative_error(lbfgs_action(g,pairs),dense_retained_action(g,pairs))<=1e-10


def test_lbfgs_three_pairs():
    pairs=pairs_fixture(3);g=np.arange(1.,5.)
    assert relative_error(lbfgs_action(g,pairs),dense_retained_action(g,pairs))<=1e-10


def test_lbfgs_eviction_current_gamma():
    all_pairs=pairs_fixture(4);retained=all_pairs[-3:];g=np.arange(1.,5.)
    action=lbfgs_action(g,retained)
    assert relative_error(action,dense_retained_action(g,retained))<=1e-10
    wrong=current_scaling(all_pairs[:-1])*np.eye(4)
    for s,y in retained:wrong,_=inverse_bfgs(wrong,s,y)
    assert np.linalg.norm(action+np.einsum('ij,j->i',wrong,g))>1e-4
    with pytest.raises(ValueError):dense_retained_action(g,all_pairs)


def test_strong_wolfe_failure_no_fallback(cfg,tmp_path):
    raw=Retainer(tmp_path,'wrong-gradient')
    objective=Objective(lambda x:(0.,np.ones(2)),raw)
    f,g=objective.at(np.zeros(2))
    with pytest.raises(RuntimeError,match='WOLFE'):
        strong_wolfe(objective,np.zeros(2),f,g,-g,cfg['case66']['controls'])
    assert 'line-search-completed-before-decision' in raw.path.read_text()


def test_covariance_scalar2x2(cfg):
    s=cfg['case67']['linear_control'];k=np.asarray(s['K']);w=np.asarray(s['W_diagonal'])
    delta=np.array([.1,-.2,.3,-.4,.5])
    actual,g,response=fixed_gamma_covariance(k,w,s['sigma'],s['gamma'])
    expected,bias,shift=scalar_2x2_statistics(k,w,s['sigma'],s['gamma'],s['truth'],s['prior'],delta)
    assert relative_error(actual,expected)<=1e-10
    assert relative_error(-s['gamma']*np.linalg.solve(g,np.asarray(s['truth'])-s['prior']),bias)<=1e-10
    assert relative_error(np.einsum('ij,j->i',response,delta),shift)<=1e-10


def test_noise_metric_covariance_separation(cfg):
    s=cfg['case67']['linear_control'];k=np.asarray(s['K']);w=np.asarray(s['W_diagonal'])
    covariance,g,_=fixed_gamma_covariance(k,w,s['sigma'],0.)
    expected=s['sigma']**2*np.linalg.inv(np.einsum('mi,mj->ij',k,k))
    assert relative_error(covariance,expected)<=1e-10
    assert not np.allclose(covariance,np.linalg.inv(g))
    first,second=fixed_noise([67001,67002]),fixed_noise([67001,67002])
    assert all(np.array_equal(first[seed],second[seed]) for seed in first)


def test_plugin_not_selection_conditional_metadata(cfg):
    text=cfg['case67']['covariance'].lower()
    assert 'plug-in' in text and 'not covariance conditional on selection event' in text
    assert cfg['case67']['no_coverage_claim'] is True


def test_incomplete_gamma_path():
    rows=[dict(gamma=0.,qualified=True,weighted_residual_norm=.1)]
    result=select_discrepancy(rows,[0.,.001],1.)
    assert result==dict(status='INCOMPLETE_GAMMA_PATH',selected_gamma=None)
    rows.append(dict(gamma=.001,qualified=False))
    assert select_discrepancy(rows,[0.,.001],1.)['selected_gamma'] is None


def test_complete_no_admissible_path():
    rows=[dict(gamma=g,qualified=True,weighted_residual_norm=2.) for g in [0.,.001]]
    assert select_discrepancy(rows,[0.,.001],1.)==dict(status='NO_ADMISSIBLE_GAMMA',selected_gamma=None)
    rows[0]['weighted_residual_norm']=.5
    assert select_discrepancy(rows,[0.,.001],1.)['selected_gamma']==0.


def test_lcurve_zero_norm_handling():
    rows=[dict(gamma=g,qualified=True,weighted_residual_norm=0.,parameter_deviation_norm=0.)
          for g in [1e-5,1e-4,1e-3,1e-2]]
    assert lcurve_chord_curvature(rows)['status']=='NOT_FOUR_FINITE_POSITIVE_POINTS'
    assert lcurve_chord_curvature([dict(gamma=.1,qualified=False)])['values']==[]


def test_real_driver_mock_full_envelope_and_raw_retention(tmp_path,monkeypatch):
    monkeypatch.setattr(run,'load_reference',lambda p:({'gate_count':48,'fields_sha256':'0'*64},{}))
    def make_case(index):
        def actual_route(*args):
            output=args[-1]
            numeric_csv(output/('mock-'+str(index)+'.csv'),['iteration','value'],[[0,1.]])
            return dict(id=run.CASE_IDS[index],passed=True,checks={'mock':True},
                        records=[{'retained':True}],metrics={'completed_fits':[17,16,42][index]})
        return actual_route
    for i,name in enumerate(['run_case65','run_case66','run_case67']):monkeypatch.setattr(run,name,make_case(i))
    out=tmp_path/'complete'
    assert run.main(['--input',str(ROOT/'inputs.json'),'--output',str(out)])==0
    result=json.loads((out/'result.json').read_text())
    validate_result(result,run.CASE_IDS,digest(ROOT/'inputs.json'),'fixed_budget_completed')
    assert sum(c['metrics']['completed_fits'] for c in result['cases'])==75 and len(result['csv_validation'])==3
    def fail(*args):raise RuntimeError('forced after first completed case')
    monkeypatch.setattr(run,'run_case66',fail)
    failed=tmp_path/'failed'
    with pytest.raises(RuntimeError,match='forced after first'):
        run.main(['--input',str(ROOT/'inputs.json'),'--output',str(failed)])
    retained=json.loads((failed/'result.json').read_text())
    assert retained['passed'] is False and retained['cases'][0]['id']==run.CASE_IDS[0]
    assert (failed/'result.partial.json').is_file()


def test_numeric_csv_public_result_contract(tmp_path):
    numeric_csv(tmp_path/'finite.csv',['index','value'],[[0,1.],[1,0.]])
    assert len(check_generated_csv(tmp_path))==1
    with pytest.raises(ValueError):numeric_csv(tmp_path/'bad.csv',['value'],[[float('inf')]])
    value=dict(schema_version=1,passed=True,input_sha256='a'*64,termination='fixed_budget_completed',
               checks={'example':True},cases=[dict(id='example',passed=True,checks={'test':True},
                                                  records=[{'x':0}],metrics={})])
    with pytest.raises(ValueError,match='metrics'):
        validate_result(value,['example'],'a'*64,'fixed_budget_completed')
