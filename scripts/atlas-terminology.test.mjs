import test from 'node:test';
import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';
import {mkdtempSync, rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {fileURLToPath} from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));

test('Japanese editorial wording preserves frozen cases and closes all public seams', {timeout: 20_000}, () => {
  const temporary = mkdtempSync(join(tmpdir(), 'atlas-terminology-test-'));
  try {
    const result = spawnSync('python3', ['-B', 'scripts/fixtures/atlas_terminology_tests.py'], {
      cwd: root, encoding: 'utf8', timeout: 15_000,
      env: {...process.env, PYTHONDONTWRITEBYTECODE: '1', ATLAS_TERMINOLOGY_TEST_SCRATCH: temporary},
    });
    assert.ifError(result.error);
    assert.equal(result.signal, null, result.stderr);
    assert.equal(result.status, 0, result.stdout + result.stderr);
    assert.match(result.stderr, /Ran 8 tests in /);
    assert.match(result.stderr, /\nOK\s*$/);
  } finally {
    rmSync(temporary, {recursive: true, force: true});
  }
});
