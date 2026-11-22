import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root),'utf8');
const inventory=JSON.parse(read('numerical-methods-atlas/test-cases/index.json'));
const catalog=JSON.parse(read('catalog/atlas-test-problems.json'));
const hash=b=>createHash('sha256').update(b).digest('hex');

test('the global count is derived from independent records and sums across domain and availability groups',()=>{
  const rows=inventory.problems,counts=inventory.counts;
  assert.equal(new Set(rows.map(x=>x.id)).size,rows.length);
  assert.equal(rows.length,catalog.problems.length);
  assert.equal(counts.test_problems,rows.length);
  assert.equal(counts.saved_test_problems+counts.code_test_problems,rows.length);
  assert.equal(Object.values(counts.groups).reduce((a,b)=>a+b,0),rows.length);
  for(const group of inventory.groups)assert.equal(rows.filter(x=>x.group===group.id).length,counts.groups[group.id]);
  assert.ok(['mhd','gravity','elliptic','time','approximation'].every(id=>counts.groups[id]>0));
});
test('evidence receipts, selected result records and code symbols still match the actual public edition',()=>{
  for(const [path,digest] of Object.entries(inventory.source_sha256))assert.equal(hash(readFileSync(new URL(path,root))),digest,path);
  for(const x of inventory.problems){
    assert.ok(x.evidence.length);
    for(const e of x.evidence){
      assert.ok(existsSync(new URL(e.path,root)),e.path);
      if(e.python_symbol)assert.ok(read(e.path).includes('def '+e.python_symbol+'('));
      if('json_pointer' in e){
        let value=JSON.parse(read(e.path));
        for(const key of e.json_pointer.split('/').slice(1))value=value[key.replaceAll('~1','/').replaceAll('~0','~')];
        assert.notEqual(value,undefined);
        if(e.where)assert.ok(value.some(row=>Object.entries(e.where).every(([k,v])=>row[k]===v)),x.id);
      }
    }
    for(const url of Object.values(x.reading))assert.ok(existsSync(new URL(new URL(url).pathname.slice(1)+'index.html',root)));
  }
});
test('all nine profile cases are included once, while repeated solver and Mach variants do not inflate problems',()=>{
  const wave=JSON.parse(read('numerical-methods-atlas/equation-gallery.json'));
  for(const item of wave.cases)assert.equal(inventory.problems.filter(x=>x.evidence.some(e=>e.path==='numerical-methods-atlas/equation-gallery.json'&&e.where?.id===item.id)).length,1,item.id);
  assert.equal(inventory.problems.filter(x=>x.id==='sod').length,1);
  assert.ok(inventory.problems.find(x=>x.id==='sod').evidence.length>2);
  assert.equal(inventory.problems.filter(x=>x.id==='nasa-wedge').length,1);
  assert.ok(!inventory.problems.some(x=>['wedge-m2','wedge-m2.5'].includes(x.id)));
  assert.ok(!inventory.problems.some(x=>/planned|reference-only/.test(x.availability)));
});
test('the new thermostat comparisons add one quartic problem and retain the original harmonic release',()=>{
  const base='code/validated-examples/2026-11-22/thermostats/';
  const cases=JSON.parse(read(base+'cases.json'));
  const results=JSON.parse(read(base+'results/result.json'));
  const receipt=JSON.parse(read(base+'verification.json'));
  const mapping=JSON.parse(read('catalog/atlas-depth-expansion.json')).case_problem_ids;
  assert.equal(catalog.problems.length,81);
  assert.equal(inventory.counts.groups.time,8);
  assert.equal(mapping['csvr-kinetic-kernel'],null);
  assert.equal(mapping['csvr-langevin-harmonic'],'langevin-harmonic');
  assert.equal(mapping['csvr-langevin-quartic'],'thermostatted-quartic');
  for(const id of ['csvr-kinetic-kernel','csvr-langevin-harmonic','csvr-langevin-quartic'])assert.ok(!catalog.problems.some(x=>x.id===id));
  const harmonic=catalog.problems.find(x=>x.id==='langevin-harmonic');
  assert.equal(harmonic.chapter,'validation-models');
  assert.equal(harmonic.code_base,'/code/validated-examples/2026-11-22/models/');
  assert.deepEqual(harmonic.supplemental_examples.map(x=>x.id),['langevin-harmonic','csvr-langevin-harmonic']);
  const quartic=catalog.problems.find(x=>x.id==='thermostatted-quartic');
  const metadata=cases.find(x=>x.id==='csvr-langevin-quartic');
  assert.equal(quartic.group,'time');
  assert.equal(quartic.chapter,'validation-thermostats');
  assert.deepEqual(quartic.name,metadata.title);
  assert.deepEqual(quartic.supplemental_examples.map(x=>x.id),['csvr-langevin-quartic']);
  assert.equal(results.input_sha256,hash(readFileSync(new URL(base+'inputs.json',root))));
  assert.equal(results.passed,true);
  for(const row of results.cases){assert.match(row.input_sha256,/^[a-f0-9]{64}$/);assert.equal(row.passed,true);assert.ok(Object.values(row.checks).every(Boolean));}
  assert.equal(receipt.group,'thermostats');
  assert.equal(receipt.all_cases_rerun,true);assert.equal(receipt.passed,true);
  assert.equal(receipt.errors+receipt.failures,0);
});
test('nonlinear Schnakenberg refinements reuse one physical problem and preserve the original onset evidence',()=>{
  const identifiers=['schnakenberg-nonlinear','schnakenberg-pattern'];
  const base='code/validated-examples/2026-11-22/biology/';
  const metadata=JSON.parse(read(base+'cases.json'));
  const mapping=JSON.parse(read('catalog/atlas-depth-expansion.json')).case_problem_ids;
  const problem=catalog.problems.find(x=>x.id==='turing-schnakenberg');
  assert.equal(catalog.problems.length,81);
  assert.equal(inventory.counts.groups.biology,5);
  assert.equal(problem.chapter,'validation-models');
  assert.equal(problem.code_base,'/code/validated-examples/2026-11-22/models/');
  assert.deepEqual(problem.supplemental_examples.map(x=>x.id),['turing-schnakenberg',...identifiers]);
  for(const id of identifiers){
    assert.equal(mapping[id],problem.id);
    assert.ok(!catalog.problems.some(x=>x.id===id));
    assert.deepEqual(problem.supplemental_examples.find(x=>x.id===id).name,metadata.find(x=>x.id===id).title);
    assert.deepEqual(metadata.find(x=>x.id===id).method_ids,['centered-difference','implicit-midpoint']);
  }
  assert.equal(problem.evidence[0].path,'code/validated-examples/2026-11-22/models/results/result.json');
  assert.equal(problem.evidence[1].path,'code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png');
  const output=JSON.parse(read(base+'results/result.json'));
  assert.equal(output.input_sha256,hash(readFileSync(new URL(base+'inputs.json',root))));
  assert.equal(output.passed,true);
  assert.deepEqual(output.cases.map(x=>x.id).sort(),[...identifiers].sort());
  assert.ok(output.cases.every(x=>x.passed&&Object.values(x.checks).every(v=>v===true)));
  const verification=JSON.parse(read(base+'verification.json'));
  assert.equal(verification.passed,true);assert.equal(verification.all_cases_rerun,true);
});
test('the public landing, coverage highlights and indexes expose the whole inventory',()=>{
  const page=read('numerical-methods-atlas/test-cases/index.html');
  assert.ok(page.includes('テスト計算：'+inventory.problems.length+'問題'));
  assert.ok(page.includes('data-site-language="ja"')&&page.includes('data-site-language="en"'));
  assert.ok(read('numerical-methods-atlas/coverage.js').includes('n:c.test_problems'));
  assert.ok(read('llms.txt').includes('Atlas-wide test-problem inventory'));
  assert.ok(JSON.parse(read('search/index.json')).documents.some(x=>x.url==='/numerical-methods-atlas/test-cases/'));
});
