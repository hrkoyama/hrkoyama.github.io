"""Public regressions for the qualified general directional M1 flux."""
import numpy as np
import geometry,wavespeeds


def test_isotropic_directional_spectrum_and_cone_bound():
    for axis in [0,1]:
        q=wavespeeds.wave_data(np.array([1.,0.,0.]),axis)
        np.testing.assert_allclose(q['eigenvalues'],[-1/np.sqrt(3),0,1/np.sqrt(3)],rtol=0,atol=2e-15)
        assert abs(float(q['cone_bound'])-1/3)<2e-15


def test_actual_transverse_pure_beam_operator_has_no_artificial_diffusion():
    y=(np.arange(8)+.5)/8;E=np.broadcast_to(1+.1*np.cos(2*np.pi*y),(8,8)).copy();u=np.stack([E,E,np.zeros_like(E)],axis=-1)
    rhs,boundary=geometry.moment_rhs(u,1/8,np.zeros(8),True)
    assert np.max(abs(rhs))==0 and boundary==0


def test_general_directional_LF_splits_retain_the_physical_cone():
    for state in [[1.,.2,.3],[2.,-.8,.7],[.5,0.,0.],[1.,1.,0.]]:
        u=np.array(state);fx,fy=geometry.fluxes(u[None,:])
        for axis,flux in enumerate([fx[0],fy[0]]):
            a=float(wavespeeds.directional_speed(u,axis))
            if a==0:assert np.max(abs(flux))==0
            else:
                for sign in [-1,1]:
                    v=u+sign*flux/a;assert v[0]-np.sqrt(np.sum(v[1:]**2))>=-3e-12


def test_speed_extensions_are_counted_without_projecting_states():
    u=np.array([[0.,0.,0.],[-1e-14,0.,0.],[1.,1+1e-13,0.]]);old=u.copy();record=wavespeeds.diagnostics();q=wavespeeds.wave_data(u,0,record)
    np.testing.assert_array_equal(u,old);np.testing.assert_array_equal(q['speed'],np.ones(3))
    assert record['vacuum_states']==1 and record['tiny_negative_energy_states']==1 and record['outside_cone_roundoff_states']==1
    assert 0<record['maximum_outside_cone_excess']<=5e-12


def test_spectrum_matches_independent_complex_step_Jacobian():
    def flux(z,axis):
        E=z[0];f=z[1:]/E;s=np.sqrt(4-3*np.sum(f*f));P=E*((s-1)*np.eye(2)/3+3*np.outer(f,f)/(s+2))
        return np.r_[z[axis+1],P[:,axis]]
    for u in [np.array([1.,.2,.3]),np.array([2.,-.8,.7])]:
        for axis in [0,1]:
            columns=[]
            for j in range(3):
                z=u.astype(complex);z[j]+=1e-30j;columns.append(flux(z,axis).imag/1e-30)
            eigen=np.linalg.eigvals(np.stack(columns,axis=1));assert np.max(abs(eigen.imag))<2e-12
            np.testing.assert_allclose(np.sort(eigen.real),np.sort(wavespeeds.wave_data(u,axis)['eigenvalues']),rtol=0,atol=2e-11)
