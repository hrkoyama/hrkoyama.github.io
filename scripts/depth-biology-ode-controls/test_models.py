"""Small component tests; frozen exact inputs first, no hidden large simulation."""
from pathlib import Path
import math
import numpy as np
import pytest
from common import Budget,adaptive,assert_frozen,maxerr

@pytest.fixture(autouse=True)
def reviewed_source():
    assert_frozen(Path(__file__).resolve().parent)

def test_independent_embedded_pairs_on_exact_decay():
    for method in ['DP54','CK54']:
        y,ledger=adaptive(lambda t,z:-z,np.array([1.]),[0.,.25,.5,1.],Budget(5),1e-11,1e-13,2000,method)
        assert maxerr(y[:,0],np.exp(-np.array([0,.25,.5,1.])))<2e-10
        assert ledger['complete'] and ledger['nfev']>0

def test_reference_cap_and_stagnation_fail_closed():
    with pytest.raises(RuntimeError):
        adaptive(lambda t,z:-z,np.array([1.]),[0.,1.],Budget(5),1e-11,1e-13,1)
    with pytest.raises(ValueError):
        adaptive(lambda t,z:-z,np.array([1.]),[0.,0.],Budget(5),1e-11,1e-13,2000)

def test_hh_singular_rates_and_segment_components():
    import hh
    q,_=hh.qualify(Budget(10))
    assert q['checks'] and all(q['checks'].values())
    assert hh.rates(-65)[5]==.125

def test_ssa_interval_factor_and_reaction_equality():
    import ssa
    ssa.I.precision=80
    law=ssa.factor('poisson',ssa.I(6))
    truth=math.exp(-6)
    cdf=law.cdf(0)
    assert float(cdf.lo)<=truth<=float(cdf.hi) or abs(float(cdf.lo)-truth)<2e-18
    assert ssa.choose_reaction(.5,6)==-1
    assert ssa.choose_reaction(.5,0)==1


def test_Hermite_interior_and_multiple_crossings_not_endpoint_only():
    import hh
    fun=lambda y,I:np.array([y[1],0.,0.,0.])
    y=np.array([[-1.,8.,0.,0.],[-1.,-8.,0.,0.]])
    events,audit=hh.event_roots([0.,1.],y,[0.],event_rhs=fun)
    assert len(events)==1 and abs(events[0]['time_ms']-(1-math.sqrt(.5))/2)<1e-9
    assert audit['interior_crossings_without_endpoint_sign_change']==2
    y=np.array([[-.08,.66,0.,0.],[.08,.66,0.,0.]])
    events,audit=hh.event_roots([0.,1.],y,[0.],event_rhs=fun)
    assert len(events)==2 and audit['maximum_cubic_roots_per_interval']==3
    assert abs(events[0]['time_ms']-.2)<1e-9 and abs(events[1]['time_ms']-.8)<1e-9

def test_Hermite_tangent_is_explicitly_unresolved():
    import hh
    y=np.array([[.25,-1.,0.,0.],[.25,1.,0.,0.]])
    events,audit=hh.event_roots([0.,1.],y,[0.],event_rhs=lambda y,I:np.array([y[1],0.,0.,0.]))
    assert not events and audit['nonsimple_or_roundoff_unresolved_intervals']==1


@pytest.mark.parametrize('complex_values',[False,True])
@pytest.mark.parametrize('strided',[False,True])
def test_explicit_products_against_independent_scalar_fsum(complex_values,strided):
    from common import mm,mv,dot,matmul,array_norm
    a=np.arange(30,dtype=float).reshape(5,6)[::2,::2]/7-.4
    b=np.arange(24,dtype=float).reshape(3,8)[:,::4]/5-.7
    if complex_values:a=a+1j*(a[::-1]+.2)/11;b=b+1j*(b[::-1]-.3)/13
    if strided:
        aa=np.zeros((6,6),dtype=a.dtype);aa[::2,::2]=a;a=aa[::2,::2]
        bb=np.zeros((6,4),dtype=b.dtype);bb[::2,::2]=b;b=bb[::2,::2]
        assert not a.flags.c_contiguous and not b.flags.c_contiguous
    else:a=a.copy();b=b.copy()
    def scalar(left,right):
        products=[complex(x)*complex(y) for x,y in zip(left,right)]
        return complex(math.fsum(v.real for v in products),math.fsum(v.imag for v in products))
    def check(actual,left,right):
        n=len(left);eps=np.finfo(float).eps;gamma=n*eps/(1-n*eps)
        bound=16*gamma*max(1.,math.fsum(abs(complex(x))*abs(complex(y)) for x,y in zip(left,right)))
        assert abs(actual-scalar(left,right))<=bound
    prod=mm(a,b);general=matmul(a,b)
    for i in range(a.shape[0]):
        for j in range(b.shape[1]):check(prod[i,j],a[i],b[:,j]);check(general[i,j],a[i],b[:,j])
    vector=mv(a,b[:,0]);general=matmul(a,b[:,0])
    for i in range(len(a)):check(vector[i],a[i],b[:,0]);check(general[i],a[i],b[:,0])
    row=matmul(a[0],b)
    for j in range(b.shape[1]):check(row[j],a[0],b[:,j])
    check(dot(a[0],b[:,0]),a[0],b[:,0]);check(matmul(a[0],b[:,0]),a[0],b[:,0])
    gram=mm(a.conj().T,a)
    for i in range(a.shape[1]):
        for j in range(a.shape[1]):check(gram[i,j],a[:,i].conj(),a[:,j])
    frobenius=math.sqrt(math.fsum(abs(complex(x))**2 for x in a.flat))
    infinity=max(math.fsum(abs(complex(x)) for x in row) for row in a)
    bound=16*a.size*np.finfo(float).eps*max(1.,frobenius,infinity)
    assert abs(array_norm(a)-frobenius)<=bound and abs(array_norm(a,np.inf)-infinity)<=bound


def test_explicit_norm_extremes_and_invalid_product_rank():
    from common import array_norm,matmul
    for scale in [1e-200,1e200]:assert abs(array_norm(np.array([scale,-scale]))/math.hypot(scale,scale)-1)<4*np.finfo(float).eps
    assert array_norm(np.zeros(3))==0
    with pytest.raises(FloatingPointError):array_norm(np.array([float('nan')]))
    with pytest.raises(ValueError):matmul(np.zeros((1,1,1)),np.zeros((1,1,1)))
