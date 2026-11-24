// Actual rendered routes and saved figures; no solver or ZIP body is run here.
import {test,expect} from '@playwright/test';
import {readFileSync} from 'node:fs';
import {writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const registry=JSON.parse(readFileSync(new URL('../numerical-methods-atlas/validation/releases.json',import.meta.url)));
const examples=['lbm-cylinder-re20','shadow-absorber2d','correlated-gaussian-mcmc'];
const publicOrigin='https://hrkoyama.github.io';
const pngSignature=Buffer.from('89504e470d0a1a0a','hex');
const digest=body=>createHash('sha256').update(body).digest('hex');
// Candidate figures may have absolute production URLs before they are published.
// Mirror only exact, manifest-bound PNG URLs, including navigation thumbnails.
const figureFixtures=new Map();
for(const id of examples){
 const release=registry.releases.find(row=>row.case_ids.includes(id));
 const base=new URL(release.base);
 if(base.origin!==publicOrigin||base.username||base.password)throw new Error('Unexpected release origin');
 const manifestBytes=readFileSync(new URL(`..${base.pathname}source-manifest.json`,import.meta.url));
 if(digest(manifestBytes)!==release.manifest_sha256)throw new Error('Release manifest hash mismatch');
 for(const [path,sha256] of Object.entries(JSON.parse(manifestBytes).files)){
  if(!path.startsWith(`results/${id}`)||!path.endsWith('.png'))continue;
  const url=new URL(path,base);
  if(url.origin!==publicOrigin||!url.pathname.startsWith(`${base.pathname}results/`)||url.search||url.hash)throw new Error('Unexpected figure path');
  const body=readFileSync(new URL(`..${url.pathname}`,import.meta.url));
  if(!body.subarray(0,8).equals(pngSignature)||digest(body)!==sha256)throw new Error('Canonical PNG hash/signature mismatch');
  figureFixtures.set(url.href,{sha256,path:url.pathname});
 }
}

test('new fluid, radiation and probability examples show figures and executable downloads',async({page,baseURL},info)=>{
 const language=info.project.metadata.language;
 const errors=[],mirrored=[];
 await page.route(url=>figureFixtures.has(url.href),async route=>{
  const original=new URL(route.request().url()),fixture=figureFixtures.get(original.href);
  expect(original.origin).toBe(publicOrigin);expect(original.username).toBe('');expect(original.password).toBe('');
  expect(route.request().method()).toBe('GET');
  const target=new URL(fixture.path,baseURL);
  // Explicit headers prevent forwarding production credentials to the local server.
  const response=await route.fetch({url:target.href,method:'GET',headers:{accept:'image/png'},maxRedirects:0,maxRetries:0});
  expect(response.status()).toBe(200);expect(response.headers()['content-type']).toMatch(/^image\/png(?:;|$)/i);
  const body=await response.body();expect(body.subarray(0,8).equals(pngSignature)).toBe(true);expect(digest(body)).toBe(fixture.sha256);
  mirrored.push({public_url:original.href,local_url:target.href,sha256:fixture.sha256,content_type:response.headers()['content-type']});
  await route.fulfill({response,body});
 });
 page.on('pageerror',error=>errors.push(error.message));
 for(const id of examples){
  await page.goto(`/numerical-methods-atlas/validation/${id}/?lang=${language}`);
  await expect(page.locator('h1:visible')).toHaveCount(1);
  const figure=page.locator(`figure:not(.validation-additional-figure) > img[src$="/results/${id}.png"]:visible`);
  await expect(figure).toHaveCount(1);
  await figure.scrollIntoViewIfNeeded();await expect(figure).toBeVisible();
  await expect.poll(()=>figure.evaluate(node=>node.complete&&node.naturalWidth>0)).toBe(true);
  await expect(page.locator('.katex-error,.katex .merror')).toHaveCount(0);
  expect(await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth)).toBeLessThanOrEqual(1);
  const download=page.locator('a[href$=".zip"]:visible').first();await expect(download).toBeVisible();
  const path=new URL(await download.getAttribute('href'),page.url()).pathname;
  const release=registry.releases.find(row=>row.case_ids.includes(id));expect(release).toBeTruthy();
  expect(path).toBe(new URL(release.archive,release.base).pathname);
  expect((await page.request.head(path)).ok()).toBe(true);
  await figure.screenshot({path:info.outputPath(`${id}.png`)});
 }
 await writeFile(info.outputPath('candidate-figure-mirror.json'),JSON.stringify({scope:'Exact HR manifest-bound PNG paths mirrored to the candidate server; no ZIP bodies or solver execution.',mirrored},null,2));
 expect(errors).toEqual([]);
});
