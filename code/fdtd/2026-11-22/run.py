"""Run fixed-input Yee checks. Exit 0=pass, 1=numerical failure, 2=input/error."""
import argparse
import csv
import hashlib
import json
import math
import platform
import sys
from pathlib import Path
import numpy as np
from solver import run_mesh


def validate(p):
    if p['case'] not in ('periodic-wave','pec-cavity'):
        raise ValueError('Unknown fixed-input case')
    if p['boundary'] != ('periodic' if p['case']=='periodic-wave' else 'pec'):
        raise ValueError('Boundary does not match case')
    if len(p['lengths'])!=2 or not all(math.isfinite(x) and x>0 for x in p['lengths']):
        raise ValueError('Two positive finite lengths required')
    if len(p['mode'])!=2 or not all(isinstance(x,int) and not isinstance(x,bool) and x>0 for x in p['mode']):
        raise ValueError('Two positive integer mode numbers required')
    if not 0<p['courant']<1:
        raise ValueError('courant must satisfy 0<courant<1')
    if not 0<p['error_periods']<=p['energy_periods']<=100:
        raise ValueError('Require 0<error_periods<=energy_periods<=100')
    meshes=p['meshes']
    if not isinstance(meshes,list) or not 3<=len(meshes)<=6:
        raise ValueError('Three to six meshes required')
    previous=None
    for mesh in meshes:
        if len(mesh)!=2 or not all(isinstance(x,int) and not isinstance(x,bool) and 4<=x<=256 for x in mesh):
            raise ValueError('Mesh sizes must be integers in [4,256]')
        if any(2*m>=n for m,n in zip(p['mode'],mesh)):
            raise ValueError('Modes must be strictly below Nyquist')
        if previous and (mesh[0]<=previous[0] or mesh[1]<=previous[1] or mesh[0]*previous[1]!=mesh[1]*previous[0]):
            raise ValueError('Meshes must refine both directions with the same ratio')
        previous=mesh
    a=p['acceptance']
    required=['max_field_error','min_order','max_frequency_error','max_dispersion_identity_error',
              'max_modified_energy_drift','max_divergence_drift','max_finest_energy_error']
    if not all(math.isfinite(a[k]) and a[k]>0 for k in required):
        raise ValueError('Positive finite acceptance thresholds required')


def evaluate(path):
    path=Path(path)
    p=json.loads(path.read_text());validate(p)
    meshes=[];history=[];snapshot=None
    for nx,ny in p['meshes']:
        metrics,trace,snapshot=run_mesh(p,nx,ny)
        meshes.append(metrics);history.extend(trace)
    def orders(key):
        return [float(np.log(x[key]/y[key])/np.log(y['nx']/x['nx'])) for x,y in zip(meshes,meshes[1:])]
    metrics=dict(meshes=meshes,observed_orders=orders('field_relative_l2'),
                 frequency_orders=orders('relative_frequency_error'),
                 energy_span_orders=orders('synchronized_energy_relative_span'),
                 physical_energy_error_orders=orders('synchronized_energy_max_relative_error'),
                 finest_field_error=meshes[-1]['field_relative_l2'],
                 max_modified_energy_drift=max(x['modified_energy_max_relative_drift'] for x in meshes),
                 max_dispersion_identity_error=max(x['dispersion_identity_relative_error'] for x in meshes),
                 finest_frequency_relative_error=meshes[-1]['relative_frequency_error'],
                 finest_synchronized_energy_error=meshes[-1]['synchronized_energy_max_relative_error'],
                 max_boundary_e=max(x['boundary_e_max'] for x in meshes),
                 max_magnetic_divergence_drift=max(x['magnetic_divergence_drift_max'] for x in meshes))
    a=p['acceptance']
    checks=dict(field_accuracy=metrics['finest_field_error']<=a['max_field_error'],
                field_refinement=min(metrics['observed_orders'])>=a['min_order'],
                frequency_accuracy=metrics['finest_frequency_relative_error']<=a['max_frequency_error'],
                frequency_refinement=min(metrics['frequency_orders'])>=a['min_order'],
                dispersion_identity=metrics['max_dispersion_identity_error']<=a['max_dispersion_identity_error'],
                modified_energy=metrics['max_modified_energy_drift']<=a['max_modified_energy_drift'],
                synchronized_energy_accuracy=meshes[-1]['synchronized_energy_max_relative_error']<=a['max_finest_energy_error'],
                synchronized_energy_refinement=min(metrics['physical_energy_error_orders'])>=a['min_order'],
                pec_boundary=metrics['max_boundary_e']==0,
                magnetic_divergence_preserved=metrics['max_magnetic_divergence_drift']<=a['max_divergence_drift'])
    result=dict(schema_version=1,case=p['case'],input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                environment=dict(python=platform.python_version(),numpy=np.__version__),
                normalization='dimensionless epsilon=mu=c=1; unit E amplitude; rectangular domain',
                field_error_norm='combined quadrature L2 at staggered E(t),H(t-dt/2), normalized by constant continuum total modal norm (area periodic, area/4 PEC)',
                termination='fixed_budget_completed',metrics=metrics,
                checks={k:bool(v) for k,v in checks.items()},passed=bool(all(checks.values())))
    return result,history,snapshot


def save(path,result,history,snapshot):
    path.mkdir(parents=True,exist_ok=True)
    (path/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    meshes=result['metrics']['meshes']
    with (path/'convergence.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(meshes[0]));w.writeheader();w.writerows(meshes)
    with (path/'energy.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['nx','ny','time','modified_energy','synchronized_energy','electric_mode_amplitude']);w.writerows(history)
    e,reference,g=snapshot
    with (path/'solution.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['x','y','Ez','analytic_Ez','error'])
        w.writerows([i*g['dx'],j*g['dy'],float(e[i,j]),float(reference[i,j]),float(e[i,j]-reference[i,j])]
                    for i in range(e.shape[0]) for j in range(e.shape[1]))
    # The immutable package includes this reproducible figure; no GUI needed.
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axes=plt.subplots(1,3,figsize=(13,3.7),constrained_layout=True)
    ns=[m['nx'] for m in meshes];errs=[m['field_relative_l2'] for m in meshes]
    axes[0].loglog(ns,errs,'o-',label='Combined field error')
    axes[0].loglog(ns,[errs[0]*(ns[0]/n)**2 for n in ns],'--',label='Second-order reference')
    axes[0].set(xlabel='Cells in x',ylabel='Relative L2 error',title='Continuum solution at fixed end time');axes[0].legend(fontsize=8)
    finest=np.asarray([row for row in history if row[0]==ns[-1]])
    axes[1].plot(finest[:,2]/(2*np.pi/meshes[-1]['analytic_frequency']),finest[:,3]/finest[0,3]-1,label='Modified energy drift')
    exact=g['lx']*g['ly']/(8 if g['boundary']=='pec' else 2)
    axes[1].plot(finest[:,2]/(2*np.pi/meshes[-1]['analytic_frequency']),finest[:,4]/exact-1,label='Centered physical energy error')
    axes[1].set(xlabel='Time / analytic period',ylabel='Relative difference',title='Energy: finest grid');axes[1].legend(fontsize=8)
    image=axes[2].imshow((e-reference).T,origin='lower',aspect='auto',extent=(0,g['lx'],0,g['ly']))
    axes[2].set(xlabel='x (normalized)',ylabel='y (normalized)',title='Electric field error, finest grid')
    fig.colorbar(image,ax=axes[2],label='Ez error (normalized)')
    fig.savefig(path/'summary.png',dpi=160);plt.close(fig)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    try:
        if args.output.exists() and (not args.output.is_dir() or any(args.output.iterdir())):
            raise ValueError('Output must be a new or empty directory')
        result,history,snapshot=evaluate(args.input)
        save(args.output,result,history,snapshot)
        print(json.dumps(dict(case=result['case'],passed=result['passed'],checks=result['checks'])))
        return 0 if result['passed'] else 1
    except Exception as exc:
        print(str(exc),file=sys.stderr);return 2


if __name__=='__main__':
    sys.exit(main())
