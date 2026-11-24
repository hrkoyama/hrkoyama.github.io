// Course UI only; PDF extraction and numerical reproduction have separate CI.
import {test,expect} from '@playwright/test';
import {readFileSync} from 'node:fs';
import {writeFile} from 'node:fs/promises';
const en=JSON.parse(readFileSync(new URL('../catalog/atlas-foundations-course.en.json',import.meta.url)));
const ja=JSON.parse(readFileSync(new URL('../catalog/atlas-foundations-course.json',import.meta.url)));

test('all English foundations chapters, figures, answers, and chapter-preserving language links',async({page},info)=>{
 const failures=[],errors=[],chapters=[];
 page.on('pageerror',error=>errors.push(error.message));
 page.on('response',response=>{
  if(response.status()>=400&&['document','script','stylesheet','image','font'].includes(response.request().resourceType()))failures.push(response.status()+' '+response.url());
 });
 for(const chapter of en.chapters){
  await page.goto(en.base+chapter.id+'/?lang=en');
  await expect(page.getByRole('heading',{level:1})).toHaveText(chapter.title);
  await expect(page.locator('main details')).toHaveCount(2);
  await page.locator('main figure img').scrollIntoViewIfNeeded();
  await expect.poll(()=>page.locator('main img').evaluateAll(images=>images.every(image=>image.complete&&image.naturalWidth>0))).toBe(true);
  const size=await page.evaluate(()=>({viewport:document.documentElement.clientWidth,page:document.documentElement.scrollWidth}));
  expect(size.page-size.viewport).toBeLessThanOrEqual(1);
  chapters.push({id:chapter.id,...size,images_loaded:true});
  if(chapter.id==='18'){
   await page.locator('main details summary').first().click();
   await expect(page.locator('main details[open]')).toHaveCount(1);
   await expect(page.locator('main details[open]')).toContainText(chapter.questions[0].answer);
   await page.screenshot({path:info.outputPath('foundations-en-answer.png')});
   await page.locator('.site-languages [data-site-lang="ja"]').click();
   await expect(page).toHaveURL(new RegExp('/learn/numerical-foundations/18/[?]lang=ja'));
   await expect(page.getByRole('heading',{level:1})).toHaveText(ja.chapters[17].title);
   await page.locator('.site-languages [data-site-lang="en"]').click();
   await expect(page).toHaveURL(new RegExp('/learn/numerical-foundations/en/18/[?]lang=en'));
   await expect(page.getByRole('heading',{level:1})).toHaveText(chapter.title);
  }
 }
 await page.goto('/numerical-methods-atlas/en/read/?lang=en');
 const courseLink=page.locator('a[href*="'+en.base+'"]').first();
 await expect(courseLink).toBeVisible();
 const courseDestination=new URL(await courseLink.getAttribute('href'),page.url());
 expect(courseDestination.pathname).toBe(en.base);expect(courseDestination.searchParams.get('lang')).toBe('en');
 const pdf=await page.request.head(en.base+en.edition+'/numerical-foundations-en.pdf');
 expect(pdf.ok()).toBe(true);expect(pdf.headers()['content-type']).toContain('application/pdf');
 await page.goto(en.base+'?lang=en');
 await expect(page.getByRole('heading',{level:1})).toHaveText(en.title);
 await page.screenshot({path:info.outputPath('foundations-en-index.png')});
 expect(failures).toEqual([]);expect(errors).toEqual([]);
 await writeFile(info.outputPath('foundations-en-checks.json'),JSON.stringify({passed:true,chapters,language_links_preserve_chapter:true,answer_toggle:true,pdf_head:true,source_commit:process.env.GITHUB_SHA||null},null,2));
});
