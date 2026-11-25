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

def test_authored_NH_map_reversal_energy_and_radial_domains():
    import deterministic as d
    checks,_=d.components(Budget(10))
    assert all(checks.values())
    with pytest.raises(ValueError):d.radial(np.zeros((1,2)),.1,1,'Berendsen')

def test_constraint_rank_signed_f1_and_valid_projected_OU():
    import constrained as c
    checks,_=c.components(Budget(10))
    assert all(checks.values())
    with pytest.raises(ValueError):c.csvr(np.array([[1.]]),.1,.5,np.array([0.]),np.array([1.]))


def test_correlation_constant_and_roundoff_limited_variance_are_unresolved():
    from common import corr
    assert corr(np.ones(4),np.arange(4.))['null_reason']=='zero_variance'
    e=np.finfo(float).eps
    r=corr(np.array([1.,1.+e,1.-e]),np.arange(3.))
    assert r['correlation'] is None and r['null_reason']=='roundoff_limited_variance'
    assert r['variance_x']<=r['variance_resolution_floor_x']
    ordinary=corr(np.array([1.,2.,3.]),np.array([3.,2.,1.]))
    assert ordinary['null_reason'] is None and abs(ordinary['correlation']+1)<1e-14


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
