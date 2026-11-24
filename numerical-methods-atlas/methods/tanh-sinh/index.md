# Tanh–sinh double-exponential quadrature / tanh–sinh二重指数求積

Status: educational-example

Evaluate stable transformed products with a finite full-endpoint trapezoidal sum.

安定な変換積を有限の全端点重み台形和で評価します。

Distinguish continuous finite-window tails from finite-sum errors. No bound on an omitted infinite-grid sum is claimed.

Other names: tanh–sinh二重指数求積, Tanh–sinh double-exponential quadrature

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quadrature/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quadrature/



- Reference: https://ems.press/doi/pdf/10.2977/prims/1195192451 — Selected extracted pp722/724/730 equations; rendered equation screenshots failed. No whole-paper proof/optimality audit.

## Small fixed-input validation supplements

Evaluate stable transformed products with a finite full-endpoint trapezoidal sum.

安定な変換積を有限の全端点重み台形和で評価します。

- G7/K15 and finite-interval tanh-sinh: https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json

Common execution records: [{"id": "gk15-double-exponential", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve this fixed scope; qualify extensions with separate inputs, references and criteria.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/tanh-sinh/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [有限・無限・多変数の定積分](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#definite-integrals-ja) (`definite-integrals`; gk15-double-exponential)

#### 問題の図 (`method-problems-ja`)

##### [G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=ja) (`gk15-double-exponential`)

![保存された変換関数と有限窓誤差（連続tailは別量） 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成26件・未達7件・計算不能0件です。FALSE/NAと失敗rawを保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential-preview.png)

共有15節点、G7次数13/K15次数23。DEは安定log式と全端点重みです。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=ja#code-ja)

- [G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja) (`gk15-double-exponential`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

9本の適応GKと24本の固定DE和を比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=ja#references-ja) (`gk15-double-exponential`)

- [G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gk15-double-exponential-ja) (`gk15-double-exponential`; 同じ問題の参照; 解析参照)

半無限exp-sinh/全実線sinh-sinhは未実装。無限台形SUMの省略項のboundは提供しません。

[既存の参照図](/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja#gk15-double-exponential-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quadrature/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### G7/K15と有限区間tanh-sinh (`gk15-double-exponential`)

[G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

9本の適応GKと24本の固定DE和を比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

安定な変換積を有限の全端点重み台形和で評価します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-25/quadrature-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/run.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/gk15.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/gk15.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/cubature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/cubature.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/experiments.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/io_contract.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/reference_cache.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/reference_cache.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/references/direct_rule.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/references/direct_rule.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/references/formulas.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/references/formulas.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/references/interval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/references/interval.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/references/qualify.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Finite, improper and multivariate definite integrals](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#definite-integrals-en) (`definite-integrals`; gk15-double-exponential)

#### Problem figures (`method-problems-en`)

##### [G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en) (`gk15-double-exponential`)

![Saved transformed integrands and finite-window defects; continuous tails are distinct The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 26 met, 7 unmet and 0 not computable. False/NA outcomes and raw failures are retained.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential-preview.png)

Shared15-node G7 degree13/K15 degree23; DE uses stable logarithmic products and full endpoint weights.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en#code-en)

- [G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en) (`gk15-double-exponential`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

Nine adaptive GK rows and twenty-four fixed DE sums are compared.


#### Exact / reference solutions (`method-references-en`)

##### [G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en#references-en) (`gk15-double-exponential`)

- [G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gk15-double-exponential-en) (`gk15-double-exponential`; Same-problem reference; Analytic reference)

Half-line exp-sinh and whole-line sinh-sinh are unimplemented; no omitted infinite-grid sum bound is provided.

[Existing reference profile](/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en#gk15-double-exponential-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quadrature/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### G7/K15 and finite-interval tanh-sinh (`gk15-double-exponential`)

[G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

Nine adaptive GK rows and twenty-four fixed DE sums are compared.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Evaluate stable transformed products with a finite full-endpoint trapezoidal sum.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

###### Related source

- [/code/validated-examples/2026-11-25/quadrature-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/run.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/gk15.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/gk15.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/cubature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/cubature.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/experiments.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/io_contract.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/reference_cache.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/reference_cache.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/references/direct_rule.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/references/direct_rule.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/references/formulas.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/references/formulas.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/references/interval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/references/interval.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/references/qualify.py)

###### Package tests

- [/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
