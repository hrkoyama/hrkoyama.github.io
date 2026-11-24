"""Independent continuum-angle Fredholm reference; no primary slab imports.

Exact cell integrals of E1 handle the logarithmic diagonal. Two distinct
representations (constant and linearly reconstructed scalar source) provide
separate fixed refinement/sensitivity checks. No E1(0) is ever sampled.
"""
import numpy as np
from scipy.special import expn
from scipy.linalg import solve


def solution(depth,albedo,cells,linear=False):
    edge=np.linspace(0,depth,cells+1);h=depth/cells;c=.5*(edge[:-1]+edge[1:]);x=c[:,None]
    a=edge[:-1][None,:]-x;b=edge[1:][None,:]-x
    lo=np.abs(a);hi=np.abs(b)
    integral=np.where(b<=0,expn(2,hi)-expn(2,lo),
                      np.where(a>=0,expn(2,lo)-expn(2,hi),2-expn(2,lo)-expn(2,hi)))
    operator=integral.copy();derivative=None
    if linear:
        derivative=np.zeros((cells,cells))
        for j in range(1,cells-1):derivative[j,j-1]=-1/(2*h);derivative[j,j+1]=1/(2*h)
        derivative[0,0]=-1/h;derivative[0,1]=1/h;derivative[-1,-2]=-1/h;derivative[-1,-1]=1/h
        primitive=lambda t:-abs(t)*expn(2,abs(t))-expn(3,abs(t))
        moment=primitive(b)-primitive(a)+(x-c[None,:])*integral
        # Banded derivative multiplication without a dense cubic product.
        for j in range(cells):
            indices=np.flatnonzero(derivative[j])
            for k in indices:operator[:,k]+=moment[:,j]*derivative[j,k]
    matrix=np.eye(cells)-.5*albedo*operator;source=.5*expn(2,c)
    scalar=solve(matrix,source,assume_a='gen',check_finite=True)
    left_weights=expn(3,edge[:-1])-expn(3,edge[1:])
    right_weights=expn(3,depth-edge[1:])-expn(3,depth-edge[:-1])
    if linear:
        g=lambda t:-t*expn(3,t)-expn(4,t)
        lm=g(edge[1:])-g(edge[:-1])-c*left_weights
        # Change variable t=depth-s for the right-weight first moment.
        rm=(depth-c)*right_weights-(g(depth-edge[:-1])-g(depth-edge[1:]))
        left_weights=left_weights+np.einsum('i,ij->j',lm,derivative,optimize=False);right_weights=right_weights+np.einsum('i,ij->j',rm,derivative,optimize=False)
    R=2*albedo*np.sum(left_weights*scalar)
    T=2*expn(3,depth)+2*albedo*np.sum(right_weights*scalar)
    A=4*(1-albedo)*h*np.sum(scalar)
    return dict(x=c,scalar=scalar,R=np.array(R),T=np.array(T),A=np.array(A),
                residual=np.array(np.max(abs(np.einsum('ij,j->i',matrix,scalar,optimize=False)-source))),balance=np.array(abs(1-R-T-A)))
