#!/usr/bin/env python3
"""Build bilingual periodic-DFT reading from prose and frozen measurements.

This build executes neither PySCF nor DFTK. A verified immutable release with
successful numerical evidence is required before any generated file is changed.
"""
from pathlib import Path
from html import escape as e
import hashlib
import json
import re
import struct
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / 'numerical-methods-atlas'
SOURCE = '/catalog/atlas-periodic-reading.json'
ORIGIN = 'https://hrkoyama.github.io'
CHAPTER = 'periodic-dft'
EXAMPLE = 'periodic-he-dft'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n')


def link(url, label):
    return '<a href="' + e(url, quote=True) + '">' + e(label) + '</a>'


def para(text):
    return '<p>' + e(text) + '</p>'


def heading(ident, title):
    return '<h2 id="' + e(ident, quote=True) + '">' + e(title) + '</h2>'


def route(lang):
    return '/numerical-methods-atlas/' + lang + '/read/' + CHAPTER + '/'


def number(value):
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, (int, float)):
        return format(value, '.12g')
    if isinstance(value, list):
        return ' × '.join(number(v) for v in value)
    return str(value)


def table(headers, rows, label):
    return '<div class="periodic-table" tabindex="0" role="region" aria-label="' + e(label) + '"><table><thead><tr>' + ''.join('<th scope="col">' + e(h) + '</th>' for h in headers) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join('<td>' + e(number(v)) + '</td>' for v in row) + '</tr>' for row in rows) + '</tbody></table></div>'


def mesh_schematic(lang):
    ja = lang == 'ja'
    label = 'Γ点のみと一様k点メッシュの2次元模式図。実際の計算は3次元。' if ja else 'Two-dimensional schematic of Γ-only and uniform k-point sampling. Actual calculations are three-dimensional.'
    circles = ''.join('<circle cx="' + str(x) + '" cy="' + str(y) + '" r="6" fill="' + ('#b34b29' if (x, y) == (510, 116) else '#245c4d') + '"/>' for x in [462, 510, 558] for y in [68, 116, 164])
    return '<figure><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 238" width="680" height="238" role="img" aria-label="' + e(label, quote=True) + '"><title>' + e(label) + '</title><rect width="680" height="238" fill="#f0f5f1"/><g fill="none" stroke="#66786e"><rect x="88" y="44" width="144" height="144"/><rect x="438" y="44" width="144" height="144"/><path d="M70 116h180M160 26v180M420 116h180M510 26v180"/></g><circle cx="160" cy="116" r="7" fill="#b34b29"/>' + circles + '<g font-family="sans-serif" font-size="15" fill="#173c30"><text x="174" y="109">Γ</text><text x="524" y="109">Γ</text><text x="92" y="218">' + ('Γ点のみ：1点近似' if ja else 'Γ only: one-point quadrature') + '</text><text x="414" y="218">' + ('一様メッシュ：各点に重み' if ja else 'Uniform mesh: weighted points') + '</text></g></svg><figcaption>' + e(label) + '</figcaption></figure>'


def measured(results, lang, base):
    ja = lang == 'ja'
    body = heading('measured-results', '実測結果：何を、どの幅で確かめたか' if ja else 'Measurements: what was checked, and to what tolerance')
    body += para('次の値は固定入力から得た保存済み結果です。ケース数は計算条件の数で、別々の物理テスト問題の数ではありません。各収束系列は同じ基準ケースを再利用します。公差との判定には丸める前のJSON値を用い、末尾の差を真の誤差の上限とは解釈しません。' if ja else 'These stored measurements come from fixed inputs. Case counts describe calculation settings, not distinct physical test problems. Convergence sequences reuse a common baseline. Acceptance uses unrounded JSON values; a final increment is not a bound on true error.')
    labels = {
        'max_reference_energy_error': ('DFTKとの差の最大値 / hartree・cell⁻¹', 'Maximum difference from DFTK / hartree per cell'),
        'max_tight_scf_commutator': ('厳しいSCF設定の最大交換子残差', 'Maximum commutator residual, tight SCF settings'),
        'max_scf_commutator': ('許容誤差走査を含む最大交換子残差', 'Maximum commutator residual, including tolerance sweeps'),
        'max_orbital_residual': ('許容誤差走査を含む最大軌道残差', 'Maximum orbital residual, including tolerance sweeps'),
        'max_electron_count_error': ('最大電子数誤差', 'Maximum electron-count error'),
        'max_orthogonality_error': ('最大軌道直交性誤差', 'Maximum orbital orthogonality error'),
        'max_energy_reconstruction_error': ('最終密度からの最大エネルギー再構成差 / hartree', 'Maximum energy reconstruction difference from final density / hartree'),
        'min_sampled_ks_gap': ('全ケースの標本点KSギャップ最小値 / hartree', 'Minimum sampled KS gap over all cases / hartree'),
        'max_overlap_condition': ('最大重なり行列条件数', 'Maximum overlap condition number'),
        'min_overlap_eigenvalue': ('最小重なり行列固有値', 'Minimum overlap eigenvalue'),
        'kpoint_last_change': ('最後のk点メッシュ間の|ΔE| / hartree・cell⁻¹', 'Final k-mesh |ΔE| / hartree per cell'),
        'basis_last_change': ('最後のGaussian基底間の|ΔE| / hartree・cell⁻¹', 'Final Gaussian-basis |ΔE| / hartree per cell'),
        'auxiliary_last_change': ('最後の補助FFT格子間の|ΔE| / hartree・cell⁻¹', 'Final auxiliary-grid |ΔE| / hartree per cell'),
        'scf_last_change': ('最後のSCF設定間の|ΔE| / hartree・cell⁻¹', 'Final SCF-setting |ΔE| / hartree per cell'),
    }
    metrics = results['metrics']
    assert set(metrics) == set(labels), 'Periodic DFT metric schema changed; update the reading explicitly'
    body += table(['測定量', '値'] if ja else ['Measured quantity', 'Value'], [(labels[k][0 if ja else 1], metrics[k]) for k in labels], '数値検査の要約' if ja else 'Numerical check summary')
    names = {'kpoint': ('k点メッシュ', 'k-point mesh'), 'basis': ('Gaussian軌道基底', 'Gaussian orbital basis'), 'auxiliary': ('補助FFT格子', 'Auxiliary FFT grid'), 'scf': ('SCF許容誤差', 'SCF tolerances')}
    body += heading('convergence-targets', '4つの収束軸を分けて読む' if ja else 'Reading four separate convergence axes')
    body += table(['変更した量', '最後の|ΔE| / hartree', '入力の目標 / hartree', '目標達成'] if ja else ['Changed quantity', 'Final |ΔE| / hartree', 'Input target / hartree', 'Target met'], [(names[k][0 if ja else 1], c['last_change'], c['target'], c['target_reached']) for k, c in results['convergence'].items()], '有限系列の停止目安' if ja else 'Stopping diagnostics for finite sequences')
    indexed = {r['id']: r for r in results['cases']}
    assert indexed and all(r['converged'] for r in indexed.values()), 'Unconverged calculations cannot be presented as successful evidence'
    for key, c in results['convergence'].items():
        rows = [indexed[i] for i in c['case_ids']]
        body += heading('results-' + key, names[key][0 if ja else 1] + ('の結果' if ja else ' results'))
        if key == 'scf':
            body += table(['ケース', 'ΔE公差', '勾配公差', 'E / hartree・cell⁻¹', '||R(SCF)||', '反復', '終了理由'] if ja else ['Case', 'Energy tolerance', 'Gradient tolerance', 'E / hartree per cell', '||R(SCF)||', 'Iterations', 'Termination'], [[r['id'], r['scf_options']['energy_tolerance'], r['scf_options']['gradient_tolerance'], r['energy_per_cell'], r['scf_commutator_norm'], r['iterations'], r['termination']] for r in rows], names[key][0 if ja else 1])
        else:
            body += table(['ケース', 'kメッシュ', '基底', '関数数', '補助FFT', 'E / hartree・cell⁻¹', 'KS gap / hartree', '||R(SCF)||'] if ja else ['Case', 'k mesh', 'Basis', 'Functions', 'Auxiliary FFT', 'E / hartree per cell', 'KS gap / hartree', '||R(SCF)||'], [[r['id'], r['kmesh'], r['basis'], r['ao_count'], r['fft_mesh'], r['energy_per_cell'], r['sampled_ks_gap'], r['scf_commutator_norm']] for r in rows], names[key][0 if ja else 1])
    body += heading('reference-results', '独立したDFTKとの全エネルギー比較' if ja else 'Total-energy comparison with independent DFTK')
    body += para('有限のGaussian軌道基底と平面波基底は異なるため、下の差は同じ有限行列の丸め誤差ではありません。モデルと定数規約をそろえ、公開した判定幅と両側の収束を合わせて評価します。' if ja else 'Finite Gaussian and plane-wave orbital spaces differ, so these differences are not rounding errors for the same finite matrix. The model and constant conventions are aligned, and the published acceptance width is assessed together with convergence on both sides.')
    body += table(['kメッシュ', 'PySCF / hartree・cell⁻¹', 'DFTK / hartree・cell⁻¹', '|差| / hartree', '判定幅 / hartree', '合格'] if ja else ['k mesh', 'PySCF / hartree per cell', 'DFTK / hartree per cell', '|Difference| / hartree', 'Acceptance width / hartree', 'Passed'], [[[r['k_n']] * 3, r['pyscf_energy_per_cell'], r['dftk_energy_per_cell'], r['absolute_difference'], r['acceptance'], r['passed']] for r in results['independent_comparison']['cases']], '独立エンジン比較' if ja else 'Independent-engine comparison')
    cutoff = results['independent_comparison']['cutoff_convergence']
    body += heading('reference-cutoff-results', 'DFTK側の平面波カットオフ収束' if ja else 'Plane-wave cutoff convergence on the DFTK side')
    body += para('カットオフの単位はhartreeです。初期の粗い設定が目標を満たさなければ、設定を追加して末尾の変化を再検査します。下の表は採用した固定版の全設定であり、途中の値を収束済みの参照とは扱いません。' if ja else 'Cutoffs are in hartree. If initial coarse settings miss the target, additional cutoffs are tested against the final increment. The table includes all settings in the fixed edition; intermediate values are not treated as converged references.')
    body += table(['kメッシュ', '軌道カットオフ / hartree', 'E / hartree・cell⁻¹', 'KS gap / hartree', '密度残差', 'SCF反復', '収束'] if ja else ['k mesh', 'Orbital cutoff / hartree', 'E / hartree per cell', 'KS gap / hartree', 'Density residual', 'SCF iterations', 'Converged'], [[[r['k_n']] * 3, r['ecut_hartree'], r['energy_per_cell'], r['sampled_ks_gap_hartree'], r['density_residual'], r['scf_iterations'], r['converged']] for r in cutoff['records']], '独立参照のカットオフ系列' if ja else 'Independent-reference cutoff sequence')
    body += table(['kメッシュ', '最後のカットオフ / hartree', '最後の|ΔE| / hartree・cell⁻¹', '目標 / hartree・cell⁻¹', '目標達成'] if ja else ['k mesh', 'Final cutoff / hartree', 'Final |ΔE| / hartree per cell', 'Target / hartree per cell', 'Target met'], [[[r['k_n']] * 3, r['to_ecut_hartree'], r['energy_change'], cutoff['target_hartree_per_cell'], r['target_reached']] for r in cutoff['last_changes']], '独立参照の末尾の変化' if ja else 'Final independent-reference increments')
    body += '<p>' + link(base + 'reference-dftk.json', 'DFTKのカットオフ収束と参照 / JSON' if ja else 'DFTK cutoff convergence and reference / JSON') + '</p>'
    assert cutoff['target_reached'] is True
    image = ROOT / (base + 'results/preview.png').lstrip('/')
    if image.is_file():
        png = image.read_bytes()
        assert png[:8] == b'\x89PNG\r\n\x1a\n'
        width, height = struct.unpack('>II', png[16:24])
        body += '<figure><img src="' + base + 'results/preview.png" width="' + str(width) + '" height="' + str(height) + '" loading="lazy" alt="' + ('周期DFTの固定入力によるk点・基底・補助格子・SCF収束の保存図' if ja else 'Stored periodic-DFT k-point, basis, auxiliary-grid and SCF convergence figure') + '"><figcaption>' + ('保存済み結果の可視化です。合否は入力・結果JSONの数値と条件で判定します。' if ja else 'A visualization of stored results. Acceptance uses the numerical values and criteria in the input/result JSON.') + '</figcaption></figure>'
    body += '<p>' + link(base + 'results/result.json', '全結果 / JSON' if ja else 'Full results / JSON') + ' · ' + link(base + 'results/solution.csv', '条件とエネルギー / CSV' if ja else 'Settings and energies / CSV') + ' · ' + link(base + 'results/scf.csv', 'SCF履歴 / CSV' if ja else 'SCF histories / CSV') + '</p>'
    return body


def build():
    data = read(ROOT / SOURCE.lstrip('/'))
    package = data['package']
    base = package['base']
    release = ROOT / base.lstrip('/')
    result_path = release / package['results']
    results = read(result_path)
    assert results['case'] == data['example_id'] == EXAMPLE
    assert results['passed'] is True and all(v is True for v in results['checks'].values())
    assert sha(release / package['input']) == results['input_sha256']
    assert sha(release / package['reference']) == results['reference_sha256']
    manifest = read(release / 'source-manifest.json')
    verification = read(release / 'verification.json')
    assert verification['failures'] == verification['errors'] == 0
    assert verification['passed'] > 0
    assert sha(release / package['archive']) == verification['archive_sha256']
    assert sha(release / 'source-manifest.json') == verification['source_manifest_sha256']
    for name, digest in manifest['files'].items():
        assert sha(release / name) == digest, name
    source_hash = sha(ROOT / SOURCE.lstrip('/'))
    sources = {SOURCE.lstrip('/'): source_hash, (base + package['results']).lstrip('/'): sha(result_path), (base + 'source-manifest.json').lstrip('/'): sha(release / 'source-manifest.json'), (base + 'verification.json').lstrip('/'): sha(release / 'verification.json')}
    methods = {m['id']: m for m in read(ROOT / 'catalog/atlas-methods.json')['methods']}
    assert all(i in methods for i in data['methods'])
    assert all(methods[i]['status'] == 'reading-only' and not methods[i].get('periodic_examples') for i in data['reading_only_methods'])
    rendered = json.loads(subprocess.check_output(['node', 'scripts/render-atlas-math.cjs'], cwd=ROOT, input=json.dumps([{'id': k, 'formula': [v]} for k, v in data['formulas'].items()]).encode()))['rendered']
    references = {r['id']: r for r in data['references']}
    documents = {lang: read(ATLAS / f'content.{lang}.json') for lang in ['ja', 'en']}
    translations = read(ATLAS / 'translation-status.json')
    for lang in ['ja', 'en']:
        ja = lang == 'ja'
        title = data['title'][lang]
        body = '<h1>' + e(title) + '</h1>' + para(data['intro'][lang])
        body += '<aside class="resource-summary">' + para(data['scope'][lang]) + '</aside>'
        example_url = '/numerical-methods-atlas/code-and-data/examples/' + EXAMPLE + '/?lang=' + lang
        body += '<nav class="resource-nav">' + link(example_url, '固定入力・コード・テスト・判定条件' if ja else 'Fixed input, code, tests and acceptance') + ' · ' + link(base + package['archive'], 'ZIP') + ' · ' + link(base + 'verification.json', '独立展開の検証 / JSON' if ja else 'Independent-extraction verification / JSON') + '</nav>'
        body += measured(results, lang, base)
        markdown = '# ' + title + '\n\n' + data['intro'][lang] + '\n\n' + data['scope'][lang] + '\n\n'
        for section in data['sections']:
            body += heading(section['id'], section['title'][lang]) + ''.join(para(p) for p in section['paragraphs'][lang])
            if section['id'] == 'kpoint-quadrature':
                body += mesh_schematic(lang)
            body += ''.join('<div class="math-block">' + rendered[f][0] + '</div>' for f in section['formulas'])
            body += '<p class="periodic-citations">' + ('関連出典：' if ja else 'Sources: ') + ', '.join(link('#source-' + i, references[i]['author'] + ' (' + str(references[i]['year']) + ')') for i in section['references']) + '</p>'
            markdown += '## ' + section['title'][lang] + '\n\n' + '\n\n'.join(section['paragraphs'][lang]) + '\n\n' + ''.join('$$\n' + data['formulas'][f] + '\n$$\n\n' for f in section['formulas'])
        body += heading('run-and-check', '取得して結果を確かめる' if ja else 'Download and verify the results')
        body += para('ZIP内の配布版フォルダで依存関係を導入し、同梱の固定入力を使います。出力先は新規または空のディレクトリにします。通常のrunnerは保存済みDFTK参照を照合します。Juliaによる参照の再生成は別工程で、参照用環境と手順を同梱しています。' if ja else 'Install dependencies in the extracted edition directory and use its fixed input. Choose a new or empty output directory. The ordinary runner compares with the saved DFTK reference. Regenerating that reference in Julia is a separate operation with its own packaged environment and instructions.')
        commands = 'python -m pip install -r requirements.txt\npython -m pytest -q\npython run.py --input inputs.json --output output'
        body += '<pre><code>' + commands + '</code></pre><p>' + link(base + package['input'], '固定入力 / JSON' if ja else 'Fixed input / JSON') + ' · ' + link(base + 'run.py', 'Runner') + ' · ' + link(base + package['reference'], 'DFTK独立参照 / JSON' if ja else 'Independent DFTK reference / JSON') + ' · ' + link(example_url, '版・受入条件・引用の共通手順' if ja else 'Edition, acceptance criteria and citation') + '</p>'
        body += heading('sources', '一次文献・関連資料と確認範囲' if ja else 'Primary publications, supporting sources and review scope')
        body += para('書誌、抄録、原文の一部、公式APIの確認を区別して示します。原論文全体の再現や全文監査を行ったという意味ではありません。論文の全文や第三者のソースコードはこの教材に転載しません。' if ja else 'Bibliographic, abstract, selected full-text and official API checks are distinguished below. They do not claim reproduction or audit of an entire paper. Full papers and third-party source code are not reprinted in this tutorial.') + '<ol>'
        for r in data['references']:
            body += '<li id="source-' + r['id'] + '">' + link(r['source'], r['author'] + ' (' + str(r['year']) + '). ' + r['title']) + '. ' + e(r['journal']) + para(r['review'][lang]) + '</li>'
        body += '</ol>'
        headings = [{'level': 2, 'id': i, 'title': re.sub('<[^>]+>', '', t)} for i, t in re.findall(r'<h2 id="([a-z0-9-]+)">(.*?)</h2>', body, re.S)]
        entry = {'title': title, 'html': body, 'headings': headings, 'locale': lang, 'source_url': SOURCE, 'updated_on': data['updated_on']}
        if ja:
            entry['translation_status'] = 'draft'
        documents[lang][CHAPTER] = entry
        directory = ROOT / route(lang).lstrip('/')
        directory.mkdir(parents=True, exist_ok=True)
        nav = '<nav class="resource-nav">' + link(f'/numerical-methods-atlas/{lang}/read/', '解説章の目次' if ja else 'Reading contents') + ' · ' + link(SOURCE, '編集用正本 / JSON' if ja else 'Editable source / JSON') + ' · ' + link(route(lang) + 'index.json', 'JSON') + ' · ' + link(route(lang) + 'index.md', 'Markdown') + '</nav>'
        toc = '<details class="periodic-toc"><summary>' + ('この章の目次' if ja else 'On this page') + '</summary><nav aria-label="' + ('この章の目次' if ja else 'On this page') + '">' + ''.join(link('#' + h['id'], h['title']) for h in headings) + '</nav></details>'
        style = '<style>.periodic-reading{max-width:1100px;margin:auto;padding:1.2rem;overflow-wrap:anywhere}.periodic-reading .prose{max-width:88ch;margin:auto}.periodic-reading .prose p{font-size:1rem;line-height:1.85}.periodic-reading .resource-nav,.periodic-reading>nav{display:flex;flex-wrap:wrap;gap:.5rem}.periodic-reading>nav a{padding:.3rem}.periodic-reading .math-block,.periodic-table{max-width:100%;overflow-x:auto}.periodic-table{margin:1rem 0}.periodic-table table{border-collapse:collapse;min-width:100%;font-size:.95rem}.periodic-table td,.periodic-table th{border-bottom:1px solid #becbc3;padding:.55rem;text-align:left}.periodic-table td:not(:first-child){font-variant-numeric:tabular-nums;white-space:nowrap}.periodic-reading img,.periodic-reading svg{width:100%;height:auto}.periodic-reading pre{white-space:pre;overflow:auto;padding:1rem;background:#eef3ef}.periodic-reading li{margin-bottom:1rem}.periodic-reading h2{scroll-margin-top:1rem}.periodic-toc{margin:1rem 0}.periodic-toc summary{padding:.5rem 0;cursor:pointer}.periodic-toc nav{display:flex;flex-wrap:wrap;gap:.5rem 1rem;padding:.6rem 0}.periodic-citations{font-size:.95rem}.periodic-reading .resource-summary{border-left:4px solid #386552;padding:.3rem 1rem;background:#eef3ef}</style>'
        document = '<!doctype html><html lang="' + lang + '"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + e(title) + ' | Numerical Methods Atlas</title><meta name="description" content="' + e(data['intro'][lang], quote=True) + '"><link rel="canonical" href="' + ORIGIN + route(lang) + '">' + ''.join('<link rel="alternate" hreflang="' + l + '" href="' + ORIGIN + route(l) + '">' for l in ['ja', 'en']) + '<link rel="stylesheet" href="/numerical-methods-atlas/vendor/katex.min.css"><link rel="stylesheet" href="/numerical-methods-atlas/style.css"><link rel="stylesheet" href="/styles/atlas-resources.css">' + style + '</head><body class="profile-page" data-content-language="' + lang + '"><main id="main" class="periodic-reading">' + nav + toc + '<article class="prose" lang="' + lang + '">' + body + '</article></main></body></html>\n'
        (directory / 'index.html').write_text(document)
        dump(directory / 'index.json', {**entry, 'url': ORIGIN + route(lang), 'methods': data['methods'], 'reading_only_methods': data['reading_only_methods'], 'execution_example': EXAMPLE, 'references': data['references'], 'source_sha256': sources, 'measurements': results['metrics']})
        markdown += '## ' + ('保存した実測値' if ja else 'Stored measurements') + '\n\n' + '\n'.join('- ' + k + ': ' + number(v) for k, v in results['metrics'].items()) + '\n\n' + ORIGIN + base + package['results'] + '\n\n'
        markdown += '## ' + ('実行' if ja else 'Execution') + '\n\n```sh\n' + commands + '\n```\n\n' + ORIGIN + example_url + '\n\n'
        markdown += '## ' + ('文献' if ja else 'Sources') + '\n\n' + '\n'.join('- ' + r['author'] + ' (' + str(r['year']) + '). ' + r['title'] + '. ' + r['source'] + ' — ' + r['review'][lang] for r in data['references']) + '\n'
        (directory / 'index.md').write_text(markdown)
        path = ATLAS / lang / 'read/index.html'
        text = re.sub(r'<!-- periodic-reading -->.*?<!-- /periodic-reading -->', '', path.read_text(), flags=re.S)
        block = '<!-- periodic-reading --><section class="page-width"><h2>' + ('周期DFTの実装と収束確認' if ja else 'Periodic DFT implementation and convergence checks') + '</h2><p>' + link(route(lang), title) + '</p></section><!-- /periodic-reading -->'
        path.write_text(text.replace('</main>', block + '</main>'))
        translations['chapters'][CHAPTER] = {'status': 'draft', 'source_url': SOURCE, 'source_sha256': source_hash, 'checked_on': data['updated_on']}
    for lang, docs in documents.items():
        dump(ATLAS / f'content.{lang}.json', docs)
        if lang == 'en':
            dump(ATLAS / 'content.json', docs)
    translations.update(total=len(documents['en']), translated=sum(k in documents['ja'] for k in documents['en']), reviewed=sum(r['status'] == 'reviewed' for r in translations['chapters'].values()))
    dump(ATLAS / 'translation-status.json', translations)
    path = ATLAS / 'home-search-index.json'
    index = read(path)
    index['entries'] = [r for r in index['entries'] if r.get('origin') != 'periodic-reading']
    index['entries'].append({'id': 'reading-periodic-dft', 'title': data['title'], 'headings': {lang: documents[lang][CHAPTER]['headings'] for lang in ['ja', 'en']}, 'keywords': data['keywords'], 'routes': {lang: route(lang) for lang in ['ja', 'en']}, 'origin': 'periodic-reading', 'kind': 'chapter'})
    dump(path, index)
    path = ATLAS / 'sitemap.xml'
    tree = ET.parse(path)
    xml = tree.getroot()
    ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    existing = {r.text for r in xml.findall('.//{*}loc')}
    for lang in ['ja', 'en']:
        url = ORIGIN + route(lang)
        if url not in existing:
            ET.SubElement(ET.SubElement(xml, ns + 'url'), ns + 'loc').text = url
    ET.register_namespace('', ns[1:-1])
    tree.write(path, encoding='utf-8', xml_declaration=True)
    print('Built bilingual periodic DFT reading from', len(results['cases']), 'measured settings and', len(results['independent_comparison']['cases']), 'independent-engine comparisons.')


if __name__ == '__main__':
    build()
