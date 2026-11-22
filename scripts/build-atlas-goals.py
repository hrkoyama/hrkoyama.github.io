#!/usr/bin/env python3
"""Publish curated, conditional routes from goals to existing public resources."""
from pathlib import Path
from html import escape as e
import json
from atlas_depth import depth_teaser, depth_assets
from atlas_goal_availability import goal_methods, goal_label, goal_attributes, goal_filter_controls, goal_filter_assets
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'catalog/atlas-goals.json').read_text())
methods={x['id']:x for x in json.loads((ROOT/'numerical-methods-atlas/methods/index.json').read_text())['methods']}
examples={x['id']:x for x in json.loads((ROOT/'catalog/atlas-execution-examples.json').read_text())['examples']}
assert len({g['id'] for g in data['goals']})==len(data['goals'])
domain_ids = {row['id'] for row in data['domains']}
assert len(domain_ids) == len(data['domains'])
assert 'all' not in domain_ids and all(ident and not any(c.isspace() for c in ident) for ident in domain_ids)
assert all(row['name'][lang] for row in data['domains'] for lang in ['ja', 'en'])
for g in data['goals']:
    assert g['domains'] and len(set(g['domains'])) == len(g['domains']) and set(g['domains']) <= domain_ids, g['id']
    assert all(x in methods for x in g['methods']),g['id']
    assert all(x in examples for x in g['examples']),g['id']
    assert g.get('availability') in [None,'reading-only']
    if g.get('availability')=='reading-only' or not any(m['status']=='educational-example' for m in goal_methods(g,methods)):
        assert not g['examples'],g['id']+' cannot advertise runnable examples'
    for resource in g.get('resources',[]):
        assert resource['status'] in ['reading-only','educational-example']
        if resource['status']=='reading-only':
            assert not resource.get('code_urls') and not resource.get('test_urls') and not resource.get('execution_examples')
        else:
            assert resource['code_urls'] and resource['test_urls'] and resource['execution_examples']
            assert {e['id'] for e in resource['execution_examples']}<=set(g['examples'])
            for example in resource['execution_examples']:
                ident=example['id']
                base=examples[ident]['release']['manifest'].rsplit('/',1)[0]+'/'
                assert all(u.startswith(base) for u in resource['code_urls']+resource['test_urls'])
                assert all((ROOT/u.removeprefix('https://hrkoyama.github.io/')).is_file() for u in resource['code_urls']+resource['test_urls'])
    assert all(g['scope'][lang] and g['title'][lang] for lang in ['ja','en'])
module='export const goals='+json.dumps(data['goals'],ensure_ascii=False,separators=(',',':'))+';\n'
module+='''export function matchGoals(query){
 const q=String(query).normalize('NFKC').toLowerCase().replace(/[‐‑‒–—−-]/g,' ').replace(/\\s+/g,' ').trim();
 if(!q)return [];
 return goals.filter(g=>{
  if(g.id==='molecular-dft' && /原子|atomic|hydrogen|helium/.test(q) && !/分子|固体|molecular|solid|periodic/.test(q))return false;
  if(g.id==='smooth-vortex' && /相対論|relativ|mhd|非圧縮|incompressible/.test(q))return false;
  if(g.id==='smooth-vortex' && /衝撃波|shock/.test(q) && !/含まない|なし|without|no shock/.test(q))return false;
  if(g.id==='shocks' && /相対論|relativ|mhd|衝撃波を含まない|衝撃波なし|without shocks?|no shocks?/.test(q))return false;
  return g.terms.some(t=>q.includes(t.normalize('NFKC').toLowerCase().replace(/[‐‑‒–—−-]/g,' ')));
 });
}
'''
(ROOT/'search/goals-data.mjs').write_text(module)
sections=[]
for lang in ['ja','en']:
    ja=lang=='ja'; parts=[f'<section data-site-language="{lang}" lang="{lang}" data-goal-filter-root data-goal-language="{lang}"><h1>'+('目的から計算法を選ぶ' if ja else 'Choose methods by your goal')+'</h1><p>'+(f'モデル・適用条件と公開状況を確認して進みます。{len(data["goals"])}の目的を案内します。' if ja else f'Check model assumptions and publication status. Explore {len(data["goals"])} goals.')+'</p>'+depth_teaser(ROOT,lang)+goal_filter_controls(lang,'goal',data['domains'])+'<nav aria-label="'+('目的を選ぶ' if ja else 'Choose a goal')+'">']
    parts += [f'<a class="goal-choice"{goal_attributes(g,methods)} href="#{g["id"]}-{lang}">{e(g["title"][lang])}<small>{e(goal_label(g,methods,lang))}</small></a>' for g in data['goals']]
    parts+=['</nav><p class="goal-status-key">'+('公開状況：関連コード・テストあり／解説のみ（専用実装なし）／解説あり・実装予定。コードの公開は、すべての用途での検証完了を意味しません。' if ja else 'Availability: related code and tests / reading only (no dedicated implementation) / reading available, implementation planned. Published code does not validate every application.')+'</p>']
    for g in data['goals']:
        parts += [f'<article class="goal-card"{goal_attributes(g,methods)} id="{g["id"]}-{lang}"><h2>{e(g["title"][lang])}</h2><p>{e(g["scope"][lang])}</p><h3>'+('候補と適用条件' if ja else 'Candidates and conditions')+'</h3>']
        for m in goal_methods(g,methods):
            m.setdefault('url',m['reading'].get(lang) or m['reading'].get('en'))
            state={'educational-example':('関連コード・テストあり','Related code and tests available'),'reading-only':('解説のみ・専用実装なし','Reading only; no dedicated implementation'),'planned':('解説あり・実装予定','Reading available; implementation planned')}[m['status']][0 if ja else 1]
            parts += [f'<div class="goal-method"><h4>{e(m["name"][lang])}</h4><p class="goal-availability" data-status="{m["status"]}">{e(state)}</p><p>{e(m["summary"][lang])}</p><p class="goal-links">']
            def link(url,label):return f'<a href="{e(url,quote=True)}">{e(label)}</a> '
            reading=m['reading'].get(lang) or m['reading'].get('en')
            if reading:parts += [link(reading,'解説' if ja else 'Explanation')]
            if m['status']=='educational-example':
                for key,label in [('code_urls','関連コード' if ja else 'Related code'),('test_urls','関連テスト' if ja else 'Related tests')]:
                    if m.get(key):parts += [link(m[key][0],label)]
            else:parts+=['<span>'+('コード・テストは未公開' if ja else 'Code and tests are not published')+'</span>']
            detail=('式・文献・検証案' if ja else 'Equations, sources and verification plans') if m.get('resource_type')=='model' else ('適用条件・文献' if ja else 'Conditions and references')
            parts += [link(m['url'],detail),'</p></div>']
        if g['examples']:
            parts+=['<h3>'+('固定入力から実行・検証する' if ja else 'Run and validate fixed inputs')+'</h3><ul>']
            for ident in g['examples']:parts += ['<li>'+link('/numerical-methods-atlas/code-and-data/examples/'+ident+'/?lang='+lang,examples[ident]['name'][lang])+'</li>']
            parts+=['</ul>']
        note=('関連コード・テストは教育用例です。各手法の全変種や目的全体の検証を意味しません。' if ja else 'Related educational code and tests do not validate every variant or the entire application.') if any(m['status']=='educational-example' for m in goal_methods(g,methods)) else ('この目的の専用コード・実行テストは未公開です。解説と今後の検証案を参照してください。' if ja else 'Dedicated code and executable tests for this goal are not published. See the reading and proposed verification.')
        parts+=['<p class="note">'+note+'</p><p><a href="#top">'+('目的一覧に戻る' if ja else 'Back to goals')+'</a></p></article>']
    parts+=['</section>'];sections.append(''.join(parts))
html='''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title data-page-title-ja="目的から計算法を選ぶ | 数値計算法アトラス" data-page-title-en="Choose methods by goal | Numerical Methods Atlas">目的から計算法を選ぶ | 数値計算法アトラス</title><meta name="description" content="流体・量子化学・DFT・温度制御・生物モデルの目的から、適用条件と実装・解説の公開状況を確認。"><link rel="canonical" href="https://hrkoyama.github.io/numerical-methods-atlas/start/"><style>.goal-choice{display:inline-block;margin:.4rem;padding:.7rem 1rem;border:1px solid #597563;border-radius:5px}.goal-choice small{display:block;font-size:.9rem;margin-top:5px}.goal-card{margin:2rem 0;padding:1.3rem;border:1px solid #bacbc1;border-radius:6px;scroll-margin-top:1rem}.goal-method{border-top:1px solid #ccd5ce;padding:.5rem 0}.goal-links{display:flex;flex-wrap:wrap;gap:.6rem}.goal-links a{display:inline-block;padding:.6rem;border:1px solid #729382;border-radius:4px;min-height:24px}.goal-availability{display:inline-block;border:1px solid #78917e;border-radius:4px;padding:.3rem .6rem;font-size:.9rem;font-weight:600}.goal-availability[data-status="reading-only"],.goal-availability[data-status="planned"]{border-style:dashed}.goal-card h4{font-size:1.1rem}.goal-card .note{font-size:.9rem}main{overflow-wrap:anywhere}</style></head><body class="profile-page" data-site-language-anchors="suffix"><main class="profile-main" id="top">'''+''.join(sections)+'</main></body></html>'
html=html.replace('</head>',goal_filter_assets(ROOT)+depth_assets(ROOT)+'</head>')
dest=ROOT/'numerical-methods-atlas/start';dest.mkdir(exist_ok=True);(dest/'index.html').write_text(html)
print('Built goal-based discovery:',len(data['goals']),'conditional routes.')
