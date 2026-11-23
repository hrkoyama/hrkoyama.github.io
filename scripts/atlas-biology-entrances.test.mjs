import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';

const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root),'utf8');
const json=p=>JSON.parse(read(p));
const cases=['schnakenberg-nonlinear','schnakenberg-pattern'];
const shared=['turing-schnakenberg',...cases];

test('the two new nonlinear cases deepen the existing biological scope without promoting other model families',()=>{
 const biology=json('catalog/atlas-depth.json').fields.find(x=>x.id==='biology');
 const goal=json('catalog/atlas-goals.json').goals.find(x=>x.id==='biological-models');
 assert.deepEqual(biology.examples,['logistic-growth','sir-epidemic']);
 assert.deepEqual(biology.supplemental_examples,['reaction-diffusion-fourier','turing-schnakenberg','fitzhugh-nagumo',...cases,'reaction-diffusion-splitting']);
 assert.deepEqual(goal.supplemental_examples,biology.supplemental_examples);
 assert.deepEqual(goal.scope,biology.scope);
 assert.deepEqual(goal.resources.find(x=>x.id==='bio-patterns').supplemental_examples,[...shared,'reaction-diffusion-splitting']);
 assert.equal(goal.resources.find(x=>x.id==='bio-excitation').status,'reading-only');
 const survey=json('numerical-methods-atlas/assets/biological-models.json').models;
 assert.equal(survey.length,22);
 assert.equal(survey.filter(x=>x.status==='scoped-educational-example').length,5);
 const equations=json('catalog/atlas-equations.json').equations;
 assert.equal(equations.length,49);
 assert.equal(equations.filter(x=>!['rotational-advection','shallow-water-bed','forced-incompressible'].includes(x.id)&&x.status==='local-example').length,23);
 for(const id of ['turing','schnakenberg']){
  const model=survey.find(x=>x.id===id),equation=equations.find(x=>x.id==='bio-'+id);
  assert.deepEqual(model.supplemental_examples,shared);
  assert.deepEqual(equation.supplemental_examples,shared);
  assert.deepEqual(model.implementation_scope,biology.schnakenberg_scope);
  assert.deepEqual(equation.execution_scope,biology.schnakenberg_scope);
 }
 assert.deepEqual(survey.find(x=>x.id==='fitzhugh-nagumo').supplemental_examples,['fitzhugh-nagumo']);
 for(const id of ['hodgkin-huxley','gray-scott','fisher-kpp'])assert.equal(equations.find(x=>x.id==='bio-'+id).status,'reading');
 assert.match(biology.reference.en,/independent dealiased Fourier/);
 assert.match(biology.reference.en,/same finite-difference semidiscretization/);
 assert.match(biology.refinement.en,/implicit-midpoint/);
 assert.match(biology.next.en,/reflection-symmetric/);
 assert.equal(json('catalog/atlas-test-problems.json').problems.length,91);
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
import ast,html,json,pathlib,re
root=pathlib.Path.cwd()
tree=ast.parse((root/'scripts/build-atlas-depth.py').read_text())
function=next(x for x in ast.walk(tree) if isinstance(x,ast.FunctionDef) and x.name=='adapt')
biology=next(x for x in json.loads((root/'catalog/atlas-depth.json').read_text())['fields'] if x['id']=='biology')
for lang in ['ja','en']:
 notice='<aside id="biological-execution-scope">managed notice</aside>'
 scope={'re':re,'e':html.escape,'biology':biology,'lang':lang,'notice':notice}
 exec(compile(ast.Module(body=[function],type_ignores=[]),'survey-overlay','exec'),scope)
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
