import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));

test('current identities cover canonical problems, registered cases and source units while retaining frozen checkpoints', () => {
  const history = readFileSync(new URL('../catalog/atlas-identity-history.json', import.meta.url));
  assert.equal(createHash('sha256').update(history).digest('hex'), '3f747b9b2e9cd436baca0bebddf5b65e2843035aa38a8ee98fbdb6b94fc6b557');
  const expanded = readFileSync(new URL('../catalog/atlas-identity-expansion-history.json', import.meta.url));
  assert.equal(createHash('sha256').update(expanded).digest('hex'), 'fd177d1229d127135b3a415deb9e806df0bd258085fe40f57edf59c496377643');
  const catalog = JSON.parse(readFileSync(new URL('../catalog/atlas-test-problems.json', import.meta.url)));
  const releases = JSON.parse(readFileSync(new URL('../numerical-methods-atlas/validation/releases.json', import.meta.url)));
  const common = JSON.parse(readFileSync(new URL('../numerical-methods-atlas/code-and-data/examples.json', import.meta.url)));
  const registry = JSON.parse(readFileSync(new URL('../catalog/atlas-identities.json', import.meta.url)));
  const report = JSON.parse(execFileSync('python3', ['-B', 'scripts/check-atlas-identities.py'], {cwd: root, encoding: 'utf8'}));
  assert.equal(report.passed, true);
  assert.equal(report.baseline_checked, true);
  assert.equal(report.validation_type, 'saved-artifact-integrity-only');
  assert.equal(report.numerical_execution, false);
  assert.equal(report.coverage, 'atlas-current');
  assert.equal(report.complete_current_inventory, true);
  assert.equal(report.frozen_checkpoints_checked, 2);
  assert.equal(report.problems, catalog.problems.length);
  assert.equal(report.cases, releases.releases.flatMap(item => item.case_ids).length + common.examples.length);
  assert.equal(report.sources, registry.entities.filter(item => item.kind === 'source').length);
  assert.equal(report.source_units, report.sources);
  assert.ok(report.active_source_revisions >= report.sources);
  assert.ok(report.entities >= JSON.parse(expanded).entities.length);
});

test('identity validation rejects tampering, wrong case/source links, unsafe paths and rewritten revisions', () => {
  execFileSync('python3', ['-B', '-m', 'unittest', 'discover', '-s', 'scripts', '-p', 'test_atlas_identit*.py', '-v'], {cwd: root, encoding: 'utf8', stdio: 'pipe'});
});
