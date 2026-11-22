#!/usr/bin/env python3
"""Rebuild the fixed two-parameter Bratu inverse experiment without network."""
from pathlib import Path
import hashlib
import json
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import numart.bratu_multinverse as m


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def plain(value):
    if isinstance(value,np.ndarray):return value.tolist()
    if isinstance(value,dict):return {k:plain(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [plain(v) for v in value]
    if isinstance(value,(np.integer,np.floating,np.bool_)):return value.item()
    return value


def fit_record(fit):
    result=fit['result'];last=fit['history'][-1]
    assert fit['converged'],fit['reason']
    return dict(converged=fit['converged'],reason=fit['reason'],
        parameters=fit['parameters'],parameter_error_l2=float(np.linalg.norm(fit['parameters']-m.TRUTH)),
        objective=result['objective'],data_objective=result['data_objective'],penalty=result['penalty'],
        data_rms=result['data_rms'],predicted=result['predicted'],misfit=result['misfit'],
        gradient=result['gradient'],projected_gradient_inf=last['projected_gradient_inf'],
        primal_residual_l2=result['primal_residual_l2'],adjoint_residual_l2=result['adjoint_residual_l2'],
        adjoint_residual_relative_l2=result['adjoint_residual_relative_l2'],
        accepted_updates=len(fit['history'])-1,evaluations=fit['evaluations'],history=fit['history'])


def build():
    inputs=json.loads((ROOT/'inputs/synthetic-observations.json').read_text())
    positions=np.array(inputs['positions']);weights=np.array(inputs['weights'])
    data=np.array(inputs['reference_data']);noise=np.array(inputs['fixed_noise'])
    truth=np.array(inputs['truth']);prior=np.array(inputs['regularization_prior'])
    settings=dict(parameter_names=['a','b'],parameter_scales=[1.,1.],truth=truth,
        coefficient_model='lambda(x)=a+b*(2*x-1)',bounds=[[1.,2.8],[-.5,.5]],
        newton_tolerance_l2=1e-10,gradient_tolerance=1e-9,gradient_norm='unscaled projected-gradient infinity norm',
        optimizer_metric=[1.,100.],initial_step=10.,armijo_c=1e-4,backtrack_factor=.5,
        maximum_updates=1000,maximum_backtracks=50,regularization_matrix='2x2 identity',
        reference_grid=1023,reference_scaled_residual_inf_tolerance=2e-14,
        reference_correction_inf_tolerance=2e-13,rank_relative_tolerance=1e-10,
        interpretation='Fixed synthetic observations and lower branch; numerical reference uses the same second-order FD approximation with an independent tridiagonal Newton implementation. No analytic continuum, global uniqueness or statistical uncertainty claim.')
    observed=dict(positions=positions,weights=weights,reference_data=data,fixed_noise=noise,
        noisy_data=data+noise,same_grid_n=31,same_grid_data=inputs['same_grid_data'],
        regularization_prior=prior,central_priors=inputs['central_priors'],central_initial=inputs['central_initial'])
    refs=[m.fine_reference(n,truth) for n in [255,511,1023]]
    np.testing.assert_allclose(refs[-1]['predicted'],data,atol=1e-13,rtol=0)
    differences=[float(np.linalg.norm(refs[i]['predicted']-refs[i+1]['predicted'])) for i in range(2)]
    refinement=dict(grids=refs,consecutive_observation_difference_l2=differences,
        difference_ratio=differences[0]/differences[1],
        note='A numerical self-refinement diagnostic, not an exact error bound; the fixed 1023-node data retain reference-grid bias.')
    multistart=[]
    for initial in inputs['initial_guesses']:
        record=fit_record(m.fit_parameters(31,inputs['same_grid_data'],initial));record['initial']=initial
        multistart.append(record)
    grid=[]
    for n in [15,31,63,127]:
        record=fit_record(m.fit_parameters(n,data,[2.,0.]));record.update(n=n,h=1/(n+1))
        if grid:record['parameter_order']=float(np.log2(grid[-1]['parameter_error_l2']/record['parameter_error_l2']))
        grid.append(record)
    regularization=[]
    for gamma in inputs['regularization_gammas']:
        clean=fit_record(m.fit_parameters(63,data,[2.,0.],gamma=gamma,prior=prior))
        noisy=fit_record(m.fit_parameters(63,data+noise,[2.,0.],gamma=gamma,prior=prior))
        ref=m.objective_reference(63,data+noise,gamma=gamma,prior=prior)
        regularization.append(dict(gamma=gamma,prior=prior,clean=clean,noisy=noisy,
            perturbation_response_l2=float(np.linalg.norm(noisy['parameters']-clean['parameters'])),
            noisy_prior_distance_l2=float(np.linalg.norm(noisy['parameters']-prior)),
            objective_only_reference=ref,reference_parameter_difference=float(np.linalg.norm(noisy['parameters']-ref['parameters']))))
    full=m.sensitivity_diagnostic(31,truth)
    center=m.sensitivity_diagnostic(31,truth,positions=[.5])
    symmetric=m.sensitivity_diagnostic(31,[2.2,0.],positions=[.5],gamma=.01)
    boundary=m.sensitivity_diagnostic(31,truth,positions=[0.,1.],gamma=.01)
    positive=m.evaluate(31,truth,data)['state'];negative=m.evaluate(31,[truth[0],-truth[1]],data)['state']
    reflection=dict(parameters_positive=truth,parameters_negative=[truth[0],-truth[1]],
        reflected_state_max_error=float(np.max(abs(positive-negative[::-1]))),
        center_prediction_positive=float(positive[15]),center_prediction_negative=float(negative[15]),
        center_prediction_difference=float(abs(positive[15]-negative[15])))
    mirrors=[]
    for selected_prior in inputs['central_priors']:
        rec=fit_record(m.fit_parameters(31,data[2:3],inputs['central_initial'],positions=[.5],gamma=inputs['central_gamma'],prior=selected_prior))
        rec['prior']=selected_prior;rec['gamma']=inputs['central_gamma'];rec['initial']=inputs['central_initial']
        rec['diagnostic']=m.sensitivity_diagnostic(31,rec['parameters'],positions=[.5],gamma=inputs['central_gamma'])
        mirrors.append(rec)
    identifiability=dict(full=full,center=center,center_symmetric=symmetric,boundary=boundary,
        reflection=reflection,mirror_fits=mirrors,
        mirror_parameter_reflection_error=float(np.linalg.norm(mirrors[0]['parameters']-mirrors[1]['parameters']*[1.,-1.])),
        mirror_data_objective_difference=float(abs(mirrors[0]['data_objective']-mirrors[1]['data_objective'])))
    gradient_checks=[]
    for theta,gamma in [([1.3,-.3],0.),([2.1,.2],1e-4),([2.6,.4],1e-3)]:
        theta=np.array(theta);value=m.evaluate(31,theta,data,gamma=gamma,prior=prior)
        j,ft=m.derivatives(value['state'],theta);s=np.linalg.solve(j,-ft)
        direct=np.einsum('i,ij->j',value['objective_state'],s)+gamma*(theta-prior)
        fd=[];epsilon=1e-5
        for delta in epsilon*np.eye(2):
            plus=m.evaluate(31,theta+delta,data,gamma=gamma,prior=prior,gradient=False)['objective']
            minus=m.evaluate(31,theta-delta,data,gamma=gamma,prior=prior,gradient=False)['objective']
            fd.append((plus-minus)/(2*epsilon))
        gradient_checks.append(dict(parameters=theta,gamma=gamma,epsilon=epsilon,
            adjoint_gradient=value['gradient'],tangent_gradient=direct,finite_difference_gradient=fd,
            adjoint_tangent_max_error=float(np.max(abs(value['gradient']-direct))),
            adjoint_fd_max_error=float(np.max(abs(value['gradient']-fd))),
            primal_residual_l2=value['primal_residual_l2'],adjoint_residual_l2=value['adjoint_residual_l2']))
    theta=np.array([2.1,.2]);value=m.evaluate(31,theta,data,gamma=1e-4)
    sweep=[]
    for epsilon in np.logspace(-9,-1,25):
        fd=[]
        for delta in epsilon*np.eye(2):
            plus=m.evaluate(31,theta+delta,data,gamma=1e-4,gradient=False)['objective']
            minus=m.evaluate(31,theta-delta,data,gamma=1e-4,gradient=False)['objective']
            fd.append((plus-minus)/(2*epsilon))
        sweep.append(dict(epsilon=float(epsilon),component_errors=abs(np.array(fd)-value['gradient'])))
    # The landscape is data-only: regularization markers do not change these contours.
    a_axis=np.linspace(2.195,2.204,45);b_axis=np.linspace(-.5,.5,49)
    landscape=np.array([[m.evaluate(31,[a,b],data[2:3],positions=[.5],gradient=False)['data_objective'] for a in a_axis] for b in b_axis])
    fig,axes=plt.subplots(2,3,figsize=(16.2,9.8),layout='constrained')
    ax=axes[0,0]
    for rec in multistart:
        path=np.array([r['parameters'] for r in rec['history']]);ax.plot(path[:,0],path[:,1],'.-',ms=2,label='start '+str(rec['initial']))
    ax.plot(*truth,'k*',ms=11,label='Generating parameters')
    ax.set(xlabel='a',ylabel='b',title='Same-grid recovery: code consistency only');ax.legend(fontsize=8)
    ax=axes[0,1]
    for component,label in enumerate(['a component','b component']):
        ax.loglog([r['epsilon'] for r in sweep],[r['component_errors'][component] for r in sweep],'.-',label=label)
    ax.set(xlabel='Parameter perturbation epsilon',ylabel='Absolute gradient difference',title='Re-solved finite differences vs adjoint');ax.legend(fontsize=8)
    ax=axes[0,2]
    labels=['Five sensors\nb=0.35','Center only\nb=0','Center + gamma=0.01\nb=0'];spectra=[full['data_singular_values'],symmetric['data_singular_values'],symmetric['augmented_singular_values']]
    xs=np.arange(3)
    for k in range(2):
        values=[r[k] if r[k]>0 else np.nan for r in spectra];ax.bar(xs+(k-.5)*.28,values,.28,label='sigma '+str(k+1))
    ax.text(1.14,1.4e-5,'zero',ha='center',fontsize=8)
    ax.set_yscale('log');ax.set_ylim(6e-6,.45);ax.set_xticks(xs,labels,fontsize=8)
    ax.set(ylabel='Singular value (parameter scales = 1)',title='Penalty curvature adds no data rank');ax.legend(fontsize=8)
    ax=axes[1,0];hs=np.array([r['h'] for r in grid]);es=np.array([r['parameter_error_l2'] for r in grid])
    ax.loglog(hs,es,'o-',label='Fixed 1023-node observations')
    ax.loglog(hs,es[0]*(hs/hs[0])**2,'--',label='Slope 2 reference')
    ax.set(xlabel='Inverse grid spacing h',ylabel='Parameter error norm',title='Fine-grid data retain a numerical reference floor');ax.legend(fontsize=8)
    ax=axes[1,1];gammas=np.array(inputs['regularization_gammas'])
    base_response=regularization[0]['perturbation_response_l2'];base_error=regularization[0]['noisy']['parameter_error_l2']
    ax.plot(gammas,[r['perturbation_response_l2']/base_response for r in regularization],'o-',label='Perturbation response / unpenalized')
    ax.plot(gammas,[r['noisy']['parameter_error_l2']/base_error for r in regularization],'s-',label='Parameter error / unpenalized')
    ax.set_xscale('symlog',linthresh=1e-6);ax.set_yscale('log')
    ax.set(xlabel='Regularization gamma',ylabel='Relative quantity',title='Stability and prior bias are distinct');ax.legend(fontsize=8)
    ax=axes[1,2];contour=ax.contourf(a_axis,b_axis,np.log10(np.maximum(landscape,1e-18)),levels=20,cmap='viridis')
    for rec,marker in zip(mirrors,['o','s']):ax.plot(*rec['parameters'],marker,color='white',ms=7,label='prior b='+str(rec['prior'][1]))
    ax.set(xlabel='a',ylabel='b',title='Center-only data: a curve of indistinguishable fits');ax.legend(fontsize=8)
    fig.colorbar(contour,ax=ax,label='log10(data objective)')
    for ax in axes.flat:ax.grid(alpha=.18)
    fig.suptitle('Bratu inverse problem: two coefficient parameters, regularization and identifiability\nFixed smaller-solution branch; data rank, penalty curvature and parameter error are separate diagnostics',fontsize=14)
    output=ROOT/'docs/figures';output.mkdir(parents=True,exist_ok=True)
    fig.savefig(output/'bratu-multinverse.png',dpi=125,metadata={'Software':'Numerical Methods Atlas'});plt.close(fig)
    sources=['numart/bratu_multinverse.py','numart/bratu_inverse.py','numart/bratu_sensitivity.py','numart/autodiff.py','numart/krylov.py','scripts/build_bratu_multinverse.py','tests/test_bratu_multinverse.py','inputs/synthetic-observations.json']
    evidence=dict(schema_version=1,settings=settings,observations=observed,reference_refinement=refinement,
        multistart=multistart,grid_runs=grid,regularization_runs=regularization,
        identifiability=identifiability,gradient_checks=gradient_checks,gradient_sweep=sweep,
        center_data_landscape=dict(a=a_axis,b=b_axis,data_objective=landscape),
        source_sha256={name:sha(ROOT/name) for name in sources},
        artifact_sha256={'docs/figures/bratu-multinverse.png':sha(output/'bratu-multinverse.png')})
    (output/'bratu-multinverse.json').write_text(json.dumps(plain(evidence),sort_keys=True,separators=(',',':'),allow_nan=False)+'\n')
    print(json.dumps(plain(dict(multistart=[r['parameters'] for r in multistart],grid=[r['parameters'] for r in grid],regularization=[dict(gamma=r['gamma'],parameters=r['noisy']['parameters'],error=r['noisy']['parameter_error_l2'],response=r['perturbation_response_l2']) for r in regularization],reference_refinement=differences,gradient_fd_max=max(r['adjoint_fd_max_error'] for r in gradient_checks))),indent=2))


if __name__=='__main__':build()
