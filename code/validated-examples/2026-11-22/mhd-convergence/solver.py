"""Matched planar ideal-MHD finite volumes, mu0=1, gamma=5/3.

Original educational implementation, following the earlier Atlas planar solver.
Both methods use piecewise-constant reconstruction, a fixed identical LLF
speed, and forward Euler with identical prescribed dt. CT uses a shared
arithmetic flux-CT corner EMF. GLM evolves cell B and psi with fixed physical
ch and kappa. The energy is physical MHD E (no psi energy); no energy reset,
Powell terms, clipping, timestep retry, or adaptive parameter is used.
"""
import math
import time
import numpy as np


class Budget:
    def __init__(self, seconds=110.):
        if isinstance(seconds, bool) or not math.isfinite(seconds) or not 0 < seconds <= 115:
            raise ValueError('Finite wall-clock budget in (0,115] required')
        self.deadline = time.perf_counter()+seconds

    def check(self):
        if time.perf_counter() >= self.deadline:
            raise RuntimeError('MHD convergence wall-clock budget exhausted')


def primitive(q, gamma=5/3):
    if not np.all(np.isfinite(q)) or np.any(q[...,0] <= 0):
        raise ValueError('Nonfinite MHD state or nonpositive density')
    rho=q[...,0];vx=q[...,1]/rho;vy=q[...,2]/rho
    bx=q[...,4];by=q[...,5]
    pressure=(gamma-1)*(q[...,3]-.5*(q[...,1]**2+q[...,2]**2)/rho-.5*(bx*bx+by*by))
    if np.any(pressure <= 0):
        raise ValueError('Nonpositive MHD pressure; no clipping or hidden retry')
    return rho,vx,vy,pressure,bx,by


def exact_smooth(n,t,cfg,gamma=5/3):
    """Exact conserved cell averages, not primitive values at cell centres."""
    x=(np.arange(n)+.5)/n
    phase_x=2*np.pi*(x[:,None]-cfg['velocity'][0]*t)
    phase_y=2*np.pi*(x[None,:]-cfg['velocity'][1]*t)
    s=np.sinc(1/n);s2=np.sinc(2/n);a=cfg['amplitude'];k=2*np.pi
    avg_a2=a*a*(1+.5*s2*(np.cos(2*phase_x)+np.cos(2*phase_y))+2*s*s*np.cos(phase_x)*np.cos(phase_y))
    avg_b2=(a*k)**2*(1-.5*s2*(np.cos(2*phase_x)+np.cos(2*phase_y)))
    q=np.zeros((n,n,7));rho=cfg['density'];u,v=cfg['velocity']
    q[...,0]=rho;q[...,1]=rho*u;q[...,2]=rho*v
    q[...,3]=(cfg['base_pressure']+.5*k*k*avg_a2)/(gamma-1)+.5*rho*(u*u+v*v)+.5*avg_b2
    q[...,4]=-a*k*s*np.sin(phase_y);q[...,5]=a*k*s*np.sin(phase_x)
    return q


def initial_ot(n,gamma=5/3):
    """Analytic conserved averages of the standard continuous OT fields."""
    x=2*np.pi*(np.arange(n)+.5)/n
    px=x[:,None];py=x[None,:];s=np.sinc(1/n)
    rho=25/(36*np.pi);p=5/(12*np.pi);b=1/np.sqrt(4*np.pi)
    v2=1-.5*np.sinc(2/n)*(np.cos(2*px)+np.cos(2*py))
    b2=b*b*(1-.5*np.sinc(2/n)*np.cos(2*py)-.5*np.sinc(4/n)*np.cos(4*px))
    q=np.zeros((n,n,7));q[...,0]=rho
    q[...,1]=-rho*s*np.sin(py);q[...,2]=rho*s*np.sin(px)
    q[...,3]=p/(gamma-1)+.5*rho*v2+.5*b2
    q[...,4]=-b*s*np.sin(py);q[...,5]=b*np.sinc(2/n)*np.sin(2*px)
    return q


def initial_q(case,n,cfg):
    if case=='smooth':return exact_smooth(n,0.,cfg)
    if case=='ot':return initial_ot(n)
    if case=='constraint':
        x=2*np.pi*(np.arange(n)+.5)/n
        q=np.zeros((n,n,7));q[...,0]=cfg['density']
        q[...,4]=cfg['amplitude']*np.cos(np.pi/n)*np.cos(x[:,None])
        q[...,3]=cfg['pressure']/(5/3-1)+.5*q[...,4]**2
        return q
    raise ValueError('Unknown initial condition')


def pack(q,method):
    if method=='ct':
        # Each initial B component depends only on the transverse coordinate;
        # the analytic face average equals its volume average in this case.
        return np.concatenate((q[...,:4],q[...,4:6]),axis=-1).copy()
    if method=='glm':return q.copy()
    raise ValueError('method must be ct or glm')


def unpack(state,method):
    if method=='glm':return state
    q=np.zeros((*state.shape[:2],7));q[...,:4]=state[...,:4]
    q[...,4]=.5*(state[...,4]+np.roll(state[...,4],1,axis=0))
    q[...,5]=.5*(state[...,5]+np.roll(state[...,5],1,axis=1))
    return q


def flux(q,axis,ch,alpha,gamma):
    rho,vx,vy,p,bx,by=primitive(q,gamma)
    v,b=(vx,bx) if axis==0 else (vy,by)
    b2=bx*bx+by*by;pt=p+.5*b2
    f=np.zeros_like(q);f[...,0]=rho*v
    f[...,1]=q[...,1]*v-bx*b;f[...,2]=q[...,2]*v-by*b
    f[...,1+axis]+=pt
    f[...,3]=(q[...,3]+pt)*v-b*(vx*bx+vy*by)
    f[...,4]=v*bx-vx*b;f[...,5]=v*by-vy*b
    f[...,4+axis]=q[...,6] if ch else 0.
    f[...,6]=ch*ch*b
    a2=gamma*p/rho;va2=b2/rho
    cf=np.sqrt(.5*(a2+va2+np.sqrt(np.maximum((a2+va2)**2-4*a2*b*b/rho,0.))))
    maximum=float(np.max(abs(v)+cf))
    if maximum > alpha*(1+2e-14):
        raise ValueError('Predeclared common LLF wave-speed bound was exceeded')
    return f,maximum


def interfaces(q,axis,ch,alpha,gamma,normal=None):
    left=q.copy();right=np.roll(q,-1,axis=axis).copy()
    if normal is not None:
        for w in (left,right):
            w[...,3]+=.5*(normal*normal-w[...,4+axis]**2)
            w[...,4+axis]=normal
    fl,al=flux(left,axis,ch,alpha,gamma);fr,ar=flux(right,axis,ch,alpha,gamma)
    return .5*(fl+fr-alpha*(right-left)),max(al,ar)


def rhs(state,method,model,budget=None):
    if budget is not None:budget.check()
    n=state.shape[0];q=unpack(state,method)
    alpha=model['wave_speed_bound'];ch=alpha if method=='glm' else 0.
    fx,ax=interfaces(q,0,ch,alpha,model['gamma'],state[...,4] if method=='ct' else None)
    fy,ay=interfaces(q,1,ch,alpha,model['gamma'],state[...,5] if method=='ct' else None)
    r=-n*(fx-np.roll(fx,1,axis=0)+fy-np.roll(fy,1,axis=1))
    if method=='ct':
        ez=.25*(-fx[...,5]-np.roll(fx[...,5],-1,axis=1)+fy[...,4]+np.roll(fy[...,4],-1,axis=0))
        result=np.empty_like(state);result[...,:4]=r[...,:4]
        result[...,4]=-n*(ez-np.roll(ez,1,axis=1))
        result[...,5]=n*(ez-np.roll(ez,1,axis=0))
    else:
        result=r;result[...,6]-=model['cleaning_rate']*state[...,6]
    return result


def divergence(state,method):
    n=state.shape[0]
    if method=='ct':
        return n*(state[...,4]-np.roll(state[...,4],1,axis=0)+state[...,5]-np.roll(state[...,5],1,axis=1))
    return common_divergence(state)


def common_divergence(q):
    n=q.shape[0]
    return .5*n*(np.roll(q[...,4],-1,axis=0)-np.roll(q[...,4],1,axis=0)+np.roll(q[...,5],-1,axis=1)-np.roll(q[...,5],1,axis=1))


def solve(case,n,steps,method,cfg,model,budget=None):
    if case not in ('smooth','ot','constraint') or method not in ('ct','glm'):
        raise ValueError('Unknown matched MHD case or method')
    if any(isinstance(a,bool) or not isinstance(a,int) for a in (n,steps)) or not 8<=n<=64 or not 1<=steps<=4096:
        raise ValueError('Bounded integer grid and steps required')
    dt=cfg['time']/steps;csum=2*model['wave_speed_bound']*n*dt
    if not 0<csum<=model['cfl_sum_maximum']:
        raise ValueError('Prescribed time step violates the declared two-dimensional CFL sum')
    q0=initial_q(case,n,cfg);state=pack(q0,method)
    if case=='constraint' and method=='ct':
        state[...,4]=cfg['amplitude']*np.cos(2*np.pi*(np.arange(n)[:,None]+1)/n)
    q=unpack(state,method)
    if np.max(abs(q-q0))>2e-14:raise ValueError('Matched initial cell states disagree')
    history=[];minimum_rho=float('inf');minimum_p=float('inf');max_native=0.;max_common=0.;max_psi=0.
    def record(t):
        nonlocal minimum_rho,minimum_p,max_native,max_common,max_psi
        q=unpack(state,method);rho,_,_,p,_,_=primitive(q,model['gamma'])
        minimum_rho=min(minimum_rho,float(rho.min()));minimum_p=min(minimum_p,float(p.min()))
        nd=float(np.max(abs(divergence(state,method))));cd=float(np.max(abs(common_divergence(q))))
        max_native=max(max_native,nd);max_common=max(max_common,cd);max_psi=max(max_psi,float(np.max(abs(q[...,6]))))
        history.append([t,float(q[...,0].mean()),float(q[...,3].mean()),nd,cd])
    record(0.)
    for i in range(steps):
        state+=dt*rhs(state,method,model,budget)
        record((i+1)*dt)
    return {'q':unpack(state,method),'state':state,'initial':q0,'history':np.asarray(history),
            'n':n,'steps':steps,'dt':dt,'cfl_sum':csum,'min_density':minimum_rho,'min_pressure':minimum_p,
            'maximum_psi_linf':max_psi,'maximum_native_divergence_linf':max_native,'maximum_common_divergence_linf':max_common}
