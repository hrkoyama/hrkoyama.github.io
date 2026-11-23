# スペクトル要素法とFR：既存FEM・DGとの軽量比較

SEMの2D PoissonとFRの1D周期移流を、既存P1 FEM・modal DGと同じ方程式・境界・参照で比較します。h/p収束、連続誤差、残差、保存と時間誤差を分け、外部Nek/PyFRソルバーの実行とは区別します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較

単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。

**使用手法**

- [スペクトル要素法（SEM）](https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/?lang=ja) (`spectral-element`)
- [連続P1 Galerkin有限要素法](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja) (`p1-fem`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja#sem-poisson-2d-ja-algorithm)

SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。

$$
-\Delta u=f,\quad u|_{\partial\Omega}=0,\quad u_*=\sin(\pi x)\sin(\pi y),\quad f=2\pi^2u_*
$$

$$
K^e=S\otimes W+W\otimes S,\quad S=D^TWD,\quad W=\operatorname{diag}(w_i)
$$

$$
E_{L^2}=\left(\int_\Omega(u_h-u_*)^2\,d\Omega\right)^{1/2},\quad E_{H^1}=\left(\int_\Omega|\nabla u_h-\nabla u_*|^2\,d\Omega\right)^{1/2}
$$

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`)

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。


**問題の図**

![スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja#sem-poisson-2d-ja-validation)

解析的な正弦製造解と勾配を参照し、GLL節点とは異なる高次Gauss点で連続L2誤差・H1半ノルムを積分。h/p収束・自由未知数を揃えた誤差・境界値・真の残差を検査し、実際の2D場とP1の頂点・三角形・解をNPZに保存。

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照 · 製造解)

カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。

- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja) (`sem-poisson-2d`; 同じ問題の参照 · 製造解)

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。
### 前提・単位・境界

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。

### 採用した計算法

SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。

$$
-\Delta u=f,\quad u|_{\partial\Omega}=0,\quad u_*=\sin(\pi x)\sin(\pi y),\quad f=2\pi^2u_*
$$

$$
K^e=S\otimes W+W\otimes S,\quad S=D^TWD,\quad W=\operatorname{diag}(w_i)
$$

$$
E_{L^2}=\left(\int_\Omega(u_h-u_*)^2\,d\Omega\right)^{1/2},\quad E_{H^1}=\left(\int_\Omega|\nabla u_h-\nabla u_*|^2\,d\Omega\right)^{1/2}
$$

### 比較・検証

解析的な正弦製造解と勾配を参照し、GLL節点とは異なる高次Gauss点で連続L2誤差・H1半ノルムを積分。h/p収束・自由未知数を揃えた誤差・境界値・真の残差を検査し、実際の2D場とP1の頂点・三角形・解をNPZに保存。

### 確認の限界

滑らかな固定問題だけの結果。要素・求積・代数ソルバーが異なるので、速度・計算量・汎用的優位性の比較ではありません。GLLの対角求積質量は一般の積の厳密な質量行列ではない。曲線格子・特異解・非圧縮流体・Nek5000/nekRS本体は未実行。

### 保存実測値と判定

```json
{
  "metrics": {
    "sem_h_l2_order": 3.0396439861149207,
    "sem_h_h1_order": 2.010636067947865,
    "p1_h_l2_order": 1.9744920294804964,
    "p1_h_h1_order": 0.9891011038360976,
    "p_refinement_l2_reduction": 311080.7699512155,
    "p6_l2_error": 3.7801651652951424e-07,
    "same_dof_free_unknowns": 225,
    "sem_finest_l2_error": 0.0002486410968007461,
    "p1_finest_l2_error": 0.005377435009938097,
    "same_dof_l2_ratio_sem_over_p1": 0.046237861794931924,
    "maximum_relative_residual": 3.1814596822002824e-12
  },
  "checks": {
    "sem_h_l2_convergence": true,
    "sem_h_h1_convergence": true,
    "p1_h_l2_convergence": true,
    "p1_h_h1_convergence": true,
    "p_refinement_monotone": true,
    "p_refinement_resolved": true,
    "equal_free_dofs": true,
    "same_dof_error_comparison": true,
    "linear_residuals": true,
    "zero_dirichlet_boundary": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/index.json

![保存した2D SEM場と節点誤差。連続誤差ノルムは別のGauss積分で評価しています。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d-preview.png)

保存した2D SEM場と節点誤差。連続誤差ノルムは別のGauss積分で評価しています。

### 取得・実行

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

### 出典と確認範囲

- A. T. Patera (1984). A spectral element method for fluid dynamics: Laminar flow in a channel expansion. https://nek5000.github.io/NekDoc/references.html; review_level=metadata
Nek5000公式参考文献の題名・巻・頁・DOIを照合。出版社の原文は未取得で、原報全体の監査・数値再現とはしない。今回の実装はLegendre GLL変種。

- Nek5000 development team (2026). Nek5000 documentation: Theory and spectral-element basis (accessed 2026-11-23). https://nek5000.github.io/NekDoc/theory.html; review_level=full-text
公式TheoryとFAQの要素局所の多項式、GLL/GL点・C0連続性を確認。教育用Poissonの実装とNek5000の流体ソルバー全体を同一視しない。

- Nek5000/RS development team (2026). Nek5000/RS project: spectral-element solvers and related implementations (accessed 2026-11-23). https://nek5000.github.io/; review_level=full-text
公式プロジェクトのSEM、nekRSのCPU/GPU対応、Nek5000との関係を確認。外部ソルバーの導入・実行・性能比較は未実施。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## FR法の1D周期移流：Radau補正と既存DGの比較

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
### 前提・単位・境界

全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。

### 採用した計算法

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

### 比較・検証

追加のGauss点で連続L2誤差を積分し、既存DGの最終多項式と共通点で照合。全RK段階の重み付き質量と各完了ステップの2次エネルギーを検査。同じFR空間演算子の行列指数解で時間誤差を別測定し、刻み半減を確認。

### 確認の限界

このRadau/Gauss・線形一定流束・アフィン要素の設定がDGに対応します。全FRと全DGの同値性、非線形流束・衝撃波・制限器・多次元FRは保証しません。hとΔtの同時細分化と行列指数による空間誤差を分け、行列指数を独立した空間PDEソルバーとは呼びません。PyFR本体は未実行。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- H. T. Huynh (2007). A Flux Reconstruction Approach to High-Order Schemes Including Discontinuous Galerkin Methods. https://ntrs.nasa.gov/api/citations/20140009969/downloads/20140009969.pdf; review_level=metadata
著者の2014年NASA報告の参考文献（本文27頁）で2007年原報の題名・著者・会議番号を確認。AIAA原文は未取得。補正式は別記の2014年本文を参照。

- H. T. Huynh (2014). On Formulations of Discontinuous Galerkin and Related Methods for Conservation Laws. https://ntrs.nasa.gov/api/citations/20140009969/downloads/20140009969.pdf; review_level=full-text
NASA原文の抄録、微分形と界面補正、本文19–21頁の式(6.2)–(6.13)のRadau補正とDG対応、27頁の書誌を確認。全報告の監査や非線形実験の再現ではない。

- PyFR development team (2026). PyFR: Flux Reconstruction and supported implementation platforms (accessed 2026-11-23). https://www.pyfr.org/; review_level=full-text
公式サイトのFRによる空間離散化・非構造格子・CPU/GPUの紹介を確認。今回の軽量Python例でPyFRを導入・実行・検証したとはしない。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
