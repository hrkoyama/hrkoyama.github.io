"""All actual2D angular/M1 runs plus same-solver nonlinear-MMS/crossed controls."""
import numpy as np
import geometry
from io_contract import ROOT,case,check,checkpoint,save_fields,run


def one(spec,c,limits,output,cases,summary):
    name=spec['id'];out=geometry.solve(spec,output/(name+'-failed-state.npz'))
    out['history_columns']=np.array(['time','energy','outgoing_boundary','absorbed_energy','forcing_energy','budget_defect','minimum_energy','minimum_cone_slack'])
    save_fields(output,name,out) # Raw completed candidate precedes reference loading/time checks.
    with np.load(ROOT/'references'/(spec['kind']+'-n'+str(spec['cells'])+'.npz'),allow_pickle=False) as f:reference=f['moments'];reference_times=f['times']
    if not np.allclose(reference_times,out['times'],rtol=0,atol=1e-14):raise ValueError('Reference snapshot times differ')
    out['reference_moments']=reference;save_fields(output,name,out)
    error=float(np.max(np.mean(abs(out['moments'][-1]-reference[-1]),axis=(0,1))))
    h=out['history'];row=dict(**spec,fields=name+'.npz',independent_moment_l1=error,maximum_budget=float(h[:,5].max()),minimum_energy=float(h[:,6].min()),minimum_cone=float(h[:,7].min()))
    if spec['method']=='m1':
        row['directional_speed_diagnostics']={str(k):(int(v) if str(k)=='calls' or str(k).endswith('_states') else float(v)) for k,v in zip(out['speed_diagnostic_names'],out['speed_diagnostic_values'])}
    c['records'].append(row)
    check(c,name+'/all-stages-finite',0.,0.,np.isfinite(out['states']).all() and np.isfinite(h).all())
    check(c,name+'/positive-energy',float(h[:,6].min()),-limits['negative_energy'],h[:,6].min()>=-limits['negative_energy'])
    check(c,name+'/realizability',float(h[:,7].min()),-limits['realizability_slack'],h[:,7].min()>=-limits['realizability_slack'])
    check(c,name+'/energy-budget',float(h[:,5].max()),limits['budget'],h[:,5].max()<=limits['budget'])
    p=out['pressure'];trace=float(np.max(abs(p[...,0]+p[...,2]+p[...,3]-out['moments'][...,0])))
    check(c,name+'/full3D-pressure-trace',trace,limits['pressure_trace'],trace<=limits['pressure_trace'])
    check(c,name+'/five-fixed-snapshots',out['times'].tolist(),np.linspace(0,spec['final_time'],5).tolist(),len(out['times'])==5 and np.allclose(out['times'],np.linspace(0,spec['final_time'],5),rtol=0,atol=1e-14))
    summary.append([spec['cells'],0 if spec['method']=='sn' else 1,spec['steps'],error,float(h[:,5].max()),float(h[:,6].min()),float(h[:,7].min())]);checkpoint(output,cases)
    return row,out


def sequence_checks(kind,method,rows,fields,c,limits,reference_required=True):
    selected=[r for r in rows if r['kind']==kind and r['method']==method and r['family']=='refinement']
    if reference_required:
        for previous,current in zip(selected,selected[1:]):
            ratio=current['independent_moment_l1']/max(previous['independent_moment_l1'],1e-300)
            check(c,f'{kind}/{method}/refinement-n{current["cells"]}',ratio,limits['refinement_ratio'],ratio<=limits['refinement_ratio'])
        bound=limits[('shadow_'+method+'_finest_l1') if kind=='shadow' else ('mms_finest_l1' if kind=='mms' else 'crossed_finest_l1')]
        check(c,kind+'/'+method+'/finest-reference',selected[-1]['independent_moment_l1'],bound,selected[-1]['independent_moment_l1']<=bound)
    probe=next(r for r in rows if r['kind']==kind and r['method']==method and r['family']=='time-probe')
    fine=selected[-1];difference=float(np.max(np.mean(abs(fields[probe['id']]['moments'][-1]-fields[fine['id']]['moments'][-1]),axis=(0,1))))
    fraction=difference/max(fine['independent_moment_l1'],1e-300)
    check(c,kind+'/'+method+'/separate-time-sensitivity',fraction,limits['time_probe_fraction'],fraction<=limits['time_probe_fraction'])


def execute(cfg,limits,output,cases):
    for ident,table in cfg['cases'].items():
        c=case(ident);cases.append(c);checkpoint(output,cases);rows=[];fields={};summary=[]
        for spec in table:
            row,out=one(spec,c,limits,output,cases,summary);rows.append(row);fields[row['id']]=out
        kind=table[0]['kind']
        for method in ['sn','m1']:
            # M1 opposing-beam mismatch is an expected closure model difference.
            sequence_checks(kind,method,rows,fields,c,limits,reference_required=not(kind=='beams' and method=='m1'))
        if kind=='beams':
            controls=[]
            for spec in cfg['same_solver_controls']:
                row,out=one(spec,c,limits,output,cases,summary);rows.append(row);fields[row['id']]=out;controls.append(row)
            sequence_checks('mms','m1',rows,fields,c,limits)
            sequence_checks('crossed','sn',rows,fields,c,limits)
            fine=fields['beams-m1-n96'];exact=fine['reference_moments'][2];mask=exact[...,0]>.1
            # Exact head-on packet moments at meeting have F0,Pxx=E; M1givesE/3.
            predicted_pressure=geometry.pressure(exact)[...,0]
            normalized_defect=np.mean(abs(exact[...,0][mask]-predicted_pressure[mask])/exact[...,0][mask])
            check(c,'head-on-closure-information-defect',float(normalized_defect),2/3,abs(normalized_defect-2/3)<=2e-14)
            c['metrics']['same_solver_controls']=['nonlinear-closed-M1-MMS','actual-x-and-y-crossed-angular-packets']
            c['metrics']['M1_transport_difference_is_model_error']=True
        c['metrics']['M1_numerical_flux']='General directional localLF:max endpoint spectralradius,LFcone-splitting bound and absolute normal reducedflux;not a nonlinearRiemannfan bound'
        c['metrics'].update(completed_primary_and_control_runs=len(c['records']),spatial_dimensions=2,angular_dimensions=3,Pzz_retained=True)
        np.savetxt(output/(ident+'.csv'),np.array(summary),delimiter=',',header='cells,method0SN1M1,steps,moment_l1,max_budget,min_energy,min_cone',comments='',fmt='%.16e')
        c['passed']=bool(all(c['checks'].values()));checkpoint(output,cases)
if __name__=='__main__':run(execute)
