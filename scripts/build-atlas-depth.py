#!/usr/bin/env python 3
"""Publish scoped field evidence; do not infer field-wide validation from a count."""
from pathlib import Path
from html import escape as e
import hashlib
import json
import re
from urllib.parse import urlparse
from atlas_depth import depth_teaser
from atlas_goal_availability import load_supplemental_examples
from atlas_biology_model_evidence import apply_biology_model_evidence

ROOT=Path(__file__).resolve().parents[1]
BASE='/numerical-methods-atlas/depth/'
ORIGIN='https://hrkoyama.github.io'
source=ROOT/'catalog/atlas-depth.json';data=json.loads(source.read_text())
registry_path=ROOT/'numerical-methods-atlas/code-and-data/examples.json'
registry=json.loads(registry_path.read_text());examples={x['id']:x for x in registry['examples']}
receipt_path=ROOT/urlparse(registry['verification_receipt']).path.lstrip('/')
public_receipt=receipt_path.with_name(receipt_path.stem+'-public.json')
receipt_url=registry['verification_receipt']
if public_receipt.is_file():
    receipt_path=public_receipt
    receipt_url=receipt_url.removesuffix('.json')+'-public.json'
receipt=json.loads(receipt_path.read_text()) if receipt_path.exists() else None
assert receipt and receipt['registry_sha256']==hashlib.sha256(registry_path.read_bytes()).hexdigest() and receipt['passed'], 'A matching successful execution receipt is required'
checks={r['id']:r['validation'] for r in receipt['examples']}
assert len(data['fields'])==len({f['id'] for f in data['fields']})
sources={}
for path in [source,registry_path,receipt_path,ROOT/'catalog/atlas-depth-expansion.json']:sources[path.relative_to(ROOT).as_posix()]=hashlib.sha256(path.read_bytes()).hexdigest()
supplements={item['id']:item for item in load_supplemental_examples(ROOT,list(dict.fromkeys(ident for field in data['fields'] for ident in field.get('supplemental_examples',[]))))}
for item in supplements.values():sources.update(item['source_sha256'])


def link(url,label):return '<a href="'+e(url,quote=True)+'">'+e(label)+'</a>'


sections=[]
for lang in ['ja','en']:
    ja=lang=='ja'
    body='<section data-site-language="'+lang+'" lang="'+lang+'"><p class="eyebrow">NUMERICAL METHODS ATLAS · EVIDENCE BY FIELD</p><h1>'+e(data['title'][lang])+'</h1><p class="intro">'+e(data['policy'][lang])+'</p>'
    body+='<nav class="resource-nav">'+link('/numerical-methods-atlas/?lang='+lang,'アトラス冒頭' if ja else 'Atlas home')+link('/numerical-methods-atlas/start/?lang='+lang,'目的から探す' if ja else 'Choose by goal')+link('/numerical-methods-atlas/code-and-data/examples/?lang='+lang,'固定入力の実行例' if ja else 'Fixed-input execution examples')+link('/numerical-methods-atlas/connections/?lang='+lang,'分野間のつながり' if ja else 'Connections across fields')+link(BASE+'index.json','根拠と範囲 / JSON' if ja else 'Evidence and scope / JSON')+'</nav>'
    body+='<p class="depth-key">'+('「参照比較」は解析解・別実装・同じ実装の細格子を区別して読みます。「収束確認」も、その入力と刻み・標本数の範囲に限ります。下の例は分野ごとの代表で、分野全体の完成率ではありません。' if ja else 'Reference comparisons distinguish analytic solutions, independent implementations and finer grids of the same solver. Refinement applies only to the published inputs, steps or sample budgets. Selected examples represent fields, not completion percentages.')+'</p><nav class="resource-nav">'+''.join(link('#'+f['id']+'-'+lang,f['name'][lang]) for f in data['fields'])+'</nav><div class="depth-grid">'
    for f in data['fields']:
        assert all((ROOT/url.lstrip('/')/'index.html').is_file() for url in f['reading'].values()),f['id']
        cases=[examples[i] for i in f['examples']]
        extra=[supplements[ident] for ident in f.get('supplemental_examples',[])]
        assert all(checks[x['id']]['passed'] for x in cases)
        has=bool(cases or extra)
        reading=link(f['reading'][lang],'解説あり' if ja else 'Reading available')
        code=link(cases[0]['release']['download'] if cases else extra[0]['download'],'専用コード・テストあり' if ja else 'Code and tests available') if has else ('未実装' if ja else 'Unimplemented')
        execution=(str(len(cases))+('共通例 + ' if ja else ' common examples + ')+str(len(extra))+('補助例・固定入力の追試済み' if ja else ' supplemental fixed-input examples rerun')) if has else ('実行例なし' if ja else 'No execution examples')
        body+='<article id="'+f['id']+'-'+lang+'" class="depth-card" data-field="'+f['id']+'"><h2>'+e(f['name'][lang])+'</h2><p>'+e(f['scope'][lang])+'</p><dl>'
        labels=[('解説' if ja else 'Reading',reading),('実装' if ja else 'Implementation',code),('実行' if ja else 'Execution',e(execution)),('参照との比較' if ja else 'Reference comparison',e(f['reference'][lang])),('収束・誤差の確認' if ja else 'Refinement and errors',e(f['refinement'][lang]))]
        body+=''.join('<div><dt>'+label+'</dt><dd>'+value+'</dd></div>' for label,value in labels)+'</dl>'
        if cases:
            body+='<ul class="depth-examples">'+''.join('<li>'+link('/numerical-methods-atlas/code-and-data/examples/'+x['id']+'/?lang='+lang,x['name'][lang])+'</li>' for x in cases)+'</ul>'
        if extra:
            body+='<ul class="depth-examples">'+''.join('<li>'+link(x['url']+'?lang='+lang,x['title'][lang])+' ('+('補助例' if ja else 'supplement')+')</li>' for x in extra)+'</ul>'
        body+='<p class="depth-next"><strong>'+('次に埋める差：' if ja else 'Next gap to close: ')+'</strong>'+e(f['next'][lang])+'</p></article>'
    body+='</div><section class="depth-batch"><h2>'+('既存の生物・確率4例の保存結果' if ja else 'Stored results for four existing biology/stochastic examples')+'</h2><p>'+(f'この4例の配布版はZIP独立展開で11検査と全入力を再実行しました。公開ZIP・入力・参照だけで追試済みの共通22例を保持し、別管理の{len(supplements)}補助例は上のリンクへ接続しています。次の数値は保存結果であり、全モデルの検証件数ではありません。' if ja else f'The release for these four examples passed 11 tests and all inputs after independent ZIP extraction. Preserve the 22 shared examples previously rerun using public ZIPs, inputs and references; the {len(supplements)} separate supplements have links above. Values below are stored results, not field-wide validation counts.')+'</p><div class="depth-results">'
    for ident in ['logistic-growth','sir-epidemic','mc-integral','gbm-sde']:
        x=examples[ident];out=next(o for o in x['outputs'] if o['format']=='json');path=ROOT/urlparse(out['url']).path.lstrip('/');r=json.loads(path.read_text());m=r['metrics']
        assert r['passed'] and all(r['checks'].values()) and hashlib.sha256(path.read_bytes()).hexdigest()==out['sha256']
        sources[path.relative_to(ROOT).as_posix()]=out['sha256']
        if ident in ['logistic-growth','sir-epidemic']:
            note=('最大誤差 ' if ja else 'Maximum error ')+format(m['finest_max_error'],'.3g')+('、観測次数 ' if ja else '; observed orders ')+', '.join(format(v,'.2f') for v in m['observed_orders'])
        elif ident=='mc-integral':
            note=('256 seed、RMS誤差／解析理論値 ' if ja else '256 seeds; RMS / analytic prediction ')+', '.join(format(v,'.3f') for v in m['rms_over_theory'])+('。区間被覆は固定seedでの実測。' if ja else '. Interval coverage is empirical for the fixed seeds.')
        else:
            note=('4096経路、強収束の観測次数 ' if ja else '4096 paths; observed strong orders ')+', '.join(format(v,'.2f') for v in m['observed_orders'])
        preview=x['release']['manifest'].rsplit('/',1)[0]+'/results/'+ident+'/preview.png'
        body+='<article><h3>'+link('/numerical-methods-atlas/code-and-data/examples/'+ident+'/?lang='+lang,x['name'][lang])+'</h3><img src="'+preview+'" alt="'+e(x['name'][lang])+'" width="960" height="570" loading="lazy"><p>'+e(note)+'</p><p>'+link(out['url'],'結果JSON' if ja else 'Result JSON')+' · '+link(x['inputs']['url'],'固定入力' if ja else 'Fixed input')+'</p></article>'
    body+='</div><p>'+link(receipt_url,'公開レジストリ・配布物による追試記録' if ja else 'Public-registry and distribution rerun receipt')+' · '+link('/code/model-benchmarks/2026-11-22/verification.json','ZIP独立展開と11検査' if ja else 'Independent extraction and 11 tests')+'</p></section></section>'
    sections.append(body)
dest=ROOT/BASE.lstrip('/');dest.mkdir(exist_ok=True)
css='/styles/atlas-depth.css';version=hashlib.sha256((ROOT/css.lstrip('/')).read_bytes()).hexdigest()[:12]
document='<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title data-page-title-ja="分野ごとの実装・検証範囲 | 数値計算法アトラス" data-page-title-en="Implementation and validation by field | Numerical Methods Atlas">分野ごとの実装・検証範囲 | 数値計算法アトラス</title><meta name="description" content="流体・原子・分子DFT・生物・確率計算・温度制御の、解説・専用コード・固定入力・参照比較・収束確認と未実装の範囲。"><link rel="canonical" href="'+ORIGIN+BASE+'"><link rel="stylesheet" href="/styles/atlas-resources.css"><link rel="stylesheet" href="'+css+'?v='+version+'"></head><body class="profile-page" data-site-language-anchors="suffix"><main class="profile-main atlas-resource-main" id="main">'+''.join(sections)+'</main></body></html>\n'
(dest/'index.html').write_text(document)
(dest/'index.json').write_text(json.dumps({**data,'registry':registry['url'],'verification_receipt':receipt_url,'source_sha256':sources},ensure_ascii=False,indent=2)+'\n')
# Keep the survey chapter explicit about its newly implemented subset, in SPA and static text.
for lang in ['ja','en']:
    biology=next(f for f in data['fields'] if f['id']=='biology')
    notice='<aside class="resource-summary" id="biological-execution-scope"><h2>'+('小さなモデルから実行・検証する' if lang=='ja' else 'Run and validate small model examples')+'</h2><p>'+e(biology['scope'][lang])+'</p><ul>'+''.join('<li>'+link(supplements[ident]['url']+'?lang='+lang,supplements[ident]['title'][lang])+'</li>' for ident in biology.get('supplemental_examples',[]))+'</ul><p>'+e(biology['reference'][lang])+'</p><p>'+link('/numerical-methods-atlas/'+lang+'/read/validation-biology/','非線形発展・成長後パターンの手法と独立参照を読む' if lang=='ja' else 'Read about nonlinear evolution, post-growth patterns and independent references')+' · '+link(BASE+'?lang='+lang+'#biology-'+lang,'実装範囲・結果・残る差' if lang=='ja' else 'Implementation scope, results and gaps')+'</p></aside>'
    def adapt(text):
        text=re.sub(r'<!-- atlas-biology-depth -->.*?<!-- /atlas-biology-depth -->','',text,flags=re.S)
        # The imported survey has wrapped English text and earlier overlays.
        # Replace its introductory scope structurally so a second refresh is identical.
        pattern=r'(<h1\b[^>]*>.*?</h1>\s*<p>.*?<strong>).*?(</strong>)'
        text=re.sub(pattern,lambda m:m[1]+e(biology['scope'][lang])+m[2],text,count=1,flags=re.S)
        description=('22モデル族の解説と小規模な増殖・SIR・酵素/QSSA・Lotka–Volterra・別固定入力SEIR・反応拡散・FHNの検証。完全HH・流体連成は未実装。' if lang=='ja' else 'A 22-family survey with small logistic, SIR, enzyme/QSSA, Lotka–Volterra, separate fixed-input SEIR, reaction–diffusion and FHN checks. Full HH and fluid coupling remain unimplemented.')
        text=re.sub(r'<meta name="description"[^>]*>', '<meta name="description" content="'+description+'">',text)
        text=re.sub(r'<meta property="og:description"[^>]*>', '<meta property="og:description" content="'+description+'">',text)
        for anchor,ident in [('01-1838-logistic-population-growth','logistic-growth'),('05-1927-sir-and-seir-compartment-models','sir-epidemic')]:
            pattern=r'(<h3 id="'+anchor+r'".*?</h3>\s*<p><strong>)(.*?)(</strong>)'
            label=('ロジスティックの固定入力・解析解比較あり。' if ident=='logistic-growth' else '閉鎖SIR例を保持。SEIRの保存則・初期線形化は別の固定入力例。') if lang=='ja' else ('Logistic fixed-input / analytic checks available.' if ident=='logistic-growth' else 'Closed-SIR example retained; SEIR conservation and early linearization have a separate fixed-input example.')
            text=re.sub(pattern,lambda m:m[1]+label+m[3],text,flags=re.S)
        for anchor,label in [('02-1913-michaelismenten-and-full-enzyme-kinetics',('固定した4状態酵素系とQSSAの限定例。初期層・積分誤差・縮約誤差を区別。','A fixed four-state enzyme/QSSA example distinguishes initial-layer, integration and reduction errors.')),('03-1920-lotkavolterra-predatorprey',('固定した正のLotka–Volterra軌道の独立参照・不変量・刻み比較。','A fixed positive Lotka–Volterra orbit has independent-reference, invariant and step-refinement comparisons.'))]:
            pattern=r'(<h3 id="'+anchor+r'".*?</h3>\s*<p><strong>)(.*?)(</strong>)'
            text=re.sub(pattern,lambda m:m[1]+label[0 if lang=='ja' else 1]+m[3],text,flags=re.S)
        for anchor,label in [('09-1952-turing-reactiondiffusion-framework',('固定1次元Schnakenberg系の線形発現・非線形発展・成長後パターンを別々に検証。','Separate scoped checks of linear onset, nonlinear evolution and post-growth patterns for fixed 1D Schnakenberg systems.')),('10-1961-fitzhughnagumo-excitation-and-recovery',('FHNの励起回復ODE・時間収束例あり。完全HHは未実装。','FHN excitation/recovery ODE and time refinement available; full HH unimplemented.')),('17-1979-schnakenberg-reactiondiffusion',('有限振幅の非線形発展と成長後パターンを独立参照・空間/時間収束で比較。一般の模様選択は対象外。','Finite-amplitude nonlinear evolution and post-growth patterns compared with independent references and separate space/time refinement; no general pattern-selection claim.'))]:
            pattern=r'(<h3 id="'+anchor+r'".*?</h3>\s*<p><strong>)(.*?)(</strong>)'
            text=re.sub(pattern,lambda m:m[1]+label[0 if lang=='ja' else 1]+m[3],text,flags=re.S)
        return re.sub(r'(</h1>)',lambda m:m[1]+'<!-- atlas-biology-depth -->'+notice+'<!-- /atlas-biology-depth -->',text,count=1)
    path=ROOT/f'numerical-methods-atlas/{lang}/read/biological-models/index.html';path.write_text(adapt(path.read_text()))
    for filename in [f'content.{lang}.json']+(['content.json'] if lang=='en' else []):
        path=ROOT/'numerical-methods-atlas'/filename;docs=json.loads(path.read_text());docs['biological-models']['html']=adapt(docs['biological-models']['html']);path.write_text(json.dumps(docs,ensure_ascii=False,separators=(',',':'))+'\n')
bio=ROOT/'numerical-methods-atlas/assets/biological-models.json';survey=json.loads(bio.read_text())
apply_biology_model_evidence(survey,biology,examples,supplements,data['reviewed_on'])
bio.write_text(json.dumps(survey,ensure_ascii=False,indent=2)+'\n')
guide=ROOT/'llms.txt';text=re.sub(r'^- \[Field-specific validation depth\].*\n?','',guide.read_text(),flags=re.M)
guide.write_text(text.rstrip()+'\n- [Field-specific validation depth]('+ORIGIN+BASE+'): bilingual scope/evidence/gaps by field. Preserve the shared 22-example registry and link '+str(len(supplements))+' independently rerun supplements across foundations, nonlinear Schnakenberg reaction-diffusion and post-growth patterns, other models, particles/transport, fluid/MHD and Langevin/CSVR comparisons. Preserve the earlier harmonic BAOAB example separately from new two-degree same-OBABO harmonic/quartic comparisons and the CSVR-kernel diagnostic. Full HH, the other 10 thermostats, general many-body and first-principles-MD coupling remain unimplemented or unvalidated.\n')
print('Built field-specific evidence and validation gaps:',len(data['fields']),'fields,',len(supplements),'separate supplements; common registry unchanged.')
