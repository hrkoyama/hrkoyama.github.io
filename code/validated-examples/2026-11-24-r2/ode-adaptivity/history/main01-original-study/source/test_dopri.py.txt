import json
import math
from pathlib import Path
import numpy as np
import pytest
import dopri

CFG=json.loads(Path(__file__).with_name('inputs.json').read_text())['cases']['rk45-dense-events']
ROW={'id':'component','method':'dormand-prince54','final_time':2.,'first_step':.4,'max_step':.4,'tolerance_id':'tight','event_direction':0,'terminal':False}


def test_constant_derivative_step_and_quartic_values():
    y=np.array([2.]);f=np.array([3.]);z,_,_,k=dopri.step(lambda t,y:np.array([3.]),.2,y,f,.4)
    segment=dopri.Segment(.2,.6,y,k)
    assert abs(z[0]-3.2)<2e-15
    for t in [.2,.27,.41,.6]:assert abs(segment(t)[0]-(2+3*(t-.2)))<5e-15


def test_time_cubic_rhs_dense_integral_exactness():
    rhs=lambda t,y:np.array([t**3]);t0=.2;h=.3;y=np.array([.1])
    _,_,_,k=dopri.step(rhs,t0,y,rhs(t0,y),h);seg=dopri.Segment(t0,t0+h,y,k)
    for t in [.2,.237,.39,.5]:assert abs(seg(t)[0]-(.1+(t**4-t0**4)/4))<2e-14


def test_scalar_linear_step_matches_independent_stability_polynomial():
    h=.1;y=np.array([1.]);out,_,_,_=dopri.step(lambda t,y:-2*y,0.,y,-2*y,h)
    z=-.2;expected=1+z+z*z/2+z**3/6+z**4/24+z**5/120+z**6/600
    assert abs(out[0]-expected)<3e-15


def test_segment_owns_input_arrays():
    y=np.array([1.,0.]);_,_,_,k=dopri.step(dopri.rotation,0.,y,dopri.rotation(0.,y),.1)
    seg=dopri.Segment(0.,.1,y,k);before=seg(.037)
    y[:]=9;k[:]=99
    assert np.array_equal(before,seg(.037))


def test_rejection_preserves_accepted_start_rhs(monkeypatch):
    original=dopri.step;starts=[]
    def force_first(rhs,t,y,f,h,observe=None):
        starts.append((t,y.copy(),f.copy()))
        out=original(rhs,t,y,f,h,observe)
        return (out[0],out[1],np.full_like(out[2],999.),out[3]) if len(starts)==1 else out
    monkeypatch.setattr(dopri,'step',force_first)
    out=dopri.integrate(dict(ROW,final_time=.2,first_step=.2),CFG)
    assert out['work']['rejected_steps']>=1
    assert starts[0][0]==starts[1][0]==0 and np.array_equal(starts[0][1],starts[1][1]) and np.array_equal(starts[0][2],starts[1][2])


def test_actual_rhs_count_excludes_dense_and_root_queries():
    count=[0]
    def rhs(t,y):count[0]+=1;return dopri.rotation(t,y)
    out=dopri.integrate(ROW,CFG,rhs=rhs)
    assert count[0]==out['work']['nfev']==1+6*out['work']['attempted_steps']
    for t in [.01,.73,1.97]:dopri.evaluate(out['segments'],t)
    assert count[0]==out['work']['nfev'] and len(out['roots'])==2


def test_terminal_root_and_full_endpoint_are_distinct():
    out=dopri.integrate(dict(ROW,event_direction=-1,terminal=True),CFG)
    assert out['termination']=='terminal_event' and abs(out['output_time']-math.pi/6)<3e-7
    assert out['times'][-1]>=out['output_time']
    assert abs(out['output_state'][0])<2e-12


def test_event_root_rejects_nonbracket():
    y=np.array([1.]);k=np.zeros((7,1));seg=dopri.Segment(0.,1.,y,k)
    with pytest.raises(ValueError,match='bracket'):dopri.root(seg,0.,1.,CFG['event_root_solver'])


def test_dense_extrapolation_rejected():
    y=np.array([1.]);k=np.zeros((7,1));seg=dopri.Segment(0.,1.,y,k)
    with pytest.raises(ValueError,match='extrapolation'):seg(1.1)


def test_upward_event_filter_ignores_first_downward_crossing():
    out=dopri.integrate(dict(ROW,event_direction=1,terminal=True),CFG)
    assert len(out['roots'])==1 and abs(out['roots'][0]['time']-math.pi/2)<3e-7


def test_initial_zero_owned_once():
    out=dopri.integrate(dict(ROW,final_time=.2,first_step=.1,max_step=.1),CFG,y0=np.array([0.,1.]))
    assert len(out['roots'])==1 and out['roots'][0]['initial'] and out['roots'][0]['time']==0


def test_trial_cap_retains_preceding_stage_and_attempt_context():
    cfg=dict(CFG,adaptivity=dict(CFG['adaptivity'],max_trials=1));events=[]
    with pytest.raises(RuntimeError,match='trial cap'):
        dopri.integrate(ROW,cfg,observe=lambda phase,**v:events.append((phase,v)))
    assert any(p=='rk-before-rhs' and v['stages'].shape==(7,2) for p,v in events)
    assert any(p=='rk-trial-result' and v['accepted'] is False for p,v in events)
