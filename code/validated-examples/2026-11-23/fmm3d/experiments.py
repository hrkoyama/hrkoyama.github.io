import numpy as np
import fmm
from references.direct import direct,octahedron
from protocol import Case
IDS=['fmm3d-inverse-r']
def rel(a,b):return float(np.sqrt(np.sum((a-b)**2)/np.sum(b*b)))

def execute(cfg,L,out,cases,budget):
    c=Case(IDS[0],out,cases);x=np.array(cfg['positions']);m=np.array(cfg['masses']);P,A=direct(x,m);rows=[]
    for depth in cfg['depths']:
        for p in cfg['orders']:
            budget.check();data,count=fmm.solve(x,m,p,depth,forced=True);tag=f'p{p}-d{depth}';c.save(tag,dict(positions=x,masses=m,reference_potential=P,reference_acceleration=A,**data))
            row=dict(id=tag,p=p,depth=depth,potential_error=rel(data['potential'],P),acceleration_error=rel(data['acceleration'],A),far_fraction=count['far_pairs']/(len(x)*(len(x)-1)),chain_potential_norm=float(np.sqrt(np.sum(data['chain_potential']**2))),relative_net_force=float(np.linalg.norm(np.sum(m[:,None]*data['acceleration'],axis=0))/np.sum(m*np.linalg.norm(A,axis=1))),**count)
            c.gate(tag+' finite potential and force',np.isfinite(data['potential']).all() and np.isfinite(data['acceleration']).all());c.gate(tag+' exact interaction ownership',np.array_equal(data['ownership'],data['expected_ownership']));c.gate(tag+' far path exercised',row['far_fraction']>=L['far_fraction']);c.gate(tag+' actual forced depth',bool(np.all(data['leaf_depths']==depth)))
            if depth==max(cfg['depths']):c.gate(tag+' nonzero complete translation chain',count['chain_pairs']>0 and row['chain_potential_norm']>L['chain_signal'])
            c.row(row);rows.append(row)
    adaptive=np.array(cfg['adaptive_positions']);ap,aa=direct(adaptive,m);data,count=fmm.solve(adaptive,m,max(cfg['orders']),3,forced=False,capacity=8);c.save('adaptive',dict(positions=adaptive,masses=m,reference_potential=ap,reference_acceleration=aa,**data))
    c.gate('adaptive finite fields',np.isfinite(data['potential']).all() and np.isfinite(data['acceleration']).all());c.gate('adaptive exact ownership',np.array_equal(data['ownership'],data['expected_ownership']));c.gate('adaptive far path',count['far_pairs']/(len(m)*(len(m)-1))>=L['far_fraction']);c.gate('adaptive unequal actual levels',len(np.unique(data['leaf_depths']))>1);c.gate('adaptive capped bucket retained',count['overfull_leaves']>0)
    c.bound('adaptive potential accuracy',rel(data['potential'],ap),L['potential']);c.bound('adaptive force accuracy',rel(data['acceleration'],aa),L['acceleration'])
    c.row(dict(id='adaptive',p=max(cfg['orders']),depth=3,potential_error=rel(data['potential'],ap),acceleration_error=rel(data['acceleration'],aa),**count))
    for depth in cfg['depths']:
        a,b=[next(r for r in rows if r['depth']==depth and r['p']==p) for p in [min(cfg['orders']),max(cfg['orders'])]]
        for name,limit in [('potential_error',L['potential']),('acceleration_error',L['acceleration'])]:
            c.bound(f'd{depth} finest '+name,b[name],limit);c.gate(f'd{depth} order refinement '+name,a[name]<=L['noise'] or b[name]<=L['order_ratio']*a[name])
    r=.2;sources=np.r_[np.eye(3)*r,-np.eye(3)*r];mass=np.full(6,1/6);targets=np.array([[0,0,0],[0,0,.6],[0,0,.9],[0,0,1.2]]);phi,acc=direct(sources,mass,targets);expectedP=[-1/r];expectedA=[0.]
    for R in [.6,.9,1.2]:v,a=octahedron(r,R);expectedP.append(v);expectedA.append(a)
    c.save('analytic-reference',dict(positions=sources,masses=mass,targets=targets,potential=phi,acceleration=acc,expected_potential=np.array(expectedP),expected_az=np.array(expectedA)));c.bound('direct octahedron potential golden',np.max(abs(phi-expectedP)),L['analytic']);c.bound('direct octahedron acceleration golden',max(np.max(abs(acc[:,2]-expectedA)),np.max(abs(acc[:,:2]))),L['analytic'])
    angle=.21;rotation=np.array([[np.cos(angle),-np.sin(angle),0],[np.sin(angle),np.cos(angle),0],[0,0,1]]);xx=np.einsum('ij,nj->ni',rotation,x,optimize=False)+np.array([.071,-.033,.019]);pp,aa=direct(xx,m);data,count=fmm.solve(xx,m,max(cfg['orders']),max(cfg['depths']),forced=True);c.save('rigid-transform',dict(positions=xx,masses=m,reference_potential=pp,reference_acceleration=aa,**data))
    c.bound('rigid transformed potential',rel(data['potential'],pp),L['potential']);c.bound('rigid transformed acceleration',rel(data['acceleration'],aa),L['acceleration']);c.gate('rigid transformed ownership',np.array_equal(data['ownership'],data['expected_ownership']));c.gate('rigid transformed actual level',np.all(data['leaf_depths']==max(cfg['depths'])))
    c.row(dict(id='rigid-transform',p=max(cfg['orders']),depth=max(cfg['depths']),potential_error=rel(data['potential'],pp),acceleration_error=rel(data['acceleration'],aa),**count));c.finish(dict(finest_potential_error=rows[-1]['potential_error'],finest_acceleration_error=rows[-1]['acceleration_error'],primary_runs=len(rows),additional_fixed_evaluations=2))
