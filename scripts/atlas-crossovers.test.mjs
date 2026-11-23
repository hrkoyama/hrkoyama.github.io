import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync, existsSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import {matchCrossover, crossoverFilterURL, wireCrossovers} from '../numerical-methods-atlas/crossovers.mjs';
import {homeOverviewPage} from '../numerical-methods-atlas/home-overview.js';
import {configureLocale} from '../numerical-methods-atlas/i18n.js';
import {searchChapters} from '../numerical-methods-atlas/home-search.js';

const root = new URL('../', import.meta.url);
const text = path => readFileSync(new URL(path, root), 'utf8');
const json = path => JSON.parse(text(path));
const origin = 'https://hrkoyama.github.io';
const routeIDs = ['dft-md', 'reaction-transport', 'poisson-fields'];
const methods = json('catalog/atlas-methods.json').methods;
const publishedMethods = json('numerical-methods-atlas/methods/index.json').methods;
const examples = json('catalog/atlas-execution-examples.json').examples;
const source = json('catalog/atlas-crossovers.json');
const published = json('numerical-methods-atlas/connections/index.json');
const html = text('numerical-methods-atlas/connections/index.html');

function decode(value) {
  return value.replace(/&(?:amp|quot|apos|lt|gt|#(\d+)|#x([a-f\d]+));/gi, (entity, decimal, hex) => {
    if (decimal || hex) return String.fromCodePoint(parseInt(decimal || hex, decimal ? 10 : 16));
    return {'&amp;': '&', '&quot;': '"', '&apos;': "'", '&lt;': '<', '&gt;': '>'}[entity.toLowerCase()];
  });
}
function attributes(value) {
  return Object.fromEntries([...value.matchAll(/([a-zA-Z_:][-a-zA-Z0-9_:.]*)(?:\s*=\s*"([^"]*)")?/g)].map(match => [match[1], decode(match[2] || '')]));
}
function localTarget(href) {
  const url = new URL(href, origin);
  assert.equal(url.origin, origin, href);
  assert.ok(!url.pathname.includes('..'), href);
  const file = url.pathname.slice(1) + (url.pathname.endsWith('/') ? 'index.html' : '');
  assert.ok(existsSync(new URL(file, root)), href);
  if (url.hash) assert.ok(text(file).includes(`id="${decodeURIComponent(url.hash.slice(1))}"`), href + ' fragment');
  return url;
}

test('crossovers preserve the scientific inventory and canonical availability', () => {
  const coverage = json('numerical-methods-atlas/coverage.json');
  assert.equal(methods.length, 151);
  assert.equal(json('catalog/atlas-equations.json').equations.length, 50);
  assert.equal(coverage.counts.papers, coverage.publications.filter(row => ['article', 'inproceedings'].includes(row.type)).length);
  assert.equal(coverage.counts.references, coverage.publications.length);
  assert.equal(json('catalog/atlas-test-problems.json').problems.length, coverage.counts.test_problems);
  assert.equal(examples.length, 22);
  for (const id of ['born-oppenheimer-md', 'car-parrinello-md']) {
    const method = publishedMethods.find(item => item.id === id);
    assert.equal(method.status, 'reading-only', id);
    assert.deepEqual(method.code_urls, [], id);
    assert.deepEqual(method.test_urls, [], id);
    assert.deepEqual(method.execution_examples, [], id);
  }
  for (const id of ['nose-hoover', 'nose-hoover-chains', 'velocity-rescaling']) {
    const method = publishedMethods.find(item => item.id === id);
    assert.equal(method.status, 'planned', id);
    assert.deepEqual(method.code_urls, [], id);
    assert.deepEqual(method.test_urls, [], id);
    assert.deepEqual(method.execution_examples, [], id);
  }
  const langevin = publishedMethods.find(item => item.id === 'langevin-thermostat');
  assert.equal(langevin.status, 'educational-example');
  assert.deepEqual(new Set(langevin.execution_examples.map(row => row.id)),new Set(['langevin-harmonic','csvr-langevin-harmonic','csvr-langevin-quartic']));
  const csvr=publishedMethods.find(item=>item.id==='stochastic-velocity-rescaling');
  assert.equal(csvr.status,'educational-example');
  assert.deepEqual(new Set(csvr.execution_examples.map(row=>row.id)),new Set(['csvr-kinetic-kernel','csvr-langevin-harmonic','csvr-langevin-quartic']));
  assert.ok(!examples.some(row => row.id === 'langevin-harmonic'), 'supplement is not silently added to the common execution registry');
});

// DOM fixture exercises the public filter with real generated route membership.
// It never computes visibility itself and refuses HTML interpretation.
class Element {
  constructor(tagName, attrs = {}) {
    this.tagName = tagName.toUpperCase(); this.attributes = {...attrs}; this.dataset = {};
    this.children = []; this.parentElement = null; this.handlers = new Map();
    this.hidden = 'hidden' in attrs; this.value = ''; this.textContent = ''; this.focused = false;
    for (const [key, value] of Object.entries(attrs)) if (key.startsWith('data-')) this.dataset[key.slice(5).replace(/-([a-z])/g, (_, c) => c.toUpperCase())] = value;
  }
  get id() { return this.attributes.id || ''; }
  set id(value) { this.attributes.id = String(value); }
  append(...nodes) { for (const node of nodes) { this.children.push(node); node.parentElement = this; } }
  getAttribute(name) { return this.attributes[name] ?? null; }
  setAttribute(name, value) { this.attributes[name] = String(value); if (name === 'hidden') this.hidden = true; }
  removeAttribute(name) { delete this.attributes[name]; if (name === 'hidden') this.hidden = false; }
  addEventListener(name, callback) { this.handlers.set(name, [...(this.handlers.get(name) || []), callback]); }
  removeEventListener(name, callback) { this.handlers.set(name, (this.handlers.get(name) || []).filter(value => value !== callback)); }
  dispatch(name, values = {}) {
    const event = {type: name, target: this, currentTarget: this, defaultPrevented: false,
      preventDefault() { this.defaultPrevented = true; }, ...values};
    for (const callback of this.handlers.get(name) || []) callback(event);
    return event;
  }
  focus() { this.focused = true; }
  matches(selector) {
    const match = selector.trim().match(/^(?:([a-z]+))?\[([^=\]]+)(?:="([^"]*)")?\]$/i);
    if (!match) return this.tagName.toLowerCase() === selector.trim().toLowerCase();
    return (!match[1] || this.tagName.toLowerCase() === match[1].toLowerCase()) && match[2] in this.attributes && (match[3] === undefined || this.attributes[match[2]] === match[3]);
  }
  querySelectorAll(selector) {
    const values = [];
    for (const child of this.children) {
      if (selector.split(',').some(part => child.matches(part))) values.push(child);
      values.push(...child.querySelectorAll(selector));
    }
    return values;
  }
  querySelector(selector) { return this.querySelectorAll(selector)[0] || null; }
  set innerHTML(_) { throw new Error('Filter state must remain text'); }
}
function environment(href) {
  const events = new Element('window');
  let location = new URL(href, origin);
  let calls = [];
  return {
    get location() { return location; },
    history: {replaceState(_state, _unused, value) { calls.push(['replace', String(value)]); location = new URL(value, location); }, pushState(_state, _unused, value) { calls.push(['push', String(value)]); location = new URL(value, location); }},
    addEventListener: events.addEventListener.bind(events), removeEventListener: events.removeEventListener.bind(events),
    get sessionStorage() { throw new Error('Crossover links must not depend on stored state'); },
    get localStorage() { throw new Error('Crossover links must not depend on stored state'); },
    get calls() { return calls; },
    navigate(value, event = 'popstate') { location = new URL(value, location); events.dispatch(event); }
  };
}

const mathIDs = ['time-evolution', 'elliptic-solves', 'nonlinear-iteration', 'stability-spectrum', 'probability-sampling'];

test('math matching is exact, supports all, and cannot interpret a partial ID as membership', () => {
  assert.ok(matchCrossover(['time-evolution', 'elliptic-solves']));
  assert.ok(matchCrossover('time-evolution elliptic-solves', 'elliptic-solves'));
  assert.ok(matchCrossover(['time-evolution'], 'time-evolution'));
  assert.ok(!matchCrossover(['time-evolution'], 'time'));
  assert.ok(!matchCrossover(['time-evolution'], 'elliptic-solves'));
  assert.ok(!matchCrossover(['time-evolution'], '<img src=x>'));
});

test('filter URLs preserve language, unrelated query parameters and exact deep links', () => {
  const href = origin + '/numerical-methods-atlas/connections/?lang=en&view=compact#dft-md-en';
  const filtered = new URL(crossoverFilterURL(href, 'elliptic-solves'), origin);
  assert.equal(filtered.pathname, '/numerical-methods-atlas/connections/');
  assert.equal(filtered.searchParams.get('lang'), 'en');
  assert.equal(filtered.searchParams.get('view'), 'compact');
  assert.equal(filtered.searchParams.get('math'), 'elliptic-solves');
  assert.equal(filtered.hash, '#dft-md-en');
  const reset = new URL(crossoverFilterURL(filtered.href, 'all'), origin);
  assert.equal(reset.searchParams.has('math'), false);
  assert.equal(reset.hash, '#dft-md-en');
  assert.equal(reset.searchParams.get('lang'), 'en');
});

function makeFixture(href = origin + '/numerical-methods-atlas/connections/?lang=ja') {
  const document = new Element('document');
  const browser = environment(href); document.defaultView = browser;
  const sections = ['ja', 'en'].map(lang => {
    const section = new Element('section', {'data-crossover-root': '', 'data-site-language': lang, lang}); section.lang = lang;
    const form = new Element('form', {'data-crossover-controls': '', hidden: ''});
    const select = new Element('select', {'data-crossover-math': ''}); select.value = 'all'; select.options = ['all', ...mathIDs].map(value => ({value}));
    const reset = new Element('button', {'data-crossover-reset': '', type: 'button'});
    const count = new Element('p', {'data-crossover-count': '', role: 'status', 'aria-live': 'polite', 'aria-atomic': 'true'});
    const empty = new Element('p', {'data-crossover-empty': '', hidden: ''});
    form.append(select, reset); section.append(form, count, empty);
    const routeNodes = [...html.matchAll(/<[a-z][^>]*\bdata-crossover-route(?:="[^"]*")?[^>]*>/g)].map(match => attributes(match[0])).filter(attrs => attrs.id?.endsWith('-' + lang));
    assert.equal(routeNodes.length, 3, 'Three generated detailed routes per language');
    const cards = []; const details = [];
    for (const attrs of routeNodes) {
      const id = attrs['data-route-id'] || attrs.id.slice(0, -lang.length - 1);
      const common = {'data-route-id': id, 'data-math-ids': attrs['data-math-ids']};
      const card = new Element('article', {...common, 'data-crossover-card': ''});
      const detail = new Element('article', {...common, ...attrs});
      cards.push(card); details.push(detail); section.append(card, detail);
    }
    document.append(section);
    return {section, lang, form, select, reset, count, empty, cards, details};
  });
  document.getElementById = id => document.querySelectorAll('[data-crossover-route]').find(node => node.getAttribute('id') === id) || null;
  return {document, browser, sections, ja: sections[0], en: sections[1]};
}
function assertVisible(fixture, expected) {
  for (const section of fixture.sections) {
    for (const nodes of [section.cards, section.details]) assert.deepEqual(nodes.filter(node => !node.hidden).map(node => node.dataset.routeId).sort(), [...expected].sort(), section.lang);
    assert.equal(section.empty.hidden, expected.length !== 0, section.lang);
    const values = (section.count.textContent.match(/\d+/g) || []).map(Number);
    assert.ok(values.includes(expected.length), section.count.textContent);
    assert.ok(values.includes(3), section.count.textContent);
  }
}
function idsFor(math) {
  return source.routes.filter(route => matchCrossover(route.math_ids, math)).map(route => route.id);
}

test('native controls synchronize bilingual cards, detailed routes, counts and URL state', () => {
  const fixture = makeFixture();
  assert.doesNotThrow(() => wireCrossovers(fixture.document, fixture.browser));
  assertVisible(fixture, routeIDs);
  for (const section of fixture.sections) assert.equal(section.form.hidden, false);
  fixture.ja.select.value = 'elliptic-solves'; fixture.ja.select.dispatch('change');
  assertVisible(fixture, idsFor('elliptic-solves'));
  assert.equal(fixture.en.select.value, 'elliptic-solves');
  assert.equal(fixture.browser.location.searchParams.get('math'), 'elliptic-solves');
  assert.equal(fixture.browser.location.searchParams.get('lang'), 'ja');
  assert.equal(fixture.en.form.dispatch('submit').defaultPrevented, true);
  fixture.en.reset.dispatch('click');
  assertVisible(fixture, routeIDs);
  assert.equal(fixture.browser.location.searchParams.has('math'), false);
  for (const section of fixture.sections) assert.equal(section.select.value, 'all');
});

test('shared filter URLs restore on initial load, browser history and reset without stored state', () => {
  const fixture = makeFixture(origin + '/numerical-methods-atlas/connections/?lang=en&math=probability-sampling');
  wireCrossovers(fixture.document, fixture.browser);
  assertVisible(fixture, idsFor('probability-sampling'));
  fixture.browser.navigate('?lang=en&math=stability-spectrum');
  assertVisible(fixture, idsFor('stability-spectrum'));
  fixture.browser.navigate('?lang=ja');
  assertVisible(fixture, routeIDs);
  assert.equal(fixture.ja.select.value, 'all');
});

test('invalid URL states cannot hide the static routes and invalid input stays inert', () => {
  for (const value of ['unknown-math', '<img src=x onerror=alert(1)>', '__proto__']) {
    const fixture = makeFixture(origin + '/numerical-methods-atlas/connections/?math=' + encodeURIComponent(value));
    assert.doesNotThrow(() => wireCrossovers(fixture.document, fixture.browser));
    assertVisible(fixture, routeIDs);
    for (const section of fixture.sections) assert.equal(section.select.value, 'all');
  }
});

test('deep links reveal the selected detailed route after filter restoration and hash navigation', () => {
  // An explicit anchor wins over a valid filter that would hide its route.
  const fixture = makeFixture(origin + '/numerical-methods-atlas/connections/?lang=en&math=elliptic-solves#dft-md-en');
  wireCrossovers(fixture.document, fixture.browser);
  assert.equal(fixture.en.details.find(node => node.dataset.routeId === 'dft-md').hidden, false);
  fixture.ja.select.value = 'probability-sampling'; fixture.ja.select.dispatch('change');
  fixture.browser.navigate('?lang=ja&math=probability-sampling#poisson-fields-ja', 'hashchange');
  assert.equal(fixture.ja.details.find(node => node.dataset.routeId === 'poisson-fields').hidden, false);
});

test('empty results announce zero in both languages and reset restores every route', () => {
  const fixture = makeFixture(origin + '/numerical-methods-atlas/connections/?math=probability-sampling');
  for (const section of fixture.sections) for (const node of [...section.cards, ...section.details]) {
    node.dataset.mathIds = 'elliptic-solves'; node.attributes['data-math-ids'] = 'elliptic-solves';
  }
  wireCrossovers(fixture.document, fixture.browser);
  assertVisible(fixture, []);
  fixture.ja.reset.dispatch('click');
  assertVisible(fixture, routeIDs);
});

test('catalog validation rejects unknown references and borrowed coupled evidence', () => {
  const program = `import copy, importlib.util, json, pathlib, sys
sys.path.insert(0, 'scripts')
spec=importlib.util.spec_from_file_location('crossover_builder','scripts/build-atlas-crossovers.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
data=json.loads(pathlib.Path('catalog/atlas-crossovers.json').read_text())
b.validate_catalog(data)
cases=[]
bad=copy.deepcopy(data);bad['schema_version']=999;cases.append(('schema',bad))
bad=copy.deepcopy(data);bad['routes'][1]['id']=bad['routes'][0]['id'];cases.append(('duplicate route',bad))
bad=copy.deepcopy(data);bad['routes'][0]['stages'][0]['method_ids']=['unknown-method'];cases.append(('method',bad))
bad=copy.deepcopy(data);bad['routes'][0]['stages'][0]['example_ids']=['unknown-example'];cases.append(('example',bad))
bad=copy.deepcopy(data);bad['routes'][0]['stages'][0]['example_role']='coupled-proof';cases.append(('role',bad))
bad=copy.deepcopy(data);bad['routes'][0]['connections'][0]['coupled_validation']['example_ids']=['periodic-he-dft'];cases.append(('borrowed coupled evidence',bad))
bad=copy.deepcopy(data);next(s for s in bad['routes'][0]['stages'] if s['id']=='nuclear-forces')['example_ids']=['periodic-he-dft'];cases.append(('static energy borrowed as forces',bad))
bad=copy.deepcopy(data);bad['routes'][0]['connections'][1]['coupled_validation']['status']='fixed-input';cases.append(('local interface promoted to full MD',bad))
bad=copy.deepcopy(data);bad['routes'][0]['coupled_validation'].update(status='fixed-input',example_ids=['periodic-he-forces']);cases.append(('force example borrowed for complete route',bad))
bad=copy.deepcopy(data);bad['routes'][2]['connections'][0]['coupled_validation'].update(status='fixed-input',example_ids=['periodic-he-forces']);cases.append(('unrelated force example borrowed for pressure bridge',bad))
bad=copy.deepcopy(data);bad['routes'][0]['connections'][0]['coupled_validation']['status']='passed';cases.append(('unmeasured coupling',bad))
bad=copy.deepcopy(data);bad['routes'][0]['connections'][0]['reference_ids']=['unknown-reference'];cases.append(('citation',bad))
bad=copy.deepcopy(data);bad['routes'][0]['connections'][0]['connection_kind']='coupled-proof';cases.append(('connection kind',bad))
bad=copy.deepcopy(data);next(s for s in bad['routes'][0]['stages'] if s['id']=='first-principles-md')['example_ids']=['periodic-he-dft'];cases.append(('borrowed AIMD execution',bad))
bad=copy.deepcopy(data);next(s for s in bad['routes'][0]['stages'] if s['id']=='thermostat')['supplemental_ids']=['gaussian-mcmc'];cases.append(('unrelated MCMC used as thermostat evidence',bad))
bad=copy.deepcopy(data);next(s for s in bad['routes'][0]['stages'] if s['id']=='thermostat')['supplemental_ids']=['nonexistent-supplement'];cases.append(('unknown supplement',bad))
bad=copy.deepcopy(data);next(s for s in bad['routes'][0]['stages'] if s['id']=='thermostat')['supplemental_role']='coupled-proof';cases.append(('supplement promoted to coupled proof',bad))
bad=copy.deepcopy(data);stage=next(s for s in bad['routes'][0]['stages'] if s['id']=='first-principles-md');stage.update(supplemental_ids=['langevin-harmonic'],supplemental_role='scoped-component',supplemental_scope={'ja':'調和振動子','en':'Oscillator'});cases.append(('oscillator borrowed for full AIMD',bad))
bad=copy.deepcopy(data);bad['routes'][0]['coupled_validation']['supplemental_ids']=['langevin-harmonic'];cases.append(('supplement borrowed for whole route',bad))
bad=copy.deepcopy(data);next(e for e in bad['routes'][0]['connections'] if e['id']=='md-to-thermostat')['coupled_validation']['supplemental_ids']=['langevin-harmonic'];cases.append(('supplement borrowed for MD-thermostat connection',bad))
for ident in ['csvr-kinetic-kernel','csvr-langevin-harmonic','csvr-langevin-quartic']:
 bad=copy.deepcopy(data);stage=next(s for s in bad['routes'][0]['stages'] if s['id']=='first-principles-md');stage.update(supplemental_ids=[ident],supplemental_role='scoped-component',supplemental_scope={'ja':'古典要素','en':'Classical component'});cases.append(('CSVR component borrowed for AIMD: '+ident,bad))
 bad=copy.deepcopy(data);bad['routes'][0]['coupled_validation']['supplemental_ids']=[ident];cases.append(('CSVR component borrowed for full route: '+ident,bad))
for ident in ['schnakenberg-nonlinear','schnakenberg-pattern']:
 bad=copy.deepcopy(data);next(s for s in bad['routes'][0]['stages'] if s['id']=='thermostat')['supplemental_ids']=[ident];cases.append(('nonlinear biology borrowed as thermostat evidence: '+ident,bad))
 bad=copy.deepcopy(data);route=next(r for r in bad['routes'] if r['id']=='reaction-transport');route['coupled_validation']['supplemental_ids']=[ident];cases.append(('nonlinear biology borrowed for full transport route: '+ident,bad))
 bad=copy.deepcopy(data);route=next(r for r in bad['routes'] if r['id']=='reaction-transport');next(e for e in route['connections'] if e['id']=='rd-to-flow')['coupled_validation']['supplemental_ids']=[ident];cases.append(('nonlinear biology borrowed for flow coupling: '+ident,bad))
for label,bad in cases:
 try:b.validate_catalog(bad)
 except ValueError:pass
 else:raise AssertionError(label+' accepted')
print('validated source and rejected misleading catalogs')
`;
  assert.match(execFileSync('python3', ['-c', program], {cwd: root, encoding: 'utf8'}), /validated source/);
});

test('cross-field routes remain on the detailed explore page rather than competing with the three landing entrances', () => {
  const home = text('numerical-methods-atlas/index.html');
  const explore = text('numerical-methods-atlas/explore/index.html');
  for (const lang of ['ja', 'en']) {
    configureLocale(json('numerical-methods-atlas/locales/messages.json'), lang);
    const runtime = homeOverviewPage(json('numerical-methods-atlas/coverage.json'));
    assert.ok(runtime.includes(`/numerical-methods-atlas/explore/?lang=${lang}`));
    assert.ok(!runtime.includes('atlas-crossover-teaser'));
    for (const id of routeIDs) {
      const href = `/numerical-methods-atlas/connections/?lang=${lang}#${id}-${lang}`;
      assert.ok(explore.includes(href), 'detailed static route ' + href);
    }
    assert.ok(explore.includes(`/numerical-methods-atlas/connections/?lang=${lang}`), 'complete connections directory');
  }
  assert.equal((home.match(/class="atlas-crossover-teaser"/g) || []).length, 0);
  assert.equal((explore.match(/class="atlas-crossover-teaser"/g) || []).length, 2);
});

test('bilingual local search reaches the exact route fragments and global search indexes one canonical page', () => {
  const local = json('numerical-methods-atlas/home-search-index.json');
  const entries = local.entries.filter(entry => entry.kind === 'connection');
  for (const id of routeIDs) for (const lang of ['ja', 'en']) {
    const expected = `/numerical-methods-atlas/connections/?lang=${lang}#${id}-${lang}`;
    const entry = entries.find(entry => entry.routes[lang] === expected);
    assert.ok(entry, expected + ' indexed route');
    assert.ok(searchChapters(local, source.routes.find(route => route.id === id).title[lang], lang).slice(0, 5).some(row => row.url === expected), expected + ' title query');
  }
  const documents = json('search/index.json').documents.filter(document => document.url === '/numerical-methods-atlas/connections/');
  assert.equal(documents.length, 1);
  assert.equal(documents[0].lang, 'both');
});

test('search permits exact connection fragments while retaining legacy navigation boundaries', () => {
  const row = (url, kind = 'connection') => ({id: 'connection-needle', kind,
    title: {ja: 'needle', en: 'needle'}, headings: {ja: [], en: []}, keywords: ['needle'],
    routes: {ja: url, en: url}});
  for (const lang of ['ja', 'en']) for (const id of routeIDs) {
    const url = `/numerical-methods-atlas/connections/?lang=${lang}#${id}-${lang}`;
    assert.equal(searchChapters({entries: [row(url)]}, 'needle', lang)[0].url, url);
  }
  for (const url of [
    'javascript:alert(1)', 'https://evil.example/connections/?lang=en#dft-md-en',
    '//evil.example/connections/?lang=en#dft-md-en',
    '/numerical-methods-atlas/connections/../?lang=en#dft-md-en',
    '/numerical-methods-atlas/connections/?lang=en#unknown-en',
    '/numerical-methods-atlas/connections/?lang=en#dft-md-ja',
    '/numerical-methods-atlas/connections/?lang=ja#dft-md-ja',
    '/numerical-methods-atlas/connections/#dft-md-en',
    '/numerical-methods-atlas/code-and-data/examples/sod/?lang=en#dft-md-en',
  ]) assert.equal(searchChapters({entries: [row(url)]}, 'needle', 'en')[0].url, null, url);
  const connectionURL = '/numerical-methods-atlas/connections/?lang=en#dft-md-en';
  assert.equal(searchChapters({entries: [row(connectionURL, 'execution-example')]}, 'needle', 'en')[0].url, null);
});

test('published connections distinguish fixed force evidence and a local MD interface from unexecuted full routes', () => {
  assert.deepEqual(source.routes.map(route => route.id), routeIDs);
  assert.deepEqual(source.math_families.map(family => family.id), mathIDs);
  assert.deepEqual(published.routes.map(route => route.id), routeIDs);
  for (const route of source.routes) {
    const publicRoute = published.routes.find(item => item.id === route.id);
    const stageIDs = route.stages.map(stage => stage.id);
    assert.equal(new Set(stageIDs).size, stageIDs.length);
    for (const item of [route, ...route.connections]) {
      const measured = {'dft-to-forces': 'fixed-input', 'forces-to-md': 'interface-only'}[item.id];
      assert.equal(item.coupled_validation.status, measured || 'not-executed');
      assert.deepEqual(item.coupled_validation.example_ids, measured ? ['periodic-he-forces'] : []);
      for (const lang of ['ja', 'en']) assert.ok(item.coupled_validation.scope[lang].trim());
    }
    for (const edge of route.connections) {
      assert.ok(stageIDs.includes(edge.from) && stageIDs.includes(edge.to));
      for (const field of ['exchanged_quantity', 'shared_math', 'what_differs', 'validation_required', 'existing_evidence']) {
        for (const lang of ['ja', 'en']) assert.ok(edge[field][lang].trim(), `${edge.id}.${field}.${lang}`);
      }
    }
    for (const stage of route.stages) {
      const evidence = publicRoute.stages.find(item => item.id === stage.id).evidence;
      assert.deepEqual(evidence.examples.map(example => example.id), stage.example_ids, stage.id);
      assert.deepEqual(evidence.supplements.map(example => example.id), stage.supplemental_ids || [], stage.id);
      assert.deepEqual(evidence.methods.map(method => method.id), stage.method_ids, stage.id);
      for (const method of evidence.methods) {
        const canonical = publishedMethods.find(item => item.id === method.id);
        for (const field of ['name', 'status', 'reading', 'code_urls', 'test_urls']) assert.deepEqual(method[field], canonical[field], `${stage.id}/${method.id}.${field}`);
      }
      for (const example of evidence.examples) {
        const record = examples.find(item => item.id === example.id);
        assert.ok(record.method_ids.some(id => stage.method_ids.includes(id)), `${stage.id}/${example.id}`);
        assert.deepEqual(example.scope, record.scope);
        assert.equal(example.process_completed, true);
        assert.equal(example.numerical_checks_passed, true);
        localTarget(example.url);
      }
      for (const supplement of evidence.supplements) {
        assert.equal(supplement.source_mode, 'independently-extracted-supplement');
        assert.equal(supplement.group, supplement.id.startsWith('csvr-')?'thermostats':supplement.id.startsWith('schnakenberg-')?'biology':'models');
        assert.equal(supplement.numerical_checks_passed, true);
        assert.ok(Object.keys(supplement.checks).length > 0);
        assert.ok(Object.values(supplement.checks).every(value => value === true));
        assert.ok(supplement.method_ids.some(id => stage.method_ids.includes(id)));
        assert.ok(!examples.some(example => example.id === supplement.id));
        assert.equal(supplement.verification_receipt.all_cases_rerun, true);
        assert.notEqual(supplement.verification_receipt.url, published.verification_receipt);
        localTarget(supplement.url);
        for (const lang of ['ja', 'en']) {
          assert.ok(evidence.supplemental_scope[lang].trim());
          assert.ok(supplement.limits[lang].trim());
          localTarget(supplement.reading[lang]);
        }
      }
    }
  }
  const stage = id => published.routes.flatMap(route => route.stages).find(stage => stage.id === id);
  assert.deepEqual(stage('nuclear-forces').evidence.examples.map(example => example.id), ['periodic-he-forces']);
  assert.equal(stage('nuclear-forces').example_role, 'exact-stage');
  assert.equal(stage('nuclear-forces').evidence.stage_status, 'fixed-input');
  for (const id of ['first-principles-md', 'thermostat', 'reaction-diffusion', 'biological-fronts']) assert.deepEqual(stage(id).evidence.examples, [], id);
  assert.equal(stage('first-principles-md').evidence.stage_status, 'reading');
  for (const id of ['thermostat', 'reaction-diffusion', 'biological-fronts']) assert.equal(stage(id).evidence.stage_status, 'scoped-supplement', id);
  assert.deepEqual(stage('thermostat').evidence.supplements.map(row => row.id), ['langevin-harmonic','csvr-kinetic-kernel','csvr-langevin-harmonic','csvr-langevin-quartic']);
  assert.deepEqual(stage('reaction-diffusion').evidence.supplements.map(row => row.id), ['reaction-diffusion-fourier', 'turing-schnakenberg', 'schnakenberg-nonlinear', 'schnakenberg-pattern']);
  assert.deepEqual(stage('biological-fronts').evidence.supplements.map(row => row.id), ['turing-schnakenberg', 'fitzhugh-nagumo', 'schnakenberg-nonlinear', 'schnakenberg-pattern']);
  for (const id of ['fluid-transport', 'hartree-field']) {
    assert.equal(stage(id).example_role, 'component-only');
    assert.equal(stage(id).evidence.stage_status, 'component-only');
  }
  assert.deepEqual(stage('gravitational-field').example_ids, ['periodic-particles']);
});

test('rendered stage downloads come only from their explicit common examples or separately verified supplements', () => {
  for (const lang of ['ja', 'en']) for (const stage of source.routes.flatMap(route => route.stages)) {
    const markup = html.match(new RegExp(`<article\\b[^>]*id="${stage.id}-${lang}"[^>]*>[\\s\\S]*?</article>`))?.[0];
    assert.ok(markup, stage.id + '-' + lang);
    const links = [...markup.matchAll(/href="([^"]+)"/g)].map(match => new URL(decode(match[1]), origin));
    const codeLinks = links.filter(url => url.pathname.startsWith('/code/')).map(url => url.href);
    const records = stage.example_ids.map(id => examples.find(example => example.id === id));
    const supplements = published.routes.flatMap(route => route.stages).find(row => row.id === stage.id).evidence.supplements;
    const expectedZIPs = [...new Set([...records.map(example => example.release.download), ...supplements.map(example => example.code_download)])].sort();
    assert.deepEqual([...new Set(codeLinks.filter(url => new URL(url).pathname.endsWith('.zip')))].sort(), expectedZIPs, stage.id + ' registered ZIP');
    if (!records.length && !supplements.length) assert.deepEqual(codeLinks, [], stage.id + ' has no stage-specific implementation');
    const allowedCode = new Set([...records.flatMap(example => [example.inputs.url, example.release.download]),
      ...supplements.flatMap(example => [example.input, example.code_download, example.verification_receipt.url])]);
    for (const url of codeLinks) assert.ok(allowedCode.has(url), stage.id + ' must not borrow method-level file ' + url);
    for (const example of records) {
      assert.ok(links.some(url => url.href === example.inputs.url), example.id + ' fixed input');
      assert.ok(links.some(url => url.href === published.verification_receipt), example.id + ' existing rerun receipt');
      assert.ok(links.some(url => url.pathname === `/numerical-methods-atlas/code-and-data/examples/${example.id}/` && url.searchParams.get('lang') === lang), example.id + ' scoped common entry');
    }
    for (const example of supplements) {
      assert.ok(markup.includes(`data-supplemental-id="${example.id}"`), example.id + ' distinct source marker');
      assert.ok(links.some(url => url.href === example.input), example.id + ' fixed supplement input');
      assert.ok(links.some(url => url.href === example.verification_receipt.url), example.id + ' independent supplement receipt');
      assert.ok(links.some(url => url.pathname === `/numerical-methods-atlas/validation/${example.id}/` && url.searchParams.get('lang') === lang), example.id + ' scoped supplement entry');
    }
    const methodRows = [...markup.matchAll(/<li\b[^>]*\bdata-method-id="[^"]+"[^>]*>/g)].map(match => attributes(match[0]));
    for (const id of stage.method_ids) {
      const method = publishedMethods.find(item => item.id === id);
      assert.equal(methodRows.find(row => row['data-method-id'] === id)?.['data-method-status'], method.status, id + ' canonical state');
      assert.ok(links.some(url => url.pathname === `/numerical-methods-atlas/methods/${id}/` && url.searchParams.get('lang') === lang), id + ' method record');
    }
    if (stage.id === 'fixed-he') assert.ok(codeLinks.every(url => new URL(url).pathname.startsWith('/code/periodic-dft/')), 'fixed periodic-He stage has no atomic/H2 downloads');
  }
});

test('flow diagrams preserve every declared branch and link nodes to their actual stage states', () => {
  const expectedEdges = source.routes.flatMap(route => route.connections);
  assert.equal(expectedEdges.length, 9);
  for (const [id, from, targets] of [
    ['reaction-transport', 'reaction-diffusion', ['biological-fronts', 'reaction-only', 'fluid-transport']],
    ['poisson-fields', 'poisson-core', ['pressure-projection', 'hartree-field', 'gravitational-field']],
  ]) {
    const edges = source.routes.find(route => route.id === id).connections;
    assert.ok(edges.every(edge => edge.from === from), id + ' branches from its common mathematical core');
    assert.deepEqual(edges.map(edge => edge.to).sort(), targets.sort(), id + ' independent target branches');
  }
  const starts = [...html.matchAll(/<[a-z][a-z\d]*\b[^>]*\bdata-crossover-flow-edge="[^"]+"[^>]*>/g)];
  assert.equal(starts.length, 18, 'Nine declared connections in each language');
  for (const lang of ['ja', 'en']) {
    const seen = [];
    for (const start of starts) {
      const row = html.slice(start.index, html.indexOf('</li>', start.index) + 5);
      const nodes = [...row.matchAll(/<a\b([^>]*\bdata-crossover-flow-node="(?:from|to)"[^>]*)>([\s\S]*?)<\/a>/g)].map(match => ({attrs: attributes(match[1]), markup: match[2], text: decode(match[2].replace(/<[^>]+>/g, ' '))}));
      if (!nodes.some(node => node.attrs.href?.endsWith('-' + lang))) continue;
      const attrs = attributes(start[0]);
      const edge = expectedEdges.find(edge => edge.id === attrs['data-crossover-flow-edge']);
      assert.ok(edge, attrs['data-crossover-flow-edge']); seen.push(edge.id);
      assert.equal(attrs['data-from'], edge.from, edge.id + ' source');
      assert.equal(attrs['data-to'], edge.to, edge.id + ' target');
      assert.equal(nodes.length, 2, edge.id + ' has two stage nodes');
      for (const endpoint of ['from', 'to']) {
        const node = nodes.find(node => node.attrs['data-crossover-flow-node'] === endpoint);
        const stage = published.routes.flatMap(route => route.stages).find(stage => stage.id === edge[endpoint]);
        assert.equal(node?.attrs.href, '#' + stage.id + '-' + lang, edge.id + ' ' + endpoint + ' anchor');
        assert.equal(node.attrs['data-stage-status'], stage.evidence.stage_status, edge.id + ' ' + endpoint + ' state');
        assert.ok(node.text.includes(stage.title[lang]), edge.id + ' ' + endpoint + ' title');
        assert.ok(!node.markup.includes('crossover-flow-arrow'), 'The relation arrow is outside stage links');
        localTarget('/numerical-methods-atlas/connections/' + node.attrs.href);
      }
      const arrow = row.match(/<span\b[^>]*class="crossover-flow-arrow"[^>]*>([^<]+)<\/span>/)?.[1];
      assert.equal(arrow, ['component-reference', 'operator-correspondence'].includes(edge.connection_kind) ? '↔' : '→', edge.id + ' relation direction');
      assert.ok(row.includes(`href="#${edge.id}-${lang}"`), edge.id + ' detail link');
    }
    assert.deepEqual(seen.sort(), expectedEdges.map(edge => edge.id).sort(), lang);
  }
});

test('operator comparisons and DFT handoffs expose the separate scopes of their measured evidence', () => {
  const poisson = source.routes.find(route => route.id === 'poisson-fields');
  const dft = source.routes.find(route => route.id === 'dft-md');
  for (const lang of ['ja', 'en']) {
    for (const edge of poisson.connections) {
      assert.equal(edge.connection_kind, 'operator-correspondence');
      const markup = html.match(new RegExp(`<article\\b[^>]*id="${edge.id}-${lang}"[^>]*>[\\s\\S]*?</article>`))?.[0];
      assert.ok(markup);
      assert.ok(markup.includes(lang === 'ja' ? '対応関係を比較する範囲：' : 'Scope of the operator correspondence:'), edge.id + ' comparison scope');
      assert.ok(!markup.includes('Coupled execution: not performed') && !markup.includes('連成実行：未実施。'), edge.id + ' keeps its own validated physical example');
      assert.ok(decode(markup).includes(edge.coupled_validation.scope[lang]), edge.id + ' existing validation boundary');
    }
    for (const edge of dft.connections) {
      assert.equal(edge.connection_kind, 'handoff');
      const markup = html.match(new RegExp(`<article\\b[^>]*id="${edge.id}-${lang}"[^>]*>[\\s\\S]*?</article>`))?.[0];
      const status = {'dft-to-forces': 'fixed-input', 'forces-to-md': 'interface-only'}[edge.id] || 'not-executed';
      const labels = {
        'fixed-input': {ja: '固定例で接続を検証：', en: 'Connection validated for the fixed example:'},
        'interface-only': {ja: '局所的な接続のみ確認：', en: 'Local interface check only:'},
        'not-executed': {ja: '連成実行：未実施。', en: 'Coupled execution: not performed.'}
      };
      assert.ok(markup?.includes(labels[status][lang]), edge.id + ' scoped handoff');
      assert.ok(markup.includes(`data-coupled-status="${status}"`), edge.id + ' machine-readable evidence scope');
    }
  }
});

test('the complete bilingual guide works as static text and every precise reading fragment exists', () => {
  const roots = [...html.matchAll(/<section\b[^>]*\bdata-crossover-root\b[^>]*>/g)];
  assert.equal(roots.length, 2);
  for (const lang of ['ja', 'en']) {
    const section = html.slice(roots[lang === 'ja' ? 0 : 1].index, roots[lang === 'ja' ? 1 : 2]?.index || html.length);
    assert.equal((section.match(/\bdata-crossover-route(?:\s|>)/g) || []).length, 3);
    const form = section.match(/<form\b([^>]*\bdata-crossover-controls\b[^>]*)>/);
    assert.ok(form && 'hidden' in attributes(form[1]), lang + ' progressively enhanced controls');
    const select = section.match(/<select\b([^>]*\bdata-crossover-math\b[^>]*)>([\s\S]*?)<\/select>/);
    assert.ok(select);
    const attrs = attributes(select[1]);
    assert.ok(attrs.id && section.includes(`for="${attrs.id}"`), lang + ' visible filter label');
    assert.deepEqual([...select[2].matchAll(/<option[^>]*value="([^"]*)"/g)].map(match => match[1]), ['all', ...mathIDs]);
    const count = section.match(/<[a-z][^>]*\bdata-crossover-count\b[^>]*>/)?.[0];
    assert.equal(attributes(count).role, 'status');
    assert.equal(attributes(count)['aria-live'], 'polite');
    for (const id of routeIDs) {
      const tag = section.match(new RegExp(`<section\\b[^>]*id="${id}-${lang}"[^>]*>`))?.[0];
      assert.ok(tag, id + '-' + lang);
      assert.ok(!('hidden' in attributes(tag)), id + ' readable before script');
    }
    for (const route of source.routes) {
      for (const stage of route.stages) {
        assert.ok(section.includes(`id="${stage.id}-${lang}"`));
        for (const reading of stage.reading) {
          assert.ok(section.includes(`href="${reading.url[lang]}"`), reading.url[lang]);
          const url = localTarget(reading.url[lang]);
          assert.ok(url.pathname.includes('/' + lang + '/read/'));
        }
      }
      for (const edge of route.connections) assert.ok(section.includes(`id="${edge.id}-${lang}"`), edge.id);
    }
    for (const family of source.math_families) for (const reading of family.reading) localTarget(reading.url[lang]);
  }
});

test('citations and machine-readable provenance retain review scope and matching local source hashes', () => {
  const references = new Map(source.references.map(reference => [reference.id, reference]));
  for (const route of source.routes) for (const item of [route, ...route.connections]) {
    assert.ok(item.reference_ids.length);
    for (const id of item.reference_ids) {
      const reference = references.get(id); assert.ok(reference, id);
      assert.ok(reference.review_level);
      assert.ok(html.includes(`href="${reference.url}"`), id);
      assert.ok(text('numerical-methods-atlas/connections/index.md').includes(']('+reference.url+')'), id+' Markdown citation');
      for (const lang of ['ja', 'en']) assert.ok(reference.review[lang].trim());
    }
  }
  for (const [path, digest] of Object.entries(published.source_sha256)) assert.equal(createHash('sha256').update(readFileSync(new URL(path, root))).digest('hex'), digest, path);
  assert.deepEqual(Object.keys(published.supplemental_verification_receipts).sort(), ['biology','models','thermostats']);
  assert.ok(Object.keys(published.supplemental_source_sha256).length >= 5);
  for (const [path, digest] of Object.entries(published.supplemental_source_sha256)) assert.equal(createHash('sha256').update(readFileSync(new URL(path, root))).digest('hex'), digest, 'separate supplement '+path);
  for(const supplementReceipt of Object.values(published.supplemental_verification_receipts)){
   assert.equal(supplementReceipt.source_mode, 'independently-extracted-supplement');
   const supplementURL = new URL(supplementReceipt.url);
   assert.equal(supplementReceipt.sha256, createHash('sha256').update(readFileSync(new URL(supplementURL.pathname.slice(1), root))).digest('hex'));
  }
  const receipt = json(new URL(published.verification_receipt).pathname.slice(1));
  assert.equal(receipt.passed, true);
  assert.equal(receipt.registry_sha256, createHash('sha256').update(readFileSync(new URL(new URL(published.registry).pathname.slice(1), root))).digest('hex'));
});

test('supplement descriptions keep oscillator and zero-dimensional excitability evidence separate from coupled physical routes', () => {
  const stage = id => published.routes.flatMap(route => route.stages).find(item => item.id === id);
  const thermostat = stage('thermostat');
  assert.match(thermostat.gap.ja, /他10手法/);
  assert.match(thermostat.gap.en, /other 10 methods/);
  assert.match(thermostat.supplemental_scope.en, /one harmonic-oscillator degree of freedom/i);
  assert.match(thermostat.supplemental_scope.en, /same OBABO/);
  assert.match(thermostat.supplemental_scope.en, /quartic lambda=0.2/);
  assert.match(thermostat.gap.en,/bath-dependent correlations/);
  assert.match(stage('biological-fronts').supplemental_scope.ja, /0次元/);
  assert.match(stage('biological-fronts').supplemental_scope.en, /zero-dimensional/);
  assert.match(stage('biological-fronts').gap.en, /Fisher front speeds/);
  for (const lang of ['ja', 'en']) {
    assert.ok(html.includes(thermostat.supplemental_scope[lang]));
    assert.ok(html.includes(stage('biological-fronts').supplemental_scope[lang]));
  }
  for (const route of published.routes) {
    assert.equal(route.coupled_validation.status, 'not-executed');
    assert.deepEqual(route.coupled_validation.example_ids, []);
  }
  assert.equal(published.routes[0].connections.find(edge => edge.id === 'md-to-thermostat').coupled_validation.status, 'not-executed');
  assert.equal(published.routes[1].connections.find(edge => edge.id === 'rd-to-biology').connection_kind, 'model-application');
});
