"""Independent reference-only qualification; no primary solver/stencil imports."""
from pathlib import Path
import argparse,json,hashlib,datetime,sys
import numpy as np
from scipy.integrate import solve_ivp
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R))
from references.thick_reference import angular_rule,continuum_matrix,action,moments
from references.analytic import closed_step
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);a=parser.parse_args();assert not a.output.exists();a.output.mkdir(parents=True)
    cfg=json.loads((R/'inputs.json').read_text())['matched_thick_limit_control'];kappas=cfg['kappa'];scaled=cfg['scaled_times'];checks={};details=[];cache={};raw={};completed=[]
    def persist():
        np.savez(a.output/'reference-partial.npz',**cache,**raw)
        (a.output/'completed-checks.json').write_text(json.dumps(dict(check_count=len(checks),passed=bool(checks) and all(checks.values()),checks=checks,details=details,completed=completed),indent=2,allow_nan=False)+'\n')
    def check(name,flag,value=None):
        assert name not in checks;checks[name]=bool(flag);details.append(dict(name=name,passed=bool(flag),value=value));persist()
    try:
        rules={name:angular_rule(n,hemi) for name,n,hemi in [('hemisphere32',32,True),('GL64',64,False),('GL128',128,False)]}
        for name,(mu,w) in rules.items():
            check(name+'/weight-measure',abs(float(w.sum())-2)<=2e-14)
            check(name+'/odd-first-moment',abs(float(np.sum(w*mu)))<=2e-14)
            check(name+'/one-third-second-moment',abs(float(.5*np.sum(w*mu*mu))-1/3)<=2e-14)
            check(name+'/positive-directional-measure',bool(np.all(w>0) and np.all(abs(mu)<1)))
            cache['mu_'+name]=mu;cache['weights_'+name]=w;cache['moments_'+name]=np.zeros((3,4,3),complex)
        full128={}
        for name,(mu,w) in rules.items():
            for j,kappa in enumerate(kappas):
                A=continuum_matrix(mu,w,kappa,cfg['epsilon']);zero=continuum_matrix(mu,w,kappa,cfg['epsilon'],wavenumber=0.)
                label=f'{name}/k{kappa}'
                check(label+'/finite-generator',np.isfinite(A).all())
                left=np.r_[.5*cfg['epsilon']*w,1.];expected=np.r_[-.5j*w*mu,0.]
                check(label+'/weighted-moment-operator-identity',np.max(abs(np.einsum('i,ij->j',left,A,optimize=False)-expected))<=2e-12)
                conjugate=continuum_matrix(mu,w,kappa,cfg['epsilon'],wavenumber=-1.)
                check(label+'/streaming-conjugacy',np.max(abs(A.conj()-conjugate))<=2e-12)
                for i,s in enumerate(scaled):
                    state=action(A,kappa*s,np.ones(len(mu)+1));value=moments(state,mu,w);cache['moments_'+name][j,i]=value;raw['active_amplitude']=state;completed.append(dict(rule=name,kappa=kappa,scaled_time=s))
                    check(label+'/s'+str(s)+'/finite-amplitude-and-positive-field-bound',np.isfinite(state).all() and np.max(abs(state))<=1+2e-11)
                    check(label+'/s'+str(s)+'/even-odd-Fourier-symmetry',max(abs(value[0].imag),abs(value[1].imag),abs(value[2].real))<=2e-12)
                    if name=='GL128':full128[(kappa,s)]=state.copy()
        for j,kappa in enumerate(kappas):
            for i,s in enumerate(scaled):
                error=float(np.max(abs(cache['moments_GL64'][j,i]-cache['moments_GL128'][j,i])*np.array([1.,1.,kappa])))
                check(f'GL64-128/k{kappa}/s{s}',error<=2e-11,error)
        mu,w=rules['GL128']
        for epsilon in [.25,1.,2.]:
            for kappa in [4,16]:
                A=continuum_matrix(mu,w,kappa,epsilon,wavenumber=0.);initial=np.r_[np.full(len(mu),1.2),.3]
                for time in [.0625,.25]:
                    state=action(A,time,initial);u,v=closed_step(1.2,.3,kappa*time,epsilon,0.);error=float(max(np.max(abs(state[:-1]-u)),abs(state[-1]-v)))
                    check(f'closed-k0/eps{epsilon}/k{kappa}/t{time}',error<=2e-12,error)
        for kappa in [4,16]:
            active={};count=[0];final_time=kappa*.25
            def direct(time,y):
                count[0]+=1;active.update(time=np.array(time),state=y.copy(),nfev=np.array(count[0]));raw.update(DOP853_active_state=y.copy(),DOP853_active_time=np.array(time),DOP853_active_nfev=np.array(count[0]))
                if count[0]%256==0:np.savez(a.output/f'DOP853-k{kappa}-partial.npz',**active)
                if count[0]>6000:raise ArithmeticError('Frozen DOP853 function-evaluation cap exceeded')
                I,V=y[:-1],y[-1]
                return np.r_[-1j*mu*I+kappa*(V-I),kappa*(.5*np.sum(w*I)-V)]
            sol=solve_ivp(direct,(0.,final_time),np.ones(len(mu)+1,dtype=complex),method='DOP853',rtol=2e-11,atol=2e-13,max_step=1/(4*kappa),t_eval=[final_time],dense_output=False)
            np.savez(a.output/f'DOP853-k{kappa}.npz',times=sol.t,states=sol.y,nfev=np.array(sol.nfev));raw['DOP853_active_state']=active['state']
            check(f'DOP853/k{kappa}/success-and-fixed-budget',sol.success and len(sol.t)==1 and sol.t[-1]==final_time and sol.nfev<=6000,int(sol.nfev))
            state=sol.y[:,-1];check(f'DOP853/k{kappa}/finite-positive-field-bound',np.isfinite(state).all() and np.max(abs(state))<=1+2e-11)
            difference=float(np.max(abs(state-full128[(kappa,.25)])));check(f'DOP853/k{kappa}/independent-expm-comparison',difference<=2e-10,difference)
        assert len(checks)==141,len(checks)
        if not all(checks.values()):raise ArithmeticError('Frozen continuum reference qualification failed; primary mode remains unexecuted')
        cache.update(kappa=np.array(kappas),scaled_times=np.array(scaled),epsilon=np.array(cfg['epsilon']),unit_initial_amplitude=np.array(1.),wavenumber=np.array(1.),role=np.array('continuum-space-angular-reference;GL64-128-and-DOP853-qualified;expm-shared'))
        np.savez_compressed(a.output/'matched-thick-reference.npz',**cache)
        result=dict(passed=True,check_count=len(checks),checks=checks,details=details,reference_cache_sha256=sha(a.output/'matched-thick-reference.npz'),input_sha256=sha(R/'inputs.json'),acceptance_sha256=sha(R/'acceptance.json'),source_sha256={n:sha(R/n) for n in ['references/thick_reference.py','references/qualify_thick.py','references/analytic.py']},finished_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),primary_rhs_probes=0,primary_mode_evolutions=0,propagator='scipy.sparse.linalg.expm_multiply(csr_matrix(t*A),initial,traceA=t*trace(A))',scope='Independent continuum-space angular reference only. GL64/128 finite sensitivity,exact closed k0capacity/exchange,weightedmoment/conjugacy,and two fixed independentDOP853 final vectors qualify the reference. No primary SSPRK2 or fixedgridAPclaim.')
        (a.output/'qualification-thick.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps({'passed':True,'checks':141,'primary_rhs_probes':0}))
    finally:persist()
if __name__=='__main__':main()
