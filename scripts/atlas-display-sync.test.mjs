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
 'bio-logistic':{common:['logistic-growth'],supplemental:[]},
 'bio-sir':{common:['sir-epidemic'],supplemental:[]},
 'bio-turing':{common:[],supplemental:['turing-schnakenberg','schnakenberg-nonlinear','schnakenberg-pattern']},
 'bio-schnakenberg':{common:[],supplemental:['turing-schnakenberg','schnakenberg-nonlinear','schnakenberg-pattern']},
 'bio-fitzhugh-nagumo':{common:[],supplemental:['fitzhugh-nagumo']},
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

test('five biology labels expose only their verified common or supplemental scope, without adding equations or physical problems',()=>{
 assert.equal(equations.length,49);
 assert.equal(equations.filter(x=>!['rotational-advection','shallow-water-bed','forced-incompressible'].includes(x.id)&&x.status==='local-example').length,23);
 assert.equal(equations.filter(x=>x.status==='reading').length,23);
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
 for(const id of ['bio-hodgkin-huxley','bio-gray-scott'])assert.equal(equations.find(x=>x.id===id).status,'reading');
 const uniqueSupplementIds=new Set(Object.keys(expected).flatMap(id=>equations.find(x=>x.id===id).supplemental_examples||[]));
 assert.deepEqual([...uniqueSupplementIds].sort(),['fitzhugh-nagumo','schnakenberg-nonlinear','schnakenberg-pattern','turing-schnakenberg']);
 assert.equal(createHash('sha256').update(read('numerical-methods-atlas/code-and-data/examples.json')).digest('hex'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
});

test('actual evidence resolves immutable receipts and refuses borrowed, missing or inflated biological executions',()=>{
 python(String.raw`
value=equation_evidence(ROOT,equations,discovery)
assert [x for x in value['supplemental_case_ids'] if x not in ['zalesak-rotation','weno-critical-epsilon','swashes-topography','dry-bed-dam-break','cavity-ghia-re100','wall-manufactured']]==['fitzhugh-nagumo','schnakenberg-nonlinear','schnakenberg-pattern','turing-schnakenberg']
assert len(value['common']['bio-logistic'])==len(value['common']['bio-sir'])==1
for scenario in ['borrow-hh','wrong-case','missing-common','inflated-scope']:
 rows=copy.deepcopy(equations);d=copy.deepcopy(discovery);byid={x['id']:x for x in rows}
 if scenario=='borrow-hh':
  byid['bio-hodgkin-huxley'].update(status='local-example',supplemental_examples=['fitzhugh-nagumo'])
 elif scenario=='wrong-case':byid['bio-turing']['supplemental_examples']=['fitzhugh-nagumo']
 elif scenario=='missing-common':next(x for x in d['examples'] if x['id']=='sir-epidemic')['equation_ids']=[]
 else:byid['bio-fitzhugh-nagumo']['execution_scope']['en']='Full spatial Hodgkin-Huxley validation'
 try:equation_evidence(ROOT,rows,d)
 except AssertionError:pass
 else:raise AssertionError('Invalid execution mapping accepted: '+scenario)
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
historical=[x for x in public['equations'] if x['id'] not in ['rotational-advection','shallow-water-bed','forced-incompressible']]
assert len(historical)==46 and sum(x['status']=='local-example' for x in historical)==23
assert public['counts']['total']==len(public['equations'])
assert public['counts']['local_example']==sum(x['status']=='local-example' for x in public['equations'])
assert public['execution_example_count']==22
assert [x for x in public['supplemental_case_ids'] if x not in ['zalesak-rotation','weno-critical-epsilon','swashes-topography','dry-bed-dam-break','cavity-ghia-re100','wall-manufactured']]==['fitzhugh-nagumo','schnakenberg-nonlinear','schnakenberg-pattern','turing-schnakenberg']
rows={x['id']:x for x in public['equations']}
for ident in ['bio-turing','bio-schnakenberg']:
 assert rows[ident]['execution_examples']==[]
 assert [x['id'] for x in rows[ident]['supplemental_execution_examples']]==['turing-schnakenberg','schnakenberg-nonlinear','schnakenberg-pattern']
for ident,case in [('bio-logistic','logistic-growth'),('bio-sir','sir-epidemic')]:
 assert [x['id'] for x in rows[ident]['execution_examples']]==[case]
 assert rows[ident]['supplemental_execution_examples']==[]
for lang in ['ja','en']:
 for case in ['fitzhugh-nagumo','schnakenberg-nonlinear','schnakenberg-pattern','turing-schnakenberg']:
  assert '/numerical-methods-atlas/validation/'+case+'/?lang='+lang in html
 assert '/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang='+lang in html
assert 'D=0' in html and 'katex-error' not in html
assert '共通22実行例とは別' in html and 'separate from the common 22 registry' in html
for ident in ['bio-hodgkin-huxley','bio-gray-scott']:
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
 for(const method of methods.filter(x=>x.group.id==='quantum')){
  assert.match(method.next_deliverable.en,/Maintain/);
  assert.match(method.next_deliverable.en,/explicit need|only when needed/);
 }
 for(const field of json('catalog/atlas-depth.json').fields.filter(x=>x.id.startsWith('quantum-'))){
  assert.match(field.next.en,/existing small examples/);assert.match(field.next.en,/only on explicit need/);
 }
 const generator=read('scripts/build-atlas-quantum.py');
 assert.ok(generator.includes('Quantum examples stay limited'));
 assert.ok(!generator.includes('Molecular and periodic examples remain next.'));
});
