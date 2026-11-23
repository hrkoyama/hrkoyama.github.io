import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
const root=new URL('../',import.meta.url);
const read=path=>JSON.parse(fs.readFileSync(new URL(path,root),'utf8'));
const source=read('catalog/atlas-detailed-reading.json');
const methods=read('catalog/atlas-methods.json').methods;
const originalPlanned=['ewald','pme','spme','slab-ewald','fdtd','pic','amg','qr-svd','eigensolvers','splines','quadrature','chebyshev','wavelets','optimization','monte-carlo','mcmc','sde','adjoint','radiation-transport','dsmc','dae','automatic-differentiation','pinn-operators'];
test('all 23 formerly unlinked methods have substantive bilingual reading while implementation states remain honest',()=>{
 assert.equal(source.chapters.length,31);
 assert.equal(methods.length,150);assert.equal(methods.filter(m=>m.status==='planned').length,16);assert.equal(methods.filter(m=>m.status==='educational-example').length,119);assert.equal(methods.filter(m=>m.status==='reading-only').length,15);
 for(const id of originalPlanned){
  const chapter=source.chapters.find(c=>c.id===id),m=methods.find(m=>m.id===id);assert.ok(chapter,id);assert.equal(m.status,['monte-carlo','sde','automatic-differentiation','adjoint','optimization','fdtd'].includes(id)||m.depth_release?'educational-example':'planned');
  if(!['automatic-differentiation','adjoint','optimization'].includes(id)){assert.equal(m.code_modules.length,0);assert.equal(m.test_files.length,0);}
  for(const lang of ['ja','en']){
   if(['automatic-differentiation','adjoint'].includes(id))assert.ok(chapter.html[lang].length>6000);
   else if(id==='fdtd'){
    const headings=[...chapter.html[lang].matchAll(/<h2 id="([^"]+)">/g)].map(m=>m[1]);
    const original=['model','algorithm','periodic-mode','cavity-mode','conditions','energy','verification','reproduce'];
    assert.deepEqual(headings.filter(id=>original.includes(id)),original);
    for(const id of ['interface','pml','pml-corners','interface-oblique','interface-p-polarization','interface-loss-dispersion'])assert.ok(headings.includes(id),lang+' '+id);
    assert.equal(new Set(headings).size,headings.length);
    const formulas=[...chapter.html[lang].matchAll(/<math-placeholder id="(fdtd-[^"]+)"><\/math-placeholder>/g)].map(m=>m[1]);
    for(const id of ['fdtd-pde','fdtd-update','fdtd-plane','fdtd-cavity','fdtd-dispersion','fdtd-energy','fdtd-order'])assert.ok(formulas.includes(id),lang+' '+id);
    for(const id of formulas)assert.ok(source.formulas[id],id);
   }
   else{assert.equal(chapter.sections.length,4);assert.ok(chapter.intro[lang].length>40);for(const section of chapter.sections)assert.ok(section.paragraphs[lang].join(' ').length>65,id+' '+lang+' '+section.id);}
   assert.equal(m.reading[lang],`/numerical-methods-atlas/${lang}/read/${id==='optimization'?'bratu-multi-inverse':id}/`);
  }
 }
 for(const m of methods)assert.ok(m.reading.ja&&m.reading.en,m.id+' has both languages');
});
test('multi-parameter Bratu reading separates data sensitivity from regularized curvature and preserves the scalar experiment',()=>{
 const chapter=source.chapters.find(c=>c.id==='bratu-multi-inverse');
 const sections=['multi-parameter-model','observations-and-data','multi-adjoint-gradient','regularization','bounded-fit','data-identifiability','reflection-ambiguity','multi-verification','error-and-scope','reproduce'];
 const release='/code/bratu-multinverse/2026-11-22/';
 assert.deepEqual(chapter.methods,['optimization','adjoint']);
 assert.ok(chapter.related_methods.includes('qr-svd'));
 assert.deepEqual(chapter.references,['armijo1966','blondel2022implicit','golub1970','hansen2008regutools']);
 const hansen=source.references.find(r=>r.id==='hansen2008regutools');
 assert.equal(hansen.type,'misc');assert.equal(hansen.year,2008);
 assert.equal(hansen.source_review.level,'full-text');assert.match(hansen.source_review.scope,/Section 2\.3\.1/);
 const formulaIds=Object.keys(source.formulas).filter(id=>id.startsWith('bratu-multi-'));
 assert.equal(formulaIds.length,16);
 assert.ok(source.formulas['bratu-multi-model'].includes('a+b(2x-1)'));
 assert.ok(source.formulas['bratu-multi-adjoint'].includes('J^Tp=q'));
 assert.ok(source.formulas['bratu-multi-adjoint'].includes('-B_\\theta^Tp'));
 assert.ok(source.formulas['bratu-multi-adjoint'].includes('+Q_h^T(e^u\\odot p)'));
 assert.ok(source.formulas['bratu-multi-regularized-curvature'].includes('A_{\\rm data}^TA_{\\rm data}+\\gamma I_2'));
 assert.ok(source.formulas['bratu-multi-center-rank'].includes('\\operatorname{rank}(H_{\\rm center}S)\\le1'));
 assert.ok(source.formulas['bratu-multi-reflection'].includes('u_h(a,-b;1/2)=u_h(a,b;1/2)'));
 assert.ok(source.formulas['bratu-multi-update'].includes('g_k^T\\Delta\\theta'));
 assert.ok(source.formulas['bratu-multi-stopping'].includes('\\theta-\\Pi_{\\mathcal B}(\\theta-g(\\theta))'));
 for(const lang of ['ja','en']){
  const html=chapter.html[lang],doc=read(`numerical-methods-atlas/${lang}/read/bratu-multi-inverse/index.json`);
  assert.deepEqual([...html.matchAll(/<h2 id="([^"]+)">/g)].map(m=>m[1]),sections);
  assert.deepEqual(doc.headings.map(h=>h.id),[...sections,'publication-scope','sources']);
  assert.deepEqual([...html.matchAll(/<math-placeholder id="([^"]+)"><\/math-placeholder>/g)].map(m=>m[1]).sort(),formulaIds.slice().sort());
  assert.equal(doc.implementation_status.optimization,'educational-example');
  for(const suffix of ['bratu-multinverse-2026-11-22.zip','README.md','numart/bratu_multinverse.py','scripts/build_bratu_multinverse.py','tests/test_bratu_multinverse.py','verification.json','source-manifest.json'])assert.ok(html.includes(release+suffix),lang+' '+suffix);
  for(const suffix of ['png','json'])assert.ok(html.includes('/numerical-methods-atlas/assets/bratu-multinverse.'+suffix));
  assert.ok(html.includes('href="/numerical-methods-atlas/assets/bratu-multinverse.png"'));
  assert.ok(html.includes(lang==='ja'?'局所的に可逆':'locally nonsingular'));
  assert.ok(html.includes('inverse crime')&&html.includes('Tikhonov')&&html.includes('Gauss–Newton'));
  assert.ok(html.includes('255')&&html.includes('511')&&html.includes('1023'));
  assert.ok(!html.includes('katex-mathml')&&!html.includes('__MEASUREMENTS')&&!html.includes('.venv/bin/python'));
  for(const id of ['bratu-inverse','adjoint','optimization']){
   const old=source.chapters.find(c=>c.id===id);
   assert.ok(old.html[lang].includes(`/numerical-methods-atlas/${lang}/read/bratu-multi-inverse/`));
   assert.ok(read(`numerical-methods-atlas/${lang}/read/${id}/index.json`).html.includes(`/numerical-methods-atlas/${lang}/read/bratu-multi-inverse/`));
  }
  assert.ok(html.includes(`/numerical-methods-atlas/${lang}/read/bratu-inverse/`));
 }
});
test('the independent Bratu inverse chapter publishes measured adjoint-gradient fits and preserves existing chapter addresses',()=>{
 const chapter=source.chapters.find(c=>c.id==='bratu-inverse');
 const sections=['inverse-data','least-squares','adjoint-gradient','bounded-optimization','synthetic-data','inverse-verification','identifiability','error-scope','reproduce'];
 const release='/code/bratu-inverse/2026-11-22/';
 assert.deepEqual(chapter.methods,['optimization','adjoint']);
 assert.ok(chapter.related_methods.includes('automatic-differentiation'));
 assert.deepEqual(chapter.references,['armijo1966','jameson1988','blondel2022implicit','jaxopt-implicit-diff']);
 const ref=source.references.find(r=>r.id==='armijo1966');
 assert.equal(ref.source_review.level,'full-text');assert.match(ref.source_review.scope,/pages 1–2/);
 const formulaIds=Object.keys(source.formulas).filter(id=>id.startsWith('bratu-inverse-'));
 assert.equal(formulaIds.length,13);
 assert.ok(source.formulas['bratu-inverse-objective'].includes('r_h(\\lambda)^TWr_h(\\lambda)'));
 assert.ok(source.formulas['bratu-inverse-adjoint'].includes('q=H_h^TWr_h'));
 assert.ok(source.formulas['bratu-inverse-adjoint'].includes('J^Tp=q'));
 assert.ok(source.formulas['bratu-inverse-gradient'].includes('+p^Te^u'));
 assert.ok(source.formulas['bratu-inverse-armijo'].includes('c g_k\\Delta\\lambda'));
 assert.ok(source.formulas['bratu-inverse-stationarity'].includes('\\lambda-\\Pi_{[\\ell,b]}(\\lambda-g(\\lambda))'));
 assert.ok(source.formulas['bratu-inverse-data-regimes'].includes('d^{\\rm noisy}=d^{\\rm cont}'));
 for(const lang of ['ja','en']){
  const html=chapter.html[lang],doc=read(`numerical-methods-atlas/${lang}/read/bratu-inverse/index.json`);
  assert.deepEqual([...html.matchAll(/<h2 id="([^"]+)">/g)].map(m=>m[1]),sections);
  assert.deepEqual(doc.headings.map(h=>h.id),[...sections,'publication-scope','sources']);
  assert.deepEqual([...html.matchAll(/<math-placeholder id="([^"]+)"><\/math-placeholder>/g)].map(m=>m[1]).sort(),formulaIds.slice().sort());
  assert.equal(doc.implementation_status.optimization,'educational-example');
  assert.equal(doc.implementation_status.adjoint,'educational-example');
  for(const suffix of ['bratu-inverse-2026-11-22.zip','README.md','numart/bratu_inverse.py','scripts/build_bratu_inverse.py','tests/test_bratu_inverse.py','verification.json','source-manifest.json'])assert.ok(html.includes(release+suffix),lang+' '+suffix);
  for(const suffix of ['png','json'])assert.ok(html.includes('/numerical-methods-atlas/assets/bratu-inverse.'+suffix));
  for(const value of ['2.684636137266','2.6816989071','2.6845902950','2.6841620622','2.9070×10⁻⁴','7.1942×10⁻⁴','2.81×10⁻¹²'])assert.ok(html.includes(value),lang+' '+value);
  assert.ok(html.includes('inverse crime')&&html.includes('Armijo')&&html.includes('BFGS'));
  assert.ok(html.includes('python scripts/build_bratu_inverse.py'));
  assert.ok(!html.includes('katex-mathml')&&!html.includes('koyamarium')&&!html.includes('.venv/bin/python'));
  for(const id of ['adjoint','optimization']){
   const old=source.chapters.find(c=>c.id===id);
   assert.ok(old.html[lang].includes(`/numerical-methods-atlas/${lang}/read/bratu-inverse/`));
   const legacyDoc=read(`numerical-methods-atlas/${lang}/read/${id}/index.json`);
   assert.ok(legacyDoc.html.includes(`/numerical-methods-atlas/${lang}/read/bratu-inverse/`));
  }
  const oldOptimization=source.chapters.find(c=>c.id==='optimization');
  assert.deepEqual([...oldOptimization.html[lang].matchAll(/<h2 id="([^"]+)">/g)].map(m=>m[1]),['model','algorithm','conditions','verification']);
  assert.ok(oldOptimization.publication_scope[lang].includes('BFGS'));
 }
});
test('implicit differentiation and discrete adjoints publish the verified Bratu sensitivity without losing old anchors',()=>{
 const chapter=source.chapters.find(c=>c.id==='adjoint');
 const sections=['implicit-root','forward-sensitivity','discrete-adjoint','bratu-family','bratu-objective','sensitivity-verification','solver-errors','continuous-limit','reproduce'];
 const aliases=['model','algorithm','conditions','verification'];
 const release='/code/bratu-sensitivity/2026-11-22/';
 assert.equal(methods.find(m=>m.id==='adjoint').status,'educational-example');
 assert.deepEqual(chapter.references,['jameson1988','linnainmaa1976','blondel2022implicit','jaxopt-implicit-diff']);
 assert.ok(source.formulas['implicit-adjoint'].includes('J^Tp=q'));
 assert.ok(source.formulas['implicit-adjoint'].includes('r-B^Tp'));
 assert.ok(source.formulas['implicit-bratu-partials'].includes('F_\\lambda=-e^u'));
 assert.ok(source.formulas['implicit-bratu-objective'].includes('\\beta=0.05'));
 assert.ok(source.formulas['implicit-continuum-gradient'].includes('\\int_0^1'));
 const formulaIds=Object.keys(source.formulas).filter(id=>id.startsWith('implicit-'));
 assert.equal(formulaIds.length,15);
 for(const lang of ['ja','en']){
  const html=chapter.html[lang],doc=read(`numerical-methods-atlas/${lang}/read/adjoint/index.json`);
  assert.deepEqual([...html.matchAll(/<h2 id="([^"]+)">/g)].map(m=>m[1]),sections);
  assert.deepEqual(doc.headings.map(h=>h.id),[...sections,'publication-scope','sources']);
  for(const id of aliases){assert.ok(html.includes(`id="${id}"`));assert.ok(doc.html.includes(`id="${id}"`));}
  for(const suffix of ['bratu-sensitivity-2026-11-22.zip','README.md','numart/bratu_sensitivity.py','scripts/build_bratu_sensitivity.py','tests/test_bratu_sensitivity.py','verification.json','source-manifest.json'])assert.ok(html.includes(release+suffix),lang+' '+suffix);
  for(const suffix of ['png','json'])assert.ok(html.includes('/numerical-methods-atlas/assets/bratu-sensitivity.'+suffix));
  assert.ok(html.includes('Bratu')&&html.includes('1.4×10⁻¹⁵')&&html.includes('1.8704×10⁻⁵'));
  assert.ok(html.includes('0.1027083914')&&html.includes('0.5857608186'));
  assert.ok(html.includes('python scripts/build_bratu_sensitivity.py'));
  assert.ok(!html.includes('katex-mathml')&&!html.includes('koyamarium'));
  assert.equal(doc.implementation_status.adjoint,'educational-example');
  assert.ok(source.chapters.find(c=>c.id==='automatic-differentiation').html[lang].includes(`/numerical-methods-atlas/${lang}/read/adjoint/`));
 }
});
test('automatic differentiation publishes the foundation chapter and Bratu evidence at its existing bilingual addresses',()=>{
 const chapter=source.chapters.find(c=>c.id==='automatic-differentiation');
 const sections=['ways-to-differentiate','forward-mode','reverse-mode','bratu-problem','bratu-verification','solver-connections','limits','reproduce'];
 const aliases=['model','algorithm','conditions','verification'];
 const release='/code/autodiff/2026-11-22/';
 assert.equal(methods.find(m=>m.id===chapter.id).status,'educational-example');
 assert.deepEqual(chapter.references,['wengert1964','linnainmaa1976','baydin2018','jax-autodiff-cookbook']);
 const formulaIds=Object.keys(source.formulas).filter(id=>id.startsWith('autodiff-foundations-'));
 assert.equal(formulaIds.length,8);
 assert.ok(source.formulas['autodiff-foundations-3'].includes('\\cosh^2(1/2)'));
 const ref=id=>source.references.find(r=>r.id===id);
 assert.equal(ref('baydin2018').source_review.level,'abstract-and-metadata');
 assert.equal(ref('jax-autodiff-cookbook').source_review.level,'full-text');
 for(const lang of ['ja','en']){
  const html=chapter.html[lang],doc=read(`numerical-methods-atlas/${lang}/read/${chapter.id}/index.json`);
  assert.deepEqual([...html.matchAll(/<h2 id="([^"]+)">/g)].map(m=>m[1]),sections);
  assert.deepEqual(doc.headings.map(h=>h.id),[...sections,'publication-scope','sources']);
  for(const id of aliases){assert.ok(html.includes(`id="${id}"`));assert.ok(doc.html.includes(`id="${id}"`));}
  for(const suffix of ['autodiff-2026-11-22.zip','README.md','numart/autodiff.py','numart/krylov.py','scripts/build_autodiff.py','tests/test_autodiff.py','verification.json','source-manifest.json'])assert.ok(html.includes(release+suffix),lang+' '+suffix);
  for(const suffix of ['png','json'])assert.ok(html.includes('/numerical-methods-atlas/assets/autodiff-bratu.'+suffix));
  assert.ok(html.includes('Bratu')&&html.includes('Newton')&&html.includes('JVP'));
  assert.ok(html.includes('10⁻¹⁴')&&html.includes('1.738×10⁻⁴'));
  assert.ok(html.includes('python scripts/build_autodiff.py'));
  assert.ok(!html.includes('katex-mathml')&&!html.includes('.venv/bin/python'));
  assert.equal(doc.implementation_status[chapter.id],'educational-example');
 }
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
 assert.ok(rk.publication_scope.en.includes('No dedicated solver'));assert.equal(methods.find(m=>m.id==='low-mach-preconditioning').status,'educational-example');
});

test('new Japanese queries reach the actual detailed reading through the public search',async()=>{
 const {makeSearch}=await import('../search/engine.mjs');const search=makeSearch(read('search/index.json').documents);
 for(const [query,chapter] of [['ダンピングルンゲクッタ','steady-runge-kutta'],['前処理行列','low-mach-preconditioning'],['直交多項式','basis-functions']]){
  assert.ok(search(query,'ja','atlas').some(x=>x.url===`/numerical-methods-atlas/ja/read/${chapter}/`),query);
 }
});
