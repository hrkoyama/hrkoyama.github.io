# Chebyshev approximation / Chebyshev近似

Status: educational-example

Connect polynomial approximation, node choice and spectral convergence. Fixed educational executions: Runge interpolation: nodes, representation and rounding.

多項式近似・節点・スペクトル収束を整理する。 固定した教育用実行例：節点・表現・丸めを分けるRunge補間。

A sampled maximum error is not a proof of a continuous uniform norm. Closed weights and discrete orthogonality on rounded nodes are not treated as exact. No arbitrary-degree or all-point stability guarantee is made.

Other names: チェビシェフ近似, チェビシェフ多項式, Chebyshev polynomials, Chebyshev approximation

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/chebyshev/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/chebyshev/



- Reference: https://doi.org/10.1007/bf01386223 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://dlmf.nist.gov/ — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://dlmf.nist.gov/3.11 — Selected E7, E9, E11 and E15 with endpoint-halving conventions; no original Clenshaw paper reading. The implementation uses full coefficients, so its final combination is derived explicitly.
- Reference: https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.interpolate.BarycentricInterpolator.html — Selected barycentric formula and interpolation-conditioning notes read during the preceding preparation. The Berrut–Trefethen paper is a bibliographic lead, not a full-text reading.

## Small fixed-input validation supplements

Fixed educational executions: Runge interpolation: nodes, representation and rounding.

固定した教育用実行例：節点・表現・丸めを分けるRunge補間。

- Runge interpolation: nodes, representation and rounding: https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json

Common execution records: [{"id": "runge-barycentric-clenshaw", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the fixed scope and qualify extensions separately.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/chebyshev/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [格納節点の多項式補間](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#polynomial-interpolation-ja) (`polynomial-interpolation`; runge-barycentric-clenshaw)

#### 問題の図 (`method-problems-ja`)

##### [節点・表現・丸めを分けるRunge補間](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=ja) (`runge-barycentric-clenshaw`)

![Runge関数と絶対値関数を等間隔・Lobatto型の固定節点で補間し、Clenshaw評価と比較します。 保存配列から作図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-preview.png)

第2重心公式と全係数Clenshaw漸化式を自作。丸め済み節点上の閉形式重みと有限Chebyshev変換をそのまま保存します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=ja#code-ja)

- [節点・表現・丸めを分けるRunge補間](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=ja) (`runge-barycentric-clenshaw`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

Runge関数と絶対値関数を等間隔・Lobatto型の固定節点で補間し、Clenshaw評価と比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [節点・表現・丸めを分けるRunge補間](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=ja#references-ja) (`runge-barycentric-clenshaw`)

- [節点・表現・丸めを分けるRunge補間](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-runge-barycentric-clenshaw-ja) (`runge-barycentric-clenshaw`; 同じ問題の参照; 解析参照)

標本最大誤差は連続一様ノルムの証明ではありません。丸め節点の閉重み・離散直交性は厳密と見なしません。任意次数・任意点の安定性は保証しません。

[既存の参照図](/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=ja#runge-barycentric-clenshaw-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/chebyshev/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 節点・表現・丸めを分けるRunge補間 (`runge-barycentric-clenshaw`)

[節点・表現・丸めを分けるRunge補間](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

Runge関数と絶対値関数を等間隔・Lobatto型の固定節点で補間し、Clenshaw評価と比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

固定した教育用実行例：節点・表現・丸めを分けるRunge補間。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-25/approximation-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/run.py)
- [/code/validated-examples/2026-11-25/approximation-controls/interpolation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/interpolation.py)
- [/code/validated-examples/2026-11-25/approximation-controls/splines.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/splines.py)
- [/code/validated-examples/2026-11-25/approximation-controls/haar.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/haar.py)
- [/code/validated-examples/2026-11-25/approximation-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/experiments.py)
- [/code/validated-examples/2026-11-25/approximation-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/io_contract.py)
- [/code/validated-examples/2026-11-25/approximation-controls/references/haar_matrix.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/references/haar_matrix.py)
- [/code/validated-examples/2026-11-25/approximation-controls/references/polynomials.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/references/polynomials.py)
- [/code/validated-examples/2026-11-25/approximation-controls/references/spline_rational.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/references/spline_rational.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Polynomial interpolation on stored nodes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#polynomial-interpolation-en) (`polynomial-interpolation`; runge-barycentric-clenshaw)

#### Problem figures (`method-problems-en`)

##### [Runge interpolation: nodes, representation and rounding](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=en) (`runge-barycentric-clenshaw`)

![Interpolate the Runge and absolute-value functions on fixed equispaced and Lobatto-like nodes, and compare with Clenshaw evaluation. Drawn from saved arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-preview.png)

Implement the second barycentric formula and a full-coefficient Clenshaw recurrence. Retain the closed weights and finite Chebyshev transform on rounded nodes.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=en#code-en)

- [Runge interpolation: nodes, representation and rounding](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=en) (`runge-barycentric-clenshaw`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

Interpolate the Runge and absolute-value functions on fixed equispaced and Lobatto-like nodes, and compare with Clenshaw evaluation.


#### Exact / reference solutions (`method-references-en`)

##### [Runge interpolation: nodes, representation and rounding](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=en#references-en) (`runge-barycentric-clenshaw`)

- [Runge interpolation: nodes, representation and rounding](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-runge-barycentric-clenshaw-en) (`runge-barycentric-clenshaw`; Same-problem reference; Analytic reference)

A sampled maximum error is not a proof of a continuous uniform norm. Closed weights and discrete orthogonality on rounded nodes are not treated as exact. No arbitrary-degree or all-point stability guarantee is made.

[Existing reference profile](/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=en#runge-barycentric-clenshaw-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/chebyshev/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Runge interpolation: nodes, representation and rounding (`runge-barycentric-clenshaw`)

[Runge interpolation: nodes, representation and rounding](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

Interpolate the Runge and absolute-value functions on fixed equispaced and Lobatto-like nodes, and compare with Clenshaw evaluation.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Fixed educational executions: Runge interpolation: nodes, representation and rounding.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

###### Related source

- [/code/validated-examples/2026-11-25/approximation-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/run.py)
- [/code/validated-examples/2026-11-25/approximation-controls/interpolation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/interpolation.py)
- [/code/validated-examples/2026-11-25/approximation-controls/splines.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/splines.py)
- [/code/validated-examples/2026-11-25/approximation-controls/haar.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/haar.py)
- [/code/validated-examples/2026-11-25/approximation-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/experiments.py)
- [/code/validated-examples/2026-11-25/approximation-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/io_contract.py)
- [/code/validated-examples/2026-11-25/approximation-controls/references/haar_matrix.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/references/haar_matrix.py)
- [/code/validated-examples/2026-11-25/approximation-controls/references/polynomials.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/references/polynomials.py)
- [/code/validated-examples/2026-11-25/approximation-controls/references/spline_rational.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/references/spline_rational.py)

###### Package tests

- [/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
