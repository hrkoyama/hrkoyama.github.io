import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root));
const json=p=>JSON.parse(read(p));
const sha=p=>createHash('sha256').update(read(p)).digest('hex');
const d=json('catalog/atlas-foundations-course.json');
const base=d.base.slice(1),edition=base+d.edition+'/';
const escaped=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;').replaceAll("'",'&#x27;');
test('beginner course retains the approved 19-chapter sequence and 38 answered questions',()=>{
 assert.equal(d.chapters.length,19);assert.deepEqual(d.chapters.map(c=>c.n),Array.from({length:19},(_,i)=>i+1));assert.equal(d.chapters.flatMap(c=>c.questions).length,38);
 for(const c of d.chapters){assert.ok(c.lead.length>=2);assert.ok(c.sections.length>=3);for(const q of c.questions){assert.ok(q.question&&q.answer);}}
});
test('Web chapters contain every shared paragraph, code fragment and answer',()=>{
 for(const c of d.chapters){const html=read(base+c.id+'/index.html').toString();const text=[...c.goals,...c.lead,...c.sections.flatMap(s=>s.paragraphs),...c.worked.paragraphs,c.worked.code,c.worked.result,c.figure.caption,...c.questions.flatMap(q=>[q.question,q.answer]),...c.pitfalls,...c.summary];for(const t of text)assert.ok(html.includes(escaped(t)),c.id+': '+t.slice(0,30));assert.equal((html.match(/<details>/g)||[]).length,2);}
});
test('same-content PDF receipt covers the exact manuscript and frozen figure/equation/PDF bytes',()=>{
 const receipt=json(edition+'book-verification.json');assert.equal(receipt.source_sha256,sha('catalog/atlas-foundations-course.json'));assert.equal(receipt.chapters,19);assert.equal(receipt.questions_and_answers,38);assert.ok(receipt.prose_and_code_fragments_checked>400);
 for(const [file,digest] of Object.entries(receipt.assets))assert.equal(sha(edition+file),digest,file);
});
test('code ZIP and its reviewed source stay frozen together',()=>{
 const r=json('code/numerical-foundations/2026-11-24/release.json');assert.equal(sha(r.zip.slice(1)),r.zip_sha256);assert.equal(r.unit_tests,25);assert.equal(r.comparison_tests,2);assert.equal(r.acceptance_checks,34);for(const [p,s]of Object.entries(r.source_files))assert.equal(sha(p),s,p);
});
test('Japanese and English directories link the matching course without changing chapter registry',()=>{
 const catalog=json('catalog/atlas-reading-index.json');for(const lang of ['ja','en']){const page=read('numerical-methods-atlas/'+lang+'/read/index.html').toString();assert.ok(page.includes(d.base+(lang==='en'?'en/':'')));const index=json('numerical-methods-atlas/'+lang+'/read/index.json');assert.equal(index.chapter_count,catalog.groups.flatMap(g=>g.chapters).length);assert.equal(index.learning_packages[0].language,lang);assert.equal(index.learning_packages[0].url,d.base+(lang==='en'?'en/':''));}
});
