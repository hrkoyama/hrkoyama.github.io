#!/usr/bin/env python3
"""Retain the bilingual public purpose statement through upstream site imports."""
from pathlib import Path
import hashlib
import html
import json
import re
import subprocess
from atlas_depth import depth_teaser, depth_assets
from atlas_crossovers import crossover_teaser, crossover_assets
from atlas_execution_discovery import load_discovery, entry_url, ENTRY_BASE
from atlas_goal_availability import goal_label, goal_attributes, goal_filter_controls, goal_filter_assets

def home_collection_inventory(root):
    """Count existing lists, without running solvers or duplicating their data."""
    root=Path(root);atlas=root/'numerical-methods-atlas'
    paths=['numerical-methods-atlas/coverage.json','numerical-methods-atlas/references.json','numerical-methods-atlas/methods/index.json','numerical-methods-atlas/solutions/index.json','catalog/atlas-reading-index.json','numerical-methods-atlas/gallery/index.json','numerical-methods-atlas/equations/index.json']
    data={path:json.loads((root/path).read_text()) for path in paths}
    counts=data[paths[0]]['counts'];references=data[paths[1]];methods=data[paths[2]]['methods'];solutions=data[paths[3]];groups=data[paths[4]]['groups']
    publications=data[paths[0]]['publications'];types={row['id']:row['type'] for row in publications}
    assert len(types)==len(publications) and set(types)<=set(row['id'] for row in references)
    assert counts['papers']==sum(kind in ['article','inproceedings'] for kind in types.values())
    assert counts['books']==sum(kind=='book' for kind in types.values())
    assert len({row['id'] for row in methods})==len(methods) and len({row['id'] for row in groups})==len(groups)
    kinds=solutions['counts'];assert set(kinds)=={'analytic','manufactured','semi-analytic','numerical-reference'}
    assert solutions['count']==len(solutions['cases'])==sum(kinds.values())
    assert all(kinds[kind]==sum(row['kind']==kind for row in solutions['cases']) for kind in kinds)
    assert counts['test_problems']==len(data[paths[5]]['items']) and counts['equations']==len(data[paths[6]]['equations'])
    result={key:counts[key] for key in ['papers','books','test_problems','equations']}
    result.update(methods=len(methods),solutions=solutions['count'],reading_groups=len(groups))
    assert all(type(value) is int and value>0 for value in result.values())
    return {'counts':result,'solution_kinds':kinds,'source_sha256':{path:hashlib.sha256((root/path).read_bytes()).hexdigest() for path in paths}}

ROOT=Path(__file__).resolve().parents[1]
ATLAS=ROOT/'numerical-methods-atlas'
copy=json.loads((ROOT/'catalog/atlas-purpose.json').read_text())
crossovers=json.loads((ROOT/'catalog/atlas-crossovers.json').read_text())
policy=json.loads((ROOT/'catalog/atlas-methods.json').read_text())['editorial_policy']
coverage=json.loads((ATLAS/'coverage.json').read_text())
discovery=load_discovery(ROOT)
discovery_by_id={x['id']:x for x in discovery['examples']}
format_counts={**coverage['counts'],'execution_examples':len(discovery['examples']),'gallery_runnable_problems':json.loads((ATLAS/'gallery/index.json').read_text())['counts']['runnable_problems']}
home=json.loads((ROOT/'catalog/atlas-home.json').read_text())
goals=json.loads((ROOT/'catalog/atlas-goals.json').read_text())
(ATLAS/'atlas-home-data.js').write_text('// Generated from catalog/atlas-home.json; navigation copy only.\nexport const homeLandingCopy='+json.dumps(home['landing'],ensure_ascii=False)+';\nexport const homeCollectionInventory='+json.dumps(home_collection_inventory(ROOT),ensure_ascii=False)+';\nexport const homeNavigationData='+json.dumps({'goalDomains':[x['id'] for x in goals['domains']]},ensure_ascii=False)+';\n')
# Reading links follow the editions that actually exist, including new chapters.
reading_languages={}
for language in ['ja','en']:
    for path in (ATLAS/language/'read').glob('*/index.html'):
        reading_languages.setdefault(path.parent.name,[]).append(language)
home_data=ATLAS/'home-overview-data.js'
source=re.sub(r'export const homeReadingLanguages = \{.*?\};', 'export const homeReadingLanguages = '+json.dumps(dict(sorted(reading_languages.items())),ensure_ascii=False,indent=2)+';', home_data.read_text(),flags=re.S)
home_data.write_text(source)
map_fallback=json.loads(subprocess.check_output(['node','scripts/render-atlas-home-map.mjs'],cwd=ROOT,text=True))
def validation_teaser(lang):
    ja=lang=='ja'
    config=json.loads((ROOT/'catalog/atlas-depth-expansion.json').read_text())
    receipts=[json.loads((ROOT/'code/validated-examples'/g.get('edition',config['edition'])/g['id']/'verification.json').read_text()) for g in config['groups']]
    assert all(r['passed'] and r['all_cases_rerun'] for r in receipts)
    cases=sum(len(r['case_ids']) for r in receipts);tests=sum(r['passed_tests'] for r in receipts)
    title='6分野の小さな実装・検証例' if ja else 'Small validated examples across six fields'
    text=(f'{cases}固定ケース・{len(receipts)}配布版・{tests}自動検査。基盤手法、確率、生物、温度制御、粒子・輸送、流体・MHDを、条件・参照・収束とともにたどれます。' if ja else f'{cases} fixed cases, {len(receipts)} supplements and {tests} automated tests. Explore foundations, stochastic models, biology, thermostats, particles/transport and fluid/MHD with conditions, references and refinement.')
    return '<section class="page-width atlas-purpose" aria-labelledby="small-validation-'+lang+'"><h2 id="small-validation-'+lang+'">'+title+'</h2><p>'+text+'</p><p><a href="/numerical-methods-atlas/validation/?lang='+lang+'">'+(f'{cases}例の結果・コード・テストと進捗を見る' if ja else f'See the {cases} results, code, tests and progress')+'</a></p></section>'

def goal_start(lang, static=False):
    data=json.loads((ROOT/'catalog/atlas-goals.json').read_text())
    c=data['home'][lang];ja=lang=='ja'
    methods={m['id']:m for m in json.loads((ATLAS/'methods/index.json').read_text())['methods']}
    cards=''.join('<a class="home-goal-choice"'+goal_attributes(g,methods)+' href="/numerical-methods-atlas/start/?lang='+lang+'#'+g['id']+'-'+lang+'"><span>'+html.escape(g['title'][lang])+'</span><small>'+html.escape(goal_label(g,methods,lang))+'</small></a>' for g in data['goals'])
    c={**c,'all':c['all'].format(count=len(data['goals']))}
    map_url='#atlas-map-'+lang if static else '#/?section=atlas-map'
    crossover_action='<a href="/numerical-methods-atlas/connections/?lang='+lang+'"><strong>'+html.escape(crossovers['home']['action'][lang])+'</strong><span>'+html.escape(crossovers['home']['short_description'][lang])+'</span></a>'
    return '<section class="intro page-width goal-first-intro" data-goal-filter-root data-goal-language="'+lang+'"><div><p class="eyebrow">'+'NaN'+'</p><h1>'+html.escape(c['title'])+'</h1><p class="intro-description">'+html.escape(c['description'])+'</p><p class="home-crossover-entry">'+crossover_action+'</p>'+goal_filter_controls(lang,'home',data['domains'])+'<nav class="home-goal-start" aria-label="'+html.escape(c['label'])+'">'+cards+'</nav><p class="home-goal-all"><a href="/numerical-methods-atlas/start/?lang='+lang+'">'+html.escape(c['all'])+'</a></p><nav class="home-primary-actions" aria-label="'+('ほかの探し方' if ja else 'Other ways to explore')+'"><a class="home-map-action" href="'+map_url+'">'+('分野地図から探す' if ja else 'Browse the field map')+'</a><a class="home-run-action" href="'+ENTRY_BASE+'?lang='+lang+'">'+('22の実行例を見る' if ja else 'See 22 runnable examples')+'</a><a href="/search/?lang='+lang+'&amp;scope=atlas">'+('手法名で検索' if ja else 'Search by method name')+'</a></nav><p class="home-share-link"><a href="/numerical-methods-atlas/share/?lang='+lang+'">'+('紹介文・共有素材' if ja else 'Introduction and sharing materials')+'</a></p>'+depth_teaser(ROOT,lang)+'</div></section>'+validation_teaser(lang)+'<section class="page-width crossover-home">'+crossover_teaser(ROOT,lang)+'</section>'

def browse(lang):
    c=copy[lang]
    routes={'words':'/search/?lang='+lang,'equations':'/numerical-methods-atlas/equations/?lang='+lang,'pictures':'/numerical-methods-atlas/gallery/?lang='+lang}
    previews={'words':'<span aria-hidden="true">Aa / あ</span>','equations':'<span aria-hidden="true">∇²u = f</span>','pictures':'<img src="/numerical-methods-atlas/assets/field-fem-poisson.png" alt="" width="900" height="360" loading="lazy">'}
    cards=[]
    for x in c['browse']:
        attr=' data-atlas-word-search' if x['id']=='words' else ''
        cards.append('<a class="atlas-way" href="'+routes[x['id']]+'"'+attr+'><div class="atlas-way-preview '+('formula' if x['id']=='equations' else '')+'">'+previews[x['id']]+'</div><h3>'+html.escape(x['title'])+'</h3><p>'+html.escape(x['description'].format(**format_counts))+'</p><span class="atlas-way-arrow">'+html.escape(x['action'])+'</span></a>')
    return '<section class="page-width atlas-ways" aria-labelledby="atlas-ways-'+lang+'"><h2 id="atlas-ways-'+lang+'">'+html.escape(c['browse_title'])+'</h2><div class="atlas-way-grid">'+''.join(cards)+'</div></section>'
def metrics(lang):
    counts=coverage['counts'];c=copy[lang]['metrics']
    routes={key:'/numerical-methods-atlas/?lang='+lang+value for key,value in {'methods':'#/coverage?kind=method','papers':'#/references','equations':'#/coverage?kind=equation'}.items()}
    routes['test_problems']='/numerical-methods-atlas/test-cases/?lang='+lang
    result='<div class="summary-counts atlas-metrics">'
    for key in ['methods','papers','equations','test_problems']:
        result+='<a href="'+routes[key]+'"><strong>'+str(counts[key])+'</strong><span>'+html.escape(c[key]['label'])+'</span><small>'+html.escape(c[key]['note'].format(**counts))+'</small></a>'
    return result+'</div>'
def render(lang):
    c=copy[lang]
    links=[('/numerical-methods-atlas/methods/',c['map']),('/numerical-methods-atlas/code-and-data/',c['code']),('/using/',c['using']),('/numerical-methods-atlas/share/',c['share'])]
    return browse(lang)+'<section class="page-width atlas-purpose" aria-labelledby="atlas-purpose-title-'+lang+'"><h2 id="atlas-purpose-title-'+lang+'">'+html.escape(c['title'])+'</h2>'+''.join('<p>'+html.escape(p)+'</p>' for p in c['paragraphs'])+'<details><summary>'+html.escape(c['scope_toggle'])+'</summary><p>'+html.escape(c['status_note'])+'</p><p><strong>'+html.escape(policy['title'][lang])+':</strong> '+html.escape(policy['statement'][lang])+'</p></details><nav aria-label="Atlas resources">'+''.join('<a href="'+url+'?lang='+lang+'">'+html.escape(label)+'</a>' for url,label in links)+'</nav></section>'

def featured(lang):
    ja=lang=='ja'
    title='固定入力から、まず3つの計算を試す' if ja else 'Start with three fixed-input calculations'
    names={'poisson-2d-sine':('Poisson：解法と誤差','Poisson: solvers and errors'),'barnes-hut':('Barnes–Hut：近似力の精度','Barnes–Hut: approximate forces'),'helium-ground-state':('H・He：原子の計算','H / He: atomic calculations')}
    body='<section class="page-width atlas-featured-examples" aria-labelledby="atlas-examples-'+lang+'"><h2 id="atlas-examples-'+lang+'">'+title+'</h2><ul>'
    for ident in ['poisson-2d-sine','barnes-hut','helium-ground-state']:
        item=discovery_by_id[ident]
        outcome=item['outcome'][lang]
        if ident=='helium-ground-state':outcome='Hの解析解比較と、Heの閉殻HF・交換のみLDAを試す。' if ja else 'Compare H with analytic states and try closed-shell HF / exchange-only LDA for He.'
        body+='<li data-featured-example="'+ident+'"><h3>'+html.escape(names[ident][0 if ja else 1])+'</h3><p>'+html.escape(outcome)+'</p><a href="'+entry_url(ident,lang)+'">'+('入力・実行・検証へ' if ja else 'Input, execution and checks')+'</a>'
        if ident=='helium-ground-state':body+=' · <a href="'+entry_url('hydrogenic-atoms',lang)+'">'+('水素型原子' if ja else 'Hydrogenic atoms')+'</a>'
        body+='</li>'
    return body+'</ul><p><a href="'+ENTRY_BASE+'?lang='+lang+'">'+('代表22問題をすべて見る' if ja else 'See all 22 representative examples')+'</a></p></section>'

sections={lang:render(lang) for lang in copy}
module=ATLAS/'atlas-purpose.js'
module.write_text("// Generated from atlas purpose, coverage and verified execution discovery.\nimport {currentLanguage} from './i18n.js';\nconst sections="+json.dumps(sections,ensure_ascii=False)+";\nconst metrics="+json.dumps({lang:metrics(lang) for lang in copy},ensure_ascii=False)+";\nexport const atlasPurpose=()=>sections[currentLanguage()];\nexport const atlasMetrics=()=>metrics[currentLanguage()];\nconst featured="+json.dumps({lang:featured(lang) for lang in copy},ensure_ascii=False)+";\nexport const atlasExamples=()=>featured[currentLanguage()];\nconst goalStarts="+json.dumps({lang:goal_start(lang) for lang in copy},ensure_ascii=False)+";\nexport const atlasGoalStart=()=>goalStarts[currentLanguage()];\n")
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()[:12]
from atlas_home_layout import build_home_layout
build_home_layout(ROOT,copy,sections,{l:metrics(l) for l in copy},{l:featured(l) for l in copy},map_fallback,{l:depth_teaser(ROOT,l)+validation_teaser(l)+'<section class=\"page-width crossover-home\">'+crossover_teaser(ROOT,l)+'</section>' for l in copy})
overview=ATLAS/'home-overview.js'
app=ATLAS/'app.js'
page=ATLAS/'index.html'
text=page.read_text()
titles={lang:home['landing'][lang]['title'] for lang in ['ja','en']}
text=re.sub(r'<title(?:\s[^>]*)?>.*?</title>','<title data-page-title-ja="'+titles['ja']+'" data-page-title-en="'+titles['en']+'">'+titles['en']+'</title>',text,count=1,flags=re.S)
text=re.sub(r'<meta name="description"[^>]*>','<meta name="description" data-description-ja="'+html.escape(copy['ja']['meta_description'],quote=True)+'" data-description-en="'+html.escape(copy['en']['meta_description'],quote=True)+'" content="'+html.escape(copy['en']['meta_description'],quote=True)+'">',text,count=1)
text=re.sub(r'<meta (?:property|name)="(?:og:(?:title|description|image(?::(?:width|height|type|alt))?|locale(?::alternate)?)|twitter:[^"]+)"[^>]*>\s*','',text)
share_image='https://hrkoyama.github.io/numerical-methods-atlas/share/atlas-intro-ja.png'
social={
    'og:title':titles['en'],'og:description':copy['en']['meta_description'],
    'og:image':share_image,'og:image:width':'1200','og:image:height':'630','og:image:type':'image/png',
    'og:image:alt':'数値計算法アトラス / An Atlas of Numerical Methods: methods, conditions, code and result checks',
    'og:locale':'ja_JP','og:locale:alternate':'en_US',
    'twitter:card':'summary_large_image','twitter:title':titles['en'],
    'twitter:description':copy['en']['meta_description'],'twitter:image':share_image,
    'twitter:image:alt':'数値計算法アトラス / An Atlas of Numerical Methods'}
text=text.replace('</head>',''.join('<meta '+('name' if key.startswith('twitter:') else 'property')+'="'+key+'" content="'+html.escape(value,quote=True)+'">\n' for key,value in social.items())+'</head>')
text=re.sub(r'src="app.js(?:[?]v=[a-f0-9]+)?"','src="app.js?v='+digest(app)+'"',text)
page.write_text(text)
# Keep the older roadmap wording consistent in both static and runtime editions.
replacements={
 '著者の要望によりAMRは保留で、今回の拡張に含みません。':'収録方針によりAMRは対象外です。',
 'AMRも引き続き保留します。':'AMRは収録対象外です。',
 'AMR is deferred at the author’s request; it is not part of this expansion.':'AMR is outside the editorial scope.',
 'and AMR remains deferred.':'and AMR is outside the editorial scope.'
}
def adapt_roadmap(text,lang):
    for old,new in replacements.items():text=text.replace(old,new)
    text=re.sub(r'<!-- atlas-scope -->.*?<!-- /atlas-scope -->','',text,flags=re.S)
    block='<!-- atlas-scope --><section><h2 id="atlas-editorial-scope">'+html.escape(policy['title'][lang])+'</h2><p>'+html.escape(policy['statement'][lang])+'</p></section><!-- /atlas-scope -->'
    return re.sub(r'(</h1>)',lambda m:m.group(1)+block,text,count=1)
for lang in ['ja','en']:
    roadmap=ATLAS/lang/'read/roadmap/index.html';roadmap.write_text(adapt_roadmap(roadmap.read_text(),lang))
for content in ATLAS.glob('content*.json'):
    data=json.loads(content.read_text());lang='ja' if '.ja.' in content.name else 'en'
    data['roadmap']['html']=adapt_roadmap(data['roadmap']['html'],lang)
    content.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n')
# A newly added chapter must also be discoverable through existing #/read links
# when a returning browser has a cached language document bundle.
from atlas_runtime_assets import build_atlas_runtime
build_atlas_runtime(ROOT)
text=page.read_text();text=re.sub(r'src="app.js(?:[?]v=[a-f0-9]+)?"','src="app.js?v='+digest(app)+'"',text);page.write_text(text)
guide=ROOT/'llms.txt';text=re.sub(r'^- \[Atlas introduction and sharing\].*\n?','',guide.read_text(),flags=re.M)
guide.write_text(text.rstrip()+'\n- [Atlas introduction and sharing](https://hrkoyama.github.io/numerical-methods-atlas/share/): Bilingual first-visit explanation, eight-area map and reading paths on /numerical-methods-atlas/explore/, and shareable introduction text and PNG/SVG cards. [Sharing metadata / JSON](https://hrkoyama.github.io/numerical-methods-atlas/share/sharing.json) derives counts from the existing catalogs. Introductory materials have their own limited sharing terms; scientific records and verification scope are unchanged.\n')
print('Built concise bilingual atlas landing and separate reading directory.')

text=re.sub(r'^- \[Cross-field connections\].*\n?','',guide.read_text(),flags=re.M)
guide.write_text(text.rstrip()+'\n- [Cross-field connections](https://hrkoyama.github.io/numerical-methods-atlas/connections/): bilingual routes from DFT to first-principles MD and thermostats, reaction–diffusion to biology and fluids, and Poisson operators to pressure, Hartree and gravity. Shared mathematics, transferred quantities and distinct validation requirements are explicit; component examples do not establish a validated coupled pipeline. Canonical metadata: /catalog/atlas-crossovers.json.\n')

guide=ROOT/'llms.txt';text=guide.read_text();text=re.sub(r'^- \[Small cross-field validation supplements\].*\n?','',text,flags=re.M)
supplement_index=json.loads((ATLAS/'validation/index.json').read_text())
supplement_tests=sum(group['passed_tests'] for group in supplement_index['groups'])
guide.write_text(text.rstrip()+f"\n- [Small cross-field validation supplements](https://hrkoyama.github.io/numerical-methods-atlas/validation/): {supplement_index['case_count']} fixed cases in {len(supplement_index['groups'])} independently extracted releases; {supplement_tests} automated tests, bilingual assumptions, adopted algorithms, primary sources, measured refinement and scope. Lightweight public-only Linux CI; separate from the shared 22-case detailed registry.\n")

text=guide.read_text()
browse_links=[
    ('Reference solution index', 'solutions/', 'Saved analytic, semi-analytic, manufactured and finite-grid numerical references, with defining formulas, assumptions, uncertainty and links to their displays. JSON and Markdown: solutions/index.json and solutions/index.md.'),
    ('Visual test-problem index', 'gallery/', 'Every published test problem by name and saved figure, with separate image provenance and execution evidence. JSON: gallery/index.json.'),
    ('Problem hub registry', 'problems/index.json', 'Every visual problem links to a bilingual hub with scoped equations, references, methods, verified execution examples and existing code evidence. Per-problem HTML, index.json and index.md live under problems/{id}/.'),
    ('Equation and model index', 'equations/', 'Current representative equations and models, linked to their scope, explanations and existing execution examples. JSON: equations/index.json.'),
]
for label, path, description in browse_links:
    text=re.sub(r'^- \['+re.escape(label)+r'\].*\n?', '', text, flags=re.M)
for label, path, description in browse_links:
    text=text.rstrip()+'\n- ['+label+'](https://hrkoyama.github.io/numerical-methods-atlas/'+path+'): '+description+'\n'
guide.write_text(text)
