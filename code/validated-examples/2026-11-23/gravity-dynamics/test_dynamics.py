from pathlib import Path
import json
import numpy as np
import pytest
import dynamics as s
from references import exact as r
from protocol import frozen
ROOT=Path(__file__).parent
C=json.loads((ROOT/'inputs.json').read_text())

@pytest.mark.parametrize('epsilon',[0.,.05])
def test_unequal_pair_force_and_energy_gradient(epsilon):
    x=np.array([[-.3,.1,0],[.7,-.2,.15]]);m=np.array([.2,.8]);a=s.direct(x,m,epsilon)[0];np.testing.assert_allclose(a,r.pair_force(x,m,epsilon),atol=2e-15);np.testing.assert_allclose(np.sum(m[:,None]*a,axis=0),0,atol=2e-15)
    h=1e-6;plus=x.copy();minus=x.copy();plus[0,1]+=h;minus[0,1]-=h;force=-(r.potential(plus,m,epsilon)-r.potential(minus,m,epsilon))/(2*h);assert abs(force-m[0]*a[0,1])<2e-10

@pytest.mark.parametrize('time',[0.,.3,1.7])
def test_kepler_closed_energy_angular_and_com(time):
    m=np.array([.6,.4]);x,v,res=r.kepler([time],m);E=.5*np.sum(m[:,None]*v[0]**2)+r.potential(x[0],m,0.);angular=np.sum(m[:,None]*np.cross(x[0],v[0]),axis=0)
    assert abs(E+.12)<3e-14;np.testing.assert_allclose(angular,[0,0,.24*np.sqrt(.84)],atol=3e-14);np.testing.assert_allclose(np.sum(m[:,None]*x[0],axis=0),0,atol=2e-15);assert max(res)<2e-13

@pytest.mark.parametrize('time',[.3,.7])
def test_analytic_kepler_velocity_satisfies_newton_ode(time):
    m=np.array([.6,.4]);h=1e-5;x,v,_=r.kepler([time],m);xp,vp,_=r.kepler([time+h],m);xm,vm,_=r.kepler([time-h],m)
    np.testing.assert_allclose((xp[0]-xm[0])/(2*h),v[0],atol=2e-8);np.testing.assert_allclose((vp[0]-vm[0])/(2*h),r.pair_force(x[0],m,0.),atol=5e-8)

@pytest.mark.parametrize('epsilon',[0.,.05])
def test_kdk_one_step_time_reversal(epsilon):
    x=np.array([[-.4,0,0],[.6,0,0]]);v=np.array([[0,-.2,0],[0,.3,0]]);m=np.array([.6,.4]);a=s.integrate(x,v,m,epsilon,.01,1);back=s.integrate(a['positions'][-1],a['velocities'][-1],m,epsilon,-.01,1)
    np.testing.assert_allclose(back['positions'][-1],x,atol=2e-15);np.testing.assert_allclose(back['velocities'][-1],v,atol=2e-15)

@pytest.mark.parametrize('theta',[0.,.35,.6])
def test_tree_same_state_force_and_real_path(theta):
    x=np.array(C['cold']['positions']);m=np.array(C['cold']['masses']);a,count=s.tree(x,m,.05,theta);ref=r.pair_force(x,m,.05)
    assert np.isfinite(a).all()
    if theta==0:np.testing.assert_allclose(a,ref,atol=3e-14);assert count['accepted_nodes']==0
    if theta==.6:assert count['accepted_nodes']>0

def test_full_second_moment_far_cluster():
    x=np.array([[-.4,-.4,-.4],[-.39,-.41,-.405],[-.415,-.39,-.395],[.7,.6,.8]]);m=np.array([.2,.3,.5,1e-12]);a,count=s.tree(x,m,.05,.6);ref=r.pair_force(x,m,.05)
    assert count['accepted_nodes']>0;assert np.linalg.norm(a[-1]-ref[-1])/np.linalg.norm(ref[-1])<1e-5

def test_theta_zero_actual_trajectory_driver():
    x=np.array(C['cold']['positions']);m=np.array(C['cold']['masses']);v=np.zeros_like(x);a=s.integrate(x,v,m,.05,.02,2);b=s.integrate(x,v,m,.05,.02,2,0.)
    np.testing.assert_allclose(a['positions'],b['positions'],atol=2e-14);np.testing.assert_allclose(a['velocities'],b['velocities'],atol=2e-14)

def test_independent_dop853_same_softened_ode():
    m=np.array([.6,.4]);x,v,_=r.kepler([0.],m);times=np.array([0.,.01,.02]);a,b,info=r.reference(x[0],v[0],m,.05,times,1e-11,1e-13);c,d,other=r.reference(x[0],v[0],m,.05,times,3e-12,3e-14)
    assert np.max(abs(a-c))<1e-9 and np.max(abs(b-d))<1e-9;np.testing.assert_array_equal(info['times'],times)

def test_mass_weighted_diagnostics_use_initial_com_and_momentum():
    x=np.array([[-.4,.2,0],[.6,-.1,0]]);v=np.array([[.1,.2,0],[.1,-.1,0]]);m=np.array([.6,.4]);a=s.integrate(x,v,m,.05,.1,10);d=a['diagnostics'];expected=d[0,7:10]+a['times'][:,None]*d[0,1:4]/m.sum();np.testing.assert_allclose(d[:,7:10],expected,atol=1e-14)

def test_collision_and_negative_softening_rejected():
    with pytest.raises(ValueError):s.direct(np.zeros((2,3)),np.ones(2),0.)
    with pytest.raises(ValueError):s.direct(np.array([[0.,0,0],[1.,0,0]]),np.ones(2),-.1)

def test_frozen_sources():assert frozen(ROOT)['shared_pytest_plus_main_budget_seconds']==120
