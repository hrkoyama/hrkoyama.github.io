import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const root=new URL('../',import.meta.url);
const read=path=>readFileSync(new URL(path,root),'utf8');
const catalog=JSON.parse(read('catalog/atlas-methods.json'));
const cohort=[
  'upwind','godunov','hllc','weno-z','rk4','sdirk2','verlet',
  'cg','newton','multigrid','p1-fem','legendre-basis','nodal-basis',
  'barnes-hut','pm','schrodinger','hartree-fock','kohn-sham-dft',
  'scf','hartree-poisson','xc-functionals','ewald','pme','spme',
];
const implementedLongRange={ewald:['ewald'],pme:['spme'],spme:['spme']};
const planned=['velocity-rescaling','berendsen-thermostat','andersen-thermostat','nose-thermostat','nose-hoover','nose-hoover-chains','gaussian-isokinetic','generalized-langevin','dpd-thermostat','lowe-andersen'];
const languages=['ja','en'];
const fields=['assumptions','units','boundary_conditions','limitations'];
const states=['specified','not-applicable','unknown'];
const roles={
  'original-method':{ja:'原法',en:'Original method'},
  'adopted-variant':{ja:'採用変種',en:'Adopted variant'},
  formulation:{ja:'定式化',en:'Formulation'},
  'reference-solution':{ja:'参照解・独立参照',en:'Reference solution / independent reference'},
  context:{ja:'関連する背景',en:'Context'},
};
const depths={
  'full-text':{ja:'本文の該当箇所を確認',en:'Relevant full-text passages checked'},
  'abstract-and-metadata':{ja:'抄録・書誌を確認',en:'Abstract and metadata checked'},
  metadata:{ja:'書誌を確認',en:'Metadata checked'},
};
const kinds=['primary-research','book','official-documentation'];
const byId=new Map(catalog.methods.map(method=>[method.id,method]));
const reviewed=cohort.map(id=>{
  assert.ok(byId.has(id),`Missing priority method ${id}`);
  return byId.get(id);
});
const escape=text=>String(text).replaceAll('&','&amp;').replaceAll('<','&lt;')
  .replaceAll('>','&gt;').replaceAll('"','&quot;').replaceAll("'",'&#x27;');
const text=(value,where)=>assert.ok(typeof value==='string'&&value.trim(),where);
function bilingual(value,where,lists=false){
  assert.ok(value&&typeof value==='object',where);
  for(const lang of languages){
    if(lists){
      assert.ok(Array.isArray(value[lang])&&value[lang].length,`${where}.${lang}`);
      for(const entry of value[lang])text(entry,`${where}.${lang} item`);
    }else text(value[lang],`${where}.${lang}`);
  }
}
function https(value,where){
  const url=new URL(value);
  assert.equal(url.protocol,'https:',where);
  assert.ok(url.hostname&&!url.username&&!url.password,where);
}
function languageSection(html,lang){
  const opening=new RegExp(`<section\\b[^>]*data-site-language="${lang}"[^>]*>`).exec(html);
  assert.ok(opening,`Missing ${lang} HTML section`);
  const start=opening.index+opening[0].length;
  const tags=/<\/?section\b[^>]*>/g;
  tags.lastIndex=start;
  let depth=1;
  for(let token;(token=tags.exec(html));){
    depth+=token[0].startsWith('</')?-1:1;
    if(depth===0)return html.slice(start,token.index);
  }
  assert.fail(`Unclosed ${lang} HTML section`);
}
function markdownSection(markdown,lang){
  const title=lang==='ja'?'条件と確認範囲':'Conditions and review scope';
  const marker=`## ${title} (${lang})\n`;
  const at=markdown.indexOf(marker);
  assert.ok(at>=0,`Missing ${lang} Markdown review`);
  const start=at+marker.length;
  const next=markdown.indexOf('\n## ',start);
  return markdown.slice(start,next<0?undefined:next);
}
const doi=value=>String(value||'').replace(/^https?:\/\/(?:dx\.)?doi\.org\//i,'').toLowerCase();
const identity=reference=>reference.doi?'doi:'+doi(reference.doi):reference.identity||'url:'+reference.source;

test('the priority inventory is the agreed 24 methods and Python accepts the complete catalog',()=>{
  assert.equal(catalog.priority_review.on,'2026-11-22');
  bilingual(catalog.priority_review.scope,'priority review scope');
  assert.deepEqual(catalog.priority_review.method_ids,cohort);
  assert.deepEqual(catalog.methods.filter(method=>method.method_review).map(method=>method.id).sort(),[...cohort].sort());
  assert.deepEqual(reviewed.filter(method=>method.status==='planned').map(method=>method.id),[]);
  const actual=JSON.parse(execFileSync('python3',['-c',[
    'import json,sys',
    'from pathlib import Path',
    "sys.path.insert(0,str(Path('scripts').resolve()))",
    'from atlas_method_review import validate_method_reviews',
    "catalog=json.loads(Path('catalog/atlas-methods.json').read_text())",
    'print(json.dumps([m["id"] for m in validate_method_reviews(catalog)]))',
  ].join('\n')],{cwd:fileURLToPath(root),encoding:'utf8'}));
  assert.deepEqual(actual,cohort);
});

test('reviewed conditions, applicability decisions and state reasons are explicit in both languages',()=>{
  for(const method of reviewed){
    const {id,method_review:review}=method;
    assert.equal(review.version,1,id);
    assert.equal(review.on,catalog.priority_review.on,id);
    for(const key of ['summary','limitations'])bilingual(method[key],`${id}.${key}`);
    bilingual({ja:method.assumptions_ja,en:method.assumptions},`${id}.assumptions`,true);
    for(const key of ['units','boundary_conditions'])bilingual({ja:method[key+'_ja'],en:method[key]},`${id}.${key}`);
    for(const key of ['problem','variant'])bilingual(review[key],`${id}.${key}`);
    for(const key of ['use_when','avoid_when'])bilingual(review[key],`${id}.${key}`,true);
    for(const field of fields){
      assert.ok(states.includes(review.fields[field].state),`${id}.${field}.state`);
      bilingual(review.fields[field].reason,`${id}.${field}.reason`);
    }
    assert.ok(['source-and-code-inspection','source-review-no-implementation'].includes(review.verification.kind),id);
    bilingual(review.verification.summary,`${id}.verification.summary`);
    bilingual(review.verification.not_checked,`${id}.verification.not_checked`,true);
    for(const evidence of review.verification.evidence){
      https(evidence.url,`${id} evidence`);text(evidence.label,`${id} evidence label`);
    }
  }
});

test('publication roles, observed access depths and primary support remain distinct',()=>{
  const observedDepths=new Set();
  for(const method of reviewed){
    assert.ok(method.references.some(ref=>ref.kind==='primary-research'&&ref.role!=='context'),method.id+' primary source');
    for(const ref of method.references){
      https(ref.url,method.id+' publication');
      assert.ok(Object.hasOwn(roles,ref.role),method.id+' role');
      assert.ok(kinds.includes(ref.kind),method.id+' publication kind');
      text(ref.scope,method.id+' citation scope');text(ref.label,method.id+' citation label');
      bilingual(ref.supports,method.id+' reference support');
      const check=ref.verification;
      assert.ok(Object.hasOwn(depths,check.level),method.id+' checked depth');
      assert.equal(check.checked_on,catalog.priority_review.on,method.id+' checked date');
      https(check.url,method.id+' inspected source');text(check.locator,method.id+' inspected passage');
      observedDepths.add(check.level);
    }
  }
  assert.deepEqual([...observedDepths].sort(),Object.keys(depths).sort());
});

test('reviewed.json and individual JSON preserve the catalog review without inventing implementation status',()=>{
  const collection=JSON.parse(read('numerical-methods-atlas/methods/reviewed.json'));
  assert.equal(collection.schema_version,1);
  assert.equal(collection.method_count,24);
  assert.equal(collection.reviewed_on,catalog.priority_review.on);
  assert.deepEqual(collection.scope,catalog.priority_review.scope);
  assert.equal(collection.catalog_source,'https://hrkoyama.github.io/catalog/atlas-methods.json');
  assert.match(collection.review_kind,/no new numerical runs/i);
  assert.deepEqual(collection.methods.map(method=>method.id),cohort);
  for(const method of reviewed){
    const records=[collection.methods.find(item=>item.id===method.id),JSON.parse(read(`numerical-methods-atlas/methods/${method.id}/index.json`))];
    for(const record of records){
      for(const key of ['status','code_modules','test_files','summary','assumptions','assumptions_ja','units','units_ja','boundary_conditions','boundary_conditions_ja','limitations','method_review','references']){
        assert.deepEqual(record[key],method[key],`${method.id} public ${key}`);
      }
      assert.equal(record.url,`https://hrkoyama.github.io/numerical-methods-atlas/methods/${method.id}/`);
    }
  }
});

test('each localized HTML and Markdown exposes its own conditions, reasons, evidence and source limits',()=>{
  const map=read('numerical-methods-atlas/methods/index.html');
  for(const lang of languages){
    const section=languageSection(map,lang);
    assert.ok(section.includes('reviewed.json'),lang+' reviewed download');
    for(const method of reviewed)assert.ok(section.includes(`${method.id}/?lang=${lang}`),method.id+' localized map link');
  }
  for(const method of reviewed){
    const route=`numerical-methods-atlas/methods/${method.id}/`;
    const html=read(route+'index.html'),markdown=read(route+'index.md');
    const review=method.method_review;
    for(const lang of languages){
      const section=languageSection(html,lang),md=markdownSection(markdown,lang);
      const prose=[method.summary[lang],review.problem[lang],review.variant[lang],
        ...review.use_when[lang],...review.avoid_when[lang],
        ...(lang==='ja'?method.assumptions_ja:method.assumptions),
        method[lang==='ja'?'units_ja':'units'],method[lang==='ja'?'boundary_conditions_ja':'boundary_conditions'],
        method.limitations[lang],review.verification.summary[lang],...review.verification.not_checked[lang],
        ...fields.map(field=>review.fields[field].reason[lang])];
      for(const value of prose){
        assert.ok(section.includes(escape(value)),`${method.id}/${lang} HTML: ${value.slice(0,65)}`);
        // The summary precedes the bilingual review block; all review details belong inside it.
        if(value!==method.summary[lang])assert.ok(md.includes(value),`${method.id}/${lang} Markdown: ${value.slice(0,65)}`);
      }
      for(const field of fields){
        assert.ok(section.includes(`data-metadata-field="${field}" data-field-state="${review.fields[field].state}"`),`${method.id}/${lang} field state`);
        assert.ok(md.includes(`${field} [${review.fields[field].state}]`),`${method.id}/${lang} Markdown state`);
      }
      for(const evidence of review.verification.evidence){
        assert.ok(section.includes(`href="${escape(evidence.url)}"`),method.id+' HTML evidence');
        assert.ok(md.includes(evidence.url),method.id+' Markdown evidence');
      }
      for(const ref of method.references){
        for(const value of [ref.supports[lang],ref.verification.locator]){
          assert.ok(section.includes(escape(value)),method.id+' localized citation scope');
          assert.ok(md.includes(value),method.id+' Markdown citation scope');
        }
        assert.ok(section.includes(roles[ref.role][lang]),method.id+' source role label');
        assert.ok(section.includes(depths[ref.verification.level][lang]),method.id+' source depth label');
        assert.ok(section.includes(`href="${escape(ref.verification.url)}"`),method.id+' inspected source link');
        assert.ok(md.includes(`[${ref.role} / ${ref.kind}]`)&&md.includes(ref.verification.level),method.id+' machine-readable source role/depth');
      }
    }
  }
});

test('scoped Ewald and smooth-PME examples expose their dedicated evidence without attributing the separately added slab evidence to their earlier review',()=>{
  const collection=JSON.parse(read('numerical-methods-atlas/methods/reviewed.json'));
  const common=JSON.parse(read('catalog/atlas-execution-examples.json')).examples;
  for(const [id,caseIDs] of Object.entries(implementedLongRange)){
    const source=byId.get(id);
    const record=collection.methods.find(method=>method.id===id);
    assert.equal(source.status,'educational-example',id);
    assert.equal(source.method_review.verification.kind,'source-and-code-inspection',id);
    assert.deepEqual(source.depth_release,{group:'particles',edition:'2026-11-22',case_ids:caseIDs});
    const added=id==='ewald'?'ewald-convergence':'spme-convergence';
    assert.deepEqual(source.depth_additional_releases.find(x=>x.group==='particle-transport').case_ids,[added]);
    assert.deepEqual(record.execution_examples.filter(example=>example.id!=='neutral-slab-yb').map(example=>example.id),[...caseIDs,added],id+' scoped independent supplements');
    assert.equal(record.code_edition,'2026-11-22',id);
    assert.ok(record.code_urls.some(url=>url.endsWith('/particles/electrostatics.py')),id+' dedicated algorithm');
    assert.ok(record.test_urls.length>0&&record.run_commands.length>0,id+' actual tests and commands');
    assert.ok(record.code_download?.endsWith('/particles/atlas-particles-2026-11-22.zip'),id+' frozen distribution');
    assert.ok(source.method_review.verification.evidence.some(item=>item.kind==='independent-extraction-receipt'),id+' independent receipt');
    for(const example of record.execution_examples){
      assert.ok(!common.some(row=>row.id===example.id),id+' supplement remains separate from common22');
      for(const lang of languages)assert.ok(example.guide[lang].includes('/validation/'+example.id+'/'),id+' direct supplemental entry');
    }
    const limits=source.method_review.verification.not_checked.en.join(' ');
    assert.match(limits,/slab/i,id+' unsupported slab boundary');
    if(id!=='ewald')assert.match(limits,/original PME/i,id+' SPME evidence does not claim the original PME');
  }
});

test('remaining planned methods do not advertise runnable code or borrow the new periodic implementations',()=>{
  assert.deepEqual(catalog.methods.filter(m=>m.status==='planned').map(m=>m.id),planned);
  for(const id of planned){
    const source=byId.get(id);
    const record=JSON.parse(read(`numerical-methods-atlas/methods/${id}/index.json`));
    assert.equal(source.status,'planned',id);
    assert.deepEqual(source.code_modules,[],id);assert.deepEqual(source.test_files,[],id);
    assert.ok(!source.example&&!source.quantum_examples?.length&&!source.depth_release,id+' no borrowed source example');
    for(const key of ['code_urls','test_urls','run_commands','execution_examples'])assert.deepEqual(record[key],[],`${id}.${key}`);
    assert.equal(record.code_edition,null,id);assert.equal(record.run_from,null,id);
    assert.ok(!record.code_download&&!record.code_examples?.length,id+' download/example');
    const html=read(`numerical-methods-atlas/methods/${id}/index.html`);
    assert.doesNotMatch(html,/<pre\b[^>]*>\s*<code\b/i,id+' runnable code block');
    assert.ok(languageSection(html,'ja').includes(escape(source.next_deliverable.ja)),id+' next JA');
    assert.ok(languageSection(html,'en').includes(escape(source.next_deliverable.en)),id+' next EN');
  }
});

test('curated publications resolve to one global record and one BibTeX entry per source',()=>{
  const sources=JSON.parse(read('catalog/atlas-method-primary-references.json')).references;
  const library=JSON.parse(read('numerical-methods-atlas/references.json'));
  const bibKeys=[...read('numerical-methods-atlas/assets/references.bib').matchAll(/@[a-z]+\s*\{\s*([^,\s]+)\s*,/gi)].map(match=>match[1]);
  assert.equal(new Set(sources.map(identity)).size,sources.length,'duplicate curated publication');
  for(const source of sources){
    const hits=library.filter(reference=>identity(reference)===identity(source));
    assert.equal(hits.length,1,source.id+' global identity');
    assert.equal(bibKeys.filter(key=>key===hits[0].id).length,1,source.id+' BibTeX entry');
  }
  for(const method of reviewed){
    for(const ref of method.references){
      if(ref.kind==='official-documentation'&&!ref.bibliography_id)continue;
      text(ref.bibliography_id,method.id+' bibliography id');
      const hits=library.filter(reference=>reference.id===ref.bibliography_id);
      assert.equal(hits.length,1,method.id+' unique citation target');
      if(new URL(ref.url).hostname==='doi.org')assert.equal(doi(hits[0].doi),doi(ref.url),method.id+' citation DOI');
      assert.equal(bibKeys.filter(key=>key===ref.bibliography_id).length,1,method.id+' citation BibTeX');
    }
  }
});

test('the validation API rejects dropped translations, inflated access claims and implementation added to a plan',()=>{
  const outcomes=JSON.parse(execFileSync('python3',['-c',[
    'import copy,json,sys',
    'from pathlib import Path',
    "sys.path.insert(0,str(Path('scripts').resolve()))",
    'from atlas_method_review import validate_method_reviews',
    "base=json.loads(Path('catalog/atlas-methods.json').read_text())",
    'outcomes=[]',
    "for case in ['reason-language','source-role','source-depth','planned-code','cohort']:",
    '    catalog=copy.deepcopy(base)',
    '    rows={m["id"]:m for m in catalog["methods"]}',
    '    method=rows["upwind"]',
    '    if case=="reason-language": method["method_review"]["fields"]["units"]["reason"].pop("en")',
    '    elif case=="source-role": method["references"][0]["role"]="everything-verified"',
    '    elif case=="source-depth": method["references"][0]["verification"]["level"]="independently-proved"',
    // A hypothetical planned copy of the now implemented slab method exercises the
    // same API guard, without reverting the implemented 3D Ewald record.
    '    elif case=="planned-code":',
    '        plan=copy.deepcopy(rows["ewald"])',
    '        plan.update(id="slab-ewald",status="planned",code_modules=["particle_mesh"],test_files=[])',
    '        plan.pop("depth_release",None)',
    '        catalog["methods"]=[plan if m["id"]=="slab-ewald" else m for m in catalog["methods"]]',
    '        rows["ewald"].pop("method_review")',
    '        catalog["priority_review"]["method_ids"]=["slab-ewald" if i=="ewald" else i for i in catalog["priority_review"]["method_ids"]]',
    '    else: catalog["priority_review"]["method_ids"].pop()',
    '    try:',
    '        validate_method_reviews(catalog)',
    '    except ValueError:',
    '        outcomes.append(case)',
    'print(json.dumps(outcomes))',
  ].join('\n')],{cwd:fileURLToPath(root),encoding:'utf8'}));
  assert.deepEqual(outcomes,['reason-language','source-role','source-depth','planned-code','cohort']);
});
