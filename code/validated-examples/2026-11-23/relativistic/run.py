#!/usr/bin/env python3
"""Six fixed, actual SRHD/RMHD FV runs; public verifier result envelope."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import relativistic as s
from references import exact as e
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2,allow_nan=False)+'\n')


def verify_contract():
    c=json.loads((ROOT/'pre-run-contract.json').read_text())
    for p,h in c['files_sha256'].items():
        if sha(ROOT/p)!=h:raise ValueError('changed scientific contract '+p)
    return c


def run_case(ident,cfg,common,limits,output):
    rows=[];checks={};wave=ident=='srmhd-alfven'
    va=e.alfven_speed(cfg['rho'],cfg['pressure'],cfg['bx'],cfg.get('eta',1.),cfg['gamma']) if wave else 0.
    final=cfg['periods']/va if wave else cfg['final_time'];star=None if wave else e.collision_star(cfg['rho'],cfg['pressure'],cfg['speed'],cfg['gamma'])
    for n in cfg['grids']:
        edges=np.linspace(0,1,n+1)
        reference=lambda t:e.alfven_means(edges,t,cfg['rho'],cfg['pressure'],cfg['bx'],cfg['eta'],cfg['gamma']) if wave else e.collision_means(edges,t,cfg['rho'],cfg['pressure'],cfg['speed'],cfg['gamma'])
        try:
            out=s.solve(reference(0.),cfg['bx'],cfg['gamma'],final,wave,common['cfl'],common['snapshots'])
        except s.PhysicsFailure as error:
            np.savez_compressed(output/'failed-state.npz',case_id=ident,n=n,**error.payload)
            dump(output/'failed-state.json',dict(case_id=ident,n=n,message=str(error),
                 step=int(error.payload['step']),stage=int(error.payload['stage']),time=float(error.payload['time']),
                 stage_time=float(error.payload['stage_time']),candidate_unmodified=True,
                 face_primitives_available=bool(error.payload['face_primitives_available'])))
            raise
        refs=np.array([reference(t) for t in out['snapshot_times']]);out['U_reference_history']=refs
        diff=abs(out['U']-refs[-1]);l1=np.mean(diff,axis=0)/np.maximum(1.,np.mean(abs(refs[-1]),axis=0))
        stages=out['stages'];balance=float(np.max(abs(out['conservation'][:,1:8])))
        row=dict(n=n,time=out['time'],steps=out['steps'],component_l1=l1.tolist(),maximum_balance=balance,
                 minimum_density=float(stages[:,3].min()),minimum_pressure=float(stages[:,4].min()),
                 maximum_speed=float(stages[:,5].max()),maximum_root_residual=float(stages[:,6].max()),
                 maximum_roundtrip_residual=float(stages[:,7].max()),maximum_recovery_iterations=int(stages[:,8].max()),
                 safeguarded_root_steps=int(stages[:,9].sum()),minimum_face_density=float(stages[:,10].min()),
                 minimum_face_pressure=float(stages[:,11].min()),maximum_face_speed=float(stages[:,12].max()),
                 recorded_stages=len(stages),state_floor_count=out['state_floor_count'],retries=out['retries'],rejected_steps=out['rejected_steps'])
        if wave:
            denom=np.mean(abs(refs[-1,:,5:7]));errors=np.mean(abs(out['U_history'][:,:,5:7]-refs[:,:,5:7]),axis=(1,2))/denom
            q=out['U'][:,5]+1j*out['U'][:,6];qr=refs[-1,:,5]+1j*refs[-1,:,6]
            fourier=np.mean(q*np.exp(-2j*np.pi*out['x']));expected=np.mean(qr*np.exp(-2j*np.pi*out['x']))
            row.update(transverse_relative_l1=float(errors[-1]),intermediate_relative_l1=errors[1:-1].tolist(),
                       phase_error=float(abs(np.angle(fourier/expected))),amplitude_error=float(abs(abs(fourier/expected)-1)),
                       bx_constant=cfg['bx'],lorentz_reference=float(1/np.sqrt(1-cfg['eta']**2*va**2)))
        else:
            half=.5*star['speed']*final;mask=abs(out['x']-.5)<half
            row['star_pressure_relative']=float(abs(np.mean(out['primitive'][mask,4])-star['pressure'])/star['pressure'])
            grad=abs(np.diff(out['primitive'][:,4]));halfindex=n//2
            locations=[float(edges[1:-1][np.argmax(grad[:halfindex])]),float(edges[1:-1][halfindex+np.argmax(grad[halfindex:])])]
            row['shock_location_error']=float(max(abs(locations[0]-(.5-star['speed']*final)),abs(locations[1]-(.5+star['speed']*final))))
            row['shock_locations']=locations
            row['symmetry_error']=float(max(np.max(abs(out['U'][:,0]-out['U'][::-1,0])),np.max(abs(out['U'][:,1]+out['U'][::-1,1]))))
            # Independent pressure-root SRHD recovery/flux on actual final states, not invented fixtures.
            error=0.
            for j in np.linspace(0,n-1,9,dtype=int):
                wr,fr=e.independent_srhd(out['U'][j],cfg['gamma']);_,fp=s.state(out['primitive'][j],0.,cfg['gamma'])
                error=max(error,float(np.max(abs(wr-out['primitive'][j]))),float(np.max(abs(fr-fp))))
            row['independent_zero_B_error']=error
        row['field_file']=f'{ident}-n{n}.npz';np.savez_compressed(output/row['field_file'],**out)
        prefix='n'+str(n)+': '
        basic={
          'fixed final time':out['time']==final,'five saved times':len(out['snapshot_times'])==common['snapshots'],
          'four records per SSP step':len(stages)==4*out['steps'],
          'all stored arrays finite':all(bool(np.all(np.isfinite(out[k]))) for k in ['U','U_history','U_reference_history','stages','conservation']),
          'positive stage density':row['minimum_density']>0,'positive stage pressure':row['minimum_pressure']>0,
          'subluminal stages':row['maximum_speed']<1,'positive reconstructed face density':row['minimum_face_density']>0,
          'positive reconstructed face pressure':row['minimum_face_pressure']>0,'subluminal reconstructed faces':row['maximum_face_speed']<1,
          'conserved finite-volume boundary budget':balance<=limits['balance'],
          'physical root residual':row['maximum_root_residual']<=limits['root_residual'],
          'full conserved primitive roundtrip':row['maximum_roundtrip_residual']<=limits['roundtrip_residual'],
          'no state floor or retry':row['state_floor_count']+row['retries']+row['rejected_steps']==0}
        checks.update({prefix+k:bool(v) for k,v in basic.items()})
        if wave:
            checks[prefix+'actual magnetic wave present']=bool(np.ptp(out['U'][:,5])>.5*cfg['eta']*cfg['bx'])
            checks[prefix+'intermediate wave errors']=bool(max(row['intermediate_relative_l1'])<=limits['wave_intermediate_relative_l1'])
        else:
            checks[prefix+'reflection symmetry']=row['symmetry_error']<=limits['collision_symmetry']
            checks[prefix+'independent SRHD zero B flux and recovery']=row['independent_zero_B_error']<=limits['independent_zero_B']
        rows.append(row)
        dump(output/(ident+'-completed-grids.json'),dict(case_id=ident,completed_grids=rows))
        print(ident,n,'steps',row['steps'],'balance',balance,flush=True)
    if wave:
        errors=[r['transverse_relative_l1'] for r in rows];orders=np.log2(np.array(errors[:-1])/errors[1:]).tolist()
        checks.update({'finest transverse L1':errors[-1]<=limits['wave_finest_transverse_relative_l1'],
                       'finest wave phase':rows[-1]['phase_error']<=limits['wave_finest_phase_error'],
                       'finest wave amplitude':rows[-1]['amplitude_error']<=limits['wave_finest_amplitude_error'],
                       'minimum observed grid order':min(orders)>=limits['wave_minimum_observed_order']})
        for i in [1,2]:checks['wave refinement '+str(i)]=errors[i]/errors[i-1]<=limits['wave_refinement_ratio']
        metrics=dict(alfven_speed=va,period=final,finest_transverse_relative_l1=errors[-1],observed_orders=orders,
                     exact_scope='Nonlinear finite-amplitude circular polarization; not linear passive transport or a generic RMHD Riemann reference.')
    else:
        checks.update({'finest D L1':rows[-1]['component_l1'][0]<=limits['collision_finest_D_l1'],
                       'finest total E L1':rows[-1]['component_l1'][4]<=limits['collision_finest_E_l1'],
                       'finest star pressure':rows[-1]['star_pressure_relative']<=limits['collision_star_pressure_relative'],
                       'finest shock position':rows[-1]['shock_location_error']<=limits['collision_shock_location']})
        for i in [1,2]:
            for k in [0,4]:checks['collision component '+str(k)+' refinement '+str(i)]=rows[i]['component_l1'][k]/rows[i-1]['component_l1'][k]<=limits['collision_refinement_ratio']
        metrics=dict(exact_star=star,finest_D_l1=rows[-1]['component_l1'][0],finest_E_l1=rows[-1]['component_l1'][4],
                     exact_scope='Symmetric identical thermodynamics, opposite normal velocities: two shocks and resting identical star states; no nontrivial contact or general three-wave certification.')
    with (output/(ident+'.csv')).open('w',newline='') as stream:
        keys=[k for k,v in rows[0].items() if not isinstance(v,(dict,list))];writer=csv.DictWriter(stream,fieldnames=keys,extrasaction='ignore');writer.writeheader();writer.writerows(rows)
    return dict(id=ident,passed=bool(all(checks.values())),checks=checks,metrics=metrics,records=rows)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--input',type=Path,default=ROOT/'inputs.json');parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    start=time.monotonic();contract=verify_contract();cfg=json.loads(args.input.read_text());limits=json.loads((ROOT/'acceptance.json').read_text())['limits']
    if sha(args.input)!=sha(ROOT/'inputs.json'):raise ValueError('only frozen input accepted')
    args.output.mkdir(parents=True,exist_ok=True);qualification=e.qualify();dump(args.output/'reference-qualification.json',qualification)
    if not qualification['passed']:raise ValueError('analytic reference qualification failed')
    cases=[run_case(i,c,cfg,limits,args.output) for i,c in cfg['cases'].items()]
    result=dict(schema_version=1,passed=all(c['passed'] for c in cases),checks={c['id']:c['passed'] for c in cases},cases=cases,
                termination='fixed_budget_completed',failure=None,input_sha256=sha(args.input),
                source_sha256={p:sha(ROOT/p) for p in [*contract['files_sha256'],'pre-run-contract.json']},
                reference_qualification=qualification,duration_seconds=time.monotonic()-start,
                numerical_gate_count=sum(len(c['checks']) for c in cases))
    dump(args.output/'result.json',result);print(json.dumps(dict(passed=result['passed'],gates=result['numerical_gate_count'],seconds=result['duration_seconds'])),flush=True)
    raise SystemExit(0 if result['passed'] else 1)


if __name__=='__main__':main()
