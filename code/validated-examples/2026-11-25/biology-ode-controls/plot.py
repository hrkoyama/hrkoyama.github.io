"""Plot saved numerical arrays and saved qualification metadata only; no solvers."""
from __future__ import annotations
import argparse,json,os
from pathlib import Path
for key in ['MPLCONFIGDIR','TMPDIR','PYTHONPYCACHEPREFIX']:
    if not os.environ.get(key) or not Path(os.environ[key]).is_absolute():
        raise RuntimeError(key+'mustpointtoanownedabsolutescratchdirectory')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from common import assert_frozen
COLORS=['#0072B2','#D55E00','#009E73','#CC79A7']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,
    'axes.titleweight':'bold','figure.facecolor':'white','axes.grid':True,'grid.alpha':.17,'savefig.facecolor':'white'})

class Saved:
    def __init__(self,path):
        self.path=Path(path);self.root=self.path.parent;self.result=json.loads(self.path.read_text())
        if self.result.get('termination')!='completed_fixed_protocol':raise ValueError('Completedfixedprotocolrequired')
        self.rows={r['id']:r for r in self.result['rows']}
    def data(self,key):
        path=self.root/self.rows[key]['data']
        with np.load(path,allow_pickle=False) as z:return {k:z[k] for k in z.files}
    def meta(self,key):return self.rows[key]

def finish(fig,out,name):
    path=Path(out)/name
    if path.exists():raise FileExistsError('Refuseoverwrite: '+str(path))
    fig.tight_layout(pad=1.5);fig.savefig(path,dpi=145);plt.close(fig)

def ecdf(ax,values,label,color):
    x=np.sort(values);ax.step(x,np.arange(1,len(x)+1)/len(x),where='post',label=label,color=color,lw=1.6)


def figures(s,out):
    d=s.data('hh-pulse-0p01');t=d['time'];y=d['state'];ref=d['reference']
    fig,ax=plt.subplots(1,2,figsize=(11.2,4.6))
    ax[0].plot(t,y[:,0],color=COLORS[0],lw=1.8,label='RK4,h=0.01ms');ax[0].plot(t,ref[:,0],color='black',ls='--',lw=.9,label='Independent reference')
    ax[0].axvspan(10,11,color=COLORS[1],alpha=.15,label='Current pulse');ax[0].set(xlabel='Time(ms)',ylabel='Membrane voltage(mV)',title='Segment-owned current');ax[0].legend(fontsize=8)
    im=ax[1].scatter(y[::3,0],y[::3,3],c=t[::3],s=8,cmap='viridis',rasterized=True)
    ax[1].set(xlabel='Membrane voltage(mV)',ylabel='Potassium gate n',title='Saved phase portrait');fig.colorbar(im,ax=ax[1],label='Time(ms)')
    finish(fig,out,'hodgkin-huxley-controls.png')
    fig,ax=plt.subplots(1,2,figsize=(11.2,4.6))
    for j,label in enumerate(['m','h','n']):ax[0].plot(t,y[:,j+1],label=label,color=COLORS[j])
    ax[0].set(xlabel='Time(ms)',ylabel='Gate fraction',title='Accepted states, no clipping');ax[0].legend()
    for j,v in enumerate([-80,-55,-40,0]):
        rr=sorted([r for k,r in s.rows.items() if k.startswith('hh-clamp-') and r['V']==v],key=lambda x:x['h'])
        positive=[r for r in rr if r['max_all_time_error']>0]
        ax[1].loglog([r['h'] for r in positive],[r['max_all_time_error'] for r in positive],'o-',color=COLORS[j],label=str(v)+'mV')
    ax[1].axhline(1e-8,color='black',ls='--',lw=.9,label='Original study goal');ax[1].set(xlabel='RK4 step(ms)',ylabel='All-time gate error',title='Exact clamp comparison');ax[1].legend(fontsize=8)
    finish(fig,out,'hodgkin-huxley-controls-diagnostics.png')
    display=s.data('ssa-display-path');d=s.data('ssa-ensemble-2');a=d['counts'];times=d['time'];limit=int(a.max());bins=np.arange(limit+2)-.5
    heat=np.array([np.histogram(a[:,j],bins=bins)[0]/len(a) for j in range(4)]).T
    fig,ax=plt.subplots(1,2,figsize=(11.2,4.6))
    path=display['event_history'];ax[0].step(np.r_[path[:,0],4],np.r_[path[:,1],path[-1,1]],where='post',color=COLORS[0],lw=1.5)
    ax[0].scatter(display['observation_time'],display['counts'],s=28,color=COLORS[1],zorder=3);ax[0].set(xlabel='Time',ylabel='Molecular count N',title='One separate fixed path (seed  11)',xlim=(0,4))
    im=ax[1].imshow(heat,origin='lower',aspect='auto',cmap='magma',extent=(-.5,3.5,-.5,limit+.5))
    ax[1].set(xticks=range(4),xticklabels=[str(v) for v in times],xlabel='Observation time (discrete)',ylabel='Molecular count N',title='2,048 saved paths, start N=5');fig.colorbar(im,ax=ax[1],label='Empirical probability')
    finish(fig,out,'immigration-death-ssa.png')
    fig,ax=plt.subplots(1,2,figsize=(11.2,4.6))
    for i in range(6):
        row=s.meta('ssa-ensemble-'+str(i));ds=row['diagnostics'];ts=[x['time'] for x in ds if not x.get('deterministic_t0')]
        mu=[x['mean'] for x in ds if not x.get('deterministic_t0')];truth=[x['exact_mean'] for x in ds if not x.get('deterministic_t0')]
        label=str(row['initial_law'])+',seed '+str(row['seed_label'])
        ax[0].plot(ts,np.array(mu)-truth,'o-',lw=1,label=label)
        ax[1].plot(ts,[x['DKW_observed'] for x in ds if not x.get('deterministic_t0')],'o-',lw=1)
    ax[0].axhline(0,color='black',lw=.8);ax[0].set(xlabel='Observation time',ylabel='Empirical minus exact mean',title='All six fixed ensembles');ax[0].legend(fontsize=7,ncol=2)
    eps=next(x['DKW_epsilon'] for x in s.meta('ssa-ensemble-2')['diagnostics'] if 'DKW_epsilon'in x)
    ax[1].axhline(eps,color='black',ls='--',label='Simultaneous nominal DKW');ax[1].set(xlabel='Observation time',ylabel='CDF deviation',title='Ideal-law reference, actual outcomes');ax[1].legend(fontsize=8)
    finish(fig,out,'immigration-death-ssa-diagnostics.png')

def main():
    p=argparse.ArgumentParser();p.add_argument('--results',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    assert_frozen(Path(__file__).resolve().parent);out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
    saved=Saved(a.results);figures(saved,out)
    names=sorted(x.name for x in out.glob('*.png'))
    (out/'figure-index.json').write_text(json.dumps({'source_result':Path(a.results).name,'figures':names,'solver_calls':0},indent=2)+'\n')
if __name__=='__main__':main()
