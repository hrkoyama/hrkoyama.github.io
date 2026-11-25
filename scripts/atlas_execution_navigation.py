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


# These are presentation groups, not new problem/execution registry entries.
PROBLEM_EXECUTION_CHOICES = {
    'bratu': (
        ('forward', {'ja': '方程式を解く・解法を比べる', 'en': 'Solve the equation and compare solvers'},
         {'ja': '与えた係数から解を求めます。小さい枝、foldの追跡、Jacobian積の比較は別の固定入力です。',
          'en': 'Compute a solution for specified coefficients. The lower branch, fold continuation and Jacobian-product comparison have separate fixed inputs.'},
         (('bratu', 'bratu'), ('bratu-fold-continuation', 'bratu-fold-continuation'),
          ('bratu-matrix-free-jfnk', 'bratu-matrix-free-jfnk'))),
        ('sensitivity', {'ja': '解の感度・随伴を確かめる', 'en': 'Check sensitivities and adjoints'},
         {'ja': '係数を変えたときの解や目的量の変化を調べます。係数そのものを推定する逆問題とは分けます。',
          'en': 'Check how a solution or objective changes with its coefficients. This is separate from estimating those coefficients.'},
         (('bratu-fold-sensitivity', 'bratu-fold-sensitivity'), ('bratu-distributed-vjp', 'bratu-distributed-vjp'))),
        ('inverse', {'ja': '観測から係数を推定する', 'en': 'Estimate coefficients from observations'},
         {'ja': '固定された観測・目的関数・制約を使います。最適化法の比較と、雑音・正則化の比較を選べます。',
          'en': 'Use the fixed observations, objectives and constraints. Choose solver comparisons or noise and regularization studies.'},
         (('bratu-gn-lm-bounds', 'bratu-gn-lm-bounds'), ('bratu-noise-regularization', 'bratu-noise-regularization'))),
    ),
    'noh': (
        ('radial-1d', {'ja': '1D：対称性を仮定して計算する', 'en': '1D: impose planar or radial symmetry'},
         {'ja': '計算座標は1次元です。平面・円筒・球の形状を選びます。球の断面図を2D・3D Cartesian計算とは扱いません。',
          'en': 'One computational coordinate, with planar, cylindrical or spherical geometry. A spherical cross-section is not a 2D or 3D Cartesian calculation.'},
         (('noh', 'noh-shock'),)),
        ('cartesian-2d', {'ja': '2D：正方形の全領域で計算する', 'en': '2D: evolve the full Cartesian square'},
         {'ja': '密度・2成分運動量・全エネルギーの2D配列を更新し、軸・対角方向の違いを調べます。',
          'en': 'Evolve 2D arrays of density, both momenta and total energy, and examine axis/diagonal differences.'},
         (('noh', 'noh-cartesian-2d'),)),
    ),
}


def problem_execution_choices(problem_id, problems, routes):
    """Select existing records without extending or mutating their scientific graph."""
    if problem_id not in PROBLEM_EXECUTION_CHOICES:
        return []
    by_id = {problem['id']: problem for problem in problems}
    if len(by_id) != len(problems):
        raise ValueError('Duplicate problem in execution picker')
    groups = []
    for purpose, title, note, identities in PROBLEM_EXECUTION_CHOICES[problem_id]:
        cases = []
        for owner, ident in identities:
            problem = by_id[owner]
            matching = [row for row in problem['executions'] if row['id'] == ident]
            if len(matching) != 1:
                raise ValueError('Picker requires its own existing execution: ' + ident)
            execution = matching[0]
            route = routes[ident]
            if (route['id'] != ident or route['kind'] != execution['kind'] or
                    not route.get('problem') or route['problem']['id'] != owner):
                raise ValueError('Picker execution route belongs to another case: ' + ident)
            base = execution['download'].rsplit('/', 1)[0] + '/'
            for key in ['download', 'input', 'manifest', 'verification']:
                _url(execution[key])
            if not all(execution[key].startswith(base) for key in ['input', 'manifest']):
                raise ValueError('Picker input and manifest must use the selected code edition')
            edition = re.search(r'/(20\d{2}-\d{2}-\d{2}(?:-r\d+)?)/', base)
            if edition is None:
                raise ValueError('Missing explicit picker edition')
            figure = route['figure']
            if execution['kind'] == 'supplement':
                if figure['kind'] != 'case-validation' or figure['url'] != base + 'results/' + ident + '.png':
                    raise ValueError('Picker figure belongs to another execution: ' + ident)
            elif any(figure[key] != problem['image'][key] for key in ['url', 'sha256', 'width', 'height']):
                raise ValueError('Common picker figure must retain its representative-image identity')
            for language in LANGUAGES:
                guide = _url(execution['guide'][language])
                if route['references']['url'][language] != guide + '#' + ident + '-' + language + '-validation':
                    raise ValueError('Picker reference must belong to the selected execution: ' + ident)
            cases.append({'execution': execution, 'route': route, 'edition': edition.group(1), 'owner': owner})
        groups.append({'purpose': purpose, 'title': title, 'note': note, 'cases': cases})
    return groups


def problem_figure_case(problem, groups):
    """The existing Noh hero is Cartesian 2D; the Bratu hero is the forward case."""
    ident = {'bratu': 'bratu', 'noh': 'noh-cartesian-2d'}.get(problem['id'])
    if ident is None or not groups:
        return None
    matches = [case['execution'] for group in groups for case in group['cases'] if case['execution']['id'] == ident]
    if len(matches) != 1:
        raise ValueError('Missing matching problem-figure execution')
    return matches[0]


def problem_figure_note(problem, groups, language):
    """Do not turn a problem-representative picture into fixed-input evidence."""
    execution = problem_figure_case(problem, groups)
    if execution is None:
        return ''
    route = next(case['route'] for group in groups for case in group['cases']
                 if case['execution']['id'] == execution['id'])
    return _figure_scope(route, language) if route['figure']['kind'] == 'problem-representative' else ''


def render_problem_execution_choices(problem_id, groups, language):
    """Purpose and conditions come before immutable edition/download details."""
    ja = _language(language)
    if not groups:
        return ''
    body = '<section class="problem-execution-picker" data-problem-case-picker="' + _id(problem_id) + '" aria-labelledby="choose-' + problem_id + '-' + language + '">'
    body += '<h2 id="choose-' + problem_id + '-' + language + '">' + ('何を確かめますか？' if ja else 'What would you like to check?') + '</h2>'
    body += _paragraph('目的と計算条件を選ぶと、その例のコード・入力・参照へ進めます。' if ja else 'Choose the purpose and computational conditions to find its code, inputs and references.', language)
    for group in groups:
        purpose = group['purpose']
        opened = ' open' if problem_id == 'noh' and purpose == 'cartesian-2d' else ''
        body += '<details class="problem-choice-group" data-execution-purpose="' + purpose + '"' + opened + '><summary><h3 id="choose-' + purpose + '-' + language + '">' + escape(_text(group['title'], language)) + '</h3></summary>'
        body += _paragraph(group['note'], language) + '<div class="problem-choice-grid">'
        for case in group['cases']:
            execution, route = case['execution'], case['route']
            ident, figure = execution['id'], route['figure']
            dimension = '1d-bvp' if problem_id == 'bratu' else ('1d-radial' if ident == 'noh-shock' else '2d-cartesian')
            labels = {'1d-bvp': ('1D境界値問題・固定条件', '1D boundary-value problem · fixed conditions'),
                      '1d-radial': ('1次元座標：平面・円筒・球対称', 'One coordinate: planar, cylindrical or spherical symmetry'),
                      '2d-cartesian': ('2D Cartesian・正方形全領域', '2D Cartesian · full square')}
            attrs = ' data-execution-case="' + ident + '"'
            guide = execution['guide'][language]
            body += '<article class="problem-choice-card"' + attrs + ' data-execution-dimension="' + dimension + '"><p class="problem-choice-dimension">' + labels[dimension][0 if ja else 1] + '</p>'
            body += '<a class="problem-choice-figure"' + attrs + ' data-execution-action="figure" href="' + escape(_url(guide), quote=True) + '"><img src="' + escape(_url(figure['url']), quote=True) + '" width="' + str(figure['width']) + '" height="' + str(figure['height']) + '" alt="' + escape(_text(figure['caption'], language), quote=True) + '" loading="lazy" decoding="async"></a>'
            if figure['kind'] == 'problem-representative':
                body += _paragraph(_figure_scope(route, language), language)
            body += '<h4>' + _link(guide, _text(execution['name'], language), attrs + ' data-execution-action="guide"') + '</h4>'
            body += _paragraph(execution['scope'], language, 'problem-choice-scope')
            body += '<p class="problem-choice-action">' + _link(guide, 'この実行例を開く →' if ja else 'Open this execution example →', attrs + ' data-execution-action="open"') + '</p>'
            body += '<details class="problem-choice-bundle"><summary>' + ('条件・参照・配布版を確認' if ja else 'Conditions, references and edition') + '</summary>'
            body += '<h5>' + ('この例の前提条件' if ja else 'Assumptions for this example') + '</h5>' + _paragraph(execution['assumptions'], language)
            body += '<p class="problem-choice-edition">' + ('配布版：' if ja else 'Edition: ') + escape(case['edition']) + '</p><ul>'
            for url, label in [(execution['input'], '固定入力 / JSON' if ja else 'Fixed input / JSON'),
                               (route['references']['url'][language], 'この例の参照・判定条件' if ja else 'This example’s references and checks'),
                               (execution['download'], 'この配布版のコード / ZIP' if ja else 'Code for this edition / ZIP'),
                               (execution['manifest'], '配布ファイルとハッシュ' if ja else 'File manifest and hashes'),
                               (execution['verification'], 'この配布版の検証記録' if ja else 'Verification receipt for this edition')]:
                body += '<li>' + _link(url, label) + '</li>'
            body += '</ul>' + _paragraph('ZIPには複数の例を含む場合があります。実行案内に示す作業フォルダとコマンドを使います。' if ja else 'A ZIP may contain several examples. Use the working directory and commands given in this example’s guide.', language)
            body += '<h5>' + ('検証の限界' if ja else 'Validation limits') + '</h5>' + _paragraph(execution['limits'], language) + '</details></article>'
        body += '</div></details>'
    return body + '</section>'
