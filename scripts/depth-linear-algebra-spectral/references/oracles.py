"""Independent exact-rational, closed-spectrum and LAPACK references.

Never imports the primary factorization/Krylov modules. Reduced primary Ritz
problems also use LAPACK; exact spectra provide separate algebraic oracles.
"""
from fractions import Fraction
import numpy as np
from scipy.linalg.lapack import dgesv,dposv
from scipy.linalg import eigh


def rational_solution(a,b):
    n=len(b);rows=[[Fraction(float(a[i,j])) for j in range(n)]+[Fraction(float(b[i]))] for i in range(n)]
    for k in range(n):
        pivot=max(range(k,n),key=lambda i:abs(rows[i][k]))
        if not rows[pivot][k]:raise ArithmeticError('exact singular reference')
        rows[k],rows[pivot]=rows[pivot],rows[k]
        for i in range(k+1,n):
            c=rows[i][k]/rows[k][k]
            for j in range(k,n+1):rows[i][j]-=c*rows[k][j]
    x=[Fraction(0)]*n
    for i in range(n-1,-1,-1):x[i]=(rows[i][-1]-sum((rows[i][j]*x[j] for j in range(i+1,n)),Fraction(0)))/rows[i][i]
    return np.array([float(z) for z in x])


def lapack_solution(a,b,positive=False):
    if positive:
        _,x,info=dposv(np.array(a,order='F',copy=True),np.array(b,order='F',copy=True),lower=1)
    else:
        _,_,x,info=dgesv(np.array(a,order='F',copy=True),np.array(b,order='F',copy=True))
    if info!=0:raise ArithmeticError('independent LAPACK failure '+str(info))
    return x


def condition_infinity(a):
    inverse=lapack_solution(a,np.eye(len(a)))
    return float(np.max(np.sum(abs(a),axis=1))*np.max(np.sum(abs(inverse),axis=1)))


def laplacian_spectrum(n):
    j=np.arange(1,n+1);return 4*(n+1)**2*np.sin(np.pi*j/(2*(n+1)))**2


def fem_spectrum(n,number):
    theta=np.pi*np.arange(1,number+1)/(n+1);return 6*(n+1)**2*(1-np.cos(theta))/(2+np.cos(theta))


def dense_spectrum(a,m=None):
    return eigh(a,m,driver='evd' if m is None else 'gvd')
