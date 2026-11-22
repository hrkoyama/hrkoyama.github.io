#!/usr/bin/env python3
"""Build the bilingual human guide from the common execution-example catalog.

Run after build-atlas-resources.py and the execution registry publisher. This
replaces only the existing code-and-data/index.html route; no scientific code is
executed and no published code edition is modified.
"""
from pathlib import Path
import hashlib
import html
import json
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
ROUTE = '/numerical-methods-atlas/code-and-data/'
ORIGIN = 'https://hrkoyama.github.io'
CATALOG = 'catalog/atlas-execution-examples.json'


def esc(value):
    return html.escape(str(value))


def link(url, label):
    assert url.startswith(('https://', '/', '#')) or url == 'examples.json', url
    return '<a href="' + esc(url) + '">' + esc(label) + '</a>'


def paragraph(value):
    return '<p>' + esc(value) + '</p>'


def localized(value, lang):
    return value[lang] if isinstance(value, dict) else value


def bullet(values):
    return '<ul>' + ''.join('<li>' + esc(x) + '</li>' for x in values) + '</ul>'


def text(value):
    return json.dumps(value, ensure_ascii=False) if not isinstance(value, str) else value


def check_condition(check):
    comparison = check['comparison']
    expected = text(check.get('expected'))
    tolerance = text(check.get('tolerance'))
    if comparison == 'abs_difference':
        value = '|value − ' + expected + '| ≤ ' + tolerance
    elif comparison == 'minimum':
        value = 'value ≥ ' + tolerance
    elif comparison in ['maximum', 'absolute_maximum']:
        value = ('|value| ≤ ' if comparison == 'absolute_maximum' else 'value ≤ ') + text(check.get('tolerance', check.get('expected')))
    elif comparison == 'equals':
        value = 'value = ' + expected
    else:
        assert comparison == 'all_true', comparison
        value = 'all values = true'
    return value + (' ' + check['units'] if check.get('units') else '')


def check_table(checks, lang, label):
    ja = lang == 'ja'
    head = ['確認する量', '参照値・許容誤差', '結果JSON内の場所'] if ja else ['Quantity', 'Reference / acceptance', 'Location in result JSON']
    body = '<div class="execution-table" role="region" tabindex="0" aria-label="' + esc(label) + '"><table><thead><tr>'
    body += ''.join('<th scope="col">' + esc(h) + '</th>' for h in head) + '</tr></thead><tbody>'
    for c in checks:
        selector = c.get('pointer', '/')
        if c.get('where'):
            selector += ' · where ' + text(c['where'])
        if c.get('field'):
            selector += ' · field ' + c['field']
        body += '<tr><td>' + esc(localized(c['description'], lang)) + '</td><td><code>' + esc(check_condition(c)) + '</code></td><td><code>' + esc(selector) + '</code></td></tr>'
    return body + '</tbody></table></div>'


def release_information(examples, root):
    releases = {}
    for x in examples:
        release = x['release']
        key = (release['family'], release['version'])
        if key in releases:
            assert releases[key]['release'] == release
            continue
        path = root / urlparse(release['verification']).path.lstrip('/')
        v = json.loads(path.read_text())
        assert v['errors'] == v['failures'] == 0
        releases[key] = {'release': release, 'verification': v}
    return releases


def validate_receipt(receipt, data, root):
    """A receipt may describe a failed run, but must describe this exact recipe."""
    registry_file = root / ROUTE.lstrip('/') / 'examples.json'
    registry_bytes = registry_file.read_bytes()
    registry = json.loads(registry_bytes)
    assert registry['examples'] == data['examples'], 'Rebuild the public execution registry before the guide'
    assert receipt['registry_url'] == ORIGIN + ROUTE + 'examples.json'
    assert hashlib.sha256(registry_bytes).hexdigest() == receipt['registry_sha256'], 'Execution receipt belongs to a different registry; rerun the recipes'
    records = receipt['examples']
    assert isinstance(records, list)
    assert len(records) == len(data['examples'])
    assert {x['id'] for x in records} == {x['id'] for x in data['examples']}
    by_id = {x['id']: x for x in records}
    for case in data['examples']:
        record = by_id[case['id']]
        execution, validation = record['execution'], record['validation']
        assert execution['group'] == case['execution_group']
        assert set(execution['shared_runner_cases']) == set(case['shared_runner_cases'])
        assert execution['command'] == case['commands']['run']
        assert execution['completed'] == (execution['exit_code'] == 0)
        if validation['passed']:
            assert validation['checks'] and all(x['passed'] is True for x in validation['checks'])
            assert all(x['passed'] is True for x in validation.get('expected_failures', []))
        assert record['passed'] == (execution['completed'] and validation['passed'])
        for shared in case['shared_runner_cases']:
            assert by_id[shared]['execution'] == execution, 'A shared run must have one consistent execution record'
    assert receipt['passed'] == all(x['passed'] for x in records)


def render_receipt(receipt_url, receipt, examples, lang):
    ja = lang == 'ja'
    body = '<section class="execution-receipt"><h2>' + ('公開ファイルからの再実行記録' if ja else 'Re-execution from the public files') + '</h2>'
    if receipt is None:
        return body + paragraph('このページの生成時点では、今回追加する再実行記録はまだ保存されていません。配布版を別フォルダへ展開した既存の検証記録は、各ZIPの案内から確認できます。追加記録の未取得は、既存の検証が失敗したという意味ではありません。' if ja else 'The additional re-execution receipt has not been saved when this page is built. Existing independent-extraction checks remain available with each code edition. An unavailable additional receipt does not mean that those checks failed.') + '</section>'
    records = receipt.get('examples', [])
    if isinstance(records, dict):
        records = [{'id': ident, **value} for ident, value in records.items()]
    records = {x['id']: x for x in records}
    body += '<p>' + link(receipt_url, '入力・環境・実行・判定の記録 / JSON' if ja else 'Inputs, environment, execution and validation / JSON') + '</p>'
    body += paragraph('公開のZIPと入力を取得し、配布物のハッシュ照合、実行終了、出力の数値判定を分けて記録しています。同じ原子計算runnerを共有する水素型原子とHeは、1回の実行結果をそれぞれの条件で確認します。' if ja else 'The receipt separates public download and hash checks, process completion, and numerical output validation. Hydrogenic and helium cases share one atomic runner execution and have separate validation conditions.')
    body += '<ul class="execution-receipt-list">'
    for x in examples:
        record = records.get(x['id'])
        if record is None:
            state = '今回の記録に該当例なし' if ja else 'This example has no entry in the additional receipt'
        else:
            execution, validation = record.get('execution', {}), record.get('validation', {})
            completed = execution.get('completed') is True and execution.get('exit_code') == 0
            checked = validation.get('passed') is True
            state = ('実行終了を確認' if completed else '実行終了を要確認') + ' · ' + ('出力条件を確認' if checked else '出力条件を要確認') if ja else ('Process completed' if completed else 'Process completion requires review') + ' · ' + ('Output conditions passed' if checked else 'Output conditions require review')
        seconds = record.get('execution', {}).get('duration_seconds') if record is not None else None
        timing = f' · {seconds:.2f} s' if isinstance(seconds, (int, float)) else ''
        body += '<li><strong>' + esc(x['name'][lang]) + '</strong> — ' + esc(state + timing) + '</li>'
    body += '</ul>'
    body += '<details><summary>' + ('実行環境と記録日' if ja else 'Execution environment and receipt date') + '</summary><pre tabindex="0"><code>'
    body += esc(json.dumps({'verified_on': receipt.get('verified_on'), 'environment': receipt.get('environment')}, ensure_ascii=False, indent=2)) + '</code></pre></details></section>'
    return body


def reference_values(example, result, lang):
    ja = lang == 'ja'
    if example['id'] == 'barnes-hut':
        rows = [('relative_rms_force_error', result['relative_rms_force_error']), ('fully_opened_max_absolute_error', result['fully_opened_max_absolute_error'])]
    elif example['id'] == 'hydrogenic-atoms':
        candidates = [x for x in result['hydrogenic']['refinement'] if x['Z'] == 1 and x['n'] == 1 and x['l'] == 0]
        row = min(candidates, key=lambda x: x['dr'])
        rows = [('H 1s / E analytic (hartree)', row['exact_energy']), ('H 1s / E finite grid (hartree)', row['energy']), ('H 1s / grid step (bohr)', row['dr'])]
    elif example['id'] == 'helium-ground-state':
        rows = []
        for x in result['helium']['independent_comparison']:
            rows.extend([(x['model'] + ' / E finite grid (hartree)', x['finest_energy']), (x['model'] + ' / E independent reference (hartree)', x['reference_energy'])])
    else:
        rows = [(name, value) for name, value in result['metrics'].items() if type(value) in [int,float]][:8]
    body = '<details><summary>' + ('同梱された参照出力の代表値' if ja else 'Selected values from the packaged reference output') + '</summary>'
    body += paragraph('固定入力の参照出力から表示しています。有限格子の値と解析解・独立参照を区別し、再実行の判定には下の許容誤差表を使います。' if ja else 'Read from the fixed-input reference output. Distinguish finite-grid values from analytic or independently computed references; use the tolerance table below to validate a rerun.')
    body += '<dl>' + ''.join('<dt>' + esc(k) + '</dt><dd><code>' + esc(f'{v:.12g}') + '</code></dd>' for k, v in rows) + '</dl></details>'
    return body


def render_example(x, result, lang, heading_level=2):
    """One verified record, shared by the complete guide and stable example pages."""
    assert lang in ['ja','en'] and heading_level in [1,2]
    ja = lang == 'ja'
    body = ''
    release = x['release']
    body += '<section class="execution-example" id="' + x['id'] + '-' + lang + '" data-execution-example="' + x['id'] + '"><h'+str(heading_level)+'>' + esc(x['name'][lang]) + '</h'+str(heading_level)+'>'
    body += paragraph(x['scope'][lang]) + '<p>' + link(x['reading'][lang], '式・図・誤差の解説' if ja else 'Equations, figures and error analysis') + ' · ' + link(release['download'], '対応するコードZIP' if ja else 'Code ZIP for this example') + '</p>'
    body += '<dl>'
    for key, jlabel, elabel in [('assumptions', '前提', 'Assumptions'), ('units', '単位', 'Units'), ('boundaries', '境界・モデルの範囲', 'Boundaries and model scope')]:
        value = x[key][lang]
        body += '<dt>' + (jlabel if ja else elabel) + '</dt><dd>' + (bullet(value) if isinstance(value, list) else esc(value)) + '</dd>'
    body += '</dl>'
    body += '<h3>' + ('入力と実行' if ja else 'Inputs and execution') + '</h3><p>' + link(x['inputs']['url'], '固定入力 / ' + x['inputs']['path'] if ja else 'Fixed input / ' + x['inputs']['path']) + '</p>'
    body += '<p>' + ('実行する場所：' if ja else 'Run from: ') + '<code>' + esc(release['archive_directory']) + '</code>' + ('（ZIPを展開した中の配布版フォルダ）' if ja else ' (the edition directory inside the extracted ZIP)') + '</p>'
    body += '<pre tabindex="0"><code>' + esc(x['commands']['install'] + '\n' + x['commands']['run']) + '</code></pre>'
    if x.get('shared_runner_cases') and len(x['shared_runner_cases']) > 1:
        body += paragraph('このコマンドは水素型原子とHeをまとめて計算します。水素型は核電荷・量子数を指定した1電子問題、Heは2電子・球対称1s²のSCF問題です。HeのHFと交換のみLDAは、電子相関を含む厳密なHeとは異なります。' if ja else 'This command computes both hydrogenic atoms and helium. Hydrogenic states are one-electron problems specified by charge and quantum numbers; helium is a two-electron spherical 1s² SCF problem. HF and exchange-only LDA are not exact correlated helium.')
    body += '<details><summary>' + ('テストと依存関係のファイル' if ja else 'Tests and dependency files') + '</summary><pre tabindex="0"><code>' + esc(x['commands']['tests']) + '</code></pre><ul>'
    for kind, url in x['dependencies'].items():
        if url:
            body += '<li>' + link(url, kind + ' / ' + Path(urlparse(url).path).name) + '</li>'
    body += '</ul></details><details class="execution-validation"><summary>' + ('出力・検証条件・引用を確認する' if ja else 'Inspect outputs, acceptance and citation') + '</summary><h3>' + ('できるファイルと参照出力' if ja else 'Generated files and reference outputs') + '</h3><ul class="execution-output-list">'
    for out in x['outputs']:
        body += '<li><code>' + esc(out['generated_path']) + '</code> (' + esc(out['format'].upper()) + ') · ' + link(out['url'], '配布版の参照出力' if ja else 'Packaged reference output') + '</li>'
    body += '</ul>'
    if x.get('reference_notes'):body += '<h3>'+('参照の種類と比較方法' if ja else 'Reference type and comparison')+'</h3>'+paragraph(x['reference_notes'][lang])
    body += reference_values(x, result, lang) + '<h3>' + ('期待する値と許容誤差' if ja else 'Expected values and tolerances') + '</h3>'
    body += paragraph('表はこの例で採用する数値検査の条件です。参照値との一致だけで、全ての条件や原論文の全結果を再現したという意味にはなりません。横長の表は左右にスクロールできます。' if ja else 'These are numerical acceptance conditions for this example. Agreement does not establish every condition or reproduce all results of the original papers. Wide tables scroll horizontally.')
    body += check_table(x['checks'], lang, x['name'][lang] + ('の数値検査' if ja else ' numerical checks'))
    if x.get('expected_failures'):
        body += '<h3>' + ('意図した失敗・未収束の判定' if ja else 'Expected failures and nonconvergence') + '</h3>'
        body += check_table(x['expected_failures'], lang, 'Failure / ' + x['name'][lang])
    if x.get('failure_scope'):
        body += '<h3>'+('失敗・未収束と確認の限界' if ja else 'Failure, nonconvergence and verification limits')+'</h3>'+paragraph(x['failure_scope'][lang])
    body += '<h3>' + ('引用・出典と利用条件' if ja else 'Citation, sources and terms') + '</h3>'
    c = x['citation']
    body += '<blockquote class="execution-citation">' + esc(', '.join([localized(c['creator'], lang), localized(c['title'], lang), 'version ' + c['version']])) + '. ' + link(c['url'], c['url']) + '</blockquote>'
    body += paragraph('計算に使った設定・変更・ハッシュ・参照日を追記してください。手法を研究に使うときは、以下の原論文も確認し引用します。' if ja else 'Add the settings, changes, hashes and access date used in your calculation. When using the method in research, review and cite the original method publications too.')
    body += '<ul>' + ''.join('<li>' + link(r['url'], localized(r['description'], lang)) + '</li>' for r in x['references']) + '</ul>'
    body += '<p>' + link(x['terms']['code_license'], '自作実装コード：MIT' if ja else 'Original implementation code: MIT') + ' · ' + link(x['terms']['content_and_data'], '本文・図・データの条件' if ja else 'Terms for text, figures and data') + '</p>' + paragraph(x['terms']['scope'][lang])
    body += '<details><summary>' + ('版とSHA-256を確認する' if ja else 'Check the edition and SHA-256 hashes') + '</summary><dl><dt>Edition</dt><dd>' + esc(release['family'] + ' / ' + release['version']) + '</dd><dt>ZIP SHA-256</dt><dd><code>' + esc(release['sha256']) + '</code></dd><dt>Input SHA-256</dt><dd><code>' + esc(x['inputs']['sha256']) + '</code></dd></dl><p>' + link(release['manifest'], 'ファイル目録 / Manifest') + ' · ' + link(release['verification'], '配布版の検証記録' if ja else 'Edition verification record') + '</p></details></details></section>'
    subheading = 'h'+str(heading_level+1)
    return body.replace('<h3>','<'+subheading+'>').replace('</h3>','</'+subheading+'>')


def render_language(data, releases, receipt, results, lang):
    ja = lang == 'ja'
    examples = data['examples']
    body = '<section data-site-language="' + lang + '" lang="' + lang + '"><p class="eyebrow">PUBLIC CODE · FIXED INPUTS · CHECKED OUTPUTS</p>'
    body += '<h1>' + ('コードを取得し、結果を確かめる' if ja else 'Get the code. Reproduce the result.') + '</h1>'
    body += '<p class="intro">' + (f'移流・衝撃波・Poisson・ODE・粒子・原子など、{len(examples)}の代表問題を固定入力から実行できます。条件を読み、JSON/CSVを生成し、解析解・数値参照・保存則などの基準で結果を確かめます。' if ja else f'Run {len(examples)} representative advection, shock, Poisson, ODE, particle and atomic problems from fixed inputs. Generate JSON/CSV and inspect analytic references, numerical references, conservation and other acceptance conditions.') + '</p>'
    body += '<nav class="resource-nav" aria-label="' + ('関連資料' if ja else 'Related resources') + '">' + ''.join(link(u, t) for u, t in [('/numerical-methods-atlas/?lang=' + lang, 'アトラス冒頭' if ja else 'Atlas home'), ('/numerical-methods-atlas/methods/?lang=' + lang, '手法の見取り図' if ja else 'Method map'), ('examples.json', '実行例の共通台帳 / JSON' if ja else 'Common execution registry / JSON'), ('#execution-steps-' + lang, '共通の実行手順' if ja else 'Common reproduction steps'), ('/numerical-methods-atlas/code-and-data/ci/?lang=' + lang, 'Linuxの継続検証' if ja else 'Linux verification CI')]) + '</nav>'
    body += '<h2>' + ('まず、確かめたい例を選ぶ' if ja else 'Choose the result you want to check') + '</h2><div class="execution-choices">'
    for x in examples:
        body += '<article><h3>' + link('#' + x['id'] + '-' + lang, x['name'][lang]) + '</h3>' + paragraph(x['scope'][lang]) + '<p class="execution-family">' + esc(x['release']['family'] + ' · ' + x['release']['version']) + '</p></article>'
    body += '</div>'
    body += '<p class="resource-summary">' + ('水素型原子とHeは同じ「quantum-atoms」ZIPと入力・runnerを共有します。1回の実行で両方の結果ができ、以下の2つの説明から別々に検証できます。Barnes–Hutは2026-11-21版、追加12問題は2026-11-22版を使います。各例のZIPと入力を組み合わせてください。' if ja else 'Hydrogenic atoms and helium share the quantum-atoms ZIP, input and runner. One run produces both sets of results, which are validated separately below. Barnes–Hut uses the 2026-11-21 atlas edition; the 12 added recipes use 2026-11-22. Use the ZIP and input specified for each example.') + '</p>'
    body += '<section id="execution-steps-' + lang + '"><h2>' + ('取得から引用までの共通手順' if ja else 'A common path from download to citation') + '</h2><ol class="execution-steps">'
    steps = [
        ('条件を読む', 'Read the conditions', '例ごとの前提、単位、境界、モデルの限界を確認します。', 'Check the assumptions, units, boundaries and model limits for your case.'),
        ('ZIPと入力を取得する', 'Download the ZIP and input', '対応するZIPを新しいフォルダへ展開します。入力リンクから固定条件を確認します。', 'Extract the corresponding ZIP into a new directory and inspect the fixed input at its link.'),
        ('依存関係を準備する', 'Prepare the dependencies', 'Python環境を用意し、その配布版のフォルダで例ごとのインストール手順を実行します。', 'Prepare a Python environment and run the installation command from that extracted edition directory.'),
        ('計算して出力を保存する', 'Run and save the output', '実行場所とコマンドを確認して実行します。公開された参照出力は上書きせず、別の出力先を使います。', 'Use the stated working directory and command. Write to a separate output directory so packaged reference results remain intact.'),
        ('値と失敗理由を確かめる', 'Check values and failure reasons', '表のJSON内の場所と許容誤差を確認します。テスト通過、出力生成、物理的な妥当性は別に判断します。', 'Compare the indicated JSON fields with the reference values and tolerances. Passing tests, producing files and physical adequacy are distinct checks.'),
        ('版と出典を残す', 'Keep the version and sources', '入力の変更、コード版、ハッシュ、参照した手法論文、ページURLと確認日を計算記録に残します。', 'Retain input changes, code version and hashes, original method papers, page URL and access date in your computation record.'),
    ]
    for jh, eh, jp, ep in steps:
        body += '<li><strong>' + esc(jh if ja else eh) + '</strong>' + paragraph(jp if ja else ep) + '</li>'
    body += '</ol><details><summary>' + ('Python環境を分けて準備する場合' if ja else 'Prepare an isolated Python environment') + '</summary>'
    body += paragraph('配布ZIPを展開したフォルダで操作します。Python 3.12で配布版を検証しています。pythonという名前が使えない場合は、環境に合うPythonコマンドで作成してください。' if ja else 'Work from the extracted ZIP directory. The editions were checked with Python 3.12. If python is not your Python command, use the appropriate command to create the environment.')
    body += '<pre tabindex="0"><code>python -m venv .venv\n# macOS / Linux\nsource .venv/bin/activate\n# Windows PowerShell\n.venv\\Scripts\\Activate.ps1</code></pre>'
    body += paragraph('有効化は自分のOSの1行を選びます。その後、下記の例にある依存関係と実行コマンドを使います。最初の依存ライブラリ取得にはネット接続が必要ですが、導入後の通常実行にChatGPT・Codex・推論APIキーは不要です。' if ja else 'Choose the activation line for your OS, then use the dependency and execution commands below. Initial dependency installation needs network access; normal runs after setup require no ChatGPT, Codex or inference API key.') + '</details></section>'

    for x in examples:
        body += render_example(x, results[x['id']], lang)

    body += '<section><h2>' + ('配布版と検査件数の意味' if ja else 'Code editions and what their check counts mean') + '</h2>'
    for (family, version), record in releases.items():
        release, v = record['release'], record['verification']
        label = '流体・重力・線形解法などの従来版' if family == 'numerical-methods-atlas' else '水素型原子・Heの原子計算版'
        if not ja:
            label = 'Original fluids, gravity and numerical-methods edition' if family == 'numerical-methods-atlas' else 'Hydrogenic / helium atomic edition'
        if family == 'numerical-methods-atlas' and version == '2026-11-22':
            label = '代表12問題の固定入力レシピ版' if ja else 'Fixed-input recipe edition for twelve representative problems'
        body += '<h3>' + esc(label) + '</h3><p>' + link(release['download'], family + ' · ' + release['version'] + ' / ZIP') + ' · ' + link(release['manifest'], 'Manifest / SHA-256') + ' · ' + link(release['verification'], 'Verification / JSON') + '</p>'
        body += paragraph((f'配布ZIPを別フォルダへ展開して、{v["passed"]}検査が通過。適用対象外によるスキップは{v["skipped"]}件、失敗・エラーは0件です。' if ja else f'The distributed ZIP was independently extracted: {v["passed"]} checks passed, {v["skipped"]} inapplicable checks skipped, and no failures or errors.'))
        if family == 'numerical-methods-atlas':
            base = release['manifest'].rsplit('/', 1)[0] + '/'
            body += '<p>' + link(base + 'LICENSE', 'MIT License') + ' · ' + link(base + 'LICENSING.md', '適用範囲 / Licensing scope') + '</p>'
    body += paragraph(f'上記は各配布版の自動検査数です。{len(examples)}の代表問題やアトラス全体の67問題とは別に数え、版をまたぐ検査数は合算しません。原子版の23検査と従来版の411検査も、それぞれの保存記録です。Ewald・PME・SPMEは未実装で、原子例も一般の分子・周期系DFT計算ではありません。' if ja else f'These are automated test counts for each edition, distinct from the {len(examples)} representative problems and the atlas-wide 67 problems. Do not add repeated tests across editions. The atomic 23 and original 411 checks retain their separate records. Ewald/PME/SPME remain unimplemented; the atomic examples are not general molecular or periodic DFT calculations.') + '</section>'
    body += render_receipt(data['verification_receipt'], receipt, examples, lang)
    body += '<section><h2>' + ('公開資料だけで再現し、出典に戻る' if ja else 'Reproduce from public material and return to the source') + '</h2>'
    body += paragraph('自作の実装コードのMITと、本文・図・データ・第三者資料の条件は別です。この案内は新しい再配布・改変公開の権限を追加するものではありません。' if ja else 'MIT for original implementation code is separate from the terms for prose, figures, data and third-party material. This guide does not add redistribution or public-adaptation permissions.')
    body += '<p>' + link('/using/?lang=' + lang, '資料の使い方と引用' if ja else 'Use and citation') + ' · ' + link('/rights/?lang=' + lang, '利用条件とAI方針' if ja else 'Rights and AI policy') + ' · ' + link('examples.json', '実行例台帳 / JSON' if ja else 'Execution registry / JSON') + '</p></section></section>'
    return body


def build(root=ROOT):
    data = json.loads((root / CATALOG).read_text())
    examples = data['examples']
    assert len(examples) == len({x['id'] for x in examples}) and examples
    releases = release_information(examples, root)
    assert {family for family, version in releases} == {'numerical-methods-atlas', 'quantum-atoms', 'model-benchmarks', 'molecular-hf', 'periodic-dft', 'periodic-forces'}
    receipt_url = data['verification_receipt']
    receipt_path = root / urlparse(receipt_url).path.lstrip('/')
    public_receipt = receipt_path.with_name(receipt_path.stem+'-public.json')
    if public_receipt.is_file():
        receipt_path = public_receipt
        receipt_url = receipt_url.removesuffix('.json')+'-public.json'
    receipt = json.loads(receipt_path.read_text()) if receipt_path.is_file() else None
    data = {**data, 'verification_receipt':receipt_url}
    if receipt is not None:
        validate_receipt(receipt, data, root)
    results = {}
    for x in examples:
        result = next(out for out in x['outputs'] if out['format'] == 'json')
        results[x['id']] = json.loads((root / urlparse(result['url']).path.lstrip('/')).read_text())
    sections = ''.join(render_language(data, releases, receipt, results, lang) for lang in ['ja', 'en'])
    document = '<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    document += '<title data-page-title-ja="コード・入力・検証 | 数値計算法アトラス" data-page-title-en="Code, inputs and validation | Numerical Methods Atlas">コード・入力・検証 | 数値計算法アトラス</title>'
    document += '<meta name="description" content="代表22問題の公開コード、固定入力、実行手順、JSON/CSV出力、参照値と許容誤差。Public code, fixed inputs, reproduction commands and numerical acceptance checks for 22 representative problems."><link rel="canonical" href="' + ORIGIN + ROUTE + '">'
    for name in ['atlas-resources', 'atlas-execution']:
        digest = hashlib.sha256((root / 'styles' / (name + '.css')).read_bytes()).hexdigest()[:12]
        document += '<link rel="stylesheet" href="/styles/' + name + '.css?v=' + digest + '">'
    document += '</head><body class="profile-page" data-site-language-anchors="suffix"><main id="main" class="profile-main atlas-resource-main atlas-execution-main">' + sections + '</main></body></html>\n'
    return document


if __name__ == '__main__':
    destination = ROOT / ROUTE.lstrip('/') / 'index.html'
    destination.write_text(build())
    print('Built bilingual acquisition and execution guide for the current scoped examples.')
