import test from 'node:test';
import assert from 'node:assert/strict';
import {validateWaveEvolutionData, waveFrameStatistics, wireWaveEvolution} from '../numerical-methods-atlas/wave-evolution.js';

const fixture = () => ({
  schema_version: 1,
  parameters: {n: 4, domain: [0, 1], dt: 0.1, advection_speed: 1},
  x: [0, 0.25, 0.5, 0.75], steps: [0, 2, 4], time: [0, 0.2, 0.4],
  y_limits: [-1.2, 1.2],
  series: {
    exact: [[0, 1, 0, -1], [1, 0, -1, 0], [0, -1, 0, 1]],
    damping_only: [[0, 1, 0, -1], [0.5, 0, -0.5, 0], [0, -0.25, 0, 0.25]],
    dispersion_only: [[0, 1, 0, -1], [0, -1, 0, 1], [-1, 0, 1, 0]],
    lax_wendroff: [[0, 1, 0, -1], [0.6, -0.2, -0.6, 0.2], [-0.2, -0.4, 0.2, 0.4]],
  },
});

test('the playback module can be imported without a browser or side effects', () => {
  const cleanup = wireWaveEvolution();
  assert.equal(typeof cleanup, 'function');
  cleanup();
});

test('wave data uses common finite samples, frame times, and fixed plotting bounds', () => {
  const data = fixture();
  const before = JSON.stringify(data);
  assert.equal(validateWaveEvolutionData(data), data);
  assert.equal(JSON.stringify(data), before);
  for (const breakData of [
    data => { data.series.dispersion_only.pop(); },
    data => { data.series.lax_wendroff[1].pop(); },
    data => { data.series.exact[1][0] = NaN; },
    data => { data.series.damping_only[1][0] = 1.5; },
    data => { data.time[1] = 0.3; },
    data => { data.steps[1] = 0; },
    data => { data.x[3] = 1; },
    data => { data.x[2] = data.x[1]; },
    data => { data.parameters.n = 8; },
  ]) {
    const malformed = fixture();
    breakData(malformed);
    assert.throws(() => validateWaveEvolutionData(malformed), /Invalid wave-evolution data/);
  }
});

test('visible metrics distinguish amplitude loss from a phase error at conserved discrete L2', () => {
  const data = fixture();
  const initial = waveFrameStatistics(data, 'exact', 0);
  assert.deepEqual(initial, {minimum: -1, maximum: 1, relativeL2: 0, l2Ratio: 1});
  const damping = waveFrameStatistics(data, 'damping_only', 1);
  assert.equal(damping.l2Ratio, 0.5);
  assert.equal(damping.relativeL2, 0.5);
  const dispersion = waveFrameStatistics(data, 'dispersion_only', 1);
  assert.equal(dispersion.l2Ratio, 1);
  assert.ok(Math.abs(dispersion.relativeL2 - Math.sqrt(2)) < 1e-14);
  assert.throws(() => waveFrameStatistics(data, 'exact', 50), RangeError);
});
