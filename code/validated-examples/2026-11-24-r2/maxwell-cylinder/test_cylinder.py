import json
from pathlib import Path
import numpy as np
import pytest
from scipy.special import hankel1
import cylinder_draft as core
from poynting import physical_flux
import reference_draft as ref
import cylinder_evolution as evolution
import run as driver

ROOT=Path(__file__).resolve().parent


@pytest.mark.parametrize('epsilon',[1.,2.25])
def test_first_step_is_exact_local_contrast_source(epsilon):
    g=core.build_grid(32,4.,.01,.5,epsilon,1.,12.);state=core.zero_state(g)
    out=core.advance(state,g,0.,2*np.pi)
    delta=(core.incident(g['x'],.01,2*np.pi,.01,g['h'])-core.incident(g['x'],0.,2*np.pi,.01,g['h']))[:,None]
    expected=-(g['epsilon']-1)/g['epsilon']*delta
    assert np.max(abs(out[0]+out[1]-expected))<2e-15
    assert np.max(abs(out[2]))==0 and np.max(abs(out[3]))==0


def test_zero_contrast_has_no_scattered_field():
    g=core.build_grid(32,4.,.01,.5,1.,1.,12.);s=core.zero_state(g)
    for j in range(8):s=core.advance(s,g,j*.01,2*np.pi)
    assert all(np.count_nonzero(z)==0 for z in s)


def test_actual_both_curls_and_linearity():
    g=core.build_grid(32,4.,.01,.5,2.25,1.,12.);a=core.zero_state(g);b=core.zero_state(g)
    for j in range(12):a=core.advance(a,g,j*.01,2*np.pi);b=core.advance(b,g,j*.01,2*np.pi,.3)
    assert np.max(abs(a[2]))>0 and np.max(abs(a[3]))>0
    assert max(np.max(abs(y-.3*x)) for x,y in zip(a,b))<2e-14


@pytest.mark.parametrize('changes',[dict(dt=.2),dict(epsilon=.5),dict(radius=1.8)])
def test_invalid_grid_has_explicit_failure(changes):
    args=dict(cells=32,length=4.,dt=.01,radius=.5,epsilon=2.25,layer=1.,strength=12.);args.update(changes)
    with pytest.raises(ValueError):core.build_grid(**args)


def test_outgoing_hankel_flux_has_physical_normalization():
    k=2*np.pi;g=core.build_grid(144,6.,.01,.25,2.25,1.,12.)
    X,Y=np.meshgrid(g['x'],g['x'],indexing='ij');r=np.hypot(X,Y);E=np.zeros_like(r,dtype=complex);E[r>0]=hankel1(0,k*r[r>0])
    X,Y=np.meshgrid(g['x'],g['xh'],indexing='ij');r=np.hypot(X,Y);Hx=1j*hankel1(1,k*r)*Y/r
    X,Y=np.meshgrid(g['xh'],g['x'],indexing='ij');r=np.hypot(X,Y);Hy=-1j*hankel1(1,k*r)*X/r
    power=physical_flux((E,Hx,Hy),g,-1.,1.)
    assert abs(power/(2/k)-1)<.005
    assert physical_flux((E,-Hx,-Hy),g,-1.,1.)<0


@pytest.mark.parametrize('epsilon',[2.25,4.])
def test_ordinary_cylindrical_modes_are_lossless_unitary(epsilon):
    n,a=ref.cylinder_coefficients(2*np.pi,.25,epsilon,12)
    assert np.array_equal(n,np.arange(-12,13))
    assert np.max(abs(a.real+abs(a)**2))<2e-13


def test_analytic_zero_contrast_exact():
    z=ref.cylinder_scattering_width(2*np.pi,.25,1.,24)
    assert z['scattering']==0 and z['extinction']==0


def test_series_doubling_qualifies_width_and_exterior_field():
    a=ref.cylinder_scattering_width(2*np.pi,.25,2.25,12);b=ref.cylinder_scattering_width(2*np.pi,.25,2.25,24)
    assert abs(a['scattering']-b['scattering'])<1e-12
    x=np.array([-.7,.8,1.]);y=np.array([.4,-.3,.1])
    assert np.max(abs(ref.cylinder_exterior_field(x,y,2*np.pi,.25,2.25,12)-ref.cylinder_exterior_field(x,y,2*np.pi,.25,2.25,24)))<1e-12


def short_spec():
    s=json.loads((ROOT/'inputs.json').read_text())['cylinder'];return {**s,'length':4.,'radius':.5,'burn_periods':2,'sample_periods':2,'contours':[.75,1.]}


def test_full_sampler_uses_own_time_phases_and_preserves_linearity(tmp_path):
    s=short_spec();a,_=evolution.solve(s,8,1.,2.25,tmp_path,'a');b,_=evolution.solve(s,8,.5,2.25,tmp_path,'b')
    assert len(a['times'])==5 and a['times'][-1]==4.
    for n in ['E','Hx','Hy']:assert np.max(abs(2*b[n+'_phasor']-a[n+'_phasor']))<2e-13


def test_raw_candidate_survives_later_reference_failure(tmp_path,monkeypatch):
    s=short_spec();s['ppw']=[8];proof=tmp_path/'references';proof.mkdir();(proof/'qualification.json').write_text('{"passed":true,"actual_checks":100}')
    monkeypatch.setattr(driver,'ROOT',tmp_path)
    monkeypatch.setattr(driver,'analyze',lambda *args:(_ for _ in ()).throw(RuntimeError('injected later reference failure')))
    with pytest.raises(RuntimeError):driver.execute({'cylinder':s},{},tmp_path,[])
    with np.load(tmp_path/'cylinder-ppw8.npz',allow_pickle=False) as f:
        assert f['E'].shape[0]==5 and np.isfinite(f['E_phasor']).all()
    assert (tmp_path/'cylinder-ppw8-history.csv').exists()


@pytest.mark.parametrize('omega',[4.,2*np.pi])
def test_incident_uses_exact_discrete_dispersion(omega):
    h=.05;dt=.02;q=2*np.arcsin(h*np.sin(omega*dt/2)/dt)/h
    z=core.incident(np.array([0.,h]),.3,omega,dt,h)
    assert abs(z[1]/z[0]-np.exp(1j*q*h))<2e-15


@pytest.mark.parametrize('degree',[0,1,2,3])
def test_four_native_half_nodes_reproduce_cubic_moments_exactly(degree):
    g=core.build_grid(32,4.,.01,.5,2.25,1.,12.)
    E=np.ones((33,33));Hx=np.zeros((33,32));Hy=np.broadcast_to((g['xh'][:,None]-.25)**degree,(32,33)).copy()
    actual=physical_flux((E,Hx,Hy),g,-1.,1.)
    exact=-.5*((1.-.25)**degree-(-1.-.25)**degree)*2.
    assert actual==exact


def test_four_point_flux_requires_interior_padding():
    g=core.build_grid(32,4.,.01,.5,2.25,1.,12.);state=core.zero_state(g)
    with pytest.raises(ValueError):physical_flux((state[0],state[2],state[3]),g,-1.875,1.875)


def test_all_fixed_contours_have_four_point_support():
    s=json.loads((ROOT/'inputs.json').read_text())['cylinder']
    for ppw in s['ppw']:
        n=int(round(s['length']*ppw));h=s['length']/n
        for radius in s['contours']:
            lo=int(round((s['length']/2-radius)/h));hi=int(round((s['length']/2+radius)/h))
            assert lo>=2 and hi<=n-2
