"""Run every frozen primary DSMC input; use bundled qualified SPARTA fields."""
import argparse,csv,hashlib,json,time,traceback
from pathlib import Path
import numpy as np
from dsmc import simulate,PROFILE_NAMES
from diagnostics import ensemble,rms,scales,stationarity,resolution,profile_comparison,flux,far_states

HERE=Path(__file__).resolve().parent
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def write_json(path,value):path.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')


def verify_contract(input_path):
    contract=json.loads((HERE/'pre-run-contract.json').read_text())
    if sha(input_path)!=contract['files_sha256']['inputs.json']:raise ValueError('Only frozen input table is accepted')
    for relative,expected in contract['files_sha256'].items():
        if sha(HERE/relative)!=expected:raise ValueError('Changed frozen scientific file: '+relative)
    ref=json.loads((HERE/'references/qualification.json').read_text())
    if ref['passed'] is not True or not ref['checks'] or not all(type(v) is bool and v for v in ref['checks'].values()):
        raise ValueError('Independent reference qualification failed')
    return contract


def run_case(ident,case,limits,output,case_record):
    records=case_record['records'];checks=case_record['checks']
    base=[];block_values=[];wall_estimates=[]
    for label,cfg in case['configurations'].items():
        seeds=case['seeds'] if label=='base' else case['seeds'][:1]
        for seed in seeds:
            key=ident+'-'+label+'-'+str(seed)
            saved=simulate(cfg,seed,output/(key+'-failed-state.npz'))
            np.savez(output/(key+'.npz'),**saved)
            p=saved['profile'];diag=resolution(p,cfg['cells'],cfg['length'],cfg['dt'])
            scale=max(1.,float(np.max(np.abs(saved['initial_totals']))))
            checks[key+'/finite']=bool(all(np.all(np.isfinite(v)) for v in saved.values()))
            checks[key+'/boundary budget']=bool(float(saved['max_budget'])<=limits['boundary_budget_scaled']*scale)
            checks[key+'/physical collisions']=bool(int(saved['collisions'])>0 and int(saved['candidates'])>=int(saved['collisions']))
            checks[key+'/collision probability']=bool(float(saved['max_probability'])<=.5*(1+2e-13))
            checks[key+'/maxwell time resolution']=bool(diag['dt_over_maxwell_tau']<=limits['dt_over_maxwell_tau'])
            checks[key+'/mean free path resolution']=bool(diag['dx_over_lambda']<=limits['dx_over_lambda'])
            with (output/(key+'-profile.csv')).open('w',newline='') as f:
                writer=csv.writer(f);writer.writerow(['x',*PROFILE_NAMES])
                for x,row in zip((np.arange(cfg['bins'])+.5)*cfg['length']/cfg['bins'],p):writer.writerow([float(x),*map(float,row)])
            if label=='base':
                base.append(p);block_values.append(saved['profiles'])
                # Opposite wall-normal conventions: lower gas transfer equals
                # +x molecular flux; upper gas transfer has the opposite sign.
                column=2 if ident=='dsmc-couette' else 4
                wall_estimates.append(float(np.sum(saved['wall_blocks'][:,0,column]-saved['wall_blocks'][:,1,column])/(2*cfg['sample_time'])))
            records.append({'configuration':label,'seed':seed,'fields':key+'.npz','profile_csv':key+'-profile.csv',
                            'resolution':diag,'collisions':int(saved['collisions']),'candidates':int(saved['candidates']),
                            'max_subcycles':int(saved['max_subcycles']),'scaled_budget':float(saved['max_budget'])/scale})
            write_json(output/(ident+'-completed-runs.json'),records)
            case_record['completed_primary_runs']=len(records)
            write_json(output/(ident+'-checkpoint.json'),case_record)
    base=np.stack(base);blocks=np.stack(block_values)
    ref=np.load(HERE/'references'/(ident+'.npz'),allow_pickle=False)['profiles_seeds']
    comparisons=profile_comparison(base,ref,ident)
    for field,value in comparisons.items():
        checks['profile error/'+field]=bool(value['error']<=limits['profile_error']+value['combined_3se'])
        checks['primary precision/'+field]=bool(value['primary_3se']<=limits['primary_profile_3se'])
        checks['reference precision/'+field]=bool(value['reference_3se']<=limits['reference_profile_3se'])
    length=case['configurations']['base']['length']
    stat=stationarity(blocks,ident,length)
    for field,value in stat['profile_equivalence'].items():checks['stationarity/'+field]=bool(value<=limits['stationarity_equivalence'])
    extra={}
    if ident=='dsmc-planar-shock':
        checks['centroid stationarity']=bool(stat['centroid_drift_bound']<=limits['centroid_drift'])
        far=far_states(base,length)
        for name,value in far.items():
            checks['RH far or full flux/'+name]=bool(value['relative_error']<=limits['far_state_relative_error']+value['relative_3se'])
            checks['RH precision/'+name]=bool(value['relative_3se']<=limits['far_state_3se'])
        extra['far_states']=far
    else:
        f=flux(base,ident);rf=flux(ref,ident);fm,fs=ensemble(f);rm,rs=ensemble(rf)
        target=abs(float(rm));combined=np.sqrt(fs*fs+rs*rs)
        checks['bulk molecular flux agreement']=bool(abs(fm-rm)<=limits['flux_relative_error']*target+3*combined)
        checks['bulk molecular flux precision']=bool(target>0 and 3*fs<=limits['flux_relative_3se']*target)
        wm,ws=ensemble(np.array(wall_estimates));dm,ds=ensemble(np.array(wall_estimates)-f)
        checks['wall versus bulk molecular flux']=bool(abs(dm)<=limits['flux_relative_error']*target+3*ds)
        checks['wall molecular flux precision']=bool(3*ws<=limits['wall_flux_relative_3se']*target)
        extra['flux']={'bulk_mean':float(fm),'bulk_se':float(fs),'reference_mean':float(rm),'reference_se':float(rs),
                       'wall_mean':float(wm),'wall_se':float(ws),'wall_minus_bulk':float(dm),'wall_minus_bulk_se':float(ds)}
    # Companion results are sensitivity diagnostics, never a fitted spatial order.
    sensitivities={}
    for row in records:
        if row['configuration']=='base':continue
        alt=np.load(output/row['fields'],allow_pickle=False)['profile']
        sensitivities[row['configuration']]={str(k):rms(alt[:,k]-base[0,:,k])/s for k,s in scales(ident).items()}
    # Halved-step sensitivity must also fit an explicit non-statistical envelope.
    for field,value in sensitivities['half_dt'].items():checks['half step sensitivity/'+field]=bool(value<=limits['half_step_sensitivity'])
    mean,se=ensemble(base)
    np.savez(output/(ident+'-ensemble.npz'),primary_profiles=base,primary_block_profiles=blocks,reference_profiles=ref,
             mean=mean,seed_se=se,wall_estimates=np.array(wall_estimates))
    metrics={'profile_comparison':comparisons,'stationarity':stat,'sensitivities':sensitivities,
             't95_multiplier_df3':3.182446305284263,**extra}
    case_record.update(passed=bool(all(checks.values())),metrics=metrics,termination='fixed_budget_completed')
    write_json(output/(ident+'-checkpoint.json'),case_record)
    return case_record


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,default=HERE/'inputs.json');p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists() and (not a.output.is_dir() or any(a.output.iterdir())):
        p.error('--output must be a fresh or empty directory; prior evidence is never overwritten')
    start=time.monotonic();a.output.mkdir(parents=True,exist_ok=True)
    cases=[];failure=None
    try:
        contract=verify_contract(a.input);inputs=json.loads(a.input.read_text());limits=json.loads((HERE/'acceptance.json').read_text())['limits']
        for ident,case in inputs['cases'].items():
            case_record={'id':ident,'passed':False,'checks':{},'metrics':{},'records':[],
                         'completed_primary_runs':0,'termination':'in_progress'}
            cases.append(case_record)
            write_json(a.output/'completed-cases.json',cases)
            run_case(ident,case,limits,a.output,case_record)
            write_json(a.output/'completed-cases.json',cases)
        result={'schema_version':1,'passed':bool(all(c['passed'] for c in cases)),
                'checks':{c['id']:c['passed'] for c in cases},'cases':cases,'termination':'fixed_budget_completed','failure':None,
                'input_sha256':sha(a.input),'source_sha256':{**contract['files_sha256'],'pre-run-contract.json':sha(HERE/'pre-run-contract.json')},
                'wall_seconds':time.monotonic()-start,'numerical_gate_count':sum(len(c['checks']) for c in cases),
                'reference_scope':'Compare every new primary case with immutable independently evolved SPARTA finite-grid HS seed fields. Reference qualification is cached and hash-bound; no SPARTA simulation in public main.'}
    except Exception as error:
        failure={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        result={'schema_version':1,'passed':False,'checks':{'completed_without_exception':False},'cases':cases,'termination':'failed','failure':failure,'wall_seconds':time.monotonic()-start}
    write_json(a.output/'result.json',result)
    print(json.dumps({'passed':result['passed'],'case_count':len(cases),'numerical_gate_count':result.get('numerical_gate_count',0),'wall_seconds':result['wall_seconds'],'failure':failure}))
    if not result['passed']:raise SystemExit(1)

if __name__=='__main__':main()
