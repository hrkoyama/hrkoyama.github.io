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
from common import assert_frozen,matmul
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
    kinds=['NH','NHC3','Berendsen','rescale'];fig,ax=plt.subplots(2,2,figsize=(10,7.8))
    for aa,kind,color in zip(ax.flat,kinds,COLORS):
        d=s.data('NH-stat-0.2-'+kind+'-1.0-0.05');z=d['state'][1]
        aa.scatter(z[:256,0],z[:256,2],s=8,alpha=.55,color=color,label='Canonical start (256)')
        aa.scatter(z[256:,0],z[256:,2],s=8,alpha=.45,color='gray',label='Heated start (128)')
        aa.set(xlabel='Position q1',ylabel='Momentum p1',title=kind+': saved state at t=20');aa.legend(fontsize=7)
    finish(fig,out,'deterministic-thermostat-contrasts.png')
    fig,ax=plt.subplots(1,2,figsize=(11.2,4.6));variances=[]
    for kind,color in zip(kinds,COLORS):
        d=s.data('NH-stat-0.2-'+kind+'-1.0-0.05');z=d['state'][1,:256];K=.5*np.sum(z[:,2:4]**2,axis=1)
        ecdf(ax[0],K,kind,color);variances.append(np.var(K,ddof=1))
        row=s.meta('NH-stat-0.2-'+kind+'-1.0-0.05');lag=row['diagnostics'][0]['lags']
        xx=[a['lag'] for a in lag];yy=[np.nan if a['K']['correlation'] is None else a['K']['correlation'] for a in lag]
        ax[1].plot(xx,yy,'o-',label=kind,color=color)
    ax[0].set(xlabel='Kinetic energy K',ylabel='Empirical CDF',title='256 canonical-start replicas');ax[0].legend(fontsize=8)
    ax[1].set(xlabel='Lag from time20',ylabel='Centered K correlation',title='Finite-time ensemble correlations');ax[1].legend(fontsize=8)
    fig.suptitle('Quartic=0.2,tau=1,h=0.05; time20 is not a mixing proof',fontsize=11)
    finish(fig,out,'deterministic-thermostat-contrasts-diagnostics.png')
    from fractions import Fraction
    refs=s.meta('constraints-components')['rational_fixtures'];fig,ax=plt.subplots(2,4,figsize=(13.2,6.5))
    for j,config in enumerate(['none','COM','COM-relative','redundant']):
        d=s.data('constraints-'+str(j)+'-Langevin-0.05');p=d['ambient_p'];centered=p-np.mean(p,axis=0);cov=matmul(centered.T,centered)/(len(p)-1)
        truth=np.array([[float(Fraction(x)) for x in row] for row in refs[j]['Fraction_covariance']])
        im=ax[0,j].imshow(cov,cmap='RdBu_r',vmin=-3,vmax=3);ax[0,j].set(title=config+'(f='+str([3,2,1,1][j])+')',xticks=[0,1,2],yticks=[0,1,2]);fig.colorbar(im,ax=ax[0,j],fraction=.05)
        delta=cov-truth;im=ax[1,j].imshow(delta,cmap='RdBu_r',vmin=-.3,vmax=.3);ax[1,j].set(xticks=[0,1,2],yticks=[0,1,2]);fig.colorbar(im,ax=ax[1,j],fraction=.05)
    ax[0,0].set_ylabel('Saved momentum covariance');ax[1,0].set_ylabel('Sample minus exact law');fig.suptitle('Langevin,h=0.05,t=4; independent 1024-replica ensembles',fontsize=11)
    finish(fig,out,'projected-canonical-dof.png')
    fig,ax=plt.subplots(1,2,figsize=(11.2,4.6))
    for j,config in enumerate(['none','COM','COM-relative','redundant']):
        d=s.data('constraints-'+str(j)+'-Langevin-0.05');f=[3,2,1,1][j];K=.5*np.sum(d['state'][-1,:,f:]**2,axis=1)
        ecdf(ax[0],K,config,COLORS[j]);row=s.meta('constraints-'+str(j)+'-Langevin-0.05');diags=row['diagnostics']
        ax[0].plot([.25,.5,1,2,4],diags[-1]['reference']['K_CDF'],'x',color=COLORS[j])
        ax[1].plot([r['time'] for r in diags],[r['temperature_actual_f'] for r in diags],'o-',label=config+' correct f',color=COLORS[j])
        ax[1].plot([r['time'] for r in diags],[r['temperature_wrong_ambient3'] for r in diags],ls=':',color=COLORS[j])
    ax[0].set(xlabel='Kinetic energy K',ylabel='CDF',title='Saved ECDF and finite-time Gaussian law');ax[0].legend(fontsize=8)
    ax[1].axhline(1,color='black',lw=.9);ax[1].set(xlabel='Time',ylabel='2 mean(K)/DOF',title='Correct DOF (solid), ambient3 (dotted)');ax[1].legend(fontsize=7)
    finish(fig,out,'projected-canonical-dof-diagnostics.png')

def main():
    p=argparse.ArgumentParser();p.add_argument('--results',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    assert_frozen(Path(__file__).resolve().parent);out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
    saved=Saved(a.results);figures(saved,out)
    names=sorted(x.name for x in out.glob('*.png'))
    (out/'figure-index.json').write_text(json.dumps({'source_result':Path(a.results).name,'figures':names,'solver_calls':0},indent=2)+'\n')
if __name__=='__main__':main()
