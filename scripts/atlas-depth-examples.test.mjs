import {supplementGroupIds,supplementCaseIds} from './fixtures/atlas-inventory.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {cpSync, mkdtempSync, readFileSync, rmSync, writeFileSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));
const bytes = path => readFileSync(join(root, path));
const text = path => bytes(path).toString();
const json = path => JSON.parse(text(path));
const sha = path => createHash('sha256').update(bytes(path)).digest('hex');
const catalog = json('catalog/atlas-depth-expansion.json');
const edition = group => catalog.groups.find(x => x.id === group).edition || catalog.edition;
const base = group => `code/validated-examples/${edition(group)}/${group}/`;
const entry = id => `numerical-methods-atlas/validation/${id}/`;
const groupIds = supplementGroupIds;
const expectedIds = [...supplementCaseIds].sort();
const metadata = group => {
  const value = json(base(group) + 'cases.json');
  return Array.isArray(value) ? value : value.cases;
};
const measured = group => json(base(group) + 'results/result.json');
const actualCases = groupIds.flatMap(group => metadata(group).map(item => ({group, item})));

test('optional figures require real manifest-bound PNGs and visible bilingual captions without affecting absent metadata', () => {
  const program = String.raw`
import base64,copy,hashlib,html,importlib.util,json,tempfile,sys
from pathlib import Path
sys.path.insert(0,str(Path.cwd()/'scripts'))
from atlas_depth_release import depth_additional_figures
spec=importlib.util.spec_from_file_location('depth_figure_builder','scripts/build-atlas-depth-examples.py')
builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)
with tempfile.TemporaryDirectory(prefix='atlas-additional-figures-') as temporary:
 directory=Path(temporary);(directory/'results').mkdir()
 png=base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+ip1sAAAAASUVORK5CYII=')
 caption={'ja':'追加の保存図：条件と誤差','en':'Additional saved figure: conditions and errors'}
 fields=['title','summary','assumptions','algorithm','validation','limits']
 case={'id':'fixture','references':[],'formulas':[],**{key:{'ja':'固定入力の試験','en':'Fixed-input fixture'} for key in fields}}
 case['additional_figures']=[{'file':'errors.png','caption':caption}]
 for name in ['fixture.png','errors.png','unlisted.png']:(directory/'results'/name).write_bytes(png)
 manifest={'files':{'results/'+name:hashlib.sha256(png).hexdigest() for name in ['fixture.png','errors.png']}}
 resolved=depth_additional_figures(directory,manifest,case)
 assert len(resolved)==1 and resolved[0]['width']==resolved[0]['height']==1
 data={'base':'/code/validated-examples/fixture/','directory':directory,'manifest':manifest,'verification':{'archive':{'file':'fixture.zip'}}}
 measured={'metrics':{'saved':0.},'checks':{'complete':True},'records':[{'n':1,'error':0.}]}
 for lang in ['ja','en']:
  rendered=builder.render_case(case,measured,data,lang,{})
  markdown=builder.markdown_case(case,measured,data,lang)
  assert '<figcaption>'+html.escape(caption[lang])+'</figcaption>' in rendered
  assert 'href="/code/validated-examples/fixture/results/errors.png"' in rendered
  assert 'https://hrkoyama.github.io/code/validated-examples/fixture/results/errors.png' in markdown and caption[lang] in markdown
  absent=copy.deepcopy(case);del absent['additional_figures']
  empty=copy.deepcopy(absent);empty['additional_figures']=[]
  assert builder.render_case(absent,measured,data,lang,{})==builder.render_case(empty,measured,data,lang,{})
  assert builder.markdown_case(absent,measured,data,lang)==builder.markdown_case(empty,measured,data,lang)
  assert 'data-validation-additional-figure' not in builder.render_case(absent,measured,data,lang,{})
 def rejects(value,expected_manifest=manifest):
  try:depth_additional_figures(directory,expected_manifest,value)
  except (AssertionError,ValueError,KeyError):return
  raise AssertionError('Invalid optional figure accepted')
 for name in ['../errors.png','/errors.png','results/errors.png','https://evil.example/errors.png','errors.svg','errors.txt','missing.png','unlisted.png']:
  bad=copy.deepcopy(case);bad['additional_figures'][0]['file']=name;rejects(bad)
 for captions in [{'ja':'説明'},{'ja':'説明','en':''},{'ja':'説明','en':42},None]:
  bad=copy.deepcopy(case);bad['additional_figures'][0]['caption']=captions;rejects(bad)
 bad=copy.deepcopy(case);bad['additional_figures']*=2;rejects(bad)
 bad=copy.deepcopy(case);bad['additional_figures'][0]['file']='fixture.png';rejects(bad)
 bad=copy.deepcopy(case);bad['additional_figures']=None;rejects(bad)
 altered=copy.deepcopy(manifest);altered['files']['results/errors.png']='a'*64;rejects(case,altered)
 for invalid in [png[:24],png[:52]+bytes([png[52]^1])+png[53:],png+b'<svg/>']:
  (directory/'results/errors.png').write_bytes(invalid)
  altered=copy.deepcopy(manifest);altered['files']['results/errors.png']=hashlib.sha256(invalid).hexdigest();rejects(case,altered)
 (directory/'results/errors.png').write_bytes(b'<svg xmlns="http://www.w3.org/2000/svg"/>')
 altered=copy.deepcopy(manifest);altered['files']['results/errors.png']=hashlib.sha256((directory/'results/errors.png').read_bytes()).hexdigest();rejects(case,altered)
 (directory/'results/errors.png').unlink();rejects(case)
 print('optional saved-figure contracts checked')
`;
  assert.match(execFileSync('python3', ['-B', '-c', program], {cwd: root, encoding: 'utf8', timeout: 30000}), /optional saved-figure contracts checked/);
});

test('forty original cases plus Noh and their independently dated releases stay distinct from the existing execution registry', () => {
  const index = json('numerical-methods-atlas/validation/index.json');
  assert.deepEqual(actualCases.map(x => x.item.id).sort(), expectedIds);
  assert.deepEqual(index.cases.map(x => x.id).sort(), expectedIds);
  assert.equal(index.case_count, 71);
  assert.equal(actualCases.filter(x => !['noh','noh-cartesian','sedov','double-mach','forward-step','low-mach','guderley','euler-positivity','zalesak','weno-critical','shallow-water','wall-flow','level-set', 'instability-growth', 'mhd-transport', 'mesh-boundary', 'moving-waves', 'relativistic', 'sem-fr'].includes(x.group)).length, 40);
  assert.equal(edition('noh'), '2026-11-23-r5');
  assert.ok(groupIds.filter(x => !['noh','noh-cartesian','sedov','double-mach','forward-step','low-mach','guderley','euler-positivity','zalesak','weno-critical','shallow-water','wall-flow','level-set', 'instability-growth', 'mhd-transport', 'mesh-boundary', 'moving-waves', 'relativistic', 'sem-fr'].includes(x)).every(x => edition(x) === '2026-11-22'));
  assert.equal(index.case_problem_ids['noh-shock'], 'noh');
  assert.deepEqual(index.groups.map(x => x.id).sort(), [...groupIds].sort());
  assert.equal(index.common_registry.example_count, 22);
  assert.equal(index.common_registry.modified_by_this_builder, false);
  assert.equal(index.common_registry.sha256, sha('numerical-methods-atlas/code-and-data/examples.json'));
  assert.equal(index.common_registry.sha256, '3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
  assert.deepEqual(index.case_problem_ids, catalog.case_problem_ids);
  assert.equal(index.case_problem_ids['glm-fourier-mode'], null);
  assert.equal(index.case_problem_ids.ewald, index.case_problem_ids.spme);
  for (const [path, hash] of Object.entries(index.source_sha256)) assert.equal(sha(path), hash, path);
  const html = text('numerical-methods-atlas/validation/index.html');
  assert.match(html, /共通22実行例の台帳とは別/);
  assert.match(html, /separately from the common 22-example registry/);
  assert.ok(html.includes(catalog.routine_policy.ja));
  assert.ok(html.includes(catalog.routine_policy.en));
});

test('frozen files, manifests and real independent-extraction receipts agree for every supplement', () => {
  for (const group of groupIds) {
    const prefix = base(group), manifest = json(prefix + 'source-manifest.json');
    const receipt = json(prefix + 'verification.json'), results = measured(group);
    assert.equal(manifest.family, 'depth-' + group);
    assert.equal(manifest.group, group);
    assert.equal(manifest.version, edition(group));
    assert.equal(receipt.edition, edition(group));
    assert.equal(receipt.passed, true);
    assert.equal(receipt.all_cases_rerun, true);
    assert.ok(Number.isInteger(receipt.passed_tests) && receipt.passed_tests > 0);
    assert.equal(receipt.passed_tests, receipt.tests);
    for (const name of ['failures', 'errors', 'skipped', 'returncode']) assert.equal(receipt[name], 0);
    assert.equal(receipt.source_manifest_sha256, sha(prefix + 'source-manifest.json'));
    assert.equal(receipt.archive.sha256, sha(prefix + receipt.archive.file));
    assert.equal(receipt.archive.bytes, bytes(prefix + receipt.archive.file).length);
    assert.ok(receipt.independent_rerun_seconds >= 0);
    for (const [path, hash] of Object.entries(manifest.files)) assert.equal(sha(prefix + path), hash, prefix + path);
    assert.equal(results.passed, true);
    assert.ok(Object.values(results.checks).every(value => value === true));
    assert.equal(results.input_sha256, sha(prefix + 'inputs.json'));
    assert.deepEqual(results.cases.map(x => x.id).sort(), metadata(group).map(x => x.id).sort());
    assert.deepEqual(receipt.case_ids.slice().sort(), metadata(group).map(x => x.id).sort());
    for (const item of results.cases) {
      assert.equal(item.passed, true, item.id);
      assert.ok(Object.keys(item.checks).length > 0 && Object.values(item.checks).every(value => value === true), item.id);
      assert.ok(Object.keys(item.metrics).length > 0 && item.records.length > 0, item.id);
    }
  }
});

test('each bilingual entry exposes its actual measurement, code, input, tests, figure and scientific limits', () => {
  for (const {group, item} of actualCases) {
    const record = json(entry(item.id) + 'index.json'), html = text(entry(item.id) + 'index.html');
    const markdown = text(entry(item.id) + 'index.md');
    assert.equal(record.id, item.id);
    assert.equal(record.group, group);
    assert.equal(record.edition, edition(group));
    assert.equal(record.problem_id, catalog.case_problem_ids[item.id]);
    assert.deepEqual(record.measured, measured(group).cases.find(x => x.id === item.id));
    assert.deepEqual(record.method_ids, item.method_ids);
    assert.deepEqual(record.additional_figures || [], item.additional_figures || []);
    assert.deepEqual(record.editorial_note, catalog.case_notes?.[item.id] || null);
    for (const lang of ['ja', 'en']) {
      assert.ok(html.includes(`data-site-language="${lang}"`));
      for (const field of ['title', 'summary', 'assumptions', 'algorithm', 'validation', 'limits']) {
        assert.ok(record[field][lang], item.id + '/' + field + '/' + lang);
        assert.ok(markdown.includes(record[field][lang]), item.id + '/' + field + '/' + lang);
      }
      if (record.editorial_note) assert.ok(markdown.includes(record.editorial_note[lang]));
      for (const figure of item.additional_figures || []) {
        const path = '/' + base(group) + 'results/' + figure.file;
        const caption = figure.caption[lang].replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#x27;');
        assert.ok(html.includes(`data-validation-additional-figure="${figure.file}"`));
        assert.ok(html.includes(`href="${path}"`) && html.includes(`<figcaption>${caption}</figcaption>`));
        assert.ok(markdown.includes('https://hrkoyama.github.io' + path) && markdown.includes(figure.caption[lang]));
      }
      assert.ok(html.includes(`/numerical-methods-atlas/${lang}/read/validation-${group}/#${item.id}`));
    }
    for (const suffix of ['inputs.json', 'results/result.json', 'verification.json', `results/${item.id}.png`])
      assert.ok(html.includes('/' + base(group) + suffix), item.id + '/' + suffix);
    assert.ok(html.includes(record.release.archive.file));
    assert.ok(record.release.test_urls.length > 0 && record.release.code_urls.some(url => url.endsWith('/run.py')));
    for (const url of record.release.test_urls) assert.ok(html.includes(url));
    assert.ok(html.includes('python -m pytest -q') && html.includes('python run.py --input inputs.json --output output'));
    assert.ok(html.includes('/LICENSING.md') && html.includes('/rights/'));
    assert.ok(!html.includes('katex-error'));
    assert.ok(html.includes('katex-mathml'), item.id);
    for (const reference of item.references) {
      assert.ok(reference.review_level);
      const review = reference.review_level.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#x27;');
      assert.ok(html.includes(review), item.id + '/' + reference.id);
      assert.ok(markdown.includes(reference.title));
    }
  }
});

test('all supplemental readings preserve measured records, real KaTeX output and machine-readable sibling documents', () => {
  for (const group of groupIds) for (const lang of ['ja', 'en']) {
    const path = `numerical-methods-atlas/${lang}/read/validation-${group}/`;
    const doc = json(path + 'index.json'), html = text(path + 'index.html'), md = text(path + 'index.md');
    assert.equal(doc.locale, lang);
    assert.equal(doc.group, group);
    assert.deepEqual(doc.measurements, measured(group).cases);
    assert.deepEqual(doc.case_ids, metadata(group).map(x => x.id));
    assert.ok(html.includes('/styles/atlas-validation.css?v='));
    assert.ok(html.includes('katex-mathml') && !html.includes('katex-error'));
    assert.ok(html.includes('class="validation-table"'));
    assert.ok(html.includes('index.json') && html.includes('index.md') && md.includes('$$'));
    for (const item of metadata(group)) {
      assert.ok(doc.headings.some(h => h.id === item.id));
      assert.ok(html.includes(`id="${item.id}"`));
      assert.ok(html.includes(`data-validation-case="${item.id}"`));
      const result = measured(group).cases.find(x => x.id === item.id);
      if (result.reference_records) {
        assert.ok(html.includes(item.id + ' reference records'));
        assert.ok(md.includes('reference_records'));
      }
    }
    for (const [source, hash] of Object.entries(doc.source_sha256)) assert.equal(sha(source), hash, source);
    const content = json(`numerical-methods-atlas/content.${lang}.json`);
    assert.equal(content['validation-' + group].html, doc.html);
  }
});

test('existing readings, unified bilingual contents and search preserve ten searchable chapters', () => {
  const search = json('numerical-methods-atlas/home-search-index.json');
  const entries = search.entries.filter(x => x.origin === 'depth-examples');
  assert.deepEqual(entries.map(x => x.id).sort(), groupIds.map(x => 'reading-validation-' + x).sort());
  for (const lang of ['ja', 'en']) {
    const contents = text(`numerical-methods-atlas/${lang}/read/index.html`);
    const contentsLinks = [...contents.matchAll(/<a\b[^>]*\bhref="([^"]+)"/g)].map(match => new URL(match[1], 'https://hrkoyama.github.io').pathname);
    const docs = json(`numerical-methods-atlas/content.${lang}.json`);
    assert.ok(docs['periodic-forces'] && docs['periodic-dft'] && docs['fdtd']);
    for (const group of groupIds) {
      assert.equal(contentsLinks.filter(path => path === `/numerical-methods-atlas/${lang}/read/validation-${group}/`).length, 1);
      assert.ok(entries.find(x => x.id === 'reading-validation-' + group).routes[lang].includes(`/read/validation-${group}/`));
    }
  }
  assert.deepEqual(json('numerical-methods-atlas/content.json'), json('numerical-methods-atlas/content.en.json'));
});

test('method-specific release resolver accepts real bindings and rejects unrelated borrowed cases', () => {
  const methods = json('catalog/atlas-methods.json').methods.filter(x => x.depth_release);
  assert.deepEqual([...new Set(methods.flatMap(x => [x.depth_release, ...(x.depth_additional_releases || [])].map(r => r.group)))].sort(), [...groupIds].sort());
  const program = String.raw`
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path.cwd()/'scripts'))
from atlas_depth_release import depth_release_record,depth_release_records
methods=json.load(sys.stdin)
for method in methods:
 records=depth_release_records(Path.cwd(),method)
 record=records[0]
 assert len(records)==1+len(method.get('depth_additional_releases',[]))
 assert set(record['case_ids'])==set(method['depth_release']['case_ids'])
 for scoped in records:
  assert scoped['code_urls'][0].endswith('/run.py')
  assert all(not u.endswith('/__init__.py') for u in scoped['code_urls'])
  assert scoped['test_urls'] and scoped['passed_tests']>0
  assert all(method['id'] in e['method_ids'] and e['measured']['passed'] for e in scoped['examples'])
bad={'id':'mcmc','status':'educational-example','depth_release':{'group':'foundations','edition':'${edition('foundations')}','case_ids':['sa-amg']}}
try:depth_release_record(Path.cwd(),bad)
except AssertionError:pass
else:raise AssertionError('Unrelated code was borrowed')
print('all bound releases checked')
`;
  const output = execFileSync('python3', ['-B', '-c', program], {cwd: root, input: JSON.stringify(methods), encoding: 'utf8', timeout: 30000});
  assert.match(output, /all bound releases checked/);
});

test('release resolver notices changed frozen source and archive after an earlier successful check', () => {
  const temporary = mkdtempSync(join(tmpdir(), 'atlas-depth-hashguard-'));
  try {
    const copied = join(temporary, base('foundations'));
    cpSync(join(root, base('foundations')), copied, {recursive: true});
    const program = String.raw`
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path.cwd()/'scripts'))
from atlas_depth_release import depth_release_record
temporary=Path(sys.argv[1]);directory=temporary/'${base('foundations')}'
m={'id':'amg','status':'educational-example','depth_release':{'group':'foundations','edition':'${edition('foundations')}','case_ids':['sa-amg']}}
depth_release_record(temporary,m)
path=directory/'solvers.py';original=path.read_bytes();path.write_bytes(original+b'\n# tampered\n')
try:depth_release_record(temporary,m)
except AssertionError:pass
else:raise AssertionError('Changed source was accepted')
path.write_bytes(original)
depth_release_record(temporary,m)
archive=directory/'atlas-foundations-${edition('foundations')}.zip';archive.write_bytes(archive.read_bytes()+b'changed')
try:depth_release_record(temporary,m)
except AssertionError:pass
else:raise AssertionError('Changed archive was accepted')
print('tamper guards rejected source and archive')
`;
    const output = execFileSync('python3', ['-B', '-c', program, temporary], {cwd: root, encoding: 'utf8', timeout: 30000});
    assert.match(output, /tamper guards rejected/);
  } finally {
    rmSync(temporary, {recursive: true, force: true});
  }
});

test('protocol links require a separate initial file or explicitly hash-proven unchanged pre-pilot input',()=>{
 const program=String.raw`
import copy,importlib.util,json,sys,tempfile
from pathlib import Path
sys.path.insert(0,'scripts')
spec=importlib.util.spec_from_file_location('depth_builder','scripts/build-atlas-depth-examples.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
with tempfile.TemporaryDirectory() as directory:
 p=Path(directory);history={'locked_before_primary_pilot_and_reference':True,'post_pilot_criteria_changes':False,'input_sha256':'1'*64}
 def write(value):(p/'protocol-history.json').write_text(json.dumps(value))
 data={'directory':p,'manifest':{'files':{'inputs.json':'1'*64,'protocol-history.json':'2'*64}}}
 write(history);assert m.initial_input_name(data)=='inputs.json'
 for change in [{'post_pilot_criteria_changes':True},{'locked_before_primary_pilot_and_reference':False},{'input_sha256':'3'*64}]:
  altered={**history,**change};write(altered)
  try:m.initial_input_name(data)
  except AssertionError:pass
  else:raise AssertionError('Unproven initial-input identity accepted')
 data['manifest']['files']['inputs-initial.json']='4'*64;assert m.initial_input_name(data)=='inputs-initial.json'
 del data['manifest']['files']['inputs-initial.json']
 archive='attempts/01/source/';(p/archive).mkdir(parents=True)
 contract={'declared_before_first_scientific_execution':True,'files_sha256':{'inputs.json':'5'*64}}
 (p/archive/'pre-run-contract.json').write_text(json.dumps(contract))
 data['manifest']['files'].update({archive+'inputs.json':'5'*64,archive+'pre-run-contract.json':'6'*64})
 assert m.initial_input_name(data)==archive+'inputs.json'
 for key,value in [('declared_before_first_scientific_execution',False),('files_sha256',{'inputs.json':'7'*64})]:
  (p/archive/'pre-run-contract.json').write_text(json.dumps({**contract,key:value}))
  try:m.initial_input_name(data)
  except AssertionError:pass
  else:raise AssertionError('Unproven archived initial-input identity accepted')
 del data['manifest']['files']['protocol-history.json'];assert m.initial_input_name(data) is None
print('Initial-input links preserve both original-copy and unchanged-input protocols')
`;
 assert.match(execFileSync('python3',['-B','-c',program],{cwd:root,encoding:'utf8',timeout:30000}),/preserve both/);
});
