#!/usr/bin/env python3
"""Frozen small MHD refinement studies with analytic and independent CT references."""
import argparse,csv,hashlib,json,time,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent/"references"))
import hlld,solver
from references import analytic
from references.qualify import restrict,pressure,relative_l1
from references.qualify_saved import qualify
ROOT=Path(__file__).resolve().parent


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def save(path,value):Path(path).write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n')


def check_frozen(root=ROOT):
    root=Path(root);contract=json.loads((root/'pre-run-contract.json').read_text())
    for name,digest in contract['files_sha256'].items():
        if sha(root/name)!=digest:raise ValueError('Changed frozen source/input/reference '+name)
    return contract


def specifications(cfg):
    return [dict(id=f'{case}-n{n}',case=case,n=n,steps=c['steps'],time=c['final_time'],family='refinement') for case,c in cfg['cases'].items() for n in c['grids']]+[dict(id=f'{case}-half-dt',case=case,n=c['grids'][-1],steps=c['steps']*c['time_probe_factor'],time=c['final_time'],family='time-probe') for case,c in cfg['cases'].items()]


def fields(case,q):
    if case=='circular-alfven-refinement':return {'transverse':q[..., [2,3,6,7]]}
    if case=='magnetic-loop-independent':return {'magnetic':q[...,5:7]}
    return {'density':q[...,0],'pressure':pressure(q)}


def errors(case,q,reference):
    a,b=fields(case,q),fields(case,reference)
    return {k:{'relative_l1':relative_l1(a[k],b[k]),'relative_l2':float(np.linalg.norm(a[k]-b[k])/np.linalg.norm(b[k])),'absolute_linf':float(np.max(abs(a[k]-b[k])))} for k in a}


def comparison(case,q,other):return {k:v['relative_l1'] for k,v in errors(case,q,other).items()}


def phase_error(q,reference):
    theta=2*np.pi*(np.arange(len(q))+.5)/len(q)
    mode=lambda a:np.sum((a[:,6]+1j*a[:,7])*np.exp(-1j*theta))
    return float(abs(np.angle(mode(q)/mode(reference))))


def load_references():
    r=ROOT/'references';result=json.loads((r/'reference-qualification.json').read_text());plan=json.loads((r/'reference-input-plan.json').read_text())
    for row in result['records']:
        if sha(r/row['file'])!=row['sha256']:raise ValueError('Changed independent reference '+row['file'])
    quality=qualify(r,result['records'],plan)
    if not result['passed'] or not quality['passed']:raise ValueError('Unqualified independent reference')
    return {row['id']:np.load(r/row['file'],allow_pickle=False)['q_history'][-1] for row in result['records']},quality


def evaluate(case,records,cfg,limits,qualification,analytic_difference):
    checks=[]
    def add(name,value,bound,passed):checks.append(dict(name=name,value=value,bound=bound,passed=bool(passed)))
    rows=[r for r in records if r['case']==case];c=cfg['cases'][case]
    add('four prescribed fixed runs',len(rows),4,len(rows)==4)
    add('qualified independent reference',qualification['passed'],True,qualification['passed'])
    if case=='circular-alfven-refinement':add('independent analytic conserved quadrature',analytic_difference,limits['analytic_quadrature'],analytic_difference<=limits['analytic_quadrature'])
    for row in rows:
        name=row['id']+' '
        add(name+'all stages finite positive',row['finite_positive'],True,row['finite_positive'])
        add(name+'final time',row['time'],c['final_time'],row['time']==c['final_time'])
        add(name+'five exact snapshots',row['snapshot_times'],np.linspace(0,c['final_time'],5).tolist(),np.allclose(row['snapshot_times'],np.linspace(0,c['final_time'],5),atol=1e-14,rtol=0))
        for label,key,bound in [('fluid integral conservation','maximum_fluid_integral_defect',limits['conservation']),('native face divergence','maximum_native_divergence',limits['native_divergence']),('measured Courant sum','maximum_courant_sum',limits['maximum_courant_sum'])]:add(name+label,row[key],bound,row[key]<=bound)
        add(name+'no cell clips or retries',[row['state_clip_count'],row['retries']],[0,0],row['state_clip_count']==0 and row['retries']==0)
        add(name+'explicit fallback accounting',row['fallback_faces'],row['fallback_count_from_history'],row['fallback_faces']==row['fallback_count_from_history'])
    sequence=[r for r in rows if r['family']=='refinement'];probe=next((r for r in rows if r['family']=='time-probe'),None)
    if len(sequence)==3:
        keys=list(sequence[-1]['errors']);fine=sequence[-1]
        for key in keys:
            measure='relative_l2' if case=='circular-alfven-refinement' else 'relative_l1'
            for previous,current in zip(sequence,sequence[1:]):
                ratio=current['errors'][key][measure]/previous['errors'][key][measure]
                add(f'{key} refinement n{current["n"]}',ratio,limits['refinement_error_ratio'],ratio<=limits['refinement_error_ratio'])
            bound=limits[{'transverse':'wave_finest_relative_l2','magnetic':'loop_finest_relative_magnetic_l1','density':'ot_finest_relative_density_l1','pressure':'ot_finest_relative_pressure_l1'}[key]]
            add(key+' finest error',fine['errors'][key][measure],bound,fine['errors'][key][measure]<=bound)
            if probe:
                fraction=probe['time_half_difference'][key]/fine['errors'][key]['relative_l1']
                add(key+' separate time contamination fraction',fraction,limits['time_contamination_fraction'],fraction<=limits['time_contamination_fraction'])
            if case!='circular-alfven-refinement':
                fraction=fine['reference_increment'][key]/fine['errors'][key]['relative_l1']
                add(key+' reference increment/error',fraction,limits['reference_increment_error_fraction'],fraction<=limits['reference_increment_error_fraction'])
        if case=='circular-alfven-refinement':
            order=float(np.log2(sequence[-2]['errors']['transverse']['relative_l2']/fine['errors']['transverse']['relative_l2']))
            add('selected wave last observed order',order,limits['wave_last_order_minimum'],order>=limits['wave_last_order_minimum'])
            add('selected wave phase error',fine['phase_error_radians'],limits['wave_finest_phase_error_radians'],fine['phase_error_radians']<=limits['wave_finest_phase_error_radians'])
        if case=='postshock-orszag-tang':add('late density compression diagnostic',fine['density_contrast'],limits['ot_density_contrast_minimum'],fine['density_contrast']>=limits['ot_density_contrast_minimum'])
    return checks


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,default=ROOT/'inputs.json');p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    contract=check_frozen()
    if sha(a.input)!=contract['files_sha256']['inputs.json']:raise ValueError('Use frozen input bytes')
    cfg=json.loads(a.input.read_text());limits=json.loads((ROOT/'acceptance.json').read_text())['limits']
    if a.output.exists() and any(a.output.iterdir()):raise ValueError('Use fresh output directory')
    a.output.mkdir(parents=True,exist_ok=True);start=time.monotonic();rows=[];files={};failure=None;quality={'passed':False};quadrature=1.;active=None;completed={}
    try:
        refs,quality=load_references()
        quadrature=max(float(np.max(abs(solver.exact_wave(n,t)-analytic.wave_means(n,t)))) for n in cfg['cases']['circular-alfven-refinement']['grids'] for t in np.linspace(0,1,5))
        for spec in specifications(cfg):
            active=spec;case=spec['case'];c=cfg['cases'][case]
            out=solver.solve(case,spec['n'],spec['steps'],spec['time'],deadline=start+cfg['main_budget_seconds'])
            q=out['q'];reference=solver.exact_wave(spec['n'],spec['time']) if q.ndim==2 else restrict(refs[c['reference_fine']],q.shape[:2])
            name=spec['id']+'.npz';np.savez_compressed(a.output/name,**out,q_reference=reference)
            files[name]=sha(a.output/name)
            history_file=spec['id']+'-history.csv';np.savetxt(a.output/history_file,out['history'],delimiter=',',header=','.join(solver.HISTORY_COLUMNS),comments='',fmt='%.16e');files[history_file]=sha(a.output/history_file)
            if q.ndim==2:coordinates=((np.arange(len(q))+.5)*out['dx'])[:,None];coordinate_names=['x']
            else:
                domain=c['domain'];x=domain[0][0]+(np.arange(q.shape[0])+.5)*out['dx'];y=domain[1][0]+(np.arange(q.shape[1])+.5)*out['dy'];xx,yy=np.meshgrid(x,y,indexing='ij');coordinates=np.stack([xx,yy],axis=-1).reshape(-1,2);coordinate_names=['x','y']
            field_file=spec['id']+'-final-fields.csv';names=['rho','mx','my','mz','E','Bx','By','Bz'];np.savetxt(a.output/field_file,np.column_stack([coordinates,q.reshape(-1,8),reference.reshape(-1,8)]),delimiter=',',header=','.join(coordinate_names+names+['reference_'+k for k in names]),comments='',fmt='%.16e');files[field_file]=sha(a.output/field_file)
            h=out['history'];row={**spec,'field':name,'snapshot_times':out['times'].tolist(),'errors':errors(case,q,reference),'finite_positive':bool(np.isfinite(h).all() and np.isfinite(out['q_history']).all() and min(h[:,2:6].min(),out['q_initial'][...,0].min(),hlld.primitive(out['q_initial'])[...,4].min())>0),'maximum_fluid_integral_defect':float(h[:,8].max()),'maximum_native_divergence':float(h[:,6].max()),'maximum_common_cell_divergence':float(h[:,7].max()),'reference_common_cell_divergence':solver.common_divergence(reference,out['dx'],out['dy']),'maximum_courant_sum':float(h[:,9].max()),'fallback_faces':out['fallback_faces'],'fallback_count_from_history':int(h[:,10].sum()),'degenerate_faces':int(h[:,11].sum()),'reconstruction_scalings':out['reconstruction_scalings'],'minimum_theta':out['minimum_theta'],'minimum_density':float(h[:,2].min()),'minimum_pressure':float(h[:,3].min()),'state_clip_count':out['state_clip_count'],'retries':out['retries'],'maximum_abs_bz':float(h[:,14].max())}
            if case=='circular-alfven-refinement':row['phase_error_radians']=phase_error(q,reference)
            else:row['reference_increment']=comparison(case,restrict(refs[c['reference_coarse']],q.shape[:2]),reference)
            if case=='postshock-orszag-tang':row['density_contrast']=float(q[...,0].max()/q[...,0].min())
            if spec['family']=='refinement':completed[case]=q.copy()
            else:row['time_half_difference']=comparison(case,q,completed[case])
            rows.append(row);print(json.dumps({'completed':spec['id'],'seconds':time.monotonic()-start}),flush=True)
    except Exception as error:
        failure=dict(type=type(error).__name__,message=str(error),active_run=active)
        if isinstance(error,solver.StageFailure):
            np.savez_compressed(a.output/'failed-stage.npz',q=error.q);files['failed-stage.npz']=sha(a.output/'failed-stage.npz');failure['stage']=error.context
    cases=[]
    for case in cfg['cases']:
        checks=evaluate(case,rows,cfg,limits,quality,quadrature);selected=[r for r in rows if r['case']==case]
        with (a.output/(case+'.csv')).open('w',newline='') as f:
            columns=['id','n','steps','time','family','minimum_density','minimum_pressure','maximum_fluid_integral_defect','maximum_native_divergence','maximum_common_cell_divergence','reference_common_cell_divergence','maximum_courant_sum','fallback_faces','degenerate_faces','reconstruction_scalings','minimum_theta','state_clip_count','retries'];w=csv.DictWriter(f,fieldnames=columns,extrasaction='ignore');w.writeheader();w.writerows(selected)
        files[case+'.csv']=sha(a.output/(case+'.csv'))
        cases.append(dict(id=case,passed=len(selected)==4 and all(x['passed'] for x in checks),checks={x['name']:x['passed'] for x in checks},check_details=checks,records=selected,metrics={'completed_pde_runs':len(selected),'reference_qualification_passed':quality['passed'],'analytic_quadrature_difference':quadrature if case=='circular-alfven-refinement' else None}))
    result=dict(schema_version=1,passed=failure is None and all(c['passed'] for c in cases),cases=cases,checks={c['id']:c['passed'] for c in cases},termination='calculation_failed' if failure else 'fixed_budget_completed',failure=failure,input_sha256=sha(a.input),files_sha256=files,source_sha256={name:sha(ROOT/name) for name in [*contract['files_sha256'],'pre-run-contract.json']},duration_seconds=time.monotonic()-start)
    save(a.output/'result.json',result);print(json.dumps(dict(passed=result['passed'],runs=len(rows),gates=sum(len(c['checks']) for c in cases),failed=[x for c in cases for x in c['check_details'] if not x['passed']],failure=failure)),flush=True)
    return 0 if result['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
