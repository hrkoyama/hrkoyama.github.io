import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));

test('pilot identities bind saved case/source artifacts and preserve the first frozen revisions', () => {
  const history = readFileSync(new URL('../catalog/atlas-identity-history.json', import.meta.url));
  assert.equal(createHash('sha256').update(history).digest('hex'), '3f747b9b2e9cd436baca0bebddf5b65e2843035aa38a8ee98fbdb6b94fc6b557');
  const report = JSON.parse(execFileSync('python3', ['-B', 'scripts/check-atlas-identities.py'], {cwd: root, encoding: 'utf8'}));
  assert.equal(report.passed, true);
  assert.equal(report.baseline_checked, true);
  assert.equal(report.validation_type, 'saved-artifact-integrity-only');
  assert.equal(report.numerical_execution, false);
  assert.ok(report.problems >= 3 && report.cases >= 3 && report.sources >= 2);
});

test('identity validation rejects tampering, wrong case/source links, unsafe paths and rewritten revisions', () => {
  execFileSync('python3', ['-B', '-m', 'unittest', 'discover', '-s', 'scripts', '-p', 'test_atlas_identities.py', '-v'], {cwd: root, encoding: 'utf8', stdio: 'pipe'});
});
