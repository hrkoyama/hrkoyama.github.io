import copy,json,math
from pathlib import Path
import numpy as np
import pytest
from geometry import area,center,crossings,distance,grid,measure,negative_triangle_fraction
from level_set import Budget,eno2,integrate,redistance,rhs,run_case,validate,velocity


@pytest.fixture(scope='module')
def configs():return json.loads(Path('inputs.json').read_text())['cases']


@pytest.fixture(scope='module')
def measured(configs):return {key:run_case(config,Budget(90))[0] for key,config in configs.items()}


def test_analytic_motions_and_nontrivial_quarter_turn(configs):
    translation,rotation=configs.values()
    np.testing.assert_allclose(center(translation,1),[.5,.45],atol=1e-15)
    np.testing.assert_allclose(center(rotation,.25),[.5,.68],atol=1e-15)
    np.testing.assert_allclose(center(rotation,1),rotation['center'],atol=1e-15)
    assert np.linalg.norm(center(rotation,.25)-center(rotation,0))>.2


def test_eno2_is_exact_on_affine_fields_for_both_velocity_signs():
    axis=np.arange(-2,18)*.05;x,y=np.meshgrid(axis,axis)
    derivatives=eno2(2*x-3*y+1,.05)
    for got,wanted in zip(derivatives,[2,2,-3,-3]):np.testing.assert_allclose(got,wanted,atol=5e-14,rtol=0)


def test_eno2_quadratic_derivatives_and_orientation():
    axis=np.arange(-2,18)*.05;x,y=np.meshgrid(axis,axis)
    values=eno2(x*x+2*y*y,.05)
    for got,wanted in zip(values,[2*x[2:-2,2:-2]]*2+[4*y[2:-2,2:-2]]*2):
        np.testing.assert_allclose(got,wanted,atol=5e-14,rtol=0)


def test_prescribed_rotation_is_divergence_free_and_tangent_to_orbits(configs):
    config=configs['level-set-rotation'];x,y=grid(32);u,v=velocity(config,x,y)
    a,b=u*(x-.5),v*(y-.5)
    # A scale-aware binary64 cancellation bound. The original fixed2e-16
    # check was below the observed one-ulp residual2.220446049250313e-16.
    assert np.all(np.abs(a+b)<=4*np.finfo(float).eps*(np.abs(a)+np.abs(b)))
    np.testing.assert_allclose((u[:,2:]-u[:,:-2])*16,0,atol=0)
    np.testing.assert_allclose((v[2:]-v[:-2])*16,0,atol=0)


def test_rhs_transports_an_affine_interior_with_the_declared_sign(configs):
    config=configs['level-set-translation'];n=32;axis=(np.arange(-2,n+2)+.5)/n
    ghost=np.meshgrid(axis,axis);x,y=grid(n);q=2*x-3*y
    result=rhs(q,config,0,ghost,velocity(config,x,y))
    np.testing.assert_allclose(result[3:-3,3:-3],-.1,atol=1e-14)


def test_triangle_clipping_has_exact_plane_area_and_handles_zero_vertices():
    def value(a,b,c):return float(negative_triangle_fraction(np.array(a,dtype=float),np.array(b,dtype=float),np.array(c,dtype=float)))
    assert value(-1,1,1)==.25
    assert value(1,-1,-1)==.75
    assert value(0,1,1)==0
    assert value(-1,0,0)==1
    assert value(0,0,0)==0
    assert value(-2,-1,-3)==1


def test_geometric_area_and_edge_crossings_refine_against_a_circle(configs):
    config=configs['level-set-translation'];errors=[]
    for n in [32,64,128]:
        x,y=grid(n);phi=distance(config,x,y,0);row,points=measure(phi,config,0)
        errors.append(abs(row['area']-math.pi*config['radius']**2))
        assert len(points)>20 and row['interface_max_radial_error']<2/n**2
    assert errors[-1]<errors[0]/8


def test_disappeared_or_nonfinite_interface_is_a_failure(configs):
    x,y=grid(32)
    with pytest.raises(RuntimeError,match='disappeared'):crossings(np.ones_like(x),x,y)
    with pytest.raises(ValueError,match='finite'):measure(np.full_like(x,np.nan),configs['level-set-translation'],0)


def test_redistancing_reduces_a_deliberately_stretched_distance_gradient(configs):
    config=configs['level-set-translation'];x,y=grid(64);phi=2*distance(config,x,y,0)
    before,_=measure(phi,config,0)
    result=redistance(phi,1/64,80,.3);after,_=measure(result,config,0)
    assert after['band_distance_gradient_rms']<.4*before['band_distance_gradient_rms']
    assert after['interface_max_radial_error']<.02
    assert not np.array_equal(result,phi)


def test_redistance_does_not_mutate_its_input_and_zero_iterations_are_identity(configs):
    x,y=grid(32);phi=distance(configs['level-set-translation'],x,y,0);original=phi.copy()
    result=redistance(phi,1/32,0,.3)
    np.testing.assert_array_equal(phi,original);np.testing.assert_array_equal(result,phi)
    redistance(phi,1/32,5,.3);np.testing.assert_array_equal(phi,original)


def test_fixed_examples_refine_and_keep_common_observation_times(configs,measured):
    for key,case in measured.items():
        assert case['passed'] and all(case['checks'].values())
        for row in case['records']:
            assert [x['time'] for x in row['snapshots']]==configs[key]['snapshots']
            assert len(row['contours'])==5 and all(len(x)>10 for x in row['contours'])
            assert row['steps']>0 and row['maximum_courant']<=.35*(1+1e-12)
            assert row['state_clip_count']==row['volume_correction_count']==row['rejected_steps']==0


def test_redistance_schedule_and_area_jumps_are_measured_not_corrected(measured):
    for case in measured.values():
        for row in case['records']:
            if row['mode']=='redistance':
                assert row['redistance_calls']==10 and row['pseudo_steps']==50
                assert len(row['redistance_log'])==10
                for entry in row['redistance_log']:
                    assert entry['area_change']==entry['area_after']-entry['area_before']
                assert row['maximum_reinitialization_area_jump']>0
            else:assert row['redistance_calls']==0 and row['redistance_log']==[]


def test_rotation_checks_quarter_period_rather_than_only_the_return(measured):
    case=measured['level-set-rotation'];row=case['records'][2]
    initial=np.asarray(row['contours'][0]);quarter=np.asarray(row['contours'][1]);final=np.asarray(row['contours'][-1])
    assert np.linalg.norm(initial.mean(axis=0)-quarter.mean(axis=0))>.15
    assert np.linalg.norm(initial.mean(axis=0)-final.mean(axis=0))<.03


def test_field_is_numerically_advanced_instead_of_reset_to_the_reference(configs):
    config=configs['level-set-translation'];q,_=integrate(config,32,False,Budget(20))
    x,y=grid(32);reference=distance(config,x,y,1)
    assert np.max(np.abs(q-reference))>1e-5
    assert np.sqrt(np.mean((q-reference)**2))<.05


def test_budget_expiration_is_a_hard_failure(monkeypatch):
    budget=Budget(1);monkeypatch.setattr('level_set.time.monotonic',lambda:budget.deadline+1)
    with pytest.raises(RuntimeError,match='budget'):budget.check()


@pytest.mark.parametrize('key,value',[('time',float('nan')),('grids',[32,64,256]),('cfl',1),('pseudo_steps',500),('center',[.3,float('inf')]),('omega',100)])
def test_unbounded_or_unreviewed_input_is_rejected(configs,key,value):
    config=copy.deepcopy(configs['level-set-translation']);config[key]=value
    with pytest.raises(ValueError):validate(config)


def test_cli_rejects_incomplete_nonfinite_inputs_and_existing_output(tmp_path):
    from run import run
    path=tmp_path/'input.json';path.write_text('{"schema_version":1,"cases":{}}')
    with pytest.raises(ValueError,match='complete'):run(path,tmp_path/'output')
    path.write_text('{"x":NaN}')
    with pytest.raises(ValueError,match='Nonfinite'):run(path,tmp_path/'output')
    output=tmp_path/'existing';output.mkdir();(output/'keep').write_text('existing data')
    with pytest.raises(ValueError,match='empty'):run('inputs.json',output)
    assert (output/'keep').read_text()=='existing data'
