import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';

const root=new URL('../',import.meta.url);
const read=path=>readFileSync(new URL(path,root),'utf8');
const json=path=>JSON.parse(read(path));
const comparison=json('catalog/atlas-thermostat-comparison.json');
const expected=['csvr-kinetic-kernel','csvr-langevin-harmonic','csvr-langevin-quartic'];
const origin='https://hrkoyama.github.io';

test('adopted CSVR formulas render offline and identify the signed original update and author correction',()=>{
 assert.deepEqual(comparison.case_ids,expected);
 const records=Object.entries(comparison.formulas).map(([id,formula])=>({id,formula:[formula]}));
 const rendered=JSON.parse(execFileSync('node',['scripts/render-atlas-math.cjs'],{cwd:root,input:JSON.stringify(records),encoding:'utf8'}));
 assert.equal(Object.keys(rendered.rendered).length,8);
 for(const [id,html] of Object.entries(rendered.rendered))assert.match(html[0],/class="katex"/,id);
 assert.match(comparison.formulas['csvr-sign'],/operatorname\{sign\}/);
 assert.match(comparison.formulas['csvr-matched'],/2\\gamma/);
 assert.equal(comparison.references.find(x=>x.id==='bussi2008localglobal').doi,'10.1016/j.cpc.2008.01.006');
 assert.ok(comparison.references.some(x=>x.id==='bussi-csvr-author-algorithms'));
 for(const source of comparison.references)for(const lang of ['ja','en'])assert.ok(source.review_note[lang]);
});

for(const lang of ['ja','en'])test(`published ${lang} reading keeps equations, review limits and immutable evidence synchronized`,()=>{
 const base=`numerical-methods-atlas/${lang}/read/thermostats/`;
 const page=read(base+'index.html'),markdown=read(base+'index.md'),data=json(base+'index.json');
 assert.equal(data.comparison_enabled,true);
 const other=lang==='ja'?'en':'ja';
 assert.ok(page.includes(`href="/numerical-methods-atlas/${other}/read/thermostats/?lang=${other}" hreflang="${other}"`),'body language switch retains its target language through shared navigation');
 assert.deepEqual(data.case_ids,['langevin-harmonic',...expected]);
 assert.deepEqual(new Set(data.implemented_method_ids),new Set(['langevin-thermostat','stochastic-velocity-rescaling']));
 assert.equal(data.planned_method_ids.length,10);
 assert.deepEqual(data.comparison,comparison);
 for(const id of Object.keys(comparison.formulas))assert.ok(page.includes(`data-equation-id="${id}"`));
 for(const section of comparison.sections){
  assert.ok(page.includes(`id="${section.id}"`));
  for(const paragraph of section.paragraphs[lang])assert.ok(markdown.includes(paragraph));
 }
 assert.ok(markdown.includes(comparison.verification[lang]));
 assert.ok(markdown.includes(comparison.source_scope[lang]));
 assert.match(page,/Kolmogorov/);
 assert.match(page,/BAOAB/);assert.match(page,/OBABO/);
 assert.match(page,lang==='ja'?/独立レプリカ/:/independent replicas/);
 for(const anchor of ['temperature','fluctuations','dynamics','executed-scope','basic','advanced','verification','source-scope'])assert.ok(page.includes(`id="${anchor}"`));
 for(const item of data.supplements){
  for(const key of ['url','download','results','verification']){
   assert.ok(item[key].startsWith('/'),`${item.id} ${key}`);
   assert.ok(page.includes(item[key]));
   assert.ok(markdown.includes(origin+item[key]));
  }
 }
 for(const [path,expectedHash] of Object.entries(data.source_sha256)){
  const actual=createHash('sha256').update(readFileSync(new URL(path,root))).digest('hex');
  assert.equal(actual,expectedHash,path);
 }
 assert.ok(!page.includes('他の11手法'));
 assert.ok(!page.includes('other 11 methods'));
 assert.ok(!page.includes('Full equation audits and numerical reproductions have not been performed.'));
});
