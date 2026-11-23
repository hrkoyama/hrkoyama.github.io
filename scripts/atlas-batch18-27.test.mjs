import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';

const root=new URL('../',import.meta.url);
const bytes=p=>readFileSync(new URL(p,root));
const json=p=>JSON.parse(bytes(p));
const sha=p=>createHash('sha256').update(bytes(p)).digest('hex');
const origin='https://hrkoyama.github.io';
const plans=[
 ['instability-growth',22,74,['kh-initial-growth','rt-initial-growth']],
 ['mhd-transport',47,125,['circular-alfven-refinement','magnetic-loop-independent','postshock-orszag-tang']],
 ['mesh-boundary',20,174,['lshape-fem','annular-viscous-mms','poisson-neumann','poisson-robin']],
 ['moving-waves',19,98,['ale-nonuniform-transport','cgrid-rotating-wave']],
 ['relativistic',25,110,['srhd-collision','srmhd-alfven']],
];
const mapping={
 'kh-initial-growth':['kh-initial-growth','forced-vorticity'],
 'rt-initial-growth':['rt-initial-growth','boussinesq-buoyancy'],
 'circular-alfven-refinement':['circular-alfven','mhd'],
 'magnetic-loop-independent':['magnetic-loop','mhd'],
 'postshock-orszag-tang':['orszag-tang','mhd'],
 'lshape-fem':['lshape-fem','poisson-laplace'],
 'annular-viscous-mms':['annular-viscous-mms','variable-viscosity-vector'],
 'poisson-neumann':['poisson-neumann','poisson-laplace'],
 'poisson-robin':['poisson-robin','poisson-laplace'],
 'ale-nonuniform-transport':['ale-nonuniform-transport','ale-scalar-transport'],
 'cgrid-rotating-wave':['cgrid-rotating-wave','linear-rotating-shallow-water'],
 'srhd-collision':['srhd-collision','srhd'],
 'srmhd-alfven':['srmhd-alfven','srmhd'],
};
const editions=Object.fromEntries(json('catalog/atlas-depth-expansion.json').groups.map(g=>[g.id,g.edition]));
const base=g=>{assert.ok(editions[g],`Missing immutable edition for ${g}`);return `code/validated-examples/${editions[g]}/${g}/`;};
const sorted=x=>[...x].sort();
const incomingAudit={
 path:'numerical-methods-atlas/agent-kits/rkdg2d/index.html',
 baseline_sha256:'00d490af888c1505fa30c1705cf5b62681c777b454e6286dc5fcb7e4d7a0296a',
 incoming_sha256:'e25a90a20e07265648fb37a94a51cbdfb7a7e043f05ae42a4704e6b5e5736458',
 incoming_commit:'d43c5cab378bc053b908148d4c53f232ca9cb786',
};

test('the ten-item addition preserves 2755 baseline payload files, one audited incoming HTML replacement and all old primary/reference/model/method records',()=>{
 const proof=json('numerical-methods-atlas/validation/verification/2026-11-23-batch18-27-preservation.json');
 assert.equal(proof.passed,true);
 assert.equal(proof.baseline_commit,'a51543e8b54129e70670e184290c9b50b5bc0645');
 assert.equal(Object.keys(proof.protected_files).length,2756);
 assert.equal(proof.original_unchanged_files,2755);
 assert.equal(proof.baseline_exceptions.length,1);
 const exception=proof.baseline_exceptions[0];
 for(const[key,value]of Object.entries(incomingAudit))assert.equal(exception[key],value,key);
 assert.ok(typeof exception.reason==='string'&&exception.reason.trim());
 assert.notEqual(exception.baseline_sha256,exception.incoming_sha256);
 assert.equal(proof.protected_files[exception.path],exception.incoming_sha256);
 for(const[p,h]of Object.entries(proof.protected_files))assert.equal(sha(p),h,p);
 if(proof.unchanged_data_files!==undefined)assert.deepEqual(proof.unchanged_data_files,[]);
 assert.equal(proof.primary_figures.length,92);
 const gallery=json('numerical-methods-atlas/gallery/preview-manifest.json').items;
 for(const old of proof.primary_figures){assert.deepEqual(gallery.find(x=>x.id===old.id),old);assert.equal(sha(old.image.slice(1)),old.image_sha256);}
 const registry=json('numerical-methods-atlas/validation/releases.json');
 assert.equal(proof.releases.length,24);
 for(const old of proof.releases)assert.deepEqual(registry.releases.find(x=>x.group===old.group),old);
 const methods=json('catalog/atlas-methods.json').methods;
 assert.equal(Object.keys(proof.method_status).length,149);
 for(const[id,status]of Object.entries(proof.method_status))assert.equal(methods.find(x=>x.id===id)?.status,id==='slab-ewald'?'educational-example':status,id);
 const equations=json('catalog/atlas-equations.json').equations;
 assert.equal(Object.keys(proof.equation_formulas).length,50);
 for(const[id,formula]of Object.entries(proof.equation_formulas))assert.deepEqual(equations.find(x=>x.id===id)?.formula,formula,id);
 const references=json('catalog/atlas-reference-supplements.json').cases;
 assert.equal(proof.reference_supplements.length,15);
 for(const old of proof.reference_supplements)assert.deepEqual(references.find(x=>x.id===old.id),old);
 const concurrent=json('numerical-methods-atlas/validation/verification/2026-11-23-batch18-27-concurrent-preservation.json');
 assert.equal(concurrent.incoming_commit,incomingAudit.incoming_commit);
 assert.equal(concurrent.protected_files[exception.path],exception.incoming_sha256);
 const requiredIncoming=[
  'code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip',
  'code/validated-examples/2026-11-23/sem-fr/source-manifest.json',
  'code/validated-examples/2026-11-23/sem-fr/verification.json',
  'code/rkdg2d/2026-11-23-pilot1/atlas-rkdg-agent-pilot.zip',
  'code/rkdg2d/2026-11-23-pilot-audit3/verify_saved_portable.py',
  'numerical-methods-atlas/agent-kits/rkdg2d/results/2026-11-23-v1/manifest.json',
  'numerical-methods-atlas/agent-kits/rkdg2d/results/2026-11-23-v1/summary.json',
 ];
 for(const p of requiredIncoming)assert.match(concurrent.protected_files[p]??'',/^[0-9a-f]{64}$/,p);
 for(const[p,h]of Object.entries(concurrent.protected_files))assert.equal(sha(p),h,p);
 assert.equal(concurrent.release.group,'sem-fr');assert.equal(concurrent.release.tests,25);
 assert.deepEqual(sorted(concurrent.release.case_ids),['fr-periodic-advection','sem-poisson-2d']);
 assert.deepEqual(registry.releases.find(x=>x.group==='sem-fr'),concurrent.release);
});

test('all thirteen examples connect bilingual explanations, actual methods, models, reference cards, gallery previews and immutable code',()=>{
 const gallery=json('numerical-methods-atlas/gallery/index.json').items;
 const equations=json('numerical-methods-atlas/equations/index.json').equations;
 const references=json('numerical-methods-atlas/solutions/index.json').cases;
 const methods=json('catalog/atlas-methods.json').methods;
 const registry=json('numerical-methods-atlas/validation/releases.json').releases;
 assert.equal(Object.keys(mapping).length,13);
 for(const[g,,,ids]of plans){
  const release=registry.find(x=>x.group===g);assert.ok(release,g);assert.deepEqual(sorted(release.case_ids),sorted(ids));
  const manifest=json(base(g)+'source-manifest.json');
  for(const id of ids){
   const[pid,eid]=mapping[id];
   const entry=json(`numerical-methods-atlas/validation/${id}/index.json`);
   const problem=json(`numerical-methods-atlas/problems/${pid}/index.json`);
   assert.equal(entry.problem_id,pid);assert.equal(entry.group,g);
   for(const field of ['title','summary','assumptions','algorithm','validation','limits'])for(const lang of ['ja','en'])assert.ok(entry[field]?.[lang]?.trim(),`${id} ${field} ${lang}`);
   assert.ok(entry.references.length&&entry.references.every(r=>r.review_level&&r.url),id);
   assert.ok(problem.executions.some(x=>x.id===id),id);
   assert.ok(problem.references.some(binding=>references.some(ref=>ref.id===binding.id)),id);
   assert.deepEqual(sorted(entry.execution_navigation.methods.map(x=>x.id)),sorted(entry.method_ids));
   for(const method of entry.method_ids)assert.equal(methods.find(x=>x.id===method)?.status,'educational-example',`${id} ${method}`);
   assert.ok(entry.execution_navigation.equations.some(x=>x.id===eid),`${id} expected physical model`);
   for(const binding of entry.execution_navigation.equations){
    const model=equations.find(x=>x.id===binding.id);assert.ok(model?.related_problems.some(x=>x.id===pid));assert.ok(model.supplemental_execution_examples.some(x=>x.id===id));
   }
   assert.ok(entry.code_files.length);
   for(const name of entry.code_files){assert.ok(manifest.files[name],`${id} ${name}`);assert.equal(sha(base(g)+name),manifest.files[name]);assert.ok(entry.release.code_urls.includes(entry.release.base+name));}
   const figure=gallery.find(x=>x.id===pid);assert.ok(figure,pid);
   const link=figure.supplemental_execution_entries.find(x=>x.id===id);assert.ok(link?.preview,id);
   assert.equal(link.preview.file,entry.gallery_figure);assert.equal(sha(base(g)+'results/'+link.preview.file),link.preview.sha256);
   const png=bytes(base(g)+'results/'+link.preview.file);assert.equal(png.subarray(0,8).toString('hex'),'89504e470d0a1a0a');assert.ok(png.readUInt32BE(16)>=500&&png.readUInt32BE(20)>=200);
   for(const lang of ['ja','en']){
    for(const u of [entry.entry[lang],entry.reading[lang],link.url[lang]])assert.equal(new URL(u).origin,origin);
    const html=bytes(`numerical-methods-atlas/${lang}/read/validation-${g}/index.html`).toString();assert.ok(html.includes(id)&&html.includes('katex-mathml')&&!html.includes('katex-error'),`${id} ${lang}`);
   }
   assert.equal(new URL(entry.release.download).origin,origin);
  }
 }
});

test('all five packages bind the original fixed inputs, 133 distinct tests and 581 numerical decisions to actual complete reruns',()=>{
 let tests=0,gates=0;
 for(const[g,expectedTests,expectedGates,ids]of plans){
  const b=base(g),contract=json(b+'pre-run-contract.json'),result=json(b+'results/result.json'),v=json(b+'verification.json');
  assert.equal(contract.planned_tests,expectedTests);assert.equal(contract.planned_numerical_gates,expectedGates);assert.equal(contract.shared_pytest_plus_main_budget_seconds,120);
  assert.equal(v.tests,expectedTests);assert.equal(v.passed_tests,expectedTests);assert.equal(v.passed,true);assert.equal(v.all_cases_rerun,true);
  for(const field of ['returncode','failures','errors','skipped'])assert.equal(v[field],0);
  assert.equal(sha(b+v.archive.file),v.archive_sha256);assert.equal(result.passed,true);assert.equal(result.failure,null);assert.ok(result.termination);
  assert.equal(result.input_sha256,sha(b+'inputs.json'));assert.deepEqual(sorted(Object.keys(result.checks)),sorted(ids));assert.ok(Object.values(result.checks).every(x=>x===true));
  assert.deepEqual(sorted(result.cases.map(c=>c.id)),sorted(ids));
  const actual=result.cases.reduce((n,c)=>n+Object.keys(c.checks).length,0);assert.equal(actual,expectedGates);
  for(const c of result.cases){assert.equal(c.passed,true);assert.ok(Object.values(c.checks).every(x=>x===true));assert.ok(Object.keys(c.metrics).length&&Object.keys(c.records).length);}
  for(const[p,h]of Object.entries(contract.files_sha256))assert.equal(sha(b+p),h,`${g} ${p}`);
  tests+=expectedTests;gates+=actual;
 }
 assert.equal(tests,133);assert.equal(gates,581);
});

test('the archived backend, reference-timestamp and resolution failures remain visible with unchanged physical acceptance',()=>{
 const i=base('instability-growth'),initial=json(i+'history/reference-attempt-01/results/result.json');assert.equal(initial.passed,false);assert.equal(initial.termination,'reference_failure');assert.equal(initial.failure.type,'RuntimeWarning');
 const oldContract=json(i+'history/reference-attempt-01/pre-run-contract.json'),nowContract=json(i+'pre-run-contract.json');
 for(const name of ['inputs.json','acceptance.json'])assert.equal(nowContract.files_sha256[name],oldContract.files_sha256[name]);
 const m=base('mesh-boundary');assert.equal(json(m+'attempts/01/results/result.json').passed,false);
 for(const name of ['inputs.json','acceptance.json','fem.py','boundary.py','references/fields.py'])assert.equal(sha(m+name),sha(m+'attempts/01/source/'+name));
 assert.equal(sha(m+'test_geometry.py'),sha(m+'attempts/01/source/archived_test_geometry.py'));
 const preservation=json(m+'execution-receipts/02-backend-and-preservation-diagnostic.json');assert.equal(preservation.passed,true);assert.equal(preservation.lshape_files,12);assert.ok(preservation.lshape.every(x=>x.all_arrays_bitwise_equal));
 const r=base('relativistic'),old=json(r+'attempts/01/results/result.json');assert.equal(old.passed,false);assert.equal(old.cases.reduce((n,c)=>n+Object.values(c.checks).filter(x=>x===true).length,0),109);
 assert.equal(sha(r+'acceptance.json'),sha(r+'attempts/01/source/acceptance.json'));
 const h=base('mhd-transport')+'references/',failed=json(h+'history/attempt-01-failed-qualification.json'),qualified=json(h+'reference-qualification.json'),qc=json(h+'qualification-contract.json');
 assert.equal(failed.passed,false);assert.equal(qualified.passed,true);assert.equal(qualified.pde_rerun_performed,false);assert.equal(qc.physical_error_bounds_unchanged,true);assert.equal(qc.declared_after_six_reference_pde_executions,true);
 assert.equal(failed.qualification.checks.length,31);assert.equal(failed.qualification.checks.filter(x=>!x.passed).length,6);assert.equal(qualified.qualification.checks.length,31);assert.ok(qualified.qualification.checks.every(x=>x.passed));
 const physical=failed.qualification.checks.filter(x=>!x.name.includes('exact requested output times'));assert.equal(physical.length,25);
 for(const old of physical){const current=qualified.qualification.checks.find(x=>x.name===old.name);assert.ok(current,old.name);assert.deepEqual(current.bound,old.bound);assert.equal(current.passed,true);}
 assert.equal(qc.field_path_map.length,6);
 for(const field of qc.field_path_map){assert.equal(sha(h+field.single_public_copy),field.sha256);const original=failed.records.find(x=>x.file===field.single_public_copy);assert.equal(original.sha256,field.sha256);}
});

test('the public output policy rejects incomplete envelopes and the retained real missing-CSV release before any new freeze',()=>{
 const code=String.raw`
import copy,importlib.util,json,pathlib
p=pathlib.Path('scripts/package-depth-examples.py');s=importlib.util.spec_from_file_location('packager',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
registry=json.loads(pathlib.Path('numerical-methods-atlas/validation/releases.json').read_text())
groups=['instability-growth','mhd-transport','mesh-boundary','moving-waves','relativistic']
rejected=0;csv_groups=0
for group in groups:
 release=next(r for r in registry['releases'] if r['group']==group)
 base=pathlib.Path('code/validated-examples')/release['edition']/group
 good=json.loads((base/'results/result.json').read_text());ids=release['case_ids'];digest=good['input_sha256']
 m.validate_result_envelope(good,ids,digest)
 assert m.validate_generated_csv(base/'results'),group+' has no policy-qualified generated CSV'
 csv_groups+=1
 variants=[]
 for key in ['termination','checks']:
  bad=copy.deepcopy(good);del bad[key];variants.append(bad)
 bad=copy.deepcopy(good);bad['checks'].pop(ids[0]);variants.append(bad)
 bad=copy.deepcopy(good);bad['cases'][0]['records']=[];variants.append(bad)
 bad=copy.deepcopy(good);bad['cases'][0]['checks'][next(iter(bad['cases'][0]['checks']))]=False;variants.append(bad)
 for bad in variants:
  try:m.validate_result_envelope(bad,ids,digest)
  except ValueError:rejected+=1
  else:raise AssertionError('incomplete/failed result accepted for '+group)
assert rejected==25 and csv_groups==5
# This was a complete scientific result whose original immutable packet lacked
# CSV output. Keep exercising the actual retained failure, not an empty mock.
retained=pathlib.Path('code/validated-examples/2026-11-23/instability-growth/results')
assert (retained/'result.json').is_file() and json.loads((retained/'result.json').read_text())['passed'] is True
assert not list(retained.glob('*.csv'))
try:m.validate_generated_csv(retained)
except ValueError as error:assert 'No generated CSV outputs' in str(error)
else:raise AssertionError('retained original missing-CSV packet would be frozen again')
print('five actual envelopes and CSV sets accepted;25 incomplete/failed variants and retained missing-CSV release rejected without executing PDEs')
`;
 assert.match(execFileSync('python3',['-B','-c',code],{cwd:root,encoding:'utf8'}),/five actual envelopes and CSV sets accepted;25 incomplete\/failed variants and retained missing-CSV release rejected/);
});
