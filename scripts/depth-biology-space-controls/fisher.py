"""Fisher--KPP special-speed front, distinct space/time/boundary experiments."""
from __future__ import annotations
import math
import numpy as np
from common import adaptive, maxerr, order


def exact(x,t,c=None):
    a=1/math.sqrt(6);c=5/math.sqrt(6) if c is None else c
    return (1+np.exp(a*(np.asarray(x)-c*t)))**-2


def contour(x,u):
    ids=np.flatnonzero((u[:-1]>=.25)&(u[1:]<.25))
    if len(ids)!=1:return None
    j=int(ids[0]);return float(x[j]+(.25-u[j])*(x[j+1]-x[j])/(u[j+1]-u[j]))


def step(y,t,dt,x,h,boundary,budget):
    def rhs(tt,z):
        budget.augment(stage='Fisher-SSPRK-RHS',stage_time=tt,stage_input=z)
        budget.tick('fisher_primary_rhs')
        full=np.empty(len(z)+2);full[1:-1]=z
        if boundary=='exact':full[[0,-1]]=exact(x[[0,-1]],tt)
        else:full[0]=1.;full[-1]=0.
        return (full[:-2]-2*z+full[2:])/h**2+z*(1-z)
    a=rhs(t,y);z=y+dt*a
    b=rhs(t+dt,z);w=.75*y+.25*(z+dt*b)
    c=rhs(t+dt/2,w)
    return y/3+2*(w+dt*c)/3


def trace(L,h,steps,boundary,budget):
    count=int(round(2*L/h));x=np.arange(count+1)*h-L;dt=1/steps
    y=exact(x[1:-1],0);saved=[];times=[];fullrows=[]
    initial_mismatch=[float(1-exact(-L,0)),float(exact(L,0))] if boundary!='exact' else [0.,0.]
    for j in range(steps+1):
        if j==0 or j%max(1,steps//4)==0:
            full=np.r_[exact(-L,j*dt) if boundary=='exact' else 1.,y,
                       exact(L,j*dt) if boundary=='exact' else 0.]
            saved.append(full);times.append(j*dt)
        if j==steps:break
        budget.tick('fisher_primary_step');budget.own(case='Fisher',L=L,h=h,step=j,state=y)
        previous=y;y=step(y,j*dt,dt,x,h,boundary,budget)
        budget.augment(last_accepted_state=previous,candidate_state=y,stage='SSPRK3candidate')
        if not np.all(np.isfinite(y)):raise FloatingPointError('Nonfinite Fisher state')
        fullrows.append(y.copy())
    return x,np.array(times),np.stack(saved),np.vstack([exact(x[1:-1],0),*fullrows]),initial_mismatch


def reference_rhs(x,h):
    nodes=list(map(float,x))
    def f(t,u):
        # Independently scalar-owned boundary forcing and tridiagonal operator.
        out=[];left=float((1+math.exp((nodes[0]-5/math.sqrt(6)*t)/math.sqrt(6)))**-2)
        right=float((1+math.exp((nodes[-1]-5/math.sqrt(6)*t)/math.sqrt(6)))**-2)
        for j,v in enumerate(u):
            lo=left if j==0 else u[j-1]
            hi=right if j+1==len(u) else u[j+1]
            out.append((lo-2*v+hi)/(h*h)+v-v*v)
        return np.array(out)
    return f


def run(rec,budget,inputs):
    a=1/math.sqrt(6);c=5/math.sqrt(6)
    xx=np.linspace(-3,3,19);z=np.exp(a*(xx-c*.3));u=(1+z)**-2
    uxxt=-2*a*a*z/(1+z)**3+6*a*a*z*z/(1+z)**4
    ut=2*a*c*z/(1+z)**3;wrong=2*a*2*z/(1+z)**3
    rec.check('Fisher/exact-PDE',maxerr(ut-uxxt-u*(1-u),np.zeros_like(u))<5e-15)
    rec.check('Fisher/wrong-special-speed-detected',float(np.max(np.abs(wrong-uxxt-u*(1-u))))>1e-4)
    rec.row('fisher-components',{'special_speed':c,'minimum_linear_speed':2.,'same_profile_speed2_not_exact':True,
            'real_arithmetic_boundary_barrier':'2exp(sigma-18), sigma=1+128(cosh(.25)-1)<6 -> <1e-4',
            'floating_point_certificate':False,'barrier_scope':'L12vsL24,constantends,|x|<=3,real discrete maximum principle'})
    space=[];data={}
    for h in [.5,.25,.125]:
        steps=int(round(20/h**2));x,t,ys,allstates,mismatch=trace(12,h,steps,'exact',budget)
        truth=np.array([exact(x,tt) for tt in t]);err=maxerr(ys,truth);space.append(err)
        rec.row('fisher-space-'+str(h).replace('.','p'),{'h':h,'steps':steps,'Linf':err,'quarter_contour':contour(x,ys[-1]),
                'min':float(ys.min()),'max':float(ys.max()),'Euler_monotonicity_bound':2*(1/steps)/h**2+1/steps},
                x=x,time=t,state=ys,exact=truth,all_time=np.arange(steps+1)/steps,all_interior=allstates)
        rec.check('Fisher/finite-space/'+str(h),np.all(np.isfinite(ys)) and ys.min()>=-1e-12 and ys.max()<=1+1e-12)
        data[h]=(x,ys)
    rec.goal('Fisher/space-finest',space[-1]<=1e-3,actual=space[-1],target=1e-3)
    oo=order(space[-2],space[-1]);rec.goal('Fisher/space-order',oo>=1.7 if oo is not None else None,actual=oo,target=1.7)
    phase=contour(data[.125][0],data[.125][1][-1]);pe=abs(phase-c) if phase is not None else None
    rec.goal('Fisher/phase',pe<=.02 if pe is not None else None,actual=pe,target=.02)
    h=.25;x=np.arange(97)*h-12.;ts=np.arange(401)/400
    refs=[];ledgers=[]
    for rtol,atol in [(1e-11,1e-13),(1e-13,1e-15)]:
        budget.own(case='Fisher-same-MOL-reference',rtol=rtol,atol=atol)
        yy,ll=adaptive(reference_rhs(x,h),exact(x[1:-1],0),ts,budget,rtol,atol,20000,first_step=1e-4)
        refs.append(yy);ledgers.append(ll)
    spread=maxerr(*refs);qualified=spread<=1e-8
    rec.check('Fisher/semidiscrete-reference',qualified)
    rec.row('fisher-time-reference',{'qualified':qualified,'spread':spread,'solvers':ledgers,
            'scope':'The SAME95interior-nodeMOL, not continuumexactfront'},time=ts,state=refs[-1],companion=refs[0],x=x[1:-1])
    terr=[]
    for steps in [100,200,400]:
        x,t,ys,allstates,_=trace(12,h,steps,'exact',budget)
        ref=refs[-1][::400//steps];err=maxerr(allstates,ref);terr.append(err)
        rec.row('fisher-time-'+str(steps),{'steps':steps,'dt':1/steps,'same_MOL_error':err},
                time=np.arange(steps+1)/steps,state=allstates,reference=ref,x=x[1:-1])
    to=order(terr[-2],terr[-1],max(20*spread,1e-13))
    rec.goal('Fisher/time-order',to>=2.7 if to is not None and qualified else None,actual=to,target=2.7,reference_spread=spread)
    rec.goal('Fisher/time-finest',terr[-1]<=1e-5 if qualified else None,actual=terr[-1],target=1e-5)
    bdata={}
    for L in [6,12,24]:
        x,t,ys,allstates,mismatch=trace(L,.125,1280,'constant',budget)
        truth=np.array([exact(x,tt) for tt in t]);core=np.abs(x)<=3
        rec.row('fisher-boundary-'+str(L),{'L':L,'h':.125,'steps':1280,'core_error':maxerr(ys[:,core],truth[:,core]),
                'full_error':maxerr(ys,truth),'initial_boundary_mismatch':mismatch},x=x,time=t,state=ys,exact=truth)
        bdata[L]=(x,ys)
    x12,u12=bdata[12];x24,u24=bdata[24];core=np.abs(x12)<=3
    start=int(round((24-12)/.125));matched=u24[:,start:start+len(x12)]
    margin=1e-4-maxerr(u12[:,core],matched[:,core])
    rec.goal('Fisher/observed-boundary-margin',margin>=0,observed_margin=margin,
             scope='Observed binary64 margin; analyticreal-arithmetic barrier is not a machine-error certificate')
