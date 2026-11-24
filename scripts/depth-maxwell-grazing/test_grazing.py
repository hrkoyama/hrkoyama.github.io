import numpy as np
import pytest
import centered_pml as core
import modal_yee_draft as old
import pml_evolution as evolution
import json
from pathlib import Path
from specifications import pml_specs


def grid(peak=6.,gamma=.005):
    return core.build(16,4.,.2,4.,.6,dict(epsilon_inf=1.,delta_epsilon=.2,omega0=12.,gamma=gamma,sigma=0.),1.,peak,3,.04)


def state(g):
    x=g['x'];xf=g['xf'];E=np.sin(np.pi*x/4)*(1+.3j);Hx=.2*E;Hy=.2*np.cos(np.pi*xf/4)*(1+.1j);P=.03*E;J=.1j*E
    return E,Hx,Hy,P,J,np.zeros_like(Hy),np.zeros_like(E),np.diff(E)/g['h'],old.node_derivative(Hy,g['h'])


@pytest.mark.parametrize('rate',[0.,2.,6.])
def test_filter_exact_bilinear_frequency_response(rate):
    dt=.02;w=6.;b,c=core.coefficients(rate,dt);z=np.exp(-1j*w*dt);H=c*(1+1/z)/(1-b/z)
    actual,_=core.filter_step(np.array([1.+0j]),np.array([1/z]),np.array([H/z]),(b,c));wt=2*np.tan(w*dt/2)/dt
    assert abs(actual[0]-(-1j*wt)/(rate-1j*wt))<2e-14


def test_zero_rate_recovers_qualified_old_Yee_arrays():
    g=grid(0.);s=state(g);out,_=core.advance(s,g)
    g['stretch_face']=(np.ones(16),np.zeros(16),np.ones(16));g['stretch_node']=(np.ones(17),np.zeros(17),np.ones(17))
    expected,_=old.advance_s(s[:7],g)
    assert max(np.max(abs(a-b)) for a,b in zip(out[:5],expected[:5]))==0


@pytest.mark.parametrize('gamma',[0.,.005,.5])
def test_direct_signed_PML_work_balances_physical_ledger(gamma):
    g=grid(gamma=gamma);s=state(g);new,d=core.advance(s,g);physical,pml=core.work(s,new,d,g)
    assert physical>=0
    assert abs(core.modified_energy(new,g)-core.modified_energy(s,g)+physical-pml)<2e-12


def test_omitting_PML_work_is_detectable_negative_control():
    g=grid();s=state(g);new,d=core.advance(s,g);physical,pml=core.work(s,new,d,g)
    assert abs(pml)>1e-10
    assert abs(core.modified_energy(new,g)-core.modified_energy(s,g)+physical)>1e-10


def test_diagnostic_lookahead_matches_qualified_functions():
    g=grid();s=state(g);new,d=core.advance(s,g);actual=evolution.energy_and_work(s,new,d,g);physical,pml=core.work(s,new,d,g)
    assert actual[0]==core.modified_energy(new,g)
    assert actual[1]==physical and actual[2]==pml


def test_negative_stretch_rate_rejected():
    with pytest.raises(ValueError):core.coefficients(-.1,.02)


def test_native_shapes_and_initialization_ownership():
    g=grid();s=state(g);reference={n:np.array([z.copy()]) for n,z in zip(['E','Hx','Hy','P','J'],s[:5])};saved={n:z.copy() for n,z in reference.items()}
    out=core.initialize(reference,g)
    assert len(out[0])==17 and len(out[2])==16
    assert len(out)==9
    out[0][1]=.2
    assert all(np.array_equal(reference[n],saved[n]) for n in reference)


def test_trapezoidal_filter_is_second_order_in_frequency():
    exact=-6j/(2-6j);errors=[]
    for dt in [.04,.02,.01]:wt=2*np.tan(6*dt/2)/dt;errors.append(abs(-1j*wt/(2-1j*wt)-exact))
    assert max(errors[1]/errors[0],errors[2]/errors[1])<.3


def test_complete_candidate_retained_before_work_diagnostic_failure(tmp_path,monkeypatch):
    g=grid();s=state(g);reference={n:np.array([z.copy()]) for n,z in zip(['E','Hx','Hy','P','J'],s[:5])};reference['box_length']=np.array(4096.)
    spec=dict(length=4.,courant=.6,pml_thickness=1.,pml_peak=6.,pml_order=3,final_time=.04)
    control=dict(cells=16,dy=.2,ky=4.,material=dict(epsilon_inf=1.,delta_epsilon=.2,omega0=12.,gamma=.005,sigma=0.),steps=g['steps'],dt=g['dt'])
    monkeypatch.setattr(evolution,'energy_and_work',lambda *args:(_ for _ in ()).throw(RuntimeError('injected work diagnostic failure')))
    with pytest.raises(RuntimeError):evolution.solve(spec,control,reference,tmp_path,'fault')
    with np.load(tmp_path/'fault-current-state.npz',allow_pickle=False) as f:
        assert int(f['step'])==1 and all(np.isfinite(f['state'+str(i)]).all() for i in range(9))


def test_layer_corefinement_preserves_reference_arguments_and_bounds_stiffness():
    root=Path(__file__).resolve().parent
    cfg=json.loads((root/'inputs.json').read_text());old_cfg=json.loads((root/'references/qualification-inputs.json').read_text())
    current=pml_specs(cfg);original=pml_specs(old_cfg)
    reference_keys=['id','cells','dy','ky','angle','material','h','dt','steps','times']
    assert [{k:s[k] for k in reference_keys} for s in current]==[{k:s[k] for k in reference_keys} for s in original]
    assert [s['pml_peak'] for s in current]==[6.,9.,12.,6.,12.]
    p=cfg['pml'];coarse=current[0]
    unrounded_coarse=p['courant']/np.sqrt(1/coarse['h']**2+1/coarse['dy']**2)
    bound=6*unrounded_coarse
    assert all(s['pml_peak']*s['dt']<=bound*(1+2e-15) for s in current[:3])
    assert all(abs(s['pml_peak']*s['h']-.75)<2e-15 for s in current[:3])


def test_actual_peak12_profile_one_step_retains_direct_work_identity():
    root=Path(__file__).resolve().parent;cfg=json.loads((root/'inputs.json').read_text());p=cfg['pml'];s=next(z for z in pml_specs(cfg) if z['id']=='damped-grazing-n1024')
    with np.load(root/'references/damped-grazing-n1024-box4096.npz',allow_pickle=False) as f:reference={n:f[n] for n in ['E','Hx','Hy','P','J']}
    g=core.build(s['cells'],p['length'],s['dy'],s['ky'],p['courant'],s['material'],p['pml_thickness'],s['pml_peak'],p['pml_order'],p['final_time'])
    initial=core.initialize(reference,g);out,d=core.advance(initial,g);physical,pml=core.work(initial,out,d,g)
    assert float(np.max(g['rate_node']))==12.
    assert physical>=0
    assert abs(core.modified_energy(out,g)-core.modified_energy(initial,g)+physical-pml)<2e-12
