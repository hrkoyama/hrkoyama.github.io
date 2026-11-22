"""Independent energy, constitutive, analytic slab and passive-limit tests."""
from copy import deepcopy
import json
from pathlib import Path
import numpy as np
import pytest
import dispersive as d
from run_dispersive import validate


def config():return json.loads((Path(__file__).parent/'inputs/loss-dispersion.json').read_text())

def small_case(**kw):return dict(config()['subcases'][1],length=8.,slab=[3.,5.],**kw)


def random_state(g):
    r=np.random.default_rng(9133);e=r.normal(size=g['nx']+1)+1j*r.normal(size=g['nx']+1);e[[0,-1]]=0;h=r.normal(size=g['nx'])+1j*r.normal(size=g['nx']);p=(r.normal(size=e.shape)+1j*r.normal(size=e.shape))*(g['f']>0);j=(r.normal(size=e.shape)+1j*r.normal(size=e.shape))*(g['f']>0)
    return e,h,p,j


@pytest.mark.parametrize('sigma,gamma,delta',[(.7,0.,0.),(0.,.8,1.5),(.6,.8,1.5),(0.,0.,1.5)])
def test_arbitrary_complex_fields_exact_modified_balance_and_independent_work(sigma,gamma,delta):
    c=small_case(sigma=sigma,gamma=gamma,delta_epsilon=delta);g=d.geometry(64,c,.025);s=random_state(g);u0=d.energy(s,g)[0];loss=0.
    for _ in range(120):
        sn=d.step(s,g);eb=(s[0]+sn[0])/2;jb=(s[3]+sn[3])/2;active=g['f']>0
        independent=g['dt']*g['dx']*(np.sum(g['sigma']*abs(eb)**2)+np.sum(g['gamma']*abs(jb[active])**2/g['f'][active]));we,wl=d.work(s,sn,g)
        assert we+wl==pytest.approx(independent,rel=2e-16,abs=2e-16);assert we>=0 and wl>=0
        loss+=independent;s=sn
    assert abs(d.energy(s,g)[0]+loss-u0)/u0<2e-14


def test_physical_minus_modified_energy_is_known_positive_half_step_square():
    g=d.geometry(64,small_case(),.025);s=random_state(g);u,v,_=d.energy(s,g);hp=d.magnetic(s[0],s[1],g)
    assert v-u==pytest.approx(g['dx']*np.sum(abs(hp-s[1])**2)/8,rel=2e-14,abs=2e-14)


def test_stiff_passive_oscillator_has_no_explicit_ADE_resonance_step_bound():
    c=small_case(omega0=200.,gamma=30.);g=d.geometry(64,c,.08);s=random_state(g);u0=d.energy(s,g)[0];loss=0.
    assert g['dt']*g['w0']>2
    for _ in range(150):
        sn=d.step(s,g);loss+=sum(d.work(s,sn,g));s=sn
    assert abs(d.energy(s,g)[0]+loss-u0)/u0<2e-14
    assert d.energy(s,g)[0]>=0 and np.isfinite(s[0]).all()


def test_closed_local_update_matches_independent_dense_midpoint_system():
    c=small_case(sigma=.3);g=d.geometry(64,c,.025);s=random_state(g);sn=d.step(s,g);hp=d.magnetic(s[0],s[1],g);curl=np.diff(hp)/g['dx'];dt=g['dt']
    for i in np.flatnonzero(g['f']>0):
        M=np.array([[-g['sigma'][i]/g['eps'][i],0,-1/g['eps'][i]],[0,0,1],[g['f'][i],-g['w0']**2,-g['gamma']]])
        old=np.array([s[0][i],s[2][i],s[3][i]]);rhs=(np.eye(3)+dt*M/2)@old+dt*np.array([curl[i-1]/g['eps'][i],0,0]);expected=np.linalg.solve(np.eye(3)-dt*M/2,rhs)
        np.testing.assert_allclose([sn[0][i],sn[2][i],sn[3][i]],expected,rtol=0,atol=3e-15)


def test_f0_resonant_frequency_is_nondispersive_and_ghost_states_cannot_feed_field():
    c=small_case(delta_epsilon=0.,sigma=.6,gamma=0.);w=np.array([c['omega0']]);assert np.isfinite(d.material(w,c)).all();assert np.isfinite(d.direct_spectral_absorption(w,c)).all()
    g=d.geometry(64,c,.025);s=random_state(g);ghost=(s[0],s[1],np.ones_like(s[2]),np.ones_like(s[3]));a=d.step(s,g);b=d.step(ghost,g)
    for x,y in zip(a,b):np.testing.assert_array_equal(x,y)
    assert np.all(a[2]==0) and np.all(a[3]==0)


@pytest.mark.parametrize('which',[0,1])
def test_slab_coefficients_match_independent_four_boundary_equation_solve(which):
    c=config()['subcases'][which]
    for omega in [2.1,3.,3.7]:
        z=d.slab(np.array([omega]),c);n=z['n'][0];q=z['q'][0];width=c['slab'][1]-c['slab'][0];ep=np.exp(1j*q*width);em=1/ep
        matrix=np.array([[1,-1,-1,0],[1,n,-n,0],[0,ep,em,-1],[0,-n*ep,n*em,1]],complex);r,a,b,t=np.linalg.solve(matrix,[-1,1,0,0])
        np.testing.assert_allclose([z[k][0] for k in ['r','a','b','t']],[r,a,b,t],rtol=0,atol=8e-16)


@pytest.mark.parametrize('delta',[0.,1.5])
def test_lossless_slab_has_unit_R_plus_T_and_zero_direct_absorption(delta):
    c=dict(config()['subcases'][1],delta_epsilon=delta,sigma=0.,gamma=0.);w=np.array([2.,3.,5.])
    z=d.slab(w,c);np.testing.assert_allclose(z['R']+z['T'],1,rtol=0,atol=8e-16);np.testing.assert_array_equal(d.direct_spectral_absorption(w,c),np.zeros(3))


def test_zero_thickness_and_vacuum_limits():
    c=dict(config()['subcases'][1],slab=[88.,88.]);z=d.slab(np.array([2.,3.,4.]),c);np.testing.assert_allclose(z['r'],0,atol=1e-15);np.testing.assert_allclose(z['t'],1,atol=1e-15)
    c=dict(c,epsilon_inf=1.,sigma=0.,delta_epsilon=0.,slab=[88.,92.]);w=np.array([2.,3.,4.]);z=d.slab(w,c);np.testing.assert_allclose(z['r'],0,atol=0);np.testing.assert_allclose(z['t'],np.exp(1j*w*4),atol=2e-15)


def test_passive_susceptibility_and_direct_volume_absorption():
    for c in config()['subcases']:
        w=np.array([1.,2.2,3.,4.5,5.8]);z=d.slab(w,c)
        assert np.min(z['epsilon'].imag)>=0 and np.min(z['n'].imag)>=0 and np.min(z['A'])>=-1e-15
        np.testing.assert_allclose(d.direct_spectral_absorption(w,c,128),z['A'],rtol=0,atol=5e-14)


def test_midpoint_harmonic_susceptibility_has_second_order_continuum_limit():
    c=config()['subcases'][1];omega=3.;f=c['delta_epsilon']*c['omega0']**2;errors=[]
    for dt in [.08,.04,.02]:
        wt=2/dt*np.tan(omega*dt/2);chi=f/(c['omega0']**2-wt*wt-1j*c['gamma']*wt);E0=1.;E1=np.exp(-1j*omega*dt);P0=chi;P1=chi*E1;J0=-1j*wt*chi;J1=J0*E1
        assert abs((P1-P0)/dt-(J1+J0)/2)<1e-14
        assert abs((J1-J0)/dt-(f*(E1+E0)-c['omega0']**2*(P1+P0)-c['gamma']*(J1+J0))/2)<3e-14
        errors.append(abs(chi-(d.material(np.array([omega]),c)[0]-c['epsilon_inf'])))
    assert min(np.log2(np.array(errors[:-1])/errors[1:]))>1.99


def test_continuum_slab_packet_satisfies_maxwell_and_material_equations():
    p=config();c=p['subcases'][1];h=1e-5;t=28.
    for x in [83.,90.,97.]:
        e=lambda xx,tt:d.packet(np.array([xx]),tt,p,c,'e')[0];hh=lambda xx,tt:d.packet(np.array([xx]),tt,p,c,'h')[0]
        ht=(hh(x,t+h)-hh(x,t-h))/(2*h);ex=(e(x+h,t)-e(x-h,t))/(2*h)
        assert abs(ht-ex)<2e-8
    w,a=d.spectrum(p,c);z=d.slab(w,c);x=90.;lo=c['slab'][0];E=(z['a']*np.exp(1j*z['q']*(x-lo))+z['b']*np.exp(-1j*z['q']*(x-lo)))*np.exp(1j*w*(lo-c['center'])-1j*w*t)*a;chi=d.material(w,c)-c['epsilon_inf'];P=chi*E;J=-1j*w*P
    et=np.sum(-1j*w*E);hx=(hh(x+h,t)-hh(x-h,t))/(2*h)
    assert abs(c['epsilon_inf']*et-hx+np.sum(J)+c['sigma']*np.sum(E))<2e-8


@pytest.mark.parametrize('key,bad',[('epsilon_inf',0.),('sigma',-.1),('gamma',-.1),('delta_epsilon',-.1),('omega0',0.)])
def test_reject_nonpassive_or_invalid_materials(key,bad):
    p=config();p['subcases'][1][key]=bad
    with pytest.raises(ValueError):validate(p)
    with pytest.raises(ValueError):d.geometry(64,small_case(**{key:bad}),.025)


def test_reject_invalid_clock_geometry_cfl_and_mesh():
    for key,value in [('courant',1.),('courant',float('nan'))]:
        p=config();p[key]=value
        with pytest.raises(ValueError):validate(p)
    p=config();p['subcases'][0]['meshes'][1]+=1
    with pytest.raises(ValueError):validate(p)
    p=config();p['subcases'][0]['monitors'][0]+=.001
    with pytest.raises(ValueError):validate(p)
    with pytest.raises(ValueError):d.geometry(64,small_case(),.125)
    with pytest.raises(ValueError):d.geometry(64,dict(small_case(),slab=[3.01,5.]),.025)


def test_common_physical_clocks_and_exact_doubling():
    p=config();validate(p)
    for c in p['subcases']:
        clocks=[d.clock(p,c,n) for n in c['meshes']];assert [n for n,dt in clocks]==[clocks[0][0]*i for i in [1,2,4]]
        for (n,dt),nx in zip(clocks,c['meshes']):
            assert n*dt==pytest.approx(c['end_time'],rel=0,abs=1e-12);assert round(c['accuracy_time']/dt)*dt==pytest.approx(c['accuracy_time'],rel=0,abs=1e-12);assert dt/(c['length']/nx)<p['courant']
