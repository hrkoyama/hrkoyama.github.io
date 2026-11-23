"""Focused algebra, independent-reference and tiny periodic conservation tests."""
import hashlib,json
import numpy as np
import pytest
import hlld,solver,run
from references import analytic
from references.qualify import official_initial,restrict

STATES=[[1,.2,-.1,.3,1,.7,-.4,.2],[.2,-1,2,-.2,.3,0,.1,.1],[3,0,0,1,.1,1,0,0]]

@pytest.mark.parametrize('state',STATES)
def test_conserved_round_trip(state):
    w=np.array(state)[None,:];np.testing.assert_allclose(hlld.primitive(hlld.conserved(w)),w,rtol=2e-14,atol=2e-14)

@pytest.mark.parametrize('axis',[0,1,2])
def test_equal_states_physical_flux(axis):
    w=np.array(STATES);f,a,s=hlld.riemann(w,w,axis=axis)
    np.testing.assert_allclose(f,hlld.physical_flux(w,axis=axis),atol=2e-14,rtol=2e-14)
    assert np.all(a>0) and s['hlle_fallback_faces']==0

@pytest.mark.parametrize('axis',[0,1,2])
def test_rejects_two_normal_fields(axis):
    a=np.array(STATES[:1]);b=a.copy();b[:,5+axis]+=.01
    with pytest.raises(ValueError,match='normal magnetic'):hlld.riemann(a,b,axis=axis)

@pytest.mark.parametrize('axis',[0,1,2])
def test_fast_speed_hydrodynamic_limit(axis):
    w=np.array(STATES);w[:,5:8]=0
    np.testing.assert_allclose(hlld.fast_speed(w,axis=axis),np.sqrt((5/3)*w[:,4]/w[:,0]),rtol=1e-14)

@pytest.mark.parametrize('component,value',[(0,0),(4,-1),(1,float('nan'))])
def test_bad_cell_state_is_rejected(component,value):
    q=hlld.conserved(np.array(STATES[:1]));q[:,component]=value
    with pytest.raises(ValueError):hlld.primitive(q)

@pytest.mark.parametrize('a,b,expected',[(1,1,1),(1,-1,0),(1,10,2)])
def test_mc_limiter(a,b,expected):assert solver.limited(np.array(a),np.array(b))==expected

@pytest.mark.parametrize('n',[16,32,64])
@pytest.mark.parametrize('time',[.125,1.])
def test_wave_exact_conserved_means(n,time):np.testing.assert_allclose(solver.exact_wave(n,time),analytic.wave_means(n,time),rtol=0,atol=2e-14)

@pytest.mark.parametrize('case',['magnetic-loop-independent','postshock-orszag-tang'])
@pytest.mark.parametrize('n',[8,16])
def test_initial_native_curl_is_solenoidal(case,n):
    q,bx,by,dx,dy=solver.initial(case,n)
    assert solver.divergence(q,bx,by,dx,dy)<1e-13

@pytest.mark.parametrize('kind',['loop','ot'])
@pytest.mark.parametrize('n',[8,16])
def test_initial_matches_independent_generator_algebra(kind,n):
    case='magnetic-loop-independent' if kind=='loop' else 'postshock-orszag-tang'
    q,*_=solver.initial(case,n);expected=official_initial(dict(kind=kind,n=n,nx=(2*n if kind=='loop' else n)))
    np.testing.assert_allclose(q,expected,atol=2e-14,rtol=2e-14)

@pytest.mark.parametrize('two_d',[False,True])
def test_uniform_state_has_zero_rhs(two_d):
    shape=(8,8,8) if two_d else (8,8);w=np.broadcast_to(STATES[0],shape).copy();q=hlld.conserved(w)
    bx=np.full((8,8),w[0,0,5]) if two_d else None;by=np.full((8,8),w[0,0,6]) if two_d else None
    r,rx,ry,_=solver.rhs(q,bx,by,.125,.125);assert np.max(abs(r))<1e-13
    if two_d:assert np.max(abs(rx))+np.max(abs(ry))<1e-13

@pytest.mark.parametrize('case',['circular-alfven-refinement','magnetic-loop-independent','postshock-orszag-tang'])
def test_tiny_heun_run_conserves_and_saves_stages(case):
    d=solver.solve(case,8,4,.001)
    assert d['history'].shape==(4,len(solver.HISTORY_COLUMNS)) and d['q_history'].shape[0]==5
    assert d['history'][:,8].max()<2e-13 and d['history'][:,6].max()<1e-13
    assert d['state_clip_count']==d['retries']==0
    np.testing.assert_allclose(d['q'].reshape(-1,8).mean(axis=0)[:5],d['q_initial'].reshape(-1,8).mean(axis=0)[:5],atol=2e-14)


def test_nested_restriction_preserves_all_integrals():
    q=np.arange(8*12*8).reshape(8,12,8);r=restrict(q,(4,3))
    np.testing.assert_allclose(r.mean(axis=(0,1)),q.mean(axis=(0,1)))


def test_nonnested_restriction_rejected():
    with pytest.raises(ValueError):restrict(np.zeros((8,8,8)),(3,4))


def test_phase_diagnostic_detects_known_shift():
    assert abs(run.phase_error(solver.exact_wave(64,.01),solver.exact_wave(64,0))-2*np.pi*.01)<1e-14


def test_frozen_hash_rejects_mutation(tmp_path):
    f=tmp_path/'fixed.txt';f.write_text('original');(tmp_path/'pre-run-contract.json').write_text(json.dumps({'files_sha256':{'fixed.txt':hashlib.sha256(f.read_bytes()).hexdigest()}}))
    run.check_frozen(tmp_path);f.write_text('changed')
    with pytest.raises(ValueError,match='Changed frozen'):run.check_frozen(tmp_path)


def test_actual_frozen_sources_and_independent_refs():
    run.check_frozen();_,qualification=run.load_references();assert qualification['passed'] and len(qualification['checks'])==31

@pytest.mark.parametrize('n,steps,t',[(7,4,.01),(8,3,.01),(8,0,.01),(8,4,0)])
def test_invalid_fixed_budget_rejected(n,steps,t):
    with pytest.raises(ValueError):solver.solve('circular-alfven-refinement',n,steps,t)


def test_tiny_positive_cell_is_not_floored():
    w=np.broadcast_to(STATES[0],(8,8)).copy();w[3,0]=1e-13
    original=w.copy();s,theta=solver.slopes(w,0)
    np.testing.assert_array_equal(w,original);assert theta[3]==0 and w[3,0]==1e-13 and np.all(s[3]==0)
