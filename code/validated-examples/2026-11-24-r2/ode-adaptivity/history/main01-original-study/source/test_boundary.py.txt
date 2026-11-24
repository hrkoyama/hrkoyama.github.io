import math
import numpy as np
import pytest
import boundary

ROW={'n_interior':7,'steps':4,'final_time':.1,'method':'strang-boundary-corrected'}


def test_continuum_mms_physical_boundary_and_equation():
    x=np.array([0.,.17,.5,.93,1.]);t=.07
    equilibrium=np.cos(x-.5)/math.cos(.5)
    mode=.1*math.exp((1-math.pi**2)*t)*np.sin(math.pi*x)
    ut=(1-math.pi**2)*mode;uxx=-equilibrium-math.pi**2*mode
    assert np.max(np.abs(ut-uxx-boundary.continuum(x,t)))<3e-15
    assert np.max(np.abs(boundary.continuum(np.array([0.,1.]),t)-1))<2e-15


def test_dirichlet_single_fd_mode_exponential():
    n=7;x=np.arange(1,n+1)/(n+1);state=np.sin(3*math.pi*x);dt=.03
    actual=boundary.semigroup_setup(n,dt,0.)(state)
    lam=-4*math.sin(3*math.pi/(2*(n+1)))**2*(n+1)**2
    assert np.max(np.abs(actual-math.exp(dt*lam)*state))<3e-15


def test_affine_source_semigroup_not_homogeneous_diffusion():
    dt=.1;out=boundary.semigroup_setup(1,dt,1.)(np.zeros(1))
    assert abs(out[0]-math.expm1(-8*dt)/-8)<3e-15 and out[0]>0


def test_composition_passes_updated_field_to_next_subflow(monkeypatch):
    calls=[]
    def setup(n,dt,source):
        def add(w):calls.append(w.copy());return w+1
        return add
    monkeypatch.setattr(boundary,'semigroup_setup',setup)
    out=boundary.integrate(ROW)
    initial=boundary.continuum(np.arange(1,8)/8,0.)-1
    assert np.max(np.abs(calls[1]-(initial+1)*math.exp(.025)))<2e-15
    assert np.max(np.abs(out['states'][1]-1-((initial+1)*math.exp(.025)+1)))<3e-15


def test_boundary_trace_defect_is_preserved_and_corrected_is_zero():
    raw=boundary.integrate(dict(ROW,method='strang-unmodified'))
    corrected=boundary.integrate(ROW)
    assert raw['boundary']['reaction_trace_defect']==math.expm1(.025)>0
    assert corrected['boundary']['reaction_trace_defect']==0
    assert raw['boundary']['last_subflow_trace_defect']==0


def test_lie_last_reaction_trace_not_falsely_zeroed():
    out=boundary.integrate(dict(ROW,method='lie-unmodified'))
    assert out['work']=={'diffusion_calls':4,'reaction_calls':4}
    assert out['boundary']['last_subflow_trace_defect']>0


def test_completed_subflow_state_observed_before_next_operation():
    captured=[]
    def stop(phase,**values):
        captured.append((phase,values['state'].copy()))
        if phase=='boundary-after-reaction':raise RuntimeError('diagnostic interrupted')
    with pytest.raises(RuntimeError,match='interrupted'):boundary.integrate(ROW,stop)
    assert [x[0] for x in captured]==['boundary-after-diffusion','boundary-after-reaction']
    assert captured[-1][1].shape==(7,) and np.isfinite(captured[-1][1]).all()


def test_quarter_observation_schedule_and_finite_nodal_fields():
    out=boundary.integrate(ROW)
    assert out['states'].shape==(5,7) and out['x'][0]==1/8 and out['x'][-1]==7/8
    assert np.max(np.abs(out['times']-np.array([0.,.025,.05,.075,.1])))<2e-14
