# 球面浅水波の軸対称定常釣合いを時間積分

球面浅水波の軸対称な無次元定常状態を実際に時間積分し、釣合い残差と格子依存を分ける。

**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=ja#sphere-zonal-balance-ja-algorithm)

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

- [球面浅水波の軸対称部分問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#spherical-shallow-water-ja) (`spherical-shallow-water`)

a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。


**問題の図**

![球面浅水波の軸対称定常釣合いを時間積分：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sphere-zonal-balance.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[球面浅水波の軸対称定常釣合いを時間積分](https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/?lang=ja) (`sphere-zonal-balance`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=ja#sphere-zonal-balance-ja-validation)

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

- [球面浅水波の軸対称定常釣合いを時間積分](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sphere-zonal-balance-ja) (`sphere-zonal-balance`; 同じ問題の参照 · 解析参照)

固定入力の式・参照・図と実行コードを対応付けます。 a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。
## 前提・単位・境界

球面浅水波の軸対称な無次元部分問題です。運動量の原始変数は子午線方向の中心差分、質量は緯度帯の面流束による有限体積形で離散化し、RK4で時間積分します。極の質量流束をゼロとし、平衡残差の差し引きや補正は行いません。固定入力・境界・参照の範囲はinputs.jsonを参照。

**編集上の補足**

a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。

## 採用した計算法

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

## 比較・検証

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

## 確認の限界

限定した教育用モデルです。元論文の全条件・全アルゴリズムや一般的な性能の再現ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "finest": {
      "grid": 64,
      "h_error": 0.00010108962138506427,
      "initial_balance_residual": 0.0018041320580228781,
      "analytic_force_residual": 0.0,
      "mass_defect": 0.0,
      "minimum_h": 8.87466665967074,
      "steps": 129
    }
  },
  "checks": {
    "analytic_balance": true,
    "balance_order": true,
    "height": true,
    "refinement": true,
    "mass": true,
    "positive": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. https://arxiv.org/pdf/astro-ph/0206401; review_level=selected-original-author-paper-sections-and-equations
- New Third-Order Finite Volume Unequal-Sized WENO Lagrangian Schemes for Solving Euler Equations. https://www.mdpi.com/2227-7390/11/23/4842; review_level=selected-publisher-fulltext-example-8
- Second Order Corner Coupled Upwind Transport Methods for Lagrangian Hydrodynamics. https://www.osti.gov/servlets/purl/15005665; review_level=secondary-bibliographic-identity-original-report-unread
- A standard test set for numerical approximations to the shallow water equations in spherical geometry. https://digital.library.unt.edu/ark:/67531/metadc1069483/; review_level=author-report-bibliography-and-abstract-original-formulas-unread
- Cascade interpolation for semi-Lagrangian advection over the sphere. https://www.image.ucar.edu/staff/rnair/qj99_sph.pdf; review_level=selected-author-hosted-formulas-and-publisher-bibliography

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Time evolution of axisymmetric spherical shallow-water balance

NondimensionalWilliamson2-type axisymmetricsubproblem. Analyticstaticstatevsactualtimeintegration; not fullglobaldynamicalcore/PVclaim.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=en#sphere-zonal-balance-en-algorithm)

NondimensionalWilliamson2-type axisymmetricsubproblem. Analyticstaticstatevsactualtimeintegration; not fullglobaldynamicalcore/PVclaim.

- [Axisymmetric spherical shallow-water subproblem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#spherical-shallow-water-en) (`spherical-shallow-water`)

Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.


**Problem figure**

![Time evolution of axisymmetric spherical shallow-water balance: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sphere-zonal-balance.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Time evolution of axisymmetric spherical shallow-water balance](https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/?lang=en) (`sphere-zonal-balance`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=en#sphere-zonal-balance-en-validation)

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

- [Time evolution of axisymmetric spherical shallow-water balance](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sphere-zonal-balance-en) (`sphere-zonal-balance`; Same-problem reference · Analytic reference)

Bind the fixed-input formula, reference, figure and executable code. Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.
## Assumptions, units and boundaries

Nondimensional axisymmetric spherical SWE subproblem. Hybrid centered meridional differences for primitive momentum and latitude-band finite-volume face fluxes for mass, advanced by RK4. Pole mass flux is zero; no equilibrium residual subtraction or correction. Fixed inputs, boundaries and reference scope are specified in inputs.json.

**Editorial clarification**

Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.

## Adopted numerical method

NondimensionalWilliamson2-type axisymmetricsubproblem. Analyticstaticstatevsactualtimeintegration; not fullglobaldynamicalcore/PVclaim.

## References and validation

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

## Limits

NondimensionalWilliamson2-type axisymmetricsubproblem. Analyticstaticstatevsactualtimeintegration; not fullglobaldynamicalcore/PVclaim.

## Stored measurements and decisions

```json
{
  "metrics": {
    "finest": {
      "grid": 64,
      "h_error": 0.00010108962138506427,
      "initial_balance_residual": 0.0018041320580228781,
      "analytic_force_residual": 0.0,
      "mass_defect": 0.0,
      "minimum_h": 8.87466665967074,
      "steps": 129
    }
  },
  "checks": {
    "analytic_balance": true,
    "balance_order": true,
    "height": true,
    "refinement": true,
    "mass": true,
    "positive": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. https://arxiv.org/pdf/astro-ph/0206401; review_level=selected-original-author-paper-sections-and-equations
- New Third-Order Finite Volume Unequal-Sized WENO Lagrangian Schemes for Solving Euler Equations. https://www.mdpi.com/2227-7390/11/23/4842; review_level=selected-publisher-fulltext-example-8
- Second Order Corner Coupled Upwind Transport Methods for Lagrangian Hydrodynamics. https://www.osti.gov/servlets/purl/15005665; review_level=secondary-bibliographic-identity-original-report-unread
- A standard test set for numerical approximations to the shallow water equations in spherical geometry. https://digital.library.unt.edu/ark:/67531/metadc1069483/; review_level=author-report-bibliography-and-abstract-original-formulas-unread
- Cascade interpolation for semi-Lagrangian advection over the sphere. https://www.image.ucar.edu/staff/rnair/qj99_sph.pdf; review_level=selected-author-hosted-formulas-and-publisher-bibliography

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
