"""Fixed matrix definitions; no solver or reference generation at import."""
import numpy as np
from fractions import Fraction


def direct_fixture(name):
    if name=='spd-tridiagonal':
        n=12;a=np.diag(np.full(n,4.))+np.diag(np.full(n-1,-1.),1)+np.diag(np.full(n-1,-1.),-1)
    elif name=='near-singular-rank-one':
        n=8;delta=2.**-16;a=np.eye(n)+(delta-1)*np.ones((n,n))/n
    elif name=='hilbert5':
        n=5;a=np.array([[1/(i+j+1) for j in range(n)] for i in range(n)])
    elif name=='wilkinson12':
        n=12;a=np.eye(n)-np.tril(np.ones((n,n)),-1);a[:,-1]=1.
    else:raise ValueError('unknown fixed direct fixture')
    nominal=np.array([1. if j%2==0 else -1. for j in range(n)])
    # Correctly rounded exact sum of the ACTUAL binary64 coefficients.
    b=np.array([float(sum((Fraction(float(a[i,j]))*int(nominal[j]) for j in range(n)),Fraction(0))) for i in range(n)])
    return a,b


def saddle(velocity_size):
    n=velocity_size;p=n//2-1;h=1/(n+1)
    H=(np.diag(np.full(n,2.))+np.diag(np.full(n-1,-1.),1)+np.diag(np.full(n-1,-1.),-1))/h**2+np.eye(n)
    B=np.zeros((p,n))
    for i in range(p):B[i,2*i]=-1/h;B[i,2*i+1]=1/h
    A=np.block([[H,B.T],[B,np.zeros((p,p))]])
    exact=np.array([(-1.)**j*(1+j/len(A)) for j in range(len(A))]);b=np.einsum('ij,j->i',A,exact,optimize=False)
    return A,b,H,B


def laplacian(n):
    h=1/(n+1);return (np.diag(np.full(n,2.))+np.diag(np.full(n-1,-1.),1)+np.diag(np.full(n-1,-1.),-1))/h**2


def string_fem(interior_nodes):
    elements=interior_nodes+1;h=1/elements;n=elements+1;K=np.zeros((n,n));M=np.zeros((n,n))
    for e in range(elements):
        ids=[e,e+1]
        for i in range(2):
            for j in range(2):
                K[ids[i],ids[j]]+=(1 if i==j else -1)/h
                M[ids[i],ids[j]]+=(2 if i==j else 1)*h/6
    return K[1:-1,1:-1],M[1:-1,1:-1],np.arange(1,elements)*h
