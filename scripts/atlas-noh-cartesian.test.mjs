import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const root=new URL('../',import.meta.url),base='code/validated-examples/2026-11-23-r2/noh-cartesian/';
const bytes=p=>readFileSync(new URL(p,root)),json=p=>JSON.parse(bytes(p)),hash=p=>createHash('sha256').update(bytes(p)).digest('hex');

test('Cartesian Noh adds one scoped run while retaining all12 original release records',()=>{
 const registry=json('numerical-methods-atlas/validation/releases.json');
 const old=registry.releases.filter(r=>!['noh-cartesian','sedov','double-mach','forward-step','low-mach','guderley'].includes(r.group));
 assert.equal(old.length,12);
 assert.equal(createHash('sha256').update(JSON.stringify(old)).digest('hex'),'af35b7cc69704e07ded7957427be6fb60f91245e808c0e854d5e5d6543e4be69');
 assert.equal(old.reduce((s,r)=>s+r.tests,0),416);
 const fresh=registry.releases.find(r=>r.group==='noh-cartesian');assert.equal(fresh.tests,19);assert.deepEqual(fresh.case_ids,['noh-cartesian-2d']);
 assert.equal(registry.case_count,47);assert.equal(registry.releases.length,18);
 assert.equal(json('catalog/atlas-test-problems.json').problems.length,86);
 const manifest=json(base+'source-manifest.json');for(const[p,h]of Object.entries(manifest.files))assert.equal(hash(base+p),h,p);
 const verification=json(base+'verification.json');assert.equal(verification.tests,19);assert.equal(verification.all_cases_rerun,true);assert.equal(verification.passed,true);
});

test('Cartesian Noh retains the preregistered code,49 gates,full2D fields and nonmonotone orientation diagnostics',()=>{
 const c=json(base+'pre-run-contract.json'),a=json(base+'acceptance.json'),z=json(base+'results/result.json'),r=z.cases[0];
 assert.equal(c.unit_tests_or_pde_executed,false);assert.equal(c.planned_test_count,19);
 const envelope=json(base+'pre-run-envelope-contract.json');assert.equal(envelope.numerical_helper_AST_identical,true);assert.equal(hash(base+'run.py'),envelope.run_sha256);
 for(const[p,h]of Object.entries(c.files_sha256))if(p!=='run.py')assert.equal(hash(base+p),h,p);
 assert.equal(z.termination,'fixed_budget_completed');
 assert.equal(a.frozen_before_first_unit_or_pde_execution,true);assert.equal(z.passed,true);
 assert.equal(Object.keys(r.checks).length,49);assert.ok(Object.values(r.checks).every(x=>x===true));
 assert.deepEqual(r.records.map(x=>x.n),[32,64,128]);
 for(const row of r.records){assert.equal(row.state_floor_count,0);assert.ok(row.conservation_relative.every(v=>v<=a.limits.balance));assert.ok(row.reference_order_relative_l1_difference<=a.limits.reference_order);assert.ok(Number.isFinite(row.center_max_internal_energy_excess));}
 assert.ok(r.records[2].shock_axis_diagonal_difference_cells>r.records[1].shock_axis_diagonal_difference_cells,'the orientation difference is deliberately not hidden or required to decrease');
 assert.match(bytes(base+'README.md').toString(),/NOT monotone/);
 const manifest=json(base+'results/figure-manifest.json');assert.equal(manifest.actual_cartesian_field,true);assert.equal(manifest.validation_passed,true);assert.equal(manifest.figures.length,6);
 const program=`import zipfile,ast,struct\nfrom pathlib import Path\np=Path(${JSON.stringify(base+'results/field-n128.npz')})\nwith zipfile.ZipFile(p) as z:\n b=z.read('q.npy');major=b[6];size=struct.unpack('<H' if major==1 else '<I',b[8:10] if major==1 else b[8:12])[0];offset=10 if major==1 else 12;h=ast.literal_eval(b[offset:offset+size].decode());assert h['shape']==(128,128,4)\nprint('full square, four conserved components')`;
 assert.match(execFileSync('python3',['-B','-c',program],{cwd:fileURLToPath(root),encoding:'utf8',timeout:10000}),/four conserved/);
});

test('Cartesian Noh gallery,chapter,reference and method routes retain both the radial and2D editions',()=>{
 const id='noh-cartesian-2d';const problem=json('numerical-methods-atlas/problems/noh/index.json');
 assert.deepEqual(problem.executions.map(r=>r.id),['noh-shock',id]);
 const gallery=json('numerical-methods-atlas/gallery/index.json').items.find(r=>r.id==='noh');
 assert.equal(gallery.image,'/'+base+'results/'+id+'-preview.png');assert.equal(gallery.image_sha256,hash(gallery.image.slice(1)));
 assert.deepEqual(gallery.supplemental_execution_entries.map(r=>r.id),['noh-shock',id]);
 const run=json('numerical-methods-atlas/validation/'+id+'/index.json');assert.deepEqual([...run.method_ids].sort(),['heun','rusanov']);assert.equal(run.problem_id,'noh');
 assert.deepEqual(run.execution_navigation.equations.map(r=>r.id),['euler']);
 for(const language of ['ja','en'])assert.ok(bytes('numerical-methods-atlas/'+language+'/read/validation-noh-cartesian/index.html').includes(Buffer.from('49')));
 const methods=json('numerical-methods-atlas/methods/index.json').methods;
 for(const id of ['rusanov','heun'])assert.ok(methods.find(r=>r.id===id).depth_additional_releases.some(r=>r.group==='noh-cartesian'));
 for(const id of ['muscl','minmod'])assert.ok(!(methods.find(r=>r.id===id).depth_additional_releases||[]).some(r=>r.group==='noh-cartesian'));
});
