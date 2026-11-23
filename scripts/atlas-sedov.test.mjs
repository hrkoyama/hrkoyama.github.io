import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {createHash} from 'node:crypto';
const root=new URL('../',import.meta.url);
const bytes=p=>fs.readFileSync(new URL(p,root));
const json=p=>JSON.parse(bytes(p));
const hash=p=>createHash('sha256').update(bytes(p)).digest('hex');
const objectHash=x=>createHash('sha256').update(JSON.stringify(x)).digest('hex');
const base='code/validated-examples/2026-11-23-r2/sedov/';

test('Sedov adds one problem and release while preserving the previous thirteen frozen release records',()=>{
 const registry=json('numerical-methods-atlas/validation/releases.json');
 assert.equal(objectHash(registry.releases.filter(r=>!['sedov','double-mach','forward-step','low-mach','guderley'].includes(r.group))),'8f4b09898b9509788ae2e51e18846b6b5b7b71458fa7366b128ffcab4f1a43f3');
 assert.equal(registry.case_count,47);assert.equal(registry.releases.length,18);
 assert.equal(registry.releases.reduce((s,r)=>s+r.tests,0),571);
 const release=registry.releases.find(r=>r.group==='sedov');assert.equal(release.tests,23);assert.deepEqual(release.case_ids,['sedov-blast']);
 const problems=json('catalog/atlas-test-problems.json').problems;assert.equal(problems.length,86);assert.equal(problems.filter(p=>p.id==='sedov').length,1);
 assert.equal(json('catalog/atlas-methods.json').methods.length,147);
 assert.equal(json('catalog/atlas-execution-examples.json').examples.length,22);
 const manifest=json(base+'source-manifest.json');for(const[p,h]of Object.entries(manifest.files))assert.equal(hash(base+p),h,p);
 const receipt=json(base+'verification.json');assert.equal(receipt.tests,23);assert.equal(receipt.all_cases_rerun,true);assert.equal(receipt.passed,true);assert.equal(hash(base+receipt.archive.file),receipt.archive.sha256);
});

test('Sedov retains three fixed-source refinements, a separate source-radius probe and independent reference evidence',()=>{
 const result=json(base+'results/result.json'),c=result.cases[0];
 assert.equal(result.passed,true);assert.equal(result.termination,'fixed_budget_completed');
 assert.deepEqual(c.records.map(r=>r.n),[128,256,512]);assert.deepEqual(c.records.map(r=>r.deposit_radius),[.03,.03,.03]);
 assert.equal(c.source_radius_sensitivity.n,512);assert.equal(c.source_radius_sensitivity.deposit_radius,.015);
 assert.equal(Object.keys(c.checks).length,48);assert.ok(Object.values(c.checks).every(v=>v===true));
 for(const row of [...c.records,c.source_radius_sensitivity]){assert.equal(row.state_floor_count,0);assert.ok(row.conservation_relative.every(x=>x<=2e-12));assert.ok(Number.isFinite(row.center_density)&&Number.isFinite(row.center_pressure));}
 const reference=json(base+'exactpack-receipt.json');assert.equal(reference.passed,true);assert.equal(reference.reference_commit,'9bacc477eb791e959c9621e771fc7a725db755fa');
 assert.equal(reference.local_reference_sha256,hash(base+'reference_sedov.py'));assert.ok(Object.values(reference.checks).every(v=>v===true));
 assert.equal(reference.snapshot_sha256,hash(base+'exactpack-snapshot.json'));
 assert.ok(reference.errors.exactpack_beta_relative<2e-7);
 const contract=json(base+'pre-run-contract.json');assert.equal(contract.declared_before_first_pde_run,true);assert.equal(contract.planned_tests,23);
 for(const[p,h]of Object.entries(contract.files_sha256))assert.equal(hash(base+p),h,p+' remains as frozen before execution');
 const figures=json(base+'results/figure-manifest.json');assert.equal(figures.actual_cartesian_field,false);assert.equal(figures.figures.length,6);
 for(const f of figures.figures)assert.equal(hash(base+'results/'+f.path),f.sha256,f.path);
});

test('Sedov picture, methods, Euler equation, semi-analytic reference and executable package are connected',()=>{
 const page=json('numerical-methods-atlas/validation/sedov-blast/index.json');
 assert.equal(page.problem_id,'sedov');assert.deepEqual([...page.method_ids].sort(),['heun','rusanov']);
 assert.deepEqual(page.execution_navigation.equations.map(r=>r.id),['euler']);
 const problem=json('numerical-methods-atlas/problems/sedov/index.json');assert.deepEqual(problem.executions.map(r=>r.id),['sedov-blast']);assert.deepEqual(problem.references.map(r=>r.id),['sedov']);
 const reference=json('numerical-methods-atlas/solutions/index.json').cases.find(r=>r.id==='sedov');assert.equal(reference.kind,'semi-analytic');
 const item=json('numerical-methods-atlas/gallery/index.json').items.find(r=>r.id==='sedov');assert.ok(item.image.endsWith('/sedov/results/sedov-blast-preview.png'));assert.equal(hash(item.image.slice(1)),item.image_sha256);
 assert.deepEqual(item.supplemental_execution_entries.map(r=>r.id),['sedov-blast']);
 for(const lang of ['ja','en']){
  const html=bytes(`numerical-methods-atlas/${lang}/read/validation-sedov/index.html`).toString();assert.ok(html.includes('10.1098/rspa.1950.0049'));assert.ok(html.includes('ExactPack'));assert.ok(html.includes('sedov-blast'));
 }
});
