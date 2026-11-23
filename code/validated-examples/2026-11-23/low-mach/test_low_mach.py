"""Algebraic, analytic, conservation, stage-failure and linear-stability checks."""
from functools import lru_cache
from pathlib import Path
from unittest.mock import patch
import hashlib,json
import numpy as np
import pytest
import lm_solver as s
from linear_stability import matrices,energy_transform,stability_scan
from references import analytic_vortex as exact
from references import miczek_matrix as oracle

ROOT=Path(__file__).resolve().parent


def test_primitive_conserved_roundtrip():
    w=np.array([[1.4,1.,-.2,2.],[.9,.4,.8,9000.]])
    np.testing.assert_allclose(s.primitive(s.conserved(w)),w,rtol=3e-15,atol=3e-12)


def test_invalid_physical_states_rejected():
    for q in [[0,0,0,1],[1,10,0,1],[1,0,0,np.inf]]:
        with pytest.raises(ValueError):s.primitive(np.array(q,float))


def test_equal_state_flux_x():
    q=s.conserved(np.array([1.2,.6,.4,2.]));np.testing.assert_allclose(s.numerical_flux(q,q,0),s.physical_flux(q,0),atol=2e-14)


def test_equal_state_flux_y():
    q=s.conserved(np.array([1.2,.6,.4,2.]));np.testing.assert_allclose(s.numerical_flux(q,q,1),s.physical_flux(q,1),atol=2e-14)


def test_roe_primitive_jump_maps_to_exact_conserved_jump():
    wl=np.array([1.3,.7,-.2,2.2]);wr=np.array([.7,-.15,.4,.9]);l,r=s.conserved(wl),s.conserved(wr)
    rho,u,v,c=s.roe_state(l,r)
    np.testing.assert_allclose(s.primitive_to_conserved_increment(wr-wl,rho,u,v),r-l,rtol=3e-15,atol=3e-15)


def test_roe_flux_difference_property_both_axes():
    l=s.conserved([1.3,.7,-.2,2.2]);r=s.conserved([.7,-.15,.4,.9]);rho,u,v,c=s.roe_state(l,r);w=np.array([rho,u,v,rho*c*c/s.GAMMA])
    for axis in (0,1):
        a,unused=oracle.conserved_matrices(w,axis,preconditioned=False)
        np.testing.assert_allclose(a@(r-l),s.physical_flux(r,axis)-s.physical_flux(l,axis),rtol=8e-14,atol=3e-14)


def test_coordinate_exchange_consistency():
    l=s.conserved([1.1,.8,.3,90.]);r=s.conserved([.9,.6,-.1,89.]);swap=[0,2,1,3]
    np.testing.assert_allclose(s.numerical_flux(l,r,0)[swap],s.numerical_flux(l[swap],r[swap],1),rtol=2e-14,atol=3e-13)


def compare_diffusion(mach,variant):
    w=np.array([1.2,.8,.4,1.2*np.hypot(.8,.4)**2/(s.GAMMA*mach*mach)])
    rho,u,v,p=w;c=np.sqrt(s.GAMMA*p/rho)
    for axis in (0,1):
        a,d=matrices(rho,u,v,c,axis,variant,mach)
        reference=oracle.primitive_diffusion_matrix(w,axis,mach,variant=='miczek')
        S=energy_transform(rho,c);np.testing.assert_allclose(S@d@np.linalg.inv(S),S@reference@np.linalg.inv(S),rtol=2e-11,atol=2e-10)


def test_standard_Roe_diffusion_matches_dense_oracle():compare_diffusion(.1,'roe')


def test_Miczek_diffusion_matches_dense_oracle_M01():compare_diffusion(.1,'miczek')


def test_Miczek_diffusion_matches_dense_oracle_M001():compare_diffusion(.01,'miczek')


def test_assembled_A_and_P_match_independent_matrix_source():
    rho,u,v,p=1.2,.8,.4,900.;c=np.sqrt(s.GAMMA*p/rho)
    for axis in (0,1):
        normal,tangent=(u,v) if axis==0 else (v,u);a,P=s.normal_matrices(rho,normal,tangent,c,'miczek',.01)
        ar,pr=oracle.primitive_matrices([rho,u,v,p],axis,.01);order=[0,1,2,3] if axis==0 else [0,2,1,3]
        np.testing.assert_allclose(a,ar[np.ix_(order,order)],atol=1e-13);np.testing.assert_allclose(P,pr[np.ix_(order,order)],rtol=3e-15)


def test_preconditioner_inverse_action():
    rho,u,v,c=1.2,.8,.4,100.;unused,P=s.normal_matrices(rho,u,v,c,'miczek',.01);delta=s.delta_parameter(rho,u,v,c,'miczek',.01)
    z=np.array([.2,-.1,.3,2.]);np.testing.assert_allclose(P@s.inverse_p_apply(z,rho,c,delta),z,rtol=5e-13,atol=2e-13)


def test_supersonic_switch_and_upwind_flux_both_signs():
    for speed in [-5.,5.]:
        l=s.conserved([1.2,speed,.2,1.]);r=s.conserved([1.1,speed+.1,.3,1.1])
        np.testing.assert_allclose(s.numerical_flux(l,r,0,'miczek',.01),s.physical_flux(l if speed>0 else r,0),rtol=3e-14,atol=3e-13)


def test_cutoff_uses_total_local_speed_and_declared_far_floor():
    assert s.delta_parameter(1.,0.,0.,100.,'miczek',.01)==99.
    assert s.delta_parameter(1.,100.,0.,100.,'miczek',.01)==0.
    assert s.delta_parameter(1.,0.,100.,100.,'miczek',.01)==0.
    with pytest.raises(ValueError):s.delta_parameter(1.,1.,0.,100.,'miczek',0.)


def test_uniform_periodic_field_is_preserved():
    q=np.broadcast_to(s.conserved([1.,1.,.5,100.]),(8,8,4)).copy()
    for variant in ['roe','miczek']:np.testing.assert_allclose(s.rhs(q,variant=variant),0,atol=2e-14)


def test_periodic_fluxes_telescope_all_four_components():
    x=(np.arange(8)+.5)*2*np.pi/8;xx,yy=np.meshgrid(x,x,indexing='ij');w=np.stack((1+.01*np.sin(xx),1+.02*np.cos(yy),.5+.01*np.cos(xx+yy),90+.03*np.sin(xx-yy)),axis=-1);q=s.conserved(w)
    for variant in ['roe','miczek']:np.testing.assert_allclose(s.rhs(q,variant=variant).sum(axis=(0,1)),0,atol=3e-12)


def test_SSPRK33_has_three_physical_rhs_stages():
    q=exact.cell_means(4,0,.1,8)
    with patch.object(s,'rhs',wraps=s.rhs) as calls:out=s.solve(q,1e-5)
    assert calls.call_count==3 and out['steps']==1 and out['time']==1e-5
    assert not np.array_equal(calls.call_args_list[0].args[0],calls.call_args_list[1].args[0])


def test_invalid_first_stage_is_retained_without_retry():
    q=np.broadcast_to(s.conserved([1.,1.,.5,90.]),(4,4,4)).copy()
    def bad(q,*args):a=np.zeros_like(q);a[...,0]=-1e100;return a
    with patch.object(s,'rhs',side_effect=bad) as calls:
        with pytest.raises(s.InvalidStage) as failure:s.solve(q,.001)
    assert calls.call_count==1 and failure.value.failed_context['stage']=='stage1'
    assert np.any(failure.value.failed_state[...,0]<0) and failure.value.completed_history==[]


def test_invalid_second_stage_is_retained_without_retry():
    q=np.broadcast_to(s.conserved([1.,1.,.5,90.]),(4,4,4)).copy();counter=[0]
    def bad(q,*args):
        counter[0]+=1;a=np.zeros_like(q)
        if counter[0]==2:a[...,0]=-1e100
        return a
    with patch.object(s,'rhs',side_effect=bad):
        with pytest.raises(s.InvalidStage) as failure:s.solve(q,.001)
    assert counter[0]==2 and failure.value.failed_context['stage']=='stage2'


def test_small_run_keeps_budget_and_zero_floor_retry_counts():
    q=exact.cell_means(4,0,.1,8);out=s.solve(q,.001)
    np.testing.assert_allclose(out['final_integral'],out['initial_integral'],rtol=3e-14,atol=3e-11)
    assert out['state_floor_count']==out['rejected_steps']==0 and out['minimum_density_all_stages']>0 and out['minimum_pressure_all_stages']>0


def test_step_budget_and_invalid_time_are_explicit():
    q=np.broadcast_to(s.conserved([1.,1.,.5,90.]),(4,4,4)).copy()
    with pytest.raises(ValueError,match='budget'):s.solve(q,1.,max_steps=1)
    with pytest.raises(ValueError):s.solve(q,-1.)


def test_initial_input_is_not_modified():
    q=exact.cell_means(4,0,.1,8);original=q.copy();s.solve(q,1e-5);np.testing.assert_array_equal(q,original)


def test_primary_inputs_and_numerical_sources_are_preregistered():
    c=json.loads((ROOT/'pre-run-contract.json').read_text());assert c['planned_tests']==35 and c['planned_numerical_gates']==143
    for name,digest in c['files_sha256'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,name


def test_analytic_field_satisfies_full_Euler_residual():
    x=np.array([-.9,-.3,.2,.8]);y=np.array([.2,-.7,.9,-.1])
    for mach in [.1,.01]:
        residual,scale=exact.analytic_euler_residual(x,y,.037,mach);assert np.max(abs(residual)/scale)<1e-11


def test_conserved_cell_quadrature_agrees_under_order_doubling():
    for mach in [.1,.01]:
        for time in [0.,.1]:
            a=exact.cell_means(16,time,mach,8);b=exact.cell_means(16,time,mach,16)
            assert np.max(abs(a-b)/np.array([1.,np.hypot(1,.5),np.hypot(1,.5),1.25]))<2e-7


def test_analytic_time_derivative_agrees_with_finite_difference():
    x=np.array([-.9,-.3,.2,.8]);y=np.array([.2,-.7,.9,-.1]);h=1e-4
    for mach in [.1,.01]:
        numerical=(exact.conserved(x,y,.037+h,mach)-exact.conserved(x,y,.037-h,mach))/(2*h)
        np.testing.assert_allclose(numerical,exact.conserved_time_derivative(x,y,.037,mach),rtol=1e-5,atol=3e-7)


def test_unscaled_temperature_family_recovers_original_KEEP_formula():
    x=np.array([-.9,-.3,.2,.8]);y=np.array([.2,-.7,.9,-.1]);mach=np.hypot(1,.5)/np.sqrt(1.4)
    radius=x*x+y*y;a=3/(2*np.pi)*np.exp(.5*(1-radius));T=1-.4*9/(8*1.4*np.pi**2)*np.exp(1-radius);rho=T**2.5
    np.testing.assert_allclose(exact.primitive(x,y,0,mach),np.stack((rho,1-a*y,.5+a*x,rho**1.4),axis=-1),rtol=3e-15,atol=3e-15)


def test_background_Mach_and_entropy_ratio_are_distinct_from_local_Mach():
    for mach in [.1,.01]:
        w=exact.primitive(np.array([0.,1.]),np.array([0.,0.]),0,mach);rho,u,v,p=np.moveaxis(w,-1,0)
        np.testing.assert_allclose(p/rho**1.4,exact.background_pressure(mach),rtol=3e-15)
        assert np.max(np.hypot(u,v)/np.sqrt(1.4*p/rho))>mach


def test_energy_scaled_physical_jacobians_are_symmetric():
    rho,u,v,c=1.2,1.,.5,100.;S=energy_transform(rho,c)
    for axis in (0,1):
        a,unused=matrices(rho,u,v,c,axis,'roe',.01);scaled=S@a@np.linalg.inv(S)
        np.testing.assert_allclose(scaled,scaled.T,atol=3e-12)


@lru_cache(None)
def scan():return stability_scan()


def test_sampled_SSPRK3_amplification_is_stable():
    result=scan();assert len(result)==4
    assert all(r['sampled_2d_modes']==17**2 and r['maximum_SSPRK3_spectral_radius']<=1.00000000005 for r in result)


def test_sampled_forward_Euler_counterexample_is_exhibited():
    r=next(r for r in scan() if r['mach_far']==.01 and r['variant']=='miczek')
    assert r['maximum_forward_Euler_spectral_radius']>1.00001


def test_energy_scaled_nonnormal_powers_are_bounded_on_selected_modes():
    assert all(r['power_indices']==[1,10,100] and r['maximum_energy_scaled_power_norm']<=4 for r in scan())


def test_unlimited_primitive_reconstruction_reproduces_affine_interior():
    i,j=np.meshgrid(np.arange(8),np.arange(8),indexing='ij')
    slope=np.array([.002,.003,-.001,.004]);w=np.array([1.,1.,.5,90.])+i[...,None]*slope+j[...,None]*slope/2
    q=s.conserved(w)
    for axis,factor in [(0,1.),(1,.5)]:
        l,r=s.reconstructed_faces(q,axis);expected=w+.5*factor*slope
        np.testing.assert_allclose(s.primitive(l)[2:-2,2:-2],expected[2:-2,2:-2],rtol=5e-15,atol=3e-13)
        np.testing.assert_allclose(s.primitive(r)[2:-2,2:-2],expected[2:-2,2:-2],rtol=5e-15,atol=3e-13)


def test_unlimited_reconstruction_rejects_and_retains_invalid_faces():
    w=np.broadcast_to([1.,1.,.5,90.],(8,8,4)).copy();w[1,:,0]=.1;w[2,:,0]=10.;q=s.conserved(w);original=q.copy()
    with pytest.raises(s.InvalidStage) as failure:s.solve(q,.001)
    np.testing.assert_array_equal(q,original);np.testing.assert_array_equal(failure.value.failed_state,original)
    assert failure.value.failed_context['stage']=='reconstruction' and failure.value.failed_context['rk_stage']=='rhs-stage1'
    assert failure.value.completed_history==[] and any(np.any(f[...,0]<=0) for f in failure.value.failed_faces.values())


def test_MUSCL_rhs_linearizes_to_independent_full_matrix_Fourier_symbol():
    n=8;i,j=np.meshgrid(np.arange(n),np.arange(n),indexing='ij');kx,ky=np.pi/2,np.pi/4;phase=kx*i+ky*j;eps=1e-5
    for mach in [.1,.01]:
        w=np.array([1.,1.,.5,1.25/(1.4*mach*mach)]);q0=np.broadcast_to(s.conserved(w),(n,n,4)).copy()
        direction=oracle.primitive_to_conserved_jacobian(w)@np.array([.1,.3,-.2,.4]);S=oracle.energy_scaling(w)
        for variant in ['roe','miczek']:
            ax,dx=oracle.conserved_matrices(w,0,mach,variant=='miczek');ay,dy=oracle.conserved_matrices(w,1,mach,variant=='miczek')
            L=-1j*(np.sin(kx)*(1.5-.5*np.cos(kx))*ax+np.sin(ky)*(1.5-.5*np.cos(ky))*ay)-.5*((1-np.cos(kx))**2*dx+(1-np.cos(ky))**2*dy)
            parts=[]
            for shape in [np.cos(phase),np.sin(phase)]:
                perturb=eps*shape[...,None]*direction
                parts.append((s.rhs(q0+perturb,n,variant,mach)-s.rhs(q0-perturb,n,variant,mach))/(2*eps))
            actual=parts[0]+1j*parts[1];expected=np.exp(1j*phase)[...,None]*(L@direction)
            scaled_error=(actual-expected)@S.T;scaled_expected=expected@S.T
            assert np.max(abs(scaled_error))<=2e-5*(1+np.max(abs(scaled_expected)))
