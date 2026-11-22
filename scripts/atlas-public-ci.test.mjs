import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';

const root = new URL('../', import.meta.url);
const read = path => readFileSync(new URL(path, root), 'utf8');
const hash = path => createHash('sha256').update(readFileSync(new URL(path, root))).digest('hex');
const pythonPrelude = String.raw`
import copy, hashlib, importlib.util, io, json, os, pathlib, subprocess, sys, tempfile, urllib.error
from unittest import mock
ROOT=pathlib.Path.cwd()
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);value=importlib.util.module_from_spec(spec);spec.loader.exec_module(value);return value
v=module('ci_verifier',ROOT/'scripts/verify-atlas-execution-examples.py')
b=v.registry_module
`;
function python(source) {
  return execFileSync('python3', ['-B', '-c', pythonPrelude + source], {cwd: root, encoding: 'utf8', timeout: 30_000});
}

test('the Linux public-artifact job has matching immutable pins, no checkout, bounded privileges and retained failure artifacts', () => {
  const workflow = read('.github/workflows/atlas-public-linux.yml');
  const pins = {
    ATLAS_BOOTSTRAP_SHA256: 'scripts/run-atlas-public-ci.py',
    ATLAS_VERIFIER_SHA256: 'scripts/verify-atlas-execution-examples.py',
    ATLAS_BUILDER_SHA256: 'scripts/build-atlas-execution-examples.py',
    ATLAS_REGISTRY_SHA256: 'numerical-methods-atlas/code-and-data/examples.json'
  };
  for (const [name, path] of Object.entries(pins)) {
    const match = workflow.match(new RegExp(`^\\s*${name}:\\s*["']?([a-f0-9]{64})`, 'm'));
    assert.ok(match, name); assert.equal(match[1], hash(path), name);
  }
  assert.doesNotMatch(workflow, /uses:\s*actions\/checkout/);
  assert.match(workflow, /contents:\s*read/);
  assert.doesNotMatch(workflow, /(?:contents|actions|packages|id-token):\s*write/);
  assert.match(workflow, /workflow_dispatch/); assert.match(workflow, /cron:/);
  assert.match(workflow, /workflow_run:/); assert.match(workflow, /conclusion\s*==\s*['"]success['"]/);
  assert.match(workflow, /actions\/upload-artifact@/);
  assert.match(workflow, /if:\s*(?:\$\{\{\s*)?always\(\)/);
  assert.match(workflow, /retention-days:\s*90/);
  assert.doesNotMatch(workflow, /\$\{\{\s*secrets\./);
});

test('the embedded publication wait saves a bootstrap only after all four public hashes match and fails without saving it on timeout', () => {
  python(String.raw`
import re, textwrap, time
workflow=(ROOT/'.github/workflows/atlas-public-linux.yml').read_text()
blocks=re.findall(r"^\s*python - <<'PY'\n(.*?)^\s*PY\s*$",workflow,re.MULTILINE|re.DOTALL)
assert len(blocks)==1,'Exercise the actual download block, not a duplicate implementation'
block=compile(textwrap.dedent(blocks[0]),'workflow-publication-wait','exec')
sources=[('scripts/run-atlas-public-ci.py','ATLAS_BOOTSTRAP_SHA256'),
         ('scripts/verify-atlas-execution-examples.py','ATLAS_VERIFIER_SHA256'),
         ('scripts/build-atlas-execution-examples.py','ATLAS_BUILDER_SHA256'),
         ('numerical-methods-atlas/code-and-data/examples.json','ATLAS_REGISTRY_SHA256')]
payloads={path:(ROOT/path).read_bytes() for path,key in sources}
class Response(io.BytesIO):pass
for scenario in ['matched','delayed-fourth','timeout']:
 with tempfile.TemporaryDirectory() as tmp:
  directory=pathlib.Path(tmp);report=directory/'report';report.mkdir();clock=[0.];calls=[];sleeps=[]
  saved=directory/'atlas-public-bootstrap.py';receipt=report/'publication-checks.json'
  environment={key:hashlib.sha256(payloads[path]).hexdigest() for path,key in sources}
  environment.update(REPORT_DIR=str(report),RUNNER_TEMP=str(directory))
  def open_public(request,**kwargs):
   assert not saved.exists() and not receipt.exists(),'Never publish a partial acquisition'
   assert kwargs['timeout']>0
   path=request.full_url.removeprefix('https://hrkoyama.github.io/')
   assert path in payloads,'Only the four expected public files may be requested'
   calls.append(path);payload=payloads[path]
   if path==sources[-1][0] and (scenario=='timeout' or (scenario=='delayed-fourth' and not sleeps)):
    payload=b'previous public version'
   return Response(payload)
  def sleep(seconds):
   assert not saved.exists() and not receipt.exists(),'A retry must not leave an executable bootstrap'
   assert seconds>0;sleeps.append(seconds);clock[0]+=seconds
  opener=mock.Mock();opener.open.side_effect=open_public
  with mock.patch.dict(os.environ,environment,clear=True),mock.patch.object(urllib.request,'build_opener',return_value=opener),mock.patch.object(time,'monotonic',side_effect=lambda:clock[0]),mock.patch.object(time,'sleep',side_effect=sleep):
   try:exec(block,{})
   except RuntimeError as error:
    assert scenario=='timeout',str(error)
    assert 'expected versions' in str(error)
   else:assert scenario!='timeout','Mismatched public files must not time out successfully'
  assert calls[:4]==[path for path,key in sources]
  if scenario=='timeout':
   assert clock[0]>=240 and sleeps
   assert not saved.exists() and not receipt.exists()
  else:
   assert saved.read_bytes()==payloads[sources[0][0]]
   records=json.loads(receipt.read_text());assert len(records)==4
   assert [(row['url'],row['sha256']) for row in records]==[('https://hrkoyama.github.io/'+path,environment[key]) for path,key in sources]
   if scenario=='matched':assert not sleeps and len(calls)==4
   else:assert sleeps and len(calls)==8
`);
});

test('nonfinite or boolean numerical output cannot create a successful or unserializable failure receipt', () => {
  python(String.raw`
example=json.loads((ROOT/'catalog/atlas-execution-examples.json').read_text())['examples'][0]
for invalid in ['NaN','Infinity','-Infinity','true']:
 with tempfile.TemporaryDirectory() as tmp:
  out=pathlib.Path(tmp)
  # The numeric force-error field deliberately contains an invalid value.
  doc='{"particles":192,"relative_rms_force_error":'+invalid+',"fully_opened_max_absolute_error":0,"checks":{"a":true},"input_sha256":"'+example['inputs']['sha256']+'"}'
  (out/'result.json').write_text(doc);(out/'forces.csv').write_text('x,y'+chr(10)+'0,0'+chr(10))
  result=v.check_case(example,out)
  assert result['passed'] is False,invalid
  numeric=next((row for row in result.get('checks',[]) if row['id']=='relative-force-error'),None)
  assert numeric is None or numeric['passed'] is False
  json.dumps(result,allow_nan=False)
for invalid in ['nan','inf','-inf','true']:
 with tempfile.TemporaryDirectory() as tmp:
  out=pathlib.Path(tmp)
  (out/'result.json').write_bytes((ROOT/b.public_path(next(a['url'] for a in example['outputs'] if a['id']=='results'))).read_bytes())
  (out/'forces.csv').write_text('x,y'+chr(10)+invalid+',0'+chr(10))
  result=v.check_case(example,out)
  assert result['passed'] is False,invalid
  assert next(row for row in result['checks'] if row['id']=='output-forces')['passed'] is False
  json.dumps(result,allow_nan=False)
`);
});

test('runner failure and timeout preserve diagnostics and outputs, do not pass on valid partial results, and allow the next group to run', () => {
  python(String.raw`
source=json.loads((ROOT/'catalog/atlas-execution-examples.json').read_text())
selected=[copy.deepcopy(source['examples'][0]),copy.deepcopy(source['examples'][3])]
registry={**source,'examples':selected}
def download(url,expected=None,**kwargs):
 payload=(ROOT/b.public_path(url)).read_bytes()
 if expected is not None:assert b.digest(payload)==expected
 return payload
for failure in ['nonzero','timeout']:
 with tempfile.TemporaryDirectory() as tmp:
  artifacts=pathlib.Path(tmp)/'artifacts';calls=[]
  def run(argv,**kwargs):
   env=kwargs.get('env');assert isinstance(env,dict),'Never inherit an unspecified subprocess environment'
   for key in ['GITHUB_TOKEN','AWS_SECRET_ACCESS_KEY','ATLAS_TEST_SECRET']:
    assert key not in env,key
   if '-c' in argv:
    return subprocess.CompletedProcess(argv,0,stdout=json.dumps({'python':'3.12.0','numpy':'2.0.2','scipy':'1.14.1','matplotlib':'3.9.4'}),stderr='')
   calls.append(argv)
   case=selected[1] if any(pathlib.Path(str(arg)).name=='run_recipe.py' for arg in argv) else selected[0]
   output=pathlib.Path(argv[argv.index('--output')+1]);output.mkdir(parents=True,exist_ok=True)
   for asset in case['outputs']:
    path=output/asset['generated_path'];path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes((ROOT/b.public_path(asset['url'])).read_bytes())
   if case['id']==selected[0]['id']:
    if failure=='timeout':raise subprocess.TimeoutExpired(argv,1,output=b'timeout-partial-stdout',stderr=b'timeout-partial-stderr')
    return subprocess.CompletedProcess(argv,7,stdout='failed-runner-stdout',stderr='failed-runner-stderr')
   return subprocess.CompletedProcess(argv,0,stdout='next-group-stdout',stderr='next-group-stderr')
  with mock.patch.dict(os.environ,{'GITHUB_TOKEN':'never-forward-token','AWS_SECRET_ACCESS_KEY':'never-forward-aws','ATLAS_TEST_SECRET':'never-forward-custom'}),mock.patch.object(v,'checked_download',side_effect=download),mock.patch.object(v.subprocess,'run',side_effect=run),mock.patch.object(v.urllib.request,'urlopen',side_effect=AssertionError('network forbidden in unit tests')):
   environment,releases,results=v.run_registry(registry,sys.executable,timeout=1,artifacts_dir=artifacts)
  assert len(calls)==2 and len(results)==2
  assert results[0]['passed'] is False
  assert results[0]['execution']['completed'] is False
  assert results[0]['execution']['timed_out'] is (failure=='timeout')
  assert results[1]['passed'] is True
  files=[path for path in artifacts.rglob('*') if path.is_file()]
  logs='\n'.join(path.read_text(errors='replace') for path in files)
  for marker in (['timeout-partial-stdout','timeout-partial-stderr'] if failure=='timeout' else ['failed-runner-stdout','failed-runner-stderr']):assert marker in logs,marker
  assert 'next-group-stdout' in logs and 'next-group-stderr' in logs
  assert any(path.suffix=='.csv' for path in files),'Retain generated numerical tables'
  assert any(path.name in ['result.json','results.json'] for path in files),'Retain generated result JSON'
  json.dumps({'environment':environment,'releases':releases,'examples':results},allow_nan=False)
`);
});

test('canonical download handlers reject off-site, downgraded and out-of-scope redirects before following them', () => {
  python(String.raw`
c=module('public_ci_bootstrap',ROOT/'scripts/run-atlas-public-ci.py')
source='https://hrkoyama.github.io/code/example/input.json'
for host in [v,c]:
 handler=host.PublicRedirectHandler()
 request=host.urllib.request.Request(source)
 for target in ['http://hrkoyama.github.io/code/example/input.json','https://other.example/code/input.json','https://hrkoyama.github.io/rights/','https://hrkoyama.github.io/code/../rights/input.json']:
  try:handler.redirect_request(request,None,302,'Found',{},target)
  except (ValueError,urllib.error.URLError):pass
  else:raise AssertionError('Unsafe redirect accepted: '+target)
 allowed=handler.redirect_request(request,None,302,'Found',{},'https://hrkoyama.github.io/code/example/renamed.json')
 assert allowed.full_url=='https://hrkoyama.github.io/code/example/renamed.json'
`);
});

test('both bootstrap and verifier reject mismatched download hashes and unsafe final URLs', () => {
  python(String.raw`
c=module('public_ci_bootstrap',ROOT/'scripts/run-atlas-public-ci.py')
class Response(io.BytesIO):
 def __init__(self,payload,url):super().__init__(payload);self.url=url;self.read_called=False
 def geturl(self):return self.url
 def read(self,*args):self.read_called=True;return super().read(*args)
for host,download in [(v,v.checked_download),(c,c.download)]:
 response=Response(b'changed','https://hrkoyama.github.io/code/example/input.json')
 with mock.patch.object(host.PUBLIC_OPENER,'open',return_value=response):
  try:download('https://hrkoyama.github.io/code/example/input.json','0'*64)
  except ValueError:pass
  else:raise AssertionError('Wrong digest accepted')
 response=Response(b'changed','https://other.example/private')
 with mock.patch.object(host.PUBLIC_OPENER,'open',return_value=response):
  try:download('https://hrkoyama.github.io/code/example/input.json')
  except (ValueError,urllib.error.URLError):pass
  else:raise AssertionError('Unsafe final URL accepted')
 assert not response.read_called,'Reject the final origin before reading its body'
`);
});

test('core dependencies accept only the five published fixed pins and never executable requirement options or URLs', () => {
  python(String.raw`
c=module('public_ci_bootstrap',ROOT/'scripts/run-atlas-public-ci.py')
expected={'numpy':'2.0.2','scipy':'1.14.1','matplotlib':'3.9.4','pytest':'8.3.5','pyscf':'2.11.0'}
assert c.REQUIRED_PINS==expected
text=chr(10).join(name+'=='+version for name,version in expected.items())+chr(10)
assert c.parse_requirements(text)==expected
for bad in ['numpy>=2','numpy==2.1.0','unreviewed-package==1.0','numpy @ https://other.example/a.whl','-r requirements.txt','--extra-index-url https://other.example','-e .','numpy==2.0.2 --index-url https://other.example','git+https://other.example/repo']:
 try:c.parse_requirements(bad)
 except (ValueError,RuntimeError):pass
 else:raise AssertionError('Unfixed or executable requirement accepted: '+bad)
registry=json.loads((ROOT/'numerical-methods-atlas/code-and-data/examples.json').read_text())
class Response(io.BytesIO):
 def __init__(self,payload,url):super().__init__(payload);self.url=url
 def geturl(self):return self.url
for tamper in [False,True]:
 acquisitions=[]
 def open_public(request,**kwargs):
  payload=(ROOT/b.public_path(request.full_url)).read_bytes()
  if tamper and request.full_url.endswith('/requirements.txt'):payload+=b'\n# changed bytes\n'
  return Response(payload,request.full_url)
 with tempfile.TemporaryDirectory() as tmp,mock.patch.object(c.PUBLIC_OPENER,'open',side_effect=open_public):
  try:actual=c.collect_requirements(registry,pathlib.Path(tmp),acquisitions)
  except ValueError:
   assert tamper,'The unmodified manifest-pinned dependency set must be accepted'
   assert acquisitions[-1]['passed'] is False
  else:
   assert not tamper,'Requirement content must match its manifest digest'
   assert actual==expected
`);
});

test('scientific and bootstrap subprocess environments retain needed runtime settings without forwarding credentials or Python path overrides', () => {
  python(String.raw`
c=module('public_ci_bootstrap',ROOT/'scripts/run-atlas-public-ci.py')
parent={'PATH':'/safe/bin','LANG':'C.UTF-8','HOME':'/original-home',
        'GITHUB_TOKEN':'token-value','AWS_SECRET_ACCESS_KEY':'aws-value','ATLAS_TEST_SECRET':'custom-value',
        'OPENAI_API_KEY':'api-value','PYTHONPATH':'untrusted-imports','PYTHONHOME':'untrusted-runtime'}
with tempfile.TemporaryDirectory() as tmp:
 for host in [v,c]:
  env=host.child_environment(pathlib.Path(tmp),parent=parent)
  assert env.get('PATH')==parent['PATH']
  assert env.get('MPLBACKEND')=='Agg'
  assert env.get('PYTHONNOUSERSITE')=='1'
  for key in ['GITHUB_TOKEN','AWS_SECRET_ACCESS_KEY','ATLAS_TEST_SECRET','OPENAI_API_KEY','PYTHONPATH','PYTHONHOME']:
   assert key not in env,key
  assert not any(value in env.values() for value in ['token-value','aws-value','custom-value','api-value'])
`);
});

test('the verifier saves a structured failure report when the public registry cannot be acquired', () => {
  python(String.raw`
with tempfile.TemporaryDirectory() as tmp:
 out=pathlib.Path(tmp)/'report.json'
 argv=['verify','--output',str(out),'--expected-registry-sha256','0'*64]
 with mock.patch.object(sys,'argv',argv),mock.patch.object(v,'checked_download',side_effect=urllib.error.URLError('simulated acquisition failure')):
  code=v.main()
 assert code!=0
 report=json.loads(out.read_text())
 assert report['passed'] is False
 assert report.get('error') or report.get('errors') or report.get('phase')
 assert 'simulated acquisition failure' in json.dumps(report)
 json.dumps(report,allow_nan=False)
`);
});

test('bootstrap setup failure is recorded without claiming that scientific checks ran or passed', () => {
  python(String.raw`
c=module('public_ci_bootstrap',ROOT/'scripts/run-atlas-public-ci.py')
registry=(ROOT/'numerical-methods-atlas/code-and-data/examples.json').read_bytes()
verifier=(ROOT/'scripts/verify-atlas-execution-examples.py').read_bytes()
builder=(ROOT/'scripts/build-atlas-execution-examples.py').read_bytes()
payloads={'https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json':registry,
          'https://hrkoyama.github.io/scripts/verify-atlas-execution-examples.py':verifier,
          'https://hrkoyama.github.io/scripts/build-atlas-execution-examples.py':builder}
def download(url,expected=None,**kwargs):
 payload=payloads[url]
 if expected is not None:assert hashlib.sha256(payload).hexdigest()==expected
 return payload
with tempfile.TemporaryDirectory() as tmp:
 output=pathlib.Path(tmp)/'new-output'
 args=['--output-dir',str(output),'--registry-sha256',hashlib.sha256(registry).hexdigest(),
       '--verifier-sha256',hashlib.sha256(verifier).hexdigest(),'--builder-sha256',hashlib.sha256(builder).hexdigest()]
 with mock.patch.object(c,'download',side_effect=download),mock.patch.object(c,'collect_requirements',return_value=dict(c.REQUIRED_PINS)),mock.patch.object(c,'create_environment',side_effect=RuntimeError('simulated wheel installation failure')),mock.patch.object(c,'run_logged',side_effect=AssertionError('Do not run science after failed setup')):
  code=c.main(args)
 assert code!=0
 summary=json.loads((output/'ci-summary.json').read_text())
 assert summary['setup_passed'] is False and summary['scientific_passed'] is not True and summary['passed'] is False
 assert summary.get('phase') and summary.get('error')
 assert 'simulated wheel installation failure' in json.dumps(summary)
`);
});

test('bootstrap requires successful process completion and a matching successful numerical report, with a positive control', () => {
  python(String.raw`
c=module('public_ci_bootstrap',ROOT/'scripts/run-atlas-public-ci.py')
registry=(ROOT/'numerical-methods-atlas/code-and-data/examples.json').read_bytes()
verifier=(ROOT/'scripts/verify-atlas-execution-examples.py').read_bytes()
builder=(ROOT/'scripts/build-atlas-execution-examples.py').read_bytes()
good=json.loads((ROOT/'numerical-methods-atlas/code-and-data/verification/2026-11-22-periodic.json').read_text())
good['verification_tool']['verifier_sha256']=hashlib.sha256(verifier).hexdigest()
good['verification_tool']['registry_builder_sha256']=hashlib.sha256(builder).hexdigest()
# Adapt the old saved success to the new diagnostic field in memory only.
for row in good['releases']+good['examples']:row['execution']['started']=True
payloads={'https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json':registry,
          'https://hrkoyama.github.io/scripts/verify-atlas-execution-examples.py':verifier,
          'https://hrkoyama.github.io/scripts/build-atlas-execution-examples.py':builder}
def download(url,expected=None,**kwargs):
 payload=payloads[url]
 if expected is not None:assert hashlib.sha256(payload).hexdigest()==expected
 return payload
for scenario in ['process-failed','timed-out','numerical-failed','wrong-registry','wrong-tool','incomplete','wrong-runner-count','missing-release','missing-report','success']:
 with tempfile.TemporaryDirectory() as tmp:
  output=pathlib.Path(tmp)/'new-output';calls=[]
  args=['--output-dir',str(output),'--registry-sha256',hashlib.sha256(registry).hexdigest(),
        '--verifier-sha256',hashlib.sha256(verifier).hexdigest(),'--builder-sha256',hashlib.sha256(builder).hexdigest()]
  def logged(argv,cwd,env,timeout,stdout_path,stderr_path):
   calls.append(argv)
   for path in [stdout_path,stderr_path]:path=pathlib.Path(path);path.parent.mkdir(parents=True,exist_ok=True);path.write_text('mock log')
   if 'install' in argv:
    assert '--isolated' in argv and '--no-cache-dir' in argv and '--only-binary=:all:' in argv
    assert argv[argv.index('--index-url')+1]=='https://pypi.org/simple'
    assert set(arg for arg in argv if '==' in arg)=={name+'=='+version for name,version in c.REQUIRED_PINS.items()}
    wheels=[{'metadata':{'name':name,'version':version},'download_info':{'url':'https://files.pythonhosted.org/packages/mock/'+name+'-'+version+'-py3-none-any.whl','archive_info':{'hashes':{'sha256':hashlib.sha256(name.encode()).hexdigest()}}}} for name,version in c.REQUIRED_PINS.items()]
    pathlib.Path(argv[argv.index('--report')+1]).write_text(json.dumps({'install':wheels}))
   if '-c' in argv:
    pathlib.Path(stdout_path).write_text(json.dumps({'python':'3.12.0','operating_system':'Linux','machine':'x86_64','packages':c.REQUIRED_PINS}))
   if '--output' in argv and scenario!='missing-report':
    report=copy.deepcopy(good)
    if scenario=='numerical-failed':report['passed']=False
    elif scenario=='wrong-registry':report['registry_sha256']='0'*64
    elif scenario=='wrong-tool':report['verification_tool']['verifier_sha256']='0'*64
    elif scenario=='incomplete':report['examples'][0]['execution']['completed']=False
    elif scenario=='wrong-runner-count':report['unique_runner_executions']=13
    elif scenario=='missing-release':report['releases'].pop()
    pathlib.Path(argv[argv.index('--output')+1]).write_text(json.dumps(report))
   verification='--output' in argv
   return {'exit_code':7 if verification and scenario=='process-failed' else 0,'timed_out':verification and scenario=='timed-out','duration_seconds':0.01}
  with mock.patch.object(c,'download',side_effect=download),mock.patch.object(c,'collect_requirements',return_value=dict(c.REQUIRED_PINS)),mock.patch.object(c,'create_environment',return_value=pathlib.Path(sys.executable)),mock.patch.object(c,'run_logged',side_effect=logged):
   code=c.main(args)
  summary=json.loads((output/'ci-summary.json').read_text())
  assert any('--output' in command for command in calls) and summary['setup_passed'] is True,(scenario,summary)
  assert summary['scientific_passed'] is (scenario=='success'),scenario
  assert summary['passed'] is (scenario=='success'),scenario
  assert (code==0) is (scenario=='success'),scenario
  stored=json.loads((output/'report.json').read_text())
  assert stored['passed'] is (scenario=='success'),scenario
  if scenario not in ['success','numerical-failed','missing-report']:
   rejected=json.loads((output/'report-unaccepted.json').read_text())
   assert rejected['passed'] is True,'Keep rejected evidence, but never expose it as the accepted report'
  json.dumps(summary,allow_nan=False)
`);
});

test('an initial CI page with no saved snapshots keeps external live status separate and invents no successful receipt', () => {
  python(String.raw`
p=module('ci_page',ROOT/'scripts/build-atlas-ci-page.py')
config,current,snapshots,source_hash=p.load(ROOT)
config=copy.deepcopy(config);config['snapshots']=[]
with mock.patch.object(p,'load',return_value=(config,current,[],source_hash)):
 html,public=p.build(ROOT)
assert public['snapshots']==[]
assert public['latest_status']=={'source':'external-github-actions-badge','recorded_conclusion':None}
assert public['workflow_runs_api']==config['workflow']['runs_api']
assert config['workflow']['badge_url'] in html.replace('&amp;','&')
assert config['workflow']['runs_url'] in html
assert 'class="ci-pending"' in html
assert 'class="ci-snapshot"' not in html
for lang in ['ja','en']:
 assert 'id="latest-'+lang+'"' in html and 'id="saved-'+lang+'"' in html
`);
});

test('a saved Linux success rechecks observations and rejects failed setup, another OS, incomplete execution or modified criteria', () => {
  python(String.raw`
p=module('ci_page',ROOT/'scripts/build-atlas-ci-page.py')
config=json.loads((ROOT/'catalog/atlas-ci.json').read_text())
raw=(ROOT/'numerical-methods-atlas/code-and-data/examples.json').read_bytes();registry=json.loads(raw);sha=hashlib.sha256(raw).hexdigest()
report=json.loads((ROOT/'numerical-methods-atlas/code-and-data/verification/2026-11-22-periodic.json').read_text())
report['environment']['operating_system']='Linux'
url='https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/ci/verification/unit-fixture.json'
envelope={'schema_version':1,'ci':{'setup_passed':True,'scientific_passed':True,'passed':True,'error':None},'verification':report,
          'run_id':'12345','attempt':1,'workflow_commit':'a'*40,
          'run_url':'https://github.com/hrkoyama/hrkoyama.github.io/actions/runs/12345',
          'artifact_url':'https://github.com/hrkoyama/hrkoyama.github.io/actions/runs/12345/artifacts/67890'}
valid=p.validate_snapshot(url,envelope,registry,sha,config,b)
assert valid['recorded_success'] is True and valid['registry_matches_current'] is True
assert valid['example_count']==21 and valid['runner_count']==20
for scenario in ['setup','science','overall','os','incomplete','criterion']:
 bad=copy.deepcopy(envelope)
 if scenario in ['setup','science','overall']:bad['ci'][{'setup':'setup_passed','science':'scientific_passed','overall':'passed'}[scenario]]=False
 elif scenario=='os':bad['verification']['environment']['operating_system']='Darwin'
 elif scenario=='incomplete':bad['verification']['examples'][0]['execution']['completed']=False
 else:
  check=next(row for row in bad['verification']['examples'][0]['validation']['checks'] if row['id']=='relative-force-error')
  check['tolerance']=.5
 try:p.validate_snapshot(url,bad,registry,sha,config,b)
 except (ValueError,KeyError,TypeError):pass
 else:raise AssertionError('False successful snapshot accepted: '+scenario)
historical=copy.deepcopy(envelope);historical['verification']['registry_sha256']='0'*64
record=p.validate_snapshot(url,historical,registry,sha,config,b)
assert record['registry_matches_current'] is False
assert 'Historical success' in p.snapshot_html(record,config,'en')
`);
});
