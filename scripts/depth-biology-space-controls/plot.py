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
    d=s.data('fisher-space-0p125');x=d['x'][1:-1];u=d['all_interior'];t=d['all_time']
    fig,ax=plt.subplots(1,2,figsize=(11.2,4.6))
    im=ax[0].pcolormesh(x,t,u,shading='auto',cmap='viridis');ax[0].set(xlabel='Position x',ylabel='Time',title='Saved Fisher front');fig.colorbar(im,ax=ax[0],label='u')
    ax[1].plot(d['x'],d['state'][-1],color=COLORS[0],label='Numerical');ax[1].plot(d['x'],d['exact'][-1],color='black',ls='--',label='Special-speed exact')
    ax[1].set(xlabel='Position x',ylabel='u(x,1)',title='Profile and quarter contour');ax[1].legend()
    finish(fig,out,'fisher-kpp-special-front.png')
    fig,ax=plt.subplots(1,2,figsize=(11.2,4.6))
    sp=sorted([r for k,r in s.rows.items() if k.startswith('fisher-space-')],key=lambda r:r['h'])
    ti=sorted([r for k,r in s.rows.items() if k.startswith('fisher-time-') and k!='fisher-time-reference'],key=lambda r:r['dt'])
    ax[0].loglog([r['h'] for r in sp],[r['Linf'] for r in sp],'o-',color=COLORS[0],label='Space: continuum error')
    ax[0].loglog([r['dt'] for r in ti],[r['same_MOL_error'] for r in ti],'s-',color=COLORS[1],label='Time: same MOL');ax[0].set(xlabel='Grid spacing or time step',ylabel='Maximum error',title='Distinct convergence experiments');ax[0].legend(fontsize=8)
    for j,L in enumerate([6,12,24]):
        b=s.data('fisher-boundary-'+str(L));ax[1].plot(b['x'],b['state'][-1]-b['exact'][-1],label='L='+str(L),color=COLORS[j])
    ax[1].axvspan(-3,3,color='gray',alpha=.1,label='Declared core');ax[1].set(xlabel='Position x',ylabel='Constant boundary minus exact',title='Full-domain boundary error');ax[1].legend(fontsize=8)
    finish(fig,out,'fisher-kpp-special-front-diagnostics.png')
    fig,ax=plt.subplots(1,3,figsize=(12.6,4.3),constrained_layout=False)
    arrays=[]
    for ic in ['N-mode42','N-mixed','D-mode42']:arrays.append(s.data('schnak-summary-'+ic)['state'][-1,0])
    vmin=min(a.min() for a in arrays);vmax=max(a.max() for a in arrays)
    for aa,ic,a in zip(ax,['Neumann: mode(4,2)','Neumann: mixed modes','Equilibrium Dirichlet'],arrays):
        im=aa.imshow(a.T,origin='lower',extent=(0,2*np.pi,0,2*np.pi),vmin=vmin,vmax=vmax,cmap='viridis',aspect='equal');aa.set(xlabel='x',ylabel='y',title=ic)
        fig.colorbar(im,ax=aa,fraction=.045,label='Saved u(x,y,2)')
    finish(fig,out,'schnakenberg-2d-boundary-modes.png')
    fig,ax=plt.subplots(1,2,figsize=(11.2,4.6))
    for j,ic in enumerate(['N-mode42','N-mixed','D-mode42']):
        a=s.data('schnak-summary-'+ic);err=a['error'][-1,0]
        ax[0].plot(np.arange(48)+.5,err[:,24],label=ic,color=COLORS[j])
        row=s.meta('schnak-summary-'+ic);ax[1].loglog([12,24,48],row['grid_errors'],'o-',label=ic,color=COLORS[j])
    ax[0].set(xlabel='Cell index (first coordinate)',ylabel='u minus Galerkin reference',title='Saved midline discrepancy');ax[0].legend(fontsize=8)
    ax[1].set(xlabel='Cells per direction',ylabel='All-field/time Linf discrepancy',title='Finite-reference comparison');ax[1].legend(fontsize=8)
    finish(fig,out,'schnakenberg-2d-boundary-modes-diagnostics.png')
    d=s.data('KS-space-N48');a=d['state'][-1,0];e=a-d['exact'][-1,0]
    fig,ax=plt.subplots(1,3,figsize=(12.6,4.3))
    for aa,value,title,cmap in zip(ax,[a,d['exact'][-1,0],e],['Saved density n','Exact cell average','Numerical minus exact'],['viridis','viridis','RdBu_r']):
        kw={'vmin':-np.max(np.abs(e)),'vmax':np.max(np.abs(e))} if title.startswith('Numerical minus') else {'vmin':min(a.min(),d['exact'][-1,0].min()),'vmax':max(a.max(),d['exact'][-1,0].max())}
        im=aa.imshow(value.T,origin='lower',extent=(0,1,0,1),cmap=cmap,**kw);aa.set(xlabel='x',ylabel='y',title=title);fig.colorbar(im,ax=aa,fraction=.045)
    finish(fig,out,'keller-segel-forced-flux.png')
    fig,ax=plt.subplots(1,2,figsize=(11.2,4.6))
    for k,label in enumerate(['n','c']):
        rows=[s.meta('KS-space-N'+str(N)) for N in [12,24,48]]
        ax[0].loglog([12,24,48],[r['Linf_fields'][k] for r in rows],'o-',label=label,color=COLORS[k])
        ax[1].plot([12,24,48],[r['mass_residual'][k] for r in rows],'o-',label=label,color=COLORS[k])
    ax[0].set(xlabel='Cells per direction',ylabel='All-time cell-average Linf error',title='Smooth manufactured solution');ax[0].legend()
    ax[1].set(xlabel='Cells per direction',ylabel='Discrete stage-ledger residual',title='Flux / reaction / source accounting');ax[1].legend()
    finish(fig,out,'keller-segel-forced-flux-diagnostics.png')

def main():
    p=argparse.ArgumentParser();p.add_argument('--results',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    assert_frozen(Path(__file__).resolve().parent);out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
    saved=Saved(a.results);figures(saved,out)
    names=sorted(x.name for x in out.glob('*.png'))
    (out/'figure-index.json').write_text(json.dumps({'source_result':Path(a.results).name,'figures':names,'solver_calls':0},indent=2)+'\n')
if __name__=='__main__':main()
