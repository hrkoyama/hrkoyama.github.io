import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
const root=new URL('../',import.meta.url);
const bytes=p=>fs.readFileSync(new URL(p,root));
const json=p=>JSON.parse(bytes(p));
const hash=p=>createHash('sha256').update(bytes(p)).digest('hex');
const objectHash=x=>createHash('sha256').update(JSON.stringify(x)).digest('hex');
const base='code/validated-examples/2026-11-23/double-mach/';

test('Double Mach extends an existing problem and preserves all fourteen earlier release records and eighty-three historical pictures',()=>{
 const registry=json('numerical-methods-atlas/validation/releases.json');
 assert.equal(objectHash(registry.releases.filter(r=>!['double-mach','forward-step'].includes(r.group))),'bb57fe2ece2d6f8b07b9e793ab8a21c3a9bcc2166d0e04dd73e00fe9d9ed46c3');
 assert.equal(registry.case_count,45);assert.equal(registry.releases.length,16);assert.equal(registry.releases.reduce((s,r)=>s+r.tests,0),503);
 const release=registry.releases.find(r=>r.group==='double-mach');assert.equal(release.tests,21);assert.deepEqual(release.case_ids,['double-mach-reflection']);
 const pictures=json('numerical-methods-atlas/gallery/preview-manifest.json').items.filter(r=>!['double-mach','forward-step'].includes(r.id)).map(({id,image,image_sha256,caption})=>({id,image,image_sha256,caption}));
 assert.equal(pictures.length,83);assert.equal(objectHash(pictures),'bf57e7292598ba2f200c4bc020dfb93d2e3ce2799dfee5b4f47e145caf5a29b4');
 assert.equal(json('catalog/atlas-test-problems.json').problems.length,85);assert.equal(json('catalog/atlas-methods.json').methods.length,147);assert.equal(json('catalog/atlas-execution-examples.json').examples.length,22);
 const manifest=json(base+'source-manifest.json');for(const[p,h]of Object.entries(manifest.files))assert.equal(hash(base+p),h,p);
 const receipt=json(base+'verification.json');assert.equal(receipt.tests,21);assert.equal(receipt.passed,true);assert.equal(receipt.all_cases_rerun,true);assert.equal(hash(base+receipt.archive.file),receipt.archive.sha256);
});

test('Double Mach retains preregistered criteria, full two-dimensional output and independently executed finite-grid reference provenance',()=>{
 const c=json(base+'pre-run-contract.json'),old=json(base+'contract-before-front-guard.json');
 assert.equal(c.declared_before_this_revision_execution,true);assert.equal(c.planned_tests,21);assert.equal(c.initial_unit_tests_passed,20);assert.equal(c.full_refinement_executed,false);
 assert.equal(c.previous_contract_sha256,hash(base+'contract-before-front-guard.json'));
 for(const[p,h]of Object.entries(c.files_sha256))assert.equal(hash(base+p),h,p);
 for(const p of ['dm_solver.py','inputs.json','acceptance.json'])assert.equal(c.files_sha256[p],old.files_sha256[p],p+' remained fixed through the diagnostic-only revision');
 const result=json(base+'results/result.json'),r=result.cases[0];assert.equal(result.passed,true);assert.equal(result.termination,'fixed_budget_completed');
 assert.deepEqual(r.records.map(x=>[x.nx,x.ny]),[[64,16],[128,32],[256,64]]);assert.ok(r.records.every(x=>x.time===.2));assert.equal(Object.keys(r.checks).length,40);assert.ok(Object.values(r.checks).every(v=>v===true));
 for(const row of r.records){assert.equal(row.state_floor_count,0);assert.equal(row.rejected_steps,0);assert.ok(row.conservation_relative.every(v=>v<=2e-12));}
 const provenance=json(base+'references/independent-reuse.json');assert.equal(provenance.new_reference_pde_executed,false);assert.equal(provenance.source_release.archive_sha256,'6fa8d75c1f70281eb0a78363eb3323c5a9a1b006f01f49182c4827f4d5710a69');
 for(const[p,h]of Object.entries(provenance.files_sha256))assert.equal(hash(base+'references/'+p),h,p);
 const program=String.raw`import ast,struct,zipfile
from pathlib import Path
p=Path('code/validated-examples/2026-11-23/double-mach/results/field-ny64.npz')
with zipfile.ZipFile(p) as z:
 b=z.read('q.npy');assert b[:6]==b'\x93NUMPY';n=struct.unpack('<H',b[8:10])[0];h=ast.literal_eval(b[10:10+n].decode());assert h['shape']==(256,64,4)
print('actual 2D conserved output checked')`;
 assert.match(execFileSync('python3',['-B','-c',program],{cwd:root,encoding:'utf8'}),/actual 2D/);
});

test('Double Mach gallery, Euler equation, methods, numerical-reference card and executable code form one route',()=>{
 const page=json('numerical-methods-atlas/validation/double-mach-reflection/index.json');assert.equal(page.problem_id,'double-mach');assert.deepEqual([...page.method_ids].sort(),['heun','hll']);assert.deepEqual(page.execution_navigation.equations.map(x=>x.id),['euler']);
 const problem=json('numerical-methods-atlas/problems/double-mach/index.json');assert.deepEqual(problem.executions.map(x=>x.id),['double-mach-reflection']);assert.deepEqual(problem.references.map(x=>x.id),['double-mach']);
 const reference=json('numerical-methods-atlas/solutions/index.json').cases.find(x=>x.id==='double-mach');assert.equal(reference.kind,'numerical-reference');assert.equal(reference.dimension,2);
 const item=json('numerical-methods-atlas/gallery/index.json').items.find(x=>x.id==='double-mach');assert.ok(item.image.endsWith('/double-mach/results/double-mach-reflection-preview.png'));assert.equal(hash(item.image.slice(1)),item.image_sha256);
 for(const lang of ['ja','en']){
  const html=bytes(`numerical-methods-atlas/${lang}/read/validation-double-mach/index.html`).toString();assert.ok(html.includes('10.1016/0021-9991(84)90142-6'));assert.ok(html.includes('double-mach-reflection'));
  assert.ok(bytes(`numerical-methods-atlas/${lang}/read/double-mach/index.html`).toString().includes('double-mach-validation-followup'),'historical chapter points to the new scoped evidence');
 }
});
