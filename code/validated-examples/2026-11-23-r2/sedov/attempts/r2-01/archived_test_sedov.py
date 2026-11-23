"""Small independent identities and explicit failure-path checks."""
from pathlib import Path
import hashlib
import json
import warnings
from unittest.mock import patch
import numpy as np
import pytest
import sedov_solver as s
import reference_sedov as ref

ROOT=Path(__file__).resolve().parent

def test_spherical_volumes_and_areas():
    e,a,v=s.geometry(40,1.3)
    assert np.isclose(v.sum(),4*np.pi*1.3**3/3,rtol=2e-15)
    assert a[0]==0 and np.isclose(a[-1],4*np.pi*1.3**2)

def test_exact_partial_deposition_energy():
    e,a,v=s.geometry(73,1.)
    q=s.initial_state(e,.033,1.)
    assert np.isclose(np.dot(q[:,2],v),1.,rtol=2e-15)
    cut=np.flatnonzero((e[:-1]<.033)&(e[1:]>.033))[0]
    assert 0<q[cut,2]<q[0,2]

def test_initial_cold_background_is_zero_not_seeded():
    e,a,v=s.geometry(64,1.)
    q=s.initial_state(e,.03)
    rho,u,p,internal=s.primitive(q)
    assert np.all(rho==1) and np.all(u==0)
    assert np.all(p[e[:-1]>=.03]==0)

def test_uniform_pressure_geometric_equilibrium():
    e,a,v=s.geometry(64,1.)
    q=np.zeros((64,3));q[:,0]=1;q[:,2]=2.5/(s.GAMMA-1)
    rhs,b,source=s.rhs(q,a,v)
    np.testing.assert_allclose(rhs,0,atol=2e-10)
    assert source[1]>0 and b[1]<0
    assert abs(source[1]+b[1])<1e-12

def test_rusanov_identical_state_is_physical_flux():
    q=np.array([[1.,.3,2.],[2.,-.5,3.]])
    np.testing.assert_allclose(s.rusanov(q,q),s.physical_flux(q),rtol=1e-15)

def test_shared_rusanov_dissipation_is_antisymmetric():
    left=np.array([[1.,.2,2.]]);right=np.array([[.5,-.1,1.]])
    np.testing.assert_allclose(s.rusanov(left,right)+s.rusanov(right,left),s.physical_flux(left)+s.physical_flux(right),rtol=1e-15)

def test_nonpositive_density_fails():
    with pytest.raises(ValueError):s.primitive(np.array([[0.,0.,1.]]))

def test_negative_internal_energy_fails():
    with pytest.raises(ValueError):s.primitive(np.array([[1.,2.,1.]]))

def test_invalid_predictor_preserves_raw_state_no_retry():
    def bad(q,a,v):
        update=np.zeros_like(q);update[:,2]=-1e100
        return update,np.zeros(3),np.zeros(3)
    with patch.object(s,'rhs',side_effect=bad) as called:
        with pytest.raises(s.InvalidStage) as got:s.solve(32,1.,.001,.4,.06)
    assert called.call_count==1
    assert np.any(got.value.failed_state[:,2]<0)
    assert got.value.failed_context['stage']=='predictor'
    assert got.value.completed_history==[]

def test_small_run_mass_and_energy_budgets():
    out=s.solve(32,1.,.0001,.4,.06)
    residual=out['final_integral']-out['initial_integral']-out['boundary_net_integral']-out['geometric_source_integral']
    np.testing.assert_allclose(residual,0,atol=3e-14)
    assert out['time']==.0001 and out['state_floor_count']==0

def test_deposition_radius_does_not_change_total_energy():
    e,a,v=s.geometry(128,1.)
    for radius in [.015,.03,.047]:
        q=s.initial_state(e,radius)
        assert abs(np.dot(q[:,2],v)-1)<3e-15

def test_reference_strong_shock_jump():
    t=.05;rs=ref.shock_radius(t);speed=.4*rs/t
    rho,u,p=ref.point_state(np.array([rs]),t)
    np.testing.assert_allclose([rho[0],u[0]/speed,p[0]/speed**2],[4,.75,.75],rtol=2e-10)

def test_reference_upstream_cold_state():
    rho,u,p=ref.point_state(np.array([1.1*ref.shock_radius(.05),1.]),.05)
    np.testing.assert_array_equal(rho,[1.,1.]);np.testing.assert_array_equal(u,[0.,0.]);np.testing.assert_array_equal(p,[0.,0.])

def test_reference_similarity_radius_scaling():
    assert np.isclose(ref.shock_radius(.1)/ref.shock_radius(.05),2**.4,rtol=2e-15)

def test_reference_swept_mass_and_energy_normalization():
    data=ref.normalization()
    assert abs(data['swept_mass_dimensionless']-1/3)<2e-8
    assert abs(4*np.pi*.4**2*data['energy_integral']*data['beta']**5-1)<1e-13

def test_reference_core_cutoff_sensitivity():
    a=ref.normalization();b=ref.normalization(cutoff=.0005,rtol=2e-11)
    assert abs(a['beta']/b['beta']-1)<1e-8
    radii=np.array([.01,.1,.3])*ref.shock_radius(.05)
    for x,y in zip(ref.point_state(radii,.05),ref.point_state(radii,.05,cutoff=.0005,rtol=2e-11)):
        np.testing.assert_allclose(x,y,rtol=2e-4,atol=1e-11)

def test_reference_split_cell_integrals():
    edges=np.linspace(0,1,129)
    q,p=ref.cell_means(edges,.05,order=16);finer,fp=ref.cell_means(edges,.05,order=32)
    vol=4*np.pi*np.diff(edges**3)/3
    assert abs(np.dot(q[:,0],vol)/(4*np.pi/3)-1)<1e-7
    assert abs(np.dot(q[:,2],vol)-1)<1e-7
    np.testing.assert_allclose(q,finer,rtol=2e-5,atol=1e-11)
    assert np.all(p>=0)

def test_reference_is_independent_of_euler_solver():
    text=(ROOT/'reference_sedov.py').read_text()
    assert 'import sedov_solver' not in text and 'from sedov_solver' not in text
    assert 'solve_ivp' in text and 'DOP853' in text

def test_fixed_source_radius_refinements_and_separate_probe():
    cfg=json.loads((ROOT/'inputs.json').read_text())['cases']['sedov-blast']
    assert cfg['grids']==[128,256,512]
    assert cfg['deposit_radius']==.03 and cfg['sensitivity_deposit_radius']==.015
    assert cfg['p0']==0 and cfg['reference_order']!=cfg['reference_check_order']

def test_preregistered_numerical_sources_and_acceptance_unchanged():
    contract=json.loads((ROOT/'pre-run-contract.json').read_text())
    assert contract['declared_before_first_pde_run'] is True
    for name,digest in contract['files_sha256'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,name
    assert contract['target_edition']=='2026-11-23-r2'
    previous=json.loads((ROOT/'contract-r1.json').read_text())
    for name,digest in previous['files_sha256'].items():
        archived='archived_test_sedov.py' if name=='test_sedov.py' else name
        assert hashlib.sha256((ROOT/'attempts/r1-source'/archived).read_bytes()).hexdigest()==digest,name
    for name in ['inputs.json','acceptance.json','reference_sedov.py','exactpack-snapshot.json','exactpack-receipt.json']:
        assert contract['files_sha256'][name]==previous['files_sha256'][name],name

def test_pinned_exactpack_snapshot_provenance():
    receipt=json.loads((ROOT/'exactpack-receipt.json').read_text())
    snapshot=ROOT/'exactpack-snapshot.json'
    assert receipt['passed'] and receipt['reference_commit']=='9bacc477eb791e959c9621e771fc7a725db755fa'
    assert hashlib.sha256(snapshot.read_bytes()).hexdigest()==receipt['snapshot_sha256']
    assert hashlib.sha256((ROOT/'reference_sedov.py').read_bytes()).hexdigest()==receipt['local_reference_sha256']

def test_independently_executed_exactpack_points_and_shock():
    snapshot=json.loads((ROOT/'exactpack-snapshot.json').read_text())
    receipt=json.loads((ROOT/'exactpack-receipt.json').read_text())
    assert receipt['criteria']['exactpack_point_scaled_max']==5e-4
    assert abs(ref.shock_radius(snapshot['time'])/snapshot['shock_radius']-1)<=receipt['criteria']['exactpack_beta_relative']
    assert [row['npts'] for row in snapshot['point_cases']]==[6001,12001]
    for row in snapshot['point_cases']:
        local=ref.point_state(np.array(row['radius']),row['time'])
        for got,name in zip(local,['density','radial_velocity','pressure']):
            external=np.array(row[name])
            assert np.max(abs(got-external)/np.maximum(1,abs(external)))<=receipt['criteria']['exactpack_point_scaled_max']


def test_cfl_cold_subnormal_and_zero_speeds_raise_no_warning():
    # The old width/speed reduction overflowed at this unrestrictive tail cell.
    tiny=np.nextafter(0.,1.)
    width=np.full(4,.25)
    with warnings.catch_warnings():
        warnings.simplefilter('error')
        with np.errstate(over='raise',divide='raise',invalid='raise'):
            assert s.cfl_step(np.array([1.,tiny,0.,0.]),width,.4,1.)==.1
            assert s.cfl_step(np.zeros(4),width,.4,.05)==.05
            assert s.cfl_step(np.full(4,tiny),width,.4,.05)==.05
