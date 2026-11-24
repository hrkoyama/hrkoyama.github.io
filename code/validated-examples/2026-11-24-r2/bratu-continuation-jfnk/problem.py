"""Dimensionless 1D Dirichlet Bratu; matrix-free residual and explicit arc-only assembly."""
import numpy as np
from dual import Dual,pad_zero


def dot(a,b):return float(np.sum(np.asarray(a)*np.asarray(b)))
def norm(a):return float(np.sqrt(dot(a,a)))
def l2(a):return norm(a)/np.sqrt(len(a)+1)


def laplace(u):
    value=u.value if isinstance(u,Dual) else np.asarray(u)
    if value.ndim!=1 or not len(value):raise ValueError('Nonempty interior vector required')
    p=pad_zero(u);return (2*p[1:-1]-p[:-2]-p[2:])*(len(value)+1)**2


def residual(u,lam):
    value=u.value if isinstance(u,Dual) else np.asarray(u)
    if not np.all(np.isfinite(value)) or np.max(value)>700:raise FloatingPointError('Unrepresentable Bratu trial')
    return laplace(u)-lam*np.exp(u)


def analytic_jv(u,lam,v):return laplace(v)-lam*np.exp(u)*v


def jacobian_diagonals(u,lam):
    """Only assembled continuation/fold and qualification may call this."""
    n=len(u);scale=(n+1)**2
    return np.full(n-1,-float(scale)),2*scale-lam*np.exp(u),np.full(n-1,-float(scale))


def sparse_jacobian(u,lam):
    from scipy.sparse import diags
    lo,di,up=jacobian_diagonals(u,lam)
    return diags([lo,di,up],[-1,0,1],format='csc')


def poisson_inverse(b):
    """Constant-coefficient Dirichlet Poisson preconditioner, O(n), no n by n storage."""
    n=len(b);di=np.full(n,2.);rhs=np.array(b,dtype=float)/(n+1)**2
    for i in range(1,n):
        di[i]-=1/di[i-1];rhs[i]+=rhs[i-1]/di[i-1]
    x=np.empty(n);x[-1]=rhs[-1]/di[-1]
    for i in range(n-2,-1,-1):x[i]=(rhs[i]+x[i+1])/di[i]
    return x


def weighted_arc_dot(z,t):return dot(z[:-1],t[:-1])/(len(z))+z[-1]*t[-1]
def arc_norm(z):return float(np.sqrt(weighted_arc_dot(z,z)))
