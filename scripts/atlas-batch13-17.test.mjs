import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
const root=new URL('../',import.meta.url);
const bytes=p=>readFileSync(new URL(p,root));
const json=p=>JSON.parse(bytes(p));
const sha=p=>createHash('sha256').update(bytes(p)).digest('hex');
const cases=[['weno-critical','weno-critical-epsilon','advection-sine'],['shallow-water','swashes-topography','swashes-topography'],['shallow-water','dry-bed-dam-break','dry-bed-dam-break'],['wall-flow','cavity-ghia-re100','lid-driven-cavity'],['wall-flow','wall-manufactured','wall-manufactured']];
const editions=Object.fromEntries(json('catalog/atlas-depth-expansion.json').groups.map(g=>[g.id,g.edition]));
const base=g=>`code/validated-examples/${editions[g]}/${g}/`;

test('the five-item addition preserves all prior distribution bytes, primary pictures, reference cards and method states',()=>{
 const proof=json('numerical-methods-atlas/validation/verification/2026-11-23-batch13-17-preservation.json');assert.equal(proof.passed,true);
 for(const[p,h]of Object.entries(proof.protected_files))assert.equal(sha(p),h,p);
 for(const[p,h]of Object.entries(proof.unchanged_data_files))assert.equal(sha(p),h,p);
 const gallery=json('numerical-methods-atlas/gallery/preview-manifest.json').items;
 for(const old of proof.primary_figures){assert.deepEqual(gallery.find(x=>x.id===old.id),old);assert.equal(sha(old.image.slice(1)),old.image_sha256);}
 const registry=json('numerical-methods-atlas/validation/releases.json');
 for(const old of proof.releases)assert.deepEqual(registry.releases.find(x=>x.group===old.group),old);
 const methods=json('catalog/atlas-methods.json').methods;for(const[id,status]of Object.entries(proof.method_status))assert.equal(methods.find(x=>x.id===id).status,id==='slab-ewald'?'educational-example':status);
 const eq=json('catalog/atlas-equations.json').equations;for(const[id,formula]of Object.entries(proof.equation_formulas))assert.deepEqual(eq.find(x=>x.id===id).formula,formula);
 const refs=json('catalog/atlas-reference-supplements.json').cases;for(const old of proof.reference_supplements)assert.deepEqual(refs.find(x=>x.id===old.id),old);
 const concurrent=json('numerical-methods-atlas/validation/verification/2026-11-23-batch13-17-concurrent-preservation.json');
 assert.equal(concurrent.incoming_commit,'11ba7a20076f052a569091ef976217f07341c3ba');
 for(const[p,h]of Object.entries(concurrent.protected_files))assert.equal(sha(p),h,p);
 assert.deepEqual(registry.releases.find(x=>x.group==='level-set'),concurrent.release);
 assert.deepEqual(json('catalog/atlas-gallery.json').items.find(x=>x.id==='level-set-circle'),concurrent.primary_figure);
 assert.deepEqual(gallery.find(x=>x.id==='level-set-circle'),concurrent.preview_record);
});

test('all five independently qualified examples connect figures, models, references, actual methods and runnable archives in both languages',()=>{
 const gallery=json('numerical-methods-atlas/gallery/index.json');
 const equations=json('numerical-methods-atlas/equations/index.json').equations;
 const references=json('numerical-methods-atlas/solutions/index.json').cases;
 const registry=json('numerical-methods-atlas/validation/releases.json');
 for(const[g,id,pid]of cases){
  const entry=json(`numerical-methods-atlas/validation/${id}/index.json`);assert.equal(entry.problem_id,pid);
  const problem=json(`numerical-methods-atlas/problems/${pid}/index.json`);assert.ok(problem.executions.some(x=>x.id===id));assert.ok(problem.references.length>0);
  const figure=gallery.items.find(x=>x.id===pid);assert.ok(figure.supplemental_execution_entries.some(x=>x.id===id));
  const release=registry.releases.find(x=>x.group===g);assert.ok(release.case_ids.includes(id));
  const receipt=json(base(g)+'verification.json');assert.equal(receipt.passed,true);assert.equal(receipt.all_cases_rerun,true);assert.equal(sha(base(g)+receipt.archive.file),receipt.archive_sha256);
  assert.ok(entry.execution_navigation.equations.length);
  for(const binding of entry.execution_navigation.equations){const model=equations.find(x=>x.id===binding.id);assert.ok(model.related_problems.some(x=>x.id===pid));assert.ok(model.supplemental_execution_examples.some(x=>x.id===id));}
  assert.ok(problem.references.some(binding=>references.some(ref=>ref.id===binding.id)));
  const preview=bytes(base(g)+`results/${id}-preview.png`);assert.equal(preview.subarray(1,4).toString(),'PNG');assert.ok(preview.readUInt32BE(16)>=500&&preview.readUInt32BE(20)>=200);
  for(const lang of ['ja','en']){const html=bytes(`numerical-methods-atlas/${lang}/read/validation-${g}/index.html`).toString();assert.ok(html.includes(id)&&html.includes('katex-mathml')&&!html.includes('katex-error'));}
 }
});

test('the new releases retain fixed protocols, every numerical decision and all failed-attempt history',()=>{
 for(const[g,tests,gates]of [['weno-critical',36,217],['shallow-water',31,109],['wall-flow',22,94]]){
  const b=base(g),contract=json(b+'pre-run-contract.json'),r=json(b+'results/result.json'),v=json(b+'verification.json');
  assert.equal(contract.planned_tests,tests);assert.equal(contract.planned_numerical_gates,gates);assert.equal(v.tests,tests);assert.equal(r.passed,true);assert.equal(r.failure,null);
  assert.equal(r.cases.reduce((n,c)=>n+Object.keys(c.checks).length,0),gates);assert.ok(r.cases.every(c=>c.passed&&Object.values(c.checks).every(x=>x===true)));
  for(const[p,h]of Object.entries(contract.files_sha256))assert.equal(sha(b+p),h,p);
 }
 const b=base('shallow-water');assert.equal(sha(b+'acceptance.json'),sha(b+'attempts/01/source/acceptance.json'));
 for(const n of ['01','02','03']){const old=json(b+`attempts/${n}/source/results/result.json`);assert.equal(old.passed,false);}
 const w=base('wall-flow');for(const n of ['inputs.json','acceptance.json','wall_flow.py'])assert.equal(sha(w+n),sha(w+'attempts/01/source/'+n));
});

test('packaging applies the actual public result contract and rejects the retained incomplete wall envelope',()=>{
 const code=String.raw`
import importlib.util,json,pathlib
p=pathlib.Path('scripts/package-depth-examples.py');s=importlib.util.spec_from_file_location('packager',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
d=json.loads(pathlib.Path('catalog/atlas-depth-expansion.json').read_text());edition=next(g['edition'] for g in d['groups'] if g['id']=='wall-flow')
base=pathlib.Path('code/validated-examples')/edition/'wall-flow'
good=json.loads((base/'results/result.json').read_text());ids=[c['id'] for c in good['cases']]
m.validate_result_envelope(good,ids,good['input_sha256'])
bad=json.loads((base/'attempts/02/source/results/result.json').read_text())
try:m.validate_result_envelope(bad,ids,bad['input_sha256'])
except ValueError:pass
else:raise AssertionError('incomplete old wall result would be frozen again')
print('actual public envelope policy is enforced before freezing')
`;
 assert.match(execFileSync('python3',['-B','-c',code],{cwd:root,encoding:'utf8'}),/enforced before freezing/);
});
