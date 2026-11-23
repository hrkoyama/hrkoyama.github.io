"""Independent jump identities, shared-flux budgets and explicit failure paths."""
from pathlib import Path
from unittest.mock import patch
import hashlib
import json
import numpy as np
import pytest
import dm_solver as s
import run

ROOT=Path(__file__).resolve().parent

def test_primitive_conserved_round_trip():
    w=np.array([[1.4,0.,0.,1.],[8.,3.,-2.,116.5]])
    np.testing.assert_allclose(s.primitive(s.conserved(w)),w,rtol=3e-15)

def test_hot_cold_normal_shock_rankine_hugoniot():
    hot,cold=s.states();normal=np.array([np.sqrt(3)/2,-.5])
    jump=normal[0]*(s.flux(hot,0)-s.flux(cold,0))+normal[1]*(s.flux(hot,1)-s.flux(cold,1))
    np.testing.assert_allclose(jump,10*(hot-cold),rtol=4e-15,atol=2e-12)

def test_equal_state_hll_consistency_x():
    q=s.conserved(np.array([[2.,3.,.4,1.7]]));np.testing.assert_allclose(s.hll(q,q,0),s.flux(q,0),rtol=2e-15)

def test_equal_state_hll_consistency_y():
    q=s.conserved(np.array([[2.,3.,.4,1.7]]));np.testing.assert_allclose(s.hll(q,q,1),s.flux(q,1),rtol=2e-15)

def test_hll_coordinate_exchange():
    a=s.conserved(np.array([[2.,1.,-.2,3.]]));b=s.conserved(np.array([[1.,-.3,.5,1.]]));sw=[0,2,1,3]
    np.testing.assert_allclose(s.hll(a,b,0)[...,sw],s.hll(a[...,sw],b[...,sw],1),rtol=2e-15)

def test_bad_density_rejected():
    with pytest.raises(ValueError):s.primitive(np.array([0.,0.,0.,1.]))

def test_negative_internal_energy_rejected():
    with pytest.raises(ValueError):s.primitive(np.array([1.,10.,0.,1.]))

def test_nonfinite_state_rejected():
    with pytest.raises(ValueError):s.primitive(np.array([1.,0.,0.,np.inf]))

def test_initial_geometry_and_cell_center_definition():
    x,y,q=s.initial(16);hot,cold=s.states()
    assert q.shape==(64,16,4) and x[0]==.03125 and y[-1]==.96875
    mask=x[:,None]<1/6+y[None,:]/np.sqrt(3)
    np.testing.assert_array_equal(q,np.where(mask[...,None],hot,cold))

def test_bottom_slip_wall_reflects_only_normal_momentum():
    x,y,q=s.initial(16);q=s.conserved(np.broadcast_to([2.,3.,-.7,4.],q.shape));g=s.ghost(q,0.,x)
    wall=x>=1/6
    np.testing.assert_array_equal(g[1:-1,0][wall],q[:,0][wall]*[1,1,-1,1])

def test_left_inflow_and_right_outflow():
    x,y,q=s.initial(16);g=s.ghost(q,.2,x);hot,cold=s.states()
    np.testing.assert_array_equal(g[0,1:-1],np.broadcast_to(hot,q[0].shape));np.testing.assert_array_equal(g[-1,1:-1],q[-1])

def test_top_boundary_advances_at_physical_stage_time():
    x,y,q=s.initial(32);hot,cold=s.states()
    g0=s.ghost(q,0.,x);g1=s.ghost(q,.1,x)
    assert np.sum(g1[1:-1,-1,0]==hot[0])>np.sum(g0[1:-1,-1,0]==hot[0])
    np.testing.assert_array_equal(g1[1:-1,-1],np.where((x<1/6+3/np.sqrt(3))[:,None],hot,cold))

def test_reflective_face_has_zero_mass_and_energy_flux():
    q=s.conserved(np.array([[2.,3.,-.7,4.]]));mirror=q*[1,1,-1,1];f=s.hll(mirror,q,1)
    np.testing.assert_allclose(f[0,[0,1,3]],0,atol=1e-14);assert f[0,2]>0

def test_flux_divergence_telescopes_to_boundary_budget():
    x,y,q=s.initial(16);d,b=s.rhs(q,.037,x,1/16)
    np.testing.assert_allclose(d.sum(axis=(0,1))/16**2,b,rtol=3e-15,atol=2e-12)

def test_both_heun_stages_use_their_actual_time():
    with patch.object(s,'rhs',wraps=s.rhs) as calls:out=s.solve(8,.0001,.4)
    assert calls.call_count==2
    assert calls.call_args_list[0].args[1]==0 and calls.call_args_list[1].args[1]==.0001
    assert out['time']==.0001

def test_invalid_predictor_preserves_raw_state_without_retry():
    def bad(q,t,x,h):
        d=np.zeros_like(q);d[...,0]=-1e100;return d,np.zeros(4)
    with patch.object(s,'rhs',side_effect=bad) as calls:
        with pytest.raises(s.InvalidStage) as caught:s.solve(8,.001,.4)
    assert calls.call_count==1 and np.any(caught.value.failed_state[...,0]<0)
    assert caught.value.failed_context['stage']=='predictor' and caught.value.completed_history==[]

def test_small_run_four_component_actual_boundary_balance():
    out=s.solve(8,.002,.4);d=out['final_integral']-out['initial_integral']-out['boundary_net_integral']
    np.testing.assert_allclose(d,0,atol=2e-12);assert out['minimum_density']>0 and out['minimum_pressure']>0
    assert out['rejected_steps']==out['state_floor_count']==0

def test_restriction_preserves_integrals_and_rejects_wrong_geometry():
    q=np.arange(32*8*4,dtype=float).reshape(32,8,4);coarse=run.restriction(q,4)
    np.testing.assert_allclose(coarse.sum(axis=(0,1))*4,q.sum(axis=(0,1)))
    with pytest.raises(ValueError):run.restriction(q,3)

def test_stored_reference_hashes_and_time_scope():
    for n in [64,128]:
        p=ROOT/'references'/('double-mach-ny'+str(n)+'.npz');m=json.loads(p.with_suffix('.json').read_text())
        assert hashlib.sha256(p.read_bytes()).hexdigest()==m['npz_sha256'] and m['time']==.2
        assert m['diagnostics']['rejected_steps']==0
        with np.load(p,allow_pickle=False) as z:assert z['q'].shape==(4*n,n,4) and float(z['time'])==.2

def test_source_inputs_criteria_and_reference_are_preregistered():
    contract=json.loads((ROOT/'pre-run-contract.json').read_text());assert contract['planned_tests']==21
    for name,digest in contract['files_sha256'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,name
    cfg=json.loads((ROOT/'inputs.json').read_text())['cases'][run.CASE]
    assert cfg['grids']==[16,32,64] and cfg['final_time']==.2
    assert cfg['wall_jet']==[1.,2.75,.25]

def test_front_diagnostic_rejects_absent_or_outside_features():
    x,y,q=s.initial(16);cfg={'front_y':.75,'front_x_window':[8.,9.]}
    with pytest.raises(ValueError):run.front(q,x,y,cfg)
    cfg['front_x_window']=[2.,3.5]
    with pytest.raises(ValueError):run.front(np.ones_like(q),x,y,cfg)
