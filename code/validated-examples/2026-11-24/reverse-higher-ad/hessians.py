"""Primary implicit rules solve F/R1/R2; no square-root family in this module."""
import numpy as np
from tape import build


def hvp(function,x,v):
    tape,node,out=build(function,x,v)
    if isinstance(out,(list,tuple))or out.value.shape!=():raise ValueError('Scalar smooth objective required')
    gradient,product=tape.reverse(out,np.array(1.),second_order=True)
    return gradient,product,tape,out


def implicit_second(theta=4.,checkpoint=lambda *a,**k:None):
    u=3.;iterations=[]
    for k in range(13):
        f=u*u-theta;checkpoint('implicit-before-division',u=np.array(u),F=np.array(f),iteration=np.array(k))
        iterations.append({'iteration':k,'u':u,'F':f})
        if abs(f)<=1e-13:break
        if k==12:raise ArithmeticError('Implicit state iteration cap')
        if u<=0 or not np.isfinite(u):raise ArithmeticError('Positive implicit branch required')
        u=u-f/(2*u)
    checkpoint('implicit-state-before-tangents',u=np.array(u),F=np.array(f))
    s=1/(2*u);r1=2*u*s-1
    checkpoint('implicit-first-before-second',u=np.array(u),s=np.array(s),R1=np.array(r1))
    t=-(2*s*s)/(2*u);r2=2*u*t+2*s*s
    curvature=.2+s*s+(u-1)*t
    checkpoint('implicit-second-before-fixed-partial',u=np.array(u),s=np.array(s),t=np.array(t),
               F=np.array(f),R1=np.array(r1),R2=np.array(r2),curvature=np.array(curvature))
    # Fixed-state partial is measured through the AD path, not copied from the oracle.
    fun=lambda th:.5*(u-1)*(u-1)+.1*th*th
    _,fixed,tape,_=hvp(fun,np.array(theta),np.array(1.))
    result={'u':u,'s':s,'t':t,'F':f,'R1':r1,'R2':r2,'total_curvature':curvature,
            'fixed_state_partial':float(fixed),'iterations':iterations,'work':tape.inventory()}
    checkpoint('implicit-completed-before-oracle',u=np.array(u),s=np.array(s),t=np.array(t),curvature=np.array(curvature))
    return result
