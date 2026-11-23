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
const base='code/validated-examples/2026-11-23/low-mach/';

test('low-Mach vortex preserves sixteen frozen release records and eighty-four other pictures',()=>{
 const registry=json('numerical-methods-atlas/validation/releases.json');
 assert.equal(objectHash(registry.releases.filter(r=>r.group!=='low-mach')),'59a536ae50edae648ee6306e24a2597ba79d20eba0c1ffd23d7aab9e1d289804');
 assert.equal(registry.case_count,46);assert.equal(registry.releases.length,17);assert.equal(registry.releases.reduce((s,r)=>s+r.tests,0),538);
 const release=registry.releases.find(r=>r.group==='low-mach');assert.equal(release.tests,35);assert.deepEqual(release.case_ids,['low-mach-vortex']);
 const pictures=json('numerical-methods-atlas/gallery/preview-manifest.json').items.filter(r=>r.id!=='isentropic-vortex').map(({id,image,image_sha256,caption})=>({id,image,image_sha256,caption}));
 assert.equal(pictures.length,84);assert.equal(objectHash(pictures),'1b8d229d378a47d05a78a8d2c3ca6350c794b1cee3366a0a12c7805602a84107');
 assert.equal(json('catalog/atlas-test-problems.json').problems.length,85);assert.equal(json('catalog/atlas-methods.json').methods.length,147);assert.equal(json('catalog/atlas-execution-examples.json').examples.length,22);
 const manifest=json(base+'source-manifest.json');for(const[p,h]of Object.entries(manifest.files))assert.equal(hash(base+p),h,p);
 const receipt=json(base+'verification.json');assert.equal(receipt.tests,35);assert.equal(receipt.passed,true);assert.equal(receipt.all_cases_rerun,true);assert.equal(hash(base+receipt.archive.file),receipt.archive.sha256);
});

test('the frozen low-Mach comparison keeps physical Euler time, twelve full2D runs and explicit stability qualifications',()=>{
 const contract=json(base+'pre-run-contract.json');assert.equal(contract.declared_before_this_revision_test_or_pde_execution,true);assert.equal(contract.planned_tests,35);assert.equal(contract.planned_numerical_gates,143);
 for(const[p,h]of Object.entries(contract.files_sha256))assert.equal(hash(base+p),h,p);
 const initial=json(base+'attempts/01/results/result.json');assert.equal(initial.passed,false);assert.equal(initial.cases[0].records.length,12);
 const failures=initial.cases[0].check_details.filter(c=>!c.passed);assert.equal(failures.length,1);assert.equal(failures[0].bound,.1);assert.ok(failures[0].value>.16);assert.match(failures[0].name,/pressure_dynamic_l1/);
 for(const name of ['inputs.json','acceptance.json'])assert.equal(hash(base+name),hash(base+'attempts/01/'+name),name+' remained byte-identical after the retained first-order failure');
 const cfg=json(base+'inputs.json').cases['low-mach-vortex'];assert.deepEqual(cfg.grids,[16,32,64]);assert.deepEqual(cfg.mach_far_values,[.1,.01]);assert.deepEqual(cfg.variants,['roe','miczek']);assert.equal(cfg.final_time,.1);assert.equal(cfg.time_integrator,'SSPRK33');assert.equal(cfg.cfl,.2);
 const result=json(base+'results/result.json'),r=result.cases[0];assert.equal(result.passed,true);assert.equal(result.termination,'fixed_budget_completed');assert.equal(r.records.length,12);
 const expected=cfg.mach_far_values.flatMap(m=>cfg.variants.flatMap(v=>cfg.grids.map(n=>[m,v,n])));assert.deepEqual(r.records.map(x=>[x.mach_far,x.variant,x.n]),expected);
 assert.equal(Object.keys(r.checks).length,143);assert.ok(Object.values(r.checks).every(v=>v===true));
 for(const row of r.records){assert.equal(row.time,.1);assert.equal(row.state_floor_count,0);assert.equal(row.rejected_steps,0);assert.ok(row.minimum_density_all_stages>0);assert.ok(row.minimum_pressure_all_stages>0);assert.ok(row.conservation_relative.every(v=>v<=3e-12));assert.ok(row.convective_to_acoustic_dt_ratio>1);}
 assert.equal(r.linear_stability.length,4);
 for(const row of r.linear_stability){assert.equal(row.sampled_2d_modes,289);assert.deepEqual(row.power_indices,[1,10,100]);assert.ok(row.maximum_SSPRK3_spectral_radius<=1.00000000005);assert.ok(row.maximum_energy_scaled_power_norm<=4);}
 assert.ok(r.linear_stability.find(x=>x.mach_far===.01&&x.variant==='miczek').maximum_forward_Euler_spectral_radius>1.00001,'forward Euler at this acoustic step is retained as an explicit counterexample');
 assert.ok(r.reference_qualification.maximum_point_Euler_residual<=1e-11);assert.ok(r.reference_qualification.maximum_quadrature_dynamic_difference<=2e-7);
 const program=String.raw`import ast,struct,zipfile
from pathlib import Path
p=Path('code/validated-examples/2026-11-23/low-mach/results/field-M0.01-miczek-n64.npz')
with zipfile.ZipFile(p) as z:
 b=z.read('q.npy');assert b[:6]==b'\x93NUMPY';n=struct.unpack('<H',b[8:10])[0];h=ast.literal_eval(b[10:10+n].decode());assert h['shape']==(64,64,4)
 assert 'q_reference.npy' in z.namelist()
print('actual full2D field and conserved-average reference checked')`;
 assert.match(execFileSync('python3',['-B','-c',program],{cwd:root,encoding:'utf8'}),/actual full2D/);
});

test('low-Mach execution, analytic reference, method status and the existing vortex picture are connected',()=>{
 const page=json('numerical-methods-atlas/validation/low-mach-vortex/index.json');assert.equal(page.problem_id,'isentropic-vortex');assert.deepEqual([...page.method_ids].sort(),['low-mach-preconditioning','muscl','roe','ssprk33']);assert.deepEqual(page.execution_navigation.equations.map(x=>x.id),['euler']);
 const problem=json('numerical-methods-atlas/problems/isentropic-vortex/index.json');assert.ok(problem.executions.some(x=>x.id==='low-mach-vortex'));assert.ok(problem.references.some(x=>x.id==='isentropic-vortex'));
 const reference=json('numerical-methods-atlas/solutions/index.json').cases.find(x=>x.id==='isentropic-vortex');assert.equal(reference.kind,'analytic');assert.equal(reference.dimension,2);
 const methods=json('numerical-methods-atlas/methods/index.json').methods;const low=methods.find(x=>x.id==='low-mach-preconditioning');assert.equal(low.status,'educational-example');assert.equal(low.depth_release.group,'low-mach');
 assert.deepEqual(Object.fromEntries(['educational-example','reading-only','planned'].map(s=>[s,methods.filter(m=>m.status===s).length])),{'educational-example':117,'reading-only':14,planned:16});
 const item=json('numerical-methods-atlas/gallery/index.json').items.find(x=>x.id==='isentropic-vortex');assert.ok(item.image.endsWith('/low-mach/results/low-mach-vortex-preview.png'));assert.equal(hash(item.image.slice(1)),item.image_sha256);assert.equal(item.runnable,true);
 for(const lang of ['ja','en']){const html=bytes(`numerical-methods-atlas/${lang}/read/validation-low-mach/index.html`).toString();assert.ok(html.includes('10.1051/0004-6361/201425059'));assert.ok(html.includes('low-mach-vortex'));}
});
