"""Plot saved measured results; the plotting dependency is optional for execution."""
import argparse
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def figures(path,destination):
    result=json.loads(path.read_text());destination.mkdir(parents=True,exist_ok=True)
    fig,axes=plt.subplots(1,2,figsize=(11.2,5.7),layout='constrained')
    for basis in ['sto-3g','nested-s-8']:
        rows=[r for r in result['cases'] if r['basis_id']==basis]
        axes[0].plot([r['bond_bohr'] for r in rows],[r['energy_total'] for r in rows],'o-',label=basis)
    axes[0].set(title='Three sampled H2 geometries (RHF)',xlabel='Bond length (bohr)',ylabel='Total energy (hartree)')
    for row in result['basis_refinement']:
        axes[1].semilogy(list(range(3,9)),[abs(v) for v in row['energy_changes']],'o-',label='R='+str(row['bond_bohr'])+' bohr')
    axes[1].axhline(result['basis_refinement'][0]['target'],color='black',ls='--',label='Finite-s target (last TWO steps)')
    axes[1].set(title='Nested s-subspace increments; not CBS error',xlabel='s functions per H',ylabel='Absolute adjacent energy change (hartree)')
    for ax in axes:ax.grid(alpha=.2);ax.legend(fontsize=9)
    fig.savefig(destination/'preview.png',dpi=100);plt.close(fig)
    row=next(r for r in result['cases'] if r['bond_bohr']==1.4 and r['basis_id']=='nested-s-8')
    fig,ax=plt.subplots(figsize=(9.6,5.7),layout='constrained')
    ax.semilogy([t['iteration'] for t in row['trace']],[max(abs(t['energy_total']-row['energy_total']),1e-16) for t in row['trace']],label='Energy difference to final same-run value')
    ax.semilogy([t['iteration'] for t in row['trace']],[max(t['scf_commutator_norm'],1e-16) for t in row['trace']],label='Orthonormal commutator norm')
    ax.set(title='H2 R=1.4 bohr, nested8s/H: SCF convergence',xlabel='SCF iteration',ylabel='Measured convergence diagnostic')
    ax.grid(alpha=.2);ax.legend();fig.savefig(destination/'scf.png',dpi=100);plt.close(fig)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();figures(a.input,a.output)
