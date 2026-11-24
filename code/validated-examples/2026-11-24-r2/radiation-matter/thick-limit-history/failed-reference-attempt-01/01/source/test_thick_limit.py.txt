"""Small controls for the actual stencil; run only after reference qualification."""
import numpy as np
import pytest
import transport,thick_limit
from references.thick_reference import continuum_matrix,discrete_upwind_matrix,diffusion_amplitudes


def test_physical_opacity_scales_both_exchange_rows_and_capacity():
    mu,w=transport.angles(8);I=np.full((8,8),1.2);V=np.full(8,.3)
    a,b=thick_limit.physical_rhs(I,V,mu,w,.25,4.,.25)
    np.testing.assert_allclose(a,4*(.3-1.2)/.25,rtol=0,atol=2e-14)
    np.testing.assert_allclose(b,4*(1.2-.3),rtol=0,atol=2e-14)
    np.testing.assert_allclose(.25*.5*np.sum(w[:,None]*a,axis=0)+b,0.,rtol=0,atol=2e-14)


def test_actual_cosine_sine_probes_match_independent_upwind_symbol():
    mu,w=transport.angles(8)
    for eps in [.25,2.]:
        actual=thick_limit.matrix_from_real_probes(mu,w,.17,4.,eps)
        expected=discrete_upwind_matrix(mu,w,4.,.17,eps)
        np.testing.assert_allclose(actual,expected,rtol=0,atol=3e-13)
        k0=continuum_matrix(mu,w,4.,eps,wavenumber=0.)
        np.testing.assert_allclose(np.einsum('ij,j->i',k0,np.ones(9),optimize=False),0.,rtol=0,atol=2e-14)


def test_cellmean_initial_condition_and_fick_sign_are_distinct_from_initial_flux():
    n=16;h=2*np.pi/n;x=(np.arange(n)+.5)*h;amp=.1*np.sinc(h/(2*np.pi))
    means=1+.1*(np.sin(x+h/2)-np.sin(x-h/2))/h
    np.testing.assert_allclose(thick_limit.reconstruct(np.array(amp+0j),x),means,rtol=0,atol=4e-16)
    expected=diffusion_amplitudes(amp,0.,4.,1.)
    assert expected[2].real==0 and expected[2].imag==pytest.approx(-amp/12)
    assert abs(expected[2])*4/amp==pytest.approx(1/3)
    wrong=diffusion_amplitudes(amp,.25,4.,1.,factor=1.)
    assert abs(wrong[0])<abs(diffusion_amplitudes(amp,.25,4.,1.)[0])


def test_reconstructed_actual_full_grid_rhs_and_periodic_budget(tmp_path):
    out=thick_limit.single_mode(4,16,[0.,.0625],number=8,partial=tmp_path/'candidate.npz')
    assert out['intensity'].shape==(2,8,16) and out['material'].shape==(2,16)
    assert float(out['semidiscrete_residual'])<2e-12 and float(out['actual_rhs_budget'])<2e-12
    np.testing.assert_allclose(out['flux'][0],0.,rtol=0,atol=2e-15)
    h=2*np.pi/16;energy=h*np.sum(out['energy']+out['material'],axis=1)
    np.testing.assert_allclose(energy,4*np.pi,rtol=0,atol=2e-12)
    assert (tmp_path/'candidate.npz').exists() and out['intensity'].min()>0
