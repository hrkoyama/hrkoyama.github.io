"""Qualify all frozen independent SPARTA outputs; never runs simulations."""
import json,sys,hashlib
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
from dsmc import profile
from diagnostics import ensemble,rms,scales,stationarity,resolution,flux,far_states


def main():
    protocol=json.loads((HERE/'reference-protocol.json').read_text());limit=protocol['acceptance']
    checks={};metrics={};cache=HERE/'qualified-cache';cache.mkdir(exist_ok=True)
    manifest={}
    for case in protocol['cases']:
        ident=case['id'];configurations={};blocks={}
        for label,cfg in case['configurations'].items():
            raw=[]
            for seed in protocol['seeds']:
                path=HERE/'runs'/ident/label/str(seed)/'raw.npz'
                a=np.load(path,allow_pickle=False)['raw_blocks']
                if a.shape!=(case['blocks'],cfg['cells'],10):raise ValueError('Reference raw shape')
                factor=cfg['cells']//case['bins']
                a=a.reshape(case['blocks'],case['bins'],factor,10).mean(axis=2)
                raw.append(a)
                manifest[str(path.relative_to(HERE))]=hashlib.sha256(path.read_bytes()).hexdigest()
            raw=np.stack(raw)
            # Each block and each full-seed estimator uses pooled raw moments.
            blocks[label]=np.stack([np.stack([profile(b) for b in seed]) for seed in raw])
            configurations[label]=np.stack([profile(np.mean(seed,axis=0)) for seed in raw])
        base=configurations['base'];mean,se=ensemble(base)
        prefix=ident+'/'
        checks[prefix+'finite']=bool(all(np.all(np.isfinite(v)) for v in configurations.values()))
        stat=stationarity(blocks['base'],ident,case['length'])
        for field,value in stat['profile_equivalence'].items():checks[prefix+'stationarity/'+field]=bool(value<=limit['reference_stationarity_rms_mean_change_plus_3se_over_profile_scale'])
        for field,scale in scales(ident).items():checks[prefix+'precision/'+str(field)]=bool(3*rms(se[:,field])/scale<=limit['reference_precision_3se_over_imposed_profile_scale'])
        if case['kind']=='shock':
            checks[prefix+'centroid stationarity']=bool(stat['centroid_drift_bound']<=limit['shock_centroid_total_drift_mean_plus_3se_lambda1'])
            far=far_states(base,case['length'])
            for name,val in far.items():checks[prefix+'RH far or flux/'+name]=bool(val['relative_error']<=limit['shock_far_state_relative_error_plus_3se']+val['relative_3se'] and val['relative_3se']<=.05)
        else:far={}
        sensitivity={}
        for label in ['fine_grid','half_dt']:
            delta=configurations[label]-base;dm,ds=ensemble(delta);values={}
            for field,scale in scales(ident).items():
                error,noise=rms(dm[:,field])/scale,3*rms(ds[:,field])/scale
                checks[prefix+label+'/sensitivity/'+str(field)]=bool(error<=limit['reference_mesh_and_dt_sensitivity_rms_mean_over_profile_scale']+noise)
                checks[prefix+label+'/precision/'+str(field)]=bool(noise<=limit['reference_precision_3se_over_imposed_profile_scale'])
                values[str(field)]={'error':error,'paired_3se':noise}
            if case['kind']=='wall':
                original=flux(base,ident);changed=flux(configurations[label],ident)
                target=float(abs(np.mean(original)));fm,fs=ensemble(changed-original)
                bm,bs=ensemble(original)
                checks[prefix+label+'/flux sensitivity']=bool(abs(fm)<=limit['wall_flux_sensitivity_relative']*target+3*fs)
                checks[prefix+label+'/flux precision']=bool(target>0 and 3*fs<=limit['wall_flux_relative_precision_3se']*target and 3*bs<=limit['wall_flux_relative_precision_3se']*target)
                values['flux']={'base':float(bm),'base_se':float(bs),'difference':float(fm),'difference_se':float(fs)}
            sensitivity[label]=values
        resolutions={}
        for label,cfg in case['configurations'].items():
            diag=resolution(configurations[label],cfg['cells'],case['length'],cfg['dt']);resolutions[label]=diag
            checks[prefix+label+'/dt tau']=bool(diag['dt_over_maxwell_tau']<=limit['all_reference_max_dt_over_local_tau'])
            if case['kind']=='shock':checks[prefix+label+'/local mean free path']=bool(diag['dx_over_lambda']<=limit['shock_reference_max_dx_over_local_lambda'])
        np.savez(cache/(ident+'.npz'),profiles_seeds=base,block_profiles=blocks['base'],fine_grid_profiles_seeds=configurations['fine_grid'],half_dt_profiles_seeds=configurations['half_dt'],seeds=np.array(protocol['seeds']))
        metrics[ident]={'stationarity':stat,'sensitivity':sensitivity,'resolution':resolutions,'far_states':far,'mean':mean.tolist(),'seed_se':se.tolist(),'t95_multiplier_df3':3.182446305284263}
    result={'passed':bool(all(checks.values())),'checks':checks,'metrics':metrics,'raw_input_sha256':manifest,'scope':protocol['reference_role'],'source_commit':protocol['source_commit'],'protocol_sha256':hashlib.sha256((HERE/'reference-protocol.json').read_bytes()).hexdigest()}
    (cache/'qualification.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'passed':result['passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}))
    if not result['passed']:raise SystemExit(1)

if __name__=='__main__':main()
