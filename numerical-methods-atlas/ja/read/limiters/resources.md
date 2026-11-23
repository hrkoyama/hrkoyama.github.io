# 勾配制限：minmod、Superbee、MC、van Leer、van Albada

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/limiters/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja>)
- [Superbee](<https://hrkoyama.github.io/numerical-methods-atlas/methods/superbee/?lang=ja>)
- [単調中心勾配制限／MC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=ja>)
- [Van Leer勾配制限](<https://hrkoyama.github.io/numerical-methods-atlas/methods/van-leer/?lang=ja>)
- [切り詰めたVan Albada勾配制限](<https://hrkoyama.github.io/numerical-methods-atlas/methods/van-albada/?lang=ja>)
- [3次Hermite CIP](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cip/?lang=ja>)

  保存済みCIPおよびリミター比較の矩形波ケースで使われる手法です。
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)

  保存済みCIPおよびリミター比較の矩形波ケースで使われる手法です。
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja>)

  保存済みCIPおよびリミター比較の矩形波ケースで使われる手法です。
- [Superbee](<https://hrkoyama.github.io/numerical-methods-atlas/methods/superbee/?lang=ja>)

  保存済みCIPおよびリミター比較の矩形波ケースで使われる手法です。
- [単調中心勾配制限／MC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=ja>)

  保存済みCIPおよびリミター比較の矩形波ケースで使われる手法です。
- [Van Leer勾配制限](<https://hrkoyama.github.io/numerical-methods-atlas/methods/van-leer/?lang=ja>)

  保存済みCIPおよびリミター比較の矩形波ケースで使われる手法です。
- [切り詰めたVan Albada勾配制限](<https://hrkoyama.github.io/numerical-methods-atlas/methods/van-albada/?lang=ja>)

  保存済みCIPおよびリミター比較の矩形波ケースで使われる手法です。
- [風上差分（upwind）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja>)

  保存済みCIPおよびリミター比較の矩形波ケースで使われる手法です。
- [TVB修正minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/tvb/?lang=ja>)

  保存済みCIPおよびリミター比較の矩形波ケースで使われる手法です。

## 方程式

- [線形移流](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja>)

  一定速度aによる輸送。波形の移動、数値拡散、安定性へ。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

## 問題の図

- [周期矩形波の線形移流](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-square.png

## 厳密解・参照解

- [周期矩形波の線形移流：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=ja#references-ja>)

  矩形波を周期的に平行移動した不連続解が基準です。参照解一覧の正弦波は同じ移流モデルの別初期値です。
- [移流／正弦波の平行移動](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 単位区間の周期境界、一定移流速度1。 方程式と周期輸送は共通ですが、参照カードは滑らかな正弦初期値であり、この矩形初期値の参照値ではありません。

## コード・検証

- [Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja>)
  availability: run

  初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。
- [Minmod：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Superbee：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/superbee/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [単調中心勾配制限／MC：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Van Leer勾配制限：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/van-leer/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [切り詰めたVan Albada勾配制限：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/van-albada/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
