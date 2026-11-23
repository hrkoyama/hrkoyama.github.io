"""Explicitly invoked independent SPARTA reference generation, not public main.

No reference simulation is run without --execute. Input writing is static.
The run list and qualification are fixed in reference-protocol.json.
"""
import argparse, hashlib, json, subprocess, time
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
MASS=1.380649e-23


def make_input(case, configuration, seed):
    length=case['length']; cells=configuration['cells'];dt=configuration['dt']
    burn=round(case['burn_in']/dt);total=round(case['sample_time']/dt)
    block=total//case['blocks']; every=10
    if total%case['blocks'] or block%every or burn%block:
        raise ValueError('Integral SPARTA block/burn schedule required')
    lines=['seed '+str(seed),'units si','dimension 3',
           'global gridcut 0.0','boundary '+('o p p' if case['kind']=='shock' else 's p p'),
           f'create_box 0 {length} 0 1 0 1',f'create_grid {cells} 1 1',
           f'global fnum {case["weight"]:.17g} nrho 1 temp 1',
           'species hs.species HS','mixture gas HS nrho 1 temp 1',
           'collide vss all hs.vss',f'timestep {dt:.17g}']
    if case['kind']=='shock':
        from math import sqrt
        u1=2*sqrt(5/3);u2=u1*7/16
        lines += [f'region left block 0 {length/2} INF INF INF INF',
                  f'region right block {length/2} {length} INF INF INF INF',
                  f'mixture up HS nrho 1 temp 1 vstream {u1:.17g} 0 0',
                  f'mixture down HS nrho {16/7:.17g} temp {133/64:.17g} vstream {u2:.17g} 0 0',
                  'create_particles up n 0 region left', 'create_particles down n 0 region right',
                  'fix inletL emit/face up xlo','fix inletR emit/face down xhi']
    else:
        temp=case['temperatures'];speed=case['speeds']
        lines += [f'mixture gas temp {sum(temp)/2:.17g}', 'create_particles gas n 0',
                  f'surf_collide cold diffuse {temp[0]} 1 translate 0 {speed[0]} 0',
                  f'surf_collide hot diffuse {temp[1]} 1 translate 0 {speed[1]} 0',
                  'bound_modify xlo collide cold','bound_modify xhi collide hot']
    lines += ['stats 1000','stats_style step cpu np nattempt ncoll',f'run {burn}',
              'compute basic grid all all nrho u v w usq vsq wsq',
              'compute tensor pflux/grid all all momxx momxy momxz',
              'compute heat eflux/grid all all heatx',
              f'fix avg ave/grid all {every} {block//every} {block} c_basic[*] c_tensor[*] c_heat[*]',
              f'dump profiles grid all {block} profiles.grid id xc f_avg[*]',
              'dump_modify profiles format float %.17g',f'run {total}']
    return '\n'.join(lines)+'\n'


def parse_dump(path):
    lines=path.read_text().splitlines(); frames=[];times=[];i=0
    while i<len(lines):
        if lines[i]!='ITEM: TIMESTEP':i+=1;continue
        step=int(lines[i+1]);i+=2
        while i<len(lines) and not lines[i].startswith('ITEM: CELLS'):i+=1
        if i==len(lines):raise ValueError('Missing SPARTA grid header')
        i+=1;rows=[]
        while i<len(lines) and not lines[i].startswith('ITEM:'):
            rows.append([float(x) for x in lines[i].split()]);i+=1
        arr=np.array(rows);arr=arr[np.argsort(arr[:,1])]
        if arr.shape[1]!=13:raise ValueError('SPARTA dump field count')
        # id,x,n,u,v,w,usq,vsq,wsq,Pxx,Pxy,Pxz,qx
        n=arr[:,2];u=arr[:,3:6]
        raw=np.zeros((len(arr),10));raw[:,0]=n;raw[:,1:4]=n[:,None]*u
        raw[:,4:7]=n[:,None]*arr[:,6:9]
        raw[:,7]=arr[:,10]/MASS+n*u[:,0]*u[:,1]
        raw[:,8]=arr[:,11]/MASS+n*u[:,0]*u[:,2]
        cross=u[:,0]*raw[:,4]+u[:,1]*raw[:,7]+u[:,2]*raw[:,8]
        raw[:,9]=2*arr[:,12]/MASS+u[:,0]*np.sum(raw[:,4:7],axis=1)+2*cross-2*n*u[:,0]*np.sum(u*u,axis=1)
        frames.append(raw);times.append(step)
    if not frames:raise ValueError('No SPARTA profile frames')
    return np.stack(frames),np.array(times)


def main():
    p=argparse.ArgumentParser();p.add_argument('--execute',action='store_true');a=p.parse_args()
    protocol=json.loads((HERE/'reference-protocol.json').read_text())
    build=json.loads((HERE/'build.json').read_text())
    binary=Path(build['binary'])
    if hashlib.sha256(binary.read_bytes()).hexdigest()!=build['binary_sha256']:raise ValueError('Changed independent binary')
    jobs=[]
    for case in protocol['cases']:
        for label,config in case['configurations'].items():
            for seed in protocol['seeds']:
                folder=HERE/'runs'/case['id']/label/str(seed);folder.mkdir(parents=True,exist_ok=True)
                (folder/'input.sparta').write_text(make_input(case,config,seed))
                (folder/'hs.species').write_text('HS 8314.46261815324 1.380649e-23 0 0 0 0 0 1 0\n')
                diameter=np.sqrt(1/(np.sqrt(2)*np.pi))
                (folder/'hs.vss').write_text(f'HS {diameter:.17g} .5 1 1\n')
                jobs.append((case,label,seed,folder))
    if not a.execute:
        print(json.dumps({'status':'INPUTS_WRITTEN_UNEXECUTED','jobs':len(jobs)}));return
    review=HERE/'independent-pre-run-review.json'
    if not review.exists():raise ValueError('Missing root independent authorization/review')
    start=time.monotonic();rows=[]
    for case,label,seed,folder in jobs:
        remaining=protocol['combined_generation_timeout_seconds']-(time.monotonic()-start)
        if remaining<=0:raise TimeoutError('Frozen independent reference generation budget exhausted')
        with (folder/'stdout.log').open('w') as log:
            result=subprocess.run([str(binary),'-in','input.sparta'],cwd=folder,stdout=log,stderr=subprocess.STDOUT,timeout=remaining)
        if result.returncode:raise RuntimeError(f'Independent reference failed: {case["id"]}/{label}/{seed}')
        raw,steps=parse_dump(folder/'profiles.grid')
        # SPARTA may emit an initial unaveraged frame at the burn boundary.
        # The accepted frames have an exact predeclared physical-time table.
        burn=round(case['burn_in']/case['configurations'][label]['dt'])
        block=round(case['sample_time']/case['blocks']/case['configurations'][label]['dt'])
        raw=raw[steps>burn];steps=steps[steps>burn]
        if not np.array_equal(steps,burn+block*np.arange(1,case['blocks']+1)):
            raise ValueError('Independent reference actual-time table mismatch')
        if len(raw)!=case['blocks']:raise ValueError('Independent output block count')
        np.savez(folder/'raw.npz',raw_blocks=raw,steps=steps)
        rows.append({'case':case['id'],'configuration':label,'seed':seed,'elapsed':time.monotonic()-start})
        (HERE/'completed-runs.json').write_text(json.dumps(rows,indent=2)+'\n')
    print(json.dumps({'status':'GENERATED_PENDING_QUALIFICATION','jobs':len(jobs),'elapsed':time.monotonic()-start}))

if __name__=='__main__':main()
