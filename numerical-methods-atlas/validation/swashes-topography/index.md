# SWASHES地形流：静水と非零流量の定常解

水没・露出した隆起上の静水と、非零流量の亜臨界定常解を別々に検査します。静水の保存と、動く定常流に残る離散化誤差を区別します。

**使用手法**

- [Godunov型有限体積法](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=ja) (`godunov`)
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) (`hll`)
- [前進Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja) (`forward-euler`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja#swashes-topography-ja-algorithm)

非負な静水圧再構成、共有HLL流束と左右の圧力補正で地形源項を離散化します。前進Euler、面Courant数.4。静水は反射壁。亜臨界流は上流で流量・下流で水深のみを指定し他変数を外挿します。floor・clip・retryはありません。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。

$$
\partial_t h+\partial_x q=0,\qquad \partial_tq+\partial_x(q^2/h+gh^2/2)=-gh\partial_xz
$$

$$
z^*=\max(z_L,z_R),\quad h_K^*=\max(0,h_K+z_K-z^*),\quad q_K^*=h_K^*u_K
$$

$$
F_K=F_{\mathrm{HLL}}(U_L^*,U_R^*)+(0,\tfrac12g(h_K^2-(h_K^*)^2))^T
$$

$$
q=4.42,\quad h+z+q^2/(2gh^2)=2+4.42^2/(8g),\quad h>(q^2/g)^{1/3}
$$

- [地形源項付き浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-bed-ja) (`shallow-water-bed`)

1次元、g=9.81、長さ25m、8<x<12でz=.2−.05(x−10)²m。水位.5/.1mの静水は200セル、流量4.42m²/s・下流深さ2mの定常流は100/200/400セル、t=2s。地形は区分定数セル平均。定常流から開始し、静水からの定常化実験とは区別します。


**問題の図**

![SWASHES地形流：静水と非零流量の定常解：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[SWASHES地形上の静止湖・定常浅水流](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja) (`swashes-topography`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja#swashes-topography-ja-validation)

31単体検査と8固定計算を事前固定。静水の水深・流量の最大変化、全FE段の非負水深、共有流束と地形運動量の収支、定常流3格子の保存量セル平均L1誤差・細分化比を保存します。独立したBernoulli二分法のエネルギー一定・亜臨界枝を照合します。

- [静止湖：表現した床の上の湿潤・露出平衡](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lake-at-rest-bed-ja) (`lake-at-rest-bed`; 同じ問題の参照 · 解析参照)

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。

- [SWASHES定常流：非射流Bernoulli根](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swashes-bernoulli-ja) (`swashes-bernoulli`; 同じ問題の参照 · 半解析参照)

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。
## 前提・単位・境界

1次元、g=9.81、長さ25m、8<x<12でz=.2−.05(x−10)²m。水位.5/.1mの静水は200セル、流量4.42m²/s・下流深さ2mの定常流は100/200/400セル、t=2s。地形は区分定数セル平均。定常流から開始し、静水からの定常化実験とは区別します。

**編集上の補足**

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。 最終改訂は31単体検査と群全体8計算109判定に合格しました。定常流の最細N400では水深L1約.0249108、相対水深L1約.000505933です。静止湖の表現した床の釣合い、有限時間の移動定常流の誤差、乾燥床の前縁誤差を別々に保存します。

## 採用した計算法

非負な静水圧再構成、共有HLL流束と左右の圧力補正で地形源項を離散化します。前進Euler、面Courant数.4。静水は反射壁。亜臨界流は上流で流量・下流で水深のみを指定し他変数を外挿します。floor・clip・retryはありません。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。

$$
\partial_t h+\partial_x q=0,\qquad \partial_tq+\partial_x(q^2/h+gh^2/2)=-gh\partial_xz
$$

$$
z^*=\max(z_L,z_R),\quad h_K^*=\max(0,h_K+z_K-z^*),\quad q_K^*=h_K^*u_K
$$

$$
F_K=F_{\mathrm{HLL}}(U_L^*,U_R^*)+(0,\tfrac12g(h_K^2-(h_K^*)^2))^T
$$

$$
q=4.42,\quad h+z+q^2/(2gh^2)=2+4.42^2/(8g),\quad h>(q^2/g)^{1/3}
$$

## 比較・検証

31単体検査と8固定計算を事前固定。静水の水深・流量の最大変化、全FE段の非負水深、共有流束と地形運動量の収支、定常流3格子の保存量セル平均L1誤差・細分化比を保存します。独立したBernoulli二分法のエネルギー一定・亜臨界枝を照合します。

## 確認の限界

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "n": 400,
    "steps": 536,
    "time": 2.0,
    "depth_l1": 0.024910750612742227,
    "momentum_l1": 0.060087246887864654,
    "relative_depth_l1": 0.0005059326932762419,
    "relative_momentum_l1": 0.0005437759899354242,
    "depth_linf": 0.006424726192375774,
    "minimum_depth": 1.7071673523958315,
    "maximum_depth": 2.0053503464023863,
    "maximum_velocity": 2.5885739653660536,
    "maximum_courant": 0.4,
    "maximum_step_mass_defect": 8.624754336295616e-15,
    "maximum_step_momentum_defect": 1.7091399469478224e-14,
    "minimum_staying_coefficient": 0.7344646405854746,
    "maximum_total_mass_defect": 8.038448654658321e-14,
    "maximum_total_momentum_defect": 3.8524326957667387e-13,
    "mass_change": 1.7453826262892047e-05,
    "boundary_mass_change": 1.745382627041232e-05,
    "bed_momentum_impulse": -0.02828240710978647,
    "initial_dry_cells": 0,
    "final_dry_cells": 0,
    "newly_wet_cells": 0,
    "all_saved_values_finite": true,
    "depth_floor_count": 0,
    "state_clip_count": 0,
    "rejected_steps": 0,
    "retries": 0
  },
  "checks": {
    "lake-immersed: maximum_step_mass_defect": true,
    "lake-immersed: maximum_step_momentum_defect": true,
    "lake-immersed: maximum_total_mass_defect": true,
    "lake-immersed: maximum_total_momentum_defect": true,
    "lake-immersed: nonnegative depth": true,
    "lake-immersed: finite arrays": true,
    "lake-immersed: face CFL": true,
    "lake-immersed: no repairs or retries": true,
    "lake-immersed: five exact output times": true,
    "lake-immersed: maximum_equilibrium_depth_drift": true,
    "lake-immersed: maximum_equilibrium_discharge": true,
    "lake-emerged: maximum_step_mass_defect": true,
    "lake-emerged: maximum_step_momentum_defect": true,
    "lake-emerged: maximum_total_mass_defect": true,
    "lake-emerged: maximum_total_momentum_defect": true,
    "lake-emerged: nonnegative depth": true,
    "lake-emerged: finite arrays": true,
    "lake-emerged: face CFL": true,
    "lake-emerged: no repairs or retries": true,
    "lake-emerged: five exact output times": true,
    "lake-emerged: maximum_equilibrium_depth_drift": true,
    "lake-emerged: maximum_equilibrium_discharge": true,
    "subcritical-n100: maximum_step_mass_defect": true,
    "subcritical-n100: maximum_step_momentum_defect": true,
    "subcritical-n100: maximum_total_mass_defect": true,
    "subcritical-n100: maximum_total_momentum_defect": true,
    "subcritical-n100: nonnegative depth": true,
    "subcritical-n100: finite arrays": true,
    "subcritical-n100: face CFL": true,
    "subcritical-n100: no repairs or retries": true,
    "subcritical-n100: five exact output times": true,
    "subcritical-n200: maximum_step_mass_defect": true,
    "subcritical-n200: maximum_step_momentum_defect": true,
    "subcritical-n200: maximum_total_mass_defect": true,
    "subcritical-n200: maximum_total_momentum_defect": true,
    "subcritical-n200: nonnegative depth": true,
    "subcritical-n200: finite arrays": true,
    "subcritical-n200: face CFL": true,
    "subcritical-n200: no repairs or retries": true,
    "subcritical-n200: five exact output times": true,
    "subcritical-n400: maximum_step_mass_defect": true,
    "subcritical-n400: maximum_step_momentum_defect": true,
    "subcritical-n400: maximum_total_mass_defect": true,
    "subcritical-n400: maximum_total_momentum_defect": true,
    "subcritical-n400: nonnegative depth": true,
    "subcritical-n400: finite arrays": true,
    "subcritical-n400: face CFL": true,
    "subcritical-n400: no repairs or retries": true,
    "subcritical-n400: five exact output times": true,
    "subcritical finest relative_depth_l1": true,
    "subcritical relative_depth_l1 refinement 1": true,
    "subcritical relative_depth_l1 refinement 2": true,
    "subcritical finest relative_momentum_l1": true,
    "subcritical relative_momentum_l1 refinement 1": true,
    "subcritical relative_momentum_l1 refinement 2": true,
    "reference: Bernoulli energy constant": true,
    "reference: subcritical branch": true,
    "reference: Gauss8 vs Gauss16 conservative means": true,
    "reference: Ritter total mass": true,
    "reference: Ritter finite difference PDE residual": true,
    "reference: exact dry branch": true,
    "all fixed runs completed": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/index.json

![保存した有限体積配列から描いた地形・水面と定常誤差のプレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png)

保存した有限体積配列から描いた地形・水面と定常誤差のプレビュー。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/attempts/01/source/inputs.json

## 出典と確認範囲

- O. Delestre et al. (2013). SWASHES: a compilation of shallow water analytic solutions for hydraulic and environmental studies. https://arxiv.org/pdf/1110.0288; review_level=selected-equations-and-fixed-inputs
- E. Audusse, F. Bouchut, M.-O. Bristeau, R. Klein, B. Perthame (2004). A Fast and Stable Well-Balanced Scheme with Hydrostatic Reconstruction for Shallow Water Flows. https://epubs.siam.org/doi/abs/10.1137/S1064827503431090; review_level=bibliography-and-author-follow-up
- E. Audusse, F. Bouchut, M.-O. Bristeau, J. Sainte-Marie (2016). Kinetic entropy inequality and hydrostatic reconstruction scheme for the Saint-Venant system. https://arxiv.org/pdf/1409.3825; review_level=selected-scheme-equations
- Institut Denis Poisson / SWASHES authors (n.d.). SWASHES project page. https://www.idpoisson.fr/en/swashes-es/; review_level=official-project-scope-and-rights

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# SWASHES topographic flow: lakes and nonzero steady discharge

Check two lake equilibria separately from nonzero subcritical flow, distinguishing lake preservation from moving-flow discretization error.

**Methods used**

- [Godunov-type finite volumes](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en) (`godunov`)
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [Forward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en) (`forward-euler`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en#swashes-topography-en-algorithm)

Hydrostatic reconstruction, shared HLL flux and left/right pressure corrections discretize the bed source; forward Euler and face CFL .4. Lakes use reflecting walls. Moving subcritical boundaries impose upstream q and downstream h, extrapolating the other datum. No state floors, clipping or retries. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.

$$
\partial_t h+\partial_x q=0,\qquad \partial_tq+\partial_x(q^2/h+gh^2/2)=-gh\partial_xz
$$

$$
z^*=\max(z_L,z_R),\quad h_K^*=\max(0,h_K+z_K-z^*),\quad q_K^*=h_K^*u_K
$$

$$
F_K=F_{\mathrm{HLL}}(U_L^*,U_R^*)+(0,\tfrac12g(h_K^2-(h_K^*)^2))^T
$$

$$
q=4.42,\quad h+z+q^2/(2gh^2)=2+4.42^2/(8g),\quad h>(q^2/g)^{1/3}
$$

- [Shallow-water equations with bed source](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-bed-en) (`shallow-water-bed`)

1D, g=9.81, L=25m, compact parabolic bed z=.2-.05(x-10)^2 on8<x<12. Lakes at surface .5/.1m use200 cells. Moving flow q=4.42m2/s, downstream h=2m uses100/200/400 cells to2s. Initialize the steady branch, not the published rest-to-steady transient.


**Problem figure**

![SWASHES topographic flow: lakes and nonzero steady discharge: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[SWASHES lakes and steady shallow flow over topography](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en) (`swashes-topography`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en#swashes-topography-en-validation)

Freeze31 unit checks and eight group runs. Record lake drift, every FE minimum depth, shared-flux/bed-impulse budgets, conservative-mean L1 errors and three-grid ratios. Qualify an independent Bernoulli bisection by energy and branch checks.

- [Lake at rest: wet and emerged equilibrium over represented bed](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lake-at-rest-bed-en) (`lake-at-rest-bed`; Same-problem reference · Analytic reference)

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.

- [SWASHES steady flow: subcritical Bernoulli root](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swashes-bernoulli-en) (`swashes-bernoulli`; Same-problem reference · Semi-analytic reference)

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.
## Assumptions, units and boundaries

1D, g=9.81, L=25m, compact parabolic bed z=.2-.05(x-10)^2 on8<x<12. Lakes at surface .5/.1m use200 cells. Moving flow q=4.42m2/s, downstream h=2m uses100/200/400 cells to2s. Initialize the steady branch, not the published rest-to-steady transient.

**Editorial clarification**

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope. The final revision passed31 unit checks and all109 gates over8 group runs. The finest moving steady case,N400, has depthL1 about.0249108 and relative depthL1 about.000505933. Represented-bed lake balance, finite-time moving steady errors and dry-bed front errors are retained separately.

## Adopted numerical method

Hydrostatic reconstruction, shared HLL flux and left/right pressure corrections discretize the bed source; forward Euler and face CFL .4. Lakes use reflecting walls. Moving subcritical boundaries impose upstream q and downstream h, extrapolating the other datum. No state floors, clipping or retries. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.

$$
\partial_t h+\partial_x q=0,\qquad \partial_tq+\partial_x(q^2/h+gh^2/2)=-gh\partial_xz
$$

$$
z^*=\max(z_L,z_R),\quad h_K^*=\max(0,h_K+z_K-z^*),\quad q_K^*=h_K^*u_K
$$

$$
F_K=F_{\mathrm{HLL}}(U_L^*,U_R^*)+(0,\tfrac12g(h_K^2-(h_K^*)^2))^T
$$

$$
q=4.42,\quad h+z+q^2/(2gh^2)=2+4.42^2/(8g),\quad h>(q^2/g)^{1/3}
$$

## References and validation

Freeze31 unit checks and eight group runs. Record lake drift, every FE minimum depth, shared-flux/bed-impulse budgets, conservative-mean L1 errors and three-grid ratios. Qualify an independent Bernoulli bisection by energy and branch checks.

## Limits

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.

## Stored measurements and decisions

```json
{
  "metrics": {
    "n": 400,
    "steps": 536,
    "time": 2.0,
    "depth_l1": 0.024910750612742227,
    "momentum_l1": 0.060087246887864654,
    "relative_depth_l1": 0.0005059326932762419,
    "relative_momentum_l1": 0.0005437759899354242,
    "depth_linf": 0.006424726192375774,
    "minimum_depth": 1.7071673523958315,
    "maximum_depth": 2.0053503464023863,
    "maximum_velocity": 2.5885739653660536,
    "maximum_courant": 0.4,
    "maximum_step_mass_defect": 8.624754336295616e-15,
    "maximum_step_momentum_defect": 1.7091399469478224e-14,
    "minimum_staying_coefficient": 0.7344646405854746,
    "maximum_total_mass_defect": 8.038448654658321e-14,
    "maximum_total_momentum_defect": 3.8524326957667387e-13,
    "mass_change": 1.7453826262892047e-05,
    "boundary_mass_change": 1.745382627041232e-05,
    "bed_momentum_impulse": -0.02828240710978647,
    "initial_dry_cells": 0,
    "final_dry_cells": 0,
    "newly_wet_cells": 0,
    "all_saved_values_finite": true,
    "depth_floor_count": 0,
    "state_clip_count": 0,
    "rejected_steps": 0,
    "retries": 0
  },
  "checks": {
    "lake-immersed: maximum_step_mass_defect": true,
    "lake-immersed: maximum_step_momentum_defect": true,
    "lake-immersed: maximum_total_mass_defect": true,
    "lake-immersed: maximum_total_momentum_defect": true,
    "lake-immersed: nonnegative depth": true,
    "lake-immersed: finite arrays": true,
    "lake-immersed: face CFL": true,
    "lake-immersed: no repairs or retries": true,
    "lake-immersed: five exact output times": true,
    "lake-immersed: maximum_equilibrium_depth_drift": true,
    "lake-immersed: maximum_equilibrium_discharge": true,
    "lake-emerged: maximum_step_mass_defect": true,
    "lake-emerged: maximum_step_momentum_defect": true,
    "lake-emerged: maximum_total_mass_defect": true,
    "lake-emerged: maximum_total_momentum_defect": true,
    "lake-emerged: nonnegative depth": true,
    "lake-emerged: finite arrays": true,
    "lake-emerged: face CFL": true,
    "lake-emerged: no repairs or retries": true,
    "lake-emerged: five exact output times": true,
    "lake-emerged: maximum_equilibrium_depth_drift": true,
    "lake-emerged: maximum_equilibrium_discharge": true,
    "subcritical-n100: maximum_step_mass_defect": true,
    "subcritical-n100: maximum_step_momentum_defect": true,
    "subcritical-n100: maximum_total_mass_defect": true,
    "subcritical-n100: maximum_total_momentum_defect": true,
    "subcritical-n100: nonnegative depth": true,
    "subcritical-n100: finite arrays": true,
    "subcritical-n100: face CFL": true,
    "subcritical-n100: no repairs or retries": true,
    "subcritical-n100: five exact output times": true,
    "subcritical-n200: maximum_step_mass_defect": true,
    "subcritical-n200: maximum_step_momentum_defect": true,
    "subcritical-n200: maximum_total_mass_defect": true,
    "subcritical-n200: maximum_total_momentum_defect": true,
    "subcritical-n200: nonnegative depth": true,
    "subcritical-n200: finite arrays": true,
    "subcritical-n200: face CFL": true,
    "subcritical-n200: no repairs or retries": true,
    "subcritical-n200: five exact output times": true,
    "subcritical-n400: maximum_step_mass_defect": true,
    "subcritical-n400: maximum_step_momentum_defect": true,
    "subcritical-n400: maximum_total_mass_defect": true,
    "subcritical-n400: maximum_total_momentum_defect": true,
    "subcritical-n400: nonnegative depth": true,
    "subcritical-n400: finite arrays": true,
    "subcritical-n400: face CFL": true,
    "subcritical-n400: no repairs or retries": true,
    "subcritical-n400: five exact output times": true,
    "subcritical finest relative_depth_l1": true,
    "subcritical relative_depth_l1 refinement 1": true,
    "subcritical relative_depth_l1 refinement 2": true,
    "subcritical finest relative_momentum_l1": true,
    "subcritical relative_momentum_l1 refinement 1": true,
    "subcritical relative_momentum_l1 refinement 2": true,
    "reference: Bernoulli energy constant": true,
    "reference: subcritical branch": true,
    "reference: Gauss8 vs Gauss16 conservative means": true,
    "reference: Ritter total mass": true,
    "reference: Ritter finite difference PDE residual": true,
    "reference: exact dry branch": true,
    "all fixed runs completed": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/index.json

![Preview of represented bed, saved FV surfaces and moving-steady errors.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png)

Preview of represented bed, saved FV surfaces and moving-steady errors.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/attempts/01/source/inputs.json

## Sources and review scope

- O. Delestre et al. (2013). SWASHES: a compilation of shallow water analytic solutions for hydraulic and environmental studies. https://arxiv.org/pdf/1110.0288; review_level=selected-equations-and-fixed-inputs
- E. Audusse, F. Bouchut, M.-O. Bristeau, R. Klein, B. Perthame (2004). A Fast and Stable Well-Balanced Scheme with Hydrostatic Reconstruction for Shallow Water Flows. https://epubs.siam.org/doi/abs/10.1137/S1064827503431090; review_level=bibliography-and-author-follow-up
- E. Audusse, F. Bouchut, M.-O. Bristeau, J. Sainte-Marie (2016). Kinetic entropy inequality and hydrostatic reconstruction scheme for the Saint-Venant system. https://arxiv.org/pdf/1409.3825; review_level=selected-scheme-equations
- Institut Denis Poisson / SWASHES authors (n.d.). SWASHES project page. https://www.idpoisson.fr/en/swashes-es/; review_level=official-project-scope-and-rights

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
