"""Visuals from actual saved fields; no AD, implicit solve or reference rerun."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def save(fig,output,ident):
    for ext in ['png','svg','pdf']:
        path=output/(ident+'.'+ext)
        if path.exists():raise FileExistsError(path)
        fig.savefig(path,dpi=160)
    fig.savefig(output/(ident+'-preview.png'),dpi=90);plt.close(fig)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--results',required=True,type=Path);parser.add_argument('--output',required=True,type=Path);args=parser.parse_args()
    path=args.results/'result.json'if args.results.is_dir()else args.results;data=json.loads(path.read_text());args.output.mkdir(parents=True,exist_ok=True)
    cases={c['id']:c for c in data['cases']}
    case=cases['reverse-vjp-duality'];row=case['records'][0]
    fig,axes=plt.subplots(2,2,figsize=(10,7),layout='constrained')
    image=axes[0,0].imshow(np.array(row['oracle_J']),cmap='coolwarm',aspect='auto');fig.colorbar(image,ax=axes[0,0]);axes[0,0].set(title='Independent rectangular Jacobian',xlabel='Input coordinate',ylabel='Output coordinate')
    err=np.abs(np.array(row['J_reverse'])-row['oracle_J']);image=axes[0,1].imshow(err,cmap='magma',aspect='auto',vmin=0,vmax=max(1e-15,float(err.max())));fig.colorbar(image,ax=axes[0,1]);axes[0,1].set(title='Actual reverse Jacobian absolute error',xlabel='Input coordinate',ylabel='Output coordinate')
    rows=[r for r in case['records']if r['id'].startswith('wide')];pos=np.arange(len(rows));width=.35
    axes[1,0].bar(pos-width/2,[r['sweep_counts']['forward_seeds']for r in rows],width,label='Forward seeds',color='#168498');axes[1,0].bar(pos+width/2,[r['sweep_counts']['full_reverse_pullbacks']for r in rows],width,label='Reverse pullbacks',color='#de9436');axes[1,0].set(xticks=pos,xticklabels=[r['id']for r in rows],ylabel='Measured traversals',title='Full Jacobian sweeps; no timing claim');axes[1,0].legend()
    axes[1,1].bar(pos,[r['work_product']['peak_node_array_bytes']for r in rows],color='#587a9b');axes[1,1].set(xticks=pos,xticklabels=[r['id']for r in rows],ylabel='Retained node-array bytes',title='Explicit tape storage, not process RSS')
    fig.suptitle('Reverse VJP and JVP/VJP duality',fontsize=14);save(fig,args.output,case['id'])
    case=cases['hessian-vector-products'];fig,axes=plt.subplots(1,3,figsize=(12,4),layout='constrained')
    for axis,row in zip(axes[:2],[case['records'][0],case['records'][2]]):
        axis.plot(row['Hv'],'o-',ms=3,lw=1,label='Forward over reverse');axis.plot(row['oracle_Hv'],'--',color='#db8f25',label='Independent reference');axis.set(title='Quadratic, size 4'if row['id']=='quadratic4'else'Bratu fixed-state energy, size 31',xlabel='Coordinate',ylabel='Hessian-vector product');axis.legend(fontsize=7);axis.grid(alpha=.2)
    row=case['records'][3];axes[2].bar(['State fixed','Implicit total'],[row['fixed_state_partial'],row['total_curvature']],color=['#168498','#de9436']);axes[2].set(title='Distinct second derivatives at theta = 4',ylabel='Curvature')
    fig.suptitle('HVPs and second-order implicit rules',fontsize=14);save(fig,args.output,case['id'])
    case=cases['kink-branch-derivatives'];fig,axes=plt.subplots(1,3,figsize=(12,4),layout='constrained')
    for kind in ['abs','relu','clip','branch']:
        rows=[r for r in case['records']if r.get('kind')==kind and r.get('direction')==1]
        axes[0].plot([r['x']for r in rows],[r['value']for r in rows],'.-',label=kind)
        for r in rows:
            if r['status']=='NONDIFFERENTIABLE':axes[0].plot(r['x'],r['value'],'o',mfc='white',mec='#333',ms=6)
    axes[0].set(title='Saved values; open markers denote kinks',xlabel='x',ylabel='Function value');axes[0].legend(fontsize=7);axes[0].grid(alpha=.2)
    rows=[r for r in case['records']if r.get('kind')=='stopped'];axes[1].scatter([r['theta']for r in rows],[r['value']for r in rows],c=[r['K']for r in rows],cmap='viridis',s=45);axes[1].set(title='Stopped-map samples, colored by update count',xlabel='theta',ylabel='Returned state');axes[1].grid(alpha=.2)
    pos=np.arange(5);axes[2].bar(pos-.15,[r['frozen_trace_slope']for r in rows],.3,label='Executed trace',color='#168498');axes[2].bar(pos+.15,np.ones(5),.3,label='Converged root',color='#de9436');axes[2].set(xticks=pos,xticklabels=['1/4','1/2','1','1/2 - eps','1/2 + eps'],title='Trace slope is not a derivative at a jump',xlabel='Fixed theta samples',ylabel='Slope');axes[2].tick_params(axis='x',labelsize=7);axes[2].legend(fontsize=7)
    fig.suptitle('Classical, directional and executed-trace derivatives are separate',fontsize=13);save(fig,args.output,case['id'])


if __name__=='__main__':main()
