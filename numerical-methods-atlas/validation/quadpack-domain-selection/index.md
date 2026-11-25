# 領域別QUADPACKと有限Simpson対照

15本の特殊化求積と15本のSimpson対照を固定入力で比較します。

**使用手法**

- [Gauss求積・適応積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja) (`quadrature`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=ja#quadpack-domain-selection-ja-algorithm)

領域と重みを明示しfull_outputの活動prefixを保持。既存Simpson関数は不変。

- [有限・無限・多変数の定積分](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#definite-integrals-ja) (`definite-integrals`)

無限Gaussian、有限振動2周波数、半無限Fourier、内部特異点。絶対公差1e-6/1e-8/1e-10、epsrel=0。


**問題の図**

![領域別QUADPACKと有限Simpson対照：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[領域別QUADPACKと有限Simpson対照](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=ja) (`quadpack-domain-selection`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=ja#quadpack-domain-selection-ja-validation)

独立の解析区間参照と実callback数を照合します。有限Gaussianは点値でなく厳密区間です。

- [領域別QUADPACKと有限Simpson対照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-quadpack-domain-selection-ja) (`quadpack-domain-selection`; 同じ問題の参照 · 解析参照)

Simpsonの特異節点失敗と未達精度を保存し、推定誤差の一般保証にしません。
## 前提・単位・境界

無限Gaussian、有限振動2周波数、半無限Fourier、内部特異点。絶対公差1e-6/1e-8/1e-10、epsrel=0。

**編集上の補足**

Simpsonの特異節点失敗と未達精度を保存し、推定誤差の一般保証にしません。 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成25件・未達2件・計算不能3件です。FALSE/NAと失敗rawを保持します。

## 採用した計算法

領域と重みを明示しfull_outputの活動prefixを保持。既存Simpson関数は不変。

$$
I=\int_\Omega f(x)\,dx
$$

## 比較・検証

独立の解析区間参照と実callback数を照合します。有限Gaussianは点値でなく厳密区間です。

## 確認の限界

Simpsonの特異節点失敗と未達精度を保存し、推定誤差の一般保証にしません。

## 保存実測値と判定

```json
{
  "metrics": {
    "records": 30,
    "integrand_evaluations": 34351,
    "accuracy_goals_met": 25,
    "accuracy_goals_unmet": 2,
    "accuracy_goals_unresolved": 3,
    "estimated_converged_rows": 26
  },
  "checks": {
    "q78:gaussian-whole-line:specialized-quadpack:a0:callback-ledger": true,
    "q78:gaussian-whole-line:specialized-quadpack:a0:finite-return": true,
    "q78:gaussian-whole-line:specialized-quadpack:a0:native-success": true,
    "q78:gaussian-whole-line:specialized-quadpack:a0:required-analytic-accuracy": true,
    "q78:gaussian-whole-line:specialized-quadpack:a0:absolute-series": true,
    "q78:gaussian-whole-line:specialized-quadpack:a1:callback-ledger": true,
    "q78:gaussian-whole-line:specialized-quadpack:a1:finite-return": true,
    "q78:gaussian-whole-line:specialized-quadpack:a1:native-success": true,
    "q78:gaussian-whole-line:specialized-quadpack:a1:required-analytic-accuracy": true,
    "q78:gaussian-whole-line:specialized-quadpack:a1:absolute-series": true,
    "q78:gaussian-whole-line:specialized-quadpack:a2:callback-ledger": true,
    "q78:gaussian-whole-line:specialized-quadpack:a2:finite-return": true,
    "q78:gaussian-whole-line:specialized-quadpack:a2:native-success": true,
    "q78:gaussian-whole-line:specialized-quadpack:a2:required-analytic-accuracy": true,
    "q78:gaussian-whole-line:specialized-quadpack:a2:absolute-series": true,
    "q78:gaussian-whole-line:simpson-companion:a0:callback-ledger": true,
    "q78:gaussian-whole-line:simpson-companion:a0:evaluation-cap": true,
    "q78:gaussian-whole-line:simpson-companion:a0:finite-return": true,
    "q78:gaussian-whole-line:simpson-companion:a0:native-status": true,
    "q78:gaussian-whole-line:simpson-companion:a1:callback-ledger": true,
    "q78:gaussian-whole-line:simpson-companion:a1:evaluation-cap": true,
    "q78:gaussian-whole-line:simpson-companion:a1:finite-return": true,
    "q78:gaussian-whole-line:simpson-companion:a1:native-status": true,
    "q78:gaussian-whole-line:simpson-companion:a2:callback-ledger": true,
    "q78:gaussian-whole-line:simpson-companion:a2:evaluation-cap": true,
    "q78:gaussian-whole-line:simpson-companion:a2:finite-return": true,
    "q78:gaussian-whole-line:simpson-companion:a2:native-status": true,
    "q78:finite-sine-40:specialized-quadpack:a0:callback-ledger": true,
    "q78:finite-sine-40:specialized-quadpack:a0:finite-return": true,
    "q78:finite-sine-40:specialized-quadpack:a0:native-success": true,
    "q78:finite-sine-40:specialized-quadpack:a0:required-analytic-accuracy": true,
    "q78:finite-sine-40:specialized-quadpack:a0:absolute-series": true,
    "q78:finite-sine-40:specialized-quadpack:a1:callback-ledger": true,
    "q78:finite-sine-40:specialized-quadpack:a1:finite-return": true,
    "q78:finite-sine-40:specialized-quadpack:a1:native-success": true,
    "q78:finite-sine-40:specialized-quadpack:a1:required-analytic-accuracy": true,
    "q78:finite-sine-40:specialized-quadpack:a1:absolute-series": true,
    "q78:finite-sine-40:specialized-quadpack:a2:callback-ledger": true,
    "q78:finite-sine-40:specialized-quadpack:a2:finite-return": true,
    "q78:finite-sine-40:specialized-quadpack:a2:native-success": true,
    "q78:finite-sine-40:specialized-quadpack:a2:required-analytic-accuracy": true,
    "q78:finite-sine-40:specialized-quadpack:a2:absolute-series": true,
    "q78:finite-sine-40:simpson-companion:a0:callback-ledger": true,
    "q78:finite-sine-40:simpson-companion:a0:evaluation-cap": true,
    "q78:finite-sine-40:simpson-companion:a0:finite-return": true,
    "q78:finite-sine-40:simpson-companion:a0:native-status": true,
    "q78:finite-sine-40:simpson-companion:a1:callback-ledger": true,
    "q78:finite-sine-40:simpson-companion:a1:evaluation-cap": true,
    "q78:finite-sine-40:simpson-companion:a1:finite-return": true,
    "q78:finite-sine-40:simpson-companion:a1:native-status": true,
    "q78:finite-sine-40:simpson-companion:a2:callback-ledger": true,
    "q78:finite-sine-40:simpson-companion:a2:evaluation-cap": true,
    "q78:finite-sine-40:simpson-companion:a2:finite-return": true,
    "q78:finite-sine-40:simpson-companion:a2:native-status": true,
    "q78:finite-sine-120:specialized-quadpack:a0:callback-ledger": true,
    "q78:finite-sine-120:specialized-quadpack:a0:finite-return": true,
    "q78:finite-sine-120:specialized-quadpack:a0:native-success": true,
    "q78:finite-sine-120:specialized-quadpack:a0:required-analytic-accuracy": true,
    "q78:finite-sine-120:specialized-quadpack:a0:absolute-series": true,
    "q78:finite-sine-120:specialized-quadpack:a1:callback-ledger": true,
    "q78:finite-sine-120:specialized-quadpack:a1:finite-return": true,
    "q78:finite-sine-120:specialized-quadpack:a1:native-success": true,
    "q78:finite-sine-120:specialized-quadpack:a1:required-analytic-accuracy": true,
    "q78:finite-sine-120:specialized-quadpack:a1:absolute-series": true,
    "q78:finite-sine-120:specialized-quadpack:a2:callback-ledger": true,
    "q78:finite-sine-120:specialized-quadpack:a2:finite-return": true,
    "q78:finite-sine-120:specialized-quadpack:a2:native-success": true,
    "q78:finite-sine-120:specialized-quadpack:a2:required-analytic-accuracy": true,
    "q78:finite-sine-120:specialized-quadpack:a2:absolute-series": true,
    "q78:finite-sine-120:simpson-companion:a0:callback-ledger": true,
    "q78:finite-sine-120:simpson-companion:a0:evaluation-cap": true,
    "q78:finite-sine-120:simpson-companion:a0:finite-return": true,
    "q78:finite-sine-120:simpson-companion:a0:native-status": true,
    "q78:finite-sine-120:simpson-companion:a1:callback-ledger": true,
    "q78:finite-sine-120:simpson-companion:a1:evaluation-cap": true,
    "q78:finite-sine-120:simpson-companion:a1:finite-return": true,
    "q78:finite-sine-120:simpson-companion:a1:native-status": true,
    "q78:finite-sine-120:simpson-companion:a2:callback-ledger": true,
    "q78:finite-sine-120:simpson-companion:a2:evaluation-cap": true,
    "q78:finite-sine-120:simpson-companion:a2:finite-return": true,
    "q78:finite-sine-120:simpson-companion:a2:native-status": true,
    "q78:fourier-half-line:specialized-quadpack:a0:callback-ledger": true,
    "q78:fourier-half-line:specialized-quadpack:a0:finite-return": true,
    "q78:fourier-half-line:specialized-quadpack:a0:native-success": true,
    "q78:fourier-half-line:specialized-quadpack:a0:required-analytic-accuracy": true,
    "q78:fourier-half-line:specialized-quadpack:a0:absolute-series": true,
    "q78:fourier-half-line:specialized-quadpack:a1:callback-ledger": true,
    "q78:fourier-half-line:specialized-quadpack:a1:finite-return": true,
    "q78:fourier-half-line:specialized-quadpack:a1:native-success": true,
    "q78:fourier-half-line:specialized-quadpack:a1:required-analytic-accuracy": true,
    "q78:fourier-half-line:specialized-quadpack:a1:absolute-series": true,
    "q78:fourier-half-line:specialized-quadpack:a2:callback-ledger": true,
    "q78:fourier-half-line:specialized-quadpack:a2:finite-return": true,
    "q78:fourier-half-line:specialized-quadpack:a2:native-success": true,
    "q78:fourier-half-line:specialized-quadpack:a2:required-analytic-accuracy": true,
    "q78:fourier-half-line:specialized-quadpack:a2:absolute-series": true,
    "q78:fourier-half-line:simpson-companion:a0:callback-ledger": true,
    "q78:fourier-half-line:simpson-companion:a0:evaluation-cap": true,
    "q78:fourier-half-line:simpson-companion:a0:finite-return": true,
    "q78:fourier-half-line:simpson-companion:a0:native-status": true,
    "q78:fourier-half-line:simpson-companion:a1:callback-ledger": true,
    "q78:fourier-half-line:simpson-companion:a1:evaluation-cap": true,
    "q78:fourier-half-line:simpson-companion:a1:finite-return": true,
    "q78:fourier-half-line:simpson-companion:a1:native-status": true,
    "q78:fourier-half-line:simpson-companion:a2:callback-ledger": true,
    "q78:fourier-half-line:simpson-companion:a2:evaluation-cap": true,
    "q78:fourier-half-line:simpson-companion:a2:finite-return": true,
    "q78:fourier-half-line:simpson-companion:a2:native-status": true,
    "q78:internal-root:specialized-quadpack:a0:callback-ledger": true,
    "q78:internal-root:specialized-quadpack:a0:finite-return": true,
    "q78:internal-root:specialized-quadpack:a0:native-success": true,
    "q78:internal-root:specialized-quadpack:a0:required-analytic-accuracy": true,
    "q78:internal-root:specialized-quadpack:a0:absolute-series": true,
    "q78:internal-root:specialized-quadpack:a1:callback-ledger": true,
    "q78:internal-root:specialized-quadpack:a1:finite-return": true,
    "q78:internal-root:specialized-quadpack:a1:native-success": true,
    "q78:internal-root:specialized-quadpack:a1:required-analytic-accuracy": true,
    "q78:internal-root:specialized-quadpack:a1:absolute-series": true,
    "q78:internal-root:specialized-quadpack:a2:callback-ledger": true,
    "q78:internal-root:specialized-quadpack:a2:finite-return": true,
    "q78:internal-root:specialized-quadpack:a2:native-success": true,
    "q78:internal-root:specialized-quadpack:a2:required-analytic-accuracy": true,
    "q78:internal-root:specialized-quadpack:a2:absolute-series": true,
    "q78:internal-root:simpson-companion:a0:callback-ledger": true,
    "q78:internal-root:simpson-companion:a0:evaluation-cap": true,
    "q78:internal-root:simpson-companion:a0:declared-singular-node": true,
    "q78:internal-root:simpson-companion:a1:callback-ledger": true,
    "q78:internal-root:simpson-companion:a1:evaluation-cap": true,
    "q78:internal-root:simpson-companion:a1:declared-singular-node": true,
    "q78:internal-root:simpson-companion:a2:callback-ledger": true,
    "q78:internal-root:simpson-companion:a2:evaluation-cap": true,
    "q78:internal-root:simpson-companion:a2:declared-singular-node": true,
    "quadpack-domain-selection:fixed-record-count": true,
    "quadpack-domain-selection:unique-record-ids": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/index.json

![活動Fourier周期の保存寄与と誤差・評価数](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection-preview.png)

活動Fourier周期の保存寄与と誤差・評価数

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

- quad: adaptive integration and QUADPACK dispatch [accessed 2026-11-25]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.quad.html; review_level=selected-official-documentation

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# QUADPACK dispatch and finite Simpson companions

Fifteen specialized quadratures and fifteen Simpson companions use fixed inputs.

**Methods used**

- [Gaussian and adaptive quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en) (`quadrature`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=en#quadpack-domain-selection-en-algorithm)

Explicit domain/weight dispatch retains active full_output prefixes. The existing Simpson function is unchanged.

- [Finite, improper and multivariate definite integrals](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#definite-integrals-en) (`definite-integrals`)

Whole-line Gaussian, two finite frequencies, half-line Fourier and an internal singularity; absolute tolerances1e-6/1e-8/1e-10 and epsrel0.


**Problem figure**

![QUADPACK dispatch and finite Simpson companions: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[QUADPACK dispatch and finite Simpson companions](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=en) (`quadpack-domain-selection`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=en#quadpack-domain-selection-en-validation)

Independent analytic interval references and actual callback counts are checked. The finite Gaussian target is an interval, not an invented erf value.

- [QUADPACK dispatch and finite Simpson companions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-quadpack-domain-selection-en) (`quadpack-domain-selection`; Same-problem reference · Analytic reference)

Singular-node failures and unmet Simpson goals remain visible; error estimates are not general guarantees.
## Assumptions, units and boundaries

Whole-line Gaussian, two finite frequencies, half-line Fourier and an internal singularity; absolute tolerances1e-6/1e-8/1e-10 and epsrel0.

**Editorial clarification**

Singular-node failures and unmet Simpson goals remain visible; error estimates are not general guarantees. The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 25 met, 2 unmet and 3 not computable. False/NA outcomes and raw failures are retained.

## Adopted numerical method

Explicit domain/weight dispatch retains active full_output prefixes. The existing Simpson function is unchanged.

$$
I=\int_\Omega f(x)\,dx
$$

## References and validation

Independent analytic interval references and actual callback counts are checked. The finite Gaussian target is an interval, not an invented erf value.

## Limits

Singular-node failures and unmet Simpson goals remain visible; error estimates are not general guarantees.

## Stored measurements and decisions

```json
{
  "metrics": {
    "records": 30,
    "integrand_evaluations": 34351,
    "accuracy_goals_met": 25,
    "accuracy_goals_unmet": 2,
    "accuracy_goals_unresolved": 3,
    "estimated_converged_rows": 26
  },
  "checks": {
    "q78:gaussian-whole-line:specialized-quadpack:a0:callback-ledger": true,
    "q78:gaussian-whole-line:specialized-quadpack:a0:finite-return": true,
    "q78:gaussian-whole-line:specialized-quadpack:a0:native-success": true,
    "q78:gaussian-whole-line:specialized-quadpack:a0:required-analytic-accuracy": true,
    "q78:gaussian-whole-line:specialized-quadpack:a0:absolute-series": true,
    "q78:gaussian-whole-line:specialized-quadpack:a1:callback-ledger": true,
    "q78:gaussian-whole-line:specialized-quadpack:a1:finite-return": true,
    "q78:gaussian-whole-line:specialized-quadpack:a1:native-success": true,
    "q78:gaussian-whole-line:specialized-quadpack:a1:required-analytic-accuracy": true,
    "q78:gaussian-whole-line:specialized-quadpack:a1:absolute-series": true,
    "q78:gaussian-whole-line:specialized-quadpack:a2:callback-ledger": true,
    "q78:gaussian-whole-line:specialized-quadpack:a2:finite-return": true,
    "q78:gaussian-whole-line:specialized-quadpack:a2:native-success": true,
    "q78:gaussian-whole-line:specialized-quadpack:a2:required-analytic-accuracy": true,
    "q78:gaussian-whole-line:specialized-quadpack:a2:absolute-series": true,
    "q78:gaussian-whole-line:simpson-companion:a0:callback-ledger": true,
    "q78:gaussian-whole-line:simpson-companion:a0:evaluation-cap": true,
    "q78:gaussian-whole-line:simpson-companion:a0:finite-return": true,
    "q78:gaussian-whole-line:simpson-companion:a0:native-status": true,
    "q78:gaussian-whole-line:simpson-companion:a1:callback-ledger": true,
    "q78:gaussian-whole-line:simpson-companion:a1:evaluation-cap": true,
    "q78:gaussian-whole-line:simpson-companion:a1:finite-return": true,
    "q78:gaussian-whole-line:simpson-companion:a1:native-status": true,
    "q78:gaussian-whole-line:simpson-companion:a2:callback-ledger": true,
    "q78:gaussian-whole-line:simpson-companion:a2:evaluation-cap": true,
    "q78:gaussian-whole-line:simpson-companion:a2:finite-return": true,
    "q78:gaussian-whole-line:simpson-companion:a2:native-status": true,
    "q78:finite-sine-40:specialized-quadpack:a0:callback-ledger": true,
    "q78:finite-sine-40:specialized-quadpack:a0:finite-return": true,
    "q78:finite-sine-40:specialized-quadpack:a0:native-success": true,
    "q78:finite-sine-40:specialized-quadpack:a0:required-analytic-accuracy": true,
    "q78:finite-sine-40:specialized-quadpack:a0:absolute-series": true,
    "q78:finite-sine-40:specialized-quadpack:a1:callback-ledger": true,
    "q78:finite-sine-40:specialized-quadpack:a1:finite-return": true,
    "q78:finite-sine-40:specialized-quadpack:a1:native-success": true,
    "q78:finite-sine-40:specialized-quadpack:a1:required-analytic-accuracy": true,
    "q78:finite-sine-40:specialized-quadpack:a1:absolute-series": true,
    "q78:finite-sine-40:specialized-quadpack:a2:callback-ledger": true,
    "q78:finite-sine-40:specialized-quadpack:a2:finite-return": true,
    "q78:finite-sine-40:specialized-quadpack:a2:native-success": true,
    "q78:finite-sine-40:specialized-quadpack:a2:required-analytic-accuracy": true,
    "q78:finite-sine-40:specialized-quadpack:a2:absolute-series": true,
    "q78:finite-sine-40:simpson-companion:a0:callback-ledger": true,
    "q78:finite-sine-40:simpson-companion:a0:evaluation-cap": true,
    "q78:finite-sine-40:simpson-companion:a0:finite-return": true,
    "q78:finite-sine-40:simpson-companion:a0:native-status": true,
    "q78:finite-sine-40:simpson-companion:a1:callback-ledger": true,
    "q78:finite-sine-40:simpson-companion:a1:evaluation-cap": true,
    "q78:finite-sine-40:simpson-companion:a1:finite-return": true,
    "q78:finite-sine-40:simpson-companion:a1:native-status": true,
    "q78:finite-sine-40:simpson-companion:a2:callback-ledger": true,
    "q78:finite-sine-40:simpson-companion:a2:evaluation-cap": true,
    "q78:finite-sine-40:simpson-companion:a2:finite-return": true,
    "q78:finite-sine-40:simpson-companion:a2:native-status": true,
    "q78:finite-sine-120:specialized-quadpack:a0:callback-ledger": true,
    "q78:finite-sine-120:specialized-quadpack:a0:finite-return": true,
    "q78:finite-sine-120:specialized-quadpack:a0:native-success": true,
    "q78:finite-sine-120:specialized-quadpack:a0:required-analytic-accuracy": true,
    "q78:finite-sine-120:specialized-quadpack:a0:absolute-series": true,
    "q78:finite-sine-120:specialized-quadpack:a1:callback-ledger": true,
    "q78:finite-sine-120:specialized-quadpack:a1:finite-return": true,
    "q78:finite-sine-120:specialized-quadpack:a1:native-success": true,
    "q78:finite-sine-120:specialized-quadpack:a1:required-analytic-accuracy": true,
    "q78:finite-sine-120:specialized-quadpack:a1:absolute-series": true,
    "q78:finite-sine-120:specialized-quadpack:a2:callback-ledger": true,
    "q78:finite-sine-120:specialized-quadpack:a2:finite-return": true,
    "q78:finite-sine-120:specialized-quadpack:a2:native-success": true,
    "q78:finite-sine-120:specialized-quadpack:a2:required-analytic-accuracy": true,
    "q78:finite-sine-120:specialized-quadpack:a2:absolute-series": true,
    "q78:finite-sine-120:simpson-companion:a0:callback-ledger": true,
    "q78:finite-sine-120:simpson-companion:a0:evaluation-cap": true,
    "q78:finite-sine-120:simpson-companion:a0:finite-return": true,
    "q78:finite-sine-120:simpson-companion:a0:native-status": true,
    "q78:finite-sine-120:simpson-companion:a1:callback-ledger": true,
    "q78:finite-sine-120:simpson-companion:a1:evaluation-cap": true,
    "q78:finite-sine-120:simpson-companion:a1:finite-return": true,
    "q78:finite-sine-120:simpson-companion:a1:native-status": true,
    "q78:finite-sine-120:simpson-companion:a2:callback-ledger": true,
    "q78:finite-sine-120:simpson-companion:a2:evaluation-cap": true,
    "q78:finite-sine-120:simpson-companion:a2:finite-return": true,
    "q78:finite-sine-120:simpson-companion:a2:native-status": true,
    "q78:fourier-half-line:specialized-quadpack:a0:callback-ledger": true,
    "q78:fourier-half-line:specialized-quadpack:a0:finite-return": true,
    "q78:fourier-half-line:specialized-quadpack:a0:native-success": true,
    "q78:fourier-half-line:specialized-quadpack:a0:required-analytic-accuracy": true,
    "q78:fourier-half-line:specialized-quadpack:a0:absolute-series": true,
    "q78:fourier-half-line:specialized-quadpack:a1:callback-ledger": true,
    "q78:fourier-half-line:specialized-quadpack:a1:finite-return": true,
    "q78:fourier-half-line:specialized-quadpack:a1:native-success": true,
    "q78:fourier-half-line:specialized-quadpack:a1:required-analytic-accuracy": true,
    "q78:fourier-half-line:specialized-quadpack:a1:absolute-series": true,
    "q78:fourier-half-line:specialized-quadpack:a2:callback-ledger": true,
    "q78:fourier-half-line:specialized-quadpack:a2:finite-return": true,
    "q78:fourier-half-line:specialized-quadpack:a2:native-success": true,
    "q78:fourier-half-line:specialized-quadpack:a2:required-analytic-accuracy": true,
    "q78:fourier-half-line:specialized-quadpack:a2:absolute-series": true,
    "q78:fourier-half-line:simpson-companion:a0:callback-ledger": true,
    "q78:fourier-half-line:simpson-companion:a0:evaluation-cap": true,
    "q78:fourier-half-line:simpson-companion:a0:finite-return": true,
    "q78:fourier-half-line:simpson-companion:a0:native-status": true,
    "q78:fourier-half-line:simpson-companion:a1:callback-ledger": true,
    "q78:fourier-half-line:simpson-companion:a1:evaluation-cap": true,
    "q78:fourier-half-line:simpson-companion:a1:finite-return": true,
    "q78:fourier-half-line:simpson-companion:a1:native-status": true,
    "q78:fourier-half-line:simpson-companion:a2:callback-ledger": true,
    "q78:fourier-half-line:simpson-companion:a2:evaluation-cap": true,
    "q78:fourier-half-line:simpson-companion:a2:finite-return": true,
    "q78:fourier-half-line:simpson-companion:a2:native-status": true,
    "q78:internal-root:specialized-quadpack:a0:callback-ledger": true,
    "q78:internal-root:specialized-quadpack:a0:finite-return": true,
    "q78:internal-root:specialized-quadpack:a0:native-success": true,
    "q78:internal-root:specialized-quadpack:a0:required-analytic-accuracy": true,
    "q78:internal-root:specialized-quadpack:a0:absolute-series": true,
    "q78:internal-root:specialized-quadpack:a1:callback-ledger": true,
    "q78:internal-root:specialized-quadpack:a1:finite-return": true,
    "q78:internal-root:specialized-quadpack:a1:native-success": true,
    "q78:internal-root:specialized-quadpack:a1:required-analytic-accuracy": true,
    "q78:internal-root:specialized-quadpack:a1:absolute-series": true,
    "q78:internal-root:specialized-quadpack:a2:callback-ledger": true,
    "q78:internal-root:specialized-quadpack:a2:finite-return": true,
    "q78:internal-root:specialized-quadpack:a2:native-success": true,
    "q78:internal-root:specialized-quadpack:a2:required-analytic-accuracy": true,
    "q78:internal-root:specialized-quadpack:a2:absolute-series": true,
    "q78:internal-root:simpson-companion:a0:callback-ledger": true,
    "q78:internal-root:simpson-companion:a0:evaluation-cap": true,
    "q78:internal-root:simpson-companion:a0:declared-singular-node": true,
    "q78:internal-root:simpson-companion:a1:callback-ledger": true,
    "q78:internal-root:simpson-companion:a1:evaluation-cap": true,
    "q78:internal-root:simpson-companion:a1:declared-singular-node": true,
    "q78:internal-root:simpson-companion:a2:callback-ledger": true,
    "q78:internal-root:simpson-companion:a2:evaluation-cap": true,
    "q78:internal-root:simpson-companion:a2:declared-singular-node": true,
    "quadpack-domain-selection:fixed-record-count": true,
    "quadpack-domain-selection:unique-record-ids": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/index.json

![Saved active Fourier contributions and actual errors/call counts](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection-preview.png)

Saved active Fourier contributions and actual errors/call counts

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

- quad: adaptive integration and QUADPACK dispatch [accessed 2026-11-25]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.quad.html; review_level=selected-official-documentation

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
