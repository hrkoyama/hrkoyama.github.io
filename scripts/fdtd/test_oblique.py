"""Independent Maxwell/jump/energy checks for oblique dielectric scattering."""
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import numpy as np
import pytest
import oblique as o
from run_oblique import validate


HERE=Path(__file__).resolve().parent
def inputs():return json.loads((HERE/'inputs/dielectric-oblique.json').read_text())


@pytest.mark.parametrize('ky',[0.,2.,4.])
def test_fresnel_matches_both_interface_conditions_and_normal_power(ky):
    k=np.array([.13,1.,3.7,6.2,11.]);z=o.fresnel(k,ky,1.3,3.9)
    np.testing.assert_allclose(z['q']**2+ky**2,3.9*z['omega']**2,rtol=2e-15)
    np.testing.assert_allclose(1+z['r'],z['t'],rtol=2e-15)
    np.testing.assert_allclose(k*(1-z['r']),z['q']*z['t'],rtol=2e-15)
    np.testing.assert_allclose(z['R']+z['T'],1.,rtol=0,atol=4e-16)
    np.testing.assert_allclose(3.9/(1.3*z['qprime'])*z['t']**2,z['T'],rtol=3e-15)
    # Snell uses the carrier wave-vector directions, not packet envelope speed.
    np.testing.assert_allclose(np.sqrt(1.3)*ky/np.hypot(k,ky),np.sqrt(3.9)*ky/np.hypot(z['q'],ky),atol=3e-16)


def test_normal_incidence_reduces_to_signed_fresnel_constants():
    z=o.fresnel(np.array([.2,3.,17.]),0.,1.,4.)
    np.testing.assert_allclose(z['r'],-1/3,rtol=0,atol=1e-16)
    np.testing.assert_allclose(z['t'],2/3,rtol=0,atol=2e-16)
    np.testing.assert_allclose(z['T'],8/9,rtol=0,atol=2e-16)
    assert np.all(z['T']>z['t']**2)


@pytest.mark.parametrize('component',['e','hx','hy'])
def test_continuum_modal_fields_satisfy_maxwell_on_each_side(component):
    p=inputs();ky=4.;h=1e-5;t=3.7
    for x,eps in [(np.array([3.1,8.2,14.7]),p['epsilon_left']),(np.array([16.3,19.1,23.7]),p['epsilon_right'])]:
        value=lambda xx,tt,c:o.modal_amplitudes(xx,p,ky,tt,c)
        time=(value(x,t+h,component)-value(x,t-h,component))/(2*h)
        if component=='e':space=((value(x+h,t,'hy')-value(x-h,t,'hy'))/(2*h)-1j*ky*value(x,t,'hx'))/eps
        elif component=='hx':space=-1j*ky*value(x,t,'e')
        else:space=(value(x+h,t,'e')-value(x-h,t,'e'))/(2*h)
        np.testing.assert_allclose(time,space,rtol=0,atol=2e-8)


def test_tangential_e_and_h_and_normal_b_match_at_interface():
    p=inputs();ky=4.;x=np.array([p['interface']]);t=10.
    for component in ['e','hx','hy']:
        left=o.modal_amplitudes(x,p,ky,t,component,'incident')+o.modal_amplitudes(x,p,ky,t,component,'reflected')
        right=o.modal_amplitudes(x,p,ky,t,component,'transmitted')
        np.testing.assert_allclose(left,right,rtol=0,atol=3e-15)


def test_parseval_incident_norm_and_finite_box_partition_are_independent_of_yee():
    p=inputs();ky=4.;incident,R,T=o.reference_energy(p,ky)
    # Dense same-time continuum quadrature independently constructs electric
    # and magnetic energy, including the eps jump and spectral cross terms.
    x=np.linspace(0,p['lengths'][0],4097)
    for time in [0.,p['end_time']]:
        e=o.modal_amplitudes(x,p,ky,time,'e');hx=o.modal_amplitudes(x,p,ky,time,'hx');hy=o.modal_amplitudes(x,p,ky,time,'hy')
        eps=np.where(x<p['interface'],p['epsilon_left'],p['epsilon_right']);eps[x==p['interface']]=(p['epsilon_left']+p['epsilon_right'])/2
        density=p['lengths'][1]/4*(eps*abs(e)**2+abs(hx)**2+abs(hy)**2)
        assert np.trapezoid(density,x)/incident==pytest.approx(1.,abs=2e-9)
        if time:
            left=x<=p['interface'];right=x>=p['interface']
            assert np.trapezoid(density[left],x[left])/incident==pytest.approx(R,abs=2e-8)
            assert np.trapezoid(density[right],x[right])/incident==pytest.approx(T,abs=2e-8)


def test_random_heterogeneous_yee_state_conserves_modified_energy():
    g=o.geometry(40,13,10.,2.,.02,1.3,3.9,5.)
    rng=np.random.default_rng(81)
    e=rng.normal(size=(41,13));e[[0,-1]]=0
    hx=rng.normal(size=e.shape);hx[[0,-1]]=0;hy=rng.normal(size=(40,13))
    state=(e,np.zeros_like(e),hx,hy);initial=o.energy(state,g)[0]
    for _ in range(100):state=o.step(state,g)
    assert o.energy(state,g)[0]/initial==pytest.approx(1.,abs=2e-15)


def test_reference_period_is_regenerated_not_zero_padded():
    p=inputs();k,a=o.spectrum(p);large,b=o.spectrum(p,2*p['reference_period'])
    assert len(large)>len(k)
    assert large[0]==pytest.approx(k[0]/2)
    assert np.any(b[::2]>0)
    small=o.reference_energy(p,4.);big=o.reference_energy(p,4.,2*p['reference_period'])
    np.testing.assert_allclose(small,big,rtol=0,atol=3e-14)


def test_schema_rejects_unsafe_clocks_nonperiodic_modes_or_unresolved_meshes():
    p=inputs();validate(p)
    for key,value in [('courant',1.),('epsilon_right',.5),('reference_period',12.),('transverse_wave_numbers',[0.,3.]),('meshes',[[770,16],[1540,32],[3080,64]]),('spectral_cutoff',1000.)]:
        bad=deepcopy(p);bad[key]=value
        with pytest.raises(ValueError):validate(bad)


def test_cli_preserves_nonempty_output_and_reports_input_error(tmp_path):
    out=tmp_path/'output';out.mkdir();marker=out/'keep.txt';marker.write_text('keep')
    proc=subprocess.run([sys.executable,str(HERE/'run_oblique.py'),'--input',str(HERE/'inputs/dielectric-oblique.json'),'--output',str(out)],capture_output=True,text=True)
    assert proc.returncode==2 and marker.read_text()=='keep'


def test_high_to_low_or_nonpositive_modes_are_outside_declared_scope():
    for k,eps1,eps2 in [(np.array([0.]),1.,4.),(np.array([-1.]),1.,4.),(np.array([2.]),4.,1.)]:
        with pytest.raises(ValueError):o.fresnel(k,4.,eps1,eps2)
