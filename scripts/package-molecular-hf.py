#!/usr/bin/env python3
"""Freeze one new immutable molecular-HF edition and independently verify its ZIP."""
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
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--edition',required=True);a=p.parse_args()
assert re.fullmatch(r'\d{4}-\d{2}-\d{2}(?:-r\d+)?',a.edition)
base=ROOT/'code/molecular-hf'/a.edition
if base.exists():raise SystemExit('Edition already exists; choose a new revision, never overwrite a published edition.')
shutil.copytree(ROOT/'scripts/h2-hf',base,ignore=shutil.ignore_patterns('__pycache__','.pytest_cache'))
with tempfile.TemporaryDirectory(prefix='atlas-molecular-hf-package-') as td:
    temp=Path(td);env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','MPLCONFIGDIR':str(temp/'mpl'),'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1'}
    # Truly regenerate the independent reference without sharing educational code.
    regenerated=temp/'reference-regenerated.json'
    subprocess.run([sys.executable,'reference_pyscf.py','--input','inputs.json','--output',str(regenerated)],cwd=base,env=env,check=True)
    fresh=json.loads(regenerated.read_text());saved=json.loads((base/'reference-pyscf.json').read_text())
    assert fresh['input_sha256']==saved['input_sha256']
    reference_delta=max(abs(x['energy_total']-y['energy_total']) for x,y in zip(fresh['cases'],saved['cases']))
    assert reference_delta<1e-10
    subprocess.run([sys.executable,'run.py','--input','inputs.json','--output','results'],cwd=base,env=env,check=True)
    subprocess.run([sys.executable,'plot_results.py','--input','results/result.json','--output','results'],cwd=base,env=env,check=True)
    files={path.relative_to(base).as_posix():sha(path) for path in sorted(base.rglob('*')) if path.is_file() and not any(s.startswith('.') or s=='__pycache__' for s in path.relative_to(base).parts)}
    dump(base/'source-manifest.json',dict(schema_version=1,family='molecular-hf',edition=a.edition,files=files,
         public_base_url='https://hrkoyama.github.io/code/molecular-hf/'+a.edition+'/',
         terms={'original_python':'MIT / LICENSE','text_figures_data':'https://hrkoyama.github.io/rights/'},
         scope='Only isolated clamped-nuclei two-electron H2 RHF with real s Gaussian contractions; finite prescribed nested s-space stabilization, not complete-basis convergence or correlated dissociation.'))
    archive=base/('molecular-hf-'+a.edition+'.zip');prefix='molecular-hf-'+a.edition+'/'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name in sorted([*files,'source-manifest.json']):
            info=zipfile.ZipInfo(prefix+name,date_time=(*map(int,a.edition[:10].split('-')),0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
            z.writestr(info,(base/name).read_bytes())
    with zipfile.ZipFile(archive) as z:
        assert set(z.namelist())=={prefix+n for n in [*files,'source-manifest.json']}
        for name,h in files.items():assert hashlib.sha256(z.read(prefix+name)).hexdigest()==h
        z.extractall(temp/'extracted')
    extracted=temp/'extracted'/prefix
    tests=subprocess.run([sys.executable,'-m','pytest','-q','--junitxml='+str(temp/'tests.xml')],cwd=extracted,env=env,text=True,capture_output=True)
    print(tests.stdout[-700:])
    if tests.returncode:print(tests.stderr);raise SystemExit(tests.returncode)
    suite=ET.parse(temp/'tests.xml').getroot().find('testsuite');counts={k:int(suite.attrib[k]) for k in ['tests','failures','errors','skipped']}
    reproduced=temp/'reproduced'
    subprocess.run([sys.executable,'run.py','--input','inputs.json','--output',str(reproduced)],cwd=extracted,env=env,check=True)
    actual=json.loads((reproduced/'result.json').read_text());stored=json.loads((base/'results/result.json').read_text())
    delta=max(abs(x['energy_total']-y['energy_total']) for x,y in zip(actual['cases'],stored['cases']))
    assert delta<1e-10 and actual['passed']
    failure=temp/'failure';failed=subprocess.run([sys.executable,'run.py','--input','inputs.json','--output',str(failure),'--max-cycles','1'],cwd=extracted,env=env,capture_output=True,text=True)
    failure_report=json.loads((failure/'result.json').read_text());assert failed.returncode==1 and not failure_report['passed'] and failure_report['termination']=='scf_not_converged'
    dump(base/'verification.json',dict(schema_version=1,family='molecular-hf',edition=a.edition,
         verified_on=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).date().isoformat(),
         archive_sha256=sha(archive),source_manifest_sha256=sha(base/'source-manifest.json'),
         execution='ZIP independently extracted; all packaged tests and the complete fixed-input runner executed without network or private source. Optional independent PySCF reference was also regenerated before packaging.',
         environment={x:importlib.metadata.version(x) for x in ['numpy','scipy','pytest','matplotlib','pyscf']},
         **counts,passed=counts['tests']-counts['failures']-counts['errors']-counts['skipped'],
         fixed_input=dict(id='h2-rhf',geometries=len({r['bond_bohr'] for r in actual['cases']}),geometry_basis_cases=len(actual['cases']),scf_tolerance_cases=len(actual['tolerance_sweep']),passed=actual['passed'],metrics=actual['metrics'],maximum_reproduced_energy_difference=delta),
         independent_reference=dict(file='reference-pyscf.json',sha256=sha(base/'reference-pyscf.json'),environment=fresh['environment'],maximum_regenerated_energy_difference=reference_delta),
         failure_check=dict(command='python run.py --input inputs.json --output failed --max-cycles 1',exit_code=failed.returncode,termination=failure_report['termination'],passed_is_false=not failure_report['passed']),
         scope=stored['scope']))
print(json.dumps({'edition':a.edition,'files':len(files),'archive_bytes':archive.stat().st_size,'passed_tests':counts['tests'],'cases':len(actual['cases']),'metrics':actual['metrics']}))
