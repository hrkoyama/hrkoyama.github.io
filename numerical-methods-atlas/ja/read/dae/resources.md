# 微分代数方程式（DAE）

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/dae/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [微分代数方程式（DAE）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=ja>)

## 方程式

- [半陽的index-1 DAE](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#index-one-dae-ja>)

  整合初期化と微分・代数残差を扱う小規模な固定例です。一般DAEソルバーの完成を意味しません。
- [拘束付き平面振り子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#constrained-pendulum-ja>)

  元の位置拘束DAE、微分した拘束に基づくODE、SHAKE/RATTLEの離散写像を区別します。

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [Robertson保存制約DAEと公式IDA保存値](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja>)
  availability: run

  Robertsonの保存制約DAEと全ODEを同じ固定時間格子で比較し、公式IDA保存値を別に照合します。 初回は元の時間精度・細分化目標4件が未達でした。
- [index-1 DAEの整合初期化と離散残差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja>)
  availability: run

  既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。
- [振り子の指数低減・拘束ドリフト・明示安定化](<https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja>)
  availability: run

  位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。
- [微分代数方程式（DAE）：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
