import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
const root=new URL('../',import.meta.url);
const read=path=>JSON.parse(fs.readFileSync(new URL(path,root),'utf8'));
const source=read('catalog/atlas-detailed-reading.json');
const methods=read('catalog/atlas-methods.json').methods;
const originalPlanned=['ewald','pme','spme','slab-ewald','fdtd','pic','amg','qr-svd','eigensolvers','splines','quadrature','chebyshev','wavelets','optimization','monte-carlo','mcmc','sde','adjoint','radiation-transport','dsmc','dae','automatic-differentiation','pinn-operators'];
test('all 23 formerly unlinked methods have substantive bilingual reading while implementation states remain honest',()=>{
 assert.equal(source.chapters.length,27);
 assert.equal(methods.length,143);assert.equal(methods.filter(m=>m.status==='planned').length,35);assert.equal(methods.filter(m=>m.status==='educational-example').length,91);assert.equal(methods.filter(m=>m.status==='reading-only').length,17);
 for(const id of originalPlanned){
  const chapter=source.chapters.find(c=>c.id===id),m=methods.find(m=>m.id===id);assert.ok(chapter,id);assert.equal(m.status,'planned');assert.equal(m.code_modules.length,0);assert.equal(m.test_files.length,0);
  for(const lang of ['ja','en']){
   assert.equal(chapter.sections.length,4);assert.ok(chapter.intro[lang].length>40);
   for(const section of chapter.sections)assert.ok(section.paragraphs[lang].join(' ').length>65,id+' '+lang+' '+section.id);
   assert.equal(m.reading[lang],`/numerical-methods-atlas/${lang}/read/${id}/`);
  }
 }
 for(const m of methods)assert.ok(m.reading.ja&&m.reading.en,m.id+' has both languages');
});
test('each detailed chapter publishes real equations, bilingual anchors, source roles and readable machine downloads',()=>{
 const refs=new Map(source.references.map(r=>[r.id,r]));
 for(const chapter of source.chapters){
  const headings=[];
  for(const lang of ['ja','en']){
   const base=`numerical-methods-atlas/${lang}/read/${chapter.id}/`;
   const html=fs.readFileSync(new URL(base+'index.html',root),'utf8'),json=read(base+'index.json'),md=fs.readFileSync(new URL(base+'index.md',root),'utf8');
   assert.ok(html.includes('katex-mathml')&&!html.includes('math-placeholder'),chapter.id);assert.ok(html.includes('id="sources"'));assert.ok(md.includes('$$')&&md.includes('https://'));
   assert.ok(json.references.length&&json.source_sha256.length===64);assert.ok(json.html.includes('id="publication-scope"'));
   headings.push(json.headings.map(h=>h.id));
   for(const id of chapter.references){const r=refs.get(id);assert.ok(r?.source_review?.url.startsWith('https://'));assert.ok(html.includes(r.title.replaceAll('&','&amp;').replaceAll('"','&quot;').replaceAll("'",'&#x27;')));}
  }
  assert.deepEqual(headings[0],headings[1],chapter.id);
 }
});
test('the basis translation preserves the nine equations, eight original sections and existing scientific scope',()=>{
 const basis=source.chapters.find(c=>c.id==='basis-functions');
 assert.equal(Object.keys(source.formulas).filter(k=>k.startsWith('basis-')).length,9);
 assert.equal((basis.html.ja.match(/math-placeholder/g)||[]).length,(basis.html.en.match(/math-placeholder/g)||[]).length);
 for(const lang of ['ja','en']){
  const doc=read(`numerical-methods-atlas/content.${lang}.json`)['basis-functions'];assert.equal(doc.locale,lang);assert.equal(doc.headings.length,10);
  assert.ok(doc.html.includes('Teukolsky')&&doc.html.includes('Dubiner'));assert.ok(doc.html.includes('P0/P1/P2'));
 }
 assert.equal(read('numerical-methods-atlas/translation-status.json').chapters['basis-functions'].status,'draft');
});
test('source identity traps and rotated-solver authorship remain distinct',()=>{
 const ref=id=>source.references.find(r=>r.id===id);
 assert.equal(ref('dawson1962').doi,'10.1063/1.1706638');assert.equal(ref('gear1971').doi,'10.1109/tct.1971.1083221');assert.equal(ref('arnoldi1951').doi,'10.1090/qam/42792');
 assert.match(ref('ren2003').author,/Ren/);assert.equal(ref('ren2003').year,2003);
 const hybrid=ref('nishikawa2008');assert.match(hybrid.author,/Nishikawa/);assert.match(hybrid.author,/Kitamura/);assert.ok(!hybrid.author.includes('Roe'));assert.equal(hybrid.year,2008);
 assert.match(ref('roe2005carbuncle').author,/Roe.*Nishikawa/);assert.equal(ref('roe2005carbuncle').year,2005);
 const record=methods.find(m=>m.id==='rotated-hybrid');assert.deepEqual(record.code_modules,['rotated_flux']);assert.ok(record.code_mapping_scope.includes('not the optimized'));
 const dois=source.references.filter(r=>r.doi).map(r=>r.doi.toLowerCase());assert.equal(new Set(dois).size,dois.length);
});

test('preconditioning distinguishes pseudo time, sonic zeros and entropy smoothing; steady RK distinguishes linear and nonlinear order',()=>{
 const pc=source.chapters.find(c=>c.id==='low-mach-preconditioning'),rk=source.chapters.find(c=>c.id==='steady-runge-kutta');
 assert.ok(pc.sections.some(s=>s.id==='weiss-smith-example'));assert.ok(pc.sections.some(s=>s.id==='sonic-point-is-different'));assert.ok(pc.publication_scope.en.includes('reading-only'));
 assert.ok(source.formulas['sonic-determinant'].includes('\\det(PA)'));assert.ok(source.formulas['steady-rk-nonlinear-order'].includes('\\tfrac14\\ne\\tfrac13'));
 assert.ok(rk.publication_scope.en.includes('No dedicated solver'));assert.equal(methods.find(m=>m.id==='low-mach-preconditioning').status,'reading-only');
});

test('new Japanese queries reach the actual detailed reading through the public search',async()=>{
 const {makeSearch}=await import('../search/engine.mjs');const search=makeSearch(read('search/index.json').documents);
 for(const [query,chapter] of [['ダンピングルンゲクッタ','steady-runge-kutta'],['前処理行列','low-mach-preconditioning'],['直交多項式','basis-functions']]){
  assert.ok(search(query,'ja','atlas').some(x=>x.url===`/numerical-methods-atlas/ja/read/${chapter}/`),query);
 }
});
