"""Saved arrays only; no solver calls or analytic-reference regeneration."""
import argparse,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    folder=a.results.parent if a.results.is_file() else a.results;result=json.loads((folder/'result.json').read_text())
    if not result['passed']:raise ValueError('Accepted saved result required')
    a.output.mkdir(parents=True,exist_ok=True)
    mode_labels={0:'analytic',1:'FD',2:'AD'};branch_labels={0:'lower',1:'upper'}
    for c in result['cases']:
        ident=c['id'];fig,ax=plt.subplots(2,2,figsize=(11,8),layout='constrained')
        if ident=='bratu-fold-continuation':
            for row in c['records']:
                n=row['n'];z=np.load(folder/(ident+'-N'+str(n)+'.npz'));states=z['states'];mid=states[:,n//2]
                ax[0,0].plot(states[:,-1],mid,label='FD N='+str(n))
                ax[1,0].semilogy(np.arange(len(states)),z['sigma_path'],label='N='+str(n))
            ax[0,0].plot(z['path_exact_lambda'],mid,'k--',label='family at matched midpoint')
            x=z['reference_x'];ax[0,1].plot(x,np.r_[0,z['lower'],0],label='lower FD');ax[0,1].plot(x,z['exact_lower'],'--',label='lower exact')
            ax[0,1].plot(x,np.r_[0,z['upper'],0],label='upper FD');ax[0,1].plot(x,z['exact_upper'],'--',label='upper exact')
            ax[1,1].loglog([1/(r['n']+1) for r in c['records']],[r['fold_error'] for r in c['records']],'o-',label='discrete vs continuum fold')
            ax[0,0].set(xlabel='lambda',ylabel='u(1/2)',title='Pseudo-arclength branch')
            ax[0,1].set(xlabel='x',ylabel='u',title='Independent fixed-lambda=2 profiles')
            ax[1,0].set(xlabel='arc step (not physical time)',ylabel='sigma_min(J)',title='Jacobian singularity along branch')
            ax[1,1].set(xlabel='h',ylabel='absolute fold-lambda error',title='Fixed three-grid refinement')
        else:
            for row in c['records']:
                trace=np.atleast_1d(np.genfromtxt(folder/(ident+'-run'+str(row['run'])+'-newton.csv'),delimiter=',',names=True))
                if row['n']==127:ax[0,0].semilogy(trace['iteration'],trace['residual'],label=mode_labels[row['mode_code']]+'/'+branch_labels[row['branch_code']])
            fine=c['records'][-2];z=np.load(folder/(ident+'-run'+str(fine['run'])+'.npz'));ax[0,1].plot(z['reference_x'],np.r_[0,z['u'],0],label='FD BVP');ax[0,1].plot(z['reference_x'],z['exact'],'--',label='analytic branch')
            q=np.load(folder/(ident+'-Jv-qualification.npz'));den=np.sqrt(np.sum(q['analytic']**2));errors=[np.sqrt(np.sum((q[k]-q['analytic'])**2))/den for k in ['ad','central_fd']]
            ax[1,0].bar(['forward AD','central FD'],errors);ax[1,0].set_yscale('symlog',linthresh=1e-16)
            ax[1,1].bar([r['run'] for r in c['records']],[r['primal_residual']+r['dual_residual'] for r in c['records']])
            ax[0,0].set(xlabel='Newton step',ylabel='discrete residual L2',title='Newton residuals (N=127)')
            ax[0,1].set(xlabel='x',ylabel='u',title='Finest upper branch')
            ax[1,0].set(ylabel='relative Jv error',title='Saved independent derivative qualification')
            ax[1,1].set(xlabel='fixed run index (last: constant eta)',ylabel='primal + dual traversals',title='Recorded evaluations, not a timing speedup')
        for axis in ax.flat:axis.grid(alpha=.2)
        for axis in ax.flat:
            if axis.get_legend_handles_labels()[0]:axis.legend(fontsize=7)
        fig.suptitle('Bratu: continuation through the fold' if ident=='bratu-fold-continuation' else 'Bratu: matrix-free Newton-Krylov')
        for suffix in ['.png','.svg','.pdf']:
            fig.savefig(a.output/(ident+suffix),dpi=150);fig.savefig(a.output/(ident+'-preview'+suffix),dpi=100)
        plt.close(fig)


if __name__=='__main__':main()
