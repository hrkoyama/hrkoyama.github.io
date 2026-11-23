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
const catalog=json('catalog/atlas-problem-links.json');
const equationSource=json('catalog/atlas-equations.json').equations;
const referenceSource=[...json('numerical-methods-atlas/assets/reference-solutions.json').cases,...json('catalog/atlas-reference-supplements.json').cases];
const inventory=json('catalog/atlas-test-problems.json').problems;
const hubs=byId(json('numerical-methods-atlas/problems/index.json').problems);
const pictures=byId(json('numerical-methods-atlas/gallery/preview-manifest.json').items);
const published={equations:json('numerical-methods-atlas/equations/index.json'),references:json('numerical-methods-atlas/solutions/index.json')};
const python=process.env.ATLAS_INDEX_PYTHON||'python3';
const importHelper=String.raw`
import json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve();sys.path.insert(0,str(root/'scripts'))
from atlas_problem_routes import load_problem_routes,invert_problem_routes
`;
const routes=JSON.parse(execFileSync(python,['-B','-c',importHelper+'\nprint(json.dumps(load_problem_routes(root)))',fileURLToPath(root)],{encoding:'utf8',maxBuffer:8*1024*1024}));

function blocks(html,attribute,value){
  const found=[];
  for(const opening of html.matchAll(/<([a-z][\w:-]*)\b[^>]*>/gi)){
    const properties=attrs(opening[0]);
    if(new RegExp('\\s'+attribute+'(?=\\s|/?>)').test(opening[0]))properties[attribute]??='';
    if(!(attribute in properties)||(value!==undefined&&properties[attribute]!==value))continue;
    const tags=new RegExp('</?'+opening[1]+'\\b[^>]*>','gi');tags.lastIndex=opening.index+opening[0].length;
    let depth=1,closing;while((closing=tags.exec(html))){depth+=closing[0].startsWith('</')?-1:1;if(!depth)break;}
    assert.ok(closing,'balanced '+attribute);
    found.push({attributes:properties,opening:opening[0],start:opening.index,end:tags.lastIndex,body:html.slice(opening.index+opening[0].length,closing.index)});
  }
  return found;
}
function links(html){return [...html.matchAll(/<a\b[^>]*href="([^"]+)"[^>]*>/g)].map(match=>decode(match[1]));}
function local(value){
  const url=new URL(value,origin);assert.equal(url.origin,origin,value);
  const path=url.pathname.slice(1)+(url.pathname.endsWith('/')?'index.html':'');
  assert.ok(existsSync(new URL(path,root)),value);
  if(url.hash&&!url.hash.startsWith('#/')&&path.endsWith('.html'))assert.ok(read(path).includes(`id="${decodeURIComponent(url.hash.slice(1))}"`),value);
  return url.href;
}
function removeBlocks(html,entries){for(const entry of [...entries].reverse())html=html.slice(0,entry.start)+html.slice(entry.end);return html;}
function localeMarkdown(markdown,language){
  const headings=[...markdown.matchAll(/^## (日本語|English)\s*$/gm)];
  const index=headings.findIndex(match=>match[1]===(language==='ja'?'日本語':'English'));assert.ok(index>=0);
  return markdown.slice(headings[index].index,headings[index+1]?.index);
}
function recordMarkdown(markdown,records,index,language,titleKey){
  const locale=localeMarkdown(markdown,language),heading=row=>'### '+row[titleKey][language]+'\n';
  const start=locale.indexOf(heading(records[index]));assert.ok(start>=0);
  const end=index+1<records.length?locale.indexOf(heading(records[index+1]),start+1):locale.length;assert.ok(end>=start);
  return locale.slice(start,end);
}

test('source inversion includes every equation/reference key and only its explicitly reviewed problem edges',()=>{
  for(const page of ['equations','solutions'])assert.match(read(`numerical-methods-atlas/${page}/index.html`),/<body\b[^>]*data-site-language-anchors="suffix"/,'language switching retains the matching localized card anchor');
  for(const [kind,source,records]of [['equations',equationSource,published.equations.equations],['references',referenceSource,published.references.cases]]){
    assert.deepEqual(Object.keys(routes[kind]).sort(),source.map(row=>row.id).sort());
    for(const record of records){
      const expected=catalog.problems.filter(problem=>kind==='equations'?problem.equation_ids.includes(record.id):problem.references.some(edge=>edge.id===record.id));
      assert.deepEqual(routes[kind][record.id].map(row=>row.id),expected.map(row=>row.id));
      assert.deepEqual(record.related_problems,routes[kind][record.id],kind+'/'+record.id+' published data is current');
      assert.equal(new Set(record.related_problems.map(row=>row.id)).size,expected.length);
      if(kind==='references')for(const card of record.related_problems){
        const edge=expected.find(row=>row.id===card.id).references.find(edge=>edge.id===record.id);
        assert.equal(card.relation,edge.relation);assert.deepEqual(card.note,edge.note);
      }
    }
  }
  assert.deepEqual(published.equations.problem_routes_source_sha256,routes.source_sha256);
  assert.deepEqual(published.references.problem_routes_source_sha256,routes.source_sha256);
  assert.equal(published.references.source_sha256,sha('numerical-methods-atlas/assets/reference-solutions.json'));
  for(const [path,hash]of Object.entries(routes.source_sha256))assert.equal(sha(path),hash,path);
});

test('reverse cards retain actual saved images, hub/code anchors and exactly the original verified executions',()=>{
  assert.deepEqual(Object.keys(routes.problems).sort(),inventory.map(row=>row.id).sort());
  for(const card of Object.values(routes.problems)){
    const source=hubs.get(card.id),picture=pictures.get(card.id);
    assert.deepEqual(card.name,source.name);
    assert.equal(local(card.image.url),local(picture.image));
    assert.equal(card.image.sha256,picture.image_sha256);assert.equal(sha(new URL(card.image.url).pathname.slice(1)),picture.image_sha256);
    for(const field of ['width','height','caption','source_kind'])assert.deepEqual(card.image[field],picture[field]);
    assert.deepEqual(card.executions.map(row=>row.id),source.executions.map(row=>row.id));
    for(const execution of card.executions){
      const original=source.executions.find(row=>row.id===execution.id);
      for(const field of ['id','kind','name','guide','input','download','verification','scope'])assert.deepEqual(execution[field],original[field],card.id+'/'+field);
      for(const url of [execution.input,execution.download,execution.verification,...Object.values(execution.guide)])local(url);
    }
    for(const language of ['ja','en']){
      assert.equal(local(card.hub[language]),`${origin}/numerical-methods-atlas/problems/${card.id}/?lang=${language}`);
      assert.equal(local(card.code[language]),card.hub[language]+'#code-'+language);
    }
  }
});

function assertRenderedRoutes(wrapper,rows,language){
  const children=blocks(wrapper.body,'data-linked-problem-id');
  assert.deepEqual(children.map(child=>child.attributes['data-linked-problem-id']),rows.map(row=>row.id));
  const overflow=blocks(wrapper.body,'class').filter(block=>block.attributes.class.split(/\s+/).includes('problem-routes-more'));
  assert.equal(overflow.length,rows.length>3?1:0);
  assert.ok(overflow.every(block=>!/(?:\s)open(?:\s|=|>)/.test(block.opening)));
  assert.deepEqual(blocks(removeBlocks(wrapper.body,overflow),'data-linked-problem-id').map(row=>row.attributes['data-linked-problem-id']),rows.slice(0,3).map(row=>row.id));
  if(!rows.length){
    assert.ok(text(wrapper.body).includes(language==='ja'?'この項目に対応付けられたテスト問題は未登録です。':'No associated test problem is registered for this entry.'));
    assert.doesNotMatch(wrapper.body,/<img\b/);assert.deepEqual(links(wrapper.body),[]);
  }
  for(const [index,child]of children.entries()){
    const row=rows[index],picture=blocks(child.body,'data-problem-picture'),name=blocks(child.body,'data-problem-name'),code=blocks(child.body,'data-problem-code');
    assert.equal(picture.length,1);assert.equal(name.length,1);assert.equal(code.length,1);
    assert.equal(local(picture[0].attributes.href),row.hub[language]);
    assert.equal(local(name[0].attributes.href),row.hub[language]);assert.equal(text(name[0].body),row.name[language]);
    assert.equal(local(code[0].attributes.href),row.code[language]);
    const image=attrs(picture[0].body.match(/<img\b[^>]*>/)?.[0]||'');
    assert.equal(local(image.src),row.image.url);assert.equal(Number(image.width),row.image.width);assert.equal(Number(image.height),row.image.height);
    const runs=blocks(child.body,'data-linked-execution-id');
    assert.deepEqual(runs.map(run=>run.attributes['data-linked-execution-id']),row.executions.map(run=>run.id));
    for(const [index,run]of runs.entries()){
      const original=row.executions[index];
      assert.deepEqual(blocks(run.body,'data-problem-execution').map(link=>local(link.attributes.href)),[original.guide[language]]);
      assert.deepEqual(blocks(run.body,'data-problem-download').map(link=>local(link.attributes.href)),[original.download]);
    }
    if(!runs.length){
      assert.ok(text(child.body).includes(language==='ja'?'固定入力実行例は未登録です。':'No fixed-input execution example is registered.'));
      assert.equal(blocks(child.body,'data-problem-execution').length+blocks(child.body,'data-problem-download').length,0);
    }
    const allowed=[row.hub[language],row.code[language],...row.executions.flatMap(run=>[run.guide[language],run.download])];
    assert.deepEqual([...new Set(links(child.body).map(local))].sort(),[...new Set(allowed)].sort(),'no unbound run/code destinations');
    if(row.note){
      const notes=blocks(child.body,'class').filter(block=>block.attributes.class.split(/\s+/).includes('problem-route-note'));
      assert.equal(notes.length,1);assert.equal(text(notes[0].body),text(row.note[language]));
      const optional=blocks(child.body,'class').filter(block=>block.attributes.class.split(/\s+/).includes('problem-route-execution-scope'));
      assert.ok(text(removeBlocks(child.body,optional)).includes(text(row.note[language])),'the relation note is outside optional execution scope');
    }
    if(row.relation)assert.ok(text(child.body).includes(row.relation==='related-model'?(language==='ja'?'関連モデルの問題':'Related-model problem'):(language==='ja'?'同じ問題への対応':'Same-problem link')));
  }
}

test('both generated indexes show the precise reverse cards, visible first three, explicit empty states and complete Markdown',()=>{
  for(const [kind,directory,attribute,records,titleKey]of [['equations','equations','data-equation-id',published.equations.equations,'name'],['references','solutions','data-solution-id',published.references.cases,'title']]){
    const html=read(`numerical-methods-atlas/${directory}/index.html`),markdown=read(`numerical-methods-atlas/${directory}/index.md`);
    for(const language of ['ja','en']){
      const edition=blocks(html,'data-site-language',language)[0].body;
      for(const [index,record]of records.entries()){
        const entry=blocks(edition,attribute,record.id);assert.equal(entry.length,1);
        const wrappers=blocks(entry[0].body,'data-problem-routes');assert.equal(wrappers.length,1);
        const rows=routes[kind][record.id];assertRenderedRoutes(wrappers[0],rows,language);
        const md=recordMarkdown(markdown,records,index,language,titleKey);
        const identities=[...md.matchAll(/^#{4,6} .* \(`([^`]+)`\)\s*$/gm)].map(match=>match[1]);
        assert.deepEqual(identities,rows.map(row=>row.id));
        for(const row of rows){
          for(const url of [row.hub[language],row.code[language],row.image.url,...row.executions.flatMap(run=>[run.guide[language],run.download])])assert.ok(md.includes(url));
          if(row.note)assert.ok(md.includes(row.note[language]));
          if(row.relation==='related-model')assert.ok(md.includes(language==='ja'?'関連モデルの問題':'Related-model problem'));
        }
      }
    }
  }
  for(const id of ['euler-vacuum','swe-dry-bed','swe-vacuum','couette'])assert.deepEqual(routes.references[id],[],'a nearby physical model does not fabricate '+id+' correspondences');
  assert.match(JSON.stringify(routes.references['taylor-green'][0].note),/π\/4/);
});

test('the twenty-two fixed-input equation shortcuts link the exact problem picture and retain their original run routes',()=>{
  const discovery=json('catalog/atlas-execution-discovery.json').examples,html=read('numerical-methods-atlas/equations/index.html');
  assert.deepEqual(published.equations.execution_examples.map(row=>row.id),discovery.map(row=>row.id));
  for(const entry of published.equations.execution_examples){
    const original=discovery.find(row=>row.id===entry.id),card=routes.problems[original.problem_id];
    assert.deepEqual(entry.related_problems,[card]);
    for(const language of ['ja','en']){
      const edition=blocks(html,'data-site-language',language)[0].body;
      const shortcut=blocks(edition,'data-execution-equation-id',entry.id)[0];assert.ok(shortcut);
      const picture=blocks(shortcut.body,'data-problem-picture');assert.equal(picture.length,1);
      assert.equal(local(picture[0].attributes.href),card.hub[language]);
      assert.equal(local(attrs(picture[0].body.match(/<img\b[^>]*>/)[0]).src),card.image.url);
      assert.ok(links(shortcut.body).includes(entry.entry[language]));local(entry.entry[language]);
    }
  }
});

test('pure inversion responds immediately to added/deleted reviewed edges and never infers matches from equal names or models',()=>{
  const output=execFileSync(python,['-B','-c',importHelper+String.raw`
import copy
problems={key:{'id':key,'name':{'ja':'同名','en':'Same name'},'model':'same-model'} for key in ['one','two','three']}
note={'ja':'条件は異なる','en':'Conditions differ'}
catalog={'problems':[{'id':'one','equation_ids':['eq-a'],'references':[{'id':'ref-a','relation':'related-model','note':note}]},{'id':'two','equation_ids':[],'references':[]},{'id':'three','equation_ids':['eq-b'],'references':[]}]}
before=copy.deepcopy((catalog,problems))
result=invert_problem_routes(catalog,problems,['eq-a','eq-b','eq-empty'],['ref-a','ref-empty'])
assert [row['id'] for row in result['equations']['eq-a']]==['one']
assert [row['id'] for row in result['references']['ref-a']]==['one']
assert result['equations']['eq-empty']==result['references']['ref-empty']==[]
assert result['references']['ref-a'][0]['relation']=='related-model'
assert result['references']['ref-a'][0]['note']==note
assert (catalog,problems)==before
catalog['problems'][1]['equation_ids']=['eq-a']
catalog['problems'][1]['references']=copy.deepcopy(catalog['problems'][0]['references'])
catalog['problems'][0]['equation_ids']=[];catalog['problems'][0]['references']=[]
changed=invert_problem_routes(catalog,problems,['eq-a','eq-b','eq-empty'],['ref-a','ref-empty'])
assert [row['id'] for row in changed['equations']['eq-a']]==['two']
assert [row['id'] for row in changed['references']['ref-a']]==['two']
mutations=["data['problems'][0]['equation_ids']=['unknown']","data['problems'][1]['equation_ids'].append('eq-a')","data['problems'][1]['references'][0]['id']='unknown'","data['problems'][1]['references'].append(copy.deepcopy(data['problems'][1]['references'][0]))","del data['problems'][1]['references'][0]['note']['en']","data['problems'].pop()"]
for mutation in mutations:
    data=copy.deepcopy(catalog);exec(mutation)
    try:invert_problem_routes(data,problems,['eq-a','eq-b','eq-empty'],['ref-a','ref-empty'])
    except ValueError:pass
    else:raise AssertionError('Accepted invalid inverse edge: '+mutation)
print('pure inverse edge mutations checked')
`,fileURLToPath(root)],{encoding:'utf8'});
  assert.match(output,/pure inverse edge mutations checked/);
});

test('the reverse loader works before generated equation/reference indexes or problem hubs are read',()=>{
  const output=execFileSync(python,['-B','-c',importHelper+String.raw`
from unittest.mock import patch
forbidden={root/'numerical-methods-atlas/equations/index.json',root/'numerical-methods-atlas/solutions/index.json'}
hub_root=root/'numerical-methods-atlas/problems'
old_bytes=pathlib.Path.read_bytes;old_text=pathlib.Path.read_text
def guard(path):
    path=path.resolve()
    assert path not in forbidden and not path.is_relative_to(hub_root),'Circular generated input: '+str(path)
def read_bytes(path):guard(path);return old_bytes(path)
def read_text(path,*args,**kwargs):guard(path);return old_text(path,*args,**kwargs)
with patch.object(pathlib.Path,'read_bytes',read_bytes),patch.object(pathlib.Path,'read_text',read_text):
    routes=load_problem_routes(root)
assert len(routes['problems'])==len(json.loads((root/'catalog/atlas-test-problems.json').read_text())['problems'])
print('independent reverse source loading checked')
`,fileURLToPath(root)],{encoding:'utf8'});
  assert.match(output,/independent reverse source loading checked/);
});
