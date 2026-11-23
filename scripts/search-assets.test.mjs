import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const root=fileURLToPath(new URL('../',import.meta.url));
const run=source=>execFileSync('python3',['-B','-c',source],{cwd:root,encoding:'utf8'});

test('search templates render deterministic assets, preserve editable logic and propagate dependency versions',()=>{
 assert.match(run(String.raw`
import json,shutil,sys,tempfile,hashlib
from pathlib import Path
sys.path.insert(0,'scripts')
from search_assets import build_search_assets,OUTPUTS
with tempfile.TemporaryDirectory(prefix='atlas-search-assets-') as temporary:
 root=Path(temporary)
 for name in ['frontend/search','search/goals-data.mjs','search/navigation.css','search/methods.css','search/search.css','search/index.html','search/atlas-query-index.json','search/query-index.json','numerical-methods-atlas/home-overview.js']:
  src=Path(name);dst=root/name;dst.parent.mkdir(parents=True,exist_ok=True)
  if src.is_dir():shutil.copytree(src,dst)
  else:shutil.copyfile(src,dst)
 sources={p:p.read_bytes() for p in (root/'frontend/search').iterdir()}
 first=build_search_assets(root);before={name:(root/name).read_bytes() for name in [*OUTPUTS,'search/asset-manifest.json','search/index.html']}
 assert build_search_assets(root)==first
 assert before=={name:(root/name).read_bytes() for name in before}
 assert all(p.read_bytes()==data for p,data in sources.items())
 for row in first['modules']:
  assert hashlib.sha256((root/row['output']).read_bytes()).hexdigest()==row['sha256']
  assert (root/row['output']).read_text().startswith('// Generated from '+row['source'])
  for name,sha in row['dependencies'].items():assert hashlib.sha256((root/name).read_bytes()).hexdigest()==sha
 (root/'frontend/search/compact-index.mjs').write_text((root/'frontend/search/compact-index.mjs').read_text()+'\n// changed source\n')
 second=build_search_assets(root)
 assert all((root/name).read_bytes()!=before[name] for name in OUTPUTS)
 (root/'search/engine.mjs').write_text('Generated output edited accidentally')
 assert build_search_assets(root)==second
 assert 'Generated output edited accidentally' not in (root/'search/engine.mjs').read_text()
 (root/'frontend/search/compact-index.mjs').write_text("import './engine.mjs?v={{asset:search/engine.mjs}}';")
 try:build_search_assets(root)
 except ValueError as error:assert 'Cyclic' in str(error)
 else:raise AssertionError('cyclic source dependencies accepted')
print('search sources and manifest checked')
`),/search sources and manifest checked/);
});

test('the explicit pipeline validates all dependencies before exposing unchanged ordered commands',()=>{
 assert.match(run(String.raw`
import copy,json,shutil,sys,tempfile
from pathlib import Path
sys.path.insert(0,'scripts')
from site_pipeline import commands
root=Path.cwd();rows=json.loads((root/'catalog/site-build-pipeline.json').read_text())
result=commands(root)
assert result[0][1]=='scripts/build-notebook-bibliography.py' and result[-1][1]=='scripts/check-site.py'
search=next(i for i,row in enumerate(result) if row[1]=='scripts/build-atlas-search.py')
assert result[search+1][1]=='scripts/build-atlas-purpose.py'
assert any(row[1]=='scripts/build-atlas-purpose.py' for row in result[:search])
with tempfile.TemporaryDirectory() as temporary:
 fixture=Path(temporary);(fixture/'catalog').mkdir()
 for row in rows['stages']:
  for name in [row['script'],*row.get('checks',[])]:
   p=fixture/name;p.parent.mkdir(parents=True,exist_ok=True);p.touch()
 for mutation in ['duplicate','forward','missing','escape']:
  bad=copy.deepcopy(rows)
  if mutation=='duplicate':bad['stages'][-1]['id']=bad['stages'][0]['id']
  if mutation=='forward':bad['stages'][0]['depends_on']=[bad['stages'][-1]['id']]
  if mutation=='missing':bad['stages'][0]['depends_on']=['unknown-stage']
  if mutation=='escape':bad['stages'][0]['script']='../private.py'
  (fixture/'catalog/site-build-pipeline.json').write_text(json.dumps(bad))
  try:commands(fixture)
  except ValueError:pass
  else:raise AssertionError(mutation+' accepted')
print('pipeline dependency contract checked')
`),/pipeline dependency contract checked/);
});

test('the SPA runtime keeps its logic in one template while document changes update only generated settings and asset versions',()=>{
 assert.match(run(String.raw`
import json,re,shutil,sys,tempfile
from pathlib import Path
sys.path.insert(0,'scripts')
from atlas_runtime_assets import build_atlas_runtime
from search_assets import TOKEN
with tempfile.TemporaryDirectory(prefix='atlas-runtime-assets-') as temporary:
 root=Path(temporary);source=Path('frontend/atlas/app.js');target=root/source;target.parent.mkdir(parents=True);shutil.copyfile(source,target)
 for name in set(TOKEN.findall(source.read_text()))-{'numerical-methods-atlas/atlas-runtime-data.mjs'}:
  p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('fixture asset '+name)
 p=root/'catalog/atlas-purpose.json';p.parent.mkdir();p.write_text(json.dumps({'ja':{'meta_description':'説明'},'en':{'meta_description':'Description'}}))
 for language in ['ja','en']:(root/'numerical-methods-atlas'/('content.'+language+'.json')).write_text('{}')
 before=target.read_bytes();first=build_atlas_runtime(root);output=(root/'numerical-methods-atlas/app.js').read_bytes();assert build_atlas_runtime(root)==first
 (root/'numerical-methods-atlas/content.en.json').write_text('{"new":"chapter"}')
 second=build_atlas_runtime(root);assert second!=first and (root/'numerical-methods-atlas/app.js').read_bytes()!=output
 assert target.read_bytes()==before
 assert 'atlasIntroDescriptions,atlasDocumentVersions' in (root/'numerical-methods-atlas/app.js').read_text()
print('runtime source boundary checked')
`),/runtime source boundary checked/);
});
