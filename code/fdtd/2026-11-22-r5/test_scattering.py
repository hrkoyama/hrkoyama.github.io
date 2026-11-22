"""Independent identities and nondefault regression checks for interface/PML."""
from copy import deepcopy
import json
from pathlib import Path
import numpy as np
import pytest
import scattering as s
from run_scattering import validate

HERE=Path(__file__).resolve().parent


def inputs(name):return json.loads((HERE/'inputs'/name).read_text())


def random_state(g,seed=11):
    rng=np.random.default_rng(seed)
    ex=rng.normal(size=(g['nx']+1,g['ny']));ey=rng.normal(size=ex.shape)
    hx=rng.normal(size=ex.shape);hy=rng.normal(size=(g['nx'],g['ny']))
    ex[[0,-1]]=0;ey[[0,-1]]=0;hx[[0,-1]]=0
    return ex,ey,hx,hy


@pytest.mark.parametrize('strength',[0.,3.,15.])
def test_signed_pml_work_closes_independent_modified_energy(strength):
    g=s.geometry(32,9,4.,2.,.025,epsilon_left=2.,epsilon_right=4.,interface=2.,pml_thickness=.5,pml_strength=strength)
    state=random_state(g);initial=s.energy(state,g)[0];we=wh=0.
    for _ in range(50):
        new=s.step(state,g);a,b=s.pml_work(state,new,g);we+=a;wh+=b;state=new
    assert abs((s.energy(state,g)[0]+we+wh)/initial-1)<5e-14
    if strength==0:assert we==wh==0


def test_physical_energy_subregions_partition_global_quadrature():
    g=s.geometry(32,9,4.,2.,.025,epsilon_left=2.,epsilon_right=4.,interface=2.)
    state=random_state(g)
    assert s.region_energy(state,g,0,2)+s.region_energy(state,g,2,4)==pytest.approx(s.energy(state,g)[1],abs=5e-14)


def test_trapezoidal_matched_magnetic_damping_is_not_scalar_field_sponge():
    g=s.geometry(32,8,4.,1.,.01,pml_thickness=1.,pml_strength=4.)
    e=np.zeros((33,8));hx=np.zeros_like(e);hy=np.ones((32,8))
    _,actual=s.magnetic(e,hx,hy,g)
    rate=g['gh'];expected=(1-.5*g['dt']*rate)/(1+.5*g['dt']*rate)
    assert np.max(np.abs(actual-expected))<2e-15
    assert actual[0,0]<actual[16,0]
    # Matching rates sampled on E and H positions are distinct profiles.
    assert g['ge'].shape!=(g['gh'].shape)


def test_two_direction_derivative_signs_and_periodic_seam():
    g=s.geometry(16,12,4.,3.,.01)
    x=g['x'][:,None];y=np.arange(g['ny'])[None,:]*g['dy']
    e=np.sin(np.pi*x/4)*np.cos(2*np.pi*y/3)
    xp,yp=s.magnetic(e,np.zeros_like(e),np.zeros((16,12)),g)
    assert np.allclose(xp,-g['dt']*(np.roll(e,-1,axis=1)-e)/g['dy'])
    assert np.allclose(yp,g['dt']*(e[1:]-e[:-1])/g['dx'])
    assert abs(xp[8,-1])>1e-4


def test_analytic_finite_packet_satisfies_continuum_maxwell_independently():
    g=s.geometry(24,16,6.,np.pi/4,.01)
    # Central differences of the analytic finite sum, not Yee evolution.
    h=1e-5;args=(g,12.,8.,3.,.5)
    a=s.continuum_packet(*args,h,h,enforce_caps=False);b=s.continuum_packet(*args,-h,-h,enforce_caps=False)
    xg={**g,'x':g['x']+h,'xh':g['xh']+h};xm={**g,'x':g['x']-h,'xh':g['xh']-h}
    plus=s.continuum_packet(xg,12.,8.,3.,.5,0,0,enforce_caps=False)
    minus=s.continuum_packet(xm,12.,8.,3.,.5,0,0,enforce_caps=False)
    # Hy lives on xhalf, so compare dHy/dt to dEz/dx at that location.
    ehg={**g,'x':g['xh']}
    ep=s.continuum_packet({**ehg,'x':g['xh']+h},12.,8.,3.,.5,0,0,enforce_caps=False)
    em=s.continuum_packet({**ehg,'x':g['xh']-h},12.,8.,3.,.5,0,0,enforce_caps=False)
    d_hy=(a[3]-b[3])/(2*h);d_e=(ep[0]+ep[1]-em[0]-em[1])/(2*h)
    assert np.max(np.abs(d_hy-d_e))<2e-7


def test_finite_layer_normal_return_has_nonzero_analytic_floor():
    p=inputs('pml-pulse.json');g=s.geometry(48,4,*p['lengths'],.01)
    times=np.linspace(10,16,501)
    reflected=s.reflected_packet_monitor(g,p,0.,times)[:,0]
    # At normal incidence the attenuation is frequency independent. Compare
    # with separately evaluated finite Fourier sum and PEC minus sign.
    ks=np.arange(1,512)*2*np.pi/64;om=ks
    weights=p['width']/np.sqrt(2*np.pi)*np.exp(-.5*p['width']**2*(ks-p['carrier_kx'])**2)*(2*np.pi/64)
    undamped=-np.sum(np.cos(ks[None,:]*(2*p['lengths'][0]-p['monitor_x']-p['center'])-times[:,None]*om)*weights,axis=1)
    attenuation=np.exp(-2*p['pml_strength']*p['pml_thickness']/(p['pml_order']+1))
    assert np.max(np.abs(reflected-undamped*attenuation))<1e-18
    assert 4e-5<np.max(np.abs(reflected))<5e-5


def test_reverse_index_interface_uses_epsilon_energy_normalization():
    p=inputs('dielectric-interface.json');p.update(epsilon_left=4.,epsilon_right=1.,width=.4,end_time=12.)
    row,_,_=s.run_interface(p,256)
    assert row['reflection_amplitude']>0
    assert abs(row['reflected_energy_fraction']-1/9)<.001
    assert abs(row['transmitted_energy_fraction']-8/9)<.001
    assert row['energy_fraction_closure']<.001


def test_fresnel_interface_grid_refinement_and_energy_are_independent():
    p=inputs('dielectric-interface.json')
    coarse,_,_=s.run_interface(p,160);fine,_,_=s.run_interface(p,320)
    assert coarse['field_relative_l2']/fine['field_relative_l2']>3.5
    assert coarse['reflection_amplitude_error']/fine['reflection_amplitude_error']>3.5
    assert fine['analytic_r']==pytest.approx(-1/3)
    assert fine['analytic_t']==pytest.approx(2/3)
    assert fine['modified_energy_max_relative_drift']<1e-13


def test_pec_caps_stay_exactly_zero_with_oblique_damped_state():
    p=inputs('pml-pulse.json');g=s.geometry(48,12,*p['lengths'],.015,pml_thickness=2,pml_strength=10)
    state=s.continuum_packet(g,12,8,5,.5,0,-.0075)
    for _ in range(40):state=s.step(state,g)
    assert np.max(np.abs((state[0]+state[1])[[0,-1]]))==0


@pytest.mark.parametrize('name',['dielectric-interface.json','pml-pulse.json'])
def test_fixed_input_schema(name):validate(inputs(name))


@pytest.mark.parametrize('value',[0,1,1.1,float('nan')])
def test_invalid_courant_rejected(value):
    p=inputs('pml-pulse.json');p['courant']=value
    with pytest.raises(ValueError):validate(p)


def test_negative_material_and_nonperiodic_transverse_mode_rejected():
    p=inputs('dielectric-interface.json');p['epsilon_right']=-1
    with pytest.raises(ValueError):validate(p)
    p=inputs('pml-pulse.json');p['transverse_wave_numbers']=[1.]
    with pytest.raises(ValueError):validate(p)


def test_pml_faces_must_align_for_physical_flux_benchmark():
    p=inputs('pml-pulse.json');p['meshes']=[[160,8],[320,16],[640,32]]
    with pytest.raises(ValueError):validate(p)
