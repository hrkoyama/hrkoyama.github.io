# 勾配法・準Newton法

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/optimization/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [勾配法・準Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja>)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [GN・LMと有界最小二乗のBratu比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja>)
  availability: run

  同じ観測からの17固定fitで、変数尺度・重み・境界と物理座標の停止条件を分けます。
- [既知最小点でのBFGSと3組L-BFGS](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja>)
  availability: run

  8次元SPD二次関数と3初期値のRosenbrockを用い、曲率・strong Wolfe・現在の有限記憶作用を検査します。
- [雑音・モデル差と有限γ経路の正則化](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja>)
  availability: run

  2独立ノイズベクトルを尺度・データ文脈で共有し、42固定fitから有限γ選択と固定γの局所共分散を分けます。
- [勾配法・準Newton法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
