"""Independent manufactured, Decimal, Jacobi and full-ODE references.

No imports from production models, Newton, or experiments are allowed here.
"""
from decimal import Decimal as D,localcontext
from fractions import Fraction as F
import json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import ellipj,ellipk
from io_contract import save_arrays,save_json


def decimal_exp(value):
    with localcontext() as ctx:
        ctx.prec=80
        return (+D(value).exp())


def decimal_index1_root(t0,yold,h):
    with localcontext() as ctx:
        ctx.prec=80
        t,h=D(t0),D(h);old=D(yold);e=(-2*(t+h)/3).exp()
        def fun(z):return z**3-((old+h*(z-e))/(1+h))**2
        lo,hi=D(2)/5,D(6)/5
        if not fun(lo)<0<fun(hi):raise ArithmeticError('Independent positive branch bracket failed')
        for _ in range(256):
            mid=(lo+hi)/2
            if fun(mid)>0:hi=mid
            else:lo=mid
        z=(lo+hi)/2;y=(old+h*(z-e))/(1+h)
        return y,z,hi-lo


def index1_qualification():
    with localcontext() as ctx:
        ctx.prec=80
        checks={};fixtures=[]
        for k,t in enumerate((D(0),D(1)/2,D(1))):
            y=(-t).exp();z=(-2*t/3).exp()
            checks['MMS-'+str(k)]=abs(z**3-y*y)<D('1e-75') and abs(-y+y-z+(-2*t/3).exp())<D('1e-75')
        e=(-D(1)).exp()
        checks['nonexpansive-positive-region']=(-1+D(2)/3*e**(-D(1)/3))<0 and (D(2)/3*e**(-D(1)/3))<1
        checks['initial-differentiated-constraint']=3*(-D(2)/3)-2*(-D(1))==0
        for t,old,h in [(D(0),D(1),D(1)/16),(D(1)/2,(-D(1)/2).exp(),D(1)/32),(D(31)/32,(-D(31)/32).exp(),D(1)/32)]:
            y,z,width=decimal_index1_root(t,old,h)
            fixtures.append({'t0':str(t),'yold':str(old),'h':str(h),'y':str(y),'z':str(z),'width':str(width)})
        checks['three-positive-branch-brackets']=all(D(f['width'])<=D('1e-60') and D(f['y'])>0 and D(f['z'])>0 for f in fixtures)
        return checks,fixtures


def raw_solve(output,ident,rhs,span,initial,times,method,rtol,atol):
    """Keep owned last callback on ordinary failure; accepted history on return."""
    last={'time':np.array([span[0]]),'state':np.array(initial,copy=True)}
    def observed(t,y):
        last.clear();last.update(time=np.array([t]),state=y.copy())
        value=rhs(t,y);last['rhs']=np.array(value,copy=True)
        return value
    save_arrays(output/(ident+'-entered.npz'),initial=initial,times=times)
    try:sol=solve_ivp(observed,span,np.array(initial,copy=True),method=method,t_eval=times,rtol=rtol,atol=atol,jac=None) if method in ('Radau','BDF') else solve_ivp(observed,span,np.array(initial,copy=True),method=method,t_eval=times,rtol=rtol,atol=atol)
    except BaseException:
        save_arrays(output/(ident+'-last-callback.npz'),**last)
        raise
    save_arrays(output/(ident+'.npz'),time=sol.t,states=sol.y.T,status=[sol.status],nfev=[sol.nfev],njev=[sol.njev],nlu=[sol.nlu])
    if not sol.success or not np.array_equal(sol.t,times) or not np.isfinite(sol.y).all():raise ArithmeticError('Independent reference did not complete its fixed observations')
    return sol.y.T,{'id':ident,'method':method,'nfev':sol.nfev,'njev':sol.njev,'nlu':sol.nlu,'status':sol.status,'observations':len(sol.t)}


def printed_intervals(path):
    data=json.loads(Path(path).read_text());values=[]
    for row in data['printed_rows']:
        with localcontext() as ctx:
            ctx.prec=80
            lo=[str(D(x)-D(h)) for x,h in zip(row['y'],row['printing_halfwidth'])]
            hi=[str(D(x)+D(h)) for x,h in zip(row['y'],row['printing_halfwidth'])]
        values.append({'t':row['t'],'lower':lo,'upper':hi})
    return values


def robertson_reference(output,cfg,times,limits,printed_path):
    def rhs(t,y):
        return np.array([-.04*y[0]+10000*y[1]*y[2],.04*y[0]-10000*y[1]*y[2]-30000000*y[1]**2,30000000*y[1]**2])
    values=[];counters=[]
    for spec in cfg['references']:
        value,count=raw_solve(output,'reference-'+spec['id'],rhs,(0.,4.),[1.,0.,0.],times,spec['method'],spec['rtol'],spec['atol'])
        values.append(value);counters.append(count)
    checks={};checks['all-reference-complete-finite-nonnegative']=all(np.isfinite(v).all() and float(v.min())>=limits['all_reference_complete_finite_and_nonnegative_min'] for v in values)
    for k,key in [(0,'Radau_loose_tight_max_component_difference'),(2,'Radau_tight_BDF_max_component_difference')]:
        difference=np.max(np.abs(values[k]-values[1]),axis=0)
        checks['reference-agreement-'+str(k)]=bool(np.all(difference<=np.array(limits[key])))
    intervals=printed_intervals(printed_path);distances=[]
    for row in intervals:
        idx=np.where(times==float(row['t']))[0]
        if len(idx)!=1:raise ArithmeticError('Official observation absent from reference grid')
        actual=values[1][idx[0]];lo=np.array(row['lower'],float);hi=np.array(row['upper'],float)
        distances.append(np.maximum(np.maximum(lo-actual,actual-hi),0))
    checks['official-IDA-printed-interval-qualification']=bool(np.all(np.array(distances)<=np.array(limits['official_IDA_to_tight_reference_distance_from_rounding_intervals_max'])))
    save_json(output/'robertson-reference-qualification.json',{'passed':all(checks.values()),'checks':checks,'counters':counters,'printed_intervals':intervals,'IDA_new_executions':0,'printed_interval_distances':np.array(distances).tolist()})
    return values[1],checks,intervals,counters


def pendulum_exact(times,theta=.7):
    k=np.sin(theta/2);m=k*k;K=ellipk(m);s,c,d,_=ellipj(K-np.array(times),m)
    qx=2*k*s*d;qy=-1+2*m*s*s;omega=-2*k*c
    return np.column_stack((qx,qy,omega*(-qy),omega*qx)),K


def agm_K(theta):
    with localcontext() as ctx:
        ctx.prec=80
        def atan(x):
            total=D(0);term=x
            for n in range(256):total+=term/D(2*n+1);term*=-x*x
            return total,abs(term)/D(513)
        a,ea=atan(D(1)/5);b,eb=atan(D(1)/239);pi=16*a-4*b
        x=D(str(theta))/2;term=x;ss=x
        for n in range(1,80):term*=-x*x/D((2*n)*(2*n+1));ss+=term
        aa=D(1);bb=(1-ss*ss).sqrt()
        for _ in range(24):aa,bb=(aa+bb)/2,(aa*bb).sqrt()
        return float(pi/(2*aa)),{'machin_remainder_bound':str(16*ea+4*eb),'agm_gap':str(abs(aa-bb)),'sine_last_term':str(abs(term))}


def pendulum_qualification(output,cfg,limits):
    times=np.linspace(0.,cfg['T'],33)
    def rhs(t,z):return np.array([z[1],-np.sin(z[0])])
    values=[];counts=[]
    for index,spec in enumerate(cfg['reference_angular_runs']):
        angular,counter=raw_solve(output,'angular-reference-'+str(index),rhs,(0.,float(cfg['T'])),[cfg['theta0'],0.],times,spec['method'],spec['rtol'],spec['atol'])
        theta=angular[:,0];omega=angular[:,1]
        values.append(np.column_stack((np.sin(theta),-np.cos(theta),omega*np.cos(theta),omega*np.sin(theta))))
        counts.append(counter)
    exact,K=pendulum_exact(times,cfg['theta0']);Kother,notes=agm_K(cfg['theta0'])
    q=exact[:,:2];v=exact[:,2:];energy=.5*np.sum(v*v,axis=1)+q[:,1]
    initial=np.array([np.sin(cfg['theta0']),-np.cos(cfg['theta0']),0.,0.])
    identities=max(float(np.max(np.abs(np.sum(q*q,axis=1)-1))),float(np.max(np.abs(np.sum(q*v,axis=1)))),float(np.max(np.abs(energy-energy[0]))))
    checks={'Jacobi-angular-agreement':float(np.max(np.abs(exact-values[1])))<=limits['Jacobi_to_tight_angular_DOP853_max_state_error'],
            'angular-tolerance-agreement':float(np.max(np.abs(values[0]-values[1])))<=limits['loose_tight_angular_DOP853_max_state_difference'],
            'Jacobi-initial':float(np.max(np.abs(exact[0]-initial)))<=limits['Jacobi_initial_state_error_max'],
            'Jacobi-invariants':identities<=limits['Jacobi_energy_and_circle_tangency_identity_max'],
            'AGM-K':abs(K-Kother)<=limits['K_AGM_to_SciPy_ellipk_abs_error_max'],
            'Decimal-remainder-qualification':D(notes['machin_remainder_bound'])<D('1e-75') and D(notes['agm_gap'])<D('1e-75') and D(notes['sine_last_term'])<D('1e-75')}
    # Exact rational identities at nonzero C,D; gravity and work signs checked.
    q=(F(3,5),F(-9,10));v=(F(1,7),F(2,9));r2=sum(x*x for x in q);dd=sum(a*b for a,b in zip(q,v));cc=(r2-1)/2;vv=sum(x*x for x in v)
    for stabilize in (False,True):
        lam=(vv-q[1]+(2*dd+cc if stabilize else 0))/r2
        cddot=vv-lam*r2-q[1]
        checks['constraint-identity-'+str(stabilize)]=cddot==(-2*dd-cc if stabilize else 0)
        acceleration=(-lam*q[0],-lam*q[1]-1)
        hdot=sum(a*b for a,b in zip(v,acceleration))+v[1]
        checks['constraint-work-'+str(stabilize)]=hdot==-lam*dd
    save_arrays(output/'pendulum-reference-qualification.npz',time=times,jacobi=exact,angular_loose=values[0],angular_tight=values[1])
    save_json(output/'pendulum-reference-qualification.json',{'passed':all(checks.values()),'checks':checks,'counters':counts,'AGM':notes,'K_error':abs(K-Kother)})
    return checks,counts
