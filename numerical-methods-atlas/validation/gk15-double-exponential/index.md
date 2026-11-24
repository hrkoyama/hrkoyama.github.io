# G7/K15と有限区間tanh-sinh

9本の適応GKと24本の固定DE和を比較します。

**使用手法**

- [Gauss求積・適応積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja) (`quadrature`)
- [Gauss–Kronrod G7/K15](https://hrkoyama.github.io/numerical-methods-atlas/methods/gauss-kronrod/?lang=ja) (`gauss-kronrod`)
- [tanh–sinh二重指数求積](https://hrkoyama.github.io/numerical-methods-atlas/methods/tanh-sinh/?lang=ja) (`tanh-sinh`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja#gk15-double-exponential-ja-algorithm)

共有15節点、G7次数13/K15次数23。DEは安定log式と全端点重みです。

- [有限・無限・多変数の定積分](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#definite-integrals-ja) (`definite-integrals`)

exp(x)、x^(-1/3)、−log(x)を[0,1]で積分。h=1/2〜1/16、切断T=3/4。


**問題の図**

![G7/K15と有限区間tanh-sinh：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=ja) (`gk15-double-exponential`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja#gk15-double-exponential-ja-validation)

解析区間参照で全誤差、連続tail、有限窓誤差を分離します。

- [G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gk15-double-exponential-ja) (`gk15-double-exponential`; 同じ問題の参照 · 解析参照)

半無限exp-sinh/全実線sinh-sinhは未実装。無限台形SUMの省略項のboundは提供しません。
## 前提・単位・境界

exp(x)、x^(-1/3)、−log(x)を[0,1]で積分。h=1/2〜1/16、切断T=3/4。

**編集上の補足**

半無限exp-sinh/全実線sinh-sinhは未実装。無限台形SUMの省略項のboundは提供しません。 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成26件・未達7件・計算不能0件です。FALSE/NAと失敗rawを保持します。

## 採用した計算法

共有15節点、G7次数13/K15次数23。DEは安定log式と全端点重みです。

## 比較・検証

解析区間参照で全誤差、連続tail、有限窓誤差を分離します。

## 確認の限界

半無限exp-sinh/全実線sinh-sinhは未実装。無限台形SUMの省略項のboundは提供しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "records": 33,
    "integrand_evaluations": 5619,
    "accuracy_goals_met": 26,
    "accuracy_goals_unmet": 7,
    "accuracy_goals_unresolved": 0,
    "estimated_converged_rows": 28
  },
  "checks": {
    "q79:smooth-exponential:gk:a0:callback-ledger": true,
    "q79:smooth-exponential:gk:a0:evaluation-cap": true,
    "q79:smooth-exponential:gk:a0:finite-return": true,
    "q79:smooth-exponential:gk:a0:panel-call-identity": true,
    "q79:smooth-exponential:gk:a0:panel-caps": true,
    "q79:smooth-exponential:gk:a0:success-accuracy-or-explicit-budget": true,
    "q79:smooth-exponential:gk:a1:callback-ledger": true,
    "q79:smooth-exponential:gk:a1:evaluation-cap": true,
    "q79:smooth-exponential:gk:a1:finite-return": true,
    "q79:smooth-exponential:gk:a1:panel-call-identity": true,
    "q79:smooth-exponential:gk:a1:panel-caps": true,
    "q79:smooth-exponential:gk:a1:success-accuracy-or-explicit-budget": true,
    "q79:smooth-exponential:gk:a2:callback-ledger": true,
    "q79:smooth-exponential:gk:a2:evaluation-cap": true,
    "q79:smooth-exponential:gk:a2:finite-return": true,
    "q79:smooth-exponential:gk:a2:panel-call-identity": true,
    "q79:smooth-exponential:gk:a2:panel-caps": true,
    "q79:smooth-exponential:gk:a2:success-accuracy-or-explicit-budget": true,
    "q79:smooth-exponential:de:T3:h0:callback-ledger": true,
    "q79:smooth-exponential:de:T3:h0:evaluation-cap": true,
    "q79:smooth-exponential:de:T3:h0:finite-return": true,
    "q79:smooth-exponential:de:T3:h0:fixed-sample-count": true,
    "q79:smooth-exponential:de:T3:h1:callback-ledger": true,
    "q79:smooth-exponential:de:T3:h1:evaluation-cap": true,
    "q79:smooth-exponential:de:T3:h1:finite-return": true,
    "q79:smooth-exponential:de:T3:h1:fixed-sample-count": true,
    "q79:smooth-exponential:de:T3:h2:callback-ledger": true,
    "q79:smooth-exponential:de:T3:h2:evaluation-cap": true,
    "q79:smooth-exponential:de:T3:h2:finite-return": true,
    "q79:smooth-exponential:de:T3:h2:fixed-sample-count": true,
    "q79:smooth-exponential:de:T3:h3:callback-ledger": true,
    "q79:smooth-exponential:de:T3:h3:evaluation-cap": true,
    "q79:smooth-exponential:de:T3:h3:finite-return": true,
    "q79:smooth-exponential:de:T3:h3:fixed-sample-count": true,
    "q79:smooth-exponential:de:T4:h0:callback-ledger": true,
    "q79:smooth-exponential:de:T4:h0:evaluation-cap": true,
    "q79:smooth-exponential:de:T4:h0:finite-return": true,
    "q79:smooth-exponential:de:T4:h0:fixed-sample-count": true,
    "q79:smooth-exponential:de:T4:h1:callback-ledger": true,
    "q79:smooth-exponential:de:T4:h1:evaluation-cap": true,
    "q79:smooth-exponential:de:T4:h1:finite-return": true,
    "q79:smooth-exponential:de:T4:h1:fixed-sample-count": true,
    "q79:smooth-exponential:de:T4:h2:callback-ledger": true,
    "q79:smooth-exponential:de:T4:h2:evaluation-cap": true,
    "q79:smooth-exponential:de:T4:h2:finite-return": true,
    "q79:smooth-exponential:de:T4:h2:fixed-sample-count": true,
    "q79:smooth-exponential:de:T4:h3:callback-ledger": true,
    "q79:smooth-exponential:de:T4:h3:evaluation-cap": true,
    "q79:smooth-exponential:de:T4:h3:finite-return": true,
    "q79:smooth-exponential:de:T4:h3:fixed-sample-count": true,
    "q79:smooth-exponential:de:T4:h3:required-finest-accuracy": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:finite-return": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:panel-call-identity": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:panel-caps": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:success-accuracy-or-explicit-budget": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:finite-return": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:panel-call-identity": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:panel-caps": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:success-accuracy-or-explicit-budget": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:finite-return": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:panel-call-identity": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:panel-caps": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:success-accuracy-or-explicit-budget": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h0:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h0:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h0:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h0:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h1:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h1:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h1:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h1:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h2:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h2:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h2:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h2:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h3:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h3:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h3:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h3:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h0:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h0:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h0:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h0:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h1:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h1:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h1:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h1:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h2:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h2:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h2:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h2:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h3:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h3:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h3:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h3:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h3:required-finest-accuracy": true,
    "q79:log-endpoint:gk:a0:callback-ledger": true,
    "q79:log-endpoint:gk:a0:evaluation-cap": true,
    "q79:log-endpoint:gk:a0:finite-return": true,
    "q79:log-endpoint:gk:a0:panel-call-identity": true,
    "q79:log-endpoint:gk:a0:panel-caps": true,
    "q79:log-endpoint:gk:a0:success-accuracy-or-explicit-budget": true,
    "q79:log-endpoint:gk:a1:callback-ledger": true,
    "q79:log-endpoint:gk:a1:evaluation-cap": true,
    "q79:log-endpoint:gk:a1:finite-return": true,
    "q79:log-endpoint:gk:a1:panel-call-identity": true,
    "q79:log-endpoint:gk:a1:panel-caps": true,
    "q79:log-endpoint:gk:a1:success-accuracy-or-explicit-budget": true,
    "q79:log-endpoint:gk:a2:callback-ledger": true,
    "q79:log-endpoint:gk:a2:evaluation-cap": true,
    "q79:log-endpoint:gk:a2:finite-return": true,
    "q79:log-endpoint:gk:a2:panel-call-identity": true,
    "q79:log-endpoint:gk:a2:panel-caps": true,
    "q79:log-endpoint:gk:a2:success-accuracy-or-explicit-budget": true,
    "q79:log-endpoint:de:T3:h0:callback-ledger": true,
    "q79:log-endpoint:de:T3:h0:evaluation-cap": true,
    "q79:log-endpoint:de:T3:h0:finite-return": true,
    "q79:log-endpoint:de:T3:h0:fixed-sample-count": true,
    "q79:log-endpoint:de:T3:h1:callback-ledger": true,
    "q79:log-endpoint:de:T3:h1:evaluation-cap": true,
    "q79:log-endpoint:de:T3:h1:finite-return": true,
    "q79:log-endpoint:de:T3:h1:fixed-sample-count": true,
    "q79:log-endpoint:de:T3:h2:callback-ledger": true,
    "q79:log-endpoint:de:T3:h2:evaluation-cap": true,
    "q79:log-endpoint:de:T3:h2:finite-return": true,
    "q79:log-endpoint:de:T3:h2:fixed-sample-count": true,
    "q79:log-endpoint:de:T3:h3:callback-ledger": true,
    "q79:log-endpoint:de:T3:h3:evaluation-cap": true,
    "q79:log-endpoint:de:T3:h3:finite-return": true,
    "q79:log-endpoint:de:T3:h3:fixed-sample-count": true,
    "q79:log-endpoint:de:T4:h0:callback-ledger": true,
    "q79:log-endpoint:de:T4:h0:evaluation-cap": true,
    "q79:log-endpoint:de:T4:h0:finite-return": true,
    "q79:log-endpoint:de:T4:h0:fixed-sample-count": true,
    "q79:log-endpoint:de:T4:h1:callback-ledger": true,
    "q79:log-endpoint:de:T4:h1:evaluation-cap": true,
    "q79:log-endpoint:de:T4:h1:finite-return": true,
    "q79:log-endpoint:de:T4:h1:fixed-sample-count": true,
    "q79:log-endpoint:de:T4:h2:callback-ledger": true,
    "q79:log-endpoint:de:T4:h2:evaluation-cap": true,
    "q79:log-endpoint:de:T4:h2:finite-return": true,
    "q79:log-endpoint:de:T4:h2:fixed-sample-count": true,
    "q79:log-endpoint:de:T4:h3:callback-ledger": true,
    "q79:log-endpoint:de:T4:h3:evaluation-cap": true,
    "q79:log-endpoint:de:T4:h3:finite-return": true,
    "q79:log-endpoint:de:T4:h3:fixed-sample-count": true,
    "q79:log-endpoint:de:T4:h3:required-finest-accuracy": true,
    "gk15-double-exponential:fixed-record-count": true,
    "gk15-double-exponential:unique-record-ids": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/index.json

![保存された変換関数と有限窓誤差（連続tailは別量）](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential-preview.png)

保存された変換関数と有限窓誤差（連続tailは別量）

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Pinned SciPy1.14.1 bundled dqk15 [accessed 2026-11-25]. https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/integrate/quadpack/dqk15.f; review_level=primary-software-source
- Double Exponential Formulas for Numerical Integration [accessed 2026-11-25]. https://ems.press/doi/pdf/10.2977/prims/1195192451; review_level=selected-primary-body-text

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# G7/K15 and finite-interval tanh-sinh

Nine adaptive GK rows and twenty-four fixed DE sums are compared.

**Methods used**

- [Gaussian and adaptive quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en) (`quadrature`)
- [Gauss–Kronrod G7/K15](https://hrkoyama.github.io/numerical-methods-atlas/methods/gauss-kronrod/?lang=en) (`gauss-kronrod`)
- [Tanh–sinh double-exponential quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/tanh-sinh/?lang=en) (`tanh-sinh`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en#gk15-double-exponential-en-algorithm)

Shared15-node G7 degree13/K15 degree23; DE uses stable logarithmic products and full endpoint weights.

- [Finite, improper and multivariate definite integrals](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#definite-integrals-en) (`definite-integrals`)

Integrate exp(x), x^(-1/3) and -log(x) on[0,1], with h from1/2 to1/16 and cutoffs3/4.


**Problem figure**

![G7/K15 and finite-interval tanh-sinh: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en) (`gk15-double-exponential`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en#gk15-double-exponential-en-validation)

Analytic interval references separate total error, continuous tail and finite-window defect.

- [G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gk15-double-exponential-en) (`gk15-double-exponential`; Same-problem reference · Analytic reference)

Half-line exp-sinh and whole-line sinh-sinh are unimplemented; no omitted infinite-grid sum bound is provided.
## Assumptions, units and boundaries

Integrate exp(x), x^(-1/3) and -log(x) on[0,1], with h from1/2 to1/16 and cutoffs3/4.

**Editorial clarification**

Half-line exp-sinh and whole-line sinh-sinh are unimplemented; no omitted infinite-grid sum bound is provided. The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 26 met, 7 unmet and 0 not computable. False/NA outcomes and raw failures are retained.

## Adopted numerical method

Shared15-node G7 degree13/K15 degree23; DE uses stable logarithmic products and full endpoint weights.

## References and validation

Analytic interval references separate total error, continuous tail and finite-window defect.

## Limits

Half-line exp-sinh and whole-line sinh-sinh are unimplemented; no omitted infinite-grid sum bound is provided.

## Stored measurements and decisions

```json
{
  "metrics": {
    "records": 33,
    "integrand_evaluations": 5619,
    "accuracy_goals_met": 26,
    "accuracy_goals_unmet": 7,
    "accuracy_goals_unresolved": 0,
    "estimated_converged_rows": 28
  },
  "checks": {
    "q79:smooth-exponential:gk:a0:callback-ledger": true,
    "q79:smooth-exponential:gk:a0:evaluation-cap": true,
    "q79:smooth-exponential:gk:a0:finite-return": true,
    "q79:smooth-exponential:gk:a0:panel-call-identity": true,
    "q79:smooth-exponential:gk:a0:panel-caps": true,
    "q79:smooth-exponential:gk:a0:success-accuracy-or-explicit-budget": true,
    "q79:smooth-exponential:gk:a1:callback-ledger": true,
    "q79:smooth-exponential:gk:a1:evaluation-cap": true,
    "q79:smooth-exponential:gk:a1:finite-return": true,
    "q79:smooth-exponential:gk:a1:panel-call-identity": true,
    "q79:smooth-exponential:gk:a1:panel-caps": true,
    "q79:smooth-exponential:gk:a1:success-accuracy-or-explicit-budget": true,
    "q79:smooth-exponential:gk:a2:callback-ledger": true,
    "q79:smooth-exponential:gk:a2:evaluation-cap": true,
    "q79:smooth-exponential:gk:a2:finite-return": true,
    "q79:smooth-exponential:gk:a2:panel-call-identity": true,
    "q79:smooth-exponential:gk:a2:panel-caps": true,
    "q79:smooth-exponential:gk:a2:success-accuracy-or-explicit-budget": true,
    "q79:smooth-exponential:de:T3:h0:callback-ledger": true,
    "q79:smooth-exponential:de:T3:h0:evaluation-cap": true,
    "q79:smooth-exponential:de:T3:h0:finite-return": true,
    "q79:smooth-exponential:de:T3:h0:fixed-sample-count": true,
    "q79:smooth-exponential:de:T3:h1:callback-ledger": true,
    "q79:smooth-exponential:de:T3:h1:evaluation-cap": true,
    "q79:smooth-exponential:de:T3:h1:finite-return": true,
    "q79:smooth-exponential:de:T3:h1:fixed-sample-count": true,
    "q79:smooth-exponential:de:T3:h2:callback-ledger": true,
    "q79:smooth-exponential:de:T3:h2:evaluation-cap": true,
    "q79:smooth-exponential:de:T3:h2:finite-return": true,
    "q79:smooth-exponential:de:T3:h2:fixed-sample-count": true,
    "q79:smooth-exponential:de:T3:h3:callback-ledger": true,
    "q79:smooth-exponential:de:T3:h3:evaluation-cap": true,
    "q79:smooth-exponential:de:T3:h3:finite-return": true,
    "q79:smooth-exponential:de:T3:h3:fixed-sample-count": true,
    "q79:smooth-exponential:de:T4:h0:callback-ledger": true,
    "q79:smooth-exponential:de:T4:h0:evaluation-cap": true,
    "q79:smooth-exponential:de:T4:h0:finite-return": true,
    "q79:smooth-exponential:de:T4:h0:fixed-sample-count": true,
    "q79:smooth-exponential:de:T4:h1:callback-ledger": true,
    "q79:smooth-exponential:de:T4:h1:evaluation-cap": true,
    "q79:smooth-exponential:de:T4:h1:finite-return": true,
    "q79:smooth-exponential:de:T4:h1:fixed-sample-count": true,
    "q79:smooth-exponential:de:T4:h2:callback-ledger": true,
    "q79:smooth-exponential:de:T4:h2:evaluation-cap": true,
    "q79:smooth-exponential:de:T4:h2:finite-return": true,
    "q79:smooth-exponential:de:T4:h2:fixed-sample-count": true,
    "q79:smooth-exponential:de:T4:h3:callback-ledger": true,
    "q79:smooth-exponential:de:T4:h3:evaluation-cap": true,
    "q79:smooth-exponential:de:T4:h3:finite-return": true,
    "q79:smooth-exponential:de:T4:h3:fixed-sample-count": true,
    "q79:smooth-exponential:de:T4:h3:required-finest-accuracy": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:finite-return": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:panel-call-identity": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:panel-caps": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:success-accuracy-or-explicit-budget": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:finite-return": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:panel-call-identity": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:panel-caps": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:success-accuracy-or-explicit-budget": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:finite-return": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:panel-call-identity": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:panel-caps": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:success-accuracy-or-explicit-budget": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h0:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h0:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h0:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h0:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h1:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h1:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h1:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h1:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h2:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h2:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h2:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h2:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h3:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h3:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h3:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h3:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h0:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h0:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h0:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h0:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h1:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h1:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h1:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h1:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h2:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h2:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h2:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h2:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h3:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h3:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h3:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h3:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h3:required-finest-accuracy": true,
    "q79:log-endpoint:gk:a0:callback-ledger": true,
    "q79:log-endpoint:gk:a0:evaluation-cap": true,
    "q79:log-endpoint:gk:a0:finite-return": true,
    "q79:log-endpoint:gk:a0:panel-call-identity": true,
    "q79:log-endpoint:gk:a0:panel-caps": true,
    "q79:log-endpoint:gk:a0:success-accuracy-or-explicit-budget": true,
    "q79:log-endpoint:gk:a1:callback-ledger": true,
    "q79:log-endpoint:gk:a1:evaluation-cap": true,
    "q79:log-endpoint:gk:a1:finite-return": true,
    "q79:log-endpoint:gk:a1:panel-call-identity": true,
    "q79:log-endpoint:gk:a1:panel-caps": true,
    "q79:log-endpoint:gk:a1:success-accuracy-or-explicit-budget": true,
    "q79:log-endpoint:gk:a2:callback-ledger": true,
    "q79:log-endpoint:gk:a2:evaluation-cap": true,
    "q79:log-endpoint:gk:a2:finite-return": true,
    "q79:log-endpoint:gk:a2:panel-call-identity": true,
    "q79:log-endpoint:gk:a2:panel-caps": true,
    "q79:log-endpoint:gk:a2:success-accuracy-or-explicit-budget": true,
    "q79:log-endpoint:de:T3:h0:callback-ledger": true,
    "q79:log-endpoint:de:T3:h0:evaluation-cap": true,
    "q79:log-endpoint:de:T3:h0:finite-return": true,
    "q79:log-endpoint:de:T3:h0:fixed-sample-count": true,
    "q79:log-endpoint:de:T3:h1:callback-ledger": true,
    "q79:log-endpoint:de:T3:h1:evaluation-cap": true,
    "q79:log-endpoint:de:T3:h1:finite-return": true,
    "q79:log-endpoint:de:T3:h1:fixed-sample-count": true,
    "q79:log-endpoint:de:T3:h2:callback-ledger": true,
    "q79:log-endpoint:de:T3:h2:evaluation-cap": true,
    "q79:log-endpoint:de:T3:h2:finite-return": true,
    "q79:log-endpoint:de:T3:h2:fixed-sample-count": true,
    "q79:log-endpoint:de:T3:h3:callback-ledger": true,
    "q79:log-endpoint:de:T3:h3:evaluation-cap": true,
    "q79:log-endpoint:de:T3:h3:finite-return": true,
    "q79:log-endpoint:de:T3:h3:fixed-sample-count": true,
    "q79:log-endpoint:de:T4:h0:callback-ledger": true,
    "q79:log-endpoint:de:T4:h0:evaluation-cap": true,
    "q79:log-endpoint:de:T4:h0:finite-return": true,
    "q79:log-endpoint:de:T4:h0:fixed-sample-count": true,
    "q79:log-endpoint:de:T4:h1:callback-ledger": true,
    "q79:log-endpoint:de:T4:h1:evaluation-cap": true,
    "q79:log-endpoint:de:T4:h1:finite-return": true,
    "q79:log-endpoint:de:T4:h1:fixed-sample-count": true,
    "q79:log-endpoint:de:T4:h2:callback-ledger": true,
    "q79:log-endpoint:de:T4:h2:evaluation-cap": true,
    "q79:log-endpoint:de:T4:h2:finite-return": true,
    "q79:log-endpoint:de:T4:h2:fixed-sample-count": true,
    "q79:log-endpoint:de:T4:h3:callback-ledger": true,
    "q79:log-endpoint:de:T4:h3:evaluation-cap": true,
    "q79:log-endpoint:de:T4:h3:finite-return": true,
    "q79:log-endpoint:de:T4:h3:fixed-sample-count": true,
    "q79:log-endpoint:de:T4:h3:required-finest-accuracy": true,
    "gk15-double-exponential:fixed-record-count": true,
    "gk15-double-exponential:unique-record-ids": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/index.json

![Saved transformed integrands and finite-window defects; continuous tails are distinct](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential-preview.png)

Saved transformed integrands and finite-window defects; continuous tails are distinct

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Pinned SciPy1.14.1 bundled dqk15 [accessed 2026-11-25]. https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/integrate/quadpack/dqk15.f; review_level=primary-software-source
- Double Exponential Formulas for Numerical Integration [accessed 2026-11-25]. https://ems.press/doi/pdf/10.2977/prims/1195192451; review_level=selected-primary-body-text

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
