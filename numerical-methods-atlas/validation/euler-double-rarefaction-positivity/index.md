# Euler二重膨張波：段階ごとの正値性

既存の強い二重希薄波を128/256/512セルで計算し、平均保存型の正値性スケーリングをMUSCL・大域LF流束・SSPRK(3,3)へ接続します。各前進Euler段と各SSP凸結合の密度・圧力・境界保存収支を記録します。

**使用手法**

- [Lax–Friedrichs法](https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-friedrichs/?lang=ja) (`lax-friedrichs`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [平均を保つ正値状態スケーリング](https://hrkoyama.github.io/numerical-methods-atlas/methods/positive-scaling/?lang=ja) (`positive-scaling`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) (`ssprk33`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja#euler-double-rarefaction-positivity-ja-algorithm)

保存量の無制限中央線形再構築を行い、セル平均と左右2端点へ共通の係数θを用いて密度・圧力を正にします。端点平均は元の保存量平均のままです。共有LF流束による前進Euler更新をSSPRK(3,3)で凸結合し、各段の流束前に再構築と制限をやり直します。ε=10⁻¹³は再構築の目標で、密度・エネルギーを加えるfloorではありません。平均の修復・無言の刻み再試行は行いません。

$$
\partial_t U+\partial_x F(U)=0,\qquad U=(\rho,m,E)^T,\quad F=(m,m^2/\rho+p,(E+p)m/\rho)^T,\quad p=(\gamma-1)(E-m^2/(2\rho))
$$

$$
U_i^{\pm}=\bar U_i\pm\delta U_i,\qquad\widehat U_i^{\pm}=\bar U_i+\theta_i(U_i^{\pm}-\bar U_i),\quad0\le\theta_i\le1,\qquad\tfrac12(\widehat U_i^-+\widehat U_i^+)=\bar U_i
$$

$$
\widehat F_{i+1/2}=\tfrac12\!\left[F(\widehat U_i^+)+F(\widehat U_{i+1}^-)-a(\widehat U_{i+1}^--\widehat U_i^+)\right],\qquad\mathcal E_{\Delta t}(\bar U)_i=\bar U_i-\frac{\Delta t}{\Delta x}(\widehat F_{i+1/2}-\widehat F_{i-1/2})
$$

$$
U^{(1)}=\mathcal E_{\Delta t}(U^n),\qquad U^{(2)}=\tfrac34U^n+\tfrac14\mathcal E_{\Delta t}(U^{(1)}),\qquad U^{n+1}=\tfrac13U^n+\tfrac23\mathcal E_{\Delta t}(U^{(2)})
$$

$$
a\ge\max_{i,\pm}(|u(\widehat U_i^\pm)|+c(\widehat U_i^\pm)),\qquad\frac{a\Delta t}{\Delta x}\le\tfrac12,\qquad\rho(\widehat U_i^\pm)>0,\quad p(\widehat U_i^\pm)>0
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

γ=1.4の無外力1次元Euler保存系。セル平均の密度・運動量・全エネルギーを、線形保存量MUSCL再構成と共有Lax–Friedrichs流束で更新します。


**問題の図**

![Euler二重膨張波：段階ごとの正値性：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/euler-double-rarefaction-positivity.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Euler二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja) (`double-rarefaction`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja#euler-double-rarefaction-positivity-ja-validation)

27単体検査と3格子73判定を実行前に固定します。スケーリング前に生じる負の端点圧力を保持し、制限後の端点・前進Euler平均・SSP凸結合平均、θ、全3保存量の境界流束収支を別々に測ります。閉形式の対称希薄波と既存の独立な対数圧力根探索を照合し、保存量のGauss8/16セル平均との誤差と格子細分化を記録します。

- [Euler／二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-double-rarefaction-ja) (`euler-double-rarefaction`; 関連モデルの参照 · 半解析参照)

γ=1.4、左右(1,-2,0.4)/(1,2,0.4)、[0,1]、x0=0.5、t=0.15が保存プレビューと一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。
## 前提・単位・境界

γ1.4、x∈[0,1]、x0=.5、左右状態(ρ,u,p)=(1,−2,.4)/(1,2,.4)、T=.15を固定します。中心の密度・圧力は小さいものの正で、真空生成例ではありません。大域LF分離速度a=4、dt·a/dx≤.4を固定し、実際の全端点の|u|+c≤aと十分条件dt·a/dx≤1/2を確認します。

**編集上の補足**

既存の二重膨張波と同じγ=1.4、左右(ρ,u,p)=(1,−2,.4)/(1,2,.4)、[0,1]、x₀=.5、t=.15の入力です。中心は低密度・低圧の正の状態で、真空生成の別入力とは区別します。段ごとのスケーリング、十分CFLとLax–Friedrichs波速条件を結び付けた限定例であり、既存WENO、DG、MHDや一般EOSの完全離散正値性を保証しません。

## 採用した計算法

保存量の無制限中央線形再構築を行い、セル平均と左右2端点へ共通の係数θを用いて密度・圧力を正にします。端点平均は元の保存量平均のままです。共有LF流束による前進Euler更新をSSPRK(3,3)で凸結合し、各段の流束前に再構築と制限をやり直します。ε=10⁻¹³は再構築の目標で、密度・エネルギーを加えるfloorではありません。平均の修復・無言の刻み再試行は行いません。

$$
\partial_t U+\partial_x F(U)=0,\qquad U=(\rho,m,E)^T,\quad F=(m,m^2/\rho+p,(E+p)m/\rho)^T,\quad p=(\gamma-1)(E-m^2/(2\rho))
$$

$$
U_i^{\pm}=\bar U_i\pm\delta U_i,\qquad\widehat U_i^{\pm}=\bar U_i+\theta_i(U_i^{\pm}-\bar U_i),\quad0\le\theta_i\le1,\qquad\tfrac12(\widehat U_i^-+\widehat U_i^+)=\bar U_i
$$

$$
\widehat F_{i+1/2}=\tfrac12\!\left[F(\widehat U_i^+)+F(\widehat U_{i+1}^-)-a(\widehat U_{i+1}^--\widehat U_i^+)\right],\qquad\mathcal E_{\Delta t}(\bar U)_i=\bar U_i-\frac{\Delta t}{\Delta x}(\widehat F_{i+1/2}-\widehat F_{i-1/2})
$$

$$
U^{(1)}=\mathcal E_{\Delta t}(U^n),\qquad U^{(2)}=\tfrac34U^n+\tfrac14\mathcal E_{\Delta t}(U^{(1)}),\qquad U^{n+1}=\tfrac13U^n+\tfrac23\mathcal E_{\Delta t}(U^{(2)})
$$

$$
a\ge\max_{i,\pm}(|u(\widehat U_i^\pm)|+c(\widehat U_i^\pm)),\qquad\frac{a\Delta t}{\Delta x}\le\tfrac12,\qquad\rho(\widehat U_i^\pm)>0,\quad p(\widehat U_i^\pm)>0
$$

## 比較・検証

27単体検査と3格子73判定を実行前に固定します。スケーリング前に生じる負の端点圧力を保持し、制限後の端点・前進Euler平均・SSP凸結合平均、θ、全3保存量の境界流束収支を別々に測ります。閉形式の対称希薄波と既存の独立な対数圧力根探索を照合し、保存量のGauss8/16セル平均との誤差と格子細分化を記録します。

## 確認の限界

この一つのP1有限体積更新と固定入力の検証です。一般のMUSCL/WENO/DG、特性再構築、反射壁、真空生成、2D/3Dの正値性を認証しません。空間再構築は無制限中央傾きで、TVD・最大値原理・無振動性を保証しません。生の端点圧力は密度が正の端点だけで評価し、密度≤0は別に数えます。圧力参照は保存量セル平均から評価するp(q̄)で、平均圧力とは異なります。ギャラリー図は保存した1次元場のx–t表示であり、2次元流体計算ではありません。ExactPackや別のPDEエンジンを実行した例ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "n": 512,
    "time": 0.15,
    "steps": 769,
    "stages": 2307,
    "density_l1": 0.013786535690656554,
    "pressure_l1": 0.01435653469629682,
    "density_linf": 0.03601512711847121,
    "pressure_linf": 0.019973924350945027,
    "velocity_linf": 0.027566317367641924,
    "reference_quadrature_maximum": 1.3322676295501878e-15,
    "scaled_cells": 6,
    "maximum_face_spectral_radius": 2.771191823275851,
    "maximum_courant": 0.4,
    "maximum_mean_preservation_defect": 2.220446049250313e-16,
    "maximum_fe_boundary_balance_defect": 1.9081958235744878e-17,
    "maximum_rk_boundary_balance_defect": 8.456776945386935e-17,
    "raw_endpoint_nonpositive_density_count": 0,
    "state_floor_count": 0,
    "rejected_steps": 0,
    "retries": 0,
    "raw_endpoint_min_density": 0.009732631218285564,
    "raw_endpoint_min_pressure": -0.5999999999999999,
    "endpoint_min_density": 0.009732631218285564,
    "endpoint_min_pressure": 1.0640377468007498e-13,
    "fe_mean_min_density": 0.009774320902145379,
    "fe_mean_min_pressure": 0.0016944640635574622,
    "rk_mean_min_density": 0.00977443913337385,
    "rk_mean_min_pressure": 0.0016944926865771217,
    "minimum_theta": 0.4494897427830696
  },
  "checks": {
    "all fixed refinements completed": true,
    "N128: final time": true,
    "N128: three records per full SSP step": true,
    "N128: rk_mean_min_density": true,
    "N128: rk_mean_min_pressure": true,
    "N128: endpoint_min_density": true,
    "N128: endpoint_min_pressure": true,
    "N128: fe_mean_min_density": true,
    "N128: fe_mean_min_pressure": true,
    "N128: maximum_face_spectral_radius": true,
    "N128: maximum_courant": true,
    "N128: maximum_mean_preservation_defect": true,
    "N128: maximum_fe_boundary_balance_defect": true,
    "N128: maximum_rk_boundary_balance_defect": true,
    "N128: zero mass/energy floor injections": true,
    "N128: zero retries or rejected steps": true,
    "N128: scaling actually exercised": true,
    "N128: raw nonadmissible reconstruction retained": true,
    "N128: mass boundary budget": true,
    "N128: momentum boundary budget": true,
    "N128: energy boundary budget": true,
    "N128: split Gauss8/16 reference": true,
    "N256: final time": true,
    "N256: three records per full SSP step": true,
    "N256: rk_mean_min_density": true,
    "N256: rk_mean_min_pressure": true,
    "N256: endpoint_min_density": true,
    "N256: endpoint_min_pressure": true,
    "N256: fe_mean_min_density": true,
    "N256: fe_mean_min_pressure": true,
    "N256: maximum_face_spectral_radius": true,
    "N256: maximum_courant": true,
    "N256: maximum_mean_preservation_defect": true,
    "N256: maximum_fe_boundary_balance_defect": true,
    "N256: maximum_rk_boundary_balance_defect": true,
    "N256: zero mass/energy floor injections": true,
    "N256: zero retries or rejected steps": true,
    "N256: scaling actually exercised": true,
    "N256: raw nonadmissible reconstruction retained": true,
    "N256: mass boundary budget": true,
    "N256: momentum boundary budget": true,
    "N256: energy boundary budget": true,
    "N256: split Gauss8/16 reference": true,
    "N512: final time": true,
    "N512: three records per full SSP step": true,
    "N512: rk_mean_min_density": true,
    "N512: rk_mean_min_pressure": true,
    "N512: endpoint_min_density": true,
    "N512: endpoint_min_pressure": true,
    "N512: fe_mean_min_density": true,
    "N512: fe_mean_min_pressure": true,
    "N512: maximum_face_spectral_radius": true,
    "N512: maximum_courant": true,
    "N512: maximum_mean_preservation_defect": true,
    "N512: maximum_fe_boundary_balance_defect": true,
    "N512: maximum_rk_boundary_balance_defect": true,
    "N512: zero mass/energy floor injections": true,
    "N512: zero retries or rejected steps": true,
    "N512: scaling actually exercised": true,
    "N512: raw nonadmissible reconstruction retained": true,
    "N512: mass boundary budget": true,
    "N512: momentum boundary budget": true,
    "N512: energy boundary budget": true,
    "N512: split Gauss8/16 reference": true,
    "finest density_l1": true,
    "density_l1 refinement ratio 1": true,
    "density_l1 refinement ratio 2": true,
    "finest pressure_l1": true,
    "pressure_l1 refinement ratio 1": true,
    "pressure_l1 refinement ratio 2": true,
    "reference: star_pressure_absolute_difference": true,
    "reference: independent_root_point_maximum_difference": true,
    "reference: maximum_scaled_euler_residual": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/index.json

![強い二重希薄波の密度・圧力：保存した1次元計算のx–t図（2次元流体計算ではない）。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/euler-double-rarefaction-positivity-preview.png)

強い二重希薄波の密度・圧力：保存した1次元計算のx–t図（2次元流体計算ではない）。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- Xiangxiong Zhang and Chi-Wang Shu (2010). On positivity-preserving high order discontinuous Galerkin schemes for compressible Euler equations on rectangular meshes. https://www.math.purdue.edu/~zhan1966/research/paper/euler.pdf; review_level=author manuscript selected sections actually inspected: §2 Theorem2.1, Remarks2.2/2.4/2.6/2.7; §4.3 distinguishes vacuum input
  著者稿の定理・LF条件・各SSP段階への適用と波速見積りの注意を確認。P1有限体積への限定適用で、原著の真空例・3次DGを再現したとは扱いません。
- David I. Ketcheson, Randall J. LeVeque and Mauricio J. del Razo (2020). Riemann Problems and Jupyter Solutions: The Euler equations of gas dynamics. https://www.clawpack.org/riemann_book/html/Euler.html; review_level=official chapter sections Riemann invariants, exact solution, symmetric expansion and vacuum; official exact_solvers/euler.py integral_curve_1/3 inspected read-only
  公式章の希薄波不変量と対称膨張・真空条件を確認。今回の固定値は既存アトラスの入力を継承し、同章の数値例そのものとは区別します。Clawpackコードは実行・転載しません。
- Chi-Wang Shu and Stanley Osher (1988). Efficient implementation of essentially non-oscillatory shock-capturing schemes. https://www.sciencedirect.com/science/article/pii/0021999188901775; review_level=publisher bibliographic record and abstract only; no full-paper audit
  出版社の書誌とTVD型Runge–Kuttaの抄録を確認。原著全文・全数値実験の監査ではありません。SSP凸結合による正値性の議論はZhang–Shu著者稿でも確認。
- Eleuterio F. Toro (2009). Riemann Solvers and Numerical Methods for Fluid Dynamics: A Practical Introduction. https://link.springer.com/book/10.1007/b79761; review_level=publisher bibliography and chapter4 title/pages115–162 only; full text not inspected
  出版社で第3版・著者・年とEulerのRiemann問題の章を確認。固定数値の原典をこの閲覧だけで断定しません。
- Hiroshi Koyama (2026). Numerical Methods Atlas: released independent Euler Riemann evaluator. https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/reference_riemann.py; review_level=local immutable source inspected; copied without changes with SHA and MIT license; execution recorded by tests, not presumed
  既存の対数圧力根探索と希薄波評価を独立な式経路の照合に使います。実行記録とSHA・MIT条項を別に保存し、異なるPDE計算エンジンの検証とは表示しません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Euler double rarefaction: positivity at every stage

Evolve the existing strong double rarefaction on 128/256/512 cells, connecting mean-preserving positivity scaling to MUSCL, global LF fluxes and SSPRK(3,3). Log density, pressure and boundary budgets for every FE substep and SSP convex combination.

**Methods used**

- [Lax–Friedrichs](https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-friedrichs/?lang=en) (`lax-friedrichs`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Mean-preserving positive-state scaling](https://hrkoyama.github.io/numerical-methods-atlas/methods/positive-scaling/?lang=en) (`positive-scaling`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en#euler-double-rarefaction-positivity-en-algorithm)

Unlimited conservative central linear reconstruction is scaled toward its mean with one common theta per cell until both endpoint densities/pressures are positive. The two endpoint mean remains the original conserved mean. Shared LF FE updates are combined by SSPRK(3,3), reconstructing/limiting before every flux stage. Epsilon1e-13 is a reconstruction target, not an injected density/energy floor. No average repair or hidden time-step retries are used.

$$
\partial_t U+\partial_x F(U)=0,\qquad U=(\rho,m,E)^T,\quad F=(m,m^2/\rho+p,(E+p)m/\rho)^T,\quad p=(\gamma-1)(E-m^2/(2\rho))
$$

$$
U_i^{\pm}=\bar U_i\pm\delta U_i,\qquad\widehat U_i^{\pm}=\bar U_i+\theta_i(U_i^{\pm}-\bar U_i),\quad0\le\theta_i\le1,\qquad\tfrac12(\widehat U_i^-+\widehat U_i^+)=\bar U_i
$$

$$
\widehat F_{i+1/2}=\tfrac12\!\left[F(\widehat U_i^+)+F(\widehat U_{i+1}^-)-a(\widehat U_{i+1}^--\widehat U_i^+)\right],\qquad\mathcal E_{\Delta t}(\bar U)_i=\bar U_i-\frac{\Delta t}{\Delta x}(\widehat F_{i+1/2}-\widehat F_{i-1/2})
$$

$$
U^{(1)}=\mathcal E_{\Delta t}(U^n),\qquad U^{(2)}=\tfrac34U^n+\tfrac14\mathcal E_{\Delta t}(U^{(1)}),\qquad U^{n+1}=\tfrac13U^n+\tfrac23\mathcal E_{\Delta t}(U^{(2)})
$$

$$
a\ge\max_{i,\pm}(|u(\widehat U_i^\pm)|+c(\widehat U_i^\pm)),\qquad\frac{a\Delta t}{\Delta x}\le\tfrac12,\qquad\rho(\widehat U_i^\pm)>0,\quad p(\widehat U_i^\pm)>0
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Unforced one-dimensional ideal-gas Euler at gamma=1.4 evolves cell means of density, momentum and total energy using linear conservative MUSCL reconstruction and shared Lax–Friedrichs fluxes.


**Problem figure**

![Euler double rarefaction: positivity at every stage: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/euler-double-rarefaction-positivity.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Euler double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en) (`double-rarefaction`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en#euler-double-rarefaction-positivity-en-validation)

Freeze 27 unit tests and 73 gates over three grids before execution. Retain negative raw endpoint pressures, then separately measure limited endpoints, FE means, SSP convex means, theta and all three boundary-flux conservation budgets. Cross-check the closed symmetric fan against the prior independent logarithmic-pressure root evaluator; record errors/refinement against conserved Gauss8/16 cell means.

- [Euler / double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-double-rarefaction-en) (`euler-double-rarefaction`; Related-model reference · Semi-analytic reference)

γ=1.4, states (1,-2,0.4)/(1,2,0.4), [0,1], x0=0.5 and t=0.15 match the saved preview. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.
## Assumptions, units and boundaries

Fix gamma1.4, x in [0,1], discontinuity x0=.5, outer primitive states(1,-2,.4)/(1,2,.4) and T=.15. The low-density central state remains strictly positive; this is not a vacuum-generating case. Use fixed global LF splitting speed a4 and dt*a/dx<=.4; assert every actual endpoint satisfies |u|+c<=a and the sufficient dt*a/dx<=1/2 condition.

**Editorial clarification**

The same fixed physical input as the existing double rarefaction uses gamma=1.4, left/right (rho,u,p)=(1,-2,.4)/(1,2,.4), [0,1], x0=.5 and t=.15. Its middle state has small positive density/pressure, unlike separate vacuum-generating data. Stage scaling is connected to sufficient CFL and Lax–Friedrichs wave-speed conditions for this scoped example, without certifying existing WENO, DG, MHD or general equations of state.

## Adopted numerical method

Unlimited conservative central linear reconstruction is scaled toward its mean with one common theta per cell until both endpoint densities/pressures are positive. The two endpoint mean remains the original conserved mean. Shared LF FE updates are combined by SSPRK(3,3), reconstructing/limiting before every flux stage. Epsilon1e-13 is a reconstruction target, not an injected density/energy floor. No average repair or hidden time-step retries are used.

$$
\partial_t U+\partial_x F(U)=0,\qquad U=(\rho,m,E)^T,\quad F=(m,m^2/\rho+p,(E+p)m/\rho)^T,\quad p=(\gamma-1)(E-m^2/(2\rho))
$$

$$
U_i^{\pm}=\bar U_i\pm\delta U_i,\qquad\widehat U_i^{\pm}=\bar U_i+\theta_i(U_i^{\pm}-\bar U_i),\quad0\le\theta_i\le1,\qquad\tfrac12(\widehat U_i^-+\widehat U_i^+)=\bar U_i
$$

$$
\widehat F_{i+1/2}=\tfrac12\!\left[F(\widehat U_i^+)+F(\widehat U_{i+1}^-)-a(\widehat U_{i+1}^--\widehat U_i^+)\right],\qquad\mathcal E_{\Delta t}(\bar U)_i=\bar U_i-\frac{\Delta t}{\Delta x}(\widehat F_{i+1/2}-\widehat F_{i-1/2})
$$

$$
U^{(1)}=\mathcal E_{\Delta t}(U^n),\qquad U^{(2)}=\tfrac34U^n+\tfrac14\mathcal E_{\Delta t}(U^{(1)}),\qquad U^{n+1}=\tfrac13U^n+\tfrac23\mathcal E_{\Delta t}(U^{(2)})
$$

$$
a\ge\max_{i,\pm}(|u(\widehat U_i^\pm)|+c(\widehat U_i^\pm)),\qquad\frac{a\Delta t}{\Delta x}\le\tfrac12,\qquad\rho(\widehat U_i^\pm)>0,\quad p(\widehat U_i^\pm)>0
$$

## References and validation

Freeze 27 unit tests and 73 gates over three grids before execution. Retain negative raw endpoint pressures, then separately measure limited endpoints, FE means, SSP convex means, theta and all three boundary-flux conservation budgets. Cross-check the closed symmetric fan against the prior independent logarithmic-pressure root evaluator; record errors/refinement against conserved Gauss8/16 cell means.

## Limits

Evidence covers this one P1 FV update and fixed input, not general MUSCL/WENO/DG, characteristic reconstruction, reflecting walls, vacuum generation or multidimensional positivity. Unlimited central slopes have no TVD, maximum-principle or nonoscillation guarantee. Raw pressure is evaluated only where raw density is positive; nonpositive raw density has its own count. Reference pressure is p(mean conserved q), not mean pressure. Gallery plots are saved one-dimensional x-t fields, not two-dimensional flow. No ExactPack or separate PDE engine is executed.

## Stored measurements and decisions

```json
{
  "metrics": {
    "n": 512,
    "time": 0.15,
    "steps": 769,
    "stages": 2307,
    "density_l1": 0.013786535690656554,
    "pressure_l1": 0.01435653469629682,
    "density_linf": 0.03601512711847121,
    "pressure_linf": 0.019973924350945027,
    "velocity_linf": 0.027566317367641924,
    "reference_quadrature_maximum": 1.3322676295501878e-15,
    "scaled_cells": 6,
    "maximum_face_spectral_radius": 2.771191823275851,
    "maximum_courant": 0.4,
    "maximum_mean_preservation_defect": 2.220446049250313e-16,
    "maximum_fe_boundary_balance_defect": 1.9081958235744878e-17,
    "maximum_rk_boundary_balance_defect": 8.456776945386935e-17,
    "raw_endpoint_nonpositive_density_count": 0,
    "state_floor_count": 0,
    "rejected_steps": 0,
    "retries": 0,
    "raw_endpoint_min_density": 0.009732631218285564,
    "raw_endpoint_min_pressure": -0.5999999999999999,
    "endpoint_min_density": 0.009732631218285564,
    "endpoint_min_pressure": 1.0640377468007498e-13,
    "fe_mean_min_density": 0.009774320902145379,
    "fe_mean_min_pressure": 0.0016944640635574622,
    "rk_mean_min_density": 0.00977443913337385,
    "rk_mean_min_pressure": 0.0016944926865771217,
    "minimum_theta": 0.4494897427830696
  },
  "checks": {
    "all fixed refinements completed": true,
    "N128: final time": true,
    "N128: three records per full SSP step": true,
    "N128: rk_mean_min_density": true,
    "N128: rk_mean_min_pressure": true,
    "N128: endpoint_min_density": true,
    "N128: endpoint_min_pressure": true,
    "N128: fe_mean_min_density": true,
    "N128: fe_mean_min_pressure": true,
    "N128: maximum_face_spectral_radius": true,
    "N128: maximum_courant": true,
    "N128: maximum_mean_preservation_defect": true,
    "N128: maximum_fe_boundary_balance_defect": true,
    "N128: maximum_rk_boundary_balance_defect": true,
    "N128: zero mass/energy floor injections": true,
    "N128: zero retries or rejected steps": true,
    "N128: scaling actually exercised": true,
    "N128: raw nonadmissible reconstruction retained": true,
    "N128: mass boundary budget": true,
    "N128: momentum boundary budget": true,
    "N128: energy boundary budget": true,
    "N128: split Gauss8/16 reference": true,
    "N256: final time": true,
    "N256: three records per full SSP step": true,
    "N256: rk_mean_min_density": true,
    "N256: rk_mean_min_pressure": true,
    "N256: endpoint_min_density": true,
    "N256: endpoint_min_pressure": true,
    "N256: fe_mean_min_density": true,
    "N256: fe_mean_min_pressure": true,
    "N256: maximum_face_spectral_radius": true,
    "N256: maximum_courant": true,
    "N256: maximum_mean_preservation_defect": true,
    "N256: maximum_fe_boundary_balance_defect": true,
    "N256: maximum_rk_boundary_balance_defect": true,
    "N256: zero mass/energy floor injections": true,
    "N256: zero retries or rejected steps": true,
    "N256: scaling actually exercised": true,
    "N256: raw nonadmissible reconstruction retained": true,
    "N256: mass boundary budget": true,
    "N256: momentum boundary budget": true,
    "N256: energy boundary budget": true,
    "N256: split Gauss8/16 reference": true,
    "N512: final time": true,
    "N512: three records per full SSP step": true,
    "N512: rk_mean_min_density": true,
    "N512: rk_mean_min_pressure": true,
    "N512: endpoint_min_density": true,
    "N512: endpoint_min_pressure": true,
    "N512: fe_mean_min_density": true,
    "N512: fe_mean_min_pressure": true,
    "N512: maximum_face_spectral_radius": true,
    "N512: maximum_courant": true,
    "N512: maximum_mean_preservation_defect": true,
    "N512: maximum_fe_boundary_balance_defect": true,
    "N512: maximum_rk_boundary_balance_defect": true,
    "N512: zero mass/energy floor injections": true,
    "N512: zero retries or rejected steps": true,
    "N512: scaling actually exercised": true,
    "N512: raw nonadmissible reconstruction retained": true,
    "N512: mass boundary budget": true,
    "N512: momentum boundary budget": true,
    "N512: energy boundary budget": true,
    "N512: split Gauss8/16 reference": true,
    "finest density_l1": true,
    "density_l1 refinement ratio 1": true,
    "density_l1 refinement ratio 2": true,
    "finest pressure_l1": true,
    "pressure_l1 refinement ratio 1": true,
    "pressure_l1 refinement ratio 2": true,
    "reference: star_pressure_absolute_difference": true,
    "reference: independent_root_point_maximum_difference": true,
    "reference: maximum_scaled_euler_residual": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/index.json

![Density/pressure of the strong double rarefaction: x-t views of saved one-dimensional evolution, not two-dimensional flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/euler-double-rarefaction-positivity-preview.png)

Density/pressure of the strong double rarefaction: x-t views of saved one-dimensional evolution, not two-dimensional flow.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- Xiangxiong Zhang and Chi-Wang Shu (2010). On positivity-preserving high order discontinuous Galerkin schemes for compressible Euler equations on rectangular meshes. https://www.math.purdue.edu/~zhan1966/research/paper/euler.pdf; review_level=author manuscript selected sections actually inspected: §2 Theorem2.1, Remarks2.2/2.4/2.6/2.7; §4.3 distinguishes vacuum input
  Inspected positivity conditions, LF proof, stage limiting and speed-bound caution. This applies the framework to P1 FV; it does not reproduce the paper’s vacuum test or third-order DG scheme.
- David I. Ketcheson, Randall J. LeVeque and Mauricio J. del Razo (2020). Riemann Problems and Jupyter Solutions: The Euler equations of gas dynamics. https://www.clawpack.org/riemann_book/html/Euler.html; review_level=official chapter sections Riemann invariants, exact solution, symmetric expansion and vacuum; official exact_solvers/euler.py integral_curve_1/3 inspected read-only
  Read the official invariants, symmetric expansion and vacuum conditions. The fixed values inherit the existing atlas case and differ from this chapter’s example. No Clawpack software is executed or copied.
- Chi-Wang Shu and Stanley Osher (1988). Efficient implementation of essentially non-oscillatory shock-capturing schemes. https://www.sciencedirect.com/science/article/pii/0021999188901775; review_level=publisher bibliographic record and abstract only; no full-paper audit
  Publisher record and abstract reviewed; the full paper and numerical experiments were not audited. The convex-combination positivity application was also checked in the Zhang–Shu manuscript.
- Eleuterio F. Toro (2009). Riemann Solvers and Numerical Methods for Fluid Dynamics: A Practical Introduction. https://link.springer.com/book/10.1007/b79761; review_level=publisher bibliography and chapter4 title/pages115–162 only; full text not inspected
  Publisher metadata and Euler Riemann chapter listing checked. This inspection alone does not establish the first historical source of the fixed numerical data.
- Hiroshi Koyama (2026). Numerical Methods Atlas: released independent Euler Riemann evaluator. https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/reference_riemann.py; review_level=local immutable source inspected; copied without changes with SHA and MIT license; execution recorded by tests, not presumed
  The prior logarithmic-pressure root and fan evaluator provide a separate algebraic check, with SHA and MIT terms. It is not a different PDE engine; execution is established by test receipts.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
