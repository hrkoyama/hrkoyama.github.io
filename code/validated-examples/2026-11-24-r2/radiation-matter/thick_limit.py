"""Actual-stencil, exact-time semidiscrete matched thick-limit control.

A limited periodic single Fourier mode, not a replacement for the existing
SSPRK2 transient calculations. No fixed-grid asymptotic-preserving claim.
"""
from pathlib import Path
import json,hashlib
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import expm_multiply
import transport
from references.thick_reference import discrete_upwind_matrix,diffusion_amplitudes


def physical_rhs(I,V,mu,w,h,kappa,epsilon):
    a,b,_=transport.rhs(I,V,mu,w,kappa*h,epsilon,np.zeros_like(V),periodic=True)
    return kappa*a,kappa*b


def matrix_from_real_probes(mu,w,h,kappa,epsilon):
    m=len(mu);A=np.zeros((m+1,m+1),complex);x=(np.arange(5)-2)*h
    for column in range(m+1):
        responses=[]
        for basis in [np.cos(x),np.sin(x)]:
            I=np.zeros((m,5));V=np.zeros(5)
            if column<m:I[column]=basis
            else:V[:]=basis
            a,b=physical_rhs(I,V,mu,w,h,kappa,epsilon);responses.append(np.r_[a[:,2],b[2]])
        A[:,column]=responses[0]+1j*responses[1]
    return A


def reconstruct(amplitude,x,background=1.):
    return background+amplitude.real[...,None]*np.cos(x)-amplitude.imag[...,None]*np.sin(x)


def single_mode(kappa,cells,scaled_times,epsilon=1.,number=32,base_amplitude=.1,partial=None):
    h=2*np.pi/cells;x=(np.arange(cells)+.5)*h;mu,w=transport.angles(number);initial_amplitude=base_amplitude*np.sinc(h/(2*np.pi));A=matrix_from_real_probes(mu,w,h,kappa,epsilon)
    initial=np.full(number+1,initial_amplitude,dtype=complex);times=kappa*np.asarray(scaled_times);amplitudes=[];intensities=[];materials=[];derivatives=[];stage='matrix-built'
    try:
        for time in times:
            stage='expm';a=initial.copy() if time==0 else expm_multiply(csr_matrix(time*A),initial,traceA=time*np.trace(A))
            amplitudes.append(a);intensities.append(reconstruct(a[:-1],x));materials.append(reconstruct(a[-1],x));derivatives.append(np.einsum('ij,j->i',A,a,optimize=False))
            if partial is not None:np.savez(partial,generator=A,amplitudes=np.array(amplitudes),intensity=np.array(intensities),material=np.array(materials),completed_times=times[:len(amplitudes)],stage=stage)
    except Exception:
        if partial is not None:np.savez(partial,generator=A,amplitudes=np.array(amplitudes),intensity=np.array(intensities),material=np.array(materials),completed_times=times[:len(amplitudes)],stage=stage)
        raise
    amplitudes=np.array(amplitudes);I=np.array(intensities);V=np.array(materials);E=.5*np.sum(w[None,:,None]*I,axis=1);F=.5*np.sum((w*mu)[None,:,None]*I,axis=1)
    moment=np.stack([.5*np.sum(w[None,:]*amplitudes[:,:-1],axis=1),amplitudes[:,-1],.5*np.sum((w*mu)[None,:]*amplitudes[:,:-1],axis=1)],axis=-1)
    residual=0.;rhs_budget=0.
    for i in range(len(times)):
        a,b=physical_rhs(I[i],V[i],mu,w,h,kappa,epsilon);expected=reconstruct(np.array(derivatives)[i],x,background=0.)
        residual=max(residual,float(np.max(abs(np.r_[a,b[None,:]]-expected)))/max(1.,kappa*initial_amplitude))
        rhs_budget=max(rhs_budget,float(abs(h*np.sum(epsilon*.5*np.sum(w[:,None]*a,axis=0)+b))))
    return dict(x=x,mu=mu,weights=w,times=times,scaled_times=np.asarray(scaled_times),kappa=np.array(kappa),cells=np.array(cells),epsilon=np.array(epsilon),initial_amplitude=np.array(initial_amplitude),generator=A,amplitudes=amplitudes,moment_amplitudes=moment,intensity=I,material=V,energy=E,flux=F,semidiscrete_residual=np.array(residual),actual_rhs_budget=np.array(rhs_budget),kind=np.array('time-exact-semidiscrete-FV-SN-Fourier-control'))


def scaled_error(left,right,kappa,amplitude):
    weight=np.array([1.,1.,kappa]);return np.max(abs(left-right)*weight/amplitude,axis=-1)


def execute_control(cfg,limits,target,output,root,check,checkpoint,cases):
    q=json.loads((root/'references/qualification-thick.json').read_text())
    if q['passed'] is not True or not q['checks'] or not all(type(v) is bool and v for v in q['checks'].values()):raise ValueError('Unqualified matched-thick reference')
    cache=root/'references/matched-thick-reference.npz'
    if hashlib.sha256(cache.read_bytes()).hexdigest()!=q['reference_cache_sha256']:raise ValueError('Changed matched-thick reference cache')
    with np.load(cache,allow_pickle=False) as f:reference={key:f[key] for key in f.files}
    if not np.array_equal(reference['kappa'],cfg['kappa']) or not np.array_equal(reference['scaled_times'],cfg['scaled_times']):raise ValueError('Matched-thick reference input mismatch')
    original_checks=dict(target['checks']);target['passed']=False
    rows=[];summary=[];progress=dict(mode_records=rows,physical_mode_evolutions_completed=0,status='in-progress')
    target['metrics']['matched_thick_limit_control']=progress;checkpoint(output,cases)
    for j,(kappa,cells) in enumerate(zip(cfg['kappa'],cfg['cells'])):
        name='su-olson-transport1997-thick-k'+str(kappa);out=single_mode(kappa,cells,cfg['scaled_times'],cfg['epsilon'],cfg['ordinates'],cfg['amplitude'],output/(name+'-candidate.npz'));np.savez_compressed(output/(name+'.npz'),**out)
        amp=float(out['initial_amplitude']);moment=out['moment_amplitudes'];c32=amp*reference['moments_hemisphere32'][j];c128=amp*reference['moments_GL128'][j]
        diffusion=np.array([diffusion_amplitudes(amp,s,kappa,cfg['epsilon']) for s in cfg['scaled_times']]);space=scaled_error(moment,c32,kappa,amp);angular=scaled_error(c32,c128,kappa,amp);continuum=np.max(abs(c128[:,:2]-diffusion[:,:2])/amp,axis=1);joint=np.max(abs(moment[:,:2]-diffusion[:,:2])/amp,axis=1);flux=abs(moment[:,2]-diffusion[:,2])*kappa/amp
        analytic=discrete_upwind_matrix(out['mu'],out['weights'],kappa,2*np.pi/cells,cfg['epsilon']);matrix_residual=float(np.max(abs(out['generator']-analytic)))/max(1.,kappa)
        energy=2*np.pi/cells*np.sum(cfg['epsilon']*out['energy']+out['material'],axis=1);budget=max(float(np.max(abs(energy-2*np.pi*(cfg['epsilon']+1)))),float(out['actual_rhs_budget']))
        minimum=float(min(out['intensity'].min(),out['material'].min()));finite=all(np.isfinite(out[key]).all() for key in ['intensity','material','energy','flux','amplitudes','generator'])
        h=2*np.pi/cells
        row=dict(id=name,kind='matched-thick-semidiscrete-mode-control',fields=name+'.npz',kappa=kappa,cells=cells,ordinates=cfg['ordinates'],mean_free_path=1/kappa,kappa_h=kappa*h,times=out['times'].tolist(),scaled_times=cfg['scaled_times'],initial_cellmean_amplitude=amp,final_FV_space_error=float(space[-1]),final_continuum_limit_error=float(continuum[-1]),final_joint_energy_error=float(joint[-1]),final_joint_scaled_flux_error=float(flux[-1]),maximum_angular_sensitivity=float(angular.max()),maximum_budget=budget,matrix_residual=matrix_residual,semidiscrete_global_RHS_residual=float(out['semidiscrete_residual']))
        out.update(reference_continuum_hemisphere32=c32,reference_continuum_GL128=c128,analytic_diffusion_amplitudes=diffusion,space_errors=space,angular_errors=angular,continuum_limit_errors=continuum,joint_energy_errors=joint,joint_scaled_flux_errors=flux)
        np.savez_compressed(output/(name+'.npz'),**out)
        series=np.array([[kappa,cells,s,t,space[i],angular[i],continuum[i],joint[i],flux[i],energy[i]] for i,(s,t) in enumerate(zip(cfg['scaled_times'],out['times']))]);np.savetxt(output/(name+'.csv'),series,delimiter=',',header='kappa,cells,scaled_time,physical_time,FV_space,angular,continuum_limit,joint_energy,joint_scaled_flux,weighted_energy',comments='',fmt='%.16e')
        prefix='thick/'+str(kappa)+'/'
        check(target,prefix+'finite-positive-fields',minimum,0.,finite and minimum>=0.)
        check(target,prefix+'periodic-weighted-energy',budget,limits['thick_budget'],budget<=limits['thick_budget'])
        residual=max(matrix_residual,float(out['semidiscrete_residual']));check(target,prefix+'actual-stencil-and-global-RHS',residual,limits['thick_operator_relative'],residual<=limits['thick_operator_relative'])
        check(target,prefix+'separate-FV-space-error',float(space.max()),limits['thick_space_error'],space.max()<=limits['thick_space_error'])
        check(target,prefix+'separate-angular-sensitivity',float(angular.max()),limits['thick_angular_error'],angular.max()<=limits['thick_angular_error'])
        initial_flux=float(np.max(abs(out['flux'][0]))*kappa/amp);fick_initial=abs(diffusion[0,2])*kappa/amp
        check(target,prefix+'physical-initial-layer-retained',dict(actual_scaled_flux=initial_flux,nonzero_Fick_scaled_amplitude=float(fick_initial)),dict(zero_flux_tolerance=limits['thick_initial_flux_zero'],Fick_amplitude=1/3),initial_flux<=limits['thick_initial_flux_zero'] and fick_initial>.3)
        check(target,prefix+'mean-free-path-resolved',kappa*h,np.pi/16,kappa*h<=np.pi/16)
        rows.append(row);progress['physical_mode_evolutions_completed']=len(rows);summary.append([kappa,cells,*[row[key] for key in ['final_FV_space_error','maximum_angular_sensitivity','final_continuum_limit_error','final_joint_energy_error','final_joint_scaled_flux_error']]])
        checkpoint(output,cases)
    for previous,current in zip(rows,rows[1:]):
        for field,label,bound in [('final_FV_space_error','space',limits['thick_space_ratio']),('final_continuum_limit_error','continuum-limit',limits['thick_continuum_ratio'])]:
            if previous[field]<=0:raise ArithmeticError('Unresolved separate asymptotic error; no fitted replacement window')
            ratio=current[field]/previous[field];check(target,'thick/'+label+'/k'+str(current['kappa']),ratio,bound,ratio<=bound)
    final=rows[-1];check(target,'thick/finest-energy-limit',final['final_joint_energy_error'],limits['thick_finest_energy'],final['final_joint_energy_error']<=limits['thick_finest_energy'])
    check(target,'thick/finest-scaled-flux-limit',final['final_joint_scaled_flux_error'],limits['thick_finest_flux'],final['final_joint_scaled_flux_error']<=limits['thick_finest_flux'])
    wrong_sign=abs(moment[-1,2]+diffusion[-1,2])*kappa/amp;check(target,'thick/wrong-flux-sign-negative-control',final['final_joint_scaled_flux_error'],limits['thick_negative_advantage']*float(wrong_sign),final['final_joint_scaled_flux_error']<=limits['thick_negative_advantage']*wrong_sign)
    wrong_D=diffusion_amplitudes(amp,cfg['scaled_times'][-1],kappa,cfg['epsilon'],factor=1.)
    wrong_energy=float(np.max(abs(moment[-1,:2]-wrong_D[:2]))/amp);check(target,'thick/missing-one-third-negative-control',final['final_joint_energy_error'],limits['thick_negative_advantage']*wrong_energy,final['final_joint_energy_error']<=limits['thick_negative_advantage']*wrong_energy)
    target['metrics']['matched_thick_limit_control']=dict(physical_mode_evolutions=3,mode_records=rows,reference_checks=q['check_count'],same_operator='kappa times actualtransport.rhs withkappa*h,bothrates',time_role='Exact-time semidiscrete Fourier control; originalSSPRK2tests/transientruns separate',reference_role='Independentcontinuum-space angularmatrixGL64/128plusDOP853qualifiers;sharedSciPysparseexpm_multiplydeclared',diffusion='D_rad1/(3kappa),D_eff1/[3kappa(epsilon+1)],matchedperiodiccellmeanIC',scope='ResolvedjointN~kappa^2limit; nofixed-gridAPorSSPRK2temporal-orderclaim. Initiallayerreportedallfourtimes;asymptoticgatesfinals.25only;nojointorderfit.')
    np.savetxt(output/'su-olson-transport1997-thick-summary.csv',np.array(summary),delimiter=',',header='kappa,cells,FV_space,angular,continuum_limit,joint_energy,joint_scaled_flux',comments='',fmt='%.16e')
    if len(target['checks'])-len(original_checks)!=29 or any(target['checks'].get(k)!=v for k,v in original_checks.items()):raise ArithmeticError('Changed original checks or wrong fixed thick gate inventory')
    target['passed']=bool(all(target['checks'].values()));checkpoint(output,cases)
