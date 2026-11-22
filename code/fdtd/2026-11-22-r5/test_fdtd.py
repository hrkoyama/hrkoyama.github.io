"""Independent mathematical properties, continuum modes and CLI contracts."""
import json
from pathlib import Path
import subprocess
import sys
import numpy as np
import pytest
from solver import (grid,exact_fields,step,energies,divergence,frequencies,
                    field_error,projected_frequency,run_mesh,magnetic_step,inner)
from run import validate

HERE=Path(__file__).parent


@pytest.mark.parametrize('boundary',['periodic','pec'])
def test_exact_discrete_eigenmode_oblique_rectangle(boundary):
    g=grid(19,27,1.2,1.7,.013,boundary)
    mode=[2,3]
    e,hx,hy=exact_fields(g,mode,0,-g['dt']/2,discrete=True)
    for _ in range(100):e,hx,hy=step(e,hx,hy,g)
    expected=exact_fields(g,mode,100*g['dt'],99.5*g['dt'],discrete=True)
    assert max(np.max(np.abs(a-b)) for a,b in zip((e,hx,hy),expected))<1e-12
    assert np.abs(divergence(hx,hy,g)).max()<1e-11


@pytest.mark.parametrize('boundary',['periodic','pec'])
def test_random_multimode_discrete_energy_and_divergence(boundary):
    g=grid(11,17,1.1,1.4,.02,boundary)
    shapes=[a.shape for a in exact_fields(g,[1,1],0,0)]
    rng=np.random.default_rng(81021)
    e,hx,hy=[rng.normal(size=s) for s in shapes]
    if boundary=='pec':
        e[[0,-1],:]=0;e[:,[0,-1]]=0
        hx[[0,-1],:]=0;hy[:,[0,-1]]=0
    u0,_=energies(e,hx,hy,g);div0=divergence(hx,hy,g)
    for _ in range(200):
        e,hx,hy=step(e,hx,hy,g)
        assert abs(energies(e,hx,hy,g)[0]/u0-1)<2e-13
        assert np.max(np.abs(divergence(hx,hy,g)-div0))<2e-12
    if boundary=='pec':assert np.all(e[[0,-1],:]==0) and np.all(e[:,[0,-1]]==0)


@pytest.mark.parametrize('boundary',['periodic','pec'])
def test_energy_identity_and_positive_modified_energy(boundary):
    g=grid(16,23,1,1.6,.015,boundary)
    e,hx,hy=exact_fields(g,[1,2],.13,.13-g['dt']/2)
    u,v=energies(e,hx,hy,g)
    xp,yp=magnetic_step(e,hx,hy,g)
    correction=.125*(inner(xp-hx,xp-hx,g,'hx')+inner(yp-hy,yp-hy,g,'hy'))
    assert u>0
    assert abs(v-u-correction)<1e-15


@pytest.mark.parametrize('case',['periodic-wave','pec-cavity'])
def test_continuum_field_and_frequency_second_order(case):
    p=json.loads((HERE/'inputs'/f'{case}.json').read_text())
    p['energy_periods']=p['error_periods']
    results=[run_mesh(p,nx,ny)[0] for nx,ny in p['meshes']]
    for a,b in zip(results,results[1:]):
        assert np.log2(a['field_relative_l2']/b['field_relative_l2'])>1.8
        assert np.log2(a['relative_frequency_error']/b['relative_frequency_error'])>1.8
    assert results[-1]['field_relative_l2']<p['acceptance']['max_field_error']
    assert max(a['dispersion_identity_relative_error'] for a in results)<1e-9


def test_projection_frequency_recovers_independent_oscillator():
    omega,dt=3.7,.013
    values=1.2*np.cos(omega*np.arange(250)*dt)+.4*np.sin(omega*np.arange(250)*dt)
    assert abs(projected_frequency(values,dt)-omega)<1e-11


@pytest.mark.parametrize('dt',[0,-1,float('nan'),float('inf'),1/np.sqrt(8**2+12**2),.1])
def test_reject_invalid_or_cfl_endpoint(dt):
    with pytest.raises(ValueError):grid(8,12,1,1,dt,'periodic')


@pytest.mark.parametrize('change',[{'courant':1},{'mode':[0,1]},{'mode':[8,1]},
                                 {'meshes':[[16,24],[32,49],[64,96]]},
                                 {'lengths':[-1,1]},{'boundary':'pec'}])
def test_invalid_inputs(change):
    p=json.loads((HERE/'inputs/periodic-wave.json').read_text());p.update(change)
    with pytest.raises(ValueError):validate(p)


def test_cli_refuses_existing_nonempty_output(tmp_path):
    (tmp_path/'keep.txt').write_text('preserve')
    r=subprocess.run([sys.executable,str(HERE/'run.py'),'--input',str(HERE/'inputs/periodic-wave.json'),'--output',str(tmp_path)],capture_output=True,text=True)
    assert r.returncode==2
    assert (tmp_path/'keep.txt').read_text()=='preserve'
    assert not (tmp_path/'result.json').exists()


def test_cavity_analytic_continuous_energy():
    # At t=0 all physical energy is electric, with spatial integral Area/8.
    g=grid(16,24,1,1.5,.01,'pec')
    e,hx,hy=exact_fields(g,[1,1],0,0)
    assert abs(.5*(inner(e,e,g,'e')+inner(hx,hx,g,'hx')+inner(hy,hy,g,'hy'))-1.5/8)<1e-14


def test_periodic_direction_and_unequal_magnetic_components():
    g=grid(16,24,1,1.5,.01,'periodic')
    kx,ky,w,_,_,_=frequencies(g,[1,1])
    e,hx,hy=exact_fields(g,[1,1],0,0)
    # Unequal kx,ky catch swapped components and incorrect Maxwell signs.
    assert abs(hx[0,0]-(ky/w)*np.cos(ky*g['dy']/2))<1e-14
    assert abs(hy[0,0]+(kx/w)*np.cos(kx*g['dx']/2))<1e-14
