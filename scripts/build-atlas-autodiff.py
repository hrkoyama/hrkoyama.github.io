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
adjoint = next(m for m in methods if m['id'] == 'adjoint')
sensitivity_release = ROOT / adjoint['sensitivity_release']['base'].lstrip('/')
for extension in ('json', 'png'):
    shutil.copyfile(sensitivity_release / f'docs/figures/bratu-sensitivity.{extension}',
                    ATLAS / f'assets/bratu-sensitivity.{extension}')
inverse = next(m for m in methods if m['id'] == 'optimization')
inverse_release = ROOT / inverse['inverse_release']['base'].lstrip('/')
for extension in ('json', 'png'):
    shutil.copyfile(inverse_release / f'docs/figures/bratu-inverse.{extension}',
                    ATLAS / f'assets/bratu-inverse.{extension}')
multi_release = ROOT / inverse['multi_inverse_release']['base'].lstrip('/')
for extension in ('json', 'png'):
    shutil.copyfile(multi_release / f'docs/figures/bratu-multinverse.{extension}',
                    ATLAS / f'assets/bratu-multinverse.{extension}')

start, end = '<!-- autodiff-foundation -->', '<!-- /autodiff-foundation -->'
for lang in ('en', 'ja'):
    label = '共通基盤：自動微分とBratuの検証' if lang == 'ja' else 'Shared foundation: automatic differentiation and Bratu verification'
    detail = ('同じ残差・初期値・Newton停止条件で解析微分・有限差分・前進モード自動微分を比較します。微分誤差・非線形残差・空間離散化誤差を分け、専用コード・8件のテスト・再生成手順を公開しています。陰関数微分と離散随伴は、別のBratuパラメータ感度の章で検証します。逆モード自動微分エンジンは未実装です。'
              if lang == 'ja' else
              'Compare analytic, finite-difference and forward-mode AD with the same residual, initial state and Newton stopping controls. Derivative error, nonlinear residual and spatial discretization error are reported separately, with dedicated code, eight tests and reproduction commands. A separate Bratu parameter-sensitivity chapter verifies implicit differentiation and discrete adjoints. A reverse-mode AD engine remains unimplemented.')
    sensitivity_label = '陰関数微分・随伴法とBratuのパラメータ感度' if lang == 'ja' else 'Implicit differentiation, adjoints and Bratu parameter sensitivity'
    inverse_label = 'Bratuの逆問題：合成観測から随伴勾配でλを推定する' if lang == 'ja' else 'Bratu inverse problem: estimate lambda from synthetic observations with adjoint gradients'
    multi_label = '複数パラメータの推定・正則化・識別可能性' if lang == 'ja' else 'Multiple parameters, regularization and identifiability'
    note = start + '<aside class="resource-summary"><p><a href="/numerical-methods-atlas/' + lang + '/read/automatic-differentiation/">' + label + '</a></p><p>' + detail + '</p><p><a href="/numerical-methods-atlas/' + lang + '/read/adjoint/">' + sensitivity_label + '</a></p><p><a href="/numerical-methods-atlas/' + lang + '/read/bratu-inverse/">' + inverse_label + '</a></p><p><a href="/numerical-methods-atlas/' + lang + '/read/bratu-multi-inverse/">' + multi_label + '</a></p></aside>' + end
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
