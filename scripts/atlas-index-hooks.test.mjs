import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync,spawnSync} from 'node:child_process';
import {mkdtempSync,mkdirSync,writeFileSync,readFileSync,readdirSync,copyFileSync,chmodSync,rmSync,existsSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {fileURLToPath} from 'node:url';

const root=fileURLToPath(new URL('../',import.meta.url));
const python=process.env.ATLAS_INDEX_PYTHON||'python3';
const prepare=join(root,'scripts/prepare-indexes.py');
const installer=join(root,'scripts/install-index-hooks.py');
const builder="from pathlib import Path\np=Path('index.txt')\np.write_text('index: '+Path('source.txt').read_text())\n";

function fixture(t,script=builder){
  const temporary=mkdtempSync(join(process.env.ATLAS_INDEX_SCRATCH||tmpdir(),'atlas-hook-test-'));
  t.after(()=>rmSync(temporary,{recursive:true,force:true}));
  const cwd=join(temporary,'repo'),scratch=join(temporary,'scratch');
  mkdirSync(join(cwd,'scripts'),{recursive:true});mkdirSync(scratch);
  const env={...process.env,ATLAS_INDEX_SCRATCH:scratch,PYTHONDONTWRITEBYTECODE:'1'};
  for(const key of Object.keys(env))if(key.startsWith('GIT_'))delete env[key];
  delete env.ATLAS_REFRESH_INDEXES_ON_COMMIT;
  const git=(args,extra={})=>execFileSync('git',args,{cwd,env:{...env,...extra},encoding:'utf8'}).trim();
  const write=(path,value)=>writeFileSync(join(cwd,path),value);
  const read=path=>readFileSync(join(cwd,path),'utf8');
  git(['init','-q']);git(['config','user.name','Index fixture']);git(['config','user.email','fixture@example.invalid']);
  git(['config','extensions.worktreeConfig','true']);
  git(['remote','add','origin','https://github.com/hrkoyama/hrkoyama.github.io.git']);
  write('source.txt','staged source\n');write('index.txt','old index\n');write('unrelated.txt','unrelated\n');
  write('scripts/refresh-site.py',script);git(['add','.']);
  const run=(args=[],extra={})=>spawnSync(python,[prepare,...args],{cwd,env:{...env,...extra},encoding:'utf8'});
  const index=()=>readFileSync(join(cwd,'.git/index'));
  return {cwd,scratch,env,git,write,read,run,index};
}
const succeeded=result=>assert.equal(result.status,0,result.stdout+'\n'+result.stderr);

test('explicit preparation uses staged inputs and preserves partial and unrelated edits',t=>{
  const f=fixture(t);
  f.write('source.txt','unstaged source\n');f.write('unrelated.txt','unstaged unrelated\n');f.write('private-note.txt','leave untracked\n');
  succeeded(f.run());
  assert.equal(f.git(['show',':index.txt']),'index: staged source');
  assert.equal(f.git(['show',':source.txt']),'staged source');
  assert.equal(f.read('source.txt'),'unstaged source\n');
  assert.equal(f.read('unrelated.txt'),'unstaged unrelated\n');
  assert.equal(f.read('private-note.txt'),'leave untracked\n');
  assert.ok(!f.git(['ls-files']).includes('private-note.txt'));
  assert.deepEqual(readdirSync(f.scratch),[],'the exported tree is removed after success');
});

test('all dirty generated collisions are rejected before any working file or index changes',t=>{
  const f=fixture(t,builder+"Path('new-index.txt').write_text('new index')\n");
  f.write('index.txt','unstaged index edit\n');f.write('new-index.txt','untracked collision\n');
  const original=f.index();
  const result=f.run();
  assert.equal(result.status,1);assert.match(result.stderr,/unstaged changes or path collisions/);
  assert.match(result.stderr,/index.txt/);assert.match(result.stderr,/new-index.txt/);
  assert.deepEqual(f.index(),original);
  assert.equal(f.read('index.txt'),'unstaged index edit\n');
  assert.equal(f.read('new-index.txt'),'untracked collision\n');
  assert.deepEqual(readdirSync(f.scratch),[]);
});

test('check mode reports additions and deletions without changing the active index or worktree',t=>{
  const f=fixture(t,"from pathlib import Path\nPath('index.txt').unlink()\nPath('new-index.txt').write_text('new')\n");
  const original=f.index(),old=f.read('index.txt');
  const result=f.run(['--check']);
  assert.equal(result.status,1);assert.match(result.stdout,/D index.txt/);assert.match(result.stdout,/A new-index.txt/);
  assert.deepEqual(f.index(),original);assert.equal(f.read('index.txt'),old);assert.equal(existsSync(join(f.cwd,'new-index.txt')),false);
  assert.deepEqual(readdirSync(f.scratch),[]);
});

test('generated additions and deletions are staged, and unchanged preparation is idempotent',t=>{
  const f=fixture(t,"from pathlib import Path\np=Path('index.txt')\nif p.exists():p.unlink()\nPath('new-index.txt').write_text('new')\n");
  succeeded(f.run());
  assert.ok(!f.git(['ls-files']).split('\n').includes('index.txt'));
  assert.equal(f.git(['show',':new-index.txt']),'new');
  assert.equal(existsSync(join(f.cwd,'index.txt')),false);
  const current=f.index();succeeded(f.run(['--check']));succeeded(f.run());
  assert.deepEqual(f.index(),current);
});

test('a failed generator leaves both working files and staged bytes intact and removes its snapshot',t=>{
  const f=fixture(t,builder+"raise SystemExit(7)\n");
  const original=f.index(),old=f.read('index.txt');
  const result=f.run();assert.equal(result.status,1);assert.match(result.stderr,/refresh failed/);
  assert.deepEqual(f.index(),original);assert.equal(f.read('index.txt'),old);assert.deepEqual(readdirSync(f.scratch),[]);
});

test('an alternate active index is honored without rewriting the default index',t=>{
  const f=fixture(t),alternate=join(f.scratch,'alternate-index');
  copyFileSync(join(f.cwd,'.git/index'),alternate);
  f.write('source.txt','alternate staged source\n');f.git(['add','source.txt'],{GIT_INDEX_FILE:alternate});
  const original=f.index();succeeded(f.run([],{GIT_INDEX_FILE:alternate}));
  assert.deepEqual(f.index(),original);
  assert.equal(f.git(['show',':index.txt'],{GIT_INDEX_FILE:alternate}),'index: alternate staged source');
  assert.equal(f.git(['show',':index.txt']),'old index');
});

test('concurrent index updates are retained and prevent generated files being applied',t=>{
  const f=fixture(t);
  f.write('scripts/refresh-site.py',builder+`import subprocess\nsubprocess.run(['git','add','unrelated.txt'],cwd=${JSON.stringify(f.cwd)},check=True)\n`);
  f.git(['add','scripts/refresh-site.py']);f.write('unrelated.txt','concurrently staged\n');
  const old=f.read('index.txt'),result=f.run();
  assert.equal(result.status,1);assert.match(result.stderr,/active Git index changed/);
  assert.equal(f.read('index.txt'),old);assert.equal(f.git(['show',':index.txt']),'old index');
  assert.equal(f.git(['show',':unrelated.txt']),'concurrently staged');
  assert.deepEqual(readdirSync(f.scratch),[]);
});

function install(f){
  mkdirSync(join(f.cwd,'.githooks'));
  copyFileSync(join(root,'.githooks/pre-commit'),join(f.cwd,'.githooks/pre-commit'));
  chmodSync(join(f.cwd,'.githooks/pre-commit'),0o755);
  copyFileSync(prepare,join(f.cwd,'scripts/prepare-indexes.py'));
  f.git(['add','.']);
  return spawnSync(python,[installer],{cwd:f.cwd,env:f.env,encoding:'utf8'});
}

test('installer rejects a forbidden origin without changing hook configuration',t=>{
  const f=fixture(t);f.git(['remote','set-url','origin','https://github.com/koyamarium/forbidden.git']);
  let result=install(f);assert.equal(result.status,1);assert.match(result.stderr,/origin does not match/);
  const config=spawnSync('git',['config','--worktree','--get','atlas.indexPython'],{cwd:f.cwd,env:f.env,encoding:'utf8'});
  assert.equal(config.status,1);assert.equal(config.stdout,'');
});

test('installer preserves an existing hooks path',t=>{
  const f=fixture(t);f.git(['config','--worktree','core.hooksPath','existing-hooks']);
  const result=install(f);assert.equal(result.status,1);assert.match(result.stderr,/existing core.hooksPath/);
  assert.equal(f.git(['config','--worktree','--get','core.hooksPath']),'existing-hooks');
});

test('installer preserves existing default hooks beyond pre-commit',t=>{
  const f=fixture(t),hook=join(f.cwd,'.git/hooks/pre-push');
  writeFileSync(hook,'#!/bin/sh\nexit 0\n');chmodSync(hook,0o755);
  const result=install(f);assert.equal(result.status,1);assert.match(result.stderr,/default hooks were preserved \(pre-push\)/);
  assert.equal(readFileSync(hook,'utf8'),'#!/bin/sh\nexit 0\n');
  const configured=spawnSync('git',['config','--get','core.hooksPath'],{cwd:f.cwd,env:f.env,encoding:'utf8'});
  assert.equal(configured.status,1);
});

test('a split active index is supported and an existing index lock prevents all output changes',t=>{
  const f=fixture(t);f.git(['update-index','--split-index']);
  succeeded(f.run());assert.equal(f.git(['show',':index.txt']),'index: staged source');
  f.write('source.txt','changed source\n');f.git(['add','source.txt']);
  const original=f.index(),old=f.read('index.txt');f.write('.git/index.lock','owned by another Git operation');
  const result=f.run();assert.equal(result.status,1);assert.match(result.stderr,/index is locked/);
  assert.deepEqual(f.index(),original);assert.equal(f.read('index.txt'),old);
  assert.equal(f.read('.git/index.lock'),'owned by another Git operation');
});

test('normal commits skip preparation and preserve partial, unrelated and untracked edits',t=>{
  const f=fixture(t,"raise SystemExit('The default commit must not run the generator')\n");
  succeeded(install(f));
  f.git(['-c','core.hooksPath=/dev/null','commit','-qm','initial']);
  const trap="raise SystemExit('The default commit must not invoke index preparation')\n";
  f.write('scripts/prepare-indexes.py',trap);
  f.write('source.txt','committed source\n');f.git(['add','source.txt']);
  f.write('source.txt','partially staged working edit\n');
  f.write('unrelated.txt','leave this unstaged\n');f.write('private-note.txt','leave untracked\n');
  const result=spawnSync('git',['commit','-qm','source only'],{cwd:f.cwd,env:f.env,encoding:'utf8'});
  succeeded(result);
  assert.match(result.stdout+'\n'+result.stderr,/Index refresh skipped/);
  assert.equal(f.git(['show','HEAD:source.txt']),'committed source');
  assert.equal(f.git(['show','HEAD:index.txt']),'old index');
  assert.equal(f.git(['show',':source.txt']),'committed source');
  assert.equal(f.read('source.txt'),'partially staged working edit\n');
  assert.equal(f.git(['show','HEAD:unrelated.txt']),'unrelated');
  assert.equal(f.read('unrelated.txt'),'leave this unstaged\n');
  assert.equal(f.read('private-note.txt'),'leave untracked\n');
  assert.ok(!f.git(['ls-files']).includes('private-note.txt'));
  assert.equal(f.read('scripts/prepare-indexes.py'),trap);
  assert.deepEqual(readdirSync(f.scratch),[],'normal commits do not export a build snapshot');
});

test('opted-in hooks refresh a path-limited commit using its temporary active index',t=>{
  const f=fixture(t);succeeded(install(f));
  assert.equal(f.git(['config','--worktree','--get','core.hooksPath']),'.githooks');
  assert.ok(f.git(['config','--worktree','--get','atlas.indexPython']).includes('python'));
  f.git(['-c','core.hooksPath=/dev/null','commit','-qm','initial']);
  f.write('source.txt','committed source\n');f.write('unrelated.txt','leave this unstaged\n');
  const result=spawnSync('git',['commit','-qm','source only','--','source.txt'],{cwd:f.cwd,env:{...f.env,ATLAS_REFRESH_INDEXES_ON_COMMIT:'1'},encoding:'utf8'});
  succeeded(result);
  assert.equal(f.git(['show','HEAD:index.txt']),'index: committed source');
  assert.equal(f.git(['show','HEAD:source.txt']),'committed source');
  assert.equal(f.git(['show','HEAD:unrelated.txt']),'unrelated');
  assert.equal(f.read('unrelated.txt'),'leave this unstaged\n');
});
