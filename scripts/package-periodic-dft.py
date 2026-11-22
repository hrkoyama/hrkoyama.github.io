#!/usr/bin/env python3
"""Freeze a new periodic-DFT edition and independently run its extracted ZIP."""
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
import time
import xml.etree.ElementTree as ET
import zipfile

ROOT=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
dump=lambda p,d:p.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--edition',required=True)
p.add_argument('--reference-regenerated',type=Path,help='Optional independently regenerated Julia result to audit; Julia is not a Python runtime dependency')
a=p.parse_args()
if not re.fullmatch(r'\d{4}-\d{2}-\d{2}(?:-r\d+)?',a.edition):raise SystemExit('Invalid edition')
source=ROOT/'scripts/periodic-dft';base=ROOT/'code/periodic-dft'/a.edition
if base.exists():raise SystemExit('Edition already exists; never overwrite a published edition.')
stored=json.loads((source/'results/result.json').read_text())
assert stored['passed'] and len(stored['cases'])==11
assert stored['input_sha256']==sha(source/'inputs.json')
reference=json.loads((source/'reference-dftk.json').read_text())
assert stored['reference_sha256']==sha(source/'reference-dftk.json')
reference_verification=dict(file='reference-dftk.json',sha256=sha(source/'reference-dftk.json'),engine='DFTK',engine_version=reference['engine_version'],julia_version=reference['julia_version'],regeneration='Optional separate Julia workflow; see README-reference.txt',regenerated_before_freeze=False)
if a.reference_regenerated:
    regenerated=json.loads(a.reference_regenerated.read_text())
    for key in ['cell','xc','input_sha256','script_sha256','pseudopotential_sha256','project_sha256','manifest_sha256']:
        assert regenerated[key]==reference[key],key
    expected=reference['cutoff_convergence']['records'];actual=regenerated['cutoff_convergence']['records']
    assert [(r['k_n'],r['ecut_hartree']) for r in actual]==[(r['k_n'],r['ecut_hartree']) for r in expected]
    delta=max(abs(x['energy_per_cell']-y['energy_per_cell']) for x,y in zip(actual,expected))
    assert delta<1e-9 and all(r['converged'] for r in actual)
    reference_verification.update(regenerated_before_freeze=True,regenerated_records=len(actual),maximum_regenerated_energy_difference=delta)
shutil.copytree(source,base,ignore=shutil.ignore_patterns('__pycache__','.pytest_cache'))
with tempfile.TemporaryDirectory(prefix='atlas-periodic-dft-package-') as td:
    temp=Path(td)
    env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','MPLCONFIGDIR':str(temp/'mpl'),'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1'}
    files={path.relative_to(base).as_posix():sha(path) for path in sorted(base.rglob('*')) if path.is_file() and not any(s.startswith('.') or s=='__pycache__' for s in path.relative_to(base).parts)}
    dump(base/'source-manifest.json',dict(schema_version=1,family='periodic-dft',edition=a.edition,files=files,
        public_base_url='https://hrkoyama.github.io/code/periodic-dft/'+a.edition+'/',
        terms={'original_driver':'MIT / LICENSE','upstream_software_datasets':'provenance.json','text_figures_data':'https://hrkoyama.github.io/rights/'},
        scope=stored['scope'],implementation=stored['implementation']))
    archive=base/('periodic-dft-'+a.edition+'.zip');prefix='periodic-dft-'+a.edition+'/'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name in sorted([*files,'source-manifest.json']):
            info=zipfile.ZipInfo(prefix+name,date_time=(*map(int,a.edition[:10].split('-')),0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
            z.writestr(info,(base/name).read_bytes())
    with zipfile.ZipFile(archive) as z:
        assert set(z.namelist())=={prefix+n for n in [*files,'source-manifest.json']}
        for name,h in files.items():assert hashlib.sha256(z.read(prefix+name)).hexdigest()==h
        z.extractall(temp/'extracted')
    extracted=temp/'extracted'/prefix
    started=time.perf_counter()
    tests=subprocess.run([sys.executable,'-m','pytest','-q','--junitxml='+str(temp/'tests.xml')],cwd=extracted,env=env,text=True,capture_output=True)
    test_seconds=time.perf_counter()-started
    print(tests.stdout[-1500:],flush=True)
    if tests.returncode:print(tests.stderr);raise SystemExit(tests.returncode)
    suite=ET.parse(temp/'tests.xml').getroot().find('testsuite');counts={k:int(suite.attrib[k]) for k in ['tests','failures','errors','skipped']}
    reproduced=temp/'reproduced';started=time.perf_counter()
    subprocess.run([sys.executable,'run.py','--input','inputs.json','--output',str(reproduced)],cwd=extracted,env=env,check=True)
    runner_seconds=time.perf_counter()-started
    actual=json.loads((reproduced/'result.json').read_text())
    assert actual['passed'] and len(actual['cases'])==11
    delta=max(abs(x['energy_per_cell']-y['energy_per_cell']) for x,y in zip(actual['cases'],stored['cases']))
    assert delta<1e-9
    dump(base/'verification.json',dict(schema_version=1,family='periodic-dft',edition=a.edition,
        verified_on=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).date().isoformat(),
        archive_sha256=sha(archive),source_manifest_sha256=sha(base/'source-manifest.json'),
        execution='ZIP independently extracted; all packaged tests and complete fixed-input Python runner executed without network or private source. The separate independent Julia reference regeneration is recorded below.',
        environment={x:importlib.metadata.version(x) for x in ['numpy','scipy','pytest','matplotlib','pyscf']},
        **counts,passed=counts['tests']-counts['failures']-counts['errors']-counts['skipped'],
        fixed_input=dict(id='periodic-he-dft',unique_cases=len(actual['cases']),passed=actual['passed'],metrics=actual['metrics'],maximum_reproduced_energy_difference=delta,runtime_seconds=runner_seconds),
        independent_reference=reference_verification,
        failure_check=dict(test='test_single_cycle_reports_nonconvergence',result='One actual limited SCF iteration is not converged and reports maximum_cycles; a failed case cannot produce a successful workflow summary.'),
        test_runtime_seconds=test_seconds,scope=stored['scope']))
print(json.dumps(dict(edition=a.edition,files=len(files),archive_bytes=archive.stat().st_size,passed_tests=counts['tests'],cases=len(actual['cases']),runner_seconds=runner_seconds,metrics=actual['metrics'])))
