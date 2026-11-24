import test from 'node:test';
import assert from 'node:assert/strict';
import {existsSync,readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {searchDOM,descendants,flushSearch} from './fixtures/search-dom.mjs';
import {configureLocale,currentLanguage} from '../numerical-methods-atlas/i18n.js';

const root=new URL('../',import.meta.url),origin='https://hrkoyama.github.io';
const read=path=>readFileSync(new URL(path,root),'utf8'),json=path=>JSON.parse(read(path));
const sha=path=>createHash('sha256').update(readFileSync(new URL(path,root))).digest('hex');
const sorted=values=>[...values].sort(),ids=rows=>rows.map(row=>row.id),byId=rows=>new Map(rows.map(row=>[row.id,row]));
const groups=['methods','equations','figures','references','code'];
const home=json('numerical-methods-atlas/home-search-index.json'),site=json('search/index.json');
const publicMethods=json('numerical-methods-atlas/methods/index.json').methods;
const common=json('catalog/atlas-execution-examples.json').examples,discovery=json('catalog/atlas-execution-discovery.json').examples;
const expansion=json('catalog/atlas-depth-expansion.json'),problems=json('numerical-methods-atlas/problems/index.json').problems;
const equations=json('numerical-methods-atlas/equations/index.json').equations,references=json('numerical-methods-atlas/solutions/index.json').cases;
const supplements=json('numerical-methods-atlas/validation/index.json').cases,bindings=byId(json('catalog/atlas-problem-links.json').problems);
const python=process.env.ATLAS_INDEX_PYTHON||'python3';
const bootstrap=String.raw`
import json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve();sys.path.insert(0,str(root/'scripts'))
from atlas_search_routes import load_search_routes
`;
let loaded;
const routes=()=>loaded??=JSON.parse(execFileSync(python,['-B','-c',bootstrap+'\nprint(json.dumps(load_search_routes(root)))',fileURLToPath(root)],{encoding:'utf8',maxBuffer:24*1024*1024}));
const path=value=>{const url=new URL(value,origin);return url.pathname+url.search+url.hash;};
function local(value){
  const url=new URL(value,origin);assert.equal(url.origin,origin,value);assert.ok(!url.username&&!url.password,value);
  assert.ok(!url.searchParams.has('q'),value+' must not contain a search query');
  const file=url.pathname.slice(1)+(url.pathname.endsWith('/')?'index.html':'');
  assert.ok(existsSync(new URL(file,root)),value);
  if(url.hash&&!url.hash.startsWith('#/')&&file.endsWith('.html'))assert.ok(read(file).includes(`id="${decodeURIComponent(url.hash.slice(1))}"`),value);
  return url;
}
const anchors=node=>descendants(node).filter(child=>child.tag==='a');
const keyed=(node,key)=>descendants(node).filter(child=>Object.hasOwn(child.dataset,key));
let sequence=0;
const fresh=relative=>import(new URL(relative+'?search-navigation-test='+(++sequence),import.meta.url));
const runIds=graph=>graph.groups.code.filter(row=>row.availability==='run').map(row=>row.id);
const registeredChapters=()=>{
  const result=new Set(),add=url=>{const match=new URL(url,origin).pathname.match(/^\/numerical-methods-atlas\/(?:ja|en)\/read\/([^/]+)\/$/);if(match)result.add(match[1]);};
  for(const record of [...publicMethods,...problems,...references,...common,...supplements])for(const url of Object.values(record.reading||{}))add(url);
  for(const equation of equations)result.add(equation.chapter);
  for(const chapter of json('catalog/atlas-detailed-reading.json').chapters)if(chapter.methods?.length||chapter.related_methods?.length)result.add(chapter.id);
  for(const chapter of json('catalog/atlas-chapter-links.json').chapters)result.add(chapter.id);
  return [...result];
};

test('both indexes carry the same source-derived graph for every typed search entity',()=>{
  const source=routes(),chapters=home.entries.filter(row=>row.kind==='chapter');
  const expected={method:ids(publicMethods),problem:ids(problems),execution:[...ids(common),...Object.keys(expansion.case_problem_ids)],equation:ids(equations),reference:ids(references),chapter:registeredChapters()};
  assert.deepEqual(sorted(Object.keys(source.nodes)),sorted(Object.entries(expected).flatMap(([kind,identifiers])=>identifiers.map(id=>kind+':'+id))));
  for(const [key,graph]of Object.entries(source.nodes)){
    assert.equal(key,graph.kind+':'+graph.id);assert.deepEqual(Object.keys(graph.groups),groups);
    for(const language of ['ja','en'])assert.ok(typeof graph.note[language]==='string'&&!/^https?:/.test(graph.note[language]),'graph notes explain scope in human language');
  }
  for(const chapter of chapters.filter(row=>!expected.chapter.includes(row.chapter)))assert.ok(!chapter.search_navigation,chapter.chapter+' remains searchable without inventing registered associations');
  for(const method of publicMethods){
    const inline=home.entries.find(row=>row.method?.id===method.id)?.method;
    const global=site.documents.find(row=>row.method?.id===method.id)?.method;
    assert.ok(inline&&global,method.id);assert.deepEqual(inline.search_navigation,source.nodes['method:'+method.id]);
    assert.deepEqual(global.search_navigation,inline.search_navigation);
    assert.deepEqual(inline.search_navigation_by_goal,source.method_goals[method.id]||{});
    assert.deepEqual(global.search_navigation_by_goal,inline.search_navigation_by_goal);
    for(const field of ['status','code_urls','test_urls','reading'])assert.deepEqual(inline[field],method[field],method.id+'/'+field);
  }
  for(const entry of home.entries.filter(row=>!row.method&&row.search_navigation)){
    const graph=entry.search_navigation;assert.deepEqual(graph,source.nodes[graph.kind+':'+graph.id],entry.id);
  }
  for(const kind of ['problem','execution','equation','reference','chapter'])for(const id of expected[kind]){
    const graph=source.nodes[kind+':'+id];
    const inline=home.entries.filter(row=>row.search_navigation?.kind===kind&&row.search_navigation?.id===id);
    assert.equal(inline.length,1,kind+':'+id+' one inline entity');
    const global=site.documents.filter(row=>row.search_navigation?.kind===kind&&row.search_navigation?.id===id);
    assert.ok(global.length>=1,kind+':'+id+' global entity');
    for(const record of global)assert.deepEqual(record.search_navigation,graph);
  }
});

test('typed equation and reference results retain real bilingual fragment routes, formulas and classifications',async()=>{
  const {searchChapters}=await fresh('../numerical-methods-atlas/home-search.js');
  const {makeSearch}=await import('../search/engine.mjs');const search=makeSearch(site.documents);
  for(const [kind,records,prefix]of [['equation',equations,''],['reference',references,'solution-']])for(const record of records){
    const entry=home.entries.find(row=>row.search_navigation?.kind===kind&&row.search_navigation?.id===record.id);assert.ok(entry);
    assert.equal(entry.kind,kind);
    const formulas=Array.isArray(record.formula)?record.formula:[record.formula];
    const query=record.name?.en||record.title.en;
    if(kind==='reference')assert.equal(routes().nodes['reference:'+record.id].groups.references.find(row=>row.id===record.id).reference_kind,record.kind);
    for(const language of ['ja','en']){
      for(const formula of formulas)assert.ok(entry.text[language].includes(formula),kind+'/'+record.id+' own formula is searchable');
      if(kind==='reference')assert.ok(entry.keywords.includes(record.kind_label[language]),record.id+' preserves analytic/semi-analytic/manufactured classification');
      const expected=`/numerical-methods-atlas/${kind==='equation'?'equations':'solutions'}/?lang=${language}#${prefix}${record.id}-${language}`;
      assert.equal(path(entry.routes[language]),expected);local(expected);
      const inline=searchChapters(home,query,language).find(row=>row.search_navigation?.kind===kind&&row.search_navigation?.id===record.id);
      assert.ok(inline,kind+'/'+record.id+' inline retrieval');assert.equal(inline.url,expected);
      const global=search(query,language,'atlas').find(row=>row.search_navigation?.kind===kind&&row.search_navigation?.id===record.id);
      assert.ok(global,kind+'/'+record.id+' global retrieval');
    }
  }
  const source=routes();
  for(const [file,hash]of Object.entries(source.source_sha256))assert.equal(sha(file),hash,file);
  for(const graph of [...Object.values(source.nodes),...Object.values(source.method_goals).flatMap(Object.values)])for(const [group,items]of Object.entries(graph.groups)){
    const actionKeys=items.map(item=>JSON.stringify([item.id,item.url,item.context_problem_id||null,item.context_execution_id||null]));
    assert.equal(new Set(actionKeys).size,items.length,graph.kind+'/'+graph.id+'/'+group+' unique scoped actions');
    for(const item of items){
      for(const language of ['ja','en']){assert.ok(item.name[language]?.trim());local(item.url[language]);if(item.note)assert.ok(typeof item.note[language]==='string');}
      if(item.image){
        const url=local(item.image.url),bytes=readFileSync(new URL(url.pathname.slice(1),root));assert.ok(item.image.width>0&&item.image.height>0);
        assert.ok(bytes.subarray(0,8).equals(Buffer.from([137,80,78,71,13,10,26,10]))||bytes.subarray(0,4).toString()==='RIFF'&&bytes.subarray(8,12).toString()==='WEBP'||/<svg\b/.test(bytes.toString('utf8')),item.image.url+' is a saved public image');
      }
      if(group==='code')assert.ok(['run','source'].includes(item.availability),'code availability is explicit');
      if(item.relation)assert.ok(['same-problem','related-model'].includes(item.relation)&&item.note.ja&&item.note.en,'reference relationships retain caveats');
    }
  }
});

test('shared navigation renders literal labels, explicit missing categories and only safe same-site destinations',async()=>{
  const {appendSearchNavigation,publicNavigationPath}=await import('../search/navigation.mjs');
  const markup='<img src=x onerror=alert(1)><script>alert(2)</script>';
  const localized={ja:markup,en:markup},safe='/numerical-methods-atlas/solutions/?lang=ja#solution-euler-sod-ja';
  const graph={kind:'reference',id:'fixture',note:localized,groups:{methods:[],equations:[],figures:[],references:[{id:'euler-sod',name:localized,url:{ja:safe,en:safe},relation:'related-model',note:localized}],code:[]}};
  const unsafe=['javascript:alert(1)','data:text/html,x','//evil.example/x','https://evil.example/x','https://user@hrkoyama.github.io/x','/numerical-methods-atlas/../rights/','/numerical-methods-atlas/%2e%2e/rights/','/numerical-methods-atlas/.private/','/numerical-methods-atlas/\\evil/'];
  for(const url of unsafe)assert.equal(publicNavigationPath(url),null,url);
  const dom=searchDOM();
  try{
    const target=dom.document.createElement('li');appendSearchNavigation(target,{search_navigation:graph},'ja');
    assert.ok(target.textContent.includes(markup));assert.equal(keyed(target,'searchNavigation').length,1);
    assert.equal(anchors(target).filter(anchor=>anchor.href===safe).length,2,'summary and named context retain the exact language fragment');
    const categories=keyed(target,'searchNavigationCategory');assert.deepEqual(categories.map(node=>node.dataset.searchNavigationCategory),groups);
    for(const node of categories.filter(node=>node.tag==='span'))assert.match(node['aria-label'],/未登録/);
    assert.ok(descendants(target).some(node=>node.className==='search-navigation-relation'&&node.textContent==='関連モデルの参照'));
    for(const url of unsafe){
      const poisoned=structuredClone(graph);poisoned.groups.references[0].url={ja:url,en:url};
      poisoned.groups.figures=[{id:'bad',name:localized,url:{ja:safe,en:safe},image:{url,width:10,height:10,caption:localized}}];
      const item=dom.document.createElement('li');appendSearchNavigation(item,{search_navigation:poisoned},'ja');
      assert.ok(anchors(item).every(anchor=>publicNavigationPath(anchor.href)));
      assert.equal(descendants(item).filter(node=>node.tag==='img').length,0,url+' cannot create a remote or dangerous image');
    }
    const inherited=dom.document.createElement('li');appendSearchNavigation(inherited,{method:{search_navigation:graph},search_navigation:null},'ja');
    assert.equal(inherited.children.length,0,'an explicit purpose restriction never falls back to the broad parent graph');
    assert.ok(dom.created.every(node=>!['script','iframe'].includes(node.tag)));
  }finally{dom.restore();}
});

test('both live searches display cross-navigation for all six result types without sending or storing the query',async()=>{
  const mark={ja:'関連の条件 <script>literal</script>',en:'Scope <script>literal</script>'};
  const item=(id,url)=>({id,name:{ja:id,en:id},url:{ja:url+'?lang=ja',en:url+'?lang=en'}});
  const graph=(kind,id)=>({kind,id,note:mark,groups:{
    methods:[item('keep','/numerical-methods-atlas/methods/keep/')],
    equations:[{...item('euler','/numerical-methods-atlas/equations/'),url:{ja:'/numerical-methods-atlas/equations/?lang=ja#euler-ja',en:'/numerical-methods-atlas/equations/?lang=en#euler-en'}}],
    figures:[{...item('sod','/numerical-methods-atlas/problems/sod/'),image:{url:'/numerical-methods-atlas/gallery/previews/sod.png',width:832,height:494,caption:{ja:'保存した図',en:'Saved figure'}}}],
    references:[{...item('euler-sod','/numerical-methods-atlas/solutions/'),note:mark,relation:'related-model'}],
    code:[{...item('sod','/numerical-methods-atlas/code-and-data/examples/sod/'),availability:'run'}]
  }});
  const fixtures=[['method','zafmethod'],['problem','zafproblem'],['execution','zafrun'],['equation','zafequation'],['reference','zafreference'],['chapter','zafchapter']].map(([kind,id])=>{
    const navigation=graph(kind,id),route={ja:`/numerical-methods-atlas/problems/sod/?lang=ja`,en:`/numerical-methods-atlas/problems/sod/?lang=en`};
    const entry={id,title:{ja:id,en:id},headings:{ja:[],en:[]},keywords:[id],focus_keywords:[id],kind:kind==='execution'?'execution-example':kind,routes:route,search_navigation:navigation};
    if(kind==='method')entry.method={...publicMethods.find(row=>row.id==='keep'),id,name:{ja:id,en:id},aliases:[],search_navigation:navigation,search_navigation_by_goal:{}};
    const doc={url:route.en,title:id,titleEn:id,text:id,headings:id,lang:'both',categoryJa:'数値解析',categoryEn:'Numerical methods',search_navigation:navigation,routes:route};
    if(entry.method)doc.method=entry.method;
    if(kind==='execution')doc.execution=entry;
    return {kind,id,entry,doc,navigation};
  });
  const oldLanguage=currentLanguage();
  try{
    for(const kind of ['home','site'])for(const language of ['ja','en']){
      configureLocale({},language);
      const dom=searchDOM({kind,language,index:kind==='home'?{entries:fixtures.map(row=>row.entry)}:{documents:fixtures.map(row=>row.doc)}});
      try{
        if(kind==='home'){const {wireHomeSearch}=await fresh('../numerical-methods-atlas/home-search.js');wireHomeSearch();}
        else{await fresh('../search/search.js');await flushSearch();}
        for(const fixture of fixtures){
          if(kind==='home'){dom.input.value=fixture.id;dom.form.fire('submit');}
          else{dom.location.hash='q='+fixture.id;dom.document.fire('site-search-query');}
          await flushSearch();
          const rendered=descendants(dom.document).filter(node=>node.dataset.searchNavigation===fixture.id);
          assert.equal(rendered.length,1,kind+'/'+language+'/'+fixture.kind);
          assert.deepEqual(keyed(rendered[0],'searchNavigationCategory').map(node=>node.dataset.searchNavigationCategory),groups);
          assert.ok(rendered[0].textContent.includes(mark[language]),'scope notes are literal text');
          for(const category of groups){
            const link=keyed(rendered[0],'searchNavigationCategory').find(node=>node.dataset.searchNavigationCategory===category);
            assert.equal(link.href,path(fixture.navigation.groups[category][0].url[language]),kind+'/'+fixture.kind+'/'+category);
          }
          assert.equal(descendants(rendered[0]).filter(node=>node.tag==='img').length,1,'one real saved preview');
        }
        assert.equal(dom.fetches.length,1,'each entry point caches its fixed public index');
        for(const fetch of dom.fetches){const url=new URL(fetch.url,origin);assert.ok(!url.href.includes('zaf'));assert.ok(!url.searchParams.has('q'));assert.ok(!url.hash);}
        assert.ok(dom.historyWrites.every(url=>!new URL(url,origin).searchParams.has('q')));
        assert.ok(!dom.location.search.includes('q='));
        assert.ok(dom.created.every(node=>!['script','iframe'].includes(node.tag)));
        if(kind==='home'){
          const all=dom.nodes('home-search-all');assert.equal(new URL(all.href,origin).searchParams.get('scope'),'atlas');assert.equal(new URL(all.href,origin).hash,'#q=zafchapter');
          dom.input.value='';dom.form.fire('submit');assert.equal(dom.nodes('home-search-results').hidden,true);assert.equal(all.hidden,true);
        }
      }finally{dom.restore();}
    }
  }finally{configureLocale({},oldLanguage);}
});

test('exact equation and reference searches remain in the main results of both interfaces',async()=>{
  const selected=[{kind:'equation',record:equations.find(row=>row.id==='poisson-laplace')},{kind:'reference',record:references.find(row=>row.id==='poisson-manufactured')}];
  assert.ok(selected.every(row=>row.record),'representative Poisson equation and manufactured reference exist');
  const oldLanguage=currentLanguage();
  try{
    for(const kind of ['home','site'])for(const language of ['ja','en']){
      configureLocale({},language);
      const dom=searchDOM({kind,language,index:kind==='home'?home:site});
      try{
        if(kind==='home'){const {wireHomeSearch}=await fresh('../numerical-methods-atlas/home-search.js');wireHomeSearch();}
        else{await fresh('../search/search.js');await flushSearch();}
        for(const selectedEntry of selected){
          const {record}=selectedEntry;
          for(const query of [record.id,(record.name||record.title)[language]]){
            if(kind==='home'){dom.input.value=query;dom.form.fire('submit');}
            else{dom.location.hash='q='+encodeURIComponent(query);dom.document.fire('site-search-query');}
            await flushSearch();
            const direct=dom.nodes(kind==='home'?'home-search-results':'search-results');
            const cards=descendants(direct).filter(node=>node.dataset.searchNavigation===record.id);
            assert.equal(cards.length,1,kind+'/'+language+'/'+query+' exact typed result must not be hidden among related pages');
            const entity=home.entries.find(row=>row.search_navigation?.kind===selectedEntry.kind&&row.search_navigation?.id===record.id);
            assert.ok(anchors(direct).some(anchor=>anchor.href===path(entity.routes[language])),'the exact localized equation/reference fragment is a main result');
            if(kind==='site'){
              const summary=cards[0].parentElement.children.find(node=>node.className==='search-excerpt');
              assert.equal(summary.textContent,entity.snippet[language],'readable scoped prose is displayed while the formula stays searchable');
              const expected=language==='ja'
                ? selectedEntry.kind==='equation'?/方程式\s*[1-9]\d*件/:/(?:厳密解・)?参照解\s*[1-9]\d*件/
                : selectedEntry.kind==='equation'?/[1-9]\d*\s+equations?\b/i:/[1-9]\d*\s+(?:exact\s*\/\s*)?reference(?:\s+solution)?s?\b/i;
              assert.match(dom.nodes('search-status').textContent,expected,'the status counts the exact typed result alongside method/run candidates');
            }
          }
        }
      }finally{dom.restore();}
    }
  }finally{configureLocale({},oldLanguage);}
});

test('purpose candidates use only their dedicated graph and planned methods retain no executable actions',async()=>{
  const {findMethods}=await import('../search/method-search.mjs');
  const {matchGoals}=await import('../search/goals-data.mjs');
  const source=routes(),methods=home.entries.filter(row=>row.method).map(row=>row.method);
  const goals=json('catalog/atlas-goals.json').goals;
  for(const goal of goals){
    const query=goal.terms.find(term=>{const matched=matchGoals(term);return matched.length===1&&matched[0].id===goal.id&&findMethods(methods,term,'ja').some(row=>row.purposeScope);});
    assert.ok(query,goal.id+' has a registered unambiguous purpose query');
    const results=findMethods(methods,query,'ja');assert.ok(results.length,goal.id);
    const allowed=new Set([...(goal.examples||[]),...(goal.supplemental_examples||[])]);
    for(const result of results){
      assert.ok(result.purposeScope,goal.id+'/'+result.id);
      const graph=source.method_goals[result.id]?.[goal.id]||null;
      assert.deepEqual(result.method.search_navigation,graph,goal.id+'/'+result.id+' cannot inherit its broader method graph');
      assert.ok(!Object.hasOwn(result.method,'search_navigation_by_goal'),'a narrowed candidate cannot recover sibling purpose scopes');
      if(graph){
        const actual=runIds(graph);assert.ok(actual.every(id=>allowed.has(id)),goal.id+' no unrelated execution');
        if(goal.availability==='reading-only')assert.deepEqual(graph.groups.code,[]);
        if(!publicMethods.some(method=>method.id===result.id)&&result.method.resource_type==='model'){
          assert.ok(graph.groups.equations.some(row=>row.id===result.id&&row.role==='model'),'biological model candidates remain distinct from numerical methods');
          assert.ok(!graph.groups.methods.some(row=>row.id===result.id));
        }
      }
    }
  }
  for(const method of publicMethods.filter(row=>row.status!=='educational-example')){
    const graph=source.nodes['method:'+method.id];assert.deepEqual(graph.groups.code,[],method.id+' no borrowed implementation');
  }
});

test('execution, method and reverse-reference graphs preserve exact runners, null controls and related-model limitations',()=>{
  const source=routes(),commonById=byId(common),supplementById=byId(supplements);
  for(const id of [...ids(common),...Object.keys(expansion.case_problem_ids)]){
    const graph=source.nodes['execution:'+id],record=commonById.get(id)||supplementById.get(id);
    assert.deepEqual(ids(graph.groups.methods),record.method_ids,id+' actual execution methods');
    assert.deepEqual(ids(graph.groups.equations),['formulation-'+id,...(commonById.has(id)?discovery.find(row=>row.id===id).equation_ids:(expansion.case_equations?.[id]?.ids||[]))]);
    assert.deepEqual(runIds(graph),[id]);assert.deepEqual(graph.groups.code[0].method_ids,record.method_ids);
    const problemId=commonById.has(id)?record.problem_id:expansion.case_problem_ids[id];
    assert.equal(graph.groups.figures.length,1);assert.equal(graph.groups.figures[0].problem_id,problemId);
    assert.equal(graph.groups.figures[0].image.kind,commonById.has(id)?'problem-representative':'case-validation');
    assert.deepEqual(ids(graph.groups.references),['validation-'+id,...(problemId?bindings.get(problemId).references.map(row=>row.id):[])]);
    for(const edge of problemId?bindings.get(problemId).references:[]){
      const item=graph.groups.references.find(row=>row.id===edge.id);assert.equal(item.relation,edge.relation);
      for(const language of ['ja','en'])assert.ok(item.note[language].includes(edge.note[language]),id+' reference scope preserved');
    }
    if(problemId===null){
      assert.equal(graph.groups.equations[0].role,'diagnostic');
      for(const language of ['ja','en'])assert.ok(graph.groups.figures[0].url[language].endsWith('/'+id+'.png'),'unbound diagnostics keep their own plot');
    }
  }
  for(const method of publicMethods){
    const graph=source.nodes['method:'+method.id];
    assert.deepEqual(sorted(runIds(graph)),sorted(new Set(method.problem_navigation.problems.flatMap(problem=>problem.executions.map(run=>run.id)))));
    for(const run of graph.groups.code.filter(row=>row.availability==='run'))assert.ok(run.method_ids.includes(method.id),method.id+' cannot borrow a runner using a different method');
  }
  assert.deepEqual(runIds(source.nodes['method:hllc']),['sod']);assert.deepEqual(runIds(source.nodes['method:weno-z']),['weno-critical-epsilon','shu-osher']);assert.deepEqual(runIds(source.nodes['method:roe']),['low-mach-vortex']);
  assert.deepEqual(ids(source.nodes['execution:h2-rhf'].groups.equations),['formulation-h2-rhf','hartree-fock-model']);
  const qualifiedRunners={
    'newton':['bratu','bratu-fold-continuation','globalization-difficult-starts','bratu-fold-sensitivity','bratu-distributed-vjp'],
    'automatic-differentiation':['bratu-matrix-free-jfnk','reverse-vjp-duality','hessian-vector-products','kink-branch-derivatives'],
    'adjoint':['diffusion-discrete-adjoint','bratu-fold-sensitivity','bratu-distributed-vjp'],
    'optimization':['bratu-gn-lm-bounds','bfgs-lbfgs-controls','bratu-noise-regularization'],
    'dogleg-trust-region':['globalization-difficult-starts'],
    'fdtd':['cylinder-mie2d','lorentz-oblique-sp','dispersive-grazing-pml'],
    'jacobian-free-newton-krylov':['bratu-matrix-free-jfnk']
  };
  for(const [id,expected]of Object.entries(qualifiedRunners)){
    const graph=source.nodes['method:'+id];assert.deepEqual(runIds(graph),expected,id+' exact qualified runners');
    assert.ok(graph.groups.code.some(row=>row.id==='method-'+id&&row.availability==='source'),'independent code editions remain accessible');
    assert.ok(graph.groups.references.some(row=>row.id==='method-'+id),'method-owned validation stays separate from forward-problem references');
  }
  assert.deepEqual(runIds(source.nodes['method:newton-krylov']),[],'the old distinct Newton-Krylov method does not borrow the new JFNK runner');
  for(const id of ['automatic-differentiation','jacobian-free-newton-krylov']){
    const graph=source.nodes['method:'+id],run=graph.groups.code.find(row=>row.id==='bratu-matrix-free-jfnk');
    assert.equal(run.availability,'run');assert.ok(run.method_ids.includes(id));
    assert.deepEqual(run.method_ids,supplementById.get('bratu-matrix-free-jfnk').method_ids);
    assert.ok(!runIds(graph).includes('bratu'),'the old related Bratu picture is still not a derivative runner');
  }
  for(const [kind,records]of [['equation',equations],['reference',references]])for(const record of records){
    const graph=source.nodes[kind+':'+record.id];
    const expected=[...bindings.values()].filter(row=>kind==='equation'?row.equation_ids.includes(record.id):row.references.some(edge=>edge.id===record.id));
    const actual=new Set(graph.groups.figures.map(row=>new URL(row.url.en,origin).pathname.match(/\/problems\/([^/]+)\//)?.[1]));
    assert.deepEqual(sorted(actual),sorted(expected.map(row=>row.id)),kind+'/'+record.id+' only curated reverse bindings');
    if(kind==='reference')for(const row of [...graph.groups.figures,...graph.groups.code]){
      const problemId=row.id.split(':')[0],edge=bindings.get(problemId).references.find(edge=>edge.id===record.id);
      assert.equal(row.relation,edge.relation);
      for(const language of ['ja','en'])assert.ok(row.note[language].includes(edge.note[language]));
    }
  }
});

test('the elliptic reading retains every problem-specific reference condition even when library IDs repeat',async()=>{
  const graph=routes().nodes['chapter:elliptic'];assert.ok(graph);
  const associated=problems.filter(problem=>Object.values(problem.reading||{}).some(url=>new URL(url,origin).pathname.endsWith('/read/elliptic/')));
  const expected=associated.flatMap(problem=>bindings.get(problem.id).references.map(reference=>({problem,reference})));
  assert.ok(expected.length>1&&new Set(expected.map(row=>row.reference.id)).size<expected.length,'the fixture exercises one reference reused for distinct boundary conditions');
  for(const {problem,reference}of expected){
    const matches=graph.groups.references.filter(row=>row.id===reference.id&&row.context_problem_id===problem.id);
    assert.equal(matches.length,1,problem.id+'/'+reference.id+' retains its own context');
    assert.equal(matches[0].relation,reference.relation);
    for(const language of ['ja','en'])assert.ok(matches[0].note[language].includes(reference.note[language]),problem.id+' boundary and reference caveats survive aggregation');
  }
  const {appendSearchNavigation}=await import('../search/navigation.mjs'),dom=searchDOM();
  try{
    for(const language of ['ja','en']){
      const item=dom.document.createElement('li');appendSearchNavigation(item,{search_navigation:graph},language);
      for(const {reference}of expected)assert.ok(item.textContent.includes(reference.note[language]),'rendered reference context remains available');
    }
  }finally{dom.restore();}
});

test('source loading never consumes its own search output and tiny binding edits never infer links from matching names',()=>{
  const output=execFileSync(python,['-B','-c',bootstrap+String.raw`
import copy,tempfile
from unittest.mock import patch
import atlas_search_routes as module
forbidden={root/'search/index.json',root/'search/atlas-navigation.json',root/'numerical-methods-atlas/home-search-index.json'}
old_bytes=pathlib.Path.read_bytes;old_text=pathlib.Path.read_text
def guard(path):assert path.resolve() not in forbidden,'Search output used as source: '+str(path)
def read_bytes(path):guard(path);return old_bytes(path)
def read_text(path,*args,**kwargs):guard(path);return old_text(path,*args,**kwargs)
with patch.object(pathlib.Path,'read_bytes',read_bytes),patch.object(pathlib.Path,'read_text',read_text):
    actual=load_search_routes(root)
assert actual['entities'] and actual['nodes']
note={'ja':'限定した条件','en':'Scoped conditions'};name={'ja':'同名','en':'Same name'}
urls=lambda path:{lang:'https://hrkoyama.github.io/numerical-methods-atlas/'+path+'?lang='+lang for lang in ['ja','en']}
image={'url':'https://hrkoyama.github.io/saved.png','width':1,'height':1,'caption':name,'kind':'problem-representative'}
run={'id':'run','method_ids':['alpha']}
card={'id':'one','name':name,'hub':urls('problems/one/'),'image':image,'role':'execution','method_note':note,'executions':[run]}
methods=[{'id':ident,'name':name,'status':'educational-example' if ident=='alpha' else 'planned','reading':{},'references':[],
          'code_urls':['https://hrkoyama.github.io/alpha.py'] if ident=='alpha' else [],
          'problem_navigation':{'equations':[{'id':'eq'}] if ident=='alpha' else [],'problems':[card] if ident=='alpha' else []}} for ident in ['alpha','beta']]
problems=[{'id':ident,'name':name,'conditions':note,'method_note':note,'reference_note':note,'reading':{},
           'methods':[{'id':'alpha','role':'execution'}] if ident=='one' else [],'equations':[{'id':'eq'}] if ident=='one' else [],
           'hub':urls('problems/'+ident+'/'),'image':image,'executions':[run] if ident=='one' else [],'code_checks':[]} for ident in ['one','two']]
binding={'id':'one','equation_ids':['eq'],'references':[{'id':'ref','relation':'related-model','note':note}]}
catalog={'problems':[binding,{'id':'two','equation_ids':[],'references':[]}]}
execution={'id':'run','kind':'common','name':name,'methods':[{'id':'alpha'}],'formulation':{'url':urls('equations/'),'note':note,'role':'problem'},
           'equations':[{'id':'eq'}],'problem':card,'figure':image,'references':{'url':urls('validation/run/'),'note':note,'cases':[{'id':'ref','relation':'related-model','note':note}]}}
graph={'executions':{'run':execution},'source_sha256':{}}
with tempfile.TemporaryDirectory(prefix='atlas-search-routes-') as directory:
    fixture=pathlib.Path(directory)
    def write(path,value):
        target=fixture/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(value))
    sources={
      'numerical-methods-atlas/methods/index.json':{'methods':methods},'numerical-methods-atlas/problems/index.json':{'problems':problems},
      'numerical-methods-atlas/equations/index.json':{'equations':[{'id':'eq','name':name,'formula':'u=0','note':note,'chapter':'registered'}]},
      'numerical-methods-atlas/solutions/index.json':{'cases':[{'id':'ref','title':name,'formula':'u=0','kind':'analytic','kind_label':{'ja':'解析参照','en':'Analytic reference'},'assumptions':note,'reading':{}}]},
      'catalog/atlas-problem-links.json':catalog,'catalog/atlas-execution-examples.json':{'examples':[{'id':'run','name':name,'scope':note,'reading':{}}]},
      'numerical-methods-atlas/validation/index.json':{'cases':[]},'catalog/atlas-goals.json':{'goals':[{'id':'restricted','methods':['alpha'],'resources':[],'examples':['run'],'scope':note,'availability':'reading-only'}]},
      'catalog/atlas-detailed-reading.json':{'chapters':[]}}
    sources['catalog/atlas-chapter-links.json']={'schema_version':1,'chapters':[]}
    for path,value in sources.items():write(path,value)
    with patch.object(module,'load_execution_routes',return_value=graph):
        before=copy.deepcopy(graph);first=load_search_routes(fixture)
        assert graph==before,'Search connections mutated validated execution metadata'
        assert [row['id'] for row in first['nodes']['equation:eq']['groups']['figures']]==['one:one']
        assert first['nodes']['method:beta']['groups']['figures']==[],'Equal names do not imply a method association'
        assert first['method_goals']['alpha']['restricted']['groups']['code']==[]
        assert first['nodes']['chapter:registered']['groups']['methods']==[],'Equation reading does not infer every related method'
        catalog['problems'][0]['equation_ids']=[];catalog['problems'][0]['references']=[]
        catalog['problems'][1]['equation_ids']=['eq'];catalog['problems'][1]['references']=[{'id':'ref','relation':'related-model','note':note}]
        write('catalog/atlas-problem-links.json',catalog)
        changed=load_search_routes(fixture)
        assert [row['id'] for row in changed['nodes']['equation:eq']['groups']['figures']]==['two:two']
        assert [row['id'] for row in changed['nodes']['reference:ref']['groups']['figures']]==['two:two']
        assert changed['nodes']['equation:eq']['groups']['code']==[],'Moving a related-model edge cannot borrow the old problem runner'
        assert load_search_routes(fixture)==changed,'Unchanged source rebuild must be deterministic'
print('source-first search and small binding mutations checked')
`,fileURLToPath(root)],{encoding:'utf8',maxBuffer:3*1024*1024});
  assert.match(output,/source-first search and small binding mutations checked/);
});
