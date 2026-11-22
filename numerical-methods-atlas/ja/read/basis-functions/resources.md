# 直交多項式と格子上の基底関数

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/basis-functions/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Legendreモード基底・正規直交化](<https://hrkoyama.github.io/numerical-methods-atlas/methods/legendre-basis/?lang=ja>)
- [Lagrange節点基底・GLL選点法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nodal-basis/?lang=ja>)
- [Legendreモード基底・正規直交化](<https://hrkoyama.github.io/numerical-methods-atlas/methods/legendre-basis/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [Lagrange節点基底・GLL選点法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nodal-basis/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [Legendreモード基底・正規直交化](<https://hrkoyama.github.io/numerical-methods-atlas/methods/legendre-basis/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Lagrange節点基底・GLL選点法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nodal-basis/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-smooth-function-projection-ja>)

  重み1の区間射影とGLL節点補間で、PDEではない。32点求積による射影を、別のLegendre再帰式と64/96点求積で調べる。実行例の式は46モデルの件数に足さない。

## 問題の図

- [滑らかな関数の多項式補間・射影](<https://hrkoyama.github.io/numerical-methods-atlas/problems/smooth-function-projection/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/smooth-function-projection.png
- [不連続関数の多項式補間・射影](<https://hrkoyama.github.io/numerical-methods-atlas/problems/jump-function-projection/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/jump-function-projection.png

## 厳密解・参照解

- [滑らかな関数の多項式補間・射影：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/smooth-function-projection/?lang=ja#references-ja>)

  指定された滑らかな対象関数の既知値を基準に、Legendre射影・節点補間の誤差を比較します。方程式を解いたデータではありません。
- [不連続関数の多項式補間・射影：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/jump-function-projection/?lang=ja#references-ja>)

  指定された段差関数の既知値と比較し、射影・補間の振動と収束を確認します。滑らかな関数の誤差評価とは区別します。
- [滑らかな関数：Legendre射影とGLL補間：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/smooth-function-projection/?lang=ja#smooth-function-projection-ja-validation>)

  CSVは次数ごとに201点、各行で射影値・GLL補間値・exp(x)を整列。次数別L2誤差、係数差、直交性残差、64/96点求積の差はJSONに記録する。

## コード・検証

- [滑らかな関数：Legendre射影とGLL補間](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/smooth-function-projection/?lang=ja>)
  availability: run

  exp(x)を次数2/4/6/8でL2射影し、同じ次数のGLL節点補間と比較する。実装の32点Gaussとは別の64/96点求積と独立Legendre再帰式で係数・直交性・誤差を確認する。
- [Legendreモード基底・正規直交化：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/legendre-basis/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Lagrange節点基底・GLL選点法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nodal-basis/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
