import numpy as np
import dynamics as s
from references import exact as r
from protocol import Case
IDS=['gravity-kepler','gravity-plummer-short']

def rms(v):return float(np.sqrt(np.mean(np.asarray(v)**2)))
def summarize(a):
    d=a['diagnostics'];t=a['times'];mass=a['masses'].sum();expected=d[0,7:10]+t[:,None]*d[0,1:4]/mass
    return dict(energy_drift=float(np.max(abs(d[:,0]-d[0,0]))/abs(d[0,0])),momentum_drift=float(np.max(abs(d[:,1:4]-d[0,1:4]))),angular_drift=float(np.max(abs(d[:,4:7]-d[0,4:7]))),com_drift=float(np.max(abs(d[:,7:10]-expected))),minimum_separation=float(d[:,-1].min()),accepted_nodes=int(a['work_counts'][:,0].sum()),direct_pairs=int(a['work_counts'][:,1].sum()))

def basic(c,tag,a,final):
    c.gate(tag+' finite synchronized fields',all(np.isfinite(a[k]).all() for k in ['positions','velocities','accelerations','diagnostics']));c.gate(tag+' fixed final time',a['times'][-1]==final);c.gate(tag+' positive pair separation',np.min(a['diagnostics'][:,-1])>0)

def execute(cfg,L,out,cases,budget):
    c=Case(IDS[0],out,cases);k=cfg['kepler'];m=np.array(k['masses']);T=2*np.pi*np.sqrt(k['a']**3/m.sum());x,v,_=r.kepler([0.],m,k['a'],k['eccentricity']);rows=[];last=None
    for steps in k['steps']:
        a=s.integrate(x[0],v[0],m,0.,T,steps,budget=budget);xr,vr,root=r.kepler(a['times'],m,k['a'],k['eccentricity']);tag=f's{steps}';c.save(tag,dict(**a,reference_positions=xr,reference_velocities=vr,kepler_root_residual=root));row=dict(id=tag,steps=steps,time=float(T),position_error=float(np.max(np.linalg.norm(a['positions']-xr,axis=2))),state_rms_error=rms(np.r_[(a['positions']-xr).ravel(),(a['velocities']-vr).ravel()]),**summarize(a));basic(c,tag,a,T)
        for key in ['momentum_drift','angular_drift','com_drift']:c.bound(tag+' '+key,row[key],L['direct_momenta'])
        c.bound(tag+' Kepler root residual',np.max(root),L['root']);c.bound(tag+' independent final pair force',np.max(abs(a['accelerations'][-1]-r.pair_force(a['positions'][-1],m,0.))),L['force_identity']);c.row(row);rows.append(row);last=(a,xr,vr)
    a,xr,vr=last;expected_energy=-m[0]*m[1]/(2*k['a']);energy=np.array([.5*np.sum(m[:,None]*vv*vv)+r.potential(xx,m,0.) for xx,vv in zip(xr,vr)])
    angular=np.sum(m[None,:,None]*np.cross(xr,vr),axis=1);expected_L=m[0]*m[1]/m.sum()*np.sqrt(m.sum()*k['a']*(1-k['eccentricity']**2))
    c.bound('analytic reference energy identity',np.max(abs(energy-expected_energy)),L['reference_identity']);c.bound('analytic reference angular identity',np.max(abs(angular-np.array([0,0,expected_L]))),L['reference_identity']);c.bound('analytic reference COM identity',np.max(abs(np.sum(m[None,:,None]*xr,axis=1))),L['reference_identity'])
    for j in [1,2]:c.gate('time refinement '+str(j),np.log2(rows[j-1]['state_rms_error']/rows[j]['state_rms_error'])>=L['order'])
    c.bound('finest Kepler position',rows[-1]['position_error'],L['kepler_position']);c.bound('finest Kepler energy',rows[-1]['energy_drift'],L['kepler_energy']);c.finish(dict(finest_position_error=rows[-1]['position_error'],finest_energy_drift=rows[-1]['energy_drift'],period=float(T)))

    c=Case(IDS[1],out,cases);k=cfg['cold'];x=np.array(k['positions']);m=np.array(k['masses']);v=np.zeros_like(x);times=np.linspace(0,k['final_time'],max(k['steps'])+1);references=[]
    for j,(rtol,atol) in enumerate(zip(k['reference_rtol'],k['reference_atol'])):
        budget.check();xr,vr,info=r.reference(x,v,m,k['epsilon'],times,rtol,atol,budget);c.save('reference-'+str(j),dict(positions=xr,velocities=vr,**info));references.append((xr,vr))
    xr,vr=references[-1];gap=max(np.max(abs(xr-references[0][0])),np.max(abs(vr-references[0][1])));c.bound('independent ODE tolerance qualification',gap,L['reference_gap'])
    energies=np.array([.5*np.sum(m[:,None]*vv*vv)+r.potential(xx,m,k['epsilon']) for xx,vv in zip(xr,vr)]);P=np.sum(m[None,:,None]*vr,axis=1);angular=np.sum(m[None,:,None]*np.cross(xr,vr),axis=1)
    c.bound('independent reference energy',np.max(abs(energies-energies[0]))/abs(energies[0]),L['reference_energy']);c.bound('independent reference momentum',np.max(abs(P-P[0])),L['direct_momenta']);c.bound('independent reference angular momentum',np.max(abs(angular-angular[0])),L['direct_momenta'])
    c.bound('antipodal initial COM',np.max(abs(np.sum(m[:,None]*x,axis=0))),L['reference_identity']);direct=[]
    for steps in k['steps']:
        a=s.integrate(x,v,m,k['epsilon'],k['final_time'],steps,budget=budget);indices=np.arange(steps+1)*(max(k['steps'])//steps);xx=xr[indices];vv=vr[indices];tag=f'direct-s{steps}';c.save(tag,dict(**a,reference_positions=xx,reference_velocities=vv));row=dict(id=tag,steps=steps,theta=-1.,time=k['final_time'],state_rms_error=rms(np.r_[(a['positions']-xx).ravel(),(a['velocities']-vv).ravel()]),**summarize(a));basic(c,tag,a,k['final_time'])
        for key in ['momentum_drift','angular_drift','com_drift']:c.bound(tag+' '+key,row[key],L['direct_momenta'])
        c.row(row);direct.append((row,a))
    fine=direct[-1][1];tree_rows=[]
    for theta in k['thetas']:
        a=s.integrate(x,v,m,k['epsilon'],k['final_time'],max(k['steps']),theta,budget);tag=f'theta{theta:g}';held=[]
        for j in np.linspace(0,len(times)-1,5,dtype=int):
            ft,count=s.tree(fine['positions'][j],m,k['epsilon'],theta);fr=r.pair_force(fine['positions'][j],m,k['epsilon']);scale=rms(fr)
            if scale<=0:raise ArithmeticError('Frozen same-position force reference has zero norm')
            held.append(rms(ft-fr)/scale)
        trajectory=rms(np.r_[(a['positions']-fine['positions']).ravel(),(a['velocities']-fine['velocities']).ravel()]);row=dict(id=tag,steps=max(k['steps']),theta=theta,time=k['final_time'],trajectory_gap=trajectory,same_position_force_relative=max(held),**summarize(a));c.save(tag,dict(**a,direct_positions=fine['positions'],direct_velocities=fine['velocities'],held_direct_force_errors=np.array(held)));basic(c,tag,a,k['final_time'])
        if theta==0.:
            for key in ['momentum_drift','angular_drift','com_drift']:c.bound(tag+' '+key,row[key],L['direct_momenta'])
            c.bound('theta0 trajectory reproduces direct',trajectory,L['theta0']);c.bound('theta0 same-position force identity',row['same_position_force_relative'],L['force_identity'])
        elif theta==.35:
            c.bound('theta.35 trajectory error',trajectory,L['tree_trajectory']);c.bound('theta.35 same-position force error',row['same_position_force_relative'],L['tree_force'])
        else:c.gate('theta.6 actual accepted nodes',row['accepted_nodes']>0);c.bound('theta.6 same-position force error',row['same_position_force_relative'],L['coarse_tree_force'])
        c.row(row);tree_rows.append(row)
    for j in [1,2]:c.gate('direct time refinement '+str(j),np.log2(direct[j-1][0]['state_rms_error']/direct[j][0]['state_rms_error'])>=L['order'])
    c.bound('finest direct state error',direct[-1][0]['state_rms_error'],L['cold_error']);c.bound('finest direct energy',direct[-1][0]['energy_drift'],L['cold_energy'])
    asym=x.copy();asym[0]+=[.013,-.007,.009];fa,counts=s.tree(asym,m,k['epsilon'],.6);fr=r.pair_force(asym,m,k['epsilon']);net=np.sum(m[:,None]*fa,axis=0);c.save('asymmetric-static',dict(positions=asym,masses=m,tree_acceleration=fa,reference_acceleration=fr,net_tree_force=net));c.gate('asymmetric diagnostics finite',np.isfinite(fa).all() and np.isfinite(net).all());c.gate('asymmetric tree approximation exercised',counts['accepted_nodes']>0)
    c.finish(dict(reference_tolerance_gap=float(gap),finest_direct_error=direct[-1][0]['state_rms_error'],finest_energy_drift=direct[-1][0]['energy_drift'],theta035_trajectory=tree_rows[1]['trajectory_gap'],asymmetric_net_force=float(np.linalg.norm(net))))
