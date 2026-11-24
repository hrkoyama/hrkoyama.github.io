"""Independent rational stencil / amplification reference, without production imports."""
from fractions import Fraction as F
import numpy as np


def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def times(a,b):return (a[0]*b,a[1]*b)


def polynomial(z):
    value=(F(1,24),F(0))
    for c in (F(1,6),F(1,2),F(1),F(1)):
        value=add(mul(value,z),(c,F(0)))
    return value


def qualify():
    checks={}
    cases=[('h32-mode4',F(1,32),(F(9),F(2))),('h32-mode8',F(1,32),(F(17),F(0))),
           ('h16-mode4',F(1,16),(F(9),F(2))),('h16-mode8',F(1,16),(F(17),F(0)))]
    for ident,h,lam in cases+[('neutral',F(1,32),(F(0),F(0))),('expanding',F(1,4),(F(17),F(0)))]:
        z=times(lam,-h)
        stage=(F(1),F(0))
        for alpha in (F(1,4),F(1,3),F(1,2),F(1)):
            stage=add((F(1),F(0)),times(mul(z,stage),alpha))
        checks[ident+':expanded-vs-stages']=stage==polynomial(z)
        norm2=stage[0]**2+stage[1]**2
        checks[ident+':prior-classification']=(norm2<F(9,10) if ident.startswith('h') else norm2==1 if ident=='neutral' else norm2>1)
    # Rational real/imaginary Fourier vectors, not a sampled continuous PDE.
    c=[F(v) for v in [1,0,-1,0]*4];s=[F(v) for v in [0,1,0,-1]*4];v=[(c[j],s[j]) for j in range(16)]
    av=[]
    for j in range(16):
        d=add(v[(j+1)%16],times(v[(j-1)%16],-1))
        lap=add(add(v[(j+1)%16],v[(j-1)%16]),times(v[j],-2))
        av.append(add(add(v[j],d),times(lap,-4)))
    checks['rational-stencil-mode4']=all(av[j]==mul((F(9),F(2)),v[j]) for j in range(16))
    w=[F((-1)**j) for j in range(16)]
    checks['rational-stencil-mode8']=all(w[j]+(w[(j+1)%16]-w[(j-1)%16])-4*(w[(j+1)%16]-2*w[j]+w[(j-1)%16])==17*w[j] for j in range(16))
    return checks


def amplification(dt, lam):
    pair=polynomial(times((F(lam[0]),F(lam[1])),-F(dt)))
    return complex(float(pair[0]),float(pair[1]))


def field_reference(dt,steps,role):
    c=np.array([1.,0.,-1.,0.]*4);s=np.array([0.,1.,0.,-1.]*4);w=np.array([1.,-1.]*8)
    if role=='neutral_control':return np.ones((steps+1,16)),np.zeros((steps+1,16))
    p4=amplification(dt,(9,2));p8=amplification(dt,(17,0)).real
    states=[];residual=[]
    star=.5+.25*c if role=='steady_iteration' else np.zeros(16)
    for n in range(steps+1):
        a=p4**n if role=='steady_iteration' else 0j
        b=.5*p8**n if role=='steady_iteration' else p8**n
        states.append(star+a.real*c-a.imag*s+b*w)
        a=(9+2j)*a
        residual.append(a.real*c-a.imag*s+17*b*w)
    return np.array(states),np.array(residual)
