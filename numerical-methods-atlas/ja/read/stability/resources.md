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

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。
- [WENO5-JS](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。
- [有限差分WENO5-Z](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。

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

  周期正弦波の解析的な平行移動が基準です。問題台帳には振幅や離散表現の異なる比較を統合しており、参照解一覧の振幅0.25を全実行例に流用しません。
- [移流／正弦波の平行移動](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 単位区間の周期境界、一定移流速度1。 同じ周期・速度1の正弦移流モデルです。参照一覧は振幅0.25、共通固定入力は0.2で、DG・CIP等の表現や時間も異なります。
- [WENO臨界点：多項式セル平均と解析的周期輸送](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-weno-critical-profile-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 局所参照はx=0を中心とする5セルの解析平均からh/2を評価する多項式です。通常・一次・二次臨界の3形、h=1/64…1/512を区別します。実際の周期輸送参照は[0,1]、速度1、T1、q₀=cos(2πx)+.1sin³(2πx)のFourier積分セル平均で、別のGauss12点関数求積と照合します。局所多項式と輸送の初期形は異なり、点値や別PDE計算の参照ではありません。 同じ一定速度の周期移流に対する追加参照ですが、cos+.1sin³のセル平均と局所臨界多項式は、従来の単一正弦・CIP表示と異なります。
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
- [周期正弦波の線形移流：風上法と解析解](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=ja>)
  availability: run

  長さ1の周期区間でq_t+a q_x=0を1周期進め、64/128点の1次風上法を平行移動した正弦波と比較する。計算値、解析値、誤差をCSVへ出す。
- [Zalesak型2D回転輸送：保存・有界性・形状誤差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja>)
  availability: run

  スロット付き円盤を実際の2次元有限体積法で一回転させ、donor-cellとminmod MUSCLを比較します。3格子と、半セルの中心ずらし・45度の初期向きを含む8計算で、保存・各SSP段の有界性・形状誤差とスロットの埋まりを測ります。
- [Euler二重膨張波：段階ごとの正値性](<https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja>)
  availability: run

  既存の強い二重希薄波を128/256/512セルで計算し、平均保存型の正値性スケーリングをMUSCL・大域LF流束・SSPRK(3,3)へ接続します。各前進Euler段と各SSP凸結合の密度・圧力・境界保存収支を記録します。
- [WENO-JS／Z：臨界点とεの固定比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja>)
  availability: run

  同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。
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
