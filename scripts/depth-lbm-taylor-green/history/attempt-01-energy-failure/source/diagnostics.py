"""Fixed continuum-unit diagnostics. No field repair or observed-speed normalization."""
import csv
from pathlib import Path
import numpy as np
from geometry import C,full_field,moments

def rms(a):return float(np.sqrt(np.mean(np.asarray(a)**2)))
def relative(a,b):return rms(np.asarray(a)-b)/rms(b)

def physical(f,g):
    rho,u=moments(f);velocity=u*g['dx']/g['dt'];p=(rho-np.mean(rho))/3*(g['dx']/g['dt'])**2
    return rho,velocity,p

def budgets(f0,f,h,g,velocity_scale):
    def totals(state):return np.r_[np.sum(state),np.sum(np.einsum('qd,qn->dn',C,state),axis=1)]
    initial=totals(f0);final=totals(f)
    states=np.vstack([h[:,:3],final]);increments=np.vstack([np.zeros(3),np.cumsum(h[:,3:6],axis=0)])
    defect=states-initial-increments
    mass_scale=initial[0];momentum_scale=initial[0]*velocity_scale
    rho,u=moments(f)
    return dict(mass_drift=abs(float(final[0]-initial[0]))/mass_scale,
                mass_ledger=float(np.max(abs(defect[:,0])))/mass_scale,
                momentum_ledger=float(np.max(abs(defect[:,1:])))/momentum_scale,
                max_mach=max(float(np.max(h[:,9])),float(np.max(np.sqrt(np.sum(u*u,axis=0))*np.sqrt(3)))),
                min_rho=min(float(np.min(h[:,10])),float(np.min(rho))),
                max_rho=max(float(np.max(h[:,11])),float(np.max(rho))),
                min_population=min(float(np.min(h[:,12])),float(np.min(f))),
                wall_mass_exchange=float(np.sum(h[:,13])),open_mass_exchange=float(np.sum(h[:,14])),
                final_lattice_momentum_x=float(final[1]),final_lattice_momentum_y=float(final[2]))

def ghia_tables(root):
    with (Path(root)/'references/ghia-re100.csv').open() as stream:rows=list(csv.DictReader(stream))
    return {component:np.array([[float(r['coordinate']),float(r['value'])] for r in rows
                               if r['component']==component]) for component in ['u','v']}

def cavity_profiles(f,g,nominal_lid):
    _,u=moments(f);ux=full_field(u[0]/nominal_lid,g);uy=full_field(u[1]/nominal_lid,g)
    n=g['nx'];coordinate=np.r_[0.,(np.arange(n)+.5)/n,1.]
    xmid=(ux[:,n//2-1]+ux[:,n//2])/2 if n%2==0 else ux[:,n//2]
    ymid=(uy[n//2-1,:]+uy[n//2,:])/2 if n%2==0 else uy[n//2,:]
    return coordinate,np.r_[0.,xmid,1.],np.r_[0.,ymid,0.]

def vortex(f,g,nominal_lid):
    # At the primary vortex both components vanish. Piecewise bilinear cells
    # are searched in a fixed interior box, then solve for a local zero.
    from scipy.optimize import root
    _,u=moments(f);ux=full_field(u[0]/nominal_lid,g);uy=full_field(u[1]/nominal_lid,g)
    axis=(np.arange(g['nx'])+.5)*g['dx'];candidates=[]
    for j in range(g['ny']-1):
        for i in range(g['nx']-1):
            if not(.4<=axis[i]<=.8 and .5<=axis[j]<=.9):continue
            a,b=ux[j:j+2,i:i+2],uy[j:j+2,i:i+2]
            if not(a.min()<=0<=a.max() and b.min()<=0<=b.max()):continue
            def field(z):
                tx,ty=z;weights=np.array([[(1-tx)*(1-ty),tx*(1-ty)],[(1-tx)*ty,tx*ty]])
                return [float(np.sum(weights*a)),float(np.sum(weights*b))]
            sol=root(field,[.5,.5],tol=1e-11)
            if np.all(sol.x>=0) and np.all(sol.x<=1) and np.linalg.norm(sol.fun)<1e-9:
                candidates.append(np.array([axis[i],axis[j]])+g['dx']*sol.x)
    if not candidates:raise ArithmeticError('No primary vortex zero in fixed search box')
    if len(candidates)>1 and max(np.linalg.norm(p-candidates[0]) for p in candidates)>g['dx']:
        raise ArithmeticError('Ambiguous primary vortex zeros')
    return candidates[0]

def cylinder_probes(f,g):
    rho,u,p=physical(f,g);uf=full_field(u[0],g);pf=full_field(p,g)
    y=(np.arange(g['ny'])+.5)*g['dx'];x=np.arange(g['nx'])*g['dx']
    row_u=np.array([np.interp(.2,y,uf[:,i]) for i in range(g['nx'])])
    # The four surrounding pressure sites at both surface probes are fluid.
    front=np.interp(.2,y,pf[:,int(round(.15/g['dx']))])
    back=np.interp(.2,y,pf[:,int(round(.25/g['dx']))])
    wake=np.where((x[:-1]>.25)&(row_u[:-1]<0)&(row_u[1:]>=0))[0]
    if len(wake)!=1:raise ArithmeticError('Expected exactly one recirculation endpoint')
    i=int(wake[0]);root_x=x[i]-row_u[i]*(x[i+1]-x[i])/(row_u[i+1]-row_u[i])
    return dict(pressure_difference=float(front-back),recirculation_length=float(root_x-.25)),row_u

def interval_distance(value,interval):
    return max(interval[0]-value,0.,value-interval[1])
