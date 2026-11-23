"""Small physical and algebraic tests; no full fixed numerical batch here."""
import json
from pathlib import Path
import numpy as np
import pytest
import shallow_water as sw
import run
from references import analytic as ref


@pytest.mark.parametrize('state',[[0.,0.],[1.,0.],[2.,3.]])
def test_consistent_hll(state):
    u=np.array([state]); f,s=sw.hll(u,u,9.81)
    np.testing.assert_allclose(f,sw.flux(u,9.81),rtol=2e-15,atol=0)


@pytest.mark.parametrize('side',[-1,1])
def test_dry_riemann_flux_direction_and_wave_bound(side):
    wet=np.array([[1.,0.]]); dry=np.zeros((1,2))
    f,s=sw.hll(wet if side==1 else dry,dry if side==1 else wet,9.81)
    assert side*f[0,0]>0
    assert s==2*np.sqrt(9.81)


@pytest.mark.parametrize('eta',[.5,.1])
def test_hydrostatic_lake_residual(eta):
    z=np.array([0.,.05,.2,.2,.05,0.]); u=np.column_stack((np.maximum(eta-z,0),np.zeros(6)))
    lf,rf,common,speed=sw.interfaces(u,z,dict(kind='reflecting'),9.81)
    np.testing.assert_allclose(lf[1:]-rf[:-1],0,atol=3e-16)
    np.testing.assert_allclose(common[:,0],0,atol=0)


@pytest.mark.parametrize('eta',[.5,.1])
def test_lake_preservation_over_many_steps(eta):
    edges=np.linspace(0,25,51); z=ref.bump(.5*(edges[1:]+edges[:-1]))
    u=np.column_stack((np.maximum(eta-z,0),np.zeros(50)))
    out=sw.solve(u,z,.5,.2,dict(kind='reflecting'))
    np.testing.assert_allclose(out['state'],u,atol=2e-15,rtol=0)


def test_actual_wetting_and_mass_conservation():
    u=np.zeros((40,2));u[:20,0]=1.
    out=sw.solve(u,np.zeros(40),.25,.1,dict(kind='reflecting'))
    assert np.any(out['state'][20:,0]>0)
    assert np.any(out['state'][20:,0]==0)
    assert out['state'][:,0].min()>=0
    assert abs(out['state'][:,0].sum()-20)<2e-14
    assert out['state_clip_count']==out['depth_floor_count']==out['retries']==0


def test_nonflat_momentum_has_measured_bed_impulse():
    z=np.r_[np.zeros(10),np.full(10,.05)];u=np.column_stack((np.ones(20),np.full(20,.1)))
    out=sw.solve(u,z,.2,.05,dict(kind='transmissive'))
    stages=out['stages']
    assert abs(stages[:,9].sum())>.001
    assert abs(stages[:,13]).max()<2e-14
    assert abs(stages[:,12]).max()<2e-14


@pytest.mark.parametrize('u',[[[-1.,0.]],[[0.,1.]]])
def test_invalid_states_are_rejected_without_repair(u):
    with pytest.raises(ArithmeticError): sw.velocity(np.array(u))


def test_cfl_guard():
    with pytest.raises(ValueError): sw.solve(np.array([[1.,0.]]),np.array([0.]),1,.1,dict(kind='reflecting'),cfl=.6)


@pytest.mark.parametrize('degree',[0,1,2,3])
def test_split_gauss_means_integrate_polynomials(degree):
    edges=np.array([-.7,-.1,.3,.9])
    value=ref.means(edges,lambda x:x**degree,breaks=[0.])
    exact=(edges[1:]**(degree+1)-edges[:-1]**(degree+1))/((degree+1)*np.diff(edges))
    np.testing.assert_allclose(value,exact,atol=3e-16,rtol=1e-14)


@pytest.mark.parametrize('t',[.1,.3,.5])
def test_ritter_conservative_means_and_mass(t):
    edges=np.linspace(-5,5,73)
    a=ref.ritter_means(edges,t,order=8);b=ref.ritter_means(edges,t,order=16)
    np.testing.assert_allclose(a,b,atol=3e-15,rtol=1e-13)
    assert abs(np.diff(edges)@a[:,0]-5)<3e-14


def test_ritter_front_and_rarefaction_edges():
    c=np.sqrt(9.81);t=.5
    value=ref.ritter(np.array([-c*t,0.,2*c*t,2*c*t+.1]),t)
    np.testing.assert_allclose(value[0],[1,0],atol=1e-15)
    np.testing.assert_allclose(value[1],[4/9,8*c/27],atol=1e-15)
    np.testing.assert_array_equal(value[2:],np.zeros((2,2)))


@pytest.mark.parametrize('x',[0.,10.,25.])
def test_subcritical_energy_and_branch(x):
    state=ref.subcritical(np.array([x]));h,q=state[0]
    assert h>(4.42**2/9.81)**(1/3)
    assert abs(h+ref.bump(np.array([x]))[0]+q*q/(2*9.81*h*h)-(2+4.42**2/(8*9.81)))<2e-15


def test_reference_qualification():
    result=ref.qualify(); assert len(result['checks'])==6
    assert all(result['checks'].values())


def test_frozen_contract():
    contract=run.check_frozen_sources()
    assert contract['planned_fixed_runs']==8
    assert contract['shared_pytest_plus_main_budget_seconds']==120


def test_all_fixed_cases_and_true_dry_inputs():
    cfg=json.loads((Path(__file__).parent/'inputs.json').read_text());runs=run.fixed_runs(cfg)
    assert len(runs)==8
    assert {r['case'] for r in runs}=={'swashes-topography','dry-bed-dam-break'}
    for r in runs:
        edges,z,initial,exact,boundary,t=run.setup(r,cfg)
        if r['family']=='ritter':
            assert np.count_nonzero(initial[:,0]==0)==r['n']//2
            assert np.all(initial[:,1]==0)
