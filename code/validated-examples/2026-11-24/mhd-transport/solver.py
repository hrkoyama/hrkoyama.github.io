"""Small full-state periodic FV ideal-MHD evolution; HLLD/MC/Heun and CT-contact.

State order rho,mx,my,mz,E,Bx,By,Bz; all three vector components retained.
Face positivity scaling changes reconstruction only. Cell states are never
clipped, and a failed stage is saved/rejected as a failed run, not retried.
"""
import time
import numpy as np
import hlld


class StageFailure(ArithmeticError):
    def __init__(self,message,q,context):
        super().__init__(message);self.q=q.copy();self.context=context


def limited(a,b):
    return np.where(a*b>0,np.sign(a)*np.minimum(.5*abs(a+b),2*np.minimum(abs(a),abs(b))),0.)


def slopes(w,axis):
    s=limited(w-np.roll(w,1,axis=axis),np.roll(w,-1,axis=axis)-w)
    theta=np.ones(w.shape[:-1])
    for component in [0,4]:
        delta=.5*abs(s[...,component])
        theta=np.minimum(theta,(w[...,component]-1e-12)/np.maximum(delta,1e-300))
    theta=np.clip(theta,0,1)
    return s*theta[...,None],theta


def contact_emf(fx,fy,w,dx,dy):
    ex=-fx[...,6];ey=fy[...,5];ec=w[...,2]*w[...,5]-w[...,1]*w[...,6]
    choose=lambda mass,a,b:np.where(mass>0,a,np.where(mass<0,b,.5*(a+b)))
    east=lambda a:np.roll(a,-1,axis=0);north=lambda a:np.roll(a,-1,axis=1)
    sy=choose(fx[...,0],ey-ec,east(ey-ec))*2/dy
    ny=choose(north(fx[...,0]),north(ec)-ey,east(north(ec)-ey))*2/dy
    wx=choose(fy[...,0],ex-ec,north(ex-ec))*2/dx
    ee=choose(east(fy[...,0]),east(ec)-ex,north(east(ec)-ex))*2/dx
    return .25*(ex+north(ex)+ey+east(ey))+.125*(dy*(sy-ny)+dx*(wx-ee))


def divergence(q,bx,by,dx,dy):
    if q.ndim==2:return float(np.max(abs((q[:,5]-np.roll(q[:,5],1))/dx)))
    return float(np.max(abs((bx-np.roll(bx,1,axis=0))/dx+(by-np.roll(by,1,axis=1))/dy)))


def common_divergence(q,dx,dy):
    if q.ndim==2:return float(np.max(abs((np.roll(q[:,5],-1)-np.roll(q[:,5],1))/(2*dx))))
    return float(np.max(abs((np.roll(q[...,5],-1,axis=0)-np.roll(q[...,5],1,axis=0))/(2*dx)+(np.roll(q[...,6],-1,axis=1)-np.roll(q[...,6],1,axis=1))/(2*dy))))


def exact_wave(n,time=0.,amplitude=.1):
    x=(np.arange(n)+.5)/n;phase=2*np.pi*(x-time);factor=np.sinc(1/n)
    q=np.zeros((n,8));q[:,0]=1.;q[:,4]=.1/(2/3)+.5+amplitude**2;q[:,5]=1.
    q[:,6]=amplitude*factor*np.cos(phase);q[:,7]=amplitude*factor*np.sin(phase)
    q[:,2:4]=-q[:,6:8]
    return q


def initial(case,n):
    if case=='circular-alfven-refinement':return exact_wave(n),None,None,1/n,1.
    loop=case=='magnetic-loop-independent'
    if not loop and case!='postshock-orszag-tang':raise ValueError('Unknown case')
    nx,ny=(2*n,n) if loop else (n,n);dx=(2. if loop else 1.)/nx;dy=1/ny
    xl=-1. if loop else -.5;yl=-.5
    x=xl+(np.arange(nx)+.5)*dx;y=yl+(np.arange(ny)+.5)*dy
    xx=x[:,None]+dx/2;yy=y[None,:]+dy/2
    if loop:az=.001*np.maximum(.3-np.hypot(xx,yy),0.)
    else:az=(np.cos(4*np.pi*xx)-2*np.cos(2*np.pi*yy))/(4*np.pi*np.sqrt(4*np.pi))
    bx=(az-np.roll(az,1,axis=1))/dy;by=-(az-np.roll(az,1,axis=0))/dx
    w=np.zeros((nx,ny,8));w[...,0]=1. if loop else 25/(36*np.pi);w[...,4]=1. if loop else 5/(12*np.pi)
    if loop:w[...,1:4]=[2.,1.,2.]
    else:w[...,1]=np.sin(2*np.pi*y)[None,:];w[...,2]=-np.sin(2*np.pi*x)[:,None]
    w[...,5]=.5*(bx+np.roll(bx,1,axis=0));w[...,6]=.5*(by+np.roll(by,1,axis=1))
    return hlld.conserved(w),bx,by,dx,dy


def interface(w,axis,normal=None):
    s,theta=slopes(w,axis);left=w+.5*s;right=np.roll(w-.5*s,-1,axis=axis)
    if normal is not None:left[...,5+axis]=normal;right[...,5+axis]=normal
    f,a,stats=hlld.riemann(left,right,axis=axis,solver='hlld')
    stats.update(max_speed=float(a.max()),minimum_face_density=float(min(left[...,0].min(),right[...,0].min())),minimum_face_pressure=float(min(left[...,4].min(),right[...,4].min())),scaling_count=int(np.count_nonzero(theta<1)),minimum_theta=float(theta.min()))
    return f,stats


def rhs(q,bx,by,dx,dy):
    w=hlld.primitive(q);fx,sx=interface(w,0,bx)
    if q.ndim==2:
        r=-(fx-np.roll(fx,1,axis=0))/dx
        return r,None,None,{**sx,'signal_sum':sx['max_speed']/dx}
    fy,sy=interface(w,1,by);r=-(fx-np.roll(fx,1,axis=0))/dx-(fy-np.roll(fy,1,axis=1))/dy
    ez=contact_emf(fx,fy,w,dx,dy)
    rx=-(ez-np.roll(ez,1,axis=1))/dy;ry=(ez-np.roll(ez,1,axis=0))/dx
    stats={k:(sx[k]+sy[k] if k in ['hlle_fallback_faces','degenerate_faces','scaling_count'] else min(sx[k],sy[k])) for k in ['hlle_fallback_faces','degenerate_faces','scaling_count','minimum_theta','minimum_face_density','minimum_face_pressure']}
    stats['signal_sum']=sx['max_speed']/dx+sy['max_speed']/dy
    return r,rx,ry,stats


def euler(q,bx,by,r,rx,ry,dt):
    q=q+dt*r
    if bx is not None:
        bx=bx+dt*rx;by=by+dt*ry
        q[...,5]=.5*(bx+np.roll(bx,1,axis=0));q[...,6]=.5*(by+np.roll(by,1,axis=1))
    return q,bx,by


HISTORY_COLUMNS=['step','time','minimum_density','minimum_pressure','face_minimum_density','face_minimum_pressure','native_divergence','common_divergence','fluid_integral_defect','maximum_courant_sum','hlle_fallback_faces','degenerate_faces','reconstruction_scalings','minimum_theta','maximum_abs_bz']


def solve(case,n,steps,final_time,deadline=None):
    if steps<=0 or steps%4 or n<8 or final_time<=0:raise ValueError('Use positive fixed steps divisible byfour and n>=8')
    q,bx,by,dx,dy=initial(case,n);q0=q.copy();dt=final_time/steps
    sums=q.reshape(-1,8).mean(axis=0);scale=np.maximum(np.mean(abs(q.reshape(-1,8)),axis=0),1.)
    snapshots=[q.copy()];bxs=[] if bx is None else [bx.copy()];bys=[] if by is None else [by.copy()];times=[0.];history=[];fallback=0;scalings=0;minimum_theta=1.
    for k in range(1,steps+1):
        if deadline is not None and time.monotonic()>deadline:raise StageFailure("fixed shared batch deadline",q,dict(case=case,n=n,step=k,stage="budget"))
        candidate=q;stage="rhs0"
        try:
            r,rx,ry,s1=rhs(q,bx,by,dx,dy);a,ax,ay=euler(q,bx,by,r,rx,ry,dt)
            candidate=a;stage="euler1";wa=hlld.primitive(a)
            r,rx,ry,s2=rhs(a,ax,ay,dx,dy);b,bxx,byy=euler(a,ax,ay,r,rx,ry,dt)
            candidate=b;stage="euler2";wb=hlld.primitive(b);trial=.5*(q+b)
            if bx is not None:
                tx=.5*(bx+bxx);ty=.5*(by+byy)
                trial[...,5]=.5*(tx+np.roll(tx,1,axis=0));trial[...,6]=.5*(ty+np.roll(ty,1,axis=1))
            else:tx=ty=None
            candidate=trial;stage="heun";wt=hlld.primitive(trial)
        except (ValueError,FloatingPointError) as err:raise StageFailure(str(err),candidate,dict(case=case,n=n,step=k,stage=stage)) from err
        defect=max(float(np.max(abs(z.reshape(-1,8).mean(axis=0)[:5]-sums[:5])/scale[:5])) for z in [a,b,trial])
        fb=s1['hlle_fallback_faces']+s2['hlle_fallback_faces'];sc=s1['scaling_count']+s2['scaling_count'];theta=min(s1['minimum_theta'],s2['minimum_theta'])
        history.append([k,final_time*k/steps,min(wa[...,0].min(),wb[...,0].min(),wt[...,0].min()),min(wa[...,4].min(),wb[...,4].min(),wt[...,4].min()),min(s1['minimum_face_density'],s2['minimum_face_density']),min(s1['minimum_face_pressure'],s2['minimum_face_pressure']),max(divergence(a,ax,ay,dx,dy),divergence(b,bxx,byy,dx,dy),divergence(trial,tx,ty,dx,dy)),common_divergence(trial,dx,dy),defect,dt*max(s1['signal_sum'],s2['signal_sum']),fb,s1['degenerate_faces']+s2['degenerate_faces'],sc,theta,float(np.max(abs(trial[...,7])))])
        fallback+=fb;scalings+=sc;minimum_theta=min(minimum_theta,theta)
        q,bx,by=trial,tx,ty
        if k%(steps//4)==0:
            snapshots.append(q.copy());times.append(final_time*k/steps)
            if bx is not None:bxs.append(bx.copy());bys.append(by.copy())
    return dict(q=q,q_initial=q0,q_history=np.array(snapshots),bx_history=np.array(bxs),by_history=np.array(bys),times=np.array(times),history=np.array(history),history_columns=np.array(HISTORY_COLUMNS),steps=steps,time=final_time,dx=dx,dy=dy,fallback_faces=fallback,reconstruction_scalings=scalings,minimum_theta=minimum_theta,retries=0,state_clip_count=0)
