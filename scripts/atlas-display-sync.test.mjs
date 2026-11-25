import {projectMethodBeforeFinal23} from './fixtures/atlas-final23-projection.mjs';
import {equationCount,equationsAddedAfterBatch37,examplesAddedAfterBatch37} from './fixtures/atlas-inventory.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';

const root=new URL('../',import.meta.url);
const read=path=>readFileSync(new URL(path,root),'utf8');
const json=path=>JSON.parse(read(path));
const equations=json('catalog/atlas-equations.json').equations;
const methods=json('catalog/atlas-methods.json').methods;
const expected={
 'bio-enzyme':{common:[],supplemental:['enzyme-qssa']},
 'bio-lotka-volterra':{common:[],supplemental:['lotka-volterra']},
 'bio-logistic':{common:['logistic-growth'],supplemental:[]},
 'bio-sir':{common:['sir-epidemic'],supplemental:[]},
 'bio-turing':{common:[],supplemental:['turing-schnakenberg','schnakenberg-nonlinear','schnakenberg-pattern']},
 'bio-schnakenberg':{common:[],supplemental:['turing-schnakenberg','schnakenberg-nonlinear','schnakenberg-pattern','schnakenberg-2d-boundary-modes']},
 'bio-fitzhugh-nagumo':{common:[],supplemental:['fitzhugh-nagumo']},
 'bio-hodgkin-huxley':{common:[],supplemental:['hodgkin-huxley-controls']},
 'bio-fisher-kpp':{common:[],supplemental:['fisher-kpp-special-front']},
 'bio-keller-segel':{common:[],supplemental:['keller-segel-forced-flux']},
 'bio-chemical-master':{common:[],supplemental:['immigration-death-ssa']},
};
const prelude=String.raw`
import ast,copy,json,pathlib,sys
ROOT=pathlib.Path.cwd();sys.path.insert(0,'scripts')
from atlas_execution_discovery import load_discovery
from atlas_equation_availability import equation_evidence
equations=json.loads((ROOT/'catalog/atlas-equations.json').read_text())['equations']
discovery=load_discovery(ROOT)
`;
const python=source=>execFileSync('python3',['-B','-c',prelude+source],{cwd:root,encoding:'utf8',timeout:30000});

test('eleven surveyed biology labels expose only their verified common or supplemental scope',()=>{
 assert.equal(equations.length,equationCount);
 assert.equal(equations.filter(x=>!['rotational-advection','shallow-water-bed','forced-incompressible','level-set-advection', 'forced-vorticity', 'boussinesq-buoyancy', 'ale-scalar-transport', 'linear-rotating-shallow-water', 'variable-viscosity-vector', 'srmhd', 'srhd','tensor-diffusion','coulomb-electrostatics','vlasov-poisson','hard-sphere-boltzmann','bio-enzyme','bio-lotka-volterra',...equationsAddedAfterBatch37].includes(x.id)&&!['bio-hodgkin-huxley','bio-fisher-kpp','bio-keller-segel','bio-chemical-master'].includes(x.id)&&x.status==='local-example').length,23);
 assert.equal(equations.filter(x=>x.status==='reading').length+['bio-hodgkin-huxley','bio-fisher-kpp','bio-keller-segel','bio-chemical-master'].length,20);
 const discovery=json('catalog/atlas-execution-discovery.json').examples;
 for(const [id,wanted] of Object.entries(expected)){
  const model=equations.find(x=>x.id===id);assert.equal(model.status,'local-example');
  assert.ok(model.execution_scope.ja&&model.execution_scope.en);
  assert.deepEqual(discovery.filter(x=>x.equation_ids.includes(id)).map(x=>x.id),wanted.common);
  assert.deepEqual(model.supplemental_examples||[],wanted.supplemental);
  assert.ok(!model.note.ja.includes('文献解説のみ')&&!model.note.en.includes('Literature-only'));
 }
 assert.ok(equations.find(x=>x.id==='bio-sir').execution_scope.en.includes('SEIR'));
 assert.ok(equations.find(x=>x.id==='bio-fitzhugh-nagumo').note.en.includes('D=0'));
 for(const id of ['bio-gray-scott'])assert.equal(equations.find(x=>x.id===id).status,'reading');
 const uniqueSupplementIds=new Set(Object.keys(expected).flatMap(id=>equations.find(x=>x.id===id).supplemental_examples||[]));
 assert.deepEqual([...uniqueSupplementIds].sort(),['enzyme-qssa','fisher-kpp-special-front','fitzhugh-nagumo','hodgkin-huxley-controls','immigration-death-ssa','keller-segel-forced-flux','lotka-volterra','schnakenberg-2d-boundary-modes','schnakenberg-nonlinear','schnakenberg-pattern','turing-schnakenberg']);
 assert.equal(createHash('sha256').update(read('numerical-methods-atlas/code-and-data/examples.json')).digest('hex'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
});

test('actual evidence resolves immutable receipts and refuses borrowed, missing or inflated biological executions',()=>{
 python(String.raw`
# Test-local immutable snapshot only; production loaders are unchanged.
from hashlib import sha256
from urllib.parse import urlsplit
from unittest import mock
import atlas_equation_availability as equation_module

requested_ids=list(dict.fromkeys(ident for row in equations for ident in row.get('supplemental_examples',[])))
snapshot_paths=set(['scripts/atlas_terminology.py','catalog/atlas-terminology.json','scripts/atlas_equation_availability.py','scripts/atlas_goal_availability.py','scripts/atlas_depth_release.py','scripts/atlas_registration.py','scripts/atlas_execution_discovery.py','scripts/atlas-display-sync.test.mjs','catalog/atlas-registration.json','catalog/schemas/atlas-registration.schema.json','catalog/atlas-equations.json','catalog/atlas-execution-examples.json','catalog/atlas-execution-discovery.json','catalog/atlas-depth-expansion.json','numerical-methods-atlas/assets/biological-models.json','numerical-methods-atlas/code-and-data/examples.json'])

def checked_file(relative):
 path=ROOT/relative
 if not isinstance(relative,str) or path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(ROOT.resolve()):
  raise RuntimeError('Unsafe immutable snapshot path')
 return path

registry=json.loads(checked_file('numerical-methods-atlas/code-and-data/examples.json').read_text())
receipt=urlsplit(registry['verification_receipt'])
if receipt.scheme!='https' or receipt.netloc!='hrkoyama.github.io' or receipt.query or receipt.fragment:
 raise RuntimeError('Unexpected common verification destination')
snapshot_paths.add(receipt.path.lstrip('/'))
config=json.loads(checked_file('catalog/atlas-depth-expansion.json').read_text())
for group in config['groups']:
 edition=group.get('edition',config['edition'])
 prefix='code/validated-examples/'+edition+'/'+group['id']+'/'
 metadata_path=prefix+'cases.json';snapshot_paths.add(metadata_path)
 raw=json.loads(checked_file(metadata_path).read_text());metadata=raw['cases'] if isinstance(raw,dict) else raw
 if not set(requested_ids).intersection(row['id'] for row in metadata):continue
 manifest_path=prefix+'source-manifest.json';verification_path=prefix+'verification.json'
 snapshot_paths.update([manifest_path,verification_path])
 manifest=json.loads(checked_file(manifest_path).read_text());verification=json.loads(checked_file(verification_path).read_text())
 for name in manifest['files']:
  if name.startswith('/') or '..' in pathlib.PurePosixPath(name).parts or '\\' in name:raise RuntimeError('Unsafe snapshot member')
  snapshot_paths.add(prefix+name)
 snapshot_paths.add(prefix+verification['archive']['file'])

def fingerprint_snapshot():
 return {name:sha256(checked_file(name).read_bytes()).hexdigest() for name in sorted(snapshot_paths)}

before_sha=fingerprint_snapshot()
real_loader=equation_module.load_supplemental_examples
verified={};real_calls=[];replay_calls=[]

def capture_verified(root,identifiers):
 if pathlib.Path(root).resolve()!=ROOT.resolve() or identifiers!=requested_ids:
  raise RuntimeError('Unexpected positive loader request')
 records=real_loader(root,identifiers)  # Mandatory actual full loader, never mocked away.
 if [row['id'] for row in records]!=identifiers:raise RuntimeError('Positive loader order differs')
 real_calls.append(list(identifiers))
 for row in records:
  if row['id'] in verified:raise RuntimeError('Duplicate verified snapshot ID')
  verified[row['id']]=copy.deepcopy(row)
 return records

with mock.patch.object(equation_module,'load_supplemental_examples',side_effect=capture_verified):
 value=equation_evidence(ROOT,equations,discovery)
if len(real_calls)!=1 or list(verified)!=requested_ids:raise RuntimeError('Actual positive full-loader count/order differs')
for name,expected in value['source_sha256'].items():
 if before_sha.get(name)!=expected:raise RuntimeError('Actual positive source SHA is outside/broken snapshot')
verified_original=copy.deepcopy(verified)

def replay_verified(root,identifiers):
 # RuntimeError is deliberate: cache/fixture failures must NOT satisfy a
 # negative control that expects a production mapping AssertionError.
 if pathlib.Path(root).resolve()!=ROOT.resolve() or not isinstance(identifiers,list) or len(identifiers)!=len(set(identifiers)) or not set(identifiers)<=verified.keys():
  raise RuntimeError('Invalid immutable snapshot request')
 result=[copy.deepcopy(verified[ident]) for ident in identifiers]
 if [row['id'] for row in result]!=identifiers:raise RuntimeError('Immutable snapshot request order differs')
 replay_calls.append(list(identifiers))
 return result
assert [x for x in value['supplemental_case_ids'] if x not in ['zalesak-rotation','weno-critical-epsilon','swashes-topography','dry-bed-dam-break','cavity-ghia-re100','wall-manufactured','level-set-translation','level-set-rotation', 'kh-initial-growth', 'rt-initial-growth', 'circular-alfven-refinement', 'magnetic-loop-independent', 'postshock-orszag-tang', 'lshape-fem', 'annular-viscous-mms', 'poisson-neumann', 'poisson-robin', 'ale-nonuniform-transport', 'cgrid-rotating-wave', 'srhd-collision', 'srmhd-alfven', 'sem-poisson-2d', 'fr-periodic-advection','checkerboard-diffusion','rotated-anisotropic-diffusion','neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short','thermal-landau-damping','thermal-two-stream','pic-independent-spatial','dsmc-couette','dsmc-fourier','dsmc-planar-shock']+${JSON.stringify(examplesAddedAfterBatch37)}]==['fitzhugh-nagumo','schnakenberg-nonlinear','schnakenberg-pattern','turing-schnakenberg']
assert len(value['common']['bio-logistic'])==len(value['common']['bio-sir'])==1
try:
 with mock.patch.object(equation_module,'load_supplemental_examples',side_effect=replay_verified):
  for scenario in ['borrow-hh','borrow-reading','wrong-case','missing-common','inflated-scope']:
   rows=copy.deepcopy(equations);d=copy.deepcopy(discovery);byid={x['id']:x for x in rows}
   if scenario=='borrow-hh':
    byid['bio-hodgkin-huxley'].update(status='local-example',supplemental_examples=['fitzhugh-nagumo'])
   elif scenario=='borrow-reading':byid['bio-gray-scott'].update(status='local-example',supplemental_examples=['fitzhugh-nagumo'])
   elif scenario=='wrong-case':byid['bio-turing']['supplemental_examples']=['fitzhugh-nagumo']
   elif scenario=='missing-common':next(x for x in d['examples'] if x['id']=='sir-epidemic')['equation_ids']=[]
   else:byid['bio-fitzhugh-nagumo']['execution_scope']['en']='Full spatial Hodgkin-Huxley validation'
   try:equation_evidence(ROOT,rows,d)
   except AssertionError:pass
   else:raise AssertionError('Invalid execution mapping accepted: '+scenario)
finally:
 # Source edits, even under unchanged manifest names, invalidate the snapshot.
 if fingerprint_snapshot()!=before_sha:raise RuntimeError('Immutable source snapshot changed')
if len(replay_calls)!=5 or verified!=verified_original:
 raise RuntimeError('Negative replay count or owned snapshot mutation differs')
for path in ['scripts/atlas_equation_availability.py','scripts/build-atlas-equations.py','scripts/build-atlas-quantum.py','scripts/integrate-depth-catalog.py']:
 ast.parse((ROOT/path).read_text())
`);
});

test('the actual equation renderer emits both languages, distinct receipts and shared-case links without writing files',()=>{
 python(String.raw`
import collections,runpy
from unittest import mock
original_read=pathlib.Path.read_text
captured={}
def read_text(path,*args,**kwargs):
 text=original_read(path,*args,**kwargs)
 if path.resolve()==(ROOT/'numerical-methods-atlas/coverage.json').resolve():
  value=json.loads(text);canonical={x['id']:x for x in equations}
  for item in value['items']:
   if item['kind']=='equation':item['status']=canonical[item['id']]['status']
  counts=collections.Counter(x['status'] for x in value['items'] if x['kind']=='equation')
  value['counts'].update(local_equations=counts['local-example'],reading_equations=counts['reading'])
  return json.dumps(value)
 return text
def write_text(path,text,*args,**kwargs):captured[str(path.resolve())]=text;return len(text)
with mock.patch.object(pathlib.Path,'read_text',read_text),mock.patch.object(pathlib.Path,'write_text',write_text),mock.patch.object(pathlib.Path,'mkdir'),mock.patch('xml.etree.ElementTree.ElementTree.write'):
 runpy.run_path('scripts/build-atlas-equations.py',run_name='__equation_render_test__')
html=captured[str(ROOT/'numerical-methods-atlas/equations/index.html')]
public=json.loads(captured[str(ROOT/'numerical-methods-atlas/equations/index.json')])
historical=[x for x in public['equations'] if x['id'] not in ['rotational-advection','shallow-water-bed','forced-incompressible','level-set-advection','forced-vorticity','boussinesq-buoyancy','ale-scalar-transport','linear-rotating-shallow-water','variable-viscosity-vector','srmhd','tensor-diffusion','coulomb-electrostatics','vlasov-poisson','hard-sphere-boltzmann']+${JSON.stringify(equationsAddedAfterBatch37)}]
assert len(historical)==46 and sum(x['status']=='local-example' for x in historical if x['id'] not in ['bio-enzyme','bio-lotka-volterra','bio-hodgkin-huxley','bio-fisher-kpp','bio-keller-segel','bio-chemical-master'])==24
assert next(x for x in historical if x['id']=='srhd')['status']=='local-example'
assert sum(x['status']=='local-example' for x in historical if x['id'] not in ['srhd','bio-enzyme','bio-lotka-volterra','bio-hodgkin-huxley','bio-fisher-kpp','bio-keller-segel','bio-chemical-master'])==23
assert public['counts']['total']==len(public['equations'])
assert public['counts']['local_example']==sum(x['status']=='local-example' for x in public['equations'])
assert public['execution_example_count']==22
assert [x for x in public['supplemental_case_ids'] if x not in ['zalesak-rotation','weno-critical-epsilon','swashes-topography','dry-bed-dam-break','cavity-ghia-re100','wall-manufactured','level-set-translation','level-set-rotation', 'kh-initial-growth', 'rt-initial-growth', 'circular-alfven-refinement', 'magnetic-loop-independent', 'postshock-orszag-tang', 'lshape-fem', 'annular-viscous-mms', 'poisson-neumann', 'poisson-robin', 'ale-nonuniform-transport', 'cgrid-rotating-wave', 'srhd-collision', 'srmhd-alfven', 'sem-poisson-2d', 'fr-periodic-advection','checkerboard-diffusion','rotated-anisotropic-diffusion','neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short','thermal-landau-damping','thermal-two-stream','pic-independent-spatial','dsmc-couette','dsmc-fourier','dsmc-planar-shock']+${JSON.stringify(examplesAddedAfterBatch37)}]==['fitzhugh-nagumo','schnakenberg-nonlinear','schnakenberg-pattern','turing-schnakenberg']
rows={x['id']:x for x in public['equations']}
for ident in ['bio-turing','bio-schnakenberg']:
 assert rows[ident]['execution_examples']==[]
 assert [x['id'] for x in rows[ident]['supplemental_execution_examples']]==['turing-schnakenberg','schnakenberg-nonlinear','schnakenberg-pattern']+(['schnakenberg-2d-boundary-modes'] if ident=='bio-schnakenberg' else [])
for ident,case in [('bio-hodgkin-huxley','hodgkin-huxley-controls'),('bio-fisher-kpp','fisher-kpp-special-front'),('bio-keller-segel','keller-segel-forced-flux'),('bio-chemical-master','immigration-death-ssa')]:
 assert rows[ident]['execution_examples']==[]
 assert [x['id'] for x in rows[ident]['supplemental_execution_examples']]==[case]
for ident,case in [('bio-enzyme','enzyme-qssa'),('bio-lotka-volterra','lotka-volterra')]:
 assert rows[ident]['execution_examples']==[]
 assert [x['id'] for x in rows[ident]['supplemental_execution_examples']]==[case]
for ident,case in [('bio-logistic','logistic-growth'),('bio-sir','sir-epidemic')]:
 assert [x['id'] for x in rows[ident]['execution_examples']]==[case]
 assert rows[ident]['supplemental_execution_examples']==[]
for lang in ['ja','en']:
 for case in ['hodgkin-huxley-controls','immigration-death-ssa','fisher-kpp-special-front','schnakenberg-2d-boundary-modes','keller-segel-forced-flux','fitzhugh-nagumo','schnakenberg-nonlinear','schnakenberg-pattern','turing-schnakenberg']:
  assert '/numerical-methods-atlas/validation/'+case+'/?lang='+lang in html
 assert '/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang='+lang in html
assert 'D=0' in html and 'katex-error' not in html
assert '共通22実行例とは別' in html and 'separate from the common 22 registry' in html
for ident in ['bio-gray-scott']:
 assert not rows[ident]['execution_examples'] and not rows[ident]['supplemental_execution_examples']
`);
});

test('released Ewald/SPME metadata and future integration no longer describe dedicated code as planned',()=>{
 for(const id of ['ewald','pme','spme']){
  const method=methods.find(x=>x.id===id);
  assert.equal(method.status,'educational-example');assert.ok(method.depth_release);
  assert.match(method.metadata_review.level,/independently extracted dedicated supplement/);
  assert.doesNotMatch(method.metadata_review.level,/planned formulation|no dedicated implementation/);
  assert.doesNotMatch(method.method_review.variant.ja,/実装前/);
 }
 assert.match(methods.find(x=>x.id==='ewald').method_review.variant.en,/cubic cell with tin-foil/);
 for(const id of ['pme','spme'])assert.match(methods.find(x=>x.id===id).method_review.variant.en,/not an implementation of the original 1993/);
 const source=read('scripts/integrate-depth-catalog.py');assert.ok(source.includes('independently extracted dedicated supplement'));
});

test('quantum next steps maintain small saved examples and defer heavy sweeps and long trajectories to explicit need',()=>{
 const fixed={'mp2':['h3plus-mp2-fci'],'configuration-interaction':['h2-rhf-uhf-fci','h3plus-mp2-fci'],'born-oppenheimer-md':['two-state-bo-cp-ou'],'car-parrinello-md':['two-state-bo-cp-ou']};
 for(const method of methods.filter(x=>x.group.id==='quantum')){
  const previous=projectMethodBeforeFinal23(method);assert.match(previous.next_deliverable.en,/Maintain/);assert.match(previous.next_deliverable.en,/explicit need|only when needed/);
  assert.match(method.next_deliverable.en,/Maintain/);
  if(Object.hasOwn(fixed,method.id)){
   assert.deepEqual(method.depth_release,{group:'quantum-small',edition:'2026-11-25',case_ids:fixed[method.id]});
   assert.equal(method.next_deliverable.en,'Maintain these fixed educational examples; broader extensions require a separately specified need.');
  }else assert.deepEqual(method.next_deliverable,previous.next_deliverable);
 }
 for(const field of json('catalog/atlas-depth.json').fields.filter(x=>x.id.startsWith('quantum-'))){
  assert.match(field.next.en,/existing small examples/);assert.match(field.next.en,/only on explicit need/);
 }
 const generator=read('scripts/build-atlas-quantum.py');
 assert.ok(generator.includes('Quantum examples stay limited'));
 assert.ok(!generator.includes('Molecular and periodic examples remain next.'));
});
