"""All fixed trajectories, including diagnostic nonconvergence, with145 gates."""
import json
from pathlib import Path
from unittest.mock import patch
import numpy as np
from problems import residual, jacobian, DomainError, dot, norm, mv
from globalization import solve, radius_update
from references import independent_residual, independent_correction
from io_contract import snapshot, save_json, csv_rows

CASE_ID = 'globalization-difficult-starts'
METHODS = ['full-newton','armijo-newton','dogleg-trust-region']
SUFFIXES = ['finite_saved_history','original_residual_recomputed','scaled_merit_recomputed',
            'method_step_ledger','work_caps','termination_category']
STATUSES = {'ROOT','MAXITER','DOMAIN_FAILURE','STATIONARY_NONROOT','NONDESCENT_DIRECTION',
            'MODEL_FAILURE','TRUST_RADIUS_EXHAUSTED','TRIALS_EXHAUSTED'}


def specifications():
    rows = []
    for scale_id, scale in [('unit',[1.,1.]),('left-scaled',[.001,1000.])]:
        for start_id, start in [('minus',[-1.2,1.]),('zero',[0.,0.])]:
            for method in METHODS:
                rows.append(dict(id=f'rosenbrock-{scale_id}-{start_id}-{method}',kind='rosenbrock',
                                 initial=start,scale=scale,method=method,
                                 required=scale_id=='unit' and method!='full-newton'))
    grid = np.arange(1,32)/32
    for amp in [0,4,8]:
        for method in METHODS:
            rows.append(dict(id=f'bratu-amp{amp}-{method}',kind='bratu',initial=amp*np.sin(np.pi*grid),
                             scale=np.ones(31),method=method,required=amp==0 and method!='full-newton'))
    return rows


def expected_gate_keys():
    ids = [s['id'] for s in specifications()]
    required = [s['id'] for s in specifications() if s['required']]
    return ([i+'/'+k for i in ids for k in SUFFIXES]+
            [i+'/'+k for i in required for k in ['original_root_residual','independent_state_or_correction_error']]+
            ['exact24_main_records']+
            ['stationary-'+m+'/'+k for m in METHODS[1:] for k in ['stationary_nonroot_status','not_false_root']]+
            ['domain/rejected_before_exp_evaluation','domain/finite_candidate_retained'])


def finite_tree(value):
    if isinstance(value, dict): return all(finite_tree(v) for v in value.values())
    if isinstance(value, (list,tuple)): return all(finite_tree(v) for v in value)
    return not isinstance(value,(float,np.floating)) or np.isfinite(value)


def ledger(spec, answer):
    residual_ok = True; merit_ok = True; step_ok = True; defect = 0.
    scale = np.asarray(spec['scale']); method = spec['method']; kind = spec['kind']
    for row in answer['history']:
        x = np.array(row['x']); f = independent_residual(kind,x)
        residual_ok &= bool(np.allclose(f,row['f'],rtol=1e-12,atol=1e-12))
        phi = .5*dot(scale*f,scale*f)
        merit_ok &= abs(phi-row['phi']) <= 1e-12*max(1.,phi)
        if row['domain_rejected']:
            step_ok &= not row['accepted']
            if method == 'dogleg-trust-region': step_ok &= row['delta_after']==.25*row['delta']
            continue
        j = jacobian(kind,x); a = scale[:,None]*j; p = np.array(row['step'])
        ff = scale*np.array(row['f']); g = np.einsum('ij,i->j',a,ff); ap=mv(a,p)
        pred = -dot(g,p)-.5*dot(ap,ap)
        dd = abs(pred-row['pred_direct'])
        bound = 64*np.finfo(float).eps*max(1.,phi,norm(g)*norm(p),dot(ap,ap))
        defect = max(defect,dd)
        step_ok &= dd <= bound and abs(pred-row['pred']) <= bound
        if method == 'dogleg-trust-region':
            step_ok &= norm(p) <= row['delta']*(1+1e-12)
            if pred > 0:
                rho = row['actual']/pred
                step_ok &= abs(rho-row['rho']) <= 1e-12*max(1.,abs(rho))
                step_ok &= row['accepted']==bool(row['actual']>0 and rho>=.1)
                step_ok &= row['delta_after']==radius_update(row['delta'],rho,norm(p))
            else: step_ok &= answer['termination']=='MODEL_FAILURE' and not row['accepted']
        elif method == 'armijo-newton':
            step_ok &= row['accepted']==bool(row['trial_phi']<=phi+1e-4*dot(g,p))
        else: step_ok &= row['accepted']
    counts = answer['counts']
    return {'finite_saved_history':bool(finite_tree(answer)),
            'original_residual_recomputed':bool(residual_ok),
            'scaled_merit_recomputed':bool(merit_ok), 'method_step_ledger':bool(step_ok),
            'work_caps':bool(counts['trials']==len(answer['history']) and len(answer['history'])<=80*25 and counts['jacobian']<=80),
            'termination_category':answer['termination'] in STATUSES}, defect


def run_all(output):
    output=Path(output); records=[]; checks={}; required_residuals=[]; required_errors=[]; defects=[]
    save_json(output/'partial-records.json',records)
    for spec in specifications():
        ident=spec['id']; trace=output/(ident+'-stages.jsonl')
        def checkpoint(stage, **values):
            event=values.pop('record',None)
            snapshot(output/'active-candidate.npz',stage,**values)
            with trace.open('a') as handle:
                handle.write(json.dumps({'stage':stage,'record':event},allow_nan=False)+'\n')
        ans=solve(spec['kind'],spec['initial'],spec['scale'],spec['method'],checkpoint)
        # Completed raw answer is retained BEFORE reference/model/error diagnostics.
        save_json(output/(ident+'-raw.json'),ans)
        arrays={'initial':spec['initial'],'final':ans['x'],'final_f':ans['f']}
        for i,row in enumerate(ans['history']):
            for key in ['x','f','candidate','candidate_f','step']:
                if key in row:arrays[f'{key}_{i:04d}']=row[key]
        snapshot(output/(ident+'.npz'),'raw-solver-completed',**arrays)
        row={'id':ident,'kind':spec['kind'],'method':spec['method'],'required_root':spec['required'],**ans}
        records.append(row); save_json(output/'partial-records.json',records)
        gates,defect=ledger(spec,ans); defects.append(defect)
        checks.update({ident+'/'+k:v for k,v in gates.items()})
        f=independent_residual(spec['kind'],np.array(ans['x'])); rms=norm(f)/np.sqrt(len(f))
        row['original_residual_rms']=rms
        if spec['required']:
            err=norm(np.array(ans['x'])-[1.,1.]) if spec['kind']=='rosenbrock' else norm(independent_correction(np.array(ans['x'])))
            row['state_or_correction_error']=err; required_residuals.append(rms);required_errors.append(err)
            checks[ident+'/original_root_residual']=ans['termination']=='ROOT' and rms<=1e-9
            checks[ident+'/independent_state_or_correction_error']=err<=1e-8
        save_json(output/'partial-records.json',records)
    for method in METHODS[1:]:
        ident='stationary-'+method
        ans=solve('stationary',[0.],[1.],method,
                  lambda stage,**values:snapshot(output/'active-candidate.npz',stage,**{k:v for k,v in values.items() if k!='record'}))
        save_json(output/(ident+'-raw.json'),ans);records.append({'id':ident,'kind':'stationary','method':method,**ans})
        checks[ident+'/stationary_nonroot_status']=ans['termination']=='STATIONARY_NONROOT'
        checks[ident+'/not_false_root']=ans['f']==[1.] and ans['x']==[0.]
        save_json(output/'partial-records.json',records)
    candidate=np.r_[800.,np.zeros(30)];calls=[];rejected=False
    snapshot(output/'domain-candidate.npz','before-domain-check',candidate=candidate)
    def forbidden_exp(*args,**kwargs): calls.append(1);raise AssertionError('Unsafe exp evaluated')
    with patch('problems.np.exp',forbidden_exp):
        try:residual('bratu',candidate)
        except DomainError:rejected=True
    records.append({'id':'domain','termination':'DOMAIN_REJECTED' if rejected else 'UNEXPECTED',
                    'candidate':candidate.tolist(),'unsafe_exp_evaluations':len(calls)})
    checks['domain/rejected_before_exp_evaluation']=rejected and not calls
    checks['domain/finite_candidate_retained']=bool(np.all(np.isfinite(candidate)))
    checks['exact24_main_records']=len(records)==24
    assert set(checks)==set(expected_gate_keys()) and len(checks)==145
    save_json(output/'partial-records.json',records)
    csv_rows(output/'trajectories.csv',[{'id':row['id'],'termination':row['termination'],
              'original_residual_rms':row.get('original_residual_rms',''),
              'F_evaluations':row.get('counts',{}).get('residual',0),
              'trials':len(row.get('history',[]))}for row in records])
    csv_rows(output/'trials.csv',[{'id':row['id'],'iteration':t['iteration'],'trial':t['trial'],
              'phi':t['phi'],'alpha':t['alpha'],'Delta':t['delta'],'accepted':int(t['accepted']),
              'domain_rejected':int(t['domain_rejected']),'rho':t.get('rho','') if t.get('rho') is not None else ''}
              for row in records for t in row.get('history',[])])
    metrics={'max_required_unscaled_residual':max(required_residuals),
             'max_required_state_or_correction_error':max(required_errors),
             'max_model_ledger_defect':max(defects),
             'total_residual_evaluations':sum(row.get('counts',{}).get('residual',0)for row in records),
             'rejected_trials':sum(not t['accepted']for row in records for t in row.get('history',[]))}
    return {'id':CASE_ID,'passed':all(checks.values()),'checks':checks,'metrics':metrics,'records':records}
