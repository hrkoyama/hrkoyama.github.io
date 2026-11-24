# MHD輸送・波・圧縮構造の独立比較

全8保存量のHLLD・MUSCL・Heunと2D CTで、円偏波・磁場ループ・圧縮後OTを計算します。解析平均または未改変Athena++の保存場を、独立参照の格子・時間誤差を区別して比較します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 円偏波Alfvén波：全成分の格子収束

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

![円偏波Alfvén波：全成分の格子収束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/results/circular-alfven-refinement.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[円偏波Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja) (`circular-alfven`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja#circular-alfven-refinement-ja-validation)

実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。解析保存平均を独立Gauss16求積と照合し、横成分誤差・位相・観測次数を検査します。

- [円偏波Alfvén波：全保存変数の解析セル平均](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-circular-alfven-refinement-ja) (`circular-alfven-refinement`; 関連モデルの参照 · 解析参照)

γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。
### 前提・単位・境界

γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。

**編集上の補足**

少数の固定入力に対する教育用検証です。HLLDのHLLE代替と再構成の正値性スケーリングを数え、セル状態の床・クリップ・再試行は行いません。有限格子参照は厳密解ではなく、任意問題の安定性・正値性や普遍的次数を保証しません。1次元整列波の次数であり、斜め2次元伝播の検証ではありません。

### 採用した計算法

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

### 比較・検証

実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。解析保存平均を独立Gauss16求積と照合し、横成分誤差・位相・観測次数を検査します。

### 確認の限界

少数の固定入力に対する教育用検証です。HLLDのHLLE代替と再構成の正値性スケーリングを数え、セル状態の床・クリップ・再試行は行いません。有限格子参照は厳密解ではなく、任意問題の安定性・正値性や普遍的次数を保証しません。1次元整列波の次数であり、斜め2次元伝播の検証ではありません。

### 保存実測値と判定

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

![保存した主計算の実際のBy(x,t)の5時刻場。1次元空間と時間を表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/results/circular-alfven-refinement-preview.png)

保存した主計算の実際のBy(x,t)の5時刻場。1次元空間と時間を表示。

### 取得・実行

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

### 出典と確認範囲

- Athena++ collaboration (2026). Athena++ official field_loop and orszag_tang problem generators, pinned source [accessed 2026-11-23]. https://github.com/PrincetonUniversity/athena/tree/1395e2f543f4368d448cb1a2cf92ba1f910e3416; review_level=Official archive SHA verified; selected src/pgen/field_loop.cpp and orszag_tang.cpp, PLM/RK2/output configuration and actual conserved tab headers inspected; not a full Athena code audit
固定コミットの公式アーカイブSHAを照合し、2初期値生成器と設定・保存列を確認。別実装を実行して参照場を作成し、空間・時間感度を検査。全ソース監査や厳密解とは表示しません。

- Thomas A. Gardiner and James M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport [accessed 2026-11-23]. https://arxiv.org/abs/astro-ph/0501557; review_level=Author arXiv PDF selected section2.2 equations13–20,3.3.1–3.3.2 and5.1–5.2 inspected; not the full paper or original experiment replication
著者公開PDFのCT節・磁場ループ・円偏波の定義を確認。論文のCTU/PPMや斜め伝播実験を再現したとは主張しません。今回の円偏波は1次元整列、公式磁場ループはvz=2の明示的変更です。

- Takahiro Miyoshi and Kanya Kusano (2005). A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics [accessed 2026-11-23]. https://doi.org/10.1016/j.jcp.2005.02.017; review_level=Bibliographic metadata checked; publisher full text returned403. This addition did not newly audit original equations or experiments
書誌を確認。出版社本文は取得できず、今回新たに原著の式や実験を監査したとは表示しません。全8変数HLLDコードは過去の公開検証済みAtlasから同一バイトで継承します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 磁場ループ：独立2次元参照と細分化

実際の2次元磁場ループ輸送を、別実装Athena++の空間・時間感度を検査した終端保存場と比較します。

**使用手法**

- [HLLDのMHDリーマン解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=ja) (`hlld`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)
- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) (`ct`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja#magnetic-loop-independent-ja-algorithm)

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
A_z=.001\max(.3-\sqrt{x^2+y^2},0),\qquad\mathbf v=(2,1,2)
$$

- [理想MHD](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#mhd-ja) (`mhd`)

[-1,1]×[-.5,.5]周期、ρ=p=1、Az=.001max(.3−r,0)、T=1、(Nx,Ny)=(16,8),(32,16),(64,32)。変更していない公式生成器と同じv=(2,1,2)で、古いvz=0設定とは区別します。


**問題の図**

![磁場ループ：独立2次元参照と細分化：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/results/magnetic-loop-independent.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[磁場ループの移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja) (`magnetic-loop`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja#magnetic-loop-independent-ja-validation)

実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。Athena++の2格子と刻み半減で参照を検定。終端保存変数を保守的に粗視化し、誤差と参照感度を分離します。共通セル発散と主計算の固有面発散は別の検査です。

- [磁場ループ：固定Athena++の独立終端参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-magnetic-loop-independent-ja) (`magnetic-loop-independent`; 関連モデルの参照 · 有限格子の数値参照)

[-1,1]×[-.5,.5]周期、ρ=p=1、Az=.001max(.3−r,0)、T=1、(Nx,Ny)=(16,8),(32,16),(64,32)。変更していない公式生成器と同じv=(2,1,2)で、古いvz=0設定とは区別します。
### 前提・単位・境界

[-1,1]×[-.5,.5]周期、ρ=p=1、Az=.001max(.3−r,0)、T=1、(Nx,Ny)=(16,8),(32,16),(64,32)。変更していない公式生成器と同じv=(2,1,2)で、古いvz=0設定とは区別します。

**編集上の補足**

少数の固定入力に対する教育用検証です。HLLDのHLLE代替と再構成の正値性スケーリングを数え、セル状態の床・クリップ・再試行は行いません。有限格子参照は厳密解ではなく、任意問題の安定性・正値性や普遍的次数を保証しません。独立比較は終端のみ。中間Athena時刻は指定四半時刻直後で、正確に整列した場とは表示しません。Athenaの固有面発散は出力しておらず測定を主張しません。密度比は圧縮の診断であり数学的衝撃波の証明ではありません。

### 採用した計算法

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
A_z=.001\max(.3-\sqrt{x^2+y^2},0),\qquad\mathbf v=(2,1,2)
$$

### 比較・検証

実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。Athena++の2格子と刻み半減で参照を検定。終端保存変数を保守的に粗視化し、誤差と参照感度を分離します。共通セル発散と主計算の固有面発散は別の検査です。

### 確認の限界

少数の固定入力に対する教育用検証です。HLLDのHLLE代替と再構成の正値性スケーリングを数え、セル状態の床・クリップ・再試行は行いません。有限格子参照は厳密解ではなく、任意問題の安定性・正値性や普遍的次数を保証しません。独立比較は終端のみ。中間Athena時刻は指定四半時刻直後で、正確に整列した場とは表示しません。Athenaの固有面発散は出力しておらず測定を主張しません。密度比は圧縮の診断であり数学的衝撃波の証明ではありません。

### 保存実測値と判定

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
    "magnetic-loop-independent-n8 all stages finite positive": true,
    "magnetic-loop-independent-n8 final time": true,
    "magnetic-loop-independent-n8 five exact snapshots": true,
    "magnetic-loop-independent-n8 fluid integral conservation": true,
    "magnetic-loop-independent-n8 native face divergence": true,
    "magnetic-loop-independent-n8 measured Courant sum": true,
    "magnetic-loop-independent-n8 no cell clips or retries": true,
    "magnetic-loop-independent-n8 explicit fallback accounting": true,
    "magnetic-loop-independent-n16 all stages finite positive": true,
    "magnetic-loop-independent-n16 final time": true,
    "magnetic-loop-independent-n16 five exact snapshots": true,
    "magnetic-loop-independent-n16 fluid integral conservation": true,
    "magnetic-loop-independent-n16 native face divergence": true,
    "magnetic-loop-independent-n16 measured Courant sum": true,
    "magnetic-loop-independent-n16 no cell clips or retries": true,
    "magnetic-loop-independent-n16 explicit fallback accounting": true,
    "magnetic-loop-independent-n32 all stages finite positive": true,
    "magnetic-loop-independent-n32 final time": true,
    "magnetic-loop-independent-n32 five exact snapshots": true,
    "magnetic-loop-independent-n32 fluid integral conservation": true,
    "magnetic-loop-independent-n32 native face divergence": true,
    "magnetic-loop-independent-n32 measured Courant sum": true,
    "magnetic-loop-independent-n32 no cell clips or retries": true,
    "magnetic-loop-independent-n32 explicit fallback accounting": true,
    "magnetic-loop-independent-half-dt all stages finite positive": true,
    "magnetic-loop-independent-half-dt final time": true,
    "magnetic-loop-independent-half-dt five exact snapshots": true,
    "magnetic-loop-independent-half-dt fluid integral conservation": true,
    "magnetic-loop-independent-half-dt native face divergence": true,
    "magnetic-loop-independent-half-dt measured Courant sum": true,
    "magnetic-loop-independent-half-dt no cell clips or retries": true,
    "magnetic-loop-independent-half-dt explicit fallback accounting": true,
    "magnetic refinement n16": true,
    "magnetic refinement n32": true,
    "magnetic finest error": true,
    "magnetic separate time contamination fraction": true,
    "magnetic reference increment/error": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/index.json

![保存した主計算の実際の2次元面内磁気エネルギー、T=1。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/results/magnetic-loop-independent-preview.png)

保存した主計算の実際の2次元面内磁気エネルギー、T=1。

### 取得・実行

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

### 出典と確認範囲

- Athena++ collaboration (2026). Athena++ official field_loop and orszag_tang problem generators, pinned source [accessed 2026-11-23]. https://github.com/PrincetonUniversity/athena/tree/1395e2f543f4368d448cb1a2cf92ba1f910e3416; review_level=Official archive SHA verified; selected src/pgen/field_loop.cpp and orszag_tang.cpp, PLM/RK2/output configuration and actual conserved tab headers inspected; not a full Athena code audit
固定コミットの公式アーカイブSHAを照合し、2初期値生成器と設定・保存列を確認。別実装を実行して参照場を作成し、空間・時間感度を検査。全ソース監査や厳密解とは表示しません。

- Thomas A. Gardiner and James M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport [accessed 2026-11-23]. https://arxiv.org/abs/astro-ph/0501557; review_level=Author arXiv PDF selected section2.2 equations13–20,3.3.1–3.3.2 and5.1–5.2 inspected; not the full paper or original experiment replication
著者公開PDFのCT節・磁場ループ・円偏波の定義を確認。論文のCTU/PPMや斜め伝播実験を再現したとは主張しません。今回の円偏波は1次元整列、公式磁場ループはvz=2の明示的変更です。

- Takahiro Miyoshi and Kanya Kusano (2005). A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics [accessed 2026-11-23]. https://doi.org/10.1016/j.jcp.2005.02.017; review_level=Bibliographic metadata checked; publisher full text returned403. This addition did not newly audit original equations or experiments
書誌を確認。出版社本文は取得できず、今回新たに原著の式や実験を監査したとは表示しません。全8変数HLLDコードは過去の公開検証済みAtlasから同一バイトで継承します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 後期Orszag–Tang：独立参照と圧縮構造

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
### 前提・単位・境界

γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。

**編集上の補足**

少数の固定入力に対する教育用検証です。HLLDのHLLE代替と再構成の正値性スケーリングを数え、セル状態の床・クリップ・再試行は行いません。有限格子参照は厳密解ではなく、任意問題の安定性・正値性や普遍的次数を保証しません。独立比較は終端のみ。中間Athena時刻は指定四半時刻直後で、正確に整列した場とは表示しません。Athenaの固有面発散は出力しておらず測定を主張しません。密度比は圧縮の診断であり数学的衝撃波の証明ではありません。

### 採用した計算法

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

### 比較・検証

実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。Athena++の2格子と刻み半減で参照を検定。終端保存変数を保守的に粗視化し、誤差と参照感度を分離します。共通セル発散と主計算の固有面発散は別の検査です。

### 確認の限界

少数の固定入力に対する教育用検証です。HLLDのHLLE代替と再構成の正値性スケーリングを数え、セル状態の床・クリップ・再試行は行いません。有限格子参照は厳密解ではなく、任意問題の安定性・正値性や普遍的次数を保証しません。独立比較は終端のみ。中間Athena時刻は指定四半時刻直後で、正確に整列した場とは表示しません。Athenaの固有面発散は出力しておらず測定を主張しません。密度比は圧縮の診断であり数学的衝撃波の証明ではありません。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- Athena++ collaboration (2026). Athena++ official field_loop and orszag_tang problem generators, pinned source [accessed 2026-11-23]. https://github.com/PrincetonUniversity/athena/tree/1395e2f543f4368d448cb1a2cf92ba1f910e3416; review_level=Official archive SHA verified; selected src/pgen/field_loop.cpp and orszag_tang.cpp, PLM/RK2/output configuration and actual conserved tab headers inspected; not a full Athena code audit
固定コミットの公式アーカイブSHAを照合し、2初期値生成器と設定・保存列を確認。別実装を実行して参照場を作成し、空間・時間感度を検査。全ソース監査や厳密解とは表示しません。

- Thomas A. Gardiner and James M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport [accessed 2026-11-23]. https://arxiv.org/abs/astro-ph/0501557; review_level=Author arXiv PDF selected section2.2 equations13–20,3.3.1–3.3.2 and5.1–5.2 inspected; not the full paper or original experiment replication
著者公開PDFのCT節・磁場ループ・円偏波の定義を確認。論文のCTU/PPMや斜め伝播実験を再現したとは主張しません。今回の円偏波は1次元整列、公式磁場ループはvz=2の明示的変更です。

- Takahiro Miyoshi and Kanya Kusano (2005). A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics [accessed 2026-11-23]. https://doi.org/10.1016/j.jcp.2005.02.017; review_level=Bibliographic metadata checked; publisher full text returned403. This addition did not newly audit original equations or experiments
書誌を確認。出版社本文は取得できず、今回新たに原著の式や実験を監査したとは表示しません。全8変数HLLDコードは過去の公開検証済みAtlasから同一バイトで継承します。

- Steven A. Orszag and Ching-Mao Tang (1979). Small-scale structure of two-dimensional magnetohydrodynamic turbulence [accessed 2026-11-23]. https://doi.org/10.1017/S002211207900210X; review_level=Original publisher abstract/bibliography inspected only; original incompressible viscous/resistive setup differs from the official compressible ideal-MHD generator used here
出版社の抄録と書誌のみ確認。原著の非圧縮・粘性抵抗モデルと、今回の圧縮性理想MHDの公式初期値を区別します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
