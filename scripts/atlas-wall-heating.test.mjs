import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {spawnSync} from 'node:child_process';
const root=process.cwd(),read=n=>fs.readFileSync(path.join(root,n),'utf8'),load=n=>JSON.parse(read(n));
const detailed=load('catalog/atlas-detailed-reading.json'),chapter=detailed.chapters.find(c=>c.id==='wall-heating');
test('wall heating explains existing Noh diagnostics and preserves their scientific interpretation',()=>{
  assert(chapter);assert.deepEqual(chapter.scoped_supplements,['noh-shock','noh-cartesian-2d']);
  const text=JSON.stringify(chapter);
  for(const value of ['2.58%','8.16%','20.59%','13.99%','15.52%'])assert(text.includes(value),value);
  assert.match(chapter.publication_scope.en,/do not eliminate/);
  assert.match(chapter.sections.find(s=>s.id==='scope').paragraphs.en.join(' '),/no new PDE execution/i);
  const image=chapter.sections.flatMap(s=>s.figures??[]);
  assert.equal(image.length,1);
  const bytes=fs.readFileSync(path.join(root,image[0].source));
  assert.equal(createHash('sha256').update(bytes).digest('hex'),image[0].sha256);
  assert.equal(bytes.readUInt32BE(16),image[0].width);assert.equal(bytes.readUInt32BE(20),image[0].height);
  for(const lang of ['ja','en']){
    const base='numerical-methods-atlas/'+lang+'/read/wall-heating/';
    const html=read(base+'index.html'),markdown=read(base+'index.md');
    assert(html.includes('class="reading-saved-figure"'));
    assert(html.includes('src="'+image[0].source+'"'));assert(markdown.includes(']('+image[0].source+')'));
    assert(html.includes('/numerical-methods-atlas/validation/noh-shock/?lang='+lang));
    assert(html.includes('/numerical-methods-atlas/validation/noh-cartesian-2d/?lang='+lang));
    const contents=read('numerical-methods-atlas/'+lang+'/read/index.html');
    assert(contents.includes('/'+lang+'/read/wall-heating/'));
  }
});
test('saved-reading-figure validation rejects changed hashes, dimensions and escaped paths',()=>{
  const script=String.raw`
import ast,hashlib,json,re
from pathlib import Path
ROOT=Path.cwd()
source=ROOT/'scripts/build-atlas-detailed-reading.py'
tree=ast.parse(source.read_text())
node=next(n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='section_figures')
exec(compile(ast.Module(body=[node],type_ignores=[]),str(source),'exec'))
data=json.loads((ROOT/'catalog/atlas-detailed-reading.json').read_text())
chapter=next(c for c in data['chapters']if c['id']=='wall-heating')
section=next(s for s in chapter['sections']if s.get('figures'))
assert len(section_figures(section,'ja'))==1
for field,value in [('sha256','0'*64),('width',1),('source','/code/validated-examples/../bad.png')]:
    clone=json.loads(json.dumps(section));clone['figures'][0][field]=value
    try:section_figures(clone,'en')
    except AssertionError:pass
    else:raise AssertionError('corruption accepted: '+field)
print('one actual saved figure accepted; three corruptions rejected')
`;
  const result=spawnSync('python3',['-B','-c',script],{cwd:root,encoding:'utf8',timeout:10000});
  assert.equal(result.status,0,result.stderr);assert.match(result.stdout,/three corruptions rejected/);
});
