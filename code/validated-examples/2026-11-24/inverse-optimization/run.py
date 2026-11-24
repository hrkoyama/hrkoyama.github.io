#!/usr/bin/env python3
"""Fixed75-fit inverse/optimization supplement; saved references are mandatory."""
import argparse
import json
from pathlib import Path
import time
import traceback

import numpy as np

from least_squares import legacy_projected, library_least_squares, own_least_squares
from model import BratuModel, canonical_box, observe_legacy
from public_contract import check_generated_csv, validate_result
from quasi_newton import library_quasi_newton, own_quasi_newton, quadratic, rosenbrock
from references.oracles import context_specification
from references.qualify import BOUND_SOURCES
from regularization import (fixed_gamma_covariance, fixed_noise, lcurve_chord_curvature,
                            scalar_2x2_statistics, select_discrepancy)
from support import (DecisionBook, Retainer, digest, numeric_csv, plain,
                     projected_gradient, relative_error, write_json)

ROOT = Path(__file__).resolve().parent
CASE_IDS = ['bratu-gn-lm-bounds', 'bfgs-lbfgs-controls', 'bratu-noise-regularization']


def load_reference(input_path):
    directory = ROOT/'references/cache'
    qualification = json.loads((directory/'qualification.json').read_text())
    if (qualification.get('passed') is not True or qualification.get('gate_count') != 48 or
            len(qualification.get('checks', {})) != 48 or
            not all(v is True for v in qualification['checks'].values())):
        raise ValueError('Reference qualification is incomplete or failed')
    if qualification['input_sha256'] != digest(input_path) or qualification['acceptance_sha256'] != digest(ROOT/'acceptance.json'):
        raise ValueError('Reference inputs or acceptance changed')
    if set(qualification['source_sha256']) != set(BOUND_SOURCES):
        raise ValueError('Reference source dependency inventory changed')
    for name, expected in qualification['source_sha256'].items():
        if digest(ROOT/name) != expected:
            raise ValueError('Reference source dependency changed: '+name)
    if digest(directory/'cache-fields.npz') != qualification['fields_sha256']:
        raise ValueError('Reference field bytes changed')
    with np.load(directory/'cache-fields.npz', allow_pickle=False) as data:
        fields = {name: data[name].copy() for name in data.files}
    return qualification, fields


def qualified_solver(answer):
    if answer.get('library_success') is not None:
        return bool(answer['library_success'] or
                    answer['reason'] == 'EXTERNALLY_STATIONARY_LIBRARY_FAILURE_RETAINED')
    return bool(answer['converged'])


def save_least_squares(answer, model, retainer):
    value, history = answer['result'], answer['history']
    # Completed candidates are durable before rank, KKT, reference or covariance work.
    retainer.raw('completed-fit-before-any-acceptance', **answer)
    return retainer.arrays('fit', parameters=answer['parameters'], state=value['state'],
                           gradient=value['gradient'], data_jacobian=value['data_jacobian'],
                           predicted=value['predicted'], misfit=value['misfit'],
                           objective=value['objective'], gamma=model.gamma,
                           path=np.asarray([row['parameters'] for row in history]),
                           path_objective=np.asarray([row['objective'] for row in history]))


def fit_least_squares(model, method, initial, scales, cfg):
    if method in ('gn', 'lm'):
        return own_least_squares(model, method, initial, scales, cfg['case65']['own_controls'])
    if method == 'legacy-pg':
        return legacy_projected(model, initial, cfg['bratu']['box'], cfg['case65']['legacy_pg_controls'])
    return library_least_squares(model, method, initial, scales, cfg['bratu']['box'],
                                 cfg['case65']['scipy_controls'])


def run_case65(cfg, limits, reference, output):
    book, records, csv_rows = DecisionBook(), [], []
    lo, hi, _ = canonical_box(cfg['bratu']['box'])
    attempted = 0
    for context_index in range(4):
        s = context_specification(cfg, context_index, reference['active_data'])
        for method_index, method in enumerate(s['methods']):
            prefix = 'fit-'+str(attempted)
            retainer = Retainer(output, 'case65-'+str(attempted).zfill(2))
            attempted += 1
            try:
                model = BratuModel(s['n'], s['data'], s['positions'], s['weights'],
                                   s['gamma'], s['prior'], retainer)
                with observe_legacy(retainer):
                    answer = fit_least_squares(model, method, cfg['bratu']['initial'], s['scales'], cfg)
                    artifact = save_least_squares(answer, model, retainer)
                    rank, singular, augmented = model.rank(answer['parameters'])
                value, theta = answer['result'], answer['parameters']
                bounded = method in ('legacy-pg', 'scipy-trf')
                stationarity = (projected_gradient(theta, value['gradient'], lo, hi) if bounded else
                                float(np.linalg.norm(value['gradient'], ord=np.inf)))
                gap = abs(value['objective']-float(reference[f'context_{context_index}_objective']))
                gap_limit = limits['reference_objective_gap_relative']*(1.+abs(float(reference[f'context_{context_index}_objective'])))
                violation = float(max(0., np.max(lo-theta), np.max(theta-hi)))
                row = dict(context=s['id'], method=method, parameters=theta,
                           objective=value['objective'], stationarity_inf=stationarity,
                           stationarity_kind='physical-projected' if bounded else 'physical-unbounded',
                           final_primal_residual_l2=value['primal_residual_l2'],
                           data_rank=rank, data_singular_values=singular,
                           augmented_singular_values=augmented, objective_reference_gap=gap,
                           box_violation=violation, gamma=s['gamma'], scales=s['scales'],
                           forward_evaluations=retainer.forward_calls, artifact=artifact,
                           solver_reason=answer['reason'], solver_converged=answer['converged'],
                           library_success=answer['library_success'], library_status=answer['library_status'],
                           library_message=answer['library_message'], nfev=answer['nfev'], njev=answer['njev'])
                row['linear_subproblem_solves']=answer.get('linear_subproblem_solves')
                records.append(plain(row))
                book.add(prefix+'-complete', qualified_solver(answer), answer['reason'])
                book.add(prefix+'-final-forward-residual', value['primal_residual_l2'] <= limits['forward_residual_l2'],
                         value['primal_residual_l2'], limits['forward_residual_l2'])
                book.add(prefix+'-stationary', stationarity <= limits['external_physical_stationarity_inf'],
                         stationarity, limits['external_physical_stationarity_inf'])
                book.add(prefix+'-objective-reference', gap <= gap_limit, gap, gap_limit)
                rank_ok = rank <= 1 if context_index == 3 else rank == 2
                book.add(prefix+'-data-rank', rank_ok, rank, '<=1' if context_index == 3 else 2)
                if bounded:
                    book.add(prefix+'-feasible', violation <= limits['box_violation'], violation, limits['box_violation'])
                if context_index == 2:
                    distance = float(np.min(np.minimum(abs(theta-lo), abs(theta-hi))))
                    book.add(prefix+'-active-constraint', distance <= 1e-6, distance, 1e-6)
                csv_rows.append([context_index, method_index, *theta, value['objective'], stationarity,
                                 value['primal_residual_l2'], rank, s['gamma'], retainer.forward_calls])
                numeric_csv(output/'case65-fits.csv',
                            ['context_index','method_index','a','b','objective','physical_stationarity_inf',
                             'final_primal_residual_l2','data_rank','gamma','forward_evaluations'], csv_rows)
            except Exception as error:
                retainer.raw('failed-fit', type=type(error).__name__, message=str(error), traceback=traceback.format_exc())
                records.append(dict(context=s['id'], method=method, failed=True,
                                    failure={'type':type(error).__name__, 'message':str(error)}))
                if prefix+'-complete' not in book.checks:
                    book.add(prefix+'-complete', False, str(error))
                else:
                    book.add(prefix+'-unexpected-diagnostic-failure', False, str(error))
    complete = [row for row in records if not row.get('failed')]
    metrics = dict(attempted_fits=attempted, completed_fits=len(complete), expected_fits=17,
                   forward_evaluations=sum(row['forward_evaluations'] for row in complete),
                   maximum_stationarity_inf=max((row['stationarity_inf'] for row in complete), default=0.),
                   reference_scope='independent Thomas state/Jacobian; shared local TRF optimizer; no global optimum proof')
    return dict(id=CASE_IDS[0], passed=bool(attempted==len(complete)==17 and all(book.checks.values())),
                checks=book.checks, check_details=book.details, records=records, metrics=metrics)


def run_case66(cfg, limits, output):
    book, records, csv_rows = DecisionBook(), [], []
    spec = cfg['case66']
    problems = [('quadratic', spec['quadratic']['initial'], quadratic)] + [
        ('rosenbrock-'+str(i), initial, rosenbrock) for i, initial in enumerate(spec['rosenbrock']['initials'])]
    attempted = 0
    for problem_index, (problem, initial, function) in enumerate(problems):
        for method_index, method in enumerate(spec['methods']):
            prefix = 'fit-'+str(attempted)
            retainer = Retainer(output, 'case66-'+str(attempted).zfill(2))
            attempted += 1
            try:
                answer = (own_quasi_newton(function, initial, method, spec['controls'], retainer)
                          if method in ('bfgs','lbfgs-m3') else
                          library_quasi_newton(function, initial, method, spec['controls'], retainer))
                retainer.raw('completed-fit-before-analytic-reference', **answer)
                artifact = retainer.arrays('fit', parameters=answer['parameters'], gradient=answer['gradient'],
                                           objective=answer['objective'],
                                           path=[row['parameters'] for row in answer['history']],
                                           path_objective=[row['objective'] for row in answer['history']],
                                           path_gradient_inf=[row['gradient_inf'] for row in answer['history']],
                                           path_calls=[row['objective_calls'] for row in answer['history']])
                point = np.asarray(spec['quadratic']['x_star'] if problem_index==0 else [1.,1.])
                point_error = (float(np.linalg.norm(answer['parameters']-point)/max(1.,np.linalg.norm(point)))
                               if problem_index==0 else float(np.linalg.norm(answer['parameters']-point,ord=np.inf)))
                gradient = float(np.linalg.norm(answer['gradient'], ord=np.inf))
                p_limit = limits['quadratic_point_relative'] if problem_index==0 else limits['rosenbrock_point_inf']
                g_limit = limits['quadratic_gradient_inf'] if problem_index==0 else limits['rosenbrock_gradient_inf']
                records.append(plain(dict(problem=problem, method=method, parameters=answer['parameters'],
                                          objective=answer['objective'], gradient_inf=gradient, point_error=point_error,
                                          objective_evaluations=answer['objective_calls'], artifact=artifact,
                                          steps=answer['steps'], solver_reason=answer['reason'],
                                          solver_converged=answer['converged'], library_success=answer['library_success'],
                                          library_status=answer['library_status'], library_message=answer['library_message'],
                                          nfev=answer['nfev'], njev=answer['njev'])))
                records[-1].update(dense_oracle_actions=answer['dense_oracle_actions'],
                                    primary_inverse_matrix_scalars=answer['primary_inverse_matrix_scalars'],
                                    maximum_retained_pair_scalars=answer['maximum_retained_pair_scalars'],
                                    reference_dense_matrix_scalars=answer['reference_dense_matrix_scalars'])
                book.add(prefix+'-complete', qualified_solver(answer), answer['reason'])
                book.add(prefix+'-point', point_error<=p_limit, point_error,p_limit)
                book.add(prefix+'-gradient', gradient<=g_limit,gradient,g_limit)
                if problem_index != 0:
                    book.add(prefix+'-objective', answer['objective']<=limits['rosenbrock_objective'],
                             answer['objective'],limits['rosenbrock_objective'])
                if method in ('bfgs','lbfgs-m3'):
                    steps = answer['steps']
                    book.add(prefix+'-strong-wolfe', bool(steps) and all(s['wolfe_armijo'] and s['wolfe_curvature'] for s in steps), len(steps))
                    book.add(prefix+'-resolved-curvature', bool(steps) and all(s['curvature']>s['curvature_guard'] for s in steps),
                             min((s['curvature']-s['curvature_guard'] for s in steps),default=0.))
                    if method=='bfgs':
                        antisymmetry=max((s['inverse_antisymmetry'] for s in steps),default=0.)
                        minimum=min((s['minimum_eigenvalue'] for s in steps),default=0.)
                        book.add(prefix+'-inverse-symmetry',antisymmetry<=limits['bfgs_symmetry_relative'],antisymmetry,limits['bfgs_symmetry_relative'])
                        book.add(prefix+'-inverse-spd',minimum>0,minimum,0.)
                    else:
                        defect=max((s['dense_direction_relative'] for s in steps),default=0.)
                        book.add(prefix+'-retained-dense-oracle',defect<=limits['lbfgs_dense_direction_relative'],defect,limits['lbfgs_dense_direction_relative'])
                csv_rows.append([problem_index,method_index,answer['objective'],gradient,point_error,answer['objective_calls']])
                numeric_csv(output/'case66-fits.csv',['problem_index','method_index','objective','gradient_inf','point_error','objective_evaluations'],csv_rows)
            except Exception as error:
                retainer.raw('failed-fit',type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
                records.append(dict(problem=problem,method=method,failed=True,failure={'type':type(error).__name__,'message':str(error)}))
                if prefix+'-complete' not in book.checks:
                    book.add(prefix+'-complete',False,str(error))
                else:
                    book.add(prefix+'-unexpected-diagnostic-failure',False,str(error))
    complete=[row for row in records if not row.get('failed')]
    return dict(id=CASE_IDS[1],passed=bool(attempted==len(complete)==16 and all(book.checks.values())),
                checks=book.checks,check_details=book.details,records=records,
                metrics=dict(attempted_fits=attempted,completed_fits=len(complete),expected_fits=16,
                             objective_evaluations=sum(row['objective_evaluations'] for row in complete),
                             maximum_gradient_inf=max((row['gradient_inf'] for row in complete),default=0.),
                             independent_target='known analytic minima; current-scaling retained-pair dense action'))


def run_case67(cfg, limits, output):
    spec, b = cfg['case67'],cfg['bratu']
    book, fits, csv_rows, path_records = DecisionBook(),[],[],[]
    lo,hi,_=canonical_box(b['box'])
    base=fixed_noise(spec['seeds'])
    np.savez_compressed(output/'case67-base-noise.npz',**{'seed_'+str(k):v for k,v in base.items()})
    attempted=0

    def fit(context_index,sigma_index,seed_index,gamma_index,data,gamma):
        nonlocal attempted
        prefix='fit-'+str(attempted)
        retainer=Retainer(output,'case67-'+str(attempted).zfill(2))
        attempted+=1
        try:
            model=BratuModel(31,data,b['positions'],b['weights'],gamma,b['prior'],retainer)
            with observe_legacy(retainer):
                answer=library_least_squares(model,'scipy-trf',b['initial'],[1.,1.],b['box'],cfg['case65']['scipy_controls'])
                artifact=save_least_squares(answer,model,retainer)
                rank,singular,_=model.rank(answer['parameters'])
            value,theta=answer['result'],answer['parameters']
            stationarity=projected_gradient(theta,value['gradient'],lo,hi)
            violation=float(max(0.,np.max(lo-theta),np.max(theta-hi)))
            qualified=bool(qualified_solver(answer) and stationarity<=limits['external_physical_stationarity_inf']
                           and violation<=limits['box_violation'] and value['primal_residual_l2']<=limits['forward_residual_l2'])
            record=plain(dict(context_index=context_index,sigma_index=sigma_index,seed_index=seed_index,
                              gamma_index=gamma_index,gamma=gamma,parameters=theta,objective=value['objective'],
                              weighted_residual_norm=float(np.sqrt(np.sum(np.asarray(b['weights'])*value['misfit']**2))),
                              parameter_deviation_norm=float(np.linalg.norm(theta-np.asarray(b['prior']))),
                              physical_projected_gradient_inf=stationarity,final_primal_residual_l2=value['primal_residual_l2'],
                              box_violation=violation,qualified=qualified,data_rank=rank,data_singular_values=singular,
                              forward_evaluations=retainer.forward_calls,data_jacobian=value['data_jacobian'],
                              solver_reason=answer['reason'],library_success=answer['library_success'],
                              library_status=answer['library_status'],library_message=answer['library_message'],
                              nfev=answer['nfev'],njev=answer['njev'],artifact=artifact))
            fits.append(record)
            write_json(output/'case67-all-fits.partial.json',fits)
            book.add(prefix+'-complete',qualified_solver(answer),answer['reason'])
            book.add(prefix+'-final-forward-residual',value['primal_residual_l2']<=limits['forward_residual_l2'],value['primal_residual_l2'],limits['forward_residual_l2'])
            book.add(prefix+'-stationary',stationarity<=limits['external_physical_stationarity_inf'],stationarity,limits['external_physical_stationarity_inf'])
            book.add(prefix+'-feasible',violation<=limits['box_violation'],violation,limits['box_violation'])
            csv_rows.append([context_index,sigma_index,seed_index,gamma_index,gamma,*theta,value['objective'],stationarity,record['weighted_residual_norm'],retainer.forward_calls])
            numeric_csv(output/'case67-fits.csv',['context_index','sigma_index','seed_index','gamma_index','gamma','a','b','objective','physical_projected_gradient_inf','weighted_residual_norm','forward_evaluations'],csv_rows)
            return record
        except Exception as error:
            retainer.raw('failed-fit',type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
            record=dict(context_index=context_index,sigma_index=sigma_index,seed_index=seed_index,
                        gamma_index=gamma_index,gamma=gamma,qualified=False,failed=True,
                        failure={'type':type(error).__name__,'message':str(error)})
            fits.append(record)
            write_json(output/'case67-all-fits.partial.json',fits)
            if prefix+'-complete' not in book.checks:
                book.add(prefix+'-complete',False,str(error))
            else:
                book.add(prefix+'-unexpected-diagnostic-failure',False,str(error))
            return record

    for context_index in range(2):
        clean=np.asarray(cfg['legacy_data']['same_grid_data'] if context_index==0 else cfg['legacy_data']['fine_1023_data'])
        for sigma_index,sigma in enumerate(spec['noise_sigmas']):
            for seed_index,seed in enumerate(spec['seeds']):
                noise=sigma*base[int(seed)]
                data=clean+noise
                rows=[fit(context_index,sigma_index,seed_index,j,data,float(gamma))
                      for j,gamma in enumerate(spec['gamma_values'])]
                path_index=len(path_records)
                noise_norm=float(np.sqrt(np.sum(np.asarray(b['weights'])*noise**2)))
                selection=select_discrepancy(rows,spec['gamma_values'],noise_norm,limits['discrepancy_factor'])
                write_json(output/'case67-current-path-before-statistics.json',
                           dict(path_index=path_index,rows=rows,selection=selection,noise_norm=noise_norm))
                completed=all(row.get('qualified',False) for row in rows)
                independently_admitted=[row['gamma'] for row in rows if row.get('qualified') and
                                        row['weighted_residual_norm']<=1.05*noise_norm]
                expected=(max(independently_admitted) if independently_admitted else None) if completed else None
                book.add(f'path-{path_index}-complete',completed,len(rows),5)
                book.add(f'path-{path_index}-selection',selection['selected_gamma']==expected and
                         ((selection['status']=='SELECTED')==(expected is not None)),selection,expected)
                selected=next((row for row in rows if row['gamma']==selection['selected_gamma']),None)
                covariance=None
                covariance_reason='No selected gamma'
                eligible=False
                if selected is not None:
                    theta=np.asarray(selected['parameters'])
                    # The already declared1e-6 active-constraint distance is also used to exclude active-bound ellipses.
                    eligible=bool(selected['data_rank']==2 and np.all(theta>lo+1e-6) and np.all(theta<hi-1e-6))
                    if eligible:
                        covariance,g,response=fixed_gamma_covariance(selected['data_jacobian'],b['weights'],sigma,selected['gamma'])
                        np.savez_compressed(output/f'case67-path-{path_index}-covariance.npz',
                                            covariance=covariance,curvature=g,response=response,
                                            parameters=theta,gamma=selected['gamma'],sigma=sigma)
                        covariance_reason='Fixed-gamma local linear-model plug-in; not selection-conditional'
                    else:
                        covariance_reason='N/A: active bound within1e-6 or data rank not2'
                if covariance is not None:
                    eigen=np.linalg.eigvalsh(covariance)
                    tolerance=128.*np.finfo(float).eps*max(float(np.linalg.norm(covariance)),1e-300)
                    covariance_ok=bool(np.all(np.isfinite(covariance)) and eigen[0]>=-tolerance)
                else:
                    covariance_ok=bool(not eligible)
                book.add(f'path-{path_index}-covariance-eligibility-and-psd',covariance_ok,covariance_reason)
                path_records.append(plain(dict(context_index=context_index,sigma=sigma,seed=seed,
                                               gamma_path_complete=completed,selection_status=selection['status'],
                                               selected_gamma=selection['selected_gamma'],noise_norm=noise_norm,
                                               selected_parameters=selected['parameters'] if selected else None,
                                               covariance=covariance,covariance_scope=covariance_reason,
                                               lcurve=lcurve_chord_curvature(rows))))
                write_json(output/'case67-paths.partial.json',path_records)
    for context_index in range(2):
        clean=cfg['legacy_data']['same_grid_data'] if context_index==0 else cfg['legacy_data']['fine_1023_data']
        control=fit(context_index,-1,-1,0,clean,0.)
        path_records.append(dict(context_index=context_index,control='noiseless-gamma0',
                                 parameters=control.get('parameters'),qualified=control['qualified']))
    linear=spec['linear_control']
    k,w=np.asarray(linear['K']),np.asarray(linear['W_diagonal'])
    c,g,response=fixed_gamma_covariance(k,w,linear['sigma'],linear['gamma'])
    np.savez_compressed(output/'case67-linear-control-before-bias.npz',
                        covariance=c,curvature=g,response=response)
    delta=np.asarray(cfg['legacy_data']['fine_1023_data'])-np.asarray(cfg['legacy_data']['same_grid_data'])
    bias=-linear['gamma']*np.linalg.solve(g,np.asarray(linear['truth'])-np.asarray(linear['prior']))
    shift=np.einsum('ij,j->i',response,delta)
    np.savez_compressed(output/'case67-linear-control.npz',covariance=c,curvature=g,response=response,
                        bias=bias,model_shift=shift,delta_data=delta)
    reference_c,reference_bias,reference_shift=scalar_2x2_statistics(k,w,linear['sigma'],linear['gamma'],
                                                                  linear['truth'],linear['prior'],delta)
    np.savez_compressed(output/'case67-linear-reference-before-comparison.npz',
                        covariance=reference_c,bias=reference_bias,model_shift=reference_shift)
    for label,actual,expected in [('covariance',c,reference_c),('bias',bias,reference_bias),('data-shift',shift,reference_shift)]:
        defect=relative_error(actual,expected)
        book.add('linear-control-'+label,defect<=limits['covariance_scalar_oracle_relative'],defect,limits['covariance_scalar_oracle_relative'])
    symmetry=relative_error(c,c.T)
    minimum=float(np.linalg.eigvalsh(c)[0])
    book.add('linear-control-symmetry',symmetry<=limits['covariance_symmetry_relative'],symmetry,limits['covariance_symmetry_relative'])
    book.add('linear-control-psd',minimum>=-128*np.finfo(float).eps*float(np.linalg.norm(c)),minimum)
    write_json(output/'case67-all-fits.json',fits)
    write_json(output/'case67-paths.json',path_records)
    complete=[row for row in fits if not row.get('failed')]
    metrics=dict(attempted_fits=attempted,completed_fits=len(complete),expected_fits=42,
                 independent_base_noise_vectors=2,coupled_gamma_paths=8,
                 forward_evaluations=sum(row['forward_evaluations'] for row in complete),
                 maximum_stationarity_inf=max((row['physical_projected_gradient_inf'] for row in complete),default=0.),
                 covariance_scope='fixed-gamma Gauss–Newton local-linear-model plug-in; no selection-event covariance or coverage claim',
                 detailed_fit_records='case67-all-fits.json')
    return dict(id=CASE_IDS[2],passed=bool(attempted==len(complete)==42 and all(book.checks.values())),
                checks=book.checks,check_details=book.details,records=path_records,metrics=metrics)


def main(argv=None):
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args(argv)
    start=time.monotonic()
    output=args.output.resolve()
    output.mkdir(parents=True,exist_ok=False)
    report=dict(schema_version=1,passed=False,input_sha256=digest(args.input),
                termination='incomplete',failure=None,cases=[],checks={},
                source_sha256={p.name:digest(p) for p in ROOT.glob('*.py')})
    try:
        cfg=json.loads(args.input.read_text())
        limits=json.loads((ROOT/'acceptance.json').read_text())['limits']
        qualification,reference=load_reference(args.input)
        report['reference_qualification']={'passed':True,'gate_count':qualification['gate_count'],
                                           'fields_sha256':qualification['fields_sha256']}
        for function in [lambda:run_case65(cfg,limits,reference,output),
                         lambda:run_case66(cfg,limits,output),
                         lambda:run_case67(cfg,limits,output)]:
            case=function()
            report['cases'].append(case)
            report['checks'][case['id']]=bool(case['passed'])
            write_json(output/'result.partial.json',report)
        report['termination']='fixed_budget_completed'
        report['passed']=bool(set(report['checks'])==set(CASE_IDS) and all(report['checks'].values()))
        if report['passed']:
            validate_result(report,CASE_IDS,report['input_sha256'],'fixed_budget_completed')
            report['csv_validation']=check_generated_csv(output)
        else:
            report['failure']={'type':'ScientificAcceptanceFailure','message':'One or more fixed required decisions failed; no criteria were relaxed.'}
    except BaseException as error:
        report['passed']=False
        report['failure']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        report['termination']='exception'
        raise
    finally:
        report['duration_seconds']=time.monotonic()-start
        write_json(output/'result.json',report)
    return 0 if report['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
