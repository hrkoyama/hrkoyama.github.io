import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {methodIds,methodCount,methodStatusCounts,supplementGroupIds,supplementCaseIds} from './fixtures/atlas-inventory.mjs';
const root=fileURLToPath(new URL('../',import.meta.url));
const run=source=>execFileSync('python3',['-B','-c',source],{cwd:root,encoding:'utf8'});

test('canonical registration IDs and statuses match the public methods and every immutable supplement',()=>{
 const value=JSON.parse(run(`import json,sys\nfrom pathlib import Path\nsys.path.insert(0,'scripts')\nfrom atlas_registration import inventory,validate_public_methods,read_json\nroot=Path.cwd()\nvalidate_public_methods(root,read_json(root/'numerical-methods-atlas/methods/index.json')['methods'])\nprint(json.dumps(inventory(root)))`));
 assert.deepEqual(value.method_ids,methodIds);assert.equal(value.method_ids.length,methodCount);assert.deepEqual(value.method_status_counts,methodStatusCounts);assert.deepEqual(value.supplement_groups,supplementGroupIds);assert.deepEqual(value.supplement_case_ids,supplementCaseIds);
});

test('invalid IDs, duplicates, unregistered evidence and unsupported educational status fail without running science',()=>{
 assert.match(run(String.raw`
import copy,json,shutil,sys,tempfile
from pathlib import Path
sys.path.insert(0,'scripts')
from atlas_registration import inventory,catalogs,read_json,validate_public_methods
root=Path.cwd();original_methods,original_depth=catalogs(root)
with tempfile.TemporaryDirectory(prefix='atlas-registration-') as temporary:
 fixture=Path(temporary);(fixture/'catalog/schemas').mkdir(parents=True)
 for p in ['catalog/atlas-registration.json','catalog/schemas/atlas-registration.schema.json']:shutil.copyfile(root/p,fixture/p)
 for g in original_depth['groups']:
  name='code/validated-examples/'+g.get('edition',original_depth['edition'])+'/'+g['id']+'/cases.json';p=fixture/name;p.parent.mkdir(parents=True);shutil.copyfile(root/name,p)
 def write(methods,depth):
  (fixture/'catalog/atlas-methods.json').write_text(json.dumps(methods));(fixture/'catalog/atlas-depth-expansion.json').write_text(json.dumps(depth))
 for mutation in ['id','duplicate','status','field','group','unknown-case']:
  methods=copy.deepcopy(original_methods);depth=copy.deepcopy(original_depth)
  if mutation=='id':methods['methods'][0]['id']='../outside'
  if mutation=='duplicate':methods['methods'].append(methods['methods'][0])
  if mutation=='status':methods['methods'][0]['status']='verified-everywhere'
  if mutation=='field':methods['methods'][0]['group']['id']='unregistered'
  if mutation=='group':depth['groups'].append(depth['groups'][0])
  if mutation=='unknown-case':next(m for m in methods['methods'] if m.get('depth_release'))['depth_release']['case_ids']=['unregistered-case']
  write(methods,depth)
  try:inventory(fixture)
  except (ValueError,AssertionError):pass
  else:raise AssertionError(mutation+' was accepted')
 write(original_methods,original_depth)
 public=read_json(root/'numerical-methods-atlas/methods/index.json')['methods']
 changed=copy.deepcopy(public);row=next(m for m in changed if m['status']=='educational-example');row['code_urls']=[]
 try:validate_public_methods(fixture,changed)
 except ValueError:pass
 else:raise AssertionError('educational status without code accepted')
 changed=copy.deepcopy(public);next(m for m in changed if m['status']=='planned')['status']='educational-example'
 try:validate_public_methods(fixture,changed)
 except ValueError:pass
 else:raise AssertionError('unreviewed status promotion accepted')
print('invalid registration rejected')
`),/invalid registration rejected/);
});

test('one canonical registration updates current inventory, packager choices and the standalone verifier allowlist',()=>{
 assert.match(run(String.raw`
import ast,copy,json,shutil,subprocess,sys,tempfile
from pathlib import Path
sys.path.insert(0,'scripts')
from atlas_registration import catalogs,inventory
from depth_verifier_assets import render_depth_verifier
original=Path.cwd();methods,depth=catalogs(original)
with tempfile.TemporaryDirectory(prefix='atlas-registration-growth-') as temporary:
 root=Path(temporary)
 for name in ['catalog/atlas-registration.json','catalog/schemas/atlas-registration.schema.json','scripts/atlas_registration.py','scripts/package-depth-examples.py','scripts/templates/verify-depth-public.py.tmpl']:
  target=root/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(original/name,target)
 for row in depth['groups']:
  name='code/validated-examples/'+row.get('edition',depth['edition'])+'/'+row['id']+'/cases.json';target=root/name;target.parent.mkdir(parents=True);shutil.copyfile(original/name,target)
 added=copy.deepcopy(next(row for row in methods['methods'] if row['status']=='planned'));added['id']='fixture-new-method';methods['methods'].append(added)
 name='fixture-new-supplement';depth['groups'].append({'id':name,'title':{'ja':'試験群','en':'Fixture group'},'fields':['foundations']})
 values=json.loads((root/'code/validated-examples'/depth['edition']/'foundations/cases.json').read_text());case=copy.deepcopy((values['cases'] if isinstance(values,dict) else values)[0]);case['id']='fixture-new-case';case['method_ids']=[methods['methods'][0]['id']]
 target=root/'code/validated-examples'/depth['edition']/name/'cases.json';target.parent.mkdir(parents=True);target.write_text(json.dumps([case]))
 (root/'catalog/atlas-methods.json').write_text(json.dumps(methods));(root/'catalog/atlas-depth-expansion.json').write_text(json.dumps(depth))
 value=inventory(root);assert value['method_ids'][-1]=='fixture-new-method' and value['supplement_groups'][-1]==name and value['supplement_case_ids'][-1]=='fixture-new-case'
 help_text=subprocess.check_output([sys.executable,str(root/'scripts/package-depth-examples.py'),'--help'],text=True);assert name in help_text
 render_depth_verifier(root)
 tree=ast.parse((root/'scripts/verify-depth-public.py').read_text());groups=next(ast.literal_eval(node.value) for node in tree.body if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='GROUPS' for t in node.targets));assert groups[-1]==name
 help_text=subprocess.check_output([sys.executable,str(root/'scripts/verify-depth-public.py'),'--help'],text=True);assert 'usage:' in help_text
print('single-source growth checked without scientific execution')
`),/single-source growth checked without scientific execution/);
});
