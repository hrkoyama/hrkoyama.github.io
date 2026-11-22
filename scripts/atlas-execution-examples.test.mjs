import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
const root=new URL('../',import.meta.url);
const read=p=>JSON.parse(readFileSync(new URL(p,root),'utf8'));
const data=read('catalog/atlas-execution-examples.json');
const bootstrap=`import importlib.util, json, pathlib, copy, io, zipfile, tempfile, hashlib, stat\nfrom unittest import mock\ndef module(name,path):\n s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m\nb=module('registry_builder','scripts/build-atlas-execution-examples.py')\nv=module('registry_verifier','scripts/verify-atlas-execution-examples.py')\nd=json.loads(pathlib.Path('catalog/atlas-execution-examples.json').read_bytes())\n`;
function python(source){return execFileSync('python3',['-c',bootstrap+source],{cwd:root,encoding:'utf8'});}

test('the twenty-two common recipes map to existing problems/methods and verified immutable artifacts',()=>{
  assert.equal(data.examples.length,22);
  assert.deepEqual(data.examples.slice(0,3).map(x=>x.id),['barnes-hut','hydrogenic-atoms','helium-ground-state']);
  const problems=read('catalog/atlas-test-problems.json').problems;
  const methods=read('catalog/atlas-methods.json').methods;
  for(const x of data.examples){
    assert.ok(problems.some(p=>p.id===x.problem_id));
    assert.ok(x.method_ids.every(id=>methods.some(m=>m.id===id)));
    for(const key of ['install','run','tests'])assert.equal(typeof x.commands[key],'string');
    assert.ok(x.outputs.some(o=>o.format==='csv')&&x.outputs.some(o=>o.format==='json'));
    assert.ok(x.terms.code_license.endsWith('/LICENSE'));
    assert.equal(x.terms.content_and_data,'https://hrkoyama.github.io/rights/');
  }
  assert.match(python("r=b.build_registry(d,source_bytes=pathlib.Path('catalog/atlas-execution-examples.json').read_bytes())\nassert len(r['examples'])==22\nassert r['url'].endswith('/code-and-data/examples.json')\nprint('verified')\n"),/verified/);
});

test('incompatible schema, false input hashes and inconsistent shared runners are rejected',()=>{
  python(`bad=copy.deepcopy(d);bad['schema_version']=2
try:b.validate_registry(bad)
except ValueError:pass
else:raise AssertionError('unsupported schema accepted')
bad=copy.deepcopy(d);bad['examples'][0]['inputs']['sha256']='0'*64
try:b.build_registry(bad)
except ValueError:pass
else:raise AssertionError('bad input hash accepted')
bad=copy.deepcopy(d);bad['examples'][2]['commands']['run_argv'][1]='other.py'
try:b.validate_registry(bad)
except ValueError:pass
else:raise AssertionError('inconsistent shared runner accepted')
`);
});

test('false flags, missing result fields and non-finite/boolean numerics never count as passed',()=>{
  python(`assert not b.evaluate_check({'checks':{'a':True,'b':False}},{'id':'flags','pointer':'/checks','comparison':'all_true'})['passed']
assert not b.evaluate_check({'value':True},{'id':'numeric','pointer':'/value','comparison':'maximum','tolerance':1})['passed']
assert not b.evaluate_check({'value':float('nan')},{'id':'numeric','pointer':'/value','comparison':'maximum','tolerance':1})['passed']
assert not b.evaluate_check({},d['examples'][0]['checks'][0])['passed']
c={'id':'failure','pointer':'/converged','comparison':'equals','expected':False}
assert b.evaluate_check({'converged':False},c)['passed']
assert not b.evaluate_check({'converged':0},c)['passed']
assert not b.evaluate_check({'a':[]},{'id':'empty','pointer':'/a','field':'error','comparison':'maximum','tolerance':1})['passed']
`);
});

test('independent download verification rejects a mismatched SHA-256',()=>{
  python(`class Response(io.BytesIO):
 def geturl(self):return 'https://hrkoyama.github.io/code/example/input.json'
with mock.patch.object(v.PUBLIC_OPENER,'open',return_value=Response(b'changed')):
 try:v.checked_download('https://hrkoyama.github.io/code/example/input.json','0'*64)
 except ValueError:pass
 else:raise AssertionError('download hash mismatch accepted')
`);
});

test('archive extraction rejects traversal and symbolic links, and accepts all seven public editions',()=>{
  python(`releases={}
for x in d['examples']:
 r=x['release'];identity=(r['family'],r['version'],r['download'],r['sha256'])
 releases.setdefault(identity,[]).append(x)
assert len(releases)==7
assert ('numerical-methods-atlas','2026-11-22') in {identity[:2] for identity in releases}
with tempfile.TemporaryDirectory() as td:
 for index,cases in enumerate(releases.values()):
  r=cases[0]['release'];mb=(b.ROOT/b.public_path(r['manifest'])).read_bytes();m=json.loads(mb)
  folder=v.safe_extract((b.ROOT/b.public_path(r['download'])).read_bytes(),m,r,pathlib.Path(td)/('release-'+str(index)))
  for x in cases:assert (folder/x['inputs']['path']).is_file(),x['id']
 payload=io.BytesIO()
 with zipfile.ZipFile(payload,'w') as z:z.writestr('../escaped.txt','bad')
 try:v.safe_extract(payload.getvalue(),{'files':{}},{'archive_directory':'edition','manifest_sha256':'0'*64},pathlib.Path(td))
 except ValueError:pass
 else:raise AssertionError('traversal accepted')
 payload=io.BytesIO();manifest=b'{}';m={'files':{'file.py':hashlib.sha256(b'x').hexdigest()}};r={'archive_directory':'edition','manifest_sha256':hashlib.sha256(manifest).hexdigest()}
 with zipfile.ZipFile(payload,'w') as z:
  info=zipfile.ZipInfo('edition/file.py');info.external_attr=(stat.S_IFLNK|0o777)<<16;z.writestr(info,b'x');z.writestr('edition/source-manifest.json',manifest)
 try:v.safe_extract(payload.getvalue(),m,r,pathlib.Path(td))
 except ValueError:pass
 else:raise AssertionError('symbolic link accepted')
`);
});
