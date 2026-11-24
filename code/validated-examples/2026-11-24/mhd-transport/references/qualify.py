"""Independent-reference algebra and numerical-field qualification, no PDE solver."""
from pathlib import Path
import json,hashlib
import numpy as np


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def restrict(q, shape):
    nx, ny = shape
    fx, fy = q.shape[0]//nx, q.shape[1]//ny
    if fx*nx != q.shape[0] or fy*ny != q.shape[1]:raise ValueError('Nested grids required')
    return q.reshape(nx,fx,ny,fy,q.shape[-1]).mean(axis=(1,3))


def pressure(q):
    return (2/3)*(q[...,4]-.5*np.sum(q[...,1:4]**2,axis=-1)/q[...,0]-.5*np.sum(q[...,5:8]**2,axis=-1))


def relative_l1(a,b):return float(np.sum(abs(a-b))/np.sum(abs(b)))



def official_initial(row):
    """Independent algebra matching the inspected pinned problem generators."""
    nx,ny=row['nx'],row['n']
    if row['kind']=='loop':xl,xr,yl,yr=-1.,1.,-.5,.5
    else:xl,xr,yl,yr=-.5,.5,-.5,.5
    dx,dy=(xr-xl)/nx,(yr-yl)/ny
    xf=xl+np.arange(nx+1)*dx;yf=yl+np.arange(ny+1)*dy
    x=xf[:-1]+dx/2;y=yf[:-1]+dy/2
    if row['kind']=='loop':
        az=.001*np.maximum(.3-np.hypot(xf[:,None],yf[None,:]),0.)
        rho=np.ones((nx,ny));v=np.broadcast_to([2.,1.,2.],(nx,ny,3));p=np.ones((nx,ny))
    else:
        az=(np.cos(4*np.pi*xf[:,None])-2*np.cos(2*np.pi*yf[None,:]))/(4*np.pi*np.sqrt(4*np.pi))
        rho=np.full((nx,ny),25/(36*np.pi));v=np.zeros((nx,ny,3));v[...,0]=np.sin(2*np.pi*y)[None,:];v[...,1]=-np.sin(2*np.pi*x)[:,None];p=np.full((nx,ny),5/(12*np.pi))
    q=np.zeros((nx,ny,8));q[...,0]=rho;q[...,1:4]=rho[...,None]*v
    q[...,5]=.5*((az[:-1,1:]-az[:-1,:-1])+(az[1:,1:]-az[1:,:-1]))/dy
    q[...,6]=-.5*((az[1:,:-1]-az[:-1,:-1])+(az[1:,1:]-az[:-1,1:]))/dx
    q[...,4]=p/(2/3)+.5*rho*np.sum(v*v,axis=-1)+.5*np.sum(q[...,5:8]**2,axis=-1)
    return q


def qualify(directory, records, plan):
    directory=Path(directory);data={}
    for row in records:
        with np.load(directory/row['file'],allow_pickle=False) as d:data[row['id']]={k:d[k].copy() for k in d.files}
    checks=[]
    def add(name,value,bound,ok):checks.append(dict(name=name,value=value,bound=bound,passed=bool(ok)))
    for row in records:
        d=data[row['id']];q=d['q_history'];p=pressure(q)
        initial_difference=float(np.max(abs(q[0]-official_initial(row))))
        add(row['id']+' inspected generator initialization',initial_difference,2e-12,initial_difference<=2e-12)
        add(row['id']+' finite positive states',bool(np.isfinite(q).all() and (q[...,0]>0).all() and (p>0).all()),True,np.isfinite(q).all() and (q[...,0]>0).all() and (p>0).all())
        add(row['id']+' exact requested output times',d['times'].tolist(),row['snapshots'],np.allclose(d['times'],row['snapshots'],rtol=0,atol=1e-14))
        totals=q[...,:5].mean(axis=(1,2));scale=np.maximum(abs(totals[0]),1.)
        drift=float(np.max(abs(totals-totals[0])/scale))
        add(row['id']+' conserved fluid integrals',drift,plan['limits']['relative_mass_energy_drift'],drift<=plan['limits']['relative_mass_energy_drift'])
    for kind,low,high in [('loop',64,128),('ot',128,256)]:
        coarse=data[f'{kind}-n{low}-cfl0p3']['q_history'][-1]
        fine=data[f'{kind}-n{high}-cfl0p3']['q_history'][-1]
        half=data[f'{kind}-n{high}-cfl0p15']['q_history'][-1]
        projected=restrict(fine,coarse.shape[:2])
        if kind=='loop':
            for label,value,key in [('space',relative_l1(coarse[...,5:7],projected[...,5:7]),'loop_spatial_relative_B_l1'),('time',relative_l1(fine[...,5:7],half[...,5:7]),'loop_time_relative_B_l1')]:
                add('loop '+label+' reference increment',value,plan['limits'][key],value<=plan['limits'][key])
        else:
            for label,a,b,prefix in [('space',coarse,projected,'ot_spatial'),('time',fine,half,'ot_time')]:
                for field,aa,bb in [('density',a[...,0],b[...,0]),('pressure',pressure(a),pressure(b))]:
                    value=relative_l1(aa,bb);key=prefix+'_relative_'+field+'_l1'
                    add('ot '+label+' '+field+' reference increment',value,plan['limits'][key],value<=plan['limits'][key])
            contrast=float(np.max(half[...,0])/np.min(half[...,0]));bound=plan['limits']['ot_final_density_contrast_minimum']
            add('finite-grid late OT density contrast',contrast,bound,contrast>=bound)
    return {'passed':len(records)==6 and len(checks)==31 and all(c['passed'] for c in checks),'checks':checks,'scope':'Actual independent Athena++ finite-grid calculations; two spatial grids and a halved-CFL companion for each problem. Density contrast is a compression diagnostic, not a proof of a continuum shock or an error bound.'}
