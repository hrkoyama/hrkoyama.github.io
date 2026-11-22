# 波追跡PPM、AUSM系と曲面前方の衝撃波

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/shock-expansion/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [制限付きPPM再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ppm/?lang=ja>)
- [AUSM系列の流束分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ausm/?lang=ja>)
- [制限付きPPM再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ppm/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [HLLC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hllc/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [HLLE／Einfeldt波速](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [AUSM系列の流束分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ausm/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Roe法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/roe/?lang=ja>)

  保存された曲面前方衝撃波の流束比較です。Rotated項目は方向別HLLE/Roeの教育用実験で、最適化Rotated-RHLLの完成検証ではありません。
- [HLLE／Einfeldt波速](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=ja>)

  保存された曲面前方衝撃波の流束比較です。Rotated項目は方向別HLLE/Roeの教育用実験で、最適化Rotated-RHLLの完成検証ではありません。
- [AUSM系列の流束分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ausm/?lang=ja>)

  保存された曲面前方衝撃波の流束比較です。Rotated項目は方向別HLLE/Roeの教育用実験で、最適化Rotated-RHLLの完成検証ではありません。
- [回転ハイブリッド・リーマンソルバー](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rotated-hybrid/?lang=ja>)

  保存された曲面前方衝撃波の流束比較です。Rotated項目は方向別HLLE/Roeの教育用実験で、最適化Rotated-RHLLの完成検証ではありません。

## 方程式

- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

## 問題の図

- [1次元の強い圧力ジャンプ](<https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/strong-shock.png
- [円柱前面の弓形衝撃波](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-expansion/forebody-48-0-density.png

## 厳密解・参照解

- [1次元の強い圧力ジャンプ：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/?lang=ja#references-ja>)

  この強い圧力段差の初期値を使った半解析的Riemann参照を保存しています。参照解一覧の標準Sodとは初期値が異なります。
- [円柱前面の弓形衝撃波：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/?lang=ja#references-ja>)

  曲面適合格子上の保存済み数値場、壁面圧力、2格子・擾乱ありなしの履歴が基準資料です。定常収束やカーバンクル消失の認定ではありません。

## コード・検証

- [制限付きPPM再構成：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ppm/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [AUSM系列の流束分割：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ausm/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
