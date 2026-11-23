#!/usr/bin/env python3
"""Freeze small validation supplements after a real independent ZIP extraction."""
import argparse,hashlib,importlib.metadata,json,os,re,shutil,subprocess,sys,tempfile,time,xml.etree.ElementTree as ET,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
GROUPS=['foundations','models','particles','mhd','thermostats','biology','mcmc','mhd-convergence','foundations-conditioning','particle-transport', 'splitting', 'noh', 'noh-cartesian', 'sedov', 'double-mach']

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def package(group,edition):
    assert group in GROUPS
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}(?:-r\d+)?',edition):raise ValueError('Use YYYY-MM-DD[-rN]')
    target=ROOT/'code/validated-examples'/edition/group
    if target.exists():raise ValueError('Immutable edition exists; choose a new revision')
    source=ROOT/'scripts'/('depth-'+group);prefix='atlas-'+group+'-'+edition
    required=['run.py','inputs.json','cases.json','requirements.txt','README.md','LICENSE']
    assert all((source/p).is_file() for p in required)
    metadata=json.loads((source/'cases.json').read_text());metadata=metadata['cases'] if isinstance(metadata,dict) else metadata
    ids={c['id'] for c in metadata};assert len(ids)==len(metadata) and ids
    assert all(re.fullmatch(r'[a-z][a-z0-9-]+',i) for i in ids)
    with tempfile.TemporaryDirectory(prefix='atlas-validation-') as tmp:
        tmp=Path(tmp);stage=tmp/prefix;stage.mkdir()
        for p in source.rglob('*'):
            rel=p.relative_to(source)
            if not p.is_file() or any(x in rel.parts for x in ['__pycache__','.pytest_cache']) or rel.parts[0] in ['results','output','outputs']:continue
            if p.name!='LICENSE' and not p.name.startswith('athinput-') and p.suffix not in ['.py','.json','.md','.txt','.npz','.patch','.csv','.log','.xml']:raise ValueError('Unexpected source file '+str(rel))
            (stage/rel).parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,stage/rel)
        env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1','MPLBACKEND':'Agg','MPLCONFIGDIR':str(tmp/'mpl')}
        def execute(cwd,out):
            start=time.monotonic();p=subprocess.run([sys.executable,'-W','error','run.py','--input','inputs.json','--output',str(out)],cwd=cwd,env=env,text=True,capture_output=True,timeout=120)
            if p.returncode:raise RuntimeError(p.stdout+'\n'+p.stderr)
            result=json.loads((out/'result.json').read_text());assert result['passed'] is True and result['checks'] and all(result['checks'].values())
            assert {c['id'] for c in result['cases']}==ids
            assert all(c['passed'] and c['checks'] and all(c['checks'].values()) for c in result['cases'])
            return result,time.monotonic()-start
        original,first_seconds=execute(stage,stage/'results')
        if (stage/'plot.py').is_file():
            plot=subprocess.run([sys.executable,'plot.py','--results','results/result.json','--output','results'],cwd=stage,env=env,capture_output=True,text=True,timeout=60)
            if plot.returncode:raise RuntimeError(plot.stdout+'\n'+plot.stderr)
            assert all((stage/'results'/(i+'.png')).is_file() for i in ids)
        files={p.relative_to(stage).as_posix():sha(p) for p in sorted(stage.rglob('*')) if p.is_file()}
        manifest={'schema_version':1,'family':'depth-'+group,'group':group,'version':edition,'public_base_url':'https://hrkoyama.github.io/code/validated-examples/'+edition+'/'+group+'/','files':files,'case_ids':sorted(ids),'scope':'Small fixed-input educational validations; each case states its own model, reference, acceptance and exclusions.'}
        dump(stage/'source-manifest.json',manifest)
        archive=stage/(prefix+'.zip')
        with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
            for name in sorted([*files,'source-manifest.json']):
                info=zipfile.ZipInfo(prefix+'/'+name,(*map(int,edition[:10].split('-')),0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16;z.writestr(info,(stage/name).read_bytes())
        with zipfile.ZipFile(archive) as z:
            assert set(z.namelist())=={prefix+'/'+p for p in [*files,'source-manifest.json']}
            for name,digest in files.items():assert hashlib.sha256(z.read(prefix+'/'+name)).hexdigest()==digest
            z.extractall(tmp/'independent')
        extracted=tmp/'independent'/prefix
        test=subprocess.run([sys.executable,'-W','error','-m','pytest','-q','-p','no:cacheprovider','--junitxml='+str(tmp/'tests.xml')],cwd=extracted,env=env,text=True,capture_output=True,timeout=120)
        if test.returncode:raise RuntimeError(test.stdout+'\n'+test.stderr)
        suite=ET.parse(tmp/'tests.xml').getroot().find('testsuite');counts={k:int(suite.attrib[k]) for k in ['tests','failures','errors','skipped']};assert counts['tests']>0 and not any(counts[k] for k in ['failures','errors','skipped'])
        rerun,second_seconds=execute(extracted,tmp/'rerun')
        assert [c['checks'] for c in original['cases']]==[c['checks'] for c in rerun['cases']]
        verification={'schema_version':1,'group':group,'edition':edition,'verified_on':edition[:10],'source_manifest_sha256':sha(stage/'source-manifest.json'),'archive':{'file':archive.name,'sha256':sha(archive),'bytes':archive.stat().st_size,'archive_directory':prefix},'archive_sha256':sha(archive),'returncode':0,'passed_tests':counts['tests'],**counts,'passed':True,'case_ids':sorted(ids),'all_cases_rerun':True,'first_run_seconds':first_seconds,'independent_rerun_seconds':second_seconds,'environment':{k:importlib.metadata.version(k) for k in ['numpy','scipy','pytest']},'execution':'ZIP independently extracted; meaningful pytest checks and every fixed input actually rerun. Scientific code needs no private checkout or network. Stored independent reference regeneration is a separate operation.'}
        dump(stage/'verification.json',verification);target.parent.mkdir(parents=True,exist_ok=True);shutil.copytree(stage,target)
        print(json.dumps({'group':group,'edition':edition,'tests':counts['tests'],'cases':len(ids),'seconds':second_seconds,'archive_sha256':sha(archive)},ensure_ascii=False),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--group',choices=GROUPS,required=True);p.add_argument('--edition',required=True);a=p.parse_args();package(a.group,a.edition)
