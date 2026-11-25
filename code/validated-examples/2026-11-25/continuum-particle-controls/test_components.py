"""Component qualification and deliberate wrong-formula controls."""
import numpy as np
import pytest
from ale_piston import mesh,geometry,face_flux
from gsph import scatter_pairs,assert_closed_energy,ContractFailure,linear_overlap,riemann_star,density_and_h
from sphere import lonlat_grid,rotate,bilinear_pole_periodic
from reference_riemann import RiemannSolution
from failure_support import NumericalFailure,persist_failure


def test_GCL_and_wrong_face_velocity_sign():
    points,cells,faces = mesh(4,2)
    _,a0,_,_,_ = geometry(points,cells,faces,0.)
    _,a1,_,_,_ = geometry(points,cells,faces,.1)
    _,_,normal,length,wn = geometry(points,cells,faces,.05)
    swept = np.zeros(len(cells))
    np.add.at(swept,faces[:,2],.1*length*wn)
    inside = faces[:,3] >= 0
    np.add.at(swept,faces[inside,3],-(.1*length*wn)[inside])
    # Independent endpoint polygon areas determine the expected volume change.
    assert np.max(np.abs(a1-a0-swept)) < 1e-12
    wrong_sign_residual = np.max(np.abs(a1-a0+swept))
    assert wrong_sign_residual > 1e-5


def test_moving_wall_mass_work_and_omitted_work_control():
    gamma,rho,pressure,wall_speed = 1.4,2.,3.,1.
    U = np.array([[rho,0.,0.,pressure/(gamma-1)]])
    faces = np.array([[0,1,0,-1]])
    normal,wn = np.array([[-1.,0.]]),np.array([-wall_speed])
    flux,_ = face_flux(U,faces,normal,wn,gamma)
    assert abs(flux[0,0]) < 1e-12
    # Impermeable moving-wall identity, independent of the integration ledger.
    expected_work = wall_speed*flux[0,1]
    assert abs(flux[0,3]-expected_work) < 1e-12
    assert abs(expected_work) > 1.
    # A zero-work ledger must reject the actual nonzero mechanical energy flux.
    omitted_wall_work_residual = .01*(flux[0,3]-0.)
    assert abs(omitted_wall_work_residual) > 1e-3


def test_pair_energy_sign_and_deliberate_wrong_sign():
    mass = np.array([.2,.3])
    i,j = np.array([0]),np.array([1])
    _,dE = scatter_pairs(i,j,np.array([.7]),np.array([.11]),mass)
    initial = np.array([3.,4.])
    assert abs(assert_closed_energy(mass,initial,initial+.01*dE)) < 1e-12
    wrong = dE.copy();wrong[1] *= -1
    with pytest.raises(ContractFailure,match='energy balance'):
        assert_closed_energy(mass,initial,initial+.01*wrong)


def test_rotation_velocity_convention_backward_inverse_and_wrong_direction():
    alpha,lon,lat = .7,.4,.3
    xyz = np.array([np.cos(lat)*np.cos(lon),np.cos(lat)*np.sin(lon),np.sin(lat)])
    axis = np.array([-np.sin(alpha),0.,np.cos(alpha)])
    velocity = np.cross(axis,xyz)
    east = np.array([-np.sin(lon),np.cos(lon),0.])
    north = np.array([-np.sin(lat)*np.cos(lon),-np.sin(lat)*np.sin(lon),np.cos(lat)])
    assert abs(velocity@east-(np.cos(lat)*np.cos(alpha)+np.sin(lat)*np.cos(lon)*np.sin(alpha))) < 1e-12
    assert abs(velocity@north+np.sin(lon)*np.sin(alpha)) < 1e-12
    forward = rotate(xyz,axis,.8)
    assert np.linalg.norm(rotate(forward,axis,-.8)-xyz) < 1e-12
    assert np.linalg.norm(rotate(forward,axis,.8)-xyz) > .1


def test_pole_ghost_requires_longitude_halfturn():
    _,_,xyz,_ = lonlat_grid(64,32)
    q = xyz[...,0]
    north = np.array([[0.,0.,1.]])
    assert abs(bilinear_pole_periodic(q,north)[0]) < 1e-12
    # Deliberately omitting the longitude half-turn copies a nonzero ring value.
    wrong_no_halfturn = .5*(q[-1,-1]+q[-1,0])
    assert abs(wrong_no_halfturn) > .01


def test_GSPH_overlap_against_independent_Gaussian_quadrature():
    Vi,Vj,distance,h = .7,1.3,.4,.2
    C,D = (Vi-Vj)/distance,.5*(Vi+Vj)
    nodes,weights = np.polynomial.hermite.hermgauss(12)
    direct=np.sum(weights*(C*h/np.sqrt(2)*nodes+D)**2)/np.sqrt(np.pi)
    assert abs(linear_overlap(Vi,Vj,distance,h)-direct) < 1e-12


def test_pair_Riemann_against_unchanged_independent_wave_oracle():
    oracle=RiemannSolution('euler',[1.,0.,1.],[.125,0.,.1],1.4)
    p,v,residual=riemann_star(np.array([1.]),np.array([0.]),np.array([1.]),np.array([.125]),np.array([0.]),np.array([.1]))
    assert abs(p[0]-oracle.star) < 1e-10
    assert abs(v[0]-oracle.velocity) < 1e-10
    assert residual < 1e-9


def test_h_fixedpoint_independent_residual_and_failure_preserves_state():
    x=(np.arange(32)+.5)/32
    mass=np.full(32,1/32)
    rho,h,diagnostics=density_and_h(x,mass,np.full(32,1.2/32),1.)
    d=x[:,None]-x[None,:];d-=np.floor(d+.5)
    # Re-evaluate the defining smooth-density relation, not its saved residual.
    smooth=np.sum(mass[None,:]*np.exp(-(d/(2*h[:,None]))**2)/(np.sqrt(np.pi)*2*h[:,None]),axis=1)
    assert np.max(np.abs(h*smooth/(1.2*mass)-1)) < 2e-10
    with pytest.raises(ContractFailure) as caught:
        density_and_h(x,mass,np.full(32,.3*1.2/32),1.,maxiter=1)
    assert caught.value.state_arrays and caught.value.diagnostics['iterations']==1


def test_analytic_zonal_force_gate_and_omitted_Coriolis_control():
    from sphere import analytic_zonal_force
    phi=np.linspace(-1.5,1.5,63)
    assert np.max(np.abs(analytic_zonal_force(phi)))<=1e-12
    omitted_coriolis_residual=analytic_zonal_force(phi)-2*2.*np.sin(phi)*.5*np.cos(phi)
    assert np.max(np.abs(omitted_coriolis_residual))>.1


def test_actual_GSPH_swapped_unequal_pair_force_and_energy_gates():
    from gsph import pair_swap_residual
    force_residual,energy_residual=pair_swap_residual()
    assert force_residual<=1e-12
    assert energy_residual<=1e-12


@pytest.mark.parametrize('failed_call,stage',[(2,'midpoint'),(3,'final')])
def test_exact_failed_particle_stage_and_true_step_start_are_owned(monkeypatch,failed_call,stage):
    import gsph
    calls=[]
    def forced_rhs(state,mass,h,length,gamma,mode):
        calls.append(state.copy())
        if len(calls)==failed_call:
            raise ContractFailure('forced stage failure',{'bad_residual':float('nan')})
        rhs=np.zeros_like(state);rhs[0]=.2;rhs[1]=.1;rhs[2]=.05
        return rhs,dict(rho=np.ones(2),pressure=np.ones(2),h=np.full(2,.1),h_relative_residual=0.,Riemann_residual=0.)
    monkeypatch.setattr(gsph,'particle_rhs',forced_rhs)
    initial=np.array([[.2,.7],[0.,0.],[3.,3.]])
    with pytest.raises(ContractFailure) as caught:
        gsph.evolve(initial,np.full(2,.5),np.full(2,.1),1.,.02)
    failure=caught.value
    assert failure.diagnostics['stage']==stage and failure.diagnostics['physical_time']>0
    assert np.array_equal(failure.state_arrays['step_start_state'],initial)
    assert np.array_equal(failure.state_arrays['failed_state'],calls[-1])
    assert not np.array_equal(failure.state_arrays['failed_state'],initial)


def test_nonfinite_failure_preserves_raw_NPZ_before_strict_JSON(tmp_path):
    import json
    failure=NumericalFailure('deliberate nonfinite failure',{'residual':float('nan'),'bound':float('inf')},{'failed_state':np.array([np.nan,np.inf,-np.inf])})
    payload=persist_failure(tmp_path,failure)
    with np.load(tmp_path/'failure-state.npz',allow_pickle=False) as raw:
        assert np.isnan(raw['failed_state'][0]) and np.isposinf(raw['failed_state'][1]) and np.isneginf(raw['failed_state'][2])
    loaded=json.loads((tmp_path/'failure.json').read_text(),parse_constant=lambda text:(_ for _ in ()).throw(ValueError(text)))
    assert loaded['diagnostics']=={'residual':'NONFINITE:NaN','bound':'NONFINITE:+Infinity'}
    assert payload['raw_state']['contains_original_nonfinite_values'] is True


def test_ALE_deadline_owns_current_mesh_and_extensive_state():
    from ale_piston import run_piston
    with pytest.raises(NumericalFailure) as caught:
        run_piston(4,2,deadline=-1.)
    failure=caught.value
    assert failure.diagnostics['stage']=='step-start' and failure.diagnostics['physical_time']==0.
    assert np.array_equal(failure.state_arrays['step_start_Q'],failure.state_arrays['failed_Q'])
    assert np.array_equal(failure.state_arrays['step_start_points'],failure.state_arrays['failed_points'])


def test_invalid_initial_SWE_state_owns_actual_arrays_without_sqrt_warning():
    from sphere import zonal_balance
    with pytest.raises(NumericalFailure) as caught:
        zonal_balance(16,h0=-1.)
    failure=caught.value
    assert failure.diagnostics['stage']=='initial-RHS' and failure.diagnostics['physical_time']==0.
    assert np.min(failure.state_arrays['failed_state'][0])<0
    assert np.array_equal(failure.state_arrays['step_start_state'],failure.state_arrays['failed_state'])


@pytest.mark.parametrize("width_scale", [1., 2.])
def test_Gaussian_density_contraction_matches_scalar_fsum_roundoff_bound(width_scale):
    import math
    from gsph import gaussian,periodic_delta
    # Same finite 32-particle fixture as the independent h-relation component.
    x=(np.arange(32)+.5)/32;mass=np.full(32,1/32)
    matrix=gaussian(periodic_delta(x,1.),np.full((32,1),width_scale*1.2/32))
    actual=np.einsum('ij,j->i',matrix,mass,optimize=False)
    oracle=np.array([math.fsum(float(a)*float(b) for a,b in zip(row,mass)) for row in matrix])
    absolute_product_sum=np.array([math.fsum(abs(float(a)*float(b)) for a,b in zip(row,mass)) for row in matrix])
    gamma=2*len(mass)*np.finfo(float).eps/(1-2*len(mass)*np.finfo(float).eps)
    assert np.isfinite(matrix).all() and np.isfinite(actual).all() and np.isfinite(oracle).all()
    assert np.all(np.abs(actual-oracle)<=gamma*absolute_product_sum)
