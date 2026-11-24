"""Render actual saved arrays only; plotting never invokes the kinetic solver."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def field(values,mask):
    result=np.full(mask.shape,np.nan);result[mask.astype(bool)]=values;return result

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--results',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    args.results=args.results.parent if args.results.is_file() else args.results
    result=json.loads((args.results/'result.json').read_text())
    if not result['passed']:raise ValueError('Plot only a fully accepted scientific result')
    args.output.mkdir(parents=True,exist_ok=True)
    for case in result['cases']:
        ident=case['id'];records=case['records'];fig,axes=plt.subplots(2,2,figsize=(11,8),layout='constrained')
        if ident=='lbm-cavity-re100':
            row=records[-1];label=ident+'-N'+str(row['n']);z=np.load(args.results/(label+'.npz'))
            q=np.load(args.results/(label+'-profiles.npz'));mask=z['mask'];u=z['velocity_lattice']/.04
            dx=float(z['dx']);x=(np.arange(mask.shape[1])+.5)*dx;y=(np.arange(mask.shape[0])+.5)*dx
            ux,uy=field(u[0],mask),field(u[1],mask);speed=np.sqrt(ux*ux+uy*uy)
            a=axes[0,0];im=a.pcolormesh(x,y,speed,shading='nearest',rasterized=True,cmap='viridis');a.streamplot(x,y,ux,uy,color='white',density=1)
            a.plot(*q['vortex'],'r.');a.set_title(f"Saved Re100 cavity · N={row['n']}");fig.colorbar(im,ax=a,label='speed / nominal lid')
            omega=np.gradient(uy,dx,axis=1)-np.gradient(ux,dx,axis=0)
            a=axes[0,1];im=a.pcolormesh(x,y,omega,shading='nearest',rasterized=True,cmap='RdBu_r',vmin=-10,vmax=10);a.set_title('Actual vorticity');fig.colorbar(im,ax=a)
            a=axes[1,0];a.plot(q['u'],q['coordinate'],label='LBM u');a.plot(q['u_reference'][:,1],q['u_reference'][:,0],'o',fillstyle='none',label='Ghia u')
            a.plot(q['coordinate'],q['v'],label='LBM v');a.plot(q['v_reference'][:,0],q['v_reference'][:,1],'s',fillstyle='none',label='Ghia v');a.set_title('Nominal-lid centerlines');a.legend(fontsize=8)
            a=axes[1,1];a.loglog([r['n'] for r in records],[r['u_error'] for r in records],'o-',label='u max error');a.loglog([r['n'] for r in records],[r['v_error'] for r in records],'s-',label='v max error');a.set_title('Fixed-Mach grid sensitivity');a.legend()
        elif ident=='lbm-taylor-green':
            z=np.load(args.results/(ident+'-run2.npz'));d=np.load(args.results/(ident+'-run2-diagnostics.npz'))
            mask=z['mask'];n=mask.shape[0];x=(np.arange(n)+.5)*float(z['dx']);y=x
            ux,uy=field(d['u'][0],mask),field(d['u'][1],mask)
            for a,data,title in [(axes[0,0],np.sqrt(ux*ux+uy*uy),'Saved nonlinear Taylor–Green speed'),
                                 (axes[0,1],field(d['p']-d['exact_p'],mask),'Pressure-gauge error')]:
                im=a.pcolormesh(x,y,data,shading='nearest',rasterized=True,cmap='viridis' if a is axes[0,0] else 'RdBu_r');a.set_title(title);fig.colorbar(im,ax=a)
            axes[0,0].quiver(x[::6],y[::6],ux[::6,::6],uy[::6,::6],color='white')
            a=axes[1,0];a.loglog([r['n'] for r in records[:3]],[r['velocity_error'] for r in records[:3]],'o-',label='velocity');a.loglog([r['n'] for r in records[:3]],[r['pressure_error'] for r in records[:3]],'s-',label='pressure');a.set_title('Combined grid/time/Mach refinement');a.legend()
            a=axes[1,1];a.plot(d['snapshot_times'],d['energy'],'o-',label='saved LBM');a.plot(d['snapshot_times'],d['exact_energy'],'--',label='continuum analytic');a.set_title('Mean kinetic energy');a.legend()
        elif ident=='lbm-annular-couette-control':
            row=records[2];label=ident+'-v0-N'+str(row['n']);z=np.load(args.results/(label+'.npz'));d=np.load(args.results/(label+'-diagnostics.npz'));mask=z['mask'];n=mask.shape[0];x=(np.arange(n)+.5)*float(z['dx']);y=x
            speed=np.sqrt(np.sum(d['u']**2,axis=0));error=d['p']-d['exact_p']
            for a,data,title in [(axes[0,0],field(speed,mask),'Saved rotating annulus speed'),(axes[0,1],field(error,mask),'Actual pointwise pressure error')]:
                im=a.pcolormesh(x,y,data,shading='nearest',rasterized=True,cmap='viridis');a.set_title(title);fig.colorbar(im,ax=a)
                for radius in [.2,.4]:a.add_patch(Circle((.5,.5),radius,fill=False,color='white',lw=1))
            for variant,label in [(0,'interpolated'),(1,'stair halfway')]:
                rows=[r for r in records if r['variant']==variant];axes[1,0].loglog([r['n'] for r in rows],[r['velocity_error'] for r in rows],'o-',label=label+' velocity');axes[1,0].loglog([r['n'] for r in rows],[r['pressure_error'] for r in rows],'s--',label=label+' pressure')
                axes[1,1].loglog([r['n'] for r in rows],[r['torque_error'] for r in rows],'o-',label=label)
            axes[1,0].set_title('Actual velocity / pointwise pressure errors');axes[1,1].set_title('Inner resisting torque error');axes[1,0].legend();axes[1,1].legend()
        else:
            row=records[-1];label=ident+'-dx'+str(row['dx']);z=np.load(args.results/(label+'.npz'));d=np.load(args.results/(label+'-diagnostics.npz'));mask=z['mask'];dx=float(z['dx']);x=np.arange(mask.shape[1])*dx;y=(np.arange(mask.shape[0])+.5)*dx
            ux,uy=field(d['u'][0],mask),field(d['u'][1],mask)
            for a,data,title in [(axes[0,0],np.sqrt(ux*ux+uy*uy),'Actual Re20 full-domain cylinder'),(axes[0,1],field(d['p'],mask),'Saved pressure, mean gauge')]:
                im=a.pcolormesh(x,y,data,shading='nearest',rasterized=True,cmap='viridis');a.add_patch(Circle((.2,.2),.05,color='white'));a.set_title(title);fig.colorbar(im,ax=a)
            t=np.arange(len(d['force_coefficients']))*float(z['dt']);a=axes[1,0]
            late=t>=20;a.plot(t[late],d['force_coefficients'][late,0],label='CD, t≥20');a.axhspan(5.57,5.59,color='gray',alpha=.2,label='original estimated range');a.set_title('Late actual momentum-exchange drag');a.legend(fontsize=8)
            a=axes[1,1];a.plot(x,d['wake_u']);a.axhline(0,color='gray',lw=.7);a.axvspan(.15,.25,color='gray',alpha=.2);a.set_xlim(.1,.5);a.set_title('Saved wake centerline ux at y=.2')
        for a in axes[0]:a.set_aspect('equal');a.set_xlabel('x');a.set_ylabel('y')
        for a in axes[1]:a.grid(alpha=.2)
        fig.suptitle(ident+' · fixed inputs · actual saved arrays',fontsize=14)
        for suffix in ['.png','.svg','.pdf']:
            fig.savefig(args.output/(ident+suffix),dpi=150)
            fig.savefig(args.output/(ident+'-preview'+suffix),dpi=100)
        plt.close(fig)

if __name__=='__main__':main()
