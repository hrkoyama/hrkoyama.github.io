# 係数ジャンプ拡散：共有流束とMG・AMG

不連続係数のFV解を独立なP1参照と比較し、線形系の残差・前進誤差と連続問題の誤差を分けます。

**使用手法**

- [幾何マルチグリッドVサイクル](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja) (`multigrid`)
- [代数的マルチグリッド（AMG）](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja) (`amg`)
- [共役勾配法](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja) (`cg`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja#checkerboard-diffusion-ja-algorithm)

直交FVの共有面調和平均。幾何MGと座標を受け取らないSA-AMGの対称Galerkin V-cycleを、同じ行列のPCGへ適用。

$$
-\nabla\cdot(a\nabla u)=1,\quad a\in\{1,100\}
$$

$$
T_f=|f|/(d_L/a_L+d_R/a_R)
$$

- [不連続係数・完全テンソル拡散の境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#tensor-diffusion-ja) (`tensor-diffusion`)

単位正方形、零Dirichlet、f=1、対角2象限100/残り1、N16/32/64。参照P1は128/192。


**問題の図**

![係数ジャンプ拡散：共有流束とMG・AMG：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja) (`checkerboard-diffusion`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja#checkerboard-diffusion-ja-validation)

非零2材料流束パッチ、残差に整合する収支、直接解の前進/energy誤差、独立三角形P1参照の格子感度。

- [係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-checkerboard-diffusion-ja) (`checkerboard-diffusion`; 同じ問題の参照 · 有限格子の数値参照)

係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。
## 前提・単位・境界

単位正方形、零Dirichlet、f=1、対角2象限100/残り1、N16/32/64。参照P1は128/192。

**編集上の補足**

係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。

## 採用した計算法

直交FVの共有面調和平均。幾何MGと座標を受け取らないSA-AMGの対称Galerkin V-cycleを、同じ行列のPCGへ適用。

$$
-\nabla\cdot(a\nabla u)=1,\quad a\in\{1,100\}
$$

$$
T_f=|f|/(d_L/a_L+d_R/a_R)
$$

## 比較・検証

非零2材料流束パッチ、残差に整合する収支、直接解の前進/energy誤差、独立三角形P1参照の格子感度。

## 確認の限界

係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "continuous_errors": [
      0.03320269631288309,
      0.008587452847326224,
      0.002547591920168387
    ],
    "reference_sensitivity": [
      0.00010935677943053456,
      0.0001088242415134897,
      0.00034850805399045157
    ]
  },
  "checks": {
    "n16_symmetry": true,
    "n16_geometric_converged": true,
    "n16_geometric_true_residual": true,
    "n16_geometric_forward": true,
    "n16_geometric_energy": true,
    "n16_geometric_history": true,
    "n16_geometric_flux_ledger": true,
    "n16_geometric_budget_residual_bound": true,
    "n16_amg_converged": true,
    "n16_amg_true_residual": true,
    "n16_amg_forward": true,
    "n16_amg_energy": true,
    "n16_amg_history": true,
    "n16_amg_flux_ledger": true,
    "n16_amg_budget_residual_bound": true,
    "n32_symmetry": true,
    "n32_geometric_converged": true,
    "n32_geometric_true_residual": true,
    "n32_geometric_forward": true,
    "n32_geometric_energy": true,
    "n32_geometric_history": true,
    "n32_geometric_flux_ledger": true,
    "n32_geometric_budget_residual_bound": true,
    "n32_amg_converged": true,
    "n32_amg_true_residual": true,
    "n32_amg_forward": true,
    "n32_amg_energy": true,
    "n32_amg_history": true,
    "n32_amg_flux_ledger": true,
    "n32_amg_budget_residual_bound": true,
    "n64_symmetry": true,
    "n64_geometric_converged": true,
    "n64_geometric_true_residual": true,
    "n64_geometric_forward": true,
    "n64_geometric_energy": true,
    "n64_geometric_history": true,
    "n64_geometric_flux_ledger": true,
    "n64_geometric_budget_residual_bound": true,
    "n64_amg_converged": true,
    "n64_amg_true_residual": true,
    "n64_amg_forward": true,
    "n64_amg_energy": true,
    "n64_amg_history": true,
    "n64_amg_flux_ledger": true,
    "n64_amg_budget_residual_bound": true,
    "refinement": true,
    "reference_sensitivity": true,
    "nonzero_harmonic_patch": true,
    "small_operator_spd": true,
    "geometric_small_cycle_spd": true,
    "amg_small_cycle_spd": true,
    "intentional_budget": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/index.json

![保存した2D解・誤差・真の残差・格子感度の検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion-preview.png)

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

# Checkerboard diffusion: shared flux, MG and AMG

Compare discontinuous-coefficient FV with independent P1 reference fields, separating linear-system residual/forward errors from continuum error.

**Methods used**

- [Geometric multigrid V-cycle](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en) (`multigrid`)
- [Algebraic multigrid / AMG](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en) (`amg`)
- [Conjugate gradients](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en) (`cg`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en#checkerboard-diffusion-en-algorithm)

Orthogonal FV with shared harmonic transmissibility. Symmetric Galerkin geometric and coordinate-free SA cycles precondition PCG on identical matrices.

$$
-\nabla\cdot(a\nabla u)=1,\quad a\in\{1,100\}
$$

$$
T_f=|f|/(d_L/a_L+d_R/a_R)
$$

- [Discontinuous and full-tensor diffusion BVP](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#tensor-diffusion-en) (`tensor-diffusion`)

Unit square, zero Dirichlet, f=1, diagonal quadrants100/others1, N16/32/64; reference P1 meshes128/192.


**Problem figure**

![Checkerboard diffusion: shared flux, MG and AMG: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en) (`checkerboard-diffusion`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en#checkerboard-diffusion-en-validation)

Nonzero two-material flux patch, residual-aware budget, direct forward/energy errors and independent triangular-P1 grid sensitivity.

- [Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-checkerboard-diffusion-en) (`checkerboard-diffusion`; Same-problem reference · Finite-grid numerical reference)

Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted.
## Assumptions, units and boundaries

Unit square, zero Dirichlet, f=1, diagonal quadrants100/others1, N16/32/64; reference P1 meshes128/192.

**Editorial clarification**

Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted.

## Adopted numerical method

Orthogonal FV with shared harmonic transmissibility. Symmetric Galerkin geometric and coordinate-free SA cycles precondition PCG on identical matrices.

$$
-\nabla\cdot(a\nabla u)=1,\quad a\in\{1,100\}
$$

$$
T_f=|f|/(d_L/a_L+d_R/a_R)
$$

## References and validation

Nonzero two-material flux patch, residual-aware budget, direct forward/energy errors and independent triangular-P1 grid sensitivity.

## Limits

Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted.

## Stored measurements and decisions

```json
{
  "metrics": {
    "continuous_errors": [
      0.03320269631288309,
      0.008587452847326224,
      0.002547591920168387
    ],
    "reference_sensitivity": [
      0.00010935677943053456,
      0.0001088242415134897,
      0.00034850805399045157
    ]
  },
  "checks": {
    "n16_symmetry": true,
    "n16_geometric_converged": true,
    "n16_geometric_true_residual": true,
    "n16_geometric_forward": true,
    "n16_geometric_energy": true,
    "n16_geometric_history": true,
    "n16_geometric_flux_ledger": true,
    "n16_geometric_budget_residual_bound": true,
    "n16_amg_converged": true,
    "n16_amg_true_residual": true,
    "n16_amg_forward": true,
    "n16_amg_energy": true,
    "n16_amg_history": true,
    "n16_amg_flux_ledger": true,
    "n16_amg_budget_residual_bound": true,
    "n32_symmetry": true,
    "n32_geometric_converged": true,
    "n32_geometric_true_residual": true,
    "n32_geometric_forward": true,
    "n32_geometric_energy": true,
    "n32_geometric_history": true,
    "n32_geometric_flux_ledger": true,
    "n32_geometric_budget_residual_bound": true,
    "n32_amg_converged": true,
    "n32_amg_true_residual": true,
    "n32_amg_forward": true,
    "n32_amg_energy": true,
    "n32_amg_history": true,
    "n32_amg_flux_ledger": true,
    "n32_amg_budget_residual_bound": true,
    "n64_symmetry": true,
    "n64_geometric_converged": true,
    "n64_geometric_true_residual": true,
    "n64_geometric_forward": true,
    "n64_geometric_energy": true,
    "n64_geometric_history": true,
    "n64_geometric_flux_ledger": true,
    "n64_geometric_budget_residual_bound": true,
    "n64_amg_converged": true,
    "n64_amg_true_residual": true,
    "n64_amg_forward": true,
    "n64_amg_energy": true,
    "n64_amg_history": true,
    "n64_amg_flux_ledger": true,
    "n64_amg_budget_residual_bound": true,
    "refinement": true,
    "reference_sensitivity": true,
    "nonzero_harmonic_patch": true,
    "small_operator_spd": true,
    "geometric_small_cycle_spd": true,
    "amg_small_cycle_spd": true,
    "intentional_budget": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/index.json

![Saved2D solution, error, true residual and refinement/reference sensitivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion-preview.png)

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
