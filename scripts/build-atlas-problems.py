#!/usr/bin/env python3
"""Build problem pages from curated links and existing execution evidence only."""
from html import escape
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = '/numerical-methods-atlas/'
LANGUAGES = ('ja', 'en')
SECTION_LABELS = {
    'equations': {'ja': '方程式・問題の定義', 'en': 'Equations and problem definitions'},
    'references': {'ja': '厳密解・参照解', 'en': 'Exact and reference solutions'},
    'methods': {'ja': '計算法', 'en': 'Numerical methods'},
    'code': {'ja': 'コード・実行', 'en': 'Code and execution'},
}
STATUS = {
    'educational-example': {'ja': '教育用例・関連コードあり', 'en': 'Educational example / related code'},
    'reading-only': {'ja': '解説のみ・専用実装なし', 'en': 'Reading only / no dedicated implementation'},
    'planned': {'ja': '収録予定', 'en': 'Planned coverage'},
}
SOURCE_LABELS = {
    'existing-figure': {'ja': '保存済みの結果図', 'en': 'Saved result figure'},
    'stored-data-plot': {'ja': '保存数値データを図示', 'en': 'Plot of saved numerical data'},
    'computed-preview': {'ja': '保存済みの計算プレビュー', 'en': 'Saved computed preview'},
}
FORMULATION_ROLES = {
    'problem': {'ja': '問題の式', 'en': 'Problem definition'},
    'approximation': {'ja': '近似・離散化の式', 'en': 'Approximation or discretization'},
    'diagnostic': {'ja': '診断量の定義', 'en': 'Diagnostic definition'},
    'example-definition': {'ja': '実行例の定義・検証式', 'en': 'Example definition or validation formula'},
}


def localized(value, language):
    return value.get(language, '') if isinstance(value, dict) else (value or '')


def paragraph(value, language, css=''):
    text = localized(value, language)
    return '<p'+(' class="'+css+'"' if css else '')+'>'+escape(text)+'</p>' if text else ''


def link(url, label, css=''):
    return '<a href="'+escape(url, quote=True)+'"'+(' class="'+css+'"' if css else '')+'>'+escape(label)+'</a>'


def kind_label(kind, language):
    return ('共通実行例' if language == 'ja' else 'Common execution example') if kind == 'common' else ('補助実行例' if language == 'ja' else 'Supplementary execution example')


def formula_batches(data, root):
    formulas = {}
    for problem in data['problems']:
        for entry in problem['equations'] + problem['formulations']:
            values = entry.get('formula', entry.get('latex', []))
            if values:
                key = tuple(values)
                formulas.setdefault(key, 'problem-formula-'+str(len(formulas)))
    if not formulas:
        return {}
    records = [{'id': ident, 'formula': list(values)} for values, ident in formulas.items()]
    result = subprocess.run(['node', 'scripts/render-atlas-math.cjs'], cwd=root,
                            input=json.dumps(records, ensure_ascii=False), text=True, capture_output=True, check=True)
    rendered = json.loads(result.stdout)['rendered']
    return {values: rendered[ident] for values, ident in formulas.items()}


def math_html(values, rendered):
    return ''.join('<div class="problem-math">'+value+'</div>' for value in rendered.get(tuple(values), []))


def result_links(execution, language):
    ja = language == 'ja'
    rows = []
    for reference in execution['reference_data']:
        rows.append('<li>'+link(reference['url'], localized(reference['description'], language))+'</li>')
    for index, url in enumerate(execution['results'], 1):
        suffix = Path(urlsplit(url).path).suffix.lstrip('.').upper()
        title = ('保存結果' if ja else 'Saved result')+(' '+str(index) if len(execution['results']) > 1 else '')+(' / '+suffix if suffix else '')
        rows.append('<li>'+link(url, title)+'</li>')
    return '<ul class="problem-reference-links">'+''.join(rows)+'</ul>' if rows else ''


def equations_section(problem, language, rendered):
    ja = language == 'ja'
    body = paragraph(problem['equation_note'], language)
    for equation in problem['equations']:
        body += '<article class="problem-entry" data-equation-id="'+escape(equation['id'], quote=True)+'"><h3>'+link(equation['url'][language], localized(equation['name'], language))+'</h3>'
        body += math_html(equation['formula'], rendered)+paragraph(equation['note'], language)+'</article>'
    if problem['formulations']:
        body += '<h3 class="problem-subheading">'+('実行例で使う式' if ja else 'Formulations used by execution examples')+'</h3>'
        for formulation in problem['formulations']:
            body += '<article class="problem-entry problem-formulation" data-formulation-id="'+escape(formulation['id'], quote=True)+'"><div class="problem-badges"><span class="problem-badge">'+kind_label(formulation['source'], language)+'</span><span class="problem-badge">'+FORMULATION_ROLES[formulation['role']][language]+'</span></div><h4>'+escape(localized(formulation['name'], language))+'</h4>'
            body += math_html(formulation['latex'], rendered)+paragraph(formulation['note'], language)+'</article>'
    return body


def references_section(problem, language):
    ja = language == 'ja'
    body = paragraph(problem['reference_note'], language)
    for reference in problem['references']:
        relation = reference['relation']
        if relation not in {'same-problem', 'related-model'}:
            raise ValueError('Unknown reference relation: '+str(relation))
        label = ({'same-problem': '同じ問題の参照', 'related-model': '関連モデルの参照'} if ja else
                 {'same-problem': 'Reference for the same problem', 'related-model': 'Related-model reference'})[relation]
        body += '<article class="problem-entry problem-reference" data-reference-id="'+escape(reference['id'], quote=True)+'" data-reference-relation="'+relation+'"><div class="problem-badges"><span class="problem-badge">'+escape(reference['kind_label'][language])+'</span><span class="problem-badge problem-relation">'+label+'</span></div>'
        body += '<h3>'+link(reference['url'][language], reference['title'][language])+'</h3><p class="problem-reference-formula" dir="ltr">'+escape(reference['formula'])+'</p>'
        body += paragraph(reference['assumptions'], language)+paragraph(reference['note'], language, 'problem-reference-note')+'</article>'
    if problem['executions']:
        body += '<h3 class="problem-subheading">'+('実行例の参照と結果' if ja else 'References and results of execution examples')+'</h3>'
        for execution in problem['executions']:
            body += '<article class="problem-entry problem-execution-reference" data-execution-reference="'+escape(execution['id'], quote=True)+'"><span class="problem-badge">'+kind_label(execution['kind'], language)+'</span><h4>'+escape(execution['name'][language])+'</h4>'
            body += paragraph(execution['reference_note'], language)+result_links(execution, language)
            body += link(execution['guide'][language], '参照・検証条件の詳細 →' if ja else 'Reference and validation details →', 'problem-text-link')+'</article>'
    return body


def methods_section(problem, language):
    ja = language == 'ja'
    body = paragraph(problem['method_note'], language)
    for role in ['execution', 'related']:
        entries = [method for method in problem['methods'] if method['role'] == role]
        if not entries:
            continue
        heading = ('この問題の実行例で使う手法' if role == 'execution' else '関連する手法の解説') if ja else ('Methods used by this problem’s execution examples' if role == 'execution' else 'Related method explanations')
        body += '<h3 class="problem-subheading">'+heading+'</h3><ul class="problem-methods">'
        for method in entries:
            body += '<li data-method-id="'+escape(method['id'], quote=True)+'" data-method-role="'+role+'" data-method-status="'+escape(method['status'], quote=True)+'"><h4>'+link(method['url'][language], method['name'][language])+'</h4>'
            body += '<p class="problem-meta">'+('手法台帳の状態：' if ja else 'Method-registry status: ')+escape(STATUS[method['status']][language])+'</p></li>'
        body += '</ul>'
    return body


def source_files(execution, language):
    ja = language == 'ja'
    if not execution['code_urls'] and not execution['test_urls']:
        return ''
    body = '<details class="problem-details"><summary>'+('配布版のソースとテスト' if ja else 'Package source and tests')+'</summary><p>'+('同じ配布版で共有するファイルを含みます。すべてがこの問題専用のコードや検査という意味ではありません。' if ja else 'These lists include files shared across the package; they are not all dedicated to this problem.')+'</p>'
    for key, title in [('code_urls', 'ソース' if ja else 'Source'), ('test_urls', '配布版のテスト' if ja else 'Package tests')]:
        if execution[key]:
            body += '<h5>'+title+'</h5><ul class="problem-source-list">'+''.join('<li>'+link(url, unquote(urlsplit(url).path))+'</li>' for url in execution[key])+'</ul>'
    return body+'</details>'


def code_section(problem, language):
    ja = language == 'ja'
    body = ''
    if not problem['executions']:
        body += '<div class="problem-empty"><p>'+('この問題の固定入力実行例は未登録です。保存結果と解説は次のリンクから確認できます。' if ja else 'No fixed-input execution example is registered for this problem. The saved visual and reading remain available below.')+'</p><p class="problem-actions">'+link(problem['image']['url'], '保存された図を見る' if ja else 'View the saved visual')+link(problem['reading'][language], '解説を読む' if ja else 'Read the explanation')+'</p></div>'
    for execution in problem['executions']:
        body += '<article class="problem-entry problem-execution" data-execution-id="'+escape(execution['id'], quote=True)+'" data-execution-kind="'+escape(execution['kind'], quote=True)+'"><span class="problem-badge">'+kind_label(execution['kind'], language)+'</span><h3>'+link(execution['guide'][language], execution['name'][language])+'</h3>'
        body += paragraph(execution['scope'], language)
        body += '<nav class="problem-actions" aria-label="'+('固定入力・コード・検証' if ja else 'Fixed input, code and verification')+'">'+link(execution['guide'][language], '実行・検証の案内' if ja else 'Execution and validation guide')
        if execution['input']:
            body += link(execution['input'], '固定入力 / JSON' if ja else 'Fixed input / JSON')
        body += link(execution['download'], 'コード / ZIP' if ja else 'Code / ZIP')+link(execution['verification'], '検証記録' if ja else 'Verification receipt')
        if execution['manifest']:
            body += link(execution['manifest'], '配布ファイルとハッシュ' if ja else 'File manifest and hashes')
        body += '</nav><details class="problem-details"><summary>'+('条件・実行コマンド・確認範囲' if ja else 'Conditions, commands and validation scope')+'</summary><h4>'+('前提条件' if ja else 'Assumptions')+'</h4>'+paragraph(execution['assumptions'], language)
        if execution['commands']:
            body += '<p>'+('ZIPを展開し、実行の案内に示す作業フォルダで使うコマンドです。配布版の複数例をまとめて実行する場合があります。' if ja else 'Use these commands in the working directory specified by the execution guide after extracting the ZIP. A command may execute several cases in the package.')+'</p><pre><code>'+escape('\n'.join(execution['commands']))+'</code></pre>'
        body += '<h4>'+('検証の限界' if ja else 'Validation limits')+'</h4>'+paragraph(execution['limits'], language)+'</details>'
        body += source_files(execution, language)+'</article>'
    if problem['code_checks']:
        body += '<h3 class="problem-subheading">'+('関連する既存のソース・検査' if ja else 'Existing related source and checks')+'</h3><p>'+('次は保存結果の根拠を確認するためのソースや検査です。登録済みの固定入力実行例とは分けて示しています。' if ja else 'These sources and checks document existing evidence, separately from registered fixed-input execution examples.')+'</p>'
        for check in problem['code_checks']:
            body += '<article class="problem-entry problem-code-check"><h4>'+link(check['url'], check['path'])+'</h4>'
            if check['symbol']:
                body += '<p><code>'+escape(check['symbol'])+'</code></p>'
            if check.get('note'):
                body += paragraph(check['note'], language, 'problem-reference-note')
            if check['download']:
                body += '<p class="problem-actions">'+link(check['download'], '対応する配布版 / ZIP' if ja else 'Corresponding code edition / ZIP')+'</p>'
            if check['commands']:
                body += '<details class="problem-details"><summary>'+('確認用コマンド' if ja else 'Check commands')+'</summary>'
                if check['run_from']:
                    body += '<p>'+('作業フォルダ：' if ja else 'Working directory: ')+'<code>'+escape(check['run_from'])+'</code></p>'
                body += '<pre><code>'+escape('\n'.join(check['commands']))+'</code></pre></details>'
            body += '</article>'
    return body


def section(problem, language, rendered):
    ja = language == 'ja'
    image = problem['image']
    body = '<section data-site-language="'+language+'" lang="'+language+'" class="problem-edition">'
    body += '<nav class="problem-breadcrumb" aria-label="'+('現在位置' if ja else 'Breadcrumb')+'">'+link(BASE+'?lang='+language, 'アトラス' if ja else 'Atlas')+'<span aria-hidden="true"> / </span>'+link(BASE+'gallery/?lang='+language, 'テスト問題を選ぶ' if ja else 'Choose a test problem')+'</nav>'
    body += '<header class="problem-heading"><p class="problem-eyebrow">NUMERICAL METHODS ATLAS · PROBLEM</p><h1>'+escape(problem['name'][language])+'</h1><p>'+('この問題の式、参照の条件、計算法、公開済みのコードをたどります。' if ja else 'Explore this problem’s equations, reference conditions, methods and published code.')+'</p></header>'
    body += '<nav class="problem-jump" aria-label="'+('この問題から探す' if ja else 'Explore this problem')+'">'+''.join(link('#'+key+'-'+language, labels[language]) for key, labels in SECTION_LABELS.items())+'</nav>'
    body += '<figure class="problem-hero"><a href="'+escape(image['url'], quote=True)+'" aria-label="'+('保存された画像を拡大' if ja else 'Open the full-size saved image')+'"><img src="'+escape(image['url'], quote=True)+'" width="'+str(image['width'])+'" height="'+str(image['height'])+'" alt="'+escape(image['caption'][language], quote=True)+'" decoding="async"></a><figcaption><span class="problem-meta">'+escape(localized(SOURCE_LABELS.get(image['source_kind'], {}), language))+'</span> '+escape(image['caption'][language])+'</figcaption></figure>'
    body += '<nav class="problem-actions problem-reading" aria-label="'+('解説と条件' if ja else 'Reading and conditions')+'">'+link(problem['reading'][language], '問題の解説を読む' if ja else 'Read the problem explanation')+link(problem['conditions'][language], '図と問題の条件・根拠' if ja else 'Image and problem conditions / evidence')+'</nav>'
    renderers = {'equations': lambda: equations_section(problem, language, rendered), 'references': lambda: references_section(problem, language), 'methods': lambda: methods_section(problem, language), 'code': lambda: code_section(problem, language)}
    for key, labels in SECTION_LABELS.items():
        body += '<section class="problem-section" data-problem-section="'+key+'" aria-labelledby="'+key+'-'+language+'"><h2 id="'+key+'-'+language+'">'+labels[language]+'</h2>'+renderers[key]()+'</section>'
    body += '<footer class="problem-footer">'+link(BASE+'gallery/?lang='+language, '別のテスト問題を探す' if ja else 'Choose another test problem')+link('index.json', 'JSON')+link('index.md', 'Markdown')+link('/using/?lang='+language, '引用と利用条件' if ja else 'Citation and reuse')+'</footer></section>'
    return body


def md_link(url, label):
    return '['+str(label).replace('[', '\\[').replace(']', '\\]')+']('+url+')'


def markdown(problem):
    out = ['# '+problem['name']['ja']+' / '+problem['name']['en'], '', problem['url'], '']
    for language in LANGUAGES:
        ja = language == 'ja'
        out += ['## '+('日本語' if ja else 'English'), '', md_link(problem['image']['url'], problem['image']['caption'][language]), '', md_link(problem['reading'][language], '解説' if ja else 'Reading')+' · '+md_link(problem['conditions'][language], '条件・根拠' if ja else 'Conditions and evidence'), '']
        out += ['### '+SECTION_LABELS['equations'][language], '', problem['equation_note'][language], '']
        for equation in problem['equations']:
            out += ['#### '+md_link(equation['url'][language], localized(equation['name'], language)), '']
            for tex in equation['formula']:
                out += ['$$', tex, '$$', '']
            out += [equation['note'][language], '']
        for formulation in problem['formulations']:
            out += ['#### '+localized(formulation['name'], language), '', kind_label(formulation['source'], language)+' · '+FORMULATION_ROLES[formulation['role']][language], '']
            for tex in formulation['latex']:
                out += ['$$', tex, '$$', '']
            out += [formulation['note'][language], '']
        out += ['### '+SECTION_LABELS['references'][language], '', problem['reference_note'][language], '']
        for reference in problem['references']:
            label = ('同じ問題の参照' if reference['relation'] == 'same-problem' else '関連モデルの参照') if ja else ('Reference for the same problem' if reference['relation'] == 'same-problem' else 'Related-model reference')
            out += ['#### '+md_link(reference['url'][language], reference['title'][language]), '', reference['kind_label'][language]+' · '+label, '', reference['formula'], '', reference['assumptions'][language], '', reference['note'][language], '']
        for execution in problem['executions']:
            out += ['#### '+execution['name'][language], '', execution['reference_note'][language], '']
            out += ['- '+md_link(value['url'], value['description'][language]) for value in execution['reference_data']]
            out += ['- '+md_link(url, '保存結果' if ja else 'Saved result') for url in execution['results']]
            out += ['', md_link(execution['guide'][language], '参照・検証条件の詳細' if ja else 'Reference and validation details'), '']
        out += ['### '+SECTION_LABELS['methods'][language], '', problem['method_note'][language], '']
        for method in problem['methods']:
            role = ('この問題の実行例で使用' if method['role'] == 'execution' else '関連する解説') if ja else ('Used by this problem’s execution examples' if method['role'] == 'execution' else 'Related explanation')
            out += ['- '+md_link(method['url'][language], method['name'][language])+' — '+role+'; '+('手法台帳の状態：' if ja else 'Method-registry status: ')+STATUS[method['status']][language]]
        out += ['', '### '+SECTION_LABELS['code'][language], '']
        if not problem['executions']:
            out += ['この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。' if ja else 'No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.', '']
        for execution in problem['executions']:
            out += ['#### '+md_link(execution['guide'][language], execution['name'][language]), '', kind_label(execution['kind'], language), '', execution['scope'][language], '', execution['assumptions'][language], '', md_link(execution['download'], 'コード / ZIP' if ja else 'Code / ZIP')+' · '+md_link(execution['verification'], '検証記録' if ja else 'Verification receipt'), '']
            if execution['input']:
                out += [md_link(execution['input'], '固定入力' if ja else 'Fixed input'), '']
            if execution['manifest']:
                out += [md_link(execution['manifest'], '配布ファイルとハッシュ' if ja else 'File manifest and hashes'), '']
            if execution['commands']:
                out += ['ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。' if ja else 'After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.', '', '```sh', *execution['commands'], '```', '']
            out += [execution['limits'][language], '']
            if execution['code_urls'] or execution['test_urls']:
                out += ['同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。' if ja else 'These source and test lists include files shared across the package; they are not all dedicated to this problem.', '']
                out += ['- '+md_link(url, unquote(urlsplit(url).path)) for url in execution['code_urls']+execution['test_urls']]
                out += ['']
        for check in problem['code_checks']:
            out += ['#### '+md_link(check['url'], check['path']), '', '関連する既存のソース・検査。固定入力実行例とは別です。' if ja else 'Existing related source/check, separate from a registered fixed-input execution example.', '']
            if check['symbol']:
                out += ['`'+check['symbol']+'`', '']
            if check.get('note'):
                out += [localized(check['note'], language), '']
            if check['download']:
                out += [md_link(check['download'], '対応する配布版 / ZIP' if ja else 'Corresponding code edition / ZIP'), '']
            if check['commands']:
                if check['run_from']:
                    out += [('作業フォルダ：' if ja else 'Working directory: ')+check['run_from'], '']
                out += ['```sh', *check['commands'], '```', '']
    return '\n'.join(out).rstrip()+'\n'


def build(root=ROOT):
    from atlas_problem_links import load_problem_links
    root = Path(root)
    data = load_problem_links(root=root)
    rendered = formula_batches(data, root)
    destination = root/'numerical-methods-atlas/problems'
    destination.mkdir(parents=True, exist_ok=True)
    css_hash = hashlib.sha256((root/'styles/atlas-problems.css').read_bytes()).hexdigest()[:12]
    for problem in data['problems']:
        if not re.fullmatch(r'[a-z0-9][a-z0-9.-]*', problem['id']):
            raise ValueError('Unsafe problem identity: '+str(problem['id']))
        titles = {language: problem['name'][language]+(' | 数値計算法アトラス' if language == 'ja' else ' | Numerical Methods Atlas') for language in LANGUAGES}
        head = '<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        head += '<title data-page-title-ja="'+escape(titles['ja'], quote=True)+'" data-page-title-en="'+escape(titles['en'], quote=True)+'">'+escape(titles['ja'])+'</title>'
        head += '<meta name="description" content="'+escape(problem['name']['ja']+'：方程式、参照解の条件、計算法、公開コードと検証記録。', quote=True)+'"><link rel="canonical" href="'+escape(problem['url'], quote=True)+'">'
        head += '<link rel="stylesheet" href="/numerical-methods-atlas/vendor/katex.min.css"><link rel="stylesheet" href="/styles/atlas-problems.css?v='+css_hash+'"></head>'
        document = head+'<body class="profile-page atlas-problem" data-site-language-anchors="suffix"><main id="main" tabindex="-1" class="problem-hub">'+''.join(section(problem, language, rendered) for language in LANGUAGES)+'</main></body></html>\n'
        directory = destination/problem['id']
        directory.mkdir(parents=True, exist_ok=True)
        (directory/'index.html').write_text(document)
        (directory/'index.json').write_text(json.dumps(problem, ensure_ascii=False, indent=2)+'\n')
        (directory/'index.md').write_text(markdown(problem))
    (destination/'index.json').write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    print('Built problem hubs:', len(data['problems']), 'bilingual pages; existing figures, references and execution records retained.')
    return data


if __name__ == '__main__':
    build()
