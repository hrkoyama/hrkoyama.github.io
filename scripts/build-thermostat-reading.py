#!/usr/bin/env python3
"""Build bilingual thermostat comparisons from verified frozen supplements.

The CSVR expansion is enabled only after all three new cases resolve to
successful immutable releases. This documentation build runs no sampler.
"""
from pathlib import Path
import hashlib
import html
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from atlas_goal_availability import load_supplemental_examples

ROOT=Path(__file__).resolve().parents[1]
ATLAS=ROOT/'numerical-methods-atlas'
ORIGIN='https://hrkoyama.github.io'
methods=[x for x in json.loads((ROOT/'catalog/atlas-methods.json').read_text())['methods'] if x['group']['id']=='thermostats']
field=next(x for x in json.loads((ROOT/'catalog/atlas-depth.json').read_text())['fields'] if x['id']=='temperature')
supplements=load_supplemental_examples(ROOT,field.get('supplemental_examples',[]))
comparison_path=ROOT/'catalog/atlas-thermostat-comparison.json'
comparison=json.loads(comparison_path.read_text())
selected_ids={item['id'] for item in supplements}
comparison_ids=set(comparison['case_ids'])
assert not comparison_ids.intersection(selected_ids) or comparison_ids <= selected_ids, 'Partial CSVR comparison evidence'
comparison_enabled=comparison_ids <= selected_ids
if comparison_enabled:
    assert {item['group'] for item in supplements if item['id'] in comparison_ids}=={'thermostats'}
    implemented={item['id'] for item in methods if item['status']=='educational-example'}
    assert implemented=={'langevin-thermostat','stochastic-velocity-rescaling'}, 'Do not promote other thermostat families'
    rendered=json.loads(subprocess.check_output(['node','scripts/render-atlas-math.cjs'],cwd=ROOT,
        input=json.dumps([{'id':key,'formula':[tex]} for key,tex in comparison['formulas'].items()]).encode()))['rendered']
else:
    rendered={}
esc=html.escape
version=hashlib.sha256((ROOT/'styles/atlas-resources.css').read_bytes()).hexdigest()[:12]
intro={
 'ja':('サーモスタット：温度制御と分布の比較','温度の平均だけでなく、揺らぎ・エルゴード性・時間相関を比べる。Nosé–Hoover、速度スケーリングから確率的・運動量保存型の手法まで。'),
 'en':('Thermostats: temperature control and distributions','Compare fluctuations, ergodicity and time correlations as well as mean temperature, from Nosé–Hoover and velocity rescaling to stochastic and momentum-conserving methods.')
}
paragraphs={
 'ja':[
  ('temperature','何の温度を制御するか','運動エネルギーをK、有効自由度数をfとすると、運動温度は T = 2 K / (f k_B)。拘束や重心運動の除去に応じてfを数え、流れがある場合は熱運動と平均流を区別する。回転自由度を含むかも明記する。'),
  ('fluctuations','同じ平均温度でも分布は違う','古典的な二次形式の運動エネルギーを持つf個の独立な運動量自由度では、正準平衡で 2 K/(k_B T₀) は自由度fのχ²分布。平均Kはf k_B T₀/2、分散はf(k_B T₀)²/2となる。単純な速度スケーリング v ← √(T₀/T) v は適用直後のKを固定し、この揺らぎを再現しない。CSVRは確率的な係数で揺らぎを生成する別の手法である。'),
  ('dynamics','分布の標本化と運動の再現を分ける','正しい不変分布を持っていても、有限時間の軌道が十分に探索するとは限らない。また平衡分布が正しくても、摩擦や衝突で速度自己相関や拡散は変わり得る。有限時間刻みの誤差、熱浴の結合時間、乱数依存性まで含めて評価する。'),
  ('verification','検証済みの範囲と次の課題','調和Langevin BAOABでは位置・運動量・全エネルギーの分布、離散Lyapunov参照、連続Gaussian伝播、刻み依存と時差相関を測定済み。以下は将来の検証案です。非調和振動子・理想気体・小さなLennard–Jones系、結合時間への依存、他の11手法の専用実装へ広げる。Nosé–Hooverには小自由度系で探索が不十分になる例も付ける。'),
 ],
 'en':[
  ('temperature','Define the controlled temperature','With kinetic energy K and f active degrees of freedom, the kinetic temperature is T = 2 K / (f k_B). Count constraints and removed center-of-mass motion consistently, and separate thermal motion from streaming. State whether rotational degrees of freedom are included.'),
  ('fluctuations','Equal mean temperature does not imply equal distributions','For f independent momentum degrees of freedom with classical quadratic kinetic energy, canonical equilibrium gives 2 K/(k_B T₀) a chi-square distribution with f degrees of freedom. Its mean K is f k_B T₀/2 and variance is f(k_B T₀)²/2. Direct rescaling v ← √(T₀/T) v fixes K immediately after application, removing these fluctuations. CSVR instead uses a stochastic factor to generate fluctuations.'),
  ('dynamics','Separate sampling from dynamics','An invariant distribution does not ensure adequate finite-time exploration. Even correct equilibrium sampling can coexist with friction- or collision-induced changes in velocity autocorrelations and diffusion. Assess integration error, heat-bath coupling time and random-seed dependence.'),
  ('verification','Validated scope and next checks','Harmonic Langevin BAOAB now has measured position/momentum/total-energy distributions, an independent discrete-Lyapunov reference, continuous Gaussian propagation, step bias and lagged correlations. Future verification plans include anharmonic oscillators, ideal gases, a small Lennard–Jones system, coupling-time dependence and dedicated implementations of the other 11 methods. Include a small-system example where Nosé–Hoover does not explore adequately.'),
 ]
}

def comparison_section(lang):
    """Render adopted equations and limits, without borrowing future evidence."""
    ja=lang=='ja'
    body='<section id="csvr-comparison"><h2>'+esc(comparison['title'][lang])+'</h2><p>'+esc(comparison['intro'][lang])+'</p>'
    for section in comparison['sections']:
        body+='<section><h3 id="'+section['id']+'">'+esc(section['title'][lang])+'</h3>'
        body+=''.join('<p>'+esc(text)+'</p>' for text in section['paragraphs'][lang])
        body+=''.join('<div class="math-display" data-equation-id="'+ident+'">'+rendered[ident][0]+'</div>' for ident in section['formulas'])
        if section['references']:
            body+='<p>'+('出典：' if ja else 'Sources: ')+' · '.join('<a href="#csvr-source-'+ident+'">'+esc(next(item['title'] for item in comparison['references'] if item['id']==ident))+'</a>' for ident in section['references'])+'</p>'
        body+='</section>'
    body+='<h3>'+('採用式の一次資料と確認範囲' if ja else 'Primary sources for the adopted equations')+'</h3><ol>'
    for item in comparison['references']:
        body+='<li id="csvr-source-'+item['id']+'"><a href="'+esc(item['url'],quote=True)+'">'+esc(item['author']+' ('+str(item['year'])+'). '+item['title'])+'</a>'
        if item.get('doi'):body+=' · <a href="https://doi.org/'+esc(item['doi'],quote=True)+'">DOI: '+esc(item['doi'])+'</a>'
        body+='<p>'+esc(item['review_note'][lang])+'</p></li>'
    return body+'</ol></section>'

def companion_documents(lang,title,description):
    """Static JSON/Markdown preserve the same scope and verified destinations."""
    sources={str(path.relative_to(ROOT)):hashlib.sha256(path.read_bytes()).hexdigest() for path in [comparison_path,ROOT/'catalog/atlas-methods.json',ROOT/'catalog/atlas-depth.json']}
    for item in supplements:sources.update(item['source_sha256'])
    public={'schema_version':1,'reviewed_on':comparison['reviewed_on'],'locale':lang,'title':title,'description':description,
        'comparison_enabled':comparison_enabled,'case_ids':[item['id'] for item in supplements],
        'implemented_method_ids':[item['id'] for item in methods if item['status']=='educational-example'],
        'planned_method_ids':[item['id'] for item in methods if item['status']=='planned'],
        'comparison':comparison if comparison_enabled else None,'field_scope':field['scope'][lang],
        'supplements':supplements,'source_sha256':sources}
    markdown='# '+title+'\n\n'+description+'\n\n'+field['scope'][lang]+'\n\n'
    for _,heading,text in paragraphs[lang][:3]:markdown+='## '+heading+'\n\n'+text+'\n\n'
    if comparison_enabled:
        markdown+='## '+comparison['title'][lang]+'\n\n'+comparison['intro'][lang]+'\n\n'
        for section in comparison['sections']:
            markdown+='### '+section['title'][lang]+'\n\n'+'\n\n'.join(section['paragraphs'][lang])+'\n\n'
            markdown+=''.join('$$\n'+comparison['formulas'][ident]+'\n$$\n\n' for ident in section['formulas'])
        markdown+='## '+('検証済みの範囲と次の課題' if lang=='ja' else 'Validated scope and next checks')+'\n\n'+comparison['verification'][lang]+'\n\n'
        markdown+='## '+('出典と確認範囲' if lang=='ja' else 'Sources and review scope')+'\n\n'+comparison['source_scope'][lang]+'\n\n'
        for item in comparison['references']:markdown+='- '+item['author']+' ('+str(item['year'])+'). '+item['title']+'. '+item['url']+'\n'
        markdown+='\n'
    markdown+='## '+('実行・検証例' if lang=='ja' else 'Execution and validation entries')+'\n\n'
    for item in supplements:
        markdown+='### '+item['title'][lang]+'\n\n'+item['limits'][lang]+'\n\n'
        markdown+='Entry: '+ORIGIN+item['url']+'?lang='+lang+'\nZIP: '+ORIGIN+item['download']+'\nResults: '+ORIGIN+item['results']+'\nReceipt: '+ORIGIN+item['verification']+'\n\n'
    return public,markdown.rstrip()+'\n'

for lang in ['ja','en']:
    ja=lang=='ja';title,description=intro[lang]
    url=f'/numerical-methods-atlas/{lang}/read/thermostats/'
    other='en' if ja else 'ja'
    body='<p class="eyebrow">MOLECULAR DYNAMICS / THERMOSTATS</p><h1>'+esc(title)+'</h1><p class="intro">'+esc(description)+'</p>'
    body+='<p class="resource-summary">'+esc(field['scope'][lang])+'</p>'
    body+='<nav class="resource-nav">'+''.join('<a href="'+u+'"'+(' hreflang="'+other+'"' if '?lang='+other in u else '')+'>'+esc(label)+'</a>' for u,label in [('/numerical-methods-atlas/methods/','手法の見取り図' if ja else 'Method map'),(f'/numerical-methods-atlas/{lang}/read/','解説章の目次' if ja else 'Reading chapters'),(f'/numerical-methods-atlas/{other}/read/thermostats/?lang={other}','English' if ja else '日本語')])+'</nav>'
    body+='<p><a href="index.json">JSON</a> · <a href="index.md">Markdown</a></p>'
    for ident,heading,text in paragraphs[lang][:3]:body+=f'<section><h2 id="{ident}">{esc(heading)}</h2><p>{esc(text)}</p></section>'
    if comparison_enabled:body+=comparison_section(lang)
    body+='<section id="executed-scope"><h2>'+((('CSVR・Langevinの実行・検証例' if ja else 'Runnable CSVR/Langevin validations')) if comparison_enabled else ('調和Langevinの実行・検証例' if ja else 'Runnable harmonic-Langevin validation'))+'</h2><p>'+esc(field['refinement'][lang])+'</p><ul>'
    for item in supplements:
        body+='<li><a href="'+item['url']+'?lang='+lang+'">'+esc(item['title'][lang])+'</a> · <a href="'+item['download']+'">ZIP</a> · <a href="'+item['results']+'">'+('保存結果' if ja else 'Stored results')+'</a> · <a href="'+item['verification']+'">'+('追試記録' if ja else 'Rerun receipt')+'</a><p>'+esc(item['limits'][lang])+'</p></li>'
    body+='</ul></section>'
    for tier in ['basic','advanced']:
        body+='<section><h2 id="'+tier+'">'+({'basic':'基本の8項目','advanced':'発展の4項目'}[tier] if ja else {'basic':'Eight foundational entries','advanced':'Four further entries'}[tier])+'</h2>'
        for x in methods:
            if x['tier']!=tier:continue
            body+='<section><h3 id="'+x['id']+'">'+esc(x['name'][lang])+'</h3><p>'+esc(x['summary'][lang])+'</p><p>'+esc(x['caution'][lang])+'</p><p class="resource-status">'+('別名・表記：' if ja else 'Other names: ')+esc(' / '.join(x['aliases']))+'</p><p><a href="/numerical-methods-atlas/methods/'+x['id']+'/">'+('項目の状況・JSON・Markdown' if ja else 'Method status, JSON and Markdown')+'</a></p><ul>'
            body+=''.join('<li><a href="'+esc(r['url'])+'">'+esc(r['label'])+'</a></li>' for r in x['references'])+'</ul></section>'
        body+='</section>'
    ident,heading,text=paragraphs[lang][-1]
    if comparison_enabled:text=comparison['verification'][lang]
    body+=f'<section><h2 id="{ident}">{esc(heading)}</h2><p>{esc(text)}</p></section>'
    source_scope=comparison['source_scope'][lang] if comparison_enabled else ('原論文のDOIと著者公開版、GROMACS・LAMMPS公式資料への案内を付けた導入です。原論文の全式の監査や数値再現は未実施です。Gaussian isokineticは提案者による教科書への入口を付けており、個別原論文の整理は継続中です。' if ja else 'An introduction linking original-paper DOIs, author preprints and official GROMACS/LAMMPS documentation. Full equation audits and numerical reproductions have not been performed. The Gaussian isokinetic entry currently links an originator-authored monograph; individual original-paper curation remains open.')
    body+='<section><h2 id="source-scope">'+('出典と確認範囲' if ja else 'Sources and review scope')+'</h2><p>'+esc(source_scope)+'</p><p><a href="/using/">'+('引用と利用条件' if ja else 'Citation and reuse')+'</a> · <a href="/numerical-methods-atlas/methods/index.json">Method registry / JSON</a></p></section>'
    structured={'@context':'https://schema.org','@type':'LearningResource','name':title,'description':description,'inLanguage':lang,'url':ORIGIN+url,'author':{'@type':'Person','name':'Hiroshi Koyama'},'dateModified':'2026-11-22'}
    document=f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} | Numerical Methods Atlas</title><meta name="description" content="{esc(description)}"><link rel="canonical" href="{ORIGIN+url}"><link rel="alternate" hreflang="ja" href="{ORIGIN}/numerical-methods-atlas/ja/read/thermostats/"><link rel="alternate" hreflang="en" href="{ORIGIN}/numerical-methods-atlas/en/read/thermostats/"><link rel="stylesheet" href="/styles/atlas-resources.css?v={version}"><script type="application/ld+json">{json.dumps(structured,ensure_ascii=False)}</script></head><body class="profile-page"><main id="main" class="profile-main atlas-resource-main">{body}</main></body></html>'''
    if comparison_enabled:document=document.replace('</head>','<link rel="stylesheet" href="/numerical-methods-atlas/vendor/katex.min.css"></head>')
    dest=ROOT/url.lstrip('/');dest.mkdir(parents=True,exist_ok=True);(dest/'index.html').write_text(document+'\n')
    public,markdown=companion_documents(lang,title,description)
    (dest/'index.json').write_text(json.dumps(public,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    (dest/'index.md').write_text(markdown)
    # Keep a human entry from the imported contents page; regenerate after every import.
    contents=ATLAS/lang/'read/index.html';text=contents.read_text()
    text=re.sub(r'<!-- thermostat-entry -->.*?<!-- /thermostat-entry -->','',text,flags=re.S)
    entry='<!-- thermostat-entry --><section class="page-width"><h2><a href="'+url+'">'+esc(title)+'</a></h2><p>'+esc(description)+'</p></section><!-- /thermostat-entry -->'
    contents.write_text(text.replace('</main>',entry+'</main>'))
xml=ET.parse(ATLAS/'sitemap.xml');root=xml.getroot();existing={x.text for x in root.findall('.//{*}loc')};ns='{http://www.sitemaps.org/schemas/sitemap/0.9}'
for lang in ['ja','en']:
    url=ORIGIN+f'/numerical-methods-atlas/{lang}/read/thermostats/'
    if url not in existing:ET.SubElement(ET.SubElement(root,ns+'url'),ns+'loc').text=url
ET.register_namespace('',ns[1:-1]);xml.write(ATLAS/'sitemap.xml',encoding='utf-8',xml_declaration=True)
guide=ROOT/'llms.txt';text=guide.read_text()
text=re.sub(r'^- \[Thermostats: comparison and planned checks\].*\n?','',text,flags=re.M)
line='- [Thermostats: comparison and planned checks]('+ORIGIN+'/numerical-methods-atlas/en/read/thermostats/): '+('CSVR and Langevin share a small OBABO harmonic/anharmonic comparison, with a separate exact kinetic-bath test. Signed CSVR follows the 2007/2008 primary papers and author correction. Canonical distributions, fluctuations and method-dependent correlations are distinguished; the earlier BAOAB release remains intact. The other ten methods remain planned. JSON/Markdown and immutable code/test/results/receipt links are available.' if comparison_enabled else '12 method introductions with primary-reference entry points. Only Langevin BAOAB for a 1D harmonic oscillator has dedicated code, fixed inputs, canonical-distribution/correlation checks and an independent linear-Gaussian reference; the other 11 methods remain planned.')+'\n'
guide.write_text(text.rstrip()+'\n'+line)
print('Built bilingual thermostat comparisons and reading-index entries for',len(methods),'methods.')
