import test from 'node:test';
import assert from 'node:assert/strict';
import {existsSync,readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const root=new URL('../',import.meta.url),origin='https://hrkoyama.github.io';
const read=path=>readFileSync(new URL(path,root),'utf8'),json=path=>JSON.parse(read(path));
const sha=path=>createHash('sha256').update(readFileSync(new URL(path,root))).digest('hex');
const byId=rows=>new Map(rows.map(row=>[row.id,row])),sorted=rows=>[...rows].sort();
const common=json('catalog/atlas-execution-examples.json'),discovery=json('catalog/atlas-execution-discovery.json');
const expansion=json('catalog/atlas-depth-expansion.json'),methods=byId(json('catalog/atlas-methods.json').methods);
const equations=byId(json('catalog/atlas-equations.json').equations),bindings=byId(json('catalog/atlas-problem-links.json').problems);
const previews=byId(json('numerical-methods-atlas/gallery/preview-manifest.json').items);
const supplements=expansion.groups.flatMap(group=>{
  const base=`code/validated-examples/${group.edition||expansion.edition}/${group.id}/`,metadata=json(base+'cases.json');
  return (Array.isArray(metadata)?metadata:metadata.cases).map(item=>({item,base,group:group.id}));
});
const commonById=byId(common.examples),supplementById=new Map(supplements.map(row=>[row.item.id,row]));
const python=process.env.ATLAS_INDEX_PYTHON||'python3';
const bootstrap=String.raw`
import json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve();sys.path.insert(0,str(root/'scripts'))
import atlas_execution_routes as module
from atlas_execution_routes import load_execution_routes
`;
const navigation=JSON.parse(execFileSync(python,['-B','-c',bootstrap+'\nprint(json.dumps(load_execution_routes(root)))',fileURLToPath(root)],{encoding:'utf8',maxBuffer:12*1024*1024}));
const decode=value=>value.replaceAll('&amp;','&').replaceAll('&quot;','"').replaceAll('&#x27;',"'").replaceAll('&#39;',"'").replaceAll('&lt;','<').replaceAll('&gt;','>');
const text=html=>decode(html.replace(/<[^>]+>/g,'')).replace(/\s+/g,' ').trim();
const attrs=tag=>Object.fromEntries([...tag.matchAll(/([\w:-]+)="([^"]*)"/g)].map(match=>[match[1],decode(match[2])]));
function blocks(html,attribute,value){
  const result=[];
  for(const opening of html.matchAll(/<([a-z][\w:-]*)\b[^>]*>/gi)){
    const properties=attrs(opening[0]);
    if(new RegExp('\\s'+attribute+'(?=\\s|/?>)').test(opening[0]))properties[attribute]??='';
    if(!(attribute in properties)||(value!==undefined&&properties[attribute]!==value))continue;
    const tags=new RegExp('</?'+opening[1]+'\\b[^>]*>','gi');tags.lastIndex=opening.index+opening[0].length;
    let depth=1,closing;while((closing=tags.exec(html))){depth+=closing[0].startsWith('</')?-1:1;if(!depth)break;}
    assert.ok(closing,'balanced '+attribute);
    result.push({attributes:properties,body:html.slice(opening.index+opening[0].length,closing.index)});
  }
  return result;
}
const links=html=>[...html.matchAll(/<a\b[^>]*href="([^"]+)"[^>]*>/g)].map(match=>decode(match[1]));
function local(href,{fragment=true}={}){
  const url=new URL(href,origin);assert.equal(url.origin,origin,href);
  const path=url.pathname.slice(1)+(url.pathname.endsWith('/')?'index.html':'');
  assert.ok(existsSync(new URL(path,root)),href);
  if(fragment&&url.hash&&!url.hash.startsWith('#/')&&path.endsWith('.html'))assert.ok(read(path).includes(`id="${decodeURIComponent(url.hash.slice(1))}"`),href);
  return url;
}
const entryPath=route=>route.kind==='common'?`numerical-methods-atlas/code-and-data/examples/${route.id}/`:`numerical-methods-atlas/validation/${route.id}/`;

test('execution routes cover only the explicit common and supplemental source cases, with exact methods and scoped formulas',()=>{
  assert.deepEqual(sorted(Object.keys(navigation.executions)),sorted([...common.examples.map(row=>row.id),...Object.keys(expansion.case_problem_ids)]));
  assert.deepEqual(sorted(supplements.map(row=>row.item.id)),sorted(Object.keys(expansion.case_problem_ids)));
  for(const route of Object.values(navigation.executions)){
    const source=route.kind==='common'?commonById.get(route.id):supplementById.get(route.id).item;
    assert.ok(source,route.id);assert.deepEqual(route.name,source.name||source.title);
    assert.deepEqual(route.methods.map(row=>row.id),source.method_ids,route.id+' does not borrow related problem methods');
    for(const method of route.methods){
      assert.deepEqual(method.name,methods.get(method.id).name);assert.equal(method.status,'educational-example');
      for(const language of ['ja','en'])assert.equal(method.url[language],`${origin}/numerical-methods-atlas/methods/${method.id}/?lang=${language}`);
    }
    const problemId=route.kind==='common'?source.problem_id:expansion.case_problem_ids[route.id];
    assert.equal(route.problem?.id??null,problemId);
    const direct=route.kind==='common'?discovery.examples.find(row=>row.id===route.id):null;
    assert.deepEqual(route.equations.map(row=>row.id),direct?.equation_ids||[]);
    for(const equation of route.equations)assert.deepEqual(equation.name,equations.get(equation.id).name);
    assert.equal(route.formulation.role,direct?.formula.role||(problemId?'example-definition':'diagnostic'));
    assert.deepEqual(route.formulation.latex,direct?.formula.latex||source.formulas||source.equations||[]);
    assert.deepEqual(route.formulation.note,direct?.formula.note||source.algorithm);
    for(const language of ['ja','en']){
      const target=new URL(route.formulation.url[language]);
      assert.equal(target.searchParams.get('lang'),language);
      assert.equal(target.pathname,route.kind==='common'?'/numerical-methods-atlas/equations/':`/numerical-methods-atlas/validation/${route.id}/`);
      assert.equal(target.hash,route.kind==='common'?`#execution-${route.id}-${language}`:`#${route.id}-${language}-algorithm`);
      assert.equal(route.references.url[language],`${origin}/${entryPath(route)}?lang=${language}#${route.id}-${language}-validation`);
      assert.ok(route.references.note[language]?.trim());
    }
    const expectedReferences=problemId?bindings.get(problemId).references:[];
    assert.deepEqual(route.references.cases.map(row=>row.id),expectedReferences.map(row=>row.id));
    for(const reference of route.references.cases){
      const original=expectedReferences.find(row=>row.id===reference.id);
      assert.equal(reference.relation,original.relation);assert.deepEqual(reference.note,original.note);
      for(const language of ['ja','en']){
        assert.ok(reference.title[language]?.trim());
        assert.equal(reference.url[language],`${origin}/numerical-methods-atlas/solutions/?lang=${language}#solution-${reference.id}-${language}`);
      }
    }
    if(route.kind==='supplement')assert.deepEqual(route.references.note,source.validation,'the saved case validation stays separate from related model references');
  }
});

test('representative problem pictures and each supplement’s own validation figures remain distinct',()=>{
  for(const route of Object.values(navigation.executions)){
    const figure=route.figure,url=local(figure.url,{fragment:false}),path=url.pathname.slice(1),raw=readFileSync(new URL(path,root));
    assert.equal(figure.sha256,sha(path));assert.ok(figure.width>0&&figure.height>0);
    assert.deepEqual([...raw.subarray(0,8)],[137,80,78,71,13,10,26,10]);
    assert.equal(raw.readUInt32BE(16),figure.width);assert.equal(raw.readUInt32BE(20),figure.height);
    if(route.kind==='common'){
      const preview=previews.get(route.problem.id);
      assert.equal(figure.kind,'problem-representative');assert.equal(url.pathname,preview.image);
      assert.deepEqual(figure.caption,preview.caption);assert.equal(figure.source_kind,preview.source_kind);
    }else{
      const source=supplementById.get(route.id);
      assert.equal(figure.kind,'case-validation');assert.equal(url.pathname,'/'+source.base+'results/'+route.id+'.png');
      assert.equal(navigation.source_sha256[path],figure.sha256);
    }
  }
  const controls=Object.entries(expansion.case_problem_ids).filter(([,id])=>id===null).map(([id])=>id);
  assert.ok(controls.length>0);
  for(const id of controls){
    const route=navigation.executions[id];assert.equal(route.problem,null);assert.deepEqual(route.equations,[]);
    assert.deepEqual(route.references.cases,[]);assert.equal(route.formulation.role,'diagnostic');assert.equal(route.figure.kind,'case-validation');
  }
  assert.deepEqual(navigation.executions.sod.methods.map(row=>row.id),commonById.get('sod').method_ids);
  assert.ok(navigation.executions.sod.methods.some(row=>row.id==='hllc'));
  assert.ok(!navigation.executions.sod.methods.some(row=>row.id==='weno-z'));
  assert.deepEqual(navigation.executions.bratu.methods.map(row=>row.id),['newton']);
  assert.deepEqual(navigation.executions['h2-rhf'].equations.map(row=>row.id),['hartree-fock-model']);
  assert.ok(bindings.get(commonById.get('h2-rhf').problem_id).equation_ids.includes('stationary-schrodinger'),'the related model exists but is not promoted to the execution formula');
});

test('new entry and chooser metadata preserves original scientific records and shares exactly the source navigation graph',()=>{
  const chooser=json('numerical-methods-atlas/code-and-data/examples/index.json'),depth=json('numerical-methods-atlas/validation/index.json');
  assert.equal(sha('numerical-methods-atlas/code-and-data/examples.json'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
  assert.deepEqual(chooser.navigation_source_sha256,navigation.source_sha256);assert.deepEqual(depth.navigation_source_sha256,navigation.source_sha256);
  assert.deepEqual(sorted(Object.keys(chooser.execution_navigation)),sorted(common.examples.map(row=>row.id)));
  for(const route of Object.values(navigation.executions)){
    const record=json(entryPath(route)+'index.json');
    assert.deepEqual(record.execution_navigation,route);assert.deepEqual(record.navigation_source_sha256,navigation.source_sha256);
    if(route.kind==='common'){
      for(const [key,value]of Object.entries(commonById.get(route.id)))assert.deepEqual(record[key],value,route.id+'/'+key);
      assert.deepEqual(chooser.execution_navigation[route.id],route);
      assert.equal(record.registry_sha256,sha('numerical-methods-atlas/code-and-data/examples.json'));
      assert.equal(record.public_rerun.passed,true);
    }else{
      const {item,base}=supplementById.get(route.id);
      for(const [key,value]of Object.entries(item))assert.deepEqual(record[key],value,route.id+'/'+key);
      assert.deepEqual(record.measured,json(base+'results/result.json').cases.find(row=>row.id===route.id));
      assert.deepEqual(depth.cases.find(row=>row.id===route.id).execution_navigation,route);
    }
  }
});

test('every bilingual execution page displays four scoped destinations with actual links, its own figure and visible reference caveats',()=>{
  for(const route of Object.values(navigation.executions)){
    const html=read(entryPath(route)+'index.html'),markdown=read(entryPath(route)+'index.md');
    for(const language of ['ja','en']){
      const edition=blocks(html,'data-site-language',language)[0];assert.ok(edition,route.id+'/'+language);
      const panels=blocks(edition.body,'data-execution-navigation',route.id);assert.equal(panels.length,1);
      const panel=panels[0],cards=blocks(panel.body,'data-execution-navigation-card');
      assert.match(panel.attributes.class,/\bexecution-resource-navigation\b/);assert.equal(panel.attributes.role,'group');assert.ok(panel.attributes['aria-label']);
      assert.deepEqual(cards.map(card=>card.attributes['data-execution-navigation-card']),['methods','equations','figure','references']);
      const card=key=>cards.find(row=>row.attributes['data-execution-navigation-card']===key).body;
      assert.deepEqual(blocks(card('methods'),'data-execution-method-id').map(row=>row.attributes['data-execution-method-id']),route.methods.map(row=>row.id));
      assert.deepEqual(blocks(card('methods'),'data-execution-method-link').map(row=>row.attributes.href),route.methods.map(row=>row.url[language]));
      assert.equal(blocks(card('equations'),'data-execution-formulation-link')[0]?.attributes.href,route.formulation.url[language]);
      assert.deepEqual(blocks(card('equations'),'data-execution-equation-id').map(row=>row.attributes['data-execution-equation-id']),route.equations.map(row=>row.id));
      assert.deepEqual(blocks(card('equations'),'data-execution-equation-link').map(row=>row.attributes.href),route.equations.map(row=>row.url[language]));
      assert.ok(text(card('equations')).includes(route.formulation.note[language].replace(/\s+/g,' ').trim()),route.id+'/'+language+' exact formulation scope');
      assert.equal(blocks(card('figure'),'data-execution-figure-link')[0]?.attributes.href,route.figure.url);
      const image=attrs(card('figure').match(/<img\b[^>]*>/)?.[0]||'');
      assert.equal(image.src,route.figure.url);assert.equal(image.width,String(route.figure.width));assert.equal(image.height,String(route.figure.height));assert.ok(image.alt);
      const problemLinks=blocks(card('figure'),'data-execution-problem-link'),codeLinks=blocks(card('figure'),'data-execution-problem-code');
      assert.deepEqual(problemLinks.map(row=>row.attributes.href),route.problem?[route.problem.hub[language]]:[]);
      assert.deepEqual(codeLinks.map(row=>row.attributes.href),route.problem?[route.problem.code[language]]:[]);
      assert.equal(blocks(card('references'),'data-execution-validation-link')[0]?.attributes.href,route.references.url[language]);
      assert.ok(text(card('references')).includes(route.references.note[language].replace(/\s+/g,' ').trim()),route.id+'/'+language+' exact validation scope');
      const references=blocks(card('references'),'data-execution-reference-id');
      assert.deepEqual(references.map(row=>row.attributes['data-execution-reference-id']),route.references.cases.map(row=>row.id));
      for(const reference of references){
        const original=route.references.cases.find(row=>row.id===reference.attributes['data-execution-reference-id']);
        assert.equal(reference.attributes['data-reference-relation'],original.relation);
        assert.equal(blocks(reference.body,'data-execution-reference-link')[0]?.attributes.href,original.url[language]);
        assert.ok(text(reference.body).includes(original.note[language].replace(/\s+/g,' ').trim()),route.id+'/'+language+' exact related-reference scope');
        assert.doesNotMatch(reference.body,/<details\b/,'related-model limitations remain beside their reference link');
      }
      for(const href of links(panel.body)){local(href);assert.ok(markdown.includes(href),route.id+' Markdown navigation parity: '+href);}
      assert.ok(markdown.includes(route.formulation.note[language]));assert.ok(markdown.includes(route.references.note[language]));
      for(const formula of route.formulation.latex)assert.ok(markdown.includes(formula),route.id+' Markdown retains exact scoped formula');
      if(route.figure.kind==='problem-representative')assert.match(text(card('figure')),language==='ja'?/代表図.*異なる場合/:/representative figure.*may differ/);
      else assert.match(text(card('figure')),language==='ja'?/この実行例で保存した検証図/:/saved validation figure for this execution/);
      if(!route.problem)assert.match(text(card('figure')),language==='ja'?/別の物理テスト問題を割り当てていません/:/No separate physical test problem is assigned/);
    }
  }
});

test('the shared guide and both choosers expose the same complete navigation without changing their execution inventories',()=>{
  const locations=[
    {path:'numerical-methods-atlas/code-and-data/index.html',ids:common.examples.map(row=>row.id)},
    {path:'numerical-methods-atlas/code-and-data/examples/index.html',ids:common.examples.map(row=>row.id)},
    {path:'numerical-methods-atlas/validation/index.html',ids:supplements.map(row=>row.item.id)}
  ];
  for(const {path,ids}of locations)for(const language of ['ja','en']){
    const edition=blocks(read(path),'data-site-language',language)[0];assert.ok(edition,path+'/'+language);
    const panels=blocks(edition.body,'data-execution-navigation');
    assert.deepEqual(sorted(panels.map(panel=>panel.attributes['data-execution-navigation'])),sorted(ids),path+'/'+language);
    for(const panel of panels){
      const route=navigation.executions[panel.attributes['data-execution-navigation']];
      assert.deepEqual(blocks(panel.body,'data-execution-navigation-card').map(card=>card.attributes['data-execution-navigation-card']),['methods','equations','figure','references']);
      for(const method of route.methods)assert.ok(links(panel.body).includes(method.url[language]));
      assert.ok(links(panel.body).includes(route.references.url[language]));
    }
  }
});

test('all navigation source hashes are current and loading works before any derived indexes or execution pages exist',()=>{
  for(const [path,hash]of Object.entries(navigation.source_sha256))assert.equal(sha(path),hash,path);
  for(const path of ['catalog/atlas-execution-discovery.json','catalog/atlas-depth-expansion.json','catalog/atlas-methods.json','catalog/atlas-equations.json'])assert.ok(navigation.source_sha256[path],path);
  const output=execFileSync(python,['-B','-c',bootstrap+String.raw`
from unittest.mock import patch
forbidden={root/'numerical-methods-atlas/equations/index.json',root/'numerical-methods-atlas/solutions/index.json',root/'numerical-methods-atlas/test-cases/index.json'}
directories=[root/'numerical-methods-atlas/methods',root/'numerical-methods-atlas/problems',root/'numerical-methods-atlas/code-and-data/examples',root/'numerical-methods-atlas/validation']
old_bytes=pathlib.Path.read_bytes;old_text=pathlib.Path.read_text
def guard(path):
    path=path.resolve()
    assert path not in forbidden and not any(path.is_relative_to(directory) for directory in directories),'Generated execution dependency: '+str(path)
def read_bytes(path):guard(path);return old_bytes(path)
def read_text(path,*args,**kwargs):guard(path);return old_text(path,*args,**kwargs)
with patch.object(pathlib.Path,'read_bytes',read_bytes),patch.object(pathlib.Path,'read_text',read_text):routes=load_execution_routes(root)
expected=set(json.loads((root/'catalog/atlas-depth-expansion.json').read_text())['case_problem_ids'])|{row['id'] for row in json.loads((root/'catalog/atlas-execution-examples.json').read_text())['examples']}
assert set(routes['executions'])==expected
print('source-first execution loading checked')
`,fileURLToPath(root)],{encoding:'utf8'});
  assert.match(output,/source-first execution loading checked/);
});

test('small loader fixtures add and remove explicit bindings without name, model or unrelated-method inference',()=>{
  const output=execFileSync(python,['-B','-c',bootstrap+String.raw`
import base64,copy,tempfile
from unittest.mock import patch
note={'ja':'限定した条件','en':'Scoped conditions'}
name={'ja':'同名','en':'Same name'}
with tempfile.TemporaryDirectory(prefix='atlas-execution-routes-') as directory:
    fixture=pathlib.Path(directory)
    def write(path,value):
        destination=fixture/path;destination.parent.mkdir(parents=True,exist_ok=True);destination.write_text(json.dumps(value))
    catalog={'problems':[{'id':'one','references':[{'id':'ref','relation':'related-model','note':note}]},{'id':'two','references':[]}]}
    method_records={'methods':[{'id':ident,'name':name,'status':'planned' if ident=='planned' else 'educational-example'} for ident in ['alpha','beta','planned']]}
    write('catalog/atlas-problem-links.json',catalog);write('catalog/atlas-methods.json',method_records)
    write('catalog/atlas-equations.json',{'equations':[{'id':ident,'name':name} for ident in ['direct','related']]})
    write('numerical-methods-atlas/assets/reference-solutions.json',{'cases':[{'id':'ref','title':'Reference','kind':'analytic'}]})
    write('numerical-methods-atlas/locales/messages.json',{'reference':{'ja':'参照','en':'Reference'}})
    expansion={'case_problem_ids':{'bound':'one','control':None}};write('catalog/atlas-depth-expansion.json',expansion)
    cards={ident:{'id':ident,'name':name,'model':'same-model','image':{'url':'/'+ident+'.png'},'executions':[{'id':'unrelated','method_ids':['beta']}]} for ident in ['one','two']}
    graph={'problems':cards,'source_sha256':{}}
    discovery={'examples':[{'id':'common','problem_id':'one','equation_ids':['direct'],'formula':{'role':'problem','latex':['x=1'],'note':note},'execution':{'name':name,'method_ids':['alpha'],'reference_notes':note}}]}
    supplements=[{'id':ident,'title':name,'method_ids':['alpha'],'download':'/code/fixture/group/archive.zip','formulas':['q=0'],'algorithm':note,'validation':note,'source_sha256':{}} for ident in ['bound','control']]
    for case in supplements:
        image=fixture/('code/fixture/group/results/'+case['id']+'.png');image.parent.mkdir(parents=True,exist_ok=True)
        image.write_bytes(base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+j5WQAAAAASUVORK5CYII='))
    original=copy.deepcopy((catalog,graph,discovery,supplements))
    with patch.object(module,'load_problem_routes',return_value=graph),patch.object(module,'load_discovery',return_value=discovery),patch.object(module,'load_supplemental_examples',return_value=supplements):
        routes=load_execution_routes(fixture)['executions']
        assert [row['id'] for row in routes['common']['methods']]==['alpha']
        assert [row['id'] for row in routes['common']['equations']]==['direct']
        assert routes['bound']['equations']==[] and routes['bound']['formulation']['role']=='example-definition'
        assert routes['control']['problem'] is None
        assert routes['control']['references']['cases']==[] and routes['control']['formulation']['role']=='diagnostic'
        assert routes['common']['references']['cases'][0]['note']==note
        assert (catalog,graph,discovery,supplements)==original,'Loader mutated scientific source inputs'
        discovery['examples'][0]['problem_id']='two';discovery['examples'][0]['equation_ids']=[]
        discovery['examples'][0]['execution']['method_ids']=['beta']
        expansion['case_problem_ids']['bound']=None;write('catalog/atlas-depth-expansion.json',expansion)
        changed=load_execution_routes(fixture)['executions']
        assert changed['common']['problem']['id']=='two' and changed['common']['references']['cases']==[]
        assert changed['common']['equations']==[] and [row['id'] for row in changed['common']['methods']]==['beta']
        assert changed['bound']['problem'] is None and changed['bound']['references']['cases']==[]
        assert changed['bound']['figure']==routes['bound']['figure'],'Own validation picture survives removing a physical binding'
        for invalid in [['unknown'],['alpha','alpha'],['planned'],[]]:
            discovery['examples'][0]['execution']['method_ids']=invalid
            try:load_execution_routes(fixture)
            except ValueError:pass
            else:raise AssertionError('Invalid method IDs accepted: '+str(invalid))
        discovery['examples'][0]['execution']['method_ids']=['alpha'];discovery['examples'][0]['problem_id']='absent'
        try:load_execution_routes(fixture)
        except ValueError:pass
        else:raise AssertionError('Unknown physical problem accepted')
        discovery['examples'][0]['problem_id']='one'
        (fixture/'code/fixture/group/results/control.png').write_bytes(b'invalid image')
        try:load_execution_routes(fixture)
        except ValueError:pass
        else:raise AssertionError('Invalid validation figure accepted')
print('small execution route mutations checked')
`,fileURLToPath(root)],{encoding:'utf8'});
  assert.match(output,/small execution route mutations checked/);
});
