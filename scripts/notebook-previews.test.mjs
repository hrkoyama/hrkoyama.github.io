import test from 'node:test';
import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

test('processed notebook material previews reject private paths, extra documents and hidden PNG metadata', () => {
  const root = fileURLToPath(new URL('../', import.meta.url));
  const result = spawnSync(process.env.PYTHON || 'python3', ['-B','scripts/test_notebook_previews.py'], {cwd:root, encoding:'utf8'});
  assert.equal(result.status,0,result.stdout+'\n'+result.stderr);
  assert.match(result.stderr,/Ran 5 tests/);
});
