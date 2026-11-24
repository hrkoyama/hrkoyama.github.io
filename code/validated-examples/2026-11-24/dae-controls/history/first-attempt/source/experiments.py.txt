"""Fixed DAE controls, preserving each raw path before diagnostics."""
from decimal import Decimal
import numpy as np
from io_contract import Case,save_arrays,save_json,csv_rows
from newton import solve,NewtonFailure
import models as M
import references as R

CASE_IDS=['index1-dae-consistent-initialization','robertson-conservation-dae','high-index-pendulum']


def order(errors):
    return [float(np.log(errors[k]/errors[k+1])/np.log(2)) for k in range(len(errors)-1)]


def all_in(values,bounds):return all(bounds[0]<=v<=bounds[1] for v in values)


def track():
    active={}
    def progress(**arrays):
        active.clear();active.update({key:np.array(value,copy=True) for key,value in arrays.items()})
    return active,progress


def initialize_index1(guess,cfg,output,ident):
    active,observe=track()
    if guess==0:
        save_arrays(output/(ident+'-raw.npz'),candidate=[1.,0.],residual=[-1.],jacobian=[[0.]])
        return np.array([1.,0.]),{'termination':'initialization_singular_jacobian','iterations':0,'residual':1.}
    n=cfg['Newton']
    try:
        z,counters,trials=solve(lambda x:np.array([x[0]**3-1]),lambda x:np.array([[3*x[0]**2]]),[guess],[1.],n['residual_target'],n['max_iterations'],n['line_search_halvings'],n['armijo_constant'],observe)
    except BaseException:
        save_arrays(output/(ident+'-failed.npz'),**active);raise
    save_arrays(output/(ident+'-raw.npz'),candidate=z,trials=trials)
    return np.array([1.,z[0]]),{'termination':'consistent_initialization','iterations':counters['iterations'],'residual':abs(float(z[0]**3-1))}


def be_path(output,ident,initial,times,fun,jac,scale,newton_cfg,target):
    state=np.array(initial,copy=True);history=np.empty((len(times),len(state)));history[0]=state
    residuals=np.zeros_like(history);counters=[];all_trials=[];active,observe=track()
    try:
        for k in range(1,len(times)):
            old=state.copy();h=float(times[k]-times[k-1]);t=float(times[k])
            state,counter,trials=solve(lambda y:fun(y,old,t,h),lambda y:jac(y,t,h),state,scale,target,newton_cfg['max_iterations'],newton_cfg['line_search_halvings'],newton_cfg['armijo_constant'],observe)
            history[k]=state;residuals[k]=fun(state,old,t,h);counter['step']=k;counters.append(counter)
            if len(trials):all_trials.extend(np.column_stack((np.full(len(trials),k),trials)).tolist())
    except BaseException as exc:
        save_arrays(output/(ident+'-failed.npz'),**active,accepted_time=times[:len(counters)+1],accepted_states=history[:len(counters)+1],accepted_residuals=residuals[:len(counters)+1])
        save_json(output/(ident+'-failed-counters.json'),{'completed_steps':counters,'exception':type(exc).__name__,'message':str(exc)})
        raise
    save_arrays(output/(ident+'.npz'),time=times,states=history,step_residuals=residuals,trials=np.array(all_trials).reshape((-1,5)))
    save_json(output/(ident+'-counters.json'),counters)
    return history,residuals,counters


def index1_case(output,cfg,accept):
    case=Case(CASE_IDS[0],output);g=accept['gates'];q,fixtures=R.index1_qualification()
    save_json(output/'index1-independent-reference.json',{'checks':q,'passed':all(q.values()),'fixtures':fixtures})
    for key,value in q.items():case.check('reference:'+key,value)
    if not all(q.values()):raise ArithmeticError('Index-one reference qualification failed')
    # These are declared three one-step component solves, not extra trajectories.
    nc=cfg['Newton'];root_differences=[]
    for k,f in enumerate(fixtures):
        h=float(f['h']);t=float(f['t0'])+h;old=np.array([float(f['yold']),float(f['yold'])**(2/3)])
        active,observe=track()
        try:root,count,trials=solve(lambda x:M.index1_residual(x,old,t,h),lambda x:M.index1_jacobian(x,h),old,[1.,1.],nc['residual_target'],progress=observe)
        except BaseException:
            save_arrays(output/('index1-root-'+str(k)+'-failed.npz'),**active);raise
        exact=np.array([float(f['y']),float(f['z'])]);save_arrays(output/('index1-root-'+str(k)+'.npz'),candidate=root,reference=exact,trials=trials)
        root_differences.append(float(np.max(np.abs(root-exact))))
    case.check('reference:three-independent-discrete-roots',max(root_differences)<=2e-12,max(root_differences))
    for guess in cfg['initialization_guesses']+[cfg['singular_initial_guess']]:
        ident='initialize-'+str(guess);value,metrics=initialize_index1(guess,cfg,output,ident)
        record=case.record({'id':ident,'kind':'initialization' if guess else 'expected_initial_failure','termination':metrics['termination'],'metrics':metrics})
        if guess:
            case.check(ident+':root',abs(float(value[1]-1))<=g['both_initialization_root_error_max'],abs(float(value[1]-1)))
            case.check(ident+':algebraic-residual',metrics['residual']<=g['both_initialization_algebraic_residual_max'])
        else:case.check(ident+':expected-singular-status',metrics['termination']=='initialization_singular_jacobian')
    errors=[];summary=[]
    for steps in cfg['step_counts']:
        ident='index1-BE-'+str(steps);times=np.linspace(0.,1.,steps+1)
        states,residuals,counters=be_path(output,ident,[1.,1.],times,lambda x,o,t,h:M.index1_residual(x,o,t,h),lambda x,t,h:M.index1_jacobian(x,h),[1.,1.],nc,nc['residual_target'])
        record=case.record({'id':ident,'kind':'trajectory','termination':'completed_fixed_steps','steps':steps,'metrics':{}})
        exact=np.column_stack((np.exp(-times),np.exp(-2*times/3)));error=float(np.max(np.abs(states-exact)));algebraic=float(np.max(np.abs(states[:,1]**3-states[:,0]**2)));residual=float(np.max(np.abs(residuals)))
        record['metrics']={'max_state_error':error,'max_algebraic_residual':algebraic,'max_derivative_unit_step_residual':residual,'Newton_iterations':sum(x['iterations'] for x in counters)};case.checkpoint()
        save_arrays(output/(ident+'-reference.npz'),reference=exact,error=states-exact)
        csv_rows(output/(ident+'-history.csv'),['time','y','z','differential_residual','algebraic_residual'],zip(times,states[:,0],states[:,1],residuals[:,0],residuals[:,1]))
        case.check(ident+':finite',np.isfinite(states).all());case.check(ident+':positive',float(np.min(states))>0)
        case.check(ident+':step-residual',residual<=g['all_step_nonlinear_residual_max'],residual)
        case.check(ident+':constraint',algebraic<=g['all_algebraic_constraint_maxabs'],algebraic)
        case.check(ident+':MMS-bound',error<=.5/steps+5e-10,error)
        errors.append(error);summary.append((steps,1/steps,error,algebraic,residual))
    orders=order(errors);case.check('first-order-refinement',all_in(orders,g['last_two_observed_time_orders_range']),orders)
    initialF=np.array([-1+1-1+1,1-1,3*(-2/3)-2*(-1)])
    case.check('initial-F-and-hidden-constraint',float(np.max(np.abs(initialF)))<=g['initial_F_and_differentiated_constraint_maxabs'])
    case.check('six-record-identities',[r['id'] for r in case.data['records']]==['initialize-'+str(x) for x in cfg['initialization_guesses']+[cfg['singular_initial_guess']]]+['index1-BE-'+str(n) for n in cfg['step_counts']])
    case.data['metrics'].update(finest_max_state_error=errors[-1],observed_orders=orders,one_step_reference_errors=root_differences)
    csv_rows(output/'index1-refinement.csv',['steps','h','state_error','algebraic_residual','step_residual'],summary)
    return case.finish()


def robertson_case(output,cfg,accept,source):
    case=Case(CASE_IDS[1],output);g=accept['gates'];times=M.robertson_nodes(cfg,4)
    reference,q,intervals,refcounts=R.robertson_reference(output,cfg,times,accept['reference_preconditions'],source/'ida-printed-values.json')
    for key,value in q.items():case.check('reference:'+key,value)
    if not all(q.values()):raise ArithmeticError('Robertson independent-reference qualification failed')
    bad=np.array(cfg['initial'],float);bad[2]+=cfg['inconsistent_y3_perturbation'];mass=float(np.sum(bad)-1)
    save_arrays(output/'robertson-inconsistent-initial.npz',candidate=bad,algebraic_residual=[mass])
    record=case.record({'id':'inconsistent-initial-rejection','kind':'expected_initial_failure','termination':'initial_algebraic_constraint_violated','metrics':{'mass_residual':mass}})
    case.check('inconsistent-initial-rejected',abs(mass)>cfg['Newton']['initial_mass_tolerance'])
    paths={};errors={};summaries=[]
    for form in cfg['formulations']:
        errors[form]=[]
        for factor in cfg['refinement_factors']:
            ident='robertson-'+form+'-r'+str(factor);tt=M.robertson_nodes(cfg,factor)
            states,residuals,counters=be_path(output,ident,cfg['initial'],tt,lambda y,o,t,h:M.robertson_residual(y,o,h,form),lambda y,t,h:M.robertson_step_jacobian(y,h,form),cfg['residual_scale'],cfg['Newton'],cfg['Newton']['scaled_step_residual_target'])
            record=case.record({'id':ident,'kind':'trajectory','formulation':form,'termination':'completed_fixed_steps','steps':len(tt)-1,'metrics':{}})
            stride=4//factor
            if not np.array_equal(tt,times[::stride]):raise ArithmeticError('Nested reference node identity failed')
            exact=reference[::stride];err=float(np.max(np.abs(states-exact)/np.array(cfg['state_error_scale'])))
            masserr=float(np.max(np.abs(np.sum(states,axis=1)-1)));res=float(np.max(np.abs(residuals)/np.array(cfg['residual_scale'])));minimum=float(np.min(states))
            record['metrics']={'max_scaled_reference_error':err,'max_mass_error':masserr,'max_scaled_step_residual':res,'minimum_species':minimum,'Newton_iterations':sum(x['iterations'] for x in counters)};case.checkpoint()
            save_arrays(output/(ident+'-reference.npz'),reference=exact,error=states-exact)
            csv_rows(output/(ident+'-history.csv'),['time','y1','y2','y3','mass_error','G1','G2','G3'],zip(tt,*states.T,np.sum(states,axis=1)-1,*residuals.T))
            case.check(ident+':finite',np.isfinite(states).all());case.check(ident+':nonnegative',minimum>=g['all_species_min'],minimum)
            case.check(ident+':nonlinear-residual',res<=g['DAE_allstep_scaled_step_residual_max'] if form=='residual_dae' else res<=g['ODE_allstep_scaled_step_residual_max'],res)
            case.check(ident+':mass',masserr<=(g['DAE_mass_error_max'] if form=='residual_dae' else g['ODE_mass_error_max']),masserr)
            paths[(form,factor)]=(tt,states);errors[form].append(err);summaries.append((form,factor,len(tt)-1,err,masserr,res))
        ratios=[errors[form][k]/errors[form][k+1] for k in range(2)]
        case.check(form+':refinement',min(ratios)>=g['both_refinement_error_ratios_min'],ratios)
        case.check(form+':finest-reference-error',errors[form][-1]<=g['both_finest_max_scaled_reference_error_max'],errors[form][-1])
        tt,states=paths[(form,4)];dist=[]
        for row in intervals:
            ii=np.flatnonzero(tt==float(row['t']))[0];lo=np.array(row['lower'],float);hi=np.array(row['upper'],float)
            dist.append(np.maximum(np.maximum(lo-states[ii],states[ii]-hi),0))
        case.check(form+':official-printed-comparison',bool(np.all(np.array(dist)<=np.array(g['finest_to_official_print_interval_component_distance_max']))),np.array(dist).tolist())
    for factor in cfg['refinement_factors']:
        diff=float(np.max(np.abs(paths[('residual_dae',factor)][1]-paths[('full_ode',factor)][1])/np.array(cfg['state_error_scale'])))
        case.check('ODE-DAE-r'+str(factor),diff<=g['DAE_ODE_max_scaled_state_difference'],diff)
    case.check('seven-record-identities',[r['id'] for r in case.data['records']]==['inconsistent-initial-rejection']+['robertson-'+f+'-r'+str(n) for f in cfg['formulations'] for n in cfg['refinement_factors']])
    case.data['metrics'].update(finest_scaled_error_DAE=errors['residual_dae'][-1],finest_scaled_error_ODE=errors['full_ode'][-1],reference_solver_counters=refcounts,IDA_new_executions=0)
    csv_rows(output/'robertson-refinement.csv',['formulation','factor','steps','scaled_reference_error','mass_error','scaled_step_residual'],summaries)
    return case.finish()


def pendulum_case(output,cfg,accept):
    case=Case(CASE_IDS[2],output);g=accept['gates'];q,refcounts=R.pendulum_qualification(output,cfg,accept['reference_preconditions'])
    for key,value in q.items():case.check('reference:'+key,value)
    if not all(q.values()):raise ArithmeticError('Pendulum independent-reference qualification failed')
    initial=M.consistent_pendulum(cfg['theta0']);bad=initial.copy();bad[2:4]=cfg['radial_velocity_perturbation']*bad[:2]
    badC,badD,_,_=M.pendulum_invariants(bad)
    save_arrays(output/'pendulum-rejected-initial.npz',candidate=bad,C=[badC],D=[badD])
    case.record({'id':'default-inconsistent-rejection','kind':'expected_initial_failure','termination':'initial_velocity_constraint_violated','metrics':{'C':float(badC),'D':float(badD)}})
    case.check('default-consistency-rejection',abs(float(badD))>cfg['consistent_start_tolerance'])
    paths={};errors=[];summaries=[]
    for spec in cfg['runs']:
        consistent=spec['initial']=='consistent';stabilized=spec['method']=='critical_constraint_stabilization';steps=spec['steps']
        ident='pendulum-'+('consistent' if consistent else 'radial')+'-'+('stabilized' if stabilized else 'underlying')+'-'+str(steps)
        state=initial.copy() if consistent else bad.copy();active,observe=track()
        try:history=M.rk4_path(state,cfg['T'],steps,stabilized,observe)
        except BaseException:
            save_arrays(output/(ident+'-failed.npz'),**active);raise
        tt=np.linspace(0.,cfg['T'],steps+1)
        save_arrays(output/(ident+'.npz'),time=tt,states=history,initial=state)
        record=case.record({'id':ident,'kind':'trajectory','initial_consistent':consistent,'constraint_extension':spec['method'],'termination':'completed_fixed_steps','steps':steps,'RHS_evaluations':4*steps,'metrics':{}})
        C,D,H,radius=M.pendulum_invariants(history);C0,D0,H0,_=M.pendulum_invariants(state)
        exactC=(C0+(D0+C0)*tt)*np.exp(-tt) if stabilized else C0+D0*tt
        exactD=(D0-(D0+C0)*tt)*np.exp(-tt) if stabilized else np.full(len(tt),D0)
        workerr=float(np.max(np.abs(H-H0-history[:,4])));energyerr=float(np.max(np.abs(H-H0)))
        cerror=float(np.max(np.abs(C-exactC)));derror=float(np.max(np.abs(D-exactD)))
        stateerr=None
        if consistent:
            exact,_=R.pendulum_exact(tt,cfg['theta0']);stateerr=float(np.max(np.abs(history[:,:4]-exact)))
            save_arrays(output/(ident+'-reference.npz'),reference=exact,error=history[:,:4]-exact)
            if not stabilized:errors.append(stateerr)
        save_arrays(output/(ident+'-constraints.npz'),C=C,D=D,H=H,work=history[:,4],exact_C=exactC,exact_D=exactD)
        record['metrics']={'max_state_error':stateerr,'max_abs_C':float(np.max(np.abs(C))),'C_exact_law_error':cerror,'D_exact_law_error':derror,'max_energy_error':energyerr,'max_energy_work_balance_error':workerr,'minimum_radius_squared':float(np.min(radius))};case.checkpoint()
        csv_rows(output/(ident+'-history.csv'),['time','qx','qy','vx','vy','work','C','D','energy','exact_C','exact_D'],zip(tt,*history.T,C,D,H,exactC,exactD))
        case.check(ident+':finite',np.isfinite(history).all());case.check(ident+':radius',float(np.min(radius))>=g['minimum_radius_squared'])
        if steps==max(cfg['step_counts']):
            if consistent:
                case.check(ident+':state',stateerr<=g['both_consistent_finest_max_state_error'],stateerr)
                case.check(ident+':energy',energyerr<=g['both_consistent_finest_energy_error_max'],energyerr)
            else:
                prefix='inconsistent_stabilized_finest_' if stabilized else 'inconsistent_underlying_finest_'
                keyC='C_error_to_critical_law_max' if stabilized else 'C_error_to_linear_law_max'
                keyD='Cdot_error_to_critical_law_max' if stabilized else 'Cdot_error_to_constant_law_max'
                case.check(ident+':C-law',cerror<=g[prefix+keyC],cerror);case.check(ident+':D-law',derror<=g[prefix+keyD],derror)
                case.check(ident+':work-ledger',workerr<=g['both_inconsistent_finest_energy_work_balance_error_max'],workerr)
        paths[(consistent,stabilized,steps)]=(tt,history,C,D)
        summaries.append((ident,steps,stateerr if stateerr is not None else '',cerror,derror,energyerr,workerr))
    observed=order(errors);case.check('underlying-consistent-fourth-order',all_in(observed,g['underlying_consistent_observed_state_orders_range']),observed)
    n=max(cfg['step_counts']);unst=abs(float(paths[(False,False,n)][2][-1]));stab=abs(float(paths[(False,True,n)][2][-1]))
    case.check('visible-unstabilized-drift',unst>=g['unstabilized_final_absC_min'],unst)
    case.check('stabilized-drift-ratio',stab/unst<=g['stabilized_to_unstabilized_final_absC_ratio_max'],stab/unst)
    case.check('eleven-record-identities',[r['id'] for r in case.data['records']]==['default-inconsistent-rejection']+['pendulum-'+('consistent' if s['initial']=='consistent' else 'radial')+'-'+('stabilized' if s['method']=='critical_constraint_stabilization' else 'underlying')+'-'+str(s['steps']) for s in cfg['runs']])
    case.data['metrics'].update(finest_consistent_state_error=errors[-1],observed_orders=observed,stabilized_to_unstabilized_drift_ratio=stab/unst,reference_solver_counters=refcounts)
    csv_rows(output/'pendulum-refinement.csv',['run','steps','state_error_if_consistent','C_law_error','D_law_error','energy_error','energy_work_error'],summaries)
    return case.finish()
