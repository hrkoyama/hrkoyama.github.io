"""Compact, scoped navigation from a verified execution to its actual resources."""
from html import escape
import re
from urllib.parse import unquote, urljoin, urlsplit


LANGUAGES = ('ja', 'en')
ORIGIN = 'https://hrkoyama.github.io'
LABELS = {
    'methods': {'ja': '使用手法', 'en': 'Methods used'},
    'equations': {'ja': '方程式', 'en': 'Equations'},
    'figure': {'ja': '問題の図', 'en': 'Problem figure'},
    'references': {'ja': '厳密解・参照解', 'en': 'Exact / reference solutions'},
}


def _language(language):
    if language not in LANGUAGES:
        raise ValueError('Unsupported execution-navigation language')
    return language == 'ja'


def _id(value):
    if not isinstance(value, str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]*', value):
        raise ValueError('Invalid execution-navigation identity')
    return value


def _text(value, language):
    result = value.get(language, '') if isinstance(value, dict) else (value or '')
    if not isinstance(result, str):
        raise ValueError('Invalid execution-navigation text')
    return result


def _url(value):
    if not isinstance(value, str) or not value or any(char.isspace() for char in value):
        raise ValueError('Missing execution-navigation URL')
    parsed = urlsplit(urljoin(ORIGIN + '/', value))
    if (parsed.scheme != 'https' or parsed.netloc != 'hrkoyama.github.io' or parsed.username or parsed.password or
            any(part in {'.', '..'} or part.startswith('.') for part in unquote(parsed.path).split('/') if part)):
        raise ValueError('Invalid public execution-navigation URL')
    if not (value.startswith('https://') or value.startswith('/') or value.startswith('#')):
        raise ValueError('Execution-navigation URL must be a public absolute, site-relative or fragment URL')
    return value


def _link(url, label, attrs=''):
    return '<a href="' + escape(_url(url), quote=True) + '"' + attrs + '>' + escape(label) + '</a>'


def _paragraph(value, language, css='execution-navigation-note'):
    text = _text(value, language)
    return '<p class="' + css + '">' + escape(text) + '</p>' if text else ''


def _scope(value, language, label):
    text = _text(value, language)
    if not text:
        return ''
    if len(text) <= 240:
        return _paragraph(text, language)
    return '<details class="execution-navigation-scope"><summary>' + label + '</summary><p>' + escape(text) + '</p></details>'


def _formulation_label(formulation, language):
    labels = {
        'problem': {'ja': 'この固定入力の問題式と条件', 'en': 'This fixed-input problem and its conditions'},
        'approximation': {'ja': 'この実行例の近似式と条件', 'en': 'This example’s approximation and conditions'},
        'diagnostic': {'ja': 'この実行例の診断式と条件', 'en': 'This example’s diagnostic and conditions'},
        'example-definition': {'ja': 'この実行例の式と条件', 'en': 'This example’s formulation and conditions'},
    }
    return labels.get(formulation.get('role'), labels['example-definition'])[language]


def _reference_label(case, language):
    relation = case.get('relation')
    if relation not in {'same-problem', 'related-model'}:
        raise ValueError('Unknown execution reference relation')
    labels = {
        'same-problem': {'ja': '同じ問題の参照', 'en': 'Same-problem reference'},
        'related-model': {'ja': '関連モデルの参照', 'en': 'Related-model reference'},
    }
    kinds = {
        'analytic': {'ja': '解析参照', 'en': 'Analytic reference'},
        'semi-analytic': {'ja': '半解析参照', 'en': 'Semi-analytic reference'},
        'manufactured': {'ja': '製造解', 'en': 'Manufactured solution'},
        'numerical-reference': {'ja': '有限格子の数値参照', 'en': 'Finite-grid numerical reference'},
    }
    if case.get('kind') not in kinds:
        raise ValueError('Unknown execution reference kind')
    return labels[relation][language] + ' · ' + kinds[case['kind']][language]


def _figure_scope(route, language):
    ja = language == 'ja'
    kind = route['figure']['kind']
    if kind == 'problem-representative':
        return ('この問題の代表図です。格子・時刻・初期値などは、この実行例の固定入力と異なる場合があります。' if ja else
                'A representative figure for the problem. Its grid, time and initial data may differ from this execution’s fixed input.')
    if kind == 'case-validation':
        return 'この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。' if ja else 'A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.'
    raise ValueError('Unknown execution figure scope')


def _methods(route, language):
    methods = route.get('methods', [])
    if not methods:
        return _paragraph('使用手法の対応は未登録です。' if language == 'ja' else 'No method association is registered.', language)
    body = '<ul class="execution-navigation-links">'
    for method in methods:
        body += '<li data-execution-method-id="' + _id(method['id']) + '">' + _link(method['url'][language], _text(method['name'], language), ' data-execution-method-link') + '</li>'
    body += '</ul>'
    body += _paragraph('この固定入力の実行に使う手法です。適用条件と検証の範囲は各案内で確認できます。' if language == 'ja' else 'Methods used by this fixed-input execution. Their guides describe applicable conditions and the checked scope.', language)
    return body


def _equations(route, language):
    ja = language == 'ja'
    formulation = route['formulation']
    body = '<p class="execution-navigation-primary">' + _link(formulation['url'][language], _formulation_label(formulation, language), ' data-execution-formulation-link') + '</p>'
    body += _scope(formulation.get('note'), language, '式・近似・診断の範囲' if ja else 'Formulation, approximation and diagnostic scope')
    equations = route.get('equations', [])
    if equations:
        body += '<ul class="execution-navigation-links">'
        for equation in equations:
            body += '<li data-execution-equation-id="' + _id(equation['id']) + '">' + _link(equation['url'][language], _text(equation['name'], language), ' data-execution-equation-link') + _paragraph(equation.get('note'), language, 'execution-navigation-equation-note') + '</li>'
        body += '</ul>'
    else:
        body += _paragraph('方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。' if ja else 'No corresponding equation-registry entry is registered. The example-specific definition above supplies its formulation, approximation or diagnostic.', language)
    return body


def _figure(route, language):
    ja = language == 'ja'
    figure = route['figure']
    for key in ['width', 'height']:
        if isinstance(figure[key], bool) or not isinstance(figure[key], int) or figure[key] <= 0:
            raise ValueError('Invalid execution figure dimensions')
    caption = _text(figure.get('caption'), language)
    name = _text(route['name'], language)
    body = '<a class="execution-navigation-figure" data-execution-figure-link href="' + escape(_url(figure['url']), quote=True) + '"><img src="' + escape(_url(figure['url']), quote=True) + '" alt="' + escape(caption or name, quote=True) + '" width="' + str(figure['width']) + '" height="' + str(figure['height']) + '" loading="lazy" decoding="async"></a>'
    body += _paragraph(_figure_scope(route, language), language)
    problem = route.get('problem')
    if problem:
        body += '<p class="execution-navigation-primary" data-execution-problem-id="' + _id(problem['id']) + '">' + _link(problem['hub'][language], _text(problem['name'], language), ' data-execution-problem-link') + '</p>'
        if problem.get('code'):
            body += '<p class="execution-navigation-primary">' + _link(problem['code'][language], 'この問題のコード・検証状況' if ja else 'This problem’s code and validation status', ' data-execution-problem-code') + '</p>'
    else:
        body += _paragraph('この検査・診断例には、別の物理テスト問題を割り当てていません。固有の診断図と検証資料を示しています。' if ja else 'No separate physical test problem is assigned to this check or diagnostic. Its own diagnostic figure and validation material are provided.', language, 'execution-navigation-unbound')
    return body


def _references(route, language):
    ja = language == 'ja'
    references = route['references']
    body = '<p class="execution-navigation-primary">' + _link(references['url'][language], 'この実行例の参照・検証' if ja else 'References and checks for this execution', ' data-execution-validation-link') + '</p>'
    body += _scope(references.get('note'), language, '参照・検証の確認範囲' if ja else 'Reference and validation scope')
    cases = references.get('cases', [])
    if cases:
        body += '<ul class="execution-navigation-reference-cases">'
        for case in cases:
            body += '<li data-execution-reference-id="' + _id(case['id']) + '" data-reference-relation="' + escape(case['relation'], quote=True) + '"><p class="execution-navigation-relation">' + _reference_label(case, language) + '</p>'
            body += '<p class="execution-navigation-primary">' + _link(case['url'][language], _text(case['title'], language), ' data-execution-reference-link') + '</p>'
            # A related model's limitations stay visible beside its link.
            body += _paragraph(case.get('note'), language, 'execution-navigation-reference-note') + '</li>'
        body += '</ul>'
    else:
        body += _paragraph('参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。' if ja else 'No corresponding reference-library card is registered. The execution-specific validation material above documents its reference values and acceptance checks.', language)
    return body


def render_execution_navigation(route, lang):
    """Four small labeled cards, reusable at every existing execution heading level."""
    ja = _language(lang)
    ident = _id(route['id'])
    if route.get('kind') not in {'common', 'supplement'}:
        raise ValueError('Unknown execution-navigation kind')
    body = '<div class="execution-navigation execution-resource-navigation" data-execution-navigation="' + ident + '" role="group" aria-label="' + ('この実行例に関連する資料' if ja else 'Resources for this execution example') + '"><div class="execution-navigation-grid">'
    renderers = {'methods': _methods, 'equations': _equations, 'figure': _figure, 'references': _references}
    for key, renderer in renderers.items():
        body += '<div class="execution-navigation-card" data-execution-navigation-card="' + key + '"><p class="execution-navigation-label"><strong>' + LABELS[key][lang] + '</strong></p>' + renderer(route, lang) + '</div>'
    return body + '</div></div>'


def _md_text(value):
    return value.replace('\\', '\\\\').replace('[', '\\[').replace(']', '\\]').replace('\n', ' ')


def _md_link(url, label, image=False):
    return ('!' if image else '') + '[' + _md_text(label) + '](' + _url(url).replace('(', '%28').replace(')', '%29') + ')'


def execution_navigation_markdown(route, lang):
    """Keep the same scoped links, including exact formulation source, in Markdown."""
    ja = _language(lang)
    _id(route['id'])
    lines = ['**' + LABELS['methods'][lang] + '**', '']
    for method in route.get('methods', []):
        lines += ['- ' + _md_link(method['url'][lang], _text(method['name'], lang)) + ' (`' + _id(method['id']) + '`)']
    if not route.get('methods'):
        lines += ['使用手法の対応は未登録です。' if ja else 'No method association is registered.']
    lines += ['', '**' + LABELS['equations'][lang] + '**', '']
    formulation = route['formulation']
    lines += [_md_link(formulation['url'][lang], _formulation_label(formulation, lang)), '', _text(formulation.get('note'), lang), '']
    for latex in formulation.get('latex', []):
        lines += ['$$', latex, '$$', '']
    for equation in route.get('equations', []):
        lines += ['- ' + _md_link(equation['url'][lang], _text(equation['name'], lang)) + ' (`' + _id(equation['id']) + '`)']
        if _text(equation.get('note'), lang):
            lines += ['', _text(equation['note'], lang), '']
    if not route.get('equations'):
        lines += ['方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。' if ja else 'No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.']
    lines += ['', '**' + LABELS['figure'][lang] + '**', '', _md_link(route['figure']['url'], _text(route['figure'].get('caption'), lang) or _text(route['name'], lang), image=True), '', _figure_scope(route, lang), '']
    problem = route.get('problem')
    if problem:
        lines += [_md_link(problem['hub'][lang], _text(problem['name'], lang)) + ' (`' + _id(problem['id']) + '`)', '']
        if problem.get('code'):
            lines += [_md_link(problem['code'][lang], 'この問題のコード・検証状況' if ja else 'This problem’s code and validation status'), '']
    else:
        lines += ['この検査・診断例には、別の物理テスト問題を割り当てていません。固有の診断図と検証資料を示しています。' if ja else 'No separate physical test problem is assigned to this check or diagnostic. Its own diagnostic figure and validation material are provided.', '']
    references = route['references']
    lines += ['**' + LABELS['references'][lang] + '**', '', _md_link(references['url'][lang], 'この実行例の参照・検証' if ja else 'References and checks for this execution'), '', _text(references.get('note'), lang), '']
    if not references.get('cases'):
        lines += ['参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。' if ja else 'No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.', '']
    for case in references.get('cases', []):
        lines += ['- ' + _md_link(case['url'][lang], _text(case['title'], lang)) + ' (`' + _id(case['id']) + '`; ' + _reference_label(case, lang) + ')', '', _text(case.get('note'), lang), '']
    return '\n'.join(lines).rstrip() + '\n'
