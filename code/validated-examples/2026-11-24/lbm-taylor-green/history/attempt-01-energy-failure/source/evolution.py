"""Actual fixed-step kinetic trajectories with saved states and native-stage ledgers."""
import csv
import json
from pathlib import Path
import numpy as np
from geometry import full_field,moments

def dump(path,data):Path(path).write_text(json.dumps(data,ensure_ascii=False,indent=2,allow_nan=False)+'\n')

def trajectory(native,g,tau,steps,checkpoints,f0,out,label):
    if any(type(k) is not int or k<=0 or k>steps for k in checkpoints) or checkpoints[-1]!=steps:
        raise ValueError('Fixed integer checkpoint/endpoint mismatch')
    f=f0.copy();histories=[];states={0:f0.copy()};completed=0
    active=out/(label+'-active.npz');partial_csv=out/(label+'-ledger.csv')
    with partial_csv.open('w',newline='') as stream:
        writer=csv.writer(stream);writer.writerow(['step','mass','px','py','boundary_mass','boundary_px',
            'boundary_py','body_fx','body_fy','body_torque','max_mach','min_rho','max_rho',
            'min_population','wall_mass','open_mass','wall_torque'])
        for target in checkpoints:
            while completed<target:
                chunk=min(1000,target-completed)
                dump(out/'active-stage.json',dict(run=label,completed_steps=completed,next_steps=chunk,
                                                fixed_total_steps=steps,tau=tau,dx=g['dx'],dt=g['dt']))
                h=native.advance(f,g,tau,chunk)
                for j,row in enumerate(h):writer.writerow([completed+j,*row.tolist()])
                stream.flush();histories.append(h);completed+=chunk
                np.savez(active,f=f,completed_steps=np.array(completed),time=np.array(completed*g['dt']))
            states[target]=f.copy()
    h=np.concatenate(histories);rho,u=moments(f)
    arrays=dict(f=f,rho=rho,velocity_lattice=u,x=g['x'],y=g['y'],mask=g['mask'].astype(np.int8),
                history=h,initial_f=f0,dx=np.array(g['dx']),dt=np.array(g['dt']),tau=np.array(tau),
                steps=np.array(steps),time=np.array(steps*g['dt']),source=g['source'],kind=g['kind'],
                fraction=g['fraction'],wall_dot=g['wall_dot'],lever=g['lever'])
    for key,state in states.items():arrays['state_'+str(key)]=state
    np.savez_compressed(out/(label+'.npz'),**arrays)
    return f,h,states,arrays
