import {projectCatalogBeforeVefVet} from './fixtures/atlas-vef-vet-projection.mjs';
import {projectCatalogBeforeFinal23} from './fixtures/atlas-final23-projection.mjs';
import {problemCount,examplesAddedAfterBatch37} from './fixtures/atlas-inventory.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const root=new URL('../',import.meta.url),origin='https://hrkoyama.github.io';
const bytes=path=>readFileSync(new URL(path,root));
const read=path=>bytes(path).toString();
const json=path=>JSON.parse(read(path));
const sha=path=>createHash('sha256').update(bytes(path)).digest('hex');
const objectSha=value=>createHash('sha256').update(JSON.stringify(value)).digest('hex');
const base='code/validated-examples/2026-11-23-r5/noh/';
const previous='code/validated-examples/2026-11-23-r3/noh/';
const commit='9bacc477eb791e959c9621e771fc7a725db755fa';
function local(value){
  const url=new URL(value,origin);assert.equal(url.origin,origin);
  const path=url.pathname.slice(1)+(url.pathname.endsWith('/')?'index.html':'');
  assert.ok(existsSync(new URL(path,root)),value);
  if(url.hash&&!url.hash.startsWith('#/')&&path.endsWith('.html'))assert.ok(read(path).includes(`id="${url.hash.slice(1)}"`),value);
  return url;
}

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

test('Noh adds one physical problem while every historical problem, image and reference value remains unchanged',()=>{
  const problems=json('catalog/atlas-test-problems.json').problems;
  assert.equal(problems.length,problemCount);assert.equal(problems.filter(row=>row.id==='noh').length,1);
  assert.equal(objectSha(projectCatalogBeforeFinal23('catalog/atlas-test-problems.json',json('catalog/atlas-test-problems.json')).problems.filter(row=>!['noh','sedov','double-mach','forward-step','isentropic-vortex','guderley','zalesak','swashes-topography','dry-bed-dam-break','lid-driven-cavity','wall-manufactured','level-set-circle', 'kh-initial-growth', 'rt-initial-growth', 'lshape-fem', 'annular-viscous-mms', 'poisson-neumann', 'poisson-robin', 'ale-nonuniform-transport', 'cgrid-rotating-wave', 'srhd-collision', 'srmhd-alfven','checkerboard-diffusion','rotated-anisotropic-diffusion','neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short','thermal-landau-damping','thermal-two-stream','dsmc-couette','dsmc-fourier','dsmc-planar-shock',...examplesAddedAfterBatch37].includes(row.id)).map(historicalProblem).map(row=>{if(row.id!=='double-rarefaction')return row;const copy={...row};delete copy.supplemental_examples;return copy;})),'3268e6e1356ae6fb75dc525ee8420673efb2237dd0aef8a111abaa919db6a7ab');
  const previews=json('numerical-methods-atlas/gallery/preview-manifest.json').items;
  assert.equal(previews.length,problemCount);
  assert.equal(objectSha(previews.filter(row=>!['noh','sedov','double-mach','forward-step','isentropic-vortex','guderley','zalesak','swashes-topography','dry-bed-dam-break','lid-driven-cavity','wall-manufactured','level-set-circle', 'kh-initial-growth', 'rt-initial-growth', 'lshape-fem', 'annular-viscous-mms', 'poisson-neumann', 'poisson-robin', 'ale-nonuniform-transport', 'cgrid-rotating-wave', 'srhd-collision', 'srmhd-alfven','checkerboard-diffusion','rotated-anisotropic-diffusion','neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short','thermal-landau-damping','thermal-two-stream','dsmc-couette','dsmc-fourier','dsmc-planar-shock',...examplesAddedAfterBatch37].includes(row.id)).map(({id,image,image_sha256,caption})=>({id,image,image_sha256,caption}))),'25c25a4cb7ad5c54e5788b984d949c44994d3f1706ed36c4ef30a3ce36fa6c2b');
  assert.equal(sha('numerical-methods-atlas/assets/reference-solutions.json'),'c33118198faa7b35b4f66d7aad6353206f6d90c848f12e0a059874b91f897edc');
  assert.equal(sha('numerical-methods-atlas/code-and-data/examples.json'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
});

test('the fixed Noh computation uses cold inflow, conservative radial averages and the original acceptance contract',()=>{
  const input=json(base+'inputs.json').cases['noh-shock'],acceptance=json(base+'acceptance.json');
  assert.equal(input.gamma,5/3);assert.equal(input.rho0,1);assert.equal(input.u0,-1);assert.equal(input.p0,0);
  assert.deepEqual(input.geometries,['planar','cylindrical','spherical']);assert.deepEqual(input.grids,[64,128,256,512]);
  assert.equal(input.state_floor,null);assert.equal(input.time_integrator,'SSPRK2');
  assert.deepEqual(input.stress_quadrature_by_geometry,{planar:'arithmetic-face',cylindrical:'arithmetic-face',spherical:'linear-radial-stress'});
  assert.deepEqual(input.reconstruction_by_geometry,{planar:'piecewise-constant',cylindrical:'piecewise-constant',spherical:'muscl-minmod'});
  assert.equal(input.active_spherical_pre_run_contract,'pre-run-contract-spherical-revision03.json');
  assert.equal(input.final_time,.6);assert.equal(input.r_max,1);
  assert.equal(acceptance.frozen_before_first_run,true);
  assert.equal(sha(base+'acceptance.json'),'a12c0ce119877e71fc8dfd852bd6dfb6aa6d8e7beb5e18bd13e91a5dd16117ff','acceptance is the file frozen before the first failed run');
  assert.equal(acceptance.checks.density_l1_finest_max,.12);
  assert.equal(acceptance.checks.density_l1_last_pair_order_min,.35);
  assert.equal(acceptance.checks.conservation_mass_relative_max,2e-12);
  assert.equal(acceptance.checks.conservation_energy_relative_max,2e-12);
  assert.equal(acceptance.checks.center_heating_bound_is_not_an_accuracy_gate,true);
  assert.match(input.geometric_source,/interfacial Rusanov normal stress/);
  assert.match(input.spatial_claim,/no Cartesian 2D/);
  const result=json(base+'results/result.json'),row=result.cases.find(row=>row.id==='noh-shock');
  assert.equal(result.passed,true);assert.equal(result.input_sha256,sha(base+'inputs.json'));
  assert.equal(Object.keys(row.checks).length,105);assert.ok(Object.values(row.checks).every(value=>value===true));
  for(const geometry of input.geometries){
    const records=row.records.filter(record=>record.geometry===geometry);
    assert.deepEqual(records.map(record=>record.n),input.grids);
    assert.ok(records.every((record,i)=>!i||record.density_l1<records[i-1].density_l1));
    for(const record of records){
      assert.ok(record.mass_balance_relative<=acceptance.checks.conservation_mass_relative_max);
      assert.ok(record.energy_balance_relative<=acceptance.checks.conservation_energy_relative_max);
      assert.ok(Number.isFinite(record.center_max_sie_relative_excess));
    }
  }
  const failed=json(base+input.retained_failed_attempt);
  assert.equal(failed.passed,false,'the initial failed source discretization remains evidence');
  assert.equal(failed.checks,59);
  assert.equal(failed.failed.length,6,'the genuine initial diagnostic summary records the six cylindrical failures');
});

test('ExactPack is a separately cited, pinned analytic comparison with reproducible hashes and an explicit gamma restriction',()=>{
  const bibliography=json(base+'exactpack-reference.json'),receipt=json(base+'exactpack-reference-receipt.json');
  assert.equal(bibliography.original_problem.doi,'10.1016/0021-9991(87)90074-X');
  assert.equal(bibliography.citation.doi,'10.1016/j.softx.2023.101560');
  assert.equal(bibliography.software.commit,commit);assert.equal(receipt.reference_commit,commit);
  assert.equal(receipt.passed,true);assert.equal(receipt.gamma_restriction_negative_control_detected,true);
  assert.equal(receipt.point_cases,12);assert.equal(receipt.cell_average_cases,12);
  assert.equal(receipt.local_analytic_reference_sha256,sha(base+'noh_reference.py'));
  assert.equal(receipt.reference_generator_sha256,sha(base+'generate_exactpack_reference.py'));
  assert.equal(receipt.snapshot_sha256,sha(base+'exactpack-reference-snapshot.json'));
  for(const value of Object.values(receipt.errors))assert.ok(value<=receipt.tolerance);
  assert.equal(receipt.source_files_sha256['exactpack/solvers/noh/noh1.py'],'bac597f501b021be85ef4956d0e075f1cdbff69aa72a3de788600f8c28e0d5a1');
  assert.match(JSON.stringify(bibliography.license),/BSD-3/);
  assert.match(JSON.stringify(bibliography.limitations),/gamma/);
  assert.match(receipt.scope,/not a spherical PDE execution/);
  const metadata=json(base+'cases.json')[0];
  assert.deepEqual([...metadata.method_ids].sort(),['heun','minmod','muscl','rusanov']);
  const prose=read(base+'README.md')+read(base+'THIRD_PARTY.md');
  for(const needle of ['ExactPack','10.1016/0021-9991(87)90074-X','10.1016/j.softx.2023.101560',commit])assert.ok(prose.includes(needle),needle);
});

test('spherical extension preserves the complete r3 release, the original59 gates and all eight planar/cylindrical profiles',()=>{
  assert.equal(sha(previous+'source-manifest.json'),'228da58295758877c3131fc888bfd39dcf33aa30d493b89655d7e3e9ce9b8207');
  assert.equal(sha(previous+'verification.json'),'056f668cd6f5450df3626383121274b55b2edf20519886d75f64f60d24ba6f29');
  assert.equal(sha(previous+'atlas-noh-2026-11-23-r3.zip'),'8c59623825c2eee95b6679a6697a0a91a729ba439545a880946d04764e384b36');
  const frozen=json(previous+'source-manifest.json');
  for(const [path,hash]of Object.entries(frozen.files))assert.equal(sha(previous+path),hash,'r3/'+path);
  const original=json(previous+'results/result.json').cases[0],current=json(base+'results/result.json').cases[0];
  assert.equal(Object.keys(original.checks).length,59);
  const details=new Map(current.check_details.map(row=>[row.name,row]));
  for(const item of original.check_details){
    assert.ok(details.has(item.name),item.name+' is retained');
    assert.deepEqual(details.get(item.name).bound,item.bound,item.name+' retains its frozen bound');
    assert.equal(current.checks[item.name],true);
  }
  assert.deepEqual(current.records.filter(row=>row.geometry!=='spherical'),original.records,'all original eight standard result records retain their values and keys');
  const profiles=Object.keys(frozen.files).filter(path=>/^results\/profiles\/(?:planar|cylindrical)-n\d+[.]csv$/.test(path));
  assert.equal(profiles.length,8);
  for(const path of profiles)assert.equal(sha(base+path),frozen.files[path],path+' retains its exact CSV bytes');
  for(const file of ['acceptance.json','noh_reference.py','generate_exactpack_reference.py','exactpack-reference.json','exactpack-reference-receipt.json','exactpack-reference-snapshot.json'])assert.equal(sha(base+file),sha(previous+file),file+' is unchanged');
  const contract=json(base+'pre-run-contract-spherical.json');
  assert.equal(contract.pde_or_unit_tests_executed_after_spherical_changes,false,'the pre-run contract remains the original declaration');
  assert.deepEqual(contract.base_check_inventory,original.check_details.map(({name,bound})=>({name,bound})));
  assert.equal(contract.files_sha256['acceptance.json'],sha(base+'acceptance.json'));
  assert.equal(contract.files_sha256['spherical-acceptance.json'],sha(base+'spherical-acceptance.json'));
  const sphericalAcceptance=json(base+'spherical-acceptance.json');
  assert.deepEqual(contract.new_spherical_check_inventory,sphericalAcceptance.check_name_templates);
  const specificNames=[...[64,128,256,512].flatMap(n=>contract.new_spherical_check_inventory.per_grid.map(name=>name.replace('{N}',n))),contract.new_spherical_check_inventory.finest];
  const sphereBase=Object.keys(original.checks).filter(name=>name.startsWith('planar')).map(name=>name.replace(/^planar/,'spherical'));
  const expected=[...Object.keys(original.checks),...sphereBase,...specificNames];
  assert.equal(expected.length,105);assert.equal(new Set(expected).size,105);
  assert.deepEqual(Object.keys(current.checks).sort(),expected.sort(),'only the declared spherical gates are added');
  const extraBounds=[sphericalAcceptance.checks.radial_momentum_balance_relative_max,sphericalAcceptance.checks.mass_temporal_bias_identity_relative_max,sphericalAcceptance.checks.energy_temporal_bias_identity_relative_max,'all finite; no maximum-error convergence gate'];
  for(const n of [64,128,256,512])for(const [i,template]of contract.new_spherical_check_inventory.per_grid.entries())assert.deepEqual(details.get(template.replace('{N}',n)).bound,extraBounds[i]);
  assert.equal(details.get(contract.new_spherical_check_inventory.finest).bound,sphericalAcceptance.checks.core_density_l1_finest_max);
  const input=json(base+'inputs.json').cases['noh-shock'];
  assert.match(input.active_spherical_pre_run_contract,/^pre-run-contract-[a-z0-9-]+[.]json$/);
  const active=json(base+input.active_spherical_pre_run_contract);
  assert.deepEqual(active.gate_inventory,current.check_details.map(({name,bound})=>({name,bound})),'the active revision retains all105 frozen names and bounds');
  assert.deepEqual(active.change.stress_quadrature_by_geometry,input.stress_quadrature_by_geometry);
  assert.deepEqual(active.change.reconstruction_by_geometry,input.reconstruction_by_geometry);
  assert.equal(active.change.default_reconstruction,'piecewise-constant');
  assert.equal(active.revision03_unit_tests_or_pde_executed,false);
  assert.equal(active.planned_pytest_count,28);
  assert.equal(json(base+'verification.json').tests,28);
  for(const path of ['inputs.json','run.py','noh_solver.py','test_noh.py','acceptance.json','spherical-acceptance.json'])assert.equal(sha(base+path),active.files_sha256[path],path+' matches the active pre-run source declaration');
  const raw=json(base+'results/results.json');
  assert.equal(raw.receipts.spherical_pre_run_contract_filename,input.active_spherical_pre_run_contract);
  assert.equal(raw.receipts.spherical_pre_run_contract_sha256,sha(base+input.active_spherical_pre_run_contract));
  for(const run of raw.runs){
    assert.equal(run.stress_quadrature,input.stress_quadrature_by_geometry[run.geometry]);
    assert.equal(run.reconstruction,input.reconstruction_by_geometry[run.geometry]);
  }
  const firstSphere=json(base+'attempts/spherical-01/results/result.json').cases[0];
  assert.equal(firstSphere.passed,false,'the original unsuccessful spherical attempt remains evidence');
  const failedNames=['spherical: finest shock_error_in_dx','spherical: finest plateau_density_relative_error'].sort();
  assert.deepEqual(Object.entries(firstSphere.checks).filter(([,passed])=>!passed).map(([name])=>name).sort(),failedNames);
  const secondSphere=json(base+'attempts/spherical-02/results/result.json').cases[0];
  assert.equal(secondSphere.passed,false);
  assert.deepEqual(Object.entries(secondSphere.checks).filter(([,passed])=>!passed).map(([name])=>name).sort(),failedNames);
});

test('spherical diagnostics distinguish discrete conservation from the signed SSPRK2 boundary bias and retain the origin in the core norm',()=>{
  const acceptance=json(base+'spherical-acceptance.json');
  assert.equal(sha(base+'spherical-acceptance.json'),'bb1c8d14feb07a8876f04711aa81780642d5f6a547f6754ccafd2eaf223530a2');
  assert.equal(acceptance.frozen_before_first_spherical_pde_run_and_unit_tests,true);
  const raw=json(base+'results/results.json');
  const sphere=raw.runs.filter(row=>row.geometry==='spherical');
  assert.deepEqual(sphere.map(row=>row.n),[64,128,256,512]);
  const close=(a,b,tolerance=2e-12)=>assert.ok(Number.isFinite(a)&&Number.isFinite(b)&&Math.abs(a-b)<=tolerance*Math.max(Math.abs(a),Math.abs(b),Number.MIN_VALUE),a+' versus '+b);
  for(const run of sphere){
    assert.equal(run.dimension,3);assert.equal(run.status,'completed');
    const m=run.metrics;assert.ok(m.dt_cubed_sum>0);
    assert.equal(run.reconstruction,'muscl-minmod');
    assert.ok(Number.isInteger(m.reconstruction_theta_reduced_stage_cells)&&m.reconstruction_theta_reduced_stage_cells>=0);
    assert.ok(Number.isInteger(m.reconstruction_theta_zero_stage_cells)&&m.reconstruction_theta_zero_stage_cells>=0&&m.reconstruction_theta_zero_stage_cells<=m.reconstruction_theta_reduced_stage_cells);
    assert.ok(m.reconstruction_theta_min>=0&&m.reconstruction_theta_min<=1);
    close(m.analytic_total_mass,512/375);close(m.analytic_total_energy,256/375);
    close(m.mass_temporal_bias_expected,m.dt_cubed_sum/6,32*Number.EPSILON);
    close(m.energy_temporal_bias_expected,m.dt_cubed_sum/12,32*Number.EPSILON);
    assert.ok(m.mass_vs_analytic_signed>0&&m.energy_vs_analytic_signed>0,'the quadrature bias is recorded without correcting the solution');
    const massResidual=m.final_integral[0]-512/375-m.dt_cubed_sum/6;
    const energyResidual=m.final_integral[2]-256/375-m.dt_cubed_sum/12;
    assert.ok(Math.abs(massResidual)/(512/375)<=acceptance.checks.mass_temporal_bias_identity_relative_max);
    assert.ok(Math.abs(energyResidual)/(256/375)<=acceptance.checks.energy_temporal_bias_identity_relative_max);
    const momentum=m.final_integral[1]-m.initial_integral[1]-m.boundary_net_integral[1]-m.geometric_source_integral[1];
    assert.ok(Math.abs(momentum)/m.radial_momentum_balance_scale<=acceptance.checks.radial_momentum_balance_relative_max);
    for(const key of ['mass_balance_signed','energy_balance_signed','radial_momentum_balance_signed','mass_temporal_bias_residual_signed','energy_temporal_bias_residual_signed','mass_temporal_bias_residual_signed_relative','energy_temporal_bias_residual_signed_relative'])assert.ok(Number.isFinite(m[key]),key);
    for(const value of Object.values(m.center_first_cell))assert.ok(Number.isFinite(value),'first-cell center diagnostics remain visible');
    for(const key of ['center_max_specific_internal_energy','center_max_specific_internal_energy_ratio','center_min_density','center_min_density_ratio','center_max_pressure','center_max_pressure_ratio'])assert.ok(Number.isFinite(m[key]),key);
    const lines=read(base+'results/'+run.profile).trim().split(/\r?\n/),columns=lines.shift().split(',');
    const cells=lines.map(line=>Object.fromEntries(line.split(',').map((value,i)=>[columns[i],Number(value)])));
    assert.equal(cells.length,run.n);
    for(const cell of cells){
      assert.ok(Number.isFinite(cell.r_volume_centroid)&&cell.r_volume_centroid>cell.r_left&&cell.r_volume_centroid<cell.r_right);
      close(cell.r_volume_centroid,.75*(cell.r_right**4-cell.r_left**4)/(cell.r_right**3-cell.r_left**3));
    }
    assert.equal(cells[0].mask_core,1);assert.equal(cells[0].mask_center,1,'the core includes the origin cells');
    const core=cells.filter(row=>row.r_right<=.7*m.shock_exact);
    assert.ok(core.length>0);assert.equal(core.length,m.core_density_errors.cells);
    const numerator=core.reduce((sum,row)=>sum+(row.r_right**3-row.r_left**3)/3*Math.abs(row.rho-64),0);
    const denominator=core.reduce((sum,row)=>sum+(row.r_right**3-row.r_left**3)/3*64,0);
    close(numerator/denominator,m.core_density_l1);
    for(const row of cells)assert.equal(row.mask_core,row.r_right<=.7*m.shock_exact?1:0);
  }
  assert.ok(sphere.at(-1).metrics.core_density_l1<=acceptance.checks.core_density_l1_finest_max);
});

test('Noh reference, figure, chapter and execution connect through their actual new records',()=>{
  const current=projectCatalogBeforeVefVet('catalog/atlas-reference-supplements.json',json('catalog/atlas-reference-supplements.json'));
  const addition=projectCatalogBeforeFinal23('catalog/atlas-reference-supplements.json',current).cases;
  const previousIDs=new Set(addition.map(row=>row.id));
  const registry=projectCatalogBeforeVefVet('numerical-methods-atlas/validation/releases.json',json('numerical-methods-atlas/validation/releases.json'));
  const oldGroups=new Set(projectCatalogBeforeFinal23('numerical-methods-atlas/validation/releases.json',registry).releases.map(row=>row.group));
  const newCases=registry.releases.filter(row=>!oldGroups.has(row.group)).flatMap(row=>row.case_ids);
  assert.equal(newCases.length,19);
  assert.deepEqual(current.cases.filter(row=>!previousIDs.has(row.id)).map(row=>row.id).sort(),['bratu-lower-branch-analytic','harmonic-oscillator-exact','stiff-cosine-exact','hydrogenic-coulomb-reference',...newCases].sort());
  for(const id of ['bratu-lower-branch-analytic','harmonic-oscillator-exact','stiff-cosine-exact','hydrogenic-coulomb-reference']){
    const card=current.cases.find(row=>row.id===id),contract=card.reference_contract;assert.equal(card.kind,'analytic');assert.equal(contract.class,'continuous-exact');
    for(const binding of [contract.fixed_input_binding,{url:contract.release_binding.manifest,sha256:contract.release_binding.manifest_sha256},{url:contract.release_binding.verification,sha256:contract.release_binding.verification_sha256}])assert.equal(sha(new URL(binding.url).pathname.slice(1)),binding.sha256,id+'/immutable-binding');
    assert.ok(card.citations.every(row=>row.role&&row.title&&row.url));
  }
  assert.deepEqual(addition.filter(row=>!['zalesak-rotation','weno-critical-profile','lake-at-rest-bed','swashes-bernoulli','ritter-dry-bed','ghia-re100','wall-mms','level-set-translation','level-set-rotation', 'kh-initial-growth', 'rt-initial-growth', 'circular-alfven-refinement', 'magnetic-loop-independent', 'postshock-orszag-tang', 'lshape-fem', 'annular-viscous-mms', 'poisson-neumann', 'poisson-robin', 'ale-nonuniform-transport', 'cgrid-rotating-wave', 'srhd-collision', 'srmhd-alfven', 'sem-poisson-2d', 'fr-periodic-advection','checkerboard-diffusion','rotated-anisotropic-diffusion','neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short','thermal-landau-damping','thermal-two-stream','pic-independent-spatial','dsmc-couette','dsmc-fourier','dsmc-planar-shock',...examplesAddedAfterBatch37].includes(row.id)).map(row=>row.id),['noh','sedov','double-mach','forward-step','isentropic-vortex','guderley']);assert.equal(addition[0].kind,'analytic');
  const reference=json('numerical-methods-atlas/solutions/index.json').cases.find(row=>row.id==='noh');
  const problem=json('numerical-methods-atlas/problems/noh/index.json');
  const run=json('numerical-methods-atlas/validation/noh-shock/index.json');
  const gallery=json('numerical-methods-atlas/gallery/index.json').items.find(row=>row.id==='noh');
  assert.deepEqual(run.additional_figures.map(row=>row.file),['noh-shock-errors.png','noh-spherical-budget.png']);
  assert.deepEqual(problem.executions.map(row=>row.id),['noh-shock','noh-cartesian-2d']);
  assert.deepEqual(problem.references.map(row=>row.id),['noh']);
  assert.deepEqual(problem.equations.map(row=>row.id),['euler']);
  assert.deepEqual([...run.method_ids].sort(),['heun','minmod','muscl','rusanov']);
  assert.ok([...run.release.code_urls,...run.release.test_urls].every(url=>!url.includes('/attempts/')),'failed revisions are evidence, not the active algorithm');
  assert.deepEqual(run.execution_navigation.methods.map(row=>row.id).sort(),['heun','minmod','muscl','rusanov']);
  const mapping=json('catalog/atlas-depth-expansion.json').case_equations['noh-shock'];
  assert.deepEqual(mapping.ids,['euler']);
  assert.deepEqual(run.execution_navigation.equations.map(row=>row.id),mapping.ids);
  assert.deepEqual(run.execution_navigation.equations[0].note,mapping.note);
  assert.equal(run.navigation_source_sha256['catalog/atlas-depth-expansion.json'],sha('catalog/atlas-depth-expansion.json'));
  assert.equal(gallery.image,'/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d-preview.png');
  assert.equal(gallery.image_sha256,sha(gallery.image.slice(1)));
  assert.equal(run.execution_navigation.figure.url,origin+'/'+base+'results/noh-shock.png');
  assert.notEqual(gallery.image,new URL(run.execution_navigation.figure.url).pathname);
  const methods=json('numerical-methods-atlas/methods/index.json').methods;
  const muscl=methods.find(row=>row.id==='muscl');
  assert.equal(muscl.depth_release.group,'mhd','the original MUSCL MHD release remains primary');
  assert.equal(objectSha(muscl.depth_release),'d0c2c83e60edf5893487c5a97f7363ed499bb100b5f886a4c80447ad4bb9e8c8','the complete primary release object is unchanged from6995ffc7');
  assert.equal(muscl.depth_release.code_edition,'2026-11-22');
  assert.deepEqual(muscl.depth_release.case_ids,['shu-independent']);
  const extra=muscl.depth_additional_releases.find(row=>row.group==='noh');
  assert.equal(extra.code_edition,'2026-11-23-r5');assert.deepEqual(extra.case_ids,['noh-shock']);
  for(const id of ['heun','minmod','muscl','rusanov']){
    const method=methods.find(row=>row.id===id),card=method.problem_navigation.problems.find(row=>row.id==='noh');
    assert.equal(card.role,'execution');
    assert.deepEqual(card.executions.map(row=>row.id),['heun','rusanov'].includes(id)?['noh-shock','noh-cartesian-2d']:['noh-shock'],id+' retains its actual scoped Noh executions');
  }
  assert.equal(addition[0].dimension,1,'symmetry dimension is distinct from a Cartesian multidimensional computation');
  assert.deepEqual(addition[0].parameters.geometry_dimensions,[1,2,3]);
  assert.match(addition[0].assumptions,/radial/);
  assert.match(addition[0].assumptions,/Cartesian/);
  for(const language of ['ja','en']){
    assert.equal(local(reference.view[language]).pathname,'/numerical-methods-atlas/validation/noh-shock/');
    assert.equal(local(reference.reading[language]).pathname,`/numerical-methods-atlas/${language}/read/validation-noh/`);
    const page=read(`numerical-methods-atlas/${language}/read/validation-noh/index.html`);
    assert.ok(page.includes('ExactPack')&&page.includes('10.1016/j.softx.2023.101560'));
    for(const figure of run.additional_figures){
      const url=origin+'/'+base+'results/'+figure.file;
      local(url);
      assert.ok(page.includes('href="'+new URL(url).pathname+'"'));
      assert.ok(read('numerical-methods-atlas/validation/noh-shock/index.md').includes(url));
      assert.ok(read(`numerical-methods-atlas/${language}/read/validation-noh/index.md`).includes(figure.caption[language]));
    }
  }
});

test('supplementary references cannot overwrite old identities or omit citation roles and localized routes',()=>{
  const program=String.raw`
import copy,json,pathlib,sys,tempfile
sys.path.insert(0,str(pathlib.Path.cwd()/'scripts'))
from atlas_reference_catalog import load_reference_cases
source=json.loads(pathlib.Path('catalog/atlas-reference-supplements.json').read_text())
with tempfile.TemporaryDirectory(prefix='atlas-reference-catalog-') as directory:
 root=pathlib.Path(directory)
 old=root/'numerical-methods-atlas/assets/reference-solutions.json';old.parent.mkdir(parents=True);old.write_text(json.dumps({'cases':[{'id':'old'}]}))
 extra=root/'catalog/atlas-reference-supplements.json';extra.parent.mkdir()
 def write(value):extra.write_text(json.dumps(value))
 write(source);assert [row['id'] for row in load_reference_cases(root) if row['id'] not in ['zalesak-rotation','weno-critical-profile','lake-at-rest-bed','swashes-bernoulli','ritter-dry-bed','ghia-re100','wall-mms','level-set-translation','level-set-rotation','sem-poisson-2d','fr-periodic-advection', 'kh-initial-growth', 'rt-initial-growth', 'circular-alfven-refinement', 'magnetic-loop-independent', 'postshock-orszag-tang', 'lshape-fem', 'annular-viscous-mms', 'poisson-neumann', 'poisson-robin', 'ale-nonuniform-transport', 'cgrid-rotating-wave', 'srhd-collision', 'srmhd-alfven','checkerboard-diffusion','rotated-anisotropic-diffusion','neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short','thermal-landau-damping','thermal-two-stream','pic-independent-spatial','dsmc-couette','dsmc-fourier','dsmc-planar-shock']+${JSON.stringify(examplesAddedAfterBatch37)}]==['old','noh','sedov','double-mach','forward-step','isentropic-vortex','guderley']+['bratu-lower-branch-analytic','harmonic-oscillator-exact','stiff-cosine-exact','hydrogenic-coulomb-reference']
 for mutation in ['duplicate','citation','route']:
  bad=copy.deepcopy(source)
  if mutation=='duplicate':bad['cases'][0]['id']='old'
  elif mutation=='citation':del bad['cases'][0]['citations'][0]['role']
  else:del bad['cases'][0]['view']['ja']
  write(bad)
  try:load_reference_cases(root)
  except ValueError:pass
  else:raise AssertionError('accepted invalid reference '+mutation)
`;
  execFileSync('python3',['-B','-c',program],{cwd:fileURLToPath(root),encoding:'utf8',timeout:10000});
});
