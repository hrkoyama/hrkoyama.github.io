import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {configureLocale} from '../numerical-methods-atlas/i18n.js';
import {homeOverviewPage,renderHomeBrowse} from '../numerical-methods-atlas/home-overview.js';

const root=new URL('../',import.meta.url),origin='https://hrkoyama.github.io';
const read=path=>readFileSync(new URL(path,root),'utf8');
const json=path=>JSON.parse(read(path));
const sha=path=>createHash('sha256').update(readFileSync(new URL(path,root))).digest('hex');
const source='numerical-methods-atlas/assets/reference-solutions.json';
const historicalCases=json(source).cases,supplementSource='catalog/atlas-reference-supplements.json';
const cases=[...historicalCases,...json(supplementSource).cases],messages=json('numerical-methods-atlas/locales/messages.json');
const translations=new Map(Object.values(messages).map(entry=>[entry.en?.replace(/\s+/g,' ').trim(),entry]));
const decode=value=>value.replaceAll('&amp;','&').replaceAll('&quot;','"').replaceAll('&#x27;',"'").replaceAll('&#39;',"'").replaceAll('&lt;','<').replaceAll('&gt;','>');
const attrs=tag=>Object.fromEntries([...tag.matchAll(/([\w:-]+)="([^"]*)"/g)].map(match=>[match[1],decode(match[2])]));
const label=html=>decode(html.replace(/<[^>]+>/g,'')).trim();
function blocks(html,attribute,value){
  const result=[];
  for(const opening of html.matchAll(/<([a-z][\w:-]*)\b[^>]*>/gi)){
    const attributes=attrs(opening[0]);
    if(new RegExp('\\s'+attribute+'(?=\\s|/?>)').test(opening[0]))attributes[attribute]??='';
    if(!(attribute in attributes)||(value!==undefined&&attributes[attribute]!==value))continue;
    const tags=new RegExp('</?'+opening[1]+'\\b[^>]*>','gi');tags.lastIndex=opening.index+opening[0].length;
    let depth=1,closing;while((closing=tags.exec(html))){depth+=closing[0].startsWith('</')?-1:1;if(!depth)break;}
    assert.ok(closing);
    result.push({attributes,start:opening.index,end:tags.lastIndex,body:html.slice(opening.index+opening[0].length,closing.index)});
  }
  return result;
}
function withoutProblemRoutes(html){
  for(const block of blocks(html,'data-problem-routes').reverse())html=html.slice(0,block.start)+html.slice(block.end);
  return html;
}
const rendered=JSON.parse(execFileSync('python3',['-B','-c',String.raw`
import contextlib,hashlib,importlib.util,io,json,pathlib,shutil,sys,tempfile
site=pathlib.Path.cwd()
sys.path.insert(0,str(site/'scripts'))
from atlas_problem_routes import load_problem_routes
routes=load_problem_routes(site)
spec=importlib.util.spec_from_file_location('solutions_builder',site/'scripts/build-atlas-solutions.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
inputs=['numerical-methods-atlas/assets/reference-solutions.json','numerical-methods-atlas/locales/messages.json','styles/atlas-solutions.css','styles/atlas-problem-routes.css','catalog/atlas-reference-supplements.json']
before={name:hashlib.sha256((site/name).read_bytes()).hexdigest() for name in inputs}
with tempfile.TemporaryDirectory(prefix='atlas-solutions-fixture-') as temporary:
    root=pathlib.Path(temporary)
    for name in inputs:
        target=root/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(site/name,target)
    with contextlib.redirect_stdout(io.StringIO()):data=module.build(root,problem_routes=routes)
    output=root/'numerical-methods-atlas/solutions'
    first={path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in output.iterdir()}
    with contextlib.redirect_stdout(io.StringIO()):module.build(root,problem_routes=routes)
    second={path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in output.iterdir()}
    after={name:hashlib.sha256((site/name).read_bytes()).hexdigest() for name in inputs}
    print(json.dumps(dict(record=data,html=(output/'index.html').read_text(),markdown=(output/'index.md').read_text(),first=first,second=second,inputs_unchanged=before==after)))
`],{cwd:fileURLToPath(root),encoding:'utf8',maxBuffer:4*1024*1024}));

test('the saved-solution index derives every existing case and source hash without changing scientific inputs',()=>{
  assert.equal(historicalCases.length,18);
  assert.equal(sha(source),'c33118198faa7b35b4f66d7aad6353206f6d90c848f12e0a059874b91f897edc','the historical18 scientific references remain byte-identical');
  assert.deepEqual(cases.slice(historicalCases.length).filter(row=>!['weno-critical-profile','lake-at-rest-bed','swashes-bernoulli','ritter-dry-bed','ghia-re100','wall-mms','level-set-translation','level-set-rotation', 'kh-initial-growth', 'rt-initial-growth', 'circular-alfven-refinement', 'magnetic-loop-independent', 'postshock-orszag-tang', 'lshape-fem', 'annular-viscous-mms', 'poisson-neumann', 'poisson-robin', 'ale-nonuniform-transport', 'cgrid-rotating-wave', 'srhd-collision', 'srmhd-alfven', 'sem-poisson-2d', 'fr-periodic-advection','checkerboard-diffusion','rotated-anisotropic-diffusion','neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short','thermal-landau-damping','thermal-two-stream','pic-independent-spatial','dsmc-couette','dsmc-fourier','dsmc-planar-shock'].includes(row.id)).map(row=>row.id),['noh','sedov','double-mach','forward-step','isentropic-vortex','guderley','zalesak-rotation']);
  assert.equal(rendered.record.supplements_source_sha256,sha(supplementSource));
  assert.deepEqual(rendered.record.cases.map(row=>row.id),cases.map(row=>row.id));
  assert.equal(rendered.record.count,cases.length);
  assert.equal(rendered.record.source_sha256,sha(source));
  assert.equal(rendered.record.translations_source_sha256,sha('numerical-methods-atlas/locales/messages.json'));
  assert.equal(rendered.inputs_unchanged,true);
  assert.deepEqual(rendered.first,rendered.second,'a second generation is byte-for-byte identical');
  assert.deepEqual(Object.keys(rendered.first).sort(),['index.html','index.json','index.md']);
  const counts={};for(const row of cases)counts[row.kind]=(counts[row.kind]||0)+1;
  assert.deepEqual(rendered.record.counts,counts);
});

test('names, formulas, dimensions and analytic/semi-analytic/manufactured distinctions come from the same source records',()=>{
  const kindNames={'analytic':'Analytic reference','semi-analytic':'Semi-analytic reference','manufactured':'Manufactured solution','numerical-reference':'Finite-grid numerical reference'};
  for(const original of cases){
    const row=rendered.record.cases.find(row=>row.id===original.id);
    for(const field of ['kind','formula','dimension','model','field_type'])assert.deepEqual(row[field],original[field],original.id+'/'+field);
    for(const field of ['parameters','bounds','sources','components'])assert.deepEqual(row[field],original[field]);
    assert.deepEqual(row.title,{ja:translations.get(original.title).ja,en:original.title});
    assert.deepEqual(row.assumptions,{ja:translations.get(original.assumptions).ja,en:original.assumptions});
    assert.deepEqual(row.kind_label,translations.get(kindNames[original.kind]));
    assert.ok(rendered.markdown.includes(original.formula));
    assert.ok(rendered.markdown.includes(row.title.ja)&&rendered.markdown.includes(row.title.en));
  }
  assert.ok(rendered.markdown.includes(rendered.record.source_sha256));
});

test('each edition exposes all names, formulas and assumptions as visible static cards',()=>{
  for(const language of ['ja','en']){
    const section=blocks(rendered.html,'data-site-language',language)[0]?.body;
    assert.ok(section);
    const cards=blocks(section,'data-solution-id');
    assert.deepEqual(cards.map(card=>card.attributes['data-solution-id']),cases.map(row=>row.id));
    for(const [index,card]of cards.entries()){
      const row=rendered.record.cases[index];
      let original=withoutProblemRoutes(card.body);
      for(const citation of blocks(original,'class','solution-citations').reverse())original=original.slice(0,citation.start)+original.slice(citation.end);
      const body=label(original);
      assert.equal(card.attributes['data-solution-kind'],row.kind);
      assert.ok(body.includes(row.title[language])&&body.includes(row.formula)&&body.includes(row.assumptions[language]));
      assert.doesNotMatch(original,/<details\b|\shidden(?:\s|=|>)/,'the original reference name, formula and conditions stay visible before optional related-problem disclosures');
    }
    const taylor=cards.find(card=>card.attributes['data-solution-id']==='taylor-green');
    assert.ok(label(withoutProblemRoutes(taylor.body)).includes(rendered.record.cases.find(row=>row.id==='taylor-green').sampling_note[language]));
  }
  assert.match(rendered.record.cases.find(row=>row.id==='taylor-green').sampling_note.en,/x-slice at y = π\/4/);
  const ids=[...rendered.html.matchAll(/\sid="([^"]+)"/g)].map(match=>match[1]);
  assert.equal(ids.length,new Set(ids).size);
});

test('historical cards retain SPA views while reviewed supplements open their own validation and guide',()=>{
  for(const row of rendered.record.cases)for(const language of ['ja','en']){
    const view=new URL(row.view[language],origin);
    assert.equal(view.origin,origin);
    const original=cases.find(item=>item.id===row.id);
    if(original.view){
      assert.equal(row.view[language],original.view[language]);
      assert.equal(view.pathname,new URL(original.view[language],origin).pathname);
      assert.equal(view.hash,new URL(original.view[language],origin).hash);
    }else{
      assert.equal(view.pathname,'/numerical-methods-atlas/');
      assert.equal(view.hash,'#/exact-solutions?case='+row.id);
    }
    assert.equal(view.searchParams.get('lang'),language);
    const reading=new URL(row.reading[language],origin);
    assert.equal(reading.pathname,original.reading?new URL(original.reading[language],origin).pathname:`/numerical-methods-atlas/${language}/read/reference-solutions/`);
    if(original.reading)assert.equal(row.reading[language],original.reading[language]);
    assert.ok(existsSync(new URL(reading.pathname.slice(1)+'index.html',root)));
    assert.ok(rendered.html.includes(row.view[language])&&rendered.markdown.includes(origin+row.view[language]));
  }
});

test('static and client home add three secondary browse links below the books while keeping the three main entrances',()=>{
  const coverage=json('numerical-methods-atlas/coverage.json');
  const staticPages=JSON.parse(execFileSync(process.execPath,['scripts/render-atlas-landing.mjs'],{cwd:fileURLToPath(root),encoding:'utf8'}));
  const expected=['solutions','gallery','equations'];
  for(const language of ['ja','en']){
    configureLocale(messages,language);
    for(const html of [homeOverviewPage(coverage,'foundations'),staticPages[language]]){
      assert.deepEqual([...html.matchAll(/data-home-entry="([^"]+)"/g)].map(match=>match[1]),['goals','try','read']);
      const links=[...html.matchAll(/<a\b[^>]*data-home-browse="([^"]+)"[^>]*>/g)];
      assert.deepEqual(links.map(link=>link[1]),expected);
      assert.ok(html.indexOf('home-browse-card')>html.indexOf('home-reference-links'));
      for(const link of links){
        const url=new URL(attrs(link[0]).href,origin);
        assert.equal(url.pathname,'/numerical-methods-atlas/'+link[1]+'/');
        assert.equal(url.searchParams.get('lang'),language);
      }
    }
    assert.equal(staticPages.browse[language],renderHomeBrowse(language,{headingId:'explore-browse-title-'+language}));
    assert.doesNotMatch(staticPages.browse[language],/<details\b|\shidden(?:\s|=|>)/);
  }
  const asset='/numerical-methods-atlas/assets/field-taylor-green.png';
  assert.ok(renderHomeBrowse('en').includes(asset));
  assert.ok(existsSync(new URL(asset.slice(1),root)));
  assert.match(read('numerical-methods-atlas/gallery.js'),/file:'field-taylor-green[.]png',dimension:2/);
});

test('published home and explore retain visible direct links to all three browse indexes',()=>{
  const home=read('numerical-methods-atlas/index.html'),explore=read('numerical-methods-atlas/explore/index.html');
  for(const html of [home,explore])for(const language of ['ja','en'])for(const name of ['solutions','gallery','equations']){
    assert.ok(html.includes(`href="/numerical-methods-atlas/${name}/?lang=${language}"`),language+'/'+name);
    assert.ok(existsSync(new URL(`numerical-methods-atlas/${name}/index.html`,root)));
  }
  for(const language of ['ja','en'])assert.deepEqual(json('numerical-methods-atlas/explore/index.json').browse[language],Object.fromEntries(['solutions','gallery','equations'].map(name=>[name,`/numerical-methods-atlas/${name}/?lang=${language}`])));
});
