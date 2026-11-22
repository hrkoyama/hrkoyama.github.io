import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {searchChapters} from '../numerical-methods-atlas/home-search.js';
const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root),'utf8');
const json=p=>JSON.parse(read(p));

test('method and problem records lead to the same stable execution examples in both languages',()=>{
  const examples=json('catalog/atlas-execution-examples.json').examples;
  const methods=json('numerical-methods-atlas/methods/index.json').methods;
  const problems=json('numerical-methods-atlas/test-cases/index.json').problems;
  const page=read('numerical-methods-atlas/code-and-data/index.html');
  assert.equal(examples.length,22);
  assert.equal(problems.length,80);
  for(const e of examples){
    const records=[problems.find(p=>p.id===e.problem_id),...e.method_ids.map(id=>methods.find(m=>m.id===id))];
    for(const record of records){
      assert.ok(record,e.id);
      const link=record.execution_examples.find(x=>x.id===e.id);
      assert.ok(link,e.id);
      assert.equal(link.registry_url,'https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json');
      for(const lang of ['ja','en']){
        assert.ok(link.guide[lang].endsWith('#'+e.id+'-'+lang));
        assert.ok(page.includes('id="'+e.id+'-'+lang+'"'));
      }
    }
  }
  for(const id of ['ewald','pme','spme']){
    const m=methods.find(x=>x.id===id);
    assert.equal(m.status,'educational-example');
    const ids=id==='ewald'?['ewald']:['spme'];
    assert.deepEqual(m.depth_release.case_ids,ids);
    assert.deepEqual(m.execution_examples.map(x=>x.id),ids);
    for(const entry of m.execution_examples){
      assert.equal(entry.kind,'dedicated-supplement');
      assert.equal(entry.registry_url,'https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json');
      assert.ok(!examples.some(x=>x.id===entry.id),'supplement must not rewrite the common registry');
      for(const lang of ['ja','en'])assert.equal(entry.guide[lang],`https://hrkoyama.github.io/numerical-methods-atlas/validation/${entry.id}/?lang=${lang}`);
    }
  }
});

test('the atom chapter and atlas search expose the shared execution instructions',()=>{
  for(const lang of ['ja','en']){
    const route=`numerical-methods-atlas/${lang}/read/quantum-atoms/`;
    const chapter=json(route+'index.json');
    assert.equal(chapter.execution_registry,'https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json');
    assert.ok(read(route+'index.html').includes('/numerical-methods-atlas/code-and-data/'));
  }
  const index=json('numerical-methods-atlas/home-search-index.json');
  for(const [q,lang] of [['共通手順','ja'],['execution guide','en']]){
    assert.ok(searchChapters(index,q,lang).some(x=>x.url?.startsWith('/numerical-methods-atlas/code-and-data/')),q);
  }
  assert.ok(read('llms.txt').includes('Shared execution records / JSON'));
});

test('a receipt for different registry bytes cannot be presented as current validation',()=>{
  const check=`import copy, importlib.util, json, pathlib
p=pathlib.Path('scripts/build-atlas-execution-guide.py')
s=importlib.util.spec_from_file_location('execution_guide',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
d=json.loads(pathlib.Path('catalog/atlas-execution-examples.json').read_text())
r=json.loads((pathlib.Path('.')/d['verification_receipt'].split('hrkoyama.github.io/')[1]).read_text())
m.validate_receipt(r,d,pathlib.Path('.'))
bad=copy.deepcopy(r);bad['registry_sha256']='0'*64
try:m.validate_receipt(bad,d,pathlib.Path('.'))
except (ValueError,AssertionError):pass
else:raise AssertionError('stale receipt accepted')
`;
  execFileSync('python3',['-c',check],{cwd:root,encoding:'utf8'});
});
