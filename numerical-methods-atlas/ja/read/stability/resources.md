# 差分、CFL条件、von Neumann解析、Laxの定理

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stability/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [空間前進差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-difference/?lang=ja>)
- [空間後退差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-difference/?lang=ja>)
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)
- [風上差分（upwind）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja>)
- [Lax–Friedrichs法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-friedrichs/?lang=ja>)
- [Lax–Wendroff法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-wendroff/?lang=ja>)
- [風上差分（upwind）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。 p+1個のGauss解点、上流数値流束、Legendre多項式によるRadau左右補正、SSPRK(3,3)。初期L2射影・上流流束・時間刻み規約をバイト一致の既存modal DGと揃えます。スケールしたCourant数(2p+1)|a|Δt/h≤.15。最後にp2/N32で刻みを半減。
- [WENO5-JS](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。 p+1個のGauss解点、上流数値流束、Legendre多項式によるRadau左右補正、SSPRK(3,3)。初期L2射影・上流流束・時間刻み規約をバイト一致の既存modal DGと揃えます。スケールしたCourant数(2p+1)|a|Δt/h≤.15。最後にp2/N32で刻みを半減。
- [有限差分WENO5-Z](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。 p+1個のGauss解点、上流数値流束、Legendre多項式によるRadau左右補正、SSPRK(3,3)。初期L2射影・上流流束・時間刻み規約をバイト一致の既存modal DGと揃えます。スケールしたCourant数(2p+1)|a|Δt/h≤.15。最後にp2/N32で刻みを半減。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。 p+1個のGauss解点、上流数値流束、Legendre多項式によるRadau左右補正、SSPRK(3,3)。初期L2射影・上流流束・時間刻み規約をバイト一致の既存modal DGと揃えます。スケールしたCourant数(2p+1)|a|Δt/h≤.15。最後にp2/N32で刻みを半減。
- [Flux Reconstruction法（FR法）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/flux-reconstruction/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。 p+1個のGauss解点、上流数値流束、Legendre多項式によるRadau左右補正、SSPRK(3,3)。初期L2射影・上流流束・時間刻み規約をバイト一致の既存modal DGと揃えます。スケールしたCourant数(2p+1)|a|Δt/h≤.15。最後にp2/N32で刻みを半減。
- [不連続Galerkin法／Legendre](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dg/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。 p+1個のGauss解点、上流数値流束、Legendre多項式によるRadau左右補正、SSPRK(3,3)。初期L2射影・上流流束・時間刻み規約をバイト一致の既存modal DGと揃えます。スケールしたCourant数(2p+1)|a|Δt/h≤.15。最後にp2/N32で刻みを半減。

## 方程式

- [線形移流](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja>)

  一定速度aによる輸送。波形の移動、数値拡散、安定性へ。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [線形移流](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja>)

  一定速度aによる輸送。波形の移動、数値拡散、安定性へ。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-advection-sine-ja>)

  一次風上差分＋前進Euler、入力CFL=0.5。連続PDEの平行移動を参照し、離散増幅因子を厳密解として再利用しない。

## 問題の図

- [周期正弦波の線形移流](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png

## 厳密解・参照解

- [周期正弦波の線形移流：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#references-ja>)

  周期正弦波の解析的な平行移動が基準です。問題台帳には振幅や離散表現の異なる比較を統合しており、参照解一覧の振幅0.25を全実行例に流用しません。 追加のGauss点で連続L2誤差を積分し、既存DGの最終多項式と共通点で照合。全RK段階の重み付き質量と各完了ステップの2次エネルギーを検査。同じFR空間演算子の行列指数解で時間誤差を別測定し、刻み半減を確認。
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
- [周期正弦波の線形移流：風上法と解析解：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=ja#advection-sine-ja-validation>)

  CSVは128点の格子中心に1行ずつ配置し、同じ時刻・位置で解析値を評価する。平均の保存と最大値原理には丸め誤差許容値10^-12を用いる。
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

## コード・検証

- [反応拡散：空間2次と時間4次を分けて測る](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja>)
  availability: run

  線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。
- [Turing不安定性：線形成長率と小振幅パターン](<https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja>)
  availability: run

  Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。
- [Schnakenberg有限振幅過渡：非線形性と独立参照](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja>)
  availability: run

  t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。
- [Schnakenberg飽和パターン：近定常性と格子・時間収束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja>)
  availability: run

  t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。
- [Re=100蓋駆動キャビティ：Ghia中心線との比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja>)
  availability: run

  非周期・粘性非圧縮の実際の2D計算を17/33/65点格子で定常化し、Ghia原著の速度中心線と比較します。流線・渦中心・真の残差と発散を同時に保存します。
- [非周期壁面の製造解：速度・剪断・圧力演算子](<https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja>)
  availability: run

  キャビティと同じ壁条件付き2Dソルバーに解析外力を与え、速度と流れ関数の格子収束、壁渦度・壁剪断の誤差を測ります。別の非零Dirichlet圧力製造解でPoisson・勾配の境界演算子も検査します。
- [KHの初期成長：滑らかな周期せん断層](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja>)
  availability: run

  実際の非線形2D渦度方程式を解き、独立Fourier–Galerkin線形初期値問題と有限時間の成長・格子誤差を比較します。
- [RTの初期成長：滑らかなBoussinesq二層](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja>)
  availability: run

  密度差を浮力だけに残す2D Boussinesq系を時間発展し、不安定な滑らかな層の初期成長を独立線形参照で調べます。
- [純Neumannの互換条件と平均値ゲージ](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja>)
  availability: run

  特異な2D Poissonを互換条件と指定平均込みで解き、不適合な外力を拒否します。
- [2D混合Robinの製造解と境界流束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja>)
  availability: run

  2D PoissonのNeumann/Robin面を実際に組み、連続製造解と境界fluxを照合します。
- [2D C-grid回転浅水波の実時間発展](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja>)
  availability: run

  実際の2D staggered場を時間積分し、連続波と離散symbolの参照を分けて比較します。
- [擬似弧長継続でBratuのfoldを越える](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja>)
  availability: run

  同じ1次元Bratu境界値問題の下枝から上枝までを追跡し、接線・fold・独立解析族との空間誤差を調べます。
- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja>)
  availability: run

  非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。
- [離散fold近傍のBratu感度](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja>)
  availability: run

  離散Bratuのfoldへ近づく6固定点で、状態誤差と線形許容差の影響を分け、独立shooting勾配と照合します。
- [分布係数Bratuの行列非形成VJP](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja>)
  availability: run

  2重みだけの局所hat作用で8/16/32個の空間係数を表し、目的関数ごとの随伴VJPを全感度参照と比較します。
- [Dirichlet境界でのStrang次数低下と補正](<https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja>)
  availability: run

  実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。
- [周期正弦波の線形移流：風上法と解析解](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=ja>)
  availability: run

  長さ1の周期区間でq_t+a q_x=0を1周期進め、64/128点の1次風上法を平行移動した正弦波と比較する。計算値、解析値、誤差をCSVへ出す。
- [Zalesak型2D回転輸送：保存・有界性・形状誤差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja>)
  availability: run

  スロット付き円盤を実際の2次元有限体積法で一回転させ、donor-cellとminmod MUSCLを比較します。3格子と、半セルの中心ずらし・45度の初期向きを含む8計算で、保存・各SSP段の有界性・形状誤差とスロットの埋まりを測ります。
- [非一様移動格子で実際に運ぶALEスカラー](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja>)
  availability: run

  質量と格子面位置を同じHeun段で更新し、一様GCLだけでなく非一様な解析波を運びます。
- [等方散乱平板の反射・透過・吸収](<https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja>)
  availability: run

  正負の角度を結合した実際の定常輸送を解き、独立な連続角Fredholm参照とR/T/Aを比較します。
- [Su–Olson1997角度輸送の独立公開表比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja>)
  availability: run

  物質交換を含む実際の正負角度輸送を進め、2023原著者公開の解析benchmark表と比較します。
- [2D吸収影と保存的M1輸送](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja>)
  availability: run

  実際の円形吸収体の影を、特性線の円弦減衰・角度輸送・M1で比較します。
- [2D反向beamとM1閉包の情報損失](<https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja>)
  availability: run

  保存した反向packetの実進行からM1の限界を示し、別の閉M1MMSで数値実装を検証します。
- [Euler二重膨張波：段階ごとの正値性](<https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja>)
  availability: run

  既存の強い二重希薄波を128/256/512セルで計算し、平均保存型の正値性スケーリングをMUSCL・大域LF流束・SSPRK(3,3)へ接続します。各前進Euler段と各SSP凸結合の密度・圧力・境界保存収支を記録します。
- [WENO-JS／Z：臨界点とεの固定比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja>)
  availability: run

  同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。
- [FR法の1D周期移流：Radau補正と既存DGの比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja>)
  availability: run

  0.4+sin(2πx)をT=.25まで移流。Gauss点・Radau補正のFRと既存のmodal DGをp=1/2、8/16/32セルで実行し、誤差・質量・時間積分誤差を測ります。
- [空間前進差分：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-difference/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [空間後退差分：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-difference/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [空間中心差分：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [風上差分（upwind）：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Lax–Friedrichs法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-friedrichs/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Lax–Wendroff法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-wendroff/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
