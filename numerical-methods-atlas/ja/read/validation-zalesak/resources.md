# Zalesak型2D回転輸送：保存・有界性・形状誤差

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-zalesak/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [風上差分（upwind）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja>)

  同じ回転速度・周期有限体積格子で、一次風上とminmod MUSCLをSSPRK(3,3)で進めます。Zalesak FCTを実装したという意味ではありません。
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)

  同じ回転速度・周期有限体積格子で、一次風上とminmod MUSCLをSSPRK(3,3)で進めます。Zalesak FCTを実装したという意味ではありません。
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja>)

  同じ回転速度・周期有限体積格子で、一次風上とminmod MUSCLをSSPRK(3,3)で進めます。Zalesak FCTを実装したという意味ではありません。
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja>)

  同じ回転速度・周期有限体積格子で、一次風上とminmod MUSCLをSSPRK(3,3)で進めます。Zalesak FCTを実装したという意味ではありません。
- [風上差分（upwind）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja>)
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja>)
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja>)

## 方程式

- [2次元の回転移流](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#rotational-advection-ja>)

  与えた剛体回転速度でスカラーを運ぶ2次元保存則。連続場は一回転で戻り、保存量・有界性と切り欠きの形状誤差を調べます。 与えた発散ゼロの回転速度に従うスカラー輸送で、Euler流体の発展ではありません。Zalesak型の円盤・スロットによる形状保持の問題を用いますが、ZalesakのFCTアルゴリズムそのものを実装した例ではありません。連続指示関数の点値と保存量の幾何学的セル平均を区別し、周期境界での数値的な裾も測ります。
- [2次元の回転移流](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#rotational-advection-ja>)

  与えた剛体回転速度でスカラーを運ぶ2次元保存則。連続場は一回転で戻り、保存量・有界性と切り欠きの形状誤差を調べます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja#zalesak-rotation-ja-algorithm>)

  解析的な発散ゼロの法線面速度と、隣接セルで共有する上流数値流束を用います。区分定数donor-cellと、方向別minmod勾配による平均保存型MUSCLを、どちらもSSPRK(3,3)で進めます。4面中点の平均がセル平均に等しいことと、各面のCourant数≤1/4による凸結合を使い、実際の値.20を各FE段で確認します。セル平均のクリップ、状態floor、刻み棄却・再試行は行いません。

## 問題の図

- [Zalesak型の切り欠き円盤の回転輸送](<https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation-preview.png
- [Zalesak型2D回転輸送：保存・有界性・形状誤差](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation.png

## 厳密解・参照解

- [Zalesak型の切り欠き円盤の回転輸送：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja#references-ja>)

  参照は流れを逆回転して初期指示関数を評価する剛体回転です。一回転後は連続場が初期形状へ戻り、比較には同じ格子の幾何学的セル平均を使います。
- [Zalesak型の切り欠き円盤：剛体回転と幾何学的セル平均](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-zalesak-rotation-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 単位正方形の2次元スカラー輸送です。速度(.5−y,x−.5)、角速度1、周期2π、中心(.5,.75)・半径.15の円盤から.475<x<.525かつy<.85のスロットを除き、内部1・外部0とします。公式Firedrake例の正規化した切り欠き円盤だけを取り出した変種で、bell・cone・背景値1・DG・流入境界は再現しません。周期有限体積の対向面では法線速度が一致します。連続解の台は境界から離れており、数値的な裾は別に測ります。参照は剛体回転の逆特性と円盤・多角形の解析的な面積積分によるセル平均で、点値を並べた画像や別PDE計算の細格子解ではありません。一回転後の連続形状への帰還と、位置・初期角度を変えた固定診断を区別します。 円盤とスロットの定義を固定し、保存した初期・帰還時のセル平均と比較します。指示関数の点値や別実装PDEの細格子解を参照と混同しません。
- [Zalesak型の切り欠き円盤：剛体回転と幾何学的セル平均](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-zalesak-rotation-ja>)
  reference_kind: analytic

  解析解 単位正方形の2次元スカラー輸送です。速度(.5−y,x−.5)、角速度1、周期2π、中心(.5,.75)・半径.15の円盤から.475<x<.525かつy<.85のスロットを除き、内部1・外部0とします。公式Firedrake例の正規化した切り欠き円盤だけを取り出した変種で、bell・cone・背景値1・DG・流入境界は再現しません。周期有限体積の対向面では法線速度が一致します。連続解の台は境界から離れており、数値的な裾は別に測ります。参照は剛体回転の逆特性と円盤・多角形の解析的な面積積分によるセル平均で、点値を並べた画像や別PDE計算の細格子解ではありません。一回転後の連続形状への帰還と、位置・初期角度を変えた固定診断を区別します。
- [Zalesak型2D回転輸送：保存・有界性・形状誤差：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja#zalesak-rotation-ja-validation>)

  26単体検査と8固定計算158判定を実行前に固定します。全FE候補・SSP凸結合のmin/max、共有流束による質量収支、再構築の平均保存、3格子のL1/L∞・相対L2を保存します。円と凸多角形の交差面積から独立に作る厳密輸送のセル平均を、SciPyの鉛直切片求積と面積・一次モーメントで照合します。1/4・1/2・3/4回転の誤差と重心も検査し、回転方向や速度の誤りが一回転のreturnだけで隠れないようにします。
- [Zalesak型の切り欠き円盤：剛体回転と幾何学的セル平均](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-zalesak-rotation-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 単位正方形の2次元スカラー輸送です。速度(.5−y,x−.5)、角速度1、周期2π、中心(.5,.75)・半径.15の円盤から.475<x<.525かつy<.85のスロットを除き、内部1・外部0とします。公式Firedrake例の正規化した切り欠き円盤だけを取り出した変種で、bell・cone・背景値1・DG・流入境界は再現しません。周期有限体積の対向面では法線速度が一致します。連続解の台は境界から離れており、数値的な裾は別に測ります。参照は剛体回転の逆特性と円盤・多角形の解析的な面積積分によるセル平均で、点値を並べた画像や別PDE計算の細格子解ではありません。一回転後の連続形状への帰還と、位置・初期角度を変えた固定診断を区別します。 円盤とスロットの定義を固定し、保存した初期・帰還時のセル平均と比較します。指示関数の点値や別実装PDEの細格子解を参照と混同しません。

## コード・検証

- [Zalesak型2D回転輸送：保存・有界性・形状誤差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja>)
  availability: run

  スロット付き円盤を実際の2次元有限体積法で一回転させ、donor-cellとminmod MUSCLを比較します。3格子と、半セルの中心ずらし・45度の初期向きを含む8計算で、保存・各SSP段の有界性・形状誤差とスロットの埋まりを測ります。
