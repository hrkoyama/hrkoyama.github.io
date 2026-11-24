"""Hand-expanded references, independent of the reverse tape and fixtures."""
from decimal import Decimal,localcontext
from fractions import Fraction
import numpy as np


def exp_decimal(x,precision=60):
    with localcontext()as c:
        c.prec=precision;return Decimal.from_float(float(x)).exp()


def precision_qualified():
    return abs(exp_decimal(-.5,60)-exp_decimal(-.5,90))<=Decimal('1e-50')


def smooth_reference(ident,x):
    if ident=='rectangular4x3':
        a,b,c,d=(Fraction.from_float(float(z))for z in x);e=exp_decimal(float(b))
        y=np.array([float(2*(a+d)**2+(c+d)**2+a*b),float(e)+float(a*c+d*d),float((a+b)*(c-d)+(2*a+c+3*d)/2)])
        j=np.array([[float(4*(a+d)+b),float(a),float(2*(c+d)),float(4*(a+d)+2*(c+d))],
                    [float(c),float(e),float(a),float(2*d)],
                    [float(c-d+1),float(c-d),float(a+b+Fraction(1,2)),float(-a-b+Fraction(3,2))]])
        return y,j
    n=len(x)
    if ident.startswith('wide'):
        e=np.array([float(exp_decimal(z))for z in x]);j=np.empty((3,n))
        for i in range(n):j[:,i]=[2*x[i]/n,e[i]/n,1/n]
        j[2,0]+=x[-1];j[2,-1]+=x[0]
        return np.array([sum(float(z)**2 for z in x)/n,sum(e)/n,x[0]*x[-1]+sum(x)/n]),j
    j=np.zeros((n,n));y=np.empty(n)
    for i in range(n):
        e=float(exp_decimal(x[i]));j[i,i]=2*(n+1)**2-2*e
        if i:j[i,i-1]=-(n+1)**2
        if i+1<n:j[i,i+1]=-(n+1)**2
        y[i]=(n+1)**2*(2*x[i]-(x[i-1]if i else 0.)-(x[i+1]if i+1<n else 0.))-2*e
    return y,j


def hvp_reference(ident,x,v):
    if ident=='quadratic4':
        q=[[Fraction(4),Fraction(1),Fraction(1,2),Fraction(0)],
           [Fraction(1),Fraction(3),Fraction(-1,4),Fraction(1,2)],
           [Fraction(1,2),Fraction(-1,4),Fraction(2),Fraction(1,4)],
           [Fraction(0),Fraction(1,2),Fraction(1,4),Fraction(3,2)]]
        c=[Fraction(1,2),Fraction(-1,4),Fraction(1,8),Fraction(-3,4)]
        xf=[Fraction.from_float(float(z))for z in x];vf=[Fraction.from_float(float(z))for z in v]
        return np.array([float(c[i]+sum(q[i][j]*xf[j]for j in range(4)))for i in range(4)]),np.array([float(sum(q[i][j]*vf[j]for j in range(4)))for i in range(4)])
    n=len(x);g=np.empty(n);hv=np.empty(n)
    for i in range(n):
        e=float(exp_decimal(x[i]));lx=(n+1)**2*(2*x[i]-(x[i-1]if i else 0.)-(x[i+1]if i+1<n else 0.))
        lv=(n+1)**2*(2*v[i]-(v[i-1]if i else 0.)-(v[i+1]if i+1<n else 0.))
        g[i]=(lx-2*e)/(n+1);hv[i]=(lv-2*e*v[i])/(n+1)
    return g,hv


def piece_reference(kind,x,d):
    x=Fraction.from_float(float(x));d=Fraction.from_float(float(d));zero=Fraction(0)
    if kind=='abs':value=abs(x);slope=1 if x>0 else-1 if x<0 else None;direction=abs(d)if x==0 else slope*d
    elif kind=='relu':value=max(x,zero);slope=1 if x>0 else 0 if x<0 else None;direction=max(d,zero)if x==0 else slope*d
    elif kind=='clip':
        value=max(Fraction(-1),min(Fraction(1),x));slope=1 if -1<x<1 else 0 if x<-1 or x>1 else None
        direction=max(d,zero)if x==-1 else min(d,zero)if x==1 else slope*d
    elif kind=='branch':
        value=x*x if x>=0 else 2*x;slope=2*x if x>0 else 2 if x<0 else None
        direction=zero if x==0 and d>=0 else 2*d if x==0 else slope*d
    else:raise ValueError(kind)
    return {'value':float(value),'slope':None if slope is None else float(slope),'directional':float(direction),'status':'NONDIFFERENTIABLE'if slope is None else'SMOOTH'}


def stopped_reference(theta):
    theta=Fraction.from_float(float(theta))
    eligible=[k for k in range(6)if abs(theta)/2**k<=Fraction(1,8)]
    k=min(eligible)if eligible else 5
    return k,float((1-Fraction(1,2**k))*theta),float(1-Fraction(1,2**k))
