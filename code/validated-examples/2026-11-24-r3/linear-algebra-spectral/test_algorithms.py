import json
from pathlib import Path
import numpy as np
import pytest
import fixtures as F
import solvers as S
import run
from references import oracles as R


def test_lu_pivot_permutation_and_factor_reconstruction():
    a=np.array([[0.,2.,1.],[3.,1.,2.],[1.,0.,4.]]);u,p=S.lu_factor(a)
    assert p[0]==1
    np.testing.assert_allclose(S.mm(np.tril(u,-1)+np.eye(3),np.triu(u)),a[p],atol=1e-14)


def test_lu_solve_multiple_nontrivial_interchanges():
    a=np.array([[0.,0.,3.],[2.,0.,1.],[0.,4.,1.]]);x=np.array([1.,-2.,3.]);f=S.lu_factor(a)
    np.testing.assert_allclose(S.lu_solve(f,S.mv(a,x)),x,atol=1e-14)


def test_singular_pivot_is_failure_not_clipped():
    with pytest.raises(ArithmeticError,match='singular'):S.lu_factor(np.diag([1.,0.]))


def test_cholesky_reconstruction_and_forward_backward_substitution():
    a=np.array([[4.,2.,0.],[2.,5.,1.],[0.,1.,3.]]);l=S.cholesky(a)
    np.testing.assert_allclose(S.mm(l,l.T),a,atol=1e-14)
    np.testing.assert_allclose(S.chol_solve(l,np.array([6.,8.,4.])),np.ones(3),atol=1e-14)


def test_cholesky_rejects_nonsymmetry_and_negative_pivot():
    with pytest.raises(ValueError):S.cholesky(np.array([[1.,1.],[0.,1.]]))
    with pytest.raises(ArithmeticError):S.cholesky(np.diag([1.,-1.]))


def test_mixed_factor_dtype_is_explicit():
    a,b=F.direct_fixture('spd-tridiagonal');f=S.lu_factor(a,np.float32)
    assert f[0].dtype==np.float32 and S.lu_solve(f,b).dtype==np.float32


def test_refinement_preserves_all_fixed_candidate_updates():
    a,b=F.direct_fixture('spd-tridiagonal');saved=[];out=S.refine(a,b,'lu',3,lambda **v:saved.append({k:np.array(x,copy=True) for k,x in v.items()}))
    assert len(saved)==4 and out['history'].shape==(4,12)
    np.testing.assert_array_equal(saved[-1]['history'],out['history'])


def test_exact_binary_rational_reference():
    a=np.array([[.5,.25],[.125,.75]]);x=np.array([2.,-4.]);b=S.mv(a,x)
    np.testing.assert_array_equal(R.rational_solution(a,b),x)


def test_wilkinson_growth_is_independent_algebraic_golden():
    a,b=F.direct_fixture('wilkinson12');u,p=S.lu_factor(a)
    assert np.max(abs(np.triu(u)))==2048 and np.array_equal(p,np.arange(12))


def test_component_backward_zero_scale_is_defined():
    assert run.backward(np.eye(2),np.zeros(2),np.zeros(2))==(0.,0.)


def test_minres_accepts_indefinite_symmetric_system():
    a=np.diag([-2.,1.,4.]);b=np.array([1.,2.,3.]);out=S.krylov_linear(a,b,'minres',1e-11,3)
    assert out['converged'] and out['iterations']<=3
    np.testing.assert_allclose(S.mv(a,out['x']),b,atol=1e-11)


def test_spd_congruence_preserves_symmetry_and_solution():
    a=np.array([[2.,1.],[1.,-1.]]);b=np.array([1.,2.]);p=np.diag([4.,2.])
    out=S.krylov_linear(a,b,'minres',1e-11,2,p)
    assert out['converged'] and out['transform_symmetry']<1e-13
    np.testing.assert_allclose(S.mv(a,out['x']),b,atol=1e-11)


def test_minres_indefinite_preconditioner_is_rejected():
    with pytest.raises(ArithmeticError):S.krylov_linear(np.eye(2),np.ones(2),'minres',1e-8,2,np.diag([1.,-1.]))


def test_cg_negative_curvature_is_not_a_universal_minres_failure():
    with pytest.raises(ArithmeticError,match='SPD'):S.curvature_guard(np.diag([2.,-1.]),np.array([0.,1.]))


def test_arnoldi_two_pass_orthogonality_and_relation():
    a=np.array([[1.,2.,0.],[0.,3.,4.],[2.,0.,5.]]);q,h,_,happy=S.arnoldi(lambda x:S.mv(a,x),np.ones(3),2)
    np.testing.assert_allclose(S.mm(q.T,q),np.eye(2),atol=1e-13)
    np.testing.assert_allclose(S.mm(q.T,S.mm(a,q)),h[:2],atol=1e-13)


def test_exact_happy_breakdown_is_retained():
    q,h,calls,happy=S.arnoldi(lambda x:2*x,np.array([1.,0.,0.]),3)
    assert happy and calls==1 and q.shape==(3,1)


def test_restarted_shift_inverse_recovers_original_pair():
    a=np.diag([1.,3.,8.]);out=S.restarted_eigen(a,np.ones(3),3,2,1e-11,shift=2.5)
    assert out['converged'] and out['operator_calls']==3
    assert out['value']==pytest.approx(3.,abs=1e-11)
    assert np.max(out['shift_solve_residuals'])<2e-12


def test_shift_singularity_raises_before_operator_iterations():
    with pytest.raises(ArithmeticError):S.restarted_eigen(np.diag([1.,2.,3.]),np.ones(3),2,2,1e-9,shift=2.)


def test_inexact_shift_solution_guard_retains_candidate(monkeypatch):
    saved=[];real=S.lu_solve
    monkeypatch.setattr(S,'lu_solve',lambda f,b:real(f,b)+.1)
    with pytest.raises(ArithmeticError,match='shift solve'):S.restarted_eigen(np.diag([1.,2.,3.]),np.ones(3),2,2,1e-9,shift=.5,progress=lambda **x:saved.append(x))
    assert saved[-1]['stage']=='failed-shift-solve' and 'shift_candidate' in saved[-1]


def test_fem_element_assembly_consistent_mass():
    k,m,x=F.string_fem(3)
    np.testing.assert_array_equal(np.diag(k),np.full(3,8.))
    np.testing.assert_allclose(np.diag(m),np.full(3,1/6),atol=1e-16)
    assert m[0,1]==pytest.approx(1/24) and k[0,1]==-4.


def test_mass_krylov_uses_M_inner_product():
    k,m,x=F.string_fem(7);out=S.mass_krylov(k,m,1+x,7,3)
    q=out['basis'];np.testing.assert_allclose(S.mm(q.T,S.mm(m,q)),np.eye(q.shape[1]),atol=2e-12)
    np.testing.assert_allclose(out['values'],R.fem_spectrum(7,3),rtol=2e-11)


def test_generalized_residual_does_not_omit_mass_matrix():
    k,m,x=F.string_fem(7);values,vectors=R.dense_spectrum(k,m)
    residual,orth=run.eigen_metrics(k,m,values[:3],vectors[:,:3]);assert residual<2e-12 and orth<2e-12
    wrong,_=run.eigen_metrics(k,np.eye(7),values[:3],vectors[:,:3]);assert wrong>.1


def test_completed_factor_candidate_is_saved_before_diagnostic_failure(tmp_path,monkeypatch):
    def fail(*args):raise ArithmeticError('intentional diagnostic failure')
    monkeypatch.setattr(run,'backward',fail)
    with pytest.raises(ArithmeticError,match='intentional diagnostic'):run.direct_case({'fixtures':['spd-tridiagonal'],'corrections':1},{},tmp_path,run.fresh_case('fixture'))
    with np.load(tmp_path/'spd-tridiagonal-lu.npz',allow_pickle=False) as f:assert f['history'].shape==(2,12) and f['a'].shape==(12,12)


def test_actual_input_schema_and_limits_are_consistent():
    root=Path(__file__).resolve().parent;cfg=json.loads((root/'inputs.json').read_text());lim=json.loads((root/'acceptance.json').read_text())['limits']
    assert len(cfg['direct']['fixtures'])==4 and cfg['mass']['eigenpairs']==3
    assert cfg['saddle']['true_residual_tolerance']>0 and lim['direct_backward']>0


def test_roundoff_Schur_construction_is_exactly_symmetric_and_preserves_raw():
    raw=np.array([[2.,1.],[np.nextafter(1.,2.),2.]]);before=raw.copy()
    block,defect,bound=run.symmetric_schur(raw,12)
    np.testing.assert_array_equal(raw,before)
    assert np.array_equal(block,block.T) and 0<defect<bound
    S.cholesky(block) # strict exact-symmetry check remains active


def test_structural_Schur_asymmetry_is_rejected_instead_of_hidden():
    with pytest.raises(ArithmeticError,match='antisymmetry'):run.symmetric_schur(np.array([[2.,1.],[1.01,2.]]),12)


def test_fem_initial_block_avoids_polynomial_image_rank_loss_on_fixed_grids():
    # rank([K Z,M Z])-rank(Z) equals the search rank after projecting
    # K^-1 M Z out of Z, without forming the nearly singular old Gram.
    # Formation error uses gamma_(n+4) (dot products plus FEM assembly).
    # Add the standard n*eps*sigma_max SVD rank scale; no measured cutoff.
    eps=np.finfo(float).eps
    for n in [15,31,63]:
        k,m,x=F.string_fem(n)
        ranks=[]
        for z in [np.column_stack([np.ones(n),x,x*x]),run.fem_initial_block(x)]:
            kz,mz=S.mm(k,z),S.mm(m,z)
            block=np.column_stack([kz,mz])
            singular=np.linalg.svd(block,compute_uv=False)
            gamma=(n+4)*eps/(1-(n+4)*eps)
            absolute=np.column_stack([S.mm(abs(k),abs(z)),S.mm(abs(m),abs(z))])
            threshold=gamma*S.norm(absolute)+max(block.shape)*eps*singular[0]
            zsing=np.linalg.svd(z,compute_uv=False)
            assert np.count_nonzero(zsing>max(z.shape)*eps*zsing[0])==3
            ranks.append(int(np.count_nonzero(singular>threshold))-3)
        assert ranks==[2,3]
