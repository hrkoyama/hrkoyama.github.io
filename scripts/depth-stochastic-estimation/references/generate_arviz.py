"""Independent process: supplied arrays plus public ArviZ APIs only."""
import argparse,hashlib,json,platform,importlib.metadata,time
from pathlib import Path
import numpy as np
import arviz as az


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists():raise ValueError('Never overwrite independent reference')
    assert az.__version__=='0.20.0';start=time.monotonic();manifest=json.loads((a.input/'manifest.json').read_text());archive=a.input/'observable-arrays.npz'
    assert hashlib.sha256(archive.read_bytes()).hexdigest()==manifest['arrays_sha256']
    calls={'rhat_rank':lambda x:az.rhat(x,method='rank'),'ess_bulk':lambda x:az.ess(x,method='bulk'),'ess_tail':lambda x:az.ess(x,method='tail',prob=(.05,.95)),'ess_mean':lambda x:az.ess(x,method='mean'),'mcse_mean':lambda x:az.mcse(x,method='mean')};rows=[]
    with np.load(archive,allow_pickle=False) as data:
        for entry in manifest['datasets']:
            x=np.asarray(data[entry['key']][:,:entry['prefix'],entry['column']],dtype='<f8',order='C')
            assert list(x.shape)==entry['shape'] and hashlib.sha256(x.tobytes()).hexdigest()==entry['sha256']
            values={k:float(fn(x)) for k,fn in calls.items()}
            if not all(np.isfinite(v) and v>0 for v in values.values()):raise ArithmeticError('Nonfinite or nonpositive independent diagnostic')
            rows.append({**entry,'metrics':values})
            a.output.with_suffix('.partial.json').write_text(json.dumps({'datasets':rows},indent=2,allow_nan=False)+'\n')
    pkg=Path(az.__file__).resolve().parent
    result={'schema_version':1,'reference':'ArviZ','version':az.__version__,'actually_executed':True,'datasets':rows,'candidate_input_manifest':manifest,'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'upstream_source_sha256':hashlib.sha256((pkg/'stats/diagnostics.py').read_bytes()).hexdigest(),'environment':{'python':platform.python_version(),'platform':platform.platform(),'packages':{k:importlib.metadata.version(k) for k in ['arviz','numpy','scipy','matplotlib','pandas','xarray']}},'seconds':time.monotonic()-start,'independence':'No atlas sampler or diagnostics imported; supplied scalar arrays plus public ArviZ APIs only. This qualifies diagnostic operators,not independent target sampling.'}
    a.output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps({'datasets':len(rows),'metric_values':len(rows)*5,'seconds':result['seconds']}))

if __name__=='__main__':main()
