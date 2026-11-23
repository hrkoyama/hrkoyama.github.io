"""25 small algebra/operator/runner regressions; six fixed runs remain in run.py."""
import json
from pathlib import Path
import sys
import numpy as np
import pytest
import relativistic as s
from references import exact as e
import run


STATES=np.array([[1.,.2,-.1,.15,.4,.3,-.6],
                 [.7,-.35,.11,.05,1.2,-.4,.2],
                 [2.,0.,.3,-.3,.05,1.1,.8]])


@pytest.mark.parametrize('bx',[0.,.7,-1.2])
def test_full_tensor_flux(bx):
    u,f=s.state(STATES,bx,4/3)
    eu,ef=e.tensor_state(STATES,bx,4/3)
    np.testing.assert_allclose(u,eu,atol=8e-15,rtol=4e-15)
    np.testing.assert_allclose(f,ef,atol=8e-15,rtol=4e-15)


@pytest.mark.parametrize('bx,gamma',[(0.,5/3),(.7,4/3),(-1.2,5/3),(2.,4/3)])
def test_full_recovery(bx,gamma):
    u,_=e.tensor_state(STATES,bx,gamma)
    w,stats=s.recover(u,bx,gamma)
    np.testing.assert_allclose(w,STATES,atol=2e-11,rtol=2e-11)
    assert stats['root_residual']<=3e-13


@pytest.mark.parametrize('row',range(3))
def test_independent_zero_field(row):
    w=STATES[row].copy();w[5:]=0
    u,f=s.state(w,0.,5/3)
    expected,ef=e.independent_srhd(u,5/3)
    actual,_=s.recover(u,0.,5/3)
    np.testing.assert_allclose(actual,expected,atol=2e-11,rtol=2e-11)
    np.testing.assert_allclose(f,ef,atol=2e-12,rtol=2e-12)


@pytest.mark.parametrize('column,value',[(0,-1.),(4,0.),(1,1.1)])
def test_primitive_reject(column,value):
    w=STATES.copy();w[1,column]=value
    with pytest.raises(ValueError,match='nonphysical'):s.state(w,1.,4/3)


@pytest.mark.parametrize('column,value',[(0,0.),(4,np.nan)])
def test_conserved_reject(column,value):
    u,_=s.state(STATES,1.,4/3);u[1,column]=value
    with pytest.raises(ValueError,match='nonpositive/nonfinite'):s.recover(u,1.,4/3)
    with pytest.raises(s.PhysicsFailure) as failure:s.solve(u,1.,4/3,.001,True,snapshots=3)
    data=failure.value.payload
    np.testing.assert_equal(data['candidate_U'],u)
    np.testing.assert_equal(data['last_valid_U'],u)
    assert data['step']==1 and data['stage']==0 and data['time']==0
    assert data['face_primitives_available'] is False and data['face_left'].shape==(0,7)


def test_induction_and_lorentz_coupling(monkeypatch):
    w=STATES.copy();u,f=s.state(w,.9,4/3)
    np.testing.assert_allclose(f[:,5],w[:,1]*w[:,5]-.9*w[:,2])
    np.testing.assert_allclose(f[:,6],w[:,1]*w[:,6]-.9*w[:,3])
    z=w.copy();z[:,5:]=0;uz,fz=s.state(z,.9,4/3)
    # Magnetic fields alter momentum, energy AND their fluxes, not just induction.
    assert np.max(abs(u[:,1:5]-uz[:,1:5]))>.05
    assert np.max(abs(f[:,1:5]-fz[:,1:5]))>.05
    original=s.state
    def face_failure(w,bx,gamma):
        if len(w)==len(u)+1:raise ValueError('injected face failure')
        return original(w,bx,gamma)
    monkeypatch.setattr(s,'state',face_failure)
    with pytest.raises(s.PhysicsFailure,match='injected face failure') as failure:s.solve(u,.9,4/3,.001,True,snapshots=3)
    data=failure.value.payload
    np.testing.assert_equal(data['candidate_U'],u)
    assert data['face_left'].shape==data['face_right'].shape==(4,7)
    assert data['face_primitives_available'] is True and data['stage']==0


def test_periodic_flux_telescopes_all_seven():
    x=(np.arange(16)+.5)/16;u,_=e.tensor_state(e.alfven_primitive(x,.13),1.,4/3)
    rhs,boundary,stats=s.operator(u,1.,4/3,1/16,True)
    np.testing.assert_allclose(rhs.sum(axis=0)/16,0.,atol=2e-14)
    np.testing.assert_array_equal(boundary,np.zeros(7))
    assert stats['face_maximum_speed']<1


def test_uniform_full_magnetic_state_preserved():
    u,_=e.tensor_state(np.repeat(STATES[0,None],12,axis=0),.8,4/3)
    out=s.solve(u,.8,4/3,.007,True,snapshots=3)
    np.testing.assert_allclose(out['U'],u,atol=1e-14,rtol=1e-14)
    assert len(out['stages'])==4*out['steps']


def test_short_full_wave_evolves_not_static():
    edges=np.linspace(0,1,17);u=e.alfven_means(edges,0.)
    out=s.solve(u,1.,4/3,.01,True,snapshots=3)
    assert np.max(abs(out['U'][:,5:]-u[:,5:]))>1e-3
    assert np.max(abs(out['conservation'][:,1:8]))<2e-13
    assert out['state_floor_count']==out['retries']==out['rejected_steps']==0


def test_nonperiodic_ssp_boundary_budget():
    edges=np.linspace(0,1,17);u=e.collision_means(edges,0.)
    out=s.solve(u,0.,5/3,.01,False,snapshots=3)
    # Inflow at both ends adds mass: a periodic-only conservation test misses this.
    assert out['conservation'][-1,8]<0
    assert out['U'][:,0].sum()>u[:,0].sum()
    assert np.max(abs(out['conservation'][:,1:8]))<2e-13


def test_two_shocks_satisfy_independent_jump():
    star=e.collision_star();assert star['density']>1 and star['pressure']>.1
    w=np.array([[1.,.3,0,0,.1,0,0],[star['density'],0,0,0,star['pressure'],0,0]])
    u,f=e.tensor_state(w,0.,5/3)
    np.testing.assert_allclose(f[1]-f[0],-star['speed']*(u[1]-u[0]),atol=2e-12)
    assert abs(star['taub_residual'])<2e-12


def test_exact_shock_cut_cell_integral():
    edges=np.array([0.,.47,.51,1.]);t=.13
    coarse=e.collision_means(edges,t)
    split=np.sort(np.r_[edges,.5-e.collision_star()['speed']*t,.5+e.collision_star()['speed']*t])
    fine=e.collision_means(split,t)
    np.testing.assert_allclose(np.diff(edges)@coarse,np.diff(split)@fine,atol=2e-15)


def test_independent_reference_qualification_and_serialization():
    q=e.qualify()
    assert q['passed'] and len(q['checks'])==6
    assert all(type(v) is bool for v in q['checks'].values())
    assert json.loads(json.dumps(q,allow_nan=False))['passed'] is True


def test_scientific_contract_rejects_tamper(tmp_path,monkeypatch):
    (tmp_path/'inputs.json').write_text('{}')
    contract={'files_sha256':{'inputs.json':run.sha(tmp_path/'inputs.json')}}
    (tmp_path/'pre-run-contract.json').write_text(json.dumps(contract));monkeypatch.setattr(run,'ROOT',tmp_path)
    assert run.verify_contract()==contract
    (tmp_path/'inputs.json').write_text('{"changed":true}')
    with pytest.raises(ValueError,match='changed scientific contract'):run.verify_contract()


def test_complete_native_result_envelope(tmp_path,monkeypatch):
    source=Path(__file__).parent;out=tmp_path/'results';cfg=tmp_path/'inputs.json'
    cfg.write_bytes((source/'inputs.json').read_bytes())
    (tmp_path/'acceptance.json').write_bytes((source/'acceptance.json').read_bytes())
    (tmp_path/'pre-run-contract.json').write_text(json.dumps({'files_sha256':{}}))
    monkeypatch.setattr(run,'ROOT',tmp_path)
    monkeypatch.setattr(e,'qualify',lambda:{'passed':True,'checks':{'independent':True}})
    def case(ident,*args):return {'id':ident,'passed':True,'checks':{'physical':True},'metrics':{'x':1.},'records':[{'n':1}]}
    monkeypatch.setattr(run,'run_case',case)
    monkeypatch.setattr(sys,'argv',['run.py','--input',str(cfg),'--output',str(out)])
    with pytest.raises(SystemExit) as status:run.main()
    assert status.value.code==0
    result=json.loads((out/'result.json').read_text())
    assert result['termination']=='fixed_budget_completed' and result['failure'] is None
    assert result['checks']=={'srhd-collision':True,'srmhd-alfven':True}
    assert all(type(v) is bool for v in result['checks'].values())
    assert result['numerical_gate_count']==2 and result['input_sha256']==run.sha(cfg)
    assert [r['id'] for r in result['cases']]==list(result['checks'])
