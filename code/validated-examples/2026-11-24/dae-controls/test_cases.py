"""Independent residual signs, constraint laws and preservation regressions."""
from fractions import Fraction as F
import numpy as np
import pytest
import models as M
import references as R
from newton import solve,NewtonFailure
from experiments import initialize_index1


def test_index1_initial_residual():
    assert np.array_equal(M.index1_residual(np.ones(2),np.ones(2),0.,1.),np.array([1.,0.]))


def test_index1_differential_exact_derivative():
    y,z=1.,1.;differential=-1+y-z+1
    assert differential==0 and 3*z*z*(-2/3)-2*y*(-1)==0


def test_index1_jacobian_independent_golden():
    assert np.array_equal(M.index1_jacobian(np.array([2.,3.]),.25),np.array([[5.,-1.],[-4.,27.]]))


def test_decimal_independent_positive_roots():
    checks,fixtures=R.index1_qualification()
    assert all(checks.values()) and len(fixtures)==3


def test_newton_quadratic_root():
    x,counter,trials=solve(lambda x:x*x-2,lambda x:np.array([[2*x[0]]]),[1.],[1.],5e-13)
    assert abs(float(x[0]*x[0]-2))<5e-13 and counter['linear_solves']>0


def test_newton_scaled_max_norm():
    x,counter,trials=solve(lambda x:np.array([2e-10,1e-13]),lambda x:np.eye(2),[0.,0.],[1.,1e-4],1e-8)
    assert counter['iterations']==0 and counter['scaled_residual']==pytest.approx(1e-9,abs=1e-24)


def test_newton_owns_input():
    start=np.array([1.]);saved=start.copy()
    solve(lambda x:x*x-2,lambda x:np.array([[2*x[0]]]),start,[1.],5e-13)
    assert np.array_equal(start,saved)


def test_newton_singular_failure_keeps_raw_arrays():
    with pytest.raises(NewtonFailure) as err:solve(lambda x:np.array([1.]),lambda x:np.array([[0.]]),[3.],[1.],1e-12)
    assert err.value.arrays['candidate'][0]==3 and err.value.arrays['residual'][0]==1


def test_newton_line_search_records_rejected_trials():
    x,c,trials=solve(lambda x:x**3-1,lambda x:np.array([[3*x[0]**2]]),[.5],[1.],5e-13)
    assert np.any(trials[:,3]==0) and abs(x[0]-1)<5e-13


def test_newton_callback_owned_snapshot():
    seen=[]
    solve(lambda x:x*x-2,lambda x:np.array([[2*x[0]]]),[1.],[1.],5e-13,progress=lambda **v:seen.append({k:np.array(x,copy=True) for k,x in v.items()}))
    assert seen[0]['candidate'][0]==1 and next(v for v in seen if 'residual' in v)['residual'][0]==-1


def test_robertson_initial_rhs():
    assert np.array_equal(M.robertson_rhs(np.array([1.,0.,0.])),np.array([-.04,.04,0.]))


def test_robertson_mass_rhs_identity():
    y=np.array([.9,3e-5,.09997]);f=M.robertson_rhs(y)
    assert abs(float(np.sum(f)))<1e-16


def test_robertson_jacobian_column_sums():
    assert np.max(np.abs(np.sum(M.robertson_jacobian(np.array([.9,3e-5,.09997])),axis=0)))<1e-12


def test_robertson_dae_mass_row():
    y=np.array([.8,.01,.2]);old=np.array([1.,0.,0.]);r=M.robertson_residual(y,old,.001,'residual_dae')
    assert r[2]==np.sum(y)-1 and np.array_equal(M.robertson_step_jacobian(y,.001,'residual_dae')[2],np.ones(3))


def test_robertson_ode_third_row_distinct():
    y=np.array([.8,.01,.2]);old=np.array([1.,0.,0.]);r=M.robertson_residual(y,old,.001,'full_ode')
    assert r[2]==y[2]-.001*3e7*y[1]**2


def test_pendulum_initial_hidden_constraint():
    state=M.consistent_pendulum();C,D,H,r2=M.pendulum_invariants(state)
    assert abs(C)<5e-15 and D==0 and abs(H+np.cos(.7))<1e-15


def test_pendulum_underlying_C_second_derivative():
    state=np.array([.6,-.9,.2,-.1,0.]);f=M.pendulum_rhs(state)
    cdd=float(np.sum(state[2:4]**2)+np.sum(state[:2]*f[2:4]))
    assert abs(cdd)<3e-16


def test_pendulum_critical_C_second_derivative():
    state=np.array([.6,-.9,.2,-.1,0.]);C,D,H,r2=M.pendulum_invariants(state);f=M.pendulum_rhs(state,True)
    cdd=float(np.sum(state[2:4]**2)+np.sum(state[:2]*f[2:4]))
    assert abs(cdd+2*D+C)<3e-16


def test_pendulum_work_sign():
    state=np.array([.6,-.9,.2,-.1,0.]);f=M.pendulum_rhs(state,True)
    assert abs(float(np.sum(state[2:4]*f[2:4])+state[3]-f[4]))<1e-16


def test_rk4_static_downward_equilibrium():
    start=np.array([0.,-1.,0.,0.,0.]);h=M.rk4_path(start,1.,4)
    assert np.array_equal(h,np.tile(start,(5,1)))


def test_rk4_input_ownership():
    start=M.consistent_pendulum();before=start.copy();M.rk4_path(start,.01,1)
    assert np.array_equal(start,before)


def test_jacobi_initial_orientation():
    states,K=R.pendulum_exact([0.]);start=M.consistent_pendulum()
    assert np.max(np.abs(states[0]-start[:4]))<5e-15


def test_decimal_agm_independent_constant():
    K,notes=R.agm_K(.7)
    assert 1.6<K<1.7 and float(notes['machin_remainder_bound'])<1e-75


def test_critical_law_initial_derivatives():
    C0=F(1,10);D0=F(1,20)
    # C=(C0+(D0+C0)t)e^-t implies C'(0)=D0, C''(0)=-2D0-C0.
    assert D0+C0-C0==D0 and C0-2*(D0+C0)==-2*D0-C0
