import {projectCatalogBeforeFinal23} from './fixtures/atlas-final23-projection.mjs';
import {projectEquationBeforeBatch78} from './fixtures/atlas-batch78-projection.mjs';
import {equationCount,equationsAddedAfterBatch37,examplesAddedAfterBatch37,groupsAddedAfterBatch37,problemCount,runnableProblemCount,supplementCaseCount,supplementGroupCount} from './fixtures/atlas-inventory.mjs';
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
const group='zalesak',id='zalesak-rotation';
const base='code/validated-examples/2026-11-23/zalesak/';
// The new batch changes execution scope only; retain every earlier formula/ID/status.
const oldEquationMetadata={"linear-advection":{"coverage_scope":"","note":{"ja":"一定速度aによる輸送。波形の移動、数値拡散、安定性へ。","en":"Transport at constant speed a: translation, numerical diffusion and stability."}},"shallow-water":{"coverage_scope":"Wet 1D flow and linear rotating Fourier symbols; no full geophysical dynamical core.","note":{"ja":"前2式は平坦床・摩擦なしの1次元系。後2行は水深Hまわりの線形回転系。非線形流れのテストと、回転系のFourier記号の検証を区別します。","en":"The first two equations are 1D flat-bed, frictionless flow; the remaining lines are the linear rotating system about depth H. Distinguish nonlinear flow tests from rotating-system Fourier-symbol checks."}},"navier-stokes":{"coverage_scope":"","note":{"ja":"一定密度・粘性の代表形。公開例は周期2次元MAC格子の射影法とTaylor–Green渦です。","en":"A representative constant-density, constant-viscosity form. Public examples use periodic 2D MAC projection and a Taylor–Green vortex."}}};
const batch18OriginalEquations={"poisson-laplace":{"id":"poisson-laplace","name":{"ja":"Poisson・Laplace方程式","en":"Poisson / Laplace equations"},"formula":["-\\nabla^2u=f","f=0\\quad\\Longrightarrow\\quad\\nabla^2u=0"],"chapter":"elliptic","note":{"ja":"楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。","en":"Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries."},"anchor_aliases":["poisson"],"status":"local-example","group":"physical","coverage_scope":""},"mhd":{"id":"mhd","name":{"ja":"理想MHD","en":"Ideal magnetohydrodynamics"},"formula":["\\rho_t+\\nabla\\cdot(\\rho\\boldsymbol v)=0","(\\rho\\boldsymbol v)_t+\\nabla\\cdot[\\rho\\boldsymbol v\\otimes\\boldsymbol v+(p+B^2/2)I-\\boldsymbol B\\otimes\\boldsymbol B]=0","E_t+\\nabla\\cdot[(E+p+B^2/2)\\boldsymbol v-(\\boldsymbol v\\cdot\\boldsymbol B)\\boldsymbol B]=0","\\boldsymbol B_t=\\nabla\\times(\\boldsymbol v\\times\\boldsymbol B),\\quad\\nabla\\cdot\\boldsymbol B=0"],"chapter":"mhd","note":{"ja":"透磁率を1とする理想MHDの代表形。Eは熱・運動・磁場を含む全エネルギー密度。解説でCT・GLMと発散の測り方、HLLDテストへ進めます。","en":"Representative ideal MHD with magnetic permeability set to one. E is total thermal, kinetic and magnetic energy density. Follow CT/GLM, divergence conventions and HLLD tests."},"status":"local-example","group":"physical","coverage_scope":""},"srhd":{"id":"srhd","name":{"ja":"特殊相対論的流体（SRHD）","en":"Special-relativistic hydrodynamics (SRHD)"},"formula":["\\partial_\\mu(\\rho_0u^\\mu)=0,\\qquad\\partial_\\mu T^{\\mu\\nu}=0","T^{\\mu\\nu}=\\rho_0h u^\\mu u^\\nu+p\\eta^{\\mu\\nu}"],"chapter":"relativistic-hydrodynamics","note":{"ja":"c=1、平坦なCartesian時空での理想流体の代表形。状態方程式と原始変数の回復が必要です。アトラスでは文献解説のみ。","en":"Representative ideal fluid in flat Cartesian spacetime, c=1. An equation of state and primitive recovery are required. Atlas coverage is literature-only."},"section":"what-changes-from-the-existing-euler-examples","status":"reading","group":"relativistic","coverage_scope":"Literature review; no local relativistic solver."}};
// Only the two corrected scope notes are projected back for this historical golden; formulas and evidence remain checked.
const priority1OriginalScopeNotes={"hartree-fock-model":{"ja":"閉殻RHFの占有空間軌道の式。一般に非局所な交換を含む。実行例は球対称1s² Heの局所還元に限定し、一般の分子・多電子のFock行列構築は未実装。","en":"Closed-shell RHF spatial-orbital equations, generally with nonlocal exchange. Runnable code is restricted to the spherical 1s² helium local reduction; general molecular/many-electron Fock-matrix construction is not implemented."},"kohn-sham-model":{"ja":"密度汎関数の局所KS代表形。実行例は球対称He・スピン非偏極Dirac交換のみLDA。相関・GGA・hybrid・一般化KS・周期系は未実装。","en":"Representative local KS equations. Runnable code covers spherical-helium spin-unpolarized Dirac exchange-only LDA. Correlation, GGA, hybrids, generalized KS and periodic systems are not implemented."}};
const batch28CaseIds=new Set(['checkerboard-diffusion', 'rotated-anisotropic-diffusion', 'neutral-slab-yb', 'fmm3d-inverse-r', 'gravity-kepler', 'gravity-plummer-short', 'thermal-landau-damping', 'thermal-two-stream', 'pic-independent-spatial', 'dsmc-couette', 'dsmc-fourier', 'dsmc-planar-shock',...examplesAddedAfterBatch37]);
const batch28HistoricalEquation=row=>{if(!Object.hasOwn(row,'supplemental_examples'))return row;const copy={...row},remaining=row.supplemental_examples.filter(id=>!batch28CaseIds.has(id));if(remaining.length)copy.supplemental_examples=remaining;else delete copy.supplemental_examples;return copy;};
const historicalEquation=row=>{row=projectEquationBeforeBatch78(row);row=batch28HistoricalEquation(row);if(priority1OriginalScopeNotes[row.id])row={...row,note:priority1OriginalScopeNotes[row.id]};row=batch18OriginalEquations[row.id]||row;if(!oldEquationMetadata[row.id])return row;const copy={...row,...oldEquationMetadata[row.id]};delete copy.execution_scope;delete copy.supplemental_examples;return copy;};


// Remove only this batch's appended WENO evidence/entry for the historical golden.
// Preserve the three original MHD problem records while projecting only appended batch18–27 links.
const batch18OriginalProblems={"orszag-tang":{"id":"orszag-tang","group":"mhd","name":{"ja":"Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）","en":"Orszag–Tang vortex (CT/GLM/error variants merged)"},"chapter":"mhd","evidence":[{"path":"numerical-methods-atlas/assets/validation.json","json_pointer":"/metrics/orszag_tang_ct"},{"path":"numerical-methods-atlas/assets/validation.json","json_pointer":"/metrics/orszag_tang_glm"},{"path":"numerical-methods-atlas/assets/movies/catalog.json","json_pointer":"/movies","where":{"chapter":"mhd"}},{"path":"code/validated-examples/2026-11-22/mhd/results/result.json","json_pointer":"/cases","where":{"id":"ct-glm-independent"}},{"path":"code/validated-examples/2026-11-22/mhd/results/ct-glm-independent.png","artifact":"image"},{"path":"code/validated-examples/2026-11-22/mhd/verification.json","json_pointer":"/all_cases_rerun"},{"path":"code/validated-examples/2026-11-22/mhd-convergence/results/result.json","json_pointer":"/cases","where":{"id":"ct-glm-ot-convergence"}},{"path":"code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-ot-convergence.png","artifact":"image"},{"path":"code/validated-examples/2026-11-22/mhd-convergence/inputs.json","json_pointer":"/ot"},{"path":"code/validated-examples/2026-11-22/mhd-convergence/verification.json","json_pointer":"/all_cases_rerun"}],"availability":"saved-output","supplemental_examples":[{"id":"ct-glm-independent","url":"/numerical-methods-atlas/validation/ct-glm-independent/","name":{"ja":"Orszag–Tang：CT・GLMと独立Athena++比較","en":"Orszag–Tang: CT, GLM and independent Athena++"}},{"id":"ct-glm-ot-convergence","url":"/numerical-methods-atlas/validation/ct-glm-ot-convergence/","name":{"ja":"Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束","en":"Orszag–Tang: matched CT/GLM and converged independent references"}}]},"circular-alfven":{"id":"circular-alfven","group":"mhd","name":{"ja":"円偏波Alfvén波","en":"Circularly polarized Alfvén wave"},"chapter":"mhd","evidence":[{"path":"numerical-methods-atlas/assets/mhd-tests/mhd-tests.json","json_pointer":"/alfven"}],"availability":"saved-output"},"magnetic-loop":{"id":"magnetic-loop","group":"mhd","name":{"ja":"磁場ループの移流","en":"Magnetic field-loop advection"},"chapter":"mhd","evidence":[{"path":"numerical-methods-atlas/assets/mhd-tests/mhd-tests.json","json_pointer":"/field_loop"}],"availability":"saved-output"}};
const historicalProblem = row => {
 const extras=(row.supplemental_examples||[]).filter(e=>!['sem-poisson-2d','fr-periodic-advection','checkerboard-diffusion','rotated-anisotropic-diffusion','neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short','thermal-landau-damping','thermal-two-stream','pic-independent-spatial','dsmc-couette','dsmc-fourier','dsmc-planar-shock',...examplesAddedAfterBatch37].includes(e.id));
 row={...row,evidence:row.evidence.filter(e=>!e.path.includes('/sem-fr/'))};
 if(extras.length)row.supplemental_examples=extras;else delete row.supplemental_examples;
 row=batch18OriginalProblems[row.id]||row;
 if(row.id!=='advection-sine')return row;
 const copy={...row,evidence:row.evidence.filter(e=>!e.path.includes('/weno-critical/'))};
 const remaining=(row.supplemental_examples||[]).filter(e=>e.id!=='weno-critical-epsilon');
 if(remaining.length)copy.supplemental_examples=remaining;else delete copy.supplemental_examples;
 return copy;
};

test('canonical equation additions enter both shared inventories without changing imported equation or method records',()=>{
 const program=String.raw`import copy,json,sys
from pathlib import Path
sys.path.insert(0,str(Path.cwd()/'scripts'))
from atlas_equation_inventory import merge_catalog_equations,ORIGIN
canonical=json.loads(Path('catalog/atlas-equations.json').read_text())['equations']
assert len(canonical)==${equationCount}
for name in ['numerical-methods-atlas/coverage.json','numerical-methods-atlas/assets/site-coverage.json']:
 original=json.loads(Path(name).read_text())['items'];before=copy.deepcopy(original)
 result=merge_catalog_equations(original,canonical)
 assert original==before
 assert {x['id'] for x in result if x['kind']=='equation'}=={x['id'] for x in canonical}
 assert len([x for x in result if x['kind']=='equation'])==${equationCount}
 for old in original:
  if old.get('origin')!=ORIGIN:
   assert next(x for x in result if x['kind']==old['kind'] and x['id']==old['id'])==old
 added=next(x for x in result if x['kind']=='equation' and x['id']=='rotational-advection')
 assert added['origin']==ORIGIN and added['chapter']=='validation-zalesak' and added['status']=='local-example'
 assert 'not Euler' in added['scope']
 assert merge_catalog_equations(result,canonical)==result
 stale=copy.deepcopy(result);next(x for x in stale if x['kind']=='equation' and x['id']=='rotational-advection')['chapter']='stale'
 assert merge_catalog_equations(stale,canonical)==result
 removed=merge_catalog_equations(result,[x for x in canonical if x['id']!='rotational-advection'])
 assert not any(x['kind']=='equation' and x['id']=='rotational-advection' for x in removed)
 for bad in [canonical+[canonical[0]]]:
  try:merge_catalog_equations(original,bad)
  except ValueError:pass
  else:raise AssertionError('duplicate canonical model accepted')
print('canonical model additions synchronize without replacing historical inventory records')`;
 assert.match(execFileSync('python3',['-B','-c',program],{cwd:root,encoding:'utf8'}),/synchronize without replacing historical inventory/);
});

test('Zalesak adds one scalar problem while preserving nineteen releases, eighty-six primary figures and all previous equations/references',()=>{
 const registry=json('numerical-methods-atlas/validation/releases.json');
 assert.equal(registry.case_count,supplementCaseCount);assert.equal(registry.releases.length,supplementGroupCount);
 assert.equal(objectHash(registry.releases.filter(r=>r.group!==group&&!['weno-critical','shallow-water','wall-flow','level-set', 'instability-growth', 'mhd-transport', 'mesh-boundary', 'moving-waves', 'relativistic', 'sem-fr','coefficient-diffusion','slab-ewald','fmm3d','gravity-dynamics','warm-pic','pic-spatial','dsmc-wall','dsmc-shock',...groupsAddedAfterBatch37].includes(r.group))),'0b22556a067a3320bc7984fd2eedcbf97fe4b935ac6db98ca449933553a1c745');
 const release=registry.releases.find(r=>r.group===group);assert.deepEqual(release.case_ids,[id]);assert.equal(release.tests,26);
 assert.equal(registry.releases.filter(r=>!['weno-critical','shallow-water','wall-flow','level-set', 'instability-growth', 'mhd-transport', 'mesh-boundary', 'moving-waves', 'relativistic', 'sem-fr','coefficient-diffusion','slab-ewald','fmm3d','gravity-dynamics','warm-pic','pic-spatial','dsmc-wall','dsmc-shock',...groupsAddedAfterBatch37].includes(r.group)).reduce((s,r)=>s+r.tests,0),598+26);
 const previews=json('numerical-methods-atlas/gallery/preview-manifest.json').items;
 assert.equal(previews.length,problemCount);assert.equal(objectHash(previews.filter(p=>p.id!==group&&!['swashes-topography','dry-bed-dam-break','lid-driven-cavity','wall-manufactured','level-set-circle', 'kh-initial-growth', 'rt-initial-growth', 'lshape-fem', 'annular-viscous-mms', 'poisson-neumann', 'poisson-robin', 'ale-nonuniform-transport', 'cgrid-rotating-wave', 'srhd-collision', 'srmhd-alfven','checkerboard-diffusion','rotated-anisotropic-diffusion','neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short','thermal-landau-damping','thermal-two-stream','dsmc-couette','dsmc-fourier','dsmc-planar-shock',...examplesAddedAfterBatch37].includes(p.id))),'3d6a5bd72993ebb9110689f25d2cd9560b11a8188806e97db4c1e7b37af5d3ef');
 const problems=json('catalog/atlas-test-problems.json').problems;assert.equal(problems.length,problemCount);
 assert.equal(objectHash(problems.filter(p=>p.id!==group&&!['swashes-topography','dry-bed-dam-break','lid-driven-cavity','wall-manufactured','level-set-circle', 'kh-initial-growth', 'rt-initial-growth', 'lshape-fem', 'annular-viscous-mms', 'poisson-neumann', 'poisson-robin', 'ale-nonuniform-transport', 'cgrid-rotating-wave', 'srhd-collision', 'srmhd-alfven','checkerboard-diffusion','rotated-anisotropic-diffusion','neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short','thermal-landau-damping','thermal-two-stream','dsmc-couette','dsmc-fourier','dsmc-planar-shock',...examplesAddedAfterBatch37].includes(p.id)).map(historicalProblem)),'8b131bb281c278a7d556d31d8e6ed9539c44a2abb8e57e5b3e333044161b6247');
 const equations=json('catalog/atlas-equations.json').equations;assert.equal(equations.length,equationCount);
 assert.equal(objectHash(projectCatalogBeforeFinal23('catalog/atlas-equations.json',json('catalog/atlas-equations.json')).equations.filter(p=>!['rotational-advection','shallow-water-bed','forced-incompressible','level-set-advection', 'forced-vorticity', 'boussinesq-buoyancy', 'ale-scalar-transport', 'linear-rotating-shallow-water', 'variable-viscosity-vector', 'srmhd','tensor-diffusion','coulomb-electrostatics','vlasov-poisson','hard-sphere-boltzmann',...equationsAddedAfterBatch37].includes(p.id)).map(historicalEquation)),'e408172f62ae24312952989490300562a76bd7f2d9164b69f97e715eb27fc9b9');
 assert.equal(objectHash(projectCatalogBeforeFinal23('catalog/atlas-reference-supplements.json',json('catalog/atlas-reference-supplements.json')).cases.filter(p=>p.id!==id&&!['weno-critical-profile','lake-at-rest-bed','swashes-bernoulli','ritter-dry-bed','ghia-re100','wall-mms','level-set-translation','level-set-rotation', 'kh-initial-growth', 'rt-initial-growth', 'circular-alfven-refinement', 'magnetic-loop-independent', 'postshock-orszag-tang', 'lshape-fem', 'annular-viscous-mms', 'poisson-neumann', 'poisson-robin', 'ale-nonuniform-transport', 'cgrid-rotating-wave', 'srhd-collision', 'srmhd-alfven', 'sem-poisson-2d', 'fr-periodic-advection','checkerboard-diffusion','rotated-anisotropic-diffusion','neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short','thermal-landau-damping','thermal-two-stream','pic-independent-spatial','dsmc-couette','dsmc-fourier','dsmc-planar-shock',...examplesAddedAfterBatch37].includes(p.id))),'b1cbe79c82644c6c2d19d3a27944e996a0c6ae7707a899068445e693e6a5dbe3');
 assert.equal(hash('numerical-methods-atlas/assets/reference-solutions.json'),'c33118198faa7b35b4f66d7aad6353206f6d90c848f12e0a059874b91f897edc');
 assert.equal(hash('numerical-methods-atlas/code-and-data/examples.json'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
 const methods=json('catalog/atlas-methods.json').methods;assert.equal(methods.length,methodCount);
 assert.deepEqual(Object.fromEntries(['educational-example','reading-only','planned'].map(s=>[s,methods.filter(m=>m.status===s).length])),methodStatusCounts);
 const receipt=json(base+'verification.json');assert.equal(receipt.passed,true);assert.equal(receipt.all_cases_rerun,true);assert.equal(receipt.tests,26);assert.equal(hash(base+receipt.archive.file),receipt.archive.sha256);
 for(const[p,h]of Object.entries(json(base+'source-manifest.json').files))assert.equal(hash(base+p),h,p);
});

test('the actual two-dimensional saved figure connects to scalar rotation, its analytic reference, four implemented methods and the runnable ZIP',()=>{
 const page=json(`numerical-methods-atlas/validation/${id}/index.json`);
 assert.equal(page.problem_id,'zalesak');assert.deepEqual([...page.method_ids].sort(),['minmod','muscl','ssprk33','upwind']);
 assert.deepEqual(page.execution_navigation.equations.map(x=>x.id),['rotational-advection']);
 const problem=json('numerical-methods-atlas/problems/zalesak/index.json');assert.ok(problem.executions.some(x=>x.id===id));assert.ok(problem.references.some(x=>x.id===id));
 const gallery=json('numerical-methods-atlas/gallery/index.json');assert.equal(gallery.items.length,problemCount);assert.equal(gallery.counts.runnable_problems,runnableProblemCount);
 const item=gallery.items.find(x=>x.id==='zalesak');assert.equal(item.image,'/'+base+'results/'+id+'-preview.png');assert.equal(item.image_sha256,hash(base+'results/'+id+'-preview.png'));assert.equal(item.runnable,true);
 const execution=item.supplemental_execution_entries.find(x=>x.id===id);assert.ok(execution);assert.ok(execution.download.endsWith('atlas-zalesak-2026-11-23.zip'));
 const reference=json('numerical-methods-atlas/solutions/index.json').cases.find(x=>x.id===id);
 assert.equal(reference.kind,'analytic');assert.equal(reference.dimension,2);assert.equal(reference.model,'rotational-advection');assert.ok(reference.related_problems.some(x=>x.id==='zalesak'));
 const equation=json('numerical-methods-atlas/equations/index.json').equations.find(x=>x.id==='rotational-advection');assert.ok(equation.related_problems.some(x=>x.id==='zalesak'));assert.deepEqual(equation.supplemental_execution_examples.map(x=>x.id),[id]);assert.deepEqual(equation.supplemental_examples,[id]);
 const methods=json('numerical-methods-atlas/methods/index.json').methods;
 for(const mid of page.method_ids){const m=methods.find(x=>x.id===mid);assert.equal(m.status,'educational-example');assert.ok([m.depth_release,...(m.depth_additional_releases||[])].some(r=>r?.group===group));}
 for(const lang of ['ja','en']){
  const chapter=bytes(`numerical-methods-atlas/${lang}/read/validation-zalesak/index.html`).toString();assert.ok(chapter.includes(id));assert.ok(chapter.includes('katex-mathml'));assert.ok(!chapter.includes('katex-error'));
  const html=bytes('numerical-methods-atlas/gallery/index.html').toString();assert.ok(html.includes(item.caption[lang]));assert.ok(html.includes(execution.url[lang]));
 }
});

test('the rotating-disk reference keeps the documented normalized geometry and separates the benchmark from FCT and Firedrake execution',()=>{
 const reference=json('catalog/atlas-reference-supplements.json').cases.find(x=>x.id===id),cfg=json(base+'inputs.json').cases[id];
 assert.deepEqual(reference.bounds,[[0,1],[0,1]]);assert.deepEqual(reference.parameters.rotation_center,[.5,.5]);assert.deepEqual(reference.parameters.disk_center,[.5,.75]);assert.equal(reference.parameters.disk_radius,.15);assert.deepEqual(reference.parameters.slot_x,[.475,.525]);assert.equal(reference.parameters.slot_y_upper,.85);assert.equal(reference.parameters.inside_value,1);assert.equal(reference.parameters.outside_value,0);
 assert.deepEqual(cfg.domain,[0,1,0,1]);assert.deepEqual(cfg.rotation_center,[.5,.5]);assert.deepEqual(cfg.shape_center,[.5,.75]);assert.equal(cfg.radius,.15);assert.equal(cfg.slot_width,.05);assert.equal(cfg.slot_top,.85);assert.equal(cfg.omega,1);assert.equal(cfg.final_time,2*Math.PI);assert.deepEqual(cfg.grids,[64,128,256]);assert.deepEqual(cfg.methods,['donor-cell','muscl-minmod']);assert.equal(cfg.face_courant,.2);assert.equal(cfg.sufficient_face_courant,.25);
 assert.deepEqual(cfg.diagnostics.map(x=>x.id),['half-cell-shift','oblique-start']);assert.ok(cfg.diagnostics.every(x=>x.n===64&&x.method==='muscl-minmod'));assert.equal(cfg.diagnostics[0].shift_cells,.5);assert.equal(cfg.diagnostics[1].angle0,Math.PI/4);
 assert.ok(reference.citations.some(x=>x.url==='https://www.firedrakeproject.org/demos/DG_advection.py.html'));assert.match(reference.reference_scope,/No Firedrake PDE or FCT algorithm is executed/);
 const source=json(base+'cases.json')[0];assert.ok(source.references.every(x=>x.review_level));assert.ok(source.formulas.length>=3);
});

test('all eight qualified rotations retain full two-dimensional fields, stage bounds, conservation and geometric-return evidence',()=>{
 const contract=json(base+'pre-run-contract.json');assert.equal(contract.planned_tests,26);assert.equal(contract.planned_numerical_gates,158);assert.equal(contract.planned_fixed_runs,8);
 for(const[p,h]of Object.entries(contract.files_sha256))assert.equal(hash(base+p),h,p);
 const original=json(base+'attempts/01/results/result.json');assert.equal(original.passed,false);assert.equal(original.failure,null);const old=original.cases.find(x=>x.id===id);assert.equal(Object.values(old.checks).filter(x=>x===true).length,156);assert.deepEqual(Object.entries(old.checks).filter(([,v])=>v===false).map(([k])=>k).sort(),['donor-cell finest relative L1','muscl-minmod finest relative L1']);
 assert.equal(hash(base+'acceptance.json'),hash(base+'attempts/01/source/acceptance.json'));assert.equal(hash(base+'rotation.py'),hash(base+'attempts/01/source/rotation.py'));assert.equal(hash(base+'test_rotation.py'),hash(base+'attempts/01/source/archived_test_rotation.py'));
 const r=json(base+'results/result.json'),c=r.cases.find(x=>x.id===id);assert.equal(r.passed,true);assert.equal(r.failure,null);assert.equal(r.termination,'fixed_budget_completed');assert.equal(c.records.length,8);assert.equal(Object.keys(c.checks).length,158);assert.ok(Object.values(c.checks).every(v=>v===true));assert.equal(Object.keys(c.reference_qualification.checks).length,8);assert.ok(Object.values(c.reference_qualification.checks).every(v=>v===true));
 for(const row of c.records){assert.ok(row.minimum>=-5e-13&&row.maximum<=1+5e-13);assert.ok(Math.abs(row.mass_change)<=3e-12);assert.ok(row.initial_area_error<=3e-12);assert.ok(row.reference_area_error<=3e-12);assert.ok(row.maximum_courant<=.25);assert.ok(row.maximum_mean_preservation_defect<=3e-15);assert.equal(row.state_clip_count,0);assert.equal(row.retries,0);assert.equal(row.rejected_steps,0);assert.equal(row.all_saved_values_finite,true);assert.ok(Number.isFinite(row.slot_probe_mean));assert.ok(Number.isFinite(row.boundary_band_mass_fraction));assert.ok(row.snapshot_relative_l1.every(Number.isFinite));}
 const finestN=Math.max(...json(base+'inputs.json').cases[id].grids);const fine=method=>c.records.find(r=>r.n===finestN&&r.method===method);assert.ok(fine('muscl-minmod').relative_l1<=.85*fine('donor-cell').relative_l1);
 const program=String.raw`import array,ast,json,math,struct,sys,zipfile
from pathlib import Path
base=Path('code/validated-examples/2026-11-23/zalesak')
rows=json.loads((base/'results/result.json').read_text())['cases'][0]['records']
def npy(z,name,values=False):
 b=z.read(name+'.npy');assert b[:6]==b'\x93NUMPY';wide=b[6]!=1
 n=struct.unpack('<I' if wide else '<H',b[8:12] if wide else b[8:10])[0];start=12 if wide else 10
 h=ast.literal_eval(b[start:start+n].decode());assert not h['fortran_order']
 if not values:return h['shape']
 payload=b[start+n:]
 if h['descr'].startswith('<U'):
  width=int(h['descr'][2:]);s=payload.decode('utf-32-le');return [s[i:i+width].rstrip('\0') for i in range(0,len(s),width)]
 assert h['descr'] in ['<f8','=f8'];a=array.array('d');a.frombytes(payload)
 if sys.byteorder!='little':a.byteswap()
 assert all(math.isfinite(x) for x in a);return a
for row in rows:
 n=row['n']
 with zipfile.ZipFile(base/'results'/row['field']) as z:
  for name in ['q','q_initial','q_reference']:
   assert npy(z,name)==(n,n);a=npy(z,name,True);assert min(a)>=-5e-13 and max(a)<=1+5e-13
  for name in ['q_history','q_reference_history']:assert npy(z,name)==(len(row['snapshot_times']),n,n)
  assert npy(z,'edges')==(n+1,);assert npy(z,'slot_probe_weights')==(n,n)
 with zipfile.ZipFile(base/'results'/row['history']) as z:
  columns=npy(z,'columns',True);assert npy(z,'values')==(3*row['steps'],len(columns))
  a=npy(z,'values',True)
  def column(name):return a[columns.index(name)::len(columns)]
  assert set(column('stage'))=={1.,2.,3.}
  for name in ['face_min','fe_min','rk_min']:assert min(column(name))>=-5e-13
  for name in ['face_max','fe_max','rk_max']:assert max(column(name))<=1+5e-13
  for name in ['fe_mass_defect','rk_mass_defect']:assert max(column(name))<=3e-12
  assert max(column('mean_preservation_defect'))<=3e-15
print('all eight full two-dimensional fields and every stage are hash-bound and retained')`;
 assert.match(execFileSync('python3',['-B','-c',program],{cwd:root,encoding:'utf8'}),/all eight full two-dimensional fields/);
});
