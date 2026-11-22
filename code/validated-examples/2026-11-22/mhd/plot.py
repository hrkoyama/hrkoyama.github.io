import argparse,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--results',required=True);p.add_argument('--output',required=True);a=p.parse_args();r=json.loads(Path(a.results).read_text());out=Path(a.output);out.mkdir(exist_ok=True);source=Path(a.results).parent
for c in r['cases']:
    fig,ax=plt.subplots(1,2,figsize=(10.8,3.7),layout='constrained');records=c['records']
    if c['id']=='ct-glm-independent':
        for method in ['ct','glm']:
            rows=[x for x in records if x['method']==method]
            ax[0].loglog([x['n'] for x in rows],[x['density_relative_l1'] for x in rows],'o-',label=method.upper())
            ax[1].loglog([x['n'] for x in rows],[x['by_relative_l1'] for x in rows],'o-',label=method.upper())
        ax[0].set_ylabel('Density relative L1 vs Athena++');ax[1].set_ylabel('By relative L1 vs Athena++')
    elif c['id'] in ['brio-independent','shu-independent']:
        key='brio' if c['id'].startswith('brio') else 'shu';v=np.loadtxt(source/(key+'-solution.csv'),delimiter=',',skiprows=1);refcol=3 if key=='brio' else 2
        ax[0].plot(v[:,0],v[:,refcol],label='Athena++ restricted reference');ax[0].plot(v[:,0],v[:,1],label='Atlas',lw=1);ax[0].set(xlabel='x',ylabel='Density')
        ax[1].loglog([x['n'] for x in records],[x['density_l1'] for x in records],'o-',label='Density L1');ax[1].set_ylabel('Mean absolute density error')
    else:
        ax[0].loglog([x['n'] for x in records],[x['l2_error'] for x in records],'o-',label='L2 vs continuous expm')
        ax[1].plot([x['n'] for x in records],[x['divergence_norm_ratio'] for x in records],'o-',label='Numerical amplitude ratio');ax[1].axhline(c['metrics']['continuum_amplitude_ratio'],ls='--',color='k',label='Continuum')
        ax[0].set_ylabel('Field L2 error');ax[1].set_ylabel('Longitudinal-mode amplitude ratio')
    for i,x in enumerate(ax):
        if not(c['id'] in ['brio-independent','shu-independent'] and i==0):x.set_xlabel('Cells per axis')
        x.grid(alpha=.2);x.legend(fontsize=8)
    fig.suptitle(c['id']);fig.savefig(out/(c['id']+'.png'),dpi=150);plt.close(fig)
