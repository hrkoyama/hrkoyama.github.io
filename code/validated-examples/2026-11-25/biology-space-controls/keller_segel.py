"""Smooth forced2D Keller--Segel transport; no aggregation/blow-up claim."""
from __future__ import annotations
import math
import numpy as np
from common import adaptive,maxerr,order
P=math.pi


def cosavg(N,k):
    x=(np.arange(N)+.5)/N
    return np.cos(k*P*x)*np.sinc(k/(2*N))


def exact(N,t):
    a=.1*math.exp(-t);b=.05*math.exp(-2*t)
    return np.array([1+a*np.outer(cosavg(N,1),cosavg(N,1)),1+b*np.outer(cosavg(N,1),cosavg(N,2))])


def expanded_source(cx,cy,t):
    a=.1*math.exp(-t);b=.05*math.exp(-2*t)
    C11=cx[1]*cy[1];C12=cx[1]*cy[2]
    chem=P*P*(-5*b*C12+a*b*(-.5*cy[1]-1.5*cy[3]-cx[2]*cy[1]-2*cx[2]*cy[3]))
    sn=a*(-1+.04*P*P+.1)*C11+a*P/2*(cx[2]-cy[2])+.2*chem+.1*a*a/4*(1+cx[2])*(1+cy[2])
    sc=b*(-1+.5*P*P)*C12-a*C11
    return np.array([sn,sc])


def source(N,t):
    return expanded_source({k:cosavg(N,k)[:,None] for k in [1,2,3]},
                           {k:cosavg(N,k)[None,:] for k in [1,2,3]},t)


def velocity(N):
    corner=np.arange(N+1)/N
    psi=np.sin(P*corner[:,None])*np.sin(P*corner[None,:])/P
    # Pin exact zero boundary streamfunction, not sin(pi) roundoff leakage.
    psi[[0,-1],:]=0;psi[:,[0,-1]]=0
    return (psi[:,1:]-psi[:,:-1])*N,-(psi[1:,:]-psi[:-1,:])*N


def primary_rhs(t,y,vel,forced=True,chi=.2,budget=None):
    if budget:budget.augment(stage="KS-SSPRK-RHS",stage_time=t,stage_input=y)
    N=y.shape[-1];h=1/N;n,c=y;wx,wy=vel
    jx=np.zeros((N+1,N));jy=np.zeros((N,N+1));kx=np.zeros_like(jx);ky=np.zeros_like(jy)
    jx[1:-1]=wx[1:-1]*(n[1:]+n[:-1])/2-.02*(n[1:]-n[:-1])/h+chi*(n[1:]+n[:-1])/2*(c[1:]-c[:-1])/h
    jy[:,1:-1]=wy[:,1:-1]*(n[:,1:]+n[:,:-1])/2-.02*(n[:,1:]-n[:,:-1])/h+chi*(n[:,1:]+n[:,:-1])/2*(c[:,1:]-c[:,:-1])/h
    kx[1:-1]=-.1*(c[1:]-c[:-1])/h;ky[:,1:-1]=-.1*(c[:,1:]-c[:,:-1])/h
    forcing=source(N,t) if forced else np.zeros_like(y)
    react=np.array([.1*n*(1-n),n-c]);divj=(jx[1:]-jx[:-1]+jy[:,1:]-jy[:,:-1])/h
    divk=(kx[1:]-kx[:-1]+ky[:,1:]-ky[:,:-1])/h
    out=np.array([-divj,-divk])+react+forcing
    return out,np.r_[react.sum(axis=(1,2))*h*h,forcing.sum(axis=(1,2))*h*h]


def reference_geometry(N):
    """Independent scalar trig integrals and scalar streamfunction face construction."""
    def mean_cos(k,i):
        if k==0:return 1.
        lo=i/N;hi=(i+1)/N
        return (math.sin(k*P*hi)-math.sin(k*P*lo))/(k*P*(hi-lo))
    terms=np.empty((7,N,N))
    for i in range(N):
        x1=mean_cos(1,i);x2=mean_cos(2,i);x11=(1+x2)/2;sx11=(1-x2)/2
        for j in range(N):
            y1=mean_cos(1,j);y2=mean_cos(2,j);y11=(1+y2)/2
            y12=(mean_cos(-1,j)+mean_cos(3,j))/2
            sy12=(mean_cos(-1,j)-mean_cos(3,j))/2
            terms[:,i,j]=[x1*y1,x1*y2,sx11*y12,2*x11*sy12,-5*x11*y12,x11*y11,
                          P/2*(x2-y2)]
    def psi(i,j):
        if i in [0,N] or j in [0,N]:return 0.
        return math.sin(P*i/N)*math.sin(P*j/N)/P
    vx=np.array([[(psi(i,j+1)-psi(i,j))*N for j in range(N)] for i in range(N+1)])
    vy=np.array([[(-psi(i+1,j)+psi(i,j))*N for j in range(N+1)] for i in range(N)])
    def forcing(t):
        a=.1*math.exp(-t);b=.05*math.exp(-2*t)
        # Unexpanded derivative/product integrals, independent of primary helpers.
        sn=-a*terms[0]+a*terms[6]+.04*P*P*a*terms[0]
        sn+=.2*P*P*(a*b*(terms[2]+terms[3]+terms[4])-5*b*terms[1])
        sn+=.1*a*terms[0]+.1*a*a*terms[5]
        sc=-2*b*terms[1]+.5*P*P*b*terms[1]-a*terms[0]+b*terms[1]
        return np.array([sn,sc])
    def rhs(t,z):
        y=z.reshape(2,N,N);n,c=y;f=forcing(t);out=np.empty_like(y)
        def face(axis,i,j):
            if axis==0:
                if i==0 or i==N:return 0.,0.
                nl=n[i-1,j];nr=n[i,j];cl=c[i-1,j];cr=c[i,j];v=vx[i,j]
            else:
                if j==0 or j==N:return 0.,0.
                nl=n[i,j-1];nr=n[i,j];cl=c[i,j-1];cr=c[i,j];v=vy[i,j]
            return v*(nl+nr)/2-.02*N*(nr-nl)+.2*N*(nl+nr)/2*(cr-cl),-.1*N*(cr-cl)
        for i in range(N):
            for j in range(N):
                l=face(0,i,j);r=face(0,i+1,j);b=face(1,i,j);u=face(1,i,j+1)
                out[0,i,j]=-N*(r[0]-l[0]+u[0]-b[0])+.1*n[i,j]*(1-n[i,j])+f[0,i,j]
                out[1,i,j]=-N*(r[1]-l[1]+u[1]-b[1])+n[i,j]-c[i,j]+f[1,i,j]
        return out.reshape(-1)
    return forcing,rhs,(vx,vy)


def trace(N,steps,budget,forced=True):
    dt=.25/steps;vel=velocity(N);y=exact(N,0) if forced else np.ones((2,N,N))
    mass0=y.mean(axis=(1,2));ledger=np.zeros(4);ys=[y.copy()];ts=[0.]
    allstates=[y.copy()] if N==24 else None
    minimum=y.min(axis=(1,2))
    for j in range(steps):
        t=j*dt;budget.tick('KS_primary_step');budget.tick('KS_primary_rhs',3)
        budget.own(case='Keller-Segel',N=N,step=j,state=y)
        k1,l1=primary_rhs(t,y,vel,forced,budget=budget);z=y+dt*k1
        k2,l2=primary_rhs(t+dt,z,vel,forced,budget=budget);w=.75*y+.25*(z+dt*k2)
        k3,l3=primary_rhs(t+dt/2,w,vel,forced,budget=budget)
        previous=y;y=y/3+2*(w+dt*k3)/3
        budget.augment(last_accepted_state=previous,candidate_state=y,stage='SSPRK3candidate',stage1=z,stage2=w)
        ledger+=dt*(l1/6+l2/6+2*l3/3)
        minimum=np.minimum(minimum,y.min(axis=(1,2)))
        if not np.all(np.isfinite(y)):raise FloatingPointError('NonfiniteKSstate')
        if (j+1)%(steps//4)==0:ys.append(y.copy());ts.append((j+1)*dt)
        if allstates is not None:allstates.append(y.copy())
    res=y.mean(axis=(1,2))-mass0-ledger[:2]-ledger[2:]
    return np.array(ts),np.stack(ys),None if allstates is None else np.stack(allstates),{
        'N':N,'steps':steps,'dt':dt,'minimum':minimum,'integrated_reaction':ledger[:2],
        'integrated_source':ledger[2:],'mass_residual':res,'mass_scale':1+np.abs(mass0)+np.abs(ledger[:2])+np.abs(ledger[2:])}


def point_reference(x,y,t):
    a=.1*math.exp(-t);b=.05*math.exp(-2*t)
    cx=math.cos(P*x);sx=math.sin(P*x);cy=math.cos(P*y);sy=math.sin(P*y)
    c2y=math.cos(2*P*y);s2y=math.sin(2*P*y)
    n=1+a*cx*cy;c=1+b*cx*c2y
    nt=-a*cx*cy;ct=-2*b*cx*c2y
    nx=-a*P*sx*cy;ny=-a*P*cx*sy
    ccx=-b*P*sx*c2y;ccy=-2*b*P*cx*s2y
    lapn=-2*P*P*a*cx*cy;lapc=-5*P*P*b*cx*c2y
    adv=sx*cy*nx-cx*sy*ny
    return np.array([nt+adv-.02*lapn+.2*(nx*ccx+ny*ccy+n*lapc)-.1*n*(1-n),ct-.1*lapc-n+c])


def components(budget,inputs):
    errors=[]
    for t in inputs['KS_probe_times']:
        for x,y in inputs['KS_source_probes']:
            ca={k:math.cos(k*P*x) for k in [1,2,3]};cb={k:math.cos(k*P*y) for k in [1,2,3]}
            p=expanded_source(ca,cb,t);r=point_reference(x,y,t)
            errors.append(maxerr(p,r)/(1+float(np.max(np.abs(r)))))
    force,ref,rv=reference_geometry(4);vel=velocity(4);rhs_errors=[]
    for t in [0.,.125,.25]:
        for state in [exact(4,t),np.ones((2,4,4))]:
            a=primary_rhs(t,state,vel,True)[0];b=ref(t,state.reshape(-1)).reshape(2,4,4)
            rhs_errors.append(maxerr(a,b)/(1+float(np.max(np.abs(b)))))
    probe=exact(4,.125);right=primary_rhs(.125,probe,vel,True)[0]
    wrong=primary_rhs(.125,probe,vel,True,chi=-.2)[0]
    omitted=right.copy();omitted[1]-=probe[0]
    stale=primary_rhs(.125+1/256,probe,vel,True)[0]
    div=(vel[0][1:]-vel[0][:-1]+vel[1][:,1:]-vel[1][:,:-1])*4
    # Zero prescribed externalflux cannot be added twice; deliberately inject one.
    duplicate=right.copy();duplicate[0,0,0]-=1e-3*4
    return {'source_point_pairs36':max(errors)<=1e-10,'wholegrid_RHS_vectorpairs96':max(rhs_errors)<=1e-10,
            'divergence_free_faces':float(np.max(np.abs(div)))<=2e-14,
            'independent_velocity':max(maxerr(a,b) for a,b in zip(vel,rv))<=1e-14,
            'wrong_chi_detected':maxerr(right,wrong)>1e-5,'omitted_coupling_detected':maxerr(right,omitted)>.1,
            'stale_source_time_detected':maxerr(right,stale)>1e-5,'duplicated_external_face_detected':maxerr(right,duplicate)>1e-4},errors,rhs_errors


def run(rec,budget,inputs):
    checks,probes,rhs_errors=components(budget,inputs)
    for k,v in checks.items():rec.check('KS/'+k,v)
    rec.row('KS-components',{'source_probe_errors':probes,'wholegrid_RHS_errors':rhs_errors,
            'zero_frequency_integral':'mean cos0=1; cosacosb=.5(cos(a-b)+cos(a+b)); sinasinb=.5(cos(a-b)-cos(a+b))',
            'continuum_integrals':'integraln=integralc=1; integralreactionn=-r*A²/4; integralsn=+r*A²/4; integralsc=0'})
    spatial=[];states={}
    for N in [12,24,48]:
        ts,ys,allstates,diag=trace(N,1024,budget);truth=np.array([exact(N,t) for t in ts]);err=np.max(np.abs(ys-truth),axis=(0,2,3));spatial.append(err);states[N]=ys
        rec.row('KS-space-N'+str(N),{**diag,'Linf_fields':err},time=ts,state=ys,exact=truth)
        rec.check('KS/massledger/'+str(N),np.max(np.abs(diag['mass_residual'])/diag['mass_scale'])<=2e-10)
        rec.goal('KS/minimum/'+str(N),diag['minimum'][0]>=.88 and diag['minimum'][1]>=.93,minimum=diag['minimum'])
    ts=np.arange(65)/256;f,ref,_=reference_geometry(24);refs=[];ledgers=[]
    for rt,at in [(2e-10,1e-12),(5e-12,2e-14)]:
        budget.own(case='KS-same-MOL-reference',N=24,rtol=rt,atol=at)
        yy,ll=adaptive(ref,exact(24,0).reshape(-1),ts,budget,rt,at,4000,first_step=1e-4)
        refs.append(yy.reshape(-1,2,24,24));ledgers.append(ll)
    spread=maxerr(*refs);qualified=spread<=1e-8;rec.check('KS/reference',qualified)
    rec.row('KS-time-reference',{'qualified':qualified,'spread':spread,'solvers':ledgers,
            'scope':'Same24x24MOL, scalar face ownership and independent unexpanded analytic cellsource'},time=ts,state=refs[-1],companion=refs[0])
    terr=[]
    for steps in [64,128,256]:
        ts0,ys,allstates,diag=trace(24,steps,budget)
        compared=allstates[::steps//64];err=maxerr(compared,refs[-1]);terr.append(err)
        rec.row('KS-time-'+str(steps),{**diag,'same_MOL_error':err},time=ts,state=compared,reference=refs[-1])
    oo=order(terr[-2],terr[-1],max(20*spread,1e-13))
    rec.goal('KS/time-order',oo>=2.5 if qualified and oo is not None else None,actual=oo,target=2.5)
    _,fine,_,diag=trace(48,2048,budget)
    contam=maxerr(fine,states[48]);rec.row('KS-halfdt-N48',diag,time=np.array([0,.0625,.125,.1875,.25]),state=fine)
    for k in range(2):
        ee=[float(e[k]) for e in spatial];oo=order(ee[-2],ee[-1],max(20*spread,1e-13))
        rec.goal('KS/space-finest/'+str(k),ee[-1]<=.002,actual=ee[-1],target=.002)
        rec.goal('KS/space-order/'+str(k),oo>=1.7 if oo is not None else None,actual=oo,target=1.7)
    rec.goal('KS/time-contamination',contam<=.1*float(max(spatial[-1])),actual=contam,finest_spatial_error=float(max(spatial[-1])))
    ts0,control,_,diag=trace(24,256,budget,False)
    rec.row('KS-constant-unforced',diag,time=ts0,state=control)
    rec.check('KS/constant-control',maxerr(control,np.ones_like(control))<=1e-12)
