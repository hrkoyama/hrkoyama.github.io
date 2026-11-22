"""Scientific controls, independent-reference guards and bounded-input contracts."""
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time

import numpy as np
import pytest
from scipy import linalg,sparse
import experiments as ex
from fixtures import decomposition_fixture,hadamard,symmetric_fixture
from run import Budget,execute,validate_input
from solvers import adaptive_simpson,arnoldi,back_substitute,householder_qr,jacobi_svd,lanczos,matrix_product,matrix_vector,smoothed_aggregation,solve_amg

HERE=Path(__file__).resolve().parent


@pytest.fixture(scope='module')
def results(tmp_path_factory):
    return execute(json.loads((HERE/'inputs.json').read_text()),tmp_path_factory.mktemp('conditioning-results'))


@pytest.mark.parametrize('identifier',['amg-conditioning','qr-svd-conditioning','krylov-eigen-conditioning','quadrature-conditioning'])
def test_predeclared_case_passes_without_dropping_checks(results,identifier):
    case=next(c for c in results['cases'] if c['id']==identifier)
    assert case['passed'] and len(case['checks'])>=20 and all(case['checks'].values())


def test_amg_separates_condition_and_anisotropy(results):
    rows=results['cases'][0]['records']
    for n in [7,15,31]:
        family=[r for r in rows if r['n']==n]
        assert len(family)==3 and len({r['condition_2_analytic'] for r in family})==1
        assert all(r['sparse_direct_vs_dst']<1e-12 for r in family)
    assert rows[-1]['condition_2_analytic']>10*rows[0]['condition_2_analytic']


def test_amg_history_true_residual_and_short_failure(results):
    case=results['cases'][0]
    for row in case['records']:
        history=[v for v in case['residual_histories'] if v['n']==row['n'] and v['epsilon']==row['epsilon']]
        assert len(history)==row['cycles']+1 and history[0]['relative_residual']==1.
        assert abs(history[-1]['relative_residual']-row['relative_residual'])<2e-13
    assert case['short_budget']['converged'] is False


@pytest.mark.parametrize('q',[0,4,8,12])
def test_exact_input_has_prescribed_binary_rhs_and_independent_reference(q):
    a,b,bp,s,u,v=decomposition_fixture(q)
    reference=ex.load_reference()['datasets']['q'+str(q)]
    assert np.array_equal(matrix_vector(a,v[:,0]),b)
    assert s[0]/s[-1]==2.**(3*q)
    np.testing.assert_allclose([float(x) for x in reference['singular_values']],s,rtol=1e-15)
    np.testing.assert_array_equal(bp,b+2.**-40*u[:,-1])


def test_rank_truncation_changes_problem_and_is_labelled(results):
    case=results['cases'][1];cut=[r for r in case['records'] if r['kind']=='rank-cutoff']
    assert [r['rank'] for r in cut]==[3,4,4]
    assert cut[0]['bias_to_untruncated_solution']>1e-2
    assert case['rank_deficient_control']['rank']==2
    assert case['sweep_budget_control']['converged'] is False


def test_ill_conditioned_small_backward_error_does_not_hide_forward_error(results):
    rows=[r for r in results['cases'][1]['records'] if r['kind']=='prescribed-spectrum']
    # Lower bounds on accidental rounding error are not portable. Sensitivity
    # is established by the independently known, fixed RHS perturbation.
    assert rows[-1]['predicted_perturbation_solution_norm']==.0625
    assert rows[-1]['perturbation_projection_absolute_error']<.01
    assert rows[-1]['qr_reconstruction']<1e-12
    assert all(r['maximum_relative_forward_error']<=r['forward_acceptance_budget'] for r in rows)


@pytest.mark.parametrize('gap',[1.,.1,.01])
def test_cluster_projectors_and_reference_construction(gap):
    a,spectrum,q=symmetric_fixture(48,gap)
    np.testing.assert_allclose(linalg.eigvalsh(a),spectrum,atol=1e-12)
    np.testing.assert_allclose(matrix_product(q.T,q),np.eye(48),atol=2e-14)
    p=matrix_product(q[:,-2:],q[:,-2:].T)
    # A rotation in the cluster changes columns but not its projector.
    rotated=matrix_product(q[:,-2:],np.array([[0.,-1.],[1.,0.]]))
    np.testing.assert_allclose(matrix_product(rotated,rotated.T),p,atol=2e-14)


def test_nonnormal_small_residual_control_is_constructed(results):
    rows=[r for r in results['cases'][2]['records'] if r['kind']=='constructed-pseudoeigenpair']
    assert rows[-1]['absolute_residual']<1e-6 and rows[-1]['eigenvalue_error']>.004
    assert 'not a solver-produced' in rows[-1]['status']
    assert rows[-1]['eigenvalue_condition']>1e4


def test_quadrature_hidden_bump_and_endpoint_are_honest(results):
    case=results['cases'][3];rows=case['records']
    blind=next(r for r in rows if r['kind']=='compact-bump-blind')
    split=next(r for r in rows if r['kind']=='compact-bump-split')
    assert blind['solver_converged'] and blind['estimated_error']==0 and blind['absolute_error']>.001
    assert split['absolute_error']<5e-9
    assert any(r['status']=='depth_budget' and not r['solver_converged'] for r in rows if r['kind']=='endpoint-direct')
    assert all(r['status']=='completed' and r['message'] is None for r in case['independent_quadpack'])


def test_zero_integral_condition_is_undefined_and_cancellation_budget_scales(results):
    rows=results['cases'][3]['records'];zero=next(r for r in rows if r['kind']=='zero-integral')
    assert zero['relative_condition'] is None
    cancel=[r for r in rows if r['kind']=='cancellation']
    assert cancel[-1]['roundoff_acceptance_budget']>1e-4
    assert abs(cancel[-1]['observed_integral_change']/cancel[-1]['predicted_integral_change']-1)<.05


@pytest.fixture
def reference_copy(tmp_path,monkeypatch):
    for name in ['reference.json','reference-input.json','fixtures.py','inputs.json','mpmath_reference.py']:
        shutil.copyfile(HERE/name,tmp_path/name)
    monkeypatch.setattr(ex,'HERE',tmp_path)
    return tmp_path


def tamper(path,monkeypatch,change):
    data=json.loads((path/'reference.json').read_text());change(data)
    payload=json.dumps(data).encode();(path/'reference.json').write_bytes(payload)
    # Bypass whole-file guard to exercise semantic guards independently.
    monkeypatch.setattr(ex,'REFERENCE_SHA256',hashlib.sha256(payload).hexdigest())


@pytest.mark.parametrize('change',[
    lambda d:d['results'].pop(),
    lambda d:d['results'].append(copy.deepcopy(d['results'][0])),
    lambda d:d['results'][0].update(id='q3'),
    lambda d:d['results'][0].update(exponent=12),
    lambda d:d['results'][0]['runs'].pop(0),
    lambda d:d['results'][0]['runs'][0].update(dps=120),
    lambda d:d['results'][0]['runs'][0]['singular_values'].__setitem__(0,'0'),
    lambda d:d['results'][0]['runs'][0]['solution'].__setitem__(0,'NaN'),
    lambda d:d['results'][0]['runs'][1]['solution'].pop(),
    lambda d:d['results'][0]['runs'][1].update(condition_2='Infinity'),
    lambda d:d['results'][0]['array_sha256'].update(matrix='0'*64),
    lambda d:d.update(reference_input_sha256='0'*64),
    lambda d:d.update(fixture_recipe_sha256='0'*64),
    lambda d:d.update(protocol_sha256='0'*64),
    lambda d:d.update(generator_sha256='0'*64),
    lambda d:d.update(all_reference_checks_passed=False),
])
def test_independent_reference_never_silently_falls_back(reference_copy,monkeypatch,change):
    tamper(reference_copy,monkeypatch,change)
    with pytest.raises((ValueError,KeyError,TypeError)):ex.load_reference()


def test_reference_whole_file_hash(reference_copy):
    with (reference_copy/'reference.json').open('a') as stream:stream.write(' ')
    with pytest.raises(ValueError,match='SHA'):ex.load_reference()


@pytest.mark.parametrize('value',[0,-1,111,float('inf'),float('nan'),True])
def test_runtime_budget_rejects_unbounded_or_invalid(value):
    with pytest.raises(ValueError):Budget(value)


def test_runtime_expiration_is_not_silent():
    budget=Budget(1);budget.start=time.monotonic()-2
    with pytest.raises(TimeoutError):budget.check()


@pytest.mark.parametrize('change',[
    lambda d:d['amg']['grid_sizes'].append(100000),
    lambda d:d['quadrature'].update(max_evaluations=10**9),
    lambda d:d['decompositions']['acceptance'].update(reconstruction=1),
    lambda d:d['krylov'].update(seed=True),
])
def test_fixed_input_cannot_redefine_acceptance_or_allocate_unbounded(change):
    data=json.loads((HERE/'inputs.json').read_text());change(data)
    with pytest.raises(ValueError):validate_input(data)


def test_previous_results_cannot_be_overwritten(tmp_path):
    (tmp_path/'keep').write_text('saved evidence')
    with pytest.raises(ValueError,match='retained'):execute(json.loads((HERE/'inputs.json').read_text()),tmp_path)
    assert (tmp_path/'keep').read_text()=='saved evidence'


def test_download_cli_and_release_report_contract(tmp_path):
    output=tmp_path/'cli-results'
    process=subprocess.run([sys.executable,'-W','error',str(HERE/'run.py'),'--input',str(HERE/'inputs.json'),'--output',str(output)],capture_output=True,text=True,timeout=110)
    assert process.returncode==0,process.stdout+process.stderr
    report=json.loads((output/'result.json').read_text())
    assert report['passed'] is True and report['termination']=='fixed_inputs_completed'
    assert report['checks']=={c['id']:True for c in report['cases']}
    assert report['input_sha256']==hashlib.sha256((HERE/'inputs.json').read_bytes()).hexdigest()
    assert report['duration_seconds']>=0
    assert len(list(output.glob('*.csv')))==5


def test_budget_and_shape_failures_of_scientific_kernels():
    a,b,*_=decomposition_fixture(4)
    assert not jacobi_svd(a,max_sweeps=0)[-1]['converged']
    with pytest.raises(ValueError):back_substitute(np.zeros((2,2)),np.ones(2))
    with pytest.raises(ValueError):lanczos(np.array([[1.,2.],[0.,1.]]),np.ones(2),2)
    with pytest.raises(ValueError):arnoldi(np.eye(2),np.zeros(2),2)
    answer=adaptive_simpson(np.exp,0.,1.,1e-16,max_evaluations=5)
    assert not answer['converged'] and answer['termination']=='evaluation_budget'
