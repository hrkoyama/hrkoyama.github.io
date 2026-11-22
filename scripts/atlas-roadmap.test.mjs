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
  assert.equal(new Set(queue.items.map(x=>x.id)).size,queue.items.length);
  for(const id of ['current-roadmap','executable-example-registry']){
    const x=queue.items.find(x=>x.id===id);
    assert.ok(['in-progress','published'].includes(x.state));
    assert.equal(x.priority,'P0');assert.equal(x.track,'current');
  }
  const h2=queue.items.find(x=>x.id==='molecular-quantum-example');assert.equal(h2.state,'published-verified-example');assert.equal(h2.track,'current');
  for(const id of ['ewald-pme-spme']){
    const x=queue.items.find(x=>x.id===id);
    assert.equal(x.state,'conditional-planned');assert.equal(x.track,'conditional');
  }
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
  assert.deepEqual(queue.milestones.map(x=>x.target),['2026-11-30','2026-12-12','2026-12-18','2026-12-23','2026-12-31']);
  for(const lang of ['ja','en']){
    for(const x of queue.milestones)assert.ok(rendered[lang].html.includes(x.title[lang]));
    assert.ok(rendered[lang].html.includes(queue.milestones.find(x=>x.id==='year-end-edition').scope[lang]));
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
