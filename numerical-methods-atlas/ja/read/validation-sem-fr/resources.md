# スペクトル要素法とFR：既存FEM・DGとの軽量比較

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-sem-fr/

この章に登録された手法・問題・実行例の関連資料です。 新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。

## 手法

- [スペクトル要素法（SEM）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/?lang=ja>)
- [連続P1 Galerkin有限要素法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja>)
- [Flux Reconstruction法（FR法）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/flux-reconstruction/?lang=ja>)
- [不連続Galerkin法／Legendre](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dg/?lang=ja>)

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja#sem-poisson-2d-ja-algorithm>)

  SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja#fr-periodic-advection-ja-algorithm>)

  p+1個のGauss解点、上流数値流束、Legendre多項式によるRadau左右補正、SSPRK(3,3)。初期L2射影・上流流束・時間刻み規約をバイト一致の既存modal DGと揃えます。スケールしたCourant数(2p+1)|a|Δt/h≤.15。最後にp2/N32で刻みを半減。
- [線形移流](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja>)

  一定速度aによる輸送。波形の移動、数値拡散、安定性へ。

## 問題の図

- [スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d.png
- [FR法の1D周期移流：Radau補正と既存DGの比較](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/fr-periodic-advection.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/fr-periodic-advection.png
- [2次元Poisson・正弦単一モード（FEMを含む）](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja>)

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png
- [周期正弦波の線形移流](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja>)

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png

## 厳密解・参照解

- [スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja#sem-poisson-2d-ja-validation>)

  解析的な正弦製造解と勾配を参照し、GLL節点とは異なる高次Gauss点で連続L2誤差・H1半ノルムを積分。h/p収束・自由未知数を揃えた誤差・境界値・真の残差を検査し、実際の2D場とP1の頂点・三角形・解をNPZに保存。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。
- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。 全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。
- [FR法の1D周期移流：Radau補正と既存DGの比較：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja#fr-periodic-advection-ja-validation>)

  追加のGauss点で連続L2誤差を積分し、既存DGの最終多項式と共通点で照合。全RK段階の重み付き質量と各完了ステップの2次エネルギーを検査。同じFR空間演算子の行列指数解で時間誤差を別測定し、刻み半減を確認。
- [移流／正弦波の平行移動](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 単位区間の周期境界、一定移流速度1。 同じ周期・速度1の正弦移流モデルです。参照一覧は振幅0.25、共通固定入力は0.2で、DG・CIP等の表現や時間も異なります。
- [WENO臨界点：多項式セル平均と解析的周期輸送](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-weno-critical-profile-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 局所参照はx=0を中心とする5セルの解析平均からh/2を評価する多項式です。通常・一次・二次臨界の3形、h=1/64…1/512を区別します。実際の周期輸送参照は[0,1]、速度1、T1、q₀=cos(2πx)+.1sin³(2πx)のFourier積分セル平均で、別のGauss12点関数求積と照合します。局所多項式と輸送の初期形は異なり、点値や別PDE計算の参照ではありません。 同じ一定速度の周期移流に対する追加参照ですが、cos+.1sin³のセル平均と局所臨界多項式は、従来の単一正弦・CIP表示と異なります。
- [FRとDGの周期正弦移流：平均0.4・T=.25の解析参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fr-periodic-advection-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。 全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。
- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja>)
  reference_kind: manufactured

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 製造解 全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。
- [FRとDGの周期正弦移流：平均0.4・T=.25の解析参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fr-periodic-advection-ja>)
  reference_kind: analytic

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 解析解 全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。
- [2次元Poisson・正弦単一モード（FEMを含む）：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#references-ja>)

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 単位正方形の製造解sin(πx)sin(πy)を使い、差分・連続P1 FEMの格子誤差と、補助AMG例の離散参照を確認します。 追加のamg-conditioningは既知の代数解を使う条件数・残差診断で、物理問題への紐付けはありません。このPoisson問題の格子精度・独立参照の証拠として流用しません。 解析的な正弦製造解と勾配を参照し、GLL節点とは異なる高次Gauss点で連続L2誤差・H1半ノルムを積分。h/p収束・自由未知数を揃えた誤差・境界値・真の残差を検査し、実際の2D場とP1の頂点・三角形・解をNPZに保存。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。
- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja>)
  relation: same-problem
  reference_kind: manufactured

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 製造解 全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。 全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。
- [周期正弦波の線形移流：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#references-ja>)

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 周期正弦波の解析的な平行移動が基準です。問題台帳には振幅や離散表現の異なる比較を統合しており、参照解一覧の振幅0.25を全実行例に流用しません。 追加のGauss点で連続L2誤差を積分し、既存DGの最終多項式と共通点で照合。全RK段階の重み付き質量と各完了ステップの2次エネルギーを検査。同じFR空間演算子の行列指数解で時間誤差を別測定し、刻み半減を確認。
- [移流／正弦波の平行移動](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja>)
  relation: related-model
  reference_kind: analytic

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 解析解 単位区間の周期境界、一定移流速度1。 同じ周期・速度1の正弦移流モデルです。参照一覧は振幅0.25、共通固定入力は0.2で、DG・CIP等の表現や時間も異なります。
- [WENO臨界点：多項式セル平均と解析的周期輸送](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-weno-critical-profile-ja>)
  relation: related-model
  reference_kind: analytic

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 解析解 局所参照はx=0を中心とする5セルの解析平均からh/2を評価する多項式です。通常・一次・二次臨界の3形、h=1/64…1/512を区別します。実際の周期輸送参照は[0,1]、速度1、T1、q₀=cos(2πx)+.1sin³(2πx)のFourier積分セル平均で、別のGauss12点関数求積と照合します。局所多項式と輸送の初期形は異なり、点値や別PDE計算の参照ではありません。 同じ一定速度の周期移流に対する追加参照ですが、cos+.1sin³のセル平均と局所臨界多項式は、従来の単一正弦・CIP表示と異なります。
- [FRとDGの周期正弦移流：平均0.4・T=.25の解析参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fr-periodic-advection-ja>)
  relation: same-problem
  reference_kind: analytic

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 解析解 全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。 全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。

## コード・検証

- [スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja>)
  availability: run

  単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。
- [FR法の1D周期移流：Radau補正と既存DGの比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja>)
  availability: run

  0.4+sin(2πx)をT=.25まで移流。Gauss点・Radau補正のFRと既存のmodal DGをp=1/2、8/16/32セルで実行し、誤差・質量・時間積分誤差を測ります。
