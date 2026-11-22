#!/usr/bin/env python3
"""Publish scoped field evidence; do not infer field-wide validation from a count."""
from pathlib import Path
from html import escape as e
import hashlib
import json
import re
from urllib.parse import urlparse
from atlas_depth import depth_teaser

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
for path in [source,registry_path,receipt_path]:sources[path.relative_to(ROOT).as_posix()]=hashlib.sha256(path.read_bytes()).hexdigest()


def link(url,label):return '<a href="'+e(url,quote=True)+'">'+e(label)+'</a>'


sections=[]
for lang in ['ja','en']:
    ja=lang=='ja'
    body='<section data-site-language="'+lang+'" lang="'+lang+'"><p class="eyebrow">NUMERICAL METHODS ATLAS · EVIDENCE BY FIELD</p><h1>'+e(data['title'][lang])+'</h1><p class="intro">'+e(data['policy'][lang])+'</p>'
    body+='<nav class="resource-nav">'+link('/numerical-methods-atlas/?lang='+lang,'アトラス冒頭' if ja else 'Atlas home')+link('/numerical-methods-atlas/start/?lang='+lang,'目的から探す' if ja else 'Choose by goal')+link('/numerical-methods-atlas/code-and-data/examples/?lang='+lang,'固定入力の実行例' if ja else 'Fixed-input execution examples')+link(BASE+'index.json','根拠と範囲 / JSON' if ja else 'Evidence and scope / JSON')+'</nav>'
    body+='<p class="depth-key">'+('「参照比較」は解析解・別実装・同じ実装の細格子を区別して読みます。「収束確認」も、その入力と刻み・標本数の範囲に限ります。下の例は分野ごとの代表で、分野全体の完成率ではありません。' if ja else 'Reference comparisons distinguish analytic solutions, independent implementations and finer grids of the same solver. Refinement applies only to the published inputs, steps or sample budgets. Selected examples represent fields, not completion percentages.')+'</p><nav class="resource-nav">'+''.join(link('#'+f['id']+'-'+lang,f['name'][lang]) for f in data['fields'])+'</nav><div class="depth-grid">'
    for f in data['fields']:
        assert all((ROOT/url.lstrip('/')/'index.html').is_file() for url in f['reading'].values()),f['id']
        cases=[examples[i] for i in f['examples']]
        assert all(checks[x['id']]['passed'] for x in cases)
        has=bool(cases)
        reading=link(f['reading'][lang],'解説あり' if ja else 'Reading available')
        code=link(cases[0]['release']['download'],'専用コード・テストあり' if ja else 'Code and tests available') if has else ('未実装' if ja else 'Unimplemented')
        execution=(str(len(cases))+('代表例・固定入力の追試済み' if ja else ' selected fixed-input examples rerun')) if has else ('実行例なし' if ja else 'No execution examples')
        body+='<article id="'+f['id']+'-'+lang+'" class="depth-card" data-field="'+f['id']+'"><h2>'+e(f['name'][lang])+'</h2><p>'+e(f['scope'][lang])+'</p><dl>'
        labels=[('解説' if ja else 'Reading',reading),('実装' if ja else 'Implementation',code),('実行' if ja else 'Execution',e(execution)),('参照との比較' if ja else 'Reference comparison',e(f['reference'][lang])),('収束・誤差の確認' if ja else 'Refinement and errors',e(f['refinement'][lang]))]
        body+=''.join('<div><dt>'+label+'</dt><dd>'+value+'</dd></div>' for label,value in labels)+'</dl>'
        if cases:
            body+='<ul class="depth-examples">'+''.join('<li>'+link('/numerical-methods-atlas/code-and-data/examples/'+x['id']+'/?lang='+lang,x['name'][lang])+'</li>' for x in cases)+'</ul>'
        body+='<p class="depth-next"><strong>'+('次に埋める差：' if ja else 'Next gap to close: ')+'</strong>'+e(f['next'][lang])+'</p></article>'
    body+='</div><section class="depth-batch"><h2>'+('今回追加した実測結果' if ja else 'New measured results')+'</h2><p>'+('4例を新しい配布版へまとめ、ZIPを別フォルダへ展開して11検査と全入力を再実行しました。さらに公開ZIP・入力・参照だけで共通21例を追試しています。次の数値は保存結果であり、全モデルの検証件数ではありません。' if ja else 'A new edition contains four examples. An independent ZIP extraction passed 11 tests and reran every input. All 21 common examples were also rerun using public ZIPs, inputs and references. Values below are stored measurements, not field-wide validation counts.')+'</p><div class="depth-results">'
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
    notice='<aside class="resource-summary" id="biological-execution-scope"><h2>'+('実行・検証があるのは2モデル' if lang=='ja' else 'Two models have executed validation')+'</h2><p>'+e(next(f for f in data['fields'] if f['id']=='biology')['scope'][lang])+'</p><p>'+link(BASE+'?lang='+lang+'#biology-'+lang,'実装範囲・結果・残る差' if lang=='ja' else 'Implementation scope, results and gaps')+'</p></aside>'
    def adapt(text):
        text=re.sub(r'<!-- atlas-biology-depth -->.*?<!-- /atlas-biology-depth -->','',text,flags=re.S)
        text=text.replace('22項目すべてが文献調査とベンチマーク設計案です。この追加では生物ソルバーを実装しておらず、生物系のシミュレーション結果も示していません。','22項目の文献調査を基に、ロジスティック増殖と閉鎖SIRの固定入力計算・参照比較・時間収束を追加しました。その他のモデルは検証案の段階です。')
        text=re.sub(r'All 22 entries are literature and proposed\s+benchmark designs; this addition implements no biological solver and reports\s+no simulated biological result\.', 'The 22-entry survey now links fixed-input logistic and closed-SIR calculations, reference comparisons and time refinement. Other models remain proposed verification designs.',text)
        text=re.sub(r'<meta name="description"[^>]*>', '<meta name="description" content="'+('22の生物モデルの解説と、ロジスティック増殖・閉鎖SIRに限定した実行・検証例。' if lang=='ja' else 'A survey of 22 biological models with runnable validation scoped to logistic growth and closed SIR.')+'">',text)
        text=re.sub(r'<meta property="og:description"[^>]*>', '<meta property="og:description" content="'+('22モデルの解説。ロジスティック増殖・閉鎖SIRには実行・検証例あり。' if lang=='ja' else '22 model readings, with executed validation for logistic growth and closed SIR.')+'">',text)
        for anchor,ident in [('01-1838-logistic-population-growth','logistic-growth'),('05-1927-sir-and-seir-compartment-models','sir-epidemic')]:
            pattern=r'(<h3 id="'+anchor+r'".*?</h3>\s*<p><strong>)(.*?)(</strong>)'
            label=('ロジスティックの固定入力・解析解比較あり。' if ident=='logistic-growth' else '閉鎖SIRの実行例あり。SEIRは未実装。') if lang=='ja' else ('Logistic fixed-input / analytic checks available.' if ident=='logistic-growth' else 'Closed-SIR example available; SEIR unimplemented.')
            text=re.sub(pattern,lambda m:m[1]+label+m[3],text,flags=re.S)
        return re.sub(r'(</h1>)',lambda m:m[1]+'<!-- atlas-biology-depth -->'+notice+'<!-- /atlas-biology-depth -->',text,count=1)
    path=ROOT/f'numerical-methods-atlas/{lang}/read/biological-models/index.html';path.write_text(adapt(path.read_text()))
    for filename in [f'content.{lang}.json']+(['content.json'] if lang=='en' else []):
        path=ROOT/'numerical-methods-atlas'/filename;docs=json.loads(path.read_text());docs['biological-models']['html']=adapt(docs['biological-models']['html']);path.write_text(json.dumps(docs,ensure_ascii=False,separators=(',',':'))+'\n')
bio=ROOT/'numerical-methods-atlas/assets/biological-models.json';survey=json.loads(bio.read_text())
survey.update(checked_on=data['reviewed_on'],scope='22 surveyed biological families; logistic and closed-SIR fixed-input calculations now have measured validation. Other families remain survey-only. SIR results do not validate SEIR.')
for model in survey['models']:
    ident={'logistic':'logistic-growth','sir':'sir-epidemic'}.get(model['id'])
    if ident:
        model.update(status='scoped-educational-example',execution_examples=[ident],implementation_scope=examples[ident]['scope'])
bio.write_text(json.dumps(survey,ensure_ascii=False,indent=2)+'\n')
guide=ROOT/'llms.txt';text=re.sub(r'^- \[Field-specific validation depth\].*\n?','',guide.read_text(),flags=re.M)
guide.write_text(text.rstrip()+'\n- [Field-specific validation depth]('+ORIGIN+BASE+'): bilingual scope/evidence/gaps by field; two biology and two stochastic fixed-input examples. Atomic references do not validate molecular/periodic DFT; other biology, MCMC and thermostats remain unimplemented in their stated scope.\n')
print('Built field-specific evidence and validation gaps:',len(data['fields']),'fields, four new measured examples.')
