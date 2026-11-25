import {problemCount} from './fixtures/atlas-inventory.mjs';
import test from 'node:test';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {searchChapters} from '../numerical-methods-atlas/home-search.js';
const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root),'utf8');
const json=p=>JSON.parse(read(p));
const data=json('catalog/atlas-quantum.json');
const methods=json('catalog/atlas-methods.json').methods.filter(x=>x.group.id==='quantum');
const coverage=json('numerical-methods-atlas/coverage.json');

test('each curated quantum topic has bilingual equations, valid source links and explicit limits with implementation scope distinguished',()=>{
  assert.deepEqual(data.sections.map(x=>x.id).sort(),methods.map(x=>x.id).sort());
  assert.equal(methods.length,20);
  const references=new Map(data.references.map(x=>[x.id,x]));
  for(const x of methods){
    assert.equal(x.status,(x.quantum_examples?.length||x.molecular_examples?.length||x.periodic_examples?.length||x.depth_release)?'educational-example':'reading-only');
    assert.deepEqual(x.code_modules,[]);assert.deepEqual(x.test_files,[]);
    const s=data.sections.find(y=>y.id===x.id);
    assert.ok(s.references.length&&s.references.every(id=>references.has(id)));
    for(const lang of ['ja','en']){
      const page=read(`numerical-methods-atlas/${lang}/read/quantum-chemistry/index.html`);
      assert.ok(page.includes('data-quantum-id="'+x.id+'"'));
      assert.ok(page.includes('id="'+x.id+'"'));
      assert.ok(page.includes(s.caution[lang]));
      if(x.depth_release){assert.ok(page.includes('data-quantum-depth-method="'+x.id+'"'));for(const id of x.depth_release.case_ids)assert.ok(page.includes('/numerical-methods-atlas/validation/'+id+'/?lang='+lang));}
      assert.ok(s.paragraphs[lang].length>=2);
      assert.ok(!page.includes('katex-error'));
      assert.ok(json(`numerical-methods-atlas/content.${lang}.json`)['quantum-chemistry']);
    }
  }
  assert.ok(read('numerical-methods-atlas/ja/read/quantum-chemistry/index.html').includes('katex-mathml'));
  assert.equal(new Set(data.references.map(x=>x.doi.toLowerCase())).size,data.references.length);
});

test('quantum additions reconcile model, method and publication counts across the common atlas',()=>{
  const quantum=coverage.items.filter(x=>x.origin==='curated-quantum-reading');
  const methodIDs=new Set(methods.map(x=>x.id)),covered=coverage.items.filter(x=>x.kind==='method'&&methodIDs.has(x.id));
  assert.deepEqual(covered.map(x=>x.id).sort(),[...methodIDs].sort());assert.equal(new Set(covered.map(x=>x.id)).size,methods.length);
  for(const row of covered){const method=methods.find(x=>x.id===row.id);assert.equal(row.status,method.status==='educational-example'?'local-example':'reading');assert.equal(row.origin,method.depth_release?'curated-depth-example':'curated-quantum-reading');}
  const modelSource=json('catalog/atlas-equations.json').equations.filter(x=>x.group==='quantum');
  assert.deepEqual(quantum.filter(x=>x.kind==='equation').map(x=>x.id).sort(),modelSource.map(x=>x.id).sort());
  assert.equal(quantum.filter(x=>x.status==='local-example'&&x.kind==='equation').length,modelSource.filter(x=>x.status==='local-example').length);
  assert.equal(coverage.counts.methods,coverage.items.filter(x=>x.kind==='method').length);
  assert.equal(coverage.counts.equations,coverage.items.filter(x=>x.kind==='equation').length);
  assert.equal(coverage.counts.papers,coverage.publications.filter(x=>['article','inproceedings'].includes(x.type)).length);
  assert.equal(coverage.counts.references,coverage.publications.length);
  assert.equal(new Set(coverage.publications.map(x=>x.identity)).size,coverage.publications.length);
  const library=json('numerical-methods-atlas/references.json');
  for(const r of data.references){
    assert.equal(library.filter(x=>x.doi?.toLowerCase()===r.doi.toLowerCase()).length,1);
    assert.equal(coverage.publications.filter(x=>x.identity==='doi:'+r.doi.toLowerCase()).length,1);
    assert.ok(read('numerical-methods-atlas/assets/references.bib').includes(r.doi));
  }
  for(const [path,expected] of Object.entries(coverage.public_extension_sha256)){
    assert.equal(createHash('sha256').update(readFileSync(new URL(path,root))).digest('hex'),expected,path);
  }
  assert.deepEqual(json('numerical-methods-atlas/assets/site-coverage.json'),coverage);
});

test('DFT is discoverable by Japanese, English and aliases, and all new equations link to the appropriate section',()=>{
  const index=json('numerical-methods-atlas/home-search-index.json');
  for(const query of ['量子化学','DFT','密度汎関数','Kohn–Sham']){
    const hits=searchChapters(index,query,'ja');
    assert.ok(hits.some(x=>x.url?.includes('quantum-chemistry')||x.url?.includes('kohn-sham-dft')),query);
  }
  for(const lang of ['ja','en']){
    assert.ok(json('guide/index.json').pages.some(x=>x.url===`https://hrkoyama.github.io/numerical-methods-atlas/${lang}/read/quantum-chemistry/`));
    const page=read(`numerical-methods-atlas/${lang}/read/site-coverage/index.html`);
    assert.ok(page.includes('quantum-extension'));
    assert.ok(page.includes(String(coverage.counts.methods))&&page.includes(String(coverage.counts.papers)));
    if(lang==='ja')assert.ok(page.includes(`ローカル実験のある項目は${coverage.counts.local_methods}、文献解説のみは${coverage.counts.reading_methods}です`));
    else assert.ok(page.includes(`${coverage.counts.journal_articles} journal-article records`));
  }
  const models=json('numerical-methods-atlas/equations/index.json').equations.filter(x=>x.group==='quantum');
  const canonical=json('catalog/atlas-equations.json').equations.filter(x=>x.group==='quantum');
  assert.deepEqual(canonical.map(x=>x.id).sort(),['stationary-schrodinger','hartree-fock-model','kohn-sham-model','time-dependent-kohn-sham','two-state-bo-cp-model','unrestricted-hartree-fock-model','finite-projector-fermi-model'].sort());
  assert.deepEqual(models.map(x=>x.id).sort(),canonical.map(x=>x.id).sort());
  for(const x of models)for(const [lang,url] of Object.entries(x.reading)){const source=canonical.find(s=>s.id===x.id),u=new URL(url);assert.equal(u.pathname,`/numerical-methods-atlas/${lang}/read/${source.chapter}/`);assert.equal(u.hash,source.section?'#'+source.section:'');}
  const app=read('numerical-methods-atlas/app.js');
  assert.equal(app.split('import {atlasIntroDescriptions,atlasDocumentVersions}').length-1,1);
  const runtime=read('numerical-methods-atlas/atlas-runtime-data.mjs');assert.equal(runtime.split('export const atlasDocumentVersions =').length-1,1);
  for(const lang of ['ja','en'])assert.ok(runtime.includes(createHash('sha256').update(readFileSync(new URL(`numerical-methods-atlas/content.${lang}.json`,root))).digest('hex').slice(0,12)));
});

test('only executed quantum examples enter test-problem counts and specialist AI is deferred until 2027',()=>{
  assert.equal(data.verification_plan.filter(x=>x.state==='verified-educational-example').length,5);
  assert.equal(data.verification_plan.length,5);
  assert.equal(data.verification_plan.filter(x=>x.state==='planned').length,0);
  const tests=json('numerical-methods-atlas/test-cases/index.json');
  assert.equal(tests.problems.length,problemCount);
  assert.equal(tests.problems.filter(x=>x.chapter==='quantum-atoms').length,2);
  assert.ok(!tests.problems.some(x=>x.chapter==='quantum-chemistry'));
  const work=json('catalog/atlas-work-queue.json').items;
  const ai=work.find(x=>x.id==='atlas-specialist-ai');
  assert.equal(ai.state,'deferred-until-2027');assert.equal(ai.target_year,2027);
  for(const lang of ['ja','en']){
    const roadmap=read(`numerical-methods-atlas/${lang}/read/roadmap/index.html`);
    assert.ok(roadmap.includes(ai.title[lang])&&roadmap.includes(ai.scope[lang]));
    assert.ok(roadmap.indexOf('id="atlas-work-queue"')<roadmap.indexOf('id="current-priority-shock-methods"'));
    assert.ok(roadmap.indexOf('id="atlas-roadmap-history"')<roadmap.indexOf('id="current-priority-shock-methods"'));
    assert.doesNotMatch(roadmap,/現在の最優先：衝撃波手法|承認済みの次の作業|Current priority: shock methods|Authorized next work/);
    assert.ok(!roadmap.includes('implementation and the dedicated literature review have not'));
  }
  const translations=json('numerical-methods-atlas/locales/messages.json');
  assert.ok(!translations['home-map.future'].ja.includes('未着手分野'));
  assert.ok(!translations['planned.quantum.status'].en.includes('have not started'));
});

test('band symmetry distinguishes little groups, SOC and antiunitary assumptions from a verified band calculation',()=>{
  const s=data.sections.find(x=>x.id==='band-symmetry');
  assert.ok(s&&s.subsections.length===4);
  assert.ok(s.formula.some(f=>f.includes('G_{\\mathbf k}')));
  assert.ok(s.subsections.find(x=>x.id==='band-symmetry-soc-tr').formula.some(f=>f.includes('\\Theta^2=-1')));
  for(const lang of ['ja','en']){
    const page=read(`numerical-methods-atlas/${lang}/read/quantum-chemistry/index.html`);
    for(const child of s.subsections)assert.ok(page.includes('id="'+child.id+'"'));
    assert.ok(page.includes(lang==='ja'?'高対称線の図だけで大域的なバンドギャップを断定しません':'it alone does not establish the global band gap'));
  }
  assert.ok(read('llms.txt').includes(data.sections.length+' bilingual introductory topics'));
});


test('scoped MP2 CI and BO CP cannot borrow old atomic H2 or periodic-He evidence',()=>{
 const result=JSON.parse(execFileSync('python3',['-B','-c',String.raw`
import ast,copy,hashlib,json,pathlib
root=pathlib.Path.cwd();path=root/'scripts/build-atlas-quantum.py';tree=ast.parse(path.read_text());ns={}
nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='quantum_implementation_allowed' or isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='SCOPED_QUANTUM_DEPTH_ONLY' for t in n.targets)]
exec(compile(ast.Module(body=nodes,type_ignores=[]),'quantum-scope-functions-only','exec'),ns)
allowed=ns['quantum_implementation_allowed'];expected=ns['SCOPED_QUANTUM_DEPTH_ONLY'];assert set(expected)=={'mp2','configuration-interaction','born-oppenheimer-md','car-parrinello-md'}
methods={x['id']:x for x in json.loads((root/'catalog/atlas-methods.json').read_text())['methods']}
base=root/'code/validated-examples/2026-11-25/quantum-small';manifest=json.loads((base/'source-manifest.json').read_text());proof=json.loads((base/'verification.json').read_text());cases=json.loads((base/'cases.json').read_text());cases=cases['cases'] if isinstance(cases,dict) else cases;results=json.loads((base/'results/result.json').read_text());checks=0
for name in ['cases.json','results/result.json']:
 assert hashlib.sha256((base/name).read_bytes()).hexdigest()==manifest['files'][name]
assert proof['passed'] is True and proof['all_cases_rerun'] is True and proof['tests']==proof['passed_tests']==18
assert proof['source_manifest_sha256']==hashlib.sha256((base/'source-manifest.json').read_bytes()).hexdigest()
for ident,ids in expected.items():
 method=methods[ident];record={'group':'quantum-small','code_edition':'2026-11-25','case_ids':ids,'passed_tests':18,'examples':[{**next(x for x in cases if x['id']==i),'measured':next(x for x in results['cases'] if x['id']==i)} for i in ids]}
 assert allowed(method,record);checks+=1
 assert allowed(method,None) is False;checks+=1
 for field,value in [('quantum_examples',['helium-ground-state']),('molecular_examples',['h2-rhf']),('periodic_examples',['periodic-he-dft']),('force_examples',['periodic-he-forces'])]:
  bad=copy.deepcopy(method);bad[field]=value
  try:allowed(bad,record)
  except AssertionError:checks+=1
  else:raise AssertionError('Legacy evidence borrowed: '+ident+'/'+field)
 for field,value in [('group','periodic-he'),('code_edition','2026-11-22'),('case_ids',['helium-ground-state']),('passed_tests',17)]:
  bad=copy.deepcopy(record);bad[field]=value
  try:allowed(method,bad)
  except AssertionError:checks+=1
  else:raise AssertionError('Wrong qualified release accepted: '+ident+'/'+field)
print(json.dumps({'passed':True,'checks':checks,'solver_executed':False}))
`],{cwd:fileURLToPath(root),encoding:'utf8',timeout:30_000}));
 assert.deepEqual(result,{passed:true,checks:40,solver_executed:false});
});
