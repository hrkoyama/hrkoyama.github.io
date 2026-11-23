# 純Neumannの互換条件と平均値ゲージ

特異な2D Poissonを互換条件と指定平均込みで解き、不適合な外力を拒否します。

**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [共役勾配法](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja) (`cg`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja#poisson-neumann-ja-algorithm)

共有面差分で特異行列を組み、体積重み平均のLagrange拘束付き疎直接法とcompatible CGを照合。物理的な不適合外力の平均を勝手に引かない。

$$
-\Delta u=f,\quad\partial_nu=g_N,\quad\int f=-\oint g_N
$$

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`)

単位正方形N16/32/64、セル中心の点DOF。cos(2pi x)cos(2pi y)、全壁Neumann0、平均0とN32の平均.25診断。


**問題の図**

![純Neumannの互換条件と平均値ゲージ：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja) (`poisson-neumann`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja#poisson-neumann-ja-validation)

L2細分化、零空間、平均、CG差、source+1拒否、境界流束/体積源の収支を保存。

- [純Neumann：解析場・互換条件・平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-neumann-ja) (`poisson-neumann`; 同じ問題の参照 · 製造解)

同じ半離散系の別線形解法は独立PDE参照ではありません。既存Dirichlet MGの成功や2D任意境界へ一般化しません。
## 前提・単位・境界

単位正方形N16/32/64、セル中心の点DOF。cos(2pi x)cos(2pi y)、全壁Neumann0、平均0とN32の平均.25診断。

**編集上の補足**

同じ半離散系の別線形解法は独立PDE参照ではありません。既存Dirichlet MGの成功や2D任意境界へ一般化しません。

## 採用した計算法

共有面差分で特異行列を組み、体積重み平均のLagrange拘束付き疎直接法とcompatible CGを照合。物理的な不適合外力の平均を勝手に引かない。

$$
-\Delta u=f,\quad\partial_nu=g_N,\quad\int f=-\oint g_N
$$

## 比較・検証

L2細分化、零空間、平均、CG差、source+1拒否、境界流束/体積源の収支を保存。

## 確認の限界

同じ半離散系の別線形解法は独立PDE参照ではありません。既存Dirichlet MGの成功や2D任意境界へ一般化しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "n": 64,
    "mean": 0.0,
    "l2": 0.0004017888396835558,
    "linf": 0.0008016429562934801,
    "residual": 1.6410484082740595e-15,
    "compatibility": 1.474514954580286e-17,
    "mean_error": 7.160477722908953e-17,
    "nullspace_defect": 0.0,
    "solver_gap": 1.0436096431476471e-14,
    "lagrange_multiplier": -2.2436555307051445e-15,
    "boundary_residual": 0.0,
    "boundary_flux_error": 0.0,
    "flux_balance": 1.474514954580286e-17,
    "symmetry": 0.0,
    "gauge_shift_error": 3.774758283725532e-15
  },
  "checks": {
    "neumann-n16 residual": true,
    "neumann-n16 boundary_residual": true,
    "neumann-n16 flux_balance": true,
    "neumann-n16 symmetry": true,
    "neumann-n16 compatibility": true,
    "neumann-n16 mean_error": true,
    "neumann-n16 nullspace_defect": true,
    "neumann-n16 solver_gap": true,
    "neumann-n32 residual": true,
    "neumann-n32 boundary_residual": true,
    "neumann-n32 flux_balance": true,
    "neumann-n32 symmetry": true,
    "neumann-n32 compatibility": true,
    "neumann-n32 mean_error": true,
    "neumann-n32 nullspace_defect": true,
    "neumann-n32 solver_gap": true,
    "neumann-n64 residual": true,
    "neumann-n64 boundary_residual": true,
    "neumann-n64 flux_balance": true,
    "neumann-n64 symmetry": true,
    "neumann-n64 compatibility": true,
    "neumann-n64 mean_error": true,
    "neumann-n64 nullspace_defect": true,
    "neumann-n64 solver_gap": true,
    "L2 refinement 1": true,
    "L2 refinement 2": true,
    "finest L2": true,
    "mean gauge shifts only constant": true,
    "incompatible source rejected without projection": true,
    "analytic Cartesian stress/source identity": true,
    "analytic annulus no-slip trace": true,
    "analytic corner analytic gradient": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/index.json

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png)

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

- PETSc developers (n.d.). KSP: Solving Singular Systems. https://petsc.org/main/manual/ksp/; review_level=selected-official-section

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Pure Neumann compatibility and mean gauge

Solve singular2D Poisson with compatibility/gauge and reject incompatible source.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Conjugate gradients](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en) (`cg`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en#poisson-neumann-en-algorithm)

Shared-face differences, weighted-mean augmented solve and compatible CG comparison; no physical RHS mean projection.

$$
-\Delta u=f,\quad\partial_nu=g_N,\quad\int f=-\oint g_N
$$

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`)

Unit square N16/32/64, cell-centred point DOFs, cosine exact field, homogeneous Neumann; mean0 andN32 mean.25 probe.


**Problem figure**

![Pure Neumann compatibility and mean gauge: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en) (`poisson-neumann`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en#poisson-neumann-en-validation)

Retain L2 refinement, nullspace/gauge/CG gap, source+1 rejection and boundary/source budget.

- [Pure Neumann: analytic field, compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-neumann-en) (`poisson-neumann`; Same-problem reference · Manufactured solution)

A different linear solver of the same matrix is not an independent PDE discretization; no general boundary/MG claim.
## Assumptions, units and boundaries

Unit square N16/32/64, cell-centred point DOFs, cosine exact field, homogeneous Neumann; mean0 andN32 mean.25 probe.

**Editorial clarification**

A different linear solver of the same matrix is not an independent PDE discretization; no general boundary/MG claim.

## Adopted numerical method

Shared-face differences, weighted-mean augmented solve and compatible CG comparison; no physical RHS mean projection.

$$
-\Delta u=f,\quad\partial_nu=g_N,\quad\int f=-\oint g_N
$$

## References and validation

Retain L2 refinement, nullspace/gauge/CG gap, source+1 rejection and boundary/source budget.

## Limits

A different linear solver of the same matrix is not an independent PDE discretization; no general boundary/MG claim.

## Stored measurements and decisions

```json
{
  "metrics": {
    "n": 64,
    "mean": 0.0,
    "l2": 0.0004017888396835558,
    "linf": 0.0008016429562934801,
    "residual": 1.6410484082740595e-15,
    "compatibility": 1.474514954580286e-17,
    "mean_error": 7.160477722908953e-17,
    "nullspace_defect": 0.0,
    "solver_gap": 1.0436096431476471e-14,
    "lagrange_multiplier": -2.2436555307051445e-15,
    "boundary_residual": 0.0,
    "boundary_flux_error": 0.0,
    "flux_balance": 1.474514954580286e-17,
    "symmetry": 0.0,
    "gauge_shift_error": 3.774758283725532e-15
  },
  "checks": {
    "neumann-n16 residual": true,
    "neumann-n16 boundary_residual": true,
    "neumann-n16 flux_balance": true,
    "neumann-n16 symmetry": true,
    "neumann-n16 compatibility": true,
    "neumann-n16 mean_error": true,
    "neumann-n16 nullspace_defect": true,
    "neumann-n16 solver_gap": true,
    "neumann-n32 residual": true,
    "neumann-n32 boundary_residual": true,
    "neumann-n32 flux_balance": true,
    "neumann-n32 symmetry": true,
    "neumann-n32 compatibility": true,
    "neumann-n32 mean_error": true,
    "neumann-n32 nullspace_defect": true,
    "neumann-n32 solver_gap": true,
    "neumann-n64 residual": true,
    "neumann-n64 boundary_residual": true,
    "neumann-n64 flux_balance": true,
    "neumann-n64 symmetry": true,
    "neumann-n64 compatibility": true,
    "neumann-n64 mean_error": true,
    "neumann-n64 nullspace_defect": true,
    "neumann-n64 solver_gap": true,
    "L2 refinement 1": true,
    "L2 refinement 2": true,
    "finest L2": true,
    "mean gauge shifts only constant": true,
    "incompatible source rejected without projection": true,
    "analytic Cartesian stress/source identity": true,
    "analytic annulus no-slip trace": true,
    "analytic corner analytic gradient": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/index.json

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png)

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

- PETSc developers (n.d.). KSP: Solving Singular Systems. https://petsc.org/main/manual/ksp/; review_level=selected-official-section

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
