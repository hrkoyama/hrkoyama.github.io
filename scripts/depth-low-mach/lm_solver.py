"""Conservative 2D Euler: unlimited primitive MUSCL with Roe or Miczek fluxes.

The physical Euler time derivative is unchanged. SSPRK(3,3) uses an acoustic
CFL, qualified separately by a frozen Fourier scan and by the fixed PDE runs.
No floors, state repair, entropy fix, pseudo-time iteration or rejected steps.
"""
import numpy as np

GAMMA = 1.4


class InvalidStage(ValueError):
    """Raw attempted state and completed history are attached on failure."""


def conserved(w):
    rho,u,v,p=np.moveaxis(np.asarray(w,dtype=float),-1,0)
    return np.stack((rho,rho*u,rho*v,p/(GAMMA-1)+.5*rho*(u*u+v*v)),axis=-1)


def primitive(q):
    q=np.asarray(q)
    if q.shape[-1]!=4 or not np.isfinite(q).all() or np.any(q[...,0]<=0):
        raise ValueError('Four finite conserved components with positive density required')
    rho=q[...,0];u=q[...,1]/rho;v=q[...,2]/rho
    p=(GAMMA-1)*(q[...,3]-.5*(q[...,1]*u+q[...,2]*v))
    if not np.isfinite(p).all() or np.any(p<=0):raise ValueError('Nonpositive pressure')
    return np.stack((rho,u,v,p),axis=-1)


def physical_flux(q,axis,w=None):
    if axis not in (0,1):raise ValueError('Cartesian axis required')
    if w is None:w=primitive(q)
    normal=w[...,1+axis];f=q*normal[...,None]
    f[...,1+axis]+=w[...,3];f[...,3]=(q[...,3]+w[...,3])*normal
    return f


def roe_state(left,right,wl=None,wr=None):
    if wl is None:wl=primitive(left)
    if wr is None:wr=primitive(right)
    sl=np.sqrt(wl[...,0]);sr=np.sqrt(wr[...,0]);den=sl+sr
    rho=sl*sr;u=(sl*wl[...,1]+sr*wr[...,1])/den;v=(sl*wl[...,2]+sr*wr[...,2])/den
    h=(sl*(left[...,3]+wl[...,3])/wl[...,0]+sr*(right[...,3]+wr[...,3])/wr[...,0])/den
    c2=(GAMMA-1)*(h-.5*(u*u+v*v))
    if not np.isfinite(c2).all() or np.any(c2<=0):raise ValueError('Invalid Roe sound speed')
    return rho,u,v,np.sqrt(c2)


def delta_parameter(rho,un,ut,c,variant,mach_cutoff):
    if variant not in ('roe','miczek') or not np.isfinite(mach_cutoff) or not 0<mach_cutoff<=1:
        raise ValueError('roe/miczek and 0 < Mach cutoff <= 1 required')
    local=np.sqrt(un*un+ut*ut)/c
    mu=np.minimum(1.,np.maximum(local,mach_cutoff))
    return np.zeros_like(local) if variant=='roe' else 1/mu-1


def a_apply(z,rho,un,c):
    dr,du,dv,dp=np.moveaxis(z,-1,0)
    return np.stack((un*dr+rho*du,un*du+dp/rho,un*dv,rho*c*c*du+un*dp),axis=-1)


def b_apply(z,rho,un,c,delta):
    unused_dr,du,unused_dv,dp=np.moveaxis(z,-1,0)
    return np.stack((rho*(1+delta*un/c)*du+delta/c*dp,
        -delta*c*du+(1-delta*un/c)/rho*dp,np.zeros_like(du),
        rho*c*(c+delta*un)*du+delta*c*dp),axis=-1)


def inverse_p_apply(z,rho,c,delta):
    dr,du,dv,dp=np.moveaxis(z,-1,0);den=1+delta*delta
    normal=(du+delta*dp/(rho*c))/den
    pressure=(dp-rho*c*delta*du)/den
    return np.stack((dr-rho*delta/c*normal,normal,dv,pressure),axis=-1)


def dissipation_primitive(jump,rho,un,ut,c,variant='miczek',mach_cutoff=.01):
    """P^-1 |PA| jump in local (rho,un,ut,p) variables, by a degree-2 polynomial.

    PA has eigenvalues un (twice), un±tau. No per-face eigenvectors are formed.
    Fully supersonic normal flow uses the exact sign(un)*A branch.
    """
    rho,un,ut,c=np.broadcast_arrays(np.asarray(rho),np.asarray(un),np.asarray(ut),np.asarray(c))
    delta=delta_parameter(rho,un,ut,c,variant,mach_cutoff)
    tau=np.sqrt(c*c*(1+delta*delta)-delta*delta*un*un)
    bz=b_apply(jump,rho,un,c,delta);bbz=b_apply(bz,rho,un,c,delta)
    absolute=(abs(un)[...,None]*jump+(un/tau)[...,None]*bz+
        ((tau-abs(un))/(tau*tau))[...,None]*bbz)
    value=inverse_p_apply(absolute,rho,c,delta)
    upwind=np.sign(un)[...,None]*a_apply(jump,rho,un,c)
    return np.where((abs(un)>=tau)[...,None],upwind,value)


def primitive_to_conserved_increment(z,rho,u,v):
    dr,du,dv,dp=np.moveaxis(z,-1,0)
    return np.stack((dr,u*dr+rho*du,v*dr+rho*dv,
        .5*(u*u+v*v)*dr+rho*(u*du+v*dv)+dp/(GAMMA-1)),axis=-1)


def numerical_flux(left,right,axis,variant='miczek',mach_cutoff=.01):
    if axis not in (0,1):raise ValueError('Cartesian axis required')
    wl,wr=primitive(left),primitive(right);rho,u,v,c=roe_state(left,right,wl,wr)
    jump=wr-wl
    order=[0,1,2,3] if axis==0 else [0,2,1,3]
    local=jump[...,order];un,ut=(u,v) if axis==0 else (v,u)
    d=dissipation_primitive(local,rho,un,ut,c,variant,mach_cutoff)[...,order]
    dq=primitive_to_conserved_increment(d,rho,u,v)
    return .5*(physical_flux(left,axis,wl)+physical_flux(right,axis,wr)-dq)


def reconstructed_faces(q,axis):
    """Unlimited centered primitive slopes; inadmissible raw faces are rejected.

    Both variants use exactly the same smooth reconstruction. No clipping,
    limiter, cell-average change or fallback is applied.
    """
    if axis not in (0,1):raise ValueError('Cartesian axis required')
    w=primitive(q);slope=.5*(np.roll(w,-1,axis=axis)-np.roll(w,1,axis=axis))
    left=w+.5*slope;right=np.roll(w-.5*slope,-1,axis=axis)
    for side,face in [('left',left),('right',right)]:
        if not np.isfinite(face).all() or np.any(face[...,0]<=0) or np.any(face[...,3]<=0):
            e=InvalidStage('Invalid unlimited primitive reconstruction: '+side)
            e.failed_state=q.copy();e.failed_faces={'left_primitive':left.copy(),'right_primitive':right.copy()}
            e.completed_history=[];e.failed_context={'stage':'reconstruction','axis':axis,'side':side};raise e
    return conserved(left),conserved(right)


def rhs(q,length=20.,variant='miczek',mach_cutoff=.01):
    if q.ndim!=3 or q.shape[0]!=q.shape[1] or length<=0:raise ValueError('Square periodic Cartesian field required')
    h=length/q.shape[0];out=np.zeros_like(q)
    for axis in (0,1):
        left,right=reconstructed_faces(q,axis)
        f=numerical_flux(left,right,axis,variant,mach_cutoff)
        out-=(f-np.roll(f,1,axis=axis))/h
    return out


def solve(q0,final_time=.1,cfl=.2,length=20.,variant='miczek',mach_cutoff=.01,max_steps=20000):
    if not np.isfinite(final_time) or final_time<=0 or not 0<cfl<=.2 or max_steps<1:
        raise ValueError('Positive fixed horizon, 0<CFL<=.2 and positive step budget required')
    q=np.array(q0,dtype=float,copy=True);primitive(q);h=length/q.shape[0]
    initial=q.sum(axis=(0,1))*h*h;t=0.;steps=0;history=[];rmin=float('inf');pmin=float('inf');dt_min=float('inf');dt_max=0.
    def checked(state,stage):
        nonlocal rmin,pmin
        try:w=primitive(state)
        except ValueError as original:
            e=InvalidStage(str(original));e.failed_state=state.copy();e.completed_history=list(history)
            e.failed_context={'stage':stage,'step':steps,'time':t};raise e
        rmin=min(rmin,float(w[...,0].min()));pmin=min(pmin,float(w[...,3].min()));return w
    def apply_rhs(state,stage):
        try:return rhs(state,length,variant,mach_cutoff)
        except InvalidStage as e:
            e.completed_history=list(history);e.failed_context.update(rk_stage=stage,step=steps,time=t);raise
    checked(q,'initial')
    while t<final_time:
        if steps>=max_steps:raise ValueError('Declared step budget exceeded')
        w=primitive(q);c=np.sqrt(GAMMA*w[...,3]/w[...,0])
        rate=(np.max(abs(w[...,1])+c)+np.max(abs(w[...,2])+c))/h
        dt=min(cfl/rate,final_time-t)
        if not np.isfinite(dt) or dt<=0:raise ValueError('Invalid physical time step')
        q1=q+dt*apply_rhs(q,'rhs-stage1');checked(q1,'stage1')
        q2=.75*q+.25*(q1+dt*apply_rhs(q1,'rhs-stage2'));checked(q2,'stage2')
        q3=q/3+(2/3)*(q2+dt*apply_rhs(q2,'rhs-stage3'));checked(q3,'stage3')
        q=q3;t+=dt;steps+=1;dt_min=min(dt_min,dt);dt_max=max(dt_max,dt)
        if steps%50==0 or t>=final_time:history.append({'step':steps,'time':t,'dt':dt,'minimum_density':rmin,'minimum_pressure':pmin})
    final=q.sum(axis=(0,1))*h*h
    return {'q':q,'time':t,'steps':steps,'history':history,'initial_integral':initial,'final_integral':final,
        'minimum_density_all_stages':rmin,'minimum_pressure_all_stages':pmin,'minimum_dt':dt_min,'maximum_dt':dt_max,
        'state_floor_count':0,'rejected_steps':0}


def normal_matrices(rho,un,ut,c,variant='miczek',mach_cutoff=.01):
    """Explicit small matrices for independent test/Fourier diagnostics, not PDE flux evaluation."""
    delta=float(delta_parameter(rho,np.asarray(un),np.asarray(ut),c,variant,mach_cutoff))
    a=np.array([[un,rho,0,0],[0,un,0,1/rho],[0,0,un,0],[0,rho*c*c,0,un]],float)
    p=np.array([[1,rho*delta/c,0,0],[0,1,0,-delta/(rho*c)],[0,0,1,0],[0,rho*c*delta,0,1]],float)
    return a,p
