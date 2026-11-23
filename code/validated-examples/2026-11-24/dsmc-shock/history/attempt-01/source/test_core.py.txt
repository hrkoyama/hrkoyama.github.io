import numpy as np
import pytest
from scipy.integrate import quad
from dsmc import (SIGMA,FluxSampler,positive_flux,collision_round,totals,
                  stream_wall,initialize,raw_profile,profile,PhysicalFailure)
from diagnostics import ensemble,stationarity


def test_zero_drift_incoming_flux():
    assert abs(positive_flux(0,2)-1/np.sqrt(np.pi))<2e-15


def test_flux_cdf_independent_adaptive_integral():
    sampler=FluxSampler(2.58,1)
    for v in [.001,.02,1,3,6]:
        integral=quad(lambda z:z*np.exp(-.5*(z-2.58)**2)/np.sqrt(2*np.pi),0,v,epsabs=1e-14)[0]
        assert abs(float(sampler.cdf(v))-integral/sampler.flux)<3e-13


def test_flux_inverse_extreme_probabilities():
    class Fixed:
        def random(self,n):return np.array([0,1e-14,1e-8,.1,.9,1-1e-12])
    for u,t in [(2.58,1),(-1.13,2.08),(0,1)]:
        sampler=FluxSampler(u,t);v=sampler.sample(Fixed(),6)
        assert np.all(np.diff(v)>0)
        assert np.max(np.abs(sampler.cdf(v)-Fixed().random(6)))<2e-12


def test_even_pair_physical_rate():
    v=np.array([[-1.,0,0],[1.,0,0]])
    out=collision_round(np.array([.2,.7]),v,1,1.,.03,.01,np.random.default_rng(112))
    assert out['candidates']==1
    assert abs(out['max_probability']-.03*SIGMA*2*.01)<1e-15


def test_odd_pair_physical_rate_correction():
    v=np.array([[0.,2/np.sqrt(3),0],[-1.,-1/np.sqrt(3),0],[1.,-1/np.sqrt(3),0]])
    out=collision_round(np.array([.2,.4,.7]),v,1,1.,.03,.01,np.random.default_rng(113))
    assert out['candidates']==1
    assert abs(out['max_probability']-3*.03*SIGMA*2*.01)<1e-15


def test_physical_collisions_conserve_pair_invariants():
    rng=np.random.default_rng(114);v=rng.normal(size=(64,3));x=rng.random(64)
    before=totals(v,1/64);accepted=0
    for _ in range(30):accepted+=collision_round(x,v,4,1.,1/64,.02,rng)['collisions']
    assert accepted>0
    np.testing.assert_allclose(totals(v,1/64),before,rtol=0,atol=3e-14)


def test_collision_subcycle_cap_fails_without_clipping():
    with pytest.raises(PhysicalFailure,match='subcycle cap'):
        collision_round(np.array([.2,.7]),np.array([[-1.,0,0],[1.,0,0]]),1,1,1,100,np.random.default_rng(115))


def test_empty_and_single_particle_cells_have_no_self_collision():
    v=np.array([[1.,2,3]])
    out=collision_round(np.array([.2]),v,8,1,1,.01,np.random.default_rng(116))
    assert out['candidates']==out['collisions']==0
    np.testing.assert_array_equal(v,[[1,2,3]])


def test_fixed_weight_mesh_companion_has_identical_initial_particles():
    config={'kind':'wall','cells':16,'length':2,'weight':1/512,'temperatures':[1,2],'speeds':[0,0]}
    x,v,_=initialize(config,117);config['cells']=32;y,w,_=initialize(config,117)
    np.testing.assert_array_equal(x,y);np.testing.assert_array_equal(v,w)


def test_flux_weighted_diffuse_wall_moments():
    rng=np.random.default_rng(118);n=25000;x=np.zeros(n);v=np.zeros((n,3));v[:,0]=-1
    before=totals(v,1/n)
    ledger,hits=stream_wall(x,v,.0001,1,[2,2],[1,1],rng,1/n)
    assert hits.tolist()==[n,0]
    assert abs(np.mean(v[:,0]**2)-4)<.12
    assert abs(np.mean(v[:,1])-1)<.04
    assert abs(np.var(v[:,1])-2)<.08
    np.testing.assert_allclose(totals(v,1/n)-before,ledger.sum(axis=0),rtol=0,atol=1e-13)


def test_wall_frame_energy_and_impulse_ledger():
    rng=np.random.default_rng(119);x=np.array([0.,1.]);v=np.array([[-1.,2,3],[2.,-1,1]])
    before=totals(v,.2)
    ledger,hits=stream_wall(x,v,.001,1,[1,2],[-.5,.5],rng,.2)
    assert hits.tolist()==[1,1]
    np.testing.assert_allclose(totals(v,.2)-before,ledger.sum(axis=0),atol=3e-15,rtol=0)


def test_raw_moments_remove_streaming_and_recover_full_flux():
    thermal=np.concatenate((np.sqrt(3)*np.eye(3),-np.sqrt(3)*np.eye(3)))
    v=thermal+np.array([1,2,3]);p=profile(raw_profile(np.full(6,.5),v,1,1,1/6))[0]
    np.testing.assert_allclose(p[[0,1,2,3,4,5,6,7,8,9,10]],[1,1,2,3,1,1,0,0,1,2,9.5],rtol=0,atol=5e-14)


def test_raw_heat_flux_matches_direct_peculiar_velocity_sum():
    v=np.array([[1.,2,3],[2.,1,0],[-2.,4,1],[5.,-1,2],[-1.,0,3]])
    p=profile(raw_profile(np.full(5,.5),v,1,1,.2))[0]
    c=v-v.mean(axis=0);direct=.5*.2*np.sum(c[:,0]*np.sum(c*c,axis=1))
    assert abs(p[7]-direct)<2e-14


def test_seed_standard_error_uses_whole_runs():
    mean,se=ensemble(np.array([0.,1,2,3]))
    assert mean==1.5 and abs(se-np.sqrt(5/12))<1e-15


def test_stationarity_equivalence_rejects_deterministic_drift():
    values=np.ones((4,5,8,11));values[:,:,:,2]=np.arange(5)[None,:,None]
    assert stationarity(values,'dsmc-couette',2)['profile_equivalence']['2']>1


def test_invalid_particle_position_is_rejected():
    with pytest.raises(PhysicalFailure,match='outside domain'):
        collision_round(np.array([-.1]),np.array([[1.,2,3]]),4,1,1,.01,np.random.default_rng(120))
