#!/usr/bin/env python3
"""Connect the separately verified AD edition to the public solver foundation."""
from pathlib import Path
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / 'numerical-methods-atlas'
methods = json.loads((ROOT / 'catalog/atlas-methods.json').read_text())['methods']
method = next(m for m in methods if m['id'] == 'automatic-differentiation')
release = ROOT / method['autodiff_release']['base'].lstrip('/')
for extension in ('json', 'png'):
    shutil.copyfile(release / f'docs/figures/autodiff-bratu.{extension}',
                    ATLAS / f'assets/autodiff-bratu.{extension}')

start, end = '<!-- autodiff-foundation -->', '<!-- /autodiff-foundation -->'
for lang in ('en', 'ja'):
    label = '共通基盤：自動微分とBratuの検証' if lang == 'ja' else 'Shared foundation: automatic differentiation and Bratu verification'
    detail = ('同じ残差・初期値・Newton停止条件で解析微分・有限差分・前進モード自動微分を比較します。微分誤差・非線形残差・空間離散化誤差を分け、専用コード・8件のテスト・再生成手順を公開しています。逆モードと陰関数感度の実行検証は今後の課題です。'
              if lang == 'ja' else
              'Compare analytic, finite-difference and forward-mode AD with the same residual, initial state and Newton stopping controls. Derivative error, nonlinear residual and spatial discretization error are reported separately, with dedicated code, eight tests and reproduction commands. Executable reverse-mode and implicit-sensitivity checks remain future work.')
    note = start + '<aside class="resource-summary"><p><a href="/numerical-methods-atlas/' + lang + '/read/automatic-differentiation/">' + label + '</a></p><p>' + detail + '</p></aside>' + end
    path = ATLAS / f'content.{lang}.json'
    documents = json.loads(path.read_text())
    for chapter in ('sparse-nonlinear', 'stiff-integration', 'roadmap'):
        entry = documents[chapter]
        entry['html'] = re.sub(re.escape(start) + '.*?' + re.escape(end), '', entry['html'], flags=re.S) + note
        static = ATLAS / lang / 'read' / chapter / 'index.html'
        html = re.sub(re.escape(start) + '.*?' + re.escape(end), '', static.read_text(), flags=re.S)
        assert '</article>' in html, static
        static.write_text(html.replace('</article>', note + '</article>', 1))
    path.write_text(json.dumps(documents, ensure_ascii=False, indent=2) + '\n')
    if lang == 'en':
        (ATLAS / 'content.json').write_text(path.read_text())
print('Connected the dedicated AD edition, measured evidence and solver reading.')
