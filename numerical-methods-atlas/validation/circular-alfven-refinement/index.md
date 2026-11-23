# 円偏波Alfvén波：全成分の格子収束

全8保存変数を進め、非零のBz・vzを含む円偏波を解析セル平均と比較します。

**使用手法**

- [HLLDのMHDリーマン解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=ja) (`hlld`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja#circular-alfven-refinement-ja-algorithm)

全8変数HLLD流束、MC-MUSCL再構成、固定刻みHeun。Bx一定の1次元有限体積更新。

$$
\partial_tU+\partial_xF_x(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B),\quad\gamma=5/3
$$

$$
\theta_i=2\pi(x_i-t),\quad(\bar B_y,\bar B_z)=.1\frac{\sin(\pi h)}{\pi h}(\cos\theta_i,\sin\theta_i)
$$

$$
\bar\rho=1,\quad\bar B_x=1,\quad(\bar m_y,\bar m_z)=-(\bar B_y,\bar B_z),\quad\bar E=.66
$$

$$
e_2=\frac{\|U-U^{\mathrm{exact}}\|_2}{\|U^{\mathrm{exact}}\|_2},\qquad p_{\mathrm{obs}}=\log_2(e_h/e_{h/2})
$$

- [理想MHD](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#mhd-ja) (`mhd`)

γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。


**問題の図**

![円偏波Alfvén波：全成分の格子収束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/circular-alfven-refinement.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[円偏波Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja) (`circular-alfven`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja#circular-alfven-refinement-ja-validation)

実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。解析保存平均を独立Gauss16求積と照合し、横成分誤差・位相・観測次数を検査します。

- [円偏波Alfvén波：全保存変数の解析セル平均](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-circular-alfven-refinement-ja) (`circular-alfven-refinement`; 関連モデルの参照 · 解析参照)

γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。
## 前提・単位・境界

γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。

**編集上の補足**

少数の固定入力に対する教育用検証です。HLLDのHLLE代替と再構成の正値性スケーリングを数え、セル状態の床・クリップ・再試行は行いません。有限格子参照は厳密解ではなく、任意問題の安定性・正値性や普遍的次数を保証しません。1次元整列波の次数であり、斜め2次元伝播の検証ではありません。

## 採用した計算法

全8変数HLLD流束、MC-MUSCL再構成、固定刻みHeun。Bx一定の1次元有限体積更新。

$$
\partial_tU+\partial_xF_x(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B),\quad\gamma=5/3
$$

$$
\theta_i=2\pi(x_i-t),\quad(\bar B_y,\bar B_z)=.1\frac{\sin(\pi h)}{\pi h}(\cos\theta_i,\sin\theta_i)
$$

$$
\bar\rho=1,\quad\bar B_x=1,\quad(\bar m_y,\bar m_z)=-(\bar B_y,\bar B_z),\quad\bar E=.66
$$

$$
e_2=\frac{\|U-U^{\mathrm{exact}}\|_2}{\|U^{\mathrm{exact}}\|_2},\qquad p_{\mathrm{obs}}=\log_2(e_h/e_{h/2})
$$

## 比較・検証

実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。解析保存平均を独立Gauss16求積と照合し、横成分誤差・位相・観測次数を検査します。

## 確認の限界

少数の固定入力に対する教育用検証です。HLLDのHLLE代替と再構成の正値性スケーリングを数え、セル状態の床・クリップ・再試行は行いません。有限格子参照は厳密解ではなく、任意問題の安定性・正値性や普遍的次数を保証しません。1次元整列波の次数であり、斜め2次元伝播の検証ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "completed_pde_runs": 4,
    "reference_qualification_passed": true,
    "analytic_quadrature_difference": 3.3306690738754696e-16
  },
  "checks": {
    "four prescribed fixed runs": true,
    "qualified independent reference": true,
    "independent analytic conserved quadrature": true,
    "circular-alfven-refinement-n32 all stages finite positive": true,
    "circular-alfven-refinement-n32 final time": true,
    "circular-alfven-refinement-n32 five exact snapshots": true,
    "circular-alfven-refinement-n32 fluid integral conservation": true,
    "circular-alfven-refinement-n32 native face divergence": true,
    "circular-alfven-refinement-n32 measured Courant sum": true,
    "circular-alfven-refinement-n32 no cell clips or retries": true,
    "circular-alfven-refinement-n32 explicit fallback accounting": true,
    "circular-alfven-refinement-n64 all stages finite positive": true,
    "circular-alfven-refinement-n64 final time": true,
    "circular-alfven-refinement-n64 five exact snapshots": true,
    "circular-alfven-refinement-n64 fluid integral conservation": true,
    "circular-alfven-refinement-n64 native face divergence": true,
    "circular-alfven-refinement-n64 measured Courant sum": true,
    "circular-alfven-refinement-n64 no cell clips or retries": true,
    "circular-alfven-refinement-n64 explicit fallback accounting": true,
    "circular-alfven-refinement-n128 all stages finite positive": true,
    "circular-alfven-refinement-n128 final time": true,
    "circular-alfven-refinement-n128 five exact snapshots": true,
    "circular-alfven-refinement-n128 fluid integral conservation": true,
    "circular-alfven-refinement-n128 native face divergence": true,
    "circular-alfven-refinement-n128 measured Courant sum": true,
    "circular-alfven-refinement-n128 no cell clips or retries": true,
    "circular-alfven-refinement-n128 explicit fallback accounting": true,
    "circular-alfven-refinement-half-dt all stages finite positive": true,
    "circular-alfven-refinement-half-dt final time": true,
    "circular-alfven-refinement-half-dt five exact snapshots": true,
    "circular-alfven-refinement-half-dt fluid integral conservation": true,
    "circular-alfven-refinement-half-dt native face divergence": true,
    "circular-alfven-refinement-half-dt measured Courant sum": true,
    "circular-alfven-refinement-half-dt no cell clips or retries": true,
    "circular-alfven-refinement-half-dt explicit fallback accounting": true,
    "transverse refinement n64": true,
    "transverse refinement n128": true,
    "transverse finest error": true,
    "transverse separate time contamination fraction": true,
    "selected wave last observed order": true,
    "selected wave phase error": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/index.json

![保存した主計算の実際のBy(x,t)の5時刻場。1次元空間と時間を表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/circular-alfven-refinement-preview.png)

保存した主計算の実際のBy(x,t)の5時刻場。1次元空間と時間を表示。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Athena++ collaboration (2026). Athena++ official field_loop and orszag_tang problem generators, pinned source. https://github.com/PrincetonUniversity/athena/tree/1395e2f543f4368d448cb1a2cf92ba1f910e3416; review_level=Official archive SHA verified; selected src/pgen/field_loop.cpp and orszag_tang.cpp, PLM/RK2/output configuration and actual conserved tab headers inspected; not a full Athena code audit
固定コミットの公式アーカイブSHAを照合し、2初期値生成器と設定・保存列を確認。別実装を実行して参照場を作成し、空間・時間感度を検査。全ソース監査や厳密解とは表示しません。

- Thomas A. Gardiner and James M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport. https://arxiv.org/abs/astro-ph/0501557; review_level=Author arXiv PDF selected section2.2 equations13–20,3.3.1–3.3.2 and5.1–5.2 inspected; not the full paper or original experiment replication
著者公開PDFのCT節・磁場ループ・円偏波の定義を確認。論文のCTU/PPMや斜め伝播実験を再現したとは主張しません。今回の円偏波は1次元整列、公式磁場ループはvz=2の明示的変更です。

- Takahiro Miyoshi and Kanya Kusano (2005). A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics. https://doi.org/10.1016/j.jcp.2005.02.017; review_level=Bibliographic metadata checked; publisher full text returned403. This addition did not newly audit original equations or experiments
書誌を確認。出版社本文は取得できず、今回新たに原著の式や実験を監査したとは表示しません。全8変数HLLDコードは過去の公開検証済みAtlasから同一バイトで継承します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Circular Alfven wave: full-state refinement

Evolve all eight conserved variables and compare circular polarization, including nonzero Bz/vz, against analytic cell means.

**Methods used**

- [HLLD MHD Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en) (`hlld`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en#circular-alfven-refinement-en-algorithm)

Full-eight-state HLLD fluxes, MC-MUSCL reconstruction and fixed-step Heun. One-dimensional finite-volume update with constant Bx.

$$
\partial_tU+\partial_xF_x(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B),\quad\gamma=5/3
$$

$$
\theta_i=2\pi(x_i-t),\quad(\bar B_y,\bar B_z)=.1\frac{\sin(\pi h)}{\pi h}(\cos\theta_i,\sin\theta_i)
$$

$$
\bar\rho=1,\quad\bar B_x=1,\quad(\bar m_y,\bar m_z)=-(\bar B_y,\bar B_z),\quad\bar E=.66
$$

$$
e_2=\frac{\|U-U^{\mathrm{exact}}\|_2}{\|U^{\mathrm{exact}}\|_2},\qquad p_{\mathrm{obs}}=\log_2(e_h/e_{h/2})
$$

- [Ideal magnetohydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en) (`mhd`)

gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure.


**Problem figure**

![Circular Alfven wave: full-state refinement: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/circular-alfven-refinement.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en) (`circular-alfven`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en#circular-alfven-refinement-en-validation)

Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify conserved analytic means by independent Gauss16 quadrature; measure transverse errors, phase and observed order.

- [Circular Alfven wave: analytic full-state conserved cell means](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-circular-alfven-refinement-en) (`circular-alfven-refinement`; Related-model reference · Analytic reference)

gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure.
## Assumptions, units and boundaries

gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure.

**Editorial clarification**

Educational fixed inputs only. Count HLLD-to-HLLE fallbacks and face reconstruction positivity scaling; no cell floor/clipping/retry. Finite-grid references are not exact solutions; no universal stability, positivity or order guarantee. The observed order is for a 1D aligned wave, not oblique 2D propagation.

## Adopted numerical method

Full-eight-state HLLD fluxes, MC-MUSCL reconstruction and fixed-step Heun. One-dimensional finite-volume update with constant Bx.

$$
\partial_tU+\partial_xF_x(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B),\quad\gamma=5/3
$$

$$
\theta_i=2\pi(x_i-t),\quad(\bar B_y,\bar B_z)=.1\frac{\sin(\pi h)}{\pi h}(\cos\theta_i,\sin\theta_i)
$$

$$
\bar\rho=1,\quad\bar B_x=1,\quad(\bar m_y,\bar m_z)=-(\bar B_y,\bar B_z),\quad\bar E=.66
$$

$$
e_2=\frac{\|U-U^{\mathrm{exact}}\|_2}{\|U^{\mathrm{exact}}\|_2},\qquad p_{\mathrm{obs}}=\log_2(e_h/e_{h/2})
$$

## References and validation

Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify conserved analytic means by independent Gauss16 quadrature; measure transverse errors, phase and observed order.

## Limits

Educational fixed inputs only. Count HLLD-to-HLLE fallbacks and face reconstruction positivity scaling; no cell floor/clipping/retry. Finite-grid references are not exact solutions; no universal stability, positivity or order guarantee. The observed order is for a 1D aligned wave, not oblique 2D propagation.

## Stored measurements and decisions

```json
{
  "metrics": {
    "completed_pde_runs": 4,
    "reference_qualification_passed": true,
    "analytic_quadrature_difference": 3.3306690738754696e-16
  },
  "checks": {
    "four prescribed fixed runs": true,
    "qualified independent reference": true,
    "independent analytic conserved quadrature": true,
    "circular-alfven-refinement-n32 all stages finite positive": true,
    "circular-alfven-refinement-n32 final time": true,
    "circular-alfven-refinement-n32 five exact snapshots": true,
    "circular-alfven-refinement-n32 fluid integral conservation": true,
    "circular-alfven-refinement-n32 native face divergence": true,
    "circular-alfven-refinement-n32 measured Courant sum": true,
    "circular-alfven-refinement-n32 no cell clips or retries": true,
    "circular-alfven-refinement-n32 explicit fallback accounting": true,
    "circular-alfven-refinement-n64 all stages finite positive": true,
    "circular-alfven-refinement-n64 final time": true,
    "circular-alfven-refinement-n64 five exact snapshots": true,
    "circular-alfven-refinement-n64 fluid integral conservation": true,
    "circular-alfven-refinement-n64 native face divergence": true,
    "circular-alfven-refinement-n64 measured Courant sum": true,
    "circular-alfven-refinement-n64 no cell clips or retries": true,
    "circular-alfven-refinement-n64 explicit fallback accounting": true,
    "circular-alfven-refinement-n128 all stages finite positive": true,
    "circular-alfven-refinement-n128 final time": true,
    "circular-alfven-refinement-n128 five exact snapshots": true,
    "circular-alfven-refinement-n128 fluid integral conservation": true,
    "circular-alfven-refinement-n128 native face divergence": true,
    "circular-alfven-refinement-n128 measured Courant sum": true,
    "circular-alfven-refinement-n128 no cell clips or retries": true,
    "circular-alfven-refinement-n128 explicit fallback accounting": true,
    "circular-alfven-refinement-half-dt all stages finite positive": true,
    "circular-alfven-refinement-half-dt final time": true,
    "circular-alfven-refinement-half-dt five exact snapshots": true,
    "circular-alfven-refinement-half-dt fluid integral conservation": true,
    "circular-alfven-refinement-half-dt native face divergence": true,
    "circular-alfven-refinement-half-dt measured Courant sum": true,
    "circular-alfven-refinement-half-dt no cell clips or retries": true,
    "circular-alfven-refinement-half-dt explicit fallback accounting": true,
    "transverse refinement n64": true,
    "transverse refinement n128": true,
    "transverse finest error": true,
    "transverse separate time contamination fraction": true,
    "selected wave last observed order": true,
    "selected wave phase error": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/index.json

![Actual saved primary By(x,t) at five times: one spatial dimension plus time.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/circular-alfven-refinement-preview.png)

Actual saved primary By(x,t) at five times: one spatial dimension plus time.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Athena++ collaboration (2026). Athena++ official field_loop and orszag_tang problem generators, pinned source. https://github.com/PrincetonUniversity/athena/tree/1395e2f543f4368d448cb1a2cf92ba1f910e3416; review_level=Official archive SHA verified; selected src/pgen/field_loop.cpp and orszag_tang.cpp, PLM/RK2/output configuration and actual conserved tab headers inspected; not a full Athena code audit
Verified the official pinned archive SHA and inspected both generators, configuration and saved columns. Executed the independent engine and checked spatial/time sensitivity. No complete code audit or exact-solution claim.

- Thomas A. Gardiner and James M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport. https://arxiv.org/abs/astro-ph/0501557; review_level=Author arXiv PDF selected section2.2 equations13–20,3.3.1–3.3.2 and5.1–5.2 inspected; not the full paper or original experiment replication
Inspected the author PDF CT section and loop/polarized-wave definitions. Original CTU/PPM and oblique-wave experiments are not replicated. Our wave is 1D aligned; the official loop generator explicitly has vz=2.

- Takahiro Miyoshi and Kanya Kusano (2005). A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics. https://doi.org/10.1016/j.jcp.2005.02.017; review_level=Bibliographic metadata checked; publisher full text returned403. This addition did not newly audit original equations or experiments
Bibliographic metadata checked; full publisher text unavailable. No new original-equation/experiment audit is claimed. Full-state HLLD is inherited byte-for-byte from the prior public validated Atlas.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
