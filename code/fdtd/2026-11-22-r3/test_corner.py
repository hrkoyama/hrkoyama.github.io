"""Independent identities and modal checks for genuine four-side/corner PML."""
from copy import deepcopy
import json
from pathlib import Path
import numpy as np
import pytest
import corner as c
from run_corner import validate


HERE=Path(__file__).resolve().parent
def inputs():return json.loads((HERE/'inputs/pml-corners.json').read_text())


def random_state(g):
    rng=np.random.default_rng(71);n=g['n']
    ex=rng.normal(size=(n+1,n+1));ey=rng.normal(size=ex.shape)
    hx=rng.normal(size=(n+1,n));hy=rng.normal(size=(n,n+1))
    ex[[0,-1]]=0;ex[:,[0,-1]]=0;ey[[0,-1]]=0;ey[:,[0,-1]]=0
    hx[[0,-1]]=0;hy[:,[0,-1]]=0
    return ex,ey,hx,hy


@pytest.mark.parametrize('strength',[0.,3.,19.])
def test_two_direction_independent_work_identity(strength):
    g=c.geometry(24,6.,.04,1.,strength)
    # Deliberately unequal x/y strengths prevent square symmetry hiding a swap.
    g['gy']*=1.7;g['gyh']*=1.7
    state=random_state(g);u0=c.energy(state,g)[0];work=np.zeros(4)
    for _ in range(80):
        new=c.step(state,g)
        work+=[np.sum(z) for z in c.work_densities(state,new,g)]
        state=new
    assert abs((c.energy(state,g)[0]+work.sum())/u0-1)<5e-14
    if strength:assert np.all(np.abs(work)>1e-3)
    else:assert np.all(work==0)


def transpose(state):return state[1].T,state[0].T,-state[3].T,-state[2].T


def test_axis_transpose_swaps_both_damping_pairs_and_magnetic_signs():
    g=c.geometry(20,5.,.04,1.,3.);g['gy']*=2.3;g['gyh']*=2.3
    swapped=deepcopy(g)
    swapped['gx']=g['gy'].T;swapped['gy']=g['gx'].T
    swapped['gxh']=g['gyh'].T;swapped['gyh']=g['gxh'].T
    state=random_state(g)
    for actual,expected in zip(c.step(transpose(state),swapped),transpose(c.step(state,g))):
        np.testing.assert_allclose(actual,expected,rtol=0,atol=2e-15)


@pytest.mark.parametrize('axis',[0,1])
def test_wall_reflection_covariance(axis):
    g=c.geometry(20,5.,.04,1.,7.);state=random_state(g)
    def reflect(s):
        z=[np.flip(a,axis=axis) for a in s]
        z[3 if axis==0 else 2]=-z[3 if axis==0 else 2]
        return tuple(z)
    for a,b in zip(c.step(reflect(state),g),reflect(c.step(state,g))):
        np.testing.assert_allclose(a,b,rtol=0,atol=2e-15)


def test_corner_quarter_weights_and_direct_tail_partition():
    g=c.geometry(16,4.,.03,1.,4.);state=random_state(g)
    assert c.weights(g,'e')[0,0]==g['dx']**2/4
    assert c.weights(g,'e')[1,0]==g['dx']**2/2
    assert c.weights(g,'hx')[0,0]==g['dx']**2/2
    inside,_=c.physical_energy_and_flux(state,g)
    outside,*_=c.initial_tail_diagnostics(state,state,g)
    assert inside+outside==pytest.approx(c.energy(state,g)[1],rel=0,abs=2e-14)


def test_corner_work_decomposition_covers_four_actual_overlap_regions():
    g=c.geometry(24,6.,.04,1.,8.);state=random_state(g);new=c.step(state,g)
    densities=c.work_densities(state,new,g);corners=c.corner_sums(densities,g)
    assert set(corners)=={'SW','SE','NW','NE'}
    assert all(abs(v)>1e-3 for v in corners.values())
    assert abs(sum(corners.values()))<sum(np.sum(np.abs(z)) for z in densities)


@pytest.mark.parametrize('component,index',[(2,(4,0)),(3,(0,4))])
def test_initial_magnetic_tail_covers_both_staggered_directions(component,index):
    g=c.geometry(16,4.,.03,1.,4.)
    state=tuple(np.zeros_like(a) for a in random_state(g))
    state[component][index]=3.
    # Hx in a y layer and Hy in an x layer must not be omitted.
    assert c.initial_tail_diagnostics(state,state,g)[-1]==3.


def test_exact_discrete_multimode_reference_against_separate_periodic_yee():
    p=inputs();p.update(length=8.,center=4.,reference_period=8.,spectral_cutoff=4.,axis_carrier=2.,diagonal_carrier=1.,width=.7,probe_offset=2.)
    g=c.geometry(32,8.,.06,0.,0.);state=c.packet(g,p,'diagonal',0,-g['dt']/2,True,clip=False)
    e=(state[0]+state[1])[:-1,:-1];hx=state[2][:-1];hy=state[3][:,:-1]
    times=np.arange(61)*g['dt'];reference=c.modal_trace(g,p,'diagonal',times,True)
    ids=np.rint(c.probes(p,'diagonal')/g['dx']).astype(int)
    for n in range(61):
        np.testing.assert_allclose(e[ids[:,0],ids[:,1]],reference[n],rtol=0,atol=5e-14)
        if n<60:
            hx=hx-g['dt']*(np.roll(e,-1,axis=1)-e)/g['dx']
            hy=hy+g['dt']*(np.roll(e,-1,axis=0)-e)/g['dx']
            e=e+g['dt']*((hy-np.roll(hy,1,axis=0))/g['dx']-(hx-np.roll(hx,1,axis=1))/g['dx'])


def test_continuum_reference_satisfies_maxwell_without_yee_update():
    p=inputs();p.update(reference_period=16.,spectral_cutoff=10.)
    g=c.geometry(16,16.,.05,2.,0.);h=1e-5;t=.4
    plus=c.packet(g,p,'diagonal',t+h,t+h,False,clip=False)
    minus=c.packet(g,p,'diagonal',t-h,t-h,False,clip=False)
    # At an electric node compare E_t with independently differentiated H.
    k,a=c.spectrum(p,'diagonal');q=np.hypot(k[:,None],k[None,:]);inv=np.divide(1.,q,out=np.zeros_like(q),where=q>0)
    x=g['x']-p['center'];co=np.cos(x[:,None]*k)
    divergence=-np.einsum('ij,jk->ik',np.einsum('ij,jk->ik',co,a*q*np.sin(q*t),optimize=False),co.T,optimize=False)
    actual=((plus[0]+plus[1])-(minus[0]+minus[1]))/(2*h)
    np.testing.assert_allclose(actual,divergence,rtol=0,atol=3e-9)


def test_all_four_pec_caps_remain_exactly_zero():
    p=inputs();g=c.geometry(32,16.,.15,2.,20.)
    state=c.packet(g,p,'diagonal',0,-g['dt']/2,True)
    for _ in range(60):state=c.step(state,g)
    e=state[0]+state[1]
    assert np.max(np.abs(e[[0,-1]]))==0
    assert np.max(np.abs(e[:,[0,-1]]))==0


def test_fixed_schema_and_unsafe_clocks_or_geometry():
    p=inputs();validate(p)
    for value in [0.,1.,1.1,float('nan')]:
        bad=deepcopy(p);bad['courant']=value
        with pytest.raises(ValueError):validate(bad)
    bad=deepcopy(p);bad['meshes']=[130,260,520]
    with pytest.raises(ValueError):validate(bad)
    bad=deepcopy(p);bad['spectral_cutoff']=np.pi*p['meshes'][0]/p['length']-.01
    with pytest.raises(ValueError,match='rounded spectrum'):validate(bad)
    with pytest.raises(ValueError):c.geometry(32,8.,.3,1.)
    with pytest.raises(ValueError):c.physical_energy_and_flux(random_state(c.geometry(16,4.,.02,0.)),c.geometry(16,4.,.02,0.))
