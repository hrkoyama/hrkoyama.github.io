import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';
const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root),'utf8');
const json=p=>JSON.parse(read(p));
const hash=bytes=>createHash('sha256').update(bytes).digest('hex');
const config=json('catalog/atlas-agent-kits.json');
const base=config.route.slice(1);

test('public RKDG instructions and manifest bind the exact immutable downloadable kit',()=>{
 const manifest=json(base+'manifest.json'),published=json(base+'index.json');
 const zip=readFileSync(new URL(config.archive.slice(1),root));
 assert.equal(hash(zip),manifest.archive.sha256);
 assert.equal(zip.length,manifest.archive.bytes);
 assert.equal(published.archive_sha256,manifest.archive.sha256);
 assert.equal(manifest.archive.url,'https://hrkoyama.github.io'+config.archive);
 assert.equal(manifest.candidate_sha256,config.source_sha256);
 for(const lang of ['ja','en']){
  const filename=lang==='ja'?'TESTSET.md':'TESTSET-en.md';
  const guide=readFileSync(new URL(base+filename,root));
  assert.equal(hash(guide),manifest.guides[lang].sha256);
  assert.equal(manifest.guides[lang].url,'https://hrkoyama.github.io'+config.route+filename);
  assert.ok(guide.toString().includes('SHA256SUMS.txt'));
  assert.ok(guide.toString().includes(manifest.commands.smoke));
  assert.ok(guide.toString().includes('--verify-only'));
  assert.doesNotMatch(guide.toString(),/公開準備用ドラフト|公開URLは未設定|\/Users\/|\/private\//);
 }
});

test('known supplemental failure and execution boundaries remain visible in both languages',()=>{
 const manifest=json(base+'manifest.json'),html=read(base+'index.html');
 assert.equal(manifest.original_48_passed,true);assert.equal(manifest.waveform_4_passed,true);
 assert.equal(manifest.reflection_6_passed,false);assert.equal(manifest.reflection_passed_count,5);
 assert.equal(json(base+'evidence/original-verdict.json').passed,true);
 assert.equal(json(base+'evidence/waveform-verdict.json').diagnostic_checks,4);
 assert.equal(json(base+'evidence/reflection-verdict.json').passed,false);
 for(const lang of ['ja','en']){
  const section=html.match(new RegExp('<section data-site-language="'+lang+'"[^>]*>([\\s\\S]*?)</main>'))?.[1];
  assert.ok(section);
  assert.ok(section.includes(lang==='ja'?'6件中5件':'five of six'));
  assert.ok(section.includes(lang==='ja'?'PDEの再実行とは分け':'separately from fresh PDE execution'));
  assert.ok(section.includes(lang==='ja'?'未実施':'have not been run'));
 }
 for(const figure of config.figures)assert.ok(existsSync(new URL(base+'figures/'+figure.file,root)));
 assert.equal(json('catalog/atlas-methods.json').methods.length,147);
 assert.equal(json('catalog/atlas-execution-examples.json').examples.length,22);
 assert.equal(json('catalog/atlas-test-problems.json').problems.length,83);
});

test('agent kit is reachable from the real static and runtime home and code guide',()=>{
 const rendered=JSON.parse(execFileSync(process.execPath,['scripts/render-atlas-landing.mjs'],{cwd:fileURLToPath(root),encoding:'utf8'}));
 const staticHome=read('numerical-methods-atlas/index.html'),guide=read('numerical-methods-atlas/code-and-data/index.html');
 for(const lang of ['ja','en'])for(const html of [rendered[lang],staticHome,guide])assert.ok(html.includes(config.route+'?lang='+lang));
 for(const file of ['TESTSET.md','TESTSET-en.md','manifest.json'])assert.ok(read('llms.txt').includes('https://hrkoyama.github.io'+config.route+file));
 assert.ok(read('scripts/refresh-site.py').includes('scripts/build-atlas-agent-kits.py'));
});
