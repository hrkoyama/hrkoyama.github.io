#!/usr/bin/env python3
"""Publish the saved reference-solution inventory without evaluating new solutions."""
from collections import Counter
from atlas_reference_catalog import load_reference_cases, SUPPLEMENT_SOURCE, ANNOTATION_SOURCE
from html import escape
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://hrkoyama.github.io'
BASE = '/numerical-methods-atlas/'
ROUTE = BASE + 'solutions/'
SOURCE = 'numerical-methods-atlas/assets/reference-solutions.json'
TRANSLATIONS = 'numerical-methods-atlas/locales/messages.json'
KIND_NAMES = {'analytic': 'Analytic reference', 'semi-analytic': 'Semi-analytic reference', 'manufactured': 'Manufactured solution', 'numerical-reference': 'Finite-grid numerical reference'}
CITATION_ROLES = {'official-setup-cross-check': ('公式の設定・境界の照合', 'Official setup and boundary cross-check'), 'original-problem': ('原問題・誤差解析', 'Original problem and error analysis'), 'reference-software-paper': ('参照ソフトの論文', 'Reference-software paper'), 'executed-reference-implementation': ('実際に照合したコード版', 'Executed reference implementation'), 'algorithm-primary': ('手法の原著（記載した範囲を確認）', 'Primary method source (stated scope reviewed)'), 'analytic-reference': ('解析参照の出典', 'Source of the analytic reference'), 'selected-primary-documentation-or-authored-identity': ('公式資料・著者の式（記載した範囲を確認）', 'Official documentation or authored identity (stated scope reviewed)'), 'selected-official-documentation': ('公式資料（選択部分を確認）', 'Selected official documentation')}

def citation_role(citation, language):
    return CITATION_ROLES.get(citation['role'], (citation['role'], citation['role']))[language == 'en']

REFERENCE_CLASSES = {
    'continuous-exact': ('連続問題の厳密解', 'Continuous exact solution'),
    'semi-analytic': ('半解析参照', 'Semi-analytic reference'),
    'manufactured': ('製造解', 'Manufactured solution'),
    'discrete-exact': ('固定した離散対象の厳密参照', 'Exact reference for a fixed discrete object'),
    'independent-numerical': ('独立な数値参照', 'Independent numerical reference'),
    'self-convergence': ('自己収束比較', 'Self-convergence comparison'),
}
CITATION_ROLES.update({
    'textbook-background': ('教科書の背景資料', 'Textbook background'),
    'reference-documentation': ('既存の参照解説資料', 'Existing reference documentation'),
    'numerical-method': ('数値手法の出典', 'Numerical-method source'),
    'solution-background': ('解の背景資料（確認範囲を参照）', 'Solution background (see read limits)'),
    'atlas-formula-or-saved-result': ('アトラスの式・保存結果', 'Atlas formula or saved result'),
})


def reference_contract_text(case, language):
    contract = case.get('reference_contract', {})
    sampling = contract.get('sampling', '')
    sampling = sampling.get(language, '') if isinstance(sampling, dict) else sampling
    label = REFERENCE_CLASSES.get(case.get('reference_class'), ('', ''))[language == 'en']
    return (' · '.join(part for part in [label, sampling] if part)).strip()


SLICE_NOTE = 'Taylor–Green: x-slice at y = π/4. These are point values, not two-dimensional cell averages.'


def dimension_label(case, language):
    if case['dimension'] is None:
        labels = {
            'finite-dimensional-algebra': ('有限次元の代数問題', 'Finite-dimensional algebra'),
            'finite-dimensional-ivp': ('常微分・微分代数方程式（空間次元なし）', 'ODE / DAE (no spatial dimension)'),
            'nonspatial-stochastic': ('空間次元を持たない確率過程', 'Stochastic process (no spatial dimension)'),
        }
        if case.get('domain_kind') not in labels:
            raise ValueError('A nonspatial reference needs an explicit supported domain')
        return labels[case['domain_kind']][language == 'en']
    if type(case['dimension']) is not int or case['dimension'] not in (1, 2, 3):
        raise ValueError('Invalid spatial reference dimension')
    return str(case['dimension']) + ('次元' if language == 'ja' else 'D')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(root=ROOT):
    root = Path(root)
    source = json.loads((root / SOURCE).read_text())
    messages = json.loads((root / TRANSLATIONS).read_text())
    translations = {' '.join(entry['en'].split()): entry for entry in messages.values() if entry.get('en')}

    def localized(value):
        entry = translations.get(' '.join(value.split()), {})
        if not entry.get('ja'):
            raise ValueError('Missing existing Japanese translation: ' + value)
        return {'ja': entry['ja'], 'en': value}

    cases = []
    for source_case in load_reference_cases(root):
        ident, kind = source_case['id'], source_case['kind']
        if not re.fullmatch(r'[a-z0-9-]+', ident) or kind not in KIND_NAMES:
            raise ValueError('Unknown reference-solution identity or kind: ' + ident)
        if not source_case['formula'].strip():
            raise ValueError('Missing reference formula or dimension: ' + ident)
        dimension_label(source_case, 'en')
        case = {key: source_case[key] for key in ['id', 'model', 'kind', 'formula', 'dimension', 'bounds', 'components', 'field_type', 'parameters', 'sources']}
        if source_case.get('domain_kind') in {'finite-dimensional-algebra', 'finite-dimensional-ivp', 'nonspatial-stochastic'}:
            case['domain_kind'] = source_case['domain_kind']
        case.update(title=localized(source_case['title']), assumptions=localized(source_case['assumptions']),
                    kind_label=localized(KIND_NAMES[kind]),
                    view=source_case.get('view', {language: BASE + '?lang=' + language + '#/exact-solutions?case=' + ident for language in ['ja', 'en']}),
                    reading=source_case.get('reading', {language: BASE + language + '/read/reference-solutions/' for language in ['ja', 'en']}))
        for key in ['citations', 'reference_scope', 'reference_class', 'reference_contract']:
            if key in source_case:
                case[key] = source_case[key]
        if ident == 'taylor-green':
            case['sampling_note'] = localized(SLICE_NOTE)
        cases.append(case)
    if len({case['id'] for case in cases}) != len(cases):
        raise ValueError('Duplicate reference-solution ID')
    extra = {'supplements_source': '/'+SUPPLEMENT_SOURCE, 'supplements_source_sha256': digest(root/SUPPLEMENT_SOURCE)} if (root/SUPPLEMENT_SOURCE).is_file() else {}
    if (root/ANNOTATION_SOURCE).is_file():
        extra.update(metadata_source='/'+ANNOTATION_SOURCE, metadata_source_sha256=digest(root/ANNOTATION_SOURCE))
    return dict(**extra, schema_version=1, url=ORIGIN + ROUTE, source='/' + SOURCE, source_sha256=digest(root / SOURCE),
                translations_source='/' + TRANSLATIONS, translations_source_sha256=digest(root / TRANSLATIONS),
                count=len(cases), counts=dict(Counter(case['kind'] for case in cases)), cases=cases)


def link(url, title):
    return '<a href="' + escape(url, quote=True) + '">' + escape(title) + '</a>'


def section(data, language):
    from atlas_problem_route_cards import render_problem_routes
    ja = language == 'ja'
    title = '厳密解・参照解' if ja else 'Exact and reference solutions'
    intro = (str(data['count']) + '件の保存済み参照解を、名前・式・適用条件から選べます。各カードから既存の表示と解説へ進めます。' if ja else
             'Choose from ' + str(data['count']) + ' saved reference cases by name, formula and assumptions. Open an existing profile or read its explanation.')
    body = '<section data-site-language="' + language + '" lang="' + language + '"><div class="solutions-heading"><p class="solutions-eyebrow">REFERENCE SOLUTION INDEX</p><h1>' + title + '</h1><p>' + intro + '</p></div>'
    body += '<nav class="solutions-navigation" aria-label="' + ('関連する一覧' if ja else 'Related indexes') + '">'
    body += link(BASE + '?lang=' + language, 'アトラスの冒頭' if ja else 'Atlas home')
    body += link(BASE + 'gallery/?lang=' + language, 'テスト問題（名前と図）' if ja else 'Test problems by name and figure')
    body += link(BASE + 'equations/?lang=' + language, '方程式' if ja else 'Equations')
    body += link(BASE + language + '/read/reference-solutions/', '参照解の定義と検証' if ja else 'Reference definitions and verification') + '</nav>'
    body += '<details class="solutions-scope"><summary>' + ('参照解の種類と表示範囲' if ja else 'Reference types and display scope') + '</summary><p>' + ('解析解・半解析解・製造解・有限格子の数値参照を区別します。半解析解は有限精度の求根・ODE積分・求積などを含み、製造解は目標解から外力を選びます。数値参照は別計算で得た有限格子の結果で、離散化・境界・時間刻みの誤差や参照自身の感度が残ります。厳密解や保証された誤差上界ではありません。' if ja else
             'Analytic, semi-analytic, manufactured and finite-grid numerical references are distinct. Semi-analytic cases include finite-precision roots, ODE integration or quadrature; manufactured cases choose forcing from a target solution. Numerical references come from separate computations and retain discretization, boundary and time-step errors and their own resolution sensitivity. They are not exact solutions or guaranteed error bounds.') + '</p><p>'
    body += ('次元は元データの定義に従います。有限次元の代数問題とODE・DAEには空間次元を割り当てません。Taylor–Greenは2次元の式ですが、既存の表示は y = π/4 のx方向断面です。' if ja else
             'Dimensions follow the source metadata. Finite-dimensional algebraic problems and ODE/DAE models have no assigned spatial dimension. Taylor–Green has a two-dimensional formula; the existing display is an x-slice at y = π/4.') + '</p></details>'
    body += '<div class="solutions-summary">' + ''.join('<span>' + escape(next(case['kind_label'][language] for case in data['cases'] if case['kind'] == kind)) + ' · ' + str(data['counts'].get(kind, 0)) + '</span>' for kind in KIND_NAMES if data['counts'].get(kind)) + '</div>'
    body += '<!-- comparison-solution-controls:' + language + ' --><div class="comparison-solution-controls" data-comparison-solution-controls hidden><label>' + ('種類から選ぶ' if ja else 'Choose a reference type') + '<select data-comparison-solution-kind><option value="all">' + ('すべて' if ja else 'All') + ' (' + str(data['count']) + ')</option>'
    body += ''.join('<option value="' + kind + '">' + escape(next(case['kind_label'][language] for case in data['cases'] if case['kind'] == kind)) + ' (' + str(data['counts'].get(kind, 0)) + ')</option>' for kind in KIND_NAMES if data['counts'].get(kind)) + '</select></label><p data-comparison-solution-count role="status" aria-live="polite">' + (str(data['count']) + ' / ' + str(data['count']) + '件を表示' if ja else 'Showing ' + str(data['count']) + ' of ' + str(data['count']) + ' references') + '</p></div><!-- /comparison-solution-controls:' + language + ' -->'
    body += '<div class="solutions-grid">'
    for case in data['cases']:
        body += '<article class="solution-card" id="solution-' + case['id'] + '-' + language + '" data-solution-id="' + case['id'] + '" data-solution-kind="' + case['kind'] + '">'
        body += '<div class="solution-badges"><span class="solution-kind">' + escape(case['kind_label'][language]) + '</span><span class="solution-dimension">' + escape(dimension_label(case, language)) + '</span></div>'
        body += '<h2>' + escape(case['title'][language]) + '</h2><p class="solution-formula" dir="ltr">' + escape(case['formula']) + '</p>'
        body += '<p class="solution-assumptions">' + escape(case['assumptions'][language]) + '</p>'
        if case.get('sampling_note'):
            body += '<p class="solution-sampling">' + escape(case['sampling_note'][language]) + '</p>'
        if reference_contract_text(case, language):
            body += '<p class="solution-sampling">'+escape(reference_contract_text(case, language))+'</p>'
        body += '<nav class="solution-links comparison-primary-links" aria-label="' + escape(case['title'][language], quote=True) + '">'
        body += link(case['view'][language], '保存済みの解を表示 →' if ja else 'View the saved profile →')
        body += link(case['reading'][language], '定義・条件を読む' if ja else 'Read definitions and conditions') + '</nav>'
        if case.get('citations'):
            body += '<details class="solution-citations"><summary>'+('出典・参照実装と確認範囲' if ja else 'Sources, reference software and scope')+'</summary><ul>'
            for citation in case['citations']:
                body += '<li>'+escape(citation_role(citation, language))+': '+link(citation['url'], citation['title'])+(' — '+escape(citation.get('note', '')) if citation.get('note') else '')+'</li>'
            body += '</ul></details>'
        related_problems = case.get('related_problems', [])
        if related_problems:
            body += '<details class="comparison-details" data-comparison-detail="solution-' + case['id'] + '-' + language + '" open><summary>' + ('関連する問題の図・コードと検証状況' if ja else 'Related problem figures, code and validation status') + '</summary><div class="comparison-details-body">'
        body += render_problem_routes(related_problems, language, heading_level=3, limit=3)
        if related_problems:
            body += '</div></details>'
        body += '</article>'
    body += '</div><footer class="solutions-footer">' + link('index.json', 'JSON') + link('index.md', 'Markdown')
    body += link('/' + SOURCE, '参照値の元データ' if ja else 'Source reference values')
    if data.get('metadata_source'):
        body += link(data['metadata_source'], '参照の種類・出典の確認範囲（JSON）' if ja else 'Reference classes and read limits (JSON)')
        body += link('/catalog/atlas-legacy-reference-contracts-2026-11-25.json', '旧配布版の検証契約と不足範囲（JSON）' if ja else 'Legacy contracts and qualification gaps (JSON)')
    body += link('/using/', '引用と利用条件' if ja else 'Citation and reuse') + '</footer></section>'
    return body


def markdown(data):
    from atlas_problem_route_cards import markdown_problem_routes
    result = '# 厳密解・参照解 / Exact and reference solutions\n\n'
    result += 'Source: ' + ORIGIN + data['source'] + '\n\nSHA-256: `' + data['source_sha256'] + '`\n\n'
    for language in ['ja', 'en']:
        ja = language == 'ja'
        result += '## ' + ('日本語' if ja else 'English') + '\n\n'
        for case in data['cases']:
            result += '### ' + case['title'][language] + '\n\n'
            result += case['kind_label'][language] + ' · ' + dimension_label(case, language) + '\n\n'
            result += '`' + case['formula'] + '`\n\n' + case['assumptions'][language] + '\n\n'
            if case.get('sampling_note'):
                result += case['sampling_note'][language] + '\n\n'
            if reference_contract_text(case, language):
                result += reference_contract_text(case, language)+'\n\n'
            result += '[' + ('保存済みの解を表示' if ja else 'View the saved profile') + '](' + ORIGIN + case['view'][language] + ') · [' + ('定義・条件を読む' if ja else 'Read definitions and conditions') + '](' + ORIGIN + case['reading'][language] + ')\n\n'
            for citation in case.get('citations', []):
                result += '- '+citation['role']+': ['+citation['title']+']('+citation['url']+')'+(' — '+citation.get('note', '') if citation.get('note') else '')+'\n'
            result += markdown_problem_routes(case.get('related_problems', []), language) + '\n\n'
    return result.rstrip() + '\n'


def build(root=ROOT, problem_routes=None):
    root = Path(root)
    data = load(root)
    if problem_routes is None:
        from atlas_problem_routes import load_problem_routes
        problem_routes = load_problem_routes(root)
    for case in data['cases']:
        case['related_problems'] = problem_routes['references'][case['id']]
    data['problem_routes_source_sha256'] = problem_routes['source_sha256']
    css_hash = digest(root / 'styles/atlas-solutions.css')[:12]
    routes_css_hash = digest(root / 'styles/atlas-problem-routes.css')[:12]
    comparison_css_hash = digest(root / 'styles/atlas-comparison-overview.css')[:12]
    comparison_js_hash = digest(root / 'frontend/atlas/comparison-overview.js')[:12]
    head = '<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    head += '<title data-page-title-ja="厳密解・参照解 | 数値計算法アトラス" data-page-title-en="Exact and reference solutions | Numerical Methods Atlas">厳密解・参照解 | 数値計算法アトラス</title>'
    head += '<meta name="description" content="保存済みの解析・半解析・製造解と有限格子数値参照を、式・適用条件・限界から選ぶ一覧。Analytic, semi-analytic, manufactured and finite-grid numerical references, with assumptions and limits.">'
    head += '<link rel="canonical" href="' + ORIGIN + ROUTE + '"><link rel="stylesheet" href="/styles/atlas-solutions.css?v=' + css_hash + '"><link rel="stylesheet" href="/styles/atlas-problem-routes.css?v=' + routes_css_hash + '"><link rel="stylesheet" href="/styles/atlas-comparison-overview.css?v=' + comparison_css_hash + '"><script type="module" src="/frontend/atlas/comparison-overview.js?v=' + comparison_js_hash + '"></script></head>'
    document = head + '<body class="profile-page atlas-solutions" data-site-language-anchors="suffix"><main id="main" class="solutions-index" data-comparison-overview="solutions">' + ''.join(section(data, language) for language in ['ja', 'en']) + '</main></body></html>\n'
    directory = root / ROUTE.strip('/')
    directory.mkdir(parents=True, exist_ok=True)
    (directory / 'index.html').write_text(document)
    (directory / 'index.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    (directory / 'index.md').write_text(markdown(data))
    print('Built saved-reference solution index:', data['count'], 'cases;', data['counts'])
    return data


if __name__ == '__main__':
    build()
