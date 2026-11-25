import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root));
const json=p=>JSON.parse(read(p));
const sha=p=>createHash('sha256').update(read(p)).digest('hex');
const en=json('catalog/atlas-foundations-course.en.json'),ja=json('catalog/atlas-foundations-course.json');
const escaped=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;').replaceAll("'",'&#x27;');
test('English translation retains Japanese scientific equations, code, sequence, and answered-question structure',()=>{
 assert.equal(en.translation.source_sha256,sha('catalog/atlas-foundations-course.json'));
 assert.equal(en.chapters.length,19);assert.equal(en.chapters.flatMap(c=>c.questions).length,38);
 for(let i=0;i<19;i++){
  const a=ja.chapters[i],b=en.chapters[i];
  for(const key of ['id','n','part','readings'])assert.deepEqual(b[key],a[key]);
  assert.deepEqual(b.sections.map(s=>s.equations.map(e=>e.tex)),a.sections.map(s=>s.equations.map(e=>e.tex)));
  assert.equal(b.figure.id,a.figure.id);assert.equal(b.experiment.data,a.experiment.data);
 }
 const output=execFileSync(process.env.PYTHON||'python3',['-c',"import sys;sys.path.insert(0,'scripts');from foundations_en_contract import load;load();print('translation contract passed')"],{cwd:root,encoding:'utf8'});
 assert.match(output,/translation contract passed/);
});
test('English Web chapters include every translated explanation, caption, example, and answer',()=>{
 for(const c of en.chapters){
  const html=read(en.base.slice(1)+c.id+'/index.html').toString();
  const expected=[c.title,...c.goals,...c.lead,...c.sections.flatMap(s=>[s.title,...s.paragraphs]),...c.worked.paragraphs,c.worked.code,c.worked.result,c.figure.caption,c.experiment.instructions,...c.questions.flatMap(q=>[q.question,q.answer]),...c.pitfalls,...c.summary];
  for(const text of expected)assert.ok(html.includes(escaped(text)),c.id+': '+text.slice(0,40));
  assert.equal((html.match(/<details>/g)||[]).length,2);
  assert.ok(html.includes('data-content-language="en"'));
 }
 const index=read(en.base.slice(1)+'index.html').toString();for(const paragraph of en.lab_guide)assert.ok(index.includes(escaped(paragraph)));
});
test('English PDF receipt binds every shared text fragment and all frozen shared scientific assets',()=>{
 const receipt=json(en.base.slice(1)+en.edition+'/book-verification.json');
 assert.equal(receipt.source_sha256,sha('catalog/atlas-foundations-course.en.json'));
 assert.equal(receipt.chapters,19);assert.equal(receipt.questions_and_answers,38);assert.equal(receipt.prose_and_code_fragments_checked,605);
 assert.equal(receipt.figures,19);assert.equal(receipt.equations,36);
 for(const [file,digest] of Object.entries(receipt.assets))assert.equal(sha(file),digest,file);
 const jaReceipt=json(ja.base.slice(1)+ja.edition+'/book-verification.json');
 for(const [file,digest] of Object.entries(jaReceipt.assets))assert.equal(sha(ja.base.slice(1)+ja.edition+'/'+file),digest,file);
});
test('language links preserve every chapter and select the matching PDF edition',()=>{
 for(const suffix of ['',...en.chapters.map(c=>c.id+'/')]){
  for(const [language,d,other] of [['ja',ja,en],['en',en,ja]]){
   const page=read(d.base.slice(1)+suffix+'index.html').toString();
   assert.ok(page.includes('hreflang="'+other.language+'" href="https://hrkoyama.github.io'+other.base+suffix+'"'));
   assert.ok(page.includes('data-content-language="'+language+'"'));
   assert.ok(page.includes('numerical-foundations-'+language+'.pdf'));
  }
 }
});
test('both search languages reach the same course resources in their own language',()=>{
 const entries=json('numerical-methods-atlas/home-search-index.json').entries;
 for(const [id,suffix] of [['foundations-course',''],...en.chapters.map(c=>['foundations-course-'+c.id,c.id+'/'])]){
  const entry=entries.find(x=>x.id===id);assert.ok(entry,id);
  assert.equal(entry.routes.ja,ja.base+suffix);assert.equal(entry.routes.en,en.base+suffix);
  assert.ok(entry.text.en.length>100);assert.ok(entry.text.ja.length>100);
 }
});

test('separate verified book edition preserves old PDFs and selects A4 Japanese and US Letter English primary downloads',()=>{
 const registry=JSON.parse(execFileSync(process.env.PYTHON||'python3',['-B','-c',"import json,sys;sys.path.insert(0,'scripts');from foundations_books import current_books;from pathlib import Path;print(json.dumps(current_books(Path('.'))))"],{cwd:root,encoding:'utf8',timeout:10000}));
 assert.equal(registry.state,'FROZEN_VERIFIED');
 for(const language of ['ja','en']){
  const row=registry.primary[language],page=read(row.web.slice(1)+'index.html').toString();
  const downloads=page.match(/<div class="downloads">([\s\S]*?)<\/div>/);assert.ok(downloads);
  assert.ok(downloads[1].startsWith('<a href="/'+row.pdf.path+'">'));
  assert.ok(downloads[1].includes('href="/'+row.previous_pdf.path+'"'));
  assert.equal(sha(row.pdf.path),row.pdf.sha256);assert.equal(sha(row.previous_pdf.path),row.previous_pdf.sha256);
  assert.equal(json('catalog/atlas-home.json').landing[language].beginner.pdf.href,'/'+row.pdf.path);
  assert.equal(row.paper.name,language==='ja'?'A4':'USLetter');
 }
});
