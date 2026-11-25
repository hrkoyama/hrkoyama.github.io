import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';

const root=new URL('../',import.meta.url);
const read=path=>readFileSync(new URL(path,root),'utf8');
const json=path=>JSON.parse(read(path));
const comparison=json('catalog/atlas-thermostat-comparison.json');
const expected=['csvr-kinetic-kernel','csvr-langevin-harmonic','csvr-langevin-quartic'];
const origin='https://hrkoyama.github.io';

test('adopted CSVR formulas render offline and identify the signed original update and author correction',()=>{
 assert.deepEqual(comparison.case_ids,expected);
 const records=Object.entries(comparison.formulas).map(([id,formula])=>({id,formula:[formula]}));
 const rendered=JSON.parse(execFileSync('node',['scripts/render-atlas-math.cjs'],{cwd:root,input:JSON.stringify(records),encoding:'utf8'}));
 assert.equal(Object.keys(rendered.rendered).length,8);
 for(const [id,html] of Object.entries(rendered.rendered))assert.match(html[0],/class="katex"/,id);
 assert.match(comparison.formulas['csvr-sign'],/operatorname\{sign\}/);
 assert.match(comparison.formulas['csvr-matched'],/2\\gamma/);
 assert.equal(comparison.references.find(x=>x.id==='bussi2008localglobal').doi,'10.1016/j.cpc.2008.01.006');
 assert.ok(comparison.references.some(x=>x.id==='bussi-csvr-author-algorithms'));
 for(const source of comparison.references)for(const lang of ['ja','en'])assert.ok(source.review_note[lang]);
});

for(const lang of ['ja','en'])test(`published ${lang} reading keeps equations, review limits and immutable evidence synchronized`,()=>{
 const base=`numerical-methods-atlas/${lang}/read/thermostats/`;
 const page=read(base+'index.html'),markdown=read(base+'index.md'),data=json(base+'index.json');
 assert.equal(data.comparison_enabled,true);
 const other=lang==='ja'?'en':'ja';
 assert.ok(page.includes(`href="/numerical-methods-atlas/${other}/read/thermostats/?lang=${other}" hreflang="${other}"`),'body language switch retains its target language through shared navigation');
 assert.deepEqual(data.case_ids,['langevin-harmonic',...expected,'two-state-bo-cp-ou','deterministic-thermostat-contrasts','projected-canonical-dof']);
 assert.deepEqual(new Set(data.implemented_method_ids),new Set(['langevin-thermostat','stochastic-velocity-rescaling','velocity-rescaling','berendsen-thermostat','nose-hoover','nose-hoover-chains']));
 assert.equal(data.planned_method_ids.length,6);
 assert.deepEqual(data.comparison,comparison);
 assert.ok(page.includes('id="deterministic-fixed-contrasts"'));
 assert.ok(page.includes('data-thermostat-case="deterministic-thermostat-contrasts"'));
 const separate=data.supplements.find(item=>item.id==='deterministic-thermostat-contrasts');
 for(const key of ['assumptions','validation','limits'])assert.ok(markdown.includes(separate[key][lang]));
 for(const id of Object.keys(comparison.formulas))assert.ok(page.includes(`data-equation-id="${id}"`));
 for(const section of comparison.sections){
  assert.ok(page.includes(`id="${section.id}"`));
  for(const paragraph of section.paragraphs[lang])assert.ok(markdown.includes(paragraph));
 }
 assert.ok(markdown.includes(comparison.verification[lang]));
 assert.ok(markdown.includes(comparison.source_scope[lang]));
 assert.match(page,/Kolmogorov/);
 assert.match(page,/BAOAB/);assert.match(page,/OBABO/);
 assert.match(page,lang==='ja'?/独立レプリカ/:/independent replicas/);
 for(const anchor of ['temperature','fluctuations','dynamics','executed-scope','basic','advanced','verification','source-scope'])assert.ok(page.includes(`id="${anchor}"`));
 for(const item of data.supplements){
  for(const key of ['url','download','results','verification']){
   assert.ok(item[key].startsWith('/'),`${item.id} ${key}`);
   assert.ok(page.includes(item[key]));
   assert.ok(markdown.includes(origin+item[key]));
  }
 }
 for(const [path,expectedHash] of Object.entries(data.source_sha256)){
  const actual=createHash('sha256').update(readFileSync(new URL(path,root))).digest('hex');
  assert.equal(actual,expectedHash,path);
 }
 assert.ok(!page.includes('他の11手法'));
 assert.ok(!page.includes('other 11 methods'));
 assert.ok(!page.includes('Full equation audits and numerical reproductions have not been performed.'));
});

test('fixed deterministic thermostat promotion requires exact qualified case, release and limits',()=>{
 const program=String.raw`
import ast,copy,html,json,pathlib,sys
sys.path.insert(0,'scripts')
from atlas_goal_availability import load_supplemental_examples
root=pathlib.Path.cwd()
tree=ast.parse(pathlib.Path('scripts/build-thermostat-reading.py').read_text())
functions=[row for row in tree.body if isinstance(row,ast.FunctionDef) and row.name in ['qualified_deterministic_thermostats','deterministic_section']]
assert len(functions)==2
namespace={'esc':html.escape};exec(compile(ast.Module(body=functions,type_ignores=[]),'<pure thermostat guards>','exec'),namespace)
methods=[row for row in json.loads((root/'catalog/atlas-methods.json').read_text())['methods'] if row['group']['id']=='thermostats']
field=next(row for row in json.loads((root/'catalog/atlas-depth.json').read_text())['fields'] if row['id']=='temperature')
supplements=load_supplemental_examples(root,field['supplemental_examples'])
guard=namespace['qualified_deterministic_thermostats'];case=guard(methods,supplements)
assert case['id']=='deterministic-thermostat-contrasts'
for lang in ['ja','en']:
 rendered=namespace['deterministic_section'](case,methods,lang)
 assert case['url']+'?lang='+lang in rendered
 for key in ['assumptions','validation','limits']:assert html.escape(case[key][lang]) in rendered
additional={'velocity-rescaling','berendsen-thermostat','nose-hoover','nose-hoover-chains'}
old=copy.deepcopy(methods)
for method in old:
 if method['id'] in additional:method['status']='planned'
assert guard(old,[row for row in supplements if row['id']!=case['id']]) is None
assert namespace['deterministic_section'](None,methods,'en')==''
def reject(mutate):
 m,c=copy.deepcopy(methods),copy.deepcopy(supplements);mutate(m,c)
 try:guard(m,c)
 except (AssertionError,KeyError):return
 raise AssertionError('Unqualified thermostat evidence accepted')
def chosen(c):return next(row for row in c if row['id']==case['id'])
reject(lambda m,c:c.remove(chosen(c)))
reject(lambda m,c:chosen(c).update(group='thermostats'))
reject(lambda m,c:chosen(c).update(method_ids=['langevin-thermostat']))
reject(lambda m,c:next(row for row in m if row['id']=='nose-hoover')['depth_release'].update(case_ids=['langevin-harmonic']))
reject(lambda m,c:next(row for row in m if row['id']=='andersen-thermostat').update(status='educational-example'))
reject(lambda m,c:next(row for row in m if row['id']=='nose-hoover')['supplemental_scope_profiles'][0]['limits'][0].update(en='General ergodicity is proved'))
reject(lambda m,c:chosen(c)['source_sha256'].pop('code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json'))
reject(lambda m,c:c.append(copy.deepcopy(chosen(c))))
reject(lambda m,c:chosen(c)['assumptions'].pop('ja'))
print('qualified deterministic thermostat scope and nine negative controls passed')
`;
 assert.match(execFileSync('python3',['-B','-c',program],{cwd:root,encoding:'utf8',timeout:30000}),/nine negative controls passed/);
});
