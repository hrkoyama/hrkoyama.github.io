"""Narrow R4 regressions; all previous27 tests remain byte-identical."""
import json
import numpy as np
import pytest
from scipy.sparse.linalg import LinearOperator,lobpcg
import fixtures as F
import solvers as S
import run as driver
from references import oracles as R


def test_mass_action_selfadjoint_and_actual_three_mode_generalized_comparison():
    # Existing smallest fixed physical mesh. 5k=n: actual LOBPCG, no eigh fallback.
    k,m,x=F.string_fem(15);mass=driver.mass_action_operator(m)
    v=.25+x;w=1+x*x
    left=float(np.sum(v*mass.matvec(w)));right=float(np.sum(mass.matvec(v)*w))
    assert abs(left-right)<=64*np.finfo(float).eps*max(1.,abs(left),abs(right))
    factor=S.cholesky(k)
    op=LinearOperator(k.shape,matvec=lambda y:S.mv(k,y),matmat=lambda y:S.mv(k,y),dtype=float)
    pre=LinearOperator(k.shape,matvec=lambda y:S.chol_solve(factor,y),matmat=lambda y:S.chol_solve(factor,y),dtype=float)
    values,vectors=lobpcg(op,driver.fem_initial_block(x),B=mass,M=pre,largest=False,tol=1e-8,maxiter=100)
    exact=R.fem_spectrum(15,3)
    residual,orth=driver.eigen_metrics(k,m,values,vectors)
    assert np.max(abs(values-exact)/exact)<=2e-8
    assert residual<=2e-8
    assert orth<=2e-9


def test_mass_action_preserves_original_exception_before_library_can_replace_it(monkeypatch,tmp_path):
    def broken(_matrix,_argument):
        raise RuntimeWarning('forced mass-action retention sentinel')
    monkeypatch.setattr(S,'mv',broken)
    m=np.diag([2.,3.,4.]);v=np.array([.5,-.25,1.])
    action=driver.mass_action_operator(m,tmp_path,'probe')
    with pytest.raises(RuntimeWarning,match='retention sentinel'):
        action.matvec(v)
    saved=json.loads((tmp_path/'probe-failed-action.json').read_text())
    assert saved['type']=='RuntimeWarning'
    assert saved['message']=='forced mass-action retention sentinel'
    with np.load(tmp_path/'probe-failed-action.npz',allow_pickle=False) as f:
        assert np.array_equal(f['m'],m)
        assert np.array_equal(f['argument'],v)
