# 求積：狭いピーク・相殺・端点・誤差推定の盲点

Gauss次数と適応公差を走査し、狭いLorentzピーク、平方根端点、巨大な相殺、零積分、見逃すcompact bumpを解析積分とQUADPACKで検証します。

**使用手法**

- [Gauss求積・適応積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja) (`quadrature`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja#quadrature-conditioning-ja-algorithm)

Golub–Welschの節点・重みと、局所差/15を用いる適応Simpsonを実装します。端点ではx=t²変換を別対照とし、狭いbumpには既知支持区間を分割した対照を用意します。これは一般的な自動救済機構ではありません。

$$
\kappa_{\rm cancel}=\frac{\int_a^b|f(x)|\,dx}{|\int_a^bf(x)\,dx|}
$$

$$
\int_{c-w}^{c+w}(1-((x-c)/w)^2)^4\,dx=\frac{256w}{315}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![求積：狭いピーク・相殺・端点・誤差推定の盲点：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/quadrature-conditioning.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja) (`quadrature-moments`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja#quadrature-conditioning-ja-validation)

roots_legendre、解析atan積分、2/3、bumpの256w/315、独立QUADPACKを比較します。QUADPACKの状態・推定誤差・評価回数・警告文も保存します。相殺はε_machine×積分絶対量に対応する絶対予算を使います。初期5点が全て零のbumpでは推定誤差0と実誤差約.00813を明示します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

区間[0,1]、Gauss次数8/16/32/64/128、公差10⁻⁵/10⁻⁷/10⁻⁹です。Lorentz幅.1/.03/.01、相殺係数0/2¹²/2²⁴/2³⁶を固定します。零積分の相対条件数は未定義としてnullで保存します。

**編集上の補足**

適応推定値や計算間の一致は任意の被積分関数の厳密誤差上界ではありません。相殺時の絶対誤差と相対誤差、未検出の局所構造、評価予算を分けて記録します。

## 採用した計算法

Golub–Welschの節点・重みと、局所差/15を用いる適応Simpsonを実装します。端点ではx=t²変換を別対照とし、狭いbumpには既知支持区間を分割した対照を用意します。これは一般的な自動救済機構ではありません。

$$
\kappa_{\rm cancel}=\frac{\int_a^b|f(x)|\,dx}{|\int_a^bf(x)\,dx|}
$$

$$
\int_{c-w}^{c+w}(1-((x-c)/w)^2)^4\,dx=\frac{256w}{315}
$$

## 比較・検証

roots_legendre、解析atan積分、2/3、bumpの256w/315、独立QUADPACKを比較します。QUADPACKの状態・推定誤差・評価回数・警告文も保存します。相殺はε_machine×積分絶対量に対応する絶対予算を使います。初期5点が全て零のbumpでは推定誤差0と実誤差約.00813を明示します。

## 確認の限界

Simpsonの推定値は厳密誤差上界ではありません。盲点の検出に合格しても積分精度への合格ではありません。平方根の直接積分は深さ予算で未収束と表示し得ます。任意の振動・特異性の完全な探索や認証付き求積は主張しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "maximum_cancellation_condition": 68719476737.0,
    "blind_bump_actual_error": 0.008126984126984127,
    "blind_bump_reported_error": 0.0,
    "resolved_bump_actual_error": 1.0884418366607918e-12,
    "zero_integral_relative_condition": null
  },
  "checks": {
    "width0.1-reference": true,
    "n8-independent-rule": true,
    "n16-independent-rule": true,
    "n32-independent-rule": true,
    "n64-independent-rule": true,
    "n128-independent-rule": true,
    "width0.1-gauss-refinement": true,
    "width0.1-tol1e-05": true,
    "width0.1-tol1e-07": true,
    "width0.1-tol1e-09": true,
    "width0.03-reference": true,
    "width0.03-gauss-refinement": true,
    "width0.03-tol1e-05": true,
    "width0.03-tol1e-07": true,
    "width0.03-tol1e-09": true,
    "width0.01-reference": true,
    "width0.01-gauss-refinement": true,
    "width0.01-tol1e-05": true,
    "width0.01-tol1e-07": true,
    "width0.01-tol1e-09": true,
    "endpoint-tol1e-05": true,
    "endpoint-tol1e-07": true,
    "endpoint-tol1e-09": true,
    "C0-absolute-error": true,
    "C4096-absolute-error": true,
    "C1.67772e+07-absolute-error": true,
    "C6.87195e+10-absolute-error": true,
    "conditioned-input-perturbation-gain": true,
    "zero-integral-relative-condition-undefined": true,
    "heuristic-blind-spot-explicit": true,
    "known-support-companion-resolves": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- G. H. Golub and J. H. Welsch (1969). Calculation of Gauss Quadrature Rules. https://www.ams.org/journals/mcom/1969-23-106/S0025-5718-69-99647-1/S0025-5718-69-99647-1.pdf; review_level=publisher-search-first-page-and-metadata
- J. N. Lyness (1969). Notes on the Adaptive Simpson Quadrature Routine. https://dl.acm.org/doi/10.1145/321526.321537; review_level=publisher-metadata
- P. Gonnet (2010). Increasing the Reliability of Adaptive Quadrature Using Explicit Interpolants. https://arxiv.org/abs/1006.3962; review_level=primary author paper, abstract and selected introduction/error-estimation text (§3)
二つの近似積分値の差が偶然小さい場合の誤差推定失敗を原文の選択節で確認しました。今回のSimpson対照は教材独自の構成であり、同論文の新積分器を実装したとは呼びません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots

Vary Gauss order and adaptive tolerance on narrow Lorentz peaks, a square-root endpoint, severe cancellation, a zero integral and a deliberately missed compact bump, using analytic integrals and QUADPACK.

**Methods used**

- [Gaussian and adaptive quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en) (`quadrature`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en#quadrature-conditioning-en-algorithm)

Implement Golub–Welsch nodes/weights and adaptive Simpson with a local difference/15 estimate. Companion checks use x=t² for the endpoint and a known-support split for the narrow bump; these are not general automatic rescue mechanisms.

$$
\kappa_{\rm cancel}=\frac{\int_a^b|f(x)|\,dx}{|\int_a^bf(x)\,dx|}
$$

$$
\int_{c-w}^{c+w}(1-((x-c)/w)^2)^4\,dx=\frac{256w}{315}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/quadrature-conditioning.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en) (`quadrature-moments`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en#quadrature-conditioning-en-validation)

Compare roots_legendre, analytic atan integrals,2/3,the bump integral256w/315 and independent QUADPACK. Preserve QUADPACK status, estimated error, evaluation count and warning message. Cancellation uses a roundoff-aware absolute budget. When all initial five bump samples vanish, expose estimated error0 versus actual error about.00813.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

Use[0,1], Gauss orders8/16/32/64/128 and tolerances10⁻⁵/10⁻⁷/10⁻⁹. Lorentz widths are.1/.03/.01; cancellation scales are0/2¹²/2²⁴/2³⁶. A zero integral has undefined relative condition, stored as null.

**Editorial clarification**

An adaptive estimate or agreement between calculations is not a rigorous error bound for arbitrary integrands. Distinguish absolute and relative error under cancellation, unresolved local structure and evaluation budgets.

## Adopted numerical method

Implement Golub–Welsch nodes/weights and adaptive Simpson with a local difference/15 estimate. Companion checks use x=t² for the endpoint and a known-support split for the narrow bump; these are not general automatic rescue mechanisms.

$$
\kappa_{\rm cancel}=\frac{\int_a^b|f(x)|\,dx}{|\int_a^bf(x)\,dx|}
$$

$$
\int_{c-w}^{c+w}(1-((x-c)/w)^2)^4\,dx=\frac{256w}{315}
$$

## References and validation

Compare roots_legendre, analytic atan integrals,2/3,the bump integral256w/315 and independent QUADPACK. Preserve QUADPACK status, estimated error, evaluation count and warning message. Cancellation uses a roundoff-aware absolute budget. When all initial five bump samples vanish, expose estimated error0 versus actual error about.00813.

## Limits

The Simpson estimate is not a certified error bound. Passing the blind-spot control does not mean accurate integration. Direct square-root integration may honestly terminate at its depth budget. Exhaustive oscillatory/singular exploration and certified quadrature are not claimed.

## Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_cancellation_condition": 68719476737.0,
    "blind_bump_actual_error": 0.008126984126984127,
    "blind_bump_reported_error": 0.0,
    "resolved_bump_actual_error": 1.0884418366607918e-12,
    "zero_integral_relative_condition": null
  },
  "checks": {
    "width0.1-reference": true,
    "n8-independent-rule": true,
    "n16-independent-rule": true,
    "n32-independent-rule": true,
    "n64-independent-rule": true,
    "n128-independent-rule": true,
    "width0.1-gauss-refinement": true,
    "width0.1-tol1e-05": true,
    "width0.1-tol1e-07": true,
    "width0.1-tol1e-09": true,
    "width0.03-reference": true,
    "width0.03-gauss-refinement": true,
    "width0.03-tol1e-05": true,
    "width0.03-tol1e-07": true,
    "width0.03-tol1e-09": true,
    "width0.01-reference": true,
    "width0.01-gauss-refinement": true,
    "width0.01-tol1e-05": true,
    "width0.01-tol1e-07": true,
    "width0.01-tol1e-09": true,
    "endpoint-tol1e-05": true,
    "endpoint-tol1e-07": true,
    "endpoint-tol1e-09": true,
    "C0-absolute-error": true,
    "C4096-absolute-error": true,
    "C1.67772e+07-absolute-error": true,
    "C6.87195e+10-absolute-error": true,
    "conditioned-input-perturbation-gain": true,
    "zero-integral-relative-condition-undefined": true,
    "heuristic-blind-spot-explicit": true,
    "known-support-companion-resolves": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- G. H. Golub and J. H. Welsch (1969). Calculation of Gauss Quadrature Rules. https://www.ams.org/journals/mcom/1969-23-106/S0025-5718-69-99647-1/S0025-5718-69-99647-1.pdf; review_level=publisher-search-first-page-and-metadata
- J. N. Lyness (1969). Notes on the Adaptive Simpson Quadrature Routine. https://dl.acm.org/doi/10.1145/321526.321537; review_level=publisher-metadata
- P. Gonnet (2010). Increasing the Reliability of Adaptive Quadrature Using Explicit Interpolants. https://arxiv.org/abs/1006.3962; review_level=primary author paper, abstract and selected introduction/error-estimation text (§3)
Checked selected original discussion of accidentally small differences between quadrature estimates. The educational Simpson counterexample is original test design, not an implementation of the paper’s new integrators.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
