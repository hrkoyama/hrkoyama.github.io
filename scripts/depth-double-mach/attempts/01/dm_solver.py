"""Budget-instrumented first-order HLL/Heun Double Mach baseline.

Derived from the already published Numart Euler2D baseline.  Both Cartesian
flux divergences are evolved; no radial reduction, state repair or retries.
The original cell-center shock classification and boundary definitions stay
unchanged. All state arrays use [x,y,(rho,rho*u,rho*v,E)].
"""
import numpy as np

GAMMA=1.4

class InvalidStage(ValueError):
    pass

def conserved(w):
    rho,u,v,p=np.moveaxis(np.asarray(w,dtype=float),-1,0)
    return np.stack((rho,rho*u,rho*v,p/(GAMMA-1)+.5*rho*(u*u+v*v)),axis=-1)

def primitive(q):
    q=np.asarray(q)
    if not np.all(np.isfinite(q)) or np.any(q[...,0]<=0):raise ValueError('Invalid density/nonfinite state')
    rho=q[...,0];u=q[...,1]/rho;v=q[...,2]/rho
    p=(GAMMA-1)*(q[...,3]-.5*(q[...,1]*u+q[...,2]*v))
    if np.any(p<=0) or not np.all(np.isfinite(p)):raise ValueError('Nonpositive pressure')
    return np.stack((rho,u,v,p),axis=-1)

def flux(q,axis):
    w=primitive(q);normal=w[...,1+axis]
    f=q*normal[...,None];f[...,1+axis]+=w[...,3]
    f[...,3]=(q[...,3]+w[...,3])*normal
    return f

def hll(left,right,axis):
    a,b=primitive(left),primitive(right)
    al=np.sqrt(GAMMA*a[...,3]/a[...,0]);ar=np.sqrt(GAMMA*b[...,3]/b[...,0])
    sl=np.minimum(np.minimum(a[...,1+axis]-al,b[...,1+axis]-ar),0.)
    sr=np.maximum(np.maximum(a[...,1+axis]+al,b[...,1+axis]+ar),0.)
    fl,fr=flux(left,axis),flux(right,axis)
    return (sr[...,None]*fl-sl[...,None]*fr+(sl*sr)[...,None]*(right-left))/(sr-sl)[...,None]

def states():
    return conserved([8.,8.25*np.sqrt(3)/2,-4.125,116.5]),conserved([1.4,0.,0.,1.])

def initial(ny):
    if not isinstance(ny,int) or ny<8:raise ValueError('Ny must be integer >=8')
    x=(np.arange(4*ny)+.5)/ny;y=(np.arange(ny)+.5)/ny
    hot,cold=states();q=np.where((x[:,None]<1/6+y[None,:]/np.sqrt(3))[...,None],hot,cold)
    return x,y,q

def ghost(q,time,x):
    hot,cold=states();g=np.pad(q,((1,1),(1,1),(0,0)),mode='edge')
    g[0,:,:]=hot
    g[1:-1,0,:]=q[:,0,:];g[1:-1,0,2]*=-1
    g[1:-1,0,:]=np.where((x<1/6)[:,None],hot,g[1:-1,0,:])
    line=1/6+(1+20*time)/np.sqrt(3)
    g[1:-1,-1,:]=np.where((x<line)[:,None],hot,cold)
    return g

def rhs(q,time,x,spacing):
    g=ghost(q,time,x)
    fx=hll(g[:-1,1:-1],g[1:,1:-1],0)
    fy=hll(g[1:-1,:-1],g[1:-1,1:],1)
    derivative=-(fx[1:]-fx[:-1])/spacing-(fy[:,1:]-fy[:,:-1])/spacing
    inward=spacing*(fx[0].sum(axis=0)-fx[-1].sum(axis=0)+fy[:,0].sum(axis=0)-fy[:,-1].sum(axis=0))
    return derivative,inward

def solve(ny=64,final_time=.2,cfl=.4):
    if not np.isfinite(final_time) or final_time<=0 or not 0<cfl<=.4:raise ValueError('Invalid fixed time/CFL')
    x,y,q=initial(ny);spacing=1/ny;area=spacing**2
    initial_integral=area*q.sum(axis=(0,1));boundary=np.zeros(4)
    time=0.;steps=0;history=[];minimum_density=float('inf');minimum_pressure=float('inf')
    def checked(state,stage):
        nonlocal minimum_density,minimum_pressure
        try:w=primitive(state)
        except ValueError as original:
            e=InvalidStage(str(original));e.failed_state=state.copy();e.completed_history=list(history)
            e.failed_context={'stage':stage,'step':steps,'time':time};raise e
        minimum_density=min(minimum_density,float(w[...,0].min()))
        minimum_pressure=min(minimum_pressure,float(w[...,3].min()))
        return w
    checked(q,'initial')
    while time<final_time:
        w=primitive(q);sound=np.sqrt(GAMMA*w[...,3]/w[...,0])
        rate=(np.max(abs(w[...,1])+sound)+np.max(abs(w[...,2])+sound))/spacing
        dt=min(cfl/rate,final_time-time)
        if not np.isfinite(dt) or dt<=0:raise ValueError('Invalid time step')
        f0,b0=rhs(q,time,x,spacing);predictor=q+dt*f0;checked(predictor,'predictor')
        f1,b1=rhs(predictor,time+dt,x,spacing);updated=.5*q+.5*(predictor+dt*f1);checked(updated,'update')
        q=updated;boundary+=.5*dt*(b0+b1);time+=dt;steps+=1
        if steps%20==0 or time>=final_time:history.append({'step':steps,'time':time,'dt':dt,'min_density':minimum_density,'min_pressure':minimum_pressure})
        if steps>100000:raise ValueError('Step budget exceeded; no hidden retry')
    return {'q':q,'x':x,'y':y,'time':time,'steps':steps,'history':history,
            'initial_integral':initial_integral,'final_integral':area*q.sum(axis=(0,1)),
            'boundary_net_integral':boundary,'minimum_density':minimum_density,
            'minimum_pressure':minimum_pressure,'state_floor_count':0,'rejected_steps':0}
