"""Actual2Dspace,3Dangle grey transport and time-advanced nonlinear M1.

c=1. Six-axis angular weights sum1; a unit +x beam has nodal intensity6.
M1 retains E,Fx,Fy and computes full3Dtensor entries including Pzz. No floors,
projection,beam relabeling or synthetic map substitutes for time advancement.
"""
import numpy as np
import mms
import wavespeeds

DIRECTIONS=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],float)
WEIGHTS=np.ones(6)/6


def pressure(state):
    e=state[...,0];f=state[...,1:]
    if not np.isfinite(state).all() or np.min(e)<-1e-13:raise ArithmeticError('Invalid M1 energy')
    g=np.zeros_like(f);np.divide(f,e[...,None],out=g,where=e[...,None]>0)
    f2=np.sum(g*g,axis=-1)
    if np.max(f2)>1+5e-12 or np.any((e<=0)&np.any(f!=0,axis=-1)):raise ArithmeticError('M1 state outside realizability cone')
    s=np.sqrt(4-3*f2);chi=(3+4*f2)/(5+2*s);a=(1-chi)/2
    # Rationalized B/f^2 has its correct finite isotropic limit3/4.
    coefficient=(6+3/(2+s))/(5+2*s)
    xx=e*(a+coefficient*g[...,0]**2);xy=e*coefficient*g[...,0]*g[...,1]
    yy=e*(a+coefficient*g[...,1]**2);zz=e*a
    return np.stack([xx,xy,yy,zz],axis=-1)


def fluxes(state):
    p=pressure(state)
    return np.stack([state[...,1],p[...,0],p[...,1]],axis=-1),np.stack([state[...,2],p[...,1],p[...,2]],axis=-1)


def rusanov_face(left,right,left_flux,right_flux,left_speed,right_speed):
    a=np.maximum(left_speed,right_speed)
    return .5*(left_flux+right_flux-a[...,None]*(right-left))


def moment_rhs(state,h,beam,periodic,speed_diagnostics=None):
    fx,fy=fluxes(state)
    sx=wavespeeds.directional_speed(state,0,speed_diagnostics);sy=wavespeeds.directional_speed(state,1,speed_diagnostics)
    right=np.roll(state,-1,axis=0);up=np.roll(state,-1,axis=1)
    f=rusanov_face(state,right,fx,np.roll(fx,-1,axis=0),sx,np.roll(sx,-1,axis=0))
    g=rusanov_face(state,up,fy,np.roll(fy,-1,axis=1),sy,np.roll(sy,-1,axis=1))
    if periodic:previous_f=np.roll(f,1,axis=0);previous_g=np.roll(g,1,axis=1);outflux=0.
    else:
        left_state=np.stack([beam,beam,np.zeros_like(beam)],axis=-1);left_fx,_=fluxes(left_state)
        left_speed=wavespeeds.directional_speed(left_state,0,speed_diagnostics)
        # Every physical boundary uses the same face rule. Vacuum speed1 is
        # an explicit conservative extension,not a claimed vacuum Jacobian.
        empty=np.zeros_like(state[0]);zero_flux=np.zeros_like(empty);vacuum_speed=np.ones_like(beam)
        left=rusanov_face(left_state,state[0],left_fx,fx[0],left_speed,sx[0])
        bottom=rusanov_face(empty,state[:,0],zero_flux,fy[:,0],vacuum_speed,sy[:,0])
        f[-1]=rusanov_face(state[-1],empty,fx[-1],zero_flux,sx[-1],vacuum_speed)
        g[:,-1]=rusanov_face(state[:,-1],empty,fy[:,-1],zero_flux,sy[:,-1],vacuum_speed)
        previous_f=np.roll(f,1,axis=0);previous_g=np.roll(g,1,axis=1);previous_f[0]=left;previous_g[:,0]=bottom
        outflux=h*(np.sum(f[-1,:,0]-left[:,0])+np.sum(g[:,-1,0]-bottom[:,0]))
    return -(f-previous_f+g-previous_g)/h,float(outflux)


def angular_rhs(intensity,h,beam,periodic):
    rate=np.zeros_like(intensity)
    for j,(nx,ny,nz) in enumerate(DIRECTIONS):
        for axis,speed in [(0,nx),(1,ny)]:
            if speed==0:continue
            upstream=np.roll(intensity[...,j],1 if speed>0 else -1,axis=axis)
            if not periodic:
                if axis==0 and speed>0:upstream[0]=6*beam if j==0 else 0.
                elif axis==0:upstream[-1]=0.
                elif speed>0:upstream[:,0]=0.
                else:upstream[:,-1]=0.
            rate[...,j]-=abs(speed)*(intensity[...,j]-upstream)/h
    outflux=0. if periodic else h*(np.sum(intensity[-1,:,0]+intensity[0,:,1]+intensity[:,-1,2]+intensity[:,0,3])/6-np.sum(beam))
    return rate,float(outflux)


def moments(intensity):
    energy=np.sum(intensity,axis=-1)/6;fx=(intensity[...,0]-intensity[...,1])/6;fy=(intensity[...,2]-intensity[...,3])/6
    return np.stack([energy,fx,fy],axis=-1)


def angular_pressure(intensity):
    return np.stack([(intensity[...,0]+intensity[...,1])/6,np.zeros(intensity.shape[:2]),(intensity[...,2]+intensity[...,3])/6,(intensity[...,4]+intensity[...,5])/6],axis=-1)


def packet(x,y,x0):return np.exp(16*(np.cos(2*np.pi*(x-x0))+np.cos(2*np.pi*(y-.5))-2))


def cell_initial(cells,kind):
    h=1/cells;x=(np.arange(cells)+.5)*h;y=x.copy();xx,yy=np.meshgrid(x,y,indexing='ij')
    if kind=='shadow':return np.zeros((cells,cells,6))
    # Actual cell means, primary4point integration; reference uses independent16.
    nodes,w=np.polynomial.legendre.leggauss(4);beams=np.zeros((cells,cells,2))
    if kind=='mms':state=np.zeros((cells,cells,3))
    for a,wa in zip(nodes,w):
        for b,wb in zip(nodes,w):
            px,py=xx+.5*h*a,yy+.5*h*b
            if kind=='mms':state+=.25*wa*wb*mms.state_and_forcing(px,py,0.)[0]
            else:beams[...,0]+=.25*wa*wb*packet(px,py,.25);beams[...,1]+=.25*wa*wb*(packet(py,px,.25) if kind=='crossed' else packet(px,py,.75))
    if kind=='mms':return state
    intensity=np.zeros((cells,cells,6));intensity[...,0]=6*beams[...,0];intensity[...,2 if kind=='crossed' else 1]=6*beams[...,1]
    return intensity


def solve(config,partial=None):
    n,kind,method=config['cells'],config['kind'],config['method'];h=1/n;steps=config['steps'];dt=config['final_time']/steps
    if steps<=0 or steps%4:raise ValueError('Fixed steps divisible byfour required')
    initial=cell_initial(n,kind);state=initial if method=='sn' or kind=='mms' else moments(initial)
    x=(np.arange(n)+.5)*h;xx,yy=np.meshgrid(x,x,indexing='ij')
    opacity=np.where((xx-.35)**2+(yy-.5)**2<.12**2,40.,0.) if kind=='shadow' else np.zeros((n,n))
    beam=np.maximum(0.,np.minimum((np.arange(n)+1)*h,.7)-np.maximum(np.arange(n)*h,.3))/h
    speed_diagnostics=wavespeeds.diagnostics()
    periodic=kind!='shadow';snapshots=[state.copy()];times=[0.];history=[];boundary=absorbed=forcing_total=0.
    energy=lambda z:np.sum(z,axis=-1)/6 if method=='sn' else z[...,0]
    e0=h*h*np.sum(energy(state));attenuation=np.exp(-.5*dt*opacity)[...,None]
    for step in range(steps):
        time=step*dt;candidate=state;stage='absorption0'
        try:
            before=h*h*np.sum(energy(state));state=state*attenuation;absorbed+=before-h*h*np.sum(energy(state))
            function=angular_rhs if method=='sn' else moment_rhs
            r,out1=function(state,h,beam,periodic) if method=='sn' else function(state,h,beam,periodic,speed_diagnostics)
            source1=np.zeros_like(state) if kind!='mms' else mms.state_and_forcing(xx,yy,time)[1]
            a=state+dt*(r+source1);candidate=a;stage='euler1'
            if method=='m1':pressure(a)
            elif not np.isfinite(a).all() or a.min()< -1e-13:raise ArithmeticError('Invalid angular first stage')
            r,out2=function(a,h,beam,periodic) if method=='sn' else function(a,h,beam,periodic,speed_diagnostics)
            source2=np.zeros_like(state) if kind!='mms' else mms.state_and_forcing(xx,yy,time+dt)[1]
            b=a+dt*(r+source2);candidate=b;stage='euler2'
            if method=='m1':pressure(b)
            elif not np.isfinite(b).all() or b.min()< -1e-13:raise ArithmeticError('Invalid angular second stage')
            state=.5*(state+b);before=h*h*np.sum(energy(state));state*=attenuation;absorbed+=before-h*h*np.sum(energy(state))
            boundary+=.5*dt*(out1+out2)
            if kind=='mms':forcing_total+=.5*dt*h*h*np.sum(source1[...,0]+source2[...,0])
            current=energy(state);total=h*h*np.sum(current)
            cone=np.min(current-np.sqrt(np.sum(state[...,1:]**2,axis=-1))) if method=='m1' else np.min(state)
            if method=='m1':pressure(state)
            history.append([(step+1)*dt,total,boundary,absorbed,forcing_total,abs(total-e0+boundary+absorbed-forcing_total),float(np.min(current)),float(cone)])
        except Exception:
            if partial is not None:np.savez(partial,state=state,candidate=candidate,time=time,step=step,stage=stage)
            raise
        if (step+1)%(steps//4)==0:snapshots.append(state.copy());times.append((step+1)*dt)
    saved=np.array(snapshots);saved_moments=np.array([moments(a) for a in saved]) if method=='sn' else saved.copy()
    saved_pressure=np.array([angular_pressure(a) if method=='sn' else pressure(a) for a in saved])
    return dict(speed_diagnostic_names=np.array(list(speed_diagnostics)),speed_diagnostic_values=np.array(list(speed_diagnostics.values()),float),x=x,y=x,states=saved,moments=saved_moments,pressure=saved_pressure,times=np.array(times),history=np.array(history),opacity=opacity,method=np.array(method),kind=np.array(kind),steps=np.array(steps))
