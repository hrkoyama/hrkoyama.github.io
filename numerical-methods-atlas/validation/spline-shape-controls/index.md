# 自然・端点微分指定スプラインとPCHIP

平坦部を持つ単調データ・3次式・直線の固定3組で、C2連続性と形状保存を比較します。

**使用手法**

- [スプライン補間](https://hrkoyama.github.io/numerical-methods-atlas/methods/splines/?lang=ja) (`splines`)
- [PCHIP単調3次Hermite補間](https://hrkoyama.github.io/numerical-methods-atlas/methods/pchip/?lang=ja) (`pchip`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=ja#spline-shape-controls-ja-algorithm)

3次Bスプラインの配置行列を解きde Boor評価。別経路でPCHIPの調和平均・端点制限とHermite評価を実装します。

$$
S_i(s)=a_i+b_i*s+c_i*s^2+d_i*s^3
$$

$$
d_k=(w_1+w_2)/(w_1/m_(k-1)+w_2/m_k)
$$

$$
S_natural(1.5)=a-9*(b-a)/88; S_clamped(1.5)=a-15*(b-a)/152
$$

- [3次スプラインと形状保存補間](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#cubic-spline-pchip-ja) (`cubic-spline-pchip`)

実binary64の節点と値を使用。自然条件は両端2階微分ゼロ、clamped条件は入力端点1階微分です。


**問題の図**

![自然・端点微分指定スプラインとPCHIP：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[自然・端点微分指定スプラインとPCHIP](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=ja) (`spline-shape-controls`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=ja#spline-shape-controls-ja-validation)

正確な有理2階微分系・有理PCHIP・SciPy 1.14.1を照合。端点15記録は16スカラー出力・13異なる入力。平坦部の負値は実binary64をFraction化した独立式で示します。

- [自然・端点微分指定スプラインとPCHIP](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-spline-shape-controls-ja) (`spline-shape-controls`; 同じ問題の参照 · 解析参照)

PCHIPは通常C1でありC2とは限りません。一般データの最良近似・外挿・ノイズ平滑化は対象外。SciPyは原著完全閲読の代用ではありません。
## 前提・単位・境界

実binary64の節点と値を使用。自然条件は両端2階微分ゼロ、clamped条件は入力端点1階微分です。

**編集上の補足**

PCHIPは通常C1でありC2とは限りません。一般データの最良近似・外挿・ノイズ平滑化は対象外。SciPyは原著完全閲読の代用ではありません。

## 採用した計算法

3次Bスプラインの配置行列を解きde Boor評価。別経路でPCHIPの調和平均・端点制限とHermite評価を実装します。

$$
S_i(s)=a_i+b_i*s+c_i*s^2+d_i*s^3
$$

$$
d_k=(w_1+w_2)/(w_1/m_(k-1)+w_2/m_k)
$$

$$
S_natural(1.5)=a-9*(b-a)/88; S_clamped(1.5)=a-15*(b-a)/152
$$

## 比較・検証

正確な有理2階微分系・有理PCHIP・SciPy 1.14.1を照合。端点15記録は16スカラー出力・13異なる入力。平坦部の負値は実binary64をFraction化した独立式で示します。

## 確認の限界

PCHIPは通常C1でありC2とは限りません。一般データの最良近似・外挿・ノイズ平滑化は対象外。SciPyは原著完全閲読の代用ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "maximum_value_scaled_reference_defect": 2.9409263239818476e-16,
    "maximum_derivative_scaled_reference_defect": 5.2306043094691055e-15,
    "endpoint_fixture_records": 15,
    "endpoint_scalar_outputs": 16,
    "endpoint_distinct_datasets": 13
  },
  "checks": {
    "reference:endpoint-branch-values": true,
    "reference:endpoint-record-count": true,
    "reference:endpoint-output-count": true,
    "reference:endpoint-distinct-datasets": true,
    "reference:negative-natural-witness": true,
    "reference:negative-clamped-witness": true,
    "plateau-natural:finite": true,
    "plateau-natural:value-reference": true,
    "plateau-natural:derivative-reference": true,
    "plateau-natural:nodal": true,
    "plateau-natural:boundary-or-shape": true,
    "plateau-clamped:finite": true,
    "plateau-clamped:value-reference": true,
    "plateau-clamped:derivative-reference": true,
    "plateau-clamped:nodal": true,
    "plateau-clamped:boundary-or-shape": true,
    "reference:pchip-actual-input-plateau": true,
    "plateau-pchip:finite": true,
    "plateau-pchip:value-reference": true,
    "plateau-pchip:derivative-reference": true,
    "plateau-pchip:nodal": true,
    "plateau-pchip:boundary-or-shape": true,
    "cubic-natural:finite": true,
    "cubic-natural:value-reference": true,
    "cubic-natural:derivative-reference": true,
    "cubic-natural:nodal": true,
    "cubic-natural:boundary-or-shape": true,
    "cubic-clamped:finite": true,
    "cubic-clamped:value-reference": true,
    "cubic-clamped:derivative-reference": true,
    "cubic-clamped:nodal": true,
    "cubic-clamped:boundary-or-shape": true,
    "cubic-pchip:finite": true,
    "cubic-pchip:value-reference": true,
    "cubic-pchip:derivative-reference": true,
    "cubic-pchip:nodal": true,
    "cubic-pchip:boundary-or-shape": true,
    "linear-natural:finite": true,
    "linear-natural:value-reference": true,
    "linear-natural:derivative-reference": true,
    "linear-natural:nodal": true,
    "linear-natural:boundary-or-shape": true,
    "linear-clamped:finite": true,
    "linear-clamped:value-reference": true,
    "linear-clamped:derivative-reference": true,
    "linear-clamped:nodal": true,
    "linear-clamped:boundary-or-shape": true,
    "linear-pchip:finite": true,
    "linear-pchip:value-reference": true,
    "linear-pchip:derivative-reference": true,
    "linear-pchip:nodal": true,
    "linear-pchip:boundary-or-shape": true,
    "reference:exact-piece-continuity": true,
    "reference:polynomial-cubic-clamped": true,
    "reference:polynomial-linear-natural": true,
    "reference:polynomial-linear-clamped": true,
    "fixed-fit-count": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/index.json

![平坦部を持つ単調データ・3次式・直線の固定3組で、C2連続性と形状保存を比較します。 保存配列から作図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-preview.png)

平坦部を持つ単調データ・3次式・直線の固定3組で、C2連続性と形状保存を比較します。 保存配列から作図。

![保存済み誤差・導関数または二乗ノルムを別表示。各境界・表現の適用範囲は本文を参照。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-diagnostics.png)

保存済み誤差・導関数または二乗ノルムを別表示。各境界・表現の適用範囲は本文を参照。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- SciPy 1.14.1 PCHIP documentation and selected source [accessed 2026-11-25]. https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/interpolate/_cubic.py; review_level=official-source-selected-lines
Selected lines 202–225, 243–254, 275–298: harmonic interior derivatives, endpoint sign and 3-slope limiter, two-point case. The original Fritsch–Butland paper has not been read in full. Own formulas are independently expressed as scalar Hermite polynomials.

- SciPy 1.14.1 BSpline and CubicSpline documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.interpolate.CubicSpline.html; review_level=official-documentation-selected-definitions
Natural and clamped boundary conditions and the BSpline recurrence were read during preparation. No de Boor original full-text claim. SciPy is a secondary numerical companion; the rational second-derivative system is the independent reference.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Natural and clamped splines versus PCHIP

Compare C2 continuity and shape preservation on three fixed data sets: a monotone plateau, a cubic and a straight line.

**Methods used**

- [Spline interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/splines/?lang=en) (`splines`)
- [PCHIP monotone cubic Hermite interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/pchip/?lang=en) (`pchip`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=en#spline-shape-controls-en-algorithm)

Solve a cubic B-spline collocation system and evaluate it with de Boor recursion. A separate path implements PCHIP harmonic slopes, endpoint limiting and Hermite evaluation.

$$
S_i(s)=a_i+b_i*s+c_i*s^2+d_i*s^3
$$

$$
d_k=(w_1+w_2)/(w_1/m_(k-1)+w_2/m_k)
$$

$$
S_natural(1.5)=a-9*(b-a)/88; S_clamped(1.5)=a-15*(b-a)/152
$$

- [Cubic splines and shape-preserving interpolation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#cubic-spline-pchip-en) (`cubic-spline-pchip`)

Use actual binary64 knots and values. Natural conditions set both endpoint second derivatives to zero; clamped conditions prescribe the first derivatives from the input.


**Problem figure**

![Natural and clamped splines versus PCHIP: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Natural and clamped splines versus PCHIP](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=en) (`spline-shape-controls`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=en#spline-shape-controls-en-validation)

Compare with exact rational second-derivative systems, rational PCHIP and SciPy 1.14.1. Fifteen endpoint records contain sixteen scalar outputs from thirteen distinct inputs. Independent Fraction formulas show plateau undershoot for the actual binary64 data.

- [Natural and clamped splines versus PCHIP](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-spline-shape-controls-en) (`spline-shape-controls`; Same-problem reference · Analytic reference)

PCHIP is generally C1, not necessarily C2. Best approximation, extrapolation and noise smoothing are outside scope. A SciPy comparison does not substitute for reading the original papers.
## Assumptions, units and boundaries

Use actual binary64 knots and values. Natural conditions set both endpoint second derivatives to zero; clamped conditions prescribe the first derivatives from the input.

**Editorial clarification**

PCHIP is generally C1, not necessarily C2. Best approximation, extrapolation and noise smoothing are outside scope. A SciPy comparison does not substitute for reading the original papers.

## Adopted numerical method

Solve a cubic B-spline collocation system and evaluate it with de Boor recursion. A separate path implements PCHIP harmonic slopes, endpoint limiting and Hermite evaluation.

$$
S_i(s)=a_i+b_i*s+c_i*s^2+d_i*s^3
$$

$$
d_k=(w_1+w_2)/(w_1/m_(k-1)+w_2/m_k)
$$

$$
S_natural(1.5)=a-9*(b-a)/88; S_clamped(1.5)=a-15*(b-a)/152
$$

## References and validation

Compare with exact rational second-derivative systems, rational PCHIP and SciPy 1.14.1. Fifteen endpoint records contain sixteen scalar outputs from thirteen distinct inputs. Independent Fraction formulas show plateau undershoot for the actual binary64 data.

## Limits

PCHIP is generally C1, not necessarily C2. Best approximation, extrapolation and noise smoothing are outside scope. A SciPy comparison does not substitute for reading the original papers.

## Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_value_scaled_reference_defect": 2.9409263239818476e-16,
    "maximum_derivative_scaled_reference_defect": 5.2306043094691055e-15,
    "endpoint_fixture_records": 15,
    "endpoint_scalar_outputs": 16,
    "endpoint_distinct_datasets": 13
  },
  "checks": {
    "reference:endpoint-branch-values": true,
    "reference:endpoint-record-count": true,
    "reference:endpoint-output-count": true,
    "reference:endpoint-distinct-datasets": true,
    "reference:negative-natural-witness": true,
    "reference:negative-clamped-witness": true,
    "plateau-natural:finite": true,
    "plateau-natural:value-reference": true,
    "plateau-natural:derivative-reference": true,
    "plateau-natural:nodal": true,
    "plateau-natural:boundary-or-shape": true,
    "plateau-clamped:finite": true,
    "plateau-clamped:value-reference": true,
    "plateau-clamped:derivative-reference": true,
    "plateau-clamped:nodal": true,
    "plateau-clamped:boundary-or-shape": true,
    "reference:pchip-actual-input-plateau": true,
    "plateau-pchip:finite": true,
    "plateau-pchip:value-reference": true,
    "plateau-pchip:derivative-reference": true,
    "plateau-pchip:nodal": true,
    "plateau-pchip:boundary-or-shape": true,
    "cubic-natural:finite": true,
    "cubic-natural:value-reference": true,
    "cubic-natural:derivative-reference": true,
    "cubic-natural:nodal": true,
    "cubic-natural:boundary-or-shape": true,
    "cubic-clamped:finite": true,
    "cubic-clamped:value-reference": true,
    "cubic-clamped:derivative-reference": true,
    "cubic-clamped:nodal": true,
    "cubic-clamped:boundary-or-shape": true,
    "cubic-pchip:finite": true,
    "cubic-pchip:value-reference": true,
    "cubic-pchip:derivative-reference": true,
    "cubic-pchip:nodal": true,
    "cubic-pchip:boundary-or-shape": true,
    "linear-natural:finite": true,
    "linear-natural:value-reference": true,
    "linear-natural:derivative-reference": true,
    "linear-natural:nodal": true,
    "linear-natural:boundary-or-shape": true,
    "linear-clamped:finite": true,
    "linear-clamped:value-reference": true,
    "linear-clamped:derivative-reference": true,
    "linear-clamped:nodal": true,
    "linear-clamped:boundary-or-shape": true,
    "linear-pchip:finite": true,
    "linear-pchip:value-reference": true,
    "linear-pchip:derivative-reference": true,
    "linear-pchip:nodal": true,
    "linear-pchip:boundary-or-shape": true,
    "reference:exact-piece-continuity": true,
    "reference:polynomial-cubic-clamped": true,
    "reference:polynomial-linear-natural": true,
    "reference:polynomial-linear-clamped": true,
    "fixed-fit-count": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/index.json

![Compare C2 continuity and shape preservation on three fixed data sets: a monotone plateau, a cubic and a straight line. Drawn from saved arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-preview.png)

Compare C2 continuity and shape preservation on three fixed data sets: a monotone plateau, a cubic and a straight line. Drawn from saved arrays.

![Saved errors, derivatives or squared norms shown separately. The text states the scope of each boundary and representation.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-diagnostics.png)

Saved errors, derivatives or squared norms shown separately. The text states the scope of each boundary and representation.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- SciPy 1.14.1 PCHIP documentation and selected source [accessed 2026-11-25]. https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/interpolate/_cubic.py; review_level=official-source-selected-lines
Selected lines 202–225, 243–254, 275–298: harmonic interior derivatives, endpoint sign and 3-slope limiter, two-point case. The original Fritsch–Butland paper has not been read in full. Own formulas are independently expressed as scalar Hermite polynomials.

- SciPy 1.14.1 BSpline and CubicSpline documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.interpolate.CubicSpline.html; review_level=official-documentation-selected-definitions
Natural and clamped boundary conditions and the BSpline recurrence were read during preparation. No de Boor original full-text claim. SciPy is a secondary numerical companion; the rational second-derivative system is the independent reference.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
