#!/usr/bin/env python3
"""Publish a sequential benchmark backlog; verify evidence before showing done.

Scientific completion uses verification (same-site JSON with passed=true),
inputs[], plots[], code[], references[], gallery and execution. Curation uses
targets[], proof[] and note. Only completed states require these fields.
An in-progress item may expose evidence for a scoped published stage without
completing the whole candidate. Planned items must not carry such evidence.
The builder reads saved evidence; it never starts scientific calculations.
"""
from collections import Counter
from copy import deepcopy
from hashlib import sha256
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import parse_qsl, unquote, urlencode, urlsplit, urlunsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://hrkoyama.github.io'
BASE = '/numerical-methods-atlas/'
ROUTE = BASE + 'backlog/'
SOURCE = 'catalog/atlas-benchmark-backlog.json'
STATES = {
    'planned': {'ja': '未着手', 'en': 'Planned'},
    'in-progress': {'ja': '作業中', 'en': 'In progress'},
    'verified': {'ja': '検証済み', 'en': 'Verified'},
    'published': {'ja': '公開済み', 'en': 'Published'},
}
ID = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def checked_url(value, same_site=False):
    if not isinstance(value, str) or not value or re.search(r'[\s\\\x00-\x1f]', value):
        raise ValueError('Invalid backlog URL: ' + str(value))
    parsed = urlsplit(value)
    if value.startswith('/') and not value.startswith('//'):
        parsed = urlsplit(ORIGIN + value)
    if parsed.scheme != 'https' or not parsed.netloc or parsed.username or parsed.password:
        raise ValueError('Backlog links require public HTTPS URLs: ' + value)
    if same_site and parsed.netloc != 'hrkoyama.github.io':
        raise ValueError('Completion evidence must be on the public site: ' + value)
    for path in (parsed.path, unquote(parsed.path)):
        if any(part.startswith('.') for part in path.split('/') if part):
            raise ValueError('Non-public backlog path: ' + value)
    return parsed


class Anchors(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if attributes.get('id'):
            self.ids.add(attributes['id'])


def target(root, value, receipts):
    parsed = checked_url(value, same_site=True)
    if parsed.path.startswith(ROUTE):
        raise ValueError('Generated backlog output cannot be its own completion evidence')
    path = (root / unquote(parsed.path).lstrip('/')).resolve()
    if root.resolve() not in path.parents:
        raise ValueError('Completion evidence escapes the repository')
    if path.is_dir():
        path /= 'index.html'
    if not path.is_file():
        raise ValueError('Missing completion evidence: ' + value)
    if parsed.fragment:
        if path.suffix != '.html':
            raise ValueError('Completion fragments require a real HTML anchor: ' + value)
        parser = Anchors(); parser.feed(path.read_text())
        if unquote(parsed.fragment) not in parser.ids:
            raise ValueError('Missing completion anchor: ' + value)
    receipts[path.relative_to(root.resolve()).as_posix()] = digest(path)
    return path


def list_of_links(completion, key):
    values = completion.get(key)
    if not isinstance(values, list) or not values or any(not isinstance(value, str) for value in values):
        raise ValueError('Completion needs a nonempty ' + key + ' URL list')
    if len(values) != len(set(values)):
        raise ValueError('Repeated completion evidence: ' + key)
    return values


def validate_plot(path):
    raw = path.read_bytes()
    valid = False
    if path.suffix.lower() == '.png':
        valid = len(raw) >= 24 and raw[:8] == b'\x89PNG\r\n\x1a\n' and raw[12:16] == b'IHDR' and int.from_bytes(raw[16:20], 'big') > 0 and int.from_bytes(raw[20:24], 'big') > 0
    elif path.suffix.lower() == '.svg':
        valid = ET.fromstring(raw).tag.rsplit('}', 1)[-1] == 'svg'
    elif path.suffix.lower() == '.pdf':
        valid = raw.startswith(b'%PDF-')
    if not valid:
        raise ValueError('Completion plot is not a supported saved PNG/SVG/PDF: ' + str(path))


def completion_evidence(root, item, receipts):
    completion = item.get('completion')
    if item['state'] == 'planned':
        if completion is not None:
            raise ValueError('Planned backlog items cannot carry completion evidence: ' + item['id'])
        return None
    partial = item['state'] == 'in-progress'
    if partial and completion is None:
        return None
    if not isinstance(completion, dict):
        raise ValueError('Backlog completion/stage evidence must be a record: ' + item['id'])
    if partial and not (isinstance(item.get('scope_note'), str) and item['scope_note'].strip()):
        raise ValueError('Published stage needs its completed and remaining scope: ' + item['id'])
    if item['kind'] == 'references':
        for key in ('targets', 'proof'):
            for value in list_of_links(completion, key):
                target(root, value, receipts)
        note = completion.get('note')
        if not (isinstance(note, str) and note.strip() or isinstance(note, dict) and isinstance(note.get('ja'), str) and note['ja'].strip()):
            raise ValueError('Curation completion needs a checked correction note')
        return {'kind': 'curation', 'partial': partial, 'local_evidence_checked': True, 'links': deepcopy(completion)}
    for key in ('inputs', 'plots', 'code'):
        for value in list_of_links(completion, key):
            path = target(root, value, receipts)
            if key == 'plots':
                validate_plot(path)
    for value in list_of_links(completion, 'references'):
        parsed = checked_url(value)
        if parsed.netloc == 'hrkoyama.github.io':
            target(root, value, receipts)
    for key in ('gallery', 'execution'):
        path = target(root, completion.get(key), receipts)
        if path.suffix != '.html':
            raise ValueError(key + ' must identify a real public entry page')
    path = target(root, completion.get('verification'), receipts)
    receipt = json.loads(path.read_text())
    if receipt.get('passed') is not True:
        raise ValueError('Scientific completion requires a saved passed=true receipt: ' + item['id'])
    return {'kind': 'scientific', 'partial': partial, 'local_evidence_checked': True,
            'verification_passed': True, 'links': deepcopy(completion)}


def load(root=ROOT):
    root = Path(root).resolve()
    source = root / SOURCE
    data = json.loads(source.read_text())
    if data.get('schema_version') != 1:
        raise ValueError('Unknown benchmark-backlog schema')
    receipts = {SOURCE: digest(source)}
    fields = {row['id']: row for row in data['fields']}
    if len(fields) != len(data['fields']) or any(not ID.fullmatch(ident) for ident in fields):
        raise ValueError('Invalid or duplicate backlog field')
    seen, sequences = set(), set()
    for item in data['items']:
        ident = item['id']
        if not ID.fullmatch(ident) or ident in seen:
            raise ValueError('Invalid or repeated backlog item: ' + ident)
        seen.add(ident)
        if item['field_id'] not in fields or item['state'] not in STATES or item['kind'] not in data['kind_labels'] or item['priority'] not in data['priority_labels']:
            raise ValueError('Unknown backlog classification: ' + ident)
        if not all(isinstance(item['title'].get(lang), str) and item['title'][lang].strip() for lang in ('ja', 'en')):
            raise ValueError('Missing backlog title: ' + ident)
        if not item.get('tasks') or not all(isinstance(text, str) and text.strip() for text in item['tasks']):
            raise ValueError('Missing minimum work/checks: ' + ident)
        sequence = item['sequence']
        if isinstance(sequence, bool) or not isinstance(sequence, int) or sequence <= 0 or sequence in sequences:
            raise ValueError('Invalid or repeated backlog sequence: ' + ident)
        sequences.add(sequence)
        if item.get('detail_language') not in ('ja', 'en'):
            raise ValueError('Unknown original-detail language: ' + ident)
        for reference in item.get('sources', []):
            checked_url(reference['url'])
        item['completion_evidence'] = completion_evidence(root, item, receipts)
    active = [item['id'] for item in data['items'] if item['state'] == 'in-progress']
    workflow = data['workflow']
    if workflow.get('max_active') != 1 or len(active) > 1 or workflow.get('active_item') != (active[0] if active else None):
        raise ValueError('Backlog must have at most one correctly identified active item')
    expected = data['source']['proposal_count'] + data['source']['shared_count']
    if expected != len(data['items']):
        raise ValueError('Backlog proposal count differs from the registered inventory')
    data['url'] = ORIGIN + ROUTE
    data['counts'] = {'total': len(data['items']), 'fields': len(fields),
                      'states': {key: sum(item['state'] == key for item in data['items']) for key in STATES},
                      'kinds': dict(Counter(item['kind'] for item in data['items'])),
                      'priorities': dict(Counter(item['priority'] for item in data['items']))}
    data['source_sha256'] = dict(sorted(receipts.items()))
    return data


def text(value):
    return escape(str(value))


def link(url, label, attrs=''):
    if not (isinstance(url, str) and re.fullmatch(r'#[a-z0-9-]+', url)):
        checked_url(url)
    return '<a href="' + escape(url, quote=True) + '"' + attrs + '>' + text(label) + '</a>'


def localized(value, language):
    if isinstance(value, str):
        return value
    return value.get(language) or value.get('ja') or value.get('en') or ''


def language_tag(value, language):
    rendered = localized(value, language)
    original = language == 'en' and bool(re.search(r'[\u3040-\u30ff\u3400-\u9fff]', rendered))
    return '<span' + (' lang="ja"' if original else '') + '>' + text(rendered) + '</span>'


def criteria(item, language):
    if item['kind'] == 'references':
        return (['対象の本文・台帳と修正した箇所が確認できる。', '出典・書誌・適用範囲の修正根拠と確認記録を残す。', '実在する対象と根拠を照合してから完了にする。'] if language == 'ja' else
                ['Identify the edited target passages and records.', 'Keep the citation/scope correction and its checked evidence.', 'Verify the real target and evidence before marking complete.'])
    return (['固定入力と適用範囲、参照解または独立参照とその出典を保存する。', '実コード・検査とpassed=trueの検証記録を揃える。', '誤差・収束と制約が分かる図を保存する。', '実在する問題ギャラリー・実行入口・入力・図への対応を確認する。'] if language == 'ja' else
            ['Save fixed inputs, scope, and a cited exact or independent reference.', 'Provide real code/checks and a saved passed=true verification receipt.', 'Save a figure showing errors, refinement and limits.', 'Check the actual gallery, execution, input and figure targets.'])


def localized_evidence_url(url, language):
    """Keep bilingual entry queries and suffixed section anchors in one locale."""
    checked = checked_url(url)
    original = urlsplit(url)
    if (checked.netloc != 'hrkoyama.github.io' or not checked.path.startswith(BASE)
            or not checked.path.endswith(('/', '.html'))
            or re.match(re.escape(BASE) + r'(?:ja|en)/read/', checked.path)):
        return url
    query = [(key, value) for key, value in parse_qsl(original.query, keep_blank_values=True) if key != 'lang']
    query.append(('lang', language))
    fragment = re.sub(r'-(?:ja|en)$', '-' + language, original.fragment)
    return urlunsplit(original._replace(query=urlencode(query), fragment=fragment))


def evidence_links(item, language):
    evidence = item.get('completion_evidence')
    if evidence is None:
        return ''
    labels = {'verification': ('検証記録', 'Verification receipt'), 'inputs': ('固定入力', 'Input'),
              'plots': ('保存図', 'Saved figure'), 'gallery': ('問題ギャラリー', 'Problem gallery'),
              'execution': ('実行・判定の入口', 'Run and validate'), 'code': ('コード', 'Code'),
              'references': ('参照の根拠', 'Reference'), 'targets': ('修正対象', 'Edited target'), 'proof': ('確認根拠', 'Checked evidence')}
    parts = []
    for key, (ja, en) in labels.items():
        values = evidence['links'].get(key, [])
        if isinstance(values, str):
            values = [values]
        for index, url in enumerate(values):
            label = (ja if language == 'ja' else en) + (' ' + str(index + 1) if len(values) > 1 else '')
            parts.append('<li>' + link(localized_evidence_url(url, language), label) + '</li>')
    partial = item['state'] == 'in-progress'
    heading = ('公開した段階の根拠' if language == 'ja' else 'Evidence for the published stage') if partial else ('確認できる完了の根拠' if language == 'ja' else 'Checked completion evidence')
    return '<section class="backlog-proof" data-backlog-evidence-scope="' + ('published-stage' if partial else 'completion') + '"><h4>' + heading + '</h4><ul>' + ''.join(parts) + '</ul></section>'


def item_html(item, data, language):
    ja = language == 'ja'
    ident = item['id']; title = localized(item['title'], language)
    search = ' '.join([ident, *item['title'].values(), item['current'], *item['tasks'], item.get('initial_coverage', '')])
    out = '<li data-backlog-item data-backlog-id="' + ident + '" data-backlog-field="' + item['field_id'] + '" data-backlog-priority="' + item['priority'] + '" data-backlog-state="' + item['state'] + '" data-backlog-kind="' + item['kind'] + '" data-backlog-search="' + escape(search, quote=True) + '">'
    out += '<details class="backlog-item" id="' + ident + '-' + language + '"><summary><span class="backlog-item-heading">' + language_tag(item['title'], language) + '</span><span class="backlog-item-meta"><span class="backlog-state backlog-state-' + item['state'] + '">' + STATES[item['state']][language] + '</span><span>' + item['priority'] + '</span><span>' + text(data['kind_labels'][item['kind']][language]) + '</span></span></summary>'
    out += '<div class="backlog-item-body" lang="' + item['detail_language'] + '">'
    if not ja:
        out += '<p class="backlog-original" lang="en">Details below are the original Japanese survey text.</p>'
    out += '<p class="backlog-coverage">調査時の範囲：' + text(item.get('initial_coverage', '')) + '</p>'
    out += '<h3>調査時の現状</h3><p>' + text(item['current']) + '</p><h3>追加内容・最小の検証</h3><ol>' + ''.join('<li>' + text(task) + '</li>' for task in item['tasks']) + '</ol>'
    if item.get('scope_note'):
        if (item.get('completion_evidence') or {}).get('partial'):
            out += '<h3>公開した段階と残る範囲</h3>'
        out += '<p class="backlog-scope">' + text(item['scope_note']) + '</p>'
    out += '<details class="backlog-baseline"><summary>現状の根拠・調査時の参照箇所</summary><ul>'
    for entry in item.get('baseline_evidence', []):
        out += '<li><code>' + text(entry['path']) + '</code>'
        if entry.get('id'):
            out += '<span> · ' + text(entry['id']) + '</span>'
        if entry.get('observation'):
            out += '<p>' + text(entry['observation']) + '</p>'
        out += '</li>'
    out += '</ul></details><h3>出典と確認範囲</h3>'
    if item.get('sources'):
        out += '<ul class="backlog-sources">'
        for source in item['sources']:
            out += '<li>' + link(source['url'], source['title'])
            if source.get('review'):
                out += '<p>' + text(source['review']) + '</p>'
            out += '</li>'
        out += '</ul>'
    else:
        out += '<p>個別の原著・参照資料は着手時に照合します。初等解・製造解に架空の原著を付けません。</p>'
    out += '</div><section class="backlog-completion" lang="' + language + '"><h3>' + ('完了条件' if ja else 'Completion criteria') + '</h3><ul>' + ''.join('<li>' + text(line) + '</li>' for line in criteria(item, language)) + '</ul></section>'
    out += evidence_links(item, language)
    out += '<p class="backlog-permalink">' + link(ORIGIN + ROUTE + '?lang=' + language + '#' + ident + '-' + language, 'この候補へのリンク' if ja else 'Link to this item') + '</p></details></li>'
    return out


def section(data, language):
    ja = language == 'ja'; counts = data['counts']; active = data['workflow']['active_item']
    out = '<section data-site-language="' + language + '" data-backlog-root="' + language + '" lang="' + language + '"><header class="backlog-heading"><p class="backlog-eyebrow">BENCHMARK WORK LOG</p><h1>' + text(data['title'][language]) + '</h1><p>' + text(data['description'][language]) + '</p></header>'
    out += '<nav class="backlog-navigation" aria-label="' + ('関連する入口' if ja else 'Related entries') + '">' + link(ORIGIN + BASE + '?lang=' + language, 'アトラス' if ja else 'Atlas home') + link(ORIGIN + BASE + 'gallery/?lang=' + language, 'テスト問題の名前と図' if ja else 'Test problems by name and figure') + link(ORIGIN + BASE + 'explore/?lang=' + language, '体系的に読む' if ja else 'Read systematically') + '</nav>'
    out += '<div class="backlog-summary">' + ''.join('<span><strong>' + str(counts['states'][state]) + '</strong> ' + STATES[state][language] + '</span>' for state in STATES) + '</div>'
    if active:
        item = next(row for row in data['items'] if row['id'] == active)
        title_language = ' lang="ja"' if not ja and re.search(r'[\u3040-\u9fff]', localized(item['title'], language)) else ''
        out += '<aside class="backlog-active"><p>' + ('いま進めている1件' if ja else 'One item currently active') + '</p>' + link('#' + active + '-' + language, localized(item['title'], language), title_language) + '<span>' + ('入力・参照・検査・図を揃えてから次へ進みます。' if ja else 'Complete its inputs, reference, checks and figure before starting the next item.') + '</span></aside>'
    out += '<details class="backlog-policy"><summary>' + ('進め方・状態と引用の読み方' if ja else 'Workflow, states and citation scope') + '</summary><p>' + text(data['policy'][language]) + '</p><p>' + text(data['workflow']['completion_rule'][language]) + '</p><p>' + text(data['citation_policy'][language]) + '</p><p>' + ('表示の検証済みは保存証拠の確認を指し、ページを開くたびに全計算を走らせるものではありません。' if ja else 'Verified means checked saved evidence; opening this page never starts calculations.') + '</p></details>'
    if not ja:
        out += '<p class="backlog-language-note">Candidate names and detailed survey notes currently remain in Japanese. English controls and summaries describe their status.</p>'
    out += '<form class="backlog-controls" data-backlog-controls hidden role="search"><div class="backlog-selects">'
    definitions = [('field', '分野', 'Field (Japanese names)', [(row['id'], localized(row['title'], language)) for row in data['fields']]),
                   ('priority', '優先度', 'Priority', [(key, key + ' · ' + value[language]) for key, value in data['priority_labels'].items()]),
                   ('state', '作業の状態', 'Work state', [(key, value[language]) for key, value in STATES.items()]),
                   ('kind', '追加するもの', 'Work type', [(key, value[language]) for key, value in data['kind_labels'].items()])]
    for name, label_ja, label_en, options in definitions:
        out += '<label>' + (label_ja if ja else label_en) + '<select data-backlog-filter="' + name + '"><option value="all">' + ('すべて' if ja else 'All') + '</option>'
        for value, label in options:
            out += '<option value="' + value + '"' + (' lang="ja"' if not ja and re.search(r'[\u3040-\u9fff]', label) else '') + '>' + text(label) + '</option>'
        out += '</select></label>'
    out += '</div><div class="backlog-query-row"><label for="backlog-query-' + language + '">' + ('候補・検証内容を検索' if ja else 'Search candidate names and checks') + '</label><input id="backlog-query-' + language + '" data-backlog-query type="search" autocomplete="off" placeholder="' + ('例：Noh、厳密解、格子収束' if ja else 'e.g. Noh, MHD, Poisson') + '"><button type="button" data-backlog-reset>' + ('すべて表示' if ja else 'Show all') + '</button></div></form>'
    out += '<p class="backlog-count" data-backlog-count role="status" aria-live="polite">' + str(counts['total']) + ('件の候補' if ja else ' candidates') + '</p><p class="backlog-empty" data-backlog-empty hidden>' + ('一致する候補がありません。条件を変えるか「すべて表示」で戻れます。' if ja else 'No candidates match. Change the filters or choose Show all.') + '</p>'
    for field in data['fields']:
        items = [item for item in data['items'] if item['field_id'] == field['id']]
        if not items:
            continue
        out += '<section class="backlog-field" data-backlog-field-group="' + field['id'] + '"><h2>' + language_tag(field['title'], language) + '<small>' + str(len(items)) + '</small></h2><ul class="backlog-items">' + ''.join(item_html(item, data, language) for item in sorted(items, key=lambda item: item['sequence'])) + '</ul></section>'
    out += '<footer class="backlog-footer">' + link(ORIGIN + ROUTE + 'index.json', 'JSON') + link(ORIGIN + ROUTE + 'index.md', 'Markdown') + link(ORIGIN + '/' + SOURCE, '台帳の正本' if ja else 'Source catalog') + '</footer></section>'
    return out


def markdown(data):
    out = '# ' + data['title']['ja'] + ' / ' + data['title']['en'] + '\n\n' + data['description']['ja'] + '\n\n' + data['policy']['ja'] + '\n\n'
    out += 'Source: ' + ORIGIN + '/' + SOURCE + '\n\n'
    for field in data['fields']:
        out += '## ' + field['title']['ja'] + '\n\n'
        for item in sorted((row for row in data['items'] if row['field_id'] == field['id']), key=lambda row: row['sequence']):
            out += '### ' + item['title']['ja'] + '\n\nID: ' + item['id'] + ' · ' + item['priority'] + ' · ' + STATES[item['state']]['ja'] + ' · ' + data['kind_labels'][item['kind']]['ja'] + '\n\n'
            out += '調査時の範囲：' + item.get('initial_coverage', '') + '\n\n調査時の現状：\n\n' + item['current'] + '\n\n追加内容・最小の検証：\n\n'
            out += ''.join('- ' + task + '\n' for task in item['tasks']) + '\n完了条件：\n\n' + ''.join('- ' + line + '\n' for line in criteria(item, 'ja')) + '\n'
            if item.get('scope_note'):
                out += ('公開した段階と残る範囲：\n\n' if (item.get('completion_evidence') or {}).get('partial') else '') + item['scope_note'] + '\n\n'
            if item.get('baseline_evidence'):
                out += '調査時の根拠：\n\n'
                for entry in item['baseline_evidence']:
                    out += '- `' + entry['path'] + '`' + (' · ' + str(entry['id']) if entry.get('id') else '') + '\n'
                    if entry.get('observation'):
                        out += '  ' + entry['observation'] + '\n'
                out += '\n'
            for source in item.get('sources', []):
                out += '- [' + source['title'].replace('[', '\\[').replace(']', '\\]') + '](<' + source['url'] + '>)\n'
                if source.get('review'):
                    out += '  ' + source['review'] + '\n'
            if item.get('completion_evidence'):
                heading = '公開した段階の根拠' if item['state'] == 'in-progress' else '完了の根拠'
                out += '\n' + heading + '：\n\n```json\n' + json.dumps(item['completion_evidence']['links'], ensure_ascii=False, indent=2) + '\n```\n'
            out += '\n'
    return out


def build(root=ROOT):
    root = Path(root).resolve(); data = load(root)
    style = 'styles/atlas-benchmark-backlog.css'; script = 'numerical-methods-atlas/benchmark-backlog.mjs'
    title_ja = data['title']['ja'] + ' | 数値計算法アトラス'; title_en = data['title']['en'] + ' | Numerical Methods Atlas'
    head = '<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title data-page-title-ja="' + text(title_ja) + '" data-page-title-en="' + text(title_en) + '">' + text(title_ja) + '</title>'
    head += '<meta name="description" content="' + escape(data['description']['ja'], quote=True) + '"><link rel="canonical" href="' + ORIGIN + ROUTE + '"><link rel="stylesheet" href="/' + style + '?v=' + digest(root / style)[:12] + '"><script type="module" src="/' + script + '?v=' + digest(root / script)[:12] + '"></script></head>'
    html = head + '<body class="profile-page benchmark-backlog" data-site-language-anchors="suffix"><main id="main" class="backlog-main">' + ''.join(section(data, language) for language in ('ja', 'en')) + '</main></body></html>\n'
    destination = root / ROUTE.strip('/'); destination.mkdir(parents=True, exist_ok=True)
    (destination / 'index.html').write_text(html)
    (destination / 'index.json').write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    (destination / 'index.md').write_text(markdown(data).rstrip() + '\n')
    print('Built sequential benchmark backlog:', data['counts']['total'], 'items;', data['counts']['fields'], 'fields;', data['counts']['states'])
    return data


if __name__ == '__main__':
    build()
