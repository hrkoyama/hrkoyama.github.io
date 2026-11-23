"""Bounded 2D ENO2/Heun level-set advection with optional Godunov redistancing."""
import math
import time
import numpy as np
from geometry import distance, grid, measure


class Budget:
    def __init__(self, seconds):
        if not math.isfinite(seconds) or not 0 < seconds <= 90:
            raise ValueError('Require a budget in (0,90] seconds')
        self.deadline = time.monotonic()+seconds

    def check(self):
        if time.monotonic() > self.deadline:
            raise RuntimeError('Fixed calculation budget exhausted')


def validate(config):
    if config['motion'] not in ['translation','rotation'] or config['grids'] != [32,64,128]:
        raise ValueError('Require the reviewed motion and 32/64/128 grids')
    for name in ['radius','time','cfl','reinit_interval','pseudo_cfl']:
        if type(config[name]) not in [int,float] or not math.isfinite(config[name]) or config[name] <= 0:
            raise ValueError('Require finite positive '+name)
    if config['time'] != 1 or config['radius'] != .15 or config['cfl'] > .4 or config['pseudo_cfl'] > .3:
        raise ValueError('Outside the fixed educational scope')
    if config['snapshots'] != [0,.25,.5,.75,1] or config['reinit_interval'] != .1 or config['pseudo_steps'] != 5:
        raise ValueError('Unreviewed observation/redistancing schedule')
    for key in ['center','velocity','pivot']:
        vector=np.asarray(config[key],dtype=float)
        if vector.shape != (2,) or not np.isfinite(vector).all():raise ValueError('Invalid '+key)
    if not math.isfinite(config['omega']) or abs(config['omega']) > 2*math.pi:
        raise ValueError('Unbounded angular velocity')
    if config['motion']=='translation' and np.max(np.abs(config['velocity'])) > .25:
        raise ValueError('Unbounded translation')
    for value in config['acceptance'].values():
        if type(value) not in [float,int] or not math.isfinite(value) or value < 0:
            raise ValueError('Invalid acceptance bound')


def velocity(config,x,y):
    if config['motion']=='translation':
        return np.full_like(x,config['velocity'][0]),np.full_like(y,config['velocity'][1])
    return -config['omega']*(y-config['pivot'][1]),config['omega']*(x-config['pivot'][0])


def eno2(padded,dx):
    q = padded[2:-2,2:-2]
    xm,xp = padded[2:-2,1:-3],padded[2:-2,3:-1]
    ym,yp = padded[1:-3,2:-2],padded[3:-1,2:-2]
    xx = (xp-2*q+xm)/dx**2; yy = (yp-2*q+ym)/dx**2
    left=(q-2*xm+padded[2:-2,:-4])/dx**2
    right=(padded[2:-2,4:]-2*xp+q)/dx**2
    down=(q-2*ym+padded[:-4,2:-2])/dx**2
    up=(padded[4:,2:-2]-2*yp+q)/dx**2
    choose=lambda a,b:np.where(np.abs(a)<=np.abs(b),a,b)
    return ((q-xm)/dx+.5*dx*choose(xx,left),
            (xp-q)/dx-.5*dx*choose(xx,right),
            (q-ym)/dx+.5*dx*choose(yy,down),
            (yp-q)/dx-.5*dx*choose(yy,up))


def rhs(phi,config,time,coordinates,velocities):
    n=len(phi); dx=1/n; xghost,yghost=coordinates
    # Prescribed analytic exterior data only. Every interior value is numerical.
    padded=distance(config,xghost,yghost,time)
    padded[2:-2,2:-2]=phi
    xm,xp,ym,yp=eno2(padded,dx)
    u,v=velocities
    return -(np.maximum(u,0)*xm+np.minimum(u,0)*xp+
             np.maximum(v,0)*ym+np.minimum(v,0)*yp)


def redistance(phi,dx,iterations,pseudo_cfl):
    """First-order Godunov pseudo-time updates; sign is frozen per call.

    No volume correction, zero-contour projection, clipping or analytic reset.
    Constant exterior extrapolation is confined to this auxiliary operation.
    """
    value=phi.copy(); sign=phi/np.sqrt(phi*phi+dx*dx)
    for _ in range(iterations):
        padded=np.pad(value,1,mode='edge')
        xm=(value-padded[1:-1,:-2])/dx; xp=(padded[1:-1,2:]-value)/dx
        ym=(value-padded[:-2,1:-1])/dx; yp=(padded[2:,1:-1]-value)/dx
        positive=np.maximum(np.maximum(xm,0)**2,np.minimum(xp,0)**2)+np.maximum(np.maximum(ym,0)**2,np.minimum(yp,0)**2)
        negative=np.maximum(np.minimum(xm,0)**2,np.maximum(xp,0)**2)+np.maximum(np.minimum(ym,0)**2,np.maximum(yp,0)**2)
        gradient=np.sqrt(np.where(sign>=0,positive,negative))
        value+=pseudo_cfl*dx*sign*(1-gradient)
    return value


def integrate(config,n,reinitialize,budget,cfl=None):
    x,y=grid(n); dx=1/n
    axis=(np.arange(-2,n+2)+.5)/n
    ghost=np.meshgrid(axis,axis,indexing='xy')
    speeds=velocity(config,x,y)
    maximum=float(np.max(np.abs(speeds[0])+np.abs(speeds[1])))
    if maximum<=0:raise ValueError('Use a nonzero prescribed velocity')
    step=(config['cfl'] if cfl is None else cfl)*dx/maximum
    phi=distance(config,x,y,0)
    times=sorted(set(config['snapshots']+[round(.1*i,12) for i in range(1,11)]))
    time_now=0.; steps=0; calls=0; records=[]; contours=[]; redistance_log=[]
    max_courant=0.; maximum_reinit_jump=0.
    row,points=measure(phi,config,0);records.append(row);contours.append(points.tolist())
    for stop in times[1:]:
        while time_now < stop-2e-15:
            budget.check(); h=min(step,stop-time_now)
            stage=phi+h*rhs(phi,config,time_now,ghost,speeds)
            phi=.5*phi+.5*(stage+h*rhs(stage,config,time_now+h,ghost,speeds))
            if not np.isfinite(phi).all() or np.max(np.abs(phi))>4:
                raise RuntimeError('Nonfinite or unbounded numerical field')
            time_now+=h;steps+=1;max_courant=max(max_courant,h*maximum/dx)
        time_now=stop
        if reinitialize and math.isclose(stop/.1,round(stop/.1),abs_tol=1e-10):
            before,_=measure(phi,config,stop)
            phi=redistance(phi,dx,config['pseudo_steps'],config['pseudo_cfl']);calls+=1
            after,_=measure(phi,config,stop)
            jump=after['area']-before['area'];maximum_reinit_jump=max(maximum_reinit_jump,abs(jump))
            redistance_log.append({'time':stop,'area_before':before['area'],'area_after':after['area'],
                                  'area_change':jump,'interface_error_before':before['interface_max_radial_error'],
                                  'interface_error_after':after['interface_max_radial_error']})
        if stop in config['snapshots']:
            row,points=measure(phi,config,stop);records.append(row);contours.append(points.tolist())
    return phi,{'n':n,'mode':'redistance' if reinitialize else 'advection-only','steps':steps,
                'redistance_calls':calls,'pseudo_steps':calls*config['pseudo_steps'],
                'maximum_courant':max_courant,'maximum_reinitialization_area_jump':maximum_reinit_jump,
                'maximum_interface_error':max(r['interface_max_radial_error'] for r in records[1:]),
                'maximum_relative_area_error':max(abs(r['relative_area_bias']) for r in records[1:]),
                'snapshots':records,'contours':contours,'redistance_log':redistance_log,
                'state_clip_count':0,'volume_correction_count':0,'rejected_steps':0}


def run_case(config,budget):
    validate(config);rows=[];fields={}
    for mode in [False,True]:
        previous=None
        for n in config['grids']:
            phi,row=integrate(config,n,mode,budget)
            if previous is not None:row['observed_order']=math.log2(previous/row['maximum_interface_error'])
            previous=row['maximum_interface_error'];rows.append(row)
            if n==config['grids'][-1]:fields[row['mode']]=phi
    plain=[r for r in rows if r['mode']=='advection-only'];red=[r for r in rows if r['mode']=='redistance']
    normal64,_=integrate(config,64,False,budget)
    half64,_=integrate(config,64,False,budget,cfl=config['cfl']/2)
    x,y=grid(64);band=np.abs(distance(config,x,y,config['time']))<=2/64
    sensitivity=float(np.sqrt(np.mean((half64[band]-normal64[band])**2)))
    bound=config['acceptance']
    checks={'advection_interface_refines':all(b['maximum_interface_error']<a['maximum_interface_error'] for a,b in zip(plain,plain[1:])),
            'advection_order_resolved':bound['order_min']<=plain[-1]['observed_order']<=bound['order_max'],
            'advection_finest_interface':plain[-1]['maximum_interface_error']<=bound['interface_max'],
            'advection_finest_area':plain[-1]['maximum_relative_area_error']<=bound['area_relative_max'],
            'redistance_finest_interface':red[-1]['maximum_interface_error']<=bound['redistance_interface_max'],
            'redistance_finest_area':red[-1]['maximum_relative_area_error']<=bound['redistance_area_relative_max'],
            'shared_observation_times':all([s['time'] for s in r['snapshots']]==config['snapshots'] for r in rows),
            'courant_bound':all(r['maximum_courant']<=config['cfl']*(1+1e-12) for r in rows),
            'time_step_sensitivity':sensitivity<=bound['time_sensitivity_max'],
            'fixed_redistance_schedule':all(r['redistance_calls']==10 for r in red) and all(r['redistance_calls']==0 for r in plain)}
    metrics={'finest_grid':128,'final_time':config['time'],'advection_observed_order':plain[-1]['observed_order'],
             'advection_finest_interface_error':plain[-1]['maximum_interface_error'],
             'advection_finest_relative_area_error':plain[-1]['maximum_relative_area_error'],
             'redistance_finest_interface_error':red[-1]['maximum_interface_error'],
             'redistance_finest_relative_area_error':red[-1]['maximum_relative_area_error'],
             'redistance_maximum_area_jump':max(r['maximum_reinitialization_area_jump'] for r in red),
             'cfl_halving_band_phi_difference_n64':sensitivity}
    return {'passed':all(checks.values()),'metrics':metrics,'checks':checks,'records':rows,
            'reference_scope':'Analytic center motion and signed distance for a prescribed rigid circle motion; no separate PDE engine or VOF implementation.'},fields
