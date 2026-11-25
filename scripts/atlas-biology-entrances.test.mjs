import {equationCount,equationsAddedAfterBatch37,problemCount} from './fixtures/atlas-inventory.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';

const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root),'utf8');
const json=p=>JSON.parse(read(p));
const cases=['schnakenberg-nonlinear','schnakenberg-pattern'];
const shared=['turing-schnakenberg',...cases];

test('earlier nonlinear biology scope is retained beside separately qualified fixed-family cases',()=>{
 const biology=json('catalog/atlas-depth.json').fields.find(x=>x.id==='biology');
 const goal=json('catalog/atlas-goals.json').goals.find(x=>x.id==='biological-models');
 assert.deepEqual(biology.examples,['logistic-growth','sir-epidemic']);
 assert.deepEqual(biology.supplemental_examples,['reaction-diffusion-fourier','turing-schnakenberg','fitzhugh-nagumo',...cases,'reaction-diffusion-splitting','enzyme-qssa','lotka-volterra','seir-linearization',...['hodgkin-huxley-controls','immigration-death-ssa','fisher-kpp-special-front','schnakenberg-2d-boundary-modes','keller-segel-forced-flux']]);
 assert.deepEqual(goal.supplemental_examples,biology.supplemental_examples);
 assert.deepEqual(goal.scope,biology.scope);
 assert.deepEqual(goal.resources.find(x=>x.id==='bio-patterns').supplemental_examples,[...shared,'reaction-diffusion-splitting']);
 assert.equal(goal.resources.find(x=>x.id==='bio-excitation').status,'reading-only');
 const survey=json('numerical-methods-atlas/assets/biological-models.json').models;
 assert.equal(survey.length,22);
 const earlier=['logistic','sir','turing','schnakenberg','fitzhugh-nagumo','enzyme','lotka-volterra'],added=['hodgkin-huxley','fisher-kpp','keller-segel','chemical-master'];
 assert.deepEqual(new Set(survey.filter(x=>x.status==='scoped-educational-example').map(x=>x.id)),new Set([...earlier,...added]));
 const equations=json('catalog/atlas-equations.json').equations;
 assert.equal(equations.length,equationCount);
 assert.equal(equations.filter(x=>!['rotational-advection','shallow-water-bed','forced-incompressible','level-set-advection', 'forced-vorticity', 'boussinesq-buoyancy', 'ale-scalar-transport', 'linear-rotating-shallow-water', 'variable-viscosity-vector', 'srmhd', 'srhd','tensor-diffusion','coulomb-electrostatics','vlasov-poisson','hard-sphere-boltzmann','bio-enzyme','bio-lotka-volterra',...equationsAddedAfterBatch37].includes(x.id)&&!['bio-hodgkin-huxley','bio-fisher-kpp','bio-keller-segel','bio-chemical-master'].includes(x.id)&&x.status==='local-example').length,23);
 for(const id of ['turing','schnakenberg']){
  const model=survey.find(x=>x.id===id),equation=equations.find(x=>x.id==='bio-'+id);
  const selected=id==='turing'?shared:[...shared,'schnakenberg-2d-boundary-modes'];
  assert.deepEqual(model.supplemental_examples,selected);
  assert.deepEqual(equation.supplemental_examples,selected);
  assert.deepEqual(model.implementation_scope,equation.execution_scope);
  if(id==='turing')assert.deepEqual(equation.execution_scope,biology.schnakenberg_scope);
  else assert.ok(equation.execution_scope.ja&&equation.execution_scope.en);
 }
 assert.deepEqual(survey.find(x=>x.id==='fitzhugh-nagumo').supplemental_examples,['fitzhugh-nagumo']);
 for(const id of added){const equation=equations.find(x=>x.id==='bio-'+id),model=survey.find(x=>x.id===id);assert.equal(equation.status,'local-example');assert.deepEqual(model.supplemental_examples,equation.supplemental_examples);assert.deepEqual(model.implementation_scope,equation.execution_scope);}
 assert.equal(equations.find(x=>x.id==='bio-gray-scott').status,'reading');
 assert.match(biology.reference.en,/independent dealiased Fourier/);
 assert.match(biology.reference.en,/same finite-difference semidiscretization/);
 assert.match(biology.refinement.en,/implicit-midpoint/);
 assert.match(biology.next.en,/reflection-symmetric/);
 assert.equal(json('catalog/atlas-test-problems.json').problems.length,problemCount);
});

test('nonlinear reaction-diffusion remains component evidence and cannot certify the transport bridge',()=>{
 const route=json('catalog/atlas-crossovers.json').routes.find(x=>x.id==='reaction-transport');
 for(const id of ['reaction-diffusion','biological-fronts']){
  const stage=route.stages.find(x=>x.id===id);
  for(const caseID of cases)assert.ok(stage.supplemental_ids.includes(caseID));
  assert.ok(stage.method_ids.includes('centered-difference')&&stage.method_ids.includes('implicit-midpoint'));
  assert.equal(stage.supplemental_role,'scoped-component');
  for(const lang of ['ja','en'])assert.ok(stage.reading.some(x=>x.url[lang]===`/numerical-methods-atlas/${lang}/read/validation-biology/`));
 }
 for(const item of [route,...route.connections]){
  assert.equal(item.coupled_validation.status,'not-executed');
  assert.deepEqual(item.coupled_validation.example_ids,[]);
  assert.deepEqual(item.coupled_validation.supplemental_ids||[],[]);
 }
 assert.match(route.stages.find(x=>x.id==='biological-fronts').gap.en,/Fisher front speeds/);
 assert.match(route.stages.find(x=>x.id==='biological-fronts').supplemental_scope.en,/zero-dimensional/);
});

test('survey overlays refresh both languages idempotently and replace the old wrapped survey-only claim',()=>{
 const source=String.raw`
import ast,html,json,pathlib,re,sys
root=pathlib.Path.cwd();sys.path.insert(0,'scripts')
from atlas_goal_availability import load_supplemental_examples
tree=ast.parse((root/'scripts/build-atlas-depth.py').read_text())
function=next(x for x in ast.walk(tree) if isinstance(x,ast.FunctionDef) and x.name=='adapt')
biology=next(x for x in json.loads((root/'catalog/atlas-depth.json').read_text())['fields'] if x['id']=='biology')
supplements={x['id']:x for x in load_supplemental_examples(root,biology['supplemental_examples'])}
link_function=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='link')
for lang in ['ja','en']:
 notice='<aside id="biological-execution-scope">managed notice</aside>'
 scope={'re':re,'e':html.escape,'biology':biology,'lang':lang,'notice':notice,'supplements':supplements}
 exec(compile(ast.Module(body=[link_function,function],type_ignores=[]),'survey-overlay','exec'),scope)
 adapt=scope['adapt']
 for original in [json.loads((root/f'numerical-methods-atlas/content.{lang}.json').read_text())['biological-models']['html'],(root/f'numerical-methods-atlas/{lang}/read/biological-models/index.html').read_text()]:
  once=adapt(original);twice=adapt(once)
  assert once==twice,lang+' overlay must be idempotent'
  assert once.count('id="biological-execution-scope"')==1
  assert html.escape(biology['scope'][lang]) in once
  assert not re.search(r'All\s+22\s+entries are literature and proposed',once)
  assert 'Finite-amplitude nonlinear evolution' in once if lang=='en' else '有限振幅の非線形発展' in once
  for anchor in ['09-1952-turing-reactiondiffusion-framework','10-1961-fitzhughnagumo-excitation-and-recovery','17-1979-schnakenberg-reactiondiffusion']:
   assert once.count('id="'+anchor+'"')==original.count('id="'+anchor+'"')==1
`;
 execFileSync('python3',['-B','-c',source],{cwd:root,encoding:'utf8',timeout:30000});
});


test('canonical biology overlays preserve old sources and reject wrong fixed-case ownership',()=>{
 const result=JSON.parse(execFileSync('python3',['-B','-c',String.raw`
import ast,copy,json,pathlib,sys
root=pathlib.Path.cwd();sys.path.insert(0,'scripts')
from atlas_goal_availability import load_supplemental_examples
ns={};tree=ast.parse((root/'scripts/atlas_biology_model_evidence.py').read_text())
functions=[x for x in tree.body if isinstance(x,ast.FunctionDef)]
exec(compile(ast.Module(body=functions,type_ignores=[]),'biology-overlay-functions-only','exec'),ns)
data=json.loads((root/'catalog/atlas-depth.json').read_text());biology=next(x for x in data['fields'] if x['id']=='biology')
equations=json.loads((root/'catalog/atlas-equations.json').read_text())['equations'];bindings=json.loads((root/'catalog/atlas-depth-expansion.json').read_text())['case_equations']
examples={x['id']:x for x in json.loads((root/'numerical-methods-atlas/code-and-data/examples.json').read_text())['examples']}
supplements={x['id']:x for x in load_supplemental_examples(root,biology['supplemental_examples'])}
survey=json.loads((root/'numerical-methods-atlas/assets/biological-models.json').read_text())
old,new=ns['apply_biology_model_evidence'],ns['apply_canonical_biology_supplements']
old(survey,biology,examples,supplements,data['reviewed_on']);before=copy.deepcopy(survey);new(survey,biology,equations,supplements,bindings)
models={x['id']:x for x in survey['models']};equation_by_id={x['id']:x for x in equations}
expected={'logistic','sir','turing','schnakenberg','fitzhugh-nagumo','enzyme','lotka-volterra','hodgkin-huxley','fisher-kpp','keller-segel','chemical-master'}
assert {x['id'] for x in survey['models'] if x['status']=='scoped-educational-example'}==expected
for ident in ['enzyme','lotka-volterra']:
 previous=next(x for x in before['models'] if x['id']==ident);assert models[ident]==previous
assert models['turing']==next(x for x in before['models'] if x['id']=='turing')
assert models['schnakenberg']['supplemental_examples']==['turing-schnakenberg','schnakenberg-nonlinear','schnakenberg-pattern','schnakenberg-2d-boundary-modes']
for ident in ['hodgkin-huxley','fisher-kpp','keller-segel','chemical-master','schnakenberg']:
 equation=equation_by_id['bio-'+ident];assert models[ident]['implementation_scope']==equation['execution_scope'];assert models[ident]['supplemental_examples']==equation['supplemental_examples']
 assert all(models[ident]['implementation_scope'][l] for l in ['ja','en'])
first=copy.deepcopy(survey);old(survey,biology,examples,supplements,data['reviewed_on']);new(survey,biology,equations,supplements,bindings);assert survey==first
negative=0
for mode in ['wrong-owner','missing-language','wrong-group','inflate-old-enzyme']:
 s,b,e,sp,ce=copy.deepcopy(before),copy.deepcopy(biology),copy.deepcopy(equations),copy.deepcopy(supplements),copy.deepcopy(bindings)
 if mode=='wrong-owner':ce['hodgkin-huxley-controls']['ids']=['bio-gray-scott']
 elif mode=='missing-language':next(x for x in e if x['id']=='bio-fisher-kpp')['execution_scope'].pop('en')
 elif mode=='wrong-group':sp['hodgkin-huxley-controls']['group']='small-models'
 else:next(x for x in e if x['id']=='bio-enzyme')['execution_scope']['en']+=' broadened'
 try:new(s,b,e,sp,ce)
 except AssertionError:negative+=1
 else:raise AssertionError('Invalid biology overlay accepted: '+mode)
print(json.dumps({'passed':True,'models':len(expected),'negative':negative,'scientific_execution':False}))
`],{cwd:root,encoding:'utf8',timeout:30000}));
 assert.deepEqual(result,{passed:true,models:11,negative:4,scientific_execution:false});
});
