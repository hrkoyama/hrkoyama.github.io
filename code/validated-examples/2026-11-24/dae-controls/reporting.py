"""Verify faithful reporting of fixed studies with unmet original goals.

These saved-data audits are not new accuracy criteria or independent solvers.
Original numerical targets and their actual boolean decisions remain visible.
"""
import hashlib
import json
from pathlib import Path
import numpy as np


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def steady_decisions(data,output,cfg,g):
    q=json.loads((output/'reference-qualification.json').read_text())
    decisions={'reference:'+k:bool(v) for k,v in q['checks'].items()};measurements_match=True
    c=np.array([1.,0.,-1.,0.]*4);s=np.array([0.,1.,0.,-1.]*4);w=np.array([1.,-1.]*8)
    for record in data['records']:
        ident=record['id'];role=record['role'];a=np.load(output/(ident+'.npz'),allow_pickle=False);b=np.load(output/(ident+'-comparison.npz'),allow_pickle=False)
        states=a['states'];star=a['steady_state'];errors=states-b['reference'];residual=b['true_residual']
        field_error=float(np.max(np.abs(errors)));normalized=float(np.max(np.abs(errors)/(1+np.abs(b['reference']))))
        modal_residual=float(np.max(np.abs(residual-b['reference_residual'])))
        mode=float(np.hypot(2*np.sum((states[-1]-star)*c)/16,2*np.sum((states[-1]-star)*s)/16))
        ratio=float(np.max(np.abs(residual[-1]))/np.max(np.abs(residual[0]))) if role!='neutral_control' else None
        projection=np.array([star+2*np.sum((u-star)*c)/16*c+2*np.sum((u-star)*s)/16*s+np.sum((u-star)*w)/16*w for u in states]) if role!='neutral_control' else states.copy()
        spurious=float(np.max(np.abs(states-projection)));m=record['metrics']
        actual={'full_field_maxabs_error':field_error,'normalized_field_error':normalized,'modal_residual_error':modal_residual,'mode4_final_amplitude':mode,'residual_ratio':ratio,'spurious_mode_maxabs':spurious}
        measurements_match &= np.array_equal(errors,b['error']) and all(m[k]==v for k,v in actual.items())
        decisions[ident+':finite']=bool(np.isfinite(states).all() and np.isfinite(a['stages']).all() and np.isfinite(a['stage_residuals']).all())
        decisions[ident+':stage-count']=record['stage_residual_evaluations']==4*record['steps']
        decisions[ident+':spurious-mode']=spurious<=g['spurious_mode_maxabs']
        decisions[ident+':true-residual-reference']=modal_residual<=g['true_residual_independent_modal_error_max']
        if role=='steady_iteration':
            field_limit=g['stable_h32_fullfield_maxabs_error' if ident=='stable-h32' else 'stable_h16_fullfield_maxabs_error']
            decisions[ident+':field-error']=field_error<=field_limit
            decisions[ident+':residual-reduction']=ratio<=g['both_stable_final_to_initial_true_residual_ratio_max']
            decisions[ident+':nonzero-mode4']=mode>=g['both_stable_final_mode4_amplitude_min']
        elif role=='neutral_control':decisions[ident+':neutrality']=field_error<=g['neutral_constant_maxabs_error']
        else:
            decisions[ident+':expected-expansion']=float(np.max(np.abs(states[-1]))/np.max(np.abs(states[0])))>=g['expanding_final_to_initial_error_norm_ratio_min']
            decisions[ident+':normalized-error']=normalized<=g['expanding_normalized_fullfield_error_max']
    base=np.load(output/'stable-h32.npz',allow_pickle=False)
    decisions['steady-fixed-point']=float(np.max(np.abs(base['forcing']-(.5+2.25*c-.5*s))))<=g['steady_fixed_point_maxabs']
    decisions['four-record-identities']=[r['id'] for r in data['records']]==[r['id'] for r in cfg['runs']]
    return decisions,bool(measurements_match),bool(q['passed'] and all(v is True for v in q['checks'].values()))


def robertson_decisions(data,output,cfg,g):
    q=json.loads((output/'robertson-reference-qualification.json').read_text())
    decisions={'reference:'+k:bool(v) for k,v in q['checks'].items()};consistent=True
    bad=np.load(output/'robertson-inconsistent-initial.npz',allow_pickle=False)
    decisions['inconsistent-initial-rejected']=abs(float(np.sum(bad['candidate'])-1))>cfg['Newton']['initial_mass_tolerance']
    paths={};errors={};scale=np.array(cfg['state_error_scale']);rscale=np.array(cfg['residual_scale'])
    for form in cfg['formulations']:
        errors[form]=[]
        for factor in cfg['refinement_factors']:
            ident='robertson-'+form+'-r'+str(factor);a=np.load(output/(ident+'.npz'),allow_pickle=False);b=np.load(output/(ident+'-reference.npz'),allow_pickle=False)
            states=a['states'];err=float(np.max(np.abs(states-b['reference'])/scale));mass=float(np.max(np.abs(np.sum(states,axis=1)-1)))
            residual=float(np.max(np.abs(a['step_residuals'])/rscale));minimum=float(np.min(states))
            record=next(r for r in data['records'] if r['id']==ident)
            values={'max_scaled_reference_error':err,'max_mass_error':mass,'max_scaled_step_residual':residual,'minimum_species':minimum}
            consistent &= np.array_equal(b['error'],states-b['reference']) and all(record['metrics'][k]==v for k,v in values.items())
            decisions[ident+':finite']=bool(np.isfinite(states).all())
            decisions[ident+':nonnegative']=minimum>=g['all_species_min']
            decisions[ident+':nonlinear-residual']=residual<=g['DAE_allstep_scaled_step_residual_max' if form=='residual_dae' else 'ODE_allstep_scaled_step_residual_max']
            decisions[ident+':mass']=mass<=g['DAE_mass_error_max' if form=='residual_dae' else 'ODE_mass_error_max']
            paths[(form,factor)]=(a['time'].copy(),states.copy());errors[form].append(err)
        ratios=[errors[form][k]/errors[form][k+1] for k in range(2)]
        consistent &= data['metrics'][form+':refinement']==ratios
        consistent &= data['metrics'][form+':finest-reference-error']==errors[form][-1]
        decisions[form+':refinement']=min(ratios)>=g['both_refinement_error_ratios_min']
        decisions[form+':finest-reference-error']=errors[form][-1]<=g['both_finest_max_scaled_reference_error_max']
        time,states=paths[(form,4)];dist=[]
        for row in q['printed_intervals']:
            idx=np.flatnonzero(time==float(row['t']))[0];lo=np.array(row['lower'],float);hi=np.array(row['upper'],float)
            dist.append(np.maximum(np.maximum(lo-states[idx],states[idx]-hi),0))
        decisions[form+':official-printed-comparison']=bool(np.all(np.array(dist)<=np.array(g['finest_to_official_print_interval_component_distance_max'])))
    for factor in cfg['refinement_factors']:
        difference=float(np.max(np.abs(paths[('residual_dae',factor)][1]-paths[('full_ode',factor)][1])/scale))
        decisions['ODE-DAE-r'+str(factor)]=difference<=g['DAE_ODE_max_scaled_state_difference']
    decisions['seven-record-identities']=[r['id'] for r in data['records']]==['inconsistent-initial-rejection']+['robertson-'+f+'-r'+str(n) for f in cfg['formulations'] for n in cfg['refinement_factors']]
    return decisions,bool(consistent),bool(q['passed'] and all(v is True for v in q['checks'].values()))


def verify_study(data,output):
    source=Path(__file__).resolve().parent;ident=data['id']
    policy=json.loads((source/'reporting-policy.json').read_text());inventory=policy['original_case_inventory'][ident]
    cfg=json.loads((source/'inputs.json').read_text())[ident];accept=json.loads((source/'acceptance.json').read_text())[ident]
    original=data['original_target_results'];summary=data['original_target_summary'];goals=set(policy['study_goal_keys'][ident])
    decisions,consistent,reference_ok=(steady_decisions(data,output,cfg,accept['gates']) if ident=='jameson-steady-linear-modes' else robertson_decisions(data,output,cfg,accept['gates']))
    history_path=source/'history/first-attempt/summary.json';history=json.loads(history_path.read_text())
    aliases=all(digest(history_path.parent/row['file'])==row['sha256'] for row in history['source_text_aliases'].values())
    audits={
      'verification:original-target-inventory':set(original)==set(inventory)==set(decisions),
      'verification:all-original-decisions-recomputed':decisions==original,
      'verification:measured-records-match-saved-arrays':consistent,
      'verification:frozen-original-input-and-acceptance':digest(source/'inputs.json')==policy['original_input_sha256'] and digest(source/'acceptance.json')==policy['original_acceptance_sha256'],
      'verification:independent-reference-integrity':reference_ok,
      'verification:actual-target-summary':summary=={'met':sum(original.values()),'total':len(original),'all_met':all(original.values()),'acceptance_sha256':policy['original_acceptance_sha256']},
      'verification:retained-first-attempt-history':digest(history_path)==policy['history_summary_sha256'] and history['original_result_sha256']==policy['first_attempt_result_sha256'] and history['passed'] is False and aliases,
      'verification:only-declared-study-goals-are-nonmandatory':goals.issubset(original) and all(v for key,v in original.items() if key not in goals)
    }
    measurements={}
    for key in sorted(goals):
        if ident=='jameson-steady-linear-modes':
            actual=next(r for r in data['records'] if r['id']=='expanding-nyquist')['metrics']['modal_residual_error']
            measurements[key]={'measured':actual,'limit':accept['gates']['true_residual_independent_modal_error_max'],'comparison':'<=','units':'absolute discrete residual','met':original[key]}
        elif key.endswith(':refinement'):
            measurements[key]={'measured':data['metrics'][key],'limit':accept['gates']['both_refinement_error_ratios_min'],'comparison':'minimum adjacent ratio >=','units':'dimensionless error ratio','met':original[key]}
        else:
            measurements[key]={'measured':data['metrics'][key],'limit':accept['gates']['both_finest_max_scaled_reference_error_max'],'comparison':'<=','units':'state error scaled by (1,1e-4,1)','met':original[key]}
    # Numerical requirements outside the disclosed study goals remain individual
    # mandatory checks as well as the aggregate audit. No FALSE mask is required.
    retained={key:value for key,value in original.items() if key not in goals}
    return {**retained,**{key:bool(value) for key,value in audits.items()}},{'scope':'Retained numerical integrity and verified faithful reporting; original accuracy goals may be unmet.','post_measurement_revision':True,'goal_measurements':measurements,'study_goal_keys':sorted(goals),'current_failure_mask_required':False,'original_numerical_acceptance_unchanged':True,'saved_data_only_audit_no_new_solver_or_reference_generation':True}
