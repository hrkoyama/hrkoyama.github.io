import {examplesAddedAfterBatch37} from './fixtures/atlas-inventory.mjs';
import {equationCount} from './fixtures/atlas-inventory.mjs';
import {methodCount,methodStatusCounts} from './fixtures/atlas-inventory.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';

const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root),'utf8');
const json=p=>JSON.parse(read(p));
const examples=['gaussian-mcmc','mcmc-multimodal-mixing','mcmc-diagnostic-reference'];

test('MCMC preserves its four historical sections and distinguishes poor mixing from passing diagnostic checks',()=>{
 const chapter=json('catalog/atlas-detailed-reading.json').chapters.find(x=>x.id==='mcmc');
 assert.deepEqual(chapter.sections.map(x=>x.id),['model','algorithm','conditions','verification']);
 assert.deepEqual(chapter.sections.flatMap(x=>x.formulas||[]),['mcmc-1']);
 assert.deepEqual(chapter.scoped_supplements,examples);
 const english=chapter.sections.flatMap(x=>x.paragraphs.en).join(' ');
 assert.match(english,/every chain starting in the same mode/);
 assert.match(english,/R-hat near one/);
 assert.match(english,/does not mean estimation succeeded/);
 assert.match(english,/false-positive rates/);
 assert.match(english,/right-mode indicator/);
 assert.match(english,/rank-normalized split\/folded R-hat/);
 assert.match(english,/independent ArviZ 0.20 execution/);
 const depth=json('catalog/atlas-depth.json').fields.find(x=>x.id==='probability');
 const goal=json('catalog/atlas-goals.json').goals.find(x=>x.id==='stochastic-calculation');
 const ssaId='immigration-death-ssa';
 assert.deepEqual(depth.supplemental_examples.filter(id=>!examplesAddedAfterBatch37.includes(id)&&id!==ssaId),examples);
 assert.deepEqual(depth.supplemental_examples.filter(id=>id===ssaId),[ssaId]);
 assert.deepEqual(goal.supplemental_examples.filter(id=>id!==ssaId),examples);
 assert.deepEqual(goal.supplemental_examples,[...examples,ssaId]);
 assert.deepEqual(depth.scope,goal.scope);
 assert.deepEqual(depth.examples,['mc-integral','gbm-sde']);
 assert.deepEqual(goal.methods.filter(id=>id!=='gillespie-ssa'),['monte-carlo','sde','mcmc']);
 assert.deepEqual(goal.methods,['monte-carlo','sde','mcmc','gillespie-ssa']);
 const ssaCase=json('code/validated-examples/2026-11-25/biology-ode-controls/cases.json').find(x=>x.id===ssaId);
 assert.deepEqual(ssaCase.method_ids,['gillespie-ssa']);
 assert.equal(json('catalog/atlas-equations.json').equations.length,equationCount);
 const methods=json('catalog/atlas-methods.json').methods;
 assert.equal(methods.length,methodCount);
 assert.equal(methods.filter(x=>x.status==='educational-example').length,methodStatusCounts['educational-example']);
 assert.equal(methods.filter(x=>x.status==='planned').length,methodStatusCounts.planned);
});

test('new MCMC reading belongs in the stochastic contents while thermostat coupling evidence stays separate',()=>{
 const index=json('catalog/atlas-reading-index.json');
 const group=index.groups.find(x=>x.id==='stochastic-models').chapters;
 assert.equal(group[group.indexOf('mcmc')+1],'validation-mcmc');
 assert.equal(index.groups.flatMap(x=>x.chapters).filter(x=>x==='validation-mcmc').length,1);
 const cross=json('catalog/atlas-crossovers.json');
 const sampling=cross.math_families.find(x=>x.id==='probability-sampling');
 for(const lang of ['ja','en'])for(const chapter of ['thermostats','mcmc','validation-mcmc'])assert.ok(sampling.reading.some(x=>x.url[lang]===`/numerical-methods-atlas/${lang}/read/${chapter}/`));
 assert.match(sampling.summary.en,/do not establish MD\/thermostat coupling/);
 for(const route of cross.routes){
  for(const stage of route.stages)assert.ok(!(stage.supplemental_ids||[]).some(x=>x.startsWith('mcmc-')));
  for(const item of [route,...route.connections])assert.ok(!(item.coupled_validation.supplemental_ids||[]).some(x=>x.startsWith('mcmc-')));
 }
});

test('optional scoped-supplement rendering preserves edition-specific links in HTML and Markdown and labels diagnostic non-addition',()=>{
 const source=String.raw`
import ast,html,pathlib
tree=ast.parse(pathlib.Path('scripts/build-atlas-detailed-reading.py').read_text())
names={'link','heading','paragraph','scoped_supplement_html','scoped_supplement_markdown'}
functions=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in names]
assert {x.name for x in functions}==names
scope={'escape':html.escape}
exec(compile(ast.Module(body=functions,type_ignores=[]),'scoped-reading-renderer','exec'),scope)
cases=[]
for ident,group,problem in [('gaussian-mcmc','models','gaussian-mcmc'),('mcmc-multimodal-mixing','mcmc','mcmc-bimodal-mixture'),('mcmc-diagnostic-reference','mcmc',None)]:
 base='https://hrkoyama.github.io/code/test-fixture/'+group+'/'
 cases.append({'id':ident,'problem_id':problem,'title':{'ja':'例<'+ident+'>','en':'Example<'+ident+'>'},'summary':{'ja':'範囲&対照','en':'Scope&control'},'limits':{'ja':'固定条件だけ','en':'Fixed conditions only'},'url':'/numerical-methods-atlas/validation/'+ident+'/', 'reading':{lang:'/numerical-methods-atlas/'+lang+'/read/validation-'+group+'/#'+ident for lang in ['ja','en']},'code_urls':[base+'example.py'],'test_urls':[base+'test_example.py'],'download':base+'example.zip','results':base+'result.json','verification':base+'verification.json'})
for lang in ['ja','en']:
 rendered=scope['scoped_supplement_html'](cases,lang);markdown=scope['scoped_supplement_markdown'](cases,lang)
 assert scope['scoped_supplement_html']([],lang)==scope['scoped_supplement_markdown']([],lang)==''
 assert rendered.count('id="scoped-examples"')==1 and rendered.count('<h3>')==3
 assert '&lt;' in rendered and '&amp;' in rendered
 assert ('物理問題数へ非加算' if lang=='ja' else 'no additional physical problem') in rendered
 assert ('物理問題数へ非加算' if lang=='ja' else 'no physical-problem increment') in markdown
 for case in cases:
  assert case['url']+'?lang='+lang in rendered and case['url']+'?lang='+lang in markdown
  for target in [case['reading'][lang],*case['code_urls'],*case['test_urls'],case['download'],case['results'],case['verification']]:assert target in rendered and target in markdown
`;
 execFileSync('python3',['-B','-c',source],{cwd:root,encoding:'utf8',timeout:30000});
});

test('the actual builder initializes a missing problem binding on the real historical Gaussian record',()=>{
 const source=String.raw`
import ast,hashlib,json,pathlib,sys
from unittest import mock
root=pathlib.Path.cwd();sys.path.insert(0,'scripts')
from atlas_goal_availability import load_supplemental_examples
config_path=root/'catalog/atlas-depth-expansion.json'
original_read=pathlib.Path.read_text
def legacy_groups(path,*args,**kwargs):
 text=original_read(path,*args,**kwargs)
 if path.resolve()==config_path:
  config=json.loads(text);config['groups']=[x for x in config['groups'] if x['id']=='models'];return json.dumps(config)
 return text
# Resolve an actual unchanged archive/receipt; no unfinished release is needed.
with mock.patch.object(pathlib.Path,'read_text',legacy_groups):
 cases=load_supplemental_examples(root,['gaussian-mcmc'])
case=cases[0];assert case['group']=='models'
assert 'problem_id' not in case
tree=ast.parse((root/'scripts/build-atlas-detailed-reading.py').read_text())
loop=next(x for x in tree.body if isinstance(x,ast.For) and isinstance(x.target,ast.Name) and x.target.id=='chapter')
initialization=next(x for x in loop.body if isinstance(x,ast.If) and isinstance(x.test,ast.Name) and x.test.id=='scoped')
scope={'ROOT':root,'json':json,'hashlib':hashlib,'scoped':cases}
exec(compile(ast.Module(body=[initialization],type_ignores=[]),'actual-scoped-initialization','exec'),scope)
record=scope['scoped_fields']['scoped_supplements'][0]
assert record['problem_id']=='gaussian-mcmc' and record['id']=='gaussian-mcmc'
assert record['code_urls']==case['code_urls'] and record['test_urls']==case['test_urls']
assert record['group']=='models'
assert scope['scoped_fields']['supplemental_source_sha256']['catalog/atlas-depth-expansion.json']==hashlib.sha256(config_path.read_bytes()).hexdigest()
`;
 execFileSync('python3',['-B','-c',source],{cwd:root,encoding:'utf8',timeout:30000});
});
