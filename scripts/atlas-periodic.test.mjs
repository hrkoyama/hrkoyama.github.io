import {methodCount} from './fixtures/atlas-inventory.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {searchChapters} from '../numerical-methods-atlas/home-search.js';
import {findMethods} from '../search/method-search.mjs';

const root = new URL('../', import.meta.url);
const bytes = path => readFileSync(new URL(path, root));
const text = path => bytes(path).toString('utf8');
const json = path => JSON.parse(text(path));
const sha = path => createHash('sha256').update(bytes(path)).digest('hex');
const base = 'code/periodic-dft/2026-11-22/';
const input = json(base + 'inputs.json');
const result = json(base + 'results/result.json');
const reference = json(base + 'reference-dftk.json');
const exampleID = 'periodic-he-dft';
const close = (actual, expected, tolerance = 1e-13) => assert.ok(Math.abs(actual - expected) <= tolerance, `${actual} differs from ${expected}`);

test('bilingual periodic reading exposes measured evidence before theory, rendered equations and explicit physical limits', () => {
  const source = json('catalog/atlas-periodic-reading.json');
  const headings = [];
  for (const lang of ['ja', 'en']) {
    const route = `numerical-methods-atlas/${lang}/read/periodic-dft/`;
    const record = json(route + 'index.json'), html = text(route + 'index.html'), markdown = text(route + 'index.md');
    assert.equal(record.locale, lang);
    assert.equal(record.execution_example, exampleID);
    assert.deepEqual(record.measurements, result.metrics);
    for (const [path, hash] of Object.entries(record.source_sha256)) assert.equal(sha(path), hash, path);
    assert.ok(html.includes('katex-mathml') && !html.includes('katex-error'));
    assert.ok(html.includes(`/code-and-data/examples/${exampleID}/`));
    assert.ok(html.includes('/code/periodic-dft/2026-11-22/reference-dftk.json'));
    assert.ok(html.indexOf('id="measured-results"') < html.indexOf('id="model-and-scope"'));
    for (const id of ['results-kpoint', 'results-basis', 'results-auxiliary', 'results-scf', 'reference-results', 'reference-cutoff-results', 'run-and-check', 'sources']) assert.ok(html.includes(`id="${id}"`), id);
    assert.ok(markdown.includes('$$') && markdown.includes('python run.py --input inputs.json --output output'));
    const summary = html.slice(html.indexOf('id="measured-results"'), html.indexOf('id="convergence-targets"'));
    const displayed = [...summary.matchAll(/<td>([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)<\/td>/g)].map(match => Number(match[1]));
    for (const key of ['max_reference_energy_error', 'kpoint_last_change', 'basis_last_change', 'auxiliary_last_change', 'scf_last_change']) {
      const expected = result.metrics[key];
      assert.ok(displayed.some(value => Math.abs(value - expected) <= Math.max(1e-20, Math.abs(expected) * 5e-12)), key);
    }
    for (const doi of ['10.1007/BF01339455', '10.1103/PhysRevB.54.1703', '10.1139/p80-159', '10.21105/jcon.00069']) assert.ok(record.references.some(r => r.doi === doi && r.review[lang]), doi);
    for (const section of source.sections) assert.ok(section.paragraphs[lang].join(' ').length > 120, `${lang}/${section.id}`);
    headings.push(record.headings.map(h => h.id));
  }
  assert.deepEqual(headings[0], headings[1]);
  const english = text('numerical-methods-atlas/en/read/periodic-dft/index.html');
  for (const phrase of ['equilibrium solid helium', 'VWN5', 'per unit cell', 'band path', 'auxiliary', 'fundamental gap', 'Both engines use Libxc', 'machine-precision agreement']) assert.ok(english.includes(phrase), phrase);
  assert.equal(source.references.find(r => r.id === 'vwn1980').review_level, 'metadata');
});

test('one artificial He test problem contains explicit three-dimensional Gamma meshes and converged finite calculations', () => {
  assert.equal(result.case, exampleID);
  assert.equal(result.passed, true);
  assert.ok(Object.values(result.checks).every(value => value === true));
  assert.equal(result.input_sha256, sha(base + 'inputs.json'));
  assert.equal(result.reference_sha256, sha(base + 'reference-dftk.json'));
  assert.equal(result.cases.length, input.cases.length);
  assert.equal(new Set(result.cases.map(row => row.id)).size, result.cases.length);
  assert.equal(input.cell.element, 'He');
  assert.deepEqual(input.cell.lattice_bohr, [[4, 0, 0], [0, 4, 0], [0, 0, 4]]);
  assert.deepEqual(input.xc.libxc, ['lda_x', 'lda_c_vwn']);
  for (const row of result.cases) {
    assert.equal(row.converged, true);
    assert.equal(row.termination, 'converged');
    assert.equal(row.trace.length, row.iterations);
    assert.equal(row.energy_total, row.energy_per_cell);
    assert.equal(row.kpoints_fractional.length, row.k_n ** 3);
    assert.equal(new Set(row.kpoints_fractional.map(k => JSON.stringify(k))).size, row.k_n ** 3);
    assert.ok(row.kpoints_fractional.some(k => k.every(value => value === 0)), 'Gamma is included for odd and even meshes');
    close(row.weights.reduce((sum, value) => sum + value, 0), 1);
    for (const weight of row.weights) close(weight, 1 / row.k_n ** 3);
    for (let axis = 0; axis < 3; axis++) assert.equal(new Set(row.kpoints_fractional.map(k => k[axis])).size, row.k_n);
    close(row.electron_count, 2, input.acceptance.max_electron_count_error);
    assert.ok(row.sampled_ks_gap >= input.acceptance.min_sampled_ks_gap);
    assert.ok(Number.isFinite(row.scf_commutator_norm) && Number.isFinite(row.orbital_residual_norm));
  }
  const problems = json('catalog/atlas-test-problems.json').problems;
  assert.equal(problems.filter(p => p.id === exampleID).length, 1);
  assert.ok(!problems.some(p => /^periodic-he-dft-(?:basis|kpoint|scf|fft)/.test(p.id)));
});

test('k-point, orbital-basis, auxiliary-grid and SCF sweeps change separate numerical controls', () => {
  const indexed = new Map(result.cases.map(row => [row.id, row]));
  for (const [axis, group] of Object.entries(result.convergence)) {
    assert.deepEqual(group.case_ids, input.convergence_groups[axis]);
    const rows = group.case_ids.map(id => indexed.get(id));
    assert.ok(rows.every(Boolean));
    for (let i = 0; i < rows.length - 1; i++) close(group.adjacent_changes[i], Math.abs(rows[i + 1].energy_per_cell - rows[i].energy_per_cell));
    close(group.last_change, group.adjacent_changes.at(-1));
    assert.equal(group.target, input.acceptance[axis + '_last_change']);
    assert.equal(group.target_reached, true);
    assert.ok(group.last_change <= group.target);
    if (axis !== 'kpoint') assert.equal(new Set(rows.map(r => r.k_n)).size, 1, axis);
    if (axis !== 'basis') assert.equal(new Set(rows.map(r => r.basis)).size, 1, axis);
    if (axis !== 'auxiliary') assert.equal(new Set(rows.map(r => JSON.stringify(r.fft_mesh))).size, 1, axis);
    if (axis !== 'scf') assert.equal(new Set(rows.map(r => JSON.stringify(r.scf_options))).size, 1, axis);
  }
});

test('independent DFTK uses the same model, explicit sampling and XC, with separately measured plane-wave convergence', () => {
  assert.deepEqual(reference.cell, input.cell);
  assert.deepEqual(reference.xc, input.xc.libxc);
  const comparisons = result.independent_comparison.cases;
  assert.deepEqual(comparisons.map(r => r.k_n).sort(), [1, 2]);
  const cutoff = result.independent_comparison.cutoff_convergence;
  assert.deepEqual(cutoff, reference.cutoff_convergence);
  assert.equal(cutoff.target_reached, true);
  for (const row of cutoff.records) {
    assert.equal(row.converged, true);
    close(row.kpoint_weights.reduce((sum, value) => sum + value, 0), 1);
    close(row.electron_count, 2, 1e-8);
    const components = Object.values(row.energy_components).reduce((sum, value) => sum + value, 0);
    close(components, row.energy_per_cell, 1e-10);
  }
  for (const row of comparisons) {
    close(row.absolute_difference, Math.abs(row.pyscf_energy_per_cell - row.dftk_energy_per_cell));
    assert.equal(row.acceptance, input.acceptance.reference_energy_difference);
    assert.equal(row.passed, true);
    assert.ok(row.absolute_difference <= row.acceptance);
    const sequence = cutoff.records.filter(r => r.k_n === row.k_n);
    assert.ok(sequence.length >= 3);
    const last = sequence.at(-1), previous = sequence.at(-2);
    assert.ok(last.ecut_hartree > previous.ecut_hartree);
    assert.equal(row.dftk_energy_per_cell, last.energy_per_cell);
    const change = cutoff.last_changes.find(r => r.k_n === row.k_n);
    close(change.energy_change, Math.abs(last.energy_per_cell - previous.energy_per_cell));
    assert.ok(change.energy_change <= cutoff.target_hartree_per_cell);
  }
  assert.match(text(base + 'periodic_dft.py'), /from pyscf.pbc import/);
  assert.match(reference.independence, /independent|Independent/);
  assert.match(reference.independence, /Libxc/);
});

test('periodic methods and the purpose entry link to reading, code and tests while molecular DFT stays scoped', () => {
  const methods = json('numerical-methods-atlas/methods/index.json').methods;
  for (const id of ['kohn-sham-dft', 'electronic-bases', 'scf', 'xc-functionals', 'pseudopotentials', 'k-point']) {
    const method = methods.find(m => m.id === id);
    assert.ok(method, id);
    assert.equal(method.status, 'educational-example', id);
    assert.deepEqual(method.periodic_examples, [exampleID]);
    assert.equal(method.periodic_release.release.family, 'periodic-dft');
    assert.ok(method.execution_examples.some(e => e.id === exampleID));
    assert.ok(method.code_urls.some(url => url.endsWith('/periodic_dft.py')));
    assert.ok(method.test_urls.length);
  }
  const goals = json('catalog/atlas-goals.json').goals;
  const periodic = goals.find(g => g.id === 'periodic-dft');
  assert.deepEqual(periodic.examples, [exampleID]);
  assert.ok(periodic.domains.includes('quantum'));
  const molecular = goals.find(g => g.id === 'molecular-dft');
  assert.deepEqual(molecular.examples, []);
  assert.equal(molecular.availability, 'reading-only');
  const index = json('numerical-methods-atlas/home-search-index.json');
  for (const lang of ['ja', 'en']) {
    const rows = searchChapters(index, lang === 'ja' ? '周期DFT 実行' : 'periodic DFT code', lang);
    assert.ok(rows.some(row => row.url?.includes(`/code-and-data/examples/${exampleID}/`)));
  }
});

test('BOMD and CPMD are searchable reading-only methods with equations and primary sources, without borrowed executions', () => {
  const methods = json('numerical-methods-atlas/methods/index.json').methods;
  const source = json('catalog/atlas-periodic-reading.json');
  const section = source.sections.find(s => s.id === 'first-principles-md');
  assert.ok(section);
  assert.equal(methods.length, methodCount);
  const coverage = json('numerical-methods-atlas/coverage.json');
  const coveredMethods = coverage.items.filter(row => row.kind === 'method');
  // The legacy inventory remains136; the newly executable slab adds one
  // unrelated method without supplying any first-principles MD trajectory.
  assert.equal(coveredMethods.filter(row => row.id !== 'slab-ewald').length, 136);
  assert.equal(coverage.counts.methods, coveredMethods.length);
  const slab = json('catalog/atlas-methods.json').methods.find(row => row.id === 'slab-ewald');
  assert.equal(slab.depth_previous_status, 'planned');
  assert.equal(slab.status, 'educational-example');
  assert.deepEqual(coveredMethods.filter(row => row.id === 'slab-ewald').map(row => row.chapter), ['validation-slab-ewald']);
  for (const [id, alias] of [['born-oppenheimer-md', 'BOMD'], ['car-parrinello-md', 'CPMD']]) {
    const method = methods.find(m => m.id === id);
    assert.equal(method.status, 'reading-only');
    assert.deepEqual(method.code_urls, []);
    assert.deepEqual(method.test_urls, []);
    assert.deepEqual(method.execution_examples, []);
    assert.ok(!method.periodic_examples?.length);
    assert.ok(!method.depth_release && !method.depth_additional_releases?.length);
    assert.ok(!method.force_release && !method.force_examples?.length);
    const coverageRow = coveredMethods.find(row => row.id === id);
    assert.equal(coverageRow.status, 'reading');
    assert.equal(coverageRow.chapter, 'quantum-chemistry');
    const individual = json(`numerical-methods-atlas/methods/${id}/index.json`);
    assert.equal(individual.status, 'reading-only');
    assert.deepEqual(individual.execution_examples, []);
    assert.deepEqual(individual.code_urls, []);
    assert.deepEqual(individual.test_urls, []);
    assert.ok(!individual.depth_release && !individual.force_release);
    for (const lang of ['ja', 'en']) {
      assert.ok(method.reading[lang].endsWith('/read/periodic-dft/#first-principles-md'));
      assert.equal(findMethods(methods, alias, lang)[0]?.method.id, id);
      const page = text(`numerical-methods-atlas/${lang}/read/periodic-dft/index.html`);
      assert.ok(page.includes('id="first-principles-md"'));
      assert.ok(page.includes(lang === 'ja' ? 'この節は解説のみ' : 'This section is reading only'));
    }
  }
  const gravity = methods.find(row => row.id === 'verlet').depth_release;
  assert.equal(gravity.group, 'gravity-dynamics');
  assert.deepEqual(gravity.case_ids, ['gravity-kepler', 'gravity-plummer-short']);
  for (const example of gravity.examples) {
    assert.deepEqual(example.domains, ['particles']);
    assert.ok(example.method_ids.includes('verlet'));
    assert.ok(!example.method_ids.some(id => ['born-oppenheimer-md', 'car-parrinello-md'].includes(id)));
  }
  assert.ok(section.formulas.includes('periodic-bo-forces'));
  assert.ok(section.formulas.includes('periodic-cp-lagrangian'));
  assert.ok(section.formulas.includes('periodic-cp-constraint-energy'));
  for (const doi of ['10.1002/andp.19273892002', '10.1103/PhysRevLett.55.2471']) assert.ok(source.references.some(r => r.doi === doi));
  const method = methods.find(m => m.id === 'car-parrinello-md');
  assert.ok(method.name.ja.includes('カー–パリネロ法'));
});
