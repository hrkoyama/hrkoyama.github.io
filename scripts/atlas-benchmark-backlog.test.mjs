import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {backlogMatches,wireBenchmarkBacklog} from '../numerical-methods-atlas/benchmark-backlog.mjs';

const root=new URL('../',import.meta.url);
const records=[
 {id:'noh',field_id:'fluid',priority:'P1',state:'in-progress',kind:'implementation',title:{ja:'Nohの衝撃波'},current:'cold gas',tasks:['原点過熱を検査']},
 {id:'weno',field_id:'fluid',priority:'P2',state:'planned',kind:'extension',title:{ja:'WENOの拡充'},current:'実装済み',tasks:['臨界点の収束']},
 {id:'citations',field_id:'shared',priority:'P0',state:'planned',kind:'references',title:{ja:'出典を整える'},current:'原著と参考資料',tasks:['書誌を照合']},
];
test('filters retain the distinction between unstarted work and already implemented extensions',()=>{
 assert.ok(backlogMatches(records[1],{state:'planned',kind:'extension'}));
 assert.ok(!backlogMatches(records[1],{kind:'implementation'}));
 assert.deepEqual(records.filter(record=>backlogMatches(record,{field:'fluid',priority:'P1',state:'in-progress'})).map(record=>record.id),['noh']);
 assert.ok(backlogMatches(records[0],{query:'Ｎｏｈ 原点'}));
 assert.ok(!backlogMatches(records[0],{query:'Noh missing'}));
});

function element(value=''){
 return {value,hidden:false,textContent:'',events:{},addEventListener(type,handler){this.events[type]=handler;},fire(type){this.events[type]?.({preventDefault(){}});}};
}
function fixture(language='ja'){
 const controls=element(),query=element(),reset=element(),count=element(),empty=element(),form=element();controls.hidden=true;
 const selects=Object.fromEntries(['field','priority','state','kind'].map(name=>[name,element('all')]));
 const items=records.map(record=>{
  const details={id:record.id+'-'+language,open:false};
  return {...element(),dataset:{backlogId:record.id,backlogField:record.field_id,backlogPriority:record.priority,backlogState:record.state,backlogKind:record.kind,backlogSearch:[record.id,record.title.ja,record.current,...record.tasks].join(' ')},querySelector:()=>details,details};
 });
 const groups=['fluid','shared'].map(id=>({...element(),dataset:{backlogFieldGroup:id}}));
 const nodes={'[data-backlog-controls]':controls,'[data-backlog-query]':query,'[data-backlog-reset]':reset,'[data-backlog-count]':count,'[data-backlog-empty]':empty,form};
 for(const [name,node]of Object.entries(selects))nodes[`[data-backlog-filter="${name}"]`]=node;
 const scope={dataset:{backlogRoot:language},querySelector:selector=>nodes[selector],querySelectorAll:selector=>selector==='[data-backlog-item]'?items:groups};
 return {scope,items,groups,selects,query,reset,count,empty,controls,visible:()=>items.filter(item=>!item.hidden).map(item=>item.dataset.backlogId)};
}
function environment(fn){
 const saved=Object.fromEntries(['location','history'].map(name=>[name,Object.getOwnPropertyDescriptor(globalThis,name)]));
 const location=new URL('https://hrkoyama.github.io/numerical-methods-atlas/backlog/?lang=ja');
 Object.defineProperty(globalThis,'location',{value:location,configurable:true});
 Object.defineProperty(globalThis,'history',{value:{state:{keep:true},replaceState(state,title,url){this.state=state;location.href=url;}},configurable:true});
 try{return fn(location);}finally{for(const [name,descriptor]of Object.entries(saved)){if(descriptor)Object.defineProperty(globalThis,name,descriptor);else delete globalThis[name];}}
}
test('progressive filters combine four conditions, count unique candidates and hide empty fields',()=>environment(location=>{
 const f=fixture();const [controller]=wireBenchmarkBacklog(f.scope);assert.equal(f.controls.hidden,false);
 f.selects.kind.value='extension';f.selects.kind.fire('change');assert.deepEqual(f.visible(),['weno']);assert.equal(f.count.textContent,'1 / 3 件の候補');assert.equal(f.groups[1].hidden,true);
 assert.equal(location.searchParams.get('backlog-kind'),'extension');assert.equal(location.searchParams.get('lang'),'ja');
 f.selects.state.value='in-progress';f.selects.state.fire('change');assert.deepEqual(f.visible(),[]);assert.equal(f.empty.hidden,false);
 f.reset.fire('click');assert.deepEqual(f.visible(),['noh','weno','citations']);assert.equal(f.empty.hidden,true);assert.equal(location.searchParams.has('backlog-kind'),false);
 f.query.value='原点';f.query.fire('input');assert.deepEqual(f.visible(),['noh']);assert.equal(location.searchParams.has('backlog-query'),false,'free text stays out of server URLs and citation referrers');
 f.reset.fire('click');
 assert.equal(wireBenchmarkBacklog(f.scope)[0],controller,'wiring is idempotent');
}));
test('direct item anchors reveal and open a candidate excluded by URL filters',()=>environment(location=>{
 location.search='?lang=en&backlog-kind=references';location.hash='#noh-en';const f=fixture('en');
 const [controller]=wireBenchmarkBacklog(f.scope);assert.equal(f.selects.kind.value,'all');assert.ok(f.items[0].details.open);assert.deepEqual(f.visible(),['noh','weno','citations']);
 assert.equal(location.hash,'#noh-en');assert.equal(f.count.textContent,'3 of 3 candidates');
 f.selects.kind.value='references';f.selects.kind.fire('change');assert.equal(location.hash,'');assert.deepEqual(f.visible(),['citations']);
 location.search='?lang=en&backlog-priority=invalid&backlog-state=planned';controller.sync();assert.equal(f.selects.priority.value,'all');assert.deepEqual(f.visible(),['weno','citations']);
}));

test('builder keeps all source items, supports Japanese originals, and requires real completion evidence',()=>{
 const python=process.env.ATLAS_INDEX_PYTHON||'python3';
 const code=String.raw`
from pathlib import Path
from copy import deepcopy
import base64,hashlib,importlib.util,json,shutil,sys,tempfile
root=Path(sys.argv[1]).resolve()
spec=importlib.util.spec_from_file_location('backlog',root/'scripts/build-atlas-benchmark-backlog.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
actual=module.load(root);assert len(actual['items'])==actual['source']['proposal_count']+actual['source']['shared_count']
assert sum(item['state']=='in-progress' for item in actual['items'])<=actual['workflow']['max_active']
with tempfile.TemporaryDirectory(prefix='atlas-backlog-test-') as raw:
 fixture=Path(raw)
 def put(path,value):
  p=fixture/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value,ensure_ascii=False) if isinstance(value,(dict,list)) else value);return p
 data=deepcopy(actual);implementation=deepcopy(next(row for row in data['items'] if row['kind']=='implementation'));curation=deepcopy(next(row for row in data['items'] if row['kind']=='references'))
 implementation.update(state='in-progress',completion=None,sequence=1);curation.update(state='planned',completion=None,sequence=2)
 data['items']=[implementation,curation];data['fields']=[row for row in data['fields'] if row['id'] in {implementation['field_id'],curation['field_id']}]
 data['source'].update(proposal_count=1,shared_count=1);data['workflow'].update(max_active=1,active_item=implementation['id']);data['workflow'].pop('active_items',None)
 for asset in ['styles/atlas-benchmark-backlog.css','numerical-methods-atlas/benchmark-backlog.mjs']:
  destination=fixture/asset;destination.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(root/asset,destination)
 def save():put(module.SOURCE,data)
 def rejected():
  try:module.load(fixture)
  except ValueError:return
  raise AssertionError('Unjustified completion was accepted')
 save();module.build(fixture);html=(fixture/'numerical-methods-atlas/backlog/index.html').read_text()
 assert html.count('data-backlog-item ')==4 and html.count('data-backlog-controls hidden')==2
 assert 'original Japanese survey text' in html and 'lang="ja"' in html
 assert implementation['id']+'-ja' in html and implementation['id']+'-en' in html
 before={str(p.relative_to(fixture)):p.read_bytes() for p in fixture.rglob('*') if p.is_file()};module.build(fixture);after={str(p.relative_to(fixture)):p.read_bytes() for p in fixture.rglob('*') if p.is_file()};assert before==after
 implementation['state']='published';data['workflow']['active_item']=None;save();rejected()
 put('code/fixture/input.json',{'fixed':True});put('code/fixture/run.py','# explicit fixture source\n');put('code/fixture/verification.json',{'passed':False});put('code/fixture/reference.json',{'representation':'cell averages'})
 put('numerical-methods-atlas/gallery/index.html','<main id="fixture-ja">Fixture gallery</main>');put('numerical-methods-atlas/validation/fixture/index.html','<main>Fixture execution</main>')
 png=fixture/'code/fixture/plot.png';png.write_bytes(base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+j2R0AAAAASUVORK5CYII='))
 implementation['completion']={'verification':'/code/fixture/verification.json','inputs':['/code/fixture/input.json'],'plots':['/code/fixture/plot.png'],'code':['/code/fixture/run.py'],'references':['/code/fixture/reference.json'],'gallery':'/numerical-methods-atlas/gallery/#fixture-ja','execution':'/numerical-methods-atlas/validation/fixture/'}
 save();rejected();put('code/fixture/verification.json',{'passed':True});assert module.load(fixture)['items'][0]['completion_evidence']['verification_passed'] is True
 implementation['completion']['gallery']='/numerical-methods-atlas/gallery/#missing';save();rejected();implementation['completion']['gallery']='/numerical-methods-atlas/gallery/#fixture-ja'
 curation['state']='verified';curation['completion']={'targets':['/code/fixture/reference.json'],'proof':['/code/fixture/verification.json'],'note':'Fixture correction checked'};save();validated=module.load(fixture);assert validated['items'][1]['completion_evidence']['kind']=='curation'
 assert 'code/fixture/plot.png' in validated['source_sha256'];assert module.SOURCE in validated['source_sha256']
 curation['state']='in-progress';implementation['state']='in-progress';curation['scope_note']='Partial citation work; more targets remain.';implementation['scope_note']='Partial scientific stage; more configurations remain.';data['workflow']['active_item']=implementation['id'];save();rejected()
print('backlog evidence, language, inventory and idempotence checks passed')
`;
 const output=execFileSync(python,['-B','-c',code,fileURLToPath(root)],{encoding:'utf8',maxBuffer:4*1024*1024});
 assert.match(output,/backlog evidence, language, inventory and idempotence checks passed/);
});

test('browser filtering has no fetch, telemetry or calculation trigger',()=>{
 const source=readFileSync(new URL('numerical-methods-atlas/benchmark-backlog.mjs',root),'utf8');
 assert.ok(!/\b(fetch|XMLHttpRequest|sendBeacon|Worker)\s*\(/.test(source));
 const css=readFileSync(new URL('styles/atlas-benchmark-backlog.css',root),'utf8');assert.match(css,/min-height:44px/);assert.match(css,/\[hidden\]/);
});

test('published stages retain in-progress scope and use the same evidence gates; planned items cannot claim a stage',()=>{
 const python=process.env.ATLAS_INDEX_PYTHON||'python3';
 const code=String.raw`
from pathlib import Path
from copy import deepcopy
import base64,importlib.util,json,sys,tempfile
root=Path(sys.argv[1]).resolve()
spec=importlib.util.spec_from_file_location('backlog',root/'scripts/build-atlas-benchmark-backlog.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
original=json.loads((root/module.SOURCE).read_text())
with tempfile.TemporaryDirectory(prefix='atlas-backlog-stage-test-') as raw:
 fixture=Path(raw)
 def put(path,value):
  p=fixture/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value,ensure_ascii=False) if isinstance(value,(dict,list)) else value);return p
 data=deepcopy(original);data['workflow'].update(max_active=1,active_item=None);data['workflow'].pop('active_items',None);item=deepcopy(next(row for row in data['items'] if row['kind']=='implementation'));tasks=deepcopy(item['tasks'])
 data['items']=[item];data['fields']=[row for row in data['fields'] if row['id']==item['field_id']];data['source'].update(proposal_count=1,shared_count=0)
 item.update(state='in-progress',scope_note='',sequence=1)
 put('code/stage/input.json',{'fixed':True});put('code/stage/run.py','# fixture scientific source\n');put('code/stage/verification.json',{'passed':True});put('code/stage/reference.json',{'cell_average':True})
 put('gallery/index.html','<main id="stage-ja">Gallery fixture</main>');put('run/index.html','<main>Run fixture</main>')
 plot=fixture/'code/stage/plot.png';plot.write_bytes(base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+j2R0AAAAASUVORK5CYII='))
 item['completion']={'verification':'/code/stage/verification.json','inputs':['/code/stage/input.json'],'plots':['/code/stage/plot.png'],'code':['/code/stage/run.py'],'references':['/code/stage/reference.json'],'gallery':'/gallery/#stage-ja','execution':'/run/'}
 def save():
  data['workflow']['active_item']=item['id'] if item['state']=='in-progress' else None
  put(module.SOURCE,data)
 def rejected():
  save()
  try:module.load(fixture)
  except ValueError:return
  raise AssertionError('Invalid partial/completion evidence accepted')
 rejected()
 item['scope_note']='Published: planar and 1D cylindrical-radial only. Remaining: spherical and Cartesian multidimensional cases.';save();normalized=module.load(fixture);stage=normalized['items'][0]
 assert stage['state']=='in-progress' and stage['completion_evidence']['partial'] is True
 assert stage['completion_evidence']['verification_passed'] is True and stage['tasks']==tasks
 assert normalized['counts']['states']['in-progress']==1 and normalized['counts']['states']['verified']==normalized['counts']['states']['published']==0
 html=module.item_html(stage,normalized,'ja');english=module.item_html(stage,normalized,'en');markdown=module.markdown(normalized)
 assert '公開した段階の根拠' in html and '確認できる完了の根拠' not in html
 assert 'Evidence for the published stage' in english and 'Checked completion evidence' not in english
 localized_stage=deepcopy(stage);localized_stage['completion_evidence']['links']['gallery']='/numerical-methods-atlas/gallery/?lang=ja#noh-ja';localized_stage['completion_evidence']['links']['references']=['/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja']
 english_links=module.evidence_links(localized_stage,'en');japanese_links=module.evidence_links(localized_stage,'ja')
 assert 'href="/numerical-methods-atlas/gallery/?lang=en#noh-en"' in english_links
 assert 'href="/numerical-methods-atlas/solutions/?lang=en#solution-noh-en"' in english_links
 assert 'href="/numerical-methods-atlas/gallery/?lang=ja#noh-ja"' in japanese_links
 assert '/code/stage/plot.png' in english_links and '/code/stage/plot.png?lang=' not in english_links
 assert module.localized_evidence_url('https://example.org/paper#section-ja','en')=='https://example.org/paper#section-ja'
 assert module.localized_evidence_url('/numerical-methods-atlas/ja/read/explicit-edition/#section-ja','en')=='/numerical-methods-atlas/ja/read/explicit-edition/#section-ja'
 assert '調査時の現状' in html and '公開した段階と残る範囲' in html and item['scope_note'] in html
 assert '公開した段階の根拠' in markdown and item['scope_note'] in markdown
 put('code/stage/verification.json',{'passed':False});rejected();put('code/stage/verification.json',{'passed':True})
 plot.unlink();rejected();plot.write_bytes(base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+j2R0AAAAASUVORK5CYII='))
 item['state']='planned';rejected();item['completion']={};rejected();item['completion']=None;save();assert module.load(fixture)['items'][0]['completion_evidence'] is None
 for state in ['verified','published']:
  item['state']=state;rejected()
 item=deepcopy(next(row for row in original['items'] if row['kind']=='references'));item.update(state='in-progress',sequence=1,scope_note='Published correction for one target; remaining citations stay queued.')
 data['items']=[item];data['fields']=[row for row in original['fields'] if row['id']==item['field_id']]
 put('code/stage/citation-proof.json',{'checked':True});item['completion']={'targets':['/code/stage/reference.json'],'proof':['/code/stage/citation-proof.json'],'note':'Checked target and correction evidence'};save();curation=module.load(fixture)['items'][0]
 assert curation['completion_evidence']['kind']=='curation' and curation['completion_evidence']['partial'] is True
 item['completion']['proof']=['/code/stage/missing-proof.json'];rejected()
print('partial stages retain scope and evidence validation without completing candidates')
`;
 const output=execFileSync(python,['-B','-c',code,fileURLToPath(root)],{encoding:'utf8',maxBuffer:4*1024*1024});
 assert.match(output,/partial stages retain scope and evidence validation without completing candidates/);
});

test('a five-item batch retains independent evidence and rejects unlisted, duplicate or excessive active work',()=>{
 const code=String.raw`
import copy,importlib.util,json,pathlib,sys
from unittest.mock import patch
root=pathlib.Path(sys.argv[1]).resolve()
spec=importlib.util.spec_from_file_location('backlog',root/'scripts/build-atlas-benchmark-backlog.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
data=json.loads((root/m.SOURCE).read_text())
for row in data['items']:
 if row['state']=='in-progress':row['state']='planned';row['completion']=None
chosen=[row for row in data['items'] if 13<=row['sequence']<=17]
assert len(chosen)==5
for row in chosen:row.update(state='in-progress',completion=None)
ids=[row['id'] for row in chosen]
data['workflow'].update(max_active=5,active_item=None,active_items=ids,batch_id='fixture-five')
original=pathlib.Path.read_text
def load(value):
 def read(path,*a,**kw):
  return json.dumps(value) if path.resolve()==(root/m.SOURCE).resolve() else original(path,*a,**kw)
 with patch.object(pathlib.Path,'read_text',read):return m.load(root)
valid=load(data)
assert valid['counts']['states']['in-progress']==5
assert all(next(row for row in valid['items'] if row['id']==i)['completion_evidence'] is None for i in ids)
html=m.section(valid,'en');assert '5 active items' in html and all('#'+i+'-en' in html for i in ids)
for mutation in ['excess','duplicate','missing','unlisted','no-batch','legacy-conflict']:
 bad=copy.deepcopy(data);w=bad['workflow']
 if mutation=='excess':w['max_active']=11
 elif mutation=='duplicate':w['active_items']=[ids[0]]*5
 elif mutation=='missing':w['active_items']=ids[:-1]
 elif mutation=='unlisted':w['active_items']=ids[:-1]+['unknown-item']
 elif mutation=='no-batch':w['batch_id']=''
 else:w['active_item']=ids[0]
 try:load(bad)
 except ValueError:pass
 else:raise AssertionError('invalid batch accepted: '+mutation)
print('five-item batches are explicit and evidence remains independent')
`;
 assert.match(execFileSync(process.env.ATLAS_INDEX_PYTHON||'python3',['-B','-c',code,fileURLToPath(root)],{encoding:'utf8'}),/five-item batches are explicit/);
});

test('ten-item publication batches preserve explicit membership and reject overflow or ambiguous slots',()=>{
 const code=String.raw`
import copy,importlib.util,json,pathlib,sys
from unittest.mock import patch
root=pathlib.Path(sys.argv[1]).resolve()
spec=importlib.util.spec_from_file_location('backlog',root/'scripts/build-atlas-benchmark-backlog.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
data=json.loads((root/m.SOURCE).read_text())
for row in data['items']:
 if row['state']=='in-progress':row.update(state='planned',completion=None)
chosen=[row for row in data['items'] if 18<=row['sequence']<=27]
assert len(chosen)==10
for row in chosen:row.update(state='in-progress',completion=None)
ids=[row['id'] for row in chosen]
data['workflow'].update(max_active=10,active_item=None,active_items=ids,batch_id='fixture-ten')
original=pathlib.Path.read_text
def load(value):
 def read(path,*a,**kw):
  return json.dumps(value) if path.resolve()==(root/m.SOURCE).resolve() else original(path,*a,**kw)
 with patch.object(pathlib.Path,'read_text',read):return m.load(root)
valid=load(data);assert valid['counts']['states']['in-progress']==10
html=m.section(valid,'en');assert '10 active items' in html and all('#'+i+'-en' in html for i in ids)
for mutation in ['overflow','excess-cap','boolean-cap','missing','duplicate','reordered','legacy-conflict']:
 bad=copy.deepcopy(data);w=bad['workflow']
 if mutation=='overflow':w['max_active']=9
 elif mutation=='excess-cap':w['max_active']=11
 elif mutation=='boolean-cap':w['max_active']=True
 elif mutation=='missing':w['active_items']=ids[:-1]
 elif mutation=='duplicate':w['active_items']=ids[:-1]+[ids[0]]
 elif mutation=='reordered':w['active_items']=list(reversed(ids))
 else:w['active_item']=ids[0]
 try:load(bad)
 except ValueError:pass
 else:raise AssertionError('invalid ten-item batch accepted: '+mutation)
print('ten-item batches retain individual completion requirements')
`;
 assert.match(execFileSync(process.env.ATLAS_INDEX_PYTHON||'python3',['-B','-c',code,fileURLToPath(root)],{encoding:'utf8'}),/ten-item batches retain/);
});


test('workflow retains the four states and bilingual completion criteria before rendering',()=>{
 const program=String.raw`
from pathlib import Path
from copy import deepcopy
import importlib.util,json,sys
root=Path(sys.argv[1]).resolve()
spec=importlib.util.spec_from_file_location('backlog_contract',root/'scripts/build-atlas-benchmark-backlog.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
workflow=json.loads((root/m.SOURCE).read_text())['workflow'];before=deepcopy(workflow)
assert m.workflow_contract(workflow) is workflow and workflow==before
assert workflow['states']==['planned','in-progress','verified','published']
for language in ['ja','en']:assert isinstance(workflow['completion_rule'][language],str) and workflow['completion_rule'][language].strip()
for mutation in ['missing-states','unknown-state','missing-rule','empty-ja','nonstr-en']:
 bad=deepcopy(workflow)
 if mutation=='missing-states':bad.pop('states')
 elif mutation=='unknown-state':bad['states'][-1]='done'
 elif mutation=='missing-rule':bad.pop('completion_rule')
 elif mutation=='empty-ja':bad['completion_rule']['ja']='  '
 else:bad['completion_rule']['en']=None
 try:m.workflow_contract(bad)
 except ValueError:pass
 else:raise AssertionError('Incomplete workflow contract accepted: '+mutation)
print('four states and bilingual completion criteria retained; five invalid controls rejected')
`;
 assert.match(execFileSync(process.env.ATLAS_INDEX_PYTHON||'python3',['-B','-c',program,fileURLToPath(root)],{encoding:'utf8',timeout:10000}),/five invalid controls rejected/);
});
