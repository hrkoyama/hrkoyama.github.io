"""Analytic binary ephemeris and independently coded scalar finite-N ODE."""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import solve_ivp

class ReferenceFailure(ArithmeticError):
    def __init__(self,message,**payload):super().__init__(message);self.payload=payload

def pair_force(x,m,epsilon):
    a=np.zeros_like(x)
    for i in range(len(x)):
        for j in range(i):
            d=[float(x[i,k]-x[j,k]) for k in range(3)];r2=sum(z*z for z in d)+epsilon*epsilon
            if r2==0:raise ValueError('Unsoftened collision')
            s=r2**1.5
            for k in range(3):a[i,k]-=m[j]*d[k]/s;a[j,k]+=m[i]*d[k]/s
    return a

def potential(x,m,epsilon):
    total=0.
    for i in range(len(x)):
        for j in range(i):total-=float(m[i]*m[j])/math.sqrt(sum(float(x[i,k]-x[j,k])**2 for k in range(3))+epsilon*epsilon)
    return total

def kepler(times,m,a=1.,e=.4):
    mass=float(sum(m));n=math.sqrt(mass/a**3);positions=[];velocities=[];residual=[]
    for t in times:
        mean=n*float(t);E=brentq(lambda E:E-e*math.sin(E)-mean,mean-e,mean+e,xtol=1e-14,rtol=1e-14);residual.append(abs(E-e*math.sin(E)-mean))
        r=a*np.array([math.cos(E)-e,math.sqrt(1-e*e)*math.sin(E),0.]);v=n*a/(1-e*math.cos(E))*np.array([-math.sin(E),math.sqrt(1-e*e)*math.cos(E),0.]);weights=np.array([-m[1]/mass,m[0]/mass])
        positions.append(weights[:,None]*r);velocities.append(weights[:,None]*v)
    return np.array(positions),np.array(velocities),np.array(residual)

def reference(x,v,m,epsilon,times,rtol,atol,budget=None):
    n=len(x)
    def rhs(t,z):
        if budget is not None:
            try:budget.check()
            except TimeoutError as error:raise ReferenceFailure(str(error),time=t,reference_candidate=z,masses=m,epsilon=epsilon) from error
        xx=z[:3*n].reshape(n,3);vv=z[3*n:].reshape(n,3)
        return np.r_[vv.ravel(),pair_force(xx,m,epsilon).ravel()]
    answer=solve_ivp(rhs,(0,float(times[-1])),np.r_[x.ravel(),v.ravel()],method='DOP853',t_eval=times,rtol=rtol,atol=atol)
    if not answer.success or not np.isfinite(answer.y).all():raise ArithmeticError('Independent finite-N reference failed')
    return answer.y[:3*n].T.reshape(-1,n,3),answer.y[3*n:].T.reshape(-1,n,3),dict(nfev=answer.nfev,times=answer.t,rtol=rtol,atol=atol)
