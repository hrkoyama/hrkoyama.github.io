import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {spawnSync} from 'node:child_process';

const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root),'utf8');
const queue=JSON.parse(read('catalog/atlas-work-queue.json'));

// Load only pure roadmap functions, without running the site generator or writing
// any generated files. Exercise both an already-published page and its TOC data.
const probe=spawnSync('python3',['-c',String.raw`
import ast,html,json,re
from pathlib import Path
root=Path.cwd()
tree=ast.parse((root/'scripts/build-atlas-quantum.py').read_text())
names={'roadmap_history_titles','build_public_roadmap','adapt_roadmap_history'}
selected=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
assert {n.name for n in selected}==names
env={'re':re,'esc':html.escape,
     'paragraph':lambda text:'<p>'+html.escape(text)+'</p>',
     'link':lambda url,label:'<a href="'+html.escape(url)+'">'+html.escape(label)+'</a>'}
exec(compile(ast.Module(body=selected,type_ignores=[]),'roadmap-functions','exec'),env)
queue=json.loads((root/'catalog/atlas-work-queue.json').read_text())
output={}
for lang in ['ja','en']:
    source=(root/f'numerical-methods-atlas/{lang}/read/roadmap/index.html').read_text()
    headings=json.loads((root/f'numerical-methods-atlas/content.{lang}.json').read_text())['roadmap']['headings']
    block,new_headings=env['build_public_roadmap'](queue,lang)
    def publish(text,old_headings):
        text=re.sub(r'<!-- atlas-work-queue -->.*?<!-- /atlas-work-queue -->','',text,flags=re.S)
        text,updated=env['adapt_roadmap_history'](text,old_headings,lang,new_headings)
        return re.sub(r'(</h1>)',lambda m:m[1]+'<!-- atlas-work-queue -->'+block+'<!-- /atlas-work-queue -->',text,count=1),updated
    first,first_headings=publish(source,headings)
    second,second_headings=publish(first,first_headings)
    output[lang]={'html':first,'headings':first_headings,'original_headings':headings,
                  'idempotent':first==second and first_headings==second_headings,
                  'titles':env['roadmap_history_titles'](lang)}
print(json.dumps(output,ensure_ascii=False))
`],{cwd:root,encoding:'utf8',maxBuffer:2_000_000});
assert.equal(probe.status,0,probe.stderr);
const rendered=JSON.parse(probe.stdout);

test('current work, conditional additions and published examples remain separate',()=>{
  assert.equal(queue.schema_version,2);
  assert.equal(queue.items.length,20);
  assert.equal(new Set(queue.items.map(x=>x.id)).size,queue.items.length);
  for(const id of ['current-roadmap','executable-example-registry']){
    const x=queue.items.find(x=>x.id===id);
    assert.equal(x.state,'published');
    assert.equal(x.priority,'P0');assert.equal(x.track,'published');
  }
  const ongoing=queue.items.filter(x=>x.track==='current');
  assert.deepEqual(ongoing.map(x=>x.id),['validated-code-kits','retreat-poster','field-validation-depth','public-reproduction-checks','year-end-release']);
  for(const x of ongoing){assert.equal(x.state,'in-progress');assert.equal(x.priority,'P0');}
  for(const id of ['molecular-quantum-example','ewald-pme-spme','periodic-dft-validation','periodic-forces-validation']){
    const x=queue.items.find(x=>x.id===id);
    assert.equal(x.state,'published-verified-example');assert.equal(x.track,'published');
  }
  const conditional=queue.items.filter(x=>x.track==='conditional');
  assert.deepEqual(conditional.map(x=>x.id),['bounded-gap-closure']);
  assert.equal(conditional[0].state,'conditional-planned');assert.equal(conditional[0].priority,'P1');
  assert.match(conditional[0].scope.en,/existing target/);
  assert.match(conditional[0].scope.en,/Extending kits to Sod.*optional P1/);
  assert.match(conditional[0].scope.en,/After 18 December allow only correctness-related fixes/);
  assert.equal(queue.items.find(x=>x.id==='quantum-examples').state,'hydrogenic-helium-verified');
  assert.equal(queue.items.find(x=>x.id==='barnes-hut-example').track,'published');
  assert.equal(queue.items.find(x=>x.id==='atlas-specialist-ai').target_year,2027);
  assert.doesNotMatch(JSON.stringify(queue),/Enterprise|owner_hours|hours_per_day|competitor|競合|本人の時間/);
});

test('roadmap rendering preserves anchors and is idempotent for both languages',()=>{
  for(const lang of ['ja','en']){
    const x=rendered[lang];assert.ok(x.idempotent,lang);
    assert.equal(x.html.split('id="atlas-work-queue"').length-1,1);
    assert.equal(new Set(x.headings.map(h=>h.id)).size,x.headings.length);
    for(const old of x.original_headings){
      assert.ok(x.headings.some(h=>h.id===old.id),old.id);
      assert.ok(x.html.includes('id="'+old.id+'"'),old.id);
    }
    assert.ok(x.html.indexOf('id="atlas-work-queue"')<x.html.indexOf('id="atlas-roadmap-history"'));
    assert.ok(x.html.indexOf('id="atlas-roadmap-history"')<x.html.indexOf('id="current-priority-shock-methods"'));
  }
});

test('public milestones give target dates without promising every implementation',()=>{
  assert.deepEqual(queue.milestones.map(x=>x.target),['2026-11-30','2026-12-12','2026-12-16','2026-12-18','2026-12-23','2026-12-31']);
  for(const lang of ['ja','en']){
    for(const x of queue.milestones)assert.ok(rendered[lang].html.includes(x.title[lang]));
    assert.ok(rendered[lang].html.includes(queue.milestones.find(x=>x.id==='year-end-edition').scope[lang]));
  }
});

test('the retreat poster has its own A0 Japanese preparation gates and does not preclaim the demonstration or the year-end candidate',()=>{
  const poster=queue.items.find(x=>x.id==='retreat-poster');
  assert.equal(poster.target_year,2026);assert.equal(poster.state,'in-progress');
  assert.equal(poster.priority,'P0');assert.equal(poster.track,'current');
  for(const text of ['poster PDF and agent demonstration are not yet complete','A0 portrait, mainly Japanese with English technical terms','two advection/diffusion demonstrations','meaningful code adaptation','catalogue scale as background','measured results, diffs, valid/bug controls','reference/criteria/executed-code versions by 12 December','finish the PDF on the 14th','full-size readability','QR targets','display/print data','short demo video and run records on the 15th','manual intervention, unimplemented features and scope as observed','presentation edition separate from later year-end changes'])assert.ok(poster.scope.en.includes(text),text);
  assert.match(poster.scope.ja,/ポスターPDFとエージェント実証は未完成/);
  assert.match(poster.scope.ja,/A0縦・日本語中心/);
  const measuredFreeze=queue.milestones.find(x=>x.id==='representative-paths');
  assert.match(measuredFreeze.scope.en,/freeze the measured results and distribution\/reference\/criteria\/executed-code versions for the poster/);
  const presentation=queue.milestones.find(x=>x.id==='retreat-presentation');
  assert.equal(presentation.target,'2026-12-16');
  for(const text of ['frozen on the 12th','A0 portrait poster, mainly Japanese with English terminology','Complete the PDF by the 14th','on the 15th','valid/bug controls and original/derived-code distinctions','without network access','do not prewrite unobserved success','presentation edition separate from the later year-end candidate','version numerical corrections with reasons'])assert.ok(presentation.scope.en.includes(text),text);
  assert.equal(queue.milestones.find(x=>x.id==='feature-freeze').target,'2026-12-18');
  for(const language of ['ja','en']){
    assert.ok(rendered[language].html.includes(poster.title[language]));
    assert.ok(rendered[language].html.includes(presentation.title[language]));
    assert.ok(rendered[language].html.includes(language==='ja'?'未実証の成功を先に書かない':'do not prewrite unobserved success'));
  }
});

test('year-end priorities specify agent-ready verified code and separate original evidence from measured derived-code results',()=>{
  const byId=new Map(queue.items.map(x=>[x.id,x]));
  const registry=JSON.parse(read('catalog/atlas-execution-examples.json'));
  const problems=JSON.parse(read('catalog/atlas-test-problems.json'));
  const methods=JSON.parse(read('catalog/atlas-methods.json'));
  const quantum=JSON.parse(read('catalog/atlas-quantum.json'));
  assert.equal(registry.examples.length,22);assert.equal(problems.problems.length,86);assert.equal(methods.methods.length,147);assert.equal(quantum.sections.length,20);
  assert.match(byId.get('executable-example-registry').scope.en,/22 examples/);
  assert.match(byId.get('representative-recipes').scope.en,/83-problem\/39-runnable-entrance/);
  assert.match(byId.get('method-assumptions-review').scope.en,/all 147 entries/);
  assert.match(byId.get('quantum-reading').scope.en,/20 topics/);
  assert.match(queue.policy.en,/From 22 November 2026, new fields are outside the standard/);
  assert.match(queue.policy.en,/18 December freezes kit\/interface additions and additions to existing validation/);
  assert.match(queue.policy.en,/Large basis\/k sweeps/);
  assert.match(queue.policy.en,/new explicit request/);
  assert.match(queue.policy.en,/agents cannot redefine passing criteria/);
  assert.match(queue.policy.en,/users’ existing AI agents is in scope this year/);
  assert.match(queue.policy.en,/specialist-AI training\/model research remains for 2027 or later/);
  const kits=byId.get('validated-code-kits');
  assert.equal(kits.state,'in-progress');
  for(const text of ['Currently at specification stage','machine-readable manifest','retrieves Atlas verified code','assembles/modifies and runs','two small 1D advection and diffusion tasks','JSON request/catalog/result','nodal-versus-cell-average output contracts','retrieval/execution CLI','separate grid/time refinement','Fix supported parameter families and criteria before running','Preserve old fixed-recipe rejection rules and immutable releases','valid modification','intentional implementation bug','Record original code, modification diff','Atlas-hosted or trained AI are not year-end requirements'])assert.ok(kits.scope.en.includes(text),text);
  for(const text of ['At least one of the two tasks','meaningful source-level assembly/adaptation','with an actual diff','Configuration changes alone do not satisfy this gate','public URL, request and explicitly listed public materials','without private working copies','record any hints or interventions'])assert.ok(kits.scope.en.includes(text),text);
  for(const text of ['Pin the evaluator, tests, references, inputs and thresholds separately from editable solver code','clean evaluation environment executes the actual delivered derived-code entrypoint','records the executed source SHA','agent self-reported passes or accidental imports of the original implementation are not evidence'])assert.ok(kits.scope.en.includes(text),text);
  assert.match(queue.description.en,/a user’s AI agent/);
  assert.match(queue.description.en,/assemble, modify, run and verify code/);
  const depth=byId.get('field-validation-depth');
  assert.match(depth.scope.en,/remains pending publication until every public file matches/);
  assert.match(depth.scope.en,/actual fresh-Linux public-ZIP rerun succeeds/);
  assert.ok(depth.links.some(x=>x.url==='/numerical-methods-atlas/validation/releases.json'));
  const ci=byId.get('linux-public-reproduction-ci');
  assert.match(ci.scope.en,/pinned NumPy\/SciPy\/pytest/);
  assert.match(ci.scope.en,/Detailed common-22 CI including quantum remains manual/);
  const use=byId.get('public-reproduction-checks');
  assert.match(use.scope.en,/existing public inputs only/);
  assert.match(use.scope.en,/new derived-code assessment in development kits/);
  assert.match(use.scope.en,/Register new input families, references and criteria before execution/);
  assert.match(use.scope.en,/fixed-recipe rejection checks are insufficient/);
  const gate=queue.milestones.find(x=>x.id==='representative-paths');
  for(const text of ['separate AI agent','two advection/diffusion tasks','kit retrieval → configuration/implementation modification → execution → reference comparison','Fix input families, references and criteria before execution','distinguish original from derived-code results','valid modification','intentional implementation bug','six goal paths','separate from rerunning original public distributions'])assert.ok(gate.scope.en.includes(text),text);
  for(const text of ['meaningful source-level assembly/adaptation','Configuration changes alone do not satisfy this gate','without private working copies','record any hints or interventions'])assert.ok(gate.scope.en.includes(text),text);
  const contract=queue.milestones.find(x=>x.id==='shared-first-examples');
  for(const text of ['language','dependencies','machine-readable manifest','failure reasons','specification is not completed implementation'])assert.ok(contract.scope.en.includes(text),text);
  const release=byId.get('year-end-release');
  for(const text of ['another directory','new release','persistent versioned public verification evidence','registry/archive/reference/criteria hashes','case/pytest counts','CI run URL','Separate original-code passes, derived-code passes and failed controls','reference/criteria changes did not manufacture success'])assert.ok(release.scope.en.includes(text),text);
  assert.match(release.scope.en,/Do not mark complete with unresolved P0/);
  assert.match(release.scope.en,/actual delivered derived-code entrypoint/);
  assert.match(release.scope.en,/records the executed source SHA/);
  const final=queue.milestones.find(x=>x.id==='year-end-edition');
  for(const text of ['fresh AI-agent contexts','artifact delivery','separate receipts','reference/criteria hashes','versioned public evidence','Unresolved P0 prevents completion'])assert.ok(final.scope.en.includes(text),text);
  // Dated aggregate snapshots belong to audit records, not evergreen visible promises.
  for(const language of ['ja','en']){
    const visible=queue.description[language]+queue.policy[language]+queue.items.map(x=>x.scope[language]).join(' ')+queue.milestones.map(x=>x.scope[language]).join(' ');
    assert.doesNotMatch(visible,/9補助配布版|9補助版|追加6ケース・75|nine public supplements|six cases and 75|ten supplements, 39 cases and 372/);
    for(const item of queue.items)assert.ok(rendered[language].html.includes(item.scope[language].replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;').replaceAll("'",'&#x27;')));
  }
});

test('history headings and static/content tables of contents agree without active old promises',()=>{
  for(const lang of ['ja','en']){
    const x=rendered[lang];
    for(const [id,title] of Object.entries(x.titles)){
      assert.ok(x.html.includes('id="'+id+'">'+title),id);
      assert.ok(x.html.includes('href="#'+id+'">'+title+'</a>'),id);
      assert.equal(x.headings.find(h=>h.id===id).title,title);
    }
    assert.doesNotMatch(x.html,/現在の最優先：衝撃波手法|承認済みの次の作業|Current priority: shock methods|Authorized next work/);
    assert.doesNotMatch(x.html,/相対論・新分野より、衝撃波手法の拡充を優先します|Shock-method expansion takes priority/);
    for(const h of x.headings.filter(h=>h.id.startsWith('atlas-queue-'))){
      assert.ok(x.html.includes('id="'+h.id+'"'));
      assert.ok(x.html.includes('href="#'+h.id+'"'));
    }
  }
});
