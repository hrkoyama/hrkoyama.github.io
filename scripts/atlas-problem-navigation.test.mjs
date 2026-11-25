import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';

const root=new URL('../',import.meta.url);
const read=path=>readFileSync(new URL(path,root),'utf8');
const sha=path=>createHash('sha256').update(readFileSync(new URL(path,root))).digest('hex');
let actual;
function renderChoices(){
  if(actual)return actual;
  const program=String.raw`
import copy,importlib.util,json,sys
from pathlib import Path
from urllib.parse import urlsplit
sys.path.insert(0,'scripts')
from atlas_execution_navigation import PROBLEM_EXECUTION_CHOICES,problem_execution_choices,render_problem_execution_choices,problem_figure_case
spec=importlib.util.spec_from_file_location('problem_page_renderer','scripts/build-atlas-problems.py')
page_renderer=importlib.util.module_from_spec(spec);spec.loader.exec_module(page_renderer)
problems=json.loads(Path('numerical-methods-atlas/problems/index.json').read_bytes())['problems']
needed={ident for groups in PROBLEM_EXECUTION_CHOICES.values() for _,_,_,pairs in groups for _,ident in pairs}
routes={}
for problem in problems:
    for execution in problem['executions']:
        if execution['id'] in needed:
            path=Path(urlsplit(execution['guide']['en']).path.lstrip('/'))/'index.json'
            routes[execution['id']]=json.loads(path.read_bytes())['execution_navigation']
before=json.dumps(problems,sort_keys=True)
rows={}
for ident in ['bratu','noh']:
    groups=problem_execution_choices(ident,problems,routes)
    problem=next(p for p in problems if p['id']==ident)
    rows[ident]={'purposes':[g['purpose'] for g in groups],
                 'ids':[[c['execution']['id'] for c in g['cases']] for g in groups],
                 'hero':problem_figure_case(problem,groups)['id'],
                 'html':{lang:render_problem_execution_choices(ident,groups,lang) for lang in ['ja','en']},
                 'bundles':[{**{k:c['execution'][k] for k in ['id','guide','input','download','manifest','verification']},
                             'edition':c['edition'],'figure':c['route']['figure']['url'],
                             'references':c['route']['references']['url']} for g in groups for c in g['cases']]}
    rows[ident]['page_order']={}
    for lang in ['ja','en']:
        html=page_renderer.section(problem,lang,{},groups)
        rows[ident]['page_order'][lang]=(html.index('class="problem-hero"')<html.index('class="problem-actions problem-reading"')<html.index('data-problem-case-picker=')<html.index('data-problem-section="equations"'))
negative=[]
def rejects(label,ps,rs):
    try: problem_execution_choices('noh',ps,rs)
    except (KeyError,ValueError): negative.append(label)
    else: raise AssertionError('Accepted wrong picker ownership: '+label)
changed=dict(routes);changed['noh-shock']=routes['noh-cartesian-2d'];rejects('wrong-route-case',problems,changed)
changed=dict(routes);bad=copy.deepcopy(routes['noh-shock']);bad['figure']=routes['noh-cartesian-2d']['figure'];changed['noh-shock']=bad;rejects('wrong-case-figure',problems,changed)
changed=dict(routes);bad=copy.deepcopy(routes['noh-shock']);bad['references']=routes['noh-cartesian-2d']['references'];changed['noh-shock']=bad;rejects('wrong-case-reference',problems,changed)
bad=copy.deepcopy(next(p for p in problems if p['id']=='noh'));bad['executions'][0]['input']=bad['executions'][1]['input'];rejects('mixed-input-edition',[bad if p['id']=='noh' else p for p in problems],routes)
rejects('duplicate-problem',problems+[problems[0]],routes)
assert before==json.dumps(problems,sort_keys=True)
assert problem_execution_choices('sod',problems,routes)==[]
assert render_problem_execution_choices('sod',[],'ja')==''
print(json.dumps({'rows':rows,'negative':negative,'scientific_records_unchanged':True}))
`;
  actual=JSON.parse(execFileSync('python3',['-B','-c',program],{
    cwd:fileURLToPath(root),encoding:'utf8',timeout:10000,maxBuffer:2*1024*1024,
    env:{...process.env,PYTHONDONTWRITEBYTECODE:'1',PYTHONNOUSERSITE:'1'},
  }));
  return actual;
}

test('purpose-first Bratu and Noh choices keep exact execution, image, input and reference ownership',()=>{
  const value=renderChoices();
  assert.deepEqual(value.rows.bratu.purposes,['forward','sensitivity','inverse']);
  assert.deepEqual(value.rows.bratu.ids,[['bratu','bratu-fold-continuation','bratu-matrix-free-jfnk'],['bratu-fold-sensitivity','bratu-distributed-vjp'],['bratu-gn-lm-bounds','bratu-noise-regularization']]);
  assert.deepEqual(value.rows.noh.purposes,['radial-1d','cartesian-2d']);
  assert.deepEqual(value.rows.noh.ids,[['noh-shock'],['noh-cartesian-2d']]);
  assert.equal(value.rows.bratu.hero,'bratu');
  assert.equal(value.rows.noh.hero,'noh-cartesian-2d');
  for(const row of Object.values(value.rows))for(const lang of ['ja','en']){
    const html=row.html[lang];
    assert.equal(row.page_order[lang],true,'the picture and primary reading actions precede the compact picker');
    assert.ok(html.indexOf('data-execution-purpose=')<html.indexOf('problem-choice-edition'));
    for(const bundle of row.bundles){
      const card=html.split(`<article class="problem-choice-card" data-execution-case="${bundle.id}"`)[1]?.split('</article>')[0];
      assert.ok(card,bundle.id+' has its own card');
      for(const url of [bundle.guide[lang],bundle.input,bundle.download,bundle.manifest,bundle.verification,bundle.references[lang],bundle.figure])assert.ok(card.includes(url.replaceAll('&','&amp;')),bundle.id+' preserves '+url);
      assert.ok(card.includes(bundle.edition));
      assert.ok(card.indexOf('problem-choice-scope')<card.indexOf('problem-choice-edition'));
      assert.ok(card.includes('data-execution-action="figure"'));
      assert.ok(card.includes('data-execution-action="guide"'));
    }
  }
  assert.ok(value.rows.noh.html.en.includes('One coordinate: planar, cylindrical or spherical symmetry'));
  assert.ok(value.rows.noh.html.en.includes('2D Cartesian · full square'));
  assert.ok(value.rows.bratu.html.en.includes('A representative figure for the problem.'));
  for(const purpose of ['forward','sensitivity','inverse'])assert.ok(value.rows.bratu.html.en.includes(`data-execution-purpose="${purpose}"><summary>`));
  assert.ok(value.rows.noh.html.en.includes('data-execution-purpose="radial-1d"><summary>'));
  assert.ok(value.rows.noh.html.en.includes('data-execution-purpose="cartesian-2d" open><summary>'));
  assert.equal(value.scientific_records_unchanged,true);
});

test('problem choices reject mixed cases, figures, references and input editions without changing other problem pages',()=>{
  assert.deepEqual(renderChoices().negative,['wrong-route-case','wrong-case-figure','wrong-case-reference','mixed-input-edition','duplicate-problem']);
});

test('generated Bratu and Noh hubs expose the picker while retaining existing resource sections and machine records',()=>{
  const css=sha('numerical-methods-atlas/styles/atlas-execution-navigation.css').slice(0,12);
  for(const id of ['bratu','noh']){
    const html=read(`numerical-methods-atlas/problems/${id}/index.html`);
    assert.equal((html.match(new RegExp(`data-problem-case-picker="${id}"`,'g'))||[]).length,2);
    assert.ok(html.includes(`/numerical-methods-atlas/styles/atlas-execution-navigation.css?v=${css}`));
    for(const lang of ['ja','en'])for(const section of ['equations','references','methods','code'])assert.ok(html.includes(`id="${section}-${lang}"`));
    const figureCase=id==='bratu'?'bratu':'noh-cartesian-2d';
    assert.equal((html.match(new RegExp(`data-problem-figure-case="${figureCase}"`,'g'))||[]).length,2);
    assert.ok(html.includes('Open full-size image'));
    const data=JSON.parse(read(`numerical-methods-atlas/problems/${id}/index.json`));
    assert.ok(!Object.hasOwn(data,'execution_choices'),'presentation does not alter the problem JSON schema');
    assert.deepEqual(data.executions.map(row=>row.id),id==='bratu'?['bratu']:['noh-shock','noh-cartesian-2d']);
    const markdown=read(`numerical-methods-atlas/problems/${id}/index.md`);
    assert.ok(!markdown.includes('data-problem-case-picker'));
  }
});
