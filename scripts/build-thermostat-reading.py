#!/usr/bin/env python 3
"""Build thermostat comparisons with strictly scoped, verified harmonic supplements."""
from pathlib import Path
import hashlib
import html
import json
import re
import xml.etree.ElementTree as ET
from atlas_goal_availability import load_supplemental_examples

ROOT=Path(__file__).resolve().parents[1]
ATLAS=ROOT/'numerical-methods-atlas'
ORIGIN='https://hrkoyama.github.io'
methods=[x for x in json.loads((ROOT/'catalog/atlas-methods.json').read_text())['methods'] if x['group']['id']=='thermostats']
field=next(x for x in json.loads((ROOT/'catalog/atlas-depth.json').read_text())['fields'] if x['id']=='temperature')
supplements=load_supplemental_examples(ROOT,field.get('supplemental_examples',[]))
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
for lang in ['ja','en']:
    ja=lang=='ja';title,description=intro[lang]
    url=f'/numerical-methods-atlas/{lang}/read/thermostats/'
    other='en' if ja else 'ja'
    body='<p class="eyebrow">MOLECULAR DYNAMICS / THERMOSTATS</p><h1>'+esc(title)+'</h1><p class="intro">'+esc(description)+'</p>'
    body+='<p class="resource-summary">'+esc(field['scope'][lang])+'</p>'
    body+='<nav class="resource-nav">'+''.join('<a href="'+u+'">'+esc(label)+'</a>' for u,label in [('/numerical-methods-atlas/methods/','手法の見取り図' if ja else 'Method map'),(f'/numerical-methods-atlas/{lang}/read/','解説章の目次' if ja else 'Reading chapters'),(f'/numerical-methods-atlas/{other}/read/thermostats/','English' if ja else '日本語')])+'</nav>'
    for ident,heading,text in paragraphs[lang][:3]:body+=f'<section><h2 id="{ident}">{esc(heading)}</h2><p>{esc(text)}</p></section>'
    body+='<section id="executed-scope"><h2>'+('調和Langevinの実行・検証例' if ja else 'Runnable harmonic-Langevin validation')+'</h2><p>'+esc(field['refinement'][lang])+'</p><ul>'
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
    ident,heading,text=paragraphs[lang][-1];body+=f'<section><h2 id="{ident}">{esc(heading)}</h2><p>{esc(text)}</p></section>'
    body+='<section><h2 id="source-scope">'+('出典と確認範囲' if ja else 'Sources and review scope')+'</h2><p>'+('原論文のDOIと著者公開版、GROMACS・LAMMPS公式資料への案内を付けた導入です。原論文の全式の監査や数値再現は未実施です。Gaussian isokineticは提案者による教科書への入口を付けており、個別原論文の整理は継続中です。' if ja else 'An introduction linking original-paper DOIs, author preprints and official GROMACS/LAMMPS documentation. Full equation audits and numerical reproductions have not been performed. The Gaussian isokinetic entry currently links an originator-authored monograph; individual original-paper curation remains open.')+'</p><p><a href="/using/">'+('引用と利用条件' if ja else 'Citation and reuse')+'</a> · <a href="/numerical-methods-atlas/methods/index.json">Method registry / JSON</a></p></section>'
    structured={'@context':'https://schema.org','@type':'LearningResource','name':title,'description':description,'inLanguage':lang,'url':ORIGIN+url,'author':{'@type':'Person','name':'Hiroshi Koyama'},'dateModified':'2026-11-22'}
    document=f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} | Numerical Methods Atlas</title><meta name="description" content="{esc(description)}"><link rel="canonical" href="{ORIGIN+url}"><link rel="alternate" hreflang="ja" href="{ORIGIN}/numerical-methods-atlas/ja/read/thermostats/"><link rel="alternate" hreflang="en" href="{ORIGIN}/numerical-methods-atlas/en/read/thermostats/"><link rel="stylesheet" href="/styles/atlas-resources.css?v={version}"><script type="application/ld+json">{json.dumps(structured,ensure_ascii=False)}</script></head><body class="profile-page"><main id="main" class="profile-main atlas-resource-main">{body}</main></body></html>'''
    dest=ROOT/url.lstrip('/');dest.mkdir(parents=True,exist_ok=True);(dest/'index.html').write_text(document+'\n')
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
guide=ROOT/'llms.txt';text=guide.read_text();line='- [Thermostats: comparison and planned checks]('+ORIGIN+'/numerical-methods-atlas/en/read/thermostats/): 12 method introductions with primary-reference entry points. Only Langevin BAOAB for a 1D harmonic oscillator has dedicated code, fixed inputs, canonical-distribution/correlation checks and an independent linear-Gaussian reference; the other 11 methods remain planned.\n'
if line not in text:guide.write_text(text.rstrip()+'\n'+line)
print('Built bilingual thermostat comparisons and reading-index entries for',len(methods),'methods.')
