import json
import math
from pathlib import Path
import numpy as np
import pytest
import models
import stiff

CFG = json.loads((Path(__file__).with_name('inputs.json')).read_text())


def test_weighted_residual_distinguishes_small_species():
    assert abs(stiff.weighted_linf(np.array([1e-8, 2e-8, 1e-8]), np.array([1., 1e-4, 1.]))-2e-4) < 1e-18


def test_robertson_jacobian_complex_step():
    for y in (np.array([1.,0.,0.]), np.array([.9,3e-5,.09997])):
        columns=[]
        for k in range(3):
            z=y.astype(complex);z[k]+=1e-30j;columns.append(np.imag(models.robertson(0.,z))/1e-30)
        assert np.max(np.abs(models.robertson_jac(0.,y)-np.array(columns).T)/(1+np.abs(models.robertson_jac(0.,y)))) < 3e-14


def test_vdp_jacobian_complex_step_for_both_mu():
    for mu in (1,100):
        y=np.array([.3,-.2]);columns=[]
        for k in range(2):
            z=y.astype(complex);z[k]+=1e-30j;columns.append(np.imag(models.vdp(0.,z,mu))/1e-30)
        assert np.max(np.abs(models.vdp_jac(0.,y,mu)-np.array(columns).T)) < 2e-14


def test_constant_rhs_stage_and_actual_work():
    w=stiff.counters();cfg=CFG['implicit_solver'];base=np.array([1.,2.])
    z,f,r=stiff.stage(lambda t,y:np.array([2.,-3.]),lambda t,y:np.zeros((2,2)),0.,base,.1,base,np.ones(2),cfg,w)
    assert np.max(np.abs(z-np.array([1.2,1.7]))) < 3e-15 and r <= 1e-12
    assert w['factorizations']==w['linear_solves']==1 and w['jacobian']==1


def test_nonlinear_stage_reuses_immutable_factor():
    w=stiff.counters();cfg=CFG['implicit_solver']
    z,_,r=stiff.stage(lambda t,y:-y*y,lambda t,y:np.array([[-2*y[0]]]),0.,np.ones(1),.1,np.ones(1),np.ones(1),cfg,w)
    expected=2/(1+math.sqrt(1.4))
    assert abs(z[0]-expected)<2e-12 and r<=cfg['newton_scaled_residual_tolerance']
    assert w['linear_solves']>w['factorizations']


def test_factor_not_reused_across_distinct_stages():
    work=stiff.counters()
    for base in (np.ones(1),np.full(1,2.)):
        stiff.stage(lambda t,y:-2*y,lambda t,y:np.array([[-2.]]),0.,base,.1,np.zeros(1),np.ones(1),CFG['implicit_solver'],work)
    assert work['factorizations']==2 and work['linear_solves']==2


def test_bdf2_startup_is_be_on_same_grid():
    result=stiff.fixed(lambda t,y:-3*y,lambda t,y:np.array([[-3.]]),np.ones(1),np.ones(1),.1,1,'bdf2',CFG['implicit_solver'])
    assert abs(result['states'][1,0]-1/1.3)<2e-15


def test_bdf2_second_step_has_actual_history_coefficients():
    result=stiff.fixed(lambda t,y:-3*y,lambda t,y:np.array([[-3.]]),np.ones(1),np.ones(1),.2,2,'bdf2',CFG['implicit_solver'])
    expected=(4/1.3-1)/(3+.6)
    assert abs(result['states'][2,0]-expected)<3e-15


def test_sdirk_l_stability_does_not_claim_generic_positivity():
    out=stiff.fixed(lambda t,y:-1000*y,lambda t,y:np.array([[-1000.]]),np.ones(1),np.ones(1),.1,1,'sdirk2',CFG['implicit_solver'])
    z=-100.;g=stiff.GAMMA;expected=(1+(1-2*g)*z)/(1-g*z)**2
    assert out['states'][-1,0]<0 and abs(out['states'][-1,0]-expected)<3e-15


def test_zero_newton_cap_retains_owned_failed_candidate():
    cfg=dict(CFG['implicit_solver'],newton_max_updates=0);guess=np.ones(1);events=[]
    with pytest.raises(stiff.StageFailure) as error:
        stiff.stage(lambda t,y:-y,lambda t,y:np.array([[-1.]]),.1,np.ones(1),.1,guess,np.ones(1),cfg,stiff.counters(),lambda phase,**v:events.append((phase,v)))
    guess[0]=9
    assert error.value.context['candidate'][0]==1 and events[-1][0]=='failed-stage'
    assert 'residual' in error.value.context


def test_step_doubling_controller_uses_declared_rms(monkeypatch):
    calls=[]
    def fake(rhs,jac,t,y,h,weights,config,work,observe):
        calls.append(h)
        # full0, firsthalf0, secondhalf[0,3.6]: ratios[0,1.2], RMS<1.
        return np.array([0.,3.6]) if len(calls)%3==0 else np.zeros(2)
    monkeypatch.setattr(stiff,'sdirk_step',fake)
    adapt=dict(CFG['sdirk_step_doubling']);adapt['loose']={'rtol':1e-100,'atol_scale':1.}
    out=stiff.adaptive(None,None,np.zeros(2),np.ones(2),np.array([0.,.1]),CFG['implicit_solver'],adapt,'loose',.1)
    assert out['work']['accepted_steps']==1 and out['work']['rejected_steps']==0
    assert abs(out['trials'][0]['error_ratio']-1.2/math.sqrt(2))<1e-14


def test_adaptive_trial_exhaustion_never_returns_complete(monkeypatch):
    def failed(*args,**kwargs):raise stiff.StageFailure('fixed-failure',{'candidate':np.ones(1)})
    monkeypatch.setattr(stiff,'sdirk_step',failed);adapt=dict(CFG['sdirk_step_doubling'],max_trials=1)
    with pytest.raises(RuntimeError,match='trial cap'):
        stiff.adaptive(None,None,np.ones(1),np.ones(1),np.array([0.,.1]),CFG['implicit_solver'],adapt,'loose',.1)
