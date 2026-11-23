import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {makeSearch} from '../search/engine.mjs';
import {searchChapters} from '../numerical-methods-atlas/home-search.js';

const root=new URL('../',import.meta.url),base='code/validated-examples/2026-11-23/level-set/';
const text=p=>readFileSync(new URL(p,root),'utf8'),json=p=>JSON.parse(text(p));
const sha=p=>createHash('sha256').update(readFileSync(new URL(p,root))).digest('hex');
const objectHash=x=>createHash('sha256').update(JSON.stringify(x)).digest('hex');
// Only these eight existing methods gained the separately validated batch13–17 bindings/scope.
// Their original IDs, names, statuses and all other scientific metadata remain in the golden.
const batchBindingFields={"p1-fem":["depth_release","depth_scope","depth_previous_status"],"dg":["depth_release","depth_scope","depth_previous_status"],"centered-difference":["depth_scope","depth_additional_releases"],"godunov":["depth_scope","depth_release"],"weno-js":["depth_release","depth_scope"],"hll":["depth_scope","depth_additional_releases"],"forward-euler":["depth_release","depth_scope"],"heun":["depth_scope","depth_additional_releases"],"rk4":["depth_scope","depth_additional_releases"],"weno-z":["depth_scope","depth_release"]};
const canonicalMethodValue=value=>Array.isArray(value)?value.map(canonicalMethodValue):value&&typeof value==='object'?Object.fromEntries(Object.keys(value).sort().map(key=>[key,canonicalMethodValue(value[key])])):value;
const historicalMethod=method=>canonicalMethodValue(Object.fromEntries(Object.entries(method).filter(([key])=>!(batchBindingFields[method.id]||[]).includes(key))));
const ids=['level-set-translation','level-set-rotation'];
const inputs=json(base+'inputs.json'),result=json(base+'results/result.json');

test('the dedicated two-case release preserves all previous releases, method records, primary pictures and the shared execution registry',()=>{
 const registry=json('numerical-methods-atlas/validation/releases.json');
 assert.equal(registry.releases.length,25);assert.equal(registry.case_count,58);
 assert.equal(registry.releases.reduce((s,r)=>s+r.tests,0),760);
 assert.equal(objectHash(registry.releases.filter(r=>!['level-set','weno-critical','shallow-water','wall-flow','sem-fr'].includes(r.group))),'150a2bfb669938f7c9c67dde0f23fcc4dace9e54c3298841fed651a57bb5fd3f');
 const methods=json('catalog/atlas-methods.json').methods;
 assert.equal(methods.length,151);
 assert.equal(objectHash(methods.filter(m=>!['level-set','vof','spectral-element','flux-reconstruction'].includes(m.id)).map(historicalMethod)),'6462e0c0e177b17a95b97d953fd12bf2887933124691bb8844c5cc0eda9ee904');
 const pictures=json('numerical-methods-atlas/gallery/preview-manifest.json').items;
 assert.equal(pictures.length,92);
 assert.equal(objectHash(pictures.filter(p=>!['level-set-circle','swashes-topography','dry-bed-dam-break','lid-driven-cavity','wall-manufactured'].includes(p.id))),'ea4dfdfc33dfb4da3c54b6a6a5d8e1c02fd10b94b2281af9e21fd15f55938d9c');
 assert.equal(sha('numerical-methods-atlas/code-and-data/examples.json'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
 assert.equal(sha(base+'inputs.json'),sha(base+'inputs-initial.json'));
 const contract=json(base+'pre-run-contract.json');assert.equal(contract.planned_tests,22);
 for(const [p,h] of Object.entries(contract.files_sha256))assert.equal(sha(base+p),h,p);
 const history=json(base+'protocol-history.json');assert.equal(history.first_fixed_protocol_passed,true);assert.equal(history.acceptance_modified_after_first_execution,false);
 assert.equal(history.unit_test_revision.original_passed,21);assert.equal(history.unit_test_revision.original_failed,1);
 const receipt=json(base+'verification.json');assert.equal(receipt.tests,22);assert.equal(receipt.passed,true);assert.equal(receipt.all_cases_rerun,true);
 for(const[p,h]of Object.entries(json(base+'source-manifest.json').files))assert.equal(sha(base+p),h,p);
});

test('observed errors follow the actual intermediate interface samples, balanced refinement and explicit redistancing jumps',()=>{
 assert.equal(result.passed,true);assert.equal(result.input_sha256,sha(base+'inputs.json'));
 for(const c of result.cases){
  assert.ok(ids.includes(c.id));assert.ok(c.passed&&Object.values(c.checks).every(Boolean));
  const config=inputs.cases[c.id];assert.deepEqual(config.grids,[32,64,128]);
  for(const mode of ['advection-only','redistance']){
   const rows=c.records.filter(r=>r.mode===mode);assert.deepEqual(rows.map(r=>r.n),config.grids);
   rows.forEach((row,index)=>{
    assert.deepEqual(row.snapshots.map(s=>s.time),config.snapshots);
    assert.equal(row.maximum_interface_error,Math.max(...row.snapshots.slice(1).map(s=>s.interface_max_radial_error)));
    if(index)assert.ok(Math.abs(row.observed_order-Math.log2(rows[index-1].maximum_interface_error/row.maximum_interface_error))<1e-12);
    row.contours.forEach((points,k)=>{
     const t=config.snapshots[k],angle=config.omega*t;
     const center=c.id.endsWith('translation')?[.3+.2*t,.35+.1*t]:[.5+.18*Math.cos(angle),.5+.18*Math.sin(angle)];
     const error=Math.max(...points.map(p=>Math.abs(Math.hypot(p[0]-center[0],p[1]-center[1])-.15)));
     assert.ok(Math.abs(error-row.snapshots[k].interface_max_radial_error)<2e-15);
    });
    assert.equal(row.redistance_calls,mode==='redistance'?10:0);
    assert.equal(row.state_clip_count,row.volume_correction_count);assert.equal(row.state_clip_count,0);
    for(const log of row.redistance_log)assert.equal(log.area_change,log.area_after-log.area_before);
   });
  }
  assert.ok(c.metrics.advection_observed_order>1.5&&c.metrics.advection_observed_order<2.5);
  assert.ok(c.metrics.redistance_finest_relative_area_error>c.metrics.advection_finest_relative_area_error);
 }
});

test('the distribution retains real finite128x128 numerical fields that differ from the analytic interior',()=>{
 const program=String.raw`
import array,ast,math,pathlib,struct,zipfile
base=pathlib.Path('code/validated-examples/2026-11-23/level-set/results')
for ident in ['level-set-translation','level-set-rotation']:
 with zipfile.ZipFile(base/(ident+'.npz')) as z:
  def field(name):
   b=z.read(name+'.npy');assert b[:6]==b'\x93NUMPY' and b[6]==1
   n=struct.unpack('<H',b[8:10])[0];h=ast.literal_eval(b[10:10+n].decode())
   assert h['shape']==(128,128) and h['descr']=='<f8' and not h['fortran_order']
   a=array.array('d');a.frombytes(b[10+n:]);assert all(math.isfinite(x) for x in a);return a
  reference=field('reference_final');plain=field('phi_advection');red=field('phi_redistance')
  assert max(abs(x-y) for x,y in zip(plain,reference))>1e-5
  assert max(abs(x-y) for x,y in zip(plain,red))>1e-5
print('real2D fields retained')
`;
 assert.match(execFileSync('python3',['-B','-c',program],{cwd:fileURLToPath(root),encoding:'utf8'}),/real2D fields retained/);
});

test('level sets have dedicated educational code while VOF remains reading-only with no borrowed execution',()=>{
 const methods=json('numerical-methods-atlas/methods/index.json').methods;
 const level=methods.find(m=>m.id==='level-set'),vof=methods.find(m=>m.id==='vof');
 assert.equal(level.status,'educational-example');assert.equal(level.depth_release.group,'level-set');
 assert.deepEqual(level.execution_examples.map(e=>e.id),ids);
 assert.ok(level.code_urls.some(u=>u.endsWith('/level-set/level_set.py')));
 assert.equal(vof.status,'reading-only');assert.deepEqual(vof.code_urls,[]);assert.deepEqual(vof.test_urls,[]);assert.deepEqual(vof.execution_examples,[]);
 const problems=json('catalog/atlas-test-problems.json').problems;
 assert.deepEqual(problems.filter(p=>(p.supplemental_examples||[]).some(e=>ids.includes(e.id))).map(p=>p.id),['level-set-circle']);
 for(const ident of ids){
  const page=json(`numerical-methods-atlas/validation/${ident}/index.json`);
  assert.equal(page.problem_id,'level-set-circle');assert.deepEqual(page.method_ids,['level-set']);
  assert.deepEqual(page.execution_navigation.equations.map(e=>e.id),['level-set-advection']);
 }
});

test('both languages and searches expose the theory, VOF comparison, geometry, two executable cases and manifest links',()=>{
 for(const lang of ['ja','en']){
  const chapter=json(`numerical-methods-atlas/${lang}/read/level-set/index.json`);
  assert.ok(chapter.html.includes('id="vof-comparison"')&&chapter.html.includes('<table'));
  assert.ok(chapter.html.includes('katex-mathml')&&!chapter.html.includes('math-placeholder'));
  assert.deepEqual(chapter.scoped_supplements.map(c=>c.id),ids);
  assert.ok(chapter.html.includes('level-set-overview.png'));
  assert.equal(chapter.implementation_status.vof,'reading-only');
  assert.ok(json(`numerical-methods-atlas/${lang}/read/index.json`).groups.some(g=>g.chapters.some(c=>c.id==='level-set')));
  for(const ident of ids){
   const html=text(`numerical-methods-atlas/validation/${ident}/index.html`);
   for(const suffix of ['inputs.json','verification.json','source-manifest.json','atlas-level-set-2026-11-23.zip',`results/${ident}.png`])assert.ok(html.includes('/'+base+suffix));
  }
 }
 const global=makeSearch(json('search/index.json').documents),inline=json('numerical-methods-atlas/home-search-index.json');
 for(const [q,lang,id]of [['レベルセット 平行移動 実行','ja',ids[0]],['level set rotation run','en',ids[1]]]){
  for(const result of [global(q,lang,'atlas'),searchChapters(inline,q,lang)])assert.ok(result.some(r=>r.kind==='execution-example'&&r.url.includes('/validation/'+id+'/')),q);
 }
});
