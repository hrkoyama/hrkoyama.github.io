#!/usr/bin/env python3
"""Explicit separate regeneration of pinned official Athena++ reference fields."""
import argparse,datetime,json,os,re,shutil,subprocess,time
from pathlib import Path
import numpy as np
from qualify import qualify,sha
ROOT=Path(__file__).resolve().parent


def save(p,d):Path(p).write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')


def parse(path,nx,ny):
    lines=path.read_text().splitlines();m=re.search(r'time=([-+0-9.eE]+)',lines[0]);assert m
    labels=lines[1].lstrip('# ').split();table=np.loadtxt(path);columns={name:i for i,name in enumerate(labels)}
    names=['dens','mom1','mom2','mom3','Etot','Bcc1','Bcc2','Bcc3']
    assert len(table)==nx*ny and all(name in columns for name in names),(labels,table.shape)
    order=np.lexsort((table[:,columns['j']],table[:,columns['i']]))
    return float(m[1]),table[order][:,[columns[name] for name in names]].reshape(nx,ny,8)


def output_text(value):
    if isinstance(value,bytes):return value.decode('utf-8',errors='replace')
    return value or ''


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--binary-loop',type=Path,required=True);p.add_argument('--binary-ot',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    contract=json.loads((ROOT/'reference-contract.json').read_text());plan=json.loads((ROOT/'reference-input-plan.json').read_text())
    for name,digest in contract['files_sha256'].items():
        if sha(ROOT/name)!=digest:raise ValueError('Changed frozen reference plan/source '+name)
    for kind,binary in [('loop',a.binary_loop),('ot',a.binary_ot)]:
        if sha(binary)!=contract['binary_sha256'][kind]:raise ValueError('Changed official binary '+kind)
    if a.output.exists():raise ValueError('Use fresh reference output path')
    a.output.mkdir(parents=True);start=time.monotonic();rows=[];failure=None;active=None;work=None
    env={**os.environ,'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'}
    try:
        for row in plan['runs']:
            work=a.output/row['id'];work.mkdir();shutil.copyfile(ROOT/row['input'],work/'athinput')
            command=[str((a.binary_loop if row['kind']=='loop' else a.binary_ot).resolve()),'-i','athinput']
            active={**row,'command':command,'input_sha256':sha(ROOT/row['input']),'binary_sha256':sha(a.binary_loop if row['kind']=='loop' else a.binary_ot),'completed':False}
            before=time.monotonic()
            try:
                proc=subprocess.run(command,cwd=work,env=env,text=True,capture_output=True,timeout=max(.1,plan['reference_batch_budget_seconds']-(before-start)))
            except subprocess.TimeoutExpired as error:
                (work/'stdout.log').write_text(output_text(error.stdout));(work/'stderr.log').write_text(output_text(error.stderr))
                active.update(termination='timeout',seconds=time.monotonic()-before,returncode=None)
                raise
            (work/'stdout.log').write_text(proc.stdout);(work/'stderr.log').write_text(proc.stderr)
            active.update(returncode=proc.returncode,seconds=time.monotonic()-before)
            if proc.returncode:raise RuntimeError(row['id']+' exited '+str(proc.returncode))
            parsed={};raw={}
            for path in sorted(work.glob('*.tab')):
                t,q=parse(path,row['nx'],row['n']);parsed[t]=q;raw[path.name]=sha(path)
            times=np.array(sorted(parsed));q=np.array([parsed[t] for t in times])
            dx=(2. if row['kind']=='loop' else 1.)/row['nx'];dy=1/row['n']
            div=(np.roll(q[...,5],-1,axis=1)-np.roll(q[...,5],1,axis=1))/(2*dx)+(np.roll(q[...,6],-1,axis=2)-np.roll(q[...,6],1,axis=2))/(2*dy)
            common_divergence=np.max(abs(div),axis=(1,2))
            name=row['id']+'.npz';np.savez_compressed(a.output/name,q_history=q,times=times,common_cell_divergence_history=common_divergence)
            rows.append({**active,'completed':True,'file':name,'sha256':sha(a.output/name),'seconds':time.monotonic()-before,'raw_table_sha256':raw,'common_cell_divergence_history':common_divergence.tolist(),'native_face_divergence_measured':False})
            active=None
            print(json.dumps({'completed':row['id'],'seconds':rows[-1]['seconds']}),flush=True)
    except Exception as error:
        if active is not None and work is not None:
            active['partial_table_inventory']=[{'file':f.name,'bytes':f.stat().st_size,'sha256':sha(f)} for f in sorted(work.glob('*.tab'))]
            active['log_sha256']={f.name:sha(f) for f in work.glob('*.log')}
            save(work/'failed-run-context.json',active)
        failure={'type':type(error).__name__,'message':str(error),'failed_run':active}
    qualification=qualify(a.output,rows,plan) if len(rows)==6 else {'passed':False,'checks':[]}
    result={'schema_version':1,'actually_executed':True,'passed':failure is None and qualification['passed'],'created_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reference_contract_sha256':sha(ROOT/'reference-contract.json'),'source_commit':plan['source_version'],'source_archive_sha256':plan['source_archive_sha256'],'records':rows,'qualification':qualification,'failure':failure,'duration_seconds':time.monotonic()-start,'divergence_scope':'Only Bcc is exported: report the same centered common-cell divergence used for primary cell fields. No Athena native-face divergence measurement or zero-native-divergence claim.'}
    save(a.output/'reference-qualification.json',result);print(json.dumps({'passed':result['passed'],'checks':len(qualification['checks']),'failed':[x for x in qualification['checks'] if not x['passed']],'failure':failure}),flush=True)
    return 0 if result['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
