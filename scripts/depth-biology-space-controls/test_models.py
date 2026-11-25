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

def test_fisher_profile_does_not_have_arbitrary_speed():
    import fisher
    x=np.linspace(-2,2,17)
    assert maxerr(fisher.exact(x,1),fisher.exact(x,1,c=2))>1e-4
    assert fisher.contour(np.array([0.,1.]),np.array([.2,.1])) is None

def test_schnakenberg_modes_corners_and_equilibrium():
    import schnakenberg as s
    checks,_=s.components(Budget(10))
    assert all(checks.values())

def test_keller_segel_independent_cell_source_and_owner():
    import json,keller_segel as k
    inputs=json.loads(Path(__file__).with_name('inputs.json').read_text())
    checks,_,_=k.components(Budget(10),inputs)
    assert all(checks.values())


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


def test_reference_qualification_uses_selected_fine_reference_and_both_unchanged_gates():
    import schnakenberg as s
    def refs(values):return [{N:np.full((1,2,1,1),v) for N in [12,24,48]} for v in values]
    primary={N:np.zeros((1,2,1,1)) for N in [12,24,48]}
    d,e,total,ok=s.reference_assessment(refs([1.01e-3,1.00002e-3,1.00001e-3,1e-3]),primary)
    assert ok and e[-1]==1e-3 and total<=.1*e[-1] and total<=2e-4
    # A historicalcoarsereferencecanmeetabsolute2e-4andfailrelative.1:retainFAIL.
    d,e,total,ok=s.reference_assessment(refs([1.4e-4,9e-5,9e-5,9e-5]),primary)
    assert not ok and total<2e-4 and total>.1*e[-1]
    assert not s.reference_assessment(refs([1.0003,1.,1.,1.]),primary)[-1]  # Absolutegate
    assert not s.reference_assessment(refs([0.,0.,0.,0.]),primary)[-1]  # Zerodenominator
