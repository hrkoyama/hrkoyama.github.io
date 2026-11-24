import numpy as np
import pytest
import modal_yee_draft as core
import slab_evolution as evolution
import reference_draft as reference
from slab_reference import vacuum_monitors


def spec():
    return dict(domain=[-8.,8.],slab=[.5,1.],ky=2.,carrier=4.,width=.5,center=-2.,courant=.5,final_time=2.,frequencies=[3.5,4.,4.5],left_monitor=0.,right_monitor=2.,material=dict(epsilon_inf=1.5,delta_epsilon=.75,omega0=9.,gamma=.5,sigma=.04))


@pytest.mark.parametrize('polarization',['s','p'])
def test_direct_closed_PEC_energy_ledger(polarization):
    s=spec();g=evolution.build(s,.25,16);state=evolution.initial(s,g,polarization);old=evolution.energy(state,g,polarization);work=0.
    advance=core.advance_s if polarization=='s' else core.advance_p
    for _ in range(12):state,d=advance(state,g);work+=evolution.physical_work(d,g,polarization)
    assert abs(evolution.energy(state,g,polarization)-old+work)<3e-12
    assert work>=0


def test_p_both_electric_components_drive_material_current():
    s=spec();g=evolution.build(s,.25,16);state=evolution.initial(s,g,'p')
    for _ in range(4):state,_=core.advance_p(state,g)
    assert np.max(abs(state[5]))>0 and np.max(abs(state[6]))>0


@pytest.mark.parametrize('polarization',['s','p'])
def test_zero_strength_cells_do_not_create_oscillators(polarization):
    s=spec();g=evolution.build(s,.25,16);state=evolution.initial(s,g,polarization);step=core.advance_s if polarization=='s' else core.advance_p
    for _ in range(4):state,_=step(state,g)
    indices=[(3,'node'),(4,'node')] if polarization=='s' else [(3,'face'),(4,'node'),(5,'face'),(6,'node')]
    for j,side in indices:assert np.count_nonzero(state[j][g['strength_'+side]==0])==0


@pytest.mark.parametrize('polarization',['s','p'])
def test_finite_window_vacuum_DFT_independent_geometric_sum(tmp_path,polarization):
    s=spec();s['material']={**s['material'],'epsilon_inf':1.,'delta_epsilon':0.,'sigma':0.}
    fields,g=evolution.solve(s,.125,16,polarization,tmp_path,'vac'+polarization)
    exact=vacuum_monitors(s,g['h'],g['dy'],g['dt'],g['steps'],polarization,fields['monitor_coordinates'])
    assert np.max(abs(fields['monitors'][1]-exact))<3e-11


def test_normal_incidence_sp_sign_convention():
    c=spec()['material'];w=np.array([5.1,6.,6.9]);s=reference.slab(w,0.,c,1.,'s');p=reference.slab(w,0.,c,1.,'p')
    assert np.max(abs(s['r']+p['r']))<2e-14
    assert np.max(abs(s['t']-p['t']))<2e-14


@pytest.mark.parametrize('polarization',['s','p'])
def test_reference_direct_loss_independent_of_RT(polarization):
    c=spec()['material'];w=np.array([5.1,6.,6.9]);z=reference.slab(w,4.,c,1.,polarization);A=reference.direct_absorptance(w,4.,c,1.,polarization)
    assert np.min(A)>0 and np.max(abs(z['R']+z['T']+A-1))<2e-12


@pytest.mark.parametrize('polarization',['s','p'])
def test_zero_width_reference_is_transparent(polarization):
    z=reference.slab(np.array([5.1,6.,6.9]),4.,spec()['material'],0.,polarization)
    assert np.max(abs(z['r']))==0 and np.max(abs(z['t']-1))<2e-15


def test_direct_volume_quadrature_doubling():
    c=spec()['material'];w=np.array([5.1,6.,6.9])
    a=reference.direct_absorptance(w,4.,c,1.,'p',2);b=reference.direct_absorptance(w,4.,c,1.,'p',4)
    assert np.max(abs(a-b))<2e-12


def test_native_curl_adjoint_with_PEC_nodes():
    E=np.sin(np.linspace(0,np.pi,17))*(1+.3j);H=np.cos((np.arange(16)+.5)*.2)*(1-.1j);h=.25
    assert abs(np.vdot(E,core.node_derivative(H,h))+np.vdot(np.diff(E)/h,H))<2e-13


def test_complete_step_retained_before_diagnostic_failure(tmp_path,monkeypatch):
    original=evolution.energy;calls=0
    def fault(*args):
        nonlocal calls
        calls+=1
        if calls==3:raise RuntimeError('injected energy diagnostic failure')
        return original(*args)
    monkeypatch.setattr(evolution,'energy',fault)
    with pytest.raises(RuntimeError):evolution.solve(spec(),.25,16,'p',tmp_path,'fault')
    with np.load(tmp_path/'fault-current-state.npz',allow_pickle=False) as f:
        assert int(f['material_step'])==1 and int(f['vacuum_step'])==1
        assert all(np.isfinite(f['material_state'+str(i)]).all() for i in range(9))
    assert (tmp_path/'fault-initial-state.npz').exists()
