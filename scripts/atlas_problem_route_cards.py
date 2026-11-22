"""Shared, compact routes from models/references back to real test problems."""
from html import escape
import re
from urllib.parse import urlsplit


LANGUAGES = ('ja', 'en')


def _language(language):
    if language not in LANGUAGES:
        raise ValueError('Unsupported problem-route language: ' + str(language))
    return language == 'ja'


def _text(value, language):
    text = value.get(language, '') if isinstance(value, dict) else (value or '')
    if not isinstance(text, str):
        raise ValueError('Invalid problem-route text')
    return text


def _url(value):
    if not isinstance(value, str):
        raise ValueError('Missing problem-route URL')
    parsed = urlsplit(value)
    if (parsed.scheme != 'https' or parsed.netloc != 'hrkoyama.github.io' or
            parsed.username or parsed.password or any(char.isspace() for char in value)):
        raise ValueError('Invalid public problem-route URL: ' + value)
    return value


def _link(url, label, attrs=''):
    return '<a href="' + escape(_url(url), quote=True) + '"' + attrs + '>' + escape(label) + '</a>'


def _relation(row, language):
    relation = row.get('relation')
    if relation is None:
        return ''
    labels = {
        'same-problem': {'ja': '同じ問題への対応', 'en': 'Same-problem link'},
        'related-model': {'ja': '関連モデルの問題', 'en': 'Related-model problem'},
    }
    if relation not in labels:
        raise ValueError('Unknown problem-route relation: ' + str(relation))
    return labels[relation][language]


def _identity(row, language):
    ident = row.get('id')
    name = _text(row.get('name'), language)
    if not isinstance(ident, str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]*', ident) or not name.strip():
        raise ValueError('Invalid linked problem identity')
    return ident, name


def _card(row, language):
    ja = language == 'ja'
    ident, name = _identity(row, language)
    image = row['image']
    width, height = image['width'], image['height']
    if any(isinstance(value, bool) or not isinstance(value, int) or value <= 0 for value in [width, height]):
        raise ValueError('Invalid linked problem image dimensions: ' + ident)
    caption = _text(image.get('caption'), language)
    alt = name + (' — ' + caption if caption else '')
    picture = '<img src="' + escape(_url(image['url']), quote=True) + '" alt="' + escape(alt, quote=True) + '" width="' + str(width) + '" height="' + str(height) + '" loading="lazy" decoding="async">'
    body = '<li class="problem-route-card" data-linked-problem-id="' + ident + '"><div class="problem-route-overview">'
    body += '<a class="problem-route-picture" data-problem-picture href="' + escape(_url(row['hub'][language]), quote=True) + '">' + picture + '</a>'
    body += '<div class="problem-route-copy"><p class="problem-route-name">' + _link(row['hub'][language], name, ' data-problem-name') + '</p>'
    relation, note = _relation(row, language), _text(row.get('note'), language)
    if relation:
        body += '<p class="problem-route-relation">' + escape(relation) + '</p>'
    if note:
        body += '<p class="problem-route-note">' + escape(note) + '</p>'
    body += '<p class="problem-route-code">' + _link(row['code'][language], 'コード・検証状況' if ja else 'Code and validation status', ' data-problem-code') + '</p></div></div>'
    executions = row.get('executions', [])
    if executions:
        body += '<ul class="problem-route-executions">'
        for execution in executions:
            execution_id, execution_name = _identity(execution, language)
            body += '<li data-linked-execution-id="' + execution_id + '">'
            body += _link(execution['guide'][language], ('実行・検証：' if ja else 'Run and validate: ') + execution_name, ' data-problem-execution')
            body += _link(execution['download'], ('コードZIP：' if ja else 'Code ZIP: ') + execution_name, ' data-problem-download')
            scope = _text(execution.get('scope'), language)
            if scope:
                body += '<details class="problem-route-execution-scope"><summary>' + ('この実行例の範囲' if ja else 'Scope of this execution example') + '</summary><p>' + escape(scope) + '</p></details>'
            body += '</li>'
        body += '</ul>'
    else:
        body += '<p class="problem-route-unregistered">' + ('固定入力実行例は未登録です。' if ja else 'No fixed-input execution example is registered.') + '</p>'
    return body + '</li>'


def render_problem_routes(rows, language, heading_level=3, limit=3):
    """Show proven links only; an empty execution list never becomes a run link."""
    ja = _language(language)
    if isinstance(heading_level, bool) or not isinstance(heading_level, int) or heading_level not in range(2, 7):
        raise ValueError('Problem-route heading level must be between 2 and 6')
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise ValueError('Problem-route limit must be a positive integer')
    rows = list(rows)
    heading = '関連するテスト問題の図とコード' if ja else 'Related test problem figures and code'
    body = '<div class="problem-routes" data-problem-routes><h' + str(heading_level) + ' class="problem-routes-heading">' + heading + '</h' + str(heading_level) + '>'
    if not rows:
        return body + '<p class="problem-routes-empty">' + ('この項目に対応付けられたテスト問題は未登録です。' if ja else 'No associated test problem is registered for this entry.') + '</p></div>'
    body += '<ul class="problem-route-list">' + ''.join(_card(row, language) for row in rows[:limit]) + '</ul>'
    if len(rows) > limit:
        remaining = len(rows) - limit
        summary = '残り' + str(remaining) + '件の問題を見る' if ja else 'View ' + str(remaining) + ' more problem' + ('' if remaining == 1 else 's')
        body += '<details class="problem-routes-more"><summary>' + summary + '</summary><ul class="problem-route-list">' + ''.join(_card(row, language) for row in rows[limit:]) + '</ul></details>'
    return body + '</div>'


def _md_text(value):
    return value.replace('\\', '\\\\').replace('[', '\\[').replace(']', '\\]').replace('\n', ' ')


def _md_link(url, label, image=False):
    target = _url(url).replace('(', '%28').replace(')', '%29')
    return ('!' if image else '') + '[' + _md_text(label) + '](' + target + ')'


def markdown_problem_routes(rows, language, heading_level=4):
    """Keep every route, relation note and actual execution in the text edition."""
    ja = _language(language)
    if isinstance(heading_level, bool) or not isinstance(heading_level, int) or heading_level not in range(2, 6):
        raise ValueError('Markdown problem-route heading level must be between 2 and 5')
    rows = list(rows)
    lines = ['#' * heading_level + ' ' + ('関連するテスト問題の図とコード' if ja else 'Related test problem figures and code'), '']
    if not rows:
        return '\n'.join(lines + ['この項目に対応付けられたテスト問題は未登録です。' if ja else 'No associated test problem is registered for this entry.', '']) + '\n'
    for row in rows:
        ident, name = _identity(row, language)
        lines += ['#' * (heading_level + 1) + ' ' + _md_link(row['hub'][language], name) + ' (`' + ident + '`)', '',
                  _md_link(row['image']['url'], _text(row['image'].get('caption'), language) or name, image=True), '',
                  _md_link(row['code'][language], 'コード・検証状況' if ja else 'Code and validation status'), '']
        relation, note = _relation(row, language), _text(row.get('note'), language)
        if relation:
            lines += [relation, '']
        if note:
            lines += [note, '']
        executions = row.get('executions', [])
        if executions:
            for execution in executions:
                execution_id, execution_name = _identity(execution, language)
                lines += ['- ' + _md_link(execution['guide'][language], ('実行・検証：' if ja else 'Run and validate: ') + execution_name) + ' (`' + execution_id + '`) · ' +
                          _md_link(execution['download'], ('コードZIP：' if ja else 'Code ZIP: ') + execution_name)]
                scope = _text(execution.get('scope'), language)
                if scope:
                    lines += ['', ('この実行例の範囲：' if ja else 'Scope of this execution example: ') + scope, '']
            lines.append('')
        else:
            lines += ['固定入力実行例は未登録です。' if ja else 'No fixed-input execution example is registered.', '']
    return '\n'.join(lines) + '\n'
