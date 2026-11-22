"""Original 2-D TMz Yee solver: normalized epsilon=mu=c=1, uniform rectangles.

State is E_z at t=n*dt and (H_x,H_y) at t=(n-1/2)*dt.
No absorbing layer, material interface, sources or fitted reference solution.
"""
import math
import numpy as np


def grid(nx, ny, lx, ly, dt, boundary):
    if (isinstance(nx, bool) or isinstance(ny, bool) or
            not isinstance(nx, int) or not isinstance(ny, int) or min(nx, ny) < 4):
        raise ValueError('nx and ny must be integers >=4')
    if boundary not in ('periodic', 'pec'):
        raise ValueError('boundary must be periodic or pec')
    if not all(math.isfinite(v) and v > 0 for v in (lx, ly, dt)):
        raise ValueError('lengths and dt must be finite and positive')
    dx, dy = lx/nx, ly/ny
    if dt*math.sqrt(dx**-2+dy**-2) >= 1:
        raise ValueError('Strict Yee CFL dt*sqrt(dx^-2+dy^-2)<1 required')
    return dict(nx=nx,ny=ny,lx=lx,ly=ly,dx=dx,dy=dy,dt=dt,boundary=boundary)


def coordinates(g):
    nx,ny,dx,dy = (g[k] for k in ('nx','ny','dx','dy'))
    pec = g['boundary']=='pec'
    xe=np.arange(nx+int(pec))*dx
    ye=np.arange(ny+int(pec))*dy
    return ((xe[:,None],ye[None,:]),
            (xe[:,None],(np.arange(ny)+.5)[None,:]*dy),
            ((np.arange(nx)+.5)[:,None]*dx,ye[None,:]))


def frequencies(g, mode):
    factor=2*np.pi if g['boundary']=='periodic' else np.pi
    kx,ky=factor*mode[0]/g['lx'],factor*mode[1]/g['ly']
    sx,sy=2*np.sin(kx*g['dx']/2)/g['dx'],2*np.sin(ky*g['dy']/2)/g['dy']
    omega=np.hypot(kx,ky)
    discrete=2*np.arcsin(.5*g['dt']*np.hypot(sx,sy))/g['dt']
    return kx,ky,float(omega),float(discrete),float(sx),float(sy)


def exact_fields(g, mode, electric_time, magnetic_time, discrete=False):
    """Independent continuum formula, or exact space/time-discrete mode.

    discrete=True replaces k amplitudes and frequency with their symbols.
    Continuum field error uses discrete=False; the two references are distinct.
    """
    kx,ky,omega,omega_h,sx,sy=frequencies(g,mode)
    w=omega_h if discrete else omega
    ax,ay=(sx/np.hypot(sx,sy),sy/np.hypot(sx,sy)) if discrete else (kx/omega,ky/omega)
    (xe,ye),(xh,yh),(xv,yv)=coordinates(g)
    if g['boundary']=='periodic':
        e=np.cos(kx*xe+ky*ye-w*electric_time)
        hx=ay*np.cos(kx*xh+ky*yh-w*magnetic_time)
        hy=-ax*np.cos(kx*xv+ky*yv-w*magnetic_time)
    else:
        e=np.sin(kx*xe)*np.sin(ky*ye)*np.cos(w*electric_time)
        hx=-ay*np.sin(kx*xh)*np.cos(ky*yh)*np.sin(w*magnetic_time)
        hy=ax*np.cos(kx*xv)*np.sin(ky*yv)*np.sin(w*magnetic_time)
        # Represent the imposed boundary exactly, including sin(m*pi) roundoff.
        e[[0,-1],:]=0; e[:,[0,-1]]=0
        hx[[0,-1],:]=0; hy[:,[0,-1]]=0
    return e,hx,hy


def magnetic_step(e,hx,hy,g):
    dx,dy,dt=(g[k] for k in ('dx','dy','dt'))
    if g['boundary']=='periodic':
        return hx-dt*(np.roll(e,-1,axis=1)-e)/dy,hy+dt*(np.roll(e,-1,axis=0)-e)/dx
    return hx-dt*np.diff(e,axis=1)/dy,hy+dt*np.diff(e,axis=0)/dx


def electric_step(e,hx,hy,g):
    dx,dy,dt=(g[k] for k in ('dx','dy','dt'))
    if g['boundary']=='periodic':
        return e+dt*((hy-np.roll(hy,1,axis=0))/dx-(hx-np.roll(hx,1,axis=1))/dy)
    out=np.zeros_like(e)
    out[1:-1,1:-1]=e[1:-1,1:-1]+dt*(np.diff(hy,axis=0)[:,1:-1]/dx-np.diff(hx,axis=1)[1:-1,:]/dy)
    return out


def step(e,hx,hy,g):
    hx1,hy1=magnetic_step(e,hx,hy,g)
    return electric_step(e,hx1,hy1,g),hx1,hy1


def inner(a,b,g,component):
    value=a*b
    if g['boundary']=='pec':
        value=value.copy()
        if component in ('e','hx'):value[[0,-1],:]*=.5
        if component in ('e','hy'):value[:,[0,-1]]*=.5
    return float(value.sum()*g['dx']*g['dy'])


def energies(e,hx,hy,g):
    """Modified invariant and ordinary energy using centered H at E's time."""
    xp,yp=magnetic_step(e,hx,hy,g)
    invariant=.5*(inner(e,e,g,'e')+inner(hx,xp,g,'hx')+inner(hy,yp,g,'hy'))
    xc,yc=.5*(hx+xp),.5*(hy+yp)
    physical=.5*(inner(e,e,g,'e')+inner(xc,xc,g,'hx')+inner(yc,yc,g,'hy'))
    return invariant,physical


def divergence(hx,hy,g):
    if g['boundary']=='periodic':
        return (np.roll(hx,-1,axis=0)-hx)/g['dx']+(np.roll(hy,-1,axis=1)-hy)/g['dy']
    return np.diff(hx,axis=0)/g['dx']+np.diff(hy,axis=1)/g['dy']


def field_error(fields,reference,g):
    squared=[];norm=[]
    for a,b,name in zip(fields,reference,('e','hx','hy')):
        squared.append(inner(a-b,a-b,g,name));norm.append(inner(b,b,g,name))
    # Normalize electric and magnetic parts by the constant total modal norm,
    # avoiding division by zero at a cavity's E/H temporal nodes.
    scale=g['lx']*g['ly']/(4 if g['boundary']=='pec' else 1)
    return float(np.sqrt(squared[0]/scale)),float(np.sqrt(sum(squared[1:])/scale)),float(np.sqrt(sum(squared)/scale))


def projected_frequency(amplitudes,dt):
    """Infer oscillator frequency from the evolved three-level recurrence."""
    a=np.asarray(amplitudes)
    q=float(np.dot(a[1:-1],a[:-2]+a[2:])/(2*np.dot(a[1:-1],a[1:-1])))
    return float(np.arccos(np.clip(q,-1,1))/dt)


def run_mesh(p,nx,ny):
    lx,ly=p['lengths'];mode=p['mode']
    omega=float(np.hypot((2 if p['boundary']=='periodic' else 1)*np.pi*mode[0]/lx,
                         (2 if p['boundary']=='periodic' else 1)*np.pi*mode[1]/ly))
    period=2*np.pi/omega
    end=p['error_periods']*period
    maximum=p['courant']/np.sqrt((nx/lx)**2+(ny/ly)**2)
    steps=int(np.ceil(end/maximum));dt=end/steps
    g=grid(nx,ny,lx,ly,dt,p['boundary'])
    e,hx,hy=exact_fields(g,mode,0,-dt/2)
    div0=divergence(hx,hy,g)
    u0,_=energies(e,hx,hy,g)
    mode_shape=exact_fields(g,mode,0,0)[0]
    denominator=inner(mode_shape,mode_shape,g,'e')
    history=[];amplitudes=[];max_drift=0.;div_drift=0.;boundary=0.
    total_steps=int(np.ceil(p['energy_periods']*period/dt))
    snapshot=None
    for n in range(total_steps+1):
        u,v=energies(e,hx,hy,g)
        amplitude=inner(e,mode_shape,g,'e')/denominator
        amplitudes.append(amplitude)
        history.append([nx,ny,n*dt,u,v,amplitude])
        max_drift=max(max_drift,abs(u/u0-1))
        div_drift=max(div_drift,float(np.max(np.abs(divergence(hx,hy,g)-div0))))
        if p['boundary']=='pec':
            boundary=max(boundary,float(np.max(np.abs(e[[0,-1],:]))),float(np.max(np.abs(e[:,[0,-1]]))))
        if n==steps:
            ref=exact_fields(g,mode,end,end-dt/2)
            err=field_error((e,hx,hy),ref,g)
            snapshot=(e.copy(),ref[0],g)
        if n<total_steps:e,hx,hy=step(e,hx,hy,g)
    frequency=projected_frequency(amplitudes,dt)
    *_,omega_h,sx,sy=frequencies(g,mode)
    physical=np.asarray(history)[:,4]
    metrics=dict(nx=nx,ny=ny,steps=steps,energy_steps=total_steps,dt=dt,
                 actual_courant=float(dt*np.sqrt(g['dx']**-2+g['dy']**-2)),
                 electric_relative_l2=err[0],magnetic_relative_l2=err[1],field_relative_l2=err[2],
                 analytic_frequency=omega,discrete_frequency=omega_h,measured_frequency=frequency,
                 relative_frequency_error=abs(frequency/omega-1),
                 dispersion_identity_relative_error=abs(frequency/omega_h-1),
                 modified_energy_max_relative_drift=max_drift,
                 synchronized_energy_relative_span=float((physical.max()-physical.min())/(.125*lx*ly if p['boundary']=='pec' else .5*lx*ly)),
                 synchronized_energy_max_relative_error=float(np.max(np.abs(physical/(.125*lx*ly if p['boundary']=='pec' else .5*lx*ly)-1))),
                 boundary_e_max=boundary,magnetic_divergence_drift_max=div_drift,
                 initial_magnetic_divergence_max=float(np.abs(div0).max()),
                 modified_energy_initial=u0)
    return metrics,history,snapshot
