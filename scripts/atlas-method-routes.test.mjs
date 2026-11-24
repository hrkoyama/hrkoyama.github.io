import test from 'node:test';
import assert from 'node:assert/strict';
import {existsSync,readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const root=new URL('../',import.meta.url),origin='https://hrkoyama.github.io';
const read=path=>readFileSync(new URL(path,root),'utf8'),json=path=>JSON.parse(read(path));
const sha=path=>createHash('sha256').update(readFileSync(new URL(path,root))).digest('hex');
const decode=value=>value.replaceAll('&amp;','&').replaceAll('&quot;','"').replaceAll('&#x27;',"'").replaceAll('&#39;',"'").replaceAll('&lt;','<').replaceAll('&gt;','>');
const text=html=>decode(html.replace(/<[^>]+>/g,'')).replace(/\s+/g,' ').trim();
const attrs=tag=>Object.fromEntries([...tag.matchAll(/([\w:-]+)="([^"]*)"/g)].map(match=>[match[1],decode(match[2])]));
const byId=rows=>new Map(rows.map(row=>[row.id,row]));
const catalog=json('catalog/atlas-problem-links.json'),methodSource=json('catalog/atlas-methods.json').methods;
const sourceMethods=byId(methodSource),sourceProblems=byId(catalog.problems);
const problems=byId(json('numerical-methods-atlas/problems/index.json').problems);
const equations=byId(json('catalog/atlas-equations.json').equations);
const referenceSources=byId([...json('numerical-methods-atlas/assets/reference-solutions.json').cases,...json('catalog/atlas-reference-supplements.json').cases]);
const publicMethods=json('numerical-methods-atlas/methods/index.json');
const python=process.env.ATLAS_INDEX_PYTHON||'python3';
const importHelper=String.raw`
import json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve();sys.path.insert(0,str(root/'scripts'))
from atlas_method_routes import load_method_routes,build_method_routes
`;
const navigation=JSON.parse(execFileSync(python,['-B','-c',importHelper+'\nprint(json.dumps(load_method_routes(root)))',fileURLToPath(root)],{encoding:'utf8',maxBuffer:12*1024*1024}));

function blocks(html,attribute,value){
  const result=[];
  for(const opening of html.matchAll(/<([a-z][\w:-]*)\b[^>]*>/gi)){
    const properties=attrs(opening[0]);
    if(new RegExp('\\s'+attribute+'(?=\\s|/?>)').test(opening[0]))properties[attribute]??='';
    if(!(attribute in properties)||(value!==undefined&&properties[attribute]!==value))continue;
    const tags=new RegExp('</?'+opening[1]+'\\b[^>]*>','gi');tags.lastIndex=opening.index+opening[0].length;
    let depth=1,closing;while((closing=tags.exec(html))){depth+=closing[0].startsWith('</')?-1:1;if(!depth)break;}
    assert.ok(closing,'balanced '+attribute);
    result.push({attributes:properties,opening:opening[0],body:html.slice(opening.index+opening[0].length,closing.index)});
  }
  return result;
}
function links(html){return [...html.matchAll(/<a\b[^>]*href="([^"]+)"[^>]*>/g)].map(match=>decode(match[1]));}
function local(href,base=origin){
  const url=new URL(href,base);assert.equal(url.origin,origin,href);
  const path=url.pathname.slice(1)+(url.pathname.endsWith('/')?'index.html':'');
  assert.ok(existsSync(new URL(path,root)),href);
  if(url.hash&&!url.hash.startsWith('#/')&&path.endsWith('.html'))assert.ok(read(path).includes(`id="${decodeURIComponent(url.hash.slice(1))}"`),href);
  return url;
}
function expectedProblems(methodId){
  return catalog.problems.filter(row=>row.method_ids.includes(methodId)||problems.get(row.id).executions.some(run=>run.method_ids.includes(methodId)));
}
const sorted=items=>[...items].sort();

test('all method routes derive from reviewed problem bindings and only that exact method’s verified runs',()=>{
  assert.deepEqual(sorted(Object.keys(navigation.methods)),sorted(methodSource.map(method=>method.id)));
  for(const method of methodSource){
    const route=navigation.methods[method.id],expected=expectedProblems(method.id),cards=byId(route.problems);
    assert.equal(route.method_id,method.id);assert.equal(route.status,method.status);
    assert.deepEqual(sorted(cards.keys()),sorted(expected.map(row=>row.id)));
    assert.equal(cards.size,route.problems.length);
    const equationIds=new Set(expected.flatMap(row=>row.equation_ids));
    assert.deepEqual(sorted(route.equations.map(row=>row.id)),sorted(equationIds));
    for(const equation of route.equations){
      assert.deepEqual(equation.name,equations.get(equation.id).name);
      assert.deepEqual(sorted(equation.problem_ids),sorted(expected.filter(row=>row.equation_ids.includes(equation.id)).map(row=>row.id)));
      for(const language of ['ja','en']){
        const url=local(equation.url[language]);assert.equal(url.pathname,'/numerical-methods-atlas/equations/');
        assert.equal(url.hash,'#'+equation.id+'-'+language);assert.equal(url.searchParams.get('lang'),language);
      }
    }
    assert.deepEqual(sorted(route.references.map(row=>row.problem_id)),sorted(expected.map(row=>row.id)),'every associated problem retains a reference context, including those without a library card');
    for(const source of expected){
      const card=cards.get(source.id),original=problems.get(source.id);
      const runs=original.executions.filter(run=>run.method_ids.includes(method.id));
      assert.deepEqual(card.name,original.name);assert.deepEqual(card.image,original.image);
      assert.deepEqual(card.executions.map(run=>run.id),runs.map(run=>run.id));
      assert.equal(card.role,runs.length?'execution':'related');assert.deepEqual(card.method_note,source.method_note);
      for(const run of card.executions){
        const actual=runs.find(row=>row.id===run.id);
        for(const field of ['id','kind','name','method_ids','guide','input','download','verification','scope'])assert.deepEqual(run[field],actual[field],method.id+'/'+run.id+'/'+field);
      }
      const context=route.references.find(row=>row.problem_id===source.id);
      assert.deepEqual(context.problem_name,original.name);assert.deepEqual(context.reference_url,card.reference_url);
      assert.deepEqual(context.cases.map(row=>row.id),source.references.map(row=>row.id));
      for(const reference of context.cases){
        const binding=source.references.find(row=>row.id===reference.id),originalReference=original.references.find(row=>row.id===reference.id);
        assert.equal(reference.relation,binding.relation);assert.deepEqual(reference.note,binding.note);
        assert.equal(reference.kind,originalReference.kind);assert.deepEqual(reference.title,originalReference.title);
        for(const language of ['ja','en']){
          const url=local(reference.url[language]);assert.equal(url.pathname,'/numerical-methods-atlas/solutions/');assert.equal(url.hash,`#solution-${reference.id}-${language}`);
          const originalView=referenceSources.get(reference.id).view?.[language] || '/numerical-methods-atlas/?lang='+language+'#/exact-solutions?case='+reference.id;
          assert.equal(local(reference.view[language]).href,local(originalView).href);
        }
      }
      for(const language of ['ja','en']){
        const hub=local(card.hub[language]);assert.equal(hub.pathname,`/numerical-methods-atlas/problems/${source.id}/`);
        assert.equal(local(card.reference_url[language]).hash,'#references-'+language);
        local(card.image.url);local(card.code[language]);
      }
    }
  }
});

test('method navigation is published consistently without replacing scientific code metadata or primary citations',()=>{
  assert.deepEqual(json('numerical-methods-atlas/methods/navigation.json'),navigation);
  assert.deepEqual(publicMethods.problem_navigation_source_sha256,navigation.source_sha256);
  for(const method of methodSource){
    const aggregate=publicMethods.methods.find(row=>row.id===method.id);
    const record=json(`numerical-methods-atlas/methods/${method.id}/index.json`);
    assert.deepEqual(aggregate.problem_navigation,navigation.methods[method.id]);assert.deepEqual(record.problem_navigation,aggregate.problem_navigation);
    for(const field of ['status','code_modules','test_files','references','method_review'])if(field in method)assert.deepEqual(record[field],method[field],method.id+'/'+field+' remains authoritative');
    for(const field of ['code_urls','test_urls','code_download','code_edition','execution_examples','autodiff_release','sensitivity_release','inverse_release','multi_inverse_release','fdtd_release','depth_release'])assert.deepEqual(record[field],aggregate[field]);
    const markdown=read(`numerical-methods-atlas/methods/${method.id}/index.md`);
    for(const equation of record.problem_navigation.equations)for(const language of ['ja','en'])assert.ok(markdown.includes(equation.url[language]));
    for(const card of record.problem_navigation.problems)for(const language of ['ja','en']){
      assert.ok(markdown.includes(card.hub[language])&&markdown.includes(card.reference_url[language]));
      for(const run of card.executions)assert.ok(markdown.includes(run.guide[language])&&markdown.includes(run.download));
    }
    for(const context of record.problem_navigation.references)for(const reference of context.cases)for(const language of ['ja','en']){
      assert.ok(markdown.includes(reference.url[language])&&markdown.includes(reference.note[language]));
    }
  }
  for(const [path,hash]of Object.entries(navigation.source_sha256))assert.equal(sha(path),hash,path);
});

test('every map entry and bilingual method page exposes four real localized destinations',()=>{
  const map=read('numerical-methods-atlas/methods/index.html');
  const sections=['equations','problems','references','execution'];
  for(const language of ['ja','en']){
    const edition=blocks(map,'data-site-language',language)[0].body;
    const rows=blocks(edition,'data-method-id');
    assert.deepEqual(sorted(rows.map(row=>row.attributes['data-method-id'])),sorted(methodSource.map(row=>row.id)));
    for(const row of rows){
      const methodId=row.attributes['data-method-id'],path=`numerical-methods-atlas/methods/${methodId}/`;
      const linksInRow=blocks(row.body,'data-method-route-link');
      assert.deepEqual(linksInRow.map(link=>link.attributes['data-method-route-link']),sections);
      for(const link of linksInRow){
        const url=local(link.attributes.href,origin+'/numerical-methods-atlas/methods/');
        assert.equal(url.pathname,'/'+path);assert.equal(url.searchParams.get('lang'),language);
        assert.equal(url.hash,'#method-'+link.attributes['data-method-route-link']+'-'+language);
        if(['references','execution'].includes(link.attributes['data-method-route-link']))assert.doesNotMatch(text(link.body),/[（(]\s*\d+\s*[)）]/,'picture-context counts do not describe all of a method’s own reference/code resources');
      }
      const detail=blocks(read(path+'index.html'),'data-site-language',language)[0].body;
      assert.deepEqual(blocks(detail,'data-method-section').map(section=>section.attributes['data-method-section']),sections);
      const jump=blocks(detail,'data-method-route-link');assert.equal(jump.length,4);
      for(const link of jump)local(link.attributes.href,origin+'/'+path+'?lang='+language);
      const problemSection=blocks(detail,'data-method-section','problems')[0].body;
      const cards=blocks(problemSection,'data-linked-problem-id');
      assert.deepEqual(cards.map(card=>card.attributes['data-linked-problem-id']),navigation.methods[methodId].problems.map(card=>card.id));
      for(const card of cards){
        const expected=navigation.methods[methodId].problems.find(row=>row.id===card.attributes['data-linked-problem-id']);
        assert.equal(card.attributes['data-method-problem-role'],expected.role);
        assert.equal(local(blocks(card.body,'data-method-problem-picture')[0].attributes.href).href,expected.hub[language]);
        const runs=blocks(card.body,'data-method-execution-id');
        assert.deepEqual(runs.map(run=>run.attributes['data-method-execution-id']),expected.executions.map(run=>run.id));
        for(const [index,run]of runs.entries()){
          assert.equal(local(blocks(run.body,'data-method-execution-link')[0].attributes.href).href,expected.executions[index].guide[language]);
          assert.equal(local(blocks(run.body,'data-method-execution-download')[0].attributes.href).href,expected.executions[index].download);
        }
        if(!runs.length)assert.ok(text(card.body).includes(language==='ja'?'この手法でこの問題を解く固定入力実行例は未登録です。':'No fixed-input execution of this problem is registered for this method.'));
        for(const href of links(card.body))local(href);
      }
      const referenceSection=blocks(detail,'data-method-section','references')[0].body;
      const contexts=blocks(referenceSection,'data-method-reference-problem-id');
      assert.deepEqual(contexts.map(context=>context.attributes['data-method-reference-problem-id']),navigation.methods[methodId].references.map(context=>context.problem_id));
      for(const context of contexts){
        const expected=navigation.methods[methodId].references.find(row=>row.problem_id===context.attributes['data-method-reference-problem-id']);
        assert.equal(local(blocks(context.body,'data-method-reference-context')[0].attributes.href).href,expected.reference_url[language]);
        const cases=blocks(context.body,'data-method-reference-id');assert.deepEqual(cases.map(row=>row.attributes['data-method-reference-id']),expected.cases.map(row=>row.id));
        for(const entry of cases){
          const original=expected.cases.find(row=>row.id===entry.attributes['data-method-reference-id']);
          assert.equal(entry.attributes['data-reference-relation'],original.relation);
          assert.ok(text(entry.body).includes(text(original.note[language])),'the exact reference relationship note remains visible');
        }
      }
      const code=blocks(detail,'data-method-section','execution')[0].body;
      assert.deepEqual(blocks(code,'data-method-matched-execution-id').map(run=>run.attributes['data-method-matched-execution-id']),navigation.methods[methodId].problems.flatMap(problem=>problem.executions.map(run=>run.id)));
    }
  }
});

test('reference destinations preserve each method’s own explanations, independent data and saved results apart from problem pictures',()=>{
  const urls=value=>typeof value==='string'?[value]:value&&typeof value==='object'?Object.values(value).flatMap(urls):[];
  for(const method of publicMethods.methods)for(const language of ['ja','en']){
    const html=blocks(read(`numerical-methods-atlas/methods/${method.id}/index.html`),'data-site-language',language)[0].body;
    const section=blocks(html,'data-method-section','references')[0].body;
    const expected={
      reading:method.reading[language]||method.reading.en?[method.reading[language]||method.reading.en]:[],
      'independent-reference':urls(method.independent_reference),
      result:[...urls(method.results),...urls(method.result_urls)],
      verification:urls(method.code_verification)
    };
    for(const [kind,wanted]of Object.entries(expected)){
      const anchors=blocks(section,'data-method-reference-resource',kind);
      assert.deepEqual(sorted(new Set(anchors.map(anchor=>local(anchor.attributes.href).href))),sorted(new Set(wanted.map(url=>local(url).href))),method.id+'/'+kind+' uses existing metadata only');
      if(kind==='result')for(const anchor of anchors)assert.match(text(anchor.body),language==='ja'?/保存結果/:/Saved result/i,'stored computed results are not relabeled as exact solutions');
    }
    if(['fdtd','automatic-differentiation','adjoint','optimization'].includes(method.id)){
      assert.ok(expected.reading.length&&expected.result.length);
      const markdown=read(`numerical-methods-atlas/methods/${method.id}/index.md`);
      for(const url of [...expected.reading,...expected.result,...expected.verification])assert.ok(markdown.includes(url),method.id+' Markdown keeps its own reference resources');
    }
  }
});

test('HLLC, WENO-Z, Roe and Bratu derivatives do not borrow one another’s execution examples',()=>{
  const method=id=>navigation.methods[id];
  const runs=id=>method(id).problems.flatMap(problem=>problem.executions.map(run=>run.id));
  assert.deepEqual(runs('hllc'),['sod']);assert.deepEqual(runs('weno-z'),['weno-critical-epsilon','shu-osher']);assert.deepEqual(runs('roe'),['low-mach-vortex']);
  for(const id of ['automatic-differentiation','adjoint','optimization']){
    const bratu=method(id).problems.find(problem=>problem.id==='bratu');
    assert.ok(bratu);assert.equal(bratu.role,'related');assert.deepEqual(bratu.executions,[]);
    const context=method(id).references.find(row=>row.problem_id==='bratu');assert.ok(context);assert.deepEqual(context.cases,[]);
  }
  // Fixed approved runners, preserving old prefixes and each new case's
  // actual method IDs. Shared Bratu/AD names do not create extra runners.
  // The original five Newton runners remain an exact ordered prefix.
  // Additional runners are limited to the four fixed68 canonical case records.
  const cohort68=json('scripts/fixtures/atlas-batch68-77-baseline.json');
  const canonicalCases68=Object.values(cohort68.canonical_packets).flatMap(packet=>{
    assert.equal(sha(packet.base+'source-manifest.json'),packet.manifest_sha256);
    const manifest=json(packet.base+'source-manifest.json');
    assert.equal(sha(packet.base+'cases.json'),manifest.files['cases.json']);
    const raw=json(packet.base+'cases.json'),rows=Array.isArray(raw)?raw:raw.cases;
    assert.deepEqual(sorted(rows.map(row=>row.id)),sorted(packet.case_ids));
    return rows;
  });
  const addedNewton68=['robertson-stiff-kinetics','robertson-conservation-dae','van-der-pol-stiff-transition','index1-dae-consistent-initialization'];
  const declaredNewton68=canonicalCases68.filter(row=>row.method_ids.includes('newton')).map(row=>row.id);
  assert.deepEqual(sorted(declaredNewton68),sorted(addedNewton68));
  assert.equal(new Set(declaredNewton68).size,4);
  const qualifiedRunners={
    'newton':['bratu','bratu-fold-continuation','globalization-difficult-starts','bratu-fold-sensitivity','bratu-distributed-vjp'],
    'automatic-differentiation':['bratu-matrix-free-jfnk','reverse-vjp-duality','hessian-vector-products','kink-branch-derivatives'],
    'adjoint':['diffusion-discrete-adjoint','bratu-fold-sensitivity','bratu-distributed-vjp'],
    'optimization':['bratu-gn-lm-bounds','bfgs-lbfgs-controls','bratu-noise-regularization'],
    'dogleg-trust-region':['globalization-difficult-starts'],
    'jacobian-free-newton-krylov':['bratu-matrix-free-jfnk']
  };
  for(const [id,expected]of Object.entries(qualifiedRunners)){
    if(id==='newton')assert.deepEqual(runs(id).slice(0,expected.length),expected,id+' exact historical prefix');
    assert.deepEqual(runs(id),id==='newton'?[...expected,...addedNewton68]:expected,id+' exact qualified runners');
  }
  assert.deepEqual(runs('newton-krylov'),[],'the distinct Newton-Krylov method keeps no unrelated Bratu runner');
  for(const [id,caseId]of [['newton','bratu-fold-continuation'],['automatic-differentiation','bratu-matrix-free-jfnk'],['jacobian-free-newton-krylov','bratu-matrix-free-jfnk']]){
    const own=method(id).problems.find(problem=>problem.id===caseId);
    assert.ok(own,id+' has its exact qualified Bratu supplement');assert.equal(own.role,'execution');
    assert.deepEqual(own.executions.map(run=>run.id),[caseId]);
  }
  const nullControls=Object.entries(json('catalog/atlas-depth-expansion.json').case_problem_ids).filter(([,problemId])=>problemId===null).map(([id])=>id);
  for(const route of Object.values(navigation.methods)){
    assert.ok(route.problems.every(problem=>!nullControls.includes(problem.id)));
    assert.ok(route.problems.flatMap(problem=>problem.executions).every(run=>!nullControls.includes(run.id)),'method-wide controls do not acquire a fabricated problem picture');
  }
});

test('dedicated derivative, inverse and FDTD code remains available even without a matching problem runner',()=>{
  for(const id of ['automatic-differentiation','adjoint','optimization','fdtd']){
    const record=publicMethods.methods.find(method=>method.id===id),html=read(`numerical-methods-atlas/methods/${id}/index.html`);
    assert.equal(record.status,'educational-example');assert.ok(record.code_download&&record.code_urls.length);local(record.code_download);
    for(const language of ['ja','en']){
      const edition=blocks(html,'data-site-language',language)[0].body;
      const code=blocks(edition,'data-method-section','execution')[0].body;
      assert.ok(links(code).some(href=>local(href).href===record.code_download),id+' exposes its own existing edition in the code destination');
    }
  }
  for(const method of methodSource.filter(method=>method.status==='planned')){
    const record=publicMethods.methods.find(row=>row.id===method.id),route=navigation.methods[method.id];
    assert.deepEqual(route.problems,[]);assert.deepEqual(route.equations,[]);assert.deepEqual(route.references,[]);
    assert.deepEqual(record.code_urls,[]);assert.deepEqual(record.test_urls,[]);assert.ok(!record.code_download);
    for(const language of ['ja','en']){
      const edition=blocks(read(`numerical-methods-atlas/methods/${method.id}/index.html`),'data-site-language',language)[0].body;
      const code=blocks(edition,'data-method-section','execution')[0].body;
      assert.ok(!links(code).some(href=>new URL(href,origin).pathname.endsWith('.zip')),'a plan does not inherit an unrelated download');
    }
  }
});

test('pure method association handles add/remove edges, equal names and unrelated execution methods without inference',()=>{
  const output=execFileSync(python,['-B','-c',importHelper+String.raw`
import copy
note={'ja':'条件','en':'Scope'}
methods={ident:{'id':ident,'name':{'ja':'同名','en':'Same name'},'status':'educational-example' if ident!='planned' else 'planned'} for ident in ['alpha','beta','planned']}
def row(ident,method_ids,equation_ids,refs):return {'id':ident,'method_ids':method_ids,'equation_ids':equation_ids,'references':refs,'method_note':note,'reference_note':note,'equation_note':note}
catalog={'schema_version':1,'scope':note,'problems':[row('one',['alpha'],['eq'],[{'id':'ref','relation':'related-model','note':note}]),row('two',[],[],[])]}
cards={ident:{'id':ident,'name':{'ja':'同名','en':'Same name'},'model':'same-model','hub':{lang:'https://hrkoyama.github.io/numerical-methods-atlas/problems/'+ident+'/?lang='+lang for lang in ['ja','en']},'executions':[]} for ident in ['one','two']}
cards['one']['executions']=[{'id':'beta-run','method_ids':['beta']}]
equations={'eq':{'id':'eq','name':{'ja':'方程式','en':'Equation'}}};references={'ref':{'id':'ref','title':{'ja':'参照','en':'Reference'},'kind':'analytic'}}
before=copy.deepcopy((catalog,cards))
routes=build_method_routes(catalog,methods,cards,equations,references)
assert [problem['id'] for problem in routes['alpha']['problems']]==['one']
assert routes['alpha']['problems'][0]['role']=='related' and routes['alpha']['problems'][0]['executions']==[]
assert [run['id'] for run in routes['beta']['problems'][0]['executions']]==['beta-run']
assert routes['planned']['problems']==[]
assert routes['alpha']['references'][0]['cases'][0]['note']==note
assert routes['alpha']['references'][0]['cases'][0]['view']=={lang:'https://hrkoyama.github.io/numerical-methods-atlas/?lang='+lang+'#/exact-solutions?case=ref' for lang in ['ja','en']}
references['ref']['view']={lang:'/numerical-methods-atlas/validation/noh-shock/?lang='+lang+'#noh-shock-'+lang+'-measurements' for lang in ['ja','en']}
reference_before=copy.deepcopy(references)
overridden=build_method_routes(catalog,methods,cards,equations,references)
assert overridden['alpha']['references'][0]['cases'][0]['view']==references['ref']['view']
assert references==reference_before
assert (catalog,cards)==before
catalog['problems'][0]['method_ids']=[];catalog['problems'][1]['method_ids']=['alpha']
changed=build_method_routes(catalog,methods,cards,equations,references)
assert [problem['id'] for problem in changed['alpha']['problems']]==['two']
assert changed['alpha']['equations']==[] and changed['alpha']['references'][0]['cases']==[]
cards['one']['executions'].append({'id':'alpha-run','method_ids':['alpha']})
actual=build_method_routes(catalog,methods,cards,equations,references)
assert [run['id'] for run in actual['alpha']['problems'][0]['executions']]==['alpha-run']
assert [run['id'] for run in actual['beta']['problems'][0]['executions']]==['beta-run']
methods['alpha']['status']='planned'
try:build_method_routes(catalog,methods,cards,equations,references)
except ValueError:pass
else:raise AssertionError('Execution promoted a planned method')
print('pure method route mutations checked')
`,fileURLToPath(root)],{encoding:'utf8'});
  assert.match(output,/pure method route mutations checked/);
});

test('the method loader uses source catalogs before generated method, problem, equation, reference or test indexes',()=>{
  const output=execFileSync(python,['-B','-c',importHelper+String.raw`
from unittest.mock import patch
forbidden={root/'numerical-methods-atlas/equations/index.json',root/'numerical-methods-atlas/solutions/index.json',root/'numerical-methods-atlas/test-cases/index.json'}
directories=[root/'numerical-methods-atlas/methods',root/'numerical-methods-atlas/problems']
old_bytes=pathlib.Path.read_bytes;old_text=pathlib.Path.read_text
def guard(path):
    path=path.resolve()
    assert path not in forbidden and not any(path.is_relative_to(directory) for directory in directories),'Generated method dependency: '+str(path)
def read_bytes(path):guard(path);return old_bytes(path)
def read_text(path,*args,**kwargs):guard(path);return old_text(path,*args,**kwargs)
with patch.object(pathlib.Path,'read_bytes',read_bytes),patch.object(pathlib.Path,'read_text',read_text):routes=load_method_routes(root)
assert set(routes['methods'])=={row['id'] for row in json.loads((root/'catalog/atlas-methods.json').read_text())['methods']}
print('source-first method loading checked')
`,fileURLToPath(root)],{encoding:'utf8'});
  assert.match(output,/source-first method loading checked/);
});
