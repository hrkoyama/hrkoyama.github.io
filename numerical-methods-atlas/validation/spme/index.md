# Bスプラインsmooth PMEの格子・次数収束

電荷をBスプラインで格子へ割り当て、FFTでEwald逆空間項を評価するsmooth PME（SPME）の小規模例です。

**使用手法**

- [Particle Mesh Ewald（PME）](https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/?lang=ja) (`pme`)
- [Smooth PME（SPME）](https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=ja) (`spme`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=ja#spme-ja-algorithm)

4次または6次のcardinal Bスプラインのテンソル積で電荷を格子化し、節点スプラインの離散構造因子補正、Gaussian Green関数、3次元FFTを組み合わせます。格子エネルギーを重みの位置微分で解析的に微分します。

$$
Q_{\mathbf j}=\sum_iq_i\prod_{a=1}^3M_p(u_{ia}-j_a+p/2)
$$

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Bスプラインsmooth PMEの格子・次数収束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/spme.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[中性周期点電荷：Ewald・smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja) (`neutral-periodic-charges`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=ja#spme-ja-validation)

16³・24³・40³格子と2つの次数で、直接Ewald逆空間和との差を記録します。Ewaldと実空間項・自己項を共有する部分も明示。最細格子の力はエネルギー差分とも比較し、全電荷の保持を確認します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

Ewaldと同じ中性立方セルと実空間項を使います。PME族のうちEssmannらのBスプライン変種を採用し、Dardenらの原法のLagrange補間とは区別します。

## 採用した計算法

4次または6次のcardinal Bスプラインのテンソル積で電荷を格子化し、節点スプラインの離散構造因子補正、Gaussian Green関数、3次元FFTを組み合わせます。格子エネルギーを重みの位置微分で解析的に微分します。

$$
Q_{\mathbf j}=\sum_iq_i\prod_{a=1}^3M_p(u_{ia}-j_a+p/2)
$$

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

## 比較・検証

16³・24³・40³格子と2つの次数で、直接Ewald逆空間和との差を記録します。Ewaldと実空間項・自己項を共有する部分も明示。最細格子の力はエネルギー差分とも比較し、全電荷の保持を確認します。

## 確認の限界

有限格子のaliasingにより、エネルギー勾配型の合力は厳密にはゼロでなく、その診断量を保存します。運動量保存・長時間MD・原法PME・最適化P³M・スラブ補正の検証ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "force_error": 7.855116843202836e-06,
    "energy_error": 8.183940956030256e-07,
    "finest_to_coarsest_force_ratio": 0.0062278365701822136,
    "charge_error": 2.1871393585115584e-14,
    "finite_difference_error": 2.6557447796449196e-08,
    "net_force": 1.919342197087559e-05
  },
  "checks": {
    "force_error": true,
    "energy_error": true,
    "finest_to_coarsest_force_ratio": true,
    "charge_error": true,
    "finite_difference_error": true,
    "both_orders_refine": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- T. Darden, D. York and L. Pedersen (1993). Particle mesh Ewald: An N·log(N) method for Ewald sums in large systems. https://doi.org/10.1063/1.464397; review_level=abstract-and-metadata
  原著PDFの冒頭と抄録を確認。歴史的なPME原法であり、実装したBスプライン変種とは区別。
- U. Essmann, L. Perera, M. L. Berkowitz, T. Darden, H. Lee and L. G. Pedersen (1995). A smooth particle mesh Ewald method. https://doi.org/10.1063/1.470117; review_level=selected-full-text
  原著PDFのBスプライン構造因子・FFT・解析勾配に関わる部分と抄録を確認。全ベンチマークの再現ではありません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Mesh/order convergence of B-spline smooth PME

A small smooth-PME example assigns charge with B-splines and evaluates the Ewald reciprocal contribution by FFT.

**Methods used**

- [Particle mesh Ewald / PME](https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/?lang=en) (`pme`)
- [Smooth particle mesh Ewald / SPME](https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=en) (`spme`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=en#spme-en-algorithm)

Tensor-product cardinal splines of order four or six spread the charges. Apply the nodal-spline discrete structure-factor correction and Gaussian Green function through 3D FFTs; analytically differentiate assignment weights for forces.

$$
Q_{\mathbf j}=\sum_iq_i\prod_{a=1}^3M_p(u_{ia}-j_a+p/2)
$$

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Mesh/order convergence of B-spline smooth PME: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/spme.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Neutral periodic charges: Ewald and smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en) (`neutral-periodic-charges`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=en#spme-en-validation)

Meshes 16³/24³/40³ and two orders are compared with directly summed Ewald reciprocal terms. Shared real/self terms are stated. Check finest-grid force derivatives by energy differences and verify assigned total charge.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

The neutral cubic cell and real-space term match the Ewald example. The adopted PME-family variant uses Essmann-type B-splines, distinct from Darden’s original Lagrange interpolation.

## Adopted numerical method

Tensor-product cardinal splines of order four or six spread the charges. Apply the nodal-spline discrete structure-factor correction and Gaussian Green function through 3D FFTs; analytically differentiate assignment weights for forces.

$$
Q_{\mathbf j}=\sum_iq_i\prod_{a=1}^3M_p(u_{ia}-j_a+p/2)
$$

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

## References and validation

Meshes 16³/24³/40³ and two orders are compared with directly summed Ewald reciprocal terms. Shared real/self terms are stated. Check finest-grid force derivatives by energy differences and verify assigned total charge.

## Limits

Finite-mesh aliasing permits nonzero net force for this energy-gradient variant; that diagnostic is reported. No exact momentum conservation, long MD, original PME, optimized P³M or slab validation is claimed.

## Stored measurements and decisions

```json
{
  "metrics": {
    "force_error": 7.855116843202836e-06,
    "energy_error": 8.183940956030256e-07,
    "finest_to_coarsest_force_ratio": 0.0062278365701822136,
    "charge_error": 2.1871393585115584e-14,
    "finite_difference_error": 2.6557447796449196e-08,
    "net_force": 1.919342197087559e-05
  },
  "checks": {
    "force_error": true,
    "energy_error": true,
    "finest_to_coarsest_force_ratio": true,
    "charge_error": true,
    "finite_difference_error": true,
    "both_orders_refine": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- T. Darden, D. York and L. Pedersen (1993). Particle mesh Ewald: An N·log(N) method for Ewald sums in large systems. https://doi.org/10.1063/1.464397; review_level=abstract-and-metadata
  Original PDF opening and abstract checked; historical original PME is distinguished from the implemented B-spline variant.
- U. Essmann, L. Perera, M. L. Berkowitz, T. Darden, H. Lee and L. G. Pedersen (1995). A smooth particle mesh Ewald method. https://doi.org/10.1063/1.470117; review_level=selected-full-text
  Original PDF abstract and selected spline/structure-factor, FFT and analytic-gradient material checked; not a reproduction of every paper benchmark.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
