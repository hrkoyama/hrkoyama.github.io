"""Independent Decimal80 analytic Bratu family; no imports from either solver."""
from decimal import Decimal,localcontext
from functools import lru_cache
import numpy as np


def cosh(x):return (x.exp()+(-x).exp())/2
def family_lambda(t):return 2*t*t/cosh(t/2)**2


def bisect(fun,left,right):
    a,b=Decimal(str(left)),Decimal(str(right));fa,fb=fun(a),fun(b)
    if fa*fb>0:raise ValueError('Independent scalar reference lacks a bracket')
    for _ in range(256):
        c=(a+b)/2;fc=fun(c)
        if fc==0:return c
        if fa*fc<0:b=c
        else:a=c;fa=fc
    return (a+b)/2


@lru_cache(maxsize=1)
def fold_parameter():
    with localcontext() as ctx:
        ctx.prec=80
        return bisect(lambda t:t*((t/2).exp()-(-t/2).exp())/((t/2).exp()+(-t/2).exp())-2,2,3)


def reference(n,lam=None,branch='lower',theta=None):
    with localcontext() as ctx:
        ctx.prec=80;tf=fold_parameter()
        if theta is None:
            target=Decimal(str(lam));a,b=(Decimal('1e-30'),tf) if branch=='lower' else (tf,Decimal(16))
            t=bisect(lambda q:family_lambda(q)-target,a,b)
        else:t=Decimal(str(theta))
        ll=family_lambda(t);values=[];ode=[]
        for i in range(n+2):
            x=Decimal(i)/Decimal(n+1);d=cosh(t*(x-Decimal('.5')))
            u=2*(cosh(t/2)/d).ln();values.append(float(u))
            ode.append(float(-2*t*t/d**2+ll*u.exp()))
        return dict(x=np.arange(n+2,dtype=float)/(n+1),u=np.array(values),theta=float(t),lam=float(ll),
                    fold_theta=float(tf),fold_lambda=float(family_lambda(tf)),ode_residual=np.array(ode))
