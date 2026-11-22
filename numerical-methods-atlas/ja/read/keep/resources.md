# KEEP法：滑らかな流れの釣合いと限界を検証する

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/keep/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [直交座標の原KEEP分割流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/keep/?lang=ja>)
- [直交座標の原KEEP分割流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/keep/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

## 方程式

- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

## 問題の図

- [周期移動等エントロピー渦](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/keep-vortex/frame-080.webp

## 厳密解・参照解

- [周期移動等エントロピー渦：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja#references-ja>)

  滑らかな周期等エントロピー渦の解析的移動解と格子・時間刻みの収束を確認します。非圧縮Taylor–Green渦の参照式とは別問題です。

## コード・検証

- [直交座標の原KEEP分割流束：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/keep/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
