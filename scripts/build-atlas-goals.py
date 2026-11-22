#!/usr/bin/env python3
"""Publish curated, conditional routes from goals to existing public resources."""
from pathlib import Path
from html import escape as e
import json
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'catalog/atlas-goals.json').read_text())
methods={x['id']:x for x in json.loads((ROOT/'numerical-methods-atlas/methods/index.json').read_text())['methods']}
examples={x['id']:x for x in json.loads((ROOT/'catalog/atlas-execution-examples.json').read_text())['examples']}
assert len({g['id'] for g in data['goals']})==len(data['goals'])
for g in data['goals']:
    assert all(x in methods for x in g['methods']),g['id']
    assert all(x in examples for x in g['examples']),g['id']
    assert all(g['scope'][lang] and g['title'][lang] for lang in ['ja','en'])
module='export const goals='+json.dumps(data['goals'],ensure_ascii=False,separators=(',',':'))+';\n'
module+='''export function matchGoals(query){
 const q=String(query).normalize('NFKC').toLowerCase().replace(/[‐‑‒–—−-]/g,' ').replace(/\\s+/g,' ').trim();
 if(!q)return [];
 return goals.filter(g=>{
  if(g.id==='smooth-vortex' && /衝撃波|shock/.test(q) && !/含まない|なし|without|no shock/.test(q))return false;
  if(g.id==='shocks' && /相対論|relativ|mhd|衝撃波を含まない|衝撃波なし|without shocks?|no shocks?/.test(q))return false;
  return g.terms.some(t=>q.includes(t.normalize('NFKC').toLowerCase().replace(/[‐‑‒–—−-]/g,' ')));
 });
}
'''
(ROOT/'search/goals-data.mjs').write_text(module)
sections=[]
for lang in ['ja','en']:
    ja=lang=='ja'; parts=[f'<section data-site-language="{lang}" lang="{lang}"><h1>'+('目的から計算法を選ぶ' if ja else 'Choose methods by your goal')+'</h1><p>'+('モデル・境界・滑らかさを確認し、候補の解説と公開コード・テストへ進みます。まず6つの代表的な目的を案内します。' if ja else 'Check the model, boundaries and smoothness before following candidate methods, published code and tests. Start with six representative goals.')+'</p><nav aria-label="'+('目的を選ぶ' if ja else 'Choose a goal')+'">']
    parts += [f'<a class="goal-choice" href="#{g["id"]}-{lang}">{e(g["title"][lang])}</a>' for g in data['goals']]
    parts+=['</nav>']
    for g in data['goals']:
        parts += [f'<article class="goal-card" id="{g["id"]}-{lang}"><h2>{e(g["title"][lang])}</h2><p>{e(g["scope"][lang])}</p><h3>'+('候補と適用条件' if ja else 'Candidates and conditions')+'</h3>']
        for ident in g['methods']:
            m=methods[ident]; parts += [f'<div class="goal-method"><h4>{e(m["name"][lang])}</h4><p>{e(m["summary"][lang])}</p><p class="goal-links">']
            def link(url,label):return f'<a href="{e(url,quote=True)}">{e(label)}</a> '
            reading=m['reading'].get(lang) or m['reading'].get('en')
            if reading:parts += [link(reading,'解説' if ja else 'Explanation')]
            if m['status']=='educational-example':
                for key,label in [('code_urls','関連コード' if ja else 'Related code'),('test_urls','関連テスト' if ja else 'Related tests')]:
                    if m.get(key):parts += [link(m[key][0],label)]
            else:parts+=['<span>'+('コード・テストは未公開' if ja else 'Code and tests are not published')+'</span>']
            parts += [link(m['url'],'適用条件・文献・全ファイル' if ja else 'Conditions, references & all files'),'</p></div>']
        if g['examples']:
            parts+=['<h3>'+('固定入力から実行・検証する' if ja else 'Run and validate fixed inputs')+'</h3><ul>']
            for ident in g['examples']:parts += ['<li>'+link('/numerical-methods-atlas/code-and-data/examples/'+ident+'/?lang='+lang,examples[ident]['name'][lang])+'</li>']
            parts+=['</ul>']
        parts+=['<p class="note">'+('関連コード・テストは教育用例です。各手法の全変種や目的全体の検証を意味しません。' if ja else 'Related educational code and tests do not validate every variant or the entire application.')+'</p><p><a href="#top">'+('目的一覧に戻る' if ja else 'Back to goals')+'</a></p></article>']
    parts+=['</section>'];sections.append(''.join(parts))
html='''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title data-page-title-ja="目的から計算法を選ぶ | 数値計算法アトラス" data-page-title-en="Choose methods by goal | Numerical Methods Atlas">目的から計算法を選ぶ | 数値計算法アトラス</title><meta name="description" content="衝撃波・低散逸な渦・Poisson・MHD・硬いODE・粒子重力の目的から、適用条件と公開コード・テストへ。"><link rel="canonical" href="https://hrkoyama.github.io/numerical-methods-atlas/start/"><style>.goal-choice{display:inline-block;margin:.4rem;padding:.7rem 1rem;border:1px solid #597563;border-radius:5px}.goal-card{margin:2rem 0;padding:1.3rem;border:1px solid #bacbc1;border-radius:6px;scroll-margin-top:1rem}.goal-method{border-top:1px solid #ccd5ce;padding:.5rem 0}.goal-links{display:flex;flex-wrap:wrap;gap:.6rem}.goal-links a{display:inline-block;padding:.6rem;border:1px solid #729382;border-radius:4px;min-height:24px}.goal-card h4{font-size:1.1rem}.goal-card .note{font-size:.9rem}main{overflow-wrap:anywhere}</style></head><body class="profile-page" data-site-language-anchors="suffix"><main class="profile-main" id="top">'''+''.join(sections)+'</main></body></html>'
dest=ROOT/'numerical-methods-atlas/start';dest.mkdir(exist_ok=True);(dest/'index.html').write_text(html)
print('Built goal-based discovery:',len(data['goals']),'conditional routes.')
