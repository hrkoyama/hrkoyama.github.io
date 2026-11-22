# Gauss求積・適応積分

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quadrature/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Gauss求積・適応積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja>)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=ja>)
  availability: run

  Legendreの3項漸化式からGauss節点と重みを構成し、2n−1次までの多項式モーメントと指数関数を検査します。適応Simpsonは指数関数とLorentz型ピークを積分し、解析積分・独立QUADPACKと比較します。
- [求積：狭いピーク・相殺・端点・誤差推定の盲点](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja>)
  availability: run

  Gauss次数と適応公差を走査し、狭いLorentzピーク、平方根端点、巨大な相殺、零積分、見逃すcompact bumpを解析積分とQUADPACKで検証します。
- [Gauss求積・適応積分：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
