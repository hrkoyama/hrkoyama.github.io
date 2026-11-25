import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';

const root=new URL('../',import.meta.url);
const read=path=>readFileSync(new URL(path,root),'utf8');

test('the method index explains its code-reference role and links to learning in each language',()=>{
  const html=read('numerical-methods-atlas/methods/index.html');
  const copy={
    ja:{title:'手法・コードの対応表',scope:['適用条件','関連コード','検証記録','公開状況'],learning:'分野別の全章目次',reason:'理論・導出'},
    en:{title:'Methods and code reference',scope:['applicable conditions','related code','verification records','publication status'],learning:'Complete chapter index',reason:'theory and derivations'},
  };
  for(const [lang,text] of Object.entries(copy)){
    assert.ok(html.includes(`data-page-title-${lang}="${text.title} | `));
    const start=html.indexOf(`<section data-method-map data-site-language="${lang}" lang="${lang}">`);
    assert.notEqual(start,-1,`${lang}: method index exists`);
    const controls=html.indexOf('<form ',start);
    assert.ok(controls>start,`${lang}: filter follows the introduction`);
    const intro=html.slice(start,controls);
    assert.ok(intro.includes(`<h1>${text.title}</h1>`),`${lang}: title matches the entry label`);
    for(const term of text.scope)assert.ok(intro.includes(term),`${lang}: explains ${term}`);
    const related=intro.match(/<p class="method-reading-entry">([\s\S]*?)<\/p>/)?.[1];
    assert.ok(related,`${lang}: learning link is visible before filters`);
    assert.ok(related.includes(text.reason),`${lang}: explains when to read chapters`);
    assert.ok(related.includes(`<a href="/numerical-methods-atlas/${lang}/read/">${text.learning}</a>`),`${lang}: learning link uses the matching language`);
    assert.ok(related.includes(`/numerical-methods-atlas/explore/?lang=${lang}`),`${lang}: suggested reading order has its distinct guide`);
    assert.doesNotMatch(intro,/手法の見取り図|A map of numerical methods|解説章の目次|Reading chapters/);
  }
});
