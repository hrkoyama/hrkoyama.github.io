# Gauss求積・適応積分

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quadrature/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Gauss求積・適応積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja>)
- [Gauss–Kronrod G7/K15](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gauss-kronrod/?lang=ja>)
- [tanh–sinh二重指数求積](<https://hrkoyama.github.io/numerical-methods-atlas/methods/tanh-sinh/?lang=ja>)
- [Smolyak疎格子求積](<https://hrkoyama.github.io/numerical-methods-atlas/methods/smolyak-sparse-grid/?lang=ja>)

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
- [領域別QUADPACKと有限Simpson対照](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=ja>)
  availability: run

  15本の特殊化求積と15本のSimpson対照を固定入力で比較します。
- [G7/K15と有限区間tanh-sinh](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja>)
  availability: run

  9本の適応GKと24本の固定DE和を比較します。
- [2〜4次元テンソル・Smolyak対照](<https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja>)
  availability: run

  滑らかな積と相互作用積の42本の固定cubatureを比較します。
- [Gauss求積・適応積分：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Gauss–Kronrod G7/K15：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gauss-kronrod/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [tanh–sinh二重指数求積：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/tanh-sinh/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Smolyak疎格子求積：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/smolyak-sparse-grid/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
