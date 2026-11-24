"""Fixed ordinary IS and genuinely two-dimensional MH; cached diagnostic engine."""
from pathlib import Path
import json,hashlib
import numpy as np
from importance import simulate as importance_simulate
from sampler import sample,observable_arrays,truth_and_scales,OBSERVABLES
from diagnostics import diagnose,mean_mcse
from support import run,sha,write,csv_numeric,case_record,finish_case

HERE=Path(__file__).resolve().parent


def fixed_diagnostic_array(data,row):
    """Qualify the SAME immutable data; fresh generated chains have a separate role."""
    x=np.asarray(data[row['key']][:,:row['prefix'],row['column']],dtype='<f8',order='C')
    if list(x.shape)!=row['shape'] or hashlib.sha256(x.tobytes()).hexdigest()!=row['sha256']:
        raise ValueError('Immutable diagnostic fixture bytes differ')
    return x


def experiment(cfg,limits,out,cases,partial):
    ir=json.loads((HERE/'references/is-reference.json').read_text());ar=json.loads((HERE/'references/arviz-reference.json').read_text());aq=json.loads((HERE/'references/arviz-qualification.json').read_text())
    if ir['passed'] is not True or aq['passed'] is not True or not all(v is True for v in aq['checks'].values()) or len(aq['checks'])!=640:raise ValueError('Independent reference qualification failed')
    if aq['reference_sha256']!=sha(HERE/'references/arviz-reference.json') or aq['diagnostics_sha256']!=sha(HERE/'diagnostics.py'):raise ValueError('Stale diagnostic reference qualification')
    for name,expected in ar['candidate_input_manifest']['source_sha256'].items():
        if sha(HERE/name)!=expected:raise ValueError('Changed reference-generating source '+name)
    if ir['input_sha256']!=sha(HERE/'inputs.json') or ir['acceptance_sha256']!=sha(HERE/'acceptance.json'):raise ValueError('IS oracle input/criteria mismatch')
    if ir['generator_sha256']!=sha(HERE/'references/qualify_is.py'):raise ValueError('Stale IS moment generator')
    if sha(HERE/'references/diagnostic-fixture.npz')!=aq['array_archive_sha256']:raise ValueError('Immutable diagnostic archive differs')
    with np.load(HERE/'references/diagnostic-fixture.npz',allow_pickle=False) as archive:fixed_arrays={k:archive[k] for k in archive.files}
    ref={(x['key'],x['prefix'],x['observable']):x for x in ar['datasets']}
    if len(ref)!=128:raise ValueError('Incomplete128dataset independent cache')
    for ident,c in cfg['cases'].items():
        row=case_record(ident,cases);checks=row['checks'];add=lambda key,value:checks.update({key:bool(value)})
        if ident=='normal-tail-importance':
            data,records=importance_simulate(c,partial);np.savez(out/(ident+'.npz'),**data);partial.clear();add('finite saved contribution arrays',all(np.isfinite(v).all() for v in data.values()));csv=[]
            for z in records:
                row['records'].append({'threshold':z['a'],'samples':z['n'],'independent_seed_batches':len(c['seeds']),'candidate_file':ident+'.npz'})
                key=f"a{z['a']}/n{z['n']}";oracle=ir['records'][str(z['a'])];p=oracle['probability'];var=oracle['variance'];ratio=z['batch_variance']/(var/z['n'])
                add(key+'/mean calibration',abs(z['estimate_mean']-p)<=limits['IS_mean_z']*z['aggregate_known_se'])
                add(key+'/batch variance calibration',limits['IS_batch_variance_ratio'][0]<=ratio<=limits['IS_batch_variance_ratio'][1])
                add(key+'/analytic variance reduction',var/oracle['direct_variance']<limits['IS_analytic_variance_reduction_ratio'])
                add(key+'/unweighted proposal negative control',abs(z['unweighted_proposal_event_mean']-p)>100*z['aggregate_known_se'])
                csv.append([z['a'],z['n'],p,z['estimate_mean'],z['aggregate_known_se'],ratio,z['IS_coverage'],*z['IS_coverage_binomial_CI'],z['direct_coverage'],z['direct_no_hit_batches']])
            row['metrics']={'records':records,'independent_batches_per_configuration':len(c['seeds']),'scope':'Known-moment calibration and finite repeated-interval coverage. Neither nominal intervals nor their64trial coverage is a deterministic bound/general95%coverage proof. Ordinary IS weights have no random denominator.'};csv_numeric(out/(ident+'.csv'),['threshold','samples','truth','estimate','aggregate_SE','variance_ratio','IS_coverage','coverage_low','coverage_high','direct_coverage','direct_nohit_batches'],csv)
        elif ident=='correlated-gaussian-mcmc':
            packed={};records=[];csv=[];truth,scale=truth_and_scales(c['rho'])
            for seed in c['seeds']:
                for pid,proposal in enumerate(c['proposals']):
                    key=f'{proposal}-{seed}';raw=sample(c,seed,proposal,partial);values=observable_arrays(raw['chains'],c['mean'],c['rho']);packed[key]=values;row['records'].append({'seed':seed,'proposal':proposal,'chains':c['chains'],'saved_draws':c['draws'],'candidate_file':ident+'.npz'})
                    for name,x in raw.items():packed[key+'-'+name]=x
                    # Preserve complete evolved candidate before diagnostics/qualification.
                    np.savez(out/(ident+'.npz'),**packed);write(out/(ident+'-candidate-checkpoint.json'),{'completed_chainsets':[k for k in packed if not k.endswith(('-chains','-accepted','-initial'))]})
                    add(key+'/finite candidate',all(np.isfinite(v).all() for v in raw.values()) and np.isfinite(values).all());partial.clear()
                    for prefix in c['prefixes']:
                        for j,obs in enumerate(OBSERVABLES):
                            x=np.asarray(values[:,:prefix,j],dtype='<f8',order='C');cache=ref[(key,prefix,obs)]
                            fixture_x=fixed_diagnostic_array(fixed_arrays,cache)
                            fixture_stats=diagnose(fixture_x);fixture_stats['mcse_mean']=mean_mcse(fixture_x)
                            stats=diagnose(x);stats['mcse_mean']=mean_mcse(x);estimate=float(x.mean());base=f'{key}/{prefix}/{obs}'
                            for name,target in cache['metrics'].items():
                                tolerance=limits['reference_rhat_absolute'] if name=='rhat_rank' else limits['reference_mcse_relative']*target if name=='mcse_mean' else limits['reference_ess_relative']*target
                                add(base+'/ArviZ/'+name,fixture_stats[name] is not None and abs(fixture_stats[name]-target)<=tolerance)
                            if proposal=='preconditioned' and prefix==c['draws']:
                                add(base+'/rank-folded Rhat',stats['rhat_rank']<=limits['MCMC_rhat_max'])
                                add(base+'/bulk-tail ESS',min(stats['ess_bulk'],stats['ess_tail'])>=limits['MCMC_bulk_tail_ess_min'])
                                add(base+'/observable MCSE',stats['mcse_mean']/scale[j]<=limits['MCMC_mcse_over_natural_sd_max'])
                                add(base+'/known target moment',abs(estimate-truth[j])<=limits['MCMC_moment_mcse_factor']*stats['mcse_mean']+limits['MCMC_moment_sd_allowance']*scale[j])
                            record={'seed':seed,'proposal':proposal,'prefix':prefix,'observable':obs,'estimate':estimate,'analytic_truth':float(truth[j]),'natural_sd':float(scale[j]),'diagnostics':stats,'same_data_fixture_sha256':cache['sha256'],'fresh_data_sha256':hashlib.sha256(x.tobytes()).hexdigest(),'fresh_equals_fixture_bytes':hashlib.sha256(x.tobytes()).hexdigest()==cache['sha256']};records.append(record);csv.append([seed,pid,prefix,j,estimate,float(truth[j]),float(scale[j]),stats['rhat_rank'],stats['ess_bulk'],stats['ess_tail'],stats['ess_mean'],stats['mcse_mean']])
                    write(out/(ident+'-diagnostic-checkpoint.json'),{'records':records,'checks':checks})
            row['metrics']={'records':records,'acceptance_rates':{k:float(v.mean()) for k,v in packed.items() if k.endswith('-accepted')},'scope':'All4preconditioned chainsets have per-observable full-prefix gates. Isotropic fixed comparator and short prefixes are reported,not required to fail or pass a mixing gate. ArviZ validates diagnostics on the immutable identical-data fixture,not on a claimed cross-platform byte-identical fresh simulation. Positive physical/mixing gates use fresh chains; analytic Gaussian moments validate joint target. Rhat/ESS/MCSE do not prove global convergence.','remaining_unimplemented':['banana','funnel','HMC','NUTS']};csv_numeric(out/(ident+'.csv'),['seed','proposal_code','prefix','observable_code','estimate','truth','natural_sd','Rhat','ESS_bulk','ESS_tail','ESS_mean','MCSE_mean'],csv)
        else:raise ValueError('Unknown fixed estimation case')
        finish_case(row,out)
    write(out/'completed-cases.json',cases)

if __name__=='__main__':run(experiment,HERE)
