# Smooth PME（SPME）

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/spme/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Smooth PME（SPME）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=ja>)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [Bスプラインsmooth PMEの格子・次数収束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=ja>)
  availability: run

  電荷をBスプラインで格子へ割り当て、FFTでEwald逆空間項を評価するsmooth PME（SPME）の小規模例です。
- [SPME：格子・補間次数・格子位相と保存則](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=ja>)
  availability: run

  BスプラインSPMEを同じ独立theta参照へ照合し、格子・次数・位相への依存、電荷の保持、エネルギー勾配と合力を測ります。
- [Smooth PME（SPME）：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
