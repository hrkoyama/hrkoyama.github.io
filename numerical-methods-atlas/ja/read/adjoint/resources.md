# 陰関数微分と随伴法：Bratuのパラメータ感度

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/adjoint/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [陰関数微分・随伴法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=ja>)
- [自動微分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja>)
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [時間離散拡散の随伴とcheckpoint](<https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja>)
  availability: run

  後退Eulerの離散写像を実際に逆伝播し、接線・独立高精度mode解・block replayと比較します。
- [離散fold近傍のBratu感度](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja>)
  availability: run

  離散Bratuのfoldへ近づく6固定点で、状態誤差と線形許容差の影響を分け、独立shooting勾配と照合します。
- [分布係数Bratuの行列非形成VJP](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja>)
  availability: run

  2重みだけの局所hat作用で8/16/32個の空間係数を表し、目的関数ごとの随伴VJPを全感度参照と比較します。
- [陰関数微分・随伴法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
