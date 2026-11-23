# 浅水流：地形・静止湖・乾燥床

浅水系の地形源項と静水再構成を、全湿潤・露出床の静止湖とSWASHESの定常Bernoulli流で検査します。別の平坦床Ritter破堤は、真の乾燥状態・保存収支・固定水深の前縁を確認します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## SWASHES地形流：静水と非零流量の定常解

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
### 前提・単位・境界

1次元、g=9.81、長さ25m、8<x<12でz=.2−.05(x−10)²m。水位.5/.1mの静水は200セル、流量4.42m²/s・下流深さ2mの定常流は100/200/400セル、t=2s。地形は区分定数セル平均。定常流から開始し、静水からの定常化実験とは区別します。

**編集上の補足**

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。 最終改訂は31単体検査と群全体8計算109判定に合格しました。定常流の最細N400では水深L1約.0249108、相対水深L1約.000505933です。静止湖の表現した床の釣合い、有限時間の移動定常流の誤差、乾燥床の前縁誤差を別々に保存します。

### 採用した計算法

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

### 比較・検証

31単体検査と8固定計算を事前固定。静水の水深・流量の最大変化、全FE段の非負水深、共有流束と地形運動量の収支、定常流3格子の保存量セル平均L1誤差・細分化比を保存します。独立したBernoulli二分法のエネルギー一定・亜臨界枝を照合します。

### 確認の限界

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- O. Delestre et al. (2013). SWASHES: a compilation of shallow water analytic solutions for hydraulic and environmental studies. https://arxiv.org/pdf/1110.0288; review_level=selected-equations-and-fixed-inputs
Author arXiv v3: sections2,3.1.1-3.1.3,4.1.2. Bump, lakes, Bernoulli and Ritter formulas inspected; no full-library audit or SWASHES execution/source reuse.

- E. Audusse, F. Bouchut, M.-O. Bristeau, R. Klein, B. Perthame (2004). A Fast and Stable Well-Balanced Scheme with Hydrostatic Reconstruction for Shallow Water Flows. https://epubs.siam.org/doi/abs/10.1137/S1064827503431090; review_level=bibliography-and-author-follow-up
Publisher/author bibliography checked. Author-linked original PDF retrieval timed out; HR algebra read in author follow-up arXiv1409.3825. No full original-paper audit.

- E. Audusse, F. Bouchut, M.-O. Bristeau, J. Sainte-Marie (2016). Kinetic entropy inequality and hydrostatic reconstruction scheme for the Saint-Venant system. https://arxiv.org/pdf/1409.3825; review_level=selected-scheme-equations
arXiv v2 section1 model/entropy caveat; section3.1 equations3.1-3.5 face states and pressure corrections. Full kinetic proof not audited or claimed for this HLL solver.

- Institut Denis Poisson / SWASHES authors (n.d.). SWASHES project page. https://www.idpoisson.fr/en/swashes-es/; review_level=official-project-scope-and-rights
Official project/library purpose, CeCILL-v2 licensing and corrected-paper/addendum notice inspected. No library code copied or executed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 乾いた河床のダム破壊：実際のwetting/drying

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
### 前提・単位・境界

平坦床・無摩擦、[−10,10]m、ダムx=0、左深さ1m・右0m、初速0、g=9.81、t=.5s、1600/3200/6400セル。SWASHESのRitter式を明示した別スケールで使い、原例の.005m・6s入力とは区別します。

**編集上の補足**

前線診断はセル平均の.001m等深線で、厳密な支持端を別に保存します。非負性は固定実行の実測です。初期乾セルの濡れを検査し、後退汀線・周期的な再乾燥、実地洪水、摩擦や地形上の移動前線は検証しません。 初回100/200/400セル・[−5,5]mでは28検査と105/109判定が合格し、乾セル残存3判定と前線誤差.3960>.25mが不合格でした。元の全記録を保持し、許容条件を変えず領域・格子を細分化しました。 領域・格子だけを変えた第2回は微小な裾のbinary64 underflowで停止しました。第3回は同じHLL更新の水量packetによる代数的評価を導入し、元の28検査に3検査を追加します。 第3回は108/109判定が合格し、最細の前線誤差.27415>.25mで不合格でした。第4回は同じ領域のRitter格子だけを1600/3200/6400に細分化します。相対水深L1は領域内参照質量で正規化し、領域変更を比べるため絶対L1も保存します。 最終改訂4の固定格子は1600/3200/6400、領域[-10,10]m、t=.5sです。31単体検査と群全体109判定に合格しました。領域拡大による規格化の有利化を避けるため、受入判定の水深L1は元の固定参照質量5m²で規格化し、最細の値は.001773819、絶対水深L1は.008869095m²です。拡大領域の参照質量10m²による.000886909は別の診断値で、受入基準には使いません。相対運動量L1は.009590172、水深.001m等値線の前縁誤差は.2069613m<.25m、最終の真の乾燥セルは1679です。前三改訂の不合格を保持し、深さfloor・状態clip・再試行は0です。

### 採用した計算法

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

### 比較・検証

全段の水深min、新たに濡れた初期乾セル数、残る乾セル数、境界流束を含む質量・運動量収支を保存します。Ritterのhとhuをファン端で分割したGauss8セル平均と比較し、Gauss16・全質量・PDE残差で参照を確認。3格子L1細分化とh≥.001mの最右セル中心を検査します。 水深L1の合否は初回と同じ固定参照質量5m²で正規化し、領域を広げたことによる基準の緩和を防ぎます。領域全体の相対L1は別の診断です。

### 確認の限界

前線診断はセル平均の.001m等深線で、厳密な支持端を別に保存します。非負性は固定実行の実測です。初期乾セルの濡れを検査し、後退汀線・周期的な再乾燥、実地洪水、摩擦や地形上の移動前線は検証しません。 初回100/200/400セル・[−5,5]mでは28検査と105/109判定が合格し、乾セル残存3判定と前線誤差.3960>.25mが不合格でした。元の全記録を保持し、許容条件を変えず領域・格子を細分化しました。 領域・格子だけを変えた第2回は微小な裾のbinary64 underflowで停止しました。第3回は同じHLL更新の水量packetによる代数的評価を導入し、元の28検査に3検査を追加します。 第3回は108/109判定が合格し、最細の前線誤差.27415>.25mで不合格でした。第4回は同じ領域のRitter格子だけを1600/3200/6400に細分化します。相対水深L1は領域内参照質量で正規化し、領域変更を比べるため絶対L1も保存します。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- O. Delestre et al. (2013). SWASHES: a compilation of shallow water analytic solutions for hydraulic and environmental studies. https://arxiv.org/pdf/1110.0288; review_level=selected-equations-and-fixed-inputs
Author arXiv v3: sections2,3.1.1-3.1.3,4.1.2. Bump, lakes, Bernoulli and Ritter formulas inspected; no full-library audit or SWASHES execution/source reuse.

- E. Audusse, F. Bouchut, M.-O. Bristeau, R. Klein, B. Perthame (2004). A Fast and Stable Well-Balanced Scheme with Hydrostatic Reconstruction for Shallow Water Flows. https://epubs.siam.org/doi/abs/10.1137/S1064827503431090; review_level=bibliography-and-author-follow-up
Publisher/author bibliography checked. Author-linked original PDF retrieval timed out; HR algebra read in author follow-up arXiv1409.3825. No full original-paper audit.

- E. Audusse, F. Bouchut, M.-O. Bristeau, J. Sainte-Marie (2016). Kinetic entropy inequality and hydrostatic reconstruction scheme for the Saint-Venant system. https://arxiv.org/pdf/1409.3825; review_level=selected-scheme-equations
arXiv v2 section1 model/entropy caveat; section3.1 equations3.1-3.5 face states and pressure corrections. Full kinetic proof not audited or claimed for this HLL solver.

- Institut Denis Poisson / SWASHES authors (n.d.). SWASHES project page. https://www.idpoisson.fr/en/swashes-es/; review_level=official-project-scope-and-rights
Official project/library purpose, CeCILL-v2 licensing and corrected-paper/addendum notice inspected. No library code copied or executed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
