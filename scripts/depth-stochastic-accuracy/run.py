"""Run all fixed scalar weak/strong experiments; preserve candidates before fitting."""
from pathlib import Path
import json
import numpy as np
from scipy.special import ndtri
from scipy.stats import beta
from paths import simulate_batch
from support import run,sha,write,csv_numeric,case_record,finish_case

HERE=Path(__file__).resolve().parent

def fit_order(h,errors):
    if not np.all(np.isfinite(errors)) or np.any(np.asarray(errors)==0):raise ArithmeticError('Unresolved/nonfinite fixed slope; no window selection')
    return float(np.polyfit(np.log(h),np.log(np.abs(errors)),1)[0])

def binomial_interval(k,n):
    return [0. if k==0 else float(beta.ppf(.025,k,n-k+1)),1. if k==n else float(beta.ppf(.975,k+1,n-k))]


def experiment(cfg,limits,out,cases,partial):
    ref=json.loads((HERE/'references/reference.json').read_text())
    if ref['passed'] is not True or not all(v is True for v in ref['checks'].values()):raise ValueError('Analytic reference qualification failed')
    if ref['input_sha256']!=sha(HERE/'inputs.json') or ref['acceptance_sha256']!=sha(HERE/'acceptance.json'):raise ValueError('Analytic cache input/criteria mismatch')
    for name,expected in ref.get('source_sha256',{}).items():
        if sha(HERE/'references'/name)!=expected:raise ValueError('Stale analytic reference source '+name)
    for ident,c in cfg['cases'].items():
        row=case_record(ident,cases);checks=row['checks'];methods=['em','milstein'] if ident.endswith('strong') else ['em'];saved=[];hashes=[]
        for seed in c['seeds']:
            candidate,driver_hash=simulate_batch(c,seed,methods,partial);saved.append(candidate);hashes.append(driver_hash);row['records'].append({'seed':seed,'steps':c['steps'],'methods':methods,'candidate_file':ident+'.npz','driver_sha256':driver_hash})
            # Completed candidate data are persisted BEFORE any error fit or gate.
            packed={k:np.stack([x[k] for x in saved]) for k in candidate}
            np.savez(out/(ident+'.npz'),**packed)
            write(out/(ident+'-candidate-checkpoint.json'),{'id':ident,'completed_batches':len(saved),'seeds':c['seeds'][:len(saved)],'fine_driver_sha256':hashes})
        partial.clear();nvalues=packed['endpoints'];exact=packed['exact'];h=np.array([c['T']/n for n in c['steps']]);reference=ref['records'][ident]
        add=lambda key,value:checks.update({key:bool(value)})
        add('finite saved candidate arrays',all(np.isfinite(v).all() for v in packed.values()))
        association=float(np.max(packed['association_error']));bound=limits['brownian_sum_roundoff_eps_factor']*np.finfo(float).eps*max(1.,float(np.max(abs(packed['terminal_w']))))
        add('declared Brownian grouping roundoff',association<=bound)
        if not ident.endswith('strong'):
            metric=[];rows=[]
            for power in [1,2]:
                number=nvalues[:,0]**power;truth=exact[:,None,:]**power;batch=(number-truth).mean(axis=2);mean=batch.mean(axis=0);se=np.std(batch,axis=0,ddof=1)/np.sqrt(len(batch));raw_mean=number.mean(axis=2);raw_se=np.std(number,axis=2,ddof=1)/np.sqrt(c['paths_per_batch']);values=[]
                for j,n in enumerate(c['steps']):
                    expected=reference[j]['bias'][power-1];pred=np.sqrt(reference[j]['paired_variance'][power-1]/(len(c['seeds'])*c['paths_per_batch']));ratio=float(se[j]/pred)
                    add(f'power{power}/n{n}/paired mean calibration',abs(mean[j]-expected)<=limits['weak_mcse_factor']*se[j]+limits['calibration_absolute_allowance'])
                    add(f'power{power}/n{n}/MCSE calibration',limits['weak_mcse_ratio'][0]<=ratio<=limits['weak_mcse_ratio'][1])
                    if j>=len(h)-2:add(f'power{power}/n{n}/resolved before slope',3*se[j]<=limits['weak_resolution_3se_fraction']*abs(expected))
                    discrete=reference[j]['discrete'][power-1];covered=(raw_mean[:,j]-ndtri(.975)*raw_se[:,j]<=discrete)&(discrete<=raw_mean[:,j]+ndtri(.975)*raw_se[:,j]);coverage=float(covered.mean());ci=binomial_interval(int(covered.sum()),len(batch))
                    values.append({'steps':n,'analytic_bias':expected,'paired_mean':float(mean[j]),'paired_MCSE':float(se[j]),'analytic_expected_MCSE':float(pred),'raw_EM_interval_coverage_for_discrete_truth':coverage,'coverage_binomial95':ci})
                    rows.append([power,n,expected,float(mean[j]),float(se[j]),float(pred),coverage,*ci])
                sampled=fit_order(h[-3:],mean[-3:]);analytic=fit_order(h[-3:],[x['bias'][power-1] for x in reference[-3:]])
                add(f'power{power}/analytic weak order',limits['weak_analytic_order'][0]<=analytic<=limits['weak_analytic_order'][1])
                add(f'power{power}/sampled paired weak order',limits['weak_sample_order'][0]<=sampled<=limits['weak_sample_order'][1])
                metric.append({'observable_power':power,'sampled_paired_order':sampled,'analytic_order':analytic,'levels':values,'coverage_scope':'Independent batch95%normal intervals target discrete EM moments,not the continuous diffusion; coverage is descriptive and not a pass criterion.'})
            row['metrics']={'observables':metric,'Brownian_association_error':association,'fine_driver_sha256':hashes,'completed_independent_seed_batches':len(saved)}
            csv_numeric(out/(ident+'.csv'),['power','steps','analytic_bias','paired_mean','MCSE','analytic_MCSE','coverage_discrete','coverage_low','coverage_high'],rows)
        else:
            rows=[];metrics=[];rms=[]
            for method_id,method in enumerate(methods):
                values=[];errors=nvalues[:,method_id]-exact[:,None,:];squared=errors*errors;levelmean=squared.mean(axis=(0,2));levelse=np.std(squared.transpose(1,0,2).reshape(len(h),-1),axis=1,ddof=1)/np.sqrt(len(exact)*c['paths_per_batch']);r=np.sqrt(levelmean);rms.append(r)
                for j,n in enumerate(c['steps']):
                    expected=reference[j][method]['mse'];add(f'{method}/n{n}/squared error calibration',abs(levelmean[j]-expected)<=limits['strong_mcse_factor']*levelse[j]+limits['calibration_absolute_allowance'])
                    lo=np.sqrt(max(0.,float(levelmean[j]-ndtri(.975)*levelse[j])));hi=np.sqrt(float(levelmean[j]+ndtri(.975)*levelse[j]));values.append({'steps':n,'sample_RMS':float(r[j]),'analytic_RMS':reference[j][method]['rms'],'squared_error_SE':float(levelse[j]),'RMS_nominal95':[float(lo),float(hi)]});rows.append([method_id,n,float(r[j]),reference[j][method]['rms'],float(levelmean[j]),float(levelse[j]),float(lo),float(hi)])
                blocks=squared.reshape(len(exact),len(h),16,c['paths_per_batch']//16).mean(axis=3).transpose(0,2,1).reshape(-1,len(h));jack=[]
                for leave in range(len(blocks)):
                    jack.append(fit_order(h[-3:],np.sqrt((blocks.sum(axis=0)-blocks[leave])/(len(blocks)-1))[-3:]))
                jack=np.array(jack);jack_se=float(np.sqrt((len(jack)-1)/len(jack)*np.sum((jack-jack.mean())**2)))
                rate=fit_order(h[-3:],r[-3:]);band=limits['strong_'+method+'_order'];add(method+'/sampled RMS order',band[0]<=rate<=band[1]);metrics.append({'method':method,'fixed_last_three_level_order':rate,'paired64block_jackknife_order_SE':jack_se,'levels':values,'scope':'L2endpoint RMS; uncertainty is first computed on complete-path squared error,not independent-level regression.'})
            add('finest Milstein advantage',rms[1][-1]<=limits['strong_finest_ratio']*rms[0][-1]);row['metrics']={'methods':metrics,'fine_driver_sha256':hashes,'Brownian_association_error':association,'same_exact_endpoint_role':'One stored fine terminal array reused by both methods and every level; sums under different associations need not be bit identical.'}
            csv_numeric(out/(ident+'.csv'),['method_code','steps','RMS','analytic_RMS','MSE','MSE_SE','RMS_low','RMS_high'],rows)
        finish_case(row,out)
    write(out/'completed-cases.json',cases)

if __name__=='__main__':run(experiment,HERE)
