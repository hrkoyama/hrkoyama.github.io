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
const base='code/validated-examples/2026-11-23/forward-step/';

test('forward step preserves all fifteen published releases and eighty-three historical gallery pictures',()=>{
 const registry=json('numerical-methods-atlas/validation/releases.json');
 assert.equal(objectHash(registry.releases.filter(r=>!['forward-step','low-mach','guderley','euler-positivity','zalesak','weno-critical','shallow-water','wall-flow','level-set', 'instability-growth', 'mhd-transport', 'mesh-boundary', 'moving-waves', 'relativistic', 'sem-fr','coefficient-diffusion','slab-ewald','fmm3d','gravity-dynamics','warm-pic','pic-spatial','dsmc-wall','dsmc-shock'].includes(r.group))),'22b3f44f5555a2e12fbacb96b4a4ccc57fb5e620a971df9c548908695cb4225b');
 assert.equal(registry.case_count,83);assert.equal(registry.releases.length,38);assert.equal(registry.releases.filter(r=>!['euler-positivity','zalesak','weno-critical','shallow-water','wall-flow','level-set', 'instability-growth', 'mhd-transport', 'mesh-boundary', 'moving-waves', 'relativistic', 'sem-fr','coefficient-diffusion','slab-ewald','fmm3d','gravity-dynamics','warm-pic','pic-spatial','dsmc-wall','dsmc-shock'].includes(r.group)).reduce((s,r)=>s+r.tests,0),571);
 const release=registry.releases.find(r=>r.group==='forward-step');assert.equal(release.tests,24);assert.deepEqual(release.case_ids,['forward-step-m3']);
 const pictures=json('numerical-methods-atlas/gallery/preview-manifest.json').items.filter(r=>!['forward-step','isentropic-vortex','guderley','zalesak','swashes-topography','dry-bed-dam-break','lid-driven-cavity','wall-manufactured','level-set-circle', 'kh-initial-growth', 'rt-initial-growth', 'lshape-fem', 'annular-viscous-mms', 'poisson-neumann', 'poisson-robin', 'ale-nonuniform-transport', 'cgrid-rotating-wave', 'srhd-collision', 'srmhd-alfven','checkerboard-diffusion','rotated-anisotropic-diffusion','neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short','thermal-landau-damping','thermal-two-stream','dsmc-couette','dsmc-fourier','dsmc-planar-shock'].includes(r.id)).map(({id,image,image_sha256,caption})=>({id,image,image_sha256,caption}));
 assert.equal(pictures.length,83);assert.equal(objectHash(pictures),'cc42574f290cd31549ef959f4bc97086be02d90e57655fcf5d2c172dbf3203b6');
 assert.equal(json('catalog/atlas-test-problems.json').problems.length,113);assert.equal(json('catalog/atlas-methods.json').methods.length,152);assert.equal(json('catalog/atlas-execution-examples.json').examples.length,22);
 const manifest=json(base+'source-manifest.json');for(const[p,h]of Object.entries(manifest.files))assert.equal(hash(base+p),h,p);
 const receipt=json(base+'verification.json');assert.equal(receipt.tests,24);assert.equal(receipt.passed,true);assert.equal(receipt.all_cases_rerun,true);assert.equal(hash(base+receipt.archive.file),receipt.archive.sha256);
});

test('forward step keeps fixed acceptance, real masked 2D fields and independently computed finite-grid references',()=>{
 const contract=json(base+'pre-run-contract.json');
 assert.equal(contract.declared_before_first_primary_pde_or_unit_execution,true);assert.equal(contract.planned_tests,24);assert.equal(contract.planned_numerical_gates,45);
 for(const[p,h]of Object.entries(contract.files_sha256))assert.equal(hash(base+p),h,p);
 const cfg=json(base+'inputs.json').cases['forward-step-m3'];assert.deepEqual(cfg.grids,[20,40,80]);assert.equal(cfg.final_time,4);assert.equal(cfg.corner_entropy_fix,false);
 const result=json(base+'results/result.json'),r=result.cases[0];assert.equal(result.passed,true);assert.equal(result.termination,'fixed_budget_completed');
 assert.deepEqual(r.records.map(x=>[x.nx,x.ny]),[[60,20],[120,40],[240,80]]);assert.equal(Object.keys(r.checks).length,45);assert.ok(Object.values(r.checks).every(v=>v===true));
 for(const row of r.records){assert.equal(row.time,4);assert.equal(row.state_floor_count,0);assert.equal(row.rejected_steps,0);assert.ok(row.conservation_relative.every(v=>v<=3e-12));assert.ok(row.wall_mass_energy_max_abs<=2e-13);assert.ok(Math.abs(row.fluid_area-2.52)<1e-14);}
 const quality=json(base+'references/quality.json');assert.equal(quality.passed,true);assert.equal(quality.new_reference_pde_executed,true);assert.equal(quality.corner_entropy_reset,false);assert.equal(quality.primary_operator_imports,false);
 const execution=json(base+'references/independent-execution.json');assert.equal(execution.passed,true);assert.equal(execution.source_language,'C++17');
 const performance=json(base+'references/performance-revision-comparison.json');assert.equal(performance.q_bitwise_equal,true);assert.equal(performance.steps_equal,true);assert.equal(performance.q_max_abs_difference,0);
 const oldReference=json(base+'references/attempts/01/independent-execution.json');assert.equal(oldReference.passed,false);assert.ok(oldReference.processes.some(p=>p.name==='reference-ny160'&&p.timed_out===true));
 const refContract=json(base+'references/pre-run-contract.json');for(const[p,h]of Object.entries(refContract.files_sha256))assert.equal(hash(base+'references/'+p),h,p);
 for(const n of [80,160]){const meta=json(base+`references/forward-step-ny${n}.json`);assert.equal(meta.time,4);assert.equal(meta.npz_sha256,hash(base+`references/forward-step-ny${n}.npz`));assert.equal(meta.new_reference_pde_executed,true);}
 const program=String.raw`import ast,struct,zipfile
from pathlib import Path
p=Path('code/validated-examples/2026-11-23/forward-step/results/field-ny80.npz')
with zipfile.ZipFile(p) as z:
 b=z.read('q.npy');assert b[:6]==b'\x93NUMPY';n=struct.unpack('<H',b[8:10])[0];h=ast.literal_eval(b[10:10+n].decode());assert h['shape']==(240,80,4)
 assert 'fluid.npy' in z.namelist()
print('actual masked 2D output checked')`;
 assert.match(execFileSync('python3',['-B','-c',program],{cwd:root,encoding:'utf8'}),/actual masked 2D/);
});

test('forward-step picture links Euler, methods, numerical reference, chapter and executable ZIP',()=>{
 const page=json('numerical-methods-atlas/validation/forward-step-m3/index.json');assert.equal(page.problem_id,'forward-step');assert.deepEqual([...page.method_ids].sort(),['heun','hll']);assert.deepEqual(page.execution_navigation.equations.map(x=>x.id),['euler']);
 const problem=json('numerical-methods-atlas/problems/forward-step/index.json');assert.deepEqual(problem.executions.map(x=>x.id),['forward-step-m3']);assert.deepEqual(problem.references.map(x=>x.id),['forward-step']);
 const reference=json('numerical-methods-atlas/solutions/index.json').cases.find(x=>x.id==='forward-step');assert.equal(reference.kind,'numerical-reference');assert.equal(reference.dimension,2);
 const item=json('numerical-methods-atlas/gallery/index.json').items.find(x=>x.id==='forward-step');assert.ok(item.image.endsWith('/forward-step/results/forward-step-m3-preview.png'));assert.equal(hash(item.image.slice(1)),item.image_sha256);assert.equal(item.runnable,true);
 for(const lang of ['ja','en']){
  const html=bytes(`numerical-methods-atlas/${lang}/read/validation-forward-step/index.html`).toString();assert.ok(html.includes('10.1016/0021-9991(84)90142-6'));assert.ok(html.includes('forward-step-m3'));
  assert.ok(bytes(`numerical-methods-atlas/${lang}/read/nasa-2d/index.html`).toString().includes('forward-step-validation-followup'));
 }
});
