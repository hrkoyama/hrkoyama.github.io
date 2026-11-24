"""Fixed educational matrices; fresh output and public result envelope."""
from pathlib import Path
import argparse,datetime,hashlib,json,traceback,time
import numpy as np
from scipy.sparse.linalg import LinearOperator,lobpcg
import fixtures as F
import solvers as S
from references import oracles as R
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()


def write(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n')


def fresh_case(ident):return dict(id=ident,passed=False,checks={},check_details=[],records=[],metrics={})


def gate(c,name,value,bound,passed):
    assert name not in c['checks'];c['checks'][name]=bool(passed);c['check_details'].append(dict(name=name,value=value,bound=bound,passed=bool(passed)))


def measured_case_metrics(case):
    """Serialize summaries of already measured records; evaluate no new norms."""
    rows=case['records']
    if not rows:raise ValueError('Measured records are required for case metrics')
    fields={
        'pivoted-direct-refinement':{
            'max_condition_infinity':'condition_infinity',
            'max_relative_forward_error':'relative_forward_error',
            'max_normwise_backward_error':'final_backward',
            'max_componentwise_backward_error':'component_backward',
            'max_relative_LAPACK_difference':'relative_LAPACK_difference',
            'max_binary64_pivot_growth':'binary64_pivot_growth'},
        'symmetric-saddle-minres':{
            'max_original_relative_residual':'true_relative_residual',
            'max_relative_reference_error':'reference_error',
            'max_iterations':'iterations',
            'max_condition_infinity_estimate':'condition_infinity_estimate'},
        'restarted-shift-invert':{
            'max_original_eigenpair_residual':'true_normalized_residual',
            'max_operator_calls':'operator_calls',
            'max_restart_cycles':'cycles',
            'max_shift_solve_count':'shift_solve_count'},
        'fem-mass-eigen':{
            'max_generalized_residual':'true_relative_residual',
            'max_M_orthogonality_defect':'M_orthogonality',
            'max_relative_reference_error':'relative_reference_error',
            'max_operator_vector_actions':'operator_vector_actions',
            'max_preconditioner_vector_actions':'preconditioner_K_inverse_vector_actions'}}
    return {metric:max(row[field] for row in rows)
            for metric,field in fields[case['id']].items()}


def checkpoint(out,cases):write(out/'completed-cases.json',cases)


def progress(out,name):
    return lambda **arrays:np.savez(out/(name+'-candidate.npz'),**arrays)


def save(out,name,data):
    arrays={k:v for k,v in data.items() if isinstance(v,(np.ndarray,float,int,bool,np.generic))};np.savez_compressed(out/(name+'.npz'),**arrays)


def backward(a,b,x):
    residual=abs(b-S.mv(a,x));den=S.mv(abs(a),abs(x))+abs(b)
    component=np.divide(residual,den,out=np.zeros_like(residual),where=den>0)
    if np.any((den==0)&(residual!=0)):raise ArithmeticError('nonzero residual at zero scale')
    scale=float(np.max(np.sum(abs(a),axis=1))*np.max(abs(x))+np.max(abs(b)))
    if scale==0:
        if np.any(residual):raise ArithmeticError('nonzero residual at zero normwise scale')
        normwise=0.
    else:normwise=float(np.max(residual)/scale)
    return normwise,float(np.max(component))


def qualification(cfg,out):
    checks={};details=[]
    def test(name,error,bound):checks[name]=bool(error<=bound);details.append(dict(name=name,error=float(error),bound=bound));write(out/'reference-qualification.json',dict(passed=all(checks.values()),checks=checks,details=details))
    for name in cfg['direct']['fixtures']:
        a,b=F.direct_fixture(name);exact=R.rational_solution(a,b);lapack=R.lapack_solution(a,b);condition=R.condition_infinity(a);save(out,'reference-'+name,dict(a=a,b=b,exact=exact,lapack=lapack,condition=condition))
        test(name+'/exact-binary-rational-vs-LAPACK',S.norm(exact-lapack)/S.norm(exact),max(5e-12,condition*2e-14))
        test(name+'/reference-backward',backward(a,b,exact)[0],5e-14)
    a=F.laplacian(cfg['restarted']['size']);values,vectors=R.dense_spectrum(a);closed=R.laplacian_spectrum(len(a));save(out,'reference-laplacian',dict(a=a,values=values,vectors=vectors,closed=closed))
    test('laplacian/exact-spectrum',float(np.max(abs(values-closed)/closed)),5e-13)
    test('laplacian/LAPACK-vectors',float(np.max(abs(S.mm(a,vectors)-vectors*values[None,:])))/float(np.max(abs(a))),5e-13)
    for n in cfg['mass']['interior_nodes']:
        k,m,x=F.string_fem(n);values,vectors=R.dense_spectrum(k,m);closed=R.fem_spectrum(n,3);save(out,'reference-fem-'+str(n),dict(k=k,m=m,x=x,values=values,vectors=vectors,closed=closed))
        test(f'fem{n}/exact-discrete-spectrum',float(np.max(abs(values[:3]-closed)/closed)),2e-11)
        test(f'fem{n}/reference-M-orthogonality',float(np.max(abs(S.mm(vectors.T,S.mm(m,vectors))-np.eye(n)))),2e-12)
    assert len(checks)==16
    if not all(checks.values()):raise ArithmeticError('Frozen independent reference qualification failed')
    return dict(passed=True,checks=checks,check_count=16,scope='Main fixed matrix reference preflight only; small pytest operator/solver fixtures may precede it.')


def direct_case(cfg,lim,out,c):
    csv=[]
    for name in cfg['fixtures']:
        a,b=F.direct_fixture(name);exact=R.rational_solution(a,b);condition=R.condition_infinity(a)
        for method in (['lu'] if name=='wilkinson12' else ['lu','cholesky']):
            label=name+'-'+method;data=S.refine(a,b,method,cfg['corrections'],progress(out,label));data.update(a=a,b=b,exact=exact);save(out,label,data)
            eta,component=backward(a,b,data['x']);initial=backward(a,b,data['history'][0])[0];forward=S.norm(data['x']-exact)/S.norm(exact);lapack=R.lapack_solution(a,b,method=='cholesky');difference=S.norm(data['x']-lapack)/S.norm(exact);bound=max(lim['direct_forward_floor'],condition*lim['direct_condition_scale'])
            row=dict(id=label,fields=label+'.npz',matrix=name,factorization=method,condition_infinity=condition,initial_backward=initial,final_backward=eta,component_backward=component,relative_forward_error=forward,relative_LAPACK_difference=difference,binary64_pivot_growth=data['growth'],corrections=cfg['corrections']);c['records'].append(row)
            gate(c,label+'/finite',0.,0.,all(np.isfinite(data[k]).all() for k in ['x','history']))
            gate(c,label+'/binary32-factor',data['factor_residual32'],lim['factor32'],data['factor_residual32']<=lim['factor32'])
            gate(c,label+'/binary64-factor',data['factor_residual64'],lim['factor64'],data['factor_residual64']<=lim['factor64'])
            gate(c,label+'/normwise-backward',eta,lim['direct_backward'],eta<=lim['direct_backward'])
            gate(c,label+'/componentwise-backward',component,lim['direct_component'],component<=lim['direct_component'])
            gate(c,label+'/condition-aware-forward',forward,bound,forward<=bound)
            gate(c,label+'/LAPACK-comparison',difference,bound,difference<=bound)
            improved=eta<=lim['direct_gain']*initial if initial>1e-12 else eta<=1e-12
            gate(c,label+'/refinement-gain-or-roundoff',eta,max(1e-12,lim['direct_gain']*initial),improved)
            csv.append([len(a),condition,initial,eta,component,forward,difference,data['growth']])
    w=next(x for x in c['records'] if x['matrix']=='wilkinson12');h=next(x for x in c['records'] if x['matrix']=='hilbert5')
    gate(c,'Wilkinson/exact-growth',w['binary64_pivot_growth'],2.**11,w['binary64_pivot_growth']==2.**11)
    gate(c,'Hilbert/ill-conditioning-not-residual',h['condition_infinity'],1e5,h['condition_infinity']>=1e5)
    np.savetxt(out/(c['id']+'.csv'),csv,delimiter=',',header='size,condition_inf,initial_backward,final_backward,component_backward,forward_error,lapack_difference,binary64_pivot_growth',comments='')


def symmetric_schur(raw,velocity_size):
    if not np.isfinite(raw).all():raise ArithmeticError('Nonfinite raw Schur block')
    antisymmetry=float(np.max(abs(raw-raw.T)))/max(1.,float(np.max(abs(raw))))
    bound=64*np.finfo(float).eps*velocity_size
    if antisymmetry>bound:raise ArithmeticError('Raw Schur antisymmetry exceeds declared roundoff guard')
    return .5*(raw+raw.T),antisymmetry,bound


def conditioned_saddle_target(a,configured,forward_limit):
    # For symmetric A, kappa_2 <= kappa_infinity in exact arithmetic.
    # This matrix-only estimate never uses a reference solution or measured error.
    if not np.array_equal(a,a.T) or configured<=0 or forward_limit<=0:raise ValueError('symmetric A and positive stopping controls required')
    kappa=R.condition_infinity(a)
    if not np.isfinite(kappa) or kappa<1:raise ArithmeticError('invalid matrix condition estimate')
    target=min(float(configured),float(forward_limit)/kappa)
    if not np.isfinite(target) or target<=0:raise ArithmeticError('invalid conditioned stopping target')
    return target,kappa


def saddle_case(cfg,lim,out,c):
    csv=[]
    for n in cfg['velocity_sizes']:
        a,b,h,B=F.saddle(n);hf=S.lu_factor(h);inverse_bt=np.column_stack([S.lu_solve(hf,row) for row in B]);raw_schur=S.mm(B,inverse_bt)
        save(out,f'saddle-{n}-raw-Schur',dict(h=h,B=B,raw_schur=raw_schur,raw_antisymmetry=np.array(float(np.max(abs(raw_schur-raw_schur.T))))))
        schur,antisymmetry,antisymmetry_bound=symmetric_schur(raw_schur,n);p=np.zeros_like(a);p[:n,:n]=h;p[n:,n:]=schur
        ref=R.lapack_solution(a,b);spectrum=R.dense_spectrum(a,p)[0];expected=np.sort(np.r_[np.full(len(B),(1-np.sqrt(5))/2),np.ones(n-len(B)),np.full(len(B),(1+np.sqrt(5))/2)])
        save(out,f'saddle-{n}-inputs',dict(a=a,b=b,raw_schur=raw_schur,symmetric_schur=schur,relative_raw_antisymmetry=antisymmetry,antisymmetry_guard=antisymmetry_bound,preconditioner=p,reference=ref,spectrum=spectrum,expected=expected))
        internal_target,condition=conditioned_saddle_target(a,cfg['true_residual_tolerance'],lim['saddle_forward'])
        save(out,f'saddle-{n}-stopping',dict(condition_infinity_estimate=np.array(condition),configured_tolerance=np.array(cfg['true_residual_tolerance']),fixed_forward_acceptance=np.array(lim['saddle_forward']),internal_target=np.array(internal_target)))
        gate(c,f'n{n}/ideal-Schur-three-point-spectrum',float(np.max(abs(spectrum-expected))),lim['schur_spectrum'],np.max(abs(spectrum-expected))<=lim['schur_spectrum'])
        for pre,pc in [('none',None),('exact-Schur',p)]:
            for method in ['minres','gmres']:
                label=f'saddle-{n}-{pre}-{method}';data=S.krylov_linear(a,b,method,internal_target,len(a),pc,progress(out,label));save(out,label,data)
                residual=S.norm(b-S.mv(a,data['x']))/S.norm(b);err=S.norm(data['x']-ref)/S.norm(ref);orth=float(data['orthogonality'].max());sym=data['transform_symmetry']/max(1.,float(np.max(abs(a))))
                c['records'].append(dict(id=label,fields=label+'.npz',method=method,preconditioner=pre,size=len(a),iterations=data['iterations'],projected_operator_actions=data['iterations'],solver_original_residual_actions=data['iterations'],posthoc_original_residual_actions=1,true_relative_residual=residual,reference_error=err,converged=data['converged'],condition_infinity_estimate=condition,internal_true_residual_target=internal_target,configured_true_residual_tolerance=cfg['true_residual_tolerance']))
                gate(c,label+'/finite',0.,0.,np.isfinite(data['x']).all() and np.isfinite(data['history']).all())
                gate(c,label+'/same-true-residual',residual,cfg['true_residual_tolerance'],data['converged'] and residual<=cfg['true_residual_tolerance'])
                gate(c,label+'/independent-reference',err,lim['saddle_forward'],err<=lim['saddle_forward'])
                gate(c,label+'/basis-orthogonality',orth,lim['orthogonality'],orth<=lim['orthogonality'])
                gate(c,label+'/symmetric-congruence',sym,lim['transform_symmetry'],sym<=lim['transform_symmetry'])
                gate(c,label+'/fixed-dimension-budget',data['iterations'],len(a),data['iterations']<=len(a))
                if pre=='exact-Schur':gate(c,label+'/ideal-three-step-control',data['iterations'],4,data['iterations']<=4)
                csv.append([len(a),int(pre!='none'),int(method=='minres'),data['iterations'],residual,err,orth])
    rejected=False
    try:S.curvature_guard(np.diag([2.,-1.]),np.array([0.,1.]))
    except ArithmeticError:rejected=True
    gate(c,'CG/explicit-negative-curvature-control',int(rejected),1,rejected)
    np.savetxt(out/(c['id']+'.csv'),csv,delimiter=',',header='size,exact_schur,minres,iterations,true_residual,reference_error,orthogonality',comments='')


def restarted_case(cfg,lim,out,c):
    n=cfg['size'];a=F.laplacian(n);exact=R.laplacian_spectrum(n);start=1+np.arange(1,n+1)/(n+1);csv=[]
    for shift in cfg['shifts']:
        target=float(exact[-1] if shift is None else exact[np.argmin(abs(exact-shift))])
        for length in cfg['restart_lengths']:
            label='restart-'+str(length)+'-shift-'+str(shift);data=S.restarted_eigen(a,start,length,cfg['max_cycles'],cfg['true_residual_tolerance'],shift,progress(out,label));save(out,label,data)
            hist=data['history'];res=float(hist[-1,3]);err=abs(data['value']-target)/target;linear=float(np.max(data['shift_solve_residuals'])) if len(data['shift_solve_residuals']) else 0.;orth=float(np.max(hist[:,6]));recovered=abs(hist[-1,2]-data['value'])/target
            c['records'].append(dict(id=label,fields=label+'.npz',shift=shift,restart_length=length,cycles=len(hist),operator_calls=data['operator_calls'],original_residual_actions=data['residual_matrix_actions'],shift_residual_matrix_actions=len(data['shift_solve_residuals']),shift_solve_count=len(data['shift_solve_residuals']),value=data['value'],exact_target=target,true_normalized_residual=res))
            gate(c,label+'/finite',0.,0.,np.isfinite(hist).all() and np.isfinite(data['vector']).all())
            gate(c,label+'/original-problem-residual',res,cfg['true_residual_tolerance'],data['converged'] and res<=cfg['true_residual_tolerance'])
            gate(c,label+'/known-spectrum',err,lim['eigenvalue_relative'],err<=lim['eigenvalue_relative'])
            gate(c,label+'/shift-linear-residual',linear,2e-12,linear<=2e-12)
            gate(c,label+'/action-budget',data['operator_calls'],length*cfg['max_cycles'],data['operator_calls']<=length*cfg['max_cycles'])
            gate(c,label+'/basis-orthogonality',orth,lim['orthogonality'],orth<=lim['orthogonality'])
            gate(c,label+'/inverse-spectral-map',recovered,lim['eigenvalue_relative'],recovered<=lim['eigenvalue_relative'])
            csv.append([-1 if shift is None else shift,length,len(hist),data['operator_calls'],data['residual_matrix_actions'],res,err,linear])
    rejected=False
    try:S.restarted_eigen(np.diag([1.,2.,3.]),np.ones(3),2,2,1e-9,shift=2.)
    except ArithmeticError:rejected=True
    gate(c,'shift/exact-singularity-failure-retained-as-control',int(rejected),1,rejected)
    np.savetxt(out/(c['id']+'.csv'),csv,delimiter=',',header='shift_minus1meansnone,restart,cycles,operator_calls,residual_actions,true_residual,eigenvalue_error,shift_solve_residual',comments='')


def eigen_metrics(k,m,values,vectors):
    residual=S.mm(k,vectors)-S.mm(m,vectors)*values[None,:]
    denominator=np.sqrt(np.sum(S.mm(k,vectors)**2,axis=0))+abs(values)*np.sqrt(np.sum(S.mm(m,vectors)**2,axis=0))
    return float(np.max(np.sqrt(np.sum(residual**2,axis=0))/denominator)),float(np.max(abs(S.mm(vectors.T,S.mm(m,vectors))-np.eye(len(values)))))


def fem_initial_block(x):
    # Degree+2 images {2,5,8} avoid the old span {0,1,2} rank defect.
    return np.column_stack([np.ones_like(x),x**3,x**6])


def mass_action_operator(m,out=None,label='mass-action'):
    """Same saved M; avoid dense-B adapter and retain any action exception."""
    def action(y):
        try:
            return S.mv(m,y)
        except Exception as exc:
            if out is not None:
                np.savez(out/(label+'-failed-action.npz'),m=m,argument=np.array(y,copy=True))
                write(out/(label+'-failed-action.json'),dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
            raise
    return LinearOperator(m.shape,matvec=action,matmat=action,dtype=m.dtype)


def mass_case(cfg,lim,out,c):
    csv=[];continuum=[]
    for n in cfg['interior_nodes']:
        k,m,x=F.string_fem(n);closed=R.fem_spectrum(n,cfg['eigenpairs']);reference=R.dense_spectrum(k,m)[0][:cfg['eigenpairs']]
        count=[0];preconditioner_count=[0];lf=S.cholesky(k)
        def counted(y):count[0]+=1 if y.ndim==1 else y.shape[1];return S.mv(k,y)
        op=LinearOperator(k.shape,matvec=counted,matmat=counted,dtype=float)
        def inverse(y):preconditioner_count[0]+=1 if y.ndim==1 else y.shape[1];return S.chol_solve(lf,y)
        pc=LinearOperator(k.shape,matvec=inverse,matmat=inverse,dtype=float)
        for method in ['mass-Krylov','SciPy-LOBPCG']:
            label=f'fem-{n}-{method}'
            if method=='mass-Krylov':data=S.mass_krylov(k,m,1+x,cfg['krylov_dimension'],cfg['eigenpairs'],progress(out,label))
            else:
                initial=fem_initial_block(x);np.savez(out/(label+'-candidate.npz'),k=k,m=m,initial=initial,stage=np.array('before-library-LOBPCG'))
                mass=mass_action_operator(m,out,label)
                values,vectors,history,residuals=lobpcg(op,initial,B=mass,M=pc,largest=False,tol=cfg['lobpcg_absolute_tolerance'],maxiter=cfg['lobpcg_max_iterations'],retLambdaHistory=True,retResidualNormsHistory=True)
                data=dict(values=values,vectors=vectors,lambda_history=np.asarray(history),residual_history=np.asarray(residuals),operator_calls=count[0])
            data.update(k=k,m=m,x=x,closed=closed,reference=reference);save(out,label,data)
            res,orth=eigen_metrics(k,m,data['values'],data['vectors']);err=float(np.max(abs(data['values']-reference)/reference));ce=float(np.max(abs(data['values']-closed)/closed));calls=data['operator_calls']
            c['records'].append(dict(id=label,fields=label+'.npz',method=method,interior_nodes=n,operator_vector_actions=calls,operator_kind='K^-1 M' if method=='mass-Krylov' else 'K',preconditioner_K_inverse_vector_actions=calls if method=='mass-Krylov' else preconditioner_count[0],true_relative_residual=res,M_orthogonality=orth,relative_reference_error=err,values=data['values'].tolist()))
            gate(c,label+'/finite',0.,0.,np.isfinite(data['values']).all() and np.isfinite(data['vectors']).all())
            gate(c,label+'/original-generalized-residual',res,lim['mass_residual'],res<=lim['mass_residual'])
            gate(c,label+'/M-orthogonality',orth,lim['mass_orthogonality'],orth<=lim['mass_orthogonality'])
            gate(c,label+'/independent-dense-reference',err,lim['mass_eigenvalue'],err<=lim['mass_eigenvalue'])
            gate(c,label+'/exact-discrete-spectrum',ce,lim['mass_eigenvalue'],ce<=lim['mass_eigenvalue'])
            gate(c,label+'/fixed-action-budget',calls,cfg['vector_action_cap'],calls<=cfg['vector_action_cap'])
            csv.append([n,int(method=='SciPy-LOBPCG'),calls,res,orth,err,*data['values']])
            if method=='mass-Krylov':continuum.append(float(np.max(abs(data['values']-(np.pi*np.arange(1,4))**2)/(np.pi*np.arange(1,4))**2)))
    for i in [1,2]:
        ratio=continuum[i]/continuum[i-1];gate(c,'continuum/second-order-ratio-'+str(i),ratio,[.2,.3],.2<=ratio<=.3)
    gate(c,'continuum/finest-three-eigenvalues',continuum[-1],lim['continuum_finest'],continuum[-1]<=lim['continuum_finest'])
    np.savetxt(out/(c['id']+'.csv'),csv,delimiter=',',header='interior_nodes,scipy_lobpcg,operator_vector_actions,generalized_residual,M_orthogonality,dense_error,lambda1,lambda2,lambda3',comments='')


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--input',type=Path,default=ROOT/'inputs.json');parser.add_argument('--output',type=Path,required=True);a=parser.parse_args()
    if a.output.exists() and (not a.output.is_dir() or any(a.output.iterdir())):parser.error('fresh empty output required')
    a.output.mkdir(parents=True,exist_ok=True);cases=[];failure=None;ref=None;contract=None;started=time.monotonic()
    try:
        contract=json.loads((ROOT/'pre-run-contract.json').read_text());assert sha(a.input)==contract['files_sha256']['inputs.json']
        for n,h in contract['files_sha256'].items():assert sha(ROOT/n)==h,n
        cfg=json.loads(a.input.read_text());limits=json.loads((ROOT/'acceptance.json').read_text())['limits'];ref=qualification(cfg,a.output)
        for ident,key,func in [('pivoted-direct-refinement','direct',direct_case),('symmetric-saddle-minres','saddle',saddle_case),('restarted-shift-invert','restarted',restarted_case),('fem-mass-eigen','mass',mass_case)]:
            c=fresh_case(ident);cases.append(c);checkpoint(a.output,cases);func(cfg[key],limits,a.output,c);c['metrics']=measured_case_metrics(c);c['passed']=bool(c['checks']) and all(c['checks'].values());checkpoint(a.output,cases)
        assert [len(c['records']) for c in cases]==[7,8,6,6]
        assert [len(c['checks']) for c in cases]==[58,55,43,39]
        passed=all(c['passed'] for c in cases)
    except Exception as error:passed=False;failure=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
    result=dict(schema_version=1,passed=bool(passed),checks={c['id']:c['passed'] for c in cases} or {'completed':False},cases=cases,termination='fixed_budget_completed' if failure is None else 'calculation_failed',failure=failure,reference_qualification=ref,input_sha256=sha(a.input),duration_seconds=time.monotonic()-started,finished_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    if contract is not None:result['source_sha256']={**contract['files_sha256'],'pre-run-contract.json':sha(ROOT/'pre-run-contract.json')}
    write(a.output/'result.json',result);print(json.dumps({'passed':passed,'cases':len(cases),'gates':sum(len(c['checks']) for c in cases),'failure':failure}))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
