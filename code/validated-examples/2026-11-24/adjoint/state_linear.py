"""State-only expanded solve integration; derivatives retain ordinary GMRES."""
from pathlib import Path
import hashlib
import json
import numpy as np
from krylov import norm
from state_krylov import gmres
from state_jacobian import jac_action
from state_expansion import residual
from io_contract import save_npz, save_json, native


def solve(u, coefficient, b, rtol, settings, factor, partial=None, retained=None):
    n=len(b);reaction=coefficient*np.exp(u);Pout,Pscratch=np.zeros(n),np.zeros(n)
    counts={'direction_Jv':0,'expanded_residual9':0,'projected_residual9':0,'preconditioner':0,'factor_builds':0}
    memory={'observed_named_peak_owned_bytes':0,'peak_low_part_elements':0,'peak_inventory':[],'stage_counts':{}}
    last_summary={}
    direction_last={}
    fixed={'base_state':u,'physical_coefficient':np.broadcast_to(coefficient,(n,)),
           'reaction_float':reaction,'actual_RHS':b,'Thomas_output':Pout,'Thomas_forward_scratch':Pscratch,**factor.arrays('P')}
    if retained is not None:
        fixed.update({'outer_retention.'+k:v for k,v in retained.items() if isinstance(v,np.ndarray)})
    def observe(stage,arrays,summary):
        all_arrays={**fixed,**direction_last,**arrays};owners={};low=set();entries=[]
        for name,a in all_arrays.items():
            root=a
            while isinstance(root.base,np.ndarray):root=root.base
            key=id(root);owners[key]=root
            if name in ['lo','base_lo','reconstruct_new_lo']:low.add(key)
            entries.append({'name':name,'shape':list(a.shape),'owner_bytes':int(root.nbytes),
                'owner_alias':next((e['name'] for e in entries if e['_id']==key),name),'_id':key})
        total=sum(a.nbytes for a in owners.values());low_elements=sum(owners[k].size for k in low)
        memory['stage_counts'][stage]=memory['stage_counts'].get(stage,0)+1
        if total>memory['observed_named_peak_owned_bytes'] or low_elements>memory['peak_low_part_elements']:
            memory['peak_inventory'].append({'stage':stage,'snapshot_owned_bytes':int(total),'low_part_elements':int(low_elements),
                'arrays':[{k:v for k,v in e.items() if k!='_id'} for e in entries]})
        memory['observed_named_peak_owned_bytes']=max(memory['observed_named_peak_owned_bytes'],int(total))
        memory['peak_low_part_elements']=max(memory['peak_low_part_elements'],int(low_elements))
        last_summary.clear();last_summary.update(stage=stage,**summary)
        if partial is not None:
            save_npz(partial,all_arrays)
            save_json(Path(partial).with_suffix('.json'),{'mode':'state_expanded_hi_plus_lo',
                'summary':last_summary,'counts':counts,'memory':memory,
                'scope':'Named snapshots,not measuredfullpeak/RSS. Expandedstatus is never a projectedvectorstatus.'})
    def direction(v):
        counts['direction_Jv']+=1
        direction_last['last_direction_input']=v.copy()
        direction_last.pop('last_direction_output',None)
        out=jac_action(u,coefficient,v)
        direction_last['last_direction_output']=out.copy()
        return out
    def remainder(hi,lo,observer=None):
        counts['expanded_residual9']+=1
        return residual(b,reaction,hi,lo,observer)
    def precondition(v):
        counts['preconditioner']+=1
        return factor.solve(v,out=Pout,scratch=Pscratch)
    cfg=settings['gmres']
    out=gmres(direction,b,precondition,cfg['restart'],cfg['max_iterations'],rtol,remainder,observe)
    # Preserve both completed components before projection/diagnostics.
    if partial is not None:
        save_npz(partial,x_hi=out['hi'],x_lo=out['lo'],actual_RHS=b,true_history=out['residuals'],
            QR_history=out['estimates'],expanded_rawpassed=out['passed'],iterations=out['iterations'])
    projected=np.add(out['hi'],out['lo']);zeros=np.zeros_like(projected)
    counts['projected_residual9']+=1
    projected_residual=residual(b,reaction,projected,zeros)
    actual_residual=residual(b,reaction,out['hi'],out['lo'])
    counts['expanded_residual9']+=1
    actual=norm(actual_residual);projected_norm=norm(projected_residual)
    if bool(out['passed'])!=(actual<=out['target']):raise ArithmeticError('Expanded true-target decision mismatch')
    observe('returned-projection',{'hi':out['hi'],'lo':out['lo'],'projected_RN_hi_plus_lo':projected,
        'projection_zero_lo':zeros,'expanded_residual':actual_residual,'projected_residual':projected_residual,
        'true_history':out['residuals'],'QR_history':out['estimates']},
        {'iterations':out['iterations'],'target':out['target'],'restart_count':out['restart_count']})
    m=cfg['restart'];cap=cfg['max_iterations']
    allowances={'new_Arnoldi_blocks_while_old_live':8*(n*(m+1)+n*m+(m+1)*m),
        'new_restart_base_hi_lo_while_old_live':8*(2*n),'new_Givens_vectors_while_old_live':8*(3*m+1),
        'new_backsolve_y_while_old_live':8*m,'direction_exp_diagonal_output_copy_family':8*(4*n),
        'ordinary_elementwise_and_validation_temporary':8*(2*n),'returned_true_and_QR_history_arrays':8*(2*cap+1)}
    memory.update(conservative_unobserved_allowances_bytes=allowances,
        conservative_named_numeric_storage_upper_bytes=memory['observed_named_peak_owned_bytes']+sum(allowances.values()),
        scope='Observed named arrays and separately summed conservative numeric-storage allowance,not measuredfullpeak/Python/I/O/allocator/RSS. Old+new blocks andmultiplelowparts explicitlylisted; not subject to62state40n gate.')
    out.update(projected=projected,projected_residual=projected_norm,projected_target_met=bool(projected_norm<=out['target']),
        actual_true_residual=actual,counts=counts,memory=memory,representation='state_expanded_hi_plus_lo')
    if partial is not None:
        save_json(Path(partial).with_suffix('.json'),{'mode':out['representation'],'expanded_target_met':bool(out['passed']),
            'projected_target_met':out['projected_target_met'],'expanded_true_residual':actual,
            'projected_true_residual':projected_norm,'target':out['target'],'iterations':out['iterations'],
            'counts':counts,'memory':memory})
    evidence=None
    if partial is not None:
        evidence_path=Path(partial).with_suffix('.memory.jsonl')
        record={'mode':out['representation'],'input_sha256':{
            'u':hashlib.sha256(u.tobytes()).hexdigest(),'coefficient':hashlib.sha256(np.asarray(coefficient).tobytes()).hexdigest(),
            'RHS':hashlib.sha256(b.tobytes()).hexdigest()},'iterations':out['iterations'],
            'expanded_target_met':bool(out['passed']),'projected_target_met':out['projected_target_met'],
            'target':out['target'],'counts':counts,'memory':memory}
        line=(json.dumps(native(record),ensure_ascii=False,sort_keys=True,allow_nan=False,separators=(',',':'))+'\n').encode()
        offset=evidence_path.stat().st_size if evidence_path.exists() else 0
        with evidence_path.open('ab') as handle:handle.write(line)
        evidence={'file':evidence_path.name,'byte_offset':offset,'record_bytes':len(line),'record_sha256':hashlib.sha256(line).hexdigest()}
    out['memory_summary']={'observed_named_peak_owned_bytes':memory['observed_named_peak_owned_bytes'],
        'peak_low_part_elements':memory['peak_low_part_elements'],
        'conservative_named_numeric_storage_upper_bytes':memory['conservative_named_numeric_storage_upper_bytes'],
        'allowances_bytes':allowances,'scope':memory['scope'],'full_inventory_evidence':evidence}
    return out
