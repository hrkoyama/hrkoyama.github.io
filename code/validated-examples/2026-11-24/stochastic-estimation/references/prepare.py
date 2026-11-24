"""Generate the eight fixed MH chainsets for an independent diagnostic engine.

This IS candidate MCMC scientific evolution,not an operator-only fixture.
Requires the source/input/acceptance reference contract and parent authorization.
"""
import argparse,hashlib,json,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from sampler import sample,observable_arrays,OBSERVABLES


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists():raise ValueError('Fresh reference-input output required')
    a.output.mkdir(parents=True);c=json.loads(a.input.read_text())['cases']['correlated-gaussian-mcmc'];arrays={};rows=[];partial={}
    try:
        for seed in c['seeds']:
            for proposal in c['proposals']:
                ident=f'{proposal}-{seed}';data=sample(c,seed,proposal,partial);values=observable_arrays(data['chains'],c['mean'],c['rho']);arrays[ident]=values
                for prefix in c['prefixes']:
                    for j,name in enumerate(OBSERVABLES):
                        x=np.asarray(values[:,:prefix,j],dtype='<f8',order='C')
                        rows.append({'key':ident,'prefix':prefix,'observable':name,'column':j,'shape':list(x.shape),'sha256':hashlib.sha256(x.tobytes()).hexdigest()})
                np.savez(a.output/'observable-arrays.npz',**arrays)
                (a.output/'completed-chainsets.json').write_text(json.dumps({'completed':list(arrays),'datasets':rows},indent=2)+'\n')
    except Exception:
        np.savez(a.output/'failed-candidate-state.npz',**partial);raise
    source=a.input.parent
    manifest={'schema_version':1,'actual_candidate_MH_evolutions':8,'datasets':rows,'input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),'source_sha256':{k:hashlib.sha256((source/k).read_bytes()).hexdigest() for k in ['sampler.py','inputs.json','acceptance.json']},'arrays_sha256':hashlib.sha256((a.output/'observable-arrays.npz').read_bytes()).hexdigest(),'scope':'Same actual scalar observable arrays supplied to ArviZ; independent diagnostic implementation,not an independent sampler or target oracle.'}
    (a.output/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'candidate_MH_evolutions':8,'scalar_datasets':len(rows)}))

if __name__=='__main__':main()
