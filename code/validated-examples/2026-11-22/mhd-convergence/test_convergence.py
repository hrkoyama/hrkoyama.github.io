"""Independent equations, operators, integrators and bounded-failure tests."""
from copy import deepcopy
import hashlib
import json
import shutil
from pathlib import Path
import numpy as np
import pytest
from numpy.polynomial.legendre import leggauss
from experiments import FIELD_NAMES,constraint_control,longitudinal_reference,load_reference,norms,order,restrict,scales,temporal_reference
from run import run,validate
from solver import (Budget,common_divergence,divergence,exact_smooth,flux,
                    initial_ot,initial_q,pack,primitive,rhs,solve,unpack)

HERE=Path(__file__).resolve().parent


@pytest.fixture(scope='module')
def config():return json.loads((HERE/'inputs.json').read_text())


def test_predeclared_inputs_unchanged(config):
    assert hashlib.sha256((HERE/'inputs.json').read_bytes()).hexdigest()=='ef1066846f52a270af0ee89282843ef6ea39279bedac758a1e13a0970c639734'
    assert hashlib.sha256((HERE/'inputs-initial.json').read_bytes()).hexdigest()=='274e3e30d1abfb15efaef12e1e53cdd8176d3bc7229a3a89bcd5fa9e3b67d67d'
    original=json.loads((HERE/'inputs-initial.json').read_text())
    for key in ('smooth','ot','model','time_reference'):assert config[key]==original[key]
    history=json.loads((HERE/'protocol-history.json').read_text());assert history['numerical_pilot_before_revision'] is False and history['physical_case_inputs_and_acceptance_changed'] is False
    validate(config)


def quadrature_cell(n,i,j,t,cfg):
    z,w=leggauss(12);x=(i+.5+.5*z[:,None])/n;y=(j+.5+.5*z[None,:])/n
    k=2*np.pi;u,v=cfg['velocity'];a=cfg['amplitude'];rho=cfg['density']
    phase_x=k*(x-u*t);phase_y=k*(y-v*t)
    potential=a*(np.cos(phase_x)+np.cos(phase_y))
    bx=-a*k*np.sin(phase_y);by=a*k*np.sin(phase_x)
    p=cfg['base_pressure']+.5*k*k*potential*potential
    q=np.zeros((12,12,6));q[...,0]=rho;q[...,1]=rho*u;q[...,2]=rho*v
    q[...,3]=p/(5/3-1)+.5*rho*(u*u+v*v)+.5*(bx*bx+by*by)
    q[...,4]=bx;q[...,5]=by
    return np.einsum('i,j,ijv->v',w,w,q)/4


@pytest.mark.parametrize('n,t,i,j',[(8,0.,0,3),(16,.1,5,8),(32,.037,9,17)])
def test_exact_conserved_cell_averages_match_independent_gaussian_quadrature(config,n,t,i,j):
    expected=quadrature_cell(n,i,j,t,config['smooth'])
    np.testing.assert_allclose(exact_smooth(n,t,config['smooth'])[i,j,:6],expected,atol=5e-16,rtol=3e-15)


def test_pressure_recovered_from_conserved_average_is_not_claimed_to_be_primitive_average(config):
    n=8;q=exact_smooth(n,0.,config['smooth']);p=primitive(q)[3]
    z=(np.arange(n)+.5)/n;k=2*np.pi;a=config['smooth']['amplitude'];s=np.sinc(1/n);s2=np.sinc(2/n)
    cx=np.cos(k*z[:,None]);cy=np.cos(k*z[None,:])
    avg_a2=a*a*(1+.5*s2*(np.cos(2*k*z[:,None])+np.cos(2*k*z[None,:]))+2*s*s*cx*cy)
    exact_pbar=config['smooth']['base_pressure']+.5*k*k*avg_a2
    assert np.max(p-exact_pbar)>1e-3 and np.min(p-exact_pbar)>0


@pytest.mark.parametrize('n',[8,16,32])
@pytest.mark.parametrize('case',['smooth','ot'])
def test_ct_and_glm_initial_cell_states_match_while_faces_preserve_native_constraint(config,n,case):
    q=initial_q(case,n,config[case]);ct=pack(q,'ct');glm=pack(q,'glm')
    np.testing.assert_array_equal(unpack(ct,'ct'),unpack(glm,'glm'))
    assert np.max(abs(divergence(ct,'ct')))<1e-14
    assert np.max(abs(divergence(glm,'glm')))<1e-14


@pytest.mark.parametrize('method',['ct','glm'])
def test_constant_full_mhd_state_has_zero_rhs(config,method):
    q=np.zeros((8,8,7));q[...,0]=1.;q[...,1]=.2;q[...,2]=-.1;q[...,3]=1.;q[...,4]=.3;q[...,5]=-.2
    assert np.max(abs(rhs(pack(q,method),method,config['model'])))==0


def test_discrete_ct_divergence_of_update_vanishes_without_projection(config):
    rng=np.random.default_rng(93);state=np.zeros((8,8,6));state[...,0]=1.;state[...,3]=2.
    state[...,4:6]=rng.normal(0,.1,(8,8,2))
    r=rhs(state,'ct',config['model']);before=divergence(state,'ct')
    update_div=8*(r[...,4]-np.roll(r[...,4],1,0)+r[...,5]-np.roll(r[...,5],1,1))
    assert np.max(abs(update_div))<8e-14
    np.testing.assert_allclose(divergence(state+.001*r,'ct'),before,atol=1e-14)
    # No concealed cell-field projection: cells are explicit face averages.
    q=unpack(state+.001*r,'ct')
    np.testing.assert_array_equal(q[...,4],.5*(state[...,4]+.001*r[...,4]+np.roll(state[...,4]+.001*r[...,4],1,0)))


@pytest.mark.parametrize('method',['ct','glm'])
def test_shared_flux_conserves_mass_energy_but_damps_only_psi_mean(config,method):
    state=pack(initial_q('smooth',8,config['smooth']),method)
    if method=='glm':state[...,6]=.003
    r=rhs(state,method,config['model'])
    assert np.max(abs(np.mean(r[...,:4],axis=(0,1))))<3e-16
    if method=='glm':assert np.mean(r[...,6])==pytest.approx(-config['model']['cleaning_rate']*.003,abs=2e-16)


def test_glm_longitudinal_rhs_matches_independent_discrete_fourier_symbol(config):
    n=16;x=2*np.pi*(np.arange(n)+.5)/n
    q=np.zeros((n,n,7));q[...,0]=1.;q[...,4]=.01*np.cos(x[:,None]);q[...,6]=.003*np.sin(x[:,None])
    q[...,3]=1.+.5*q[...,4]**2
    actual=rhs(q,'glm',config['model']);alpha=config['model']['wave_speed_bound'];kappa=config['model']['cleaning_rate']
    derivative=n*np.sin(2*np.pi/n);diffusion=alpha*n*(np.cos(2*np.pi/n)-1)
    expected_b=-.003*derivative*np.cos(x[:,None])+diffusion*q[...,4]
    expected_psi=alpha*alpha*.01*derivative*np.sin(x[:,None])+(diffusion-kappa)*q[...,6]
    np.testing.assert_allclose(actual[...,4],np.broadcast_to(expected_b,(n,n)),atol=2e-16)
    np.testing.assert_allclose(actual[...,6],np.broadcast_to(expected_psi,(n,n)),atol=3e-16)


def test_native_face_and_common_cell_divergence_operators_are_distinct(config):
    state=pack(initial_q('smooth',8,config['smooth']),'ct');state[3,4,4]+=.001
    native=divergence(state,'ct');common=common_divergence(unpack(state,'ct'))
    assert np.max(abs(native-common))>.001


def test_conservative_reference_restriction_preserves_mean_and_orientation():
    fine=8;x=np.tile(np.arange(fine),fine);y=np.repeat(np.arange(fine),fine)
    table=np.zeros((fine*fine,12));table[:,4]=100*x+y;table[:,9]=x;table[:,10]=y
    a=restrict(table,4)
    np.testing.assert_allclose(a[...,0],100*(2*np.arange(4)[:,None]+.5)+2*np.arange(4)[None,:]+.5)
    assert np.mean(a[...,0])==np.mean(table[:,4])
    with pytest.raises(ValueError):restrict(table,3)


@pytest.mark.parametrize('fault',['unexecuted','execution_boolean','missing_file','empty_datasets','missing_dataset','wrong_grid','wrong_cfl','wrong_time','wrong_input'])
def test_reference_completeness_provenance_and_hashes(tmp_path,monkeypatch,fault):
    import experiments
    refs=tmp_path/'references';shutil.copytree(HERE/'references',refs)
    path=refs/'reference-manifest.json';manifest=json.loads(path.read_text())
    if fault=='unexecuted':manifest['actually_executed']=False
    if fault=='execution_boolean':manifest['actually_executed']=1
    if fault=='missing_file':del manifest['files']['ATHENA-LICENSE.txt']
    if fault=='empty_datasets':manifest['datasets']={}
    if fault=='missing_dataset':del manifest['datasets']['512-cfl03']
    if fault=='wrong_grid':manifest['datasets']['128']['n']=512
    if fault=='wrong_cfl':manifest['datasets']['512']['cfl']=.3
    if fault=='wrong_time':manifest['datasets']['512']['time']=.1
    if fault=='wrong_input':manifest['datasets']['512']['input']='athinput-ot-512-cfl03'
    path.write_text(json.dumps(manifest));monkeypatch.setattr(experiments,'HERE',tmp_path)
    with pytest.raises(ValueError,match='manifest SHA'):load_reference()
    # Exercise semantic guards independently of the outer frozen digest.
    monkeypatch.setattr(experiments,'REFERENCE_MANIFEST_SHA256',hashlib.sha256(path.read_bytes()).hexdigest())
    with pytest.raises(ValueError):load_reference()


def test_reference_data_tampering_fails_before_loading(tmp_path,monkeypatch):
    import experiments
    refs=tmp_path/'references';shutil.copytree(HERE/'references',refs)
    (refs/'athena-ot-512-cfl015.npz').write_bytes(b'changed')
    monkeypatch.setattr(experiments,'HERE',tmp_path)
    with pytest.raises(ValueError,match='file SHA'):load_reference()


def test_actual_independent_reference_files_are_bound_and_resolved():
    arrays,manifest=load_reference()
    assert set(arrays)=={'128','256','512','512-cfl03'}
    assert all(np.all(np.isfinite(a)) for a in arrays.values())


@pytest.mark.parametrize('change',[('model','wave_speed_bound',float('nan')),('model','cleaning_rate',-1),('model','maximum_seconds',10000),('model','cfl_sum_maximum',.8),('smooth','spatial_steps',True),('ot','time',.1),('smooth','grids',[16,32,100000]),('ot','reference_grids',[256,512])])
def test_bad_configs_fail_before_allocation(config,change):
    modified=deepcopy(config);section,key,value=change;modified[section][key]=value
    with pytest.raises(ValueError):validate(modified)


def test_fixed_step_cfl_guard_is_active(config):
    with pytest.raises(ValueError,match='CFL'):solve('smooth',64,1,'glm',config['smooth'],config['model'])


def test_positivity_and_common_wave_bound_fail_loudly(config):
    q=initial_q('smooth',8,config['smooth']);q[...,3]=-1
    with pytest.raises(ValueError,match='pressure'):primitive(q)
    q=initial_q('smooth',8,config['smooth']);q[...,1]=100.
    with pytest.raises(ValueError):flux(q,0,3.,3.,5/3)


def test_order_requires_resolved_nonzero_errors():
    assert order([.04,.02,.01])==[1.,1.]
    with pytest.raises(ValueError):order([0.,0.])


def test_deadline_and_output_overwrite_guards(config,tmp_path):
    budget=Budget();budget.deadline=0.
    with pytest.raises(RuntimeError,match='budget exhausted'):rhs(pack(initial_q('smooth',8,config['smooth']),'ct'),'ct',config['model'],budget)
    (tmp_path/'keep.txt').write_text('keep')
    with pytest.raises(ValueError,match='new or empty'):run(HERE/'inputs.json',tmp_path)
    assert (tmp_path/'keep.txt').read_text()=='keep'


def test_schema_boolean_is_not_an_integer_version(config):
    modified=deepcopy(config);modified['schema_version']=True
    with pytest.raises(ValueError,match='schema'):validate(modified)


def test_independent_literal_fourier_recurrence_matches_matrix_power(config):
    c=config['constraint_control'];n=c['n'];count=c['steps'];alpha=config['model']['wave_speed_bound'];kappa=config['model']['cleaning_rate'];dt=c['time']/count
    theta=2*np.pi/n;nu=alpha*n*(np.cos(theta)-1);kd=n*np.sin(theta)
    b=complex(c['amplitude']*np.cos(np.pi/n));psi=0j
    for _ in range(count):b,psi=b+dt*(nu*b-1j*kd*psi),psi+dt*(-1j*alpha*alpha*kd*b+(nu-kappa)*psi)
    actual=longitudinal_reference(n,count,c['time'],c['amplitude'],alpha,kappa)[0]
    np.testing.assert_allclose(actual,[b,psi],atol=3e-17)


def test_full_mhd_constraint_control_activates_psi_and_separates_physical_damping(config):
    case,_=constraint_control(config,Budget(20.))
    assert case['passed'] and case['checks']['ct_initial_constraint_is_deliberately_nonzero']
    assert case['metrics']['damped_to_undamped_B_psi_wave_energy_ratio']==pytest.approx(.7977071754336023,abs=3e-14)
    rows=[r for r in case['records'] if r['method']=='glm']
    assert all(r['maximum_psi_linf']>.01 and r['fourier_FE_reference_linf']<2e-15 for r in rows)


def test_bilingual_metadata_and_unimplemented_methods_are_not_borrowed():
    cases=json.loads((HERE/'cases.json').read_text());assert len(cases)==3
    for case in cases:
        assert case['method_ids']==['ct','glm']
        for key in ('title','summary','assumptions','algorithm','validation','limits'):assert set(case[key])=={'ja','en'} and all(case[key].values())
        assert case['references'] and case['equations']
        assert all((HERE/name).is_file() for name in case['code_files'])
