# 乾いた河床のダム破壊：実際のwetting/drying

右半分を厳密にh=q=0として開始する浅水方程式を解き、実際の乾湿前線の進行と保存をRitter解析解と比較します。

**使用手法**

- [Godunov型有限体積法](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=ja) (`godunov`)
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) (`hll`)
- [前進Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja) (`forward-euler`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja#dry-bed-dam-break-ja-algorithm)

同じ有限体積ソルバーが乾状態h=q=0を直接扱います。片側乾床HLL波速はu−c,u+2c（反対向きも同様）。面Courant数.4で前進Euler更新し、状態の切上げなしに全更新後の非負性と共有流束収支を記録します。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。

$$
c_L=\sqrt{gh_L},\quad x_A=x_0-c_Lt,\quad x_B=x_0+2c_Lt
$$

$$
h=(2c_L-(x-x_0)/t)^2/(9g),\quad u=\tfrac23((x-x_0)/t+c_L)\quad (x_A<x<x_B)
$$

$$
\bar U_i^{\mathrm{ref}}=\Delta x^{-1}\int_{C_i}(h,hu)^Tdx,\quad x_{.001}=x_B-3t\sqrt{g(0.001)}
$$

- [浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-ja) (`shallow-water`)

平坦床・無摩擦、[−10,10]m、ダムx=0、左深さ1m・右0m、初速0、g=9.81、t=.5s、1600/3200/6400セル。SWASHESのRitter式を明示した別スケールで使い、原例の.005m・6s入力とは区別します。


**問題の図**

![乾いた河床のダム破壊：実際のwetting/drying：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[乾燥床へのRitter破堤流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja) (`dry-bed-dam-break`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja#dry-bed-dam-break-ja-validation)

全段の水深min、新たに濡れた初期乾セル数、残る乾セル数、境界流束を含む質量・運動量収支を保存します。Ritterのhとhuをファン端で分割したGauss8セル平均と比較し、Gauss16・全質量・PDE残差で参照を確認。3格子L1細分化とh≥.001mの最右セル中心を検査します。 水深L1の合否は初回と同じ固定参照質量5m²で正規化し、領域を広げたことによる基準の緩和を防ぎます。領域全体の相対L1は別の診断です。

- [Ritter乾燥床破堤：g9.81の専用セル平均参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ritter-dry-bed-ja) (`ritter-dry-bed`; 同じ問題の参照 · 解析参照)

前線診断はセル平均の.001m等深線で、厳密な支持端を別に保存します。非負性は固定実行の実測です。初期乾セルの濡れを検査し、後退汀線・周期的な再乾燥、実地洪水、摩擦や地形上の移動前線は検証しません。 初回100/200/400セル・[−5,5]mでは28検査と105/109判定が合格し、乾セル残存3判定と前線誤差.3960>.25mが不合格でした。元の全記録を保持し、許容条件を変えず領域・格子を細分化しました。 領域・格子だけを変えた第2回は微小な裾のbinary64 underflowで停止しました。第3回は同じHLL更新の水量packetによる代数的評価を導入し、元の28検査に3検査を追加します。

- [浅水／乾床への膨張波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swe-dry-bed-ja) (`swe-dry-bed`; 関連モデルの参照 · 解析参照)

既存の乾燥床浅水参照は元の重力・領域・時刻を保持します。今回のg9.81・[-10,10]・t.5は専用Ritter参照で照合します。
## 前提・単位・境界

平坦床・無摩擦、[−10,10]m、ダムx=0、左深さ1m・右0m、初速0、g=9.81、t=.5s、1600/3200/6400セル。SWASHESのRitter式を明示した別スケールで使い、原例の.005m・6s入力とは区別します。

**編集上の補足**

前線診断はセル平均の.001m等深線で、厳密な支持端を別に保存します。非負性は固定実行の実測です。初期乾セルの濡れを検査し、後退汀線・周期的な再乾燥、実地洪水、摩擦や地形上の移動前線は検証しません。 初回100/200/400セル・[−5,5]mでは28検査と105/109判定が合格し、乾セル残存3判定と前線誤差.3960>.25mが不合格でした。元の全記録を保持し、許容条件を変えず領域・格子を細分化しました。 領域・格子だけを変えた第2回は微小な裾のbinary64 underflowで停止しました。第3回は同じHLL更新の水量packetによる代数的評価を導入し、元の28検査に3検査を追加します。 第3回は108/109判定が合格し、最細の前線誤差.27415>.25mで不合格でした。第4回は同じ領域のRitter格子だけを1600/3200/6400に細分化します。相対水深L1は領域内参照質量で正規化し、領域変更を比べるため絶対L1も保存します。 最終改訂4の固定格子は1600/3200/6400、領域[-10,10]m、t=.5sです。31単体検査と群全体109判定に合格しました。領域拡大による規格化の有利化を避けるため、受入判定の水深L1は元の固定参照質量5m²で規格化し、最細の値は.001773819、絶対水深L1は.008869095m²です。拡大領域の参照質量10m²による.000886909は別の診断値で、受入基準には使いません。相対運動量L1は.009590172、水深.001m等値線の前縁誤差は.2069613m<.25m、最終の真の乾燥セルは1679です。前三改訂の不合格を保持し、深さfloor・状態clip・再試行は0です。

## 採用した計算法

同じ有限体積ソルバーが乾状態h=q=0を直接扱います。片側乾床HLL波速はu−c,u+2c（反対向きも同様）。面Courant数.4で前進Euler更新し、状態の切上げなしに全更新後の非負性と共有流束収支を記録します。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。

$$
c_L=\sqrt{gh_L},\quad x_A=x_0-c_Lt,\quad x_B=x_0+2c_Lt
$$

$$
h=(2c_L-(x-x_0)/t)^2/(9g),\quad u=\tfrac23((x-x_0)/t+c_L)\quad (x_A<x<x_B)
$$

$$
\bar U_i^{\mathrm{ref}}=\Delta x^{-1}\int_{C_i}(h,hu)^Tdx,\quad x_{.001}=x_B-3t\sqrt{g(0.001)}
$$

## 比較・検証

全段の水深min、新たに濡れた初期乾セル数、残る乾セル数、境界流束を含む質量・運動量収支を保存します。Ritterのhとhuをファン端で分割したGauss8セル平均と比較し、Gauss16・全質量・PDE残差で参照を確認。3格子L1細分化とh≥.001mの最右セル中心を検査します。 水深L1の合否は初回と同じ固定参照質量5m²で正規化し、領域を広げたことによる基準の緩和を防ぎます。領域全体の相対L1は別の診断です。

## 確認の限界

前線診断はセル平均の.001m等深線で、厳密な支持端を別に保存します。非負性は固定実行の実測です。初期乾セルの濡れを検査し、後退汀線・周期的な再乾燥、実地洪水、摩擦や地形上の移動前線は検証しません。 初回100/200/400セル・[−5,5]mでは28検査と105/109判定が合格し、乾セル残存3判定と前線誤差.3960>.25mが不合格でした。元の全記録を保持し、許容条件を変えず領域・格子を細分化しました。 領域・格子だけを変えた第2回は微小な裾のbinary64 underflowで停止しました。第3回は同じHLL更新の水量packetによる代数的評価を導入し、元の28検査に3検査を追加します。 第3回は108/109判定が合格し、最細の前線誤差.27415>.25mで不合格でした。第4回は同じ領域のRitter格子だけを1600/3200/6400に細分化します。相対水深L1は領域内参照質量で正規化し、領域変更を比べるため絶対L1も保存します。

## 保存実測値と判定

```json
{
  "metrics": {
    "n": 6400,
    "steps": 2263,
    "time": 0.5,
    "depth_l1": 0.00886909478548199,
    "momentum_l1": 0.02351989621706402,
    "relative_depth_l1": 0.0008869094785479971,
    "relative_momentum_l1": 0.009590171750074893,
    "depth_linf": 0.018378452319254834,
    "minimum_depth": 0.0,
    "maximum_depth": 1.0,
    "maximum_velocity": 5.618969641557241,
    "maximum_courant": 0.4000000000000001,
    "maximum_step_mass_defect": 2.175706973437462e-15,
    "maximum_step_momentum_defect": 2.47198095326695e-17,
    "minimum_staying_coefficient": 0.6038337128225417,
    "maximum_total_mass_defect": 4.973799150320701e-14,
    "maximum_total_momentum_defect": 7.549516567451064e-15,
    "mass_change": -7.904787935332912e-15,
    "boundary_mass_change": 0.0,
    "bed_momentum_impulse": 0.0,
    "initial_dry_cells": 3200,
    "final_dry_cells": 1679,
    "newly_wet_cells": 1521,
    "all_saved_values_finite": true,
    "depth_floor_count": 0,
    "state_clip_count": 0,
    "rejected_steps": 0,
    "retries": 0,
    "front_depth_threshold": 0.001,
    "numerical_threshold_front": 2.7765625000000007,
    "analytic_threshold_front": 2.9835237865001925,
    "analytic_support_front": 3.132091952673165,
    "threshold_front_error": 0.20696128650019174,
    "depth_acceptance_reference_mass": 5.0,
    "fixed_reference_relative_depth_l1": 0.001773818957096398
  },
  "checks": {
    "ritter-n1600: maximum_step_mass_defect": true,
    "ritter-n1600: maximum_step_momentum_defect": true,
    "ritter-n1600: maximum_total_mass_defect": true,
    "ritter-n1600: maximum_total_momentum_defect": true,
    "ritter-n1600: nonnegative depth": true,
    "ritter-n1600: finite arrays": true,
    "ritter-n1600: face CFL": true,
    "ritter-n1600: no repairs or retries": true,
    "ritter-n1600: five exact output times": true,
    "ritter-n1600: actual wetting": true,
    "ritter-n1600: dry cells retained": true,
    "ritter-n3200: maximum_step_mass_defect": true,
    "ritter-n3200: maximum_step_momentum_defect": true,
    "ritter-n3200: maximum_total_mass_defect": true,
    "ritter-n3200: maximum_total_momentum_defect": true,
    "ritter-n3200: nonnegative depth": true,
    "ritter-n3200: finite arrays": true,
    "ritter-n3200: face CFL": true,
    "ritter-n3200: no repairs or retries": true,
    "ritter-n3200: five exact output times": true,
    "ritter-n3200: actual wetting": true,
    "ritter-n3200: dry cells retained": true,
    "ritter-n6400: maximum_step_mass_defect": true,
    "ritter-n6400: maximum_step_momentum_defect": true,
    "ritter-n6400: maximum_total_mass_defect": true,
    "ritter-n6400: maximum_total_momentum_defect": true,
    "ritter-n6400: nonnegative depth": true,
    "ritter-n6400: finite arrays": true,
    "ritter-n6400: face CFL": true,
    "ritter-n6400: no repairs or retries": true,
    "ritter-n6400: five exact output times": true,
    "ritter-n6400: actual wetting": true,
    "ritter-n6400: dry cells retained": true,
    "ritter finest relative_depth_l1": true,
    "ritter relative_depth_l1 refinement 1": true,
    "ritter relative_depth_l1 refinement 2": true,
    "ritter finest relative_momentum_l1": true,
    "ritter relative_momentum_l1 refinement 1": true,
    "ritter relative_momentum_l1 refinement 2": true,
    "finest threshold front error": true,
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

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/index.json

![実際の1次元浅水計算の保存配列による水深・流量と乾湿前線のプレビュー。時空間図は1次元の5保存時刻です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png)

実際の1次元浅水計算の保存配列による水深・流量と乾湿前線のプレビュー。時空間図は1次元の5保存時刻です。

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

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/attempts/01/source/inputs.json

## 出典と確認範囲

- O. Delestre et al. (2013). SWASHES: a compilation of shallow water analytic solutions for hydraulic and environmental studies. https://arxiv.org/pdf/1110.0288; review_level=selected-equations-and-fixed-inputs
Author arXiv v3: sections2,3.1.1-3.1.3,4.1.2. Bump, lakes, Bernoulli and Ritter formulas inspected; no full-library audit or SWASHES execution/source reuse.

- E. Audusse, F. Bouchut, M.-O. Bristeau, R. Klein, B. Perthame (2004). A Fast and Stable Well-Balanced Scheme with Hydrostatic Reconstruction for Shallow Water Flows. https://epubs.siam.org/doi/abs/10.1137/S1064827503431090; review_level=bibliography-and-author-follow-up
Publisher/author bibliography checked. Author-linked original PDF retrieval timed out; HR algebra read in author follow-up arXiv1409.3825. No full original-paper audit.

- E. Audusse, F. Bouchut, M.-O. Bristeau, J. Sainte-Marie (2016). Kinetic entropy inequality and hydrostatic reconstruction scheme for the Saint-Venant system. https://arxiv.org/pdf/1409.3825; review_level=selected-scheme-equations
arXiv v2 section1 model/entropy caveat; section3.1 equations3.1-3.5 face states and pressure corrections. Full kinetic proof not audited or claimed for this HLL solver.

- Institut Denis Poisson / SWASHES authors (n.d.). SWASHES project page. https://www.idpoisson.fr/en/swashes-es/; review_level=official-project-scope-and-rights
Official project/library purpose, CeCILL-v2 licensing and corrected-paper/addendum notice inspected. No library code copied or executed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Dry-bed dam break: actual wetting and dry states

Start the right half at exactly h=q=0 and compare wetting-front advance, conservation and conservative errors with the Ritter analytic solution.

**Methods used**

- [Godunov-type finite volumes](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en) (`godunov`)
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [Forward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en) (`forward-euler`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en#dry-bed-dam-break-en-algorithm)

The FV solver supports h=q=0 directly; one-sided dry HLL speeds use u-c/u+2c and their reflection. Forward Euler at face CFL .4 records every minimum and shared-flux budget without raising cell depths. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.

$$
c_L=\sqrt{gh_L},\quad x_A=x_0-c_Lt,\quad x_B=x_0+2c_Lt
$$

$$
h=(2c_L-(x-x_0)/t)^2/(9g),\quad u=\tfrac23((x-x_0)/t+c_L)\quad (x_A<x<x_B)
$$

$$
\bar U_i^{\mathrm{ref}}=\Delta x^{-1}\int_{C_i}(h,hu)^Tdx,\quad x_{.001}=x_B-3t\sqrt{g(0.001)}
$$

- [Shallow-water equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-en) (`shallow-water`)

Flat frictionless bed on[-10,10]m, dam0, hL=1m/hR=0, initial velocity0, g=9.81, t=.5s,1600/3200/6400 cells. The Ritter formula uses an explicit rescaling distinct from the paper numerical example.


**Problem figure**

![Dry-bed dam break: actual wetting and dry states: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Ritter dam break onto a dry bed](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en) (`dry-bed-dam-break`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en#dry-bed-dam-break-en-validation)

Record all FE minima, newly wetted and remaining dry cells, boundary-aware mass/momentum budgets, and L1 refinement. Split Gauss8 h/hu references are qualified by Gauss16, mass and PDE identities. Diagnose the rightmost cell center with mean h>=.001m. Depth acceptance uses the original fixed5m2 reference mass, preventing domain extension from weakening the criterion; full-domain relativeL1 remains a separate diagnostic.

- [Ritter dry-bed dam break: dedicated g9.81 cell-mean reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ritter-dry-bed-en) (`ritter-dry-bed`; Same-problem reference · Analytic reference)

The .001m mean-depth contour differs from the analytic support edge, which is reported separately. These fixed runs test wetting of initially dry cells. Retreating shorelines, re-drying cycles, real floods, friction and moving fronts over topography are outside scope. The initial100/200/400-cell [-5,5]m attempt passed28 tests and105/109 gates; three retained-dry-cell gates and the .3960m>.25m contour error failed. All original records remain archived; revision2 enlarges/refines the input without changing acceptance. Revision2 then stopped on a binary64 subnormal-tail dry-momentum artifact. Revision3 factors the same HLL update into water packets and adds three regression/equivalence tests; the original28 remain unchanged.

- [Shallow water / dry-bed fan](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swe-dry-bed-en) (`swe-dry-bed`; Related-model reference · Analytic reference)

Retain the historical dry-bed reference gravity/domain/time unchanged. The new g9.81,[-10,10],t.5 computation uses its dedicated Ritter reference.
## Assumptions, units and boundaries

Flat frictionless bed on[-10,10]m, dam0, hL=1m/hR=0, initial velocity0, g=9.81, t=.5s,1600/3200/6400 cells. The Ritter formula uses an explicit rescaling distinct from the paper numerical example.

**Editorial clarification**

The .001m mean-depth contour differs from the analytic support edge, which is reported separately. These fixed runs test wetting of initially dry cells. Retreating shorelines, re-drying cycles, real floods, friction and moving fronts over topography are outside scope. The initial100/200/400-cell [-5,5]m attempt passed28 tests and105/109 gates; three retained-dry-cell gates and the .3960m>.25m contour error failed. All original records remain archived; revision2 enlarges/refines the input without changing acceptance. Revision2 then stopped on a binary64 subnormal-tail dry-momentum artifact. Revision3 factors the same HLL update into water packets and adds three regression/equivalence tests; the original28 remain unchanged. Revision3 passed108/109 gates but failed the .27415m>.25m contour criterion. Revision4 refines only Ritter grids to1600/3200/6400. Relative depth L1 is normalized by domain reference mass; absolute L1 is also retained because the domain changed between revisions1 and2. Final revision4 uses1600/3200/6400cells on[-10,10]m at t.5s and passed31 unit checks and all109 group gates. Acceptance depthL1 retains the original fixed reference mass5m², giving finest.001773819 and absolute depthL1.008869095m². Normalization by the enlarged-domain reference mass10m² gives.000886909 as a separate diagnostic, never an easier acceptance criterion. Relative momentumL1 is.009590172; the depth.001m contour error is.2069613m<.25m and1679 genuinely dry cells remain. All three earlier failures are retained; depth floors,state clips and retries are zero.

## Adopted numerical method

The FV solver supports h=q=0 directly; one-sided dry HLL speeds use u-c/u+2c and their reflection. Forward Euler at face CFL .4 records every minimum and shared-flux budget without raising cell depths. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.

$$
c_L=\sqrt{gh_L},\quad x_A=x_0-c_Lt,\quad x_B=x_0+2c_Lt
$$

$$
h=(2c_L-(x-x_0)/t)^2/(9g),\quad u=\tfrac23((x-x_0)/t+c_L)\quad (x_A<x<x_B)
$$

$$
\bar U_i^{\mathrm{ref}}=\Delta x^{-1}\int_{C_i}(h,hu)^Tdx,\quad x_{.001}=x_B-3t\sqrt{g(0.001)}
$$

## References and validation

Record all FE minima, newly wetted and remaining dry cells, boundary-aware mass/momentum budgets, and L1 refinement. Split Gauss8 h/hu references are qualified by Gauss16, mass and PDE identities. Diagnose the rightmost cell center with mean h>=.001m. Depth acceptance uses the original fixed5m2 reference mass, preventing domain extension from weakening the criterion; full-domain relativeL1 remains a separate diagnostic.

## Limits

The .001m mean-depth contour differs from the analytic support edge, which is reported separately. These fixed runs test wetting of initially dry cells. Retreating shorelines, re-drying cycles, real floods, friction and moving fronts over topography are outside scope. The initial100/200/400-cell [-5,5]m attempt passed28 tests and105/109 gates; three retained-dry-cell gates and the .3960m>.25m contour error failed. All original records remain archived; revision2 enlarges/refines the input without changing acceptance. Revision2 then stopped on a binary64 subnormal-tail dry-momentum artifact. Revision3 factors the same HLL update into water packets and adds three regression/equivalence tests; the original28 remain unchanged. Revision3 passed108/109 gates but failed the .27415m>.25m contour criterion. Revision4 refines only Ritter grids to1600/3200/6400. Relative depth L1 is normalized by domain reference mass; absolute L1 is also retained because the domain changed between revisions1 and2.

## Stored measurements and decisions

```json
{
  "metrics": {
    "n": 6400,
    "steps": 2263,
    "time": 0.5,
    "depth_l1": 0.00886909478548199,
    "momentum_l1": 0.02351989621706402,
    "relative_depth_l1": 0.0008869094785479971,
    "relative_momentum_l1": 0.009590171750074893,
    "depth_linf": 0.018378452319254834,
    "minimum_depth": 0.0,
    "maximum_depth": 1.0,
    "maximum_velocity": 5.618969641557241,
    "maximum_courant": 0.4000000000000001,
    "maximum_step_mass_defect": 2.175706973437462e-15,
    "maximum_step_momentum_defect": 2.47198095326695e-17,
    "minimum_staying_coefficient": 0.6038337128225417,
    "maximum_total_mass_defect": 4.973799150320701e-14,
    "maximum_total_momentum_defect": 7.549516567451064e-15,
    "mass_change": -7.904787935332912e-15,
    "boundary_mass_change": 0.0,
    "bed_momentum_impulse": 0.0,
    "initial_dry_cells": 3200,
    "final_dry_cells": 1679,
    "newly_wet_cells": 1521,
    "all_saved_values_finite": true,
    "depth_floor_count": 0,
    "state_clip_count": 0,
    "rejected_steps": 0,
    "retries": 0,
    "front_depth_threshold": 0.001,
    "numerical_threshold_front": 2.7765625000000007,
    "analytic_threshold_front": 2.9835237865001925,
    "analytic_support_front": 3.132091952673165,
    "threshold_front_error": 0.20696128650019174,
    "depth_acceptance_reference_mass": 5.0,
    "fixed_reference_relative_depth_l1": 0.001773818957096398
  },
  "checks": {
    "ritter-n1600: maximum_step_mass_defect": true,
    "ritter-n1600: maximum_step_momentum_defect": true,
    "ritter-n1600: maximum_total_mass_defect": true,
    "ritter-n1600: maximum_total_momentum_defect": true,
    "ritter-n1600: nonnegative depth": true,
    "ritter-n1600: finite arrays": true,
    "ritter-n1600: face CFL": true,
    "ritter-n1600: no repairs or retries": true,
    "ritter-n1600: five exact output times": true,
    "ritter-n1600: actual wetting": true,
    "ritter-n1600: dry cells retained": true,
    "ritter-n3200: maximum_step_mass_defect": true,
    "ritter-n3200: maximum_step_momentum_defect": true,
    "ritter-n3200: maximum_total_mass_defect": true,
    "ritter-n3200: maximum_total_momentum_defect": true,
    "ritter-n3200: nonnegative depth": true,
    "ritter-n3200: finite arrays": true,
    "ritter-n3200: face CFL": true,
    "ritter-n3200: no repairs or retries": true,
    "ritter-n3200: five exact output times": true,
    "ritter-n3200: actual wetting": true,
    "ritter-n3200: dry cells retained": true,
    "ritter-n6400: maximum_step_mass_defect": true,
    "ritter-n6400: maximum_step_momentum_defect": true,
    "ritter-n6400: maximum_total_mass_defect": true,
    "ritter-n6400: maximum_total_momentum_defect": true,
    "ritter-n6400: nonnegative depth": true,
    "ritter-n6400: finite arrays": true,
    "ritter-n6400: face CFL": true,
    "ritter-n6400: no repairs or retries": true,
    "ritter-n6400: five exact output times": true,
    "ritter-n6400: actual wetting": true,
    "ritter-n6400: dry cells retained": true,
    "ritter finest relative_depth_l1": true,
    "ritter relative_depth_l1 refinement 1": true,
    "ritter relative_depth_l1 refinement 2": true,
    "ritter finest relative_momentum_l1": true,
    "ritter relative_momentum_l1 refinement 1": true,
    "ritter relative_momentum_l1 refinement 2": true,
    "finest threshold front error": true,
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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/index.json

![Preview from actual saved 1D shallow-water depth/discharge arrays. The space-time panel shows five saved times, not a 2D flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png)

Preview from actual saved 1D shallow-water depth/discharge arrays. The space-time panel shows five saved times, not a 2D flow.

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

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/attempts/01/source/inputs.json

## Sources and review scope

- O. Delestre et al. (2013). SWASHES: a compilation of shallow water analytic solutions for hydraulic and environmental studies. https://arxiv.org/pdf/1110.0288; review_level=selected-equations-and-fixed-inputs
Author arXiv v3: sections2,3.1.1-3.1.3,4.1.2. Bump, lakes, Bernoulli and Ritter formulas inspected; no full-library audit or SWASHES execution/source reuse.

- E. Audusse, F. Bouchut, M.-O. Bristeau, R. Klein, B. Perthame (2004). A Fast and Stable Well-Balanced Scheme with Hydrostatic Reconstruction for Shallow Water Flows. https://epubs.siam.org/doi/abs/10.1137/S1064827503431090; review_level=bibliography-and-author-follow-up
Publisher/author bibliography checked. Author-linked original PDF retrieval timed out; HR algebra read in author follow-up arXiv1409.3825. No full original-paper audit.

- E. Audusse, F. Bouchut, M.-O. Bristeau, J. Sainte-Marie (2016). Kinetic entropy inequality and hydrostatic reconstruction scheme for the Saint-Venant system. https://arxiv.org/pdf/1409.3825; review_level=selected-scheme-equations
arXiv v2 section1 model/entropy caveat; section3.1 equations3.1-3.5 face states and pressure corrections. Full kinetic proof not audited or claimed for this HLL solver.

- Institut Denis Poisson / SWASHES authors (n.d.). SWASHES project page. https://www.idpoisson.fr/en/swashes-es/; review_level=official-project-scope-and-rights
Official project/library purpose, CeCILL-v2 licensing and corrected-paper/addendum notice inspected. No library code copied or executed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
