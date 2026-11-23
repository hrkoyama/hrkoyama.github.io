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
const base='code/validated-examples/2026-11-23-r3/noh/';
const commit='9bacc477eb791e959c9621e771fc7a725db755fa';
function local(value){
  const url=new URL(value,origin);assert.equal(url.origin,origin);
  const path=url.pathname.slice(1)+(url.pathname.endsWith('/')?'index.html':'');
  assert.ok(existsSync(new URL(path,root)),value);
  if(url.hash&&!url.hash.startsWith('#/')&&path.endsWith('.html'))assert.ok(read(path).includes(`id="${url.hash.slice(1)}"`),value);
  return url;
}

test('Noh adds one physical problem while every historical problem, image and reference value remains unchanged',()=>{
  const problems=json('catalog/atlas-test-problems.json').problems;
  assert.equal(problems.length,84);assert.equal(problems.filter(row=>row.id==='noh').length,1);
  assert.equal(objectSha(problems.filter(row=>row.id!=='noh')),'7d8427b4abea2ecc81c651b25888e242c35033c414d53fccfdf4b1e49a778434');
  const previews=json('numerical-methods-atlas/gallery/preview-manifest.json').items;
  assert.equal(previews.length,84);
  assert.equal(objectSha(previews.filter(row=>row.id!=='noh').map(({id,image,image_sha256,caption})=>({id,image,image_sha256,caption}))),'57239dc61d0fc48ff97ec9cfa2c771bd1b675b561a884bb6843c70251f4481c0');
  assert.equal(sha('numerical-methods-atlas/assets/reference-solutions.json'),'c33118198faa7b35b4f66d7aad6353206f6d90c848f12e0a059874b91f897edc');
  assert.equal(sha('numerical-methods-atlas/code-and-data/examples.json'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
});

test('the fixed Noh computation uses cold inflow, conservative radial averages and the original acceptance contract',()=>{
  const input=json(base+'inputs.json').cases['noh-shock'],acceptance=json(base+'acceptance.json');
  assert.equal(input.gamma,5/3);assert.equal(input.rho0,1);assert.equal(input.u0,-1);assert.equal(input.p0,0);
  assert.deepEqual(input.geometries,['planar','cylindrical']);assert.deepEqual(input.grids,[64,128,256,512]);
  assert.equal(input.state_floor,null);assert.equal(input.time_integrator,'SSPRK2');
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
  assert.equal(Object.keys(row.checks).length,59);assert.ok(Object.values(row.checks).every(value=>value===true));
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
  assert.deepEqual([...metadata.method_ids].sort(),['heun','rusanov']);
  const prose=read(base+'README.md')+read(base+'THIRD_PARTY.md');
  for(const needle of ['ExactPack','10.1016/0021-9991(87)90074-X','10.1016/j.softx.2023.101560',commit])assert.ok(prose.includes(needle),needle);
});

test('Noh reference, figure, chapter and execution connect through their actual new records',()=>{
  const addition=json('catalog/atlas-reference-supplements.json').cases;
  assert.deepEqual(addition.map(row=>row.id),['noh']);assert.equal(addition[0].kind,'analytic');
  const reference=json('numerical-methods-atlas/solutions/index.json').cases.find(row=>row.id==='noh');
  const problem=json('numerical-methods-atlas/problems/noh/index.json');
  const run=json('numerical-methods-atlas/validation/noh-shock/index.json');
  const gallery=json('numerical-methods-atlas/gallery/index.json').items.find(row=>row.id==='noh');
  assert.deepEqual(problem.executions.map(row=>row.id),['noh-shock']);
  assert.deepEqual(problem.references.map(row=>row.id),['noh']);
  assert.deepEqual(problem.equations.map(row=>row.id),['euler']);
  assert.deepEqual([...run.method_ids].sort(),['heun','rusanov']);
  assert.ok([...run.release.code_urls,...run.release.test_urls].every(url=>!url.includes('/attempts/')),'failed revisions are evidence, not the active algorithm');
  assert.deepEqual(run.execution_navigation.methods.map(row=>row.id).sort(),['heun','rusanov']);
  const mapping=json('catalog/atlas-depth-expansion.json').case_equations['noh-shock'];
  assert.deepEqual(mapping.ids,['euler']);
  assert.deepEqual(run.execution_navigation.equations.map(row=>row.id),mapping.ids);
  assert.deepEqual(run.execution_navigation.equations[0].note,mapping.note);
  assert.equal(run.navigation_source_sha256['catalog/atlas-depth-expansion.json'],sha('catalog/atlas-depth-expansion.json'));
  assert.equal(gallery.image,'/'+base+'results/noh-shock-preview.png');
  assert.equal(gallery.image_sha256,sha(base+'results/noh-shock-preview.png'));
  assert.equal(run.execution_navigation.figure.url,origin+'/'+base+'results/noh-shock.png');
  assert.notEqual(gallery.image,new URL(run.execution_navigation.figure.url).pathname);
  assert.match(JSON.stringify(addition[0].assumptions),/not a two-dimensional Cartesian computation/);
  for(const language of ['ja','en']){
    assert.equal(local(reference.view[language]).pathname,'/numerical-methods-atlas/validation/noh-shock/');
    assert.equal(local(reference.reading[language]).pathname,`/numerical-methods-atlas/${language}/read/validation-noh/`);
    const page=read(`numerical-methods-atlas/${language}/read/validation-noh/index.html`);
    assert.ok(page.includes('ExactPack')&&page.includes('10.1016/j.softx.2023.101560'));
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
 write(source);assert [row['id'] for row in load_reference_cases(root)]==['old','noh']
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
  execFileSync('python3',['-B','-c',program],{cwd:fileURLToPath(root),encoding:'utf8'});
});
