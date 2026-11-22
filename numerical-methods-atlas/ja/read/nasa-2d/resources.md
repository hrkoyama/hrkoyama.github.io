# NASAの2次元検証・妥当性確認問題集

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/nasa-2d/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [単調中心勾配制限／MC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [単調中心勾配制限／MC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

## 方程式

- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

## 問題の図

- [15度楔の斜め衝撃波（Mach数の違いを統合）](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/wedge-m2-mc.png
- [Mach 3前向きステップ](<https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/step-m3-mc.png

## 厳密解・参照解

- [15度楔の斜め衝撃波（Mach数の違いを統合）：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja#references-ja>)

  斜め衝撃波の弱い枝に対する衝撃波角・状態比の解析関係と、格子収束を用います。Mach数別の条件は統合せず確認します。
- [Mach 3前向きステップ：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#references-ja>)

  段差回りの保存済み数値場・格子比較・時間履歴を参照します。この公開例に全場の厳密解は添付されていません。

## コード・検証

章固有の対応は未登録です。全体一覧：[コード・入力・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja)
