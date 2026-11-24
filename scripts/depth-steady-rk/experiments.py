"""The four fixed field iterations and their distinct controls."""
from fractions import Fraction
import numpy as np
from io_contract import Case,save_arrays,save_json,csv_rows
import steady
import references as R

CASE_ID='jameson-steady-linear-modes'


def run_case(output,cfg,accept):
    case=Case(CASE_ID,output)
    q=R.qualify();save_json(output/'reference-qualification.json',{'passed':all(q.values()),'checks':q})
    for key,value in q.items():case.check('reference:'+key,value)
    if not all(q.values()):raise ArithmeticError('Prior exact discrete-reference qualification failed')
    c,s,w=steady.patterns();g=accept['gates'];diagnostics=[]
    for spec in cfg['runs']:
        ident=spec['id'];role=spec['role'];shift=spec.get('shift_override',1)
        star=.5+.25*c if role=='steady_iteration' else np.zeros(16)
        error=c+.5*w if role=='steady_iteration' else np.ones(16) if role=='neutral_control' else w.copy()
        forcing=steady.operator(star,shift);dt=float(Fraction(spec['dtau']));active={}
        def progress(**arrays):
            active.clear();active.update({key:np.array(value,copy=True) for key,value in arrays.items()})
        try:
            history,stages,residuals=steady.evolve(star+error,forcing,dt,spec['steps'],shift,progress)
        except BaseException:
            save_arrays(output/(ident+'-failed-candidate.npz'),**active)
            raise
        save_arrays(output/(ident+'.npz'),x=np.arange(16)/16,tau=np.arange(spec['steps']+1)*dt,states=history,stages=stages,stage_residuals=residuals,forcing=forcing,steady_state=star)
        record=case.record({'id':ident,'role':role,'termination':'completed_fixed_steps','steps':spec['steps'],'stage_residual_evaluations':4*spec['steps'],'monitor_residual_evaluations':spec['steps']+1,'metrics':{}})
        exact,reference_residual=R.field_reference(spec['dtau'],spec['steps'],role)
        actual_residual=np.array([steady.operator(u,shift)-forcing for u in history])
        errors=history-exact
        row_error=float(np.max(np.abs(errors)));normalized=float(np.max(np.abs(errors)/(1+np.abs(exact))))
        ratio=float(np.max(np.abs(actual_residual[-1]))/np.max(np.abs(actual_residual[0]))) if role!='neutral_control' else None
        mode4=float(np.hypot(2*np.sum((history[-1]-star)*c)/16,2*np.sum((history[-1]-star)*s)/16))
        projections=np.array([star+2*np.sum((u-star)*c)/16*c+2*np.sum((u-star)*s)/16*s+np.sum((u-star)*w)/16*w for u in history]) if role!='neutral_control' else history.copy()
        metrics={'full_field_maxabs_error':row_error,'normalized_field_error':normalized,'mode4_final_amplitude':mode4,'residual_ratio':ratio,'spurious_mode_maxabs':float(np.max(np.abs(history-projections))),'modal_residual_error':float(np.max(np.abs(actual_residual-reference_residual)))}
        record['metrics']=metrics;case.checkpoint()
        save_arrays(output/(ident+'-comparison.npz'),reference=exact,true_residual=actual_residual,reference_residual=reference_residual,error=errors)
        csv_rows(output/(ident+'-history.csv'),['tau','max_error_to_discrete_reference','true_residual_linf'],zip(np.arange(len(history))*dt,np.max(np.abs(errors),axis=1),np.max(np.abs(actual_residual),axis=1)))
        case.check(ident+':finite',np.isfinite(history).all() and np.isfinite(stages).all() and np.isfinite(residuals).all())
        case.check(ident+':stage-count',record['stage_residual_evaluations']==4*spec['steps'])
        case.check(ident+':spurious-mode',metrics['spurious_mode_maxabs']<=g['spurious_mode_maxabs'])
        case.check(ident+':true-residual-reference',metrics['modal_residual_error']<=g['true_residual_independent_modal_error_max'])
        if role=='steady_iteration':
            key='stable_h32_fullfield_maxabs_error' if ident=='stable-h32' else 'stable_h16_fullfield_maxabs_error'
            case.check(ident+':field-error',row_error<=g[key],row_error)
            case.check(ident+':residual-reduction',ratio<=g['both_stable_final_to_initial_true_residual_ratio_max'],ratio)
            case.check(ident+':nonzero-mode4',mode4>=g['both_stable_final_mode4_amplitude_min'],mode4)
        elif role=='neutral_control':case.check(ident+':neutrality',row_error<=g['neutral_constant_maxabs_error'],row_error)
        else:
            growth=float(np.max(np.abs(history[-1]))/np.max(np.abs(history[0])))
            case.check(ident+':expected-expansion',growth>=g['expanding_final_to_initial_error_norm_ratio_min'],growth)
            case.check(ident+':normalized-error',normalized<=g['expanding_normalized_fullfield_error_max'],normalized)
        diagnostics.append((ident,row_error,normalized,mode4))
    fixed=steady.operator(.5+.25*c)-(.5+2.25*c-.5*s)
    case.check('steady-fixed-point',float(np.max(np.abs(fixed)))<=g['steady_fixed_point_maxabs'])
    case.check('four-record-identities',[r['id'] for r in case.data['records']]==[x['id'] for x in cfg['runs']])
    csv_rows(output/'measurements.csv',['run','field_error','normalized_error','mode4_final'],diagnostics)
    case.data['metrics']['max_field_error']=max(row[1] for row in diagnostics)
    return case.finish()
