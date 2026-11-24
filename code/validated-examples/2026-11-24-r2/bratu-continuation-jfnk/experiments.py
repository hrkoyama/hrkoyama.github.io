"""Two fixed Bratu cases: continuum-reference checks are separate from discrete solver residuals."""
import numpy as np
from scipy.linalg import eigh_tridiagonal
from problem import residual,analytic_jv,jacobian_diagonals,l2,norm,dot,weighted_arc_dot
from continuation import follow,solve_fold,fixed_lambda,fold_equations
from matrix_free import inexact_newton,Evaluator
from references.analytic_family import reference
from io_contract import Case,dump,numeric_csv,array_progress,save_arc_raw,save_root_raw,save_jfnk_raw

ARC_GRID_GATES=['finite complete branch','discrete residual','unit tangent','tangent equation','tangent orientation',
 'turning tangent','lower and upper lambda2 neighborhoods','fold discrete equation','fold null equation','fold null normalization',
 'fold sigma_min','simple fold parameter transversality','simple fold quadratic transversality',
 'lower discrete root','upper discrete root','ordered distinct branches','nonzero reference fields']
ARC_GLOBAL_GATES=['Decimal80 continuum ODE','Decimal80 zero endpoints','reference fixed lambda','reference fold printed anchor',
 'no-solution lambda4 proof bound','lambda4 Newton reports failure','lambda4 finite retained states','lambda4 remains above tolerance',
 'finest full path shape','finest family curve lambda','finest continuous fold error','fold first refinement order',
 'fold second refinement order','finest lower exact solution','finest upper exact solution','both branch errors refine']
JFNK_RUN_GATES=['nonlinear converged','finite states','discrete residual','continuous branch error','analytic verified forcing',
 'declared eta','evaluation count ledger','bounded Krylov storage','accepted Armijo steps']
JFNK_GLOBAL_GATES=['nonzero Jv reference','AD Jv exact','AD primal exact','central FD Jv','zero Jv branch',
 'mode agreement N63 lower','mode agreement N63 upper','mode agreement N127 lower','mode agreement N127 upper',
 'finest exact branches','all mode errors refine','constant forcing companion matches']


def run_continuation(out,inputs,limits,cases):
    case=Case('bratu-fold-continuation',out,cases);records=[];references=[]
    for n in inputs['N']:
        label='bratu-fold-continuation-N'+str(n)
        def checkpoint(states,tangents,rows,correctors):
            arrays=dict(states=states,tangents=tangents)
            for k,row in enumerate(correctors):arrays['corrector_states_'+str(k)]=row['states'];arrays['corrector_residuals_'+str(k)]=row['residuals']
            np.savez_compressed(out/(label+'-active.npz'),**arrays)
            dump(out/'active-stage.json',dict(case=case.data['id'],n=n,arc_completed=rows[-1]['step']))
        arc=follow(n,inputs['ds'],inputs['arc_steps'],inputs['tolerance'],inputs['max_corrector'],checkpoint,array_progress(out,label+'-corrector'))
        save_arc_raw(out,label,arc)
        folded=solve_fold(arc,inputs['tolerance'],inputs['max_fold'],array_progress(out,label+'-fold'))
        np.savez_compressed(out/(label+'-completed-fold.npz'),**folded)
        w=folded['w'];u,lam,v=w[:n],float(w[n]),w[n+1:]
        rr=reference(n,lam=inputs['branch_lambda'],branch='lower');ru=reference(n,lam=inputs['branch_lambda'],branch='upper');rf=reference(n,theta=rr['fold_theta']);references.extend([rr,ru,rf])
        tl=arc['tangents'][:,-1];ll=arc['states'][:,-1];mid=arc['states'][:,n//2]
        lower_candidates=np.flatnonzero(tl>0);upper_candidates=np.flatnonzero(tl<0)
        roots=[]
        for candidates in [lower_candidates,upper_candidates]:
            if not len(candidates):raise ArithmeticError('Fixed arc failed to reach both branches')
            index=int(candidates[np.argmin(abs(ll[candidates]-inputs['branch_lambda']))])
            root_label=label+'-fixed-'+str(len(roots))
            ans=fixed_lambda(arc['states'][index,:-1],inputs['branch_lambda'],inputs['tolerance'],inputs['max_fixed'],array_progress(out,root_label))
            save_root_raw(out,root_label,ans);roots.append(ans)
        low,up=roots;errors=[float(np.max(abs(sol['u']-ref['u'][1:-1]))) for sol,ref in zip(roots,[rr,ru])]
        path_shape=[];path_lambda=[];path_exact_lambda=[];path_exact_profiles=[]
        for state in arc['states']:
            theta=2*np.arccosh(np.exp(state[n//2]/2));ref=reference(n,theta=float(theta))
            path_shape.append(float(np.max(abs(state[:-1]-ref['u'][1:-1]))));path_lambda.append(abs(float(state[-1])-ref['lam']))
            path_exact_lambda.append(ref['lam']);path_exact_profiles.append(ref['u'])
        lo,di,upper=jacobian_diagonals(u,lam);ev=eigh_tridiagonal(di,lo,eigvals_only=True);sigma=float(np.min(abs(ev)))
        vals=[np.all(np.isfinite(arc['states'])) and len(arc['rows'])==inputs['arc_steps']+1,
              max(r['residual'] for r in arc['rows'])<=limits['discrete_residual'],
              max(abs(r['tangent_norm']-1) for r in arc['rows'])<=limits['tangent_norm'],
              max(r['tangent_equation'] for r in arc['rows'])<=limits['tangent_equation'],
              all(weighted_arc_dot(a,b)>0 for a,b in zip(arc['tangents'][:-1],arc['tangents'][1:])),
              tl[0]>0 and tl[-1]<0,
              np.any((ll<inputs['branch_lambda'])&(tl>0)) and np.any((ll<inputs['branch_lambda'])&(tl<0)),
              l2(residual(u,lam))<=limits['discrete_residual'],l2(analytic_jv(u,lam,v))<=limits['fold_null'],
              abs(dot(v,v)/(n+1)-1)<=limits['fold_normalization'],sigma/max(abs(di))<=limits['fold_sigma_ratio'],
              abs(dot(v,-np.exp(u))/(n+1))>=limits['transversality_min'],
              abs(dot(v,-lam*np.exp(u)*v*v)/(n+1))>=limits['transversality_min'],
              low['passed'] and l2(residual(low['u'],inputs['branch_lambda']))<=limits['discrete_residual'],
              up['passed'] and l2(residual(up['u'],inputs['branch_lambda']))<=limits['discrete_residual'],
              up['u'][n//2]>low['u'][n//2]+1.,norm(rr['u'])>1e-3 and norm(ru['u'])>1e-3]
        for name,value in zip(ARC_GRID_GATES,vals):case.gate('N'+str(n)+'/'+name,value)
        arrays=dict(states=arc['states'],tangents=arc['tangents'],fold=w,fold_states=folded['states'],fold_residuals=folded['residuals'],
                    lower=low['u'],upper=up['u'],lower_states=low['states'],upper_states=up['states'],lower_residuals=low['residuals'],upper_residuals=up['residuals'],
                    exact_lower=rr['u'],exact_upper=ru['u'],reference_x=rr['x'],sigma_path=np.array([r['sigma_min'] for r in arc['rows']]),path_shape=np.array(path_shape),path_lambda=np.array(path_lambda),
                    path_exact_lambda=np.array(path_exact_lambda),path_exact_profiles=np.array(path_exact_profiles))
        for k,item in enumerate(arc['correctors']):arrays['corrector_states_'+str(k)]=item['states'];arrays['corrector_residuals_'+str(k)]=item['residuals']
        np.savez_compressed(out/(label+'.npz'),**arrays);numeric_csv(out/(label+'-path.csv'),arc['rows']);case.data['data_files'].append(label+'.npz')
        row=dict(n=n,arc_steps=inputs['arc_steps'],fold_lambda=lam,continuous_fold_lambda=rr['fold_lambda'],fold_error=abs(lam-rr['fold_lambda']),
                 sigma_min=sigma,lower_error=errors[0],upper_error=errors[1],path_shape_error=max(path_shape),path_lambda_error=max(path_lambda))
        records.append(row);case.row(row)
    impossible=fixed_lambda(np.zeros(inputs['failure_N']),inputs['failure_lambda'],inputs['tolerance'],inputs['max_fixed'],array_progress(out,'bratu-intended-lambda4'))
    np.savez_compressed(out/'bratu-fold-continuation-intended-lambda4-failure.npz',**{k:impossible[k] for k in ['u','states','residuals']})
    n=inputs['failure_N'];mu1=4*(n+1)**2*np.sin(np.pi/(2*(n+1)))**2
    orders=[float(np.log(records[k]['fold_error']/records[k+1]['fold_error'])/np.log(2)) for k in [0,1]]
    ref_errors=[float(np.max(abs(r['ode_residual']))) for r in references];fine=records[-1]
    vals=[max(ref_errors)<=limits['reference_ode'],max(abs(r['u'][0])+abs(r['u'][-1]) for r in references)<=limits['reference_endpoint'],
          max(abs(references[i]['lam']-inputs['branch_lambda']) for i in range(len(references)) if i%3!=2)<=limits['reference_lambda'],
          abs(references[0]['fold_lambda']-3.513830719)<=1e-8,
          inputs['failure_lambda']>mu1/np.e,not impossible['passed'],np.all(np.isfinite(impossible['states'])),impossible['residuals'][-1]>inputs['tolerance'],
          fine['path_shape_error']<=limits['path_shape'],fine['path_lambda_error']<=limits['path_lambda'],fine['fold_error']<=limits['fold_lambda'],
          orders[0]>=limits['fold_order'],orders[1]>=limits['fold_order'],fine['lower_error']<=limits['solution_error'],fine['upper_error']<=limits['solution_error'],
          all(records[-1][key]<records[0][key] for key in ['lower_error','upper_error'])]
    for name,value in zip(ARC_GLOBAL_GATES,vals):case.gate(name,value)
    numeric_csv(out/'bratu-fold-continuation-summary.csv',records)
    case.finish(dict(fold_orders=orders,intended_failure_reason=impossible['reason'],discrete_nonexistence_bound=float(mu1/np.e),
                     matching='Fullpathfamilycoordinatefrommidpointisexplicit;separatefixedlambda2rootsvalidatebothbrancheswithoutparameterfitting.',reference_qualification_max_ODE=max(ref_errors)))


def run_jfnk(out,inputs,limits,cases):
    case=Case('bratu-matrix-free-jfnk',out,cases);n=31;x=np.arange(1,n+1)/(n+1);u=.4*np.sin(np.pi*x)+.1*np.sin(2*np.pi*x);v=np.sin(3*np.pi*x)+.3*np.cos(2*np.pi*x)
    exact=analytic_jv(u,3.,v);ad=Evaluator(3.,'forward-ad');fd=Evaluator(3.,'central-fd');from dual import Dual
    dual=residual(Dual(u,v),3.);finite=fd.operator(u,v);zero=ad.operator(u,np.zeros(n))
    qvals=[norm(exact)>1e-3,norm(dual.tangent-exact)/norm(exact)<=limits['ad_jv'],norm(dual.value-residual(u,3.))<=limits['ad_primal'],norm(finite-exact)/norm(exact)<=limits['fd_jv'],np.array_equal(zero,np.zeros(n))]
    for name,value in zip(JFNK_GLOBAL_GATES[:5],qvals):case.gate(name,value)
    np.savez_compressed(out/'bratu-matrix-free-jfnk-Jv-qualification.npz',u=u,v=v,analytic=exact,ad=dual.tangent,central_fd=finite,ad_primal=dual.value)
    specs=[dict(n=n,branch=b,mode=m,constant=False) for n in inputs['N'] for b in inputs['branches'] for m in inputs['modes']]
    specs.append(dict(n=inputs['N'][0],branch='lower',mode='analytic',constant=True));saved={};records=[]
    for index,spec in enumerate(specs):
        settings=dict(inputs['settings'])
        if spec['constant']:settings['constant_eta']=inputs['constant_eta']
        label='bratu-matrix-free-jfnk-run'+str(index)
        def checkpoint(states,rows,counts):
            np.savez_compressed(out/(label+'-active.npz'),states=np.array(states));dump(out/'active-stage.json',dict(case=case.data['id'],run=index,outer_completed=len(rows),counts=counts))
        ans=inexact_newton(spec['n'],inputs['lambda'],spec['branch'],spec['mode'],settings,checkpoint)
        save_jfnk_raw(out,label,ans)
        ref=reference(spec['n'],lam=inputs['lambda'],branch=spec['branch']);error=float(np.max(abs(ans['u']-ref['u'][1:-1])))
        count=ans['counts'];nonzero=count['jv']-count['zero_jv'];mode=spec['mode'];eta_min=inputs['constant_eta'] if spec['constant'] else settings['eta_min'];eta_max=inputs['constant_eta'] if spec['constant'] else settings['eta_max']
        ledger=(count['primal_residual']>=2*nonzero if mode=='central-fd' else count['dual_residual']==nonzero if mode=='forward-ad' else count['dual_residual']==0)
        vals=[ans['passed'],np.all(np.isfinite(ans['states'])),ans['final_residual']<=settings['nonlinear_tolerance'],error<=limits['all_solution_error'],
              all(r['analytic_linear_ratio']<=limits['forcing_factor']*r['eta']+limits['forcing_absolute'] for r in ans['rows']),
              all(eta_min<=r['eta']<=eta_max for r in ans['rows']),ledger,
              all(r['basis_columns']<=settings['restart']+1 for r in ans['rows']),
              all('accepted_residual' in r and r['accepted_residual']<=(1-settings['armijo']*r['alpha'])*r['residual'] for r in ans['rows'])]
        for name,value in zip(JFNK_RUN_GATES,vals):case.gate(str(index)+'/'+name,value)
        arrays=dict(states=ans['states'],u=ans['u'],exact=ref['u'],reference_x=ref['x'])
        for k,h in enumerate(ans['linear_histories']):arrays['inner_'+str(k)]=h
        for k,trial in enumerate(ans['line_trials']):arrays['line_trial_'+str(k)]=trial['state']
        np.savez_compressed(out/(label+'.npz'),**arrays)
        if ans['rows']:numeric_csv(out/(label+'-newton.csv'),ans['rows'])
        row=dict(run=index,n=spec['n'],mode_code=inputs['modes'].index(mode),branch_code=inputs['branches'].index(spec['branch']),constant_eta_code=int(spec['constant']),
                 error=error,residual=ans['final_residual'],newton_steps=len(ans['rows']),**count)
        records.append(row);case.row(row);case.data['data_files'].append(label+'.npz')
        saved[(spec['n'],spec['branch'],mode,spec['constant'])]=dict(u=ans['u'],error=error,reason=ans['reason'])
    comparisons=[]
    for n in inputs['N']:
        for branch in inputs['branches']:
            base=saved[(n,branch,'analytic',False)]['u'];gap=max(float(np.max(abs(saved[(n,branch,m,False)]['u']-base))) for m in inputs['modes']);comparisons.append(gap)
    vals=[gap<=limits['mode_agreement'] for gap in comparisons]
    vals.extend([max(saved[(inputs['N'][-1],b,m,False)]['error'] for b in inputs['branches'] for m in inputs['modes'])<=limits['finest_solution_error'],
                 all(saved[(inputs['N'][-1],b,m,False)]['error']<saved[(inputs['N'][0],b,m,False)]['error'] for b in inputs['branches'] for m in inputs['modes']),
                 float(np.max(abs(saved[(inputs['N'][0],'lower','analytic',True)]['u']-saved[(inputs['N'][0],'lower','analytic',False)]['u'])))<=limits['mode_agreement']])
    for name,value in zip(JFNK_GLOBAL_GATES[5:],vals):case.gate(name,value)
    numeric_csv(out/'bratu-matrix-free-jfnk-summary.csv',records)
    case.finish(dict(mode_gap_max=max(comparisons),qualification_AD_relative=norm(dual.tangent-exact)/norm(exact),qualification_FD_relative=norm(finite-exact)/norm(exact),
                     reasons=[saved[(s['n'],s['branch'],s['mode'],s['constant'])]['reason'] for s in specs],
                     evaluation_scope='Actualsolverevaluations;analyticlinear-forcingvalidationcountedseparately.NoPETScorassemblednonlinearJacobianusedbyJFNK.'))
