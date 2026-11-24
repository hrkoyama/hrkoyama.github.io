# 自動微分：数値ソルバーのための微分計算

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/automatic-differentiation/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [自動微分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja>)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja>)
  availability: run

  非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。
- [独自逆モードVJPとJVP/VJP双対性](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=ja>)
  availability: run

  重複gatherとbroadcastを含む真の逆tapeを独立Jacobianと照合します。
- [HVPと状態固定・陰関数全微分の区別](<https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=ja>)
  availability: run

  forward-over-reverse HVPと二階陰関数則を別々の独立参照へ照合します。
- [非滑らか点・分岐・停止条件の微分範囲](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=ja>)
  availability: run

  古典微分・一方向微分・実行trace微分を、kinkと停止分岐の固定例で区別します。
- [自動微分：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
