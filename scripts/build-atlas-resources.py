#!/usr/bin/env python3
"""Generate stable, bilingual human and machine routes from one method catalog."""
from pathlib import Path
import hashlib
import html
import json
import re
import xml.etree.ElementTree as ET
from atlas_sensitivity_release import sensitivity_release_record
from atlas_inverse_release import inverse_release_record
from atlas_fdtd_release import fdtd_release_record
from atlas_multinverse_release import multinverse_release_record
from atlas_depth_release import depth_release_record
from atlas_method_review import (validate_method_reviews, review_intro, field_note,
                                 verification_html, references_html, review_markdown)

ROOT=Path(__file__).resolve().parents[1]
ATLAS=ROOT/'numerical-methods-atlas'
ORIGIN='https://hrkoyama.github.io'
DATA=json.loads((ROOT/'catalog/atlas-methods.json').read_text())
METHODS=DATA['methods']
REVIEWED=validate_method_reviews(DATA)
EXECUTION_RECORDS=json.loads((ROOT/'catalog/atlas-execution-examples.json').read_text())['examples']
EXECUTION_REGISTRY=ORIGIN+'/numerical-methods-atlas/code-and-data/examples.json'
def execution_links(method_id):
    return [{'id':e['id'],'registry_url':EXECUTION_REGISTRY,'guide':{lang:ORIGIN+'/numerical-methods-atlas/code-and-data/?lang='+lang+'#'+e['id']+'-'+lang for lang in ['ja','en']}} for e in EXECUTION_RECORDS if method_id in e['method_ids']]
# Remove obsolete generated records when the editorial catalog excludes a topic.
active_ids={x['id'] for x in METHODS}
for directory in (ATLAS/'methods').glob('*'):
    if directory.is_dir() and directory.name not in active_ids:
        assert {p.name for p in directory.iterdir()} <= {'index.html','index.json','index.md'},directory
        for p in directory.iterdir():p.unlink()
        directory.rmdir()
existing_count=sum(x['status']!='planned' for x in METHODS)
example_count=sum(x['status']=='educational-example' for x in METHODS)
reading_count=sum(x['status']=='reading-only' for x in METHODS)
planned_count=sum(x['status']=='planned' for x in METHODS)
CODE=DATA['code_base']
EDITION=DATA['code_edition']
release=ROOT/CODE.lstrip('/')
verification=json.loads((release/'verification.json').read_text())
archive='atlas-code-'+EDITION+'.zip'
archive_hash=hashlib.sha256((release/archive).read_bytes()).hexdigest()
assert archive_hash==verification['archive_sha256']
manifest=json.loads((release/'source-manifest.json').read_text())
module_count=sum(name.startswith('numart/') and name.endswith('.py') for name in manifest['files'])
test_count=sum(name.startswith('tests/test_') and name.endswith('.py') for name in manifest['files'])
archive_mb=f'{(release/archive).stat().st_size/1_000_000:.1f}'
assert verification['failures']==verification['errors']==0
for name,digest in manifest['files'].items():
    assert hashlib.sha256((release/name).read_bytes()).hexdigest()==digest,name
ATOMS=json.loads((ROOT/'catalog/atlas-quantum-examples.json').read_text())
ACODE=ATOMS['code_base']
ABASE=ROOT/ACODE.lstrip('/')
AVER=json.loads((ABASE/'verification.json').read_text())
AHASH=hashlib.sha256((ABASE/ATOMS['archive']).read_bytes()).hexdigest()
assert AHASH==AVER['archive_sha256'] and AVER['failures']==AVER['errors']==0
ACASES={x['id']:x for x in ATOMS['cases']}
esc=html.escape
STATUS={'educational-example':{'ja':'教育用例・関連コードあり','en':'Educational example / related code'},'reading-only':{'ja':'解説あり・専用実装なし','en':'Reading only / no dedicated implementation'},'planned':{'ja':'Under construction / 収録予定','en':'Under construction / planned'}}
def status(x,lang):
    if x['status']=='planned' and x['reading']:
        return '解説あり・実装予定' if lang=='ja' else 'Reading / implementation planned'
    return STATUS[x['status']][lang]
def link(url,label):return '<a href="'+esc(url)+'">'+esc(label)+'</a>'
def page(title_ja,title_en,url,sections,structured=None,extra_head=''):
    metadata='' if structured is None else '<script type="application/ld+json">'+json.dumps(structured,ensure_ascii=False).replace('<','\\u003c')+'</script>'
    return f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title data-page-title-ja="{esc(title_ja)} | 数値計算法アトラス" data-page-title-en="{esc(title_en)} | Numerical Methods Atlas">{esc(title_ja)} | 数値計算法アトラス</title>
<meta name="description" content="{esc(title_ja)}：位置付け、解説、コード、検証、一次文献と実装状況。"><link rel="canonical" href="{ORIGIN+url}">
<link rel="stylesheet" href="/styles/atlas-resources.css?v={hashlib.sha256((ROOT/'styles/atlas-resources.css').read_bytes()).hexdigest()[:12]}">{metadata}{extra_head}</head>
<body class="profile-page"><main class="profile-main atlas-resource-main" id="main">{sections}</main></body></html>'''
def write(path,text):
    p=ROOT/path.lstrip('/');p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
def nav(lang):
    labels=['手法の見取り図','コード・入力・検証','解説章の目次'] if lang=='ja' else ['Method map','Code, inputs and checks','Reading chapters']
    return '<nav class="resource-nav" aria-label="Atlas resources">'+''.join(link(u,l) for u,l in zip(['/numerical-methods-atlas/methods/','/numerical-methods-atlas/code-and-data/',f'/numerical-methods-atlas/{lang}/read/'],labels))+'</nav>'
AUTODIFF_RELEASES={}
def autodiff_release_record(x):
    """Resolve a separately verified supplement without changing the code edition."""
    config=x['autodiff_release']
    assert x['id']=='automatic-differentiation' and x['status']=='educational-example'
    assert not x['code_modules'] and not x['test_files']
    key=json.dumps(config,sort_keys=True)
    if key in AUTODIFF_RELEASES:return AUTODIFF_RELEASES[key]
    base=config['base']
    assert base.startswith('/code/autodiff/') and base.endswith('/') and '..' not in base
    directory=ROOT/base.lstrip('/')
    def file(name):
        path=Path(name)
        assert not path.is_absolute() and '..' not in path.parts and name
        target=directory/path
        assert target.resolve().is_relative_to(directory.resolve())
        return target
    source=json.loads(file(config['manifest']).read_text())
    receipt=json.loads(file(config['verification']).read_text())
    assert source['version']==config['edition'] and source['public_base_url']==ORIGIN+base
    assert source['family']=='autodiff'
    required={'numart/autodiff.py','numart/krylov.py','scripts/build_autodiff.py',
              'tests/test_autodiff.py','README.md','requirements.txt','LICENSE','LICENSING.md',config['evidence']}
    assert required<=source['files'].keys()
    for name,digest in source['files'].items():
        assert hashlib.sha256(file(name).read_bytes()).hexdigest()==digest,name
    archive=receipt['archive']
    assert archive['file']==config['archive']
    archive_bytes=file(config['archive']).read_bytes()
    assert len(archive_bytes)==archive['bytes']
    assert hashlib.sha256(archive_bytes).hexdigest()==archive['sha256']
    assert receipt['returncode']==0 and receipt['passed_tests']==8
    assert receipt['failures']==receipt['errors']==0
    assert receipt['archive_sha256']==archive['sha256']
    assert receipt['source_manifest_sha256']==hashlib.sha256(file(config['manifest']).read_bytes()).hexdigest()
    record=dict(code_base=ORIGIN+base,code_edition=config['edition'],
        code_urls=[ORIGIN+base+name for name in ['numart/autodiff.py','numart/krylov.py','scripts/build_autodiff.py']],
        test_urls=[ORIGIN+base+'tests/test_autodiff.py'],
        run_commands=['python -m pytest -q tests/test_autodiff.py','python scripts/build_autodiff.py'],
        run_from='Extracted autodiff supplement directory',
        code_download=ORIGIN+base+config['archive'],code_manifest=ORIGIN+base+config['manifest'],
        code_verification=ORIGIN+base+config['verification'],code_archive_sha256=archive['sha256'],
        results=ORIGIN+base+config['evidence'],passed_tests=receipt['passed_tests'])
    AUTODIFF_RELEASES[key]=record
    return record

def public_record(x):
    url=ORIGIN+'/numerical-methods-atlas/methods/'+x['id']+'/'
    record={**x,'url':url,'json_url':url+'index.json','markdown_url':url+'index.md',
            'reading':{lang:ORIGIN+path for lang,path in x['reading'].items()},
            'code_urls':[ORIGIN+CODE+'numart/'+name+'.py' for name in x['code_modules']],
            'test_urls':[ORIGIN+CODE+'tests/'+name+'.py' for name in x['test_files']],
            'run_commands':['python -m pytest -q '+' '.join('tests/'+name+'.py' for name in x['test_files'])] if x['test_files'] else [],
            'run_from':'Extracted code edition directory' if x['code_modules'] else None,
            'code_base':ORIGIN+CODE,'code_edition':EDITION if x['code_modules'] else None}
    if x.get('quantum_examples'):
        record.update(code_urls=[ORIGIN+ACODE+f for f in ['atomic_radial.py','run.py']],test_urls=[ORIGIN+ACODE+'test_atomic_radial.py'],run_commands=[ATOMS['test_command'],ATOMS['run_command']],run_from='Extracted quantum-atoms edition directory',code_base=ORIGIN+ACODE,code_edition=ATOMS['edition'],code_verification=ORIGIN+ACODE+'verification.json',code_download=ORIGIN+ACODE+ATOMS['archive'],inputs=ORIGIN+ACODE+'inputs.json',results=ORIGIN+ACODE+'results/results.json',independent_reference=ORIGIN+ACODE+'reference-pyscf.json',code_examples=[{**ACASES[i],'reading':{l:ORIGIN+f'/numerical-methods-atlas/{l}/read/quantum-atoms/#{ACASES[i]["section"]}' for l in ['ja','en']}} for i in x['quantum_examples']])
    if x.get('model_examples'):
        cases=[e for e in EXECUTION_RECORDS if e['id'] in x['model_examples']]
        assert {e['id'] for e in cases}==set(x['model_examples']) and x['status']=='educational-example'
        base=cases[0]['release']['manifest'].rsplit('/',1)[0]+'/'
        assert all(e['release']==cases[0]['release'] and x['id'] in e['method_ids'] for e in cases)
        record.update(code_urls=[base+'models.py',base+'run.py'],test_urls=[base+'test_models.py'],
                      code_base=base,code_edition=cases[0]['release']['version'],code_download=cases[0]['release']['download'],
                      code_verification=cases[0]['release']['verification'],run_commands=[e['commands']['run'] for e in cases],
                      run_from='Extracted model-benchmarks edition directory')
    if x.get('molecular_examples'):
        cases=[e for e in EXECUTION_RECORDS if e['id'] in x['molecular_examples']]
        assert {e['id'] for e in cases}==set(x['molecular_examples']) and x['status']=='educational-example'
        assert all(e['release']['family']=='molecular-hf' and x['id'] in e['method_ids'] for e in cases)
        molecular_base=cases[0]['release']['manifest'].rsplit('/',1)[0]+'/'
        record['code_urls'] += [molecular_base+'molecular_hf.py',molecular_base+'run.py']
        record['test_urls'] += [molecular_base+'test_molecular_hf.py']
        record['molecular_release']={'release':cases[0]['release'],'code_base':molecular_base,
            'examples':x['molecular_examples'],'run_commands':[e['commands']['run'] for e in cases],
            'scope':x['molecular_scope']}
        if not x.get('quantum_examples'):
            record.update(code_base=molecular_base,code_edition=cases[0]['release']['version'],
                          code_download=cases[0]['release']['download'],code_verification=cases[0]['release']['verification'],
                          inputs=molecular_base+'inputs.json',results=molecular_base+'results/result.json',
                          independent_reference=molecular_base+'reference-pyscf.json',
                          run_commands=[e['commands']['run'] for e in cases],run_from='Extracted molecular-hf edition directory')
    if x.get('periodic_examples'):
        cases=[e for e in EXECUTION_RECORDS if e['id'] in x['periodic_examples']]
        assert {e['id'] for e in cases}==set(x['periodic_examples']) and x['status']=='educational-example'
        assert all(e['release']['family']=='periodic-dft' and x['id'] in e['method_ids'] for e in cases)
        base=cases[0]['release']['manifest'].rsplit('/',1)[0]+'/'
        record['code_urls'] += [base+'periodic_dft.py',base+'run.py']
        record['test_urls'] += [base+'test_periodic_dft.py']
        record['periodic_release']={'release':cases[0]['release'],'code_base':base,'examples':x['periodic_examples'],
            'run_commands':[e['commands']['run'] for e in cases],'scope':x['periodic_scope'],
            'implementation':'Original educational workflow using PySCF; independent reference uses DFTK.'}
        if not x.get('quantum_examples') and not x.get('molecular_examples'):
            record.update(code_base=base,code_edition=cases[0]['release']['version'],
                          code_download=cases[0]['release']['download'],code_verification=cases[0]['release']['verification'],
                          inputs=base+'inputs.json',results=base+'results/result.json',independent_reference=base+'reference-dftk.json',
                          run_commands=[e['commands']['run'] for e in cases],run_from='Extracted periodic-dft edition directory')
    if x.get('autodiff_release'):record.update(autodiff_release_record(x))
    if x.get('force_examples'):
        cases=[e for e in EXECUTION_RECORDS if e['id'] in x['force_examples']]
        assert {e['id'] for e in cases}==set(x['force_examples']) and x['status']=='educational-example'
        assert all(e['release']['family']=='periodic-forces' and x['id'] in e['method_ids'] for e in cases)
        force_base=cases[0]['release']['manifest'].rsplit('/',1)[0]+'/'
        record['code_urls'] += [force_base+'periodic_forces.py',force_base+'bomd.py',force_base+'run.py']
        record['test_urls'] += [force_base+'test_periodic_forces.py']
        record['force_release']={'release':cases[0]['release'],'code_base':force_base,'examples':x['force_examples'],
            'run_commands':[e['commands']['run'] for e in cases],'scope':x['force_scope'],
            'implementation':'Original PySCF force-validation workflow with independent DFTK reference; BOMD adapter is locally checked, not a validated production trajectory.'}
    if x.get('sensitivity_release'):record.update(sensitivity_release_record(ROOT,x))
    if x.get('inverse_release'):record.update(inverse_release_record(ROOT,x))
    if x.get('fdtd_release'):record.update(fdtd_release_record(ROOT,x))
    if x.get('multi_inverse_release'):
        record['scalar_inverse_release']=inverse_release_record(ROOT,x)
        record.update(multinverse_release_record(ROOT,x))
    record['execution_examples']=execution_links(x['id'])
    if x.get('depth_release'):
        supplement=depth_release_record(ROOT,x)
        record['depth_release']=supplement
        had_code=bool(record['code_urls'])
        record['code_urls']=list(dict.fromkeys(record['code_urls']+supplement['code_urls']))
        record['test_urls']=list(dict.fromkeys(record['test_urls']+supplement['test_urls']))
        if not had_code:
            for key in ['code_base','code_edition','code_download','code_manifest','code_verification','code_archive_sha256','results','run_commands','run_from']:
                record[key]=supplement[key]
        record['code_mapping_scope']='Scoped fixed-input examples; original method variants and earlier releases remain distinct.'
        record['execution_examples'] += [{'id':e['id'],'registry_url':ORIGIN+'/numerical-methods-atlas/validation/releases.json',
            'guide':{lang:e['entry']+'?lang='+lang for lang in ['ja','en']},'kind':'dedicated-supplement'} for e in supplement['examples']]
    return record


def method_search_text(x):
    # The filter describes the method record, not every paper linked by its chapter.
    values=[x['id'],*x['name'].values(),*x.get('aliases',[]),x['group']['ja'],x['group']['en'],
            *x['summary'].values(),x['status'],*STATUS[x['status']].values(),status(x,'ja'),status(x,'en')]
    return ' '.join(values)

def method_filter_controls(lang):
    ja=lang=='ja'
    labels={
        'all':('すべて','All'),
        'educational-example':('教育用例・関連コードあり','Educational examples / related code'),
        'reading-only':('解説のみ・専用実装なし','Reading only / no dedicated implementation'),
        'planned':('実装予定（解説ありを含む）','Implementation planned (including published reading)'),
    }
    counts={'all':len(METHODS),'educational-example':example_count,'reading-only':reading_count,'planned':planned_count}
    body='<form class="method-map-controls" data-method-controls hidden role="search" aria-label="'+('手法を絞り込む' if ja else 'Filter methods')+'">'
    body+='<div class="method-filter-fields"><div><label for="method-query-'+lang+'">'+('キーワード（日英対応）' if ja else 'Keywords (English / Japanese)')+'</label><input data-method-query id="method-query-'+lang+'" type="search" maxlength="200" autocomplete="off" aria-describedby="method-filter-hint-'+lang+'" placeholder="'+('例：共役勾配、Poisson、ノセフーバー' if ja else 'e.g. CG, Poisson, Nose Hoover')+'"></div>'
    body+='<div><label for="method-status-'+lang+'">'+('状態' if ja else 'Status')+'</label><select data-method-status id="method-status-'+lang+'">'
    body+=''.join('<option value="'+key+'">'+esc(labels[key][0 if ja else 1])+' ('+str(counts[key])+')</option>' for key in labels)+'</select></div>'
    body+='<button type="button" data-method-reset>'+('絞り込みを解除' if ja else 'Clear filters')+'</button></div>'
    body+='<p id="method-filter-hint-'+lang+'" class="method-filter-hint">'+('日英の名称・別名・分野・説明を検索します。複数語はすべて含む項目を表示します。' if ja else 'Search names, aliases, domains and summaries in either language. Every word must match.')+'</p>'
    body+='<p class="method-filter-hint">'+('条件はこのタブ内で保持し、言語を切り替えても引き継ぎます。検索語はブラウザ内で処理します。' if ja else 'Filters stay in this tab across language changes. Search terms are processed in your browser.')+'</p>'
    body+='<p class="method-filter-count" data-method-count role="status" aria-live="polite" aria-atomic="true">'+(str(len(METHODS))+' / '+str(len(METHODS))+'項目を表示' if ja else 'Showing '+str(len(METHODS))+' of '+str(len(METHODS))+' entries')+'</p></form>'
    body+='<noscript><p>'+('この環境では全件を表示しています。ブラウザのページ内検索でも手法名を探せます。' if ja else 'All entries are shown here. You can also use your browser’s Find in page to locate a method.')+'</p></noscript>'
    return body

sections=[]
for lang in ['ja','en']:
    ja=lang=='ja'
    intro=(f'全{len(METHODS)}項目から、状態と日英のキーワードで手法を探せます。教育用例・解説のみ・収録予定を区別して表示します。' if ja else f'Find methods among {len(METHODS)} entries by status and keywords in English or Japanese. Educational examples, reading-only entries and planned coverage remain distinct.')
    body='<section data-method-map data-site-language="'+lang+'" lang="'+lang+'"><p class="eyebrow">NUMERICAL METHODS / OPEN RESEARCH RESOURCES</p><h1>'+('手法の見取り図' if ja else 'A map of numerical methods')+'</h1><p class="intro resource-lead">'+intro+'</p>'+nav(lang)
    body+=method_filter_controls(lang)
    body+='<details class="method-map-about"><summary>'+('一覧の範囲・状態の説明' if ja else 'Scope and status definitions')+'</summary>'
    body+='<p class="resource-summary">'+(f'既存{existing_count}項目のうち教育用例{example_count}・解説のみ{reading_count}、拡張候補{planned_count}。教育用例は完成した汎用ソルバーの数ではありません。公開コード配布版の既存検査は{verification["passed"]}件通過・{verification["skipped"]}件対象外です。' if ja else f'{existing_count} existing entries: {example_count} with scoped educational examples and {reading_count} reading-only. Another {planned_count} are development candidates. These are not counts of complete production solvers. The code edition passes {verification["passed"]} existing checks, with {verification["skipped"]} inapplicable cases skipped.')+'</p>'
    body+='<p>'+('幅広い数値計算を結ぶ拡張中の地図です。未収録の分野もあり、すべての手法や原論文を網羅するという意味ではありません。' if ja else 'An expanding cross-field map, with gaps still to fill; not a claim to exhaust every method or original paper.')+'</p>'
    body+='<p><strong>'+esc(DATA['editorial_policy']['title'][lang])+':</strong> '+esc(DATA['editorial_policy']['statement'][lang])+'</p>'
    body+='<p>'+link('index.json','手法台帳 / JSON' if ja else 'Method registry / JSON')+' · '+link('/catalog/atlas-methods.json','正本データ' if ja else 'Catalog source')+' · '+link('/using/','使い方と引用' if ja else 'Use and citation')+'</p>'
    body+='</details>'
    if REVIEWED:
        body+='<details class="reviewed-methods" id="reviewed-'+lang+'"><summary>'+('主要24手法：条件・制約・一次文献を個別整理' if ja else '24 priority methods: curated conditions, limits and primary sources')+'</summary><p>'+('解く問題、採用形、使える条件・避ける条件、単位と境界、既存の確認範囲を同じ順で読めます。文献を整理した状態と、専用コードが実装・検証された状態は別です。' if ja else 'Read the problem, adopted formulation, suitable and unsuitable conditions, units, boundaries and existing checks in a common order. Source curation and a numerically verified dedicated implementation are separate states.')+'</p><p>'+link('reviewed.json','主要24手法 / JSON' if ja else '24 reviewed records / JSON')+'</p><ul class="reviewed-links">'+''.join('<li>'+link(x['id']+'/?lang='+lang,x['name'][lang])+'</li>' for x in REVIEWED)+'</ul></details>'
    body+='<nav class="resource-nav method-group-nav" aria-label="'+('手法の分野' if ja else 'Method groups')+'">'+''.join('<a data-method-group-link="'+g['id']+'" href="#'+g['id']+'-'+lang+'">'+esc(g[lang])+'</a>' for g in DATA['groups'])+'</nav>'
    body+='<p class="method-filter-empty" data-method-empty hidden>'+('該当する手法がありません。キーワードや状態を変えるか、絞り込みを解除してください。' if ja else 'No methods match. Change the keywords or status, or clear the filters.')+'</p>'
    for group in DATA['groups']:
        rows=[x for x in METHODS if x['group']['id']==group['id']]
        if not rows:continue
        body+='<section data-method-group="'+group['id']+'" id="'+group['id']+'-'+lang+'"><h2>'+esc(group[lang])+' — <span data-method-group-count>'+str(len(rows))+'</span></h2><ul class="method-list">'
        for x in rows:
            badge=('<span class="method-curated">'+('条件・文献を個別整理' if ja else 'Conditions and sources curated')+'</span>') if x.get('method_review') else ''
            body+='<li data-method-id="'+x['id']+'" data-status="'+x['status']+'" data-search="'+esc(method_search_text(x),quote=True)+'">'+link(x['id']+'/',x['name'][lang])+'<br><span class="resource-status">'+status(x,lang)+'</span>'+badge+'<p>'+esc(x['summary'][lang])+'</p></li>'
        body+='</ul></section>'
    body+='</section>';sections.append(body)
map_head='<link rel="stylesheet" href="/styles/atlas-methods.css?v='+hashlib.sha256((ROOT/'styles/atlas-methods.css').read_bytes()).hexdigest()[:12]+'"><script type="module" src="/atlas-methods.mjs?v='+hashlib.sha256((ROOT/'atlas-methods.mjs').read_bytes()).hexdigest()[:12]+'"></script>'
map_page=page('手法の見取り図','A map of numerical methods','/numerical-methods-atlas/methods/',''.join(sections),extra_head=map_head)
map_page=map_page.replace('<body class="profile-page">','<body class="profile-page" data-site-language-anchors="suffix">',1)
write('/numerical-methods-atlas/methods/index.html',map_page)
published={**DATA,'methods':[public_record(x) for x in METHODS],'code_release':{'download':ORIGIN+CODE+archive,'manifest':ORIGIN+CODE+'source-manifest.json','verification':ORIGIN+CODE+'verification.json','sha256':archive_hash}}
write('/numerical-methods-atlas/methods/index.json',json.dumps(published,ensure_ascii=False,indent=2)+'\n')
if REVIEWED:
    reviewed={'schema_version':1,'reviewed_on':DATA['priority_review']['on'],
              'scope':DATA['priority_review']['scope'],'method_count':len(REVIEWED),
              'review_kind':'method conditions, primary sources and existing code inspected; no new numerical runs',
              'catalog_source':ORIGIN+'/catalog/atlas-methods.json',
              'methods':[public_record(x) for x in REVIEWED]}
    write('/numerical-methods-atlas/methods/reviewed.json',json.dumps(reviewed,ensure_ascii=False,indent=2)+'\n')

for x in METHODS:
    record=public_record(x)
    url='/numerical-methods-atlas/methods/'+x['id']+'/'
    sections=[]
    for lang in ['ja','en']:
        ja=lang=='ja';body='<section data-site-language="'+lang+'" lang="'+lang+'"><p class="eyebrow">'+esc(x['group'][lang])+'</p><h1>'+esc(x['name'][lang])+'</h1><p class="resource-status">'+status(x,lang)+'</p><p class="intro">'+esc(x['summary'][lang])+'</p>'+nav(lang)
        if x.get('aliases'):body+='<p>'+('別名・表記：' if ja else 'Other names: ')+esc(' / '.join(x['aliases']))+'</p>'
        if x.get('method_review'):body+=review_intro(x,lang)
        if x['status']=='planned':
            body+='<h2>'+('次の成果物' if ja else 'Next deliverable')+'</h2><p>'+esc(x['next_deliverable'][lang])+'</p>'
        if x['reading']:
            reading=x['reading'].get(lang) or x['reading']['en']
            label=('解説章を読む' if lang in x['reading'] else '英語の解説を読む（日本語版未公開）') if ja else 'Read the chapter'
            label=x.get('reading_label',{}).get(lang,label)
            body+='<h2>'+('解説と位置付け' if ja else 'Read the formulation')+'</h2><p>'+link(reading,label)+'</p>'
        if x.get('caution'):body+='<h2>'+('比較するときの注意' if ja else 'Comparison notes')+'</h2><p>'+esc(x['caution'][lang])+'</p>'
        if x.get('assumptions'):
            body+='<h2>'+(('前提・比較仕様' if ja else 'Assumptions and comparison specification') if x.get('method_review') else ('この例の前提' if ja else 'Assumptions for this example'))+'</h2><ul>'+''.join('<li>'+esc(a)+'</li>' for a in (x.get('assumptions_ja',x['assumptions']) if ja else x['assumptions']))+'</ul>'
            if x.get('method_review'):body+=field_note(x,'assumptions',lang)
        if x.get('boundary_conditions'):
            body+='<p><strong>'+('境界条件' if ja else 'Boundaries')+':</strong> '+esc(x.get('boundary_conditions_ja',x['boundary_conditions']) if ja else x['boundary_conditions'])+'</p>'
            if x.get('method_review'):body+=field_note(x,'boundary_conditions',lang)
            body+='<p><strong>'+('単位系' if ja else 'Units')+':</strong> '+esc(x.get('units_ja',x['units']) if ja else x['units'])+'</p>'
            if x.get('method_review'):body+=field_note(x,'units',lang)
        if x['code_modules']:
            body+='<h2>'+('関連コードと検証' if ja else 'Related code and checks')+'</h2><p>'+('この章に関係する実装と検査です。各ファイルが、その名前の手法のすべての変種を検証するわけではありません。' if ja else 'Chapter-related implementations and checks. These files do not verify every variant of the named method.')+'</p><ul class="resource-files">'
            body+=''.join('<li>'+link(CODE+'numart/'+name+'.py','numart/'+name+'.py')+'</li>' for name in x['code_modules'])
            body+=''.join('<li>'+link(CODE+'tests/'+name+'.py','tests/'+name+'.py')+'</li>' for name in x['test_files'])+'</ul><p>'+link('/numerical-methods-atlas/code-and-data/','一式の取得と実行手順' if ja else 'Download the complete edition and run it')+'</p>'
            if x['test_files']:body+='<pre><code>python -m pytest -q '+' '.join('tests/'+name+'.py' for name in x['test_files'])+'</code></pre>'
        if x.get('quantum_examples'):
            body+='<h2>'+('実行できる原子計算例' if ja else 'Runnable atomic examples')+'</h2><p>'+esc(x['example_scope'][lang])+'</p><ul>'
            for ident in x['quantum_examples']:
                c=ACASES[ident];body+='<li>'+link(f'/numerical-methods-atlas/{lang}/read/quantum-atoms/#{c["section"]}',c['name'][lang])+'</li>'
            body+='</ul><p>'+link(ACODE+ATOMS['archive'],'コード・入力・結果 ZIP' if ja else 'Code, inputs and results ZIP')+' · '+link(ACODE+'verification.json','独立展開の検証記録' if ja else 'Independent-extraction verification')+'</p><p>'+link(ACODE+'atomic_radial.py','Python solver')+' · '+link(ACODE+'test_atomic_radial.py','Tests')+' · '+link(ACODE+'inputs.json','Inputs JSON')+' · '+link(ACODE+'results/results.json','Results JSON')+' · '+link(ACODE+'reference-pyscf.json','Independent reference JSON')+'</p><pre><code>'+esc(ATOMS['test_command']+'\n'+ATOMS['run_command'])+'</code></pre>'
        if x.get('model_examples'):
            body+='<h2>'+('固定入力の専用実装と検証' if ja else 'Dedicated fixed-input implementation and checks')+'</h2><p>'+esc(x['example_scope'][lang])+'</p><p>'+link(record['code_urls'][0],'Python solver')+' · '+link(record['test_urls'][0],'Tests')+' · '+link(record['code_download'],'ZIP')+' · '+link(record['code_verification'],'Verification JSON')+'</p>'
        if x.get('autodiff_release'):
            base=record['code_base']
            body+='<h2>'+('Bratu方程式で微分を比較する専用配布版' if ja else 'Dedicated Bratu derivative-comparison supplement')+'</h2>'
            body+='<p>'+('同じ離散残差に対する解析微分・有限差分・前進モード自動微分を比較し、微分誤差、Newton収束、空間格子の細分化を別々に検査します。逆モード・陰関数感度の実装や一般的な速度の優劣は検証しません。既存のコード配布版と共通実行台帳を保持した別配布版です。' if ja else 'Compare analytic, finite-difference and forward-mode AD derivatives of one discrete residual, separating derivative errors, Newton convergence and spatial refinement. Reverse mode, implicit sensitivities and general speed rankings are outside the implemented scope. This supplement preserves the existing code edition and shared execution registry.')+'</p>'
            body+='<p>'+link(base+'README.md','取得・実行手順 / README')+' · '+link(record['code_download'],'コード・検査・図とデータ ZIP' if ja else 'Code, tests, figure and data ZIP')+' · '+link(record['code_manifest'],'ファイル目録・SHA-256' if ja else 'File manifest / SHA-256')+' · '+link(record['code_verification'],str(record['passed_tests'])+('件成功・検証記録' if ja else ' tests passed / verification'))+'</p>'
            body+='<ul>'+''.join('<li>'+link(url,name)+'</li>' for url,name in zip(record['code_urls'],['numart/autodiff.py','numart/krylov.py','scripts/build_autodiff.py']))+'<li>'+link(record['test_urls'][0],'tests/test_autodiff.py')+'</li></ul>'
            body+='<p>'+link(record['results'],'微分・残差・格子収束の測定記録 / JSON' if ja else 'Derivative, residual and mesh-refinement measurements / JSON')+'</p>'
            body+='<p>'+('ZIPを展開したフォルダで仮想環境を作成・有効化し、依存関係を導入して実行します。コードのMITと、図・本文・データの利用条件を区別してください。' if ja else 'From the extracted folder, create and activate a virtual environment, install dependencies and run the checks. Distinguish the code MIT license from the separate terms for figures, prose and data.')+'</p><pre><code>'+esc('python -m pip install -r requirements.txt\n'+'\n'.join(record['run_commands']))+'</code></pre>'
            body+='<p>'+link(base+'LICENSE','MIT License')+' · '+link(base+'LICENSING.md','適用範囲 / Licensing scope')+'</p>'
        if x.get('sensitivity_release'):
            base=record['code_base']
            body+='<h2>'+('Bratuパラメータ感度：陰関数微分と離散随伴の専用配布版' if ja else 'Bratu parameter sensitivity: implicit and discrete-adjoint supplement')+'</h2>'
            body+='<p>'+('収束した同じ離散方程式を微分し、解析的な連続感度、陰関数の感度方程式、随伴勾配、パラメータを変えて解き直した有限差分を照合します。非線形求解・感度求解・随伴求解の残差と格子誤差を分けます。一般の逆問題最適化や非滑らかな衝撃波の感度は対象外です。' if ja else 'Differentiate the same converged discrete equation and compare the analytic continuous sensitivity, implicit sensitivity solve, adjoint gradient and finite differences with fresh nonlinear solves. Primal, sensitivity and adjoint residuals are separated from grid error. General inverse optimization and nonsmooth shock sensitivities are outside this example.')+'</p>'
            body+='<p>'+link(base+'README.md','取得・実行手順 / README')+' · '+link(record['code_download'],'コード・検査・図とデータ ZIP' if ja else 'Code, tests, figure and data ZIP')+' · '+link(record['code_manifest'],'ファイル目録・SHA-256' if ja else 'File manifest / SHA-256')+' · '+link(record['code_verification'],str(record['passed_tests'])+('件成功・検証記録' if ja else ' tests passed / verification'))+'</p>'
            body+='<ul>'+''.join('<li>'+link(url,url.removeprefix(base))+'</li>' for url in record['code_urls']+record['test_urls'])+'</ul>'
            body+='<p>'+link(record['results'],'感度・随伴・差分・格子収束の測定記録 / JSON' if ja else 'Sensitivity, adjoint, finite-difference and grid-refinement measurements / JSON')+'</p>'
            body+='<pre><code>'+esc('python -m pip install -r requirements.txt\n'+'\n'.join(record['run_commands']))+'</code></pre>'
            body+='<p>'+link(base+'LICENSE','MIT License')+' · '+link(base+'LICENSING.md','適用範囲 / Licensing scope')+'</p>'
        if x.get('inverse_release'):
            scalar=record.get('scalar_inverse_release',record)
            base=scalar['code_base']
            body+='<h2>'+('Bratuの逆問題：随伴勾配によるλ推定の専用配布版' if ja else 'Bratu inverse problem: adjoint-gradient parameter fitting')+'</h2>'
            body+='<p>'+('定数λを1個推定する既存配布版です。同じ離散化での回復、連続解析解からの観測、固定摂動を分けて検証します。2パラメータの拡張は次の別配布版で扱います。' if ja else 'The existing edition fits one constant lambda and distinguishes same-discretization recovery, continuous analytic observations and fixed perturbations. The following separate edition provides the two-parameter extension.')+'</p>'
            body+='<p>'+link(base+'README.md','取得・実行手順 / README')+' · '+link(scalar['code_download'],'コード・検査・観測データ・図 ZIP' if ja else 'Code, tests, observations and figure ZIP')+' · '+link(scalar['code_manifest'],'ファイル目録・SHA-256' if ja else 'File manifest / SHA-256')+' · '+link(scalar['code_verification'],str(scalar['passed_tests'])+('件成功・検証記録' if ja else ' tests passed / verification'))+'</p>'
            body+='<ul>'+''.join('<li>'+link(url,url.removeprefix(base))+'</li>' for url in scalar['code_urls']+scalar['test_urls'])+'</ul>'
            body+='<p>'+link(scalar['results'],'随伴勾配・推定履歴・格子バイアス・固定ノイズの記録 / JSON' if ja else 'Adjoint gradients, fit histories, grid bias and fixed-noise records / JSON')+'</p>'
            body+='<pre><code>'+esc('python -m pip install -r requirements.txt\n'+'\n'.join(scalar['run_commands']))+'</code></pre>'
            body+='<p>'+link(base+'LICENSE','MIT License')+' · '+link(base+'LICENSING.md','適用範囲 / Licensing scope')+'</p>'
        if x.get('multi_inverse_release'):
            base=record['code_base']
            body+='<h2>'+('Bratuの複数パラメータ逆問題：正則化と識別可能性' if ja else 'Multi-parameter Bratu inversion: regularization and identifiability')+'</h2><p>'+esc(x['limitations'][lang])+'</p>'
            body+='<p>'+link(base+'README.md','取得・実行手順 / README')+' · '+link(record['code_download'],'コード・検査・観測データ・図 ZIP' if ja else 'Code, tests, observations and figure ZIP')+' · '+link(record['code_manifest'],'ファイル目録・SHA-256' if ja else 'File manifest / SHA-256')+' · '+link(record['code_verification'],str(record['passed_tests'])+('件成功・検証記録' if ja else ' tests passed / verification'))+'</p>'
            body+='<ul>'+''.join('<li>'+link(url,url.removeprefix(base))+'</li>' for url in record['code_urls']+record['test_urls'])+'</ul>'
            body+='<p>'+link(record['results'],'係数推定・正則化・データ感度SVD・識別不能例の記録 / JSON' if ja else 'Coefficient fits, regularization, data-sensitivity SVD and ambiguity records / JSON')+'</p>'
            body+='<pre><code>'+esc('python -m pip install -r requirements.txt\n'+'\n'.join(record['run_commands']))+'</code></pre>'
            body+='<p>'+link(base+'LICENSE','MIT License')+' · '+link(base+'LICENSING.md','適用範囲 / Licensing scope')+'</p>'
        if x.get('fdtd_release'):
            base=record['code_base']
            body+='<h2>'+('2次元TMzのYee FDTD：周期波・完全導体空洞' if ja else '2D TMz Yee FDTD: periodic wave and PEC cavity')+'</h2>'
            body+='<p>'+esc(x['limitations'][lang])+'</p>'
            body+='<p>'+link(base+'README.md','取得・実行手順 / README')+' · '+link(record['code_download'],'コード・固定入力・結果 ZIP' if ja else 'Code, fixed inputs and results ZIP')+' · '+link(record['code_manifest'],'ファイル目録・SHA-256' if ja else 'File manifest / SHA-256')+' · '+link(record['code_verification'],str(record['passed_tests'])+('件成功・独立展開の検証記録' if ja else ' tests passed / independent-extraction verification'))+'</p>'
            body+='<ul>'+''.join('<li>'+link(url,url.removeprefix(base))+'</li>' for url in record['code_urls']+record['test_urls'])+'</ul>'
            body+='<p>'+link(record['result_urls']['periodic-wave'],'周期平面波 / Periodic-wave JSON')+' · '+link(record['result_urls']['pec-cavity'],'完全導体空洞 / PEC-cavity JSON')+'</p>'
            body+='<pre><code>'+esc('python -m pip install -r requirements.txt\n'+'\n'.join(record['run_commands']))+'</code></pre>'
            body+='<p>'+link(base+'LICENSE','MIT License')+' · '+link('/rights/','本文・図・データの利用条件' if ja else 'Terms for prose, figures and data')+'</p>'
        if x.get('molecular_examples'):
            molecular=record['molecular_release'];molecular_base=molecular['code_base']
            body+='<h2>'+('H₂の有限Gaussian基底RHF' if ja else 'H₂ RHF in finite Gaussian bases')+'</h2><p>'+esc(x['molecular_scope'][lang])+'</p><p>'+link('/numerical-methods-atlas/'+lang+'/read/h2-hf/','独立参照・SCF・基底の収束' if ja else 'Independent reference, SCF and basis refinement')+' · '+link(molecular_base+'molecular_hf.py','Python solver')+' · '+link(molecular_base+'test_molecular_hf.py','Tests')+' · '+link(molecular['release']['download'],'ZIP')+'</p>'
        if x.get('periodic_examples'):
            periodic=record['periodic_release'];base=periodic['code_base']
            body+='<h2>'+('周期HeセルのDFT：PySCFの実行・収束検査' if ja else 'Periodic-He DFT: PySCF execution and convergence checks')+'</h2><p>'+esc(x['periodic_scope'][lang])+'</p><p>'+link('/numerical-methods-atlas/'+lang+'/read/periodic-dft/','Γ点・k点・基底・SCFと独立参照' if ja else 'Gamma, k mesh, basis, SCF and independent reference')+' · '+link(base+'periodic_dft.py','Python driver')+' · '+link(base+'test_periodic_dft.py','Tests')+' · '+link(periodic['release']['download'],'ZIP')+'</p>'
        if x.get('force_examples'):
            forces=record['force_release'];force_base=forces['code_base']
            body+='<h2>'+('周期He₂の原子間力とBOMDへの接続' if ja else 'Periodic He₂ forces and the BOMD interface')+'</h2><p>'+esc(x['force_scope'][lang])+'</p><p>'+link('/numerical-methods-atlas/'+lang+'/read/periodic-forces/','力の有限差分・独立参照・収束' if ja else 'Force finite differences, independent reference and refinement')+' · '+link(force_base+'periodic_forces.py','Python force driver')+' · '+link(force_base+'bomd.py','BOMD adapter')+' · '+link(force_base+'test_periodic_forces.py','Tests')+' · '+link(forces['release']['download'],'ZIP')+'</p>'
        if x.get('depth_release'):
            extra=record['depth_release']
            body+='<h2>'+('小規模な専用実装と実測検証' if ja else 'Small dedicated implementations and measured checks')+'</h2><p>'+esc(x['depth_scope'][lang])+'</p><ul>'
            body+=''.join('<li>'+link(e['entry']+'?lang='+lang,e['title'][lang])+' · '+link(e['reading'][lang],'条件・数式・一次文献' if ja else 'Conditions, equations and primary sources')+'</li>' for e in extra['examples'])
            body+='</ul><p>'+link(extra['code_download'],'コード・固定入力・テスト・結果 ZIP' if ja else 'Code, fixed inputs, tests and results ZIP')+' · '+link(extra['code_verification'],str(extra['passed_tests'])+('件の検査と独立展開記録' if ja else ' tests and independent-extraction receipt'))+'</p><p>'+('選択した固定例の検証です。共通22例の台帳とは別の補助配布版で、各手法の全変種を検証するものではありません。' if ja else 'Validation applies to the selected fixed examples. These supplements are separate from the shared22-case registry and do not verify every variant of a named method.')+'</p>'
        for common in execution_links(x['id']):
            body+='<p class="resource-summary">'+link(common['guide'][lang],'入力・実行・結果判定・引用の共通手順' if ja else 'Shared input, execution, validation and citation steps')+'</p>'
        if x.get('example'):
            example=x['example']
            body+='<h2>'+('固定入力から計算する' if ja else 'Run an explicit input')+'</h2><p>'+('192粒子の座標・質量を保存した入力を使い、ツリーと直接和の力を計算します。出力は誤差と検査を記録するJSON、粒子ごとの力を記録するCSVです。' if ja else 'Use explicit positions and masses for 192 particles. Compute tree and direct-sum forces, then export error/check records as JSON and particle forces as CSV.')+'</p><p>'+link(example['input'],'入力 / Input JSON')+' · '+link(example['runner'],'実行コード / Runner')+' · '+link(example['reference'],'参照出力 / Reference JSON')+' · '+link(example['forces'],'力のデータ / Force CSV')+'</p><pre><code>'+esc(example['command'])+'</code></pre>'
        body+='<h2>'+('適用範囲と残る作業' if ja else 'Scope and remaining work')+'</h2><p>'+esc(x['limitations'][lang])+'</p>'
        if x.get('method_review'):body+=field_note(x,'limitations',lang)+verification_html(x,lang)
        if x['metadata_review']['level'].startswith('chapter-linked') and not x.get('assumptions'):
            body+='<p>'+('この項目の条件・単位の個別整理は継続中です。空欄は適用条件がないことを意味しません。解説章とコードの条件を確認してください。' if ja else 'Method-record assumptions and units are still being curated. Missing fields do not mean unrestricted applicability; consult the chapter and code.')+'</p>'
        if x.get('method_review'):
            body+=references_html(x,lang)
        elif x['references']:
            body+='<h2>'+('文献への入口' if ja else 'Reference entry points')+'</h2><ul>'+''.join('<li>'+link(r['url'],r.get('label',r['url']))+'</li>' for r in x['references'])+'</ul><p>'+('書誌や章の参照先の案内です。原文・式の確認範囲は元の章とJSONのscope欄を参照してください。' if ja else 'Bibliographic and chapter reference links. Consult the chapter and JSON scope fields for the extent of source review.')+'</p>'
        else:
            body+='<p>'+('一次文献の個別整理は今後の作業です。' if ja else 'Dedicated primary-reference curation remains to be completed.')+'</p>'
        body+='<p>'+link('index.json','この項目 / JSON' if ja else 'This record / JSON')+' · '+link('index.md','この項目 / Markdown' if ja else 'This record / Markdown')+' · '+link('/using/','引用と利用条件' if ja else 'Citation and reuse')+'</p></section>'
        sections.append(body)
    structured={'@context':'https://schema.org','@type':'LearningResource','name':x['name']['en'],'url':ORIGIN+url,'author':{'@type':'Person','name':'Hiroshi Koyama'},'isPartOf':{'@type':'WebSite','name':'An Atlas of Numerical Methods','url':ORIGIN+'/numerical-methods-atlas/'},'description':x['summary']['en'],'inLanguage':['ja','en']}
    write(url+'index.html',page(x['name']['ja'],x['name']['en'],url,''.join(sections),structured))
    record=public_record(x)
    write(url+'index.json',json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    md='# '+x['name']['en']+' / '+x['name']['ja']+'\n\nStatus: '+x['status']+'\n\n'+x['summary']['en']+'\n\n'+x['summary']['ja']+'\n\n'+x['limitations']['en']+'\n\n'
    if x.get('aliases'):md+='Other names: '+', '.join(x['aliases'])+'\n\n'
    if x.get('caution'):md+='Comparison notes: '+x['caution']['en']+'\n\n'+x['caution']['ja']+'\n\n'
    if x.get('method_review'):md+=review_markdown(x)+'\n\n'
    md+='\n'.join('- Reading ('+lang+'): '+ORIGIN+u for lang,u in x['reading'].items())+'\n\n'
    md+='\n'.join('- Code: '+ORIGIN+CODE+'numart/'+name+'.py' for name in x['code_modules'])+'\n\n'
    md+='\n'.join('- Reference: '+r['url']+' — '+r['scope'] for r in x['references'])+'\n\n'
    if x.get('model_examples'):md+='Scoped example: '+x['example_scope']['en']+'\n\nCode: '+record['code_urls'][0]+'\nTests: '+record['test_urls'][0]+'\nDownload: '+record['code_download']+'\nVerification: '+record['code_verification']+'\n\n'
    if x.get('quantum_examples'):md+='Scoped example: '+x['example_scope']['en']+'\n\n'+json.dumps(record['code_examples'],ensure_ascii=False,indent=2)+'\n\nDownload: '+record['code_download']+'\nVerification: '+record['code_verification']+'\nSource: '+record['code_urls'][0]+'\nResults: '+record['results']+'\nCommands (from extracted atomic edition):\n\n'+ '\n'.join(record['run_commands'])+'\n\n'
    if x.get('molecular_examples'):md+='Molecular scope: '+x['molecular_scope']['en']+'\n\n'+json.dumps(record['molecular_release'],ensure_ascii=False,indent=2)+'\n\n'
    if x.get('periodic_examples'):md+='Periodic scope: '+x['periodic_scope']['en']+'\n\n'+json.dumps(record['periodic_release'],ensure_ascii=False,indent=2)+'\n\n'
    if x.get('autodiff_release'):
        md+='Forward-mode AD supplement: analytic/finite-difference/AD Bratu derivatives, Newton convergence and spatial refinement. Reverse-mode execution and implicit sensitivities are not implemented in this edition. The separate Bratu sensitivity edition is linked from /numerical-methods-atlas/en/read/adjoint/.\n\n'
        md+='\n'.join('- Code: '+u for u in record['code_urls'])+'\n\n'+'\n'.join('- Tests: '+u for u in record['test_urls'])+'\n\n'
        md+='Download: '+record['code_download']+'\nManifest: '+record['code_manifest']+'\nVerification: '+record['code_verification']+'\nMeasurements: '+record['results']+'\n\nCommands (from extracted supplement):\n\n```sh\npython -m pip install -r requirements.txt\n'+'\n'.join(record['run_commands'])+'\n```\n\n'
    if x.get('sensitivity_release'):
        md+='Bratu implicit sensitivity and discrete-adjoint supplement. Includes analytic continuous sensitivity, finite differences with fresh nonlinear solves, grid refinement and a nonsymmetric transpose test.\n\n'
        md+='\n'.join('- Code: '+u for u in record['code_urls'])+'\n\n'+'\n'.join('- Tests: '+u for u in record['test_urls'])+'\n\n'
        md+='Download: '+record['code_download']+'\nManifest: '+record['code_manifest']+'\nVerification: '+record['code_verification']+'\nMeasurements: '+record['results']+'\n\nCommands (from extracted supplement):\n\n```sh\npython -m pip install -r requirements.txt\n'+'\n'.join(record['run_commands'])+'\n```\n\n'
    if x.get('force_examples'):md+='Force scope: '+x['force_scope']['en']+'\n\n'+json.dumps(record['force_release'],ensure_ascii=False,indent=2)+'\n\n'
    if x.get('depth_release'):
        extra=record['depth_release']
        md+='## Small fixed-input validation supplement\n\n'+x['depth_scope']['en']+'\n\n'+x['depth_scope']['ja']+'\n\n'
        md+='\n'.join('- '+e['title']['en']+': '+e['entry'] for e in extra['examples'])+'\n\n'
        md+='Download: '+extra['code_download']+'\nVerification: '+extra['code_verification']+'\nResults: '+extra['results']+'\n\n'
    if x.get('inverse_release'):
        scalar=record.get('scalar_inverse_release',record)
        md+='Bratu inverse supplement: bounded projected adjoint-gradient fitting of one scalar parameter from fixed synthetic observations. Same-model consistency, continuous-observation grid bias and fixed-noise shifts are separate checks.\n\n'
        md+='\n'.join('- Code: '+u for u in scalar['code_urls'])+'\n\n'+'\n'.join('- Tests: '+u for u in scalar['test_urls'])+'\n\n'
        md+='Download: '+scalar['code_download']+'\nManifest: '+scalar['code_manifest']+'\nVerification: '+scalar['code_verification']+'\nMeasurements: '+scalar['results']+'\n\nCommands (from extracted supplement):\n\n```sh\npython -m pip install -r requirements.txt\n'+'\n'.join(scalar['run_commands'])+'\n```\n\n'
    if x.get('multi_inverse_release'):
        md+='Multi-parameter Bratu inverse supplement: two spatial coefficients, adjoint fitting, Tikhonov regularization and data-only SVD identifiability diagnostics. Regularization does not add observational information.\n\n'
        md+='\n'.join('- Code: '+u for u in record['code_urls'])+'\n\n'+'\n'.join('- Tests: '+u for u in record['test_urls'])+'\n\n'
        md+='Download: '+record['code_download']+'\nManifest: '+record['code_manifest']+'\nVerification: '+record['code_verification']+'\nMeasurements: '+record['results']+'\n\nCommands (from extracted supplement):\n\n```sh\npython -m pip install -r requirements.txt\n'+'\n'.join(record['run_commands'])+'\n```\n\n'
    if x.get('fdtd_release'):
        md+='2D TMz Yee FDTD supplement: source-free dimensionless vacuum, periodic oblique plane wave and rectangular PEC cavity. Analytic fields, grid refinement, dispersion and modified discrete energy are checked separately.\n\n'
        md+='\n'.join('- Code: '+u for u in record['code_urls'])+'\n\n'+'\n'.join('- Tests: '+u for u in record['test_urls'])+'\n\n'
        md+='Download: '+record['code_download']+'\nManifest: '+record['code_manifest']+'\nVerification: '+record['code_verification']+'\n\n'+'\n'.join('- '+case+': '+u for case,u in record['result_urls'].items())+'\n\nCommands (from extracted supplement):\n\n```sh\npython -m pip install -r requirements.txt\n'+'\n'.join(record['run_commands'])+'\n```\n\n'
    if record['execution_examples']:md+='Common execution records: '+json.dumps(record['execution_examples'],ensure_ascii=False)+'\n\n'
    if x.get('next_deliverable'):md+='Next: '+x['next_deliverable']['en']+'\n\n'
    if x.get('example'):md+='Runnable example:\n\n'+json.dumps(x['example'],ensure_ascii=False,indent=2)+'\n\n'
    md+='Source: '+ORIGIN+url+'\nEdition and terms: '+ORIGIN+'/numerical-methods-atlas/code-and-data/\n'
    write(url+'index.md',md)

sections=[]
for lang in ['ja','en']:
    ja=lang=='ja'
    body='<section data-site-language="'+lang+'" lang="'+lang+'"><p class="eyebrow">CODE EDITION '+EDITION+'</p><h1>'+('コード・入力・検証を取得する' if ja else 'Get code, inputs and verification')+'</h1><p class="intro">'+(f'{module_count}個のPythonモジュール、{test_count}個の検査ファイル、検査に必要な保存データをまとめた教育用配布版です。認証なしで取得できます。' if ja else f'An educational edition with {module_count} Python modules, {test_count} test files and the stored data required by the tests. No authentication is needed.')+'</p>'+nav(lang)
    body+='<aside class="resource-summary"><h2>'+('新しい原子計算の配布版' if ja else 'Separate atomic calculation edition')+'</h2><p>'+esc(ATOMS['scope'][lang])+'</p><p>'+link(f'/numerical-methods-atlas/{lang}/read/quantum-atoms/','水素型原子・Heの結果と実行手順' if ja else 'Hydrogenic/He results and reproduction')+' · '+link(ACODE+ATOMS['archive'],'Quantum atoms ZIP')+' · '+link(ACODE+'verification.json',str(AVER['passed'])+' checks passed / verification')+'</p></aside>'
    body+='<p>'+link(CODE+archive,f'コード一式を取得 / ZIP（約{archive_mb} MB）' if ja else f'Download code edition / ZIP (about {archive_mb} MB)')+' · '+link(CODE+'source-manifest.json','ファイル目録・SHA-256 / Manifest')+' · '+link(CODE+'verification.json','実行した検証の記録 / Verification')+'</p>'
    body+='<h2>'+('実行する' if ja else 'Run the examples')+'</h2><p>'+('ZIPを展開し、そのフォルダでPythonの仮想環境を作成・有効化してから実行してください。Python 3.12で配布版を検証しました。' if ja else 'Extract the ZIP, create and activate a Python virtual environment, then run these commands from the extracted folder. The edition was checked with Python 3.12.')+'</p><pre><code>python -m pip install -r requirements.txt\npython -m pytest -q\npython -m numart.cli --help</code></pre>'
    body+='<p>'+('小さな重力の検査から始める場合：' if ja else 'Start with a small gravity check:')+'</p><pre><code>python -m pytest -q tests/test_particle_gravity.py</code></pre>'
    body+='<p>'+link('/numerical-methods-atlas/methods/barnes-hut/','192粒子の固定入力を使い、JSONとCSVを出力する例' if ja else 'Run 192 explicitly specified particles and export JSON and CSV')+'</p>'
    body+='<h2>'+('検証した範囲' if ja else 'Verified scope')+'</h2><p>'+(f'ZIPを独立したフォルダに展開し、同梱ファイルだけで既存検査を実行しました。{verification["passed"]}件通過、適用対象外{verification["skipped"]}件、失敗0件です。これは全手法の汎用性や原論文の全図の再現を保証するものではありません。' if ja else f'The ZIP was extracted into an independent directory and checked using packaged files: {verification["passed"]} passed, {verification["skipped"]} inapplicable cases skipped, 0 failed. This does not establish general applicability or reproduction of every original figure.')+'</p>'
    body+='<p>'+('Barnes–Hutの孤立・軟化重力と、周期FFT PMは異なる境界問題です。この配布版に専用のEwald・PME・SPME・量子化学・DFTソルバーは含まれません。' if ja else 'Isolated softened Barnes–Hut gravity and periodic FFT PM are different boundary problems. No dedicated Ewald, PME, SPME, quantum-chemistry or DFT solver is included in this edition.')+'</p>'
    body+='<h2>'+('版と利用条件' if ja else 'Version and reuse')+'</h2><p class="resource-files">SHA-256: <code>'+archive_hash+'</code></p><p>'+('コード版・入力条件・原論文・参照URLを計算記録に残してください。自作実装コードはMIT、保存データ・本文・図は別条件です。' if ja else 'Retain the code edition, inputs, original method papers and source URL. Original implementation code is MIT; stored data, prose and figures have separate terms.')+'</p><p>'+link(CODE+'LICENSE','MIT License')+' · '+link(CODE+'LICENSING.md','適用範囲 / Licensing scope')+' · '+link('/using/','使い方・引用 / Use and cite')+'</p></section>'
    sections.append(body)
structured={'@context':'https://schema.org','@type':'SoftwareSourceCode','name':'Numerical Methods Atlas code edition '+EDITION,'codeRepository':'https://github.com/hrkoyama/hrkoyama.github.io/tree/main'+CODE,'programmingLanguage':'Python','softwareVersion':EDITION,'downloadUrl':ORIGIN+CODE+archive,'license':ORIGIN+CODE+'LICENSE','author':{'@type':'Person','name':'Hiroshi Koyama'}}
write('/numerical-methods-atlas/code-and-data/index.html',page('コード・入力・検証','Code, inputs and verification','/numerical-methods-atlas/code-and-data/',''.join(sections),structured))

# The old history remains private; normal navigation points to the public edition.
for p in ATLAS.rglob('*.html'):
    text=p.read_text()
    def replace(match):
        href,label=match.group(1),match.group(2)
        if not re.match(r'https://github[.]com/koyamarium/(?:numerical-methods-atlas|the-art-of-numerical-algorithms)(?:/|$)',href):return match.group(0)
        return link('/numerical-methods-atlas/code-and-data/','公開コード・データ / Public code and data')
    new=re.sub(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>',replace,text,flags=re.S)
    if p==ATLAS/'index.html':
        marker='<!-- public-resource-entry -->'
        new=re.sub(r'<!-- public-resource-entry -->.*?<!-- /public-resource-entry -->','',new,flags=re.S)
        entry=marker+'<nav aria-label="Public atlas resources" style="display:flex;flex-wrap:wrap;gap:12px 24px;padding:16px 5%;border-bottom:1px solid #d2d3c8">'+link('/numerical-methods-atlas/methods/','手法の見取り図 / Method map')+link('/numerical-methods-atlas/code-and-data/','コード・入力・検証 / Code, inputs and checks')+'</nav><!-- /public-resource-entry -->'
        new=new.replace('<main',entry+'<main',1)
    if new!=text:p.write_text(new)
site_config=ATLAS/'site.json'
config=json.loads(site_config.read_text());config['repositoryUrl']=ORIGIN+'/numerical-methods-atlas/code-and-data/';config['legacyRepositoryUrl']=config['repositoryUrl'];site_config.write_text(json.dumps(config,ensure_ascii=False,indent=2)+'\n')
for p in ATLAS.glob('content*.json'):
    text=p.read_text()
    text=re.sub(r'https://github[.]com/koyamarium/(?:numerical-methods-atlas|the-art-of-numerical-algorithms)(?:/[^\s"<>\\)]*)?', ORIGIN+'/numerical-methods-atlas/code-and-data/', text)
    json.loads(text)
    p.write_text(text)
xml=ET.parse(ATLAS/'sitemap.xml');root=xml.getroot();existing={n.text for n in root.findall('.//{*}loc')};ns='{http://www.sitemaps.org/schemas/sitemap/0.9}'
for node in list(root):
    loc=node.find(ns+'loc')
    match=re.fullmatch(ORIGIN+r'/numerical-methods-atlas/methods/([^/]+)/',loc.text or '') if loc is not None else None
    if match and match.group(1) not in active_ids:root.remove(node)
for path in ['/numerical-methods-atlas/methods/','/numerical-methods-atlas/code-and-data/']+['/numerical-methods-atlas/methods/'+x['id']+'/' for x in METHODS]:
    if ORIGIN+path not in existing:ET.SubElement(ET.SubElement(root,ns+'url'),ns+'loc').text=ORIGIN+path
ET.register_namespace('',ns[1:-1]);xml.write(ATLAS/'sitemap.xml',encoding='utf-8',xml_declaration=True)
guide=ROOT/'llms.txt'
block=f'''\n## Method records and executable code

- [Method map]({ORIGIN}/numerical-methods-atlas/methods/): {existing_count} existing method/building-block entries and {planned_count} separately labeled development candidates. Planned entries have no dedicated solver or verification result.
- [Method registry / JSON]({ORIGIN}/numerical-methods-atlas/methods/index.json): Names, status, reading routes, chapter-related Python modules, tests, reference links and explicit metadata gaps. Each entry has a stable HTML URL, index.json and index.md. Null assumptions or boundaries mean not yet curated, not unrestricted applicability.
- [Reviewed priority methods / JSON]({ORIGIN}/numerical-methods-atlas/methods/reviewed.json): {len(REVIEWED)} method-specific records with problems, adopted variants, use/avoid conditions, units, boundary conventions, explicit specified/not-applicable/unknown states, source roles and actual source-check depth. Metadata review is not a new numerical verification run; planned methods retain their status.
- Editorial scope: {DATA['editorial_policy']['statement']['en']}
- [Code, inputs and verification]({ORIGIN}/numerical-methods-atlas/code-and-data/): Public ZIP, file hashes, dependencies and standalone verification. Original implementation code is MIT within its scope; datasets and content retain separate terms.
- [Shared execution records / JSON]({EXECUTION_REGISTRY}): {len(EXECUTION_RECORDS)} existing problem families (transport, shocks, Poisson, ODEs, particles, and atoms) with fixed inputs, versioned downloads, commands, outputs, numeric acceptance rules, failure scope and citation. Follow each record’s guide URL and the linked public-download rerun receipt. The atomic examples share one runner.
- [Code edition manifest]({ORIGIN}{CODE}source-manifest.json): Direct file URLs are the public_base_url plus each listed path. The archive contains no Git history or private manuscripts.
- [Code edition verification]({ORIGIN}{CODE}verification.json): {verification['passed']} passed, {verification['skipped']} intentionally inapplicable cases skipped in an independent extraction. No Ewald/PME/SPME or DFT implementation is included in this edition.
- [Runnable atomic examples]({ORIGIN}/numerical-methods-atlas/en/read/quantum-atoms/): two hydrogenic/He problem families, {AVER["passed"]} independently extracted package checks passed; code, fixed inputs, CSV profiles, SCF histories and PySCF reference results. [Atomic source manifest]({ORIGIN}{ACODE}source-manifest.json) and [verification]({ORIGIN}{ACODE}verification.json). Only spherical 1s² HF and Dirac exchange-only LDA for He; not general molecular or periodic DFT.
- [Quantum chemistry and DFT]({ORIGIN}/numerical-methods-atlas/en/read/quantum-chemistry/): {sum(x['group']['id']=='quantum' for x in METHODS)} bilingual introductory topics, primary references, representative formulas and scoped atomic, H2 RHF and fixed-He periodic-LDA calculations; general molecular DFT and other periodic materials remain unvalidated. Canonical text and references: /catalog/atlas-quantum.json. Atlas-based specialist AI is deferred to 2027 or later in /catalog/atlas-work-queue.json.
'''
text=guide.read_text()
text=re.sub(r'\n## Method records and executable code\n.*?(?=\n## |\Z)',lambda _:block,text,flags=re.S) if '\n## Method records and executable code\n' in text else text+block
guide.write_text(text)
print(f'Built {len(METHODS)} method records, a public map and code download guide.')
