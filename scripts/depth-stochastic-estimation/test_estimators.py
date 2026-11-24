import numpy as np
import pytest
from scipy.stats import multivariate_normal
from scipy.special import log_ndtr
from importance import log_weight,moment,variance,count_interval
from sampler import target_logpdf,observable_arrays,truth_and_scales,sample
from diagnostics import diagnose,mean_mcse


@pytest.mark.parametrize('a',[3.,6.])
def test_importance_expectation_is_target_tail(a):
    assert abs(moment(a,1)-np.exp(log_ndtr(-a)))<1e-24
    assert variance(a)>0
    assert .5/moment(a,1)>100 # omitted weights estimate the proposal event


@pytest.mark.parametrize('a',[3.,6.])
def test_weight_sign_by_density_ratio(a):
    x=np.array([-2.,0.,3.]);ratio=np.exp(-x*x/2)/np.exp(-(x-a)**2/2)
    np.testing.assert_allclose(np.exp(log_weight(x,a)),ratio,rtol=1e-13,atol=0)


def test_zero_hit_interval_is_not_zero_width():
    lo,hi=count_interval(0,8192)
    assert lo==0 and hi>0 and lo<1e-9<hi


@pytest.mark.parametrize('rho',[0.,.95,-.5])
def test_joint_logpdf_has_correct_covariance(rho):
    x=np.array([[0.,0.],[1.,2.],[-3.,1.]])
    expected=multivariate_normal.logpdf(x,mean=[1.,-1.],cov=[[1.,rho],[rho,1.]])
    np.testing.assert_allclose(target_logpdf(x,[1.,-1.],rho),expected,rtol=2e-14,atol=2e-14)


def test_joint_Q_matches_independent_whitening():
    rho=.95;L=np.linalg.cholesky([[1.,rho],[rho,1.]])
    x=np.array([[[.1,.2],[.8,-1.1]],[[3.,-2.],[-1.,2.]]]);y=x-np.array([1.,-1.]);q=(np.linalg.solve(L,y.reshape(-1,2).T)**2).sum(axis=0).reshape(2,2)
    np.testing.assert_allclose(observable_arrays(x,[1.,-1.],rho)[...,5],q,rtol=2e-14)


def test_correct_marginals_wrong_joint_is_detected():
    x=np.array([[[-1.,-1.],[-1.,1.],[1.,-1.],[1.,1.]]])
    obs=observable_arrays(x,[0.,0.],.95)
    assert obs[...,2].mean()==obs[...,3].mean()==1
    assert abs(obs[...,4].mean()-.95)>.9 and abs(obs[...,5].mean()-2)>10


def test_rejected_states_are_retained(monkeypatch):
    class Fixed:
        def normal(self,size):return np.full(size,100.)
        def random(self,n):return np.full(n,.5)
    monkeypatch.setattr(np.random,'default_rng',lambda seed:Fixed())
    cfg=dict(mean=[1.,-1.],rho=.95,chains=4,burn=0,draws=16,initial_whitened=[[-4.,-4.],[-4.,4.],[4.,-4.],[4.,4.]],proposals={'preconditioned':.9})
    out=sample(cfg,3,'preconditioned',{})
    assert not out['accepted'].any()
    np.testing.assert_array_equal(out['chains'],np.repeat(out['initial'][:,None,:],16,axis=1))


def test_constant_diagnostics_are_explicitly_undefined():
    assert diagnose(np.ones((4,32)))['status']=='zero_global_variance'
    with pytest.raises(ValueError,match='nonconstant'):mean_mcse(np.ones((4,32)))


def test_mcse_uses_original_observable_scale():
    x=np.arange(128,dtype=float).reshape(4,32)%13
    assert mean_mcse(3*x+2)==pytest.approx(3*mean_mcse(x),rel=2e-14)
    assert truth_and_scales(.95)[0][5]==2
