"""Independent algebra, full-Yee equivalence and energy tests for optical p."""
from copy import deepcopy
import json
from pathlib import Path
import numpy as np
import pytest
import polarization as p
from run_polarization import validate


def config():return json.loads((Path(__file__).parent/'inputs/p-polarization.json').read_text())


def random_state(g):
    r=np.random.default_rng(921);n=g['nx'];a=[r.normal(size=n)+1j*r.normal(size=n) for _ in range(2)];ey=r.normal(size=n+1)+1j*r.normal(size=n+1);ey[[0,-1]]=0
    return a[0],a[1],ey


@pytest.mark.parametrize('eps',[1.,3.9])
def test_weighted_energy_with_unequal_materials_and_arbitrary_complex_fields(eps):
    g=p.geometry(32,16,[8.,np.pi],.025,1.7,eps,4.,2.);s=random_state(g);u0=p.energy(s,g)[0]
    for _ in range(140):s=p.step(s,g)
    assert abs(p.energy(s,g)[0]/u0-1)<2e-14


def test_physical_energy_difference_is_electric_half_step_square():
    g=p.geometry(24,12,[6.,np.pi],.02,1.2,4.,3.,2.);s=random_state(g);xp,yp=p.electric(s,g);u,v=p.energy(s,g)
    expected=g['ly']*g['dx']/16*(np.sum(g['epsx']*abs(xp-s[1])**2)+np.sum(g['epsy']*abs(yp-s[2])**2))
    assert v-u==pytest.approx(expected,rel=0,abs=3e-14)


def test_full_real_2d_yee_is_exactly_the_same_single_mode_backend():
    g=p.geometry(20,16,[5.,np.pi],.025,1.3,3.1,2.5,4.);s=random_state(g);y=np.arange(g['ny'])*g['dy'];yh=y+g['dy']/2
    def expand(a):return tuple(np.real(z[:,None]*np.exp(1j*g['ky']*yy)[None,:]) for z,yy in zip(a,[yh,y,yh]))
    full=expand(s)
    for _ in range(15):
        s=p.step(s,g);full=p.full_step(full,g)
        for a,b in zip(full,expand(s)):np.testing.assert_allclose(a,b,rtol=0,atol=4e-15)


def test_epsilon_face_average_and_region_partition_preserve_total_energy():
    g=p.geometry(24,12,[6.,np.pi],.02,1.,4.,3.,2.);s=random_state(g)
    assert g['epsy'][12]==2.5
    assert g['epsx'][11]==1 and g['epsx'][12]==4
    total=p.energy(s,g)[1];left=p.region_energy(s,g,0,3.);right=p.region_energy(s,g,3.,6.)
    assert left+right==pytest.approx(total,rel=0,abs=3e-14)
    # Interface Ey belongs half to each physical material, not epsilon_avg/2.
    z=tuple(np.zeros_like(a) for a in s);z[2][12]=1
    assert p.physical_integral(z,g,3.,6.)==pytest.approx(.25*g['ly']*g['dx']*4*.5)


def test_initial_discrete_D_divergence_is_preserved_not_assumed_zero():
    g=p.geometry(24,12,[6.,np.pi],.02,1.,4.,3.,2.);s=random_state(g)
    def div(a):return np.diff(g['epsx']*a[1])/g['dx']+1j*g['K']*g['epsy'][1:-1]*a[2][1:-1]
    old=div(s)
    for _ in range(30):s=p.step(s,g)
    np.testing.assert_allclose(div(s),old,rtol=0,atol=8e-14)


@pytest.mark.parametrize('eps1,eps2,ky',[(1.,4.,2.),(4.,1.,4.)])
def test_fresnel_matches_independent_complex_boundary_linear_solve(eps1,eps2,ky):
    ks=np.array([1.7,2.1,3.3,5.2]);z=p.fresnel(ks,ky,eps1,eps2)
    for i,k in enumerate(ks):
        q=z['q'][i];r,t=np.linalg.solve(np.array([[1.,-1.],[-k/eps1,-q/eps2]],complex),np.array([-1.,-k/eps1],complex))
        assert abs(r-z['r'][i])<4e-16 and abs(t-z['t'][i])<4e-16
    np.testing.assert_allclose(z['R']+z['T'],1,rtol=0,atol=5e-16)


def test_brewster_carrier_zero_and_nonzero_finite_band_packet_are_distinct():
    cfg=config();c=cfg['subcases'][1];z=p.fresnel(np.array([c['carrier_kx']]),c['ky'],c['epsilon_left'],c['epsilon_right'])
    assert abs(z['r'][0])<1e-15
    _,R,T=p.incident_energy(cfg,c)
    assert 0<R<.01 and abs(R+T-1)<1e-15


def test_TIR_every_compact_band_mode_decays_with_unit_reflection():
    cfg=config();c=cfg['subcases'][2];k,a=p.spectrum(cfg,c);z=p.fresnel(k,c['ky'],4.,1.)
    assert np.all(a>0) and np.all(z['q'].imag>0) and np.all(z['q'].real==0)
    np.testing.assert_allclose(z['R'],1,rtol=0,atol=6e-16);assert np.max(z['T'])==0
    carrier=p.fresnel(np.array([4.]),4.,4.,1.)
    assert carrier['q'][0]==pytest.approx(1j*np.sqrt(8))
    assert carrier['r'][0]==pytest.approx(-7/9-1j*4*np.sqrt(2)/9)
    ey=carrier['q'][0]/carrier['omega'][0]*carrier['t'][0]
    assert abs(np.real(ey*np.conj(carrier['t'][0])))<1e-15


def test_continuum_modal_fields_satisfy_maxwell_at_each_material():
    cfg=config();c=cfg['subcases'][0];h=2e-5;t=15.
    for x,eps in [(44.,1.),(52.,4.)]:
        a=lambda xx,tt,component:p.amplitude(np.array([xx]),cfg,c,tt,component)[0]
        ht=(a(x,t+h,'h')-a(x,t-h,'h'))/(2*h);ext=(a(x,t+h,'ex')-a(x,t-h,'ex'))/(2*h);eyt=(a(x,t+h,'ey')-a(x,t-h,'ey'))/(2*h)
        hx=(a(x+h,t,'h')-a(x-h,t,'h'))/(2*h);eyx=(a(x+h,t,'ey')-a(x-h,t,'ey'))/(2*h)
        assert abs(eps*ext-1j*c['ky']*a(x,t,'h'))<2e-7
        assert abs(eps*eyt+hx)<2e-7
        assert abs(ht-(1j*c['ky']*a(x,t,'ex')-eyx))<2e-7


def test_validation_rejects_unsafe_geometry_clock_and_TIR_support():
    cfg=config();validate(cfg)
    for badvalue in [0.,1.,float('nan')]:
        bad=deepcopy(cfg);bad['courant']=badvalue
        with pytest.raises(ValueError):validate(bad)
    bad=deepcopy(cfg);bad['subcases'][2]['epsilon_right']=4.
    with pytest.raises(ValueError):validate(bad)
    bad=deepcopy(cfg);bad['subcases'][0]['meshes'][1][1]+=1
    with pytest.raises(ValueError):validate(bad)
    with pytest.raises(ValueError):p.geometry(16,8,[4.,np.pi],1.,1.,4.,2.,2.)
    with pytest.raises(ValueError):p.geometry(16,8,[4.,np.pi],.01,1.,4.,2.,0.)


def test_joint_refinement_has_shared_exact_interface_accuracy_and_end_clocks():
    cfg=config()
    for c in cfg['subcases']:
        clocks=[p.clock(cfg,c,*mesh) for mesh in c['meshes']]
        assert [n for n,dt in clocks]==[clocks[0][0]*f for f in [1,2,4]]
        for (n,dt),(nx,ny) in zip(clocks,c['meshes']):
            assert round(c['accuracy_time']/dt)*dt==pytest.approx(c['accuracy_time'],rel=0,abs=1e-12)
            assert n*dt==pytest.approx(c['end_time'],rel=0,abs=1e-12)
            assert dt*np.hypot(nx/c['lengths'][0],ny/c['lengths'][1])/np.sqrt(min(c['epsilon_left'],c['epsilon_right']))<1


def test_transient_flux_metric_retains_error_when_signed_integrals_cancel():
    t=np.linspace(0,2*np.pi,2049);reference=np.sin(t);numerical=reference+.1*np.sin(2*t)
    assert abs(p.trapezoid(numerical-reference,t))<1e-15
    assert p.transient_flux_error(numerical,reference,t)==pytest.approx(.1,rel=0,abs=2e-16)
    with pytest.raises(ValueError):p.transient_flux_error(numerical,np.zeros_like(t),t)
