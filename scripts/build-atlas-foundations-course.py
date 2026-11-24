#!/usr/bin/env python3
"""Publish the beginner course from one shared manuscript; never run solvers/PDF here."""
import hashlib
import json
from html import escape as e
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ORIGIN='https://hrkoyama.github.io'


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def paragraphs(items):return ''.join('<p>'+e(t)+'</p>' for t in items)
def items(values):return '<ul>'+''.join('<li>'+e(t)+'</li>' for t in values)+'</ul>'


def build(root=ROOT):
    source=root/'catalog/atlas-foundations-course.json';d=json.loads(source.read_text());base=d['base'];out=root/base.lstrip('/');edition=out/d['edition'];assets=base+d['edition']+'/'
    receipt=json.loads((edition/'book-verification.json').read_text())
    assert receipt['source_sha256']==sha(source),'PDF manuscript is stale: rebuild PDF and inspect before refreshing indexes'
    for file,digest in receipt['assets'].items():assert sha(edition/file)==digest,file
    release=json.loads((root/'code/numerical-foundations/2026-11-24/release.json').read_text());assert sha(root/release['zip'].lstrip('/'))==release['zip_sha256']
    for file,digest in release['source_files'].items():assert sha(root/file)==digest,file
    def layout(title,body,route):
        document = '<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+e(title)+' | 数値計算の基礎</title><meta name="description" content="誤差、安定性、境界条件、分割法、シンプレクティック積分を学ぶ初学者向け教材。本文・図・小さな計算例・確認問題をWebとPDFで。"><link rel="canonical" href="'+ORIGIN+route+'"><link rel="stylesheet" href="/styles/atlas-foundations-course.css?v='+sha(root/'styles/atlas-foundations-course.css')[:12]+'"></head><body><main><nav aria-label="パンくず"><a href="/numerical-methods-atlas/ja/read/">アトラスの読み物</a> / <a href="'+base+'">数値計算の基礎</a></nav>'+body+'<footer><a href="'+base+'">全19章の目次</a> · <a href="'+assets+'numerical-foundations-ja.pdf">同じ内容のPDF</a> · <a href="'+release['zip']+'">計算例のコードZIP</a><p>2026年11月24日版 · '+e(d['rights'])+'</p></footer></main></body></html>\n'
        counterpart=base+'en/'+route[len(base):]
        alternates='<link rel="alternate" hreflang="ja" href="'+ORIGIN+route+'"><link rel="alternate" hreflang="en" href="'+ORIGIN+counterpart+'">'
        language='<nav class="course-language" aria-label="教材の言語"><a href="'+route+'" hreflang="ja" aria-current="page">日本語</a> · <a href="'+counterpart+'" hreflang="en" lang="en">English</a></nav>'
        return document.replace('</head>',alternates+'</head>').replace('<body>','<body data-content-language="ja">').replace('<main>','<main>'+language,1)
    downloads='<div class="downloads"><a href="'+assets+'numerical-foundations-ja.pdf">PDFをダウンロード</a><a href="'+release['zip']+'">小さな計算例のコードZIP</a><a href="/catalog/atlas-foundations-course.json">共通の原稿JSON</a></div>'
    intro='<p class="eyebrow">NUMERICAL METHODS ATLAS / FOUNDATIONS</p><h1>'+e(d['title'])+'</h1><p class="subtitle">'+e(d['subtitle'])+'</p><p>全19章 · 19枚の図 · 38問の確認問題と解答 · 2026年11月24日版</p>'+downloads+'<section><h2 id="start">はじめに</h2>'+paragraphs(d['preface'])+'<p>想定読者：'+e(d['audience'])+'</p><p>コード断片は配布ZIPのディレクトリで実行します。第19章のコマンドはシェルに入力します。</p></section>'
    for part in d['parts']:
        intro+='<section><h2 id="'+part['id']+'">'+e(part['title'])+'</h2><ol start="'+part['range'].split('-')[0]+'">'+''.join('<li><a href="'+base+c['id']+'/">'+e(c['title'])+'</a><p>'+e(c['goals'][0])+'</p></li>' for c in d['chapters'] if c['part']==part['id'])+'</ol></section>'
    intro+='<section><h2 id="symbols">よく使う記号</h2><dl>'+''.join('<dt>'+e(t)+'</dt><dd>'+e(v)+'</dd>' for t,v in d['glossary'])+'</dl></section><section><h2 id="references">参考資料と再現手順</h2>'
    for r in d['references']:intro+='<h3><a href="'+r['url']+'">'+e(r['title'])+'</a></h3><p>'+e(r['scope'])+'</p>'
    intro+='<h3>教材の実行・制作範囲</h3><p>'+e(d['execution_scope'])+'</p><p>25単体テスト・34固定判定・15CSVをZIPの verify_release.py で再実行できます。意図的な不安定例は異常を検出する対照例です。</p></section>'
    out.mkdir(parents=True,exist_ok=True);(out/'index.html').write_text(layout(d['title'],intro,base))
    for c in d['chapters']:
        body='<p class="eyebrow">第'+str(c['n'])+'章 / 全19章</p><h1>'+e(c['title'])+'</h1>'+''.join('<p class="goal">到達目標：'+e(t)+'</p>' for t in c['goals'])+paragraphs(c['lead']);eq=0
        for i,s in enumerate(c['sections'],1):
            body+='<section><h2 id="section-'+str(i)+'">'+e(s['title'])+'</h2>'+paragraphs(s['paragraphs'])
            for formula in s['equations']:
                eq+=1;body+='<div class="equation"><img src="'+assets+'equations/equation-'+c['id']+'-'+str(eq)+'.svg" alt="'+e(formula['plain'],quote=True)+'"></div>'
            body+='</section>'
        body+='<section><h2 id="example">小さな計算例</h2>'+paragraphs(c['worked']['paragraphs'])+'<pre><code>'+e(c['worked']['code'])+'</code></pre><p>'+e(c['worked']['result'])+'</p><figure><a href="'+assets+'figures/'+c['figure']['id']+'.svg"><img src="'+assets+'figures/'+c['figure']['id']+'.svg" alt="'+e(c['figure']['alt'],quote=True)+'" width="760" height="350" loading="lazy"></a><figcaption>'+e(c['figure']['caption'])+'</figcaption></figure><p class="data">保存データ：'+e(c['experiment']['data'])+'</p><p>'+e(c['experiment']['instructions'])+'</p><p><a href="'+release['zip']+'">コード・入力・保存CSV・テストを取得</a> / <a href="'+assets+'figures/'+c['figure']['id']+'.png">図のPNG</a> / <a href="'+assets+'figures/'+c['figure']['id']+'.pdf">図のPDF</a></p></section><section><h2 id="questions">確認問題と解答</h2>'
        for i,q in enumerate(c['questions'],1):body+='<p>問'+str(i)+'　'+e(q['question'])+'</p><details><summary>解答を開く</summary><p>'+e(q['answer'])+'</p></details>'
        body+='</section><section><h2 id="pitfalls">つまずきやすい点</h2>'+items(c['pitfalls'])+'</section><section><h2 id="summary">この章の要点</h2>'+items(c['summary'])+'</section><section><h2 id="reading">アトラスで先を読む</h2><ul>'+''.join('<li><a href="'+d['readings'][k]['url']+'">'+e(d['readings'][k]['title'])+'</a></li>' for k in c['readings'])+'</ul></section>'
        body+='<nav class="chapter-nav" aria-label="章を移動">'+(('<a rel="prev" href="'+base+f'{c["n"]-1:02d}/">← 前の章</a>') if c['n']>1 else '<a href="'+base+'">← はじめに</a>')+'<a href="'+base+'">目次</a>'+('<a rel="next" href="'+base+f'{c["n"]+1:02d}/">次の章 →</a>' if c['n']<19 else '<a href="'+base+'#references">参考資料 →</a>')+'</nav>'
        chapter=out/c['id'];chapter.mkdir(exist_ok=True);(chapter/'index.html').write_text(layout(c['title'],body,base+c['id']+'/'))
    print('Built 19 beginner chapters + course index from shared PDF manuscript; frozen assets verified.')
    from foundations_en_web import build as build_english
    build_english(root)

if __name__=='__main__':build()
