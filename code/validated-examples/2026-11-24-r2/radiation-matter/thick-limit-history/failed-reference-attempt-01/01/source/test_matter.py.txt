import json
import numpy as np
import pytest
import diffusion,transport,io_contract
from references.analytic import closed_step


def test_robin_halfcell_flux_exact_linear_steady_solution():
    n,L=16,2.;h=L/n;x=(np.arange(n)+.5)*h;u=(L-x)/(L+2/np.sqrt(3));matrix,b=diffusion.operator(n,L)
    np.testing.assert_allclose(matrix.dot(u),b,rtol=0,atol=5e-14)


def test_capacity_weighted_exchange_nonunit_epsilon():
    for eps in [.25,2.]:
        u,v=1.2,.3
        for _ in range(100):u,v=diffusion.closed_advance(u,v,.001,eps,0.)
        exact=closed_step(1.2,.3,.1,eps,0.)
        assert max(abs(u-exact[0]),abs(v-exact[1]))<.002
        assert eps*u+v==pytest.approx(eps*1.2+.3,abs=1e-12)


def test_forced_exchange_source_enters_only_radiation_budget():
    u,v=diffusion.closed_advance(1.,.2,.01,.25,.7)
    assert .25*u+v==pytest.approx(.25+.2+.007,abs=2e-15)


def test_closed_equilibrium_is_preserved():
    for eps in [.25,1.,2.]:
        u,v=diffusion.closed_advance(.8,.8,.01,eps,0.)
        assert u==pytest.approx(.8,abs=2e-15) and v==pytest.approx(.8,abs=2e-15)


def test_negative_capacity_rejected_before_evolution():
    with pytest.raises(ValueError):diffusion.solve({'cells':8,'length':1.,'epsilon':0.})


def test_signed_transport_weights_are_normalized():
    mu,w=transport.angles(16)
    assert np.sum(w)==pytest.approx(2.,abs=2e-15) and np.sum(w*mu)==pytest.approx(0.,abs=2e-15)


def test_uniform_actual_transport_operator_capacity_and_source_signs():
    mu,w=transport.angles(8);I=np.full((8,8),2.);V=np.ones(8);Q=np.full(8,.3)
    a,b,f=transport.rhs(I,V,mu,w,.125,.25,Q,periodic=True)
    np.testing.assert_allclose(a,-.7/.25,atol=2e-15);np.testing.assert_allclose(b,1.,atol=2e-15)
    assert f==0 and np.max(abs(.25*.5*np.sum(w[:,None]*a,axis=0)+b-Q))<2e-15


def test_reflecting_boundary_and_outflow_conserve_full_energy():
    mu,w=transport.angles(8);I=.2+np.arange(64).reshape(8,8)/64;V=np.ones(8)*.3;Q=np.zeros(8)
    a,b,out=transport.rhs(I,V,mu,w,.125,2.,Q)
    assert abs(.125*np.sum(2*.5*np.sum(w[:,None]*a,axis=0)+b)+out)<2e-14


def test_vacuum_and_zero_source_remain_vacuum():
    mu,w=transport.angles(8);a,b,f=transport.rhs(np.zeros((8,8)),np.zeros(8),mu,w,.125,1.,np.zeros(8))
    assert not np.any(a) and not np.any(b) and f==0.


def test_actual_box_source_halfspace_energy_strength():
    c={'cells':8,'length':1.,'epsilon':1.,'ordinates':8,'times':[.001],'max_dt':.001,'source_off':10.}
    out=transport.solve(c)
    assert out['history'][-1,1]==pytest.approx(.5*.001,abs=2e-16)


def test_invalid_ordinate_count_rejected():
    for n in [0,1,3]:
        with pytest.raises(ValueError):transport.angles(n)


def test_reference_closed_formula_separates_capacity_convention():
    u,v=closed_step(1.,0.,.3,.25,0.)
    assert .25*u+v==pytest.approx(.25,abs=2e-15)
    assert u-v==pytest.approx(np.exp(-5*.3),abs=2e-15)


def test_qualified_independent_data_have_both_energy_fields():
    with np.load(io_contract.ROOT/'references/transport-reference.npz',allow_pickle=False) as f:
        assert f['values'].shape==(3,13,2)
        assert f['values'][0,0,0]>f['values'][0,0,1]>0


def test_actual_frozen_source_and_independent_reference_contract():
    c=io_contract.verify(io_contract.ROOT/'inputs.json');assert c['planned_primary_runs']==10


def test_diffusion_failed_candidate_and_last_valid_are_retained(tmp_path,monkeypatch):
    class InvalidFactor:
        def solve(self,rhs):return np.full_like(rhs,np.nan)
    monkeypatch.setattr(diffusion,'splu',lambda matrix:InvalidFactor())
    path=tmp_path/'failed-state.npz'
    config=dict(cells=8,length=1.,epsilon=1.,times=[.001],max_dt=.001)
    with pytest.raises(ArithmeticError):diffusion.solve(config,path)
    with np.load(path,allow_pickle=False) as f:
        assert np.all(f['last_valid_u']==0) and np.isnan(f['candidate_u']).all()
        assert str(f['stage'])=='update' and int(f['step'])==0


def test_transport_failed_stage_candidate_and_last_valid_are_retained(tmp_path,monkeypatch):
    def invalid_rhs(I,V,*args,**kwargs):return np.full_like(I,-2000.),np.zeros_like(V),0.
    monkeypatch.setattr(transport,'rhs',invalid_rhs)
    path=tmp_path/'failed-state.npz'
    config=dict(cells=8,length=1.,epsilon=1.,ordinates=8,times=[.001],max_dt=.001,source_off=10.)
    with pytest.raises(ArithmeticError):transport.solve(config,path)
    with np.load(path,allow_pickle=False) as f:
        assert np.all(f['last_valid_intensity']==0) and np.all(f['candidate_intensity1']==-2.)
        assert str(f['stage'])=='euler1' and 'candidate_intensity2' not in f


def test_completed_pde_candidate_survives_later_comparison_failure(tmp_path,monkeypatch):
    import run as driver
    candidate=dict(x=np.zeros(1),states=np.zeros((1,2,1)),times=np.zeros(1),history=np.zeros((1,7)))
    monkeypatch.setattr(driver.diffusion,'solve',lambda *args:candidate)
    def fail_comparison(*args):raise ArithmeticError('intentional reference diagnostic failure')
    monkeypatch.setattr(driver,'compare',fail_comparison)
    cfg={'cases':{'su-olson-diffusion1996':[{'id':'retention-fixture'}]}}
    with pytest.raises(ArithmeticError,match='reference diagnostic'):driver.execute(cfg,{},tmp_path,[])
    with np.load(tmp_path/'su-olson-diffusion1996-retention-fixture.npz',allow_pickle=False) as f:
        np.testing.assert_array_equal(f['states'],candidate['states'])
    assert (tmp_path/'su-olson-diffusion1996-retention-fixture-history.csv').is_file()
