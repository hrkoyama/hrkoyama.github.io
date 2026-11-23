import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
const root=new URL('../',import.meta.url);
const bytes=p=>readFileSync(new URL(p,root));
const json=p=>JSON.parse(bytes(p));
const hash=p=>createHash('sha256').update(bytes(p)).digest('hex');
const objectHash=x=>createHash('sha256').update(JSON.stringify(x)).digest('hex');
const base='code/validated-examples/2026-11-23-r3/guderley/';

test('a metadata schema error is rejected before packaging launches scientific subprocesses',()=>{
 const program=String.raw`import importlib.util,json,tempfile
from pathlib import Path
from unittest.mock import patch
spec=importlib.util.spec_from_file_location('package_depth',Path('scripts/package-depth-examples.py'))
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
with tempfile.TemporaryDirectory(prefix='atlas-invalid-metadata-') as directory:
 p.ROOT=Path(directory);source=p.ROOT/'scripts/depth-guderley';source.mkdir(parents=True)
 case={'id':'fixture','method_ids':['hll'],'references':[{'review_level':'fixture'}]}
 case.update({key:{'ja':'条件','en':'Scope'} for key in ['title','summary','assumptions','algorithm','validation','validation_limits']})
 for name in ['run.py','inputs.json','requirements.txt','README.md','LICENSE']:(source/name).write_text('fixture')
 (source/'cases.json').write_text(json.dumps([case]))
 with patch.object(p.subprocess,'run',side_effect=AssertionError('scientific subprocess launched')) as child:
  try:p.package('guderley','2026-11-23')
  except KeyError as error:assert error.args==('limits',)
  else:raise AssertionError('invalid metadata accepted')
  assert child.call_count==0
 assert not (p.ROOT/'code').exists()
print('invalid metadata rejected before scientific execution')`;
 assert.match(execFileSync('python3',['-B','-c',program],{cwd:root,encoding:'utf8'}),/before scientific execution/);
});

test('Guderley adds one physical problem while preserving seventeen releases and all eighty-five earlier pictures',()=>{
 const registry=json('numerical-methods-atlas/validation/releases.json');
 assert.equal(objectHash(registry.releases.filter(r=>!['guderley','euler-positivity','zalesak'].includes(r.group))),'b95903d012a9887e306fcf32ee3955420226f179b2ab9861acd3a9aea94c54b6');
 assert.equal(registry.case_count,49);assert.equal(registry.releases.length,20);
 const release=registry.releases.find(r=>r.group==='guderley');assert.deepEqual(release.case_ids,['guderley-implosion']);
 assert.equal(registry.releases.filter(r=>!['euler-positivity','zalesak'].includes(r.group)).reduce((s,r)=>s+r.tests,0),538+release.tests);
 const pictures=json('numerical-methods-atlas/gallery/preview-manifest.json').items.filter(r=>!['guderley','zalesak'].includes(r.id)).map(({id,image,image_sha256,caption})=>({id,image,image_sha256,caption}));
 assert.equal(pictures.length,85);assert.equal(objectHash(pictures),'2a351e7c3700902a8c862474c75f7c2bd985b2c3312d573bdc9e2187f8def7f4');
 assert.equal(json('catalog/atlas-test-problems.json').problems.length,87);
 assert.equal(json('catalog/atlas-methods.json').methods.length,147);assert.equal(json('catalog/atlas-execution-examples.json').examples.length,22);
 const receipt=json(base+'verification.json');assert.equal(receipt.tests,release.tests);assert.equal(receipt.passed,true);assert.equal(receipt.all_cases_rerun,true);assert.equal(hash(base+receipt.archive.file),receipt.archive.sha256);
 for(const[p,h]of Object.entries(json(base+'source-manifest.json').files))assert.equal(hash(base+p),h,p);
});

test('the frozen spherical Guderley run retains cold upstream, reference qualification, three radial fields and discrete budgets',()=>{
 const contract=json(base+'pre-run-contract.json');for(const[p,h]of Object.entries(contract.files_sha256))assert.equal(hash(base+p),h,p);
 const cfg=json(base+'inputs.json').cases['guderley-implosion'];assert.deepEqual(cfg.grids,[128,256,512]);assert.equal(cfg.gamma,1.4);assert.equal(cfg.upstream_pressure,0);assert.equal(cfg.initial_time,-1);assert.equal(cfg.final_time,-.85);assert.equal(cfg.shock_radius_at_minus_one,.6);
 const historical=base+'references/attempts/01-eigenvalue-recompute/';const refContract=json(historical+'pre-reference-contract.json');assert.equal(refContract.declared_before_reference_execution,true);for(const[p,h]of Object.entries(refContract.files_sha256))assert.equal(hash(historical+p),h,p);
 const qualification=json(historical+'qualification.json');assert.equal(qualification.passed,true);assert.equal(Object.keys(qualification.checks).length,8);assert.ok(Object.values(qualification.checks).every(x=>x===true));assert.equal(qualification.original_state_calls.length,8);assert.equal(qualification.reflected_branch_executed,false);assert.equal(qualification.pde_evolution_executed,false);
 const cached=json(base+'references/cache-qualification.json');assert.equal(cached.passed,true);assert.equal(Object.keys(cached.checks).length,6);assert.equal(cached.full_eigenvalue_shooting_executed,false);assert.equal(cached.fresh_original_state_calls,0);assert.equal(cached.fresh_critical_phase_calls,1);
 assert.equal(contract.declared_before_first_pde_run,false);assert.equal(contract.declared_before_this_revision_pde_execution,true);assert.equal(contract.declared_before_this_revision_pytest_execution,true);
 const shared=json(base+'execution-receipts/gd-combined-03.json');assert.equal(shared.passed,true);assert.ok(shared.duration_seconds<120);assert.deepEqual(shared.commands.map(x=>x.returncode),[0,0]);
 const failed=json(base+'attempts/02/failed-linux-report.json').groups.find(x=>x.group==='guderley');assert.equal(failed.pytest.tests,33);assert.equal(failed.pytest.failures,0);assert.equal(failed.run_process.timed_out,true);
 const result=json(base+'results/result.json'),item=result.cases[0];assert.equal(result.passed,true);assert.deepEqual(item.records.map(r=>r.n),[128,256,512]);assert.equal(Object.keys(item.checks).length,contract.planned_numerical_gates);assert.ok(Object.values(item.checks).every(x=>x===true));
 for(const row of item.records){assert.equal(row.time,-.85);assert.equal(row.state_floor_count,0);assert.equal(row.rejected_steps,0);assert.ok(row.minimum_density_all_stages>0);assert.ok(row.minimum_internal_energy_all_stages>=-64*Number.EPSILON);assert.ok(row.conservation_relative.every(x=>x<=2e-12));assert.ok(row.shock_trajectory.length>1);assert.ok(Number.isFinite(row.density_linf)&&Number.isFinite(row.pressure_linf));}
 const program=String.raw`import ast,struct,zipfile
from pathlib import Path
p=Path('code/validated-examples/2026-11-23-r3/guderley/results/field-n512.npz')
with zipfile.ZipFile(p) as z:
 b=z.read('q.npy');assert b[:6]==b'\x93NUMPY';n=struct.unpack('<H',b[8:10])[0];h=ast.literal_eval(b[10:10+n].decode());assert h['shape']==(512,3)
 assert all(s in z.namelist() for s in ['q_initial.npy','q_reference.npy','q_history.npy','history_times.npy'])
for n in [128,256,512]:
 old=Path(f'code/validated-examples/2026-11-23-r2/guderley/results/field-n{n}.npz')
 new=Path(f'code/validated-examples/2026-11-23-r3/guderley/results/field-n{n}.npz')
 with zipfile.ZipFile(old) as a,zipfile.ZipFile(new) as b:
  assert set(a.namelist())==set(b.namelist())
  assert all(a.read(name)==b.read(name) for name in a.namelist())
print('three conserved radial components and saved trajectories')`;
 assert.match(execFileSync('python3',['-B','-c',program],{cwd:root,encoding:'utf8'}),/saved trajectories/);
});

test('Guderley gallery, Euler, semi-analytic reference, actual methods and execution are linked in both languages',()=>{
 const page=json('numerical-methods-atlas/validation/guderley-implosion/index.json');assert.equal(page.problem_id,'guderley');assert.deepEqual([...page.method_ids].sort(),['heun','hll']);assert.deepEqual(page.execution_navigation.equations.map(x=>x.id),['euler']);
 assert.ok(page.release.code_urls.every(url=>!new URL(url,'https://hrkoyama.github.io').pathname.split('/').includes('attempts')),'historical source remains downloadable through its manifest but is excluded from active code links');
 const problem=json('numerical-methods-atlas/problems/guderley/index.json');assert.deepEqual(problem.executions.map(x=>x.id),['guderley-implosion']);assert.ok(problem.references.some(x=>x.id==='guderley'));
 const reference=json('numerical-methods-atlas/solutions/index.json').cases.find(x=>x.id==='guderley');assert.equal(reference.kind,'semi-analytic');assert.equal(reference.dimension,1);
 const gallery=json('numerical-methods-atlas/gallery/index.json').items.find(x=>x.id==='guderley');assert.equal(gallery.runnable,true);assert.equal(hash(gallery.image.slice(1)),gallery.image_sha256);
 for(const lang of ['ja','en']){const html=bytes(`numerical-methods-atlas/${lang}/read/validation-guderley/index.html`).toString();assert.ok(html.includes('10.1080/10618562.2011.647768'));assert.ok(html.includes('10.1016/j.softx.2023.101560'));assert.ok(html.includes('guderley-implosion'));}
});
