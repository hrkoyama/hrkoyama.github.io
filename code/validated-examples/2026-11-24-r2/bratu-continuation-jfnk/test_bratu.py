import json
from pathlib import Path
import numpy as np
import pytest
from dual import Dual
import problem
from problem import residual,laplace,analytic_jv,poisson_inverse,norm,l2,arc_norm,weighted_arc_dot
from continuation import tangent_at,arc_correct,fold_equations,fold_jacobian,fixed_lambda
from matrix_free import Evaluator,gmres,inexact_newton
from references.analytic_family import reference
from io_contract import Case,numeric_csv

SETTINGS=json.loads((Path(__file__).parent/'inputs.json').read_text())['jfnk']['settings']


def test_quadratic_Dirichlet_stencil():
    x=np.arange(1,16)/16;np.testing.assert_allclose(laplace(x*(1-x)),2,rtol=0,atol=2e-14)


def test_discrete_sine_eigenvalue():
    x=np.arange(1,16)/16;v=np.sin(3*np.pi*x);e=4*16**2*np.sin(3*np.pi/32)**2
    np.testing.assert_allclose(laplace(v),e*v,rtol=0,atol=5e-13)


def test_dual_residual_same_primal_expression():
    x=np.arange(1,8)/8;u=.3*np.sin(np.pi*x);v=np.cos(2*np.pi*x)
    np.testing.assert_allclose(residual(Dual(u,v),2.).value,residual(u,2.),rtol=0,atol=1e-13)


def test_forward_AD_Jv_vs_analytic_direction():
    x=np.arange(1,16)/16;u=.3*np.sin(np.pi*x);v=np.cos(2*np.pi*x)
    np.testing.assert_allclose(residual(Dual(u,v),2.).tangent,analytic_jv(u,2.,v),rtol=0,atol=2e-13)


def test_zero_direction_needs_no_FD_division():
    ev=Evaluator(2.,'central-fd');np.testing.assert_array_equal(ev.operator(np.zeros(7),np.zeros(7)),0)
    assert ev.counts['jv']==ev.counts['zero_jv']==1 and ev.counts['primal_residual']==0


def test_central_FD_Jv_qualifies_against_analytic():
    x=np.arange(1,16)/16;u=.3*np.sin(np.pi*x);v=np.cos(2*np.pi*x);ev=Evaluator(2.,'central-fd')
    assert norm(ev.operator(u,v)-analytic_jv(u,2.,v))/norm(analytic_jv(u,2.,v))<2e-7


def test_actual_FD_evaluation_count_is_two_per_nonzero_Jv():
    ev=Evaluator(2.,'central-fd');ev.operator(np.zeros(7),np.ones(7));assert ev.counts['primal_residual']==2 and ev.counts['jv']==1


def test_actual_AD_evaluation_count_is_one_directional_traversal():
    ev=Evaluator(2.,'forward-ad');ev.operator(np.zeros(7),np.ones(7));assert ev.counts['dual_residual']==1 and ev.counts['primal_residual']==0


def test_Poisson_preconditioner_solves_its_declared_operator():
    b=np.sin(np.arange(1,16));np.testing.assert_allclose(laplace(poisson_inverse(b)),b,rtol=0,atol=3e-13)


def test_continuous_family_has_second_order_discrete_consistency():
    errors=[]
    for n in [15,31,63]:
        r=reference(n,theta=1);errors.append(l2(residual(r['u'][1:-1],r['lam'])))
    assert all(3.5<errors[k]/errors[k+1]<4.5 for k in [0,1])


def test_Decimal80_family_endpoints_and_ODE_are_independently_qualified():
    r=reference(15,theta=2.);assert r['u'][0]==r['u'][-1]==0 and np.max(abs(r['ode_residual']))<1e-60


def test_independent_fixed_lambda_lower_and_upper_are_distinct():
    lo=reference(15,lam=2.,branch='lower');up=reference(15,lam=2.,branch='upper')
    assert abs(lo['lam']-2)<2e-14 and abs(up['lam']-2)<2e-14 and up['u'][8]>lo['u'][8]+1


def test_reference_fold_matches_published_rounded_anchor():
    r=reference(7,theta=1);assert abs(r['fold_lambda']-3.513830719)<1e-8


def test_initial_weighted_tangent_matches_poisson_sensitivity():
    n=15;t=tangent_at(np.zeros(n+1));x=np.arange(1,n+1)/(n+1)
    np.testing.assert_allclose(t[:-1]/t[-1],x*(1-x)/2,rtol=0,atol=2e-15);assert abs(arc_norm(t)-1)<2e-15


def test_corrector_satisfies_F_and_hyperplane():
    t=tangent_at(np.zeros(8));predict=.1*t;z,h,states=arc_correct(predict,t,1e-10,12)
    assert l2(residual(z[:-1],z[-1]))<1e-10 and abs(weighted_arc_dot(z-predict,t))<1e-12


def test_fold_system_Jacobian_direction_is_correct():
    n=7;x=np.arange(1,n+1)/(n+1);w=np.r_[np.sin(np.pi*x),3.,np.sin(np.pi*x)];v=np.cos(np.arange(2*n+1))
    fd=(fold_equations(w+1e-6*v)-fold_equations(w-1e-6*v))/2e-6;exact=fold_jacobian(w).dot(v)
    assert norm(fd-exact)/norm(exact)<2e-7


def test_lambda4_exceeds_discrete_existence_upper_bound():
    n=31;mu=4*(n+1)**2*np.sin(np.pi/(2*(n+1)))**2
    assert mu/np.e<np.pi**2/np.e<4


def test_fixed_lambda_Newton_reaches_lower_discrete_solution():
    r=fixed_lambda(np.zeros(15),2.);assert r['passed'] and l2(residual(r['u'],2.))<1e-10


def test_GMRES_identity_callable_has_true_residual():
    b=np.arange(1,10,dtype=float);r=gmres(lambda v:v,b,lambda v:v,9,20,1e-12)
    assert r['passed'];np.testing.assert_allclose(r['x'],b,rtol=0,atol=2e-14)


def test_GMRES_diagonal_callable_reaches_known_solution():
    d=np.arange(1,10,dtype=float);b=np.ones(9);r=gmres(lambda v:d*v,b,lambda v:v,9,20,1e-10)
    assert r['passed'] and norm(d*r['x']-b)<1e-9


def test_GMRES_rejects_an_explicit_matrix():
    with pytest.raises(TypeError):gmres(np.eye(3),np.ones(3),lambda v:v,3,3,1e-5)


def test_JFNK_runs_with_both_Jacobian_assembly_entrypoints_forbidden(monkeypatch):
    def forbidden(*a,**k):raise AssertionError('Nonlinear Jacobian assembly in JFNK')
    monkeypatch.setattr(problem,'sparse_jacobian',forbidden);monkeypatch.setattr(problem,'jacobian_diagonals',forbidden)
    r=inexact_newton(15,2.,'lower','analytic',SETTINGS)
    assert r['passed'] and r['final_residual']<=SETTINGS['nonlinear_tolerance']


def test_forward_AD_JFNK_uses_directional_evaluations():
    r=inexact_newton(15,2.,'lower','forward-ad',SETTINGS);assert r['passed'] and r['counts']['dual_residual']>0


def test_central_FD_JFNK_uses_residual_probes():
    r=inexact_newton(15,2.,'lower','central-fd',SETTINGS)
    assert r['passed'] and r['counts']['primal_residual']>=2*(r['counts']['jv']-r['counts']['zero_jv'])


def test_finite_CSV_contract_rejects_nan_ragged_and_empty(tmp_path):
    for rows in [[dict(x=float('nan'))],[dict(x=1.),dict(y=2.)],[]]:
        with pytest.raises(ValueError):numeric_csv(tmp_path/'bad.csv',rows)


def test_completed_JFNK_inner_and_line_trials_survive_reference_failure(tmp_path,monkeypatch):
    import experiments as E
    def fail(*a,**kw):raise ArithmeticError('injected reference diagnostic failure')
    monkeypatch.setattr(E,'reference',fail)
    cfg=dict(N=[7],**{'lambda':3.},branches=['lower','upper'],modes=['analytic','central-fd','forward-ad'],constant_eta=1e-8,settings=SETTINGS)
    with pytest.raises(ArithmeticError,match='injected reference'):E.run_jfnk(tmp_path,cfg,dict(ad_jv=1e-12,ad_primal=1e-13,fd_jv=2e-6),[])
    with np.load(tmp_path/'bratu-matrix-free-jfnk-run0-completed-solve.npz',allow_pickle=False) as z:
        assert z['states'].shape[1]==7 and z['states'].shape[0]>1
        assert any(k.startswith('inner_') for k in z.files) and any(k.startswith('line_trial_') for k in z.files)
    result=json.loads((tmp_path/'bratu-matrix-free-jfnk-run0-completed-solve.json').read_text())
    assert result['counts']['jv']>0 and result['rows'] and result['line_trials']


def test_completed_arc_correctors_survive_next_fold_solver_failure(tmp_path,monkeypatch):
    import experiments as E
    def fail(*a,**kw):raise ArithmeticError('injected next fold solver failure')
    monkeypatch.setattr(E,'solve_fold',fail)
    cfg=dict(N=[7],ds=.1,arc_steps=2,tolerance=1e-10,max_corrector=12,max_fold=16)
    with pytest.raises(ArithmeticError,match='injected next fold'):E.run_continuation(tmp_path,cfg,{},[])
    with np.load(tmp_path/'bratu-fold-continuation-N7-completed-arc.npz',allow_pickle=False) as z:
        assert z['states'].shape==(3,8) and z['tangents'].shape==(3,8)
        assert 'corrector_states_0' in z.files and 'corrector_residuals_1' in z.files
