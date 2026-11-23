"""Small analytic/operator tests, separate from the fixed physical batch."""
import numpy as np
import pytest
import primary
import loading
from references.estimate import damped,growing
from references.linear import dispersion,upper_plane_integral,volterra


def fixture():
    n=8;length=2*np.pi;x=np.repeat(np.arange(n)*length/n,[3,2,1,2,3,2,1,2]);return n,length,x


def test_single_mode_charge():
    n,l,x=fixture();a,e,r,d=primary.field(x,n,l);np.testing.assert_allclose(r,-.5*np.cos(2*np.arange(n)*l/n),atol=2e-15)

def test_analytic_poisson_sign():
    n,l,x=fixture();a,e,r,d=primary.field(x,n,l);np.testing.assert_allclose(e,-.25*np.sin(2*np.arange(n)*l/n),atol=2e-15)

def test_electron_force_sign():
    n,l,x=fixture();a,e,r,d=primary.field(x,n,l);np.testing.assert_allclose(a,.25*np.sin(2*x),atol=2e-15)

def test_matched_cic_momentum():
    rng=np.random.default_rng(7);x=rng.uniform(0,5,41);a,*_=primary.field(x,15,5);assert abs(a.sum())<2e-14

def test_positive_unequal_weight_momentum():
    rng=np.random.default_rng(8);x=rng.uniform(0,5,41);w=rng.uniform(.5,1.5,41);w*=5/w.sum();a,*_=primary.field(x,16,5,w);assert abs(np.sum(w*a))<2e-14

def test_periodic_translation():
    n,l,x=fixture();a,e,r,d=primary.field(x,n,l);b,*_=primary.field(x+5*l,n,l);np.testing.assert_allclose(a,b,atol=5e-15)

def test_nyquist_is_reported_separately():
    x=np.repeat(np.arange(8)*2*np.pi/8,[3,1]*4);a,e,r,d=primary.field(x,8,2*np.pi);assert d['nyquist_charge']>.49;assert np.max(abs(e))<1e-15;assert d['resolved_gauss']<1e-15

def test_charge_neutrality():
    rng=np.random.default_rng(9);_,_,_,d=primary.field(rng.uniform(0,7,73),17,7);assert d['charge_error']<3e-15

def test_invalid_weight_rejected():
    with pytest.raises(ValueError):primary.field(np.arange(8.),8,8,np.zeros(8))

def test_invalid_fixed_step_rejected():
    with pytest.raises(ValueError):primary.advance(np.arange(8.),np.zeros(8),8,8,.03,.2)

def test_self_consistent_field_is_recomputed(monkeypatch):
    calls=[];original=primary.field
    def wrapped(*args,**kwargs):calls.append(np.copy(args[0]));return original(*args,**kwargs)
    monkeypatch.setattr(primary,'field',wrapped);n,l,x=fixture();out=primary.advance(x,np.zeros_like(x),n,l,.01,.04);assert len(calls)==5;assert np.max(abs(calls[-1]-calls[0]))>1e-6

def test_verlet_reversal():
    n,l,x=fixture();v=.1*np.cos(x);a=primary.advance(x,v,n,l,.01,.04);b=primary.advance(a['x_history'][-1],-a['v_history'][-1],n,l,.01,.04);np.testing.assert_allclose(b['x_history'][-1],x,atol=3e-15);np.testing.assert_allclose(b['v_history'][-1],-v,atol=3e-15)

def test_five_snapshots_and_finite_history():
    n,l,x=fixture();out=primary.advance(x,np.zeros_like(x),n,l,.01,.04);assert out['x_history'].shape==(5,len(x));assert np.isfinite(out['history']).all()

@pytest.mark.parametrize('drift',[0.,3.])
def test_gaussian_moments(drift):
    v,w=loading.velocities(128,drift);assert abs(np.sum(w*v))<1e-13;assert abs(np.sum(w*v*v)-1-drift*drift)<1e-12;assert np.all(w>0)

@pytest.mark.parametrize('drift',[0.,3.])
def test_joint_loading_is_not_marginals_only(drift):
    l=4*np.pi;x,v,w,z,q=loading.load(64,128,l,.01,drift,3);r=loading.qualification(x,v,w,z,q,l,.01,drift);assert r['joint_low_mode_factorization_defect']<5e-12;assert r['gaussian_characteristic_defect']<5e-8

def test_seed_reproducibility_and_conditional_shift():
    a=loading.load(64,128,12.,.01,0.,4);b=loading.load(64,128,12.,.01,0.,4);c=loading.load(64,128,12.,.01,0.,5);np.testing.assert_array_equal(a[0],b[0]);assert not np.array_equal(a[0],c[0]);np.testing.assert_array_equal(a[1],c[1]);np.testing.assert_array_equal(a[2],c[2])

def test_gaussian_tail_is_not_truncated_midquantiles():
    v,w=loading.velocities(128,0);assert v.max()>10;assert np.sum(w[abs(v)>2.8])>.004

def test_damped_estimator_known_wave():
    t=np.arange(0,16.001,.04);y=np.exp(-.15*t)*(.9*np.cos(1.4*t)+.2*np.sin(1.4*t));r=damped(t,y,[4,12],[-.16,1.41]);assert abs(r['gamma']+.15)<1e-9;assert abs(r['omega']-1.4)<1e-9

def test_growing_estimator_known_wave():
    t=np.arange(0,40.001,.05);r=growing(t,-2*np.exp(.2*t),[12,20]);assert abs(r['gamma']-.2)<1e-13

def test_growth_zero_crossing_not_silently_deleted():
    t=np.arange(0,21.);y=t-15
    with pytest.raises(ValueError):growing(t,y,[0,20])

def test_upper_half_plane_direct_velocity_integral():
    omega=.3+.4j;assert abs(dispersion(omega,.5,3)-upper_plane_integral(omega,.5,3,14))<2e-9

def test_volterra_initial_acceleration():
    t,y=volterra(.5,0,.02,.001);expected=-(1+.5**2);acceleration=(y[2]-2*y[1]+y[0])/.001**2;assert abs(acceleration-expected)<1e-4

def test_uniform_full_f_equilibrium():
    x,v,w,_,_=loading.load(64,32,4*np.pi,0,0,6);out=primary.advance(x,v,32,4*np.pi,.01,.04,w);assert np.max(abs(out['electric_history']))<2e-14

def test_dielectric_conjugate_parity_for_symmetric_equilibrium():
    omega=.8+.2j
    for drift in [0.,3.]:assert abs(dispersion(-omega.conjugate(),.5,drift)-dispersion(omega,.5,drift).conjugate())<2e-13


def test_completed_candidate_retained_before_estimator_failure(monkeypatch):
    import experiments
    candidate={'history':np.zeros((3,13))}
    monkeypatch.setattr(experiments.loading,'load',lambda *args:(np.arange(4.),np.zeros(4),np.ones(4),np.zeros(4),np.ones(4)))
    monkeypatch.setattr(experiments.loading,'qualification',lambda *args:{})
    monkeypatch.setattr(experiments.primary,'advance',lambda *args:candidate)
    retained=[]
    cfg={'k':.5,'spatial_strata':64,'drift':0,'final_time':16,'amplitude':.01,'fit_window':[4,12]}
    spec={'nodes':128,'amplitude':.01,'seed':3,'grid':32,'dt':.04,'family':'ensemble'}
    ref={'times':np.array([0.,16.]),'normalized_field':np.ones(2),'omega_real':1.4,'gamma':-.15}
    def failed(*args):raise ValueError('forced estimator failure')
    monkeypatch.setattr(experiments,'fit',failed)
    with pytest.raises(ValueError,match='forced estimator failure'):experiments.run_one('thermal-landau-damping',cfg,spec,ref,None,retained.append)
    assert len(retained)==1 and retained[0] is candidate


def test_periodic_rounding_of_tiny_negative_coordinate():
    length=2*np.pi;x=np.arange(8)*length/8;x[0]=-1e-20
    a,e,r,d=primary.field(x,8,length)
    np.testing.assert_allclose(r,0,atol=2e-15);np.testing.assert_allclose(a,0,atol=2e-15)


def test_runner_reads_actual_nested_acceptance_contract():
    from pathlib import Path
    import json
    from run import read_limits
    path=Path(__file__).parent/'acceptance.json';actual=json.loads(path.read_text());limits=read_limits(path)
    assert limits==actual['limits']
    assert all(key in limits for key in ['root_residual','energy','load_joint','rate_ivp_relative_error'])
    assert 'schema_version' not in limits


def test_full_driver_wiring_without_extra_physics(tmp_path,monkeypatch):
    import json,csv,sys
    import run as driver
    case='thermal-landau-damping';controls={'cases':{case:{}},'main_budget_seconds':115}
    source=tmp_path/'source';source.mkdir();inputs=source/'inputs.json';inputs.write_text(json.dumps(controls));(source/'acceptance.json').write_text(json.dumps({'schema_version':1,'limits':{}}));(source/'pre-run-contract.json').write_text(json.dumps({'files_sha256':{'inputs.json':driver.sha(inputs)}}))
    monkeypatch.setattr(driver,'ROOT',source)
    monkeypatch.setattr(driver,'qualify',lambda *args:({'passed':True,'omega_real':1.4,'gamma':-.15},{'times':np.array([0.,.04]),'normalized_field':np.ones(2)}))
    monkeypatch.setattr(driver,'specs',lambda *args:[{'id':'mock'}])
    row={'id':'mock','case':case,'family':'ensemble','seed':1,'grid':8,'nodes':16,'amplitude':.01,'dt':.01,'particles':16,'steps':4,'time':.04,'fit':{'gamma':-.15,'omega':1.4,'relative_fit_residual':0.},'maximum_charge_error':0.,'maximum_momentum_drift':0.,'maximum_resolved_gauss':0.,'maximum_energy_drift':0.}
    def candidate(*args,retain_completed):
        arrays={'history':np.zeros((5,13))};retain_completed(arrays);return dict(row),arrays,np.ones(5)
    monkeypatch.setattr(driver,'run_one',candidate);monkeypatch.setattr(driver,'decisions',lambda *args:([{'name':'mocked wiring only','passed':True}],{'wiring_only':True}))
    output=tmp_path/'output';monkeypatch.setattr(sys,'argv',['run.py','--input',str(inputs),'--output',str(output)])
    assert driver.main()==0
    result=json.loads((output/'result.json').read_text());assert result['checks']=={case:True};assert result['completed_run_count']==result['retained_complete_candidate_count']==1;assert result['failure'] is None
    assert json.loads((output/'completed-runs.json').read_text())[0]['case']==case
    assert (output/(case+'-mock.npz')).is_file()
    with (output/(case+'.csv')).open() as handle:rows=list(csv.reader(handle))
    assert len(rows)==2 and len(rows[0])==len(rows[1])


def test_declared_particle_space_probe_changes_only_spatial_strata():
    import json
    from pathlib import Path
    from experiments import specs
    cases=json.loads((Path(__file__).parent/'inputs.json').read_text())['cases']
    landau=specs('thermal-landau-damping',cases['thermal-landau-damping']);two=specs('thermal-two-stream',cases['thermal-two-stream'])
    assert len(landau)==10 and len(two)==9
    baseline=landau[0];probe=next(q for q in landau if q['family']=='spatial-strata')
    assert baseline['spatial_strata']==256 and probe['spatial_strata']==512
    assert all(probe[key]==baseline[key] for key in ['seed','grid','nodes','dt','amplitude'])
    assert all(q['spatial_strata']==64 for q in two)
