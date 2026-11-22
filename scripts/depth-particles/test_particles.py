"""Independent identities, references, invariants and adverse-input checks."""
import json
from pathlib import Path
import numpy as np
import pytest
from electrostatics import ewald,spme,assignment,nacl_theta_reference
from fmm import fmm,direct
from transport import poisson,cic_deposit,cic_gather,cold_plasma,elastic_round,dsmc_ensemble,absorption_slab
from run import run


@pytest.fixture(scope='module')
def config():return json.loads(Path(__file__).with_name('inputs.json').read_text())


@pytest.fixture(scope='module')
def results(config):return run(config)


def test_all_declared_benchmarks_and_no_hidden_tolerance_changes(config,results):
    assert results['passed'] and len(results['cases'])==6
    assert set(results['checks'])=={'ewald','spme','fmm','pic','dsmc','radiation-transport'}
    assert all(c['checks'] and all(c['checks'].values()) for c in results['cases'])
    assert config['spme']['acceptance']['force_error']==2e-4
    assert config['pic']['acceptance']['mode_error']==2e-3


def test_theta_integral_is_independent_of_three_dimensional_sums():
    a,ea=nacl_theta_reference(1e-12,12);b,eb=nacl_theta_reference(1e-13,24)
    assert abs(a-b)<5e-13 and max(ea,eb)<1e-11
    assert abs(a-1.7475645946331822)<5e-13


def test_ewald_translation_and_permutation_invariance(config):
    c=config['ewald'];x=np.array(c['positions']);q=np.array(c['charges'])
    e,f=ewald(x,q)
    moved,g=ewald(x+np.array([.134,.275,.319]),q)
    order=np.array([3,0,6,4,1,2,7,5]);reordered,h=ewald(x[order],q[order])
    assert abs(e-moved)<1e-11 and abs(e-reordered)<1e-11
    assert np.max(abs(g-f))<1e-10 and np.max(abs(h-f[order]))<1e-10
    assert np.max(abs(f.sum(axis=0)))<1e-11


@pytest.mark.parametrize('bad', ['net_charge','collision','nan'])
def test_ewald_rejects_unsupported_physics(config,bad):
    x=np.array(config['ewald']['positions']);q=np.array(config['ewald']['charges'],float)
    if bad=='net_charge':q[0]+=1
    if bad=='collision':x[1]=x[0]+[1,0,0]
    if bad=='nan':x[0,0]=np.nan
    with pytest.raises(ValueError):ewald(x,q)


@pytest.mark.parametrize('order',[4,6,8])
def test_bspline_partition_and_derivative(order):
    for value in [.001,.123,.499,.881,.999]:
        indices,w,dw=assignment(np.array([value,.371,.714]),1.,32,order)
        for axis in range(3):
            assert len(indices[axis])==order and abs(w[axis].sum()-1)<5e-11
            assert min(w[axis])>-1e-10 and abs(dw[axis].sum())<1e-8


def test_spme_is_energy_gradient_not_force_lookup(config):
    x=np.array(config['ewald']['positions']);q=np.array(config['ewald']['charges']);step=2e-6
    energy,force,charge=spme(x,q,mesh=32,order=6)
    for atom,axis in [(0,0),(2,1),(7,2)]:
        lo=x.copy();hi=x.copy();lo[atom,axis]-=step;hi[atom,axis]+=step
        fd=-(spme(hi,q,mesh=32,order=6)[0]-spme(lo,q,mesh=32,order=6)[0])/(2*step)
        assert abs(fd-force[atom,axis])<1e-6
    assert np.isfinite(energy) and charge<1e-10
    with pytest.raises(ValueError):spme(x,q,mesh=8,order=6)


def test_fmm_contains_far_and_local_translations_and_converges(results):
    case=next(c for c in results['cases'] if c['id']=='fmm')
    rows=case['records'];assert rows[-1]['m2l_translations']>0 and rows[-1]['l2l_translations']>0
    assert rows[-1]['near_pairs']<rows[-1]['all_pairs']
    assert rows[-1]['field_max_error']<1e-3*rows[0]['field_max_error']


def test_fmm_two_sources_and_free_space_force_sign():
    z=np.array([.1+.1j,.9+.9j]);q=np.array([1.,-2.])
    refp,reff=direct(z,q);p,f,_=fmm(z,q,order=12,depth=3)
    assert np.max(abs(p-refp))<1e-10 and np.max(abs(f-reff))<1e-9
    assert f[0,0]>0 and f[0,1]>0 # opposite charge at upper right attracts positive target


def test_fmm_permutation_and_potential_gradient():
    rng=np.random.default_rng(17);z=rng.uniform(.05,.95,32)+1j*rng.uniform(.05,.95,32);q=rng.normal(size=32)
    p,f,_=fmm(z,q,12,3);order=np.arange(31,-1,-1);a,b,_=fmm(z[order],q[order],12,3)
    assert np.max(abs(a-p[order]))<1e-12 and np.max(abs(b-f[order]))<1e-11
    h=1e-6;lo=z.copy();hi=z.copy();lo[0]-=h;hi[0]+=h
    # Its own source is excluded, so moving target 0 differentiates its potential.
    fd=-(fmm(hi,q,12,3)[0][0]-fmm(lo,q,12,3)[0][0])/(2*h)
    assert abs(fd-f[0,0])<1e-6
    with pytest.raises(ValueError):fmm(np.array([.1+.1j,.1+.1j]),np.ones(2))


def test_spectral_poisson_matches_manufactured_mode():
    n=64;length=2*np.pi;x=np.arange(n)*length/n
    e,residual=poisson(np.cos(3*x),length)
    assert np.max(abs(e-np.sin(3*x)/3))<1e-14 and residual<1e-14
    with pytest.raises(ValueError):poisson(np.array([np.nan]*8),1.)


def test_cic_charge_and_single_particle_self_force():
    length=2*np.pi
    for position in [0.,.0001,.417,length-1e-8]:
        x=np.array([position]);rho=cic_deposit(x,length,64,length)
        assert abs(rho.sum()*length/64)<1e-13
        e,_=poisson(rho,length);assert abs(cic_gather(e,x,length)[0])<1e-13


def test_pic_reproduces_small_amplitude_oscillation():
    r=cold_plasma(64,8,.05,np.pi,.001)
    assert r['max_mode_error']<.01 and r['charge_error']<1e-12
    assert r['poisson_residual']<1e-12
    with pytest.raises(ValueError):cold_plasma(amplitude=.1)


def test_each_elastic_round_preserves_momentum_and_energy():
    rng=np.random.default_rng(823);v=rng.normal(size=(64,3));p=v.sum(axis=0);e=np.sum(v*v)
    for _ in range(30):
        elastic_round(v,rng)
        assert np.max(abs(v.sum(axis=0)-p))<1e-12
        assert abs(np.sum(v*v)-e)<1e-11
    with pytest.raises(ValueError):elastic_round(np.ones((3,3)),rng)


def test_dsmc_fixed_seed_is_reproducible_and_not_a_continuum_timestep():
    a=dsmc_ensemble(256,4,3);b=dsmc_ensemble(256,4,3)
    assert a==b and len(a['records'])==4
    assert a['records'][0]['expected']==3.
    assert a['energy_error']<1e-13
    with pytest.raises(ValueError):dsmc_ensemble(255,4,3)


def test_absorption_upwind_is_positive_conservative_and_first_order():
    a=absorption_slab(32,8,.7);b=absorption_slab(64,8,.7)
    assert 0<=a['minimum_intensity']<=a['maximum_intensity']<=1
    assert a['balance_error']<1e-12 and b['balance_error']<1e-12
    assert b['spatial_flux_error']<.6*a['spatial_flux_error']
    assert b['flux']>b['discrete_ray_reference'] # first-order upstream numerical diffusion


def test_absorption_formal_rays_and_angular_integral():
    a=absorption_slab(8,32,.7,'exponential')
    assert a['ray_max_error']<1e-14 and a['angular_flux_error']<1e-8
    with pytest.raises(ValueError):absorption_slab(optical_depth=-1)


@pytest.mark.parametrize('bad',['budget','empty_acceptance','nan_tolerance'])
def test_runner_rejects_invalid_budgets_and_acceptance(config,bad):
    import copy
    c=copy.deepcopy(config)
    if bad=='budget':c['spme']['meshes'][-1]=1000000
    if bad=='empty_acceptance':c['ewald']['acceptance']={}
    if bad=='nan_tolerance':c['pic']['acceptance']['mode_error']=float('nan')
    with pytest.raises(ValueError):run(c)


@pytest.mark.parametrize('rho',[np.ones(8),np.arange(8.),np.zeros((8,2))])
def test_periodic_poisson_rejects_incompatible_zero_mode_and_shape(rho):
    with pytest.raises(ValueError):poisson(rho,1.)


def test_radiation_errors_separate_angle_from_space():
    upstream=absorption_slab(32,8,.7,'upwind')
    exact_rays=absorption_slab(32,8,.7,'exponential')
    assert upstream['angular_flux_error']==exact_rays['angular_flux_error']
    assert upstream['spatial_flux_error']>100*upstream['angular_flux_error']
    assert abs(upstream['total_flux_error']-abs(upstream['flux']-upstream['continuum_reference']))<1e-15
    assert exact_rays['spatial_flux_error']<1e-14
