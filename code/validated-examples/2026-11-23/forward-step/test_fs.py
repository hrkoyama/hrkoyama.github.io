"""Analytic jump, wall invariants, orientation and raw failure-path checks."""
from pathlib import Path
from unittest.mock import patch
import hashlib
import json
import numpy as np
import pytest
import fs_solver as s
import run

ROOT = Path(__file__).resolve().parent

def test_primitive_conserved_round_trip():
    w = np.array([[1.4,3.,0.,1.],[3.,1.,-.7,5.]])
    np.testing.assert_allclose(s.primitive(s.conserved(w)),w,rtol=3e-15)

def test_stationary_mach3_normal_shock_rankine_hugoniot():
    ratio = (s.GAMMA+1)*9/((s.GAMMA-1)*9+2)
    pressure = 1+2*s.GAMMA/(s.GAMMA+1)*8
    downstream = s.conserved([1.4*ratio,3/ratio,0.,pressure])
    np.testing.assert_allclose(s.flux(downstream,0),s.flux(s.upstream(),0),rtol=3e-15,atol=2e-14)

def test_hll_equal_state_consistency_x():
    q = s.conserved(np.array([[2.,3.,.4,1.7]])); np.testing.assert_allclose(s.hll(q,q,0),s.flux(q,0),rtol=2e-15)

def test_hll_equal_state_consistency_y():
    q = s.conserved(np.array([[2.,3.,.4,1.7]])); np.testing.assert_allclose(s.hll(q,q,1),s.flux(q,1),rtol=2e-15)

def test_hll_coordinate_exchange():
    a = s.conserved(np.array([[2.,1.,-.2,3.]])); b = s.conserved(np.array([[1.,-.3,.5,1.]])); sw = [0,2,1,3]
    np.testing.assert_allclose(s.hll(a,b,0)[...,sw],s.hll(a[...,sw],b[...,sw],1),rtol=2e-15)

def test_bad_density_rejected():
    with pytest.raises(ValueError): s.primitive(np.array([0.,0.,0.,1.]))

def test_negative_internal_energy_rejected():
    with pytest.raises(ValueError): s.primitive(np.array([1.,10.,0.,1.]))

def test_nonfinite_state_rejected():
    with pytest.raises(ValueError): s.primitive(np.array([1.,0.,0.,np.inf]))

def test_exact_aligned_geometry_and_fluid_area():
    x,y,fluid,q = s.initial(20)
    assert q.shape==(60,20,4) and abs(fluid.sum()/20**2-2.52)<1e-14
    np.testing.assert_array_equal(fluid,~((x[:,None]>=.6)&(y[None,:]<.2)))
    assert np.all(fluid[:12]) and not np.any(fluid[12:,:4]) and np.all(fluid[:,4:])

def test_unaligned_geometry_rejected():
    for ny in [8,21,20.,True]:
        with pytest.raises(ValueError): s.geometry(ny)

def test_exact_inlet_and_zero_gradient_outlet():
    x,y,fluid,q = s.initial(10); q = s.conserved(np.broadcast_to([2.,2.,.2,3.],q.shape))
    (fx,ml,mr),unused = s.face_fluxes(q,fluid)
    np.testing.assert_allclose(fx[0],s.hll(np.broadcast_to(s.upstream(),q[0].shape),q[0],0),rtol=2e-15)
    np.testing.assert_allclose(fx[-1][fluid[-1]],s.flux(q[-1][fluid[-1]],0),rtol=2e-15)

def test_top_bottom_slip_has_no_mass_energy_or_tangential_flux():
    x,y,fluid,q = s.initial(10); q = s.conserved(np.broadcast_to([2.,2.,.2,3.],q.shape))
    unused,(fy,ml,mr) = s.face_fluxes(q,fluid)
    for f in [fy[:,-1],fy[:,0][fluid[:,0]]]:
        np.testing.assert_allclose(f[:,[0,1,3]],0,atol=2e-14)
        assert np.all(f[:,2]>0)

def test_vertical_step_wall_reflects_normal_momentum_only():
    x,y,fluid,q = s.initial(10)
    (fx,ml,mr),unused = s.face_fluxes(q,fluid); f = fx[ml & ~mr]
    assert len(f)==2
    np.testing.assert_allclose(f[:,[0,2,3]],0,atol=2e-14)
    assert np.all(f[:,1]>1.)

def test_horizontal_step_wall_has_correct_pressure_traction():
    x,y,fluid,q = s.initial(10)
    unused,(fy,ml,mr) = s.face_fluxes(q,fluid); f = fy[~ml & mr]
    assert len(f)==24
    np.testing.assert_allclose(f,np.broadcast_to([0.,0.,1.,0.],f.shape),atol=2e-14)

def test_solid_dummy_storage_does_not_change_fluid_derivative():
    x,y,fluid,q = s.initial(10); a,b = s.rhs(q,fluid,.1)
    changed = q.copy(); changed[~fluid] = s.conserved([9.,-2.,3.,8.]); c,d = s.rhs(changed,fluid,.1)
    np.testing.assert_array_equal(a[fluid],c[fluid]); np.testing.assert_array_equal(b,d)
    np.testing.assert_array_equal(a[~fluid],0)

def test_full_fluid_flux_divergence_telescopes_to_all_boundaries():
    x,y,fluid,q = s.initial(10)
    q = s.conserved(np.stack((2+.03*np.broadcast_to(x[:,None],fluid.shape),
        np.full(fluid.shape,2.),np.full(fluid.shape,.1),np.full(fluid.shape,3.)),axis=-1))
    derivative,b = s.rhs(q,fluid,.1)
    np.testing.assert_allclose(.01*derivative[fluid].sum(axis=0),b.sum(axis=0),rtol=2e-14,atol=2e-12)

def test_uniform_parallel_channel_is_preserved():
    q = np.broadcast_to(s.upstream(),(30,10,4)).copy(); fluid = np.ones((30,10),dtype=bool)
    derivative,b = s.rhs(q,fluid,.1)
    np.testing.assert_allclose(derivative,0,atol=1e-14)
    np.testing.assert_allclose(b.sum(axis=0),0,atol=1e-14)

def test_step_wall_inward_impulse_orientation():
    x,y,fluid,q = s.initial(10); derivative,b = s.rhs(q,fluid,.1)
    assert b[s.BOUNDARIES.index('vertical_step'),1]<0
    assert b[s.BOUNDARIES.index('horizontal_step'),2]>0
    np.testing.assert_allclose(b[2:][:,[0,3]],0,atol=2e-14)

def test_both_heun_stages_use_shared_flux_operator():
    with patch.object(s,'rhs',wraps=s.rhs) as calls: out = s.solve(10,.0001,.4)
    assert calls.call_count==2 and out['steps']==1 and out['time']==.0001
    assert not np.array_equal(calls.call_args_list[0].args[0],calls.call_args_list[1].args[0])

def test_invalid_predictor_retains_raw_state_without_retry():
    def bad(q,fluid,h):
        d = np.zeros_like(q); d[fluid,0] = -1e100; return d,np.zeros((6,4))
    with patch.object(s,'rhs',side_effect=bad) as calls:
        with pytest.raises(s.InvalidStage) as caught: s.solve(10,.001,.4)
    assert calls.call_count==1 and np.any(caught.value.failed_state[...,0]<0)
    assert caught.value.failed_context['stage']=='predictor' and caught.value.completed_history==[]

def test_small_run_budget_and_declared_step_limit():
    out = s.solve(10,.002,.4)
    np.testing.assert_allclose(out['final_integral']-out['initial_integral']-out['boundary_net_integral'],0,atol=3e-12)
    assert out['minimum_density']>0 and out['minimum_pressure']>0 and out['state_floor_count']==out['rejected_steps']==0
    with pytest.raises(ValueError,match='step budget'): s.solve(10,4.,.4,1)

def test_restriction_preserves_fluid_integrals():
    x,y,fluid,q = s.initial(20); q = q.copy(); q[...,0] += .1*x[:,None]
    coarse = run.restriction(q,10); a,b,coarse_fluid = s.geometry(10)
    np.testing.assert_allclose(coarse[coarse_fluid].sum(axis=0)*4,q[fluid].sum(axis=0),rtol=3e-14)
    with pytest.raises(ValueError): run.restriction(q,8)

def test_independent_reference_hash_time_and_geometry():
    for n in [80,160]:
        p = ROOT/'references'/('forward-step-ny'+str(n)+'.npz'); m = json.loads(p.with_suffix('.json').read_text())
        assert hashlib.sha256(p.read_bytes()).hexdigest()==m['npz_sha256'] and m['time']==4.
        with np.load(p,allow_pickle=False) as z:
            assert z['q'].shape==(3*n,n,4) and float(z['time'])==4.
            np.testing.assert_array_equal(z['fluid'],s.geometry(n)[2])

def test_input_criteria_source_and_reference_preregistered():
    contract = json.loads((ROOT/'pre-run-contract.json').read_text()); assert contract['planned_tests']==24
    for name,digest in contract['files_sha256'].items(): assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,name
    cfg = json.loads((ROOT/'inputs.json').read_text())['cases'][run.CASE]
    assert cfg['grids']==[20,40,80] and cfg['final_time']==4. and cfg['corner_entropy_fix'] is False
