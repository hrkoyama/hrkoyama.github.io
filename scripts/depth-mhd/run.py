"""Small cross-implementation fluid/MHD validation; frozen sources remain unchanged."""
import argparse,csv,hashlib,json,time
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from legacy.mhd import solve_orszag_tang,primitive as planar_primitive
from legacy.mhd_tests import solve_1d
from legacy.hlld import primitive as mhd_primitive
from legacy.benchmarks import get_problem
from legacy.solvers import solve

ROOT=Path(__file__).resolve().parent

def read_reference(case,n):
    path=ROOT/'references'/f'athena-{case}-{n}.npz'
    return np.load(path)['table']

def cell_average_1d(a,n,xlo,xhi,columns):
    # A piecewise-constant integral of independent fine-cell averages, not point interpolation.
    x=a[:,1];dx=(xhi-xlo)/len(x);edges=np.linspace(xlo,xhi,len(x)+1)
    target=np.linspace(xlo,xhi,n+1)
    values=[]
    for c in columns:
        integral=np.r_[0.,np.cumsum(a[:,c])*dx]
        values.append(np.diff(np.interp(target,edges,integral))/(target[1]-target[0]))
    return np.stack(values,axis=-1)

def block_average(a,n,columns):
    fine=int(round(len(a)**.5));assert fine*fine==len(a) and fine%n==0
    r=fine//n
    # Athena table has x1 running fastest, whereas atlas arrays have x index first.
    return np.stack([a[:,c].reshape(fine,fine).T.reshape(n,r,n,r).mean(axis=(1,3)) for c in columns],axis=-1)

def independent_1d(case,cfg):
    grids=cfg['reference_grids'];ref=read_reference(case,grids[-1]);previous=read_reference(case,grids[-2])
    cols=[2,7] if case=='brio' else [2]
    # Table columns for Brio are i,x,rho,p,vx,vy,vz,Bx,By,Bz; use By at 8.
    if case=='brio':cols=[2,8]
    lo,hi=(0.,1.) if case=='brio' else (-5.,5.)
    reference_records=[]
    for coarse,fine in zip(grids,grids[1:]):
        a=read_reference(case,coarse);b=read_reference(case,fine)
        delta=float(np.max(np.mean(abs(cell_average_1d(b,coarse,lo,hi,cols)-a[:,cols]),axis=0)))
        reference_records.append({'coarse_n':coarse,'fine_n':fine,'last_pair_l1':delta,'target':cfg['acceptance']['independent_reference_l1'],'target_reached':delta<cfg['acceptance']['independent_reference_l1']})
    refdiff=reference_records[-1]['last_pair_l1']
    records=[];last=None;finest_solution=None
    for n in cfg['grids']:
        exact=cell_average_1d(ref,n,lo,hi,cols)
        if case=='brio':
            result=solve_1d(n=n,final_time=cfg['time'],cfl=cfg['cfl']);w=mhd_primitive(result.q,2.);values=w[:,[0,6]]
        else:
            p=get_problem('shu-osher');result=solve(p,n=n,method='muscl',riemann='hllc',limiter='mc',cfl=cfg['cfl']);w=p.equation.primitive(result.q);values=w[:,[0]]
        error=np.mean(abs(values-exact),axis=0)
        record={'n':n,'density_l1':float(error[0]),'steps':result.steps,'min_density':float(w[:,0].min()),'min_pressure':float(w[:,4 if case=='brio' else 2].min())}
        if case=='brio':record['by_l1']=float(error[1])
        records.append(record);last=values;finest_solution=np.column_stack((np.linspace(lo,hi,n,endpoint=False)+(hi-lo)/n/2,values,exact))
    t=cfg['acceptance'];checks={'independent_reference_refined':refdiff<t['independent_reference_l1'],'density_error':records[-1]['density_l1']<t['finest_density_l1'],'grid_improvement':records[-1]['density_l1']/records[-2]['density_l1']<t['last_error_ratio'],'positive_states':all(r['min_density']>0 and r['min_pressure']>0 for r in records)}
    if case=='brio':checks['magnetic_error']=records[-1]['by_l1']<t['finest_by_l1']
    return {'id':'brio-independent' if case=='brio' else 'shu-independent','checks':checks,'passed':all(checks.values()),'metrics':{'reference_last_pair_l1':refdiff,'reference_finest_n':grids[-1],'finest_density_l1':records[-1]['density_l1']},'records':records,'reference_records':reference_records},finest_solution

def ot_comparison(cfg):
    ref=read_reference('ot',256);previous=read_reference('ot',128)
    refdiff=float(np.mean(abs(block_average(ref,128,[4])-previous[:,4].reshape(128,128).T[...,None])))
    records=[];fields={};t=cfg['acceptance'];checks={'independent_reference_refined':refdiff<t['independent_reference_l1']}
    for method in ['ct','glm']:
        errors=[]
        for n in cfg['grids']:
            result=solve_orszag_tang(n=n,final_time=cfg['time'],method=method,cfl=cfg['cfl'])
            state=result.q;rho,_,_,p,bx,by=planar_primitive(state)
            exact=block_average(ref,n,[4,10])
            er=float(np.mean(abs(rho-exact[...,0]))/np.mean(abs(exact[...,0])))
            eb=float(np.mean(abs(by-exact[...,1]))/np.mean(abs(exact[...,1])))
            history=result.history
            mass=float(np.max(abs(history[:,2]-history[0,2]))/abs(history[0,2]))
            energy=float(np.max(abs(history[:,3]-history[0,3]))/abs(history[0,3]))
            common=.5*n*(np.roll(bx,-1,axis=0)-np.roll(bx,1,axis=0)+np.roll(by,-1,axis=1)-np.roll(by,1,axis=1))
            records.append({'method':method,'n':n,'density_relative_l1':er,'by_relative_l1':eb,'native_divergence_linf':float(abs(result.divergence).max()),'common_cell_divergence_linf':float(abs(common).max()),'mass_relative_drift':mass,'energy_relative_drift':energy,'min_density':float(rho.min()),'min_pressure':float(p.min()),'steps':result.steps})
            errors.append(er);fields[method]=rho
            if method=='ct':checks['ct_native_constraint_'+str(n)]=float(abs(result.divergence).max())<t['ct_native_divergence']
        checks[method+'_density_error']=errors[-1]<t['finest_density_relative_l1']
        checks[method+'_magnetic_error']=records[-1]['by_relative_l1']<t['finest_by_relative_l1']
        checks[method+'_refinement']=errors[-1]/errors[-2]<t['last_error_ratio']
    checks['conservation']=all(max(r['mass_relative_drift'],r['energy_relative_drift'])<t['conserved_relative_drift'] for r in records)
    checks['positive_states']=all(r['min_density']>0 and r['min_pressure']>0 for r in records)
    fields['reference']=block_average(ref,cfg['grids'][-1],[4])[...,0]
    return {'id':'ct-glm-independent','checks':checks,'passed':all(checks.values()),'metrics':{'reference_density_128_256_l1':refdiff,'ct_glm_finest_density_l1':float(np.mean(abs(fields['ct']-fields['glm'])))},'records':records},fields

def glm_mode(cfg):
    k=2*np.pi;ch=cfg['speed'];damping=cfg['damping'];end=cfg['time'];records=[]
    matrix=np.array([[0.,-1j*k],[-1j*ch**2*k,-damping]])
    exact=expm(end*matrix)@np.array([1.,0.]);decay=abs(exact[0]);t=cfg['acceptance']
    for n in cfg['grids']:
        x=(np.arange(n)+.5)/n;q=np.stack((np.cos(k*x),np.zeros(n)),axis=-1)
        dt=cfg['cfl']/n/ch;steps=int(np.ceil(end/dt));dt=end/steps
        def rhs(a):
            grad=(np.roll(a,-1,axis=0)-np.roll(a,1,axis=0))*n/2
            return np.stack((-grad[:,1],-ch*ch*grad[:,0]-damping*a[:,1]),axis=-1)
        for _ in range(steps):
            a=rhs(q);b=rhs(q+.5*dt*a);c=rhs(q+.5*dt*b);d=rhs(q+dt*c);q+=dt*(a+2*b+2*c+d)/6
        target=np.real(np.exp(1j*k*x)[:,None]*exact)
        records.append({'n':n,'l2_error':float(np.sqrt(np.mean((q-target)**2))),'divergence_norm_ratio':float(np.linalg.norm(q[:,0])/np.linalg.norm(np.cos(k*x))),'steps':steps})
    order=float(np.log2(records[-2]['l2_error']/records[-1]['l2_error']))
    checks={'analytic_expm_comparison':records[-1]['l2_error']<t['finest_l2'],'spatial_order':order>t['min_order'],'divergence_damping':records[-1]['divergence_norm_ratio']<t['divergence_ratio']}
    return {'id':'glm-fourier-mode','passed':all(checks.values()),'checks':checks,'metrics':{'observed_order':order,'continuum_amplitude_ratio':float(decay)},'records':records}

def validate_config(config):
    for key,end in [('ot',.05),('brio',.1),('shu',1.8)]:
        c=config[key]
        if c['time']!=end:raise ValueError('Stored Athena reference fixes the physical comparison time')
        if not 0<c['cfl']<=.35:raise ValueError('Require 0<CFL<=.35')
        if any(not isinstance(n,int) or n<8 for n in c['grids']) or sorted(set(c['grids']))!=c['grids']:raise ValueError('Increasing integer grids required')
    if any(256%n for n in config['ot']['grids']):raise ValueError('OT grids must divide the stored 256² reference')
    c=config['glm_mode']
    if c['time']<=0 or c['speed']<=0 or c['damping']<0 or not 0<c['cfl']<=.5:raise ValueError('Invalid linear GLM controls')
    for c in config.values():
        if isinstance(c,dict) and 'acceptance' in c and any(not np.isfinite(v) or v<=0 for v in c['acceptance'].values()):raise ValueError('Finite positive acceptance values required')

def run(input_path,output):
    start=time.monotonic();config=json.loads(Path(input_path).read_text());validate_config(config);output=Path(output);output.mkdir(parents=True,exist_ok=True)
    if sorted(config['ot']['grids'])!=config['ot']['grids'] or min(config['ot']['grids'])<8:raise ValueError('Increasing grids >=8 required')
    cases=[]
    a,fields=ot_comparison(config['ot']);cases.append(a);np.savez_compressed(output/'ot-fields.npz',**fields)
    for name in ['brio','shu']:
        a,solution=independent_1d(name,config[name]);cases.append(a);np.savetxt(output/(name+'-solution.csv'),solution,delimiter=',',header='x,'+('rho,By,reference_rho,reference_By' if name=='brio' else 'rho,reference_rho'),comments='')
    cases.append(glm_mode(config['glm_mode']));checks={c['id']:c['passed'] for c in cases}
    result={'schema_version':1,'input_sha256':hashlib.sha256(Path(input_path).read_bytes()).hexdigest(),'passed':all(checks.values()),'checks':checks,'cases':cases,'duration_seconds':time.monotonic()-start,'termination':'fixed_inputs_completed','scope':'Existing atlas finite-volume solvers vs independently compiled Athena++ references; a separate linear GLM diagnostic has a matrix-exponential analytic reference.'}
    (output/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');return result
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--input',default='inputs.json');parser.add_argument('--output',required=True);a=parser.parse_args();r=run(a.input,a.output);print(json.dumps({'passed':r['passed'],'duration_seconds':r['duration_seconds'],'cases':[{k:c[k] for k in ['id','passed','checks']} for c in r['cases']]}));raise SystemExit(0 if r['passed'] else 1)
