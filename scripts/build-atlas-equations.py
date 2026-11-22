#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publish every shared equation/model entry with statically typeset formulas and deep reading links."""
from collections import Counter
from pathlib import Path
import hashlib
import html
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from atlas_execution_discovery import load_discovery, entry_url
from atlas_equation_availability import equation_evidence

ROOT=Path(__file__).resolve().parents[1]
ATLAS=ROOT/'numerical-methods-atlas'
ORIGIN='https://hrkoyama.github.io'
URL='/numerical-methods-atlas/equations/'
data=json.loads((ROOT/'catalog/atlas-equations.json').read_text())
coverage=json.loads((ATLAS/'coverage.json').read_text())
inventory={x['id']:x for x in coverage['items'] if x['kind']=='equation'}
records=data['equations']
discovery=load_discovery(ROOT)
execution_examples=discovery['examples']
evidence=equation_evidence(ROOT,records,discovery)
assert len({x['id'] for x in records})==len(records)
assert {x['id'] for x in records}==set(inventory),'Reconcile equation formulas with the shared coverage inventory'
assert len(records)==coverage['counts']['equations']
groups={g['id']:g for g in data['groups']}
for x in records:
    assert x['status']==inventory[x['id']]['status'],x['id']
    assert x['chapter']==inventory[x['id']]['chapter'],x['id']
    assert x['group'] in groups and x['formula'] and all(x['formula']),x['id']
    assert x['name']['ja'] and x['name']['en'] and x['note']['ja'] and x['note']['en']

math=json.loads(subprocess.run(
    ['node','scripts/render-atlas-math.cjs'],cwd=ROOT,
    input=json.dumps(records+[
        {'id':'execution-'+x['id'],'formula':x['formula']['latex']}
        for x in execution_examples],ensure_ascii=False),
    text=True,capture_output=True,check=True
).stdout)
counts=Counter(x['group'] for x in records)
status_counts=Counter(x['status'] for x in records)
assert status_counts['local-example']==coverage['counts']['local_equations']
assert status_counts['reading']==coverage['counts']['reading_equations']
esc=html.escape

def link(url,label):
    return '<a href="'+esc(url)+'">'+esc(label)+'</a>'

def reading(chapter,lang,section=None):
    path=ATLAS/lang/'read'/chapter/'index.html'
    assert path.is_file(),path
    if section:
        assert re.search(r'\bid=[\"\']'+re.escape(section)+r'[\"\']',path.read_text()),(chapter,lang,section)
    return f'/numerical-methods-atlas/{lang}/read/{chapter}/'+('#'+section if section else '')

def related_examples(model_id):
    return evidence['common'][model_id]

def execution_shortcuts(lang):
    ja=lang=='ja'
    body='<section class="execution-equation-shortcuts" id="execution-formulas-'+lang+'"><h2>'+(
        f'公開{len(execution_examples)}問題を、式から実行する' if ja else
        f'Run {len(execution_examples)} published examples from their formulas')+'</h2>'
    body+='<p>'+esc(
        f'下の式は固定入力に対応する問題・近似の定義です。各カードから入力・実行・参照値と許容誤差へ直接進めます。全{len(records)}方程式・モデルの台帳とは別の案内で、モデル数や検証問題数を追加しません。' if ja else
        f'These problem and approximation formulas match fixed execution inputs. Each card leads directly to the input, run instructions, references and tolerances. This is separate from the {len(records)}-model inventory and adds no models or verified problems.')+'</p>'
    body+='<p class="execution-formula-scroll-note">'+('数式が収まらない場合は、式の部分を横にスクロールできます。' if ja else 'Wide formulas scroll horizontally within each card.')+'</p>'
    body+='<div class="execution-formula-grid">'
    role_names={'problem':('問題の式','Problem equation'),
                'approximation':('近似・表現の式','Approximation / representation'),
                'diagnostic':('診断式','Diagnostic')}
    for x in execution_examples:
        wide=' execution-formula-card-wide' if any(len(f)>130 for f in x['formula']['latex']) else ''
        body+='<article class="execution-formula-card'+wide+'" id="execution-'+x['id']+'-'+lang+'" data-execution-equation-id="'+x['id']+'">'
        body+='<p class="execution-formula-role">'+role_names[x['formula']['role']][0 if ja else 1]+'</p><h3>'+esc(x['execution']['name'][lang])+'</h3>'
        body+='<div class="execution-formula-preview">'+''.join(math['rendered']['execution-'+x['id']])+'</div>'
        body+='<p class="execution-formula-outcome">'+esc(x['outcome'][lang])+'</p>'
        body+='<details><summary>'+('式の条件と参照の種類' if ja else 'Formula conditions and reference type')+'</summary><p>'+esc(x['formula']['note'][lang])+'</p></details>'
        body+=link(entry_url(x['id'],lang),'この問題の入力・実行・判定へ →' if ja else 'Input, run and validate this example →')+'</article>'
    return body+'</div></section>'

sections=[]
for lang in ['ja','en']:
    ja=lang=='ja'
    title='数式から探す' if ja else 'Browse by equation'
    body='<section data-site-language="'+lang+'" lang="'+lang+'"><p class="eyebrow">EQUATIONS / ALL ATLAS MODELS</p><h1>'+title+'</h1>'
    intro=(f'アトラスに収録中の全{len(records)}方程式・モデルを並べました。式の形から選び、それぞれの解説へ進めます。' if ja else f'Browse all {len(records)} equation/model entries in the atlas. Recognize a formula and follow its explanation.')
    body+='<p class="intro">'+intro+'</p>'
    summary=(f'計算例あり{status_counts["local-example"]}項目・文献解説のみ{status_counts["reading"]}項目。モデルの種類数であり、表示する式の行数ではありません。' if ja else f'{status_counts["local-example"]} entries link to scoped local examples; {status_counts["reading"]} are literature-only. These count model entries, not displayed equation lines.')
    body+='<p class="resource-summary">'+summary+'</p>'
    note=('式は代表形、または明記した模式形です。係数・単位・次元・構成則・境界条件は解説先で確認してください。「計算例あり」には縮約模型やFourier記号の検証も含みます。' if ja else 'Formulas are representative or explicitly schematic forms. Consult each chapter for coefficients, units, dimensions, closure and boundaries. Local examples can include reduced models and Fourier-symbol checks.')
    body+='<p>'+note+'</p><nav class="resource-nav">'
    body+=link('/numerical-methods-atlas/?lang='+lang,'アトラスの冒頭' if ja else 'Atlas home')
    body+=link('/numerical-methods-atlas/?lang='+lang+'#/coverage?kind=equation','収録台帳と数え方' if ja else 'Coverage inventory and counting rules')
    body+=link('/numerical-methods-atlas/test-cases/?lang='+lang,'テスト計算の全体一覧' if ja else 'All test problems')+'</nav>'
    body+='<nav class="resource-nav" aria-label="'+('実行例とモデルの一覧' if ja else 'Examples and model inventory')+'">'
    body+=link('#execution-formulas-'+lang,f'{len(execution_examples)}問題の式・実行へ' if ja else f'{len(execution_examples)} example formulas and runs')
    body+=link('#all-models-'+lang,f'全{len(records)}方程式・モデルへ' if ja else f'All {len(records)} equations and models')+'</nav>'
    body+=execution_shortcuts(lang)
    body+='<section class="equation-model-inventory" id="all-models-'+lang+'"><h2>'+(
        f'全{len(records)}方程式・モデルの解説を探す' if ja else f'Explore all {len(records)} equation/model explanations')+'</h2>'
    body+='<nav class="resource-nav" aria-label="Equation groups">'
    body+=''.join(link('#'+g['id']+'-'+lang,g[lang]+' ('+str(counts[g['id']])+')') for g in data['groups'])+'</nav>'
    for group in data['groups']:
        group_rows=[x for x in records if x['group']==group['id']]
        body+='<section><h2 id="'+group['id']+'-'+lang+'">'+esc(group[lang])+' — '+str(len(group_rows))+'</h2>'
        body+='<nav class="equation-jump-list" aria-label="'+esc(group[lang])+'">'
        body+=''.join(link('#'+x['id']+'-'+lang,x['name'][lang]) for x in group_rows)+'</nav><div class="equation-index">'
        for x in group_rows:
            route=reading(x['chapter'],lang,x.get('section'))
            wide=' equation-entry-wide' if any(len(f)>95 for f in x['formula']) else ''
            body+='<article class="equation-entry'+wide+'" id="'+x['id']+'-'+lang+'" data-equation-id="'+x['id']+'" data-equation-status="'+x['status']+'">'
            for alias in x.get('anchor_aliases',[]):body+='<span id="'+alias+'-'+lang+'"></span>'
            body+='<h3>'+esc(x['name'][lang])+'</h3>'
            label=('限定した計算例あり' if x.get('execution_scope') else '計算例あり') if x['status']=='local-example' and ja else ('Scoped local example' if x['status']=='local-example' else ('文献解説のみ・専用ソルバーなし' if ja else 'Literature only / no dedicated solver'))
            body+='<p class="resource-status">'+label+'</p><div class="equation-preview">'+''.join(math['rendered'][x['id']])+'</div>'
            if wide:body+='<p class="equation-scroll-note">'+('長い数式は横にスクロールして読めます。' if ja else 'Scroll horizontally to read long equations.')+'</p>'
            body+='<p>'+esc(x['note'][lang])+'</p>'+link(route,'このモデルの解説へ →' if ja else 'Read this model →')
            for chapter in x.get('related_chapters',[]):body+=' · '+link(reading(chapter,lang),'関連するテストの解説' if ja else 'Related test definitions')
            if x.get('execution_scope'):
                body+='<p class="equation-execution-scope">'+esc(x['execution_scope'][lang])+'</p>'
            examples=related_examples(x['id'])
            if examples:
                assert x['status']=='local-example','Reading-only entries cannot gain executable claims'
                body+='<div class="model-execution-links"><p>'+('このモデルに対応する固定入力・実行例' if ja else 'Fixed-input execution examples for this model')+'</p><ul>'
                body+=''.join('<li>'+link(entry_url(e['id'],lang),e['execution']['name'][lang])+'</li>' for e in examples)+'</ul></div>'
            supplements=evidence['supplemental'][x['id']]
            if supplements:
                assert x['status']=='local-example'
                body+='<div class="model-supplemental-links"><p>'+('共通22実行例とは別の、限定した補助実行例' if ja else 'Scoped supplemental runs, separate from the common 22 registry')+'</p><ul>'
                body+=''.join('<li>'+link(e['url']+'?lang='+lang,e['title'][lang])+'</li>' for e in supplements)+'</ul></div>'
            body+='</article>'
        body+='</div></section>'
    body+='</section>'
    body+='<p>'+link('index.json','全方程式・モデル / JSON' if ja else 'All equations and models / JSON')+' · '+link('/using/','引用と利用条件' if ja else 'Citation and reuse')+'</p></section>'
    sections.append(body)

digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()[:12]
head='<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
head+='<title data-page-title-ja="数式から探す | 数値計算法アトラス" data-page-title-en="Browse by equation | Numerical Methods Atlas">数式から探す | 数値計算法アトラス</title>'
head+='<meta name="description" content="公開'+str(len(execution_examples))+'問題の式から入力・実行・判定へ。全'+str(len(records))+'方程式・モデルの解説一覧も掲載。Find fixed-input examples by formula and browse every atlas model.">'
head+='<link rel="canonical" href="'+ORIGIN+URL+'">'
head+='<link rel="stylesheet" href="/numerical-methods-atlas/vendor/katex.min.css">'
head+='<link rel="stylesheet" href="/styles/atlas-resources.css?v='+digest(ROOT/'styles/atlas-resources.css')+'">'
head+='<link rel="stylesheet" href="/styles/atlas-purpose.css?v='+digest(ROOT/'styles/atlas-purpose.css')+'">'
head+='<link rel="stylesheet" href="/styles/atlas-equations.css?v='+digest(ROOT/'styles/atlas-equations.css')+'"></head>'
dest=ROOT/URL.lstrip('/');dest.mkdir(parents=True,exist_ok=True)
(dest/'index.html').write_text(head+'<body class="profile-page"><main id="main" class="profile-main atlas-resource-main">'+''.join(sections)+'</main></body></html>\n')
public={**data,'url':ORIGIN+URL,'counts':{'total':len(records),'local_example':status_counts['local-example'],'reading_only':status_counts['reading'],'groups':dict(counts)},'formula_renderer':{'name':math['renderer'],'version':math['version']},'equations':[{**x,'reading':{lang:ORIGIN+reading(x['chapter'],lang,x.get('section')) for lang in ['ja','en']},'execution_examples':[{'id':e['id'],'name':e['execution']['name'],'entry':{lang:entry_url(e['id'],lang) for lang in ['ja','en']}} for e in related_examples(x['id'])],
        'supplemental_execution_examples':[{'id':e['id'],'name':e['title'],'entry':{lang:ORIGIN+e['url']+'?lang='+lang for lang in ['ja','en']},'code_urls':e['code_urls'],'test_urls':e['test_urls'],'verification':e['verification'],'results':e['results']} for e in evidence['supplemental'][x['id']]]} for x in records],
        'execution_example_count':len(execution_examples),
        'supplemental_case_ids':evidence['supplemental_case_ids'],
        'execution_evidence_source_sha256':evidence['source_sha256'],
        'execution_formula_scope':discovery['scope'],
        'execution_discovery_source':{'url':ORIGIN+'/catalog/atlas-execution-discovery.json','sha256':discovery['source_sha256']},
        'execution_examples':[{**{k:v for k,v in x.items() if k!='execution'},'name':x['execution']['name'],'method_ids':x['execution']['method_ids'],'entry':{lang:entry_url(x['id'],lang) for lang in ['ja','en']},'input':x['execution']['inputs']['url'],'reference_type':x['execution'].get('reference_type')} for x in execution_examples]}
(dest/'index.json').write_text(json.dumps(public,ensure_ascii=False,indent=2)+'\n')
path=ATLAS/'sitemap.xml';xml=ET.parse(path);root=xml.getroot();ns='{http://www.sitemaps.org/schemas/sitemap/0.9}'
if ORIGIN+URL not in {x.text for x in root.findall('.//{*}loc')}:ET.SubElement(ET.SubElement(root,ns+'url'),ns+'loc').text=ORIGIN+URL
ET.register_namespace('',ns[1:-1]);xml.write(path,encoding='utf-8',xml_declaration=True)
guide=ROOT/'llms.txt';text=guide.read_text()
text=re.sub(r'^- \[Equation/model index\].*\n?','',text,flags=re.M)
line=f'- [Equation/model index]({ORIGIN}{URL}): {len(execution_examples)} scoped fixed-input example formulas with direct execution links, separately from all {len(records)} shared model entries with scoped local-example/literature-only status; biological model links resolve to their verified common or supplemental cases without adding physical problems. Machine-readable records are at {ORIGIN}{URL}index.json.\n'
guide.write_text(text.rstrip()+'\n'+line)
print('Built complete equation/model index:',len(records),'entries;',dict(status_counts))
