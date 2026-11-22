# 代数的マルチグリッド（AMG）

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/amg/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [代数的マルチグリッド（AMG）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja>)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [行列から粗視化するAMG：残差と解誤差を分ける](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja>)
  availability: run

  正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。
- [代数的マルチグリッド（AMG）：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
