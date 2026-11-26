import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';

const root = fileURLToPath(new URL('../', import.meta.url));
const workflow = readFileSync(new URL('../.github/workflows/atlas-depth-linux.yml', import.meta.url), 'utf8');

test('Linux scope decisions preserve full checks after science changes, failures and uncertain comparisons', () => {
  execFileSync('python3', ['-B', '-m', 'unittest', 'discover', '-s', 'scripts', '-p', 'test_atlas_depth_scope.py', '-v'],
    {cwd: root, encoding: 'utf8', stdio: 'pipe', timeout: 30_000});
});

test('the scope gate is source-only and the full scientific job keeps public-only execution', () => {
  const start = workflow.indexOf('\n  public-supplements:');
  assert.ok(start > 0);
  const gate = workflow.slice(0, start), science = workflow.slice(start);
  assert.match(gate, /classify-changes:/);
  assert.match(gate, /actions\/checkout@/);
  assert.match(gate, /sparse-checkout:/);
  assert.match(gate, /persist-credentials: false/);
  assert.match(gate, /scripts\/plan-atlas-depth-ci\.py/);
  assert.match(gate, /actions: read/);
  assert.match(gate, /run_full: \$\{\{ steps\.plan\.outputs\.run_full \}\}/);
  assert.match(gate, /target_sha: \$\{\{ steps\.plan\.outputs\.target_sha \}\}/);
  assert.match(science, /needs: classify-changes/);
  assert.match(science, /needs\.classify-changes\.outputs\.run_full != 'false'/);
  assert.doesNotMatch(workflow, /(?:contents|actions|packages|id-token): write|write-all|secrets\./);
  assert.match(science, /needs:.*classify-changes/);
  assert.doesNotMatch(science, /actions\/checkout|persist-credentials/);
  assert.match(science, /source_checkout.*False/);
  assert.match(science, /numpy==2\.0\.2 scipy==1\.14\.1 pytest==8\.3\.5/);
  assert.match(workflow, /workflow_dispatch:/);
  assert.match(workflow, /cron: '37 3 \* \* 1'/);
  assert.match(workflow, /group: atlas-depth-public-linux/);
  assert.match(workflow, /cancel-in-progress: false/);
});
