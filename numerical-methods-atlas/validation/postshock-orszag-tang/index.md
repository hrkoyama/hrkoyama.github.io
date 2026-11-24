# 後期Orszag–Tang：独立参照と圧縮構造

圧縮性理想MHDのOrszag–TangをT=.2まで進め、相互作用する圧縮・衝撃波構造の密度と圧力を独立有限格子参照で検査します。

**使用手法**

- [HLLDのMHDリーマン解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=ja) (`hlld`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)
- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) (`ct`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja#postshock-orszag-tang-ja-algorithm)

全8変数HLLD流束、MC-MUSCL再構成、固定刻みHeun。共有面流束とCT-contact角電場から面磁場を更新し、セル磁場は隣接面平均。初期状態は公式生成器の離散ベクトルポテンシャルと中心流体値に一致させます。

$$
\partial_tU+\partial_xF_x(U)+\partial_yF_y(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B)
$$

$$
E=\frac{p}{\gamma-1}+\frac12\rho|\mathbf v|^2+\frac12|\mathbf B|^2,\quad\gamma=5/3
$$

$$
\frac{dB_x}{dt}=-D_y\mathcal E_z,\quad\frac{dB_y}{dt}=D_x\mathcal E_z,\quad D_xB_x+D_yB_y=\mathrm{constant}
$$

$$
\bar U_i^{\mathrm{ref}}=\frac1{N_i}\sum_{j\in i}\bar U_j^{\mathrm{fine}},\qquad e_1=\frac{\sum|U-U^{\mathrm{ref}}|}{\sum|U^{\mathrm{ref}}|}
$$

$$
\rho_0=\frac{25}{36\pi},\quad p_0=\frac5{12\pi},\quad\mathbf v_0=(\sin2\pi y,-\sin2\pi x,0)
$$

- [理想MHD](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#mhd-ja) (`mhd`)

γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。


**問題の図**

![後期Orszag–Tang：独立参照と圧縮構造：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/results/postshock-orszag-tang.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja) (`orszag-tang`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja#postshock-orszag-tang-ja-validation)

実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。Athena++の2格子と刻み半減で参照を検定。終端保存変数を保守的に粗視化し、誤差と参照感度を分離します。共通セル発散と主計算の固有面発散は別の検査です。

- [後期Orszag–Tang：独立有限格子の密度・圧力参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-postshock-orszag-tang-ja) (`postshock-orszag-tang`; 関連モデルの参照 · 有限格子の数値参照)

γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。
## 前提・単位・境界

γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。

**編集上の補足**

少数の固定入力に対する教育用検証です。HLLDのHLLE代替と再構成の正値性スケーリングを数え、セル状態の床・クリップ・再試行は行いません。有限格子参照は厳密解ではなく、任意問題の安定性・正値性や普遍的次数を保証しません。独立比較は終端のみ。中間Athena時刻は指定四半時刻直後で、正確に整列した場とは表示しません。Athenaの固有面発散は出力しておらず測定を主張しません。密度比は圧縮の診断であり数学的衝撃波の証明ではありません。

## 採用した計算法

全8変数HLLD流束、MC-MUSCL再構成、固定刻みHeun。共有面流束とCT-contact角電場から面磁場を更新し、セル磁場は隣接面平均。初期状態は公式生成器の離散ベクトルポテンシャルと中心流体値に一致させます。

$$
\partial_tU+\partial_xF_x(U)+\partial_yF_y(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B)
$$

$$
E=\frac{p}{\gamma-1}+\frac12\rho|\mathbf v|^2+\frac12|\mathbf B|^2,\quad\gamma=5/3
$$

$$
\frac{dB_x}{dt}=-D_y\mathcal E_z,\quad\frac{dB_y}{dt}=D_x\mathcal E_z,\quad D_xB_x+D_yB_y=\mathrm{constant}
$$

$$
\bar U_i^{\mathrm{ref}}=\frac1{N_i}\sum_{j\in i}\bar U_j^{\mathrm{fine}},\qquad e_1=\frac{\sum|U-U^{\mathrm{ref}}|}{\sum|U^{\mathrm{ref}}|}
$$

$$
\rho_0=\frac{25}{36\pi},\quad p_0=\frac5{12\pi},\quad\mathbf v_0=(\sin2\pi y,-\sin2\pi x,0)
$$

## 比較・検証

実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。Athena++の2格子と刻み半減で参照を検定。終端保存変数を保守的に粗視化し、誤差と参照感度を分離します。共通セル発散と主計算の固有面発散は別の検査です。

## 確認の限界

少数の固定入力に対する教育用検証です。HLLDのHLLE代替と再構成の正値性スケーリングを数え、セル状態の床・クリップ・再試行は行いません。有限格子参照は厳密解ではなく、任意問題の安定性・正値性や普遍的次数を保証しません。独立比較は終端のみ。中間Athena時刻は指定四半時刻直後で、正確に整列した場とは表示しません。Athenaの固有面発散は出力しておらず測定を主張しません。密度比は圧縮の診断であり数学的衝撃波の証明ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "completed_pde_runs": 4,
    "reference_qualification_passed": true,
    "analytic_quadrature_difference": null
  },
  "checks": {
    "four prescribed fixed runs": true,
    "qualified independent reference": true,
    "postshock-orszag-tang-n16 all stages finite positive": true,
    "postshock-orszag-tang-n16 final time": true,
    "postshock-orszag-tang-n16 five exact snapshots": true,
    "postshock-orszag-tang-n16 fluid integral conservation": true,
    "postshock-orszag-tang-n16 native face divergence": true,
    "postshock-orszag-tang-n16 measured Courant sum": true,
    "postshock-orszag-tang-n16 no cell clips or retries": true,
    "postshock-orszag-tang-n16 explicit fallback accounting": true,
    "postshock-orszag-tang-n32 all stages finite positive": true,
    "postshock-orszag-tang-n32 final time": true,
    "postshock-orszag-tang-n32 five exact snapshots": true,
    "postshock-orszag-tang-n32 fluid integral conservation": true,
    "postshock-orszag-tang-n32 native face divergence": true,
    "postshock-orszag-tang-n32 measured Courant sum": true,
    "postshock-orszag-tang-n32 no cell clips or retries": true,
    "postshock-orszag-tang-n32 explicit fallback accounting": true,
    "postshock-orszag-tang-n64 all stages finite positive": true,
    "postshock-orszag-tang-n64 final time": true,
    "postshock-orszag-tang-n64 five exact snapshots": true,
    "postshock-orszag-tang-n64 fluid integral conservation": true,
    "postshock-orszag-tang-n64 native face divergence": true,
    "postshock-orszag-tang-n64 measured Courant sum": true,
    "postshock-orszag-tang-n64 no cell clips or retries": true,
    "postshock-orszag-tang-n64 explicit fallback accounting": true,
    "postshock-orszag-tang-half-dt all stages finite positive": true,
    "postshock-orszag-tang-half-dt final time": true,
    "postshock-orszag-tang-half-dt five exact snapshots": true,
    "postshock-orszag-tang-half-dt fluid integral conservation": true,
    "postshock-orszag-tang-half-dt native face divergence": true,
    "postshock-orszag-tang-half-dt measured Courant sum": true,
    "postshock-orszag-tang-half-dt no cell clips or retries": true,
    "postshock-orszag-tang-half-dt explicit fallback accounting": true,
    "density refinement n32": true,
    "density refinement n64": true,
    "density finest error": true,
    "density separate time contamination fraction": true,
    "density reference increment/error": true,
    "pressure refinement n32": true,
    "pressure refinement n64": true,
    "pressure finest error": true,
    "pressure separate time contamination fraction": true,
    "pressure reference increment/error": true,
    "late density compression diagnostic": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/index.json

![保存した主計算の実際の2次元密度場、T=.2。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/results/postshock-orszag-tang-preview.png)

保存した主計算の実際の2次元密度場、T=.2。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Athena++ collaboration (2026). Athena++ official field_loop and orszag_tang problem generators, pinned source [accessed 2026-11-23]. https://github.com/PrincetonUniversity/athena/tree/1395e2f543f4368d448cb1a2cf92ba1f910e3416; review_level=Official archive SHA verified; selected src/pgen/field_loop.cpp and orszag_tang.cpp, PLM/RK2/output configuration and actual conserved tab headers inspected; not a full Athena code audit
固定コミットの公式アーカイブSHAを照合し、2初期値生成器と設定・保存列を確認。別実装を実行して参照場を作成し、空間・時間感度を検査。全ソース監査や厳密解とは表示しません。

- Thomas A. Gardiner and James M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport [accessed 2026-11-23]. https://arxiv.org/abs/astro-ph/0501557; review_level=Author arXiv PDF selected section2.2 equations13–20,3.3.1–3.3.2 and5.1–5.2 inspected; not the full paper or original experiment replication
著者公開PDFのCT節・磁場ループ・円偏波の定義を確認。論文のCTU/PPMや斜め伝播実験を再現したとは主張しません。今回の円偏波は1次元整列、公式磁場ループはvz=2の明示的変更です。

- Takahiro Miyoshi and Kanya Kusano (2005). A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics [accessed 2026-11-23]. https://doi.org/10.1016/j.jcp.2005.02.017; review_level=Bibliographic metadata checked; publisher full text returned403. This addition did not newly audit original equations or experiments
書誌を確認。出版社本文は取得できず、今回新たに原著の式や実験を監査したとは表示しません。全8変数HLLDコードは過去の公開検証済みAtlasから同一バイトで継承します。

- Steven A. Orszag and Ching-Mao Tang (1979). Small-scale structure of two-dimensional magnetohydrodynamic turbulence [accessed 2026-11-23]. https://doi.org/10.1017/S002211207900210X; review_level=Original publisher abstract/bibliography inspected only; original incompressible viscous/resistive setup differs from the official compressible ideal-MHD generator used here
出版社の抄録と書誌のみ確認。原著の非圧縮・粘性抵抗モデルと、今回の圧縮性理想MHDの公式初期値を区別します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Late Orszag-Tang: independent reference and compression structure

Evolve compressible ideal-MHD Orszag-Tang to T.2 and check density/pressure in interacting compression/shock structure against an independent finite-grid reference.

**Methods used**

- [HLLD MHD Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en) (`hlld`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)
- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) (`ct`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en#postshock-orszag-tang-en-algorithm)

Full-eight-state HLLD fluxes, MC-MUSCL reconstruction and fixed-step Heun. Shared face fluxes and CT-contact corner EMFs update native face B; cell B is adjacent-face averaged. Initial discrete vector-potential curl and sampled fluid states match the official generator.

$$
\partial_tU+\partial_xF_x(U)+\partial_yF_y(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B)
$$

$$
E=\frac{p}{\gamma-1}+\frac12\rho|\mathbf v|^2+\frac12|\mathbf B|^2,\quad\gamma=5/3
$$

$$
\frac{dB_x}{dt}=-D_y\mathcal E_z,\quad\frac{dB_y}{dt}=D_x\mathcal E_z,\quad D_xB_x+D_yB_y=\mathrm{constant}
$$

$$
\bar U_i^{\mathrm{ref}}=\frac1{N_i}\sum_{j\in i}\bar U_j^{\mathrm{fine}},\qquad e_1=\frac{\sum|U-U^{\mathrm{ref}}|}{\sum|U^{\mathrm{ref}}|}
$$

$$
\rho_0=\frac{25}{36\pi},\quad p_0=\frac5{12\pi},\quad\mathbf v_0=(\sin2\pi y,-\sin2\pi x,0)
$$

- [Ideal magnetohydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en) (`mhd`)

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.


**Problem figure**

![Late Orszag-Tang: independent reference and compression structure: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/results/postshock-orszag-tang.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) (`orszag-tang`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en#postshock-orszag-tang-en-validation)

Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify Athena++ with two grids and a half-CFL probe. Conservatively restrict final conserved states and separate reference sensitivity from primary error. Common-cell divergence and primary native-face divergence are distinct checks.

- [Late Orszag-Tang: independent finite-grid density/pressure reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-postshock-orszag-tang-en) (`postshock-orszag-tang`; Related-model reference · Finite-grid numerical reference)

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.
## Assumptions, units and boundaries

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.

**Editorial clarification**

Educational fixed inputs only. Count HLLD-to-HLLE fallbacks and face reconstruction positivity scaling; no cell floor/clipping/retry. Finite-grid references are not exact solutions; no universal stability, positivity or order guarantee. Independent comparisons are final-only. Intermediate Athena outputs occur just after requested quarter times and are not matched frames. Athena native-face divergence is not exported/measured. Density contrast diagnoses compression, not a mathematical proof of shock formation.

## Adopted numerical method

Full-eight-state HLLD fluxes, MC-MUSCL reconstruction and fixed-step Heun. Shared face fluxes and CT-contact corner EMFs update native face B; cell B is adjacent-face averaged. Initial discrete vector-potential curl and sampled fluid states match the official generator.

$$
\partial_tU+\partial_xF_x(U)+\partial_yF_y(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B)
$$

$$
E=\frac{p}{\gamma-1}+\frac12\rho|\mathbf v|^2+\frac12|\mathbf B|^2,\quad\gamma=5/3
$$

$$
\frac{dB_x}{dt}=-D_y\mathcal E_z,\quad\frac{dB_y}{dt}=D_x\mathcal E_z,\quad D_xB_x+D_yB_y=\mathrm{constant}
$$

$$
\bar U_i^{\mathrm{ref}}=\frac1{N_i}\sum_{j\in i}\bar U_j^{\mathrm{fine}},\qquad e_1=\frac{\sum|U-U^{\mathrm{ref}}|}{\sum|U^{\mathrm{ref}}|}
$$

$$
\rho_0=\frac{25}{36\pi},\quad p_0=\frac5{12\pi},\quad\mathbf v_0=(\sin2\pi y,-\sin2\pi x,0)
$$

## References and validation

Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify Athena++ with two grids and a half-CFL probe. Conservatively restrict final conserved states and separate reference sensitivity from primary error. Common-cell divergence and primary native-face divergence are distinct checks.

## Limits

Educational fixed inputs only. Count HLLD-to-HLLE fallbacks and face reconstruction positivity scaling; no cell floor/clipping/retry. Finite-grid references are not exact solutions; no universal stability, positivity or order guarantee. Independent comparisons are final-only. Intermediate Athena outputs occur just after requested quarter times and are not matched frames. Athena native-face divergence is not exported/measured. Density contrast diagnoses compression, not a mathematical proof of shock formation.

## Stored measurements and decisions

```json
{
  "metrics": {
    "completed_pde_runs": 4,
    "reference_qualification_passed": true,
    "analytic_quadrature_difference": null
  },
  "checks": {
    "four prescribed fixed runs": true,
    "qualified independent reference": true,
    "postshock-orszag-tang-n16 all stages finite positive": true,
    "postshock-orszag-tang-n16 final time": true,
    "postshock-orszag-tang-n16 five exact snapshots": true,
    "postshock-orszag-tang-n16 fluid integral conservation": true,
    "postshock-orszag-tang-n16 native face divergence": true,
    "postshock-orszag-tang-n16 measured Courant sum": true,
    "postshock-orszag-tang-n16 no cell clips or retries": true,
    "postshock-orszag-tang-n16 explicit fallback accounting": true,
    "postshock-orszag-tang-n32 all stages finite positive": true,
    "postshock-orszag-tang-n32 final time": true,
    "postshock-orszag-tang-n32 five exact snapshots": true,
    "postshock-orszag-tang-n32 fluid integral conservation": true,
    "postshock-orszag-tang-n32 native face divergence": true,
    "postshock-orszag-tang-n32 measured Courant sum": true,
    "postshock-orszag-tang-n32 no cell clips or retries": true,
    "postshock-orszag-tang-n32 explicit fallback accounting": true,
    "postshock-orszag-tang-n64 all stages finite positive": true,
    "postshock-orszag-tang-n64 final time": true,
    "postshock-orszag-tang-n64 five exact snapshots": true,
    "postshock-orszag-tang-n64 fluid integral conservation": true,
    "postshock-orszag-tang-n64 native face divergence": true,
    "postshock-orszag-tang-n64 measured Courant sum": true,
    "postshock-orszag-tang-n64 no cell clips or retries": true,
    "postshock-orszag-tang-n64 explicit fallback accounting": true,
    "postshock-orszag-tang-half-dt all stages finite positive": true,
    "postshock-orszag-tang-half-dt final time": true,
    "postshock-orszag-tang-half-dt five exact snapshots": true,
    "postshock-orszag-tang-half-dt fluid integral conservation": true,
    "postshock-orszag-tang-half-dt native face divergence": true,
    "postshock-orszag-tang-half-dt measured Courant sum": true,
    "postshock-orszag-tang-half-dt no cell clips or retries": true,
    "postshock-orszag-tang-half-dt explicit fallback accounting": true,
    "density refinement n32": true,
    "density refinement n64": true,
    "density finest error": true,
    "density separate time contamination fraction": true,
    "density reference increment/error": true,
    "pressure refinement n32": true,
    "pressure refinement n64": true,
    "pressure finest error": true,
    "pressure separate time contamination fraction": true,
    "pressure reference increment/error": true,
    "late density compression diagnostic": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/index.json

![Actual saved primary 2D density field at T.2.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/results/postshock-orszag-tang-preview.png)

Actual saved primary 2D density field at T.2.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Athena++ collaboration (2026). Athena++ official field_loop and orszag_tang problem generators, pinned source [accessed 2026-11-23]. https://github.com/PrincetonUniversity/athena/tree/1395e2f543f4368d448cb1a2cf92ba1f910e3416; review_level=Official archive SHA verified; selected src/pgen/field_loop.cpp and orszag_tang.cpp, PLM/RK2/output configuration and actual conserved tab headers inspected; not a full Athena code audit
Verified the official pinned archive SHA and inspected both generators, configuration and saved columns. Executed the independent engine and checked spatial/time sensitivity. No complete code audit or exact-solution claim.

- Thomas A. Gardiner and James M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport [accessed 2026-11-23]. https://arxiv.org/abs/astro-ph/0501557; review_level=Author arXiv PDF selected section2.2 equations13–20,3.3.1–3.3.2 and5.1–5.2 inspected; not the full paper or original experiment replication
Inspected the author PDF CT section and loop/polarized-wave definitions. Original CTU/PPM and oblique-wave experiments are not replicated. Our wave is 1D aligned; the official loop generator explicitly has vz=2.

- Takahiro Miyoshi and Kanya Kusano (2005). A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics [accessed 2026-11-23]. https://doi.org/10.1016/j.jcp.2005.02.017; review_level=Bibliographic metadata checked; publisher full text returned403. This addition did not newly audit original equations or experiments
Bibliographic metadata checked; full publisher text unavailable. No new original-equation/experiment audit is claimed. Full-state HLLD is inherited byte-for-byte from the prior public validated Atlas.

- Steven A. Orszag and Ching-Mao Tang (1979). Small-scale structure of two-dimensional magnetohydrodynamic turbulence [accessed 2026-11-23]. https://doi.org/10.1017/S002211207900210X; review_level=Original publisher abstract/bibliography inspected only; original incompressible viscous/resistive setup differs from the official compressible ideal-MHD generator used here
Inspected publisher abstract and bibliography only. Distinguish the original incompressible viscous/resistive study from the official compressible ideal-MHD setup used here.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
