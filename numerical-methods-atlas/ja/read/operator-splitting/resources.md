# 作用素分割：Lie–Trotter と Strang の比較

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/operator-splitting/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Lie–Trotter分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=ja>)
- [Strang分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja>)
- [陰的中点則](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja>)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [同じ非線形反応拡散でLie–TrotterとStrangを比較する](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja>)
  availability: run

  32格子・終了時刻1のSchnakenberg反応拡散を、同じ入力・部分ソルバーでLie–TrotterとStrangにより進めます。4段階の時間刻みで1次／2次の収束、参照の感度、反応収支と未収束時の失敗を確かめる軽量な比較例です。
- [Lie–Trotter分割：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Strang分割：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
