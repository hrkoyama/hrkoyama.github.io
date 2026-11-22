"""Optional summary figure from an already completed numerical result."""
import argparse,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    p=argparse.ArgumentParser();p.add_argument('--result',type=Path,default=Path('results/result.json'));p.add_argument('--output',type=Path,default=Path('results/preview.png'));a=p.parse_args();r=json.loads(a.result.read_text())
    fig,axes=plt.subplots(1,3,figsize=(12,3.7),layout='constrained')
    for name in ['kpoint','basis','basis-k2','auxiliary','scf']:
        c=r['convergence'][name];axes[0].semilogy(range(1,len(c['adjacent_changes'])+1),c['adjacent_changes'],'o-',label=name)
    axes[0].set(xlabel='Refinement index',ylabel='Max force increment [Eh/bohr]',title='Independent convergence sweeps');axes[0].legend(fontsize=8)
    fd=r['finite_difference']['components'];axes[1].plot(range(6),[c['force_analytic'] for c in fd],'o',label='PySCF analytic');axes[1].plot(range(6),[c['force_finite_difference'] for c in fd],'+',label='Energy finite difference');axes[1].set(xticks=range(6),xticklabels=['0x','0y','0z','1x','1y','1z'],ylabel='Force [Eh/bohr]',title='All Cartesian components');axes[1].legend(fontsize=8)
    for c in r['independent_comparison']['cases']:
        errors=[abs(p-q) for ps,qs in zip(c['pyscf_forces_cartesian'],c['dftk_forces_cartesian']) for p,q in zip(ps,qs)]
        axes[2].semilogy(range(6),errors,'o-',label='k='+str(c['k_n'])+'^3')
    axes[2].set(xticks=range(6),xticklabels=['0x','0y','0z','1x','1y','1z'],ylabel='Absolute force difference [Eh/bohr]',title='Gaussian / plane-wave comparison');axes[2].legend(fontsize=8)
    a.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(a.output,dpi=140);plt.close(fig)
if __name__=='__main__':main()
