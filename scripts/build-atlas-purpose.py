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

ROOT=Path(__file__).resolve().parents[1]
ATLAS=ROOT/'numerical-methods-atlas'
copy=json.loads((ROOT/'catalog/atlas-purpose.json').read_text())
crossovers=json.loads((ROOT/'catalog/atlas-crossovers.json').read_text())
policy=json.loads((ROOT/'catalog/atlas-methods.json').read_text())['editorial_policy']
coverage=json.loads((ATLAS/'coverage.json').read_text())
discovery=load_discovery(ROOT)
discovery_by_id={x['id']:x for x in discovery['examples']}
format_counts={**coverage['counts'],'execution_examples':len(discovery['examples'])}
map_fallback=json.loads(subprocess.check_output(['node','scripts/render-atlas-home-map.mjs'],cwd=ROOT,text=True))
def goal_start(lang, static=False):
    data=json.loads((ROOT/'catalog/atlas-goals.json').read_text())
    c=data['home'][lang];ja=lang=='ja'
    methods={m['id']:m for m in json.loads((ATLAS/'methods/index.json').read_text())['methods']}
    cards=''.join('<a class="home-goal-choice"'+goal_attributes(g,methods)+' href="/numerical-methods-atlas/start/?lang='+lang+'#'+g['id']+'-'+lang+'"><span>'+html.escape(g['title'][lang])+'</span><small>'+html.escape(goal_label(g,methods,lang))+'</small></a>' for g in data['goals'])
    c={**c,'all':c['all'].format(count=len(data['goals']))}
    map_url='#atlas-map-'+lang if static else '#/?section=atlas-map'
    crossover_action='<a href="/numerical-methods-atlas/connections/?lang='+lang+'"><strong>'+html.escape(crossovers['home']['action'][lang])+'</strong><span>'+html.escape(crossovers['home']['short_description'][lang])+'</span></a>'
    return '<section class="intro page-width goal-first-intro" data-goal-filter-root data-goal-language="'+lang+'"><div><p class="eyebrow">'+('数値計算法アトラス' if ja else 'An Atlas of Numerical Methods')+'</p><h1>'+html.escape(c['title'])+'</h1><p class="intro-description">'+html.escape(c['description'])+'</p><p class="home-crossover-entry">'+crossover_action+'</p>'+goal_filter_controls(lang,'home',data['domains'])+'<nav class="home-goal-start" aria-label="'+html.escape(c['label'])+'">'+cards+'</nav><p class="home-goal-all"><a href="/numerical-methods-atlas/start/?lang='+lang+'">'+html.escape(c['all'])+'</a></p><nav class="home-primary-actions" aria-label="'+('ほかの探し方' if ja else 'Other ways to explore')+'"><a class="home-map-action" href="'+map_url+'">'+('分野地図から探す' if ja else 'Browse the field map')+'</a><a class="home-run-action" href="'+ENTRY_BASE+'?lang='+lang+'">'+('21の実行例を見る' if ja else 'See 21 runnable examples')+'</a><a href="/search/?lang='+lang+'&amp;scope=atlas">'+('手法名で検索' if ja else 'Search by method name')+'</a></nav><p class="home-share-link"><a href="/numerical-methods-atlas/share/?lang='+lang+'">'+('紹介文・共有素材' if ja else 'Introduction and sharing materials')+'</a></p>'+depth_teaser(ROOT,lang)+'</div></section><section class="page-width crossover-home">'+crossover_teaser(ROOT,lang)+'</section>'

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
    return body+'</ul><p><a href="'+ENTRY_BASE+'?lang='+lang+'">'+('代表21問題をすべて見る' if ja else 'See all 21 representative examples')+'</a></p></section>'

sections={lang:render(lang) for lang in copy}
module=ATLAS/'atlas-purpose.js'
module.write_text("// Generated from atlas purpose, coverage and verified execution discovery.\nimport {currentLanguage} from './i18n.js';\nconst sections="+json.dumps(sections,ensure_ascii=False)+";\nconst metrics="+json.dumps({lang:metrics(lang) for lang in copy},ensure_ascii=False)+";\nexport const atlasPurpose=()=>sections[currentLanguage()];\nexport const atlasMetrics=()=>metrics[currentLanguage()];\nconst featured="+json.dumps({lang:featured(lang) for lang in copy},ensure_ascii=False)+";\nexport const atlasExamples=()=>featured[currentLanguage()];\nconst goalStarts="+json.dumps({lang:goal_start(lang) for lang in copy},ensure_ascii=False)+";\nexport const atlasGoalStart=()=>goalStarts[currentLanguage()];\n")
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()[:12]
overview=ATLAS/'home-overview.js';text=overview.read_text()
text=re.sub(r"from './home-overview-data[.]js(?:[?]v=[a-f0-9]+)?'","from './home-overview-data.js?v="+digest(ATLAS/'home-overview-data.js')+"'",text)
text=re.sub(r"import \{atlasPurpose[^}]*\} from './atlas-purpose[.]js(?:[?]v=[a-f0-9]+)?';\n?",'',text)
marker=' ${homeSearchPage()}'
text=re.sub(r'^[ \t]*\$\{atlasPurpose\(\)\}[ \t]*\n(?:[ \t]*\n)*','',text,flags=re.M)
text=re.sub(r'^[ \t]*\$\{atlasExamples\(\)\}[ \t]*\n(?:[ \t]*\n)*','',text,flags=re.M)
assert text.count(marker)==1,'Review upstream homepage layout before adapting'
text="import {atlasPurpose,atlasMetrics,atlasExamples,atlasGoalStart} from './atlas-purpose.js?v="+digest(module)+"';\n"+text.replace(marker,' ${atlasPurpose()}\n'+marker+'\n ${atlasExamples()}\n')
if '${atlasMetrics()}' not in text:
    text,count=re.subn(r'<div class="summary-counts">.*?</div><p class="flow">','${atlasMetrics()}<p class="flow">',text,count=1)
    assert count==1,'Review upstream coverage presentation'
filter_version=digest(ATLAS/'goal-filters.mjs')
text=re.sub(r"import \{wireGoalFilters\} from './goal-filters[.]mjs(?:[?]v=[a-f0-9]+)?';\n?",'',text)
text="import {wireGoalFilters} from './goal-filters.mjs?v="+filter_version+"';\n"+text
overview.write_text(text)
app=ATLAS/'app.js';text=app.read_text()
text,count=re.subn(r"from './home-overview[.]js(?:[?]v=[a-f0-9]+)?'","from './home-overview.js?v="+digest(overview)+"'",text)
assert count==1,'Review upstream homepage module import'
app.write_text(text)
page=ATLAS/'index.html';text=page.read_text()
text=re.sub(r'<!-- atlas-purpose-fallback -->.*?<!-- /atlas-purpose-fallback -->','',text,flags=re.S)
text=re.sub(r'<!-- atlas-intro-fallback -->.*?<!-- /atlas-intro-fallback -->','',text,flags=re.S)
text=re.sub(r'(<main\b[^>]*>)\s*<section class="page-intro page-width">.*?</section>',r'\1',text,count=1,flags=re.S)
intro='<!-- atlas-intro-fallback -->'+''.join('<div class="home-overview" data-site-language="'+lang+'" lang="'+lang+'">'+goal_start(lang,True)+'</div>' for lang in copy)+'<!-- /atlas-intro-fallback -->'
fallback='<!-- atlas-purpose-fallback -->'+''.join('<div class="home-overview atlas-static" data-site-language="'+lang+'" lang="'+lang+'"><section class="page-width">'+metrics(lang)+'</section>'+sections[lang]+featured(lang)+map_fallback[lang]+'</div>' for lang in copy)+'<!-- /atlas-purpose-fallback -->'
text=re.sub(r'(<main\b[^>]*>)',lambda m:m[1]+intro,text,count=1)
text=text.replace('</main>',fallback+'</main>')
text=re.sub(r'<link rel="stylesheet" href="/styles/atlas-goal-filters[.]css[^"]*">\n?','',text)
text=re.sub(r'<script type="module" src="/numerical-methods-atlas/goal-filters[.]mjs[^"]*"></script>\n?','',text)
text=re.sub(r'<link rel="stylesheet" href="/styles/atlas-depth[.]css[^"]*">\n?','',text)
text=re.sub(r'<link rel="stylesheet" href="/styles/atlas-crossovers[.]css[^"]*">\n?','',text)
text=text.replace('</head>',goal_filter_assets(ROOT)+depth_assets(ROOT)+crossover_assets(ROOT)+'</head>')
text=re.sub(r'href="home-overview.css(?:[?]v=[a-f0-9]+)?"','href="home-overview.css?v='+digest(ATLAS/'home-overview.css')+'"',text)
text=re.sub(r'<link rel="stylesheet" href="/styles/atlas-purpose.css(?:[?]v=[a-f0-9]+)?">\n?','',text)
text=text.replace('</head>','<link rel="stylesheet" href="/styles/atlas-purpose.css?v='+digest(ROOT/'styles/atlas-purpose.css')+'">\n</head>')
text=re.sub(r'<link rel="stylesheet" href="/styles/atlas-discovery.css(?:[?]v=[a-f0-9]+)?">\n?','',text)
text=text.replace('</head>','<link rel="stylesheet" href="/styles/atlas-discovery.css?v='+digest(ROOT/'styles/atlas-discovery.css')+'">\n</head>')
titles={'ja':'数値計算法アトラス','en':'An Atlas of Numerical Methods'}
text=re.sub(r'<title(?:\s[^>]*)?>.*?</title>','<title data-page-title-ja="'+titles['ja']+'" data-page-title-en="'+titles['en']+'">'+titles['ja']+' | '+titles['en']+'</title>',text,count=1,flags=re.S)
text=re.sub(r'<meta name="description"[^>]*>','<meta name="description" data-description-ja="'+html.escape(copy['ja']['meta_description'],quote=True)+'" data-description-en="'+html.escape(copy['en']['meta_description'],quote=True)+'" content="'+html.escape(copy['en']['meta_description'],quote=True)+'">',text,count=1)
text=re.sub(r'<meta (?:property|name)="(?:og:(?:title|description|image(?::(?:width|height|type|alt))?|locale(?::alternate)?)|twitter:[^"]+)"[^>]*>\s*','',text)
share_image='https://hrkoyama.github.io/numerical-methods-atlas/share/atlas-intro-ja.png'
social={
    'og:title':titles['ja']+' | '+titles['en'],'og:description':copy['en']['meta_description'],
    'og:image':share_image,'og:image:width':'1200','og:image:height':'630','og:image:type':'image/png',
    'og:image:alt':'数値計算法アトラス / An Atlas of Numerical Methods: methods, conditions, code and result checks',
    'og:locale':'ja_JP','og:locale:alternate':'en_US',
    'twitter:card':'summary_large_image','twitter:title':titles['ja']+' | '+titles['en'],
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
versions={lang:digest(ATLAS/('content.'+lang+'.json')) for lang in ['ja','en']}
text=app.read_text()
text=re.sub(r'const atlasIntroDescriptions = [^\n]+;\n','',text)
text='const atlasIntroDescriptions = '+json.dumps({lang:copy[lang]['meta_description'] for lang in copy},ensure_ascii=False)+';\n'+text
text,count=re.subn(r"const description = (?:currentLanguage\(\)==='ja' \? [^\n]+|atlasIntroDescriptions\[currentLanguage\(\)\]);",'const description = atlasIntroDescriptions[currentLanguage()];',text,count=1)
assert count==1,'Review upstream description handling'
anchor=" document.querySelector('meta[property=\"og:title\"]').content=site.title[currentLanguage()];"
social_line=" // atlas-social-locale\n for(const key of ['twitter:title','twitter:description'])document.querySelector('meta[name=\"'+key+'\"]').content=key==='twitter:title'?site.title[currentLanguage()]:description;\n document.querySelector('meta[property=\"og:image\"]').content=new URL('share/atlas-intro-'+currentLanguage()+'.png',import.meta.url).href;\n document.querySelector('meta[name=\"twitter:image\"]').content=new URL('share/atlas-intro-'+currentLanguage()+'.png',import.meta.url).href;\n // /atlas-social-locale"
text=re.sub(r'\n // atlas-social-locale\n.*?\n // /atlas-social-locale','',text,flags=re.S)
assert text.count(anchor)==1
text=text.replace(anchor,anchor+'\n'+social_line)
text=re.sub(r"'locales/messages.json(?:[?]v=[a-f0-9]+)?'","'locales/messages.json?v="+digest(ATLAS/'locales/messages.json')+"'",text)
text=re.sub(r'const atlasDocumentVersions = [^\n]+;\n','',text)
text=text.replace('const documentCache = new Map();','const atlasDocumentVersions = '+json.dumps(versions)+';\nconst documentCache = new Map();')
text=text.replace('fetch(`content.${language}.json`)','fetch(`content.${language}.json?v=${atlasDocumentVersions[language]}`)')
assert 'fetch(`content.${language}.json?v=${atlasDocumentVersions[language]}`)' in text
app.write_text(text)
text=page.read_text();text=re.sub(r'src="app.js(?:[?]v=[a-f0-9]+)?"','src="app.js?v='+digest(app)+'"',text);page.write_text(text)
guide=ROOT/'llms.txt';text=re.sub(r'^- \[Atlas introduction and sharing\].*\n?','',guide.read_text(),flags=re.M)
guide.write_text(text.rstrip()+'\n- [Atlas introduction and sharing](https://hrkoyama.github.io/numerical-methods-atlas/share/): Bilingual first-visit explanation, eight-area map in the homepage static text, and shareable introduction text and PNG/SVG cards. [Sharing metadata / JSON](https://hrkoyama.github.io/numerical-methods-atlas/share/sharing.json) derives counts from the existing catalogs. Introductory materials have their own limited sharing terms; scientific records and verification scope are unchanged.\n')
print('Built bilingual atlas purpose statement for the live homepage and static fallback.')

text=re.sub(r'^- \[Cross-field connections\].*\n?','',guide.read_text(),flags=re.M)
guide.write_text(text.rstrip()+'\n- [Cross-field connections](https://hrkoyama.github.io/numerical-methods-atlas/connections/): bilingual routes from DFT to first-principles MD and thermostats, reaction–diffusion to biology and fluids, and Poisson operators to pressure, Hartree and gravity. Shared mathematics, transferred quantities and distinct validation requirements are explicit; component examples do not establish a validated coupled pipeline. Canonical metadata: /catalog/atlas-crossovers.json.\n')
