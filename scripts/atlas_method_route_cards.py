"""Render method-specific routes without borrowing another method's execution."""
from html import escape
import re
from urllib.parse import unquote, urljoin, urlsplit


LANGUAGES = ('ja', 'en')
ORIGIN = 'https://hrkoyama.github.io'
SECTIONS = {
    'equations': {'ja': '方程式', 'en': 'Equations'},
    'problems': {'ja': '問題の図', 'en': 'Problem figures'},
    'references': {'ja': '厳密解・参照解', 'en': 'Exact / reference solutions'},
    'execution': {'ja': 'コード・検証', 'en': 'Code and validation'},
}


def _language(language):
    if language not in LANGUAGES:
        raise ValueError('Unsupported method-route language: ' + str(language))
    return language == 'ja'


def _text(value, language):
    result = value.get(language, '') if isinstance(value, dict) else (value or '')
    if not isinstance(result, str):
        raise ValueError('Invalid method-route text')
    return result


def _url(value):
    if not isinstance(value, str) or not value or any(char.isspace() for char in value):
        raise ValueError('Missing or invalid method-route URL')
    if value.startswith('#'):
        if not re.fullmatch(r'#[a-z0-9-]+', value):
            raise ValueError('Invalid method-route fragment')
        return value
    parsed = urlsplit(urljoin(ORIGIN + '/', value))
    if (parsed.scheme != 'https' or parsed.netloc != 'hrkoyama.github.io' or
            parsed.username or parsed.password or
            any(part in {'.', '..'} or part.startswith('.') for part in unquote(parsed.path).split('/') if part)):
        raise ValueError('Invalid public method-route URL: ' + value)
    if not (value.startswith('https://') or value.startswith('/')):
        raise ValueError('Method-route URL must be absolute or site-relative')
    return value


def _link(url, label, attrs=''):
    return '<a href="' + escape(_url(url), quote=True) + '"' + attrs + '>' + escape(label) + '</a>'


def _id(value):
    if not isinstance(value, str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]*', value):
        raise ValueError('Invalid method-route identity: ' + str(value))
    return value


def _name(row, language, key='name'):
    name = _text(row.get(key), language)
    if not name.strip():
        raise ValueError('Missing method-route name')
    return name


def _paragraph(value, language, css='method-route-note'):
    text = _text(value, language)
    return '<p class="' + css + '">' + escape(text) + '</p>' if text else ''


def _section_id(section, language):
    return 'method-' + section + '-' + language


def _reference_kind(kind, language):
    labels = {
        'analytic': {'ja': '解析参照', 'en': 'Analytic reference'},
        'semi-analytic': {'ja': '半解析参照', 'en': 'Semi-analytic reference'},
        'manufactured': {'ja': '製造解', 'en': 'Manufactured solution'},
        'numerical-reference': {'ja': '有限格子の数値参照', 'en': 'Finite-grid numerical reference'},
    }
    if kind not in labels:
        raise ValueError('Unknown method reference kind: ' + str(kind))
    return labels[kind][language]


def _runs(route):
    selected, seen = [], set()
    for problem in route.get('problems', []):
        for execution in problem.get('executions', []):
            ident = _id(execution['id'])
            if execution.get('method_ids') is not None and route['method_id'] not in execution['method_ids']:
                raise ValueError('Execution belongs to another method: ' + ident)
            key = (execution.get('kind'), ident)
            if key not in seen:
                seen.add(key)
                selected.append((execution, problem))
    return selected


def render_method_route_links(route, lang, base=''):
    """Four compact destinations; code availability is never inferred from a count."""
    _language(lang)
    counts = {key: len(route.get(key, [])) for key in ['equations', 'problems', 'references']}
    body = '<nav class="method-route-links" data-method-route-links="' + _id(route['method_id']) + '" aria-label="' + ('手法から関連資料へ' if lang == 'ja' else 'Method resources') + '">'
    for key, labels in SECTIONS.items():
        label = labels[lang]
        if key in {'equations', 'problems'}:
            label += ' (' + str(counts[key]) + ')'
        body += _link(base + '#' + _section_id(key, lang), label, ' data-method-route-link="' + key + '"')
    return body + '</nav>'


def _limited(rows, render, language, css, limit=3):
    rows = list(rows)
    body = '<ul class="' + css + '">' + ''.join(render(row) for row in rows[:limit]) + '</ul>'
    if len(rows) > limit:
        count = len(rows) - limit
        title = '残り' + str(count) + '件を表示' if language == 'ja' else 'Show ' + str(count) + ' more'
        body += '<details class="method-route-more"><summary>' + title + '</summary><ul class="' + css + '">' + ''.join(render(row) for row in rows[limit:]) + '</ul></details>'
    return body


def _execution_links(execution, language):
    ja = language == 'ja'
    name = _name(execution, language)
    body = _link(execution['guide'][language], ('実行・検証：' if ja else 'Run and validate: ') + name, ' data-method-execution-link')
    body += _link(execution['download'], ('コードZIP：' if ja else 'Code ZIP: ') + name, ' data-method-execution-download')
    return body


def _problem_card(row, language):
    ja = language == 'ja'
    ident, name, image = _id(row['id']), _name(row, language), row['image']
    for key in ['width', 'height']:
        if isinstance(image[key], bool) or not isinstance(image[key], int) or image[key] <= 0:
            raise ValueError('Invalid method problem-image dimensions')
    executions = row.get('executions', [])
    role = row.get('role', 'related')
    if role not in {'execution', 'related'}:
        raise ValueError('Invalid method problem role')
    badge = ('この手法の実行例あり' if ja else 'Matched method execution') if executions else ('関連する検証問題' if ja else 'Related validation problem')
    caption = _text(image.get('caption'), language)
    body = '<li class="method-route-problem" data-linked-problem-id="' + ident + '" data-method-problem-role="' + role + '"><div class="method-route-problem-overview">'
    body += '<a class="method-route-picture" data-method-problem-picture href="' + escape(_url(row['hub'][language]), quote=True) + '"><img src="' + escape(_url(image['url']), quote=True) + '" alt="' + escape(name + (' — ' + caption if caption else ''), quote=True) + '" width="' + str(image['width']) + '" height="' + str(image['height']) + '" loading="lazy" decoding="async"></a>'
    body += '<div class="method-route-problem-copy"><p class="method-route-name">' + _link(row['hub'][language], name, ' data-method-problem-name') + '</p><p class="method-route-badge">' + badge + '</p>'
    body += _paragraph(row.get('method_note'), language)
    if row.get('note') and row.get('note') != row.get('method_note'):
        body += _paragraph(row['note'], language)
    body += '<p class="method-route-actions">' + _link(row['reference_url'][language], 'この問題の参照・検証資料' if ja else 'This problem’s references and checks', ' data-method-problem-reference')
    body += _link(row['code'][language], 'この問題のコード・検証状況' if ja else 'This problem’s code and validation status', ' data-method-problem-code') + '</p></div></div>'
    if executions:
        body += '<ul class="method-route-matched-runs">'
        for execution in executions:
            body += '<li data-method-execution-id="' + _id(execution['id']) + '">' + _execution_links(execution, language)
            scope = _text(execution.get('scope'), language)
            if scope:
                body += '<details class="method-route-scope"><summary>' + ('この実行例の範囲' if ja else 'Scope of this execution example') + '</summary><p>' + escape(scope) + '</p></details>'
            body += '</li>'
        body += '</ul>'
    else:
        body += '<p class="method-route-empty method-route-no-execution">' + ('この手法でこの問題を解く固定入力実行例は未登録です。' if ja else 'No fixed-input execution of this problem is registered for this method.') + '</p>'
    return body + '</li>'


def _reference_context(context, language):
    ja = language == 'ja'
    ident, name = _id(context['problem_id']), _name(context, language, 'problem_name')
    body = '<li class="method-route-reference-context" data-method-reference-problem-id="' + ident + '"><h3>' + _link(context['reference_url'][language], name, ' data-method-reference-context') + '</h3>'
    cases = context.get('cases', [])
    if not cases:
        body += '<p class="method-route-note">' + ('参照解一覧の対応カードは未登録です。この問題の解析的基準・独立数値参照・保存則などは、問題ごとの参照・検証資料で確認できます。' if ja else 'No corresponding reference-library card is registered. Consult this problem’s references and checks for analytic standards, independent numerical references or conservation checks.') + '</p>'
    else:
        body += '<ul class="method-route-reference-cases">'
        for case in cases:
            relation = case.get('relation')
            if relation not in {'same-problem', 'related-model'}:
                raise ValueError('Invalid method reference relation')
            label = ({'same-problem': '同じ問題の参照', 'related-model': '関連モデルの参照'} if ja else {'same-problem': 'Same-problem reference', 'related-model': 'Related-model reference'})[relation]
            body += '<li data-method-reference-id="' + _id(case['id']) + '" data-reference-relation="' + relation + '"><p class="method-route-badge">' + label + ' · ' + _reference_kind(case['kind'], language) + '</p><p class="method-route-name">' + _link(case['url'][language], _name(case, language, 'title')) + '</p>'
            body += _paragraph(case.get('note'), language, 'method-route-reference-note')
            body += '<p class="method-route-actions">' + _link(case['view'][language], '既存の参照図を表示' if ja else 'View the existing reference profile') + '</p></li>'
        body += '</ul>'
    body += '<p class="method-route-actions">' + _link(context['reference_url'][language], 'この問題の参照・検証資料へ' if ja else 'Open this problem’s references and checks') + '</p>'
    return body + '</li>'


def _method_reference_resources(record, language):
    """Use existing record fields; saved results never become independent references."""
    ja = language == 'ja'
    resources, seen = [], set()

    def add(role, value, label):
        url = _text(value, language)
        if url and (role, url) not in seen:
            seen.add((role, url))
            resources.append({'role': role, 'url': _url(url), 'label': label})

    reading = _text(record.get('reading'), language)
    reading_fallback = False
    if not reading and isinstance(record.get('reading'), dict):
        reading = record['reading'].get('en', '')
        reading_fallback = bool(reading)
    english_reading = ja and reading and (reading_fallback or '/en/read/' in urlsplit(reading).path)
    reading_label = '手法の解説・条件' + ('（英語）' if english_reading else '') if ja else 'Method explanation and conditions'
    add('reading', reading, reading_label)
    add('independent-reference', record.get('independent_reference'), '独立参照の保存データ' if ja else 'Saved independent-reference data')
    result_urls = record.get('result_urls', {})
    if not isinstance(result_urls, dict):
        raise ValueError('Method result URLs must be a case-name mapping')
    for name, url in result_urls.items():
        add('result', url, str(name) + ' の保存結果' if ja else 'Saved results: ' + str(name))
    add('result', record.get('results'), 'この配布版の保存結果' if ja else 'Saved results from this edition')
    add('verification', record.get('code_verification'), '配布版の検証記録' if ja else 'Edition verification receipt')
    return resources


def _reference_resource_role(role, language):
    return {
        'reading': {'ja': '解説', 'en': 'Explanation'},
        'independent-reference': {'ja': '独立参照', 'en': 'Independent reference'},
        'result': {'ja': '保存結果', 'en': 'Saved result'},
        'verification': {'ja': '検証記録', 'en': 'Verification receipt'},
    }[role][language]


def _render_method_reference_resources(record, language):
    ja = language == 'ja'
    resources = _method_reference_resources(record, language)
    if not resources:
        return ''

    def render(resource):
        return '<li><span class="method-route-resource-role">' + _reference_resource_role(resource['role'], language) + '</span>' + _link(resource['url'], resource['label'], ' data-method-reference-resource="' + resource['role'] + '"') + '</li>'

    body = '<div class="method-route-reference-resources"><h3>' + ('手法の解説・独立参照・保存結果' if ja else 'Method explanations, independent references and saved results') + '</h3><p class="method-route-note">' + ('資料ごとに役割を示しています。適用条件と照合方法は各資料で確認してください。' if ja else 'Each resource is labeled by its role. Consult it for applicable conditions and comparison procedures.') + '</p>'
    fixed = [resource for resource in resources if resource['role'] != 'result']
    if fixed:
        body += '<ul class="method-route-reference-resource-list">' + ''.join(render(resource) for resource in fixed) + '</ul>'
    results = [resource for resource in resources if resource['role'] == 'result']
    if results:
        body += '<h4>' + ('保存結果' if ja else 'Saved results') + '</h4>' + _limited(results, render, language, 'method-route-reference-resource-list')
    return body + '</div>'


def _source_urls(record, key):
    values = record.get(key, [])
    if not isinstance(values, list):
        raise ValueError('Method source URLs must be a list')
    return list(dict.fromkeys(values))


def _download(record):
    if record.get('code_download'):
        return record['code_download']
    if record.get('code_urls') or record.get('source_urls') or record.get('test_urls'):
        return record.get('fallback_download') or record.get('globalfallback_download')
    return None


def _legacy_examples(route, record):
    matched = {execution['id'] for execution, _ in _runs(route)}
    return [example for example in record.get('execution_examples', []) if example['id'] not in matched and example.get('guide')]


def _code_section(route, language, record):
    ja = language == 'ja'
    runs = _runs(route)
    body = '<p class="method-route-intro">' + ('問題図に対応する実行例と、手法の既存配布版・関連ソースを分けて示します。実行範囲は各案内の固定入力と確認条件に従います。' if ja else 'Matched problem executions are separated from existing method editions and related source. Execution scope follows each guide’s fixed inputs and checks.') + '</p>'
    if runs:
        body += '<h3>' + ('この手法と問題図が対応する実行例' if ja else 'Executions matched to this method and a problem figure') + '</h3><ul class="method-route-execution-list">'
        for execution, problem in runs:
            body += '<li data-method-matched-execution-id="' + _id(execution['id']) + '"><p class="method-route-name">' + _link(problem['hub'][language], _name(problem, language)) + '</p><div class="method-route-execution-actions">' + _execution_links(execution, language)
            for key, label in [('input', '固定入力 / JSON' if ja else 'Fixed input / JSON'), ('verification', '検証記録' if ja else 'Verification receipt')]:
                if execution.get(key):
                    body += _link(execution[key], label)
            body += '</div>' + _paragraph(execution.get('scope'), language) + '</li>'
        body += '</ul>'
    else:
        body += '<p class="method-route-empty method-route-no-matched-executions">' + ('この手法と問題図を対応付けた固定入力実行例は未登録です。' if ja else 'No fixed-input execution example is linked between this method and a problem figure.') + '</p>'
    legacy = _legacy_examples(route, record)
    if legacy:
        body += '<h3>' + ('問題図との対応付けとは別の登録実行・検査例' if ja else 'Registered executions and checks separate from problem-figure links') + '</h3><ul class="method-route-legacy-examples">'
        for example in legacy:
            guide = _text(example['guide'], language)
            name = _text(example.get('name'), language) or example['id']
            body += '<li data-method-other-execution-id="' + _id(example['id']) + '">' + _link(guide, name) + '</li>'
        body += '</ul>'
    sources = list(dict.fromkeys(_source_urls(record, 'code_urls') + _source_urls(record, 'source_urls')))
    tests = _source_urls(record, 'test_urls')
    download = _text(_download(record), language)
    if sources or tests or download or record.get('code_verification'):
        body += '<div class="method-route-package"><h3>' + ('既存の配布版・関連ソースと検査' if ja else 'Existing editions, related source and tests') + '</h3><p class="method-route-note">' + ('共用のモジュールや配布版全体の検査を含みます。個々の問題専用の実装・検査であるという意味ではありません。' if ja else 'These resources include shared modules and package-wide checks; they are not all dedicated implementations or tests for an individual problem.') + '</p>'
        body += _paragraph(record.get('depth_scope'), language)
        body += _paragraph(record.get('code_mapping_scope'), language)
        body += '<p class="method-route-actions">'
        if download:
            body += _link(download, '対応する配布版 / ZIP' if ja else 'Related code edition / ZIP', ' data-method-code-download')
        if record.get('code_verification'):
            body += _link(_text(record['code_verification'], language), '配布版の検証記録' if ja else 'Edition verification receipt', ' data-method-code-verification')
        body += '</p>'
        for urls, title in [(sources, '関連ソース' if ja else 'Related source'), (tests, '配布版のテスト' if ja else 'Package tests')]:
            if urls:
                body += '<h4>' + title + '</h4>' + _limited(urls, lambda url: '<li>' + _link(url, unquote(urlsplit(url).path)) + '</li>', language, 'method-route-source-list')
        if record.get('run_commands'):
            body += '<details class="method-route-scope"><summary>' + ('配布版の検査・実行コマンド' if ja else 'Package check and execution commands') + '</summary><p>' + ('複数例の検査や図生成を含む場合があります。条件と作業フォルダは配布版の案内を確認してください。' if ja else 'Commands may include checks or figure generation for several cases. Consult the edition’s guide for conditions and working directory.') + '</p><pre><code>' + escape('\n'.join(record['run_commands'])) + '</code></pre></details>'
        body += '</div>'
    else:
        body += '<p class="method-route-empty">' + ('この手法に対応するソース・検査・配布版のリンクは未登録です。' if ja else 'No related source, tests or code-edition links are registered for this method.') + '</p>'
    return body


def render_method_routes(route, lang, record):
    """Detail-page sections, using only the reviewed links and filtered runs supplied."""
    ja = _language(lang)
    _id(route['method_id'])
    _runs(route)
    body = '<div class="method-route-navigation" data-method-navigation="' + _id(route['method_id']) + '">'
    for section, labels in SECTIONS.items():
        body += '<section class="method-route-section" id="' + _section_id(section, lang) + '" data-method-section="' + section + '"><h2>' + labels[lang] + '</h2>'
        rows = route.get(section, [])
        if section == 'equations':
            body += '<p class="method-route-intro">' + ('この手法に対応付けられた問題から方程式をたどれます。検証した範囲は各問題の入力・境界条件に従います。' if ja else 'Equations are linked through associated test problems. The checked scope follows each problem’s inputs and boundaries.') + '</p>'
            if rows:
                def equation(row):
                    count = len(row.get('problem_ids', []))
                    return '<li data-linked-equation-id="' + _id(row['id']) + '">' + _link(row['url'][lang], _name(row, lang)) + '<span class="method-route-meta">' + (str(count) + '問題から対応' if ja else 'Linked through ' + str(count) + ' problem' + ('' if count == 1 else 's')) + '</span></li>'
                body += _limited(rows, equation, lang, 'method-route-equation-list')
            else:
                body += '<p class="method-route-empty">' + ('この手法に対応付けられた問題からたどれる方程式一覧の項目は未登録です。' if ja else 'No equation-registry entry is linked through this method’s associated problems.') + '</p>'
        elif section == 'problems':
            if rows:
                body += _limited(rows, lambda row: _problem_card(row, lang), lang, 'method-route-problem-list')
            else:
                body += '<p class="method-route-empty">' + ('この手法に対応付けられたテスト問題の図は未登録です。' if ja else 'No test-problem figure is registered for this method.') + '</p>'
        elif section == 'references':
            body += '<p class="method-route-intro">' + ('参照資料は問題ごとに示します。「関連モデル」の初期値・境界・標本化は、問題の図と同じとは限りません。' if ja else 'References are shown in their problem context. Related-model initial data, boundaries and sampling may differ from the problem figure.') + '</p>'
            if rows:
                body += _limited(rows, lambda row: _reference_context(row, lang), lang, 'method-route-reference-list')
            else:
                body += '<p class="method-route-empty">' + ('この手法の問題図に結び付く参照資料は未登録です。' if ja else 'No reference context is registered for this method’s problem figures.') + '</p>'
            body += _render_method_reference_resources(record, lang)
        else:
            body += _code_section(route, lang, record)
        body += '</section>'
    return body + '</div>'


def _md_text(value):
    return value.replace('\\', '\\\\').replace('[', '\\[').replace(']', '\\]').replace('\n', ' ')


def _md_link(url, label, image=False):
    return ('!' if image else '') + '[' + _md_text(label) + '](' + _url(url).replace('(', '%28').replace(')', '%29') + ')'


def markdown_method_routes(route, record):
    """Bilingual text edition retaining problem-specific reference and code scope."""
    _id(route['method_id'])
    runs = _runs(route)
    lines = ['## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code', '']
    for language in LANGUAGES:
        ja = language == 'ja'
        lines += ['### ' + ('日本語' if ja else 'English'), '']
        for section, labels in SECTIONS.items():
            lines += ['#### ' + labels[language] + ' (`' + _section_id(section, language) + '`)', '']
            rows = route.get(section, [])
            if section == 'equations':
                lines += ['問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。' if ja else 'These links are derived through associated problems; checked scope follows their inputs and boundaries.', '']
                if rows:
                    lines += ['- ' + _md_link(row['url'][language], _name(row, language)) + ' (`' + _id(row['id']) + '`; ' + ', '.join(row.get('problem_ids', [])) + ')' for row in rows]
                else:
                    lines += ['対応する方程式一覧の項目は未登録です。' if ja else 'No corresponding equation-registry entry is registered.']
            elif section == 'problems':
                if not rows:
                    lines += ['この手法に対応付けられたテスト問題の図は未登録です。' if ja else 'No test-problem figure is registered for this method.']
                for row in rows:
                    lines += ['##### ' + _md_link(row['hub'][language], _name(row, language)) + ' (`' + _id(row['id']) + '`)', '', _md_link(row['image']['url'], _text(row['image'].get('caption'), language) or _name(row, language), image=True), '']
                    for key in ['method_note', 'note']:
                        note = _text(row.get(key), language)
                        if note and (key != 'note' or row.get(key) != row.get('method_note')):
                            lines += [note, '']
                    lines += [_md_link(row['reference_url'][language], 'この問題の参照・検証資料' if ja else 'This problem’s references and checks') + ' · ' + _md_link(row['code'][language], 'この問題のコード・検証状況' if ja else 'This problem’s code and validation status'), '']
                    if not row.get('executions'):
                        lines += ['この手法でこの問題を解く固定入力実行例は未登録です。' if ja else 'No fixed-input execution of this problem is registered for this method.', '']
                    for execution in row.get('executions', []):
                        lines += ['- ' + _md_link(execution['guide'][language], _name(execution, language)) + ' (`' + _id(execution['id']) + '`) · ' + _md_link(execution['download'], 'コードZIP' if ja else 'Code ZIP')]
                        if execution.get('scope'):
                            lines += ['', _text(execution['scope'], language), '']
            elif section == 'references':
                if not rows:
                    lines += ['この手法の問題図に結び付く参照資料は未登録です。' if ja else 'No reference context is registered for this method’s problem figures.']
                for context in rows:
                    lines += ['##### ' + _md_link(context['reference_url'][language], _name(context, language, 'problem_name')) + ' (`' + _id(context['problem_id']) + '`)', '']
                    if not context.get('cases'):
                        lines += ['参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。' if ja else 'No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.', '']
                    for case in context.get('cases', []):
                        relation = case['relation']
                        if relation not in {'same-problem', 'related-model'}:
                            raise ValueError('Invalid method reference relation')
                        label = ({'same-problem': '同じ問題の参照', 'related-model': '関連モデルの参照'} if ja else {'same-problem': 'Same-problem reference', 'related-model': 'Related-model reference'})[relation]
                        lines += ['- ' + _md_link(case['url'][language], _name(case, language, 'title')) + ' (`' + _id(case['id']) + '`; ' + label + '; ' + _reference_kind(case['kind'], language) + ')', '', _text(case.get('note'), language), '', _md_link(case['view'][language], '既存の参照図' if ja else 'Existing reference profile'), '']
                resources = _method_reference_resources(record, language)
                if resources:
                    lines += ['##### ' + ('手法の解説・独立参照・保存結果' if ja else 'Method explanations, independent references and saved results'), '', '資料ごとの役割と適用条件・照合方法を確認してください。' if ja else 'Check each resource’s role, applicable conditions and comparison procedure.', '']
                    lines += ['- ' + _reference_resource_role(resource['role'], language) + ': ' + _md_link(resource['url'], resource['label']) for resource in resources]
                    lines.append('')
            else:
                lines += ['問題図に対応する実行例と、既存配布版・関連ソースを区別します。' if ja else 'Matched problem executions are separate from existing editions and related source.', '']
                if not runs:
                    lines += ['この手法と問題図を対応付けた固定入力実行例は未登録です。' if ja else 'No fixed-input execution example is linked between this method and a problem figure.', '']
                for execution, problem in runs:
                    lines += ['##### ' + _name(execution, language) + ' (`' + _id(execution['id']) + '`)', '', _md_link(problem['hub'][language], _name(problem, language)) + ' · ' + _md_link(execution['guide'][language], '実行・検証' if ja else 'Run and validate') + ' · ' + _md_link(execution['download'], 'コードZIP' if ja else 'Code ZIP'), '']
                    for key, label in [('input', '固定入力' if ja else 'Fixed input'), ('verification', '検証記録' if ja else 'Verification receipt')]:
                        if execution.get(key):
                            lines += [_md_link(execution[key], label), '']
                    if execution.get('scope'):
                        lines += [_text(execution['scope'], language), '']
                legacy = _legacy_examples(route, record)
                if legacy:
                    lines += ['##### ' + ('問題図との対応付けとは別の登録実行・検査例' if ja else 'Registered executions and checks separate from problem-figure links'), '']
                    lines += ['- ' + _md_link(_text(example['guide'], language), _text(example.get('name'), language) or example['id']) + ' (`' + _id(example['id']) + '`)' for example in legacy]
                    lines.append('')
                sources = list(dict.fromkeys(_source_urls(record, 'code_urls') + _source_urls(record, 'source_urls')))
                tests = _source_urls(record, 'test_urls')
                download = _text(_download(record), language)
                if sources or tests or download or record.get('code_verification'):
                    lines += ['##### ' + ('既存の配布版・関連ソースと検査' if ja else 'Existing editions, related source and tests'), '', '共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。' if ja else 'Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.', '']
                    for key in ['depth_scope', 'code_mapping_scope']:
                        if record.get(key):
                            lines += [_text(record[key], language), '']
                    if download:
                        lines += [_md_link(download, '対応する配布版 / ZIP' if ja else 'Related code edition / ZIP'), '']
                    if record.get('code_verification'):
                        lines += [_md_link(_text(record['code_verification'], language), '配布版の検証記録' if ja else 'Edition verification receipt'), '']
                    for urls, title in [(sources, '関連ソース' if ja else 'Related source'), (tests, '配布版のテスト' if ja else 'Package tests')]:
                        if urls:
                            lines += ['###### ' + title, ''] + ['- ' + _md_link(url, unquote(urlsplit(url).path)) for url in urls] + ['']
                    if record.get('run_commands'):
                        lines += ['配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。' if ja else 'Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.', '', '```sh', *record['run_commands'], '```', '']
                else:
                    lines += ['この手法に対応するソース・検査・配布版のリンクは未登録です。' if ja else 'No related source, tests or code-edition links are registered for this method.', '']
            lines.append('')
    return '\n'.join(lines).rstrip() + '\n'
