"""Scientific contracts: full saved run plus actual small electronic calculations.

The release builder separately re-executes the entire registered run, so these
checks never rerun thirteen sweeps for each individual pytest assertion.
"""
import copy
import json
from pathlib import Path
import numpy as np
import pytest
from periodic_forces import solve, energy_and_forces, require_converged, fractional_points, validate_model
from bomd import velocity_verlet_step
from run import validate_reference, summarize, sha

ROOT=Path(__file__).resolve().parent
@pytest.fixture(scope='module')
def config():return json.loads((ROOT/'inputs.json').read_text())
@pytest.fixture(scope='module')
def result():return json.loads((ROOT/'results/result.json').read_text())
@pytest.fixture(scope='module')
def reference():return json.loads((ROOT/'reference-dftk.json').read_text())


def test_saved_full_run_passes(result):
    assert result['passed'] and all(result['checks'].values())
    assert len(result['cases'])==13
    assert result['input_sha256']==sha(ROOT/'inputs.json')
    assert result['reference_sha256']==sha(ROOT/'reference-dftk.json')


def test_all_six_nonzero_forces_have_energy_derivatives(result):
    fd=result['finite_difference'];records=fd['components']
    assert {(r['atom'],r['axis']) for r in records}=={(i,j) for i in range(2) for j in range(3)}
    assert all(abs(r['force_analytic'])>.01 for r in records)
    assert fd['max_component_error']<2e-6
    for r in records:
        assert r['force_finite_difference']==pytest.approx(-(r['energy_plus']-r['energy_minus'])/(2*r['step_bohr']),abs=1e-12)


def test_displacement_scan_resolves_truncation_error(result):
    scan=result['finite_difference']['steps']
    assert [r['step_bohr'] for r in scan]==[.008,.004,.002]
    assert scan[-1]['absolute_error']<scan[0]['absolute_error']
    assert scan[0]['absolute_error']<1e-5


def test_each_force_convergence_is_measured(config,result):
    for name,group in result['convergence'].items():
        assert group['case_ids']==config['convergence_groups'][name]
        assert group['last_change']<=group['target']
        assert group['last_change']==pytest.approx(np.max(np.abs(np.asarray(group['forces_cartesian'][-1])-group['forces_cartesian'][-2])))
    # Gamma is visibly inadequate for this force; it cannot be advertised as
    # interchangeable with the k-mesh result merely because each SCF converged.
    assert result['convergence']['kpoint']['adjacent_changes'][0]>.01


def test_independent_gaussian_planewave_force_comparison(result):
    comparisons=result['independent_comparison']['cases']
    assert {r['k_n'] for r in comparisons}=={1,2}
    assert all(r['max_absolute_force_difference']<2e-4 and r['energy_absolute_difference']<2e-4 for r in comparisons)
    assert all(r['case_id'].endswith('gth-qzv3p') for r in comparisons)


def test_grid_translation_balance(result):
    indexed={r['id']:r for r in result['cases']}
    assert indexed['fft-31']['net_force_max']>indexed['fft-47']['net_force_max']
    assert indexed['fft-47']['net_force_max']<1e-7


def test_actual_bo_interface_smoke_is_scoped(result):
    b=result['bomd']
    assert len(b['electronic_force_evaluations'])==3
    assert all(r['converged'] for r in b['electronic_force_evaluations'])
    assert b['position_max_difference']<1e-6
    assert b['full_step_energy_defect']<1e-6
    assert b['two_half_steps_energy_defect']<1e-6
    assert 'not a long-time NVE' in b['scope']


def test_recalculate_all_acceptance(config,result,reference):
    new=summarize(config,result['cases'],result['finite_difference'],result['bomd'],reference,result['input_sha256'],result['reference_sha256'])
    assert new['checks']==result['checks'] and new['passed']


@pytest.mark.parametrize('mutation',[lambda r:r.update(energy_offset_applied=1),lambda r:r.update(force_unit='eV/angstrom'),lambda r:r['cell'].update(charge=2),lambda r:r.update(script_sha256='0'*64)])
def test_reject_incompatible_independent_model(config,reference,mutation):
    altered=copy.deepcopy(reference);mutation(altered)
    with pytest.raises(ValueError):validate_reference(config,altered)


def test_reject_independent_force_nan(config,reference):
    altered=copy.deepcopy(reference);altered['comparisons'][0]['forces_cartesian'][0][0]=float('nan')
    with pytest.raises(ValueError):validate_reference(config,altered)


def test_reject_independent_density_nan(config,reference):
    altered=copy.deepcopy(reference);altered['cutoff_convergence']['records'][0]['electron_count']=float('nan')
    with pytest.raises(ValueError):validate_reference(config,altered)


def test_reject_wrong_independent_weight(config,reference):
    altered=copy.deepcopy(reference);altered['comparisons'][1]['kpoint_weights'][0]+=.01
    with pytest.raises(ValueError):validate_reference(config,altered)


def test_do_not_trust_cutoff_pass_flag(config,reference):
    altered=copy.deepcopy(reference);records=altered['cutoff_convergence']['records']
    first=next(r for r in records if r['k_n']==1 and r['ecut_hartree']==180)
    first['forces_cartesian'][0][0]+=.01
    assert not validate_reference(config,altered)['passed']


def test_reject_forged_reference_finite_difference(config,reference):
    altered=copy.deepcopy(reference);altered['finite_difference']['records'][0]['energy_plus']+=.1
    with pytest.raises(ValueError):validate_reference(config,altered)


@pytest.mark.parametrize('n',[1,2,3,4])
def test_mesh_count_and_weights(n):
    points=fractional_points(n)
    assert points.shape==(n**3,3)
    assert len(set(map(tuple,points)))==n**3
    assert [0,0,0] in points.tolist()


def test_unregistered_geometry_rejected(config):
    with pytest.raises(ValueError):validate_model(config,[[0,0,0],[0,0,0]])
    with pytest.raises(ValueError):validate_model(config,[[0,0,0],[float('nan'),0,0]])


def test_scf_failure_is_not_a_usable_bo_force(config):
    # An actual one-cycle electronic solve must remain a failure even when it
    # returns finite energy; a mock convergence flag cannot establish this.
    spec=copy.deepcopy(config['cases'][0]);spec.update(basis='gth-dzv',fft_n=25,max_cycles=1)
    row=solve(config,spec,with_forces=False)
    assert not row['converged']
    with pytest.raises(RuntimeError):require_converged(row)


def test_nonfinite_scf_residual_rejected():
    with pytest.raises(RuntimeError):require_converged(dict(converged=True,scf_commutator_norm=float('nan'),forces_cartesian=[[0]*3]*2))


def harmonic_callback(r):
    return dict(converged=True,energy_per_cell=float(.5*np.sum(r*r)),forces_cartesian=(-r).tolist(),positions_bohr=r.tolist())


def integrate_harmonic(dt):
    r=np.array([[1.,0,0]]);v=np.zeros_like(r)
    for _ in range(round(1/dt)):
        step=velocity_verlet_step(harmonic_callback,r,v,[1.],dt)
        r=np.asarray(step['positions_bohr']);v=np.asarray(step['velocities_bohr_per_atomic_time'])
    return r[0,0],v[0,0]


def test_verlet_second_order_against_exact_oscillator():
    errors=[abs(integrate_harmonic(dt)[0]-np.cos(1.)) for dt in [.1,.05,.025]]
    assert 3.9<errors[0]/errors[1]<4.1
    assert 3.9<errors[1]/errors[2]<4.1


def test_verlet_rejects_unconverged_force():
    with pytest.raises(RuntimeError):velocity_verlet_step(lambda r:dict(converged=False),[[0.,0,0]],[[0.,0,0]],[1.],.1)


def test_verlet_rejects_stale_force():
    initial=harmonic_callback(np.array([[1.,0,0]]))
    with pytest.raises(ValueError):velocity_verlet_step(harmonic_callback,[[2.,0,0]],[[0.,0,0]],[1.],.1,initial_record=initial)


@pytest.mark.parametrize('mass,dt',[(0,.1),(-1,.1),(1,0),(1,float('nan'))])
def test_verlet_invalid_units_values(mass,dt):
    with pytest.raises(ValueError):velocity_verlet_step(harmonic_callback,[[0.,0,0]],[[0.,0,0]],[mass],dt)


def test_successful_force_api_against_actual_displaced_energies(config):
    spec=copy.deepcopy(config['cases'][0]);spec.update(basis='gth-dzv',fft_n=31)
    positions=np.asarray(config['cell']['positions_bohr']);row=energy_and_forces(config,spec,positions)
    energies=[];h=.002
    for sign in [-1,1]:
        moved=positions.copy();moved[1,0]+=sign*h
        state=solve(config,spec,moved,with_forces=False);require_converged(state);energies.append(state['energy_per_cell'])
    assert row['converged']
    assert row['forces_cartesian'][1][0]==pytest.approx(-(energies[1]-energies[0])/(2*h),abs=2e-6)


def test_reject_failed_independent_displaced_scf(config,reference):
    altered=copy.deepcopy(reference);altered['finite_difference']['records'][0]['displaced_records'][0]['converged']=False
    with pytest.raises(ValueError):validate_reference(config,altered)


def test_reject_nonfinite_independent_displaced_scf(config,reference):
    altered=copy.deepcopy(reference);altered['finite_difference']['records'][0]['displaced_records'][0]['density_residual']=float('nan')
    with pytest.raises(ValueError):validate_reference(config,altered)


def test_reject_independent_nominal_geometry_change(config,reference):
    altered=copy.deepcopy(reference);altered['comparisons'][0]['positions_bohr'][0][0]+=.01
    with pytest.raises(ValueError):validate_reference(config,altered)


def test_reject_negative_independent_residual(config,reference):
    altered=copy.deepcopy(reference);altered['cutoff_convergence']['records'][0]['density_residual']=-1e-9
    with pytest.raises(ValueError):validate_reference(config,altered)
