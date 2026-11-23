# WENOの臨界点・ε依存性

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-weno-critical/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [WENO5-JS](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=ja>)
- [有限差分WENO5-Z](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=ja>)
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja#weno-critical-epsilon-ja-algorithm>)

  3候補と線形重み(.1,.6,.3)、Jiang–Shu指標を共通にし、JSはd/(β+ε)²、Zはd[1+(|β₀−β₂|/(β+ε))²]を正規化します。ε=10⁻⁴⁰,10⁻⁶,h²です。輸送は共有風上面流束と古典RK4、Courant.1を使い、状態クリップ・再試行を行いません。
- [線形移流](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja>)

  一定速度aによる輸送。波形の移動、数値拡散、安定性へ。

## 問題の図

- [WENO-JS／Z：臨界点とεの固定比較](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/results/weno-critical-epsilon.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/results/weno-critical-epsilon.png

## 厳密解・参照解

- [WENO臨界点：多項式セル平均と解析的周期輸送](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-weno-critical-profile-ja>)
  reference_kind: analytic

  解析解 局所参照はx=0を中心とする5セルの解析平均からh/2を評価する多項式です。通常・一次・二次臨界の3形、h=1/64…1/512を区別します。実際の周期輸送参照は[0,1]、速度1、T1、q₀=cos(2πx)+.1sin³(2πx)のFourier積分セル平均で、別のGauss12点関数求積と照合します。局所多項式と輸送の初期形は異なり、点値や別PDE計算の参照ではありません。
- [WENO-JS／Z：臨界点とεの固定比較：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja#weno-critical-epsilon-ja-validation>)

  実行前契約で72局所再構成・24PDE計算・36pytestを固定します。解析セル平均を独立Gauss12求積と照合し、局所の誤差・重み、輸送のL1/L2/L∞・質量・全段有限性・中間時刻と保存流束を記録します。最細格子で6通りの刻み半減差が対応する連続解誤差の10%以下か確認します。
- [移流／正弦波の平行移動](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 単位区間の周期境界、一定移流速度1。 同じ周期・速度1の正弦移流モデルです。参照一覧は振幅0.25、共通固定入力は0.2で、DG・CIP等の表現や時間も異なります。
- [WENO臨界点：多項式セル平均と解析的周期輸送](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-weno-critical-profile-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 局所参照はx=0を中心とする5セルの解析平均からh/2を評価する多項式です。通常・一次・二次臨界の3形、h=1/64…1/512を区別します。実際の周期輸送参照は[0,1]、速度1、T1、q₀=cos(2πx)+.1sin³(2πx)のFourier積分セル平均で、別のGauss12点関数求積と照合します。局所多項式と輸送の初期形は異なり、点値や別PDE計算の参照ではありません。 同じ一定速度の周期移流に対する追加参照ですが、cos+.1sin³のセル平均と局所臨界多項式は、従来の単一正弦・CIP表示と異なります。

## コード・検証

- [WENO-JS／Z：臨界点とεの固定比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja>)
  availability: run

  同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。
