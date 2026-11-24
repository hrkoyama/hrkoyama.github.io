# 節点・表現・丸めを分けるRunge補間

Runge関数と絶対値関数を等間隔・Lobatto型の固定節点で補間し、Clenshaw評価と比較します。

**使用手法**

- [Chebyshev近似](https://hrkoyama.github.io/numerical-methods-atlas/methods/chebyshev/?lang=ja) (`chebyshev`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=ja#runge-barycentric-clenshaw-ja-algorithm)

第2重心公式と全係数Clenshaw漸化式を自作。丸め済み節点上の閉形式重みと有限Chebyshev変換をそのまま保存します。

$$
p(x)=sum_j y_j*prod_(k!=j)((x-x_k)/(x_j-x_k))
$$

$$
R(x)=(sum_j w_j*y_j/(x-x_j))/(sum_j w_j/(x-x_j))
$$

$$
C(x)=sum_(k=0)^n a_k*T_k(x); b_k=a_k+2*x*b_(k+1)-b_(k+2)
$$

- [格納節点の多項式補間](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#polynomial-interpolation-ja) (`polynomial-interpolation`)

無次元区間[-1,1]、次数8・16・32、固定2048中点。節点・データ・重みは実際のbinary64値を対象にします。


**問題の図**

![節点・表現・丸めを分けるRunge補間：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[節点・表現・丸めを分けるRunge補間](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=ja) (`runge-barycentric-clenshaw`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=ja#runge-barycentric-clenshaw-ja-validation)

格納値の補間多項式P、閉重み有理式R、格納係数級数C、目標関数fを区別。17点の正確な有理参照・演算別誤差上界・節点一致・固定Runge傾向を照合します。

- [節点・表現・丸めを分けるRunge補間](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-runge-barycentric-clenshaw-ja) (`runge-barycentric-clenshaw`; 同じ問題の参照 · 解析参照)

標本最大誤差は連続一様ノルムの証明ではありません。丸め節点の閉重み・離散直交性は厳密と見なしません。任意次数・任意点の安定性は保証しません。
## 前提・単位・境界

無次元区間[-1,1]、次数8・16・32、固定2048中点。節点・データ・重みは実際のbinary64値を対象にします。

**編集上の補足**

標本最大誤差は連続一様ノルムの証明ではありません。丸め節点の閉重み・離散直交性は厳密と見なしません。任意次数・任意点の安定性は保証しません。

## 採用した計算法

第2重心公式と全係数Clenshaw漸化式を自作。丸め済み節点上の閉形式重みと有限Chebyshev変換をそのまま保存します。

$$
p(x)=sum_j y_j*prod_(k!=j)((x-x_k)/(x_j-x_k))
$$

$$
R(x)=(sum_j w_j*y_j/(x-x_j))/(sum_j w_j/(x-x_j))
$$

$$
C(x)=sum_(k=0)^n a_k*T_k(x); b_k=a_k+2*x*b_(k+1)-b_(k+2)
$$

## 比較・検証

格納値の補間多項式P、閉重み有理式R、格納係数級数C、目標関数fを区別。17点の正確な有理参照・演算別誤差上界・節点一致・固定Runge傾向を照合します。

## 確認の限界

標本最大誤差は連続一様ノルムの証明ではありません。丸め節点の閉重み・離散直交性は厳密と見なしません。任意次数・任意点の安定性は保証しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "max_node_table_cosine_defect": 1.6816803605601774e-16,
    "maximum_sampled_function_error": 105718.65676159713,
    "reference_certificate_probes_per_interpolant": 17,
    "coefficient_sets": 6
  },
  "checks": {
    "reference:fixed-cosine-node-table": true,
    "runge-equispaced-8:finite": true,
    "runge-equispaced-8:node-hit-identity": true,
    "runge-equispaced-8:barycentric-operation-certificate": true,
    "runge-lobatto-8:clenshaw-operation-certificate": true,
    "runge-lobatto-8:finite": true,
    "runge-lobatto-8:node-hit-identity": true,
    "runge-lobatto-8:barycentric-operation-certificate": true,
    "runge-equispaced-16:finite": true,
    "runge-equispaced-16:node-hit-identity": true,
    "runge-equispaced-16:barycentric-operation-certificate": true,
    "runge-lobatto-16:clenshaw-operation-certificate": true,
    "runge-lobatto-16:finite": true,
    "runge-lobatto-16:node-hit-identity": true,
    "runge-lobatto-16:barycentric-operation-certificate": true,
    "runge-equispaced-32:finite": true,
    "runge-equispaced-32:node-hit-identity": true,
    "runge-equispaced-32:barycentric-operation-certificate": true,
    "runge-lobatto-32:clenshaw-operation-certificate": true,
    "runge-lobatto-32:finite": true,
    "runge-lobatto-32:node-hit-identity": true,
    "runge-lobatto-32:barycentric-operation-certificate": true,
    "absolute-equispaced-8:finite": true,
    "absolute-equispaced-8:node-hit-identity": true,
    "absolute-equispaced-8:barycentric-operation-certificate": true,
    "absolute-lobatto-8:clenshaw-operation-certificate": true,
    "absolute-lobatto-8:finite": true,
    "absolute-lobatto-8:node-hit-identity": true,
    "absolute-lobatto-8:barycentric-operation-certificate": true,
    "absolute-equispaced-16:finite": true,
    "absolute-equispaced-16:node-hit-identity": true,
    "absolute-equispaced-16:barycentric-operation-certificate": true,
    "absolute-lobatto-16:clenshaw-operation-certificate": true,
    "absolute-lobatto-16:finite": true,
    "absolute-lobatto-16:node-hit-identity": true,
    "absolute-lobatto-16:barycentric-operation-certificate": true,
    "absolute-equispaced-32:finite": true,
    "absolute-equispaced-32:node-hit-identity": true,
    "absolute-equispaced-32:barycentric-operation-certificate": true,
    "absolute-lobatto-32:clenshaw-operation-certificate": true,
    "absolute-lobatto-32:finite": true,
    "absolute-lobatto-32:node-hit-identity": true,
    "absolute-lobatto-32:barycentric-operation-certificate": true,
    "reference:polynomial-control-equispaced": true,
    "reference:polynomial-control-lobatto": true,
    "runge:equispaced-growth": true,
    "runge:lobatto-refinement": true,
    "fixed-record-and-coefficient-count": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/index.json

![Runge関数と絶対値関数を等間隔・Lobatto型の固定節点で補間し、Clenshaw評価と比較します。 保存配列から作図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-preview.png)

Runge関数と絶対値関数を等間隔・Lobatto型の固定節点で補間し、Clenshaw評価と比較します。 保存配列から作図。

![保存済み誤差・導関数または二乗ノルムを別表示。各境界・表現の適用範囲は本文を参照。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-diagnostics.png)

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

- NIST DLMF §3.11(ii): Chebyshev series and Clenshaw summation [accessed 2026-11-25]. https://dlmf.nist.gov/3.11; review_level=official-reference-selected-equations
Selected E7, E9, E11 and E15 with endpoint-halving conventions; no original Clenshaw paper reading. The implementation uses full coefficients, so its final combination is derived explicitly.

- SciPy 1.14.1 BarycentricInterpolator documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.interpolate.BarycentricInterpolator.html; review_level=official-documentation-selected-notes
Selected barycentric formula and interpolation-conditioning notes read during the preceding preparation. The Berrut–Trefethen paper is a bibliographic lead, not a full-text reading.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Runge interpolation: nodes, representation and rounding

Interpolate the Runge and absolute-value functions on fixed equispaced and Lobatto-like nodes, and compare with Clenshaw evaluation.

**Methods used**

- [Chebyshev approximation](https://hrkoyama.github.io/numerical-methods-atlas/methods/chebyshev/?lang=en) (`chebyshev`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=en#runge-barycentric-clenshaw-en-algorithm)

Implement the second barycentric formula and a full-coefficient Clenshaw recurrence. Retain the closed weights and finite Chebyshev transform on rounded nodes.

$$
p(x)=sum_j y_j*prod_(k!=j)((x-x_k)/(x_j-x_k))
$$

$$
R(x)=(sum_j w_j*y_j/(x-x_j))/(sum_j w_j/(x-x_j))
$$

$$
C(x)=sum_(k=0)^n a_k*T_k(x); b_k=a_k+2*x*b_(k+1)-b_(k+2)
$$

- [Polynomial interpolation on stored nodes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#polynomial-interpolation-en) (`polynomial-interpolation`)

Dimensionless interval [-1,1], degrees 8, 16 and 32, and 2048 fixed midpoints. Actual binary64 nodes, data and weights define the discrete problem.


**Problem figure**

![Runge interpolation: nodes, representation and rounding: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Runge interpolation: nodes, representation and rounding](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=en) (`runge-barycentric-clenshaw`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=en#runge-barycentric-clenshaw-en-validation)

Separate the stored-data polynomial P, closed-weight rational expression R, stored-coefficient series C and target f. Check exact rational references at 17 probes, operation-based error bounds, node identities and fixed Runge trends.

- [Runge interpolation: nodes, representation and rounding](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-runge-barycentric-clenshaw-en) (`runge-barycentric-clenshaw`; Same-problem reference · Analytic reference)

A sampled maximum error is not a proof of a continuous uniform norm. Closed weights and discrete orthogonality on rounded nodes are not treated as exact. No arbitrary-degree or all-point stability guarantee is made.
## Assumptions, units and boundaries

Dimensionless interval [-1,1], degrees 8, 16 and 32, and 2048 fixed midpoints. Actual binary64 nodes, data and weights define the discrete problem.

**Editorial clarification**

A sampled maximum error is not a proof of a continuous uniform norm. Closed weights and discrete orthogonality on rounded nodes are not treated as exact. No arbitrary-degree or all-point stability guarantee is made.

## Adopted numerical method

Implement the second barycentric formula and a full-coefficient Clenshaw recurrence. Retain the closed weights and finite Chebyshev transform on rounded nodes.

$$
p(x)=sum_j y_j*prod_(k!=j)((x-x_k)/(x_j-x_k))
$$

$$
R(x)=(sum_j w_j*y_j/(x-x_j))/(sum_j w_j/(x-x_j))
$$

$$
C(x)=sum_(k=0)^n a_k*T_k(x); b_k=a_k+2*x*b_(k+1)-b_(k+2)
$$

## References and validation

Separate the stored-data polynomial P, closed-weight rational expression R, stored-coefficient series C and target f. Check exact rational references at 17 probes, operation-based error bounds, node identities and fixed Runge trends.

## Limits

A sampled maximum error is not a proof of a continuous uniform norm. Closed weights and discrete orthogonality on rounded nodes are not treated as exact. No arbitrary-degree or all-point stability guarantee is made.

## Stored measurements and decisions

```json
{
  "metrics": {
    "max_node_table_cosine_defect": 1.6816803605601774e-16,
    "maximum_sampled_function_error": 105718.65676159713,
    "reference_certificate_probes_per_interpolant": 17,
    "coefficient_sets": 6
  },
  "checks": {
    "reference:fixed-cosine-node-table": true,
    "runge-equispaced-8:finite": true,
    "runge-equispaced-8:node-hit-identity": true,
    "runge-equispaced-8:barycentric-operation-certificate": true,
    "runge-lobatto-8:clenshaw-operation-certificate": true,
    "runge-lobatto-8:finite": true,
    "runge-lobatto-8:node-hit-identity": true,
    "runge-lobatto-8:barycentric-operation-certificate": true,
    "runge-equispaced-16:finite": true,
    "runge-equispaced-16:node-hit-identity": true,
    "runge-equispaced-16:barycentric-operation-certificate": true,
    "runge-lobatto-16:clenshaw-operation-certificate": true,
    "runge-lobatto-16:finite": true,
    "runge-lobatto-16:node-hit-identity": true,
    "runge-lobatto-16:barycentric-operation-certificate": true,
    "runge-equispaced-32:finite": true,
    "runge-equispaced-32:node-hit-identity": true,
    "runge-equispaced-32:barycentric-operation-certificate": true,
    "runge-lobatto-32:clenshaw-operation-certificate": true,
    "runge-lobatto-32:finite": true,
    "runge-lobatto-32:node-hit-identity": true,
    "runge-lobatto-32:barycentric-operation-certificate": true,
    "absolute-equispaced-8:finite": true,
    "absolute-equispaced-8:node-hit-identity": true,
    "absolute-equispaced-8:barycentric-operation-certificate": true,
    "absolute-lobatto-8:clenshaw-operation-certificate": true,
    "absolute-lobatto-8:finite": true,
    "absolute-lobatto-8:node-hit-identity": true,
    "absolute-lobatto-8:barycentric-operation-certificate": true,
    "absolute-equispaced-16:finite": true,
    "absolute-equispaced-16:node-hit-identity": true,
    "absolute-equispaced-16:barycentric-operation-certificate": true,
    "absolute-lobatto-16:clenshaw-operation-certificate": true,
    "absolute-lobatto-16:finite": true,
    "absolute-lobatto-16:node-hit-identity": true,
    "absolute-lobatto-16:barycentric-operation-certificate": true,
    "absolute-equispaced-32:finite": true,
    "absolute-equispaced-32:node-hit-identity": true,
    "absolute-equispaced-32:barycentric-operation-certificate": true,
    "absolute-lobatto-32:clenshaw-operation-certificate": true,
    "absolute-lobatto-32:finite": true,
    "absolute-lobatto-32:node-hit-identity": true,
    "absolute-lobatto-32:barycentric-operation-certificate": true,
    "reference:polynomial-control-equispaced": true,
    "reference:polynomial-control-lobatto": true,
    "runge:equispaced-growth": true,
    "runge:lobatto-refinement": true,
    "fixed-record-and-coefficient-count": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/index.json

![Interpolate the Runge and absolute-value functions on fixed equispaced and Lobatto-like nodes, and compare with Clenshaw evaluation. Drawn from saved arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-preview.png)

Interpolate the Runge and absolute-value functions on fixed equispaced and Lobatto-like nodes, and compare with Clenshaw evaluation. Drawn from saved arrays.

![Saved errors, derivatives or squared norms shown separately. The text states the scope of each boundary and representation.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-diagnostics.png)

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

- NIST DLMF §3.11(ii): Chebyshev series and Clenshaw summation [accessed 2026-11-25]. https://dlmf.nist.gov/3.11; review_level=official-reference-selected-equations
Selected E7, E9, E11 and E15 with endpoint-halving conventions; no original Clenshaw paper reading. The implementation uses full coefficients, so its final combination is derived explicitly.

- SciPy 1.14.1 BarycentricInterpolator documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.interpolate.BarycentricInterpolator.html; review_level=official-documentation-selected-notes
Selected barycentric formula and interpolation-conditioning notes read during the preceding preparation. The Berrut–Trefethen paper is a bibliographic lead, not a full-text reading.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
