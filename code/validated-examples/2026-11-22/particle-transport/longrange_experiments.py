"""Preregistered small long-range convergence and invariance experiments.

The old MIT algorithms are retained in separate source copies; diagnostics,
independent reference paths and acceptance here are new. No stored outcomes
are used as a substitute for recomputing the references during this run.
"""
from functools import lru_cache
import numpy as np
from electrostatics import ewald,spme,assignment,theta_periodic_reference
from fmm import fmm,independent_direct,analytic_two_source,analytic_regular_ring


def maxabs(value):return float(np.max(np.abs(value)))


def result_case(identifier,checks,metrics,records):
    checks={key:bool(value) for key,value in checks.items()}
    return dict(id=identifier,passed=bool(all(checks.values())),checks=checks,metrics=metrics,records=records)


def sampled_gradient(energy,x,components,step):
    values=[]
    for i,axis in components:
        lo=x.copy();hi=x.copy();lo[i,axis]-=step;hi[i,axis]+=step
        values.append(-(energy(hi)-energy(lo))/(2*step))
    return np.array(values)


def force_reference_error(measured,reference):
    """Detector is also exercised with a deliberately corrupted reference."""
    return maxabs(np.asarray(measured)-np.asarray(reference))


def theta_references(c):
    x=np.array(c['positions']);q=np.array(c['charges']);length=c['length']
    outputs=[];records=[]
    for name in ('reference','reference_refined','reference_tail'):
        energy,force,info=theta_periodic_reference(x,q,length,**c[name])
        outputs.append((energy,force,info))
        records.append(dict(series='independent_theta',setting=name,energy=energy,forces=force.tolist(),**info))
    return outputs,records


def ewald_case(c,refs=None,reference_records=None):
    if refs is None:refs,reference_records=theta_references(c)
    x=np.array(c['positions']);q=np.array(c['charges']);length=c['length'];tol=c['acceptance']
    re,rf,_=refs[-1];records=list(reference_records or []);alpha=c['baseline_alpha']
    base_e,base_f=ewald(x,q,length,alpha,c['baseline_images'],c['baseline_kmax'])
    metrics=dict(reference_energy=re,reference_energy_refinement=abs(refs[1][0]-refs[0][0]),reference_force_refinement=maxabs(refs[1][1]-refs[0][1]),reference_tail_energy=abs(refs[2][0]-refs[1][0]),reference_tail_force=maxabs(refs[2][1]-refs[1][1]),reference_quadrature_estimate=max(r[2]['quad_error'] for r in refs),energy_error=abs(base_e-re),force_error=force_reference_error(base_f,rf))
    splits=[]
    for a in c['alphas']:
        e,f=ewald(x,q,length,a,c['baseline_images'],c['baseline_kmax']);splits.append((e,f))
        records.append(dict(series='splitting',alpha=a,energy=e,energy_error=abs(e-re),force_error=maxabs(f-rf)))
    metrics['splitting_energy_spread']=max(abs(e-base_e) for e,_ in splits)
    metrics['splitting_force_spread']=max(maxabs(f-base_f) for _,f in splits)
    real=[];reciprocal=[]
    for images in c['real_cutoffs']:
        e,f=ewald(x,q,length,alpha,images,c['baseline_kmax']);real.append(maxabs(f-rf))
        records.append(dict(series='real_cutoff',images=images,alpha=alpha,energy=e,energy_error=abs(e-re),force_error=real[-1]))
    for cutoff in c['reciprocal_cutoffs']:
        e,f=ewald(x,q,length,alpha,c['baseline_images'],cutoff);reciprocal.append(maxabs(f-rf))
        records.append(dict(series='reciprocal_cutoff',cutoff=cutoff,alpha=alpha,energy=e,energy_error=abs(e-re),force_error=reciprocal[-1]))
    metrics['real_refinement_ratio']=real[-1]/max(real[0],np.finfo(float).tiny)
    metrics['reciprocal_refinement_ratio']=reciprocal[-1]/max(reciprocal[0],np.finfo(float).tiny)
    e,f=ewald(x+np.array(c['translation']),q,length,alpha,c['baseline_images'],c['baseline_kmax'])
    metrics.update(translation_energy=abs(e-base_e),translation_force=maxabs(f-base_f))
    perm=np.array(c['permutation']);e,f=ewald(x[perm],q[perm],length,alpha,c['baseline_images'],c['baseline_kmax'])
    metrics['permutation_force']=maxabs(f-base_f[perm]);metrics['net_force']=maxabs(base_f.sum(axis=0))
    grad=sampled_gradient(lambda p:ewald(p,q,length,alpha,c['baseline_images'],c['baseline_kmax'])[0],x,c['gradient_components'],c['finite_difference_step'])
    metrics['gradient_error']=maxabs(grad-np.array([base_f[i,a] for i,a in c['gradient_components']]))
    _,control=ewald(x,q,length,alpha,0,c['reciprocal_cutoffs'][0]);metrics['control_force_error']=maxabs(control-rf)
    checks={key:metrics[key]<=value for key,value in tol.items() if key!='control_force_error_min'}
    checks['truncation_control_detected']=metrics['control_force_error']>=tol['control_force_error_min'] and metrics['control_force_error']>tol['force_error']
    checks['asymmetric_forces_nonzero']=maxabs(rf)>.1
    checks['reference_quadrature_converged']=all(r[2]['left_success'] and r[2]['right_success'] for r in refs)
    records.append(dict(series='force_reference',energy=base_e,forces=base_f.tolist(),reference_forces=rf.tolist(),net_force=metrics['net_force'],gradient_components=c['gradient_components'],gradient_values=grad.tolist()))
    return result_case('ewald-convergence',checks,metrics,records)


def spme_case(c,ec,reference):
    x=np.array(ec['positions']);q=np.array(ec['charges']);length=ec['length'];re,rf=reference;tol=c['acceptance']
    records=[];outputs={};charge=[];all_net=[]
    for order in c['orders']:
        for mesh in c['meshes']:
            phase_outputs=[]
            for phase,shift in enumerate(c['translations']):
                e,f,ce=spme(x+np.array(shift),q,length,c['alpha'],c['images'],mesh,order)
                phase_outputs.append((e,f));charge.append(ce);all_net.append(maxabs(f.sum(axis=0)))
                records.append(dict(series='mesh_phase',order=order,mesh=mesh,phase=phase,energy=e,energy_error=abs(e-re),force_error=maxabs(f-rf),net_force=maxabs(f.sum(axis=0)),charge_error=ce))
            outputs[order,mesh]=phase_outputs
    finest=outputs[c['orders'][-1],c['meshes'][-1]];coarsest=outputs[c['orders'][-1],c['meshes'][0]]
    e,f=finest[0]
    shared_e,shared_f=ewald(x,q,length,c['alpha'],c['images'],ec['baseline_kmax'])
    metrics=dict(fine_energy_error=max(abs(a-re) for a,_ in finest),fine_force_error=max(maxabs(a-rf) for _,a in finest),force_refinement_ratio=max(maxabs(a-rf) for _,a in finest)/max(maxabs(a-rf) for _,a in coarsest),phase_energy_spread=max(abs(a-e) for a,_ in finest),phase_force_spread=max(maxabs(a-f) for _,a in finest),charge_error=max(charge),fine_net_force=max(maxabs(a.sum(axis=0)) for _,a in finest),maximum_net_force_all_meshes=max(all_net),shared_ewald_energy_error=abs(shared_e-re),shared_ewald_force_error=maxabs(shared_f-rf))
    partition=[];derivative=[]
    for order in c['orders']:
        for phase in c['partition_phases']:
            _,weights,derivatives=assignment(np.array([phase,.371,.714]),length,32,order)
            partition.extend(abs(float(w.sum())-1) for w in weights)
            derivative.extend(abs(float(w.sum())) for w in derivatives)
    metrics.update(partition_error=max(partition),partition_derivative_error=max(derivative))
    grad=sampled_gradient(lambda p:spme(p,q,length,c['alpha'],c['images'],c['meshes'][-1],c['orders'][-1])[0],x,c['gradient_components'],c['finite_difference_step'])
    metrics['gradient_error']=maxabs(grad-np.array([f[i,a] for i,a in c['gradient_components']]))
    control=outputs[c['orders'][0],c['meshes'][0]][0][1]
    metrics['coarse_control_force_error']=maxabs(control-rf)
    checks={key:metrics[key]<=value for key,value in tol.items() if key!='coarse_control_force_error_min'}
    checks['coarse_control_detected']=metrics['coarse_control_force_error']>=tol['coarse_control_force_error_min'] and metrics['coarse_control_force_error']>tol['fine_force_error']
    checks['both_orders_refine']=all(max(maxabs(a-rf) for _,a in outputs[o,c['meshes'][-1]])<max(maxabs(a-rf) for _,a in outputs[o,c['meshes'][0]]) for o in c['orders'])
    records.append(dict(series='gradient',order=c['orders'][-1],mesh=c['meshes'][-1],gradient_values=grad.tolist(),force_components=[float(f[i,a]) for i,a in c['gradient_components']],reference_forces=rf.tolist(),forces=f.tolist(),shared_ewald_energy=shared_e,shared_ewald_forces=shared_f.tolist()))
    return result_case('spme-convergence',checks,metrics,records)


def fmm_case(c):
    rng=np.random.default_rng(c['seed']);n=c['particles'];lo,hi=c['position_interval']
    z=rng.uniform(lo,hi,n)+1j*rng.uniform(lo,hi,n);q=rng.uniform(*c['charge_interval'],n)
    rp,rf=independent_direct(z,q);records=[];outputs={};tol=c['acceptance']
    for depth in c['depths']:
        for order in c['orders']:
            p,f,ops=fmm(z,q,order,depth);outputs[depth,order]=(p,f,ops)
            records.append(dict(series='order_depth',depth=depth,order=order,potential_error=maxabs(p-rp),field_error=maxabs(f-rf),**ops))
    depth=c['baseline_depth'];order=c['orders'][-1];p,f,ops=outputs[depth,order]
    coarse=outputs[depth,c['orders'][0]][1];depth2=outputs[c['depths'][0],order][1]
    force=q[:,None]*f;direct_force=q[:,None]*rf
    metrics=dict(fine_potential_error=maxabs(p-rp),fine_field_error=maxabs(f-rf),order_refinement_ratio=maxabs(f-rf)/maxabs(coarse-rf),depth2_field_error=maxabs(depth2-rf),net_force_relative=maxabs(force.sum(axis=0))/max(float(np.sum(np.linalg.norm(direct_force,axis=1))),np.finfo(float).tiny),net_force_absolute=maxabs(force.sum(axis=0)),direct_net_force=maxabs(direct_force.sum(axis=0)),coarse_control_field_error=maxabs(coarse-rf))
    shift=complex(*c['translation']);tp,tf,tops=fmm(z+shift,q,order,depth)
    metrics.update(translation_potential_error=maxabs(tp-p),translation_field_error=maxabs(tf-f))
    angle=c['rotation_radians'];rot=np.exp(1j*angle);rotated=(z-(.5+.5j))*rot+(.5+.5j)
    ap,af,aops=fmm(rotated,q,order,depth)
    matrix=np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])
    metrics.update(rotation_potential_error=maxabs(ap-p),rotation_field_error=maxabs(af-f@matrix.T))
    sources=np.array(c['analytic_sources']);targets=np.array(c['analytic_targets']);charges=np.array(c['analytic_charges'])
    allx=np.vstack([sources,targets]);allz=allx[:,0]+1j*allx[:,1];allq=np.r_[charges,np.zeros(len(targets))]
    dp,df=independent_direct(allz,allq);exact_p,exact_f=analytic_two_source(targets,*sources,*charges)
    metrics.update(analytic_direct_potential_error=maxabs(dp[2:]-exact_p),analytic_direct_field_error=maxabs(df[2:]-exact_f))
    center=.5+.5j;m=c['symmetry_particles'];radius=c['symmetry_radius'];ring=center+radius*np.exp(2j*np.pi*np.arange(m)/m)
    sp,sf,_=fmm(ring,np.ones(m),order,depth)
    # Exact radial field on a regular unit-charge polygon: (m-1)/(2R).
    expected=(m-1)/(2*radius)*np.column_stack((np.cos(2*np.pi*np.arange(m)/m),np.sin(2*np.pi*np.arange(m)/m)))
    metrics['symmetric_field_error']=maxabs(sf-expected)
    center=complex(*c['multipole_center']);m=c['multipole_sources'];radius=c['multipole_radius'];target=complex(*c['multipole_target'])
    ring=center+radius*np.exp(2j*np.pi*np.arange(m)/m)
    mp,mf,mops=fmm(np.r_[ring,target],np.r_[np.ones(m),0.],order,depth)
    ep,ef=analytic_regular_ring(target,center,radius,m)
    metrics.update(multipole_potential_error=abs(mp[-1]-ep),multipole_field_error=maxabs(mf[-1]-ef))
    checks={key:metrics[key]<=value for key,value in tol.items() if key!='coarse_control_field_error_min'}
    checks['coarse_control_detected']=metrics['coarse_control_field_error']>=tol['coarse_control_field_error_min'] and metrics['coarse_control_field_error']>tol['fine_field_error']
    checks.update(actual_m2l=ops['m2l_translations']>0,actual_l2l=ops['l2l_translations']>0,near_pairs_subset=ops['near_pairs']<ops['all_pairs'],multipole_probe_has_far_translation=mops['m2l_translations']>0)
    records += [dict(series='invariance',translation_potential_error=metrics['translation_potential_error'],translation_field_error=metrics['translation_field_error'],rotation_potential_error=metrics['rotation_potential_error'],rotation_field_error=metrics['rotation_field_error'],net_force=metrics['net_force_absolute']),dict(series='analytic_two_source',potential=dp[2:].tolist(),reference_potential=exact_p.tolist(),field=df[2:].tolist(),reference_field=exact_f.tolist()),dict(series='analytic_ring',potential=float(mp[-1]),reference_potential=ep,field=mf[-1].tolist(),reference_field=ef.tolist())]
    return result_case('fmm-convergence',checks,metrics,records)


def build_longrange_cases(config):
    refs,records=theta_references(config['ewald'])
    return [ewald_case(config['ewald'],refs,records),spme_case(config['spme'],config['ewald'],refs[-1][:2]),fmm_case(config['fmm'])]
