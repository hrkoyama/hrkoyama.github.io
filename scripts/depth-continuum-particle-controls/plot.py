"""Plot and CSV export from saved result arrays only; no solver calls."""
import argparse,csv,json,hashlib
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection


def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args();source=args.results.parent;out=args.output;out.mkdir(parents=True,exist_ok=True);report=json.loads(args.results.read_text());provenance={'result_sha256':hashlib.sha256(args.results.read_bytes()).hexdigest(),'data_sources':{},'plots':{},'scope':'Plots and CSV are derived only from saved arrays. No numerical solver executes here.'}
    def load(path):
        provenance['data_sources'][path.name]=hashlib.sha256(path.read_bytes()).hexdigest()
        return np.load(path,allow_pickle=False)
    def save(fig,ident):
        fig.tight_layout();fig.savefig(out/(ident+'.png'),dpi=150);fig.savefig(out/(ident+'-preview.png'),dpi=90);plt.close(fig);provenance['plots'][ident]={name:hashlib.sha256((out/name).read_bytes()).hexdigest() for name in [ident+'.png',ident+'-preview.png']}
    def table(name,header,values):np.savetxt(out/name,values,delimiter=',',header=','.join(header),comments='')
    f=sorted(source.glob('piston-*.npz'))[-1];d=load(f);polygons=d['points'][d['cells']];U=d['conserved'];exact=d['exact_conserved_average'];center=polygons.mean(axis=1);rho=U[:,0];pressure=(5/3-1)*(U[:,3]-.5*np.sum(U[:,1:3]**2,axis=1)/rho);fig,axes=plt.subplots(2,1,figsize=(10,6));collection=PolyCollection(polygons,array=rho,cmap='viridis',edgecolors=(0,0,0,.2),linewidths=.25);axes[0].add_collection(collection);axes[0].autoscale();axes[0].set(xlabel='x',ylabel='y',title='Prescribed-ALE skew piston: saved density and mesh');fig.colorbar(collection,ax=axes[0],label='Density');axes[1].scatter(center[:,0],rho,s=5,label='Computed cell means');axes[1].scatter(center[:,0],exact[:,0],s=5,alpha=.6,label='Exact conserved-volume means');axes[1].set(xlabel='Cell center x',ylabel='Density');axes[1].legend();save(fig,'saltzman-ale-piston');table('saltzman-ale-piston.csv',['x','y','rho','rho_exact_cell_mean','pressure_of_computed_mean'],np.column_stack((center,rho,exact[:,0],pressure)))
    f=sorted(source.glob('sphere-*.npz'),key=lambda path:(int(path.stem.split('-')[1]),float(path.stem.split('-')[3])))[-1];d=load(f);fig,axes=plt.subplots(1,2,figsize=(11,4));extent=[0,360,-90,90]
    for ax,data,title in zip(axes,[d['final'],abs(d['final']-d['exact'])],['Scalar after one rotation','Absolute point-value error']):
        im=ax.imshow(data,origin='lower',extent=extent,aspect='auto',cmap='viridis');ax.set(xlabel='Longitude (degrees)',ylabel='Latitude (degrees)',title=title);fig.colorbar(im,ax=ax)
    save(fig,'williamson-sphere-transport');lon,lat=np.meshgrid(d['lon'],d['lat']);table('williamson-sphere-transport.csv',['lon','lat','q','q_exact','area'],np.column_stack([a.ravel() for a in [lon,lat,d['final'],d['exact'],d['areas']]]))
    d=load(sorted(source.glob('zonal-*.npz'))[-1]);phi=d['phi']*180/np.pi;fig,axes=plt.subplots(1,3,figsize=(12,3.6))
    for k,(ax,label) in enumerate(zip(axes,['Depth h','Zonal velocity u','Meridional velocity v'])):
        ax.plot(phi,d['initial'][k],label='Stationary reference');ax.plot(phi,d['final'][k],'--',label='Time-integrated');ax.set(xlabel='Latitude (degrees)',ylabel=label)
    axes[0].legend();save(fig,'sphere-zonal-balance');table('sphere-zonal-balance.csv',['latitude','h','u','v','h_exact','u_exact','v_exact'],np.column_stack((d['phi'],d['final'].T,d['initial'].T)))
    f=sorted(source.glob('sod-gsph-*.npz'),key=lambda path:int(path.stem.split('-')[-1]))[-1];d=load(f);ref=d['reference'];rref=ref[:,0];vref=ref[:,1]/rref;pref=.4*(ref[:,2]-.5*ref[:,1]**2/rref);order=np.argsort(d['x']);mask=(d['x'][order]>=-.4)&(d['x'][order]<=.4);indices=order[mask];fig,axes=plt.subplots(1,3,figsize=(12,3.7))
    for ax,label,actual,expected in zip(axes,['Density','Pressure','Velocity'],[d['density'],d['pressure'],d['velocity']],[rref,pref,vref]):
        ax.plot(d['x'][indices],expected[indices],color='black',label='Independent Riemann reference');ax.scatter(d['x'][indices],actual[indices],s=8,label='GSPH particles');ax.set(xlabel='Physical x',ylabel=label)
    axes[0].legend(fontsize=7);save(fig,'gsph-sod');table('gsph-sod.csv',['x','rho','pressure','velocity','h','rho_reference','pressure_reference','velocity_reference'],np.column_stack((d['x'],d['density'],d['pressure'],d['velocity'],d['h'],rref,pref,vref)))
    f=sorted(source.glob('smooth-gsph-wave-jitter-*.npz'),key=lambda path:int(path.stem.split('-')[-1]))[-1];d=load(f);order=np.argsort(d['x']);fig,axes=plt.subplots(1,2,figsize=(11,3.7));axes[0].scatter(d['x'],d['density']-1,s=9,label='GSPH jittered particles');axes[0].plot(d['x'][order],1e-3*np.sin(2*np.pi*(d['x'][order]-.2)),color='black',label='Linearized reference');axes[0].set(xlabel='x',ylabel='Density perturbation');axes[0].legend(fontsize=8);axes[1].scatter(d['initial_x'],d['initial_density']-d['initial_model_density'],s=9);axes[1].set(xlabel='Initial particle x',ylabel='Initial kernel reconstruction error');save(fig,'sph-pressure-acoustics');table('sph-pressure-acoustics.csv',['x','rho','pressure','velocity','h'],np.column_stack((d['x'],d['density'],d['pressure'],d['velocity'],d['h'])))
    with (out/'case-summary.csv').open('w',newline='') as stream:
        writer=csv.writer(stream);writer.writerow(['case','passed','checks','metrics'])
        for row in report['cases']:writer.writerow([row['id'],row['passed'],json.dumps(row['checks'],sort_keys=True),json.dumps(row['metrics'],sort_keys=True)])
    (out/'figure-provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')


if __name__=='__main__':main()
