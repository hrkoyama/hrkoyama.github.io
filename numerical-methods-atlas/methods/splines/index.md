# Spline interpolation / スプライン補間

Status: educational-example

Relate interpolation, boundary conditions and smoothness. Fixed educational executions: Natural and clamped splines versus PCHIP.

補間条件・境界条件と滑らかさを整理する。 固定した教育用実行例：自然・端点微分指定スプラインとPCHIP。

PCHIP is generally C1, not necessarily C2. Best approximation, extrapolation and noise smoothing are outside scope. A SciPy comparison does not substitute for reading the original papers.

Other names: スプライン, スプライン補間法, spline interpolation

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/splines/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/splines/



- Reference: https://doi.org/10.1016/0021-9045(72)90080-9 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/interpolate/_cubic.py — Selected lines 202–225, 243–254, 275–298: harmonic interior derivatives, endpoint sign and 3-slope limiter, two-point case. The original Fritsch–Butland paper has not been read in full. Own formulas are independently expressed as scalar Hermite polynomials.
- Reference: https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.interpolate.CubicSpline.html — Natural and clamped boundary conditions and the BSpline recurrence were read during preparation. No de Boor original full-text claim. SciPy is a secondary numerical companion; the rational second-derivative system is the independent reference.

## Small fixed-input validation supplements

Fixed educational executions: Natural and clamped splines versus PCHIP.

固定した教育用実行例：自然・端点微分指定スプラインとPCHIP。

- Natural and clamped splines versus PCHIP: https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json

Common execution records: [{"id": "spline-shape-controls", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the fixed scope and qualify extensions separately.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/splines/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [3次スプラインと形状保存補間](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#cubic-spline-pchip-ja) (`cubic-spline-pchip`; spline-shape-controls)

#### 問題の図 (`method-problems-ja`)

##### [自然・端点微分指定スプラインとPCHIP](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=ja) (`spline-shape-controls`)

![平坦部を持つ単調データ・3次式・直線の固定3組で、C2連続性と形状保存を比較します。 保存配列から作図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-preview.png)

3次Bスプラインの配置行列を解きde Boor評価。別経路でPCHIPの調和平均・端点制限とHermite評価を実装します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=ja#code-ja)

- [自然・端点微分指定スプラインとPCHIP](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=ja) (`spline-shape-controls`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

平坦部を持つ単調データ・3次式・直線の固定3組で、C2連続性と形状保存を比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [自然・端点微分指定スプラインとPCHIP](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=ja#references-ja) (`spline-shape-controls`)

- [自然・端点微分指定スプラインとPCHIP](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-spline-shape-controls-ja) (`spline-shape-controls`; 同じ問題の参照; 解析参照)

PCHIPは通常C1でありC2とは限りません。一般データの最良近似・外挿・ノイズ平滑化は対象外。SciPyは原著完全閲読の代用ではありません。

[既存の参照図](/numerical-methods-atlas/validation/spline-shape-controls/?lang=ja#spline-shape-controls-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/splines/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 自然・端点微分指定スプラインとPCHIP (`spline-shape-controls`)

[自然・端点微分指定スプラインとPCHIP](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

平坦部を持つ単調データ・3次式・直線の固定3組で、C2連続性と形状保存を比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

固定した教育用実行例：自然・端点微分指定スプラインとPCHIP。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-25/approximation-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/run.py)
- [/code/validated-examples/2026-11-25/approximation-controls/splines.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/splines.py)
- [/code/validated-examples/2026-11-25/approximation-controls/interpolation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/interpolation.py)
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

- [Cubic splines and shape-preserving interpolation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#cubic-spline-pchip-en) (`cubic-spline-pchip`; spline-shape-controls)

#### Problem figures (`method-problems-en`)

##### [Natural and clamped splines versus PCHIP](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=en) (`spline-shape-controls`)

![Compare C2 continuity and shape preservation on three fixed data sets: a monotone plateau, a cubic and a straight line. Drawn from saved arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-preview.png)

Solve a cubic B-spline collocation system and evaluate it with de Boor recursion. A separate path implements PCHIP harmonic slopes, endpoint limiting and Hermite evaluation.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=en#code-en)

- [Natural and clamped splines versus PCHIP](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=en) (`spline-shape-controls`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

Compare C2 continuity and shape preservation on three fixed data sets: a monotone plateau, a cubic and a straight line.


#### Exact / reference solutions (`method-references-en`)

##### [Natural and clamped splines versus PCHIP](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=en#references-en) (`spline-shape-controls`)

- [Natural and clamped splines versus PCHIP](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-spline-shape-controls-en) (`spline-shape-controls`; Same-problem reference; Analytic reference)

PCHIP is generally C1, not necessarily C2. Best approximation, extrapolation and noise smoothing are outside scope. A SciPy comparison does not substitute for reading the original papers.

[Existing reference profile](/numerical-methods-atlas/validation/spline-shape-controls/?lang=en#spline-shape-controls-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/splines/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Natural and clamped splines versus PCHIP (`spline-shape-controls`)

[Natural and clamped splines versus PCHIP](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

Compare C2 continuity and shape preservation on three fixed data sets: a monotone plateau, a cubic and a straight line.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Fixed educational executions: Natural and clamped splines versus PCHIP.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

###### Related source

- [/code/validated-examples/2026-11-25/approximation-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/run.py)
- [/code/validated-examples/2026-11-25/approximation-controls/splines.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/splines.py)
- [/code/validated-examples/2026-11-25/approximation-controls/interpolation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/interpolation.py)
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
