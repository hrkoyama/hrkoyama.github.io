# Smolyak sparse-grid quadrature / Smolyak疎格子求積

Status: educational-example

Compare nested Clenshaw–Curtis differences and tensor rules on fixed integrals in two to four variables.

2〜4変数の固定積分で入れ子Clenshaw–Curtis差分とテンソル積を比べます。

Low sparse levels can miss interactions. No general high-dimensional optimality or ranking against MC/QMC is claimed.

Other names: Smolyak疎格子求積, Smolyak sparse-grid quadrature

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quadrature/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quadrature/



- Reference: https://www.sam.math.ethz.ch/sam_reports/reports_final/reports2008/2008-07.pdf — Selected cover/introduction/sec2 extracted equations2.1–2.6; not the entire DFT proof or performance study. This report supports the Clenshaw-Curtis rule only. The Smolyak Delta/combination assembly is independently derived here; the Smolyak1963 and Gerstner-Griebel1998 original bodies remain unread.

## Small fixed-input validation supplements

Compare nested Clenshaw–Curtis differences and tensor rules on fixed integrals in two to four variables.

2〜4変数の固定積分で入れ子Clenshaw–Curtis差分とテンソル積を比べます。

- Tensor and Smolyak controls in two to four dimensions: https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json

Common execution records: [{"id": "tensor-smolyak-dimensions", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve this fixed scope; qualify extensions with separate inputs, references and criteria.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/smolyak-sparse-grid/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [有限・無限・多変数の定積分](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#definite-integrals-ja) (`definite-integrals`; tensor-smolyak-dimensions)

#### 問題の図 (`method-problems-ja`)

##### [2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja) (`tensor-smolyak-dimensions`)

![実2次元節点と符号付き積分重み 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成24件・未達18件・計算不能0件です。FALSE/NAと失敗rawを保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions-preview.png)

正規化dyadic角キーで同一節点を所有し、符号付き重みと評価台帳を保持。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja#code-ja)

- [2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja) (`tensor-smolyak-dimensions`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

滑らかな積と相互作用積の42本の固定cubatureを比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja#references-ja) (`tensor-smolyak-dimensions`)

- [2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-tensor-smolyak-dimensions-ja) (`tensor-smolyak-dimensions`; 同じ問題の参照; 解析参照)

一般の誤差単調性、常時正重み、疎格子の費用優位は主張しません。物理PDEの空間ではありません。

[既存の参照図](/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja#tensor-smolyak-dimensions-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quadrature/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 2〜4次元テンソル・Smolyak対照 (`tensor-smolyak-dimensions`)

[2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

滑らかな積と相互作用積の42本の固定cubatureを比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

2〜4変数の固定積分で入れ子Clenshaw–Curtis差分とテンソル積を比べます。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-25/quadrature-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/run.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/cubature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/cubature.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/gk15.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/gk15.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py)
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

- [Finite, improper and multivariate definite integrals](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#definite-integrals-en) (`definite-integrals`; tensor-smolyak-dimensions)

#### Problem figures (`method-problems-en`)

##### [Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en) (`tensor-smolyak-dimensions`)

![Actual two-dimensional nodes and signed integration weights The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 24 met, 18 unmet and 0 not computable. False/NA outcomes and raw failures are retained.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions-preview.png)

Canonical dyadic angle keys own shared nodes; signed weights and call ledgers are retained.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en#code-en)

- [Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en) (`tensor-smolyak-dimensions`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

Forty-two fixed cubatures compare a smooth product and an interaction product.


#### Exact / reference solutions (`method-references-en`)

##### [Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en#references-en) (`tensor-smolyak-dimensions`)

- [Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-tensor-smolyak-dimensions-en) (`tensor-smolyak-dimensions`; Same-problem reference; Analytic reference)

No general error monotonicity, positive-weight or cost-superiority claim; these are integration coordinates, not a physical PDE space.

[Existing reference profile](/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en#tensor-smolyak-dimensions-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quadrature/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Tensor and Smolyak controls in two to four dimensions (`tensor-smolyak-dimensions`)

[Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

Forty-two fixed cubatures compare a smooth product and an interaction product.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Compare nested Clenshaw–Curtis differences and tensor rules on fixed integrals in two to four variables.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

###### Related source

- [/code/validated-examples/2026-11-25/quadrature-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/run.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/cubature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/cubature.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/gk15.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/gk15.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py)
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
