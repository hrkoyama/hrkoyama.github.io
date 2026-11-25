# 作用素分割：Lie–Trotter と Strang の比較

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/operator-splitting/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Lie–Trotter分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=ja>)
- [Strang分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja>)
- [陰的中点則](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja>)

## 方程式

- [非同次境界を持つ線形反応拡散](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#inhomogeneous-reaction-diffusion-ja>)

  同じ非周期有限差分系に対する時間誤差と、連続厳密解に対する空間誤差を分けます。

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [同じ非線形反応拡散でLie–TrotterとStrangを比較する](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja>)
  availability: run

  32格子・終了時刻1のSchnakenberg反応拡散を、同じ入力・部分ソルバーでLie–TrotterとStrangにより進めます。4段階の時間刻みで1次／2次の収束、参照の感度、反応収支と未収束時の失敗を確かめる軽量な比較例です。
- [Dirichlet境界でのStrang次数低下と補正](<https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja>)
  availability: run

  実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。
- [結合した2周波数系と共鳴の有限窓](<https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja>)
  availability: run

  2自由度の実結合系で、12の64刻みprobeと6の精度軌道を使い、真のモード、座標間交換、離散写像と丸めを分けます。
- [Schnakenberg：2D境界と初期モード](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja>)
  availability: run

  2つのNeumann摂動とDirichlet摂動を独立な非線形Galerkin参照と比較します。
- [Lie–Trotter分割：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Strang分割：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
