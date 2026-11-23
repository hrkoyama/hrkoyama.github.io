import numpy as np
import electrostatics as s
from references import twoperiodic as r
from protocol import Case
IDS=['neutral-slab-yb']

def execute(cfg,L,out,cases,budget):
    c=Case(IDS[0],out,cases);x=np.array(cfg['positions']);q=np.array(cfg['charges']);lateral=np.array(cfg['lateral']);refs=[]
    for tag,alpha,rcut,kcut in [('fine',4.,2.5,64.),('split',3.,2.5,64.),('cut',4.,2.,48.)]:
        budget.check();e,f,a=r.energy_force(x,q,lateral,alpha,rcut,kcut);c.save('reference-'+tag,dict(positions=x,charges=q,energy=e,force=f,**a));refs.append((e,f))
    refE,refF=refs[0]
    for j,tag in [(1,'splitting'),(2,'cutoff')]:
        c.bound('reference '+tag+' energy',abs(refs[j][0]-refE),L['reference_energy']);c.bound('reference '+tag+' force',np.max(abs(refs[j][1]-refF)),L['reference_force'])
    records=[]
    for z in cfg['vacuum_lengths']:
        for alpha in cfg['alphas']:
            budget.check();box=np.r_[lateral,z];E,F,a=s.corrected(x,q,box,alpha,cfg['real_cutoff'],cfg['k_cutoff']);tag=f'z{z:g}-a{alpha:g}'
            c.save(tag,dict(positions=x,charges=q,lengths=box,energy=E,force=F,reference_energy=refE,reference_force=refF,**a))
            row=dict(id=tag,Lz=z,alpha=alpha,energy=E,reference_energy=refE,corrected_energy_error=abs(E-refE),uncorrected_energy_error=abs(a['uncorrected_energy']-refE),corrected_force_error=float(np.max(abs(F-refF))),uncorrected_force_error=float(np.max(abs(a['uncorrected_force']-refF))),net_force=float(np.max(abs(F.sum(axis=0)))),reciprocal_count=a['reciprocal_count'])
            c.gate(tag+' finite saved fields',bool(np.isfinite(F).all() and np.isfinite(a['potential']).all() and np.isfinite(E)));c.bound(tag+' neutral net force',row['net_force'],L['net_force']);c.row(row);records.append((row,E,F))
    for z in cfg['vacuum_lengths']:
        a,b=[v for v in records if v[0]['Lz']==z];c.bound(f'z{z:g} alpha energy',abs(a[1]-b[1]),L['alpha_energy']);c.bound(f'z{z:g} alpha force',np.max(abs(a[2]-b[2])),L['alpha_force'])
    for row,E,F in [v for v in records if v[0]['Lz']==max(cfg['vacuum_lengths'])]:
        c.bound(row['id']+' finest energy',row['corrected_energy_error'],L['energy']);c.bound(row['id']+' finest force',row['corrected_force_error'],L['force'])
        for key,noise in [('energy',L['reference_energy']),('force',L['reference_force'])]:c.gate(row['id']+' correction improves '+key,row['uncorrected_'+key+'_error']<=100*noise or row['corrected_'+key+'_error']<=row['uncorrected_'+key+'_error']/10)
    box=np.r_[lateral,max(cfg['vacuum_lengths'])];base=s.corrected(x,q,box,4.)[:2];shift=np.array(cfg['translation']);translated=s.corrected(x+shift,q,box,4.)[:2]
    c.bound('neutral translation energy',abs(translated[0]-base[0]),L['translation_energy']);c.bound('neutral translation force',np.max(abs(translated[1]-base[1])),L['translation_force'])
    for h in cfg['difference_steps']:
        for kind in ['production','reference']:
            error=0.
            for i,d in cfg['difference_components']:
                xp=x.copy();xm=x.copy();xp[i,d]+=h;xm[i,d]-=h
                if kind=='production':ep=s.corrected(xp,q,box,4.)[0];em=s.corrected(xm,q,box,4.)[0];force=base[1][i,d]
                else:ep=r.energy_force(xp,q,lateral,4.)[0];em=r.energy_force(xm,q,lateral,4.)[0];force=refF[i,d]
                error=max(error,abs(-(ep-em)/(2*h)-force))
            c.bound(kind+f' energy gradient h{h:g}',error,L['difference'])
    omitted=r.energy_force(x,q,lateral,4.,include_zero=False)[0];c.gate('omitted zero mode is detected',abs(omitted-refE)>L['negative_control'])
    targets=np.array([[.37,.19,6.],[.37,.19,-6.]]);phi,field,zero=r.evaluate(x,q,lateral,4.,2.5,64.,targets);mz=float(np.sum(q*x[:,2]));expected=np.array([1.,-1.])*2*np.pi*mz/np.prod(lateral)
    c.save('far-zero-mode',dict(targets=targets,potential=phi,field=field,expected_potential=expected,zero_potential=zero));c.bound('far-z potential step',np.max(abs(phi-expected)),L['far']);c.bound('far-z zero field',np.max(abs(field)),L['far'])
    order=np.array([2,0,3,1]);pe,pf,_=s.corrected(x[order],q[order],box,4.);c.bound('source permutation energy',abs(pe-base[0]),L['permutation']);c.bound('source permutation force',np.max(abs(pf-base[1][order])),L['permutation'])
    try:s.corrected(x,q+np.array([.1,0,0,0]),box)
    except ValueError:c.gate('charged cell rejected',True)
    else:c.gate('charged cell rejected',False)
    c.finish(dict(reference_energy=refE,maximum_reference_force=float(np.max(abs(refF))),dipole_z=mz,finest_energy_error=records[-1][0]['corrected_energy_error'],finest_force_error=records[-1][0]['corrected_force_error']))
