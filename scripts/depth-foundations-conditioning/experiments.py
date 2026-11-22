"""Fixed conditioning experiments; references and expected failures stay distinct."""
from pathlib import Path
import hashlib
import json
import math
import numpy as np
from scipy import integrate, linalg, sparse, special
from scipy.sparse.linalg import spsolve
from scipy.fft import dstn, idstn
from fixtures import array_sha256, decomposition_fixture, symmetric_fixture
from solvers import (adaptive_simpson, arnoldi, back_substitute, gauss_legendre,
                     householder_qr, jacobi_svd, lanczos, matrix_product,
                     matrix_vector, smoothed_aggregation, solve_amg)

HERE=Path(__file__).resolve().parent
EPS=np.finfo(float).eps
REFERENCE_SHA256='b8d4776330ee86843de225f6800a9dba180083e5af728a178f9f9670135d83e8'


def record(identifier,checks,metrics,rows,**extras):
    return {'id':identifier,'passed':bool(all(checks.values())),
            'checks':{k:bool(v) for k,v in checks.items()},'metrics':metrics,
            'records':rows,**extras}


def relative(actual,reference):
    return float(np.linalg.norm(actual-reference)/max(np.linalg.norm(reference),1e-300))


def amg_case(c,budget):
    rows=[];histories=[];checks={};t=c['acceptance']
    for n in c['grid_sizes']:
        budget.check(); h=1/(n+1)
        tri=sparse.diags([-np.ones(n-1),2*np.ones(n),-np.ones(n-1)],[-1,0,1]).tocsr()/h**2
        lam=linalg.eigh_tridiagonal(2*np.ones(n)/h**2,-np.ones(n-1)/h**2,eigvals_only=True)
        analytic=4*np.sin(np.pi*np.arange(1,n+1)/(2*(n+1)))**2/h**2
        kappa=float(analytic[-1]/analytic[0])
        grid=np.arange(1,n+1)/(n+1); x,y=np.meshgrid(grid,grid,indexing='ij')
        known=(np.sin(np.pi*x)*np.sin(np.pi*y)+.2*np.sin(3*np.pi*x)*np.sin(2*np.pi*y)).ravel()
        vmin=(np.sin(np.pi*x)*np.sin(np.pi*y)).ravel();vmin/=np.linalg.norm(vmin)
        vmax=(np.sin(n*np.pi*x)*np.sin(n*np.pi*y)).ravel();vmax/=np.linalg.norm(vmax)
        for epsilon in c['anisotropies']:
            budget.check()
            a=(sparse.kron(tri,sparse.eye(n))+epsilon*sparse.kron(sparse.eye(n),tri)).tocsr()
            rhs=a@known; direct=spsolve(a,rhs)
            # Separate spectral inversion, not the AMG hierarchy or sparse LU.
            eigenvalues=analytic[:,None]+epsilon*analytic[None,:]
            spectral=idstn(dstn(rhs.reshape(n,n),type=1,norm='ortho')/eigenvalues,type=1,norm='ortho').ravel()
            level=smoothed_aggregation(a,c['strength'],c['coarse_size'])
            solution,info=solve_amg(level,rhs,c['relative_tolerance'],c['max_cycles'])
            residual=float(np.linalg.norm(rhs-a@solution)/np.linalg.norm(rhs))
            forward=relative(solution,direct)
            complexity=0.;sizes=[];current=level
            while current is not None:
                complexity+=current.matrix.nnz/a.nnz;sizes.append(current.matrix.shape[0]);current=current.coarse
            # Same square-grid kappa for every epsilon; anisotropy is a separate variable.
            lmin=(1+epsilon)*analytic[0];lmax=(1+epsilon)*analytic[-1]
            base=lmax*vmax; perturbed=base+c['perturbation']*lmax*vmin
            base_ref=spsolve(a,base); pert_ref=spsolve(a,perturbed)
            gain=relative(pert_ref,base_ref)/c['perturbation']
            key=f'n{n}-eps{epsilon:g}'
            checks[key+'-true-residual']=abs(residual-info['relative_residual'])<=t['true_residual_agreement']
            checks[key+'-forward-bound']=forward<=2*kappa*residual+t['forward_bound_roundoff_factor']*EPS*kappa
            checks[key+'-condition-gain']=abs(gain/kappa-1)<=t['condition_gain_relative_error']
            checks[key+'-complexity']=complexity<=t['operator_complexity'] and len(sizes)>1
            checks[key+'-independent-dst']=relative(direct,spectral)<=t['direct_solution_error'] and relative(spectral,known)<=t['direct_solution_error']
            if epsilon==1:
                checks[key+'-resolved']=info['converged'] and residual<=t['relative_residual'] and forward<=t['direct_solution_error']
            else:
                checks[key+'-stress-honest']=residual<=t['stress_residual_ratio'] and (
                    (info['converged'] and info['termination']=='residual_tolerance') or
                    (not info['converged'] and info['termination']=='cycle_budget' and info['cycles']==c['max_cycles']))
            rows.append({'n':n,'unknowns':n*n,'epsilon':epsilon,'condition_2_analytic':kappa,
                         'lambda_min':float(lmin),'lambda_max':float(lmax),'cycles':info['cycles'],
                         'relative_residual':residual,'relative_forward_error':forward,
                         'sparse_direct_vs_dst':relative(direct,spectral),'dst_vs_known_solution':relative(spectral,known),
                         'condition_times_residual':kappa*residual,'condition_gain_direct':gain,
                         'operator_complexity':float(complexity),'levels':len(sizes),
                         'solver_converged':info['converged'],'termination':info['termination'],
                         'scope':'algebraic known-solution system; no continuum PDE order'})
            histories.extend({'n':n,'epsilon':epsilon,'cycle':i,'relative_residual':v} for i,v in enumerate(info['history']))
        checks[f'n{n}-independent-spectrum']=relative(lam,analytic)<=t['spectrum_relative_error']
    short,short_info=solve_amg(level,rhs,c['relative_tolerance'],1)
    checks['short-budget-failure-explicit']=not short_info['converged'] and short_info['termination']=='cycle_budget'
    return record(c['case_id'],checks,{
        'maximum_condition_2':max(r['condition_2_analytic'] for r in rows),
        'maximum_actual_relative_residual':max(r['relative_residual'] for r in rows),
        'maximum_actual_forward_error':max(r['relative_forward_error'] for r in rows),
        'stress_budget_exhaustions':sum(not r['solver_converged'] for r in rows),
        'maximum_condition_gain_relative_error':max(abs(r['condition_gain_direct']/r['condition_2_analytic']-1) for r in rows)},rows,
        residual_histories=histories,short_budget={'converged':short_info['converged'],'relative_residual':short_info['relative_residual'],'termination':short_info['termination']})


def load_reference():
    path=HERE/'reference.json';data=json.loads(path.read_text())
    if hashlib.sha256(path.read_bytes()).hexdigest()!=REFERENCE_SHA256:raise ValueError('High-precision reference SHA mismatch')
    # Additional semantics are checked independently of the file digest.
    if data.get('all_reference_checks_passed') is not True or data.get('environment',{}).get('mpmath')!='1.3.0' or data.get('environment',{}).get('precision_dps')!=[80,120]:
        raise ValueError('Independent high-precision execution provenance required')
    for key,name in [('protocol_sha256','inputs.json'),('fixture_recipe_sha256','fixtures.py'),('reference_input_sha256','reference-input.json'),('generator_sha256','mpmath_reference.py')]:
        if data.get(key)!=hashlib.sha256((HERE/name).read_bytes()).hexdigest():raise ValueError('Reference input/source binding mismatch')
    datasets=data.get('results',[])
    if len(datasets)!=4 or {row.get('id') for row in datasets}!={'q0','q4','q8','q12'}:raise ValueError('Reference dataset completeness mismatch')
    normalized={}
    for row in datasets:
        exponent=int(row['id'][1:])
        if row.get('exponent')!=exponent:raise ValueError('Reference exponent mismatch')
        if set(row.get('array_sha256',{}))!={'matrix','rhs','perturbed_rhs'}:raise ValueError('Reference array binding incomplete')
        if [v.get('dps') for v in row.get('runs',[])]!=[80,120]:raise ValueError('Reference precision pair missing')
        arrays=decomposition_fixture(exponent)[:3]
        for key,array in zip(['matrix','rhs','perturbed_rhs'],arrays):
            if row['array_sha256'][key]!=array_sha256(array):raise ValueError('Actual fixture reference mismatch')
        fine=row['runs'][-1]
        for run in row['runs']:
            for key in ['singular_values','solution','perturbed_solution']:
                values=np.asarray(run.get(key,[]),dtype=float)
                if values.shape!=(4,) or not np.all(np.isfinite(values)) or (key=='singular_values' and np.any(values<=0)):
                    raise ValueError('Invalid independent reference metric')
            for key in ['condition_2','residual_norm','perturbed_residual_norm']:
                value=float(run.get(key,'nan'))
                if not math.isfinite(value) or value<0 or (key=='condition_2' and value<1):raise ValueError('Invalid independent reference scalar')
        normalized[row['id']]={**fine,'arrays':{k:{'sha256':v} for k,v in row['array_sha256'].items()}}
    return {'datasets':normalized}


def decomposition_case(c,budget):
    reference=load_reference();rows=[];checks={};t=c['acceptance']
    for exponent in c['spectrum_exponents']:
        budget.check();a,b,bp,s,u0,v0=decomposition_fixture(exponent,c['perturbation'])
        independent=reference['datasets']['q'+str(exponent)]
        for name,array in [('matrix',a),('rhs',b),('perturbed_rhs',bp)]:
            if independent['arrays'][name]['sha256']!=array_sha256(array):raise ValueError('Actual binary matrix/reference mismatch')
        high_s=np.array([float(v) for v in independent['singular_values']]);high_x=np.array([float(v) for v in independent['solution']]);high_xp=np.array([float(v) for v in independent['perturbed_solution']])
        q,r=householder_qr(a);u,sv,vt,info=jacobi_svd(a,c['jacobi_tolerance'],c['max_sweeps'],c['rank_rtol'])
        xqr=back_substitute(r,matrix_vector(q.T,b));xpqr=back_substitute(r,matrix_vector(q.T,bp))
        xsv=matrix_vector(vt.T,matrix_vector(u.T,b)/sv);xpsv=matrix_vector(vt.T,matrix_vector(u.T,bp)/sv)
        _,ref_s,_=linalg.svd(a,full_matrices=False,lapack_driver='gesdd')
        xr,_,rank,_=linalg.lstsq(a,b,cond=c['rank_rtol'],lapack_driver='gelsd')
        xpr,_,_,_=linalg.lstsq(a,bp,cond=c['rank_rtol'],lapack_driver='gelsy')
        kappa=float(s[0]/s[-1]);budget_x=max(t['minimum_forward_budget'],t['forward_roundoff_factor']*EPS*kappa)
        qr_recon=relative(matrix_product(q,r),a);sv_recon=relative(matrix_product(u*sv,vt),a)
        orth=max(float(np.linalg.norm(matrix_product(q.T,q)-np.eye(4),2)),float(np.linalg.norm(matrix_product(u.T,u)-np.eye(4),2)),float(np.linalg.norm(matrix_product(vt,vt.T)-np.eye(4),2)))
        singular_error=float(np.max(abs(sv-high_s))/high_s[0]);forward=max(relative(xqr,high_x),relative(xsv,high_x),relative(xpqr,high_xp),relative(xpsv,high_xp))
        # Project perturbation onto its known direction rather than infer relative accuracy from a tiny subtraction.
        predicted=c['perturbation']*kappa
        gain_error=max(abs(float(v0[:,-1]@(xpqr-xqr))-predicted),abs(float(v0[:,-1]@(xpsv-xsv))-predicted))
        checks[f'q{exponent}-factorization']=qr_recon<=t['reconstruction'] and sv_recon<=t['reconstruction'] and orth<=t['orthogonality'] and info['converged'] and info['rank']==4
        checks[f'q{exponent}-high-precision-spectrum']=singular_error<=t['scaled_singular_error'] and relative(ref_s,high_s)<=t['reference_relative_error']
        checks[f'q{exponent}-condition-aware-forward']=forward<=budget_x
        checks[f'q{exponent}-lapack-reference']=relative(xr,high_x)<=budget_x and relative(xpr,high_xp)<=budget_x and rank==4
        checks[f'q{exponent}-perturbation-gain']=gain_error<=t['condition_gain_absolute_error']*max(predicted,1e-12)+2*budget_x
        rows.append({'kind':'prescribed-spectrum','exponent':exponent,'condition_2':kappa,'rank':info['rank'],
                     'qr_reconstruction':qr_recon,'svd_reconstruction':sv_recon,'orthogonality':orth,
                     'scaled_singular_error':singular_error,'smallest_singular_relative_error':float(abs(sv[-1]-high_s[-1])/high_s[-1]),
                     'maximum_relative_forward_error':forward,'forward_acceptance_budget':budget_x,
                     'qr_relative_residual':relative(matrix_vector(a,xqr),b),'svd_relative_residual':relative(matrix_vector(a,xsv),b),
                     'predicted_perturbation_solution_norm':predicted,'perturbation_projection_absolute_error':gain_error,'jacobi_sweeps':info['sweeps']})
    # Truncation is compared with the same declared numerical-rank convention.
    for cutoff in c['rank_cutoffs']:
        u,sv,vt,info=jacobi_svd(a,c['jacobi_tolerance'],c['max_sweeps'],cutoff)
        actual=matrix_vector(vt.T,matrix_vector(u.T,bp)/sv)
        target,_,rank,_=linalg.lstsq(a,bp,cond=cutoff,lapack_driver='gelsd')
        normal=float(np.linalg.norm(matrix_vector(a.T,matrix_vector(a,actual)-bp))/np.linalg.norm(a))
        checks[f'cutoff{cutoff:g}-rank-aware']=info['rank']==rank and relative(actual,target)<=max(1e-8,100*EPS*float(sv[0]/sv[-1])) and normal<=t['normal_residual']
        rows.append({'kind':'rank-cutoff','rank_rtol':cutoff,'rank':info['rank'],'reference_rank':int(rank),'effective_condition_2':float(sv[0]/sv[-1]),'least_squares_stationarity':normal,'relative_truncated_reference_error':relative(actual,target),'bias_to_untruncated_solution':relative(actual,high_xp)})
    a0,b0,_,_,u0,v0=decomposition_fixture(4,c['perturbation']);deficient=np.einsum('ik,k,jk->ij',u0,np.array([1.,.5,0.,0.]),v0,optimize=False)
    u,sv,vt,info=jacobi_svd(deficient,rank_rtol=c['rank_rtol']);_,_,rank,_=linalg.lstsq(deficient,b0,cond=c['rank_rtol'],lapack_driver='gelsd')
    checks['exact-rank-deficiency']=info['rank']==rank==2 and relative(matrix_product(u*sv,vt),deficient)<=t['reconstruction']
    _,_,_,exhausted=jacobi_svd(a0,max_sweeps=0);checks['sweep-budget-failure-explicit']=not exhausted['converged'] and exhausted['termination']=='sweep_budget'
    return record(c['case_id'],checks,{'largest_condition_2':float(2.**36),'maximum_backward_reconstruction':max(max(r.get('qr_reconstruction',0),r.get('svd_reconstruction',0)) for r in rows),'maximum_forward_error':max(r.get('maximum_relative_forward_error',0) for r in rows),'minimum_numerical_rank':min([2]+[r['rank'] for r in rows]),'reference_precision_digits':120},rows,
                  rank_deficient_control={'rank':info['rank'],'reference_rank':int(rank),'jacobi_converged':info['converged']},sweep_budget_control=exhausted)


def ritz_measure(a,start,dimension,method,reference_values,reference_vectors):
    q,h,info=(lanczos if method=='lanczos' else arnoldi)(a,start,dimension)
    values,vectors=np.linalg.eigh(h) if method=='lanczos' else np.linalg.eig(h)
    indices=np.argsort(values.real)[-2:]
    value=values[indices[-1]];vector=matrix_vector(q,vectors[:,indices[-1]]);vector/=np.linalg.norm(vector)
    norm_a=float(linalg.norm(a,2));residual=float(np.linalg.norm(matrix_vector(a,vector)-value*vector))
    pair=matrix_product(q,vectors[:,indices]);pair,_=linalg.qr(pair,mode='economic')
    refpair=reference_vectors[:,-2:];refpair,_=linalg.qr(refpair,mode='economic')
    projector_error=float(linalg.norm(matrix_product(pair,pair.conj().T)-matrix_product(refpair,refpair.conj().T),2))
    return {'dimension':info['dimensions'],'eigenvalue_real':float(value.real),'eigenvalue_imag':float(value.imag),
            'eigenvalue_error':float(abs(value-reference_values[-1])),
            'absolute_residual':residual,'relative_backward_residual':residual/(norm_a+abs(value)),
            'orthogonality':float(linalg.norm(matrix_product(q.T,q)-np.eye(q.shape[1]),2)),
            'top_two_projector_error':projector_error,'happy_breakdown':info['happy_breakdown']}


def krylov_case(c,budget):
    rows=[];checks={};t=c['acceptance'];rng=np.random.default_rng(c['seed']);start=rng.normal(size=c['n'])
    for gap in c['cluster_gaps']:
        budget.check();a,spectrum,_=symmetric_fixture(c['n'],gap);ref,vec=linalg.eigh(a)
        checks[f'gap{gap:g}-analytic-spectrum']=float(np.max(abs(ref-spectrum)))<=t['analytic_eigenvalue_reference']
        family=[]
        for dimension in c['dimensions']:
            r=ritz_measure(a,start,dimension,'lanczos',ref,vec);r.update(kind='symmetric-cluster',gap=gap,eigenvalue_condition=1.);family.append(r);rows.append(r)
        fine=family[-1]
        checks[f'gap{gap:g}-resolved']=fine['relative_backward_residual']<=t['backward_residual'] and fine['eigenvalue_error']<=t['eigenvalue_absolute_floor'] and fine['top_two_projector_error']<=t['final_top_subspace_sine']
        checks[f'gap{gap:g}-basis']=max(r['orthogonality'] for r in family)<=t['orthogonality']
    for strength in c['nonnormal_strengths']:
        budget.check();a=np.diag(np.r_[5.,5.+c['nonnormal_gap'],np.linspace(-1.,1.,c['n']-2)]);a[0,1]=strength
        ref,left,right=linalg.eig(a,left=True,right=True);order=np.argsort(ref.real);ref=ref[order];left=left[:,order];right=right[:,order]
        condition=float(np.linalg.norm(left[:,-1])*np.linalg.norm(right[:,-1])/abs(np.vdot(left[:,-1],right[:,-1])))
        analytic_condition=math.sqrt(1+(strength/c['nonnormal_gap'])**2)
        checks[f'K{strength:g}-condition']=abs(condition/analytic_condition-1)<=t['condition_relative_error']
        checks[f'K{strength:g}-analytic-spectrum']=abs(ref[-1]-(5.+c['nonnormal_gap']))<=t['analytic_eigenvalue_reference']
        family=[]
        for dimension in c['dimensions']:
            r=ritz_measure(a,start,dimension,'arnoldi',ref,right);r.update(kind='nonnormal-arnoldi',coupling=strength,eigenvalue_condition=condition);family.append(r);rows.append(r)
        fine=family[-1];bound=max(t['eigenvalue_absolute_floor'],t['conditioned_error_factor']*condition*(fine['absolute_residual']+EPS*linalg.norm(a,2)))
        checks[f'K{strength:g}-resolved']=fine['relative_backward_residual']<=t['backward_residual'] and fine['eigenvalue_error']<=bound and fine['top_two_projector_error']<=t['final_top_subspace_sine']
        checks[f'K{strength:g}-basis']=max(r['orthogonality'] for r in family)<=t['orthogonality']
        fine['condition_aware_eigenvalue_error_budget']=float(bound)
    # This intentionally constructed pseudoeigenpair is NOT labelled an Arnoldi failure.
    sensitivity=[]
    for strength in c['pseudopair_strengths']:
        gap=c['pseudopair_gap'];a=np.array([[1.,strength],[0.,1.+gap]])
        shift=gap/2;value=1.+shift;v=np.array([1.,shift/strength]);v/=np.linalg.norm(v)
        residual=float(np.linalg.norm(matrix_vector(a,v)-value*v));formula=abs(shift*(gap-shift))/(strength*math.sqrt(1+(shift/strength)**2))
        error=min(abs(value-1.),abs(value-(1.+gap)))
        checks[f'pseudoK{strength:g}-literal-formula']=abs(residual/formula-1)<=t['pseudopair_relative_error']
        sensitivity.append({'kind':'constructed-pseudoeigenpair','coupling':strength,'gap':gap,'absolute_residual':residual,'eigenvalue_error':float(error),'eigenvalue_condition':math.sqrt(1+(strength/gap)**2),'status':'constructed sensitivity control; not a solver-produced pair'})
    checks['small-residual-does-not-certify-forward-error']=sensitivity[-1]['absolute_residual']<t['pseudopair_small_residual'] and sensitivity[-1]['eigenvalue_error']>t['pseudopair_large_error']
    rows+=sensitivity
    # A one-vector Krylov budget cannot be reported as a certified eigenpair.
    q,h,info=arnoldi(a,np.ones(2),1);value=h[0,0];res=float(np.linalg.norm(matrix_vector(a,q[:,0])-value*q[:,0]))
    checks['short-dimension-has-residual']=not info['happy_breakdown'] and res>t['backward_residual']
    return record(c['case_id'],checks,{'maximum_basis_orthogonality':max(r.get('orthogonality',0) for r in rows),'largest_eigenvalue_condition':max(r['eigenvalue_condition'] for r in rows),'constructed_small_residual':sensitivity[-1]['absolute_residual'],'constructed_forward_error':sensitivity[-1]['eigenvalue_error']},rows)


def quad_reference(function,a,b,points=None):
    output=integrate.quad(function,a,b,epsabs=2e-13,epsrel=2e-13,points=points,limit=300,full_output=1)
    value,error,info=output[:3]
    return float(value),{'estimated_error':float(error),'evaluations':int(info['neval']),'status':'completed' if len(output)==3 else 'reported-warning','message':None if len(output)==3 else output[3]}


def quadrature_case(c,budget):
    rows=[];references=[];checks={};t=c['acceptance']
    for width in c['lorentz_widths']:
        budget.check();center=c['lorentz_center'];function=lambda x:1/(1+((x-center)/width)**2)
        exact=width*(math.atan((1-center)/width)+math.atan(center/width));ref,ref_info=quad_reference(function,0.,1.,[center])
        references.append({'kind':'lorentzian','width':width,'value':ref,**ref_info})
        checks[f'width{width:g}-reference']=abs(ref-exact)<=t['independent_reference_absolute_error'] and ref_info['status']=='completed'
        errors=[]
        for order in c['gauss_orders']:
            nodes,weights=gauss_legendre(order);rnodes,rweights=special.roots_legendre(order)
            answer=float(weights@function((nodes+1)/2)/2);error=abs(answer-exact);errors.append(error)
            checks[f'n{order}-independent-rule']=max(float(np.max(abs(nodes-rnodes))),float(np.max(abs(weights-rweights))))<=t['gauss_reference_scaled_error']
            rows.append({'kind':'narrow-gauss','width':width,'order':order,'value':answer,'absolute_error':error,'integral_condition_1':1.,'status':'fixed-order measurement; not a tolerance certificate'})
        checks[f'width{width:g}-gauss-refinement']=errors[-1]<errors[0] and errors[-1]<=t['gauss_narrow_finest_error']
        for tol in c['adaptive_tolerances']:
            answer=adaptive_simpson(function,0.,1.,tol,c['max_evaluations'],c['max_depth']);error=abs(answer['value']-exact)
            checks[f'width{width:g}-tol{tol:g}']=answer['converged'] and error<=t['adaptive_tolerance_factor']*tol
            rows.append({'kind':'narrow-adaptive','width':width,'tolerance':tol,'value':answer['value'],'absolute_error':error,'estimated_error':answer['estimated_error'],'evaluations':answer['evaluations'],'solver_converged':answer['converged'],'status':answer['termination'],'reference_status':ref_info['status']})
    # Endpoint singular derivative: a known change of variables is a companion, not a universal cure.
    for tol in c['adaptive_tolerances']:
        direct=adaptive_simpson(math.sqrt,0.,1.,tol,c['max_evaluations'],c['max_depth'])
        transformed=adaptive_simpson(lambda z:2*z*z,0.,1.,tol,c['max_evaluations'],c['max_depth'])
        direct_error=abs(direct['value']-2/3);transformed_error=abs(transformed['value']-2/3)
        checks[f'endpoint-tol{tol:g}']=transformed['converged'] and transformed_error<=t['transformed_endpoint_absolute_error'] and ((direct['converged'] and direct_error<=t['adaptive_tolerance_factor']*tol) or (not direct['converged'] and direct['termination'] in ('depth_budget','evaluation_budget')))
        rows.extend([{'kind':'endpoint-'+name,'tolerance':tol,'value':ans['value'],'absolute_error':err,'evaluations':ans['evaluations'],'solver_converged':ans['converged'],'status':ans['termination']} for name,ans,err in [('direct',direct,direct_error),('transformed',transformed,transformed_error)]])
    for scale in c['cancellation_scales']:
        budget.check();shift=c['perturbation']*(1+scale)
        function=lambda x:1+scale*(2*x-1)
        perturbed=lambda x:1+shift+scale*(2*x-1)
        original=adaptive_simpson(function,0.,1.,1e-9,c['max_evaluations'],c['max_depth'])
        changed=adaptive_simpson(perturbed,0.,1.,1e-9,c['max_evaluations'],c['max_depth'])
        kappa_l1=1. if scale<=1 else (scale*scale+1)/(2*scale)
        error=abs(original['value']-1.);gain=changed['value']-original['value'];roundoff=t['roundoff_factor']*EPS*max(1.,scale)
        checks[f'C{scale:g}-absolute-error']=error<=roundoff and abs(changed['value']-(1+shift))<=roundoff
        if scale==c['cancellation_scales'][-1]:checks['conditioned-input-perturbation-gain']=abs(gain/shift-1)<=t['cancellation_gain_relative_error']
        rows.append({'kind':'cancellation','scale':scale,'value':original['value'],'absolute_error':error,'condition_infinity':1+scale,'cancellation_condition_1':kappa_l1,'input_relative_infinity_perturbation':c['perturbation'],'predicted_integral_change':shift,'observed_integral_change':gain,'roundoff_acceptance_budget':roundoff,'solver_converged':original['converged'],'status':original['termination']})
    zero=adaptive_simpson(lambda x:2*x-1,0.,1.,1e-9,c['max_evaluations'],c['max_depth'])
    checks['zero-integral-relative-condition-undefined']=abs(zero['value'])<2e-14
    rows.append({'kind':'zero-integral','value':zero['value'],'absolute_error':abs(zero['value']),'relative_condition':None,'status':'undefined relative condition because the exact integral is zero'})
    center,width,power=c['bump_center'],c['bump_width'],c['bump_power']
    def bump(x):
        z=(x-center)/width
        return (1-z*z)**power if abs(z)<1 else 0.
    exact=width*256/315
    blind=adaptive_simpson(bump,0.,1.,1e-9,c['max_evaluations'],c['max_depth'])
    split=adaptive_simpson(bump,center-width,center+width,1e-9,c['max_evaluations'],c['max_depth'])
    ref,ref_info=quad_reference(bump,0.,1.,[center-width,center,center+width])
    references.append({'kind':'compact-bump-known-breakpoints','value':ref,**ref_info})
    checks['heuristic-blind-spot-explicit']=blind['converged'] and blind['value']==0. and blind['estimated_error']==0. and abs(blind['value']-exact)>t['missed_bump_minimum_error']
    checks['known-support-companion-resolves']=split['converged'] and abs(split['value']-exact)<=t['resolved_bump_absolute_error'] and abs(ref-exact)<=t['independent_reference_absolute_error'] and ref_info['status']=='completed'
    rows.extend([{'kind':'compact-bump-'+name,'value':ans['value'],'absolute_error':abs(ans['value']-exact),'estimated_error':ans['estimated_error'],'evaluations':ans['evaluations'],'solver_converged':ans['converged'],'status':('expected false reassurance, not an accurate integral' if name=='blind' else ans['termination'])} for name,ans in [('blind',blind),('split',split)]])
    return record(c['case_id'],checks,{'maximum_cancellation_condition':max(1+v for v in c['cancellation_scales']),'blind_bump_actual_error':abs(blind['value']-exact),'blind_bump_reported_error':blind['estimated_error'],'resolved_bump_actual_error':abs(split['value']-exact),'zero_integral_relative_condition':None},rows,independent_quadpack=references)
