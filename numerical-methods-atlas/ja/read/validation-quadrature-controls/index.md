# 領域別・二重指数・疎格子求積

固定した積分を適用条件に応じて比較し、推定誤差・実誤差・予算終了・未解像対照を区別します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 領域別QUADPACKと有限Simpson対照

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
### 前提・単位・境界

無限Gaussian、有限振動2周波数、半無限Fourier、内部特異点。絶対公差1e-6/1e-8/1e-10、epsrel=0。

**編集上の補足**

Simpsonの特異節点失敗と未達精度を保存し、推定誤差の一般保証にしません。 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成25件・未達2件・計算不能3件です。FALSE/NAと失敗rawを保持します。

### 採用した計算法

領域と重みを明示しfull_outputの活動prefixを保持。既存Simpson関数は不変。

$$
I=\int_\Omega f(x)\,dx
$$

### 比較・検証

独立の解析区間参照と実callback数を照合します。有限Gaussianは点値でなく厳密区間です。

### 確認の限界

Simpsonの特異節点失敗と未達精度を保存し、推定誤差の一般保証にしません。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- quad: adaptive integration and QUADPACK dispatch [accessed 2026-11-25]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.quad.html; review_level=selected-official-documentation

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## G7/K15と有限区間tanh-sinh

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
### 前提・単位・境界

exp(x)、x^(-1/3)、−log(x)を[0,1]で積分。h=1/2〜1/16、切断T=3/4。

**編集上の補足**

半無限exp-sinh/全実線sinh-sinhは未実装。無限台形SUMの省略項のboundは提供しません。 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成26件・未達7件・計算不能0件です。FALSE/NAと失敗rawを保持します。

### 採用した計算法

共有15節点、G7次数13/K15次数23。DEは安定log式と全端点重みです。

$$
I=\int_\Omega f(x)\,dx
$$

### 比較・検証

解析区間参照で全誤差、連続tail、有限窓誤差を分離します。

### 確認の限界

半無限exp-sinh/全実線sinh-sinhは未実装。無限台形SUMの省略項のboundは提供しません。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- Pinned SciPy1.14.1 bundled dqk15 [accessed 2026-11-25]. https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/integrate/quadpack/dqk15.f; review_level=primary-software-source
- Double Exponential Formulas for Numerical Integration [accessed 2026-11-25]. https://ems.press/doi/pdf/10.2977/prims/1195192451; review_level=selected-primary-body-text

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 2〜4次元テンソル・Smolyak対照

滑らかな積と相互作用積の42本の固定cubatureを比較します。

**使用手法**

- [Gauss求積・適応積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja) (`quadrature`)
- [Smolyak疎格子求積](https://hrkoyama.github.io/numerical-methods-atlas/methods/smolyak-sparse-grid/?lang=ja) (`smolyak-sparse-grid`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja#tensor-smolyak-dimensions-ja-algorithm)

正規化dyadic角キーで同一節点を所有し、符号付き重みと評価台帳を保持。

- [有限・無限・多変数の定積分](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#definite-integrals-ja) (`definite-integrals`)

[0,1]^d、d=2/3/4。テンソルlevel1/2/3、疎格子level1/2/3/4。


**問題の図**

![2〜4次元テンソル・Smolyak対照：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja) (`tensor-smolyak-dimensions`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja#tensor-smolyak-dimensions-ja-validation)

解析積分と独立Delta/combination組立を区別し、L<dの相互作用未解像を可視化。

- [2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-tensor-smolyak-dimensions-ja) (`tensor-smolyak-dimensions`; 同じ問題の参照 · 解析参照)

一般の誤差単調性、常時正重み、疎格子の費用優位は主張しません。物理PDEの空間ではありません。
### 前提・単位・境界

[0,1]^d、d=2/3/4。テンソルlevel1/2/3、疎格子level1/2/3/4。

**編集上の補足**

一般の誤差単調性、常時正重み、疎格子の費用優位は主張しません。物理PDEの空間ではありません。 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成24件・未達18件・計算不能0件です。FALSE/NAと失敗rawを保持します。

### 採用した計算法

正規化dyadic角キーで同一節点を所有し、符号付き重みと評価台帳を保持。

$$
I=\int_\Omega f(x)\,dx
$$

### 比較・検証

解析積分と独立Delta/combination組立を区別し、L<dの相互作用未解像を可視化。

### 確認の限界

一般の誤差単調性、常時正重み、疎格子の費用優位は主張しません。物理PDEの空間ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "records": 42,
    "integrand_evaluations": 18482,
    "accuracy_goals_met": 24,
    "accuracy_goals_unmet": 18,
    "accuracy_goals_unresolved": 0,
    "estimated_converged_rows": 42
  },
  "checks": {
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:required-finest-accuracy": true,
    "q80:d2:smooth-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d2:smooth-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d2:smooth-product:smolyak-delta:L1:finite-return": true,
    "q80:d2:smooth-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d2:smooth-product:smolyak-delta:L1:mass": true,
    "q80:d2:smooth-product:smolyak-delta:L1:low-moments": true,
    "q80:d2:smooth-product:smolyak-delta:L1:delta-combination": true,
    "q80:d2:smooth-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d2:smooth-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d2:smooth-product:smolyak-delta:L2:finite-return": true,
    "q80:d2:smooth-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d2:smooth-product:smolyak-delta:L2:mass": true,
    "q80:d2:smooth-product:smolyak-delta:L2:low-moments": true,
    "q80:d2:smooth-product:smolyak-delta:L2:delta-combination": true,
    "q80:d2:smooth-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d2:smooth-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d2:smooth-product:smolyak-delta:L3:finite-return": true,
    "q80:d2:smooth-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d2:smooth-product:smolyak-delta:L3:mass": true,
    "q80:d2:smooth-product:smolyak-delta:L3:low-moments": true,
    "q80:d2:smooth-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d2:smooth-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d2:smooth-product:smolyak-delta:L4:finite-return": true,
    "q80:d2:smooth-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d2:smooth-product:smolyak-delta:L4:mass": true,
    "q80:d2:smooth-product:smolyak-delta:L4:low-moments": true,
    "q80:d2:smooth-product:smolyak-delta:L4:required-finest-accuracy": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:required-product-moment": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:required-product-moment": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:required-product-moment": true,
    "q80:d2:interaction-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d2:interaction-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d2:interaction-product:smolyak-delta:L1:finite-return": true,
    "q80:d2:interaction-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d2:interaction-product:smolyak-delta:L1:mass": true,
    "q80:d2:interaction-product:smolyak-delta:L1:low-moments": true,
    "q80:d2:interaction-product:smolyak-delta:L1:delta-combination": true,
    "q80:d2:interaction-product:smolyak-delta:L1:underresolution-identity": true,
    "q80:d2:interaction-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d2:interaction-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d2:interaction-product:smolyak-delta:L2:finite-return": true,
    "q80:d2:interaction-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d2:interaction-product:smolyak-delta:L2:mass": true,
    "q80:d2:interaction-product:smolyak-delta:L2:low-moments": true,
    "q80:d2:interaction-product:smolyak-delta:L2:delta-combination": true,
    "q80:d2:interaction-product:smolyak-delta:L2:required-product-moment": true,
    "q80:d2:interaction-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d2:interaction-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d2:interaction-product:smolyak-delta:L3:finite-return": true,
    "q80:d2:interaction-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d2:interaction-product:smolyak-delta:L3:mass": true,
    "q80:d2:interaction-product:smolyak-delta:L3:low-moments": true,
    "q80:d2:interaction-product:smolyak-delta:L3:required-product-moment": true,
    "q80:d2:interaction-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d2:interaction-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d2:interaction-product:smolyak-delta:L4:finite-return": true,
    "q80:d2:interaction-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d2:interaction-product:smolyak-delta:L4:mass": true,
    "q80:d2:interaction-product:smolyak-delta:L4:low-moments": true,
    "q80:d2:interaction-product:smolyak-delta:L4:required-product-moment": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:required-finest-accuracy": true,
    "q80:d3:smooth-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d3:smooth-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d3:smooth-product:smolyak-delta:L1:finite-return": true,
    "q80:d3:smooth-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d3:smooth-product:smolyak-delta:L1:mass": true,
    "q80:d3:smooth-product:smolyak-delta:L1:low-moments": true,
    "q80:d3:smooth-product:smolyak-delta:L1:delta-combination": true,
    "q80:d3:smooth-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d3:smooth-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d3:smooth-product:smolyak-delta:L2:finite-return": true,
    "q80:d3:smooth-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d3:smooth-product:smolyak-delta:L2:mass": true,
    "q80:d3:smooth-product:smolyak-delta:L2:low-moments": true,
    "q80:d3:smooth-product:smolyak-delta:L2:delta-combination": true,
    "q80:d3:smooth-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d3:smooth-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d3:smooth-product:smolyak-delta:L3:finite-return": true,
    "q80:d3:smooth-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d3:smooth-product:smolyak-delta:L3:mass": true,
    "q80:d3:smooth-product:smolyak-delta:L3:low-moments": true,
    "q80:d3:smooth-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d3:smooth-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d3:smooth-product:smolyak-delta:L4:finite-return": true,
    "q80:d3:smooth-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d3:smooth-product:smolyak-delta:L4:mass": true,
    "q80:d3:smooth-product:smolyak-delta:L4:low-moments": true,
    "q80:d3:smooth-product:smolyak-delta:L4:required-finest-accuracy": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:required-product-moment": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:required-product-moment": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:required-product-moment": true,
    "q80:d3:interaction-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d3:interaction-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d3:interaction-product:smolyak-delta:L1:finite-return": true,
    "q80:d3:interaction-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d3:interaction-product:smolyak-delta:L1:mass": true,
    "q80:d3:interaction-product:smolyak-delta:L1:low-moments": true,
    "q80:d3:interaction-product:smolyak-delta:L1:delta-combination": true,
    "q80:d3:interaction-product:smolyak-delta:L1:underresolution-identity": true,
    "q80:d3:interaction-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d3:interaction-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d3:interaction-product:smolyak-delta:L2:finite-return": true,
    "q80:d3:interaction-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d3:interaction-product:smolyak-delta:L2:mass": true,
    "q80:d3:interaction-product:smolyak-delta:L2:low-moments": true,
    "q80:d3:interaction-product:smolyak-delta:L2:delta-combination": true,
    "q80:d3:interaction-product:smolyak-delta:L2:underresolution-identity": true,
    "q80:d3:interaction-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d3:interaction-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d3:interaction-product:smolyak-delta:L3:finite-return": true,
    "q80:d3:interaction-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d3:interaction-product:smolyak-delta:L3:mass": true,
    "q80:d3:interaction-product:smolyak-delta:L3:low-moments": true,
    "q80:d3:interaction-product:smolyak-delta:L3:required-product-moment": true,
    "q80:d3:interaction-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d3:interaction-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d3:interaction-product:smolyak-delta:L4:finite-return": true,
    "q80:d3:interaction-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d3:interaction-product:smolyak-delta:L4:mass": true,
    "q80:d3:interaction-product:smolyak-delta:L4:low-moments": true,
    "q80:d3:interaction-product:smolyak-delta:L4:required-product-moment": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:required-finest-accuracy": true,
    "q80:d4:smooth-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d4:smooth-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d4:smooth-product:smolyak-delta:L1:finite-return": true,
    "q80:d4:smooth-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d4:smooth-product:smolyak-delta:L1:mass": true,
    "q80:d4:smooth-product:smolyak-delta:L1:low-moments": true,
    "q80:d4:smooth-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d4:smooth-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d4:smooth-product:smolyak-delta:L2:finite-return": true,
    "q80:d4:smooth-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d4:smooth-product:smolyak-delta:L2:mass": true,
    "q80:d4:smooth-product:smolyak-delta:L2:low-moments": true,
    "q80:d4:smooth-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d4:smooth-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d4:smooth-product:smolyak-delta:L3:finite-return": true,
    "q80:d4:smooth-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d4:smooth-product:smolyak-delta:L3:mass": true,
    "q80:d4:smooth-product:smolyak-delta:L3:low-moments": true,
    "q80:d4:smooth-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d4:smooth-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d4:smooth-product:smolyak-delta:L4:finite-return": true,
    "q80:d4:smooth-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d4:smooth-product:smolyak-delta:L4:mass": true,
    "q80:d4:smooth-product:smolyak-delta:L4:low-moments": true,
    "q80:d4:smooth-product:smolyak-delta:L4:required-finest-accuracy": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:required-product-moment": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:required-product-moment": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:required-product-moment": true,
    "q80:d4:interaction-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d4:interaction-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d4:interaction-product:smolyak-delta:L1:finite-return": true,
    "q80:d4:interaction-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d4:interaction-product:smolyak-delta:L1:mass": true,
    "q80:d4:interaction-product:smolyak-delta:L1:low-moments": true,
    "q80:d4:interaction-product:smolyak-delta:L1:underresolution-identity": true,
    "q80:d4:interaction-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d4:interaction-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d4:interaction-product:smolyak-delta:L2:finite-return": true,
    "q80:d4:interaction-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d4:interaction-product:smolyak-delta:L2:mass": true,
    "q80:d4:interaction-product:smolyak-delta:L2:low-moments": true,
    "q80:d4:interaction-product:smolyak-delta:L2:underresolution-identity": true,
    "q80:d4:interaction-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d4:interaction-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d4:interaction-product:smolyak-delta:L3:finite-return": true,
    "q80:d4:interaction-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d4:interaction-product:smolyak-delta:L3:mass": true,
    "q80:d4:interaction-product:smolyak-delta:L3:low-moments": true,
    "q80:d4:interaction-product:smolyak-delta:L3:underresolution-identity": true,
    "q80:d4:interaction-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d4:interaction-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d4:interaction-product:smolyak-delta:L4:finite-return": true,
    "q80:d4:interaction-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d4:interaction-product:smolyak-delta:L4:mass": true,
    "q80:d4:interaction-product:smolyak-delta:L4:low-moments": true,
    "q80:d4:interaction-product:smolyak-delta:L4:required-product-moment": true,
    "tensor-smolyak-dimensions:fixed-record-count": true,
    "tensor-smolyak-dimensions:unique-record-ids": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/index.json

![実2次元節点と符号付き積分重み](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions-preview.png)

実2次元節点と符号付き積分重み

### 取得・実行

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

### 出典と確認範囲

- Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules [accessed 2026-11-25]. https://www.sam.math.ethz.ch/sam_reports/reports_final/reports2008/2008-07.pdf; review_level=selected-primary-body-text

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
