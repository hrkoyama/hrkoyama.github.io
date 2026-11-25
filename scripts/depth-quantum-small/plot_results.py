"""DRAFT: render only saved data/fields after the frozen scientific run."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from io_utils import dot

ROOT=Path(__file__).resolve().parent


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--results',required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
    source_result=Path(args.results)
    if not source_result.is_file():source_result=source_result/'result.json'
    source_result_sha256=hashlib.sha256(source_result.read_bytes()).hexdigest()
    base=source_result.parent
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    cards=json.loads((ROOT/'cards.json').read_text())['cards']
    filenames={card['sequence']:card['id']+'.png' for card in cards}
    read=lambda n:json.loads((base/(n+'.json')).read_text())
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'#faf9f6','axes.facecolor':'#faf9f6'})
    def finish(fig,filename,title):
        target=out/filenames[int(filename.split('-')[0])]
        if target.exists():raise FileExistsError('Refuse to overwrite figure '+str(target))
        fig.suptitle(title,fontsize=13);fig.tight_layout(rect=[0,0,1,.94]);fig.savefig(target,dpi=160);plt.close(fig)
    md=read('95-result');fig,axes=plt.subplots(1,2,figsize=(10,4))
    for ident,label in [('bo-2','Analytic BO surface'),('cp-mu004-2','CP-type mu=0.04'),('cp-mu001','CP-type mu=0.01')]:
        row=next(x for x in md['runs'] if x['id']==ident);tr=row['trajectory'];q=[x['state'][0] for x in tr];v=[x['state'][1] for x in tr]
        axes[0].plot(q,v,label=label);e0=tr[0]['extended_energy'];axes[1].plot([x['time'] for x in tr],[x['extended_energy']-e0 for x in tr],label=label)
    thermal=md['thermal'];e0=thermal[0]['extended_energy']
    axes[1].plot([x['time'] for x in thermal],[x['extended_energy']-e0-x['bath_heat'] for x in thermal],ls='--',label='CP + OU: E - heat')
    axes[0].set(xlabel='Nuclear Q',ylabel='Nuclear velocity',title='Actual short coupled trajectories');axes[1].set(xlabel='Time',ylabel='Extended energy change (heat corrected)',title='NVE and measured nuclear-bath heat')
    for ax in axes:ax.legend(fontsize=8);ax.grid(alpha=.2)
    finish(fig,'95-two-state-bo-cp-ou.png','Two-state educational BO / CP-type dynamics; no equilibration claim')
    atom=read('96-result');fig,axes=plt.subplots(1,2,figsize=(10,4));rows=atom['cases']
    axes[0].bar(['HF\n40 s','LDA_X\n250 x 110','LDA_X\n500 x 194'],[x['energy'] for x in rows],color=['#234e70','#cb763b','#cb763b'])
    axes[0].set(ylabel='Saved total energy (hartree)',title='Different finite-basis models; not correlated exact He')
    delta=rows[1]['energy']-rows[2]['energy'];axes[1].bar(['Stored LDA_X grid difference'],[delta],color='#cb763b');axes[1].ticklabel_format(axis='y',style='sci',scilimits=(0,0));axes[1].set(ylabel='Saved coarse minus fine energy (hartree)',title='3 stored rows, each with 40 basis functions')
    finish(fig,'96-atomic-reference-cards.png','Immutable H/He reference cards: saved He values, no SCF rerun')
    eig=read('97-result')['rows'];fig,axes=plt.subplots(1,2,figsize=(10,4))
    for ax,row in zip(axes,[next(x for x in eig if x['id']=='box-M128'),next(x for x in eig if x['model']=='HO' and x['M']==256)]):
        for pair in row['pairs']:
            line=ax.plot(row['x'],pair['u'],label='FD state '+str(pair['state']))[0]
            raw=np.array(pair['analytic_raw']);sign=1 if dot(np.array(pair['u']),raw)>=0 else -1
            ax.plot(row['x'],sign*raw,ls='--',color=line.get_color(),alpha=.6)
        ax.set(xlabel='x (declared atomic units)',ylabel='Wavefunction',title=row['id']+'; dashed continuum formula');ax.legend(fontsize=8);ax.grid(alpha=.2)
    finish(fig,'97-box-ho-eigenpairs.png','Low three stationary eigenpairs on each actual finite Dirichlet domain')
    mol=read('98-99-result');h2=mol['H2'];fig,axes=plt.subplots(1,2,figsize=(10,4))
    for method in ['RHF','UHF','FCI']:axes[0].plot([x['bond'] for x in h2],[x[method]['energy'] for x in h2],'o--',label=method)
    axes[0].set(xlabel='H-H distance (bohr)',ylabel='Total energy (hartree)',title='Two fixed geometries; lines guide the eye');axes[0].legend()
    axes[1].bar([str(x['bond']) for x in h2],[x['UHF']['spin_square'] for x in h2],color='#a94a3f');axes[1].set(xlabel='H-H distance (bohr)',ylabel='UHF <S^2>',title='Broken-spin determinant diagnostic')
    finish(fig,'98-h2-rhf-uhf-fci.png','Same explicit minimal H basis: finite-basis correlation and symmetry breaking')
    h3=mol['H3plus'];config=json.loads((ROOT/'inputs.json').read_text());shell=config['molecule98']['basis']['shells'][0]
    aa=np.array(shell['exponents']);ww=np.array(shell['coefficients'])*(2*aa/math.pi)**.75
    nn=sum(ww[i]*ww[j]*(math.pi/(a+b))**1.5 for i,a in enumerate(aa) for j,b in enumerate(aa));ww/=math.sqrt(nn)
    xx=np.linspace(-1,2.5,101);yy=np.linspace(-1,2.5,101);X,Y=np.meshgrid(xx,yy);orbital=np.zeros_like(X)
    for center,coefficient in zip(h3['geometry'],np.array(h3['RHF']['C'])[:,0]):
        r2=(X-center[0])**2+(Y-center[1])**2+center[2]**2
        orbital+=coefficient*sum(w*np.exp(-a*r2) for a,w in zip(aa,ww))
    fig,axes=plt.subplots(1,2,figsize=(10,4));image=axes[0].pcolormesh(X,Y,2*orbital**2,shading='auto',cmap='magma');fig.colorbar(image,ax=axes[0],label='RHF n(x,y,z=0), bohr^-3')
    pos=np.array(h3['geometry']);axes[0].scatter(pos[:,0],pos[:,1],c='cyan',edgecolors='black');axes[0].set(xlabel='x (bohr)',ylabel='y (bohr)',title='Actual 3-center orbital-density slice',aspect='equal')
    reference=h3['RHF']['energy'];axes[1].bar(['RHF','MP2','FCI'],[0,h3['MP2_energy']-reference,h3['FCI']['energy']-reference],color=['#234e70','#cb763b','#4e766d']);axes[1].set(ylabel='Energy minus RHF (hartree)',title='Two electrons, three s orbitals, one geometry')
    finish(fig,'99-h3plus-mp2-fci.png','Tiny H3+ molecular correlation example; no general DFT/CC claim')
    he=read('100-result');fig,axes=plt.subplots(1,2,figsize=(10,4));fd=he['finite_difference']['components'];indices=np.arange(6)
    axes[0].bar(indices,[x['absolute_error'] for x in fd],color='#234e70');axes[0].axhline(he['acceptance_unchanged']['finite_difference_max_error'],ls='--',color='black',label='Original bound');axes[0].set(yscale='log',xticks=indices,xticklabels=['0x','0y','0z','1x','1y','1z'],ylabel='Saved absolute force error (hartree/bohr)',title='Analytic vs finite difference, same Gaussian case');axes[0].legend(fontsize=8)
    row=he['independent_cases'][0];error=abs(np.array(row['pyscf_forces_cartesian'])-np.array(row['dftk_forces_cartesian'])).ravel();axes[1].bar(indices,error,color='#cb763b');axes[1].axhline(row['force_acceptance'],ls='--',color='black',label='Original bound');axes[1].set(yscale='log',xticks=indices,xticklabels=['0x','0y','0z','1x','1y','1z'],ylabel='Saved force difference (hartree/bohr)',title='Independent Gaussian / PW, fixed Gamma cell');axes[1].legend(fontsize=8)
    finish(fig,'100-periodic-he-reference-audit.png','Immutable displaced-He cell reference audit; no electronic rerun')
    pw=read('101-result')['center'];fig,axes=plt.subplots(1,2,figsize=(10,4));row=pw['rows'][1]
    beta=np.array([complex(z['real'],z['imag']) for z in row['projector_beta']]);kernel=config['periodic101']['projector_eta']*abs(np.outer(beta,beta.conj()))
    image=axes[0].imshow(kernel,origin='lower',cmap='viridis');fig.colorbar(image,ax=axes[0],label='|eta beta_G beta_G\' *|');axes[0].set(xticks=[0,1,2],xticklabels=['-1','0','1'],yticks=[0,1,2],yticklabels=['-1','0','1'],xlabel="G'",ylabel='G',title='Actual rank-one nonlocal kernel, k=0.25')
    for i,row in enumerate(pw['rows']):axes[1].plot(row['energies'],pw['thermo']['f'][i],'o--',label='k='+str(row['k']))
    axes[1].axvline(pw['thermo']['mu'],ls=':',color='black',label='Chemical potential');axes[1].set(xlabel='Band energy (model units)',ylabel='Fermi occupation, spin factor 2',ylim=[-.05,2.05],title='Fixed mean N=1.5, T=0.05, two k points');axes[1].legend(fontsize=8)
    finish(fig,'101-projector-fermi-occupations.png','Three-wave periodic educational model; no real-metal validation')
    (out/'plot-manifest.json').write_text(json.dumps({'source_results':source_result.name,'source_results_sha256':source_result_sha256,'plots':sorted(x.name for x in out.glob('*.png')),'scope':'Saved numerical arrays/analytic field evaluation only; no eigensolve or SCF rerun.'},indent=2)+'\n')


if __name__=='__main__':main()
