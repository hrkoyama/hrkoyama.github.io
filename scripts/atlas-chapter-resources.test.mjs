import test from 'node:test';
import assert from 'node:assert/strict';
import {existsSync,readFileSync,readdirSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import vm from 'node:vm';
import {readingURL} from '../numerical-methods-atlas/reading-urls.js';

const root=new URL('../',import.meta.url),origin='https://hrkoyama.github.io';
const read=path=>readFileSync(new URL(path,root),'utf8'),json=path=>JSON.parse(read(path));
const sha=path=>createHash('sha256').update(readFileSync(new URL(path,root))).digest('hex');
const groups=['methods','equations','figures','references','code'],sorted=values=>[...values].sort();
const inventory={};
for(const language of ['ja','en'])for(const id of readdirSync(new URL(`numerical-methods-atlas/${language}/read/`,root))){
  const path=`numerical-methods-atlas/${language}/read/${id}/index.html`;
  if(existsSync(new URL(path,root)))(inventory[id]??={})[language]=path;
}
const decode=value=>value.replaceAll('&amp;','&').replaceAll('&quot;','"').replaceAll('&#x27;',"'").replaceAll('&#39;',"'").replaceAll('&lt;','<').replaceAll('&gt;','>');
const attrs=tag=>Object.fromEntries([...tag.matchAll(/([\w:-]+)="([^"]*)"/g)].map(match=>[match[1],decode(match[2])]));
const plain=value=>decode(value.replace(/<[^>]+>/g,'')).replace(/\s+/g,' ').trim();
function blocks(html,attribute,value){
  const result=[];
  for(const opening of html.matchAll(/<([a-z][\w:-]*)\b[^>]*>/gi)){
    const properties=attrs(opening[0]);
    if(new RegExp('\\s'+attribute+'(?=\\s|/?>)').test(opening[0]))properties[attribute]??='';
    if(!(attribute in properties)||(value!==undefined&&properties[attribute]!==value))continue;
    const tags=new RegExp('</?'+opening[1]+'\\b[^>]*>','gi');tags.lastIndex=opening.index+opening[0].length;
    let depth=1,closing;while((closing=tags.exec(html))){depth+=closing[0].startsWith('</')?-1:1;if(!depth)break;}
    assert.ok(closing,'balanced '+attribute);result.push({attributes:properties,body:html.slice(opening.index+opening[0].length,closing.index)});
  }
  return result;
}
const links=html=>[...html.matchAll(/<a\b[^>]*href="([^"]+)"[^>]*>/g)].map(match=>decode(match[1]));
function local(href,base=origin){
  const url=new URL(href,base);assert.equal(url.origin,origin,href);assert.ok(!url.username&&!url.password);
  const file=url.pathname.slice(1)+(url.pathname.endsWith('/')?'index.html':'');assert.ok(existsSync(new URL(file,root)),href);
  if(url.hash&&!url.hash.startsWith('#/')&&file.endsWith('.html'))assert.ok(read(file).includes(`id="${decodeURIComponent(url.hash.slice(1))}"`),href);
  return url;
}
const python=process.env.ATLAS_INDEX_PYTHON||'python3';
const bootstrap=String.raw`
import importlib.util,json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve();sys.path.insert(0,str(root/'scripts'))
from atlas_search_routes import load_search_routes
spec=importlib.util.spec_from_file_location('chapter_resources',root/'scripts/build-atlas-chapter-resources.py')
builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)
`;
let navigation;
const source=()=>navigation??=JSON.parse(execFileSync(python,['-B','-c',bootstrap+'\nprint(json.dumps(load_search_routes(root)))',fileURLToPath(root)],{encoding:'utf8',maxBuffer:32*1024*1024}));

test('every physical chapter has consistent bilingual resource records and unchanged canonical addresses',()=>{
  const aggregate=json('numerical-methods-atlas/reading-resources.json');
  assert.deepEqual(sorted(Object.keys(aggregate.chapters)),sorted(Object.keys(inventory)));
  for(const [id,editions]of Object.entries(inventory)){
    const record=aggregate.chapters[id];assert.equal(record.id,id);
    assert.ok(['registered','directory-only'].includes(record.association_status));
    assert.equal(record.resource_navigation.kind,'chapter');assert.equal(record.resource_navigation.id,id);
    assert.deepEqual(Object.keys(record.resource_navigation.groups),groups);
    for(const [language,path]of Object.entries(editions)){
      const html=read(path),directory=path.slice(0,-'index.html'.length),sidecar=json(directory+'resources.json');
      const canonical=[...html.matchAll(/<link\b[^>]*>/g)].map(match=>attrs(match[0])).find(row=>row.rel==='canonical');
      assert.equal(canonical?.href,origin+'/'+directory);assert.equal(local(record.routes[language]).pathname,'/'+directory);
      assert.equal(record.title[language],plain(html.match(/<h1\b[^>]*>([\s\S]*?)<\/h1>/)?.[1]||''));
      assert.deepEqual(sidecar.resource_navigation,record.resource_navigation);
      assert.equal(sidecar.id,id);assert.ok(read(directory+'resources.md').includes(record.title[language]));
    }
  }
  for(const [path,hash]of Object.entries(aggregate.source_sha256))assert.equal(sha(path),hash,path);
});

test('registered chapter links follow only reviewed method, problem, equation, reference and actual execution contexts',()=>{
  const aggregate=json('numerical-methods-atlas/reading-resources.json'),nodes=source().nodes;
  for(const [id,record]of Object.entries(aggregate.chapters)){
    const expected=nodes['chapter:'+id];
    if(expected){assert.equal(record.association_status,'registered');assert.deepEqual(record.resource_navigation,expected,id);}
    else{
      assert.equal(record.association_status,'directory-only');
      assert.ok(groups.every(group=>record.resource_navigation.groups[group].length===0),id+' global directories are not fabricated scientific associations');
    }
    for(const [group,items]of Object.entries(record.resource_navigation.groups))for(const item of items){
      for(const language of Object.keys(inventory[id]))local(item.url[language]);
      if(group==='code')assert.ok(['source','run'].includes(item.availability));
      if(item.relation){assert.ok(['same-problem','related-model'].includes(item.relation));assert.ok(item.note.ja&&item.note.en);}
    }
  }
  for(const id of ['textbooks','history','references','roadmap']){
    assert.equal(aggregate.chapters[id].association_status,'directory-only');
    assert.deepEqual(aggregate.chapters[id].resource_navigation.groups.code,[],id+' has no invented runner');
  }
  for(const id of ['accuracy-stability','chapman-enskog','coordinates-viscosity','meshes','steady-runge-kutta'])assert.equal(aggregate.chapters[id].association_status,'registered',id+' explicit technical association');
  for(const binding of json('catalog/atlas-chapter-links.json').chapters){
    const graph=aggregate.chapters[binding.id].resource_navigation;
    for(const language of ['ja','en'])assert.ok(graph.note[language].includes(binding.note[language]));
    for(const link of binding.code_links||[]){
      const item=graph.groups.code.find(row=>row.id===link.id);assert.ok(item);assert.equal(item.availability,'source');
      for(const language of ['ja','en']){assert.equal(item.url[language],link.url);assert.ok(item.note[language].includes(link.note[language]));}
    }
  }
  for(const id of ['coordinates-viscosity','meshes']){
    const graph=aggregate.chapters[id].resource_navigation;
    assert.ok(graph.groups.code.length&&graph.groups.code.every(row=>row.availability==='source'));
    for(const group of groups.filter(group=>group!=='code'))assert.deepEqual(graph.groups[group],[],id+' pointwise/geometry checks do not become a PDE solver, picture or exact-solution claim');
  }
  const jamesonCode=aggregate.chapters['steady-runge-kutta'].resource_navigation.groups.code;
  assert.deepEqual(jamesonCode.map(row=>[row.id,row.availability]),[
    ['jameson-steady-linear-modes','run'],['method-jameson-steady-rk','source'],
  ],'only the new qualified steady-RK run and its method-specific source are added');
  for(const item of jamesonCode)assert.deepEqual(item.method_ids,['jameson-steady-rk']);
  assert.deepEqual(jamesonCode.filter(row=>row.method_ids.some(id=>['rk4','multigrid','dual-time','low-mach-preconditioning'].includes(id))),[],
    'related RK4 and multigrid definitions do not become a Jameson solver');
  const jamesonEntry=json('numerical-methods-atlas/validation/jameson-steady-linear-modes/index.json');
  const jamesonRelease=json('numerical-methods-atlas/validation/releases.json').releases.find(row=>row.group==='steady-rk');
  assert.deepEqual(jamesonRelease.case_ids,['jameson-steady-linear-modes']);assert.equal(jamesonEntry.group,'steady-rk');
  assert.deepEqual(jamesonEntry.method_ids,['jameson-steady-rk']);assert.equal(jamesonEntry.release.base,jamesonRelease.base);
  assert.deepEqual(jamesonCode[0].note,jamesonEntry.summary,'the run carries only its own canonical limited-study scope');
  assert.match(jamesonEntry.limits.en,/no JST compressible flux/,'the linear supplement is not a complete compressible-flow solver');
  const jamesonBase=`code/validated-examples/${jamesonRelease.edition}/steady-rk/`,jamesonProof=json(jamesonBase+'verification.json');
  assert.equal(sha(jamesonBase+'verification.json'),jamesonRelease.verification_sha256);
  assert.equal(jamesonProof.passed,true);assert.equal(jamesonProof.all_cases_rerun,true);
  assert.equal(jamesonProof.tests,jamesonRelease.tests);assert.equal(jamesonProof.passed_tests,jamesonRelease.tests);
  assert.equal(jamesonEntry.release.passed_tests,jamesonRelease.tests);
  const jamesonManifest=json(jamesonBase+'source-manifest.json');assert.equal(sha(jamesonBase+'source-manifest.json'),jamesonRelease.manifest_sha256);
  for(const file of ['run.py','steady.py']){assert.equal(sha(jamesonBase+file),jamesonManifest.files[file]);assert.ok(jamesonEntry.release.code_urls.includes(jamesonRelease.base+file));}
  for(const language of ['ja','en']){
    assert.equal(jamesonCode[0].url[language],`${origin}/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=${language}`);
    assert.equal(jamesonCode[1].url[language],`${origin}/numerical-methods-atlas/methods/jameson-steady-rk/?lang=${language}#method-execution-${language}`);
  }
  assert.deepEqual(jamesonCode[1].url,nodes['method:jameson-steady-rk'].groups.code.find(row=>row.id==='method-jameson-steady-rk').url);
  assert.deepEqual(jamesonCode[1].note,nodes['method:jameson-steady-rk'].groups.code.find(row=>row.id==='method-jameson-steady-rk').note);
  assert.deepEqual(aggregate.chapters['chapman-enskog'].resource_navigation.groups.code.filter(row=>row.availability==='run'),[],'the shear-wave source check is not a new fixed-input PDE entry');
  const methods=new Map(json('numerical-methods-atlas/methods/index.json').methods.map(row=>[row.id,row]));
  const problems=new Map(json('numerical-methods-atlas/problems/index.json').problems.map(row=>[row.id,row]));
  let namedMethodLinks=0,namedProblemLinks=0;
  for(const record of Object.values(aggregate.chapters)){
    for(const item of record.resource_navigation.groups.code){
      const target=new URL(item.url.en),methodId=target.pathname.match(/\/methods\/([^/]+)\/$/)?.[1];
      if(!methodId||!target.hash.startsWith('#method-execution-'))continue;
      const method=methods.get(methodId);assert.ok(method);
      for(const language of ['ja','en'])assert.ok(item.name[language].includes(method.name[language]),record.id+'/'+methodId+' code link names the actual method');
      const canonical=source().nodes['method:'+methodId].groups.code.find(row=>row.id===item.id);
      assert.deepEqual(canonical.name,{ja:'この手法のコード・検証',en:'Code and validation for this method'},'chapter display names do not mutate canonical method records');namedMethodLinks++;
    }
    for(const item of record.resource_navigation.groups.references){
      const target=new URL(item.url.en),problemId=target.pathname.match(/\/problems\/([^/]+)\/$/)?.[1];
      if(!problemId||!target.hash.startsWith('#references-'))continue;
      const problem=problems.get(problemId);assert.ok(problem);
      for(const language of ['ja','en'])assert.ok(item.name[language].includes(problem.name[language]),record.id+'/'+problemId+' reference link names the actual problem');
      const canonical=source().nodes['problem:'+problemId].groups.references.find(row=>row.id==='problem-'+problemId);
      assert.deepEqual(canonical.name,{ja:'この問題の参照・比較条件',en:'References and comparison conditions for this problem'},'chapter display names do not mutate canonical problem records');namedProblemLinks++;
    }
  }
  assert.ok(namedMethodLinks&&namedProblemLinks,'both formerly generic link types are exercised');
  const elliptic=aggregate.chapters.elliptic.resource_navigation.groups.references;
  assert.ok(elliptic.some(row=>row.context_problem_id),'boundary-specific reference contexts remain separate');
  for(const item of source().nodes['chapter:elliptic'].groups.references)assert.ok(elliptic.some(row=>JSON.stringify(row)===JSON.stringify(item)),'no reused reference ID overwrites a different boundary condition');
});

test('each static chapter exposes a front door and five typed sections with real localized resources and honest directory fallbacks',()=>{
  const aggregate=json('numerical-methods-atlas/reading-resources.json');
  for(const [id,editions]of Object.entries(inventory))for(const [language,path]of Object.entries(editions)){
    const html=read(path),record=aggregate.chapters[id],base=origin+'/'+path;
    const jumps=blocks(html,'data-chapter-resource-jump',id),panels=blocks(html,'data-chapter-resources',id);
    assert.equal(jumps.length,1,id+'/'+language+' one visible front door');assert.equal(panels.length,1,id+'/'+language+' one resource panel');
    assert.equal(panels[0].attributes.id,'chapter-resources');assert.match(panels[0].attributes.class,/\bchapter-resource-navigation\b/);assert.match(panels[0].attributes.class,/\bsearch-navigation\b/);
    const sections=blocks(panels[0].body,'data-chapter-resource-group');
    assert.deepEqual(sections.map(row=>row.attributes['data-chapter-resource-group']),groups);
    const jumpLinks=links(jumps[0].body);assert.equal(jumpLinks.length,groups.length);
    assert.deepEqual(jumpLinks.map(href=>local(href,base).hash),groups.map(group=>'#chapter-resources-'+group));
    for(const group of groups){
      const section=sections.find(row=>row.attributes['data-chapter-resource-group']===group),items=record.resource_navigation.groups[group];
      assert.equal(section.attributes.id,'chapter-resources-'+group);
      const urls=links(section.body).map(href=>local(href,base).href),markdown=read(path.replace('index.html','resources.md'));
      for(const item of items){
        assert.ok(urls.includes(new URL(item.url[language],origin).href),id+'/'+group+'/'+item.id);
        assert.ok(plain(section.body).includes(item.name[language]),'actual linked resource names remain visible');
        if(item.note)assert.ok(plain(section.body).includes(item.note[language].replace(/\s+/g,' ').trim()),id+' reference/applicability caveat');
        assert.ok(markdown.includes(item.url[language]),id+' resource Markdown parity');
      }
      const directory=record.directories[group];assert.ok(directory?.name?.[language]);local(directory.url[language]);
      if(group==='code'&&items.length&&items.every(item=>item.availability==='source'))assert.match(plain(section.body),language==='ja'?/コード・検証/:/Code & checks/,'source checks retain their own label');
      if(!items.length){
        assert.ok(urls.includes(new URL(directory.url[language],origin).href),id+'/'+group+' has an explicit global directory');
        assert.match(plain(section.body),language==='ja'?/未登録|対応.*ありません|一覧/:/not registered|no .*registered|director|index/i);
      }
    }
    for(const name of ['chapter-resources',...groups.map(group=>'chapter-resources-'+group)])assert.equal([...html.matchAll(/\bid="([^"]+)"/g)].filter(match=>match[1]===name).length,1,id+'/'+name+' unique target');
    assert.ok(!/<article\b[^>]*>[\s\S]*data-chapter-resource-jump=/.test(html.split('</article>')[0]),'the front door is outside the original article');
  }
});

test('the application resolves every physical legacy reading route including the static-only thermostat chapter and section anchors',async()=>{
  const {chapterEditions}=await import('../numerical-methods-atlas/chapter-resources.mjs');
  assert.deepEqual(sorted(Object.keys(chapterEditions)),sorted(Object.keys(inventory)));
  for(const [id,editions]of Object.entries(inventory))assert.deepEqual(sorted(Object.keys(chapterEditions[id])),sorted(Object.keys(editions)));
  const app=read('numerical-methods-atlas/app.js'),start=app.indexOf('async function route('),end=app.indexOf(' const renderers=',start);
  assert.ok(start>=0&&end>start,'the actual app router exposes its redirect branch');
  const route=app.slice(start,end).replaceAll('import.meta.url',JSON.stringify(origin+'/numerical-methods-atlas/app.js'))+'\n}';
  const redirected=[],state={language:'ja',loads:0};
  const context=vm.createContext({URL,URLSearchParams,navigationVersion:0,chapterEditions,documents:{},readingURL,
    currentLanguage:()=>state.language,resolveHomeLegacyURL:()=>null,disposeMovies(){},disposeEquations(){},disposeComparisons(){},
    loadDocuments:async()=>{state.loads++;return {};},location:{href:'',hash:'',replace:url=>redirected.push(url)}});
  vm.runInContext(route,context);
  for(const [id,editions]of Object.entries(inventory))for(const language of ['ja','en']){
    state.language=language;
    const edition=editions[language]?language:editions.en?'en':Object.keys(editions)[0];
    const section=read(editions[edition]).match(/<h[2-6]\b[^>]*\bid="([^"]+)"/)?.[1]||'';
    context.location.hash='#/read/'+id+(section?'?section='+encodeURIComponent(section):'');context.location.href=origin+'/numerical-methods-atlas/?lang='+language+context.location.hash;
    const before=redirected.length;await context.route();assert.equal(redirected.length,before+1,id+'/'+language+' redirects once');
    const url=local(redirected.at(-1));assert.equal(url.pathname,`/numerical-methods-atlas/${edition}/read/${id}/`);assert.equal(url.searchParams.get('lang'),edition);assert.equal(decodeURIComponent(url.hash.slice(1)),section);
  }
  assert.equal(state.loads,0,'known physical routes do not depend on the incomplete SPA content registry');
  assert.ok(chapterEditions.thermostats?.ja&&chapterEditions.thermostats?.en);
  for(const [requested,available]of [['ja','en'],['en','ja']]){
    state.language=requested;context.chapterEditions={'single-edition':{[available]:`/numerical-methods-atlas/${available}/read/single-edition/`}};
    context.location.hash='#/read/single-edition?section=kept-anchor';await context.route();
    const url=new URL(redirected.at(-1));assert.equal(url.pathname,`/numerical-methods-atlas/${available}/read/single-edition/`);assert.equal(url.searchParams.get('lang'),available);assert.equal(url.hash,'#kept-anchor');
  }
});

test('explicit chapter openings keep the typed front door after the original lead and outside the article',()=>{
 const result=execFileSync(python,['-B','-c',String.raw`
import ast,json,pathlib,re
from html.parser import HTMLParser
path=pathlib.Path('scripts/build-atlas-chapter-resources.py')
node=next(node for node in ast.parse(path.read_text()).body if isinstance(node,ast.ClassDef) and node.name=='ReadingPage')
ns={'HTMLParser':HTMLParser,'re':re}
exec(compile(ast.Module(body=[node],type_ignores=[]),str(path),'exec'),ns)
article='<article class="prose"><h2 id="kept-anchor">Body heading</h2><p>Conserved value 1.2345.</p></article>'
marker='<!-- chapter-resource-position -->'
opening='<div class="reading-opening" data-chapter-opening><h1>Existing title</h1><p>Existing lead.</p></div>'
html='<html><head><title>Existing title</title></head><body><main>'+opening+marker+'<nav>Existing auxiliary links</nav>'+article+'</main></body></html>'
page=ns['ReadingPage'](html)
assert page.jump==html.index(marker)+len(marker)
inserted=html[:page.jump]+'<nav data-chapter-resource-jump="fixture">Five typed links</nav>'+html[page.jump:]
assert inserted.index('Existing lead.')<inserted.index('data-chapter-resource-jump')<inserted.index('Existing auxiliary links')<inserted.index(article)
assert article in inserted and inserted.replace('<nav data-chapter-resource-jump="fixture">Five typed links</nav>','')==html
legacy=html.replace(opening+marker,'').replace(article,'<article><h1>Legacy title</h1>'+article+'</article>')
assert ns['ReadingPage'](legacy).jump==legacy.index('<article>'),'Legacy article boundary stays intact'
for invalid in [html.replace(marker,marker+marker),html.replace(marker,'').replace('<h2',marker+'<h2',1)]:
 try:ns['ReadingPage'](invalid)
 except ValueError:pass
 else:raise AssertionError('Ambiguous or inside-article positions must fail')
print(json.dumps({'opening_after_lead':True,'original_article_unchanged':True,'legacy_boundary_preserved':True}))
`],{cwd:root,encoding:'utf8'});
 assert.deepEqual(JSON.parse(result),{opening_after_lead:true,original_article_unchanged:true,legacy_boundary_preserved:true});
});

test('small chapter fixtures preserve original bodies and downloads, replace poisoned output and follow source and edition changes idempotently',()=>{
  const output=execFileSync(python,['-B','-c',bootstrap+String.raw`
import copy,hashlib,re,shutil,tempfile
note={'ja':'限定された関連資料','en':'Explicitly scoped resources'}
def graph(ident):return {'kind':'chapter','id':ident,'note':note,'groups':{key:[] for key in ['methods','equations','figures','references','code']}}
with tempfile.TemporaryDirectory(prefix='atlas-chapter-resources-') as directory:
    fixture=pathlib.Path(directory)
    def write(path,value):
        target=fixture/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(value if isinstance(value,str) else json.dumps(value,ensure_ascii=False))
    def read(path):return (fixture/path).read_text()
    def page(language,ident,title,article=True):
        prose='<h1>'+title+'</h1><h2 id="scientific-anchor">Scientific heading</h2><p data-original="yes">Original body &amp; conserved result 1.2345.</p>'
        body='<article class="prose">'+prose+'</article>' if article else prose
        path='numerical-methods-atlas/'+language+'/read/'+ident+'/'
        write(path+'index.html','<!doctype html><html><head><title>'+title+'</title><link rel="canonical" href="https://hrkoyama.github.io/'+path+'"></head><body><main id="main">'+body+'<aside class="chapter-toc"><a href="#scientific-anchor">Original contents</a></aside></main></body></html>')
        write(path+'index.json',{'original_measurement':1.2345,'implementation_status':'reading-only','html':body})
        write(path+'index.md','# '+title+'\n\nOriginal scientific text and result 1.2345.\n')
        return path,body
    originals={}
    for language,ident,title,article in [('ja','bound','対応する章',True),('en','bound','Bound chapter',True),('ja','textbooks','教科書案内',False),('en','textbooks','Textbook guide',False),('en','static-only','Static-only chapter',False)]:
        path,body=page(language,ident,title,article);originals[path]=body
    for name in ['content.ja.json','content.en.json','content.json']:
        write('numerical-methods-atlas/'+name,'{"original":"unchanged SPA content"}\n')
    for name in ['methods','equations','gallery','solutions','code-and-data','code-and-data/examples']:
        write('numerical-methods-atlas/'+name+'/index.html','<main><h1>Global directory</h1></main>')
    write('numerical-methods-atlas/app.js',(root/'numerical-methods-atlas/app.js').read_text())
    write('numerical-methods-atlas/index.html','<html><head></head><body><script type="module" src="app.js"></script></body></html>')
    write('llms.txt','')
    for name in ['styles/atlas-chapter-resources.css']:
        target=fixture/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(root/name,target)
    write('catalog/fixture-links.json',{'scope':'first'})
    def hashes():return {'catalog/fixture-links.json':hashlib.sha256((fixture/'catalog/fixture-links.json').read_bytes()).hexdigest()}
    navigation={'nodes':{'chapter:bound':graph('bound')},'source_sha256':hashes()}
    navigation['nodes']['chapter:bound']['groups']['methods']=[{'id':'alpha','name':{'ja':'最初の関連手法','en':'First linked method'},'url':{lang:'https://hrkoyama.github.io/numerical-methods-atlas/methods/?lang='+lang for lang in ['ja','en']},'note':note}]
    protected={path:path.read_bytes() for path in fixture.rglob('*') if path.is_file() and (path.name in {'content.json','content.en.json','content.ja.json'} or path.name in {'index.json','index.md'} and '/read/' in str(path))}
    write('numerical-methods-atlas/reading-resources.json',{'chapters':{'ghost':{'id':'ghost','resource_navigation':graph('ghost')}}})
    write('numerical-methods-atlas/en/read/bound/resources.json',{'resource_navigation':{'poison':'stale generated association'}})
    before=copy.deepcopy(navigation);builder.build(fixture,navigation=navigation);assert navigation==before
    aggregate=json.loads(read('numerical-methods-atlas/reading-resources.json'))
    assert set(aggregate['chapters'])=={'bound','textbooks','static-only'} and 'ghost' not in aggregate['chapters']
    assert aggregate['chapters']['textbooks']['association_status']=='directory-only'
    for path,body in originals.items():
        html=read(path+'index.html')
        if body.startswith('<article'):assert body in html,'Original article changed'
        else:
            assert '<h2 id="scientific-anchor">Scientific heading</h2><p data-original="yes">Original body &amp; conserved result 1.2345.</p>' in html
        assert html.count('data-chapter-resource-jump=')==html.count('data-chapter-resources=')==1
        assert '<a href="#scientific-anchor">Original contents</a>' in html
        assert (fixture/path/'resources.json').is_file() and (fixture/path/'resources.md').is_file()
    assert all(path.read_bytes()==data for path,data in protected.items()),'Original content or legacy machine downloads changed'
    snapshot={str(path.relative_to(fixture)):path.read_bytes() for path in fixture.rglob('*') if path.is_file()}
    builder.build(fixture,navigation=navigation)
    assert snapshot=={str(path.relative_to(fixture)):path.read_bytes() for path in fixture.rglob('*') if path.is_file()},'Repeated build is not bytewise idempotent'
    changed=copy.deepcopy(navigation)
    changed['nodes']['chapter:bound']['groups']['methods'][0]['id']='beta'
    changed['nodes']['chapter:bound']['groups']['methods'][0]['name']={'ja':'更新した関連手法','en':'Updated linked method'}
    write('catalog/fixture-links.json',{'scope':'changed'});changed['source_sha256']=hashes()
    builder.build(fixture,navigation=changed)
    for language in ['ja','en']:
        path='numerical-methods-atlas/'+language+'/read/bound/'
        sidecar=json.loads(read(path+'resources.json'));assert sidecar['resource_navigation']==changed['nodes']['chapter:bound']
        assert 'beta' in read(path+'resources.md') or changed['nodes']['chapter:bound']['groups']['methods'][0]['name'][language] in read(path+'resources.md')
        assert changed['nodes']['chapter:bound']['groups']['methods'][0]['name'][language] in read(path+'index.html')
        assert 'First linked method' not in read(path+'index.html') and '最初の関連手法' not in read(path+'index.html')
    assert all(path.read_bytes()==data for path,data in protected.items())
    page('ja','added','New chapter',False)
    (fixture/'numerical-methods-atlas/en/read/static-only/index.html').unlink()
    builder.build(fixture,navigation=changed)
    latest=json.loads(read('numerical-methods-atlas/reading-resources.json'))
    assert 'added' in latest['chapters'] and 'static-only' not in latest['chapters'],'Physical inventory edits must update records without hand-pinned IDs'
    assert latest['chapters']['added']['association_status']=='directory-only'
    assert 'ghost' not in read('numerical-methods-atlas/chapter-resources.mjs')
print('chapter resources preserve articles and update idempotently')
`,fileURLToPath(root)],{encoding:'utf8',maxBuffer:3*1024*1024});
  assert.match(output,/chapter resources preserve articles and update idempotently/);
});

test('the real-site builder never writes SPA content or legacy scientific JSON and Markdown',()=>{
  const output=execFileSync(python,['-B','-c',bootstrap+String.raw`
import builtins,os,re
from unittest.mock import patch
navigation=load_search_routes(root);writes={}
def capture(path,value,*args,**kwargs):
    path=path.resolve();relative=path.relative_to(root).as_posix()
    assert not re.fullmatch(r'numerical-methods-atlas/content(?:\.(?:ja|en))?[.]json',relative),'SPA content write: '+relative
    assert not re.fullmatch(r'numerical-methods-atlas/(?:ja|en)/read/[^/]+/index[.](?:json|md)',relative),'Legacy chapter download write: '+relative
    writes[path]=value
    return len(value)
old_open=builtins.open
def read_only_open(file,mode='r',*args,**kwargs):
    assert not any(char in mode for char in 'wax+'),'Uncaptured filesystem mutation: '+str(file)
    return old_open(file,mode,*args,**kwargs)
with patch.object(pathlib.Path,'write_text',capture),patch.object(pathlib.Path,'write_bytes',capture),patch.object(pathlib.Path,'mkdir'),patch.object(pathlib.Path,'unlink',side_effect=AssertionError('Unexpected deletion in real-site write guard')),patch.object(builtins,'open',read_only_open):
    builder.build(root,navigation=navigation)
for language in ['ja','en']:
    for page in (root/'numerical-methods-atlas'/language/'read').glob('*/index.html'):
        before=page.read_text();after=writes.get(page,before)
        assert re.findall(r'<article\b[^>]*>.*?</article>',before,re.S)==re.findall(r'<article\b[^>]*>.*?</article>',after,re.S),'Article mutation: '+str(page)
        assert re.findall(r'<aside\b[^>]*class="chapter-toc"[^>]*>.*?</aside>',before,re.S)==re.findall(r'<aside\b[^>]*class="chapter-toc"[^>]*>.*?</aside>',after,re.S),'Original contents mutation: '+str(page)
print('protected chapter content write guard checked')
`,fileURLToPath(root)],{encoding:'utf8',maxBuffer:3*1024*1024});
  assert.match(output,/protected chapter content write guard checked/);
});
