import test from 'node:test';
import assert from 'node:assert/strict';
import {existsSync,readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {searchChapters} from '../numerical-methods-atlas/home-search.js';

const root=new URL('../',import.meta.url),origin='https://hrkoyama.github.io';
const read=path=>readFileSync(new URL(path,root),'utf8');
const json=path=>JSON.parse(read(path));
const digest=path=>createHash('sha256').update(readFileSync(new URL(path,root))).digest('hex');
const decode=value=>value.replaceAll('&amp;','&').replaceAll('&quot;','"').replaceAll('&#x27;',"'").replaceAll('&#39;',"'").replaceAll('&lt;','<').replaceAll('&gt;','>');
const attrs=tag=>Object.fromEntries([...tag.matchAll(/([\w:-]+)="([^"]*)"/g)].map(match=>[match[1],decode(match[2])]));
const inventory=json('catalog/atlas-test-problems.json').problems;
const mapping=json('catalog/atlas-problem-links.json');
const index=json('numerical-methods-atlas/problems/index.json');
const gallery=json('numerical-methods-atlas/gallery/index.json');
const equations=json('catalog/atlas-equations.json').equations;
const references=json('numerical-methods-atlas/solutions/index.json').cases;
const methods=json('catalog/atlas-methods.json').methods;
const common=json('catalog/atlas-execution-examples.json').examples;
const supplements=json('catalog/atlas-depth-expansion.json').case_problem_ids;
const byId=rows=>new Map(rows.map(row=>[row.id,row]));

test('the constructed MHD equilibrium has its own hub and keeps active-cleaning controls outside physical problems',()=>{
  const physical='advected-magnetostatic-equilibrium';
  const source=mapping.problems.find(row=>row.id===physical);
  const problem=index.problems.find(row=>row.id===physical);
  assert.deepEqual(source.equation_ids,['mhd']);
  assert.deepEqual(source.method_ids,['ct','glm']);
  assert.deepEqual(source.references,[],'no different reference-library problem is borrowed');
  assert.deepEqual(problem.executions.map(row=>row.id),['ct-glm-smooth-convergence']);
  assert.deepEqual(problem.methods.map(row=>row.id),['ct','glm']);
  assert.deepEqual(problem.formulations.map(row=>row.id),['supplement-ct-glm-smooth-convergence']);
  assert.ok(problem.executions[0].download.includes('/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip'));
  assert.ok(problem.reference_note.en.includes('not a separate spatial solver'));
  assert.ok(problem.method_note.en.includes('whole discretizations'));
  assert.equal(supplements['ct-glm-constraint-control'],null);
  assert.ok(!index.problems.some(row=>row.id==='ct-glm-constraint-control'));
  const ot=index.problems.find(row=>row.id==='orszag-tang');
  const otExecutions=ot.executions.map(row=>row.id);
  assert.deepEqual(otExecutions.filter(id=>id!=='postshock-orszag-tang'),['ct-glm-independent','ct-glm-ot-convergence']);
  assert.deepEqual(otExecutions.filter(id=>id==='postshock-orszag-tang'),['postshock-orszag-tang']);
});

test('conditioning releases extend only their three algebraic or integral families and keep AMG diagnostics outside PDE evidence',()=>{
  const additions=[['matrix-factorization','qr-svd','qr-svd-factorization','qr-svd-conditioning'],['krylov-spectrum','eigensolvers','krylov-eigenvalues','krylov-eigen-conditioning'],['quadrature-moments','quadrature','gauss-adaptive-quadrature','quadrature-conditioning']];
  for(const [id,method,previous,added] of additions){
    const source=mapping.problems.find(row=>row.id===id),problem=index.problems.find(row=>row.id===id);
    assert.deepEqual(source.equation_ids,[],'algebraic or integral checks do not invent a PDE equation');
    assert.deepEqual(source.references,[],'no distinct physical reference-library problem is borrowed');
    assert.deepEqual(source.method_ids,[method]);
    assert.deepEqual(problem.executions.map(row=>row.id),[previous,added]);
    assert.deepEqual(problem.methods.map(row=>row.id),[method]);
    assert.deepEqual(problem.formulations.map(row=>row.id),['supplement-'+previous,'supplement-'+added]);
    const execution=problem.executions.find(row=>row.id===added);
    assert.ok(execution.download.includes('/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip'));
    for(const lang of ['ja','en'])assert.ok(execution.guide[lang].includes('/validation/'+added+'/?lang='+lang));
  }
  assert.equal(supplements['amg-conditioning'],null);
  assert.ok(!index.problems.some(row=>row.id==='amg-conditioning'));
  assert.ok(!index.problems.some(row=>row.executions.some(execution=>execution.id==='amg-conditioning')));
  const poisson=index.problems.find(row=>row.id==='poisson-2d-sine');
  assert.ok(poisson.executions.some(row=>row.id==='sa-amg'));
  assert.match(poisson.reference_note.en,/not borrowed as evidence/);
});

test('particle and transport checks extend five existing targets while keeping kernels, backgrounds and reference roles explicit',()=>{
  const bindings=[
    ['neutral-periodic-charges',['ewald','spme'],['ewald-convergence','spme-convergence'],['ewald','pme','spme']],
    ['logarithmic-particles',['fmm'],['fmm-convergence'],['fmm']],
    ['cold-plasma-pic',['pic'],['pic-conservation'],['pic']],
    ['maxwell-collisions',['dsmc'],['dsmc-statistics'],['dsmc']],
    ['absorbing-slab',['radiation-transport'],['radiation-convergence'],['radiation-transport']],
  ];
  for(const [id,previous,added,methodIds] of bindings){
    const source=mapping.problems.find(row=>row.id===id),problem=index.problems.find(row=>row.id===id);
    assert.deepEqual(source.method_ids,methodIds);
    assert.deepEqual(source.references,[],'no different physical reference-library case is borrowed');
    assert.deepEqual(problem.executions.map(row=>row.id),[...previous,...added]);
    assert.deepEqual(problem.formulations.map(row=>row.id),[...previous,...added].map(value=>'supplement-'+value));
    for(const addedId of added){
      assert.equal(supplements[addedId],id);
      const execution=problem.executions.find(row=>row.id===addedId);
      assert.ok(execution.download.includes('/particle-transport/atlas-particle-transport-2026-11-22.zip'));
      for(const language of ['ja','en'])assert.ok(execution.guide[language].includes('/validation/'+addedId+'/?lang='+language));
    }
  }
  assert.match(mapping.problems.find(row=>row.id==='neutral-periodic-charges').reference_note.en,/original Lagrange PME and exact momentum conservation are not claimed/);
  assert.match(mapping.problems.find(row=>row.id==='logarithmic-particles').reference_note.en,/neither monotonic error with depth/);
  assert.match(mapping.problems.find(row=>row.id==='cold-plasma-pic').reference_note.en,/stationary background ions/);
  assert.match(mapping.problems.find(row=>row.id==='maxwell-collisions').reference_note.en,/Collision rounds are not physical time/);
  assert.match(mapping.problems.find(row=>row.id==='absorbing-slab').reference_note.en,/does not extend to scattering/);
});

function blocks(html,attribute,value){
  const result=[];
  for(const opening of html.matchAll(/<([a-z][\w:-]*)\b[^>]*>/gi)){
    const attributes=attrs(opening[0]);
    if(!(attribute in attributes)||(value!==undefined&&attributes[attribute]!==value))continue;
    const name=opening[1],tags=new RegExp('</?'+name+'\\b[^>]*>','gi');
    tags.lastIndex=opening.index+opening[0].length;
    let depth=1,closing;
    while((closing=tags.exec(html))){
      depth+=closing[0].startsWith('</')?-1:1;
      if(!depth)break;
    }
    assert.ok(closing,'balanced '+attribute+'='+attributes[attribute]);
    result.push({attributes,body:html.slice(opening.index+opening[0].length,closing.index),opening:opening[0]});
  }
  return result;
}

function local(href,base=origin){
  const url=new URL(href,base);
  assert.equal(url.origin,origin,href);
  const path=url.pathname.slice(1)+(url.pathname.endsWith('/')?'index.html':'');
  assert.ok(existsSync(new URL(path,root)),href);
  if(url.hash&&!url.hash.startsWith('#/')&&path.endsWith('.html')){
    let fragment;try{fragment=decodeURIComponent(url.hash.slice(1));}catch{assert.fail('invalid fragment: '+href);}
    assert.ok(read(path).includes(`id="${fragment}"`),href+' existing fragment');
  }
  return url;
}

function links(html){
  return [...html.matchAll(/<a\b[^>]*href="([^"]+)"[^>]*>/g)].map(match=>decode(match[1]));
}

test('the reviewed problem links and generated hub inventory cover every physical problem exactly once',()=>{
  assert.equal(inventory.length,102);
  const expected=inventory.map(row=>row.id);
  for(const rows of [mapping.problems,index.problems]){
    assert.deepEqual(rows.map(row=>row.id),expected);
    assert.equal(new Set(rows.map(row=>row.id)).size,expected.length);
  }
  for(const problem of index.problems){
    const record=json(`numerical-methods-atlas/problems/${problem.id}/index.json`);
    assert.equal(record.id,problem.id);
    assert.deepEqual(record.name,byId(inventory).get(problem.id).name);
    for(const field of ['equations','references','methods','executions','code_checks'])assert.deepEqual(record[field],problem[field]);
    const html=read(`numerical-methods-atlas/problems/${problem.id}/index.html`);
    for(const language of ['ja','en']){
      const editions=blocks(html,'data-site-language',language);
      assert.equal(editions.length,1,problem.id+'/'+language+' edition');
      const sections=blocks(editions[0].body,'data-problem-section');
      assert.deepEqual(sections.map(section=>section.attributes['data-problem-section']),['equations','references','methods','code']);
      assert.ok(sections.every(section=>!/<details\b|\shidden(?:\s|=|>)/.test(section.opening)),'the four destinations are visible without interaction');
      assert.ok(editions[0].body.includes(problem.name[language]));
    }
  }
});

test('all problem pages have current bilingual search records and named problem results retain their own kind label',()=>{
  const search=json('numerical-methods-atlas/home-search-index.json');
  const records=search.entries.filter(entry=>entry.kind==='problem');
  assert.deepEqual(records.map(entry=>entry.id),inventory.map(problem=>'problem-'+problem.id));
  assert.equal(new Set(records.map(entry=>entry.id)).size,inventory.length);
  const global=json('search/index.json').documents;
  for(const problem of index.problems){
    const record=records.find(entry=>entry.id==='problem-'+problem.id);
    assert.equal(record.origin,'public-problem-registry');
    const html=read(`numerical-methods-atlas/problems/${problem.id}/index.html`);
    const documents=global.filter(entry=>entry.url===`/numerical-methods-atlas/problems/${problem.id}/`);
    assert.equal(documents.length,1,problem.id+' has one published global-search page');
    for(const language of ['ja','en']){
      const edition=blocks(html,'data-site-language',language)[0].body;
      const title=decode(edition.match(/<h1\b[^>]*>([\s\S]*?)<\/h1>/)?.[1]?.replace(/<[^>]+>/g,'')||'').trim();
      assert.equal(title,problem.name[language]);
      assert.equal(record.title[language],title,'search uses the published localized name');
      const url=local(record.routes[language]);
      assert.equal(url.pathname,`/numerical-methods-atlas/problems/${problem.id}/`);
      assert.equal(url.searchParams.get('lang'),language);
      assert.ok((language==='ja'?documents[0].title:documents[0].titleEn).includes(title));
    }
  }
  for(const [id,query]of [['sod','Sod'],['gaussian-mcmc','gaussian-mcmc']])for(const language of ['ja','en']){
    const result=searchChapters(search,query,language).find(entry=>entry.id==='problem-'+id);
    assert.ok(result,query+'/'+language+' includes the problem independently of method/run ranking');
    assert.equal(result.kind,'problem');
    assert.equal(result.badge,language==='ja'?'テスト問題':'Test problem');
    assert.equal(result.title,byId(inventory).get(id).name[language]);
    assert.equal(result.url,`/numerical-methods-atlas/problems/${id}/?lang=${language}`);
  }
});

test('every gallery image and problem title opens its hub while the original run badges remain direct',()=>{
  const html=read('numerical-methods-atlas/gallery/index.html');
  for(const item of gallery.items)for(const language of ['ja','en']){
    const tile=blocks(html,'id',item.id+'-'+language)[0];
    assert.ok(tile,item.id+'/'+language);
    const image=tile.body.match(/<a\b[^>]*class="gallery-image-link"[^>]*>/)?.[0];
    const heading=tile.body.match(/<h2\b[^>]*>[\s\S]*?<\/h2>/)?.[0];
    assert.ok(image&&heading);
    for(const href of [attrs(image).href,links(heading)[0]]){
      const url=local(href);
      assert.equal(url.pathname,`/numerical-methods-atlas/problems/${item.id}/`);
      assert.equal(url.searchParams.get('lang'),language);
    }
    assert.equal(attrs(image)['aria-label'],item.name[language]+(language==='ja'?'の方程式・参照解・手法・コードへ':': open equations, references, methods and code'));
    if(item.execution_entry){
      const badge=tile.body.match(/<p class="gallery-execution-badge">([\s\S]*?)<\/p>/)?.[1];
      assert.ok(badge&&links(badge).includes(item.execution_entry.url[language]));
    }
    for(const extra of item.supplemental_execution_entries){
      const badge=blocks(tile.body,'data-supplemental-execution',extra.id)[0];
      assert.ok(badge&&links(badge.body).includes(extra.url[language]));
    }
  }
});

test('hub equations, references and methods use only explicitly reviewed identities and real public destinations',()=>{
  const equationMap=byId(equations),referenceMap=byId(references),methodMap=byId(methods),catalog=byId(mapping.problems);
  for(const problem of index.problems){
    const reviewed=catalog.get(problem.id),markdown=read(`numerical-methods-atlas/problems/${problem.id}/index.md`);
    assert.deepEqual(problem.equations.map(row=>row.id),reviewed.equation_ids);
    assert.deepEqual(problem.references.map(row=>row.id),reviewed.references.map(row=>row.id));
    const executionMethods=[...new Set(problem.executions.flatMap(row=>row.method_ids))].sort();
    assert.deepEqual(problem.methods.map(row=>row.id),[...new Set([...reviewed.method_ids,...executionMethods])]);
    for(const equation of problem.equations){
      assert.deepEqual(equation.formula,equationMap.get(equation.id).formula);
      assert.ok(markdown.includes(equation.id));
    }
    for(const reference of problem.references){
      const source=referenceMap.get(reference.id),binding=reviewed.references.find(row=>row.id===reference.id);
      assert.ok(source);
      assert.equal(reference.relation,binding.relation);
      assert.ok(['same-problem','related-model'].includes(reference.relation));
      assert.deepEqual(reference.note,binding.note);
      assert.equal(reference.kind,source.kind);
      assert.deepEqual(reference.title,source.title);
      for(const language of ['ja','en']){assert.ok(markdown.includes(reference.url[language]),reference.id+' explicit reference destination');assert.ok(markdown.includes(reference.title[language]),reference.id+' localized reference title');}
    }
    for(const method of problem.methods){
      assert.equal(method.status,methodMap.get(method.id).status);
      assert.deepEqual(method.name,methodMap.get(method.id).name);
      assert.ok(['execution','related'].includes(method.role));
      assert.ok(markdown.includes(method.id));
    }
    for(const language of ['ja','en']){
      assert.ok(markdown.includes(problem.name[language]));
      const html=blocks(read(`numerical-methods-atlas/problems/${problem.id}/index.html`),'data-site-language',language)[0].body;
      for(const href of links(html))local(href,problem.hub[language]);
    }
  }
});

test('fixed-input executions come only from each problem’s common or explicitly bound supplemental cases',()=>{
  for(const problem of index.problems){
    const commonCases=common.filter(row=>row.problem_id===problem.id);
    const extraIds=Object.entries(supplements).filter(([,problemId])=>problemId===problem.id).map(([id])=>id);
    assert.deepEqual(problem.executions.map(row=>row.id).sort(),[...commonCases.map(row=>row.id),...extraIds].sort(),problem.id+' has no borrowed execution case');
    const allowedMethods=new Set();
    for(const execution of problem.executions){
      const shared=commonCases.find(row=>row.id===execution.id);
      if(shared)assert.deepEqual(execution.method_ids,shared.method_ids);
      for(const method of execution.method_ids)allowedMethods.add(method);
      const guides=typeof execution.guide==='string'?[execution.guide]:Object.values(execution.guide||{});
      assert.ok(guides.length,execution.id+' execution guide');
      for(const href of guides){
        const url=local(href);
        assert.equal(url.pathname,shared?`/numerical-methods-atlas/code-and-data/examples/${execution.id}/`:`/numerical-methods-atlas/validation/${execution.id}/`);
      }
      for(const field of ['input','download','verification','manifest']){
        assert.equal(typeof execution[field],'string',execution.id+'/'+field);
        local(execution[field]);
      }
      for(const href of [...execution.code_urls,...execution.test_urls])local(href);
    }
    for(const method of problem.methods.filter(row=>row.role==='execution'))assert.ok(allowedMethods.has(method.id),problem.id+'/'+method.id+' is backed by a matching execution');
    for(const check of problem.code_checks){
      const url=local(check.url),path=url.pathname.slice(1),symbol=check.symbol.split('::').at(-1).split('[')[0].split('.').at(-1);
      assert.ok(path.endsWith('.py'));
      assert.equal(check.path.replace(/^\//,''),path);
      assert.ok(read(path).match(new RegExp('\\bdef\\s+'+symbol.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\s*\\(')),check.symbol+' is an actual published test function');
      assert.ok(check.commands?.length&&check.run_from,problem.id+' includes runnable context for its raw test');
      if(check.download)local(check.download);
    }
  }
});

test('problems outside the physical equation registry retain explicit scope notes and genuine execution formulations',()=>{
  const discovery=byId(json('catalog/atlas-execution-discovery.json').examples);
  for(const problem of index.problems){
    const markdown=read(`numerical-methods-atlas/problems/${problem.id}/index.md`);
    if(!problem.equations.length){
      assert.ok(problem.equation_note.ja?.trim()&&problem.equation_note.en?.trim(),problem.id+' explains the unmapped model');
      for(const language of ['ja','en'])assert.ok(markdown.includes(problem.equation_note[language]));
    }
    for(const formulation of problem.formulations){
      assert.ok(['common','supplement'].includes(formulation.source));
      const executionId=formulation.id.replace(new RegExp('^'+formulation.source+'-'),'');
      assert.ok(problem.executions.some(row=>row.id===executionId),'a displayed formulation belongs to this problem’s execution');
      assert.ok(formulation.latex.length&&formulation.latex.every(value=>typeof value==='string'&&value.trim()));
      if(formulation.source==='common'){
        assert.deepEqual(formulation.latex,discovery.get(executionId).formula.latex);
        assert.deepEqual(formulation.note,discovery.get(executionId).formula.note);
      }
      for(const tex of formulation.latex)assert.ok(markdown.includes(tex));
      const html=read(`numerical-methods-atlas/problems/${problem.id}/index.html`);
      for(const language of ['ja','en']){
        const edition=blocks(html,'data-site-language',language)[0].body;
        const entry=blocks(edition,'data-formulation-id',formulation.id)[0];
        assert.ok(entry&&entry.body.includes('katex'),'execution math is statically typeset in both editions');
      }
    }
  }
});

test('square advection, Sod, Taylor–Green, Bratu and MCMC retain distinct reference and execution meanings',()=>{
  const problems=byId(index.problems);
  const square=problems.get('advection-square');
  assert.equal(square.executions.length,0,'a nearby sine-wave execution is not a square-wave execution');
  assert.ok(square.references.every(reference=>reference.relation!=='same-problem'),'a sine-wave formula is not the same initial-value problem');
  const sod=problems.get('sod');
  const sodReference=sod.references.find(reference=>reference.id==='euler-sod');
  assert.equal(sodReference?.relation,'related-model','matching physical states do not imply identical point/cell-mean samples');
  assert.match(sodReference.note.en,/sampling|cell|point/i);
  assert.ok(sod.executions.some(execution=>execution.id==='sod'));
  const taylor=problems.get('taylor-green');
  assert.ok(taylor.references.some(reference=>reference.id==='taylor-green'));
  assert.match(JSON.stringify(taylor.references)+JSON.stringify(taylor.reference_note),/π\/4/,'the stored reference is explicitly a fixed-y slice');
  for(const id of ['bratu','gaussian-mcmc','mcmc-bimodal-mixture']){
    const problem=problems.get(id);
    assert.equal(problem.references.length,0,id+' is absent from the separate eighteen-case reference library');
    assert.ok(problem.reference_note.ja?.trim()&&problem.reference_note.en?.trim());
    assert.ok(problem.executions.length,id+' still has its own verified numerical/reference data');
  }
  assert.deepEqual(problems.get('bratu').executions.map(row=>row.id),['bratu']);
  const bratuMethods=byId(problems.get('bratu').methods);
  assert.equal(bratuMethods.get('newton')?.role,'execution','Newton remains the method used by the common Bratu solve');
  for(const id of ['automatic-differentiation','adjoint','optimization'])assert.equal(bratuMethods.get(id)?.role,'related',id+' is a related derivative or inverse-problem edition');
  assert.deepEqual(problems.get('gaussian-mcmc').executions.map(row=>row.id),['gaussian-mcmc']);
  assert.deepEqual(problems.get('mcmc-bimodal-mixture').executions.map(row=>row.id),['mcmc-multimodal-mixing']);
});

test('uniform-source Poisson uses its actual multigrid comparison test and publishes the reviewed correction',()=>{
  const id='poisson-2d-uniform',problem=byId(index.problems).get(id),reviewed=byId(mapping.problems).get(id);
  assert.deepEqual(problem.code_checks.map(check=>check.symbol),['test_multigrid_removes_smooth_error_faster_than_relaxation']);
  assert.equal(problem.code_checks[0].path,reviewed.code_evidence[0].path);
  assert.deepEqual(problem.code_checks[0].note,reviewed.code_evidence[0].note);
  assert.match(problem.code_checks[0].note.en,/uniform forcing f=1/);
  const markdown=read(`numerical-methods-atlas/problems/${id}/index.md`),html=read(`numerical-methods-atlas/problems/${id}/index.html`);
  for(const language of ['ja','en']){
    const edition=blocks(html,'data-site-language',language)[0].body;
    const code=blocks(edition,'data-problem-section','code')[0].body;
    assert.ok(code.includes(problem.code_checks[0].note[language]),'the corrected evidence has a visible explanation');
    assert.ok(markdown.includes(problem.code_checks[0].note[language]));
  }
});

const python=process.env.ATLAS_INDEX_PYTHON||'python3';
const importHelper=String.raw`
import importlib.util,json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve();sys.path.insert(0,str(root/'scripts'))
spec=importlib.util.spec_from_file_location('problem_links',root/'scripts/atlas_problem_links.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
`;

test('raw-test commands start in the real ZIP top directory and point to the same archived test file',()=>{
  const checks=index.problems.flatMap(problem=>problem.code_checks).filter(check=>check.download);
  assert.ok(checks.length);
  const output=execFileSync(python,['-B','-c',importHelper+String.raw`
from contextlib import ExitStack
from urllib.parse import urlsplit
import zipfile
checks=json.loads(sys.argv[2]);archives={}
with ExitStack() as stack:
    for check in checks:
        download=check['download']
        if download not in archives:
            archive=stack.enter_context(zipfile.ZipFile(root/urlsplit(download).path.lstrip('/')))
            members={name for name in archive.namelist() if not name.endswith('/')}
            prefixes={pathlib.PurePosixPath(name).parts[0] for name in members}
            assert len(prefixes)==1,download
            archives[download]=(archive,members,next(iter(prefixes))+'/')
        archive,members,prefix=archives[download]
        assert check['run_from']==prefix,(check['path'],check['run_from'],prefix)
        public_base=pathlib.PurePosixPath(urlsplit(download).path).parent.as_posix().lstrip('/')
        relative=pathlib.PurePosixPath(check['path']).relative_to(public_base).as_posix()
        member=prefix+relative
        assert member in members,(download,member)
        assert archive.read(member)==(root/check['path']).read_bytes(),check['path']
print(str(len(checks))+' archive working directories checked')
`,fileURLToPath(root),JSON.stringify(checks)],{encoding:'utf8',maxBuffer:4*1024*1024});
  assert.match(output,new RegExp('^'+checks.length+' archive working directories checked'));
});

test('loading the navigation graph preserves every existing scientific catalog and preview receipt',()=>{
  const paths=['catalog/atlas-test-problems.json','catalog/atlas-equations.json','catalog/atlas-methods.json','catalog/atlas-gallery.json','catalog/atlas-execution-examples.json','catalog/atlas-depth-expansion.json','numerical-methods-atlas/assets/reference-solutions.json',...['preview-manifest.json','calculations.json','verification.json'].map(name=>'numerical-methods-atlas/gallery/'+name)];
  const before=paths.map(digest);
  const output=JSON.parse(execFileSync(python,['-B','-c',importHelper+String.raw`
data=module.load_problem_links(root)
print(json.dumps({'ids':[row['id'] for row in data['problems']],'source_sha256':data['source_sha256']}))
`,fileURLToPath(root)],{encoding:'utf8',maxBuffer:4*1024*1024}));
  assert.deepEqual(output.ids,inventory.map(row=>row.id));
  assert.deepEqual(paths.map(digest),before,'navigation does not regenerate scientific inputs, measurements or images');
  for(const [path,hash]of Object.entries(output.source_sha256))assert.equal(digest(path),hash,path);
});

test('unknown or duplicate problem, equation, reference and method identities fail catalog validation',()=>{
  const mutations=[
    ['missing problem',"data['problems'].pop()"],
    ['duplicate problem',"data['problems'].append(copy.deepcopy(data['problems'][0]))"],
    ['unknown problem',"data['problems'][0]['id']='unknown-problem'"],
    ['unknown equation',"data['problems'][0]['equation_ids']=['unknown-equation']"],
    ['duplicate equation',"row=next(row for row in data['problems'] if row['equation_ids']);row['equation_ids'].append(row['equation_ids'][0])"],
    ['unknown reference',"data['problems'][0]['references']=[dict(id='unknown-reference',relation='same-problem',note={'ja':'確認','en':'Checked'})]"],
    ['duplicate reference',"row=next(row for row in data['problems'] if row['references']);row['references'].append(copy.deepcopy(row['references'][0]))"],
    ['unreviewed relation',"row=next(row for row in data['problems'] if row['references']);row['references'][0]['relation']='unreviewed'"],
    ['unknown method',"data['problems'][0]['method_ids']=['unknown-method']"],
    ['duplicate method',"row=next(row for row in data['problems'] if row['method_ids']);row['method_ids'].append(row['method_ids'][0])"],
    ['missing override translation',"row=next(row for row in data['problems'] if row['id']=='poisson-2d-uniform');del row['code_evidence'][0]['note']['en']"]
  ];
  const checked=JSON.parse(execFileSync(python,['-B','-c',importHelper+String.raw`
import copy
catalog=json.loads((root/'catalog/atlas-problem-links.json').read_text())
def ids(path,key):return {row['id'] for row in json.loads((root/path).read_text())[key]}
from atlas_reference_catalog import load_reference_cases
arguments=[ids('catalog/atlas-test-problems.json','problems'),ids('catalog/atlas-equations.json','equations'),{row['id'] for row in load_reference_cases(root)},ids('catalog/atlas-methods.json','methods')]
module.validate_catalog(catalog,*arguments)
checked=[]
for name,mutation in json.loads(sys.argv[2]):
    data=copy.deepcopy(catalog);exec(mutation)
    try:module.validate_catalog(data,*arguments)
    except ValueError:checked.append(name)
    else:raise AssertionError('Accepted invalid catalog: '+name)
print(json.dumps(checked))
`,fileURLToPath(root),JSON.stringify(mutations)],{encoding:'utf8',maxBuffer:4*1024*1024}));
  assert.deepEqual(checked,mutations.map(([name])=>name));
});

test('a curated test override cannot borrow an existing source file from a different problem',()=>{
  const output=execFileSync(python,['-B','-c',importHelper+String.raw`
from unittest.mock import patch
catalog_path=root/'catalog/atlas-problem-links.json'
catalog=json.loads(catalog_path.read_text())
inventory=json.loads((root/'numerical-methods-atlas/test-cases/index.json').read_text())['problems']
problem=next(row for row in inventory if row['id']=='poisson-2d-uniform')
allowed={evidence['path'] for evidence in problem['evidence']}
foreign=next(evidence for row in inventory for evidence in row['evidence'] if evidence.get('python_symbol') and evidence['path'] not in allowed)
override=next(row for row in catalog['problems'] if row['id']=='poisson-2d-uniform')['code_evidence'][0]
override.update(path=foreign['path'],python_symbol=foreign['python_symbol'])
original=pathlib.Path.read_bytes
def fixture_read(path):
    return json.dumps(catalog).encode() if path.resolve()==catalog_path.resolve() else original(path)
with patch.object(pathlib.Path,'read_bytes',fixture_read):
    try:module.load_problem_links(root)
    except ValueError as error:assert 'outside the problem sources' in str(error),str(error)
    else:raise AssertionError('Accepted an unrelated source override')
print('unrelated source override rejected')
`,fileURLToPath(root)],{encoding:'utf8',maxBuffer:4*1024*1024});
  assert.match(output,/unrelated source override rejected/);
});

test('public navigation URL validation rejects absent files, external destinations, credentials and unsafe schemes',()=>{
  const result=execFileSync(python,['-B','-c',importHelper+String.raw`
import tempfile
with tempfile.TemporaryDirectory(prefix='atlas-problem-urls-') as temporary:
    fixture=pathlib.Path(temporary);(fixture/'allowed').mkdir();(fixture/'allowed/index.html').write_text('<main>Allowed</main>')
    module.validate_public_url('/allowed/',fixture)
    module.validate_public_url('https://hrkoyama.github.io/allowed/?lang=ja',fixture)
    invalid=['javascript:alert(1)','data:text/html,x','http://hrkoyama.github.io/allowed/','https://evil.example/allowed/','//evil.example/allowed/','https://user:secret@hrkoyama.github.io/allowed/','/missing/','/../../outside/']
    for url in invalid:
        try:module.validate_public_url(url,fixture)
        except ValueError:pass
        else:raise AssertionError('Accepted invalid public URL: '+url)
print('URL mutations rejected')
`,fileURLToPath(root)],{encoding:'utf8'});
  assert.match(result,/URL mutations rejected/);
});
