# FR法の1D周期移流：Radau補正と既存DGの比較

0.4+sin(2πx)をT=.25まで移流。Gauss点・Radau補正のFRと既存のmodal DGをp=1/2、8/16/32セルで実行し、誤差・質量・時間積分誤差を測ります。

**使用手法**

- [Flux Reconstruction法（FR法）](https://hrkoyama.github.io/numerical-methods-atlas/methods/flux-reconstruction/?lang=ja) (`flux-reconstruction`)
- [不連続Galerkin法／Legendre](https://hrkoyama.github.io/numerical-methods-atlas/methods/dg/?lang=ja) (`dg`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja#fr-periodic-advection-ja-algorithm)

p+1個のGauss解点、上流数値流束、Legendre多項式によるRadau左右補正、SSPRK(3,3)。初期L2射影・上流流束・時間刻み規約をバイト一致の既存modal DGと揃えます。スケールしたCourant数(2p+1)|a|Δt/h≤.15。最後にp2/N32で刻みを半減。

$$
u_t+a u_x=0,\quad u_*(x,t)=0.4+\sin(2\pi(x-at)),\quad a=1
$$

$$
f^C=f^D+(f_L^*-f_L^D)g_L+(f_R^*-f_R^D)g_R,\quad \dot u=-\frac{2}{h}\partial_\xi f^C
$$

$$
g_L=\frac{(-1)^p}{2}(P_p-P_{p+1}),\quad g_R=\frac12(P_p+P_{p+1}),\quad\frac{d}{dt}\frac12\|u_h\|^2=-\frac{|a|}{2}\sum_{\rm faces}[u_h]^2
$$

- [線形移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja) (`linear-advection`)

全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。


**問題の図**

![FR法の1D周期移流：Radau補正と既存DGの比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/fr-periodic-advection.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) (`advection-sine`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja#fr-periodic-advection-ja-validation)

追加のGauss点で連続L2誤差を積分し、既存DGの最終多項式と共通点で照合。全RK段階の重み付き質量と各完了ステップの2次エネルギーを検査。同じFR空間演算子の行列指数解で時間誤差を別測定し、刻み半減を確認。

- [移流／正弦波の平行移動](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja) (`sine-advection`; 関連モデルの参照 · 解析参照)

同じ周期・速度1の正弦移流モデルです。参照一覧は振幅0.25、共通固定入力は0.2で、DG・CIP等の表現や時間も異なります。

- [WENO臨界点：多項式セル平均と解析的周期輸送](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-weno-critical-profile-ja) (`weno-critical-profile`; 関連モデルの参照 · 解析参照)

同じ一定速度の周期移流に対する追加参照ですが、cos+.1sin³のセル平均と局所臨界多項式は、従来の単一正弦・CIP表示と異なります。

- [FRとDGの周期正弦移流：平均0.4・T=.25の解析参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fr-periodic-advection-ja) (`fr-periodic-advection`; 同じ問題の参照 · 解析参照)

全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。
## 前提・単位・境界

全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。

## 採用した計算法

p+1個のGauss解点、上流数値流束、Legendre多項式によるRadau左右補正、SSPRK(3,3)。初期L2射影・上流流束・時間刻み規約をバイト一致の既存modal DGと揃えます。スケールしたCourant数(2p+1)|a|Δt/h≤.15。最後にp2/N32で刻みを半減。

$$
u_t+a u_x=0,\quad u_*(x,t)=0.4+\sin(2\pi(x-at)),\quad a=1
$$

$$
f^C=f^D+(f_L^*-f_L^D)g_L+(f_R^*-f_R^D)g_R,\quad \dot u=-\frac{2}{h}\partial_\xi f^C
$$

$$
g_L=\frac{(-1)^p}{2}(P_p-P_{p+1}),\quad g_R=\frac12(P_p+P_{p+1}),\quad\frac{d}{dt}\frac12\|u_h\|^2=-\frac{|a|}{2}\sum_{\rm faces}[u_h]^2
$$

## 比較・検証

追加のGauss点で連続L2誤差を積分し、既存DGの最終多項式と共通点で照合。全RK段階の重み付き質量と各完了ステップの2次エネルギーを検査。同じFR空間演算子の行列指数解で時間誤差を別測定し、刻み半減を確認。

## 確認の限界

このRadau/Gauss・線形一定流束・アフィン要素の設定がDGに対応します。全FRと全DGの同値性、非線形流束・衝撃波・制限器・多次元FRは保証しません。hとΔtの同時細分化と行列指数による空間誤差を分け、行列指数を独立した空間PDEソルバーとは呼びません。PyFR本体は未実行。

## 保存実測値と判定

```json
{
  "metrics": {
    "p1_l2_order": 1.9917679206568963,
    "p1_exponential_l2_order": 1.991760641915898,
    "p2_l2_order": 2.999596193727679,
    "p2_exponential_l2_order": 2.9995943579113864,
    "finest_l2_error": 2.6116268430230035e-05,
    "maximum_fr_vs_published_dg": 3.9968028886505635e-15,
    "maximum_stage_mass_drift": 3.552713678800501e-15,
    "maximum_step_energy_increase": 0.0,
    "maximum_scaled_courant": 0.15,
    "finest_rk3_time_error": 9.442398008716171e-09,
    "halved_cfl_time_error": 1.1816779053955014e-09,
    "time_error_halving_ratio": 0.12514595384612126,
    "actual_transport_l2_change": 0.9999999629484513
  },
  "checks": {
    "p1_l2_convergence": true,
    "p2_l2_convergence": true,
    "semidiscrete_spatial_convergence": true,
    "finest_analytic_error": true,
    "published_dg_agreement": true,
    "periodic_stage_mass": true,
    "nonincreasing_step_energy": true,
    "scaled_courant_bound": true,
    "time_error_control": true,
    "nontrivial_translation": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/index.json

![保存したFRの初期・最終場と解析解との差。T=.25の実際の移流を表示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/fr-periodic-advection-preview.png)

保存したFRの初期・最終場と解析解との差。T=.25の実際の移流を表示します。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs-initial.json

## 出典と確認範囲

- H. T. Huynh (2007). A Flux Reconstruction Approach to High-Order Schemes Including Discontinuous Galerkin Methods. https://ntrs.nasa.gov/api/citations/20140009969/downloads/20140009969.pdf; review_level=metadata
著者の2014年NASA報告の参考文献（本文27頁）で2007年原報の題名・著者・会議番号を確認。AIAA原文は未取得。補正式は別記の2014年本文を参照。

- H. T. Huynh (2014). On Formulations of Discontinuous Galerkin and Related Methods for Conservation Laws. https://ntrs.nasa.gov/api/citations/20140009969/downloads/20140009969.pdf; review_level=full-text
NASA原文の抄録、微分形と界面補正、本文19–21頁の式(6.2)–(6.13)のRadau補正とDG対応、27頁の書誌を確認。全報告の監査や非線形実験の再現ではない。

- PyFR development team (2026). PyFR: Flux Reconstruction and supported implementation platforms (accessed 2026-11-23). https://www.pyfr.org/; review_level=full-text
公式サイトのFRによる空間離散化・非構造格子・CPU/GPUの紹介を確認。今回の軽量Python例でPyFRを導入・実行・検証したとはしない。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# 1D periodic FR advection: Radau correction and published DG comparison

Transport0.4+sin(2pi x) toT=.25. Execute Gauss-node/Radau FR and the existing modal DG for p=1/2 and8/16/32 cells; measure analytic error, mass and time-integration error.

**Methods used**

- [Flux reconstruction (FR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/flux-reconstruction/?lang=en) (`flux-reconstruction`)
- [Discontinuous Galerkin / Legendre](https://hrkoyama.github.io/numerical-methods-atlas/methods/dg/?lang=en) (`dg`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en#fr-periodic-advection-en-algorithm)

p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.

$$
u_t+a u_x=0,\quad u_*(x,t)=0.4+\sin(2\pi(x-at)),\quad a=1
$$

$$
f^C=f^D+(f_L^*-f_L^D)g_L+(f_R^*-f_R^D)g_R,\quad \dot u=-\frac{2}{h}\partial_\xi f^C
$$

$$
g_L=\frac{(-1)^p}{2}(P_p-P_{p+1}),\quad g_R=\frac12(P_p+P_{p+1}),\quad\frac{d}{dt}\frac12\|u_h\|^2=-\frac{|a|}{2}\sum_{\rm faces}[u_h]^2
$$

- [Linear advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en) (`linear-advection`)

Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.


**Problem figure**

![1D periodic FR advection: Radau correction and published DG comparison: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/fr-periodic-advection.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) (`advection-sine`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en#fr-periodic-advection-en-validation)

Integrate continuous L2 error at additional Gauss points and compare final polynomials with the actual published DG at common points. Check weighted mass at every RK stage and quadratic energy at each completed step. A matrix exponential of the same FR operator separately measures RK3 time error and its timestep-halving response.

- [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en) (`sine-advection`; Related-model reference · Analytic reference)

Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.

- [WENO critical points: polynomial cell means and analytic periodic transport](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en) (`weno-critical-profile`; Related-model reference · Analytic reference)

An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.

- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en) (`fr-periodic-advection`; Same-problem reference · Analytic reference)

Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.
## Assumptions, units and boundaries

Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.

## Adopted numerical method

p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.

$$
u_t+a u_x=0,\quad u_*(x,t)=0.4+\sin(2\pi(x-at)),\quad a=1
$$

$$
f^C=f^D+(f_L^*-f_L^D)g_L+(f_R^*-f_R^D)g_R,\quad \dot u=-\frac{2}{h}\partial_\xi f^C
$$

$$
g_L=\frac{(-1)^p}{2}(P_p-P_{p+1}),\quad g_R=\frac12(P_p+P_{p+1}),\quad\frac{d}{dt}\frac12\|u_h\|^2=-\frac{|a|}{2}\sum_{\rm faces}[u_h]^2
$$

## References and validation

Integrate continuous L2 error at additional Gauss points and compare final polynomials with the actual published DG at common points. Check weighted mass at every RK stage and quadratic energy at each completed step. A matrix exponential of the same FR operator separately measures RK3 time error and its timestep-halving response.

## Limits

DG correspondence is for these Radau/Gauss choices, a constant linear flux and affine elements. No all-FR/all-DG equivalence, nonlinear flux, shock, limiter or multidimensional FR claim. Distinguish coupled h/dt refinement from the exponential spatial result; the exponential is not an independent spatial PDE solver. PyFR itself is not run.

## Stored measurements and decisions

```json
{
  "metrics": {
    "p1_l2_order": 1.9917679206568963,
    "p1_exponential_l2_order": 1.991760641915898,
    "p2_l2_order": 2.999596193727679,
    "p2_exponential_l2_order": 2.9995943579113864,
    "finest_l2_error": 2.6116268430230035e-05,
    "maximum_fr_vs_published_dg": 3.9968028886505635e-15,
    "maximum_stage_mass_drift": 3.552713678800501e-15,
    "maximum_step_energy_increase": 0.0,
    "maximum_scaled_courant": 0.15,
    "finest_rk3_time_error": 9.442398008716171e-09,
    "halved_cfl_time_error": 1.1816779053955014e-09,
    "time_error_halving_ratio": 0.12514595384612126,
    "actual_transport_l2_change": 0.9999999629484513
  },
  "checks": {
    "p1_l2_convergence": true,
    "p2_l2_convergence": true,
    "semidiscrete_spatial_convergence": true,
    "finest_analytic_error": true,
    "published_dg_agreement": true,
    "periodic_stage_mass": true,
    "nonincreasing_step_energy": true,
    "scaled_courant_bound": true,
    "time_error_control": true,
    "nontrivial_translation": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/index.json

![Saved FR initial/final field and analytic nodal error; actual transport atT=.25.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/fr-periodic-advection-preview.png)

Saved FR initial/final field and analytic nodal error; actual transport atT=.25.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs-initial.json

## Sources and review scope

- H. T. Huynh (2007). A Flux Reconstruction Approach to High-Order Schemes Including Discontinuous Galerkin Methods. https://ntrs.nasa.gov/api/citations/20140009969/downloads/20140009969.pdf; review_level=metadata
Original 2007 title/author/AIAA number checked in the author's 2014 NASA report, printed p.27. The original AIAA text was not retrieved; correction formulas use the separately cited 2014 report.

- H. T. Huynh (2014). On Formulations of Discontinuous Galerkin and Related Methods for Conservation Laws. https://ntrs.nasa.gov/api/citations/20140009969/downloads/20140009969.pdf; review_level=full-text
Selected original NASA passages: abstract, differential form/interface correction, printed pp.19–21 equations(6.2)–(6.13) for Radau/DG, and p.27 bibliography. No full-report audit or nonlinear experiment reproduction.

- PyFR development team (2026). PyFR: Flux Reconstruction and supported implementation platforms (accessed 2026-11-23). https://www.pyfr.org/; review_level=full-text
Official overview: FR spatial discretization, unstructured meshes and CPU/GPU platforms. PyFR is not installed, invoked or validated by this small Python example.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
