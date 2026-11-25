// Navigation tasks only: reuse the published scientific inputs and releases.
import {test,expect} from '@playwright/test';

test('choose learning order, full chapter index and the matching Bratu and Noh calculations',async({page,baseURL},info)=>{
 const lang=info.project.metadata.language,errors=[];
 page.on('pageerror',error=>errors.push(error.message));
 // The candidate server mirrors reviewed HR pages locally; downloads are checked
 // separately after publication. Never run or fetch a ZIP in this UI scenario.
 const base=new URL(baseURL);
 await page.route('https://hrkoyama.github.io/**',async route=>{
  const url=new URL(route.request().url());
  if(url.pathname.endsWith('.zip'))return route.abort('blockedbyclient');
  url.protocol=base.protocol;url.host=base.host;
  return route.fulfill({response:await route.fetch({url:url.href})});
 });
 const active=()=>page.locator(`[data-site-language="${lang}"]`);
 const noOverflow=async()=>expect(await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth)).toBeLessThanOrEqual(1);

 await page.goto(`/numerical-methods-atlas/?lang=${lang}`);
 await expect(page.locator('#home-search-input')).toBeVisible();
 await expect(page.locator('[data-home-entry]')).toHaveCount(3);
 await expect(page.locator('[data-home-beginner="web"]')).toBeVisible();
 await expect(page.locator('[data-home-beginner="pdf"]')).toBeVisible();
 await page.locator('[data-home-entry="read"]').click();
 await expect(page).toHaveURL(new RegExp(`/explore/.*lang=${lang}`));
 await expect(active().locator('[data-learning-guide-role]')).toBeVisible();
 await expect(active().locator('[data-learning-guide-paths]')).toBeVisible();
 await active().locator('[data-learning-guide-toc]').click();
 await expect(page).toHaveURL(new RegExp(`/${lang}/read/`));
 await expect(page.locator('[data-reading-index-role]')).toBeVisible();
 await expect(page.locator('[data-reading-group]')).toHaveCount(10);
 await expect(page.locator('[data-reading-learning-guide]')).toBeVisible();
 await noOverflow();
 const stability=page.locator('[data-reading-chapter="stability"] a');
 const readingField=await stability.evaluate(node=>node.closest('[data-reading-group]').getAttribute('data-reading-group'));
 await stability.click();
 await expect(page).toHaveURL(new RegExp(`/${lang}/read/stability/`));
 const sidebar=page.locator('aside.atlas-reading-nav');
 await expect(sidebar.locator('[data-reading-current-field]')).toHaveAttribute('data-reading-current-field',readingField);
 await expect(sidebar.locator('[data-reading-field-chapter="stability"]')).toHaveAttribute('aria-current','page');
 await expect(sidebar.locator('[data-reading-other-fields]')).not.toHaveAttribute('open','');
 if(info.project.use.viewport.width<=620){
  expect(await page.locator('article').evaluate(node=>node.getBoundingClientRect().top)).toBeLessThan(await sidebar.evaluate(node=>node.getBoundingClientRect().top));
 }
 await noOverflow();
 await page.screenshot({path:info.outputPath('stability-navigation.png'),fullPage:false});

 await page.goto(`/numerical-methods-atlas/problems/bratu/?lang=${lang}`);
 const bratu=active().locator('[data-problem-case-picker="bratu"]');
 for(const purpose of ['forward','sensitivity','inverse'])await expect(bratu.locator(`[data-execution-purpose="${purpose}"]`)).toBeVisible();
 await bratu.locator('[data-execution-purpose="inverse"] > summary').click();
 const inverse=bratu.locator('article[data-execution-case="bratu-gn-lm-bounds"]');
 await expect(inverse).toBeVisible();
 await expect(inverse).toHaveAttribute('data-execution-dimension','1d-bvp');
 await expect(inverse.locator('img')).toBeVisible();
 await inverse.locator('[data-execution-action="guide"]').click();
 await expect(page).toHaveURL(new RegExp(`/validation/bratu-gn-lm-bounds/.*lang=${lang}`));
 await expect(active().locator('a[href$=".zip"]').first()).toBeVisible();
 await noOverflow();

 await page.goto(`/numerical-methods-atlas/gallery/?lang=${lang}`);
 await active().locator('[data-problem-id="noh"] .gallery-image-link').click();
 await expect(page).toHaveURL(new RegExp(`/problems/noh/.*lang=${lang}`));
 const noh=active().locator('[data-problem-case-picker="noh"]');
 await expect(noh.locator('[data-execution-purpose="radial-1d"]')).toBeVisible();
 await expect(noh.locator('[data-execution-purpose="cartesian-2d"]')).toBeVisible();
 await noh.locator('[data-execution-purpose="radial-1d"] > summary').click();
 await expect(noh.locator('article[data-execution-case="noh-shock"]')).toHaveAttribute('data-execution-dimension','1d-radial');
 const cartesian=noh.locator('article[data-execution-case="noh-cartesian-2d"]');
 await expect(cartesian).toHaveAttribute('data-execution-dimension','2d-cartesian');
 const hero=active().locator('[data-problem-figure-case="noh-cartesian-2d"]');
 await expect(hero).toHaveAttribute('href',await cartesian.locator('[data-execution-action="guide"]').getAttribute('href'));
 await hero.click();
 await expect(page).toHaveURL(new RegExp(`/validation/noh-cartesian-2d/.*lang=${lang}`));
 await expect(active().locator('a[href$=".zip"]').first()).toBeVisible();
 await noOverflow();
 expect(errors).toEqual([]);
});
