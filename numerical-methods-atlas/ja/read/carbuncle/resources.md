# カーバンクル現象

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/carbuncle/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Roe法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/roe/?lang=ja>)

  保存された垂直衝撃波診断の流束とRoe音響エントロピー平滑化です。圧力センサー混合法をRotated-RHLLと同一視しません。
- [Roe音響波のエントロピー修正](<https://hrkoyama.github.io/numerical-methods-atlas/methods/entropy-fix/?lang=ja>)

  保存された垂直衝撃波診断の流束とRoe音響エントロピー平滑化です。圧力センサー混合法をRotated-RHLLと同一視しません。
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja>)

  保存された垂直衝撃波診断の流束とRoe音響エントロピー平滑化です。圧力センサー混合法をRotated-RHLLと同一視しません。
- [HLLE／Einfeldt波速](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=ja>)

  保存された垂直衝撃波診断の流束とRoe音響エントロピー平滑化です。圧力センサー混合法をRotated-RHLLと同一視しません。
- [AUSM系列の流束分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ausm/?lang=ja>)

  保存された垂直衝撃波診断の流束とRoe音響エントロピー平滑化です。圧力センサー混合法をRotated-RHLLと同一視しません。

## 方程式

- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

## 問題の図

- [定常平面衝撃波のodd–even診断](<https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-methods/planar-128-0.png

## 厳密解・参照解

- [定常平面衝撃波のodd–even診断：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja#references-ja>)

  Mach-6定常垂直衝撃波の解析的下流状態と、種を与えた行デカップリング指標・無擾乱対照を比較します。一般的な横方向不安定性全体の検証ではありません。

## コード・検証

章固有の対応は未登録です。全体一覧：[コード・入力・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja)
