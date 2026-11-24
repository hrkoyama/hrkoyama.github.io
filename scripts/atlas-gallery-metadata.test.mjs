// Small metadata fixtures only. Never solve, plot or extract a real release.
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const root=new URL('../',import.meta.url);
// Private authoring overrides select the exact proposed source/config before
// installation; normal CI uses the checked-in publisher files below.
const primer=process.env.ATLAS_GALLERY_PRIMER_SOURCE||fileURLToPath(new URL('scripts/prime-atlas-gallery-metadata.py',root));
const pipeline=process.env.ATLAS_GALLERY_PRIMER_PIPELINE||fileURLToPath(new URL('catalog/site-build-pipeline.json',root));

test('saved gallery metadata appends idempotently and rejects stale or unsafe sources',()=>{
 const output=execFileSync(process.env.ATLAS_INDEX_PYTHON||'python3',['-B','-c',String.raw`
import contextlib,hashlib,importlib.util,io,json,struct,sys,tempfile,types,unittest,zlib
from pathlib import Path
from unittest.mock import patch
source=Path(sys.argv[1]);spec=importlib.util.spec_from_file_location('gallery_primer',source)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def chunk(k,data):return struct.pack('>I',len(data))+k+data+struct.pack('>I',zlib.crc32(k+data)&0xffffffff)
png=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',2,1,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(b'\0'+b'\0'*6))+chunk(b'IEND',b'')
class MetadataFixtures(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory(prefix='atlas-gallery-metadata-');self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)
  r=self.root;self.gallery=r/'numerical-methods-atlas/gallery';self.gallery.mkdir(parents=True)
  (r/'scripts').mkdir();(r/'scripts/prime-atlas-gallery-metadata.py').write_text('# fixture producer\n')
  (r/'assets').mkdir();(r/'assets/old.png').write_bytes(png)
  self.base=r/'code/validated-examples/2026-11-24/fixture';self.base.mkdir(parents=True)
  self.case={'id':'new','limits':{'ja':'制限','en':'Limits'},'gallery_figure':'new-preview.png','additional_figures':[{'file':'new-preview.png','caption':{'ja':'保存図','en':'Saved figure'}}]}
  for name,value in [('cases.json',[self.case]),('inputs.json',{'fixed':1}),('acceptance.json',{'limit':1}),('pre-run-contract.json',{'fixed':True}),('results/result.json',{'fixture_only':True})]:dump(self.base/name,value)
  for name in ['new.png','new-preview.png']:(self.base/'results'/name).write_bytes(png)
  self.manifest={'group':'fixture','version':'2026-11-24','files':{p.relative_to(self.base).as_posix():digest(p) for p in self.base.rglob('*') if p.is_file()}}
  dump(self.base/'source-manifest.json',self.manifest)
  (self.base/'fixture.zip').write_bytes(b'metadata-only fixture, not a real ZIP')
  self.verification={'group':'fixture','edition':'2026-11-24','passed':True,'all_cases_rerun':True,'failures':0,'errors':0,'skipped':0,'source_manifest_sha256':digest(self.base/'source-manifest.json'),'archive':{'file':'fixture.zip','sha256':digest(self.base/'fixture.zip')}}
  dump(self.base/'verification.json',self.verification)
  self.catalog={'reviewed_on':'2026-11-24','items':[{'id':'old','kind':'image','source':'/assets/old.png','caption':{'ja':'元の図','en':'Old figure'}},{'id':'new','kind':'image','source':'/code/validated-examples/2026-11-24/fixture/results/new-preview.png','caption':{'ja':'保存図 表示条件','en':'Saved figure Display scope'}}]}
  dump(r/'catalog/atlas-gallery.json',self.catalog);dump(r/'catalog/atlas-test-problems.json',{'problems':[{'id':'old'},{'id':'new'}]})
  dump(r/'catalog/atlas-depth-expansion.json',{'groups':[{'id':'fixture','edition':'2026-11-24'}],'case_problem_ids':{'new':'new'},'case_notes':{'new':{'ja':'制限 表示条件','en':'Limits Display scope'}}})
  dump(self.gallery/'calculations.json',{'historical_numerics':'unchanged'});dump(self.gallery/'verification.json',{'historical_tests':20})
  self.old={'schema_version':1,'items':[{'id':'old','image':'/assets/old.png','image_sha256':digest(r/'assets/old.png'),'width':2,'height':1,'source_kind':'existing-figure','caption':self.catalog['items'][0]['caption']}],'source_sha256':{'assets/old.png':digest(r/'assets/old.png'),'catalog/atlas-gallery.json':'0'*64,'catalog/atlas-test-problems.json':'1'*64,'catalog/atlas-depth-expansion.json':'2'*64},'calculations_sha256':digest(self.gallery/'calculations.json'),'metadata_updates':[{'scope':'Retained prior history'}]}
  dump(self.gallery/'preview-manifest.json',self.old);self.calls=0
 def load(self,root,group,edition):
  self.assertEqual((Path(root),group,edition),(self.root,'fixture','2026-11-24'));self.calls+=1
  # Only the canonical-loader output INTERFACE is mocked. These fixtures make
  # no claim that this fake package or numerical results pass the real loader.
  return {'manifest':self.manifest,'verification':self.verification,'metadata':[self.case]}
 def assemble(self):return module.assemble(self.root,load_group=self.load)
 def test_append_idempotence_and_only_manifest_write(self):
  before={p.relative_to(self.root).as_posix():p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
  with patch.dict(sys.modules,{'atlas_depth_release':types.SimpleNamespace(load_depth_group=self.load)}),contextlib.redirect_stdout(io.StringIO()):module.prime(self.root)
  once=(self.gallery/'preview-manifest.json').read_bytes();result=json.loads(once)
  self.assertEqual(result['items'][:1],self.old['items']);self.assertEqual(result['items'][1]['image'],self.catalog['items'][1]['source']);self.assertEqual(self.calls,1)
  self.assertEqual(result['metadata_updates'][:1],self.old['metadata_updates']);self.assertEqual(result['metadata_updates'][-1]['added_primary_ids'],['new']);self.assertNotIn('recorded_at_utc',result['metadata_updates'][-1])
  self.assertEqual(result['items'][1]['width'],2);self.assertEqual(result['items'][1]['height'],1)
  for name,value in before.items():
   if name!='numerical-methods-atlas/gallery/preview-manifest.json':self.assertEqual((self.root/name).read_bytes(),value,name)
  with patch.dict(sys.modules,{'atlas_depth_release':types.SimpleNamespace(load_depth_group=self.load)}),contextlib.redirect_stdout(io.StringIO()):module.prime(self.root)
  self.assertEqual((self.gallery/'preview-manifest.json').read_bytes(),once);self.assertFalse((self.gallery/'preview-manifest.json.metadata.tmp').exists())
 def test_new_scientific_plot_is_not_implicitly_generated(self):
  self.catalog['items'][1]['kind']='computed-preview';dump(self.root/'catalog/atlas-gallery.json',self.catalog)
  with self.assertRaises(ValueError):self.assemble()
 def test_old_caption_change_is_not_accepted(self):
  self.catalog['items'][0]['caption']['en']='Changed';dump(self.root/'catalog/atlas-gallery.json',self.catalog)
  with self.assertRaises(ValueError):self.assemble()
 def test_stale_old_image_is_rejected_before_any_write(self):
  before=(self.gallery/'preview-manifest.json').read_bytes();(self.root/'assets/old.png').write_bytes(b'stale')
  with self.assertRaisesRegex(ValueError,'Stale existing'):self.assemble()
  self.assertEqual((self.gallery/'preview-manifest.json').read_bytes(),before)
 def test_saved_input_mutation_is_rejected(self):
  dump(self.base/'inputs.json',{'fixed':2})
  with self.assertRaises(ValueError):self.assemble()
 def test_PNG_CRC_checked_even_with_matching_manifest_hash(self):
  f=self.base/'results/new-preview.png';data=bytearray(f.read_bytes());data[-1]^=1;f.write_bytes(data)
  self.manifest['files']['results/new-preview.png']=digest(f);dump(self.base/'source-manifest.json',self.manifest);self.verification['source_manifest_sha256']=digest(self.base/'source-manifest.json');dump(self.base/'verification.json',self.verification)
  with self.assertRaisesRegex(ValueError,'CRC'):self.assemble()
 def test_unsafe_image_member_is_rejected(self):
  self.catalog['items'][1]['source']='/code/validated-examples/2026-11-24/fixture/../escape.png';dump(self.root/'catalog/atlas-gallery.json',self.catalog)
  with self.assertRaises(ValueError):self.assemble()
 def test_canonical_loader_failure_is_not_bypassed(self):
  before=(self.gallery/'preview-manifest.json').read_bytes()
  def reject(*args):raise AssertionError('Invalid canonical package')
  with patch.dict(sys.modules,{'atlas_depth_release':types.SimpleNamespace(load_depth_group=reject)}),self.assertRaises(AssertionError):module.prime(self.root)
  self.assertEqual((self.gallery/'preview-manifest.json').read_bytes(),before)
suite=unittest.defaultTestLoader.loadTestsFromTestCase(MetadataFixtures);result=unittest.TextTestRunner(verbosity=1).run(suite)
assert result.wasSuccessful() and result.testsRun==8
print('Eight metadata-only fixtures passed; no scientific package or solver executed.')
`,primer],{encoding:'utf8',timeout:20000,maxBuffer:4*1024*1024});
 assert.match(output,/Eight metadata-only fixtures passed/);
});

test('saved-image priming precedes strict reverse-route consumers',()=>{
 const rows=JSON.parse(readFileSync(pipeline)).stages;
 const index=id=>rows.findIndex(row=>row.id===id);
 const p=index('prime-atlas-gallery-metadata'),d=index('build-atlas-depth-examples'),r=index('build-atlas-detailed-reading');
 assert.ok(r>=0&&r<p&&p<d);
 assert.deepEqual(rows[p].depends_on,['build-atlas-detailed-reading']);
 assert.deepEqual(rows[d].depends_on,['prime-atlas-gallery-metadata']);
 assert.equal(rows[p].script,'scripts/prime-atlas-gallery-metadata.py');
 const source=readFileSync(primer,'utf8');assert.match(source,/from atlas_depth_release import load_depth_group/);
 assert.doesNotMatch(source,/import numpy|import matplotlib|from PIL|subprocess|render-atlas-gallery/);
});
