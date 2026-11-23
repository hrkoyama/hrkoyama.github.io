# 回転異方性拡散：完全テンソルQ1とMG・AMG

非零Kxyを保つQ1弱形式で、解析解への収束と同じ行列のMG・AMG収束を比較します。

**使用手法**

- [Q1有限要素法（スカラー拡散・曲線座標ベクトルBVP）](https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=ja) (`q1-fem`)
- [幾何マルチグリッドVサイクル](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja) (`multigrid`)
- [代数的マルチグリッド（AMG）](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja) (`amg`)
- [共役勾配法](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja) (`cg`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja#rotated-anisotropic-diffusion-ja-algorithm)

完全2×2テンソルQ1とGauss積分。MG/SA-AMGは対称2/2Jacobi、Galerkin粗行列、粗CholeskyでSPDの固定適用。

$$
-\nabla\cdot(K\nabla u)=f,\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

$$
f=\pi^2(K_{xx}+K_{yy})\sin\pi x\sin\pi y-2\pi^2K_{xy}\cos\pi x\cos\pi y
$$

- [不連続係数・完全テンソル拡散の境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#tensor-diffusion-ja) (`tensor-diffusion`)

単位正方形、零Dirichlet、K=R(pi/6)diag(1,.01)Rᵀ、厳密解sin(pi x)sin(pi y)、N16/32/64。


**問題の図**

![回転異方性拡散：完全テンソルQ1とMG・AMG：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja) (`rotated-anisotropic-diffusion`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja#rotated-anisotropic-diffusion-ja-validation)

u=xy,f=−2Kxyパッチ、解析流束由来のsource、積分L2/energy誤差と4/6点求積感度、直接解との比較。

- [回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rotated-anisotropic-diffusion-ja) (`rotated-anisotropic-diffusion`; 同じ問題の参照 · 製造解)

指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。
## 前提・単位・境界

単位正方形、零Dirichlet、K=R(pi/6)diag(1,.01)Rᵀ、厳密解sin(pi x)sin(pi y)、N16/32/64。

**編集上の補足**

指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。

## 採用した計算法

完全2×2テンソルQ1とGauss積分。MG/SA-AMGは対称2/2Jacobi、Galerkin粗行列、粗CholeskyでSPDの固定適用。

$$
-\nabla\cdot(K\nabla u)=f,\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

$$
f=\pi^2(K_{xx}+K_{yy})\sin\pi x\sin\pi y-2\pi^2K_{xy}\cos\pi x\cos\pi y
$$

## 比較・検証

u=xy,f=−2Kxyパッチ、解析流束由来のsource、積分L2/energy誤差と4/6点求積感度、直接解との比較。

## 確認の限界

指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "continuous_errors": [
      0.0043094975495807045,
      0.0010835497491345043,
      0.0002713461470266456
    ],
    "reference_sensitivity": []
  },
  "checks": {
    "n16_quadrature": true,
    "n16_symmetry": true,
    "n16_geometric_converged": true,
    "n16_geometric_true_residual": true,
    "n16_geometric_forward": true,
    "n16_geometric_energy": true,
    "n16_geometric_history": true,
    "n16_amg_converged": true,
    "n16_amg_true_residual": true,
    "n16_amg_forward": true,
    "n16_amg_energy": true,
    "n16_amg_history": true,
    "n32_quadrature": true,
    "n32_symmetry": true,
    "n32_geometric_converged": true,
    "n32_geometric_true_residual": true,
    "n32_geometric_forward": true,
    "n32_geometric_energy": true,
    "n32_geometric_history": true,
    "n32_amg_converged": true,
    "n32_amg_true_residual": true,
    "n32_amg_forward": true,
    "n32_amg_energy": true,
    "n32_amg_history": true,
    "n64_quadrature": true,
    "n64_symmetry": true,
    "n64_geometric_converged": true,
    "n64_geometric_true_residual": true,
    "n64_geometric_forward": true,
    "n64_geometric_energy": true,
    "n64_geometric_history": true,
    "n64_amg_converged": true,
    "n64_amg_true_residual": true,
    "n64_amg_forward": true,
    "n64_amg_energy": true,
    "n64_amg_history": true,
    "refinement": true,
    "l2_refinement_ratios": true,
    "finest_l2": true,
    "affine_patch": true,
    "xy_patch": true,
    "small_operator_spd": true,
    "geometric_small_cycle_spd": true,
    "amg_small_cycle_spd": true,
    "intentional_budget": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/index.json

![保存した2D解・誤差・真の残差・格子感度の検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion-preview.png)

保存した2D解・誤差・真の残差・格子感度の検証図。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Two-point flux approximation. https://dumux.org/docs/doxygen/master/group___c_c_tpfa_discretization.html; review_level=selected-official-derivation-read
Scalar harmonic transmissibility, shared flux and K-orthogonality restriction. No DuMux code executed.

- BoomerAMG: smoother options. https://hypre.readthedocs.io/en/latest/solvers-boomeramg.html; review_level=selected-official-documentation-read
CG requires a symmetric smoother. Our educational SA code is not hypre and no hypre code was run.

- Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems. https://link.springer.com/article/10.1007/BF02238511; review_level=publisher-abstract-only-full-paper-unread
Metadata and abstract only. No general robustness theorem claimed for these fixed jumps/tensors.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Rotated diffusion: full-tensor Q1, MG and AMG

Retain nonzero Kxy in the Q1 weak form and compare analytic refinement with MG/AMG convergence for the same matrix.

**Methods used**

- [Q1 FEM for scalar diffusion and mapped vector BVPs](https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=en) (`q1-fem`)
- [Geometric multigrid V-cycle](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en) (`multigrid`)
- [Algebraic multigrid / AMG](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en) (`amg`)
- [Conjugate gradients](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en) (`cg`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en#rotated-anisotropic-diffusion-en-algorithm)

Full2x2 tensor Q1 and Gauss quadrature. Fixed SPD MG/SA cycles use symmetric2/2Jacobi, Galerkin operators and coarse Cholesky.

$$
-\nabla\cdot(K\nabla u)=f,\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

$$
f=\pi^2(K_{xx}+K_{yy})\sin\pi x\sin\pi y-2\pi^2K_{xy}\cos\pi x\cos\pi y
$$

- [Discontinuous and full-tensor diffusion BVP](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#tensor-diffusion-en) (`tensor-diffusion`)

Unit square, zero Dirichlet, K=R(pi/6)diag(1,.01)R^T, exact sin(pi x)sin(pi y), N16/32/64.


**Problem figure**

![Rotated diffusion: full-tensor Q1, MG and AMG: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en) (`rotated-anisotropic-diffusion`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en#rotated-anisotropic-diffusion-en-validation)

u=xy,f=-2Kxy patch, analytic-flux source, integrated L2/energy error,4/6point quadrature sensitivity and direct-solve comparison.

- [Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rotated-anisotropic-diffusion-en) (`rotated-anisotropic-diffusion`; Same-problem reference · Manufactured solution)

One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.
## Assumptions, units and boundaries

Unit square, zero Dirichlet, K=R(pi/6)diag(1,.01)R^T, exact sin(pi x)sin(pi y), N16/32/64.

**Editorial clarification**

One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.

## Adopted numerical method

Full2x2 tensor Q1 and Gauss quadrature. Fixed SPD MG/SA cycles use symmetric2/2Jacobi, Galerkin operators and coarse Cholesky.

$$
-\nabla\cdot(K\nabla u)=f,\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

$$
f=\pi^2(K_{xx}+K_{yy})\sin\pi x\sin\pi y-2\pi^2K_{xy}\cos\pi x\cos\pi y
$$

## References and validation

u=xy,f=-2Kxy patch, analytic-flux source, integrated L2/energy error,4/6point quadrature sensitivity and direct-solve comparison.

## Limits

One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.

## Stored measurements and decisions

```json
{
  "metrics": {
    "continuous_errors": [
      0.0043094975495807045,
      0.0010835497491345043,
      0.0002713461470266456
    ],
    "reference_sensitivity": []
  },
  "checks": {
    "n16_quadrature": true,
    "n16_symmetry": true,
    "n16_geometric_converged": true,
    "n16_geometric_true_residual": true,
    "n16_geometric_forward": true,
    "n16_geometric_energy": true,
    "n16_geometric_history": true,
    "n16_amg_converged": true,
    "n16_amg_true_residual": true,
    "n16_amg_forward": true,
    "n16_amg_energy": true,
    "n16_amg_history": true,
    "n32_quadrature": true,
    "n32_symmetry": true,
    "n32_geometric_converged": true,
    "n32_geometric_true_residual": true,
    "n32_geometric_forward": true,
    "n32_geometric_energy": true,
    "n32_geometric_history": true,
    "n32_amg_converged": true,
    "n32_amg_true_residual": true,
    "n32_amg_forward": true,
    "n32_amg_energy": true,
    "n32_amg_history": true,
    "n64_quadrature": true,
    "n64_symmetry": true,
    "n64_geometric_converged": true,
    "n64_geometric_true_residual": true,
    "n64_geometric_forward": true,
    "n64_geometric_energy": true,
    "n64_geometric_history": true,
    "n64_amg_converged": true,
    "n64_amg_true_residual": true,
    "n64_amg_forward": true,
    "n64_amg_energy": true,
    "n64_amg_history": true,
    "refinement": true,
    "l2_refinement_ratios": true,
    "finest_l2": true,
    "affine_patch": true,
    "xy_patch": true,
    "small_operator_spd": true,
    "geometric_small_cycle_spd": true,
    "amg_small_cycle_spd": true,
    "intentional_budget": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/index.json

![Saved2D solution, error, true residual and refinement/reference sensitivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion-preview.png)

Saved2D solution, error, true residual and refinement/reference sensitivity.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Two-point flux approximation. https://dumux.org/docs/doxygen/master/group___c_c_tpfa_discretization.html; review_level=selected-official-derivation-read
Scalar harmonic transmissibility, shared flux and K-orthogonality restriction. No DuMux code executed.

- BoomerAMG: smoother options. https://hypre.readthedocs.io/en/latest/solvers-boomeramg.html; review_level=selected-official-documentation-read
CG requires a symmetric smoother. Our educational SA code is not hypre and no hypre code was run.

- Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems. https://link.springer.com/article/10.1007/BF02238511; review_level=publisher-abstract-only-full-paper-unread
Metadata and abstract only. No general robustness theorem claimed for these fixed jumps/tensors.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
