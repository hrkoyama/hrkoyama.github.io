// Candidate UI integration only: no solver, scientific test or ZIP download.
// The five-group cohort below was derived from actual frozen canonical packets.
// Direct public-HR verification remains a separate post-Pages requirement.
import {test,expect} from '@playwright/test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const root=new URL('../',import.meta.url);
const read=path=>JSON.parse(readFileSync(new URL(path,root),'utf8'));
const digest=bytes=>createHash('sha256').update(bytes).digest('hex');
const policy={
 "groups": {
  "biology-ode-controls": {
   "ids": [
    "hodgkin-huxley-controls",
    "immigration-death-ssa"
   ],
   "edition": "2026-11-25",
   "manifest": "6b39422e0a480658f7435dbfff210ade94c3016ec5cc7cbfc55e54fff3215016",
   "verification": "b6106b16b00c01c4a8fa95e0fc44d8cddf2f41ae19973598df7aa5c4e8a3cef9"
  },
  "biology-space-controls": {
   "ids": [
    "fisher-kpp-special-front",
    "keller-segel-forced-flux",
    "schnakenberg-2d-boundary-modes"
   ],
   "edition": "2026-11-25",
   "manifest": "b9ebb71638b3f18fde2d5b32b8042016e0f33ac1daa42173937f957c3f65d0ab",
   "verification": "2e7efea396ecd14287ef8fe8b7326d88c61955a6201431eda4dbaa09c26daed2"
  },
  "thermostat-constraint-controls": {
   "ids": [
    "deterministic-thermostat-contrasts",
    "projected-canonical-dof"
   ],
   "edition": "2026-11-25",
   "manifest": "6e64499f6bda68ad17ccc7402e49a7296b82d500174ce0eb238e0acd076cc45e",
   "verification": "c3273335cc6619c07d956252d65b00abf58ff3497d0a35776b3fc376ae70134e"
  },
  "quantum-small": {
   "ids": [
    "atomic-reference-cards",
    "h2-rhf-uhf-fci",
    "h3plus-mp2-fci",
    "periodic-he-reference-cards",
    "periodic-projector-occupations",
    "quantum-box-ho",
    "two-state-bo-cp-ou"
   ],
   "edition": "2026-11-25",
   "manifest": "b13b8873c5f74ec3b1b25207ed145cf7ece1ceec2e0e254a9b7f18e93f73350c",
   "verification": "f78f47618f7524ef69e2b96ed460f1d1e4636cf42775f1ae643e062dabf99dbe"
  },
  "continuum-particle-controls": {
   "ids": [
    "gsph-sod",
    "saltzman-ale-piston",
    "sph-pressure-acoustics",
    "sphere-zonal-balance",
    "williamson-sphere-transport"
   ],
   "edition": "2026-11-25",
   "manifest": "2017c5da0e0a6d70ba01242b63d5bc391feb1fbe24795f8ceab2389790bbec00",
   "verification": "0ce44ce14104c4cdd7e6876b8118d9e6c5635ae40af0f631623418c05264600e"
  }
 },
 "problemByCase": {
  "hodgkin-huxley-controls": "hodgkin-huxley-controls",
  "immigration-death-ssa": "immigration-death-ssa",
  "fisher-kpp-special-front": "fisher-kpp-special-front",
  "keller-segel-forced-flux": "keller-segel-forced-flux",
  "schnakenberg-2d-boundary-modes": "schnakenberg-2d-boundary-modes",
  "deterministic-thermostat-contrasts": "thermostatted-quartic",
  "projected-canonical-dof": "projected-canonical-dof",
  "atomic-reference-cards": "helium-ground-state",
  "h2-rhf-uhf-fci": "h2-rhf",
  "h3plus-mp2-fci": "h3plus-minimal",
  "periodic-he-reference-cards": "periodic-he-forces",
  "periodic-projector-occupations": "finite-projector-fermi",
  "quantum-box-ho": "quantum-box-ho",
  "two-state-bo-cp-ou": "two-state-bo-cp-model",
  "gsph-sod": "sod",
  "saltzman-ale-piston": "saltzman-ale-piston",
  "sph-pressure-acoustics": "sph-pressure-acoustics",
  "sphere-zonal-balance": "sphere-zonal-balance",
  "williamson-sphere-transport": "williamson-sphere-transport"
 },
 "newProblems": [
  "finite-projector-fermi",
  "fisher-kpp-special-front",
  "h3plus-minimal",
  "hodgkin-huxley-controls",
  "immigration-death-ssa",
  "keller-segel-forced-flux",
  "projected-canonical-dof",
  "quantum-box-ho",
  "saltzman-ale-piston",
  "schnakenberg-2d-boundary-modes",
  "sph-pressure-acoustics",
  "sphere-zonal-balance",
  "two-state-bo-cp-model",
  "williamson-sphere-transport"
 ],
 "reusedProblems": [
  "h2-rhf",
  "helium-ground-state",
  "periodic-he-forces",
  "sod",
  "thermostatted-quartic"
 ]
};
const origin='https://hrkoyama.github.io',pngSignature=Buffer.from('89504e470d0a1a0a','hex');
const registry=read('numerical-methods-atlas/validation/releases.json');
const expansion=read('catalog/atlas-depth-expansion.json');
const gallerySources=new Map(read('catalog/atlas-gallery.json').items.map(row=>[row.id,row]));
const images=new Map(),cases=[],study=new Map();
function fixtureImageRoutes(baseURL){
 const base=new URL(baseURL);
 assert.equal(base.protocol,'http:');assert.equal(base.hostname,'127.0.0.1');
 for(const field of ['username','password','search','hash'])assert.equal(base[field],'');
 assert.equal(base.pathname,'/');
 const routes=new Map(images);
 for(const image of images.values())routes.set(new URL(image.path,base).href,image);
 return routes;
}
for(const [group,fixed] of Object.entries(policy.groups)){
 const matches=registry.releases.filter(row=>row.group===group);assert.equal(matches.length,1,group);
 const release=matches[0],base=new URL(release.base);
 assert.equal(base.origin,origin);assert.equal(base.pathname,`/code/validated-examples/${fixed.edition}/${group}/`);
 assert.equal(base.username,'');assert.equal(base.password,'');assert.equal(base.search,'');assert.equal(base.hash,'');
 assert.equal(release.edition,fixed.edition);assert.deepEqual([...release.case_ids].sort(),[...fixed.ids].sort());
 assert.equal(release.manifest_sha256,fixed.manifest);assert.equal(release.verification_sha256,fixed.verification);
 const manifestBytes=readFileSync(new URL(`.${base.pathname}source-manifest.json`,root));
 assert.equal(digest(manifestBytes),fixed.manifest);const manifest=JSON.parse(manifestBytes);
 let metadata=read(`.${base.pathname}cases.json`);metadata=Array.isArray(metadata)?metadata:metadata.cases;
 for(const [name,hash] of Object.entries(manifest.files)){
  if(!/^results\/[A-Za-z0-9][A-Za-z0-9_.-]*\.png$/.test(name))continue;
  const url=new URL(name,base),bytes=readFileSync(new URL('.'+url.pathname,root));
  assert(bytes.subarray(0,8).equals(pngSignature));assert.equal(digest(bytes),hash);
  images.set(url.href,{path:url.pathname,sha256:hash});
 }
 for(const id of fixed.ids){
  const meta=metadata.filter(row=>row.id===id);assert.equal(meta.length,1);
  assert.equal(expansion.case_problem_ids[id],policy.problemByCase[id]);
  const png=new URL(`results/${id}.png`,base);assert(images.has(png.href),id+'/primary');
  cases.push({id,group,release,title:meta[0].title,png:png.href});
 }
 if(['biology-space-controls','thermostat-constraint-controls'].includes(group)){
  const stored=read(`.${base.pathname}results/result.json`);
  for(const [id,prefix] of Object.entries({'deterministic-thermostat-contrasts':'NH/','schnakenberg-2d-boundary-modes':'Schnakenberg/'})){
   if(!fixed.ids.includes(id))continue;
   const goals=Object.entries(stored.study_goals).filter(([name])=>name.startsWith(prefix)).map(([name,value])=>({name,stored:value}));
   assert(goals.length);assert(goals.every(row=>[true,false,null].includes(row.stored.observed)));
   const counts={met:goals.filter(row=>row.stored.observed===true).length,unmet:goals.filter(row=>row.stored.observed===false).length,unresolved:goals.filter(row=>row.stored.observed===null).length,total:goals.length};
   if(id==='deterministic-thermostat-contrasts')assert.equal(counts.unmet,117);
   else assert.equal(counts.unresolved,1);
   study.set(id,{goals,counts,result:manifest.files['results/result.json'],acceptance:manifest.files['acceptance.json']});
  }
 }
}
assert.equal(cases.length,19);assert.equal(new Set(cases.map(row=>row.id)).size,19);
assert.equal(policy.newProblems.length,14);assert.equal(policy.reusedProblems.length,5);
assert.equal(new Set(Object.values(policy.problemByCase)).size,19);
for(const item of cases){
 if(policy.newProblems.includes(policy.problemByCase[item.id]))assert.equal(gallerySources.get(policy.problemByCase[item.id]).source,new URL(item.png).pathname);
}
const skillBase='/numerical-methods-atlas/skills/0.1.0/';
const skillManifest=read(skillBase.slice(1)+'manifest.json');
assert.equal(skillManifest.name,'nan-numerics');assert.equal(skillManifest.version,'0.1.0');
assert.equal(skillManifest.archive.bytes,3961);assert.equal(skillManifest.archive.file,'nan-numerics-0.1.0.zip');
assert.equal(skillManifest.archive.sha256,'0be858df2e290a9df5c5b4fb49dc2a7e269db89f3587829eb15053deb8834139');
assert.deepEqual(Object.keys(skillManifest.files).sort(),['nan-numerics/LICENSE','nan-numerics/SKILL.md','nan-numerics/references/public-resources.md']);

test('final23 execution figures, typed study outcomes, gallery bindings and skill guide',async({page,baseURL},info)=>{
 test.setTimeout(120_000); // Only this new bounded test; existing project timeouts stay unchanged.
 const language=info.project.metadata.language,width=info.project.use.viewport.width;
 expect(['ja','en']).toContain(language);expect([390,1280]).toContain(width);
 const collectionClicks=[];
 const routedImages=fixtureImageRoutes(baseURL),fixtureOrigin=new URL(baseURL).origin;
 const errors=[],mirrored=[],visited=[],zipRequests=[];
 page.on('pageerror',error=>errors.push(error.message));
 await page.route(url=>url.pathname.endsWith('.zip'),route=>{zipRequests.push(route.request().url());return route.abort('blockedbyclient');});
 await page.route(url=>routedImages.has(url.href),async route=>{
  const original=new URL(route.request().url()),fixture=routedImages.get(original.href);
  expect(route.request().method()).toBe('GET');expect([origin,fixtureOrigin]).toContain(original.origin);
  const target=new URL(fixture.path,baseURL);
  const response=await route.fetch({url:target.href,method:'GET',headers:{accept:'image/png'},maxRedirects:0,maxRetries:0});
  expect(response.status()).toBe(200);expect(response.headers()['content-type']).toMatch(/^image\/png(?:;|$)/i);
  const bytes=await response.body();expect(bytes.subarray(0,8).equals(pngSignature)).toBe(true);expect(digest(bytes)).toBe(fixture.sha256);
  mirrored.push({public_url:new URL(fixture.path,origin).href,requested_url:original.href,local_url:target.href,sha256:fixture.sha256});await route.fulfill({response,body:bytes});
 });
 try{
  // Each top-level category opens its actual list with the correct initial scope.
  const homeCopy=read('catalog/atlas-home.json').landing[language].collection;
  const collectionExpected={papers:read('numerical-methods-atlas/coverage.json').counts.papers,books:read('numerical-methods-atlas/coverage.json').counts.books,methods:read('numerical-methods-atlas/methods/index.json').methods.length,tests:read('numerical-methods-atlas/gallery/index.json').items.length,solutions:read('numerical-methods-atlas/solutions/index.json').count,equations:read('numerical-methods-atlas/equations/index.json').equations.length,fields:read('catalog/atlas-reading-index.json').groups.length};
  for(const item of homeCopy.items){
   await page.goto(`/numerical-methods-atlas/?lang=${language}`,{waitUntil:'domcontentloaded'});
   const panel=page.locator('.home-collection:visible'),link=panel.locator(`[data-home-collection-item="${item.id}"]`);await expect(panel).toBeVisible();await expect(panel.locator('[data-home-collection-item]')).toHaveCount(7);
   await expect(link).toContainText(String(collectionExpected[item.id]));await expect(link).toContainText(item.label);
   const expected=new URL(item.href,baseURL);await link.click();await expect.poll(()=>{const url=new URL(page.url());return url.pathname+url.search+url.hash;}).toBe(expected.pathname+expected.search+expected.hash);
   if(['papers','books'].includes(item.id)){
    await expect(page.locator('#reference-search')).toHaveValue(item.id==='papers'?'type:paper':'type:book');
    await expect(page.locator('.reference-item')).toHaveCount(collectionExpected[item.id]);
    const actual=await page.locator('.reference-item .reference-links code').allTextContents();
    const desired=read('numerical-methods-atlas/coverage.json').publications.filter(row=>item.id==='papers'?['article','inproceedings'].includes(row.type):row.type==='book').map(row=>row.id);expect(actual.sort()).toEqual(desired.sort());
   }else if(item.id==='methods'){
    const active=page.locator(`[data-site-language="${language}"]`);await expect(active.locator('[data-method-status]')).toHaveValue('all');await expect(active.locator('[data-method-query]')).toHaveValue('');await expect(active.locator('[data-method-id]')).toHaveCount(collectionExpected.methods);
   }else if(item.id==='tests'){
    const active=page.locator(`[data-gallery][data-site-language="${language}"]`);await expect(active.locator('[data-gallery-group="all"]')).toHaveAttribute('aria-pressed','true');await expect(active.locator(`[id="gallery-query-${language}"]`)).toHaveValue('');await expect(active.locator('[data-problem-id]')).toHaveCount(collectionExpected.tests);
   }else if(item.id==='solutions'){
    const active=page.locator(`[data-site-language="${language}"]`);await expect(active.locator('[data-solution-id]')).toHaveCount(collectionExpected.solutions);
    for(const [kind,count]of Object.entries(read('numerical-methods-atlas/solutions/index.json').counts))await expect(active.locator(`[data-solution-kind="${kind}"]`)).toHaveCount(count);
   }else if(item.id==='equations')await expect(page.locator(`[data-site-language="${language}"] [data-equation-id]`)).toHaveCount(collectionExpected.equations);
   else{await expect(page.locator('[data-reading-group]')).toHaveCount(collectionExpected.fields);await expect(page.locator('[data-reading-input]')).toHaveValue('');}
   const overflowMetrics=await page.evaluate(()=>({url:location.href,scrollWidth:document.documentElement.scrollWidth,clientWidth:document.documentElement.clientWidth,innerWidth:window.innerWidth,fontStatus:document.fonts?.status||'unavailable'}));
   expect(overflowMetrics.scrollWidth-overflowMetrics.clientWidth,'Collection overflow: '+JSON.stringify(overflowMetrics)).toBeLessThanOrEqual(1);collectionClicks.push({id:item.id,count:collectionExpected[item.id],path:new URL(page.url()).pathname,hash:new URL(page.url()).hash});
  }
  for(const item of cases){
   const response=await page.goto(`/numerical-methods-atlas/validation/${item.id}/?lang=${language}`,{waitUntil:'domcontentloaded'});expect(response.status()).toBe(200);
   const active=page.locator(`[data-site-language="${language}"]`),article=active.locator(`[data-validation-case="${item.id}"]`);
   await expect(article).toHaveCount(1);await expect(article.locator('h1')).toBeVisible();await expect(article.locator('h1')).toHaveText(item.title[language]);
   await expect(page.locator('h1:visible')).toHaveCount(1);
   const image=article.locator(':scope > figure:not(.validation-additional-figure) > img');
   await expect(image).toHaveCount(1);expect(await image.evaluate(node=>node.src)).toBe(new URL(new URL(item.png).pathname,baseURL).href);
   await image.scrollIntoViewIfNeeded();await expect(image).toBeVisible();
   await expect.poll(()=>image.evaluate(node=>node.complete&&node.naturalWidth>0&&node.naturalHeight>0)).toBe(true);
   const zip=article.locator('.validation-actions a').filter({hasText:'ZIP'});
   await expect(zip).toHaveCount(1);await expect(zip).toBeVisible();
   expect(await zip.evaluate(node=>node.href)).toBe(new URL(new URL(item.release.archive,item.release.base).pathname,baseURL).href);
   await expect(page.locator('.katex-error,.katex .merror')).toHaveCount(0);
   if(study.has(item.id)){
    const expected=study.get(item.id),counts=expected.counts;
    const goals=article.locator('[data-typed-study-outcomes="true"]');await expect(goals).toHaveCount(1);await expect(goals).toBeVisible();
    const headline=language==='ja'?`調査した目標：達成${counts.met}・未達${counts.unmet}・未確定${counts.unresolved}（全${counts.total}）`:`Study goals: ${counts.met} met, ${counts.unmet} unmet, ${counts.unresolved} unresolved (${counts.total} total)`;
    await expect(goals.locator('h2')).toHaveText(headline);await expect(goals.locator('h2')).toBeVisible();
    expect(await goals.getAttribute('data-result-sha256')).toBe(expected.result);expect(await goals.getAttribute('data-acceptance-sha256')).toBe(expected.acceptance);
    const details=goals.locator('details');await details.locator('summary').click();await expect(details.locator('table')).toBeVisible();
    const rows=await details.locator('tbody > tr').evaluateAll(nodes=>nodes.map(row=>({name:row.querySelector('th').textContent.trim(),outcome:row.querySelector('td').textContent.trim(),stored:JSON.parse(row.querySelector('code').textContent)})));
    expect(rows).toHaveLength(expected.goals.length);
    const expectedByName=new Map(expected.goals.map(row=>[row.name,row.stored]));expect(new Set(rows.map(row=>row.name)).size).toBe(rows.length);
    for(const row of rows){expect(row.stored).toEqual(expectedByName.get(row.name));const label=row.stored.observed===null?'unresolved':row.stored.observed?'met':'unmet';expect(row.outcome).toBe(language==='ja'?{met:'達成',unmet:'未達',unresolved:'未確定'}[label]:label);}
    if(item.id==='deterministic-thermostat-contrasts')expect(rows.filter(row=>row.stored.observed===false)).toHaveLength(117);
    else expect(rows.filter(row=>row.stored.observed===null)).toHaveLength(1);
   }
   expect(await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth)).toBeLessThanOrEqual(1);
   visited.push(item.id);
  }
  // Physical-problem identity is distinct from execution identity. Existing He/H2/Sod pictures remain valid.
  let response=await page.goto(`/numerical-methods-atlas/gallery/?lang=${language}`,{waitUntil:'domcontentloaded'});expect(response.status()).toBe(200);
  const gallery=page.locator(`[data-gallery][data-site-language="${language}"]`);await expect(gallery).toBeVisible();
  for(const item of cases){
   const problem=policy.problemByCase[item.id],tile=gallery.locator(`[data-problem-id="${problem}"]`);await expect(tile).toHaveCount(1);await expect(tile).toBeVisible();
   const entry=tile.locator(`[data-supplemental-execution="${item.id}"] a`);await expect(entry).toHaveCount(1);await expect(entry).toBeVisible();
   const destination=new URL(await entry.getAttribute('href'),page.url());expect(destination.origin).toBe(origin);expect(destination.pathname).toBe(`/numerical-methods-atlas/validation/${item.id}/`);expect(destination.searchParams.get('lang')).toBe(language);
   if(policy.newProblems.includes(problem))expect(new URL(await tile.locator('.gallery-image-link img').getAttribute('src'),page.url()).pathname).toBe(new URL(item.png).pathname);
  }
  response=await page.goto(`/numerical-methods-atlas/skills/?lang=${language}`,{waitUntil:'domcontentloaded'});expect(response.status()).toBe(200);
  const skill=page.locator(`[data-site-language="${language}"]`);await expect(skill).toBeVisible();await expect(page.locator('h1:visible')).toHaveCount(1);
  await expect(skill.locator('h1')).toHaveText(language==='ja'?'NaNを使うスキル':'Develop with NaN');await expect(skill).toContainText('3,961 bytes');
  const download=skill.locator('a[download]');await expect(download).toHaveCount(1);await expect(download).toBeVisible();expect(new URL(await download.getAttribute('href'),page.url()).pathname).toBe(skillBase+skillManifest.archive.file);
  const manifest=skill.locator(`a[href="${skillBase}manifest.json"]`);await expect(manifest).toHaveCount(1);await expect(manifest).toBeVisible();
  for(const name of Object.keys(skillManifest.files))await expect(skill.locator(`a[href="${skillBase}${name}"]`)).toBeVisible();
  expect(await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth)).toBeLessThanOrEqual(1);
  expect(visited).toHaveLength(19);expect(zipRequests).toEqual([]);expect(errors).toEqual([]);
  await info.attach('final23-ui-coverage',{body:Buffer.from(JSON.stringify({scope:'Candidate UI integration only; no scientific execution, ZIP bodies or actual public-HR success claim.',language,width,collectionClicks,visited,new_physical_problems:policy.newProblems,reused_physical_problems:policy.reusedProblems,mirrored,zip_requests:zipRequests,pageerrors:errors},null,2)),contentType:'application/json'});
 }finally{await page.unrouteAll({behavior:'wait'});}
});
