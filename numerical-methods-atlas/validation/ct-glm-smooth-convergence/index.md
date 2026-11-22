# CT・GLM：移動する磁気静力学平衡の格子・時間収束

非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。

**使用手法**

- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) (`ct`)
- [GLM発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja) (`glm`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja#ct-glm-smooth-convergence-ja-algorithm)

両法とも区分定数・同じ固定Rusanov速度α=3・前進Eulerです。CTは面Bと共有算術corner EMF、GLMはcell B/ψとch=3・物理減衰率κ=2を使用。全格子で同じ384刻み、両法のdt列も同一です。CT面平均から復元した初期cell BとGLM初期Bが一致します。

$$
A=a[\cos k(x-ut)+\cos k(y-vt)],\quad\mathbf B=(A_y,-A_x),\quad J_z=-\Delta A=k^2A
$$

$$
p=p_0+\tfrac12k^2A^2,\qquad\nabla p=J_z\nabla A=\mathbf J\times\mathbf B
$$

$$
\bar{\mathbf U}_{ij}=\frac1{\Delta x\Delta y}\int_{K_{ij}}\mathbf U\,dx\,dy,\qquad p(\bar{\mathbf U})\ne\bar p
$$

$$
\mathbf U^{m+1}=\mathbf U^m+\Delta t\,L_h(\mathbf U^m),\qquad C_{\rm sum}=\alpha\Delta t(\Delta x^{-1}+\Delta y^{-1})
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![CT・GLM：移動する磁気静力学平衡の格子・時間収束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[CT・GLM：移動する磁気静力学平衡の格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=ja) (`advected-magnetostatic-equilibrium`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja#ct-glm-smooth-convergence-ja-validation)

16²/32²/64²の保存変数L1/L2/L∞誤差と観測次数を測ります。最細格子の刻み倍増差を空間誤差の.1以下と比較。時間収束は固定8²で16/32/64/128刻みを、許容誤差・最大刻みを二重に細分したDOP853へ照合します。質量・E、正値性、native CT divと共通cell div、ψも記録します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

周期単位正方形、γ=5/3、μ₀=1、平面MHD。A=.05[cos2π(x−.3t)+cos2π(y−.2t)]、B=(Ay,−Ax)、ρ=1、v=(.3,.2)、p=.1+(2π)²A²/2、t=.1。保存変数の解析的セル平均を比較します。公刊の標準問題名を借りない構成検証例です。

**編集上の補足**

この滑らかな移流平衡はアトラスで構成した厳密解です。保存量のセル平均を比較し、そのセル平均から回復する圧力と圧力自体の厳密なセル平均を区別します。同じ半離散空間演算子に別の時間積分を適用した参照は、時間誤差の照合であり独立PDEソルバーとは呼びません。

## 採用した計算法

両法とも区分定数・同じ固定Rusanov速度α=3・前進Eulerです。CTは面Bと共有算術corner EMF、GLMはcell B/ψとch=3・物理減衰率κ=2を使用。全格子で同じ384刻み、両法のdt列も同一です。CT面平均から復元した初期cell BとGLM初期Bが一致します。

$$
A=a[\cos k(x-ut)+\cos k(y-vt)],\quad\mathbf B=(A_y,-A_x),\quad J_z=-\Delta A=k^2A
$$

$$
p=p_0+\tfrac12k^2A^2,\qquad\nabla p=J_z\nabla A=\mathbf J\times\mathbf B
$$

$$
\bar{\mathbf U}_{ij}=\frac1{\Delta x\Delta y}\int_{K_{ij}}\mathbf U\,dx\,dy,\qquad p(\bar{\mathbf U})\ne\bar p
$$

$$
\mathbf U^{m+1}=\mathbf U^m+\Delta t\,L_h(\mathbf U^m),\qquad C_{\rm sum}=\alpha\Delta t(\Delta x^{-1}+\Delta y^{-1})
$$

## 比較・検証

16²/32²/64²の保存変数L1/L2/L∞誤差と観測次数を測ります。最細格子の刻み倍増差を空間誤差の.1以下と比較。時間収束は固定8²で16/32/64/128刻みを、許容誤差・最大刻みを二重に細分したDOP853へ照合します。質量・E、正値性、native CT divと共通cell div、ψも記録します。

## 確認の限界

定数LLF粘性・周期中心演算子では、GLMのdiv=ψ=0部分空間は丸めまで保たれます。本例は結合MHDの精度を調べ、能動的cleaningは別の非物理診断対照で調べます。p(q平均)はpの厳密平均と同一ではありません。DOP853は時間だけ独立で空間RHSは共有します。刻み倍増差は経験的汚染目安で厳密誤差上界ではなく、CT/GLMの内部表現差を含む有限離散化全体の比較です。

## 保存実測値と判定

```json
{
  "metrics": {
    "initial_cell_state_linf_difference": 0.0,
    "ct_finest_spatial_error": 0.030434862760674048,
    "ct_minimum_spatial_order": 0.8792002695252499,
    "ct_time_contamination_ratio": 0.00042240836130500326,
    "ct_finest_temporal_scaled_l2": 0.00028691666346522787,
    "ct_minimum_temporal_order": 1.003588237880181,
    "ct_time_reference_to_primary_ratio": 1.0480281669324549e-12,
    "glm_finest_spatial_error": 0.053272941712543334,
    "glm_minimum_spatial_order": 0.8519970902037858,
    "glm_time_contamination_ratio": 0.0002497746629066176,
    "glm_finest_temporal_scaled_l2": 0.0006005455648426271,
    "glm_minimum_temporal_order": 1.004074134741654,
    "glm_time_reference_to_primary_ratio": 4.049255315353574e-13
  },
  "checks": {
    "identical_initial_cell_states": true,
    "ct_native_constraint_n16": true,
    "ct_native_constraint_n32": true,
    "ct_native_constraint_n64": true,
    "ct_spatial_order": true,
    "ct_continuum_error": true,
    "ct_common_divergence_bounded": true,
    "ct_time_contamination_bounded": true,
    "ct_positive_states": true,
    "ct_conservative_mass_energy": true,
    "glm_spatial_order": true,
    "glm_continuum_error": true,
    "glm_common_divergence_bounded": true,
    "glm_time_contamination_bounded": true,
    "glm_positive_states": true,
    "glm_conservative_mass_energy": true,
    "ct_temporal_order": true,
    "ct_temporal_error": true,
    "ct_temporal_reference_resolved": true,
    "glm_temporal_order": true,
    "glm_temporal_error": true,
    "glm_temporal_reference_resolved": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs-initial.json

## 出典と確認範囲

- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; selected original equations 17–19 and 24, pp.650–651
  通常のGLMのB/ψ式と減衰、エネルギー保存、追加のEGLM項との区別を原著の選択式で確認しました。全文監査ではありません。
- T. A. Gardiner and J. M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport. https://arxiv.org/abs/astro-ph/0501557; review_level=author preprint; selected section2.2/equations13–20
  面平均Bと共有corner EMFの構造を確認しました。今回の算術flux-CTを、論文のupwind CT・CTU実装そのものとは呼びません。
- G. Tóth (2000). The ∇·B=0 Constraint in Shock-Capturing Magnetohydrodynamics Codes. https://doi.org/10.1006/jcph.2000.6519; review_level=author paper abstract and bibliographic metadata
  div B制約手法の比較という原著の主題と書誌を確認しました。今回の数値判定や新しい構成例の出典とはしません。
- SciPy developers (2024). scipy.integrate.solve_ivp: DOP853. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official versioned API and actual independent time-integrator execution
  DOP853を別の時間積分器として実行します。空間RHSを共有するため、独立した空間離散化とは呼びません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium

Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence.

**Methods used**

- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) (`ct`)
- [GLM divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en) (`glm`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en#ct-glm-smooth-convergence-en-algorithm)

Both use piecewise constants, the same fixed Rusanov speed alpha3 and forward Euler. CT uses face B/shared arithmetic corner EMFs; GLM uses cell B/psi with fixed ch3 and physical damping rate kappa2. All meshes use384 steps and identical CT/GLM dt sequences; initial reconstructed CT cell B matches GLM cell B.

$$
A=a[\cos k(x-ut)+\cos k(y-vt)],\quad\mathbf B=(A_y,-A_x),\quad J_z=-\Delta A=k^2A
$$

$$
p=p_0+\tfrac12k^2A^2,\qquad\nabla p=J_z\nabla A=\mathbf J\times\mathbf B
$$

$$
\bar{\mathbf U}_{ij}=\frac1{\Delta x\Delta y}\int_{K_{ij}}\mathbf U\,dx\,dy,\qquad p(\bar{\mathbf U})\ne\bar p
$$

$$
\mathbf U^{m+1}=\mathbf U^m+\Delta t\,L_h(\mathbf U^m),\qquad C_{\rm sum}=\alpha\Delta t(\Delta x^{-1}+\Delta y^{-1})
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=en) (`advected-magnetostatic-equilibrium`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en#ct-glm-smooth-convergence-en-validation)

Measure conserved-variable L1/L2/Linf errors and observed orders at16²/32²/64². Compare finest-grid step doubling with.1 of the spatial error. At fixed8², compare16/32/64/128 steps with doubly refined DOP853 tolerances/max steps. Record mass/E, positivity, native CT divergence, common cell divergence and psi.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

Periodic unit square, gamma5/3, mu0=1, planar MHD. A=.05[cos2pi(x−.3t)+cos2pi(y−.2t)], B=(Ay,−Ax), rho1, v=(.3,.2), p=.1+(2pi)²A²/2 at t=.1. Compare analytic conserved cell averages. This is a constructed verification case, not a claimed published standard benchmark.

**Editorial clarification**

This translating smooth equilibrium is an exact solution constructed for the Atlas. Compare conserved cell averages, distinguishing pressure recovered from them from the exact cell average of pressure. A separate time integrator on the same spatial semidiscretization checks time error; it is not an independent PDE solver.

## Adopted numerical method

Both use piecewise constants, the same fixed Rusanov speed alpha3 and forward Euler. CT uses face B/shared arithmetic corner EMFs; GLM uses cell B/psi with fixed ch3 and physical damping rate kappa2. All meshes use384 steps and identical CT/GLM dt sequences; initial reconstructed CT cell B matches GLM cell B.

$$
A=a[\cos k(x-ut)+\cos k(y-vt)],\quad\mathbf B=(A_y,-A_x),\quad J_z=-\Delta A=k^2A
$$

$$
p=p_0+\tfrac12k^2A^2,\qquad\nabla p=J_z\nabla A=\mathbf J\times\mathbf B
$$

$$
\bar{\mathbf U}_{ij}=\frac1{\Delta x\Delta y}\int_{K_{ij}}\mathbf U\,dx\,dy,\qquad p(\bar{\mathbf U})\ne\bar p
$$

$$
\mathbf U^{m+1}=\mathbf U^m+\Delta t\,L_h(\mathbf U^m),\qquad C_{\rm sum}=\alpha\Delta t(\Delta x^{-1}+\Delta y^{-1})
$$

## References and validation

Measure conserved-variable L1/L2/Linf errors and observed orders at16²/32²/64². Compare finest-grid step doubling with.1 of the spatial error. At fixed8², compare16/32/64/128 steps with doubly refined DOP853 tolerances/max steps. Record mass/E, positivity, native CT divergence, common cell divergence and psi.

## Limits

With constant LLF viscosity and periodic centered operators, the GLM div=psi=0 subspace remains invariant up to roundoff. This tests coupled-MHD accuracy; a separate nonphysical control activates cleaning. p(q-average) is not the exact averaged p. DOP853 is independent in time only and shares the spatial RHS. Step differences are empirical contamination indicators, not rigorous bounds; face/cell representation differences remain part of the comparison.

## Stored measurements and decisions

```json
{
  "metrics": {
    "initial_cell_state_linf_difference": 0.0,
    "ct_finest_spatial_error": 0.030434862760674048,
    "ct_minimum_spatial_order": 0.8792002695252499,
    "ct_time_contamination_ratio": 0.00042240836130500326,
    "ct_finest_temporal_scaled_l2": 0.00028691666346522787,
    "ct_minimum_temporal_order": 1.003588237880181,
    "ct_time_reference_to_primary_ratio": 1.0480281669324549e-12,
    "glm_finest_spatial_error": 0.053272941712543334,
    "glm_minimum_spatial_order": 0.8519970902037858,
    "glm_time_contamination_ratio": 0.0002497746629066176,
    "glm_finest_temporal_scaled_l2": 0.0006005455648426271,
    "glm_minimum_temporal_order": 1.004074134741654,
    "glm_time_reference_to_primary_ratio": 4.049255315353574e-13
  },
  "checks": {
    "identical_initial_cell_states": true,
    "ct_native_constraint_n16": true,
    "ct_native_constraint_n32": true,
    "ct_native_constraint_n64": true,
    "ct_spatial_order": true,
    "ct_continuum_error": true,
    "ct_common_divergence_bounded": true,
    "ct_time_contamination_bounded": true,
    "ct_positive_states": true,
    "ct_conservative_mass_energy": true,
    "glm_spatial_order": true,
    "glm_continuum_error": true,
    "glm_common_divergence_bounded": true,
    "glm_time_contamination_bounded": true,
    "glm_positive_states": true,
    "glm_conservative_mass_energy": true,
    "ct_temporal_order": true,
    "ct_temporal_error": true,
    "ct_temporal_reference_resolved": true,
    "glm_temporal_order": true,
    "glm_temporal_error": true,
    "glm_temporal_reference_resolved": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs-initial.json

## Sources and review scope

- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; selected original equations 17–19 and 24, pp.650–651
  Checked selected original GLM B/psi and damping equations, conserved physical energy, and the distinction from extra EGLM source terms; not a full-paper audit.
- T. A. Gardiner and J. M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport. https://arxiv.org/abs/astro-ph/0501557; review_level=author preprint; selected section2.2/equations13–20
  Checked the face-average/shared-corner-EMF structure. The present arithmetic flux-CT is not identified with the paper’s upwind CT/CTU algorithm.
- G. Tóth (2000). The ∇·B=0 Constraint in Shock-Capturing Magnetohydrodynamics Codes. https://doi.org/10.1006/jcph.2000.6519; review_level=author paper abstract and bibliographic metadata
  Confirmed the original comparison topic and bibliographic identity; not a source of this experiment’s criteria or constructed equilibrium.
- SciPy developers (2024). scipy.integrate.solve_ivp: DOP853. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official versioned API and actual independent time-integrator execution
  Execute DOP853 as a separate time integrator; shared spatial RHS means it is not an independent spatial discretization.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
