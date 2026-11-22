"""Numerical and provenance checks for this fixed, library-backed workflow."""
import copy
import csv
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import numpy as np
import pytest

from periodic_dft import fractional_points, solve
from run import summarize, validate_reference, write_outputs

ROOT=Path(__file__).resolve().parent


@pytest.fixture(scope='session')
def evidence():
    return tuple(json.loads((ROOT/name).read_text()) for name in ['inputs.json','reference-dftk.json','results/result.json'])


def test_fixed_input_validation(evidence):
    """Re-evaluate all recorded cases and criteria, not the saved success flag."""
    config,reference,saved=evidence
    assert len(saved['cases'])==11
    assert [r['id'] for r in saved['cases']]==[r['id'] for r in config['cases']]
    actual=summarize(config,saved['cases'],reference,saved['input_sha256'],saved['reference_sha256'])
    assert actual['passed'] and all(actual['checks'].values())
    assert actual['metrics']==saved['metrics']
    assert saved['input_sha256']==hashlib.sha256((ROOT/'inputs.json').read_bytes()).hexdigest()
    assert saved['reference_sha256']==hashlib.sha256((ROOT/'reference-dftk.json').read_bytes()).hexdigest()
    assert all(r['ao_count']>=2 and r['sampled_ks_gap']>0 for r in actual['cases'])


@pytest.fixture(scope='session')
def live_gamma(evidence):
    config,_,_=evidence
    return solve(config,config['cases'][0])


def test_live_gamma_independent_energy_and_residuals(evidence,live_gamma):
    config,reference,_=evidence
    ref=next(r for r in reference['comparisons'] if r['k_n']==1)
    assert live_gamma['converged']
    assert abs(live_gamma['energy_per_cell']-ref['energy_per_cell'])<config['acceptance']['reference_energy_difference']
    assert live_gamma['scf_commutator_norm']<1e-5
    assert live_gamma['orbital_residual_norm']<1e-5
    assert live_gamma['electron_count_error']<1e-8
    assert live_gamma['orthogonality_error']<1e-8
    assert live_gamma['energy_reconstruction_error']<1e-8
    assert live_gamma['sampled_ks_gap']>0.1
    assert live_gamma['overlap_min_eigenvalue']>config['overlap_eigenvalue_floor']


def test_single_cycle_reports_nonconvergence(evidence):
    config,_,_=evidence
    spec={**config['cases'][0],'basis':'gth-dzv','fft_n':25,'max_cycles':1}
    failed=solve(config,spec)
    assert not failed['converged'] and failed['termination']=='maximum_cycles'
    assert failed['iterations']==1
    assert np.isfinite(failed['energy_per_cell'])


@pytest.mark.parametrize('n',[1,2,3,4])
def test_explicit_k_mesh_has_distinct_product_points(n,evidence):
    config,_,_=evidence
    points=fractional_points(n)
    assert len(set(map(tuple,points)))==n**3
    assert np.array_equal(points,np.asarray(config['kpoint_meshes'][str(n)]))
    assert np.array_equal(points[0],[0.,0.,0.])


def test_correlated_coordinate_set_cannot_replace_product_mesh(evidence):
    config,_,_=copy.deepcopy(evidence)
    # Each individual coordinate has the right multiset, but the triples do not.
    config['kpoint_meshes']['2']=[[0.,0.,0.]]*4+[[.5,.5,.5]]*4
    with pytest.raises(ValueError,match='mesh'):
        solve(config,config['cases'][1])


@pytest.mark.parametrize('tolerance',[0.,float('nan')])
def test_invalid_scf_tolerance_rejected(tolerance,evidence):
    config,_,_=evidence
    with pytest.raises(ValueError,match='tolerances'):
        solve(config,{**config['cases'][0],'energy_tolerance':tolerance})


def test_actual_xc_string_is_bound_to_reference_model(evidence):
    config,reference,_=copy.deepcopy(evidence)
    config['xc']['pyscf']='LDA_X'
    with pytest.raises(ValueError,match='XC pair'):
        validate_reference(config,reference)
    with pytest.raises(ValueError,match='XC pair'):
        solve(config,config['cases'][0])


@pytest.mark.parametrize('corruption',['cell','xc','offset','weights','final_energy','failed_scf','missing_cutoff','nan_electrons','nan_component'])
def test_independent_reference_rejects_inconsistent_evidence(corruption,evidence):
    config,reference,_=copy.deepcopy(evidence)
    if corruption=='cell':reference['cell']['lattice_bohr'][0][0]+=0.1
    if corruption=='xc':reference['xc']=['lda_x']
    if corruption=='offset':reference['energy_offset_applied']=0.01
    if corruption=='weights':reference['comparisons'][1]['kpoint_weights'][0]=0.5
    if corruption=='final_energy':reference['comparisons'][0]['energy_per_cell']+=0.01
    if corruption=='failed_scf':reference['cutoff_convergence']['records'][0]['converged']=False
    if corruption=='missing_cutoff':reference['cutoff_convergence']['records'].pop()
    if corruption=='nan_electrons':reference['cutoff_convergence']['records'][0]['electron_count']=float('nan')
    if corruption=='nan_component':reference['cutoff_convergence']['records'][0]['energy_components']['Kinetic']=float('nan')
    with pytest.raises(ValueError):validate_reference(config,reference)


def test_cutoff_acceptance_is_recomputed_from_energies(evidence):
    config,reference,_=copy.deepcopy(evidence)
    reference['cutoff_convergence']['target_reached']=False
    assert validate_reference(config,reference) # Saved flag has no authority.
    r=[r for r in reference['cutoff_convergence']['records'] if r['k_n']==1][-2]
    r['energy_per_cell']+=0.01
    r['energy_components']['AtomicLocal']+=0.01
    reference['cutoff_convergence']['target_reached']=True
    assert not validate_reference(config,reference)


def test_failed_scf_cannot_produce_a_successful_summary(evidence):
    config,reference,saved=copy.deepcopy(evidence)
    saved['cases'][0]['converged']=False
    actual=summarize(config,saved['cases'],reference,'input','reference')
    assert not actual['passed'] and not actual['checks']['all_scf_converged']
    assert actual['termination']=='scf_not_converged'


@pytest.mark.parametrize('field,check,value',[('overlap_condition_max','overlap_condition',1e15),('scf_commutator_norm','tight_scf_residual',0.1)])
def test_unacceptable_state_diagnostic_prevents_success(field,check,value,evidence):
    config,reference,saved=copy.deepcopy(evidence)
    saved['cases'][0][field]=value
    actual=summarize(config,saved['cases'],reference,'input','reference')
    assert not actual['passed'] and not actual['checks'][check]


def test_csv_is_numeric_and_keeps_every_case_and_iteration(evidence,tmp_path):
    config,_,saved=evidence
    write_outputs(tmp_path,saved,config)
    for name,expected in [('solution.csv',11),('scf.csv',sum(len(r['trace']) for r in saved['cases']))]:
        with (tmp_path/name).open() as f:rows=list(csv.reader(f))
        assert len(rows)-1==expected
        assert np.isfinite(np.asarray(rows[1:],dtype=float)).all()


def test_independent_artifact_hashes_match_provenance(evidence):
    _,reference,_=evidence
    for key,path in [('script_sha256','reference.jl'),('pseudopotential_sha256','He.gth'),('project_sha256','reference-environment/Project.toml'),('manifest_sha256','reference-environment/Manifest.toml'),('input_sha256','inputs.json')]:
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==reference[key]
    assert 'periodic_dft' not in (ROOT/'reference.jl').read_text()


def test_existing_output_is_not_overwritten(tmp_path):
    marker=tmp_path/'keep.txt';marker.write_text('preserve')
    completed=subprocess.run([sys.executable,str(ROOT/'run.py'),'--input',str(ROOT/'inputs.json'),'--output',str(tmp_path)],capture_output=True,text=True)
    assert completed.returncode==2 and 'new or empty' in completed.stderr
    assert marker.read_text()=='preserve'
