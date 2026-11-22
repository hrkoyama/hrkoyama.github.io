#!/usr/bin/env python3
"""Build the bilingual connection guide without extending component validation."""
import argparse
from copy import deepcopy
import hashlib
from html import escape as esc
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlparse

from atlas_crossovers import BASE, crossover_assets


ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://hrkoyama.github.io'
LANGUAGES = ('ja', 'en')


def fail(condition, message):
    if not condition:
        raise ValueError(message)


def bilingual(value, label):
    fail(isinstance(value, dict) and all(isinstance(value.get(lang), str) and value[lang].strip() for lang in LANGUAGES), label + ': Japanese and English text are required')


def read_json(path):
    return json.loads(path.read_text())


def load_catalog(root=ROOT):
    return read_json(Path(root) / 'catalog/atlas-crossovers.json')


def local_target(root, url, check_anchor=True):
    """Reject invented local destinations, including missing explanation anchors."""
    parsed = urlparse(url)
    if parsed.netloc and parsed.netloc != urlparse(ORIGIN).netloc:
        return
    fail(parsed.path.startswith('/'), 'A local evidence link must use an absolute site path: ' + url)
    path = Path(root) / unquote(parsed.path).lstrip('/')
    if parsed.path.endswith('/'):
        path /= 'index.html'
    fail(path.is_file(), 'Missing local evidence destination: ' + url)
    if check_anchor and parsed.fragment and path.suffix == '.html':
        text = path.read_text()
        anchor = unquote(parsed.fragment)
        fail(re.search(r'\bid\s*=\s*[\"\']' + re.escape(anchor) + r'[\"\']', text) is not None, 'Missing explanation anchor: ' + url)


def evidence_context(root):
    root = Path(root)
    canonical_path = root / 'catalog/atlas-methods.json'
    published_path = root / 'numerical-methods-atlas/methods/index.json'
    registry_path = root / 'numerical-methods-atlas/code-and-data/examples.json'
    canonical = read_json(canonical_path)
    published = read_json(published_path)
    methods = {method['id']: method for method in canonical['methods']}
    resolved = {method['id']: method for method in published['methods']}
    fail(methods.keys() == resolved.keys(), 'Rebuild published methods before the connection guide')
    for ident, method in methods.items():
        fail(method['status'] == resolved[ident]['status'], 'Published method status is stale: ' + ident)
    registry = read_json(registry_path)
    receipt_url = registry['verification_receipt']
    receipt_path = root / urlparse(receipt_url).path.lstrip('/')
    public_path = receipt_path.with_name(receipt_path.stem + '-public.json')
    if public_path.is_file():
        receipt_path = public_path
        receipt_url = receipt_url.removesuffix('.json') + '-public.json'
    receipt = read_json(receipt_path)
    fail(receipt.get('passed') is True and receipt.get('registry_sha256') == hashlib.sha256(registry_path.read_bytes()).hexdigest(), 'A matching successful public execution receipt is required')
    checks = {entry['id']: entry for entry in receipt['examples']}
    return {'methods': methods, 'resolved_methods': resolved,
            'registry': registry, 'examples': {entry['id']: entry for entry in registry['examples']},
            'receipt': receipt, 'checks': checks, 'receipt_url': receipt_url,
            'sources': [canonical_path, published_path, registry_path, receipt_path]}


def validate_catalog(data, root=ROOT):
    """Validate IDs and provenance before writing any public output."""
    context = evidence_context(root)
    for key in ('title', 'intro', 'policy'):
        bilingual(data.get(key), key)
    for key in ('title', 'description', 'action'):
        bilingual(data.get('home', {}).get(key), 'home.' + key)
    fail(data.get('schema_version') == 1, 'Unsupported crossover schema version')
    fail(isinstance(data.get('reviewed_on'), str), 'A review date is required')
    math = data.get('math_families', [])
    math_ids = [entry['id'] for entry in math]
    fail(len(set(math_ids)) == len(math_ids) and math_ids, 'Unique math-family IDs are required')
    for entry in math:
        bilingual(entry.get('name'), entry['id'] + '.name')
        bilingual(entry.get('summary'), entry['id'] + '.summary')
        for reading in entry.get('reading', []):
            bilingual(reading.get('label'), entry['id'] + '.reading.label')
            bilingual(reading.get('url'), entry['id'] + '.reading.url')
            for url in reading['url'].values():
                local_target(root, url)
    references = data.get('references', [])
    reference_ids = [entry['id'] for entry in references]
    fail(len(set(reference_ids)) == len(reference_ids), 'Duplicate reference IDs')
    for reference in references:
        bilingual(reference.get('review'), reference['id'] + '.review')
        fail(reference.get('url', '').startswith('https://'), 'A reference URL is required: ' + reference['id'])
        fail(bool(reference.get('review_level')), 'A reference review level is required: ' + reference['id'])
    routes = data.get('routes', [])
    route_ids = [route['id'] for route in routes]
    fail(set(route_ids) == {'dft-md', 'reaction-transport', 'poisson-fields'} and len(route_ids) == 3, 'The guide requires its three scoped routes')
    global_anchors = set()
    for route in routes:
        label = route['id']
        for key in ('title', 'summary'):
            bilingual(route.get(key), label + '.' + key)
        fail(route.get('math_ids') and set(route['math_ids']) <= set(math_ids), label + ': unknown math family')
        coupled = route.get('coupled_validation', {})
        fail(coupled.get('status') == 'not-executed' and coupled.get('example_ids') == [], label + ': route coupled validation must remain not-executed with empty example_ids')
        bilingual(coupled.get('scope'), label + '.coupled_validation.scope')
        stages = route.get('stages', [])
        stage_ids = [stage['id'] for stage in stages]
        fail(stages and len(stage_ids) == len(set(stage_ids)), label + ': unique stage IDs are required')
        for stage in stages:
            stage_label = label + '.' + stage['id']
            fail(stage['id'] not in global_anchors, 'Stage IDs must be globally unique: ' + stage['id'])
            global_anchors.add(stage['id'])
            for key in ('title', 'summary', 'gap'):
                bilingual(stage.get(key), stage_label + '.' + key)
            method_ids = stage.get('method_ids', [])
            fail(set(method_ids) <= context['methods'].keys(), stage_label + ': unknown method ID')
            if stage.get('model_ids'):
                models = {model['id'] for model in read_json(Path(root) / 'numerical-methods-atlas/assets/biological-models.json')['models']}
                fail(set(stage['model_ids']) <= models, stage_label + ': unknown biological model ID')
            examples = stage.get('example_ids', [])
            fail(set(examples) <= context['examples'].keys(), stage_label + ': unknown execution example')
            if examples:
                fail(stage.get('example_role') in ('exact-stage', 'component-only'), stage_label + ': examples require an explicit example_role')
                fail(stage['id'] not in {'nuclear-forces', 'first-principles-md', 'thermostat'}, stage_label + ': no force/AIMD/thermostat execution is available; component examples cannot validate this stage')
            for ident in examples:
                example = context['examples'][ident]
                fail(set(example['method_ids']) & set(method_ids), stage_label + ': execution is not linked to a declared component method: ' + ident)
                checked = context['checks'].get(ident, {})
                fail(checked.get('execution', {}).get('completed') is True and checked.get('validation', {}).get('passed') is True, stage_label + ': execution and numerical checks must both pass: ' + ident)
            for reading in stage.get('reading', []):
                bilingual(reading.get('label'), stage_label + '.reading.label')
                bilingual(reading.get('url'), stage_label + '.reading.url')
                for url in reading['url'].values():
                    local_target(root, url)
            for ident in method_ids:
                method = context['resolved_methods'][ident]
                for lang in LANGUAGES:
                    local_target(root, '/numerical-methods-atlas/methods/' + ident + '/')
                for key in ('code_urls', 'test_urls'):
                    for url in method.get(key, []):
                        local_target(root, url)
        edges = route.get('connections', [])
        edge_ids = [edge['id'] for edge in edges]
        fail(edges and len(edge_ids) == len(set(edge_ids)), label + ': unique connection IDs are required')
        for edge in edges:
            edge_label = label + '.' + edge['id']
            fail(edge['id'] not in global_anchors, 'Connection IDs must be globally unique: ' + edge['id'])
            global_anchors.add(edge['id'])
            fail(edge.get('from') in stage_ids and edge.get('to') in stage_ids and edge['from'] != edge['to'], edge_label + ': missing or identical connection endpoints')
            fail(edge.get('math_ids') and set(edge['math_ids']) <= set(math_ids), edge_label + ': unknown math family')
            fail(edge.get('connection_kind') in CONNECTION_KINDS, edge_label + ': unknown connection kind')
            for key in ('title', 'exchanged_quantity', 'shared_math', 'what_differs', 'validation_required', 'existing_evidence'):
                bilingual(edge.get(key), edge_label + '.' + key)
            coupled = edge.get('coupled_validation', {})
            fail(coupled.get('status') == 'not-executed' and coupled.get('example_ids') == [], edge_label + ': edge coupled validation must remain not-executed; do not borrow component example_ids')
            bilingual(coupled.get('scope'), edge_label + '.coupled_validation.scope')
            fail(set(edge.get('reference_ids', [])) <= set(reference_ids), edge_label + ': unknown reference ID')
        fail(set(route.get('reference_ids', [])) <= set(reference_ids), label + ': unknown reference ID')
    return context


def link(url, label, attrs=''):
    return '<a href="' + esc(url, quote=True) + '"' + attrs + '>' + esc(label) + '</a>'


def stage_state(stage, context):
    if stage.get('example_ids'):
        return 'fixed-input' if stage['example_role'] == 'exact-stage' else 'component-only'
    return 'planned' if any(context['methods'][ident]['status'] == 'planned' for ident in stage.get('method_ids', [])) else 'reading'


def stage_state_label(state, lang):
    labels = {'fixed-input': ('固定条件の実行例', 'Fixed-input execution example'),
              'component-only': ('要素例のみ', 'Component examples only'),
              'planned': ('解説あり・専用実装予定', 'Reading / dedicated implementation planned'),
              'reading': ('解説・段階の実行例なし', 'Reading / no stage execution example')}
    return labels[state][0 if lang == 'ja' else 1]


def stage_evidence(stage, context):
    return {'stage_status': stage_state(stage, context),
            'methods': [{key: context['resolved_methods'][ident].get(key) for key in ('id', 'name', 'status', 'reading', 'code_urls', 'test_urls', 'code_mapping_scope')} for ident in stage.get('method_ids', [])],
            'examples': [{'id': ident, 'name': context['examples'][ident]['name'], 'scope': context['examples'][ident]['scope'],
                          'url': ORIGIN + '/numerical-methods-atlas/code-and-data/examples/' + ident + '/',
                          'process_completed': context['checks'][ident]['execution']['completed'],
                          'numerical_checks_passed': context['checks'][ident]['validation']['passed']} for ident in stage.get('example_ids', [])]}


def math_tags(ids, math, lang):
    return '<div class="crossover-tags">' + ''.join('<span class="crossover-tag">' + esc(math[ident]['name'][lang]) + '</span>' for ident in ids) + '</div>'


def method_html(method, lang):
    ja = lang == 'ja'
    labels = {'educational-example': ('教育用例あり（別用途を含む）', 'Educational examples (including other uses)'),
              'reading-only': ('解説のみ・専用実装なし', 'Reading only / no dedicated implementation'),
              'planned': ('解説あり・実装予定', 'Reading / implementation planned')}
    body = '<li data-method-id="' + method['id'] + '" data-method-status="' + method['status'] + '">' + link('/numerical-methods-atlas/methods/' + method['id'] + '/?lang=' + lang, method['name'][lang])
    body += ' <span class="crossover-status" data-state="' + method['status'] + '">' + labels[method['status']][0 if ja else 1] + '</span>'
    return body + '</li>'


def stage_html(stage, context, lang):
    ja = lang == 'ja'
    state = stage_state(stage, context)
    body = '<article class="crossover-stage" id="' + stage['id'] + '-' + lang + '" data-stage-id="' + stage['id'] + '" data-stage-status="' + state + '"><h4>' + esc(stage['title'][lang]) + '</h4><span class="crossover-status" data-state="' + state + '">' + stage_state_label(state, lang) + '</span><p>' + esc(stage['summary'][lang]) + '</p>'
    if stage.get('reading'):
        body += '<ul>' + ''.join('<li>' + link(reading['url'][lang], reading['label'][lang]) + '</li>' for reading in stage['reading']) + '</ul>'
    if stage.get('method_ids'):
        body += '<h5>' + ('手法の記録と現在の状態' if ja else 'Method records and current states') + '</h5><ul class="crossover-methods">' + ''.join(method_html(context['resolved_methods'][ident], lang) for ident in stage['method_ids']) + '</ul>'
    if stage.get('example_ids'):
        body += '<h5>' + ('既存の要素計算・実行の根拠' if ja else 'Existing component execution evidence') + '</h5><ul class="crossover-example-list">'
        for ident in stage['example_ids']:
            example = context['examples'][ident]
            body += '<li>' + link('/numerical-methods-atlas/code-and-data/examples/' + ident + '/?lang=' + lang, example['name'][lang]) + '<p>' + esc(example['scope'][lang]) + '</p><p class="crossover-provenance">' + ('実行完了・当該入力の数値判定合格。' if ja else 'Process completed; numerical checks passed for these inputs. ') + link(example['release']['download'], 'コード・テスト / ZIP' if ja else 'Code and tests / ZIP') + ' · ' + link(example['inputs']['url'], '固定入力' if ja else 'Fixed input') + ' · ' + link(context['receipt_url'], '追試記録' if ja else 'Rerun receipt') + '</p></li>'
        body += '</ul>'
    body += '<p class="crossover-stage-gap"><strong>' + ('残る差：' if ja else 'Remaining gap: ') + '</strong>' + esc(stage['gap'][lang]) + '</p></article>'
    return body


CONNECTION_KINDS = {
    'handoff': ('量を受け渡す接続', 'Quantity handoff'),
    'model-application': ('モデルを適用する接続', 'Model application'),
    'component-reference': ('要素計算との比較', 'Component comparison'),
    'operator-correspondence': ('共通演算子の対応', 'Shared operator correspondence'),
}


def connection_kind_label(edge, lang):
    return CONNECTION_KINDS[edge['connection_kind']][0 if lang == 'ja' else 1]


def connection_scope_label(edge, lang):
    labels = {
        'handoff': ('連成実行：未実施。', 'Coupled execution: not performed. '),
        'model-application': ('空間モデルの実行：未実施。', 'Spatial-model execution: not performed. '),
        'component-reference': ('要素例を参照する範囲：', 'Scope of the component reference: '),
        'operator-correspondence': ('対応関係を比較する範囲：', 'Scope of the operator correspondence: '),
    }
    return labels[edge['connection_kind']][0 if lang == 'ja' else 1]


def connection_flow_html(route, stages, context, lang):
    """Show declared handoffs and branches, with each node's own evidence state."""
    body = '<ul class="crossover-flow">'
    for edge in route['connections']:
        body += '<li class="crossover-flow-edge" data-crossover-flow-edge="' + edge['id'] + '" data-from="' + edge['from'] + '" data-to="' + edge['to'] + '"><div class="crossover-flow-pair">'
        for endpoint in ('from', 'to'):
            stage = stages[edge[endpoint]]
            state = stage_state(stage, context)
            if endpoint == 'to':
                body += '<span class="crossover-flow-arrow" aria-hidden="true">' + ('↔' if edge['connection_kind'] in ('component-reference', 'operator-correspondence') else '→') + '</span>'
            body += '<a class="crossover-flow-node" data-crossover-flow-node="' + endpoint + '" data-stage-status="' + state + '" href="#' + stage['id'] + '-' + lang + '"><span class="crossover-flow-name">' + esc(stage['title'][lang]) + '</span><span class="crossover-status" data-state="' + state + '">' + stage_state_label(state, lang) + '</span></a>'
        body += '</div><p class="crossover-flow-detail">' + link('#' + edge['id'] + '-' + lang, edge['title'][lang]) + '<small data-coupled-status="not-executed">' + connection_kind_label(edge, lang) + '</small></p></li>'
    return body + '</ul>'


def connection_html(edge, stages, math, lang):
    ja = lang == 'ja'
    labels = [('exchanged_quantity', '受け渡す量・対応する量', 'Exchanged or corresponding quantity'),
              ('shared_math', '共通する数理', 'Shared mathematics'),
              ('what_differs', '接続先で異なる点', 'What changes across the connection'),
              ('existing_evidence', '既存の根拠（要素ごと）', 'Existing evidence (components)'),
              ('validation_required', '接続を検証するための条件', 'Validation required for the connection')]
    body = '<article class="crossover-edge" id="' + edge['id'] + '-' + lang + '" data-connection-id="' + edge['id'] + '"><h4>' + esc(edge['title'][lang]) + '</h4><p class="crossover-endpoints">' + link('#' + edge['from'] + '-' + lang, stages[edge['from']]['title'][lang]) + ' <span aria-hidden="true">↔</span> ' + link('#' + edge['to'] + '-' + lang, stages[edge['to']]['title'][lang]) + '</p>'
    body += math_tags(edge['math_ids'], math, lang) + '<dl>'
    for key, title_ja, title_en in labels:
        classname = ' class="crossover-existing"' if key == 'existing_evidence' else ' class="crossover-required"' if key == 'validation_required' else ''
        body += '<div' + classname + '><dt>' + (title_ja if ja else title_en) + '</dt><dd>' + esc(edge[key][lang]) + '</dd></div>'
    body += '</dl><p class="crossover-no-coupling" data-coupled-status="not-executed"><strong>' + connection_scope_label(edge, lang) + '</strong>' + esc(edge['coupled_validation']['scope'][lang]) + '</p></article>'
    return body


def render_language(data, context, lang):
    ja = lang == 'ja'
    math = {entry['id']: entry for entry in data['math_families']}
    references = {entry['id']: entry for entry in data.get('references', [])}
    body = '<section data-crossover-root data-site-language="' + lang + '" lang="' + lang + '"><p class="eyebrow">NUMERICAL METHODS ATLAS · CONNECTIONS</p><h1>' + esc(data['title'][lang]) + '</h1><p class="intro crossover-intro">' + esc(data['intro'][lang]) + '</p>'
    body += '<nav class="resource-nav">' + link('/numerical-methods-atlas/?lang=' + lang, 'アトラス冒頭' if ja else 'Atlas home') + link('/numerical-methods-atlas/methods/?lang=' + lang, '手法の見取り図' if ja else 'Method map') + link('/numerical-methods-atlas/depth/?lang=' + lang, '実装・検証範囲' if ja else 'Implementation and validation scope') + '</nav>'
    body += '<form class="crossover-controls" data-crossover-controls hidden aria-label="' + ('共通する数理で経路を絞る' if ja else 'Filter routes by shared mathematics') + '"><div class="crossover-control-row"><div><label for="crossover-math-' + lang + '">' + ('共通する数理' if ja else 'Shared mathematics') + '</label><select id="crossover-math-' + lang + '" data-crossover-math><option value="all">' + ('すべての数理' if ja else 'All mathematics') + '</option>'
    body += ''.join('<option value="' + entry['id'] + '">' + esc(entry['name'][lang]) + '</option>' for entry in data['math_families']) + '</select></div><button type="button" data-crossover-reset>' + ('絞り込みを解除' if ja else 'Clear filter') + '</button></div><p class="crossover-filter-note">' + ('条件はURLで共有できます。接続の詳細へのリンクを開くと、その経路を表示します。' if ja else 'The filter is shareable in the URL. Following a detail link reveals its route.') + '</p><p class="crossover-filter-note" data-crossover-count role="status" aria-live="polite" aria-atomic="true">' + ('3 / 3 の経路を表示' if ja else 'Showing 3 of 3 routes') + '</p></form>'
    body += '<noscript><p>' + ('すべての経路と詳細を表示しています。' if ja else 'All routes and their details are shown.') + '</p></noscript><p data-crossover-empty hidden>' + ('この数理に一致する経路はありません。絞り込みを解除してください。' if ja else 'No routes match this mathematics. Clear the filter.') + '</p><div class="crossover-route-grid">'
    for route in data['routes']:
        body += '<article class="crossover-route-card" data-crossover-card data-route-id="' + route['id'] + '" data-math-ids="' + ' '.join(route['math_ids']) + '"><h2>' + link('#' + route['id'] + '-' + lang, route['title'][lang]) + '</h2><p>' + esc(route['summary'][lang]) + '</p>' + math_tags(route['math_ids'], math, lang) + link('#' + route['id'] + '-' + lang, '接続の条件と根拠を見る' if ja else 'Read connection conditions and evidence', ' class="crossover-card-link"') + '</article>'
    body += '</div>'
    body += '<p class="crossover-policy">' + esc(data['policy'][lang]) + '</p>'
    body += '<details class="crossover-math-guide"><summary>' + ('共通する数理の観点を読む' if ja else 'Read the shared mathematical perspectives') + '</summary>'
    for entry in data['math_families']:
        body += '<div><h3>' + esc(entry['name'][lang]) + '</h3><p>' + esc(entry['summary'][lang]) + '</p>'
        if entry.get('reading'):
            body += '<p>' + ' · '.join(link(reading['url'][lang], reading['label'][lang]) for reading in entry['reading']) + '</p>'
        body += '</div>'
    body += '</details>'
    for route in data['routes']:
        stages = {stage['id']: stage for stage in route['stages']}
        body += '<section class="crossover-route" id="' + route['id'] + '-' + lang + '" data-crossover-route data-route-id="' + route['id'] + '" data-math-ids="' + ' '.join(route['math_ids']) + '"><h2>' + esc(route['title'][lang]) + '</h2><p class="crossover-route-summary">' + esc(route['summary'][lang]) + '</p>' + math_tags(route['math_ids'], math, lang)
        body += '<div class="crossover-scope" data-coupled-status="not-executed"><strong>' + ('この経路で確認できる範囲：' if ja else 'Evidence scope of this route: ') + '</strong>' + esc(route['coupled_validation']['scope'][lang]) + '</div>'
        body += '<h3>' + ('接続を選ぶ' if ja else 'Choose a connection') + '</h3>' + connection_flow_html(route, stages, context, lang)
        body += '<h3>' + ('各要素の解説と現在の根拠' if ja else 'Readings and current evidence for each component') + '</h3><div class="crossover-stages">' + ''.join(stage_html(stage, context, lang) for stage in route['stages']) + '</div>'
        body += '<h3>' + ('量の受け渡し・共通数理・検証の違い' if ja else 'Quantities, shared mathematics and different validation needs') + '</h3>' + ''.join(connection_html(edge, stages, math, lang) for edge in route['connections'])
        ids = route.get('reference_ids', [])
        if ids:
            body += '<h3>' + ('一次文献と確認した範囲' if ja else 'Primary references and scope of review') + '</h3><ul class="crossover-reference-list">'
            for ident in ids:
                ref = references[ident]
                title = ref['title'][lang] if isinstance(ref['title'], dict) else ref['title']
                author = ref.get('author', ref.get('authors', ''))
                if isinstance(author, list): author = ', '.join(author)
                body += '<li id="reference-' + route['id'] + '-' + ident + '-' + lang + '">' + esc(str(author)) + ' (' + esc(str(ref['year'])) + '). ' + link(ref['url'], title) + '<p class="crossover-reference-review">' + esc(ref['review'][lang]) + '</p></li>'
            body += '</ul>'
        body += '</section>'
    body += '<p class="crossover-provenance">' + ('根拠の出典：' if ja else 'Evidence sources: ') + link('/catalog/atlas-crossovers.json', '接続の正本' if ja else 'Connection catalog') + ' · ' + link('/numerical-methods-atlas/methods/index.json', '手法台帳' if ja else 'Method registry') + ' · ' + link(context['registry']['url'], '実行例台帳' if ja else 'Execution registry') + ' · ' + link(context['receipt_url'], '現在の追試記録' if ja else 'Current rerun receipt') + ' · ' + link(BASE + 'index.json', '接続データ / JSON' if ja else 'Connection data / JSON') + ' · ' + link(BASE + 'index.md', '本文 / Markdown' if ja else 'Text / Markdown') + '</p></section>'
    return body


def render_markdown(data, context):
    lines = []
    references = {entry['id']: entry for entry in data.get('references', [])}
    for lang in LANGUAGES:
        ja = lang == 'ja'
        lines += ['# ' + data['title'][lang], '', data['intro'][lang], '', data['policy'][lang], '']
        for route in data['routes']:
            lines += ['## ' + route['title'][lang], '', '[HTML](' + ORIGIN + BASE + '?lang=' + lang + '#' + route['id'] + '-' + lang + ')', '', route['summary'][lang], '', ('この経路で確認できる範囲：' if ja else 'Evidence scope of this route: ') + route['coupled_validation']['scope'][lang], '']
            for stage in route['stages']:
                lines += ['### ' + stage['title'][lang], '', stage['summary'][lang], '', ('段階の状態: ' if ja else 'Stage state: ') + stage_state(stage, context), '']
                for reading in stage.get('reading', []):
                    lines += ['- [' + reading['label'][lang] + '](' + reading['url'][lang] + ')']
                for ident in stage.get('method_ids', []):
                    method = context['methods'][ident]
                    lines += ['- [' + method['name'][lang] + '](' + ORIGIN + '/numerical-methods-atlas/methods/' + ident + '/?lang=' + lang + '): ' + method['status']]
                for ident in stage.get('example_ids', []):
                    example = context['examples'][ident]
                    lines += ['- [' + example['name'][lang] + '](' + ORIGIN + '/numerical-methods-atlas/code-and-data/examples/' + ident + '/?lang=' + lang + '): ' + example['scope'][lang]]
                lines += ['', ('残る差: ' if ja else 'Remaining gap: ') + stage['gap'][lang], '']
            for edge in route['connections']:
                lines += ['### ' + edge['title'][lang], '', connection_kind_label(edge, lang), '']
                for key, title_ja, title_en in [('exchanged_quantity', '受け渡す量', 'Exchanged quantity'), ('shared_math', '共通する数理', 'Shared mathematics'), ('what_differs', '異なる点', 'What differs'), ('existing_evidence', '既存の要素根拠', 'Existing component evidence'), ('validation_required', '接続に必要な検証', 'Validation required')]:
                    lines += ['**' + (title_ja if ja else title_en) + ':** ' + edge[key][lang], '']
                lines += [connection_scope_label(edge, lang) + edge['coupled_validation']['scope'][lang], '']
            if route.get('reference_ids'):
                lines += ['### ' + ('一次文献と確認した範囲' if ja else 'Primary references and scope of review'), '']
                for ident in route['reference_ids']:
                    reference = references[ident]
                    title = reference['title'][lang] if isinstance(reference['title'], dict) else reference['title']
                    lines += ['- ' + str(reference['author']) + ' (' + str(reference['year']) + '). [' + title + '](' + reference['url'] + '). ' + reference['review'][lang]]
                lines += ['']
        lines += ['## ' + ('共通する数理' if ja else 'Shared mathematics'), '']
        for family in data['math_families']:
            lines += ['### ' + family['name'][lang], '', family['summary'][lang], '']
            for reading in family.get('reading', []):
                lines += ['- [' + reading['label'][lang] + '](' + reading['url'][lang] + ')']
            lines += ['']
        lines += [('根拠の出典: ' if ja else 'Evidence sources: ') + '[Connection catalog](' + ORIGIN + '/catalog/atlas-crossovers.json) · [Method registry](' + ORIGIN + '/numerical-methods-atlas/methods/index.json) · [Execution registry](' + context['registry']['url'] + ') · [Rerun receipt](' + context['receipt_url'] + ')', '']
    return '\n'.join(lines).rstrip() + '\n'


def build(root=ROOT, data=None):
    root = Path(root)
    data = data if data is not None else load_catalog(root)
    context = validate_catalog(data, root)
    public = deepcopy(data)
    for route in public['routes']:
        route['url'] = {lang: ORIGIN + BASE + '?lang=' + lang + '#' + route['id'] + '-' + lang for lang in LANGUAGES}
        for stage in route['stages']:
            stage['evidence'] = stage_evidence(stage, context)
    sources = [root / 'catalog/atlas-crossovers.json', *context['sources']]
    if any(stage.get('model_ids') for route in data['routes'] for stage in route['stages']):
        sources.append(root / 'numerical-methods-atlas/assets/biological-models.json')
    public.update(registry=context['registry']['url'], verification_receipt=context['receipt_url'],
                  source_sha256={path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in sources})
    title_ja = data['title']['ja'] + ' | 数値計算法アトラス'
    title_en = data['title']['en'] + ' | Numerical Methods Atlas'
    document = '<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title data-page-title-ja="' + esc(title_ja, quote=True) + '" data-page-title-en="' + esc(title_en, quote=True) + '">' + esc(title_ja) + '</title><meta name="description" content="' + esc(data['intro']['ja'], quote=True) + '"><link rel="canonical" href="' + ORIGIN + BASE + '"><link rel="stylesheet" href="/styles/atlas-resources.css">' + crossover_assets(root, interactive=True) + '</head><body class="profile-page" data-site-language-anchors="suffix"><main class="profile-main atlas-resource-main atlas-crossover-main" id="main">' + ''.join(render_language(data, context, lang) for lang in LANGUAGES) + '</main></body></html>\n'
    destination = root / BASE.lstrip('/')
    destination.mkdir(parents=True, exist_ok=True)
    (destination / 'index.html').write_text(document)
    (destination / 'index.json').write_text(json.dumps(public, ensure_ascii=False, indent=2) + '\n')
    (destination / 'index.md').write_text(render_markdown(data, context))
    return public


def main(root=ROOT):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--catalog', type=Path, help='Validate an alternate catalog (use --validate-only for review).')
    parser.add_argument('--validate-only', action='store_true')
    args = parser.parse_args()
    data = read_json(args.catalog) if args.catalog else load_catalog(root)
    if args.validate_only:
        validate_catalog(data, root)
        print('Crossover catalog and component evidence validated; no outputs written.')
    else:
        fail(args.catalog is None, 'Alternate catalogs are supported only with --validate-only')
        build(root, data)
        print('Built bilingual cross-field connections with separate component evidence and coupled-validation gaps.')


if __name__ == '__main__':
    main()
