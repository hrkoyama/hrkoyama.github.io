"""Fixed products and branch traces;46+27+144 meaningful case gates."""
from pathlib import Path
from fractions import Fraction
import numpy as np
from tape import build,values
from fixtures import reverse_specs,hvp_specs
from hessians import hvp,implicit_second
from kinks import piece,max_tie,stopped,inactive_log
from references import smooth_reference,hvp_reference,piece_reference,stopped_reference,precision_qualified
from io_contract import snapshot,save_json,csv_rows

CASE_IDS=['reverse-vjp-duality','hessian-vector-products','kink-branch-derivatives']
REV_IDS=['rectangular4x3','wide7','wide31','bratu7','bratu31']
HVP_IDS=['quadratic4','bratu-energy7','bratu-energy31','implicit-scalar4']


def dot(a,b):return float(np.sum(np.asarray(a)*np.asarray(b)))
def norm(a):return float(np.sqrt(dot(a,a)))
def mv(a,x):return np.einsum('ij,j->i',a,x)
def mtv(a,x):return np.einsum('ij,i->j',a,x)
def error(a,b):return norm(np.asarray(a)-b)
def close(a,b,tolerance):return error(a,b)<=tolerance*max(1.,norm(b))


def expected_gate_keys():
    reverse=[i+'/'+k for i in REV_IDS for k in ['primal','independentJVP','independentVJP','fullforwardJacobian',
             'fullreverseJacobian','duality','reset_ownership','measuredsweepcounts']]
    reverse+=['metric/product','metric/pairing']+['negative/'+m for m in ['drop-duplicate','broadcast-first','permuted-output','stale-cotangent']]
    second=[i+'/'+k for i in HVP_IDS for k in ['finite','reference_product','primary_path_ownership','work_counters']]
    second += [i+'/'+k for i in HVP_IDS[:3]for k in ['independent_gradient','bilinear_symmetry']]
    second += ['implicit/'+k for k in ['state_residual','first_tangent_residual','second_tangent_residual','fixed_partial','total_curvature']]
    scalar=[ident+'/'+k for ident in kink_ids() for k in ['category','finite_oracle_values']]
    scalar += ['stop-'+str(i)+'/'+k for i in range(5)for k in ['exactK','trace_AD_slope']]
    scalar += ['jump/'+str(i)for i in range(3)]+['inactive/no_log_evaluation']
    return dict(zip(CASE_IDS,[reverse,second,scalar]))


def kink_ids():
    return ([f'{kind}-{i}-{direction}'for kind in ['abs','relu','clip','branch']for i in range(7)for direction in [-1,1]]+
            ['max-tie-'+str(i)for i in range(3)]+['stop-'+str(i)for i in range(5)]+['inactive-log'])


def finite(value):
    if isinstance(value,dict):return all(finite(v)for v in value.values())
    if isinstance(value,(list,tuple)):return all(finite(v)for v in value)
    if isinstance(value,np.ndarray):return bool(np.all(np.isfinite(value)))
    return not isinstance(value,(float,np.floating))or np.isfinite(value)


def run_reverse(output):
    records=[];checks={};maxj=maxv=maxdual=0.;forward_count=reverse_count=0
    save_json(output/'reverse-partial.json',records)
    if not precision_qualified():raise ArithmeticError('Independent Decimal reference precision failed')
    for spec in reverse_specs():
        ident=spec['id'];x=np.array(spec['x'],copy=True);original=x.copy();x.setflags(write=False)
        v=spec['v'];w=spec['w'];fun=spec['function']
        snapshot(output/'active-candidate.npz','before-reverse-primal',x=x,v=v,w=w)
        tape,node,out=build(fun,x,v);y=values(out);jv=values(out,'tangent')
        product,_=tape.reverse(out,w)
        snapshot(output/(ident+'-raw.npz'),'raw-products-before-oracle',x=x,v=v,w=w,y=y,Jv=jv,JTw=product)
        raw={'id':ident,'x':x,'v':v,'w':w,'y':y,'Jv':jv,'JTw':product,
             'tape':tape.descriptors(),'work_product':tape.inventory()}
        save_json(output/(ident+'-raw.json'),raw)
        record={**raw};records.append(record);save_json(output/'reverse-partial.json',records)
        yr,j=smooth_reference(ident,x);jvr=mv(j,v);pr=mtv(j,w)
        snapshot(output/(ident+'-reference.npz'),'reference-before-Jacobian-sweeps',oracle_y=yr,oracle_J=j,oracle_Jv=jvr,oracle_JTw=pr)
        columns=[]
        for k in range(len(x)):
            seed=np.zeros(len(x));seed[k]=1.;ft,fn,fo=build(fun,x,seed);columns.append(values(fo,'tangent'))
            snapshot(output/(ident+'-forward-J-partial.npz'),'forward-seed-completed',columns=np.array(columns),seed=seed,x=x)
        jf=np.column_stack(columns)
        rt,rn,ro=build(fun,x);rows=[]
        for k in range(len(y)):
            seed=np.zeros(len(y));seed[k]=1.;rows.append(rt.reverse(ro,seed)[0])
            snapshot(output/(ident+'-reverse-J-partial.npz'),'reverse-seed-completed',rows=np.array(rows),seed=seed,x=x)
        jr=np.array(rows)
        saved=product.copy();again=tape.reverse(out,w)[0];opposite=tape.reverse(out,-w)[0]
        ownership=np.array_equal(saved,product)and np.array_equal(again,product)and close(opposite,-product,3e-11)and np.array_equal(x,original)
        dual=abs(dot(w,jv)-dot(v,product));dscale=max(1.,norm(w)*norm(jv),norm(v)*norm(product))
        gates={'primal':close(y,yr,3e-11),'independentJVP':close(jv,jvr,3e-11),
               'independentVJP':close(product,pr,3e-11),'fullforwardJacobian':close(jf,j,3e-11),
               'fullreverseJacobian':close(jr,j,3e-11),'duality':dual<=3e-11*dscale,
               'reset_ownership':ownership,'measuredsweepcounts':len(columns)==len(x)and len(rows)==len(y)and rt.pullbacks==len(y)}
        checks.update({ident+'/'+k:bool(z)for k,z in gates.items()})
        record.update(oracle_y=yr,oracle_J=j,oracle_Jv=jvr,oracle_JTw=pr,J_forward=jf,J_reverse=jr,
                      JVP_error=error(jv,jvr),VJP_error=error(product,pr),duality_defect=dual,
                      sweep_counts={'forward_seeds':len(columns),'full_reverse_pullbacks':len(rows),'product_and_lifecycle_pullbacks':tape.pullbacks},
                      work_reverse_jacobian=rt.inventory())
        snapshot(output/(ident+'.npz'),'all-products-completed',x=x,v=v,w=w,y=y,Jv=jv,JTw=product,
                 oracle_J=j,oracle_Jv=jvr,oracle_JTw=pr,J_forward=jf,J_reverse=jr)
        save_json(output/'reverse-partial.json',records)
        maxj=max(maxj,error(jv,jvr));maxv=max(maxv,error(product,pr));maxdual=max(maxdual,dual)
        forward_count+=len(columns);reverse_count+=len(rows)+tape.pullbacks
        if ident=='rectangular4x3':
            gx=np.array([1.,2.,4.,8.]);gy=np.array([[2.,.5,0.],[.5,1.,0.],[0.,0.,3.]])
            weighted=tape.reverse(out,mv(gy,w))[0]/gx;reference=mtv(j,mv(gy,w))/gx
            checks['metric/product']=close(weighted,reference,3e-11)
            checks['metric/pairing']=abs(dot(jv,mv(gy,w))-dot(v,gx*weighted))<=3e-11*max(1.,norm(jv)*norm(mv(gy,w)),norm(v)*norm(gx*weighted))
            record['weighted_adjoint']=weighted;record['weighted_oracle']=reference;reverse_count+=1
            for fault in ['drop-duplicate','broadcast-first','permuted-output','stale-cotangent']:
                nt,nn,no=build(fun,x)
                if fault=='stale-cotangent':nt.reverse(no,w)
                bad=nt.reverse(no,w,negative_control=fault)[0]
                checks['negative/'+fault]=not close(bad,pr,3e-11)
                snapshot(output/('negative-'+fault+'.npz'),'declared-negative',computed=bad,oracle=pr)
                record.setdefault('negative_controls',{})[fault]={'error':error(bad,pr),'work':nt.inventory()}
                reverse_count+=nt.pullbacks
            save_json(output/'reverse-partial.json',records)
    csv_rows(output/'reverse-products.csv',[{'id':r['id'],'JVP_error':r['JVP_error'],'VJP_error':r['VJP_error'],
               'duality_defect':r['duality_defect'],'forward_seeds':r['sweep_counts']['forward_seeds'],
               'reverse_sweeps':r['sweep_counts']['full_reverse_pullbacks'],'node_array_bytes':r['work_product']['peak_node_array_bytes']}for r in records])
    assert set(checks)==set(expected_gate_keys()[CASE_IDS[0]])and len(checks)==46
    return {'id':CASE_IDS[0],'passed':all(checks.values()),'checks':checks,'records':records,
            'metrics':{'max_JVP_oracle_error':maxj,'max_VJP_oracle_error':maxv,'max_duality_defect':maxdual,
                       'actual_forward_seeds':forward_count,'actual_reverse_pullbacks':reverse_count}}


def run_hvp(output):
    records=[];checks={};errors=[];symmetries=[]
    save_json(output/'HVP-partial.json',records)
    for spec in hvp_specs():
        ident=spec['id'];x=spec['x'];v=spec['v'];w=spec['w']
        snapshot(output/'active-candidate.npz','before-HVP',x=x,v=v,w=w)
        gradient,product,tape,out=hvp(spec['function'],x,v)
        snapshot(output/(ident+'-raw.npz'),'raw-HVP-before-reference',x=x,v=v,w=w,gradient=gradient,Hv=product)
        record={'id':ident,'gradient':gradient,'Hv':product,'x':x,'v':v,'w':w,'work':tape.inventory()}
        save_json(output/(ident+'-raw.json'),record);records.append(record);save_json(output/'HVP-partial.json',records)
        gr,pr=hvp_reference(ident,x,v)
        _,hw,_,_=hvp(spec['function'],x,w)
        symmetry=abs(dot(w,product)-dot(v,hw));scale=max(1.,norm(w)*norm(product),norm(v)*norm(hw))
        limit=1e-13 if ident=='quadratic4'else 5e-11*max(1.,norm(pr))
        gates={'finite':finite(record),'reference_product':error(product,pr)<=limit,
               'primary_path_ownership':tape.inventory()['max_node_rank']<=1 and not np.shares_memory(gradient,product)and not np.shares_memory(x,gradient),
               'work_counters':tape.pullbacks==1 and tape.second_rules==tape.inventory()['primal_rules'],
               'independent_gradient':close(gradient,gr,5e-11),'bilinear_symmetry':symmetry<=1e-11*scale}
        checks.update({ident+'/'+k:bool(z)for k,z in gates.items()})
        record.update(oracle_gradient=gr,oracle_Hv=pr,Hw=hw,HVP_error=error(product,pr),symmetry_defect=symmetry)
        snapshot(output/(ident+'.npz'),'HVP-complete',x=x,v=v,w=w,gradient=gradient,Hv=product,Hw=hw,oracle_gradient=gr,oracle_Hv=pr)
        save_json(output/'HVP-partial.json',records);errors.append(error(product,pr));symmetries.append(symmetry)
    def checkpoint(stage,**arrays):snapshot(output/'active-candidate.npz',stage,**arrays)
    answer=implicit_second(checkpoint=checkpoint)
    save_json(output/'implicit-scalar4-raw.json',answer)
    snapshot(output/'implicit-scalar4.npz','implicit-before-oracle',**{k:np.array(answer[k])for k in ['u','s','t','F','R1','R2','total_curvature','fixed_state_partial']})
    records.append({'id':'implicit-scalar4',**answer});save_json(output/'HVP-partial.json',records)
    ident='implicit-scalar4'
    checks.update({ident+'/finite':bool(finite(answer)),ident+'/reference_product':abs(answer['total_curvature']-.23125)<=1e-12,
                   ident+'/primary_path_ownership':answer['iterations'][0]['u']==3. and len(answer['iterations'])>1,
                   ident+'/work_counters':len(answer['iterations'])<=13 and answer['work']['second_rules']>0})
    checks.update({'implicit/state_residual':abs(answer['F'])<=1e-12,'implicit/first_tangent_residual':abs(answer['R1'])<=1e-12,
                   'implicit/second_tangent_residual':abs(answer['R2'])<=1e-12,'implicit/fixed_partial':abs(answer['fixed_state_partial']-.2)<=1e-12,
                   'implicit/total_curvature':abs(answer['total_curvature']-.23125)<=1e-12})
    csv_rows(output/'HVP-products.csv',[{'id':r['id'],'product_or_curvature_error':r.get('HVP_error',abs(r.get('total_curvature',.23125)-.23125)),
               'symmetry_defect':r.get('symmetry_defect',''),'stored_node_array_bytes':r['work']['peak_node_array_bytes']}for r in records])
    assert set(checks)==set(expected_gate_keys()[CASE_IDS[1]])and len(checks)==27
    return {'id':CASE_IDS[1],'passed':all(checks.values()),'checks':checks,'records':records,
            'metrics':{'max_HVP_oracle_error':max(errors),'max_bilinear_symmetry_defect':max(symmetries),
                       'implicit_state_residual':abs(answer['F']),'implicit_tangent_residual':abs(answer['R1']),
                       'implicit_second_tangent_residual':abs(answer['R2']),'implicit_total_curvature':answer['total_curvature']}}


def run_kinks(output):
    records=[];checks={};smooth_errors=[];trace_errors=[]
    save_json(output/'kinks-partial.json',records)
    for kind in ['abs','relu','clip','branch']:
        for i,x in enumerate([-2.,-1.,-.25,0.,.25,1.,2.]):
            for direction in [-1,1]:
                ident=f'{kind}-{i}-{direction}'
                snapshot(output/'active-candidate.npz','before-piece',x=np.array(x),direction=np.array(direction))
                ans=piece(kind,x,direction);records.append({'id':ident,**ans});save_json(output/'kinks-partial.json',records)
                ref=piece_reference(kind,x,direction)
                checks[ident+'/category']=ans['status']==ref['status']and(ans['classical_slope']is None)==(ref['slope']is None)
                value_ok=abs(ans['value']-ref['value'])<=1e-10 and abs(ans['one_sided_directional']-ref['directional'])<=1e-10
                if ref['slope']is not None:
                    e=abs(ans['classical_slope']-ref['slope']);smooth_errors.append(e);value_ok&=e<=1e-10
                checks[ident+'/finite_oracle_values']=bool(finite(ans)and value_ok)
    for i,direction in enumerate([(1,-1),(-1,1),(1,1)]):
        ident='max-tie-'+str(i);ans=max_tie(direction);records.append({'id':ident,**ans});save_json(output/'kinks-partial.json',records)
        checks[ident+'/category']=ans['status']=='NONDIFFERENTIABLE'and ans['classical_slope']is None
        expected=float(max(Fraction(direction[0]),Fraction(direction[1])))
        checks[ident+'/finite_oracle_values']=finite(ans)and ans['value']==0. and ans['one_sided_directional']==expected
    for i,theta in enumerate([.25,.5,1.,.5-2.**-20,.5+2.**-20]):
        ident='stop-'+str(i);ans=stopped(theta);records.append({'id':ident,**ans});save_json(output/'kinks-partial.json',records)
        k,value,slope=stopped_reference(theta)
        checks[ident+'/category']=ans['status']=='STOP_TOL'and(ans['classical_slope']is None)==(theta in [.25,.5,1.])
        checks[ident+'/finite_oracle_values']=finite(ans)and abs(ans['value']-value)<=1e-10
        checks[ident+'/exactK']=ans['K']==k
        checks[ident+'/trace_AD_slope']=abs(ans['frozen_trace_slope']-slope)<=1e-10
        trace_errors.append(abs(ans['frozen_trace_slope']-slope))
    ans=inactive_log();records.append({'id':'inactive-log',**ans});save_json(output/'kinks-partial.json',records)
    checks['inactive-log/category']=ans['status']=='SMOOTH_EXECUTED_BRANCH'
    checks['inactive-log/finite_oracle_values']=finite(ans)and ans['value']==1. and ans['classical_slope']==-2.
    checks['inactive/no_log_evaluation']=ans['invalid_log_calls']==0
    inactive_calls=ans['invalid_log_calls']
    center=next(r for r in records if r['id']=='stop-1')['value'];probes=[];qerrors=[]
    for i,h in enumerate([2.**-16,2.**-20,2.**-24]):
        ans=stopped(.5+h);probe={'h':h,'result':ans};probes.append(probe);save_json(output/'jump-probes-partial.json',probes)
        quotient=(ans['value']-center)/h;expected=1/(16*h)+7/8;err=abs(quotient-expected)
        checks['jump/'+str(i)]=err<=1e-10;probe.update(quotient=quotient,oracle=expected);qerrors.append(err)
    save_json(output/'jump-probes.json',probes)
    arrays={}
    for i,row in enumerate(records):
        arrays[f'value_{i}']=np.array(row['value'])
        for key in ['classical_slope','one_sided_directional','frozen_trace_slope']:
            if row.get(key)is not None:arrays[f'{key}_{i}']=np.array(row[key])
    snapshot(output/'kinks-values.npz','all-kink-records-complete',**arrays)
    csv_rows(output/'kink-branches.csv',[{'id':row['id'],'value':row['value'],'status':row['status'],
              'classical_slope':row.get('classical_slope')if row.get('classical_slope')is not None else'',
              'classical_valid':int(row.get('classical_slope')is not None),
              'one_sided_directional':row.get('one_sided_directional',''),
              'frozen_trace_slope':row.get('frozen_trace_slope',''),'K':row.get('K','')}for row in records])
    assert len(records)==65 and set(checks)==set(expected_gate_keys()[CASE_IDS[2]])and len(checks)==144
    return {'id':CASE_IDS[2],'passed':all(checks.values()),'checks':checks,'records':records,'auxiliary_stopped_probes':probes,
            'metrics':{'max_smooth_slope_oracle_error':max(smooth_errors),'max_fixed_trace_slope_error':max(trace_errors),
                       'stop_switch_jump':probes[-1]['result']['value']-center-probes[-1]['result']['frozen_trace_slope']*probes[-1]['h'],
                       'max_jump_quotient_identity_error':max(qerrors),'inactive_invalid_branch_calls':inactive_calls}}
