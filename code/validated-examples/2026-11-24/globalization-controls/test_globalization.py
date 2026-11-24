import json
from pathlib import Path
import numpy as np
import pytest
from globalization import dogleg,least_squares,solve,radius_update
from problems import residual,jacobian,DomainError,dot,norm
from references import dogleg_intersection,fraction_cauchy,independent_residual
from experiments import specifications,expected_gate_keys,ledger
from io_contract import snapshot,save_json,csv_rows


def test_rosenbrock_residual_jacobian():
    x=np.array([.25,-.5]);h=2.**-20
    numeric=np.column_stack([(residual('rosenbrock',x+h*e)-residual('rosenbrock',x-h*e))/(2*h)for e in np.eye(2)])
    assert np.array_equal(jacobian('rosenbrock',x),numeric)

def test_bratu_stencil_boundary():
    x=np.array([.1,.2,.3]);assert np.allclose(residual('bratu',x),independent_residual('bratu',x),atol=1e-13,rtol=0)
    assert np.array_equal(jacobian('bratu',np.zeros(3)),np.array([[29.,-16.,0.],[-16.,29.,-16.],[0.,-16.,29.]]))

def test_root_test_is_unscaled():
    for scale in [[1.,1.],[.001,1000.]]:assert solve('rosenbrock',[1.,1.],scale,'dogleg-trust-region')['termination']=='ROOT'

def test_cauchy_boundary():
    p,info=dogleg(np.diag([2.,1.]),np.array([2.,1.]),.25)
    assert info['branch']=='cauchy-boundary';assert np.allclose(p,-.25*np.array([4.,1.])/np.sqrt(17.),rtol=0,atol=1e-14)
    assert np.array_equal(fraction_cauchy(),np.array([-68/65,-17/65]))

def test_intermediate_dogleg():
    p,info=dogleg(np.diag([2.,1.]),np.array([2.,1.]),1.2)
    assert info['branch']=='intermediate';assert np.allclose(p,dogleg_intersection(1.2),atol=1e-12,rtol=0)
    assert np.allclose(dogleg_intersection(1.2,60),dogleg_intersection(1.2,90),atol=1e-14,rtol=0)

def test_interior_gauss_newton():
    p,info=dogleg(np.diag([2.,1.]),np.array([2.,1.]),2.)
    assert info['branch']=='gauss-newton';assert np.array_equal(p,[-1.,-1.])

def test_rank_one_minimum_norm():
    p,s,rank=least_squares(np.array([[1.,0.],[0.,0.]]),np.array([1.,1.]));assert rank==1;assert np.array_equal(p,[-1.,0.])
    p,_=dogleg(np.array([[1.,0.],[0.,0.]]),np.array([1.,1.]),.5);assert np.array_equal(p,[-.5,0.])

def test_stationary_is_not_root():
    for method in ['armijo-newton','dogleg-trust-region']:
        ans=solve('stationary',[0.],[1.],method);assert ans['termination']=='STATIONARY_NONROOT';assert ans['f']==[1.]

def test_zero_residual_precedes_model():
    ans=solve('rosenbrock',[1.,1.],[1.,1.],'dogleg-trust-region');assert ans['termination']=='ROOT';assert ans['counts']['linear']==0

def test_radius_literal_boundaries():
    assert radius_update(1.,.25,1.)==1.;assert radius_update(1.,.75,1.)==1.
    assert radius_update(1.,-.1,1.)==.25;assert radius_update(1.,.8,.99)==2.;assert radius_update(80.,.8,80.)==100.

def test_armijo_ledger():
    spec=dict(kind='rosenbrock',initial=[-1.2,1.],scale=[1.,1.],method='armijo-newton')
    answer=solve(**spec);gates,_=ledger(spec,answer);assert gates['method_step_ledger']
    assert any(not row['accepted']for row in answer['history'])

def test_domain_before_exp(monkeypatch):
    calls=[]
    def bad(*a,**k):calls.append(1);raise AssertionError('exp should not run')
    monkeypatch.setattr('problems.np.exp',bad)
    with pytest.raises(DomainError):residual('bratu',np.r_[800.,np.zeros(30)])
    assert calls==[]

def test_rejected_candidate_ownership():
    initial=np.array([-1.2,1.]);old=initial.copy();ans=solve('rosenbrock',initial,[1.,1.],'armijo-newton')
    assert np.array_equal(initial,old);first=ans['history'][0];assert first['x']==old.tolist();assert not first['accepted']

def test_fixed_caps_counts_and_gate_inventory():
    ans=solve('rosenbrock',[-1.2,1.],[1.,1.],'armijo-newton',max_iterations=1,max_trials=1)
    assert ans['termination']=='TRIALS_EXHAUSTED';assert ans['counts']['trials']==1
    assert len(specifications())==21;assert sum(row['required']for row in specifications())==6
    assert len(expected_gate_keys())==len(set(expected_gate_keys()))==145

def test_candidate_saved_before_failing_linear_solve(monkeypatch,tmp_path):
    stages=[]
    def checkpoint(stage,**arrays):
        stages.append(stage);snapshot(tmp_path/'candidate.npz',stage,**{k:v for k,v in arrays.items()if k!='record'})
    def broken(*a,**k):raise RuntimeError('intentional')
    monkeypatch.setattr('globalization.svd',broken)
    with pytest.raises(RuntimeError):solve('rosenbrock',[0.,0.],[1.,1.],'armijo-newton',checkpoint)
    assert stages[-1]=='before-model-solve'
    with np.load(tmp_path/'candidate.npz')as saved:assert 'scaled_j'in saved and np.array_equal(saved['x'],[0.,0.])

def test_finite_json_csv_serialization(tmp_path):
    save_json(tmp_path/'a.json',{'value':np.array([1.,2.]),'unavailable':None})
    assert json.loads((tmp_path/'a.json').read_text())['unavailable']is None
    csv_rows(tmp_path/'a.csv',[{'value':1.,'status':'ROOT'},{'value':2.,'status':'MAXITER'}])
    assert len((tmp_path/'a.csv').read_text().splitlines())==3
    with pytest.raises(ValueError):save_json(tmp_path/'bad.json',{'value':float('nan')})
