import numpy as np
import pytest
from scipy.integrate import quad
from paths import grouped_increments,bridge_coefficients,gbm_step,simulate_batch
from references.analytic import gbm,ou,strong


@pytest.mark.parametrize('steps',[2,4,8])
def test_grouping_reuses_declared_fine_increments(steps):
    fine=np.arange(32,dtype=float).reshape(4,8)/32
    expected=np.array([[sum(row[j:j+8//steps]) for j in range(0,8,8//steps)] for row in fine])
    np.testing.assert_array_equal(grouped_increments(fine,steps),expected)


@pytest.mark.parametrize('k,h',[(1.5,.125),(1.5,1/64),(2.,.01)])
def test_ou_bridge_covariance_and_variance_by_independent_integrals(k,h):
    alpha,beta=bridge_coefficients(k,h)
    c=quad(lambda s:np.exp(-k*(h-s)),0,h)[0]
    v=quad(lambda s:np.exp(-2*k*(h-s)),0,h)[0]
    assert abs(alpha*h-c)<1e-14 and abs(alpha*alpha*h+beta*beta-v)<1e-14


@pytest.mark.parametrize('method',['em','milstein'])
def test_zero_noise_is_discrete_euler_not_exponential(method):
    cfg=dict(kind='gbm',initial=1.,mu=.5,sigma=0.,T=1.,steps=[4],paths_per_batch=16)
    out,_=simulate_batch(cfg,7,[method],{})
    np.testing.assert_allclose(out['endpoints'],(1+.5/4)**4,rtol=0,atol=1e-15)
    np.testing.assert_array_equal(out['exact'],np.full(16,np.exp(.5)))
    assert abs(out['endpoints'][0,0,0]-out['exact'][0])>.01


def test_milstein_compensation_negative_control():
    x=np.ones(2);dw=np.array([-.1,.1]);h=.01
    good=gbm_step(x,dw,h,.15,.4,'milstein')
    omitted=x*(1+.15*h+.4*dw+.5*.4**2*dw**2)
    np.testing.assert_allclose(omitted-good,.5*.4**2*h,rtol=0,atol=3e-16)
    assert abs(good.mean()-(1+.15*h))<1e-15


def test_exact_endpoint_is_single_saved_fine_sum():
    cfg=dict(kind='gbm',initial=1.,mu=.15,sigma=.4,T=1.,steps=[4,8],paths_per_batch=16)
    out,_=simulate_batch(cfg,17,['em','milstein'],{})
    np.testing.assert_array_equal(out['exact'],np.exp((.15-.5*.4**2)+.4*out['terminal_w']))
    assert out['endpoints'].shape==(2,2,16)


def test_grouping_rejects_non_nested_levels():
    with pytest.raises(ValueError,match='nested'):grouped_increments(np.ones((4,8)),3)


@pytest.mark.parametrize('n',[8,64])
def test_weak_moment_identities_sigma_zero(n):
    c=dict(initial=1.,mu=.5,sigma=0.,T=1.)
    row=gbm(c,n)
    assert all(abs(x)<__import__('decimal').Decimal('1e-65') for x in row['paired_variance'])
    assert abs(float(row['bias'][0])-((1+.5/n)**n-np.exp(.5)))<1e-14


def test_ou_second_moment_contains_squared_mean():
    c=dict(initial=.7,theta=.2,kappa=1.5,sigma=.8,T=1.)
    row=ou(c,32);m=.2+.5*np.exp(-1.5);v=.8**2*(1-np.exp(-3))/3
    assert abs(float(row['continuous'][1])-(m*m+v))<1e-15
    assert abs(float(row['continuous'][1])-v)>.05


@pytest.mark.parametrize('method',['em','milstein'])
def test_strong_analytic_mse_positive_precision_agrees(method):
    c=dict(initial=1.,mu=.15,sigma=.4,T=1.)
    a=strong(c,128,method,80);b=strong(c,128,method,120)
    assert a['mse']>0 and abs(a['mse']-b['mse'])<b['mse']*__import__('decimal').Decimal('1e-40')
