# 作用素分割：同じ反応拡散でLie–TrotterとStrangを比較

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-splitting/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Lie–Trotter分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=ja>)
- [Strang分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja>)

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja#reaction-diffusion-splitting-ja-algorithm>)

  Lie–Trotterは拡散h→反応h、Strangは拡散h/2→反応h→拡散h/2。どちらも更新後の状態を次へ渡します。拡散は2次中心FD行列の指数をFFTで厳密適用、反応は同じ陰的中点則・Newton公差2e−13・上限12評価を使用。反応流は厳密解ではなく2次近似です。クリッピング・自動刻み変更・代替解法への切替を行わず、未収束は失敗にします。

## 問題の図

- [同じ非線形反応拡散でLie–TrotterとStrangを比較する](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/results/reaction-diffusion-splitting.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/results/reaction-diffusion-splitting.png

## 厳密解・参照解

- [同じ非線形反応拡散でLie–TrotterとStrangを比較する：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja#reaction-diffusion-splitting-ja-validation>)

  参照は同じFD半離散系を実空間の疎行列・別記述の反応RHSで組み、分割せずRadauで積分した数値解です。Radauの公差細分化と別のDOP853で参照自身の差を測り、最細Strang誤差との比を判定します。ノルムは成分ごとの平均L1・RMS L2・最大L∞を求めて悪い成分を採用し、4つの正の共通出力時刻の最大値で次数を測定。Newton公差感度、全副段階の正濃度、反応source/sink収支と逆順Lieの対照も記録します。

## コード・検証

- [同じ非線形反応拡散でLie–TrotterとStrangを比較する](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja>)
  availability: run

  32格子・終了時刻1のSchnakenberg反応拡散を、同じ入力・部分ソルバーでLie–TrotterとStrangにより進めます。4段階の時間刻みで1次／2次の収束、参照の感度、反応収支と未収束時の失敗を確かめる軽量な比較例です。
