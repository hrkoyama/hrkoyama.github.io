"""Plot measured periodic DFT sweeps; optional matplotlib dependency."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--input',type=Path,required=True)
p.add_argument('--output',type=Path,required=True)
a=p.parse_args();r=json.loads(a.input.read_text())
indexed={c['id']:c for c in r['cases']}
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(2,3,figsize=(13,7.5),layout='constrained')
fig.suptitle('Periodic KS-LDA: artificial He cell, a = 4 bohr\nPySCF Gaussian driver and independent DFTK plane-wave reference',fontsize=15)
for ax,name,title in zip(axes.flat[:3],['kpoint','basis','auxiliary'],['k-point sampling','Gaussian orbital basis','Auxiliary FFT / XC grid']):
    c=r['convergence'][name];rows=[indexed[i] for i in c['case_ids']]
    energies=np.asarray(c['energies_per_cell'])
    labels=([str(row['k_n']) for row in rows] if name=='kpoint' else [row['basis'].replace('gth-','').upper() for row in rows] if name=='basis' else [str(row['fft_mesh'][0]) for row in rows])
    ax.plot(range(len(rows)),(energies-energies[-1])*1000,'o-',color='#176a89')
    ax.axhline(0,color='gray',linewidth=.6)
    ax.set_xticks(range(len(rows)),labels)
    ax.set(title=title+'\nLast change: %.4g mEh'%(c['last_change']*1000),xlabel={'kpoint':'N in N x N x N mesh','basis':'Non-nested GTH basis family','auxiliary':'Grid points per direction'}[name],ylabel='E - last E (mEh / cell)')
ax=axes[1,0]
rows=[indexed[i] for i in r['convergence']['scf']['case_ids']]
ax.semilogy(range(3),[row['scf_commutator_norm'] for row in rows],'o-',color='#176a89')
ax.set_xticks(range(3),['loose','medium','tight'])
ax.set(title='SCF tolerance at fixed basis and mesh',xlabel='SCF tolerance setting',ylabel='Final orthogonalized commutator norm')
ax=axes[1,1]
records=r['independent_comparison']['cutoff_convergence']['records']
for n in [1,2]:
    subset=sorted([x for x in records if x['k_n']==n],key=lambda x:x['ecut_hartree'])
    ax.semilogy([x['ecut_hartree'] for x in subset[:-1]],[abs(x['energy_per_cell']-subset[-1]['energy_per_cell'])*1e6 for x in subset[:-1]],'o-',label='Gamma' if n==1 else '2 x 2 x 2')
ax.set(title='Independent DFTK cutoff sweep',xlabel='Plane-wave cutoff (Ha)',ylabel='|E - E(240 Ha)| (microEh / cell)');ax.legend()
ax=axes[1,2]
comparisons=r['independent_comparison']['cases']
ax.bar(['Gamma','2 x 2 x 2'],[c['absolute_difference']*1e6 for c in comparisons],color=['#176a89','#dc8f31'])
ax.set(title='Independent engine agreement',ylabel='|E(PySCF) - E(DFTK)| (microEh / cell)')
ax.set_ylim(0,max(c['absolute_difference']*1e6 for c in comparisons)*1.5)
ax.text(.04,.95,'Same physical model; finite bases differ.\nNo fitted energy offset.\nUnoccupied bands are not converged.',transform=ax.transAxes,va='top',fontsize=8)
fig.supxlabel('Per-cell ground-state energy tests; finite refinement increments are not rigorous error bounds.',fontsize=10)
a.output.mkdir(parents=True,exist_ok=True)
fig.savefig(a.output/'preview.png',dpi=150)
plt.close(fig)
