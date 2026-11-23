# 2D混合Robinの製造解と境界流束

2D PoissonのNeumann/Robin面を実際に組み、連続製造解と境界fluxを照合します。

**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja#poisson-robin-ja-algorithm)

半セル距離を用いてRobin境界値を消去し、外向きgradientの面積積分を離散式と同じ重みで評価。

$$
\alpha u_b+\beta\partial_nu=g,\quad\partial_nu=(g-\alpha u_i)/(\beta+\alpha h/2)
$$

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`)

単位正方形N16/32/64、u=cos(pi x)cos(2pi y)+x+y。x壁Neumann±1、y壁alpha1,beta.5の解析Robin。


**問題の図**

![2D混合Robinの製造解と境界流束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2D混合Robinの製造解と境界流束](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja) (`poisson-robin`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja#poisson-robin-ja-validation)

2D解/誤差、真の残差、Robin関係残差と解析法線flux誤差、3格子細分化と積分収支を保存。

- [混合Robin：2次元解析場と独立な法線流束](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-robin-ja) (`poisson-robin`; 同じ問題の参照 · 製造解)

Robin問題は一意なので平均ゲージを重ねません。境界条件の代数残差と物理flux精度を区別します。
## 前提・単位・境界

単位正方形N16/32/64、u=cos(pi x)cos(2pi y)+x+y。x壁Neumann±1、y壁alpha1,beta.5の解析Robin。

**編集上の補足**

Robin問題は一意なので平均ゲージを重ねません。境界条件の代数残差と物理flux精度を区別します。

## 採用した計算法

半セル距離を用いてRobin境界値を消去し、外向きgradientの面積積分を離散式と同じ重みで評価。

$$
\alpha u_b+\beta\partial_nu=g,\quad\partial_nu=(g-\alpha u_i)/(\beta+\alpha h/2)
$$

## 比較・検証

2D解/誤差、真の残差、Robin関係残差と解析法線flux誤差、3格子細分化と積分収支を保存。

## 確認の限界

Robin問題は一意なので平均ゲージを重ねません。境界条件の代数残差と物理flux精度を区別します。

## 保存実測値と判定

```json
{
  "metrics": {
    "n": 64,
    "mean": 0.0,
    "l2": 0.00037706113250587296,
    "linf": 0.0008911573863470412,
    "residual": 5.729791641151394e-15,
    "compatibility": 3.9384615384615382,
    "mean_error": 0.0,
    "nullspace_defect": 0.0,
    "solver_gap": 0.0,
    "lagrange_multiplier": 0.0,
    "boundary_residual": 4.440892098500626e-16,
    "boundary_flux_error": 0.0006164157489298994,
    "flux_balance": 1.6335890973273592e-13,
    "symmetry": 0.0
  },
  "checks": {
    "robin-n16 residual": true,
    "robin-n16 boundary_residual": true,
    "robin-n16 flux_balance": true,
    "robin-n16 symmetry": true,
    "robin-n32 residual": true,
    "robin-n32 boundary_residual": true,
    "robin-n32 flux_balance": true,
    "robin-n32 symmetry": true,
    "robin-n64 residual": true,
    "robin-n64 boundary_residual": true,
    "robin-n64 flux_balance": true,
    "robin-n64 symmetry": true,
    "L2 refinement 1": true,
    "L2 refinement 2": true,
    "finest L2": true,
    "boundary flux refinement 1": true,
    "boundary flux refinement 2": true,
    "finest boundary flux": true,
    "analytic Cartesian stress/source identity": true,
    "analytic annulus no-slip trace": true,
    "analytic corner analytic gradient": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/index.json

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin-preview.png)

実際に保存した計算配列と固定入力の収束指標から描いた検証図。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/attempts/01/source/inputs.json

## 出典と確認範囲

- MFEM developers (n.d.). Boundary Conditions: Robin boundary conditions. https://mfem.org/fem_bc/; review_level=selected-official-equations

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# 2D mixed Robin MMS and boundary flux

Assemble actual2D Neumann/Robin faces and compare the manufactured field and boundary flux.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en#poisson-robin-en-algorithm)

Eliminate Robin trace at half-cell distance, using the same outward-gradient face weights in the discrete PDE and budget.

$$
\alpha u_b+\beta\partial_nu=g,\quad\partial_nu=(g-\alpha u_i)/(\beta+\alpha h/2)
$$

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`)

Unit square N16/32/64; cosine-plus-linear exact field. x walls Neumann±1; y walls analytic Robin alpha1,beta.5.


**Problem figure**

![2D mixed Robin MMS and boundary flux: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[2D mixed Robin MMS and boundary flux](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en) (`poisson-robin`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en#poisson-robin-en-validation)

Save2D solution/errors, true residuals, Robin relation and analytic normal-flux errors, three-grid refinement and integral budget.

- [Mixed Robin: 2D analytic field and independent normal flux](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-robin-en) (`poisson-robin`; Same-problem reference · Manufactured solution)

The unique Robin problem has no additional mean gauge. Algebraic boundary satisfaction differs from physical flux accuracy.
## Assumptions, units and boundaries

Unit square N16/32/64; cosine-plus-linear exact field. x walls Neumann±1; y walls analytic Robin alpha1,beta.5.

**Editorial clarification**

The unique Robin problem has no additional mean gauge. Algebraic boundary satisfaction differs from physical flux accuracy.

## Adopted numerical method

Eliminate Robin trace at half-cell distance, using the same outward-gradient face weights in the discrete PDE and budget.

$$
\alpha u_b+\beta\partial_nu=g,\quad\partial_nu=(g-\alpha u_i)/(\beta+\alpha h/2)
$$

## References and validation

Save2D solution/errors, true residuals, Robin relation and analytic normal-flux errors, three-grid refinement and integral budget.

## Limits

The unique Robin problem has no additional mean gauge. Algebraic boundary satisfaction differs from physical flux accuracy.

## Stored measurements and decisions

```json
{
  "metrics": {
    "n": 64,
    "mean": 0.0,
    "l2": 0.00037706113250587296,
    "linf": 0.0008911573863470412,
    "residual": 5.729791641151394e-15,
    "compatibility": 3.9384615384615382,
    "mean_error": 0.0,
    "nullspace_defect": 0.0,
    "solver_gap": 0.0,
    "lagrange_multiplier": 0.0,
    "boundary_residual": 4.440892098500626e-16,
    "boundary_flux_error": 0.0006164157489298994,
    "flux_balance": 1.6335890973273592e-13,
    "symmetry": 0.0
  },
  "checks": {
    "robin-n16 residual": true,
    "robin-n16 boundary_residual": true,
    "robin-n16 flux_balance": true,
    "robin-n16 symmetry": true,
    "robin-n32 residual": true,
    "robin-n32 boundary_residual": true,
    "robin-n32 flux_balance": true,
    "robin-n32 symmetry": true,
    "robin-n64 residual": true,
    "robin-n64 boundary_residual": true,
    "robin-n64 flux_balance": true,
    "robin-n64 symmetry": true,
    "L2 refinement 1": true,
    "L2 refinement 2": true,
    "finest L2": true,
    "boundary flux refinement 1": true,
    "boundary flux refinement 2": true,
    "finest boundary flux": true,
    "analytic Cartesian stress/source identity": true,
    "analytic annulus no-slip trace": true,
    "analytic corner analytic gradient": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/index.json

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin-preview.png)

Validation preview from actual saved PDE arrays and fixed-input refinement measurements.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/attempts/01/source/inputs.json

## Sources and review scope

- MFEM developers (n.d.). Boundary Conditions: Robin boundary conditions. https://mfem.org/fem_bc/; review_level=selected-official-equations

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
