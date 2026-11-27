#!/usr/bin/env python3
"""Build bilingual periodic-force reading from prose and frozen measurements.

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
from atlas_reading_presentation import specialized_reading_layout
from atlas_depth_release import load_depth_group
from atlas_md_scope import chapter_md_scope

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / 'numerical-methods-atlas'
SOURCE = '/catalog/atlas-forces-reading.json'
ORIGIN = 'https://hrkoyama.github.io'
CHAPTER = 'periodic-forces'
EXAMPLE = 'periodic-he-forces'


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


def measured(results, lang, base, config, reference):
    ja = lang == 'ja'
    indexed = {r['id']: r for r in results['cases']}
    assert len(indexed) == len(results['cases']) and indexed
    assert all(r['converged'] and r['termination'] == 'converged' for r in indexed.values())
    names = {'kpoint': ('k点メッシュ', 'k-point mesh'), 'basis': ('ΓのGaussian軌道基底', 'Gaussian orbital basis at Γ'), 'basis-k2': ('2³メッシュのGaussian軌道基底', 'Gaussian orbital basis on the 2³ mesh'), 'auxiliary': ('補助FFT格子', 'auxiliary FFT grid'), 'scf': ('SCF許容誤差', 'SCF tolerances')}
    force_norm = lambda a, b: max(abs(x - y) for va, vb in zip(a, b, strict=True) for x, y in zip(va, vb, strict=True))
    close = lambda a, b: abs(a - b) <= max(1e-14, abs(b) * 1e-10)
    fd = results['finite_difference']
    assert len(fd['components']) == 6
    assert {(r['atom'], r['axis']) for r in fd['components']} == {(a, i) for a in range(2) for i in range(3)}
    for row in fd['components']:
        assert close(row['force_finite_difference'], -(row['energy_plus'] - row['energy_minus']) / (2 * fd['step_bohr']))
        assert close(row['absolute_error'], abs(row['force_analytic'] - row['force_finite_difference']))
    assert close(fd['max_component_error'], max(r['absolute_error'] for r in fd['components']))
    comparisons = results['independent_comparison']['cases']
    assert sorted(row['k_n'] for row in comparisons) == [1, 2]
    for row in comparisons:
        assert close(row['max_absolute_force_difference'], force_norm(row['pyscf_forces_cartesian'], row['dftk_forces_cartesian']))
        assert row['passed'] is True and row['max_absolute_force_difference'] <= config['acceptance']['reference_force_difference']
    body = heading('measured-results', '保存した実測値：有限差分・独立参照・力の収束' if ja else 'Stored measurements: finite differences, independent references and force convergence')
    body += para('下の数値は公開版の固定入力から得た保存結果です。力の比較は特記しない限り全Cartesian成分の最大絶対差（hartree/bohr）です。異なる収束系列は同じ設定を再利用し、設定数を別々の物理問題の数とは数えません。判定には表示の丸め前の数値を用います。横長の数値表は表の中を横にスクロールして読めます。' if ja else 'These stored results come from the release’s fixed input. Force comparisons use the maximum absolute difference over Cartesian components in hartree/bohr unless stated otherwise. Sweeps reuse common settings; setting counts are not distinct physical problems. Acceptance uses unrounded values. Wide numeric tables scroll horizontally within their own region.')
    summary = [
        ['全6成分の有限差分との最大差' if ja else 'Maximum finite-difference error over all six components', fd['max_component_error'], config['acceptance']['finite_difference_max_error']],
        ['変位幅走査の最大差' if ja else 'Maximum error across the displacement scan', fd['scan_max_error'], config['acceptance']['finite_difference_scan_max_error']],
        ['Γ・2³でのDFTKとの最大差' if ja else 'Maximum DFTK force difference at Γ and 2³', max(r['max_absolute_force_difference'] for r in comparisons), config['acceptance']['reference_force_difference']],
    ]
    body += table(['比較 / hartree・bohr⁻¹', '実測値', '入力の受入幅'] if ja else ['Comparison / hartree per bohr', 'Measured value', 'Input acceptance width'], summary, '力の照合の要約' if ja else 'Force comparison summary')
    body += heading('force-components', '各設定の力の全成分' if ja else 'All force components for each setting')
    body += para('原子番号は0から始めます。FD照合の基底・格子・k点は入力で指定したcase_idに対応し、DFTKとの独立比較に使う大きなGaussian基底とは区別します。' if ja else 'Atom indices start at zero. The basis, grid and k mesh for finite-difference checks are specified by case_id in the input; these are distinct from the larger Gaussian bases used for independent DFTK comparisons.')
    body += table(['ケース', 'kメッシュ', '基底', 'FFT', 'E / hartree', 'F₀x', 'F₀y', 'F₀z', 'F₁x', 'F₁y', 'F₁z', '||R(SCF)||', '反復', '終了'] if ja else ['Case', 'k mesh', 'Basis', 'FFT', 'E / hartree', 'F₀x', 'F₀y', 'F₀z', 'F₁x', 'F₁y', 'F₁z', '||R(SCF)||', 'Iterations', 'Termination'], [[r['id'], [r['k_n']] * 3, r['basis'], r['fft_mesh'], r['energy_per_cell'], *r['forces_cartesian'][0], *r['forces_cartesian'][1], r['scf_commutator_norm'], r['iterations'], r['termination']] for r in indexed.values()], '力の成分：hartree/bohr' if ja else 'Force components: hartree/bohr')
    body += heading('finite-difference-results', 'PySCF内の照合：全6成分のエネルギー中心差分' if ja else 'PySCF internal check: central energy differences for all six components')
    body += para(('基準ケース：' if ja else 'Baseline case: ') + fd['case_id'] + ('、変位幅h / bohr：' if ja else '; displacement h / bohr: ') + number(fd['step_bohr']))
    body += table(['原子', '軸', 'E(−h) / hartree', 'E(+h) / hartree', '解析力', '有限差分力', '|差|'] if ja else ['Atom', 'Axis', 'E(−h) / hartree', 'E(+h) / hartree', 'Analytic force', 'Finite-difference force', '|Difference|'], [[r['atom'], 'xyz'[r['axis']], r['energy_minus'], r['energy_plus'], r['force_analytic'], r['force_finite_difference'], r['absolute_error']] for r in fd['components']], 'エネルギー微分と力：hartree/bohr' if ja else 'Energy derivatives and forces: hartree/bohr')
    body += heading('finite-difference-steps', '変位幅hの走査' if ja else 'Displacement-step scan')
    body += table(['h / bohr', '解析力', '有限差分力', '|差| / hartree・bohr⁻¹'] if ja else ['h / bohr', 'Analytic force', 'Finite-difference force', '|Difference| / hartree per bohr'], [[r['step_bohr'], r['force_analytic'], r['force_finite_difference'], r['absolute_error']] for r in fd['steps']], '固定した1成分のh依存性' if ja else 'Step-size dependence for one fixed component')
    body += heading('convergence-targets', '力の5つの収束系列' if ja else 'Five force-convergence sequences')
    for axis, group in results['convergence'].items():
        assert axis in names and group['case_ids'] == config['convergence_groups'][axis]
        rows = [indexed[i] for i in group['case_ids']]
        changes = [force_norm(a['forces_cartesian'], b['forces_cartesian']) for a, b in zip(rows, rows[1:])]
        assert len(changes) == len(group['adjacent_changes']) and all(close(a, b) for a, b in zip(changes, group['adjacent_changes']))
        assert close(group['last_change'], changes[-1])
        assert group['target_reached'] is True and group['last_change'] <= group['target']
    body += table(['変更した量', '最後の||ΔF||∞', '入力の目標', '目標達成'] if ja else ['Changed quantity', 'Final ||ΔF||∞', 'Input target', 'Target met'], [[names[k][0 if ja else 1], r['last_change'], r['target'], r['target_reached']] for k, r in results['convergence'].items()], '末尾の力の変化：hartree/bohr' if ja else 'Final force increments: hartree/bohr')
    for axis, group in results['convergence'].items():
        body += heading('results-' + axis, names[axis][0 if ja else 1] + ('の系列' if ja else ' sequence'))
        rows = [indexed[i] for i in group['case_ids']]
        body += table(['ケース', 'k', '基底', 'FFT', 'ΔE公差', '軌道勾配公差', '前の設定からの||ΔF||∞'] if ja else ['Case', 'k', 'Basis', 'FFT', 'Energy tolerance', 'Orbital-gradient tolerance', '||ΔF||∞ from previous'], [[r['id'], r['k_n'], r['basis'], r['fft_mesh'], r['scf_options']['energy_tolerance'], r['scf_options']['gradient_tolerance'], '—' if j == 0 else group['adjacent_changes'][j - 1]] for j, r in enumerate(rows)], names[axis][0 if ja else 1])
    body += heading('reference-results', '独立DFTKとの全成分比較' if ja else 'All-component comparison with independent DFTK')
    body += para('両エンジンは同じXC評価のLibxcを共用しますが、Hamiltonian・SCF・軌道離散化・力の実装は別です。有限空間の違いを含む比較を、同一行列の丸め誤差や完全基底極限の証明と呼びません。' if ja else 'Both engines share Libxc for XC evaluation, while Hamiltonians, SCF, orbital discretizations and force implementations differ. Differences between finite spaces are not rounding errors of an identical matrix or proof of the complete-basis limit.')
    body += table(['kメッシュ', 'PySCFケース', 'max|ΔF| / hartree・bohr⁻¹', '|ΔE| / hartree', '力の受入幅', '合格'] if ja else ['k mesh', 'PySCF case', 'max|ΔF| / hartree per bohr', '|ΔE| / hartree', 'Force acceptance width', 'Passed'], [[[r['k_n']] * 3, r['case_id'], r['max_absolute_force_difference'], r['energy_absolute_difference'], config['acceptance']['reference_force_difference'], r['passed']] for r in comparisons], '独立エンジン比較' if ja else 'Independent-engine comparison')
    body += table(['kメッシュ', '原子', '軸', 'PySCF', 'DFTK', '|差|'] if ja else ['k mesh', 'Atom', 'Axis', 'PySCF', 'DFTK', '|Difference|'], [[[r['k_n']] * 3, a, 'xyz'[i], r['pyscf_forces_cartesian'][a][i], r['dftk_forces_cartesian'][a][i], abs(r['pyscf_forces_cartesian'][a][i] - r['dftk_forces_cartesian'][a][i])] for r in comparisons for a in range(2) for i in range(3)], '独立力の全成分：hartree/bohr' if ja else 'All independent force components: hartree/bohr')
    cutoff = reference['cutoff_convergence']
    assert cutoff['target_reached'] is True
    body += heading('reference-cutoff-results', '参照側の平面波カットオフ収束' if ja else 'Plane-wave cutoff convergence of the reference')
    body += table(['kメッシュ', 'カットオフ / hartree', 'E / hartree', 'F₀x', 'F₀y', 'F₀z', '密度残差', 'SCF収束'] if ja else ['k mesh', 'Cutoff / hartree', 'E / hartree', 'F₀x', 'F₀y', 'F₀z', 'Density residual', 'SCF converged'], [[[r['k_n']] * 3, r['ecut_hartree'], r['energy_per_cell'], *r['forces_cartesian'][0], r['density_residual'], r['converged']] for r in cutoff['records']], 'DFTKカットオフ系列' if ja else 'DFTK cutoff sequence')
    body += table(['kメッシュ', '最後のカットオフ', '最後の||ΔF||∞', '力の目標', '最後の|ΔE|', 'エネルギー目標', '目標達成'] if ja else ['k mesh', 'Final cutoff', 'Final ||ΔF||∞', 'Force target', 'Final |ΔE|', 'Energy target', 'Target met'], [[[r['k_n']] * 3, r['to_ecut_hartree'], r['force_max_change'], cutoff['force_target_hartree_per_bohr'], r['energy_change'], cutoff['energy_target_hartree_per_cell'], r['target_reached']] for r in cutoff['last_changes']], '参照収束の力とエネルギー' if ja else 'Force and energy reference convergence')
    ref_fd = reference['finite_difference']
    body += heading('reference-finite-difference-results', 'DFTK側でも解析力とエネルギー差分を照合' if ja else 'DFTK-side analytic-force and energy-difference checks')
    body += table(['原子', '軸', 'h / bohr', '解析力', '有限差分力', '|差|'] if ja else ['Atom', 'Axis', 'h / bohr', 'Analytic force', 'Finite-difference force', '|Difference|'], [[r['atom_index'], 'xyz'[r['component']], r['step_bohr'], r['analytic_force'], r['central_difference_force'], r['absolute_error']] for r in ref_fd['records']], 'DFTK内部の力照合：hartree/bohr' if ja else 'DFTK internal force checks: hartree/bohr')
    body += heading('bomd-interface-results', 'BOMD接続の短い実行試験' if ja else 'Short execution check of the BOMD interface')
    body += para('同じ短い時間を、速度Verletの1刻みと2つの半刻みで進め、各配置で電子状態を再収束させます。下の位置・速度差とエネルギー変化は接続の局所的な検査であり、長時間NVEの保存性や刻み幅収束の次数の証明ではありません。入力の質量・初速度・時間を固定し、温度制御は使いません。' if ja else 'The same short interval is advanced with one velocity-Verlet step and two half steps, reconverging electrons at each configuration. Position/velocity differences and energy changes below are local interface checks, not proof of long-time NVE conservation or an observed timestep-convergence order. Masses, initial velocities and duration are fixed; no thermostat is used.')
    md = results['bomd']
    body += table(['量', '実測値', '単位'] if ja else ['Quantity', 'Measured value', 'Unit'], [
        ['合計時間' if ja else 'Total interval', md['total_time_atomic_units'], 'atomic time'],
        ['位置の最大成分差' if ja else 'Maximum position-component difference', md['position_max_difference'], 'bohr'],
        ['速度の最大成分差' if ja else 'Maximum velocity-component difference', md['velocity_max_difference'], 'bohr / atomic time'],
        ['1刻みの|ΔE|（全エネルギー）' if ja else '|ΔE| of total energy: one step', md['full_step_energy_defect'], 'hartree'],
        ['2つの半刻みの|ΔE|（全エネルギー）' if ja else '|ΔE| of total energy: two half steps', md['two_half_steps_energy_defect'], 'hartree'],
    ], 'BOMDの局所接続試験' if ja else 'Local BOMD interface check')
    image = ROOT / (base + 'results/preview.png').lstrip('/')
    if image.is_file():
        png = image.read_bytes()
        assert png[:8] == b'\x89PNG\r\n\x1a\n'
        width, height = struct.unpack('>II', png[16:24])
        body += '<figure><img src="' + base + 'results/preview.png" width="' + str(width) + '" height="' + str(height) + '" loading="lazy" alt="' + ('固定He₂配置の力の有限差分・基底・k点・補助格子・SCF収束の保存図' if ja else 'Stored finite-difference, basis, k-point, auxiliary-grid and SCF force-convergence plots for a fixed He2 configuration') + '"><figcaption>' + ('保存結果の可視化です。合否は元の入力・結果JSONで判定します。' if ja else 'A visualization of stored results; acceptance uses the original input/result JSON.') + '</figcaption></figure>'
    body += '<p>' + link(base + 'results/result.json', '全結果 / JSON' if ja else 'Full results / JSON') + ' · ' + link(base + 'results/solution.csv', '設定と力 / CSV' if ja else 'Settings and forces / CSV') + ' · ' + link(base + 'reference-dftk.json', '独立参照と収束 / JSON' if ja else 'Independent reference and convergence / JSON') + '</p>'
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
    # Reading-only is local to this He chapter; the global method also has a
    # separately qualified two-state educational example, not a KS trajectory.
    md_packet = load_depth_group(ROOT, 'quantum-small', '2026-11-25')
    md_scope = chapter_md_scope(data, methods, md_packet)
    sources.update(md_packet['source_sha256'])
    sources.update({name: sha(ROOT / name) for name in ['catalog/atlas-methods.json', 'scripts/atlas_md_scope.py']})
    rendered = json.loads(subprocess.check_output(['node', 'scripts/render-atlas-math.cjs'], cwd=ROOT, input=json.dumps([{'id': k, 'formula': [v]} for k, v in data['formulas'].items()]).encode()))['rendered']
    references = {r['id']: r for r in data['references']}
    documents = {lang: read(ATLAS / f'content.{lang}.json') for lang in ['ja', 'en']}
    translations = read(ATLAS / 'translation-status.json')
    for lang in ['ja', 'en']:
        ja = lang == 'ja'
        title = data['title'][lang]
        body = '<h1>' + e(title) + '</h1>' + para(data['intro'][lang])
        body += '<aside class="resource-summary">' + para(data['scope'][lang]) + '</aside>'
        opening = body
        example_url = '/numerical-methods-atlas/code-and-data/examples/' + EXAMPLE + '/?lang=' + lang
        body += '<nav class="resource-nav">' + link(example_url, '固定入力・コード・テスト・判定条件' if ja else 'Fixed input, code, tests and acceptance') + ' · ' + link('/numerical-methods-atlas/' + lang + '/read/periodic-dft/', '周期DFTの基礎' if ja else 'Periodic DFT foundations') + ' · ' + link('/numerical-methods-atlas/connections/?lang=' + lang + '#dft-md-' + lang, '分野をつなぐ経路' if ja else 'Cross-field path') + ' · ' + link(base + package['archive'], 'ZIP') + ' · ' + link(base + 'verification.json', '独立展開の検証 / JSON' if ja else 'Independent-extraction verification / JSON') + '</nav>'
        body += measured(results, lang, base, read(release / package['input']), read(release / package['reference']))
        markdown = '# ' + title + '\n\n' + data['intro'][lang] + '\n\n' + data['scope'][lang] + '\n\n'
        for section in data['sections']:
            body += heading(section['id'], section['title'][lang]) + ''.join(para(p) for p in section['paragraphs'][lang])
            body += ''.join('<div class="math-block">' + rendered[f][0] + '</div>' for f in section['formulas'])
            body += '<p class="periodic-citations">' + ('関連出典：' if ja else 'Sources: ') + ', '.join(link('#source-' + i, references[i]['author'] + ' (' + str(references[i]['year']) + ')') for i in section['references']) + '</p>'
            markdown += '## ' + section['title'][lang] + '\n\n' + '\n\n'.join(section['paragraphs'][lang]) + '\n\n' + ''.join('$$\n' + data['formulas'][f] + '\n$$\n\n' for f in section['formulas'])
            if section['id'] == 'bomd-interface':
                body += '<p class="resource-nav">' + link(md_scope['entry']+'?lang='+lang, md_scope['title'][lang]) + ' · ' + link(md_scope['source_manifest'], '別模型の固定版・SHA-256' if ja else 'Separate-model fixed edition and SHA-256') + '</p>'
                markdown += md_scope['title'][lang] + ': ' + md_scope['entry']+'?lang='+lang + '\n\n' + md_scope['source_manifest'] + '\n\n'
        body += heading('run-and-check', '取得して結果を確かめる' if ja else 'Download and verify the results')
        body += para('ZIP内の配布版フォルダで依存関係を導入し、同梱の固定入力を使います。出力先は新規または空のディレクトリにします。通常のrunnerは保存済みDFTK参照を照合します。Juliaによる参照の再生成は別工程で、参照用環境と手順を同梱しています。' if ja else 'Install dependencies in the extracted edition directory and use its fixed input. Choose a new or empty output directory. The ordinary runner compares with the saved DFTK reference. Regenerating that reference in Julia is a separate operation with its own packaged environment and instructions.')
        commands = 'python -m pip install -r requirements.txt\npython -m pytest -q\npython run.py --input inputs.json --output output'
        body += '<pre><code>' + commands + '</code></pre><p>' + link(base + package['input'], '固定入力 / JSON' if ja else 'Fixed input / JSON') + ' · ' + link(base + 'run.py', 'Runner') + ' · ' + link(base + 'periodic_forces.py', '原子間力のAPI' if ja else 'Atomic-force API') + ' · ' + link(base + 'bomd.py', 'BOMDの接続' if ja else 'BOMD interface') + ' · ' + link(base + package['reference'], 'DFTK独立参照 / JSON' if ja else 'Independent DFTK reference / JSON') + ' · ' + link(example_url, '版・受入条件・引用の共通手順' if ja else 'Edition, acceptance criteria and citation') + '</p>'
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
        style = '<style>.periodic-reading{max-width:1100px;margin:auto;padding:1.2rem;overflow-wrap:anywhere}.periodic-reading .prose{max-width:88ch;margin:auto}.periodic-reading .prose h1{font-size:clamp(1.8rem,3.5vw,2.75rem);line-height:1.35;margin-block:1.1rem}.periodic-reading .prose p{font-size:1rem;line-height:1.85}.periodic-reading .resource-nav,.periodic-reading>nav{display:flex;flex-wrap:wrap;gap:.5rem}.periodic-reading>nav a{padding:.3rem}.periodic-reading .math-block,.periodic-table{max-width:100%;overflow-x:auto}.periodic-table{margin:1rem 0}.periodic-table table{border-collapse:collapse;min-width:100%;font-size:.95rem}.periodic-table td,.periodic-table th{border-bottom:1px solid #becbc3;padding:.55rem;text-align:left}.periodic-table td:not(:first-child){font-variant-numeric:tabular-nums;white-space:nowrap}.periodic-table th:first-child,.periodic-table td:first-child{min-width:12rem;overflow-wrap:normal}.periodic-reading img,.periodic-reading svg{width:100%;height:auto}.periodic-reading pre{white-space:pre;overflow:auto;padding:1rem;background:#eef3ef}.periodic-reading li{margin-bottom:1rem}.periodic-reading h2{scroll-margin-top:1rem}.periodic-toc{margin:1rem 0}.periodic-toc summary{padding:.5rem 0;cursor:pointer}.periodic-toc nav{display:flex;flex-wrap:wrap;gap:.5rem 1rem;padding:.6rem 0}.periodic-citations{font-size:.95rem}.periodic-reading .resource-summary{border-left:4px solid #386552;padding:.3rem 1rem;background:#eef3ef}</style>'
        document = '<!doctype html><html lang="' + lang + '"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + e(title) + ' | Numerical Methods Atlas</title><meta name="description" content="' + e(data['intro'][lang], quote=True) + '"><link rel="canonical" href="' + ORIGIN + route(lang) + '">' + ''.join('<link rel="alternate" hreflang="' + l + '" href="' + ORIGIN + route(l) + '">' for l in ['ja', 'en']) + '<link rel="stylesheet" href="/numerical-methods-atlas/vendor/katex.min.css"><link rel="stylesheet" href="/numerical-methods-atlas/style.css"><link rel="stylesheet" href="/styles/atlas-resources.css">' + style + '</head><body class="profile-page" data-content-language="' + lang + '"><main id="main" class="periodic-reading">' + specialized_reading_layout(nav, toc, body, opening, lang) + '</main></body></html>\n'
        (directory / 'index.html').write_text(document)
        dump(directory / 'index.json', {**entry, 'url': ORIGIN + route(lang), 'methods': data['methods'], 'reading_only_methods': data['reading_only_methods'], 'reading_only_methods_scope': data['reading_only_methods_scope'], 'scoped_educational_examples': [md_scope], 'execution_example': EXAMPLE, 'references': data['references'], 'source_sha256': sources, 'measurements': results['metrics']})
        markdown += '## ' + ('保存した実測値' if ja else 'Stored measurements') + '\n\n' + '\n'.join('- ' + k + ': ' + number(v) for k, v in results['metrics'].items()) + '\n\n' + ORIGIN + base + package['results'] + '\n\n'
        markdown += '## ' + ('実行' if ja else 'Execution') + '\n\n```sh\n' + commands + '\n```\n\n' + ORIGIN + example_url + '\n\n'
        markdown += '## ' + ('文献' if ja else 'Sources') + '\n\n' + '\n'.join('- ' + r['author'] + ' (' + str(r['year']) + '). ' + r['title'] + '. ' + r['source'] + ' — ' + r['review'][lang] for r in data['references']) + '\n'
        (directory / 'index.md').write_text(markdown)
        path = ATLAS / lang / 'read/index.html'
        text = re.sub(r'<!-- forces-reading -->.*?<!-- /forces-reading -->', '', path.read_text(), flags=re.S)
        block = '<!-- forces-reading --><section class="page-width"><h2>' + ('DFTの原子間力とBOMDへの接続' if ja else 'DFT atomic forces and the BOMD interface') + '</h2><p>' + link(route(lang), title) + '</p></section><!-- /forces-reading -->'
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
    index['entries'] = [r for r in index['entries'] if r.get('origin') != 'forces-reading']
    index['entries'].append({'id': 'reading-periodic-forces', 'title': data['title'], 'headings': {lang: documents[lang][CHAPTER]['headings'] for lang in ['ja', 'en']}, 'keywords': data['keywords'], 'routes': {lang: route(lang) for lang in ['ja', 'en']}, 'origin': 'forces-reading', 'kind': 'chapter'})
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
    print('Built bilingual periodic-force reading from', len(results['cases']), 'measured settings.')


if __name__ == '__main__':
    build()
