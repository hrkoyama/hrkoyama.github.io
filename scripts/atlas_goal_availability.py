"""Availability of resources for a specific goal, without promoting catalog status."""
from html import escape
from hashlib import sha256

def goal_methods(goal, methods):
    rows = [dict(methods[ident]) for ident in goal['methods']] + [dict(x) for x in goal.get('resources', [])]
    for row in rows:
        if goal.get('availability') == 'reading-only':
            row.update(status='reading-only', code_urls=[], test_urls=[], execution_examples=[])
    return rows


def goal_label(goal, methods, lang):
    rows = goal_methods(goal, methods)
    if any(row['status'] == 'educational-example' for row in rows):
        pair = ('固定入力で実行', 'Runnable fixed inputs') if goal['examples'] else ('関連コード・テストあり', 'Related code and tests')
    elif rows and all(row['status'] == 'planned' for row in rows):
        pair = ('解説あり・実装予定', 'Reading; implementation planned')
    else:
        pair = ('解説のみ・専用実装なし', 'Reading only; no implementation')
    return pair[0 if lang == 'ja' else 1]


def goal_flags(goal, methods):
    rows = goal_methods(goal, methods)
    code = any(row['status'] == 'educational-example' and row.get('code_urls') and row.get('test_urls') for row in rows)
    if code:
        return ['run', 'code'] if goal['examples'] else ['code']
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
