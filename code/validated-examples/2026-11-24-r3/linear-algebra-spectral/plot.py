"""Saved matrix/eigenvector/error data only; no solver/reference execution."""
from pathlib import Path
import argparse,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def load(directory,row):
    with np.load(directory/row['fields'],allow_pickle=False) as f:return {k:f[k] for k in f.files}


def save(fig,out,name):
    for ext in ['png','svg','pdf']:fig.savefig(out/(name+'.'+ext),dpi=145,bbox_inches='tight')
    plt.close(fig)


def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();d=a.results.parent if a.results.is_file() else a.results;result=json.loads((d/'result.json').read_text());assert result['passed'];a.output.mkdir(parents=True,exist_ok=True)
    title_by_id={row['id']:row['title']['en'] for row in json.loads((Path(__file__).resolve().parent/'cases.json').read_text())}
    for c in result['cases']:
        fig,axes=plt.subplots(1,2,figsize=(10.4,4.2));rows=c['records'];ident=c['id']
        if ident=='pivoted-direct-refinement':
            row=next(x for x in rows if x['matrix']=='hilbert5' and x['factorization']=='lu');z=load(d,row);im=axes[0].imshow(z['a'],cmap='viridis');axes[0].set(title='Hilbert matrix (5 x 5)',xlabel='Column',ylabel='Row');fig.colorbar(im,ax=axes[0])
            for row in rows:
                z=load(d,row);errors=np.sqrt(np.sum((z['history']-z['exact'])**2,axis=1))/np.sqrt(np.sum(z['exact']**2));axes[1].semilogy(np.arange(len(errors)),np.maximum(errors,np.finfo(float).tiny),'.-',label=row['id'])
            axes[1].set(title='Actual mixed-precision correction history',xlabel='Fixed correction index',ylabel='Relative L2 error / rounded reference')
        elif ident=='symmetric-saddle-minres':
            row=max(rows,key=lambda r:r['size']);z=np.load(d/('saddle-24-inputs.npz'),allow_pickle=False);im=axes[0].imshow(z['a'],cmap='coolwarm');axes[0].set(title='Actual symmetric saddle matrix',xlabel='Column',ylabel='Row');fig.colorbar(im,ax=axes[0]);z.close()
            for row in rows:
                z=load(d,row);axes[1].semilogy(np.arange(1,len(z['history'])+1),z['history'],'.-',label=row['id'])
            axes[1].set(title='Same unpreconditioned stopping residual',xlabel='Projected matrix actions',ylabel='||b-Ax|| / ||b||')
        elif ident=='restarted-shift-invert':
            with np.load(d/'reference-laplacian.npz',allow_pickle=False) as f:im=axes[0].imshow(f['a'],cmap='coolwarm');fig.colorbar(im,ax=axes[0])
            axes[0].set(title='Dirichlet Laplacian (31 x 31)',xlabel='Column',ylabel='Row')
            for row in rows:
                z=load(d,row);h=z['history'];axes[1].semilogy(h[:,4],h[:,3],'.-',label=row['id'])
            axes[1].set(title='Original eigenproblem residual',xlabel='Krylov operator actions (A or shift solves)',ylabel='Normalized residual')
        else:
            row=next(r for r in rows if r['interior_nodes']==63 and r['method']=='mass-Krylov');z=load(d,row);gram=np.einsum('ij,jk,kl->il',z['vectors'].T,z['m'],z['vectors'],optimize=False);im=axes[0].imshow(gram-np.eye(3),cmap='coolwarm');fig.colorbar(im,ax=axes[0]);axes[0].set(title='Actual M-orthogonality defect',xlabel='Mode',ylabel='Mode')
            for j in range(3):axes[1].plot(z['x'],z['vectors'][:,j],label=f'M-normalized mode {j+1}')
            axes[1].set(title='Actual consistent-mass FEM eigenvectors',xlabel='Physical string coordinate x',ylabel='Eigenvector; arbitrary sign')
        axes[1].legend(fontsize=6);axes[1].grid(alpha=.2);fig.suptitle(title_by_id[ident]);fig.tight_layout()
        if ident=='pivoted-direct-refinement':
            fig.text(.5,.01,'Reference: exact Fraction solve rounded to binary64.\nExact zero errors are shown at float64.tiny for log display only.',ha='center',va='bottom',fontsize=7)
            fig.tight_layout(rect=(0,.12,1,1))
        save(fig,a.output,ident)
        # Same scientific panels, separately named gallery preview.
        fig,ax=plt.subplots(figsize=(6.4,4.2))
        if ident=='fem-mass-eigen':
            for j in range(3):ax.plot(z['x'],z['vectors'][:,j],label=f'mode {j+1}')
            ax.set(xlabel='String coordinate',ylabel='M-normalized eigenvector');ax.legend()
        else:
            if ident=='pivoted-direct-refinement':matrix=load(d,rows[0])['a']
            else:
                filename='saddle-24-inputs.npz' if ident=='symmetric-saddle-minres' else 'reference-laplacian.npz'
                with np.load(d/filename,allow_pickle=False) as f:matrix=f['a']
            fig.colorbar(ax.imshow(matrix,cmap='coolwarm'),ax=ax);ax.set(xlabel='Column',ylabel='Row')
        ax.set_title(title_by_id[ident]+' — saved data');fig.tight_layout();save(fig,a.output,ident+'-preview')
if __name__=='__main__':main()
