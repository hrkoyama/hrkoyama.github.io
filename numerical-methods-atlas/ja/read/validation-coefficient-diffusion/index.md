# 係数ジャンプ・回転異方性のMG／AMG

同じ行列の幾何MG・SA-AMG・直接解と、連続問題の解析解・別離散参照を分けて比較します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 係数ジャンプ拡散：共有流束とMG・AMG

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
### 前提・単位・境界

単位正方形、零Dirichlet、f=1、対角2象限100/残り1、N16/32/64。参照P1は128/192。

**編集上の補足**

係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。

### 採用した計算法

直交FVの共有面調和平均。幾何MGと座標を受け取らないSA-AMGの対称Galerkin V-cycleを、同じ行列のPCGへ適用。

$$
-\nabla\cdot(a\nabla u)=1,\quad a\in\{1,100\}
$$

$$
T_f=|f|/(d_L/a_L+d_R/a_R)
$$

### 比較・検証

非零2材料流束パッチ、残差に整合する収支、直接解の前進/energy誤差、独立三角形P1参照の格子感度。

### 確認の限界

係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- Two-point flux approximation. https://dumux.org/docs/doxygen/master/group___c_c_tpfa_discretization.html; review_level=selected-official-derivation-read
Scalar harmonic transmissibility, shared flux and K-orthogonality restriction. No DuMux code executed.

- BoomerAMG: smoother options. https://hypre.readthedocs.io/en/latest/solvers-boomeramg.html; review_level=selected-official-documentation-read
CG requires a symmetric smoother. Our educational SA code is not hypre and no hypre code was run.

- Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems. https://link.springer.com/article/10.1007/BF02238511; review_level=publisher-abstract-only-full-paper-unread
Metadata and abstract only. No general robustness theorem claimed for these fixed jumps/tensors.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 回転異方性拡散：完全テンソルQ1とMG・AMG

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
### 前提・単位・境界

単位正方形、零Dirichlet、K=R(pi/6)diag(1,.01)Rᵀ、厳密解sin(pi x)sin(pi y)、N16/32/64。

**編集上の補足**

指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。

### 採用した計算法

完全2×2テンソルQ1とGauss積分。MG/SA-AMGは対称2/2Jacobi、Galerkin粗行列、粗CholeskyでSPDの固定適用。

$$
-\nabla\cdot(K\nabla u)=f,\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

$$
f=\pi^2(K_{xx}+K_{yy})\sin\pi x\sin\pi y-2\pi^2K_{xy}\cos\pi x\cos\pi y
$$

### 比較・検証

u=xy,f=−2Kxyパッチ、解析流束由来のsource、積分L2/energy誤差と4/6点求積感度、直接解との比較。

### 確認の限界

指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- Two-point flux approximation. https://dumux.org/docs/doxygen/master/group___c_c_tpfa_discretization.html; review_level=selected-official-derivation-read
Scalar harmonic transmissibility, shared flux and K-orthogonality restriction. No DuMux code executed.

- BoomerAMG: smoother options. https://hypre.readthedocs.io/en/latest/solvers-boomeramg.html; review_level=selected-official-documentation-read
CG requires a symmetric smoother. Our educational SA code is not hypre and no hypre code was run.

- Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems. https://link.springer.com/article/10.1007/BF02238511; review_level=publisher-abstract-only-full-paper-unread
Metadata and abstract only. No general robustness theorem claimed for these fixed jumps/tensors.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
