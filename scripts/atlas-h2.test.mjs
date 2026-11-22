import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const root=new URL('../',import.meta.url);
const bytes=p=>readFileSync(new URL(p,root));
const text=p=>bytes(p).toString('utf8');
const json=p=>JSON.parse(text(p));
const sha=p=>createHash('sha256').update(bytes(p)).digest('hex');
const base='code/molecular-hf/2026-11-22/';
const input=json(base+'inputs.json');
const result=json(base+'results/result.json');
const reference=json(base+'reference-pyscf.json');

test('H2 bilingual reading exposes the actual frozen measurements, rendered equations and bounded source-review claims',()=>{
 const headings=[];
 for(const lang of ['ja','en']){
  const route=`numerical-methods-atlas/${lang}/read/h2-hf/`;
  const record=json(route+'index.json'),html=text(route+'index.html'),markdown=text(route+'index.md');
  assert.equal(record.locale,lang);assert.equal(record.execution_example,'h2-rhf');
  assert.equal(record.url,`https://hrkoyama.github.io/${route}`);
  assert.deepEqual(record.measurements,result.metrics);
  for(const [path,hash] of Object.entries(record.source_sha256))assert.equal(sha(path),hash,path);
  assert.ok(html.includes('katex-mathml')&&!html.includes('katex-error'));
  for(const id of ['geometry-and-basis-results','nested-basis-target','scf-tolerance-results','run-and-check','sources'])assert.ok(html.includes(`id="${id}"`));
  assert.ok(html.includes('/code-and-data/examples/h2-rhf/'));
  assert.ok(html.includes('/code/molecular-hf/2026-11-22/reference-pyscf.json'));
  assert.ok(markdown.includes('$$')&&markdown.includes('python run.py --input inputs.json --output output'));
  const normalize=s=>s.replace(/e([+-])0+/g,'e$1');
  for(const key of ['max_reference_energy_error','last_two_basis_changes_max'])assert.ok(normalize(html).includes(String(Number(result.metrics[key].toPrecision(12)))),key);
  headings.push(record.headings.map(h=>h.id));
  assert.ok(record.references.some(r=>r.doi==='10.1103/RevModPhys.23.69'));
  assert.ok(record.references.some(r=>r.doi==='10.1063/1.1672392'&&r.review_level==='metadata'));
  assert.ok(record.references.some(r=>r.id==='bse-sto3g-v1'&&r.source.includes('version=1')));
 }
 assert.deepEqual(headings[0],headings[1]);
 const english=text('numerical-methods-atlas/en/read/h2-hf/index.html');
 assert.match(english,/s-only/);assert.match(english,/complete-basis/);assert.match(english,/dissociation/);
 assert.match(english,/Frobenius/);assert.match(english,/full RHF\/UHF stability analysis/);
});

test('one H2 problem contains 24 geometry/basis calculations with independent finite-basis energies and explicit SCF histories',()=>{
 assert.equal(result.case,'h2-rhf');assert.equal(result.passed,true);
 assert.equal(result.input_sha256,sha(base+'inputs.json'));assert.equal(reference.input_sha256,result.input_sha256);
 assert.equal(result.reference_sha256,sha(base+'reference-pyscf.json'));
 assert.equal(input.bonds_bohr.length,3);assert.equal(input.basis_definitions.length,8);assert.equal(result.cases.length,24);
 const key=r=>`${r.bond_bohr}/${r.basis_id}`;
 const refs=new Map(reference.cases.map(r=>[key(r),r]));
 assert.equal(refs.size,24);
 for(const row of result.cases){
  const ref=refs.get(key(row));assert.ok(ref,key(row));assert.equal(row.nbf,ref.nbf);
  assert.equal(row.reference_energy,ref.energy_total);
  assert.equal(row.energy_error,Math.abs(row.energy_total-ref.energy_total));
  assert.ok(row.energy_error<=input.acceptance.max_reference_energy_error);
  assert.equal(row.converged,true);assert.equal(row.termination,'converged');
  assert.equal(row.trace.length,row.iterations);
  const final=row.trace.at(-1);
  assert.equal(final.energy_total,row.energy_total);assert.equal(final.scf_commutator_norm,row.scf_commutator_norm);
  assert.ok(final.scf_commutator_norm<=input.scf.residual_tolerance);
  assert.ok(final.density_change<=input.scf.density_tolerance);assert.ok(final.delta_energy<=input.scf.energy_tolerance);
 }
 assert.equal(result.basis_refinement.length,3);
 for(const row of result.basis_refinement){
  assert.equal(row.target,input.basis_convergence_target.two_successive_additions_max_change);
  assert.equal(row.last_two_changes_max,Math.max(...row.energy_changes.slice(-2).map(Math.abs)));
  assert.equal(row.target_reached,true);assert.ok(row.last_two_changes_max<=row.target);
 }
 assert.match(input.scope,/not complete-basis/);assert.match(reference.scope,/not a correlated/);
 const referenceCode=text(base+'reference_pyscf.py');
 assert.match(referenceCode,/from pyscf import/);assert.ok(!/^\s*(?:from|import)\s+(?:molecular_hf|run)\b/m.test(referenceCode));
 const problems=json('catalog/atlas-test-problems.json').problems;
 assert.equal(problems.filter(p=>p.id==='h2-rhf').length,1);
 assert.ok(!problems.some(p=>/^h2-rhf-(?:sto|nested|bond)/.test(p.id)));
});

test('molecular HF augments atomic method links while DFT and unrelated applications remain reading-only routes',()=>{
 const methods=json('numerical-methods-atlas/methods/index.json').methods;
 for(const id of ['hartree-fock','scf']){
  const m=methods.find(m=>m.id===id);assert.ok(m,id);
  assert.deepEqual(m.quantum_examples,['helium-ground-state']);
  assert.equal(m.code_base,'https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/');
  assert.ok(m.code_urls.some(url=>url.endsWith('/atomic_radial.py')));
  assert.ok(m.code_urls.some(url=>url.endsWith('/molecular_hf.py')));
  assert.equal(m.molecular_release.release.family,'molecular-hf');
  assert.ok(m.execution_examples.some(e=>e.id==='helium-ground-state'));
  assert.ok(m.execution_examples.some(e=>e.id==='h2-rhf'));
 }
 const ks=methods.find(m=>m.id==='kohn-sham-dft');
 assert.ok(!ks.execution_examples.some(e=>e.id==='h2-rhf'));
 assert.ok(!ks.molecular_examples?.length);
 const goals=json('catalog/atlas-goals.json').goals;
 const dft=goals.find(g=>g.id==='molecular-dft');assert.equal(dft.availability,'reading-only');assert.deepEqual(dft.examples,[]);
 const hf=goals.find(g=>g.id==='molecular-hf');assert.deepEqual(hf.examples,['h2-rhf']);
 const resource=hf.resources.find(r=>r.execution_examples.some(e=>e.id==='h2-rhf'));
 assert.equal(resource.status,'educational-example');assert.ok(resource.code_urls.length&&resource.test_urls.length);
 assert.match(hf.scope.en,/s-type/);assert.match(hf.scope.en,/does not validate.*DFT/);
});
