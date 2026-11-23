#!/usr/bin/env python3
"""Build the RKDG agent entry from an immutable code kit; never run a solver."""
from pathlib import Path
from html import escape as esc
import hashlib
import json
import re
from atlas_rkdg_prompts import prompt_section

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://hrkoyama.github.io'
data = json.loads((ROOT/'catalog/atlas-agent-kits.json').read_text())
route = data['route']
dest = ROOT/route.lstrip('/')
archive = ROOT/data['archive'].lstrip('/')
assert route == '/numerical-methods-atlas/agent-kits/rkdg2d/'
assert archive.is_file(), 'Install the fixed RKDG release before building its public entry'
archive_sha = hashlib.sha256(archive.read_bytes()).hexdigest()
for name in ['TESTSET.md', 'TESTSET-en.md', 'manifest.json']:
    assert (dest/name).is_file(), 'Missing agent entry input: '+name
manifest=json.loads((dest/'manifest.json').read_text())
assert manifest['release']==data['edition']
assert manifest['archive']['url']==ORIGIN+data['archive']
assert manifest['archive']['sha256']==archive_sha
assert manifest['archive']['bytes']==archive.stat().st_size
assert manifest['candidate_sha256']==data['source_sha256']
assert manifest['original_48_passed'] is True and manifest['waveform_4_passed'] is True
assert manifest['reflection_6_passed'] is False and manifest['reflection_passed_count']==5
for lang in ['ja','en']:
    guide='TESTSET.md' if lang=='ja' else 'TESTSET-en.md'
    assert manifest['guides'][lang]['url']==ORIGIN+route+guide
    assert manifest['guides'][lang]['sha256']==hashlib.sha256((dest/guide).read_bytes()).hexdigest()
assert (ROOT/(data['archive']+'.sha256').lstrip('/')).read_text().split()==[archive_sha,'atlas-rkdg-agent-kit.zip']
for figure in data['figures']:
    assert (dest/'figures'/figure['file']).is_file(), figure['file']
original = json.loads((dest/'evidence/original-verdict.json').read_text())
waveform = json.loads((dest/'evidence/waveform-verdict.json').read_text())
reflection = json.loads((dest/'evidence/reflection-verdict.json').read_text())
assert original['passed'] is True and waveform['passed'] is True
assert reflection['passed'] is False, 'Keep the known supplemental failure visible'
assert sum(original['case_counts'][key] for key in ['smooth','directional','double_mach','temporal'])==48
assert waveform['diagnostic_checks']==4
assert reflection['case_count']==6 and sum(case['passed'] for case in reflection['cases'])==5


def link(url, label):
    assert url.startswith(('/', 'https://', '#')), url
    return '<a href="'+esc(url, quote=True)+'">'+esc(label)+'</a>'


def p(text):
    return '<p>'+esc(text)+'</p>'


def pre(text):
    return '<pre tabindex="0"><code>'+esc(text)+'</code></pre>'


sections = []
for lang in ['ja', 'en']:
    ja = lang == 'ja'
    guide = 'TESTSET.md' if ja else 'TESTSET-en.md'
    body = '<section data-site-language="'+lang+'" lang="'+lang+'"><p class="eyebrow">NUMERICAL METHODS ATLAS · AGENT CODE KIT</p>'
    body += '<h1>'+esc(data['title'][lang])+'</h1><p class="kit-lead">'+esc(data['lead'][lang])+'</p>'
    body += '<nav class="kit-actions" aria-label="'+('取得するもの' if ja else 'Get the kit')+'">'
    body += link('#prompts-'+lang, '開発・修正プロンプトをコピー' if ja else 'Copy development / repair prompts')
    body += link(route+guide, 'AIに渡す案内 / Markdown' if ja else 'Agent instructions / Markdown')
    body += link(route+'manifest.json', '版・実行仕様 / JSON' if ja else 'Release and execution manifest / JSON')
    body += link(data['archive'], 'コードと固定テスト / ZIP' if ja else 'Code and fixed tests / ZIP')+'</nav>'
    body += p(data['scope'][lang])
    body += '<p class="kit-hash">'+esc(data['edition'])+' · '+format(archive.stat().st_size/1_000_000, '.1f')+' MB · SHA256 <code>'+archive_sha+'</code><br>'+link(data['archive']+'.sha256', 'SHA256ファイル' if ja else 'SHA256 file')+'</p>'
    rendered_prompts, prompt_manifest = prompt_section(ROOT, route, lang)
    assert prompt_manifest['archive_sha256'] == archive_sha
    body += rendered_prompts
    body += '<section id="start-'+lang+'"><h2>'+('AIエージェントへの最初の依頼' if ja else 'The first instruction for your AI agent')+'</h2>'
    body += p('次のURLを渡し、「案内を読んでキットを取得し、SHA256を確認して、新しい出力先でクイックテストを実行。結果と未実施の範囲を報告して」と依頼します。' if ja else 'Pass the following URL to your agent: “Read the guide, download the kit, verify SHA256, and run the quick test in a new output directory. Report the result and what was not rerun.”')
    body += pre(ORIGIN+route+guide)
    body += p('ブラウザやGitHubのログイン、ChatGPT・Codexのアカウント、推論APIキーは実行に不要です。初回のNumPy導入にはネット接続が必要です。' if ja else 'Running the code requires no browser/GitHub sign-in, ChatGPT/Codex account or inference API key. Initial NumPy installation needs network access.')+'</section>'
    body += '<section><h2>'+('取得して、最初の計算を動かす' if ja else 'Download and run the first calculation')+'</h2>'
    body += p('macOS / Linuxの例です。既存ファイルのない作業フォルダで実行し、Python環境は案内の対応条件に合わせます。Windows等では、その環境に対応する取得・SHA256・Pythonの操作へ読み替えます。' if ja else 'Example for macOS / Linux. Use a new working directory and the Python requirements in the guide. On Windows or other environments, use the corresponding download, SHA256 and Python operations.')
    command = '\n'.join([
        'set -eu',
        'curl --fail --location --output atlas-rkdg-agent-kit.zip '+ORIGIN+data['archive'],
        'curl --fail --location --output atlas-rkdg-agent-kit.zip.sha256 '+ORIGIN+data['archive']+'.sha256',
        'shasum -a 256 -c atlas-rkdg-agent-kit.zip.sha256',
        'unzip atlas-rkdg-agent-kit.zip',
        'cd atlas-rkdg-agent-kit',
        'shasum -a 256 -c SHA256SUMS.txt',
        'python3 -m venv .venv',
        '. .venv/bin/activate',
        'python -m pip install -r requirements-verified.txt',
        'python scripts/run_rkdg_smoke.py --solver agent-kits/rkdg2d/generated/rkdg2d.py --output outputs/quick-smoke.json',
    ])
    body += pre(command)
    body += p('クイックテストは小さな新規PDE計算です。終了コードと出力JSONを確認してください。これだけで全固定試験への合格とはしません。' if ja else 'The quick test performs small fresh PDE solves. Inspect its exit code and output JSON. Passing it does not establish a pass of the full fixed suite.')+'</section>'
    body += '<section><h2>'+('検証を段階的に進める' if ja else 'Choose the verification depth')+'</h2><ol class="kit-workflow">'
    steps = [
        ('クイック実計算', 'Fresh quick calculation', '小さな斜め波を実際に解き、厳密解との誤差と保存則を確認します。', 'Actually evolve a small oblique wave and check analytic error and conservation.'),
        ('保存結果を再判定', 'Recheck the stored results', '配布物全体のハッシュを照合し、元48ケースの指標と波形4診断を再評価します。PDEの再実行とは分けて報告します。', 'Verify the complete file hashes and reassess the original 48-case metrics and four waveform diagnostics. Report this separately from fresh PDE execution.'),
        ('全固定入力で再計算', 'Rerun the full fixed inputs', '斜めエントロピー波、x/yのSod・Shu–Osher、Double Mach、時間刻みの計算と負例を実行し、独立参照・固定基準へ渡します。実行時間は機種に依存します。', 'Run oblique entropy waves, x/y Sod and Shu–Osher, Double Mach, time refinement and the negative control, then apply independent references and frozen criteria. Runtime depends on the machine.'),
        ('自分のコードを評価', 'Evaluate your modified code', '検証済み候補を別の場所へ複製して改修。Python候補は--solverで指定し、移植・MPIは共通出力契約へ接続します。基準・参照・既存記録は変更しません。', 'Copy the accepted candidate before editing. Select a Python candidate with --solver; connect language ports and MPI output through the interchange contract. Keep the criteria, references and historical records unchanged.'),
    ]
    for jp, en, jtext, etext in steps:
        body += '<li><strong>'+esc(jp if ja else en)+'</strong>'+p(jtext if ja else etext)+'</li>'
    body += '</ol>'+p('コマンド、JSONの合否、ソースSHA、未実施の項目をまとめる報告様式はMarkdownとmanifestを参照してください。反転xの追加試験は元の候補SHAに固定した別試験です。' if ja else 'The Markdown and manifest specify commands, JSON acceptance, source hashes and reporting of unperformed checks. The additional reversed-x test is a separate check pinned to the original candidate SHA.')+'</section>'
    body += '<section class="kit-known-limit"><h2>'+('既知の結果と限界' if ja else 'Known results and limits')+'</h2>'
    body += p('公開候補は元48科学ケースと波形4診断に合格。追加の反転対称性試験は6件中5件が合格し、Shu–Osher p3は規格化最大差1.4833×10⁻¹⁰が固定上限1×10⁻¹⁰を超えて不合格です。失敗を含めて配布します。' if ja else 'The published candidate passes the original 48 scientific cases and four waveform diagnostics. The additional reflection test passes five of six; Shu–Osher p3 fails because the normalized maximum difference, 1.4833e-10, exceeds the frozen 1e-10 limit. The failure is included in the kit.')
    body += p('x/yの厳密1D入力は解析的な1D縮約を使用。斜め波とDouble Machが完全2D結合を確認します。正値性は指定した求積点・面・頂点の範囲です。衝撃波の全域で2・3・4次精度を主張しません。' if ja else 'Exactly 1D x/y inputs use an analytic 1D restriction. Oblique waves and Double Mach exercise full 2D coupling. Positivity is checked at specified quadrature, face and corner points. No global second/third/fourth-order accuracy is claimed across shocks.')
    body += p('C++17の解析多項式I/Oと1/2/4分割の保存出力は確認済み。実MPI起動や他言語PDEソルバーの実行は未実施です。共通22実行例とは別の開発キットで、サイト全体の問題・手法件数へ追加していません。' if ja else 'C++17 analytic-polynomial I/O and stored 1/2/4-partition fixtures were checked. Real MPI execution and foreign-language PDE solvers have not been run. This development kit is separate from the 22 shared recipes and does not add to the site-wide problem/method counts.')
    body += '<nav class="resource-nav">'+link(route+'evidence/original-verdict.json', '元48ケースの判定 / JSON' if ja else 'Original 48-case verdict / JSON')+link(route+'evidence/waveform-verdict.json', '波形4診断 / JSON' if ja else 'Four waveform diagnostics / JSON')+link(route+'evidence/reflection-verdict.json', '反転6ケース・失敗記録 / JSON' if ja else 'Six reflection cases and failure / JSON')+'</nav></section>'
    body += '<section><h2>'+('保存された図を確かめる' if ja else 'Inspect the stored figures')+'</h2>'
    for figure in data['figures']:
        body += '<figure><img src="'+route+'figures/'+esc(figure['file'])+'" alt="'+esc(figure['caption'][lang],quote=True)+'" loading="lazy"><figcaption>'+esc(figure['caption'][lang])+'</figcaption></figure>'
    body += '</section><section><h2>'+('出典と利用条件' if ja else 'References and reuse')+'</h2>'
    body += p('実装コードは同梱MITライセンス。本文・図・保存データと第三者資料の条件はコードと分け、ZIPの来歴・ライセンス案内を確認してください。独立参照は別実装のFV WENO5/HLLCとFV MUSCL/HLL、およびSodの厳密Riemann解です。' if ja else 'Implementation code uses the bundled MIT license. Read the kit provenance and license notes separately for text, figures, stored data and third-party material. Independent references use separate FV WENO5/HLLC and FV MUSCL/HLL implementations and the exact Sod Riemann solution.')
    body += '<ul>'+''.join('<li>'+link('https://doi.org/'+x['doi'],x['label'])+'</li>' for x in data['references'])+'</ul>'
    body += p('詳しい数式、固定入力、実測値、過去の失敗・修正履歴はZIP内の docs/rkdg.md / docs/rkdg-en.md を参照してください。' if ja else 'See docs/rkdg.md / docs/rkdg-en.md inside the ZIP for equations, fixed inputs, measurements and the history of failures and repairs.')+'</section>'
    if data.get('history'):
        body += '<section><h2>'+('配布版の履歴' if ja else 'Release history')+'</h2>'
        for old in data['history']:
            body += '<h3>'+esc(old['edition'])+'</h3>'+p(old['note'][lang])
            body += '<nav class="resource-nav">'+link(old['archive'], '旧版ZIP' if ja else 'Previous ZIP')+link(old['manifest'], '保存したmanifest' if ja else 'Archived manifest')+link(old['guides'][lang], '保存したMarkdown' if ja else 'Archived Markdown')+'</nav>'
        body += '</section>'
    body += '<nav class="resource-nav">'+link('/numerical-methods-atlas/?lang='+lang, 'アトラス冒頭' if ja else 'Atlas home')+link('/numerical-methods-atlas/code-and-data/?lang='+lang, '既存の実行例とコード' if ja else 'Existing examples and code')+link('/numerical-methods-atlas/methods/dg/?lang='+lang, 'DG法の解説と対応表' if ja else 'DG method and code reference')+'</nav></section>'
    sections.append(body)

css='/styles/atlas-agent-kits.css'
version=hashlib.sha256((ROOT/css.lstrip('/')).read_bytes()).hexdigest()[:12]
js='/scripts/atlas-agent-prompts.mjs'
js_version=hashlib.sha256((ROOT/js.lstrip('/')).read_bytes()).hexdigest()[:12]
document='<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title data-page-title-ja="2D RKDG開発キット | 数値計算法アトラス" data-page-title-en="2D RKDG agent code kit | Numerical Methods Atlas">2D RKDG開発キット | 数値計算法アトラス</title><meta name="description" content="AIエージェントが2D Euler RKDGの完成コード・固定テスト・独立参照を取得し、実行・改修・判定する日英Markdownと機械可読manifest。"><link rel="canonical" href="'+ORIGIN+route+'"><link rel="stylesheet" href="/styles/atlas-resources.css"><link rel="stylesheet" href="'+css+'?v='+version+'"></head><body class="profile-page"><main class="profile-main atlas-resource-main agent-kit" id="main">'+''.join(sections)+'</main></body></html>\n'
document=document.replace('</body>', '<script type="module" src="'+js+'?v='+js_version+'"></script></body>')
(dest/'index.html').write_text(document)
(dest/'index.json').write_text(json.dumps({**data,'archive_sha256':archive_sha,'archive_bytes':archive.stat().st_size,'guides':{l:ORIGIN+route+('TESTSET.md' if l=='ja' else 'TESTSET-en.md') for l in ['ja','en']},'manifest':ORIGIN+route+'manifest.json','prompts':prompt_manifest,'scientific_computation_run_by_builder':False},ensure_ascii=False,indent=2)+'\n')
guide=ROOT/'llms.txt'
text=guide.read_text()
marker='\n## Agent code kits / AIエージェント向け開発キット\n'
text=re.sub(r'\n## Agent code kits / AIエージェント向け開発キット\n.*?(?=\n## |\Z)', '', text, flags=re.S)
text += marker+'\n- [2D Euler RKDG agent guide — 日本語]('+ORIGIN+route+'TESTSET.md): working Q1/Q2/Q3 code, SHA256-verified ZIP, fresh quick test, saved-result reassessment and full fixed tests. Preserve original48 + waveform4 PASS separately from additional reflection5/6 known failure.\n- [2D Euler RKDG agent guide — English]('+ORIGIN+route+'TESTSET-en.md)\n- [2D Euler RKDG manifest]('+ORIGIN+route+'manifest.json): source/version, acquisition and execution contract. Full MPI and foreign-language PDE runs remain unperformed.\n'
guide.write_text(text)
text=guide.read_text()
for name, info in prompt_manifest['files'].items():
    text += '- [RKDG '+name+']('+info['url']+'): copyable development/repair prompt, frozen original48 + waveform4 target; failures and incomplete runs must remain visible.\n'
guide.write_text(text)
print('Built RKDG agent entry; no scientific computation. ZIP SHA256 '+archive_sha)
