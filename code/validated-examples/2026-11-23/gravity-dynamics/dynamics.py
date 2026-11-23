"""Isolated N-body KDK with direct or original full-second-moment BH force.

No post-step recentering, floor, adaptive step, retry or energy repair.
BH formulas follow the existing original atlas implementation, not library code.
"""
from dataclasses import dataclass
import numpy as np

class StateFailure(ArithmeticError):
    def __init__(self,message,**payload):super().__init__(message);self.payload=payload

def direct(x,m,epsilon):
    x=np.asarray(x);m=np.asarray(m);d=x[:,None,:]-x[None,:,:];r2=np.sum(d*d,axis=2)+epsilon**2
    selfmask=np.eye(len(x),dtype=bool)
    if epsilon<0 or np.any((r2==0)&~selfmask):raise ValueError('Invalid softening or collision')
    r2[selfmask]=np.inf
    return -np.einsum('ij,ijk->ik',m[None,:]/r2**1.5,d,optimize=False),dict(accepted_nodes=0,direct_pairs=len(x)*(len(x)-1))

@dataclass
class Node:
    ids:object;center:object;half:float;mass:float;com:object;second:object;children:list

def build(x,m,ids,center,half,depth=0):
    mass=float(m[ids].sum());com=np.sum(m[ids,None]*x[ids],axis=0)/mass;v=x[ids]-com;second=np.einsum('n,ni,nj->ij',m[ids],v,v,optimize=False);children=[]
    if len(ids)>1 and depth<32 and half>1e-14:
        codes=np.sum((x[ids]>=center)*[1,2,4],axis=1)
        for k in range(8):
            selected=ids[codes==k]
            if len(selected):children.append(build(x,m,selected,center+np.array([1 if k&(1<<a) else -1 for a in range(3)])*half/2,half/2,depth+1))
    return Node(ids,center,half,mass,com,second,children)

def tree(x,m,epsilon,theta=.6):
    if epsilon<=0 or theta<0:raise ValueError('BH uses positive softening and nonnegative opening')
    center=(x.max(axis=0)+x.min(axis=0))/2;half=max(float(np.ptp(x,axis=0).max())/2,1e-10)*(1+1e-12);root=build(x,m,np.arange(len(x)),center,half);a=np.zeros_like(x);counts=dict(accepted_nodes=0,direct_pairs=0)
    for i,t in enumerate(x):
        stack=[root]
        while stack:
            n=stack.pop();r=t-n.com;distance=float(np.sqrt(np.sum(r*r)));contains=np.all(abs(t-n.center)<=n.half*(1+1e-12))
            if n.children and not contains and distance>0 and 2*n.half/distance<theta:
                s2=float(np.sum(r*r)+epsilon**2);s=np.sqrt(s2);sr=np.einsum('ij,j->i',n.second,r,optimize=False);moment=float(np.sum(r*sr));trace=float(np.trace(n.second))
                a[i]+=-n.mass*r/s**3+3*sr/s**5-7.5*moment*r/s**7+1.5*trace*r/s**5;counts['accepted_nodes']+=1
            elif n.children:stack.extend(n.children)
            else:
                ids=n.ids[n.ids!=i];d=t-x[ids];r2=np.sum(d*d,axis=1)+epsilon**2;a[i]-=np.sum(m[ids,None]*d/r2[:,None]**1.5,axis=0);counts['direct_pairs']+=len(ids)
    return a,counts

def diagnostics(x,v,m,epsilon):
    d=x[:,None,:]-x[None,:,:];r2=np.sum(d*d,axis=2)+epsilon**2;np.fill_diagonal(r2,np.inf)
    U=-.5*np.sum(m[:,None]*m[None,:]/np.sqrt(r2));K=.5*np.sum(m[:,None]*v*v)
    return np.r_[K+U,np.sum(m[:,None]*v,axis=0),np.sum(m[:,None]*np.cross(x,v),axis=0),np.sum(m[:,None]*x,axis=0)/m.sum(),np.sqrt(np.min(r2-epsilon**2))]

def integrate(x,v,m,epsilon,final,steps,theta=None,budget=None):
    x=np.array(x,float);v=np.array(v,float);m=np.array(m,float);dt=final/steps
    force=lambda X:direct(X,m,epsilon) if theta is None else tree(X,m,epsilon,theta)
    try:a,c=force(x)
    except Exception as error:raise StateFailure(str(error),candidate_x=x,candidate_v=v,time=0.,dt=dt,step=0) from error
    if not np.isfinite(a).all():raise StateFailure('Nonfinite initial force',candidate_x=x,candidate_v=v,acceleration=a,time=0.,dt=dt,step=0)
    xs=[x.copy()];vs=[v.copy()];diag=[diagnostics(x,v,m,epsilon)];forces=[a.copy()];counts=[list(c.values())]
    for step in range(steps):
        if budget is not None:
            try:budget.check()
            except TimeoutError as error:raise StateFailure(str(error),candidate_x=x,candidate_v=v,acceleration=a,time=step*dt,dt=dt,step=step,positions=np.array(xs),velocities=np.array(vs),diagnostics=np.array(diag)) from error
        vh=v+.5*dt*a;xx=x+dt*vh
        try:aa,c=force(xx)
        except Exception as error:raise StateFailure(str(error),previous_x=x,previous_v=v,candidate_x=xx,half_velocity=vh,time=step*dt,dt=dt,step=step,positions=np.array(xs),velocities=np.array(vs)) from error
        vv=vh+.5*dt*aa
        if not np.isfinite(xx).all() or not np.isfinite(vv).all():raise StateFailure('Nonfinite KDK state',candidate_x=xx,candidate_v=vv,acceleration=aa,time=(step+1)*dt,step=step,positions=np.array(xs),velocities=np.array(vs))
        x,v,a=xx,vv,aa;xs.append(x.copy());vs.append(v.copy());forces.append(a.copy());diag.append(diagnostics(x,v,m,epsilon));counts.append(list(c.values()))
    return dict(times=np.linspace(0,final,steps+1),positions=np.array(xs),velocities=np.array(vs),accelerations=np.array(forces),diagnostics=np.array(diag),work_counts=np.array(counts),masses=m,epsilon=epsilon)
