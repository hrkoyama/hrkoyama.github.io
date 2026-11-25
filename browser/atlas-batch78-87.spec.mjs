// DRAFT candidate-server checks only. No solver, training or ZIP body is run.
// Actual HR publication UI verification remains a separate post-Pages task.
import {test,expect} from '@playwright/test';
import {readFileSync} from 'node:fs';
import {writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const root=new URL('../',import.meta.url),read=p=>JSON.parse(readFileSync(new URL(p,root)));
const registry=read('numerical-methods-atlas/validation/releases.json');
const freeze=read('scripts/fixtures/atlas-batch78-87-freeze.json');
const landingCopy=read('catalog/atlas-home.json').landing;
if(freeze.status!=='ROOT_REVIEWED_ACTUAL_CANONICAL_FREEZE')throw new Error('Actual canonical freeze required');
const EXPECTED={
 'quadrature-controls':['quadpack-domain-selection','gk15-double-exponential','tensor-smolyak-dimensions'],
 'approximation-controls':['runge-barycentric-clenshaw','spline-shape-controls','haar-mallat-boundary-threshold'],
 'small-models':['pinn-poisson','fno-periodic-heat','enzyme-qssa','lotka-volterra','seir-linearization'],
};
const representatives=['quadpack-domain-selection','runge-barycentric-clenshaw','fno-periodic-heat'];
const publicOrigin='https://hrkoyama.github.io',pngSignature=Buffer.from('89504e470d0a1a0a','hex');
const digest=body=>createHash('sha256').update(body).digest('hex');
const fixtures=new Map();
for(const [group,ids] of Object.entries(EXPECTED)){
 const releases=registry.releases.filter(r=>r.group===group);
 if(releases.length!==1)throw new Error('Missing or duplicate group');
 const release=releases[0],base=new URL(release.base),fixed=freeze.canonical_packets[group];
 if(base.origin!==publicOrigin||base.username||base.password||base.search||base.hash||release.edition!==fixed.edition)throw new Error('Unexpected release provenance');
 if(JSON.stringify([...release.case_ids].sort())!==JSON.stringify([...ids].sort()))throw new Error('Case inventory mismatch');
 const body=readFileSync(new URL(`.${base.pathname}source-manifest.json`,root));
 if(digest(body)!==release.manifest_sha256||release.manifest_sha256!==fixed.manifest_sha256)throw new Error('Manifest mismatch');
 for(const [name,hash] of Object.entries(JSON.parse(body).files)){
  if(!ids.some(id=>name.startsWith(`results/${id}`))||!name.endsWith('.png'))continue;
  const url=new URL(name,base);
  if(url.origin!==publicOrigin||!url.pathname.startsWith(base.pathname+'results/')||url.search||url.hash||name.includes('..'))throw new Error('Unexpected figure path');
  const png=readFileSync(new URL('.'+url.pathname,root));
  if(!png.subarray(0,8).equals(pngSignature)||digest(png)!==hash)throw new Error('PNG mismatch');
  fixtures.set(url.href,{path:url.pathname,sha256:hash});
 }
}

test('three new groups render their own figures, code and reference routes',async({page,baseURL},info)=>{
 const language=info.project.metadata.language,errors=[],mirrored=[];
 expect(['ja','en']).toContain(language);
 expect([390,1280]).toContain(info.project.use.viewport.width);
 page.on('pageerror',error=>errors.push(error.message));
 try {
 await page.route('**/*.zip',route=>route.request().method()==='HEAD'?route.continue():route.abort('blockedbyclient'));
 // Introduction/contact follow-up: inspect mailto attributes only, never send mail.
 const contactEmail='hrkoyamacontact@gmail.com',contactHref='mailto:'+contactEmail;
 await page.goto(`/?lang=${language}`);
 const portfolio=page.locator(`[data-site-language="${language}"]`);
 const atlasHomeURL=new URL('/numerical-methods-atlas/?lang='+language,page.url()).href;
 const atlasFeature=portfolio.locator(`.home-feature`).filter({has:page.locator(`h3 a[href="${atlasHomeURL}"]`)});
 await expect(atlasFeature.locator('h3 a')).toHaveText(language==='ja'?'NaN — 数値計算アトラス':'NaN — An Atlas of Numerical Methods');
 await expect(atlasFeature).toBeVisible();
 const profileContact=page.locator(`#profile-${language} a[href="${contactHref}"]`);
 await expect(profileContact).toHaveCount(1);await expect(profileContact).toBeVisible();await expect(profileContact).toHaveText(contactEmail);
 // Current home branding only; fixed chapter names and published editions stay descriptive.
 const siteTitle='NaN — Not just Algorithms, but Numerics.';
 await page.goto(`/numerical-methods-atlas/?lang=${language}`);
 await expect(page).toHaveTitle(siteTitle);
 await expect(page.locator('main h1:visible')).toHaveCount(1);
 await expect(page.locator('main h1:visible')).toHaveText(siteTitle);
 const home=page.locator('#home-overview'),intro=landingCopy[language].introduction;
 await expect(home.locator('.landing-description')).toHaveText(landingCopy[language].description);
 const beginner=home.locator('.landing-beginner'),beginnerCopy=landingCopy[language].beginner;
 await expect(beginner.locator('p')).toHaveText(beginnerCopy.title);
 await expect(beginner.locator('a')).toHaveCount(2);
 for(const kind of ['web','pdf']){
  const link=beginner.locator(`[data-home-beginner="${kind}"]`);
  await expect(link).toBeVisible();await expect(link).toBeInViewport({ratio:1});await expect(link).toHaveText(beginnerCopy[kind].label);
  expect(await link.evaluate(node=>node.href)).toBe(new URL(beginnerCopy[kind].href,page.url()).href);
 }
 expect(await beginner.locator('[data-home-beginner="pdf"]').getAttribute('download')).toBeNull();
 for(const key of ['why','connections','ai']){
  const paragraph=home.locator(`[data-home-purpose="${key}"]`);
  await expect(paragraph).toHaveCount(1);await expect(paragraph).toBeVisible();await expect(paragraph).toHaveText(intro[key]);
 }
 await expect(home.locator('.landing-purpose details,.landing-purpose [hidden]')).toHaveCount(0);
 await expect(home.locator('.landing-ways')).toHaveText(intro.ways);
 await expect(home.locator('.home-entrypoints [data-home-entry]')).toHaveCount(3);
 await expect(home.locator('.landing-feedback p')).toBeVisible();await expect(home.locator('.landing-feedback p')).toHaveText(intro.feedback);
 expect(await home.evaluate(root=>{
  const nodes=['.landing-description','.landing-beginner','.landing-purpose','.home-search','.landing-ways','.home-entrypoints','.landing-feedback','a[href^="mailto:"]'].map(selector=>root.querySelector(selector));
  return nodes.every(Boolean)&&nodes.slice(1).every((node,index)=>!!(nodes[index].compareDocumentPosition(node)&Node.DOCUMENT_POSITION_FOLLOWING));
 })).toBe(true);
 await expect(page.locator('.site-header .brand > span:last-child')).toHaveText('NaN');
 const homeContact=page.locator(`#home-overview a[href="${contactHref}"]`);
 await expect(homeContact).toHaveCount(1);await expect(homeContact).toBeVisible();await expect(homeContact).toHaveText(contactEmail);
 expect(await page.locator('meta[property="og:title"]').getAttribute('content')).toBe(siteTitle);
 expect(await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth)).toBeLessThanOrEqual(1);
 await page.route(url=>fixtures.has(url.href),async route=>{
  const original=new URL(route.request().url()),fixture=fixtures.get(original.href);
  expect(original.origin).toBe(publicOrigin);expect(original.username).toBe('');expect(original.password).toBe('');expect(route.request().method()).toBe('GET');
  const target=new URL(fixture.path,baseURL);
  const response=await route.fetch({url:target.href,method:'GET',headers:{accept:'image/png'},maxRedirects:0,maxRetries:0});
  expect(response.status()).toBe(200);expect(response.headers()['content-type']).toMatch(/^image\/png(?:;|$)/i);
  const body=await response.body();expect(body.subarray(0,8).equals(pngSignature)).toBe(true);expect(digest(body)).toBe(fixture.sha256);
  mirrored.push({public_url:original.href,local_url:target.href,sha256:fixture.sha256});await route.fulfill({response,body});
 });
 for(const id of representatives){
  const release=registry.releases.find(r=>r.case_ids.includes(id));expect(release).toBeTruthy();
  const validation=`/numerical-methods-atlas/validation/${id}/?lang=${language}`;
  await page.goto(validation);await expect(page.locator('h1:visible')).toHaveCount(1);
  await expect(page.locator(`[data-site-language="${language}"]`)).toBeVisible();
  const image=page.locator(`figure:not(.validation-additional-figure)>img[src$="/results/${id}.png"]:visible`);
  await expect(image).toHaveCount(1);await image.scrollIntoViewIfNeeded();await expect(image).toBeVisible();
  await expect.poll(()=>image.evaluate(node=>node.complete&&node.naturalWidth>0)).toBe(true);
  await expect(page.locator('.katex-error,.katex .merror')).toHaveCount(0);
  expect(await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth)).toBeLessThanOrEqual(1);
  const details=page.locator('details:visible').filter({has:page.locator(`a[href="${release.base}run.py"]`)});
  await expect(details).toHaveCount(1);await details.locator('summary').click();
  const code=details.locator(`a[href="${release.base}run.py"]`);await expect(code).toBeVisible();
  const codeURL=new URL(await code.getAttribute('href'));expect(codeURL.origin).toBe(publicOrigin);
  expect((await page.request.head(codeURL.pathname)).ok()).toBe(true);
  const reference=page.locator(`[data-execution-reference-id="${id}"] [data-execution-reference-link]:visible`);
  await expect(reference).toHaveCount(1);const referenceURL=new URL(await reference.getAttribute('href'),page.url());
  expect(referenceURL.pathname).toBe('/numerical-methods-atlas/solutions/');expect(referenceURL.searchParams.get('lang')).toBe(language);expect(referenceURL.hash).toBe(`#solution-${id}-${language}`);
  const readingURL=new URL(`/numerical-methods-atlas/${language}/read/validation-${release.group}/`,page.url());readingURL.searchParams.set('lang',language);readingURL.hash=id;
  const reading=page.locator(`a[href="${readingURL.href}"]:visible`).first();await expect(reading).toBeVisible();
  const zip=page.locator('a[href$=".zip"]:visible').first();await expect(zip).toBeVisible();
  const zipURL=new URL(await zip.getAttribute('href'),page.url());expect(zipURL.pathname).toBe(new URL(release.archive,release.base).pathname);expect((await page.request.head(zipURL.pathname)).ok()).toBe(true);
  await image.screenshot({path:info.outputPath(id+'.png')});
  await page.goto(referenceURL.pathname+referenceURL.search+referenceURL.hash);
  await expect(page.locator(referenceURL.hash)).toBeVisible();
  const back=page.locator(`a[href*="/validation/${id}/?lang=${language}"]:visible`).first();await expect(back).toBeVisible();
 }
 } finally {
  await page.unrouteAll({behavior:'wait'});
 }
 expect(errors).toEqual([]);
 await writeFile(info.outputPath('candidate-figure-mirror.json'),JSON.stringify({scope:'Candidate-only exact HR manifest PNG paths mirrored to the local server; no ZIP bodies, numerical runs or public-UI completion claim.',representatives,language,viewport:info.project.use.viewport,mirrored},null,2));
});
