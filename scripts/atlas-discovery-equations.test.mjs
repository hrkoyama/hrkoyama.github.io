import test from 'node:test';
import assert from 'node:assert/strict';
import {existsSync,readFileSync} from 'node:fs';

const root=new URL('../',import.meta.url);
const read=path=>readFileSync(new URL(path,root),'utf8');
const json=path=>JSON.parse(read(path));
const config=json('catalog/atlas-execution-discovery.json');
const registry=json('catalog/atlas-execution-examples.json');
const coverage=json('numerical-methods-atlas/coverage.json');
const source=json('catalog/atlas-equations.json');
const published=json('numerical-methods-atlas/equations/index.json');
const html=read('numerical-methods-atlas/equations/index.html');
const sorted=items=>[...items].sort();
const entry=(id,lang)=>`https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/${id}/?lang=${lang}`;

test('all execution families have scoped bilingual formula and outcome metadata',()=>{
  assert.equal(config.examples.length,22);
  assert.deepEqual(sorted(config.examples.map(x=>x.id)),sorted(registry.examples.map(x=>x.id)));
  const equations=new Map(source.equations.map(x=>[x.id,x]));
  for(const row of config.examples){
    const original=registry.examples.find(x=>x.id===row.id);
    assert.equal(row.problem_id,original.problem_id);
    assert.ok(['problem','approximation','diagnostic'].includes(row.formula.role));
    assert.ok(row.formula.latex.length&&row.formula.latex.every(x=>typeof x==='string'&&x.trim()));
    assert.ok(row.keywords.length);
    for(const lang of ['ja','en'])assert.ok(row.outcome[lang]&&row.formula.note[lang]);
    for(const id of row.equation_ids)assert.equal(equations.get(id)?.status,'local-example',`${row.id} promotes ${id}`);
  }
  const helium=config.examples.find(x=>x.id==='helium-ground-state');
  for(const alias of ['UHF','ROHF','PBE','PBE0','SCAN','B3LYP','GGA','meta-GGA','hybrid']){
    assert.ok(!helium.keywords.some(x=>x.toLowerCase()===alias.toLowerCase()),alias);
  }
  assert.deepEqual(helium.equation_ids,['hartree-fock-model','kohn-sham-model']);
  for(const id of ['stiff-cosine','smooth-function-projection'])assert.deepEqual(config.examples.find(x=>x.id===id).equation_ids,[]);
});

test('twenty-two execution formulas stay separate from the unchanged model inventory',()=>{
  assert.equal(published.counts.total,coverage.counts.equations);
  assert.equal(published.counts.total,56);
  assert.equal(published.equations.length,source.equations.length);
  assert.equal(published.counts.local_example,coverage.counts.local_equations);
  assert.equal(published.counts.reading_only,coverage.counts.reading_equations);
  assert.equal(published.execution_example_count,22);
  assert.deepEqual(sorted(published.execution_examples.map(x=>x.id)),sorted(config.examples.map(x=>x.id)));
  assert.equal((html.match(/data-equation-id=/g)||[]).length,2*coverage.counts.equations);
  assert.equal((html.match(/data-execution-equation-id=/g)||[]).length,44);
  for(const model of published.equations){
    const previous=source.equations.find(x=>x.id===model.id);
    assert.equal(model.status,previous.status);
    assert.deepEqual(model.formula,previous.formula);
    const expected=config.examples.filter(x=>x.equation_ids.includes(model.id));
    assert.deepEqual(sorted(model.execution_examples.map(x=>x.id)),sorted(expected.map(x=>x.id)));
    if(model.status==='reading')assert.deepEqual(model.execution_examples,[]);
  }
  assert.deepEqual(published.equations.find(x=>x.id==='time-dependent-kohn-sham').execution_examples,[]);
  assert.equal(coverage.counts.test_problems,102);
});

test('formula shortcuts contain static math and direct input/run/validation routes',()=>{
  assert.ok(!html.includes('katex-error'));
  for(const row of published.execution_examples){
    const original=config.examples.find(x=>x.id===row.id);
    assert.deepEqual(row.formula,original.formula);
    for(const lang of ['ja','en']){
      assert.equal(row.entry[lang],entry(row.id,lang));
      const card=html.match(new RegExp(`<article[^>]*data-execution-equation-id="${row.id}"[^>]*>[\\s\\S]*?<\\/article>`,'g'))?.find(x=>x.includes(`execution-${row.id}-${lang}`));
      assert.ok(card,`${row.id}/${lang}`);
      assert.ok(card.includes('katex-mathml')&&card.includes('application/x-tex'));
      assert.ok(card.includes(`href="${entry(row.id,lang)}"`));
      assert.ok(!card.includes('#/'));
      assert.ok(existsSync(new URL(`numerical-methods-atlas/code-and-data/examples/${row.id}/index.html`,root)));
    }
  }
  for(const lang of ['ja','en']){
    assert.ok(html.includes(`id="execution-formulas-${lang}"`));
    assert.ok(html.includes(`id="all-models-${lang}"`));
  }
});
