// UI/resource checks only. Scientific solvers, references and ZIP bodies are
// covered by their independent immutable-release and public-Linux checks.
import {test,expect} from '@playwright/test';
import {readFileSync} from 'node:fs';
import {writeFile} from 'node:fs/promises';
import {gzipSync} from 'node:zlib';
import {methodCount,methodStatusCounts} from '../scripts/fixtures/atlas-inventory.mjs';
const budgets=JSON.parse(readFileSync(new URL('../search/budgets.json',import.meta.url)));

test('home → search → execution, method filter and mathematical article',async({page},info)=>{
 const language=info.project.metadata.language;
 const assetErrors=[],pageErrors=[],requests=[];
 page.on('pageerror',error=>pageErrors.push(error.message));
 page.on('request',request=>requests.push(request.url()));
 page.on('response',response=>{
  if(response.status()>=400&&['document','script','stylesheet','image','font','fetch'].includes(response.request().resourceType()))assetErrors.push(`${response.status()} ${response.url()}`);
 });
 const noOverflow=async()=>expect(await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth)).toBeLessThanOrEqual(1);
 const stylesApplied=async(path)=>expect.poll(()=>page.evaluate(path=>Array.from(document.styleSheets).some(sheet=>sheet.href?.includes(path)&&sheet.cssRules.length>0),path)).toBe(true);

 await page.goto(`/numerical-methods-atlas/?lang=${language}`);
 const input=page.locator('#home-search-input');await expect(input).toBeVisible();
 await stylesApplied('/numerical-methods-atlas/home-overview.css');
 await expect(page.locator('.home-search-controls')).toHaveCSS('display','flex');
 await noOverflow();
 expect(requests.some(url=>/\/search\/(?:atlas-)?query-index[.]json/.test(url))).toBe(false);
 const responsePromise=page.waitForResponse(response=>new URL(response.url()).pathname==='/search/atlas-query-index.json');
 await input.fill('Sod test');await input.press('Tab');
 const button=page.locator('#home-search-form button');await expect(button).toBeFocused();await button.press('Enter');
 const first=page.locator('#home-search-results > li').first().locator('a').first();
 await expect(first).toHaveAttribute('href',new RegExp('/examples/sod/[?]lang='+language));
 const indexResponse=await responsePromise,body=await indexResponse.body();
 expect(body.length).toBeLessThanOrEqual(budgets.atlas.decoded_bytes);
 expect(gzipSync(body,{level:9}).length).toBeLessThanOrEqual(budgets.atlas.gzip_bytes);
 const transfer={index:new URL(indexResponse.url()).pathname,decoded_bytes:body.length,gzip_level9_bytes:gzipSync(body,{level:9}).length,content_encoding:indexResponse.headers()['content-encoding']||'identity',scope:'Local CI static server; gzip is a modeled byte budget, not a network timing or CDN transfer measurement.'};
 await writeFile(info.outputPath('index-transfer.json'),JSON.stringify(transfer,null,2));
 const homeHref=await first.getAttribute('href');
 await page.locator('#home-search-all').click();
 await expect(page).toHaveURL(/\/search\/[?].*scope=atlas.*#q=Sod%20test/);
 const globalFirst=page.locator('#search-results > li').first().locator('h2 a');
 await expect(globalFirst).toHaveAttribute('href',homeHref);
 const context=page.locator('#search-results .search-navigation-context').first();
 await context.locator('summary').click();
 const scopeNote=context.locator('.search-navigation-context-body > p.search-navigation-note');await expect(scopeNote).toHaveCount(1);await expect(scopeNote).toContainText(language==='ja'?'固定入力':'fixed');
 await noOverflow();
 await page.screenshot({path:info.outputPath('search-result.png'),fullPage:true});
 await globalFirst.click();
 await expect(page).toHaveURL(/\/code-and-data\/examples\/sod\//);
 await expect(page.getByRole('heading',{level:1,name:/Sod/})).toBeVisible();
 const download=page.locator('a[href$=".zip"]:visible').first();await expect(download).toBeVisible();
 const downloadPath=new URL(await download.getAttribute('href'),page.url()).pathname;
 expect((await page.request.head(downloadPath)).ok()).toBe(true);

 await page.goto(`/numerical-methods-atlas/methods/?lang=${language}`);
 const map=page.locator(`[data-method-map][lang="${language}"]`);await expect(map).toBeVisible();
 await stylesApplied('/styles/atlas-methods.css');await expect(map.locator('.method-filter-fields')).toHaveCSS('display','grid');
 await map.locator('[data-method-query]').fill('WENO');
 const rows=map.locator('[data-method-id]:visible');await expect(rows).not.toHaveCount(0);
 for(const row of await rows.all())expect((await row.getAttribute('data-search')).toLowerCase()).toContain('weno');
 await map.locator('[data-method-query]').fill('');await map.locator('[data-method-status]').selectOption('planned');await expect(map.locator('[data-method-id]:visible')).toHaveCount(methodStatusCounts.planned);for(const row of await map.locator('[data-method-id]:visible').all())expect(await row.getAttribute('data-status')).toBe('planned');
 await map.locator('[data-method-reset]').click();await expect(map.locator('[data-method-query]')).toHaveValue('');await expect(map.locator('[data-method-status]')).toHaveValue('all');await expect(map.locator('[data-method-id]:visible')).toHaveCount(methodCount);
 await noOverflow();

 await page.goto(`/numerical-methods-atlas/${language}/read/spectral-element/`);
 await expect(page.getByRole('heading',{level:1,name:language==='ja'?/スペクトル要素/:/Spectral elements/})).toBeVisible();
 await expect(page.locator('.katex').first()).toBeVisible();await expect(page.locator('.katex-error,.katex .merror')).toHaveCount(0);
 const table=page.locator('article [role="region"][tabindex="0"]').filter({has:page.locator('table')}).first();await expect(table).toBeVisible();
 await table.focus();await expect(table).toBeFocused();
 const dimensions=await table.evaluate(node=>({content:node.scrollWidth,viewport:node.clientWidth}));
 if(info.project.use.viewport.width===390){expect(dimensions.content).toBeGreaterThan(dimensions.viewport);await page.keyboard.press('ArrowRight');await expect.poll(()=>table.evaluate(node=>node.scrollLeft)).toBeGreaterThan(0);}
 await noOverflow();await page.screenshot({path:info.outputPath('article.png')});
 expect(requests.some(url=>/\/(?:search\/index|numerical-methods-atlas\/home-search-index)[.]json/.test(url))).toBe(false);
 expect(requests.some(url=>new URL(url).search.includes('Sod%20test'))).toBe(false);
 expect(assetErrors).toEqual([]);expect(pageErrors).toEqual([]);
});
