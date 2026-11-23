# Mach 3前向きステップ：壁面収支と多格子検証

実際の2次元Euler有限体積計算を60×20・120×40・240×80でT=4まで行い、別実装のMUSCL有限格子参照と比較します。段差の垂直面・上面を含む実際の数値流束から4保存量の収支を評価し、角のエントロピー補正を加えない変種として図とコードを公開します。

**使用手法**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) (`hll`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja#forward-step-m3-ja-algorithm)

既存Numartの区分定数HLL・非分割x/y発散・Heun/SSPRK(2,2)を小型配布物にし、6種類の境界ごとに両RK段で実際に使う流束を同じ重みで積算します。CFL=.4、各格子の上限20000刻み。全予測・更新段の正の密度と圧力を確認し、状態floor・修復・隠れた再試行はしません。不正段は生配列と完了履歴を保持して失敗します。

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
\Omega=([0,3]\times[0,1])\setminus([0.6,3]\times[0,0.2]),\quad (\rho,u,v,p)_\infty=(1.4,3,0,1)
$$

$$
\sum_{C\subset\Omega}|C|(\bar U_C^{n+1}-\bar U_C^n)=\frac{\Delta t}{2}(B(U^n)+B(U^{(1)})),\quad B=-\sum_{\partial\Omega}|f|\widehat F_n
$$

$$
\epsilon_1(\rho)=\frac{\sum_{C\subset\Omega}|\bar\rho_C-\overline{\rho_{\rm ref}}_C|}{\sum_{C\subset\Omega}|\overline{\rho_{\rm ref}}_C|}
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

γ=1.4の2次元圧縮性Euler保存系。Mach 3の一様流入と、段差・流路上下の反射壁、右端の流出境界を固定入力に定義します。


**問題の図**

![Mach 3前向きステップ：壁面収支と多格子検証：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Mach 3前向きステップ](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja) (`forward-step`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja#forward-step-m3-ja-validation)

入力・受入基準・24単体検査・数値ソースを主計算の初回検査・PDE実行前に固定しました。解析的なMach3垂直衝撃波のRankine–Hugoniot関係、一様な平行流路、壁の質量・エネルギー流束ゼロ、段差の圧力力の向き、実際の4成分収支、不正段の保持を検査します。別実装のC++17 MUSCL/generalized-minmod θ1.5/HLL/HeunによるNy80/160の参照を新規に実行し、保存量を保守的に制限して密度・圧力の全流体領域L1を比較します。参照の再計算は通常の公開ZIP追試には含めず、保存データ・ソース・契約・実行記録を同梱します。 最初の参照Ny160は事前固定の120秒上限で停止した記録を保持し、診断文字列の不要なメモリ割当てだけを除く参照改訂を、主計算の初回実行前に再固定しました。入力・演算・CFL・判定値は変更していません。 24検査と全3計算・45判定が-W errorで合格。主計算の密度L1は.14754/.12878/.10265、圧力L1は.19373/.16015/.12242、密度の最後の2格子の傾きは.327。参照80/160増分は.02636/.03063で、最細主計算差の約.257/.250。全4成分の境界収支の最大相対残差は2.99e-13、全壁の積分質量・エネルギー流束は0でした。主計算3格子は元のMacで約46秒、性能改訂後の参照80/160は約8/65秒です。

- [Mach 3前向きステップ：独立C++有限格子数値参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-forward-step-ja) (`forward-step`; 同じ問題の参照 · 有限格子の数値参照)

新しく独立実行したC++17のMUSCL/HLL/Heun参照を保存量制限で比較します。同じHLL族・Heunと角無補正条件を共有する有限格子数値参照であり、全場の厳密解や誤差上界ではありません。
## 前提・単位・境界

無次元[0,3]×[0,1]からx≥.6・y<.2の固体を除き、γ=1.4、初期・左流入(ρ,u,v,p)=(1.4,3,0,1)。音速1なのでMach3です。右はゼロ勾配流出、上下と段差の両面は法線運動量を反転する滑り壁。格子Nyは5の倍数で両壁を厳密に整列し、固体記憶領域は流体ノルム・積分から除外します。Woodward–Colella型の角エントロピー・エンタルピー再設定は行いません。

**編集上の補足**

有限個の格子と固定入力による軽量検証です。Woodward–Colella型の段差角エントロピー・エンタルピー修正は行わず、角からの数値的なエントロピー層が下流の反射衝撃波・Mach stemに影響し得る設定です。元論文の角補正付きPPM像との一致や、微細なすべり線・渦までの収束を保証しません。

## 採用した計算法

既存Numartの区分定数HLL・非分割x/y発散・Heun/SSPRK(2,2)を小型配布物にし、6種類の境界ごとに両RK段で実際に使う流束を同じ重みで積算します。CFL=.4、各格子の上限20000刻み。全予測・更新段の正の密度と圧力を確認し、状態floor・修復・隠れた再試行はしません。不正段は生配列と完了履歴を保持して失敗します。

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
\Omega=([0,3]\times[0,1])\setminus([0.6,3]\times[0,0.2]),\quad (\rho,u,v,p)_\infty=(1.4,3,0,1)
$$

$$
\sum_{C\subset\Omega}|C|(\bar U_C^{n+1}-\bar U_C^n)=\frac{\Delta t}{2}(B(U^n)+B(U^{(1)})),\quad B=-\sum_{\partial\Omega}|f|\widehat F_n
$$

$$
\epsilon_1(\rho)=\frac{\sum_{C\subset\Omega}|\bar\rho_C-\overline{\rho_{\rm ref}}_C|}{\sum_{C\subset\Omega}|\overline{\rho_{\rm ref}}_C|}
$$

## 比較・検証

入力・受入基準・24単体検査・数値ソースを主計算の初回検査・PDE実行前に固定しました。解析的なMach3垂直衝撃波のRankine–Hugoniot関係、一様な平行流路、壁の質量・エネルギー流束ゼロ、段差の圧力力の向き、実際の4成分収支、不正段の保持を検査します。別実装のC++17 MUSCL/generalized-minmod θ1.5/HLL/HeunによるNy80/160の参照を新規に実行し、保存量を保守的に制限して密度・圧力の全流体領域L1を比較します。参照の再計算は通常の公開ZIP追試には含めず、保存データ・ソース・契約・実行記録を同梱します。 最初の参照Ny160は事前固定の120秒上限で停止した記録を保持し、診断文字列の不要なメモリ割当てだけを除く参照改訂を、主計算の初回実行前に再固定しました。入力・演算・CFL・判定値は変更していません。 24検査と全3計算・45判定が-W errorで合格。主計算の密度L1は.14754/.12878/.10265、圧力L1は.19373/.16015/.12242、密度の最後の2格子の傾きは.327。参照80/160増分は.02636/.03063で、最細主計算差の約.257/.250。全4成分の境界収支の最大相対残差は2.99e-13、全壁の積分質量・エネルギー流束は0でした。主計算3格子は元のMacで約46秒、性能改訂後の参照80/160は約8/65秒です。

## 確認の限界

参照は別実装ですがHLL流束族とHeunを共有し、外部AMROC・LAVA・RKDGを実行した意味ではありません。有限格子の数値参照であり、厳密2D解や誤差上界ではありません。角の特別処理を加えない入力では数値的なエントロピー層が下流へ運ばれうるため、補正付き原著PPMの細部一致を主張しません。全流体領域の差とL∞、固定した角近傍の密度・圧力・エントロピー診断を隠さず残します。傾きは純粋な空間次数の証明ではなく、薄いすべり線・巻き上がり・一般形状や高次精度の収束は未検証です。 正規化した密度の最大差は.592/.670/.665で減少せず、角近傍のlog(p/ρ^γ)の最小値も−.0784/−.1224/−.3510と大きく変わります。これは任意の定数を含む絶対量で、負になるほど誤差が大きいという指標ではありませんが、角の極値や点ごとのパターンが安定・収束したとは主張できません。

## 保存実測値と判定

```json
{
  "metrics": {
    "n": 80,
    "ny": 80,
    "nx": 240,
    "time": 4.0,
    "steps": 5557,
    "fluid_cells": 16128,
    "fluid_area": 2.52,
    "density_l1": 0.10265130952593862,
    "pressure_l1": 0.12242245655875464,
    "density_l2": 0.17407969884723082,
    "density_linf": 0.6649309657923782,
    "minimum_density_all_stages": 0.572306931838617,
    "minimum_pressure_all_stages": 0.7623628074232572,
    "density_min": 0.6990444287976558,
    "density_max": 6.591899988897764,
    "pressure_min": 0.8066533197248239,
    "pressure_max": 12.16201901303801,
    "state_floor_count": 0,
    "rejected_steps": 0,
    "wall_mass_energy_max_abs": 0.0,
    "corner_density_l1": 0.03512271217575579,
    "corner_density_max": 5.840654003919099,
    "corner_pressure_max": 11.902361154385352,
    "corner_entropy_min": -0.35096779612542683,
    "corner_entropy_max": 0.3051128979484177
  },
  "checks": {
    "three final-time refinements complete": true,
    "ny20: requested time reached": true,
    "ny20: minimum_density_all_stages": true,
    "ny20: minimum_pressure_all_stages": true,
    "ny20: state_floor_count": true,
    "ny20: rejected_steps": true,
    "ny20: exact aligned fluid area": true,
    "ny20: mass including step-wall boundary balance": true,
    "ny20: x momentum including step-wall boundary balance": true,
    "ny20: y momentum including step-wall boundary balance": true,
    "ny20: energy including step-wall boundary balance": true,
    "ny20: stationary-wall integrated mass/energy flux": true,
    "ny20: unmasked full-field/corner diagnostics retained": true,
    "ny40: requested time reached": true,
    "ny40: minimum_density_all_stages": true,
    "ny40: minimum_pressure_all_stages": true,
    "ny40: state_floor_count": true,
    "ny40: rejected_steps": true,
    "ny40: exact aligned fluid area": true,
    "ny40: mass including step-wall boundary balance": true,
    "ny40: x momentum including step-wall boundary balance": true,
    "ny40: y momentum including step-wall boundary balance": true,
    "ny40: energy including step-wall boundary balance": true,
    "ny40: stationary-wall integrated mass/energy flux": true,
    "ny40: unmasked full-field/corner diagnostics retained": true,
    "ny80: requested time reached": true,
    "ny80: minimum_density_all_stages": true,
    "ny80: minimum_pressure_all_stages": true,
    "ny80: state_floor_count": true,
    "ny80: rejected_steps": true,
    "ny80: exact aligned fluid area": true,
    "ny80: mass including step-wall boundary balance": true,
    "ny80: x momentum including step-wall boundary balance": true,
    "ny80: y momentum including step-wall boundary balance": true,
    "ny80: energy including step-wall boundary balance": true,
    "ny80: stationary-wall integrated mass/energy flux": true,
    "ny80: unmasked full-field/corner diagnostics retained": true,
    "finest density_l1": true,
    "finest pressure_l1": true,
    "density difference decreases across the fixed grids": true,
    "last-pair density difference slope": true,
    "reference increment density_l1": true,
    "reference increment / primary finest density_l1": true,
    "reference increment pressure_l1": true,
    "reference increment / primary finest pressure_l1": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/atlas-forward-step-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Paul Woodward and Phillip Colella (1984). The numerical simulation of two-dimensional fluid flow with strong shocks. https://www.sciencedirect.com/science/article/pii/0021999184901426; review_level=previously-reviewed-publisher-metadata; setup cross-checked against Cockburn-Shu1991 primary report
強衝撃波の標準比較の原著として引用。今回の出版社ページは取得拒否、原著本文を直接通読したとは主張せず、前向きステップの設定と角処理の区別はCockburn–Shu(1991)の一次資料で確認した。

- Bernardo Cockburn and Chi-Wang Shu (1991). The P¹-RKDG Method for Two-Dimensional Euler Equations of Gas Dynamics. https://ntrs.nasa.gov/citations/19910015505; review_level=selected-text-review: Example2 printedp7/PDFpage11 and Fig3 captions printedp8/PDFpage12
Example2の形状、Mach3一様流、流入・流出・反射境界、T=4、および角の特別処理あり/なしを比べるFig3の説明を確認。本文の選択箇所の確認であり、図の転載・RKDGの実行は行わない。

- Ralf Deiterding / AMROC project (2004). 2D Euler equations — Forward facing step. https://amroc.sourceforge.net/examples/euler/2d/html/ffstep_n.htm; review_level=official-example-selected-problem-description
角セルに特別なエントロピー補正を加えない変種とT=4の公式説明を確認。AMROCの計算・AMR・図をこの例へ取り込んだものではない。

- Hiroshi Koyama (2026). Independent C++17 MUSCL finite-volume reference for the uncorrected Mach-3 forward-facing step. https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/references/reference.cpp; review_level=source-and-preregistered-new-execution
主計算の空間演算をimportしない別実装。HLLとHeunの族は共有し、外部エンジンの実行ではありません。初版の時間切れと診断引数だけの性能改訂を保存し、参照データ・入力・実行履歴・契約を同梱します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Mach3 forward step: wall budgets and grid verification

Actual2D Euler finite volumes evolve60x20,120x40 and240x80 meshes toT4, comparing separately implemented MUSCL finite-grid references. Actual numerical wall fluxes, including the vertical and horizontal step faces, close all four conserved budgets. Figures and code explicitly use the variant without corner entropy correction.

**Methods used**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en#forward-step-m3-en-algorithm)

Published Numart piecewise-constant HLL, unsplit x/y divergence and Heun/SSPRK(2,2) become a standalone package. Six boundary categories integrate the actual fluxes at both RK stages with identical weights. CFL.4, at most20000steps per grid. Every predictor/update checks positive density and pressure. No state floor, repair or hidden retry; invalid stages retain raw arrays/completed history and fail.

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
\Omega=([0,3]\times[0,1])\setminus([0.6,3]\times[0,0.2]),\quad (\rho,u,v,p)_\infty=(1.4,3,0,1)
$$

$$
\sum_{C\subset\Omega}|C|(\bar U_C^{n+1}-\bar U_C^n)=\frac{\Delta t}{2}(B(U^n)+B(U^{(1)})),\quad B=-\sum_{\partial\Omega}|f|\widehat F_n
$$

$$
\epsilon_1(\rho)=\frac{\sum_{C\subset\Omega}|\bar\rho_C-\overline{\rho_{\rm ref}}_C|}{\sum_{C\subset\Omega}|\overline{\rho_{\rm ref}}_C|}
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Two-dimensional compressible Euler conservation laws with gamma=1.4. Fixed inputs define uniform Mach-3 inflow, reflecting channel/step walls and right outflow.


**Problem figure**

![Mach3 forward step: wall budgets and grid verification: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Mach-3 forward-facing step](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en) (`forward-step`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en#forward-step-m3-en-validation)

Inputs, acceptance,24 unit checks and numerical source were frozen before the first primary test/PDE execution. Checks cover analytic Mach3 normal-shock Rankine-Hugoniot identities, uniform parallel-channel flow, zero stationary-wall mass/energy flux, step-pressure force orientation, actual four-component budgets and raw failure retention. Newly executed separate C++17 MUSCL/generalized-minmod theta1.5/HLL/Heun references atNy80/160 are conservatively restricted for whole-fluid density/pressure L1 comparison. Ordinary public-ZIP verification reads saved reference data; reference source, contracts and execution records are bundled. The first referenceNy160 exhausted its preregistered120second budget; that actual timeout is preserved. A reference revision removed only unnecessary diagnostic-string allocation and was repinned before first primary execution; physical inputs,arithmetic,CFL and acceptance values did not change. All24 tests, three final-time runs and45 gates passed with-W error. Primary density L1=.14754/.12878/.10265, pressure L1=.19373/.16015/.12242 and last-pair density slope=.327. Reference80/160 increments=.02636/.03063, about.257/.250 of the finest primary differences. Maximum four-component relative boundary-budget residual=2.99e-13; all integrated wall mass/energy fluxes are zero. The three primary grids took about46seconds on the original Mac; revised reference80/160 took about8/65seconds.

- [Mach-3 forward-facing step: independent C++ finite-grid numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-forward-step-en) (`forward-step`; Same-problem reference · Finite-grid numerical reference)

Conservatively restrict newly independently executed C++17 MUSCL/HLL/Heun reference data. The finite-grid numerical reference shares the HLL family,Heun and the uncorrected corner; it is not an exact full-field solution or error bound.
## Assumptions, units and boundaries

Nondimensional[0,3]x[0,1] minus solidx>=.6,y<.2; gamma1.4, initial/left-inflow(rho,u,v,p)=(1.4,3,0,1), giving sound speed1 and Mach3. Right zero-gradient outflow; top,bottom and both step faces are slip walls by normal-momentum reflection. Ny multiples of5 align both walls exactly; solid storage is excluded from every fluid norm/integral. No Woodward-Colella corner entropy/enthalpy reset.

**Editorial clarification**

A lightweight verification on fixed inputs and a small number of grids. No Woodward–Colella corner entropy/enthalpy correction is applied; the numerical entropy layer from the corner can affect downstream reflected shocks and the Mach stem. It does not establish agreement with the original corner-corrected PPM picture or convergence of fine slip lines and vortices.

## Adopted numerical method

Published Numart piecewise-constant HLL, unsplit x/y divergence and Heun/SSPRK(2,2) become a standalone package. Six boundary categories integrate the actual fluxes at both RK stages with identical weights. CFL.4, at most20000steps per grid. Every predictor/update checks positive density and pressure. No state floor, repair or hidden retry; invalid stages retain raw arrays/completed history and fail.

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
\Omega=([0,3]\times[0,1])\setminus([0.6,3]\times[0,0.2]),\quad (\rho,u,v,p)_\infty=(1.4,3,0,1)
$$

$$
\sum_{C\subset\Omega}|C|(\bar U_C^{n+1}-\bar U_C^n)=\frac{\Delta t}{2}(B(U^n)+B(U^{(1)})),\quad B=-\sum_{\partial\Omega}|f|\widehat F_n
$$

$$
\epsilon_1(\rho)=\frac{\sum_{C\subset\Omega}|\bar\rho_C-\overline{\rho_{\rm ref}}_C|}{\sum_{C\subset\Omega}|\overline{\rho_{\rm ref}}_C|}
$$

## References and validation

Inputs, acceptance,24 unit checks and numerical source were frozen before the first primary test/PDE execution. Checks cover analytic Mach3 normal-shock Rankine-Hugoniot identities, uniform parallel-channel flow, zero stationary-wall mass/energy flux, step-pressure force orientation, actual four-component budgets and raw failure retention. Newly executed separate C++17 MUSCL/generalized-minmod theta1.5/HLL/Heun references atNy80/160 are conservatively restricted for whole-fluid density/pressure L1 comparison. Ordinary public-ZIP verification reads saved reference data; reference source, contracts and execution records are bundled. The first referenceNy160 exhausted its preregistered120second budget; that actual timeout is preserved. A reference revision removed only unnecessary diagnostic-string allocation and was repinned before first primary execution; physical inputs,arithmetic,CFL and acceptance values did not change. All24 tests, three final-time runs and45 gates passed with-W error. Primary density L1=.14754/.12878/.10265, pressure L1=.19373/.16015/.12242 and last-pair density slope=.327. Reference80/160 increments=.02636/.03063, about.257/.250 of the finest primary differences. Maximum four-component relative boundary-budget residual=2.99e-13; all integrated wall mass/energy fluxes are zero. The three primary grids took about46seconds on the original Mac; revised reference80/160 took about8/65seconds.

## Limits

The reference is separately implemented but shares the HLL family and Heun; no external AMROC,LAVA or RKDG engine was executed. Finite-grid numerical data are neither an exact2D solution nor an error bound. Without special corner treatment, a numerical entropy layer may be advected downstream; no agreement with corrected originalPPM fine structures is claimed. Whole-fluid differences,Linf and fixed corner density/pressure/entropy diagnostics are retained. Slopes do not prove pure spatial order; thin slip lines,roll-up,general geometries and high-order convergence remain unverified. Normalized maximum density differences=.592/.670/.665 do not decrease. Corner minima of log(p/rho^gamma)=-.0784/-.1224/-.3510 change substantially. This absolute entropy variable includes an arbitrary additive constant; a more-negative value is not itself an error increase. Neither stable corner extrema nor pointwise pattern convergence is established.

## Stored measurements and decisions

```json
{
  "metrics": {
    "n": 80,
    "ny": 80,
    "nx": 240,
    "time": 4.0,
    "steps": 5557,
    "fluid_cells": 16128,
    "fluid_area": 2.52,
    "density_l1": 0.10265130952593862,
    "pressure_l1": 0.12242245655875464,
    "density_l2": 0.17407969884723082,
    "density_linf": 0.6649309657923782,
    "minimum_density_all_stages": 0.572306931838617,
    "minimum_pressure_all_stages": 0.7623628074232572,
    "density_min": 0.6990444287976558,
    "density_max": 6.591899988897764,
    "pressure_min": 0.8066533197248239,
    "pressure_max": 12.16201901303801,
    "state_floor_count": 0,
    "rejected_steps": 0,
    "wall_mass_energy_max_abs": 0.0,
    "corner_density_l1": 0.03512271217575579,
    "corner_density_max": 5.840654003919099,
    "corner_pressure_max": 11.902361154385352,
    "corner_entropy_min": -0.35096779612542683,
    "corner_entropy_max": 0.3051128979484177
  },
  "checks": {
    "three final-time refinements complete": true,
    "ny20: requested time reached": true,
    "ny20: minimum_density_all_stages": true,
    "ny20: minimum_pressure_all_stages": true,
    "ny20: state_floor_count": true,
    "ny20: rejected_steps": true,
    "ny20: exact aligned fluid area": true,
    "ny20: mass including step-wall boundary balance": true,
    "ny20: x momentum including step-wall boundary balance": true,
    "ny20: y momentum including step-wall boundary balance": true,
    "ny20: energy including step-wall boundary balance": true,
    "ny20: stationary-wall integrated mass/energy flux": true,
    "ny20: unmasked full-field/corner diagnostics retained": true,
    "ny40: requested time reached": true,
    "ny40: minimum_density_all_stages": true,
    "ny40: minimum_pressure_all_stages": true,
    "ny40: state_floor_count": true,
    "ny40: rejected_steps": true,
    "ny40: exact aligned fluid area": true,
    "ny40: mass including step-wall boundary balance": true,
    "ny40: x momentum including step-wall boundary balance": true,
    "ny40: y momentum including step-wall boundary balance": true,
    "ny40: energy including step-wall boundary balance": true,
    "ny40: stationary-wall integrated mass/energy flux": true,
    "ny40: unmasked full-field/corner diagnostics retained": true,
    "ny80: requested time reached": true,
    "ny80: minimum_density_all_stages": true,
    "ny80: minimum_pressure_all_stages": true,
    "ny80: state_floor_count": true,
    "ny80: rejected_steps": true,
    "ny80: exact aligned fluid area": true,
    "ny80: mass including step-wall boundary balance": true,
    "ny80: x momentum including step-wall boundary balance": true,
    "ny80: y momentum including step-wall boundary balance": true,
    "ny80: energy including step-wall boundary balance": true,
    "ny80: stationary-wall integrated mass/energy flux": true,
    "ny80: unmasked full-field/corner diagnostics retained": true,
    "finest density_l1": true,
    "finest pressure_l1": true,
    "density difference decreases across the fixed grids": true,
    "last-pair density difference slope": true,
    "reference increment density_l1": true,
    "reference increment / primary finest density_l1": true,
    "reference increment pressure_l1": true,
    "reference increment / primary finest pressure_l1": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/atlas-forward-step-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Paul Woodward and Phillip Colella (1984). The numerical simulation of two-dimensional fluid flow with strong shocks. https://www.sciencedirect.com/science/article/pii/0021999184901426; review_level=previously-reviewed-publisher-metadata; setup cross-checked against Cockburn-Shu1991 primary report
Cited as the original standard strong-shock comparison. The publisher page rejected retrieval in this task; no direct full-paper reading is claimed. Setup and the distinction between corner treatments were checked in the primary Cockburn–Shu(1991) report.

- Bernardo Cockburn and Chi-Wang Shu (1991). The P¹-RKDG Method for Two-Dimensional Euler Equations of Gas Dynamics. https://ntrs.nasa.gov/citations/19910015505; review_level=selected-text-review: Example2 printedp7/PDFpage11 and Fig3 captions printedp8/PDFpage12
Reviewed Example2 setup, Mach3 uniform flow, inlet/outlet/reflection boundaries, T4 and the Fig3 distinction between untreated and specially treated corners. Selected text only; no figure redistribution or RKDG execution.

- Ralf Deiterding / AMROC project (2004). 2D Euler equations — Forward facing step. https://amroc.sourceforge.net/examples/euler/2d/html/ffstep_n.htm; review_level=official-example-selected-problem-description
Checked the official example description explicitly omitting special corner entropy corrections and using T4. No AMROC calculation, AMR or figure is imported.

- Hiroshi Koyama (2026). Independent C++17 MUSCL finite-volume reference for the uncorrected Mach-3 forward-facing step. https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/references/reference.cpp; review_level=source-and-preregistered-new-execution
Separate implementation without primary spatial-operator imports. HLL and Heun families are shared; no external engine execution. The original timeout and diagnostic-argument-only performance revision are retained alongside saved data,inputs,execution history and contracts.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
