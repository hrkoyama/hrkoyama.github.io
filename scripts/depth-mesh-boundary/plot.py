import argparse,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

def finish(fig,out,ident):
    for ext in ['png','svg','pdf']:fig.savefig(out/(ident+'.'+ext),dpi=150)
    fig.savefig(out/(ident+'-preview.png'),dpi=80);plt.close(fig)

def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True);base=a.results.parent;cases=json.loads(a.results.read_text())['cases'];plt.rcParams.update({'font.size':10})
    for c in cases:
        ident=c['id'];rows=c['records'];fig,ax=plt.subplots(2,2,figsize=(12,7.8),layout='constrained');n=max(r['n'] for r in rows)
        if ident=='lshape-fem':
            for axes,family in zip(ax[0],['uniform','graded']):
                d=np.load(base/(ident+'-'+family+'-n'+str(n)+'.npz'));t=tri.Triangulation(*d['points'].T,d['cells']);im=axes.tripcolor(t,d['u'],shading='gouraud');fig.colorbar(im,ax=axes);axes.triplot(t,color='k',lw=.12,alpha=.4);axes.set(aspect='equal',xlabel='x',ylabel='y',title=family+' P1 mesh and computed singular field')
            for family in ['uniform','graded']:
                seq=[r for r in rows if r['family']==family];ax[1,0].loglog([r['dofs'] for r in seq],[r['h1'] for r in seq],'o-',label=family+' H1');ax[1,0].loglog([r['dofs'] for r in seq],[r['l2'] for r in seq],'s--',label=family+' L2')
            ax[1,0].legend();ax[1,0].set(xlabel='matched free unknowns',ylabel='integrated error',title='Graded versus uniform, singular quadrature checked')
            for family in ['square','warped']:
                seq=[r for r in rows if r['family']==family];ax[1,1].loglog([r['n'] for r in seq],[r['condition_one_norm_estimate'] for r in seq],'o-',label=family)
            ax[1,1].legend();ax[1,1].set(xlabel='square-grid divisions',ylabel='estimated 1-norm condition',title='Separate smooth square/warped-mesh diagnostic')
        elif ident=='annular-viscous-mms':
            d=np.load(base/(ident+'-annulus-n'+str(n)+'.npz'));X=np.column_stack((d['x'],d['x'][:,0]));Y=np.column_stack((d['y'],d['y'][:,0]));speed=np.linalg.norm(d['u'],axis=-1);error=np.linalg.norm(d['u']-d['reference'],axis=-1)
            for axes,value,title in [(ax[0,0],speed,'Actual 2D annular vector solution'),(ax[0,1],error,'Nodal velocity error vs manufactured field')]:
                value=np.column_stack((value,value[:,0]));im=axes.pcolormesh(X,Y,value,shading='gouraud');fig.colorbar(im,ax=axes);axes.set(aspect='equal',xlabel='x',ylabel='y',title=title)
            ax[0,0].quiver(d['x'][::3,::3],d['y'][::3,::3],d['u'][::3,::3,0],d['u'][::3,::3,1],color='k',alpha=.7)
            for key in ['relative_l2','relative_strain_l2','relative_traction_l2']:ax[1,0].loglog([r['n'] for r in rows],[r[key] for r in rows],'o-',label=key)
            ax[1,0].legend(fontsize=8);ax[1,0].set(xlabel='radial cells',ylabel='relative L2',title='Velocity / strain / boundary traction refinement')
            for key in ['traction_flux_balance','reaction_balance','work_identity']:ax[1,1].semilogy([r['n'] for r in rows],[max(r[key],1e-17) for r in rows],'o-',label=key)
            ax[1,1].legend(fontsize=8);ax[1,1].set(xlabel='radial cells',ylabel='relative budget residual',title='Physical traction versus algebraic reaction/work')
        else:
            family='neumann' if ident=='poisson-neumann' else 'robin';d=np.load(base/(ident+'-'+family+'-n'+str(n)+'.npz'))
            for axes,value,title in [(ax[0,0],d['u'],'Actual 2D Poisson solution'),(ax[0,1],d['u']-d['reference'],'Error vs manufactured point values')]:
                im=axes.imshow(value,origin='lower',extent=[0,1,0,1],cmap='RdBu_r');fig.colorbar(im,ax=axes);axes.set(xlabel='x',ylabel='y',title=title)
            ax[1,0].loglog([r['n'] for r in rows],[r['l2'] for r in rows],'o-');ax[1,0].set(xlabel='cells per side',ylabel='RMS error',title='Fixed boundary-value refinement')
            if family=='neumann':
                gauge=np.load(base/(ident+'-gauge-shift.npz'));gap=gauge['shifted']-gauge['zero_mean']-.25
                im=ax[1,1].imshow(gap,origin='lower',extent=[0,1,0,1],cmap='RdBu_r');fig.colorbar(im,ax=ax[1,1]);ax[1,1].set(xlabel='x',ylabel='y',title='Mean .25 probe: shift minus exact constant')
            else:
                faces=d['face_records'];error=d['normal_gradient']-faces[:,6];k=faces[:,0].astype(int)
                for mask,coord,label in [(faces[:,1]==-1,k//n,'left Neumann'),(faces[:,1]==1,k//n,'right Neumann'),(faces[:,2]==-1,k%n,'bottom Robin'),(faces[:,2]==1,k%n,'top Robin')]:
                    j=np.flatnonzero(mask);j=j[np.argsort(coord[j])];ax[1,1].plot((coord[j]+.5)/n,error[j],label=label)
                ax[1,1].legend(fontsize=8);ax[1,1].set(xlabel='coordinate along boundary',ylabel='outward-gradient error',title='Physical flux error on each boundary')
        fig.suptitle(ident+' | fixed-input PDE validation',fontsize=14);finish(fig,a.output,ident)
if __name__=='__main__':main()
