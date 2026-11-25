import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const root=new URL('../../',import.meta.url),json=p=>JSON.parse(readFileSync(new URL(p,root)));
export const mdCase='two-state-bo-cp-ou',mdBase='https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/';
const relative='code/validated-examples/2026-11-25/quantum-small/';
const manifestBytes=readFileSync(new URL(relative+'source-manifest.json',root));
export const mdManifestSHA=createHash('sha256').update(manifestBytes).digest('hex');
assert.equal(mdManifestSHA,'b13b8873c5f74ec3b1b25207ed145cf7ece1ceec2e0e254a9b7f18e93f73350c');
const metadata=json(relative+'cases.json');
export const mdMetadata=(Array.isArray(metadata)?metadata:metadata.cases).find(c=>c.id===mdCase);
export function assertScopedMDMethod(method){
  assert.equal(method.status,'educational-example');
  assert.deepEqual(method.depth_release.case_ids,[mdCase]);
  assert.equal(method.depth_release.group,'quantum-small');
  assert.equal(method.depth_release.code_edition,'2026-11-25');
  assert.equal(method.depth_release.code_manifest,mdBase+'source-manifest.json');
  assert.deepEqual(method.execution_examples.map(e=>e.id),[mdCase]);
  assert.ok(method.code_urls.includes(mdBase+'coupled_md.py'));
  assert.ok(method.code_urls.every(url=>url.startsWith(mdBase)));
  assert.ok(method.test_urls.length&&method.test_urls.every(url=>url.startsWith(mdBase)));
  assert.ok(!method.periodic_examples?.length&&!method.periodic_release);
  assert.ok(!method.force_examples?.length&&!method.force_release);
  assert.deepEqual(method.depth_release.examples.map(e=>e.id),[mdCase]);
  assert.deepEqual(method.depth_release.examples[0].limits,mdMetadata.limits);
  assert.ok(method.supplemental_scope_profiles.some(p=>p.release.group==='quantum-small'&&p.release.edition==='2026-11-25'&&p.release.case_ids.includes(mdCase)));
}
export function assertChapterMDScope(record){
  assert.equal(record.reading_only_methods_scope,'chapter-local');
  assert.deepEqual(record.reading_only_methods,['born-oppenheimer-md','car-parrinello-md']);
  assert.ok(['periodic-he-dft','periodic-he-forces'].includes(record.execution_example));
  assert.equal(record.scoped_educational_examples.length,1);
  const example=record.scoped_educational_examples[0];
  assert.equal(example.id,mdCase);assert.equal(example.scope,'two-state-educational-model');
  assert.equal(example.entry,'https://hrkoyama.github.io/numerical-methods-atlas/validation/'+mdCase+'/');
  assert.equal(example.code,mdBase+'coupled_md.py');
  assert.equal(example.source_manifest,mdBase+'source-manifest.json');assert.equal(example.source_manifest_sha256,mdManifestSHA);
  assert.deepEqual(example.title,mdMetadata.title);assert.deepEqual(example.assumptions,mdMetadata.assumptions);assert.deepEqual(example.limits,mdMetadata.limits);
}
