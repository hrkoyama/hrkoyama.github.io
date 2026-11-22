"""Availability of resources for a specific goal, without promoting catalog status."""
from html import escape
from hashlib import sha256
import json
from pathlib import Path
from atlas_depth_release import load_depth_group, depth_code_urls


def load_supplemental_examples(root, identifiers):
    """Resolve only immutable, successful supplements, separate from the common registry."""
    assert isinstance(identifiers, list) and len(identifiers) == len(set(identifiers))
    if not identifiers:
        return []
    config = json.loads((root / 'catalog/atlas-depth-expansion.json').read_text())
    selected = {}
    for group in config['groups']:
        edition = group.get('edition', config['edition'])
        metadata = json.loads((root / 'code/validated-examples' / edition / group['id'] / 'cases.json').read_text())
        if isinstance(metadata, dict):
            metadata = metadata['cases']
        if not set(identifiers).intersection(case['id'] for case in metadata):
            continue
        data = load_depth_group(root, group['id'], edition)
        for case in data['metadata']:
            ident = case['id']
            if ident not in identifiers:
                continue
            assert ident not in selected, 'Repeated supplemental case: ' + ident
            selected[ident] = {
                **case, 'name': case['title'], 'group': group['id'],
                'url': '/numerical-methods-atlas/validation/' + ident + '/',
                'reading': {lang: '/numerical-methods-atlas/' + lang + '/read/validation-' + group['id'] + '/#' + ident for lang in ['ja', 'en']},
                'code_urls': depth_code_urls(data, [ident]), 'test_urls': data['test_urls'],
                'download': data['base'] + data['verification']['archive']['file'],
                'results': data['base'] + 'results/result.json',
                'verification': data['base'] + 'verification.json',
                'source_sha256': data['source_sha256'],
            }
    assert set(selected) == set(identifiers), 'Unknown supplemental case IDs: ' + str(set(identifiers) - set(selected))
    return [selected[ident] for ident in identifiers]


def goal_supplements(goal):
    return load_supplemental_examples(Path(__file__).resolve().parents[1], goal.get('supplemental_examples', []))

def goal_methods(goal, methods):
    rows = [dict(methods[ident]) for ident in goal['methods']] + [dict(x) for x in goal.get('resources', [])]
    supplements = {item['id']: item for item in goal_supplements(goal)}
    for row in rows:
        selected = row.get('supplemental_examples', [])
        if selected:
            assert set(selected) <= supplements.keys()
            row.update(status='educational-example',
                       code_urls=list(dict.fromkeys(url for ident in selected for url in supplements[ident]['code_urls'])),
                       test_urls=list(dict.fromkeys(url for ident in selected for url in supplements[ident]['test_urls'])),
                       supplemental_execution_examples=[{'id':ident,'name':supplements[ident]['title'],'guide':{lang:supplements[ident]['url']+'?lang='+lang for lang in ['ja','en']}} for ident in selected])
        if goal.get('availability') == 'reading-only':
            assert not supplements
            row.update(status='reading-only', code_urls=[], test_urls=[], execution_examples=[])
    return rows


def goal_label(goal, methods, lang):
    rows = goal_methods(goal, methods)
    if goal_supplements(goal) or any(row['status'] == 'educational-example' for row in rows):
        pair = ('固定入力で実行', 'Runnable fixed inputs') if goal['examples'] or goal_supplements(goal) else ('関連コード・テストあり', 'Related code and tests')
    elif rows and all(row['status'] == 'planned' for row in rows):
        pair = ('解説あり・実装予定', 'Reading; implementation planned')
    else:
        pair = ('解説のみ・専用実装なし', 'Reading only; no implementation')
    return pair[0 if lang == 'ja' else 1]


def goal_flags(goal, methods):
    rows = goal_methods(goal, methods)
    supplements = goal_supplements(goal)
    code = bool(supplements) or any(row['status'] == 'educational-example' and row.get('code_urls') and row.get('test_urls') for row in rows)
    if code:
        return ['run', 'code'] if goal['examples'] or supplements else ['code']
    return ['planned'] if rows and all(row['status'] == 'planned' for row in rows) else ['reading']


def goal_attributes(goal, methods):
    return ' data-goal-item data-goal-id="' + escape(goal['id'], quote=True) + '" data-goal-states="' + ' '.join(goal_flags(goal, methods)) + '" data-goal-domains="' + escape(' '.join(goal['domains']), quote=True) + '"'


def goal_filter_controls(lang, context, domains):
    ja = lang == 'ja'
    ident = context + '-availability-' + lang
    domain_id = context + '-domain-' + lang
    options = [('all', 'すべて', 'All'), ('run', '実行例あり', 'Runnable examples'), ('code', 'コードとテストあり', 'Code and tests'), ('reading', '解説のみ', 'Reading only'), ('planned', '実装予定', 'Implementation planned')]
    domain_options = '<option value="all">' + ('すべて' if ja else 'All') + '</option>' + ''.join('<option value="' + escape(row['id'], quote=True) + '">' + escape(row['name'][lang]) + '</option>' for row in domains)
    return '<div class="goal-filter-controls" data-goal-controls hidden><div class="goal-filter-field"><label for="' + domain_id + '">' + ('分野' if ja else 'Field') + '</label><select id="' + domain_id + '" data-goal-domain aria-describedby="' + ident + '-help">' + domain_options + '</select></div><div class="goal-filter-field"><label for="' + ident + '">' + ('公開状況' if ja else 'Availability') + '</label><select id="' + ident + '" data-goal-filter aria-describedby="' + ident + '-help">' + ''.join('<option value="' + value + '">' + (jp if ja else en) + '</option>' for value, jp, en in options) + '</select></div><button type="button" data-goal-reset>' + ('すべて表示' if ja else 'Show all') + '</button><button type="button" data-goal-copy>' + ('共有リンクをコピー' if ja else 'Copy share link') + '</button><p data-goal-count role="status" aria-live="polite" aria-atomic="true"></p><p class="goal-filter-help" id="' + ident + '-help">' + ('分野と公開状況の両方に一致する目的を表示します。条件はURLで共有・ブックマークできます。「コードとテストあり」には、実行例ありも含みます。' if ja else 'Goals must match both field and availability. Share or bookmark the URL to keep these filters. Code and tests also includes goals with runnable examples.') + '</p><p class="goal-copy-feedback" data-goal-copy-feedback role="status" aria-live="polite" aria-atomic="true" hidden></p><div class="goal-copy-fallback" data-goal-copy-fallback hidden><label for="' + ident + '-share">' + ('共有リンク' if ja else 'Share link') + '</label><input type="url" id="' + ident + '-share" data-goal-copy-url readonly spellcheck="false"></div></div><p data-goal-empty hidden>' + ('該当する目的がありません。「すべて表示」で戻れます。' if ja else 'No goals match. Choose Show all to reset.') + '</p>'


def goal_filter_assets(root):
    css = sha256((root / 'styles/atlas-goal-filters.css').read_bytes()).hexdigest()[:12]
    js = sha256((root / 'numerical-methods-atlas/goal-filters.mjs').read_bytes()).hexdigest()[:12]
    return '<link rel="stylesheet" href="/styles/atlas-goal-filters.css?v=' + css + '">\n<script type="module" src="/numerical-methods-atlas/goal-filters.mjs?v=' + js + '"></script>\n'
