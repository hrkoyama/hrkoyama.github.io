// Actual rendered routes and saved figures; no solver or ZIP body is run here.
import {test,expect} from '@playwright/test';
import {readFileSync} from 'node:fs';
const registry=JSON.parse(readFileSync(new URL('../numerical-methods-atlas/validation/releases.json',import.meta.url)));
const examples=['lbm-cylinder-re20','shadow-absorber2d','correlated-gaussian-mcmc'];

test('new fluid, radiation and probability examples show figures and executable downloads',async({page},info)=>{
 const language=info.project.metadata.language;
 const errors=[];
 page.on('pageerror',error=>errors.push(error.message));
 for(const id of examples){
  await page.goto(`/numerical-methods-atlas/validation/${id}/?lang=${language}`);
  await expect(page.locator('h1:visible')).toHaveCount(1);
  const figure=page.locator(`img[src*="/results/${id}"]:visible`).first();
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
 expect(errors).toEqual([]);
});
