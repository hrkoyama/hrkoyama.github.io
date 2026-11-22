"""Physical, algebraic, independent-reference and failure-path tests for H2 RHF."""
import json
from math import pi,sqrt
from pathlib import Path
import subprocess
import sys
import numpy as np
import pytest
from scipy.integrate import quad
from molecular_hf import (boys0,normalization,primitive_overlap,primitive_kinetic,
                         primitive_nuclear,primitive_eri,integrals,solve)
from run import calculate

ROOT=Path(__file__).parent
CONFIG=json.loads((ROOT/'inputs.json').read_text())
REF=json.loads((ROOT/'reference-pyscf.json').read_text())


@pytest.fixture(scope='module')
def result():return calculate(ROOT/'inputs.json')


@pytest.mark.parametrize('x',[0.,1e-10,1e-4,1.,40.])
def test_boys_against_independent_quadrature(x):
    reference=quad(lambda t:np.exp(-x*t*t),0,1,epsabs=1e-14)[0]
    assert abs(boys0(x)-reference)<3e-14


@pytest.mark.parametrize('a',[.3,1.1,3.5])
def test_normalized_one_centre_analytic_integrals(a):
    A=np.zeros(3);n=normalization(a)
    assert abs(n*n*primitive_overlap(a,A,a,A)-1)<2e-15
    assert abs(n*n*primitive_kinetic(a,A,a,A)-1.5*a)<1e-13
    assert abs(n*n*primitive_nuclear(a,A,a,A,A)+2*sqrt(2*a/pi))<1e-13
    assert abs(n**4*primitive_eri(a,A,a,A,a,A,a,A)-2*sqrt(a/pi))<1e-13


def test_integral_symmetries_and_independent_pyscf_spectra():
    for basis in CONFIG['basis_definitions']:
        S,T,V,eri=integrals(basis,1.4)
        np.testing.assert_allclose(eri,eri.transpose(1,0,2,3),atol=1e-14)
        np.testing.assert_allclose(eri,eri.transpose(0,1,3,2),atol=1e-14)
        np.testing.assert_allclose(eri,eri.transpose(2,3,0,1),atol=1e-14)
        ref=next(r for r in REF['cases'] if r['bond_bohr']==1.4 and r['basis_id']==basis['id'])
        # AO order can differ; spectra are invariant under a permutation of AOs.
        np.testing.assert_allclose(np.linalg.eigvalsh(S),ref['overlap_eigenvalues'],atol=1e-11,rtol=0)
        np.testing.assert_allclose(np.linalg.eigvalsh(T+V),ref['core_eigenvalues'],atol=1e-10,rtol=0)


def test_fixed_input_validation(result):
    assert len(result['cases'])==len(CONFIG['bonds_bohr'])*len(CONFIG['basis_definitions'])
    assert result['passed'] and all(result['checks'].values())
    for row in result['cases']:
        assert row['converged'] and row['termination']=='converged'
        assert row['energy_error']<2e-9
        assert row['scf_commutator_norm']<1e-9
        assert row['orthogonality_max']<1e-10
        assert row['error_electron_count']<1e-10
        assert row['idempotency_norm']<1e-9
        assert row['energy_consistency_error']<1e-10
        assert row['iterations']>5


def test_nested_variational_and_two_addition_stabilization(result):
    nested=[b for b in CONFIG['basis_definitions'] if b['family']=='nested-s-only']
    for a,b in zip(nested,nested[1:]):
        assert all(s in b['shells'] for s in a['shells'])
    for row in result['basis_refinement']:
        assert all(d<=1e-9 for d in row['energy_changes'])
        assert row['target_reached'] and row['last_two_changes_max']<=row['target']
    # The nuclear repulsion is not part of the electronic energy.
    for row in result['cases']:
        assert abs(row['energy_total']-row['energy_electronic']-1/row['bond_bohr'])<1e-13


def test_scf_tolerance_refinement_records_residual_and_energy(result):
    sweep=result['tolerance_sweep'];assert len(sweep)==3
    assert sweep[0]['energy_error_to_tight']<2e-6
    assert sweep[-1]['scf_commutator_norm']<1e-10
    assert sweep[-1]['energy_error_to_tight']<=sweep[0]['energy_error_to_tight']


def test_linear_dependence_is_rejected_without_basis_deletion():
    basis={'id':'duplicate','shells':[{'exponents':[1.],'coefficients':[1.]}]*2}
    with pytest.raises(ValueError,match='no basis function is discarded'):solve(basis,1.4,CONFIG['scf'])


def test_unconverged_iteration_has_explicit_stop_reason():
    row=solve(CONFIG['basis_definitions'][0],1.4,{**CONFIG['scf'],'max_cycles':1})
    assert row['termination']=='max_cycles' and not row['converged']
    assert row['trace'][0]['delta_energy'] is None
    assert row['scf_commutator_norm']>CONFIG['scf']['residual_tolerance']


def test_two_controlled_initial_guesses_reach_same_rhf_state():
    basis=CONFIG['basis_definitions'][2]
    rows=[solve(basis,1.4,{**CONFIG['scf'],'initial_rotation':angle}) for angle in [.05,.3]]
    assert all(row['converged'] for row in rows)
    assert abs(rows[0]['energy_total']-rows[1]['energy_total'])<1e-10


@pytest.mark.parametrize('update',[{'max_cycles':0},{'mixing':0},{'residual_tolerance':-1}])
def test_invalid_scf_controls_fail(update):
    with pytest.raises(ValueError):solve(CONFIG['basis_definitions'][0],1.4,{**CONFIG['scf'],**update})


def test_cli_writes_finite_numeric_csv_and_results(tmp_path):
    out=tmp_path/'output';run=subprocess.run([sys.executable,str(ROOT/'run.py'),'--input',str(ROOT/'inputs.json'),'--output',str(out)],capture_output=True,text=True)
    assert run.returncode==0,run.stderr
    assert json.loads((out/'result.json').read_text())['passed']
    for filename in ['solution.csv','scf.csv']:
        values=np.genfromtxt(out/filename,delimiter=',',skip_header=1)
        assert np.isfinite(values).all()


def test_cli_preserves_failed_calculation_and_existing_output(tmp_path):
    out=tmp_path/'failed';argv=[sys.executable,str(ROOT/'run.py'),'--input',str(ROOT/'inputs.json'),'--output',str(out),'--max-cycles','1']
    run=subprocess.run(argv,capture_output=True,text=True);assert run.returncode==1,run.stderr
    result=json.loads((out/'result.json').read_text());assert result['termination']=='scf_not_converged' and not result['passed']
    before=(out/'result.json').read_bytes();run=subprocess.run(argv,capture_output=True)
    assert run.returncode==2 and (out/'result.json').read_bytes()==before
