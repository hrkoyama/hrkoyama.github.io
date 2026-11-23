"""Spherical radial finite volumes: shared Rusanov fluxes and Heun steps."""
import numpy as np
GAMMA=5/3

class InvalidStage(ValueError):
    pass

def geometry(n,radius):
    if int(n)!=n or n<8 or radius<=0:raise ValueError('Invalid radial mesh')
    edges=np.linspace(0.,float(radius),int(n)+1)
    areas=4*np.pi*edges**2
    volumes=4*np.pi*np.diff(edges**3)/3
    return edges,areas,volumes

def primitive(q):
    if not np.all(np.isfinite(q)) or np.any(q[:,0]<=0):raise ValueError('Nonfinite state or nonpositive density')
    rho=q[:,0];u=q[:,1]/rho;kinetic=.5*q[:,1]*u;internal=q[:,2]-kinetic
    tolerance=64*np.finfo(float).eps*np.maximum(abs(q[:,2]),abs(kinetic))
    if np.any(internal < -tolerance):raise ValueError('Negative internal energy beyond roundoff')
    p=(GAMMA-1)*internal
    return rho,u,p,internal

def initial_state(edges,deposit_radius,energy=1.):
    if not 0<deposit_radius<edges[-1] or energy<=0:raise ValueError('Invalid deposition sphere')
    volumes=4*np.pi*np.diff(edges**3)/3
    overlap=4*np.pi*np.diff(np.minimum(edges,deposit_radius)**3)/3
    q=np.zeros((len(volumes),3));q[:,0]=1.
    q[:,2]=energy/(4*np.pi*deposit_radius**3/3)*overlap/volumes
    return q

def physical_flux(q):
    rho,u,p,_=primitive(q)
    return np.column_stack([q[:,1],q[:,1]*u+p,(q[:,2]+p)*u])

def rusanov(left,right):
    rl,ul,pl,_=primitive(left);rr,ur,pr,_=primitive(right)
    a=np.maximum(abs(ul)+np.sqrt(np.maximum(GAMMA*pl/rl,0.)),abs(ur)+np.sqrt(np.maximum(GAMMA*pr/rr,0.)))
    return .5*(physical_flux(left)+physical_flux(right))-.5*a[:,None]*(right-left)

def rhs(q,areas,volumes):
    rho,u,p,_=primitive(q)
    left=np.vstack([q[0]*[1,-1,1],q]);right=np.vstack([q,q[-1]])
    flux=rusanov(left,right)
    derivative=-(areas[1:,None]*flux[1:]-areas[:-1,None]*flux[:-1])/volumes[:,None]
    source=np.zeros_like(q);source[:,1]=p*np.diff(areas)/volumes
    derivative+=source
    boundary=areas[0]*flux[0]-areas[-1]*flux[-1]
    return derivative,boundary,np.sum(source*volumes[:,None],axis=0)

def solve(n=128,radius=1.,final_time=.05,cfl=.4,deposit_radius=.03,energy=1.):
    if final_time<=0 or not 0<cfl<=.5:raise ValueError('Invalid time budget/CFL')
    edges,areas,volumes=geometry(n,radius);q=initial_state(edges,deposit_radius,energy)
    initial=np.sum(q*volumes[:,None],axis=0);boundary=np.zeros(3);sources=np.zeros(3)
    history=[];t=0.;steps=0;minrho=1.;minp=0.;minround=0.
    def checked(state,label):
        nonlocal minrho,minp,minround
        try:rho,u,p,internal=primitive(state)
        except ValueError as original:
            err=InvalidStage(str(original));err.failed_state=state.copy();err.completed_history=list(history);err.failed_context={'stage':label,'step':steps,'time':t};raise err
        minrho=min(minrho,float(rho.min()));minp=min(minp,float(p.min()))
        denom=np.finfo(float).eps*abs(state[:,2])
        units=np.divide(internal,denom,out=np.zeros_like(internal),where=denom>0)
        minround=min(minround,float(np.min(units)))
    checked(q,'initial')
    while t<final_time:
        rho,u,p,_=primitive(q);speed=abs(u)+np.sqrt(np.maximum(GAMMA*p/rho,0.))
        ratios=np.divide(volumes/(areas[:-1]+areas[1:]),speed,out=np.full_like(speed,np.inf),where=speed>0)
        dt=min(float(cfl*np.min(ratios)),final_time-t)
        if not np.isfinite(dt) or dt<=0:raise ValueError('Invalid time step')
        k0,b0,s0=rhs(q,areas,volumes);predictor=q+dt*k0;checked(predictor,'predictor')
        k1,b1,s1=rhs(predictor,areas,volumes);candidate=.5*q+.5*(predictor+dt*k1);checked(candidate,'update')
        q=candidate;boundary+=.5*dt*(b0+b1);sources+=.5*dt*(s0+s1);t+=dt;steps+=1
        if steps%20==0 or t>=final_time:history.append({'step':steps,'time':t,'dt':dt,'min_density':float(q[:,0].min()),'total_energy':float(np.dot(q[:,2],volumes))})
        if steps>100000:raise ValueError('Step budget exhausted; no hidden retry')
    final=np.sum(q*volumes[:,None],axis=0)
    return {'q':q,'edges':edges,'volumes':volumes,'time':t,'steps':steps,'initial_integral':initial,'final_integral':final,'boundary_net_integral':boundary,'geometric_source_integral':sources,'history':history,'minimum_density':minrho,'minimum_pressure':minp,'minimum_internal_roundoff_units':minround,'state_floor_count':0}
