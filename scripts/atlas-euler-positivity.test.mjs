import {methodCount,methodStatusCounts} from './fixtures/atlas-inventory.mjs';
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
const group='euler-positivity',id='euler-double-rarefaction-positivity';
const base='code/validated-examples/2026-11-23-r2/euler-positivity/';

// Remove only this batch's appended WENO evidence/entry for the historical golden.
// Preserve the three original MHD problem records while projecting only appended batch18–27 links.
const batch18OriginalProblems={"orszag-tang":{"id":"orszag-tang","group":"mhd","name":{"ja":"Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）","en":"Orszag–Tang vortex (CT/GLM/error variants merged)"},"chapter":"mhd","evidence":[{"path":"numerical-methods-atlas/assets/validation.json","json_pointer":"/metrics/orszag_tang_ct"},{"path":"numerical-methods-atlas/assets/validation.json","json_pointer":"/metrics/orszag_tang_glm"},{"path":"numerical-methods-atlas/assets/movies/catalog.json","json_pointer":"/movies","where":{"chapter":"mhd"}},{"path":"code/validated-examples/2026-11-22/mhd/results/result.json","json_pointer":"/cases","where":{"id":"ct-glm-independent"}},{"path":"code/validated-examples/2026-11-22/mhd/results/ct-glm-independent.png","artifact":"image"},{"path":"code/validated-examples/2026-11-22/mhd/verification.json","json_pointer":"/all_cases_rerun"},{"path":"code/validated-examples/2026-11-22/mhd-convergence/results/result.json","json_pointer":"/cases","where":{"id":"ct-glm-ot-convergence"}},{"path":"code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-ot-convergence.png","artifact":"image"},{"path":"code/validated-examples/2026-11-22/mhd-convergence/inputs.json","json_pointer":"/ot"},{"path":"code/validated-examples/2026-11-22/mhd-convergence/verification.json","json_pointer":"/all_cases_rerun"}],"availability":"saved-output","supplemental_examples":[{"id":"ct-glm-independent","url":"/numerical-methods-atlas/validation/ct-glm-independent/","name":{"ja":"Orszag–Tang：CT・GLMと独立Athena++比較","en":"Orszag–Tang: CT, GLM and independent Athena++"}},{"id":"ct-glm-ot-convergence","url":"/numerical-methods-atlas/validation/ct-glm-ot-convergence/","name":{"ja":"Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束","en":"Orszag–Tang: matched CT/GLM and converged independent references"}}]},"circular-alfven":{"id":"circular-alfven","group":"mhd","name":{"ja":"円偏波Alfvén波","en":"Circularly polarized Alfvén wave"},"chapter":"mhd","evidence":[{"path":"numerical-methods-atlas/assets/mhd-tests/mhd-tests.json","json_pointer":"/alfven"}],"availability":"saved-output"},"magnetic-loop":{"id":"magnetic-loop","group":"mhd","name":{"ja":"磁場ループの移流","en":"Magnetic field-loop advection"},"chapter":"mhd","evidence":[{"path":"numerical-methods-atlas/assets/mhd-tests/mhd-tests.json","json_pointer":"/field_loop"}],"availability":"saved-output"}};
const historicalProblem = row => {
 const extras=(row.supplemental_examples||[]).filter(e=>!['sem-poisson-2d','fr-periodic-advection','checkerboard-diffusion','rotated-anisotropic-diffusion','neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short','thermal-landau-damping','thermal-two-stream','pic-independent-spatial','dsmc-couette','dsmc-fourier','dsmc-planar-shock'].includes(e.id));
 row={...row,evidence:row.evidence.filter(e=>!e.path.includes('/sem-fr/'))};
 if(extras.length)row.supplemental_examples=extras;else delete row.supplemental_examples;
 row=batch18OriginalProblems[row.id]||row;
 if(row.id!=='advection-sine')return row;
 const copy={...row,evidence:row.evidence.filter(e=>!e.path.includes('/weno-critical/'))};
 const remaining=(row.supplemental_examples||[]).filter(e=>e.id!=='weno-critical-epsilon');
 if(remaining.length)copy.supplemental_examples=remaining;else delete copy.supplemental_examples;
 return copy;
};

test('a supplemental gallery picture must opt in to a verified additional PNG with bilingual captions',()=>{
 const program=String.raw`import base64,copy,hashlib,tempfile,sys
from pathlib import Path
sys.path.insert(0,str(Path.cwd()/'scripts'))
from atlas_depth_release import depth_gallery_figure
with tempfile.TemporaryDirectory(prefix='atlas-gallery-opt-in-') as temporary:
 d=Path(temporary);(d/'results').mkdir()
 png=base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+ip1sAAAAASUVORK5CYII=')
 (d/'results/preview.png').write_bytes(png)
 h=hashlib.sha256(png).hexdigest();m={'files':{'results/preview.png':h}}
 c={'id':'fixture','additional_figures':[{'file':'preview.png','caption':{'ja':'保存した時空間の場','en':'Saved space-time field'}}]}
 assert depth_gallery_figure(d,m,c) is None
 c['gallery_figure']='preview.png';f=depth_gallery_figure(d,m,c)
 assert f['sha256']==h and f['width']==f['height']==1
 for value in ['missing.png','../preview.png','https://example.test/p.png','fixture.png',None,{},['preview.png']]:
  bad=copy.deepcopy(c);bad['gallery_figure']=value
  try:depth_gallery_figure(d,m,bad)
  except (AssertionError,TypeError):pass
  else:raise AssertionError('unbound gallery preview accepted')
 bad=copy.deepcopy(c);bad['additional_figures'][0]['caption']={'ja':'片言語'}
 try:depth_gallery_figure(d,m,bad)
 except AssertionError:pass
 else:raise AssertionError('untranslated preview accepted')
 (d/'results/preview.png').write_bytes(png+b'changed')
 try:depth_gallery_figure(d,m,c)
 except AssertionError:pass
 else:raise AssertionError('changed PNG accepted')
print('manifest-bound supplemental gallery opt-in checked')`;
 assert.match(execFileSync('python3',['-B','-c',program],{cwd:root,encoding:'utf8'}),/gallery opt-in checked/);
});

test('Euler stage positivity reuses one problem and preserves eighteen older releases and all eighty-six primary pictures',()=>{
 const registry=json('numerical-methods-atlas/validation/releases.json');
 assert.equal(objectHash(registry.releases.filter(r=>r.group!==group&&!['zalesak','weno-critical','shallow-water','wall-flow','level-set', 'instability-growth', 'mhd-transport', 'mesh-boundary', 'moving-waves', 'relativistic', 'sem-fr','coefficient-diffusion','slab-ewald','fmm3d','gravity-dynamics','warm-pic','pic-spatial','dsmc-wall','dsmc-shock'].includes(r.group))),'897f2f731b5911739be0230dfb5ae0ab174ebeb08b954bcca028f02d59dba1ee');
 assert.equal(registry.case_count,83);assert.equal(registry.releases.length,38);
 const release=registry.releases.find(r=>r.group===group);assert.deepEqual(release.case_ids,[id]);
 assert.equal(registry.releases.filter(r=>!['zalesak','weno-critical','shallow-water','wall-flow','level-set', 'instability-growth', 'mhd-transport', 'mesh-boundary', 'moving-waves', 'relativistic', 'sem-fr','coefficient-diffusion','slab-ewald','fmm3d','gravity-dynamics','warm-pic','pic-spatial','dsmc-wall','dsmc-shock'].includes(r.group)).reduce((s,r)=>s+r.tests,0),571+release.tests);
 const pictures=json('numerical-methods-atlas/gallery/preview-manifest.json').items.filter(r=>!['zalesak','swashes-topography','dry-bed-dam-break','lid-driven-cavity','wall-manufactured','level-set-circle', 'kh-initial-growth', 'rt-initial-growth', 'lshape-fem', 'annular-viscous-mms', 'poisson-neumann', 'poisson-robin', 'ale-nonuniform-transport', 'cgrid-rotating-wave', 'srhd-collision', 'srmhd-alfven','checkerboard-diffusion','rotated-anisotropic-diffusion','neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short','thermal-landau-damping','thermal-two-stream','dsmc-couette','dsmc-fourier','dsmc-planar-shock'].includes(r.id)).map(({id,image,image_sha256,caption})=>({id,image,image_sha256,caption}));
 assert.equal(pictures.length,86);assert.equal(objectHash(pictures),'c64fafd78d6ae0a39941161c2932799ffca4f8eb0e3885ce2998de58f4a1f429');
 const problems=json('catalog/atlas-test-problems.json').problems;
 assert.equal(problems.length,113);
 const before=problems.filter(p=>!['zalesak','swashes-topography','dry-bed-dam-break','lid-driven-cavity','wall-manufactured','level-set-circle', 'kh-initial-growth', 'rt-initial-growth', 'lshape-fem', 'annular-viscous-mms', 'poisson-neumann', 'poisson-robin', 'ale-nonuniform-transport', 'cgrid-rotating-wave', 'srhd-collision', 'srmhd-alfven','checkerboard-diffusion','rotated-anisotropic-diffusion','neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short','thermal-landau-damping','thermal-two-stream','dsmc-couette','dsmc-fourier','dsmc-planar-shock'].includes(p.id)).map(historicalProblem).map(p=>{if(p.id!=='double-rarefaction')return p;const copy={...p};delete copy.supplemental_examples;return copy;});
 assert.equal(objectHash(before),'cb3e36911d193201104862c1d0038e1b1b08c551946f7508a0ce7f4eb1fafd67');
 assert.equal(json('catalog/atlas-methods.json').methods.length,methodCount);
 assert.equal(hash('numerical-methods-atlas/code-and-data/examples.json'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
 const receipt=json(base+'verification.json');assert.equal(receipt.tests,release.tests);assert.equal(receipt.passed,true);assert.equal(receipt.all_cases_rerun,true);assert.equal(hash(base+receipt.archive.file),receipt.archive.sha256);
 for(const[p,h]of Object.entries(json(base+'source-manifest.json').files))assert.equal(hash(base+p),h,p);
});

test('the new double-rarefaction figure is visible and linked to actual methods, Euler and the existing reference',()=>{
 const page=json(`numerical-methods-atlas/validation/${id}/index.json`);
 assert.equal(page.problem_id,'double-rarefaction');assert.deepEqual([...page.method_ids].sort(),['lax-friedrichs','muscl','positive-scaling','ssprk33']);
 assert.deepEqual(page.execution_navigation.equations.map(x=>x.id),['euler']);
 const problem=json('numerical-methods-atlas/problems/double-rarefaction/index.json');assert.ok(problem.executions.some(x=>x.id===id));assert.ok(problem.references.some(x=>x.id==='euler-double-rarefaction'));
 const item=json('numerical-methods-atlas/gallery/index.json').items.find(x=>x.id==='double-rarefaction');
 assert.equal(item.image,'/numerical-methods-atlas/gallery/previews/double-rarefaction.png');assert.equal(item.runnable,true);
 const extra=item.supplemental_execution_entries.find(x=>x.id===id);assert.ok(extra.preview);assert.equal(hash(extra.preview.url.slice(1)),extra.preview.sha256);
 const html=bytes('numerical-methods-atlas/gallery/index.html').toString();
 for(const lang of ['ja','en']){
  assert.ok(html.includes(extra.preview.caption[lang]));assert.ok(html.includes(extra.url[lang]));
  const chapter=bytes(`numerical-methods-atlas/${lang}/read/validation-${group}/index.html`).toString();assert.ok(chapter.includes(id));assert.ok(chapter.includes('10.1016/j.jcp.2010.08.016'));
  assert.ok(bytes(`numerical-methods-atlas/${lang}/read/advanced-limiters/index.html`).toString().includes('euler-stage-positivity-followup'));
 }
 assert.equal((html.match(new RegExp('data-supplemental-preview="'+id+'"','g'))||[]).length,2);
 const methods=json('numerical-methods-atlas/methods/index.json').methods;
 for(const mid of page.method_ids){const method=methods.find(x=>x.id===mid);assert.equal(method.status,'educational-example');assert.ok([method.depth_release,...(method.depth_additional_releases||[])].some(x=>x.group===group));}
 assert.deepEqual(Object.fromEntries(['educational-example','reading-only','planned'].map(s=>[s,methods.filter(m=>m.status===s).length])),methodStatusCounts);
});

test('the frozen three-grid Euler update retains every positive stage, actual scaling, shared-flux budgets and full x-t data',()=>{
 const contract=json(base+'pre-run-contract.json');assert.equal(contract.planned_tests,27);assert.equal(contract.planned_numerical_gates,73);
 for(const[p,h]of Object.entries(contract.files_sha256))assert.equal(hash(base+p),h,p);
 const cfg=json(base+'inputs.json').cases[id];assert.deepEqual(cfg.grids,[128,256,512]);assert.equal(cfg.gamma,1.4);assert.deepEqual(cfg.domain,[0,1]);assert.deepEqual(cfg.left,[1,-2,.4]);assert.deepEqual(cfg.right,[1,2,.4]);assert.equal(cfg.final_time,.15);assert.equal(cfg.fixed_lf_alpha,4);assert.equal(cfg.cfl,.4);assert.equal(cfg.positivity_cfl_bound,.5);assert.equal(cfg.reconstruction_epsilon,1e-13);
 const result=json(base+'results/result.json'),c=result.cases.find(x=>x.id===id);assert.equal(result.passed,true);assert.equal(result.termination,'fixed_budget_completed');assert.equal(result.failure,null);
 assert.deepEqual(c.records.map(r=>r.n),[128,256,512]);assert.equal(Object.keys(c.checks).length,73);assert.ok(Object.values(c.checks).every(v=>v===true));
 for(const row of c.records){
  assert.equal(row.time,.15);assert.equal(row.state_floor_count,0);assert.equal(row.rejected_steps,0);assert.equal(row.retries,0);assert.ok(row.scaled_cells>0);assert.ok(row.raw_endpoint_min_pressure<0);assert.ok(row.minimum_theta>=0&&row.minimum_theta<1);assert.ok(row.maximum_face_spectral_radius<=4);assert.ok(row.maximum_courant<=.5);assert.ok(row.conservation_relative.every(x=>x<=3e-12));
  const history=json(base+'results/'+row.history);assert.equal(history.length,3*row.steps);assert.equal(row.stages,history.length);
  for(const s of history){for(const name of ['endpoint_min_density','endpoint_min_pressure','fe_mean_min_density','fe_mean_min_pressure','rk_mean_min_density','rk_mean_min_pressure'])assert.ok(s[name]>0,`${row.n}/${s.step}/${s.stage}/${name}`);assert.ok(s.maximum_mean_preservation_defect<=3e-14);assert.ok(s.maximum_fe_boundary_balance_defect<=3e-12);assert.ok(s.maximum_rk_boundary_balance_defect<=3e-12);}
 }
 assert.ok(c.reference_qualification.independent_root_point_maximum_difference<=2e-12);assert.ok(c.reference_qualification.maximum_scaled_euler_residual<=2e-6);assert.ok(c.reference_qualification.star_density>0);assert.ok(c.reference_qualification.star_pressure>0);
 const program=String.raw`import ast,struct,zipfile
from pathlib import Path
p=Path('code/validated-examples/2026-11-23-r2/euler-positivity/results/field-n512.npz')
with zipfile.ZipFile(p) as z:
 def shape(name):
  b=z.read(name+'.npy');assert b[:6]==b'\x93NUMPY';n=struct.unpack('<H',b[8:10])[0];return ast.literal_eval(b[10:10+n].decode())['shape']
 assert shape('q')==shape('q_initial')==shape('q_reference')==(512,3)
 assert shape('edges')==(513,)
 h=shape('q_history');assert len(h)==3 and h[0]>2 and h[1:]==(512,3)
 assert shape('history_times')==(h[0],)
print('full conservative x-t arrays retained')`;
 assert.match(execFileSync('python3',['-B','-c',program],{cwd:root,encoding:'utf8'}),/x-t arrays retained/);
});

test('packaging rejects a missing reviewed scientific pin before a staging directory or subprocess is created',()=>{
 const program=String.raw`import importlib.util,json,tempfile
from pathlib import Path
from unittest.mock import patch
spec=importlib.util.spec_from_file_location('package_depth',Path('scripts/package-depth-examples.py'))
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
v_spec=importlib.util.spec_from_file_location('public_depth',Path('scripts/verify-depth-public.py'))
v=importlib.util.module_from_spec(v_spec);v_spec.loader.exec_module(v)
assert p.REVIEWED_REQUIREMENTS=={name+'=='+version for name,version in v.DIRECT_PINS.items()}
with tempfile.TemporaryDirectory(prefix='atlas-incomplete-pins-') as directory:
 p.ROOT=Path(directory);source=p.ROOT/'scripts/depth-euler-positivity';source.mkdir(parents=True)
 case={'id':'fixture','method_ids':['lax-friedrichs'],'references':[{'id':'fixture-reference','title':'Fixture formulation','url':'https://example.org/formulation','review_level':'source inspected'}]}
 case.update({key:{'ja':'固定入力の条件','en':'Fixed-input conditions'} for key in ['title','summary','assumptions','algorithm','validation','limits']})
 for name in ['run.py','inputs.json','README.md','LICENSE']:(source/name).write_text('fixture')
 (source/'cases.json').write_text(json.dumps([case]))
 (source/'requirements.txt').write_text('numpy==2.0.2\npytest==8.3.5\n')
 with patch.object(p.subprocess,'run',side_effect=AssertionError('scientific subprocess launched')) as child,patch.object(p.tempfile,'TemporaryDirectory',side_effect=AssertionError('staging directory created')) as staging:
  try:p.package('euler-positivity','2026-11-23-r2')
  except ValueError as error:assert 'three reviewed direct pins' in str(error)
  else:raise AssertionError('incomplete reviewed requirements accepted')
  assert child.call_count==staging.call_count==0
 assert not (p.ROOT/'code').exists()
print('missing reviewed pin rejected before science or staging')`;
 assert.match(execFileSync('python3',['-B','-c',program],{cwd:root,encoding:'utf8'}),/before science or staging/);
});
