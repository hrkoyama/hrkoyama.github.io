"""Moving-volume upwind/Heun and actual 2D C-grid/RK4 time advances."""
import numpy as np


class NumericalFailure(ArithmeticError):
    def __init__(self,message,**state):
        super().__init__(message);self.state=state


def ale_rhs(x,m,xi,t,constant=False):
    volume=np.diff(x)
    if np.min(volume)<=0:raise NumericalFailure('Moving cell inversion',x=x,m=m,xi=xi,time=t)
    q=m/volume;w=.2*np.sin(2*np.pi*xi)*np.cos(2*np.pi*t)
    flux=(.7-w)*np.r_[q[-1],q]
    return w,-np.diff(flux),flux


def ale_solve(n,final_time,cfl=.4,fixed_steps=None,constant=False):
    xi=np.linspace(0,1,n+1);x=xi.copy()
    m=np.diff(x) if constant else np.diff(x)-.2/(2*np.pi)*np.diff(np.cos(2*np.pi*x))
    initial=m.copy();t=0.;times=[0.];states=[m.copy()];geometry=[x.copy()];records=[]
    targets=np.linspace(0,final_time,5)
    while t<final_time:
        tx=targets[len(times)]
        try:w,r,f=ale_rhs(x,m,xi,t)
        except NumericalFailure as failure:
            failure.state.update(times=np.array(times),history=np.array(states),geometry=np.array(geometry),stages=np.array(records))
            raise
        dt=final_time/fixed_steps if fixed_steps else cfl*np.min(np.diff(x))/.9
        dt=min(dt,tx-t)
        x1=x+dt*w;m1=m+dt*r
        try:w1,r1,f1=ale_rhs(x1,m1,xi,t+dt)
        except NumericalFailure as failure:
            failure.state.update(previous_x=x,previous_mass=m,euler_x=x1,euler_mass=m1,dt=dt,
                                 times=np.array(times),history=np.array(states),geometry=np.array(geometry),stages=np.array(records))
            raise
        xx=.5*x+.5*(x1+dt*w1);mm=.5*m+.5*(m1+dt*r1)
        # Positive relative advection leaves cell i through its RIGHT face.
        stage_cfl=max(np.max(dt*np.abs(.7-w[1:])/np.diff(x)),np.max(dt*np.abs(.7-w1[1:])/np.diff(x1)))
        if stage_cfl>.5+1e-14 or not np.isfinite(mm).all() or np.min(mm)<0:
            message='Frozen ALE CFL violated' if stage_cfl>.5+1e-14 else 'Invalid transported mass, no repair'
            raise NumericalFailure(message,previous_x=x,previous_mass=m,xi=xi,time=t,dt=dt,
                                   euler_x=x1,euler_mass=m1,candidate_x=xx,candidate_mass=mm,
                                   face_velocity=w,stage1_face_velocity=w1,flux=f,stage1_flux=f1,
                                   times=np.array(times),history=np.array(states),geometry=np.array(geometry),stages=np.array(records))
        mass_defect=mm.sum()-m.sum()+.5*dt*((f[-1]-f[0])+(f1[-1]-f1[0]))
        gcl=np.max(abs(np.diff(xx)-np.diff(x)-.5*dt*np.diff(w+w1)))
        t=tx if dt==tx-t else t+dt;x,m=xx,mm
        records.append([t,dt,np.min(np.diff(x)),np.min(m/np.diff(x)),stage_cfl,mass_defect,gcl])
        if t==tx:times.append(t);states.append(m.copy());geometry.append(x.copy())
    return dict(m=m,x=x,initial_mass=initial,times=np.array(times),history=np.array(states),geometry=np.array(geometry),stages=np.array(records))


def cgrid_rhs(q):
    eta,u,v=q;n=eta.shape[0];h=1/n
    vu=.25*(v+np.roll(v,-1,axis=1)+np.roll(v,1,axis=0)+np.roll(np.roll(v,-1,axis=1),1,axis=0))
    uv=.25*(u+np.roll(u,1,axis=1)+np.roll(u,-1,axis=0)+np.roll(np.roll(u,1,axis=1),-1,axis=0))
    return np.array([-((u-np.roll(u,1,axis=1))+(v-np.roll(v,1,axis=0)))/h,
                     vu-(np.roll(eta,-1,axis=1)-eta)/h,
                     -uv-(np.roll(eta,-1,axis=0)-eta)/h])


def cgrid_solve(initial,final_time,steps):
    q=initial.copy();dt=final_time/steps;t=0.;history=[q.copy()];times=[0.];records=[]
    for step in range(steps):
        k1=cgrid_rhs(q);s1=q+.5*dt*k1;k2=cgrid_rhs(s1);s2=q+.5*dt*k2;k3=cgrid_rhs(s2);s3=q+dt*k3;k4=cgrid_rhs(s3)
        new=q+dt/6*(k1+2*k2+2*k3+k4)
        if not all(np.isfinite(a).all() for a in [s1,s2,s3,new]):
            raise NumericalFailure('Nonfinite C-grid RK stage',previous=q,time=t,dt=dt,step=step,
                                   stage1=s1,stage2=s2,stage3=s3,candidate=new,k1=k1,k2=k2,k3=k3,k4=k4,
                                   history=np.array(history),times=np.array(times),stages=np.array(records))
        records.append([(step+1)*dt,np.mean(new[0]),.5*np.mean(np.sum(new**2,axis=0)),abs(np.mean(np.sum(q*k1,axis=0))),
                        np.max(abs(new)),np.max(abs(new-q-dt/6*(k1+2*k2+2*k3+k4)))])
        q=new;t=final_time if step+1==steps else (step+1)*dt
        if (step+1)%(steps//4)==0:history.append(q.copy());times.append(t)
    return dict(state=q,history=np.array(history),times=np.array(times),stages=np.array(records))
