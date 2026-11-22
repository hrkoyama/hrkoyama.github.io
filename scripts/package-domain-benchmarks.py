#!/usr/bin/env python3
"""Freeze a new model-benchmark edition; run independent extraction and recipes."""
import argparse
import datetime
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile

ROOT=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
dump=lambda p,d:p.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
p=argparse.ArgumentParser();p.add_argument('--edition',required=True);a=p.parse_args()
assert re.fullmatch(r'\d{4}-\d{2}-\d{2}(?:-r\d+)?',a.edition)
base=ROOT/'code/model-benchmarks'/a.edition
if base.exists():raise SystemExit('Edition already exists; use a new revision. No overwriting.')
base.parent.mkdir(parents=True,exist_ok=True)
shutil.copytree(ROOT/'scripts/domain-benchmarks',base,ignore=shutil.ignore_patterns('__pycache__','.pytest_cache','references'))
env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','MPLCONFIGDIR':tempfile.mkdtemp(prefix='atlas-domain-mpl-')}
subprocess.run([sys.executable,'reference_sir.py'],cwd=base,env=env,check=True)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
for path in sorted((base/'inputs').glob('*.json')):
    ident=path.stem;out=base/'results'/ident
    subprocess.run([sys.executable,'run.py','--input',str(path),'--output',str(out)],cwd=base,env=env,check=True,stdout=subprocess.DEVNULL)
    result=json.loads((out/'result.json').read_text())
    values=np.genfromtxt(out/'solution.csv',delimiter=',',names=True)
    fig,ax=plt.subplots(figsize=(9.6,5.7),layout='constrained')
    ax.set_title(ident.replace('-',' ').title()+' · fixed-input calculation')
    if ident in ['logistic-growth','sir-epidemic']:
        n=max(values['steps']);v=values[values['steps']==n]
        names=['population'] if ident=='logistic-growth' else ['S','I','R']
        for name in names:
            ax.plot(v['time'],v[name],label=name+' RK4')
            ref='analytic' if ident=='logistic-growth' else name+'_reference'
            ax.plot(v['time'][::4],v[ref][::4],'.',label=name+' reference')
        ax.set_xlabel('Time (dimensionless)');ax.set_ylabel('Population / fraction')
    elif ident=='mc-integral':
        ns=np.unique(values['samples']);rms=result['metrics']['rms_errors']
        ax.loglog(ns,rms,'o-',label='RMS over 256 independent seeds')
        ax.loglog(ns,np.sqrt((4/45)/ns),'--',label='Analytic sqrt(4 / (45 N))')
        ax.set_xlabel('Samples per seed');ax.set_ylabel('RMS integration error')
    else:
        ns=np.unique(values['steps']);error=result['metrics']['strong_rms_errors']
        ax.loglog(1/ns,error,'o-',label='Coupled-path strong RMS error')
        ax.loglog(1/ns,error[-1]*np.sqrt(ns[-1]/ns),'--',label='Slope 1/2 guide')
        ax.set_xlabel('Time step (dimensionless)');ax.set_ylabel('Endpoint RMS error')
    ax.grid(alpha=.25);ax.legend();fig.savefig(out/'preview.png',dpi=100);plt.close(fig)
files={path.relative_to(base).as_posix():sha(path) for path in sorted(base.rglob('*')) if path.is_file() and not any(x.startswith('.') or x=='__pycache__' for x in path.relative_to(base).parts)}
dump(base/'source-manifest.json',dict(schema_version=1,family='model-benchmarks',edition=a.edition,files=files,
     public_base_url='https://hrkoyama.github.io/code/model-benchmarks/'+a.edition+'/',
     scope='Four dimensionless educational fixed-input cases; no general biological or stochastic solver certification.'))
archive=base/('model-benchmarks-'+a.edition+'.zip');prefix='model-benchmarks-'+a.edition+'/'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for name in sorted([*files,'source-manifest.json']):
        info=zipfile.ZipInfo(prefix+name,date_time=(*map(int,a.edition[:10].split('-')),0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
        z.writestr(info,(base/name).read_bytes())
with tempfile.TemporaryDirectory(prefix='atlas-domain-extract-') as temp:
    temp=Path(temp)
    with zipfile.ZipFile(archive) as z:
        assert set(z.namelist())=={prefix+n for n in [*files,'source-manifest.json']}
        for name,digest in files.items():assert hashlib.sha256(z.read(prefix+name)).hexdigest()==digest
        z.extractall(temp)
    extracted=temp/prefix
    tests=subprocess.run([sys.executable,'-m','pytest','-q','--junitxml='+str(temp/'tests.xml')],cwd=extracted,env=env,check=True,capture_output=True,text=True)
    print(tests.stdout[-400:])
    suite=ET.parse(temp/'tests.xml').getroot().find('testsuite');counts={k:int(suite.attrib[k]) for k in ['tests','failures','errors','skipped']}
    reruns=[]
    for path in sorted((extracted/'inputs').glob('*.json')):
        out=temp/('rerun-'+path.stem)
        subprocess.run([sys.executable,'run.py','--input',str(path),'--output',str(out)],cwd=extracted,env=env,check=True,stdout=subprocess.DEVNULL)
        r=json.loads((out/'result.json').read_text());saved=json.loads((base/'results'/path.stem/'result.json').read_text())
        assert r['metrics']==saved['metrics'] and r['passed']
        reruns.append({'id':path.stem,'passed':True,'result_sha256':sha(out/'result.json'),'csv_sha256':sha(out/'solution.csv')})
    dump(base/'verification.json',dict(schema_version=1,edition=a.edition,verified_on=datetime.date.today().isoformat(),
         archive_sha256=sha(archive),source_manifest_sha256=sha(base/'source-manifest.json'),
         **counts,passed=counts['tests']-counts['failures']-counts['errors']-counts['skipped'],
         environment={x:importlib.metadata.version(x) for x in ['numpy','scipy','pytest','matplotlib']},
         execution='ZIP independently extracted; all packaged tests and all four fixed-input recipes executed without network or private source.',
         recipes=reruns,independent_reference='SIR uses separately coded SciPy DOP853; logistic/MC/GBM use analytic references.',
         scope='Fixed dimensionless logistic/SIR, IID x-squared integration and scalar Ito GBM only; stochastic thresholds apply to the published seeds/budgets.'))
print(json.dumps({'edition':a.edition,'archive_bytes':archive.stat().st_size,'passed':counts['tests'],'recipes':len(reruns)}))
