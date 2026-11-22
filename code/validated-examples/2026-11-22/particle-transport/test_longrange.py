"""Independent long-range references, gradients, controls and finite budgets."""
import copy
import json
from pathlib import Path
import numpy as np
import pytest
import electrostatics as electro
from fmm import fmm,independent_direct,analytic_two_source,analytic_regular_ring
from longrange_experiments import build_longrange_cases,force_reference_error,sampled_gradient


@pytest.fixture(scope='module')
def config():return json.loads(Path(__file__).with_name('inputs.json').read_text())


@pytest.fixture(scope='module')
def cases(config):return {r['id']:r for r in build_longrange_cases(config)}


def test_all_longrange_cases_pass_fixed_nonempty_criteria(cases):
    assert set(cases)=={'ewald-convergence','spme-convergence','fmm-convergence'}
    for result in cases.values():
        assert result['passed'] is True and result['records'] and result['metrics']
        assert result['checks'] and all(type(v) is bool and v for v in result['checks'].values())
        assert all(np.isfinite(v) for v in result['metrics'].values())
    assert cases['ewald-convergence']['metrics']['control_force_error']>.0001
    assert cases['spme-convergence']['metrics']['coarse_control_force_error']>.0003
    assert cases['fmm-convergence']['metrics']['coarse_control_field_error']>.001


def test_theta_reference_cannot_call_primary_algorithms(monkeypatch,config,cases):
    def forbidden(*args,**kwargs):raise AssertionError('Primary numerical helper called by independent reference')
    for name in ('ewald','spme','real_space','reciprocal_vectors','assignment'):
        monkeypatch.setattr(electro,name,forbidden)
    c=config['ewald'];e,f,info=electro.theta_periodic_reference(c['positions'],c['charges'],c['length'],**c['reference_refined'])
    expected=cases['ewald-convergence']['metrics']['reference_energy']
    assert abs(e-expected)<c['acceptance']['reference_energy_refinement']
    assert np.max(abs(f))>.1 and info['left_success'] and info['right_success']
    assert info['left_status']==info['right_status']==0
    assert info['left_message'] and info['right_message']


def test_independent_theta_force_is_negative_energy_gradient(config):
    c=config['ewald'];x=np.array(c['positions']);q=np.array(c['charges'])
    e,f,info=electro.theta_periodic_reference(x,q,c['length'],**c['reference_refined'])
    measured=sampled_gradient(lambda p:electro.theta_periodic_reference(p,q,c['length'],**c['reference_refined'])[0],x,c['gradient_components'],c['finite_difference_step'])
    target=np.array([f[i,a] for i,a in c['gradient_components']])
    assert np.max(abs(target))>.1
    assert np.max(abs(measured-target))<c['acceptance']['gradient_error']


def test_theta_nacl_independent_normalization_and_zero_force():
    # Legacy analytic lattice identity fixes the overall factor/sign separately
    # from the asymmetric Ewald comparison. This is a new execution, no table fit.
    x=np.array([[i,j,k] for i in (0,1) for j in (0,1) for k in (0,1)],float)
    q=np.array([(-1.)**int(p.sum()) for p in x])
    energy,force,info=electro.theta_periodic_reference(x,q,2.,upper=40.)
    madelung,error=electro.nacl_theta_reference()
    assert abs(-energy/4-madelung)<2e-10
    assert np.max(abs(force))<2e-10 and error<1e-10


def test_corrupted_reference_force_is_detected(config,cases):
    row=next(r for r in cases['ewald-convergence']['records'] if r['series']=='force_reference')
    measured=np.array(row['forces']);reference=np.array(row['reference_forces'])
    assert force_reference_error(measured,reference)<config['ewald']['acceptance']['force_error']
    corrupted=reference.copy();corrupted[0,0]+=.01
    assert force_reference_error(measured,corrupted)>config['ewald']['acceptance']['force_error']


@pytest.mark.parametrize('bad',['net_charge','collision','nan'])
def test_both_coulomb_paths_reject_unsupported_input(config,bad):
    c=config['ewald'];x=np.array(c['positions']);q=np.array(c['charges'],float)
    if bad=='net_charge':q[0]+=1
    if bad=='collision':x[1]=x[0]+[c['length'],0,0]
    if bad=='nan':x[0,0]=np.nan
    for implementation in (electro.ewald,electro.theta_periodic_reference):
        with pytest.raises(ValueError):implementation(x,q,c['length'])


@pytest.mark.parametrize('order',[4,6])
def test_spline_partition_and_derivative_all_fixed_phases(config,order):
    c=config['spme']
    for phase in c['partition_phases']:
        indices,weights,derivatives=electro.assignment([phase,.371,.714],1.,32,order)
        for w,dw in zip(weights,derivatives):
            assert np.min(w)>-1e-12
            assert abs(w.sum()-1)<c['acceptance']['partition_error']
            assert abs(dw.sum())<c['acceptance']['partition_derivative_error']


def test_energy_gradient_spme_does_not_claim_exact_momentum(cases,config):
    c=config['spme'];case=cases['spme-convergence'];metrics=case['metrics']
    assert metrics['gradient_error']<c['acceptance']['gradient_error']
    assert metrics['fine_net_force']<c['acceptance']['fine_net_force']
    # A translation-phase-dependent mesh energy has a nonzero total force.
    # Record this actual limitation instead of silently equating energy and
    # momentum conservation or subtracting the measured force mean.
    assert metrics['fine_net_force']>100*np.finfo(float).eps
    assert metrics['phase_force_spread']>100*np.finfo(float).eps


def test_separate_cartesian_direct_matches_closed_two_source_gradient(config):
    c=config['fmm'];source=np.array(c['analytic_sources']);target=np.array(c['analytic_targets']);charges=np.array(c['analytic_charges'])
    a=np.vstack((source,target));z=a[:,0]+1j*a[:,1];q=np.r_[charges,np.zeros(len(target))]
    p,f=independent_direct(z,q);ep,ef=analytic_two_source(target,*source,*charges)
    assert np.max(abs(p[2:]-ep))<c['acceptance']['analytic_direct_potential_error']
    assert np.max(abs(f[2:]-ef))<c['acceptance']['analytic_direct_field_error']
    h=config['ewald']['finite_difference_step']
    shifted=target.copy();shifted[0,0]+=h;plus=analytic_two_source(shifted,*source,*charges)[0][0]
    shifted[0,0]-=2*h;minus=analytic_two_source(shifted,*source,*charges)[0][0]
    assert ef[0,0]>0 and abs(-(plus-minus)/(2*h)-ef[0,0])<2e-7


def test_fmm_field_matches_its_target_potential_gradient(config):
    c=config['fmm'];source=np.array(c['analytic_sources']);target=np.array(c['analytic_targets'])
    a=np.vstack((source,target));z=a[:,0]+1j*a[:,1];q=np.r_[c['analytic_charges'],np.zeros(len(target))]
    p,f,_=fmm(z,q,c['orders'][-1],c['baseline_depth'])
    h=config['ewald']['finite_difference_step'];hi=z.copy();lo=z.copy();hi[-1]+=h;lo[-1]-=h
    derivative=-(fmm(hi,q,c['orders'][-1],c['baseline_depth'])[0][-1]-fmm(lo,q,c['orders'][-1],c['baseline_depth'])[0][-1])/(2*h)
    assert abs(derivative-f[-1,0])<2e-7


def test_closed_ring_polynomial_reference_matches_separate_pair_loop(config):
    c=config['fmm'];center=complex(*c['multipole_center']);radius=c['multipole_radius'];n=c['multipole_sources'];target=complex(*c['multipole_target'])
    ring=center+radius*np.exp(2j*np.pi*np.arange(n)/n)
    p,f=independent_direct(np.r_[ring,target],np.r_[np.ones(n),0.])
    exact_p,exact_f=analytic_regular_ring(target,center,radius,n)
    assert abs(p[-1]-exact_p)<1e-13 and np.max(abs(f[-1]-exact_f))<1e-12


@pytest.mark.parametrize('kwargs',[{'depth':0},{'depth':5},{'depth':2.5},{'order':0},{'order':21},{'order':2.5}])
def test_fmm_rejects_invalid_or_unbounded_tree_parameters(kwargs):
    with pytest.raises(ValueError):fmm(np.array([.2+.2j,.8+.8j]),np.array([1.,-1.]),**kwargs)


@pytest.mark.parametrize('kwargs',[{'mesh':8,'order':6},{'mesh':32,'order':3}])
def test_spme_rejects_invalid_mesh_and_order(config,kwargs):
    c=config['ewald']
    with pytest.raises(ValueError):electro.spme(c['positions'],c['charges'],**kwargs)
