import json
import numpy as np
import pytest
import geometry,mms,io_contract
from references.analytic import mms_forcing_complex_step


def test_exact_vacuum_pressure_branch():assert not np.any(geometry.pressure(np.zeros((1,3))))


def test_nonzero_isotropic_energy_retains_outofplane_pressure():
    np.testing.assert_allclose(geometry.pressure(np.array([[1.,0.,0.]])),[[1/3,0.,1/3,1/3]],atol=2e-15)


def test_pure_beam_tensor_limit():
    np.testing.assert_allclose(geometry.pressure(np.array([[1.,1.,0.]])),[[1.,0.,0.,0.]],atol=2e-15)


def test_realizability_guard_including_tiny_negative_energy():
    for state in [[1,1.1,0],[0,.1,0],[-1,0,0],[-1e-14,1,0]]:
        with pytest.raises(ArithmeticError):geometry.pressure(np.array([state],float))


def test_pressure_full3Dtrace_not_only2Dblock():
    u=np.array([[1.,.2,.1],[2.,.3,-.5]]);p=geometry.pressure(u)
    np.testing.assert_allclose(p[:,0]+p[:,2]+p[:,3],u[:,0],atol=2e-15)
    assert np.all(p[:,0]+p[:,2]<u[:,0])


def test_spherical_sixaxis_isotropic_second_moments():
    i=np.ones((2,2,6));u=geometry.moments(i);p=geometry.angular_pressure(i)
    np.testing.assert_allclose(u,np.broadcast_to([1.,0.,0.],u.shape),atol=2e-15)
    np.testing.assert_allclose(p,np.broadcast_to([1/3,0.,1/3,1/3],p.shape),atol=2e-15)


def test_unit_beam_nodal_intensity_includes_quadrature_weight():
    i=np.zeros((2,2,6));i[...,0]=6;u=geometry.moments(i)
    np.testing.assert_allclose(u,np.broadcast_to([1.,1.,0.],u.shape),atol=2e-15)


def test_mms_analytic_forcing_uses_closed_nonlinear_M1tensor():
    x=np.array([.13,.47,.81]);y=np.array([.21,.59,.73]);_,s=mms.state_and_forcing(x,y,.117)
    np.testing.assert_allclose(s,mms_forcing_complex_step(x,y,.117),rtol=0,atol=2e-12)


def test_mms_reduced_flux_magnitude_and_direction_vary():
    u,_=mms.state_and_forcing(np.array([.1,.4,.8]),np.array([.2,.6,.9]),.1);g=u[:,1:]/u[:,0,None]
    assert np.ptp(g[:,0])>.01 and np.ptp(g[:,1])>.01 and np.min(u[:,0])>.8


def test_uniform_periodic_moment_state_has_zero_spatial_rhs():
    u=np.broadcast_to([1.,.2,.1],(8,8,3)).copy();r,f=geometry.moment_rhs(u,1/8,np.zeros(8),True)
    assert np.max(abs(r))==0. and f==0.


def test_periodic_angular_xy_conservative_operator():
    i=np.arange(8*8*6,dtype=float).reshape(8,8,6)/100+1;r,f=geometry.angular_rhs(i,1/8,np.zeros(8),True)
    assert abs(np.sum(r))<1e-12 and f==0.


def test_moment_boundary_energy_flux_matches_global_rhs():
    e=np.arange(64).reshape(8,8)/100+1;u=np.stack([e,e,np.zeros_like(e)],axis=-1)
    r,f=geometry.moment_rhs(u,1/8,np.ones(8),False)
    assert abs(np.sum(r[...,0])/64+f)<1e-13


def test_angular_boundary_flux_matches_global_rhs():
    i=np.arange(8*8*6,dtype=float).reshape(8,8,6)/100+1;r,f=geometry.angular_rhs(i,1/8,np.ones(8),False)
    assert abs(np.sum(r)/6/64+f)<1e-13


def test_crossed_initial_condition_excites_actual_y_operator():
    i=geometry.cell_initial(8,'crossed');u=geometry.moments(i)
    assert u[...,1].max()>0 and u[...,2].max()>0
    r,_=geometry.angular_rhs(i,1/8,np.zeros(8),True);assert abs(r[...,0]).max()>0 and abs(r[...,2]).max()>0


def test_invalid_fixed_steps_rejected_without_evolution():
    with pytest.raises(ValueError):geometry.solve({'cells':8,'kind':'mms','method':'m1','steps':3,'final_time':.1})


def test_actual_frozen_source_and_reference_contract():
    c=io_contract.verify(io_contract.ROOT/'inputs.json');assert c['planned_primary_runs']==24


def test_completed_2Dcandidate_survives_later_missing_reference(tmp_path,monkeypatch):
    import run as driver
    candidate=dict(states=np.zeros((1,1,1,3)),moments=np.zeros((1,1,1,3)),times=np.zeros(1),history=np.zeros((1,8)))
    monkeypatch.setattr(driver.geometry,'solve',lambda *args:candidate)
    spec=dict(id='retention-fixture',kind='intentionally-missing-reference',cells=1)
    with pytest.raises(FileNotFoundError):driver.one(spec,{}, {},tmp_path,[],[])
    with np.load(tmp_path/'retention-fixture.npz',allow_pickle=False) as f:
        np.testing.assert_array_equal(f['states'],candidate['states'])
    assert (tmp_path/'retention-fixture-history.csv').is_file()
