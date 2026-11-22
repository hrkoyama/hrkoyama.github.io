#!/usr/bin/env python3
"""Publish every independent test problem as a bilingual image-to-problem card.

No numerical runtime is needed: verify the saved scientific-preview receipts.
"""
from collections import Counter
import hashlib
import html
import json
from pathlib import Path
import re
import struct
import xml.etree.ElementTree as ET
from atlas_execution_discovery import load_discovery, entry_url
from atlas_goal_availability import load_supplemental_examples
from atlas_problem_links import problem_url

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / 'numerical-methods-atlas'
DEST = ATLAS / 'gallery'
ORIGIN = 'https://hrkoyama.github.io'
ROUTE = '/numerical-methods-atlas/gallery/'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
esc = html.escape
inventory = json.loads((ATLAS / 'test-cases/index.json').read_text())
discovery = load_discovery(ROOT)
runnable = {x['problem_id']: x for x in discovery['examples']}
assert len(runnable) == len(discovery['examples']), 'Every runnable example must have a distinct gallery problem'
depth_catalog = json.loads((ROOT / 'catalog/atlas-depth-expansion.json').read_text())
supplements = {x['id']: x for x in load_supplemental_examples(ROOT, list(depth_catalog['case_problem_ids']))}
mapping = json.loads((ROOT / 'catalog/atlas-gallery.json').read_text())
manifest = json.loads((DEST / 'preview-manifest.json').read_text())
calculations = json.loads((DEST / 'calculations.json').read_text())
verification = json.loads((DEST / 'verification.json').read_text())
ids = [x['id'] for x in inventory['problems']]
assert set(runnable) <= set(ids), 'Every execution example must match an existing gallery problem'
for rows in [mapping['items'], manifest['items']]:
    assert len(rows) == len(ids) and {x['id'] for x in rows} == set(ids), 'Gallery must match every inventory ID exactly once'
assert manifest['calculations_sha256'] == sha(DEST / 'calculations.json')
assert set(calculations['cases']) == {x['id'] for x in mapping['items'] if x['kind'] == 'computed-preview'}
assert verification['failures'] == verification['errors'] == 0 and verification['passed'] > 0
receipts = {**manifest['source_sha256'], **verification['source_sha256']}
for path, digest in receipts.items():
    assert sha(ROOT / path) == digest, 'Regenerate previews or verification: ' + path
for name in ['preview-manifest.json', 'calculations.json', 'verification.json', '../test-cases/index.json']:
    path = (DEST / name).resolve()
    receipts[path.relative_to(ROOT).as_posix()] = sha(path)
for name in ['catalog/atlas-execution-discovery.json', 'scripts/atlas_execution_discovery.py',
             'catalog/atlas-depth-expansion.json', 'scripts/atlas_depth_release.py', 'scripts/atlas_goal_availability.py']:
    receipts[name] = sha(ROOT / name)
for supplement in supplements.values():
    receipts.update(supplement['source_sha256'])
visuals = {x['id']: x for x in manifest['items']}
inputs = {x['id']: x for x in mapping['items']}
items = []
for problem in inventory['problems']:
    image = visuals[problem['id']]
    path = (ROOT / image['image'].lstrip('/')).resolve()
    assert path.is_relative_to(ROOT) and sha(path) == image['image_sha256'], problem['id']
    # Dimension metadata is saved during authoring; normal refresh needs no Pillow.
    width, height = image['width'], image['height']
    assert width > 0 and height > 0
    if path.suffix == '.png':
        assert path.read_bytes()[:8] == b'\x89PNG\r\n\x1a\n'
        assert (width, height) == struct.unpack('>II', path.read_bytes()[16:24])
    else:
        assert path.suffix == '.webp'
    example = runnable.get(problem['id'])
    entry = ({'id': example['id'], 'url': {lang: entry_url(example['id'], lang) for lang in ['ja', 'en']},
              'outcome': example['outcome']} if example else None)
    extra_entries = []
    for extra in problem.get('supplemental_examples', []):
        supplement = supplements[extra['id']]
        assert depth_catalog['case_problem_ids'][extra['id']] == problem['id'], 'Unrelated supplement borrowed by a gallery problem'
        assert extra['url'] == supplement['url'] and extra['name'] == supplement['title'], 'Stale supplemental gallery metadata'
        extra_entries.append({'id': extra['id'], 'title': supplement['title'], 'group': supplement['group'],
            'url': {lang: ORIGIN + supplement['url'] + '?lang=' + lang for lang in ['ja', 'en']},
            **{key: supplement[key] for key in ['code_urls', 'test_urls']},
            **{key: ORIGIN + supplement[key] for key in ['download', 'results', 'verification']}})
    items.append({**problem, **image, 'visual_input': inputs[problem['id']], 'width': width, 'height': height,
                  'gallery_url': ORIGIN + ROUTE + '#' + problem['id'] + '-ja',
                  'problem_page': {lang: problem_url(problem['id'], lang) for lang in ['ja', 'en']},
                  'runnable': example is not None or bool(extra_entries), 'execution_entry': entry,
                  'supplemental_execution_entries': extra_entries})
runnable_problem_ids = {x['id'] for x in items if x['runnable']}
supplemental_problem_ids = {x['id'] for x in items if x['supplemental_execution_entries']}
supplemental_case_ids = {e['id'] for x in items for e in x['supplemental_execution_entries']}
counts = Counter(x['group'] for x in items)
source_labels = {
    'existing-figure': {'ja': '保存済みの結果図', 'en': 'Saved result figure'},
    'stored-data-plot': {'ja': '保存数値データを図示', 'en': 'Plot of saved numerical data'},
    'computed-preview': {'ja': '公開コードによる保存済みプレビュー', 'en': 'Saved preview from public code'},
}
groups = {x['id']: x for x in inventory['groups']}
def link(url, label):
    return '<a href="' + esc(url) + '">' + esc(label) + '</a>'
sections = []
for lang in ['ja', 'en']:
    ja = lang == 'ja'
    body = '<section data-site-language="' + lang + '" data-gallery lang="' + lang + '">'
    body += '<p class="eyebrow">NUMERICAL METHODS ATLAS · VISUAL INDEX</p><h1>' + ('絵から探す：全' + str(len(ids)) + 'のテスト計算' if ja else 'Browse by picture: all ' + str(len(ids)) + ' test problems') + '</h1>'
    body += '<p class="intro gallery-intro">' + (f'図を選ぶと、その問題の方程式・厳密解や参照解・計算法・公開コードをまとめて確認できます。実行・検証例がある{len(runnable_problem_ids)}問題には、固定入力・コード・結果の確かめ方も案内します。' if ja else f'Select a picture to explore the problem’s equations, exact or reference solutions, methods and published code. For {len(runnable_problem_ids)} runnable problems, find fixed inputs and validation as well.') + '</p>'
    body += '<nav class="resource-nav">' + ''.join(link(url, label) for url, label in [
        ('/numerical-methods-atlas/?lang=' + lang, 'アトラス冒頭' if ja else 'Atlas home'),
        ('/numerical-methods-atlas/equations/?lang=' + lang, '数式から探す' if ja else 'Browse by equation'),
        ('/numerical-methods-atlas/test-cases/?lang=' + lang, '問題台帳と数え方' if ja else 'Inventory and counting rules'),
        ('/numerical-methods-atlas/?lang=' + lang + '#/figures', '図版・比較ツール' if ja else 'Figures and comparison tools'),
    ]) + '</nav>'
    body += '<div class="gallery-tools"><label for="gallery-query-' + lang + '">' + ('問題名・現象で絞り込む（日英対応）' if ja else 'Filter by problem or phenomenon (Japanese / English)') + '</label><div class="gallery-search-row"><input id="gallery-query-' + lang + '" type="search" placeholder="' + ('例：Poisson、渦、衝撃波' if ja else 'e.g. Poisson, vortex, shock') + '"><button type="button" data-gallery-reset>' + ('絞り込みを解除' if ja else 'Reset filters') + '</button></div><details class="gallery-domain-filter"><summary>' + ('分野で絞り込む' if ja else 'Filter by domain') + '</summary><div class="gallery-groups" role="group" aria-label="' + ('分野' if ja else 'Domain') + '">'
    body += '<button type="button" data-gallery-group="all" aria-pressed="true">' + ('すべて' if ja else 'All') + ' (' + str(len(ids)) + ')</button>'
    for g in inventory['groups']:
        body += '<button type="button" data-gallery-group="' + g['id'] + '" aria-pressed="false">' + esc(g[lang]) + ' (' + str(counts[g['id']]) + ')</button>'
    body += '</div></details><div class="gallery-execution-filter"><button type="button" data-gallery-runnable aria-pressed="false" aria-describedby="gallery-illustration-note-' + lang + '">' + (f'実行・検証例あり {len(runnable_problem_ids)}' if ja else f'Runnable and validated: {len(runnable_problem_ids)}') + '</button><span>' + ('分野・検索語と組み合わせて絞り込めます' if ja else 'Combine with a domain and search terms') + '</span></div><p class="gallery-count" data-gallery-count role="status" aria-live="polite">' + (f'{len(ids)} / {len(ids)} 問題を表示' if ja else f'Showing {len(ids)} of {len(ids)} problems') + '</p></div>'
    body += '<details class="gallery-policy"><summary>' + ('図の条件・検証範囲・数え方' if ja else 'Image conditions, validation scope and counting rules') + '</summary>'
    body += '<p class="gallery-note" id="gallery-illustration-note-' + lang + '">' + ('画像は保存済みの図版・数値データ・プレビュー計算です。「実行・検証例あり」は、固定入力からJSON/CSVを作り結果を判定する経路がある印です。画像の計算条件は「条件・根拠」、再実行する条件は実行例の入力で確認してください。画像と固定入力の条件は一致するとは限りません。' if ja else 'Images are saved figures, numerical data or preview calculations. A runnable badge identifies a fixed-input path that produces JSON/CSV with acceptance checks. See “Conditions and evidence” for image settings and the execution input for rerun settings; these need not match.') + '</p>'
    body += '<p class="gallery-note">' + (f'{len(ids)}は手法・格子・刻み違いを統合した問題数です。解に加え、誤差・残差・収束の図も含み、共有図は説明に明記しています。図示用の9問題の計算記録と、代表{len(runnable)}問題の実行・検証記録は別に確認できます。' if ja else f'The {len(ids)} problems merge method, grid and time-step variants. Visuals include solutions, errors, residuals and convergence; captions identify shared figures. Records for nine preview calculations and the {len(runnable)} representative execution examples remain separate.') + '</p>'
    body += '<p class="gallery-note">' + (f'共通{len(runnable)}実行例の台帳と、別配布の補助{len(supplements)}例は区別しています。このギャラリーでは補助{len(supplemental_case_ids)}例が{len(supplemental_problem_ids)}問題に接続し、同じ問題への手法追加は重複加算しません。' if ja else f'The common {len(runnable)}-example registry remains separate from the {len(supplements)} supplementary cases. This gallery links {len(supplemental_case_ids)} supplements to {len(supplemental_problem_ids)} problems; additional methods do not duplicate a problem count.') + '</p></details><ul class="gallery-grid">'
    for x in items:
        example = runnable.get(x['id'])
        extras = x['supplemental_execution_entries']
        search = ' '.join([x['id'], *x['name'].values(), *groups[x['group']].values(), *x['caption'].values(), x['chapter'],
                           *([*example['keywords'], *example['outcome'].values()] if example else []),
                           *[word for e in extras for word in [e['id'], *e['title'].values(), *supplements[e['id']]['method_ids']]],
                           *(['実行・検証例あり 実行 検証 runnable execution validated'] if x['runnable'] else [])])
        reading = x['reading'][lang]
        destination = entry_url(example['id'], lang) if example else (extras[0]['url'][lang] if extras else reading)
        hub = x['problem_page'][lang]
        fallback = ja and '/en/read/' in reading
        body += '<li class="gallery-tile" id="' + x['id'] + '-' + lang + '" data-problem-id="' + x['id'] + '" data-group="' + x['group'] + '" data-runnable="' + str(x['runnable']).lower() + '" data-search="' + esc(search) + '">'
        image_label = 'の方程式・参照解・手法・コードへ' if ja else ': open equations, references, methods and code'
        body += '<a class="gallery-image-link" href="' + esc(hub) + '" aria-label="' + esc(x['name'][lang] + image_label) + '"><img src="' + esc(x['image']) + '" alt="' + esc(x['name'][lang] + ' — ' + x['caption'][lang]) + '" width="' + str(x['width']) + '" height="' + str(x['height']) + '" loading="lazy" decoding="async"></a>'
        body += '<div class="gallery-card-body"><p class="gallery-meta">' + esc(groups[x['group']][lang]) + '</p>'
        if example:
            body += '<p class="gallery-execution-badge">' + link(destination, '実行・検証例あり →' if ja else 'Run and validate →') + '</p>'
        for extra in extras:
            body += '<p class="gallery-execution-badge gallery-supplemental-badge" data-supplemental-execution="' + extra['id'] + '">' + link(extra['url'][lang], ('補助実行例：' if ja else 'Supplementary run: ') + extra['title'][lang]) + '</p>'
        body += '<h2>' + link(hub, x['name'][lang]) + '</h2><p>' + esc(x['caption'][lang]) + '</p><p class="gallery-meta">' + source_labels[x['source_kind']][lang] + (' · 英語の解説（日本語版未公開）' if fallback else '') + '</p><nav class="gallery-card-links">'
        body += link(reading, '解説へ →' if ja else 'Read →') + link('/numerical-methods-atlas/test-cases/?lang=' + lang + '#' + x['id'] + ('' if ja else '-en'), '条件・根拠' if ja else 'Conditions and evidence') + link(x['image'], '画像を拡大' if ja else 'Full-size image') + '</nav></div></li>'
    body += '</ul><p class="gallery-empty" data-gallery-empty hidden>' + ('該当する問題がありません。検索語や分野を変えてください。' if ja else 'No matching problems. Try another query or domain.') + '</p><p>'
    body += link('index.json', '画像・解説・出典の全件JSON' if ja else 'All images, readings and sources / JSON') + ' · ' + link('calculations.json', '図示用9計算の入力・値・数値検査' if ja else 'Inputs, values and checks for nine preview calculations') + ' · ' + link('verification.json', 'プレビューの実行確認' if ja else 'Preview verification') + ' · ' + link('/scripts/render-atlas-gallery.py', '図の再生成スクリプト' if ja else 'Preview reproduction script')
    body += '</p><p>' + link('/using/?lang=' + lang, '利用・引用' if ja else 'Reuse and citation') + '</p></section>'
    sections.append(body)
doc = '<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title data-page-title-ja="絵から探す：58のテスト計算 | 数値計算法アトラス" data-page-title-en="Browse 58 test problems by picture | Numerical Methods Atlas">絵から探す：58のテスト計算 | 数値計算法アトラス</title><meta name="description" content="数値計算法アトラス全58問題の画像一覧。波形、衝撃波、渦、重力、Poisson問題、時間積分、関数近似から解説へ。A visual index of all 58 numerical test problems."><link rel="canonical" href="' + ORIGIN + ROUTE + '">'
for style in ['atlas-resources', 'atlas-gallery']:
    doc += '<link rel="stylesheet" href="/styles/' + style + '.css?v=' + sha(ROOT / 'styles' / (style + '.css'))[:12] + '">'
doc=doc.replace('58',str(len(ids)))
doc += '<script type="module" src="/atlas-gallery.mjs?v=' + sha(ROOT / 'atlas-gallery.mjs')[:12] + '"></script></head><body class="profile-page"><main id="main" class="profile-main atlas-resource-main atlas-gallery-main">' + ''.join(sections) + '</main></body></html>\n'
(DEST / 'index.html').write_text(doc)
(DEST / 'index.json').write_text(json.dumps({'schema_version': 1, 'url': ORIGIN + ROUTE, 'reviewed_on': mapping['reviewed_on'], 'scope': mapping['scope'], 'counts': {'test_problems': len(ids), 'runnable_problems': len(runnable_problem_ids), 'common_runnable_problems': len(runnable), 'supplemental_runnable_problems': len(supplemental_problem_ids), 'supplemental_case_count': len(supplemental_case_ids), 'supplemental_release_case_count': len(supplements), 'groups': dict(counts), 'visual_sources': dict(Counter(x['source_kind'] for x in items))}, 'items': items, 'source_sha256': receipts}, ensure_ascii=False, indent=2) + '\n')

# Preserve the old route as an entrance to the complete index. Original visual
# experiments remain available under #/figures, including their comparison tools.
app = ATLAS / 'app.js'
text = app.read_text()
marker = " if(type==='gallery'){location.replace('/numerical-methods-atlas/gallery/?lang='+currentLanguage());return;}"
if marker not in text:
    target = " if(type==='read' && !documents[parts[1]]) {"
    assert target in text
    text = text.replace(target, marker + '\n' + target, 1)
text = re.sub(r'gallery,(?:figures:gallery,)+movies:moviesPage', 'gallery,figures:gallery,movies:moviesPage', text)
if 'figures:gallery' not in text:
    text = text.replace('methods:methodPage,gallery,', 'methods:methodPage,gallery,figures:gallery,', 1)
text = text.replace("gallery:'Numerical gallery',movies:", "gallery:'Numerical gallery',figures:'Figures and comparison tools',movies:")
assert 'figures:gallery' in text
app.write_text(text)
path = ATLAS / 'sitemap.xml'
xml = ET.parse(path); ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
if ORIGIN + ROUTE not in {x.text for x in xml.getroot().findall('.//{*}loc')}:
    ET.SubElement(ET.SubElement(xml.getroot(), ns + 'url'), ns + 'loc').text = ORIGIN + ROUTE
ET.register_namespace('', ns[1:-1]); xml.write(path, encoding='utf-8', xml_declaration=True)
guide = ROOT / 'llms.txt'
lines = [x for x in guide.read_text().splitlines() if not x.startswith('- [Atlas-wide visual test index]')]
guide.write_text('\n'.join(lines).rstrip() + '\n- [Atlas-wide visual test index](' + ORIGIN + ROUTE + '): all ' + str(len(ids)) + ' independent problems, one mapped visual each, bilingual readings, source receipts and JSON. Shared figures and newly computed results are labeled.\n')
print('Built complete visual index:', len(ids), 'problems.')
