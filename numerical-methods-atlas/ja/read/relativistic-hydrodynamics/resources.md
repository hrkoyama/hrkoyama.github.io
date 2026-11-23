# 相対論的流体力学：SRHD、GRHD、GRMHD

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/relativistic-hydrodynamics/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

章固有の対応は未登録です。全体一覧：[手法・コードの対応表](https://hrkoyama.github.io/numerical-methods-atlas/methods/?lang=ja)

## 方程式

- [特殊相対論的流体（SRHD）](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srhd-ja>)

  c=1、平坦なCartesian時空の理想流体。γ則EOSと原始変数回復を使う穏やかな対称二衝撃波の固定例を追加。一般三波Riemann解、極端なLorentz因子、一般相対論を検証したとはしません。
- [一般相対論的流体（GRHD）](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#grhd-ja>)

  c=G=1、計量符号(−,+,+,+)の理想流体。背景計量を固定する場合と、Einstein方程式も解く場合を区別します。文献解説のみ。
- [一般相対論的MHD（GRMHD）](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#grmhd-ja>)

  理想電気伝導の代表形。物質と電磁場の応力エネルギー、磁場制約、計量を組み合わせます。状態方程式・時空の扱いを含む完全系は解説先へ。文献解説のみ。
- [相対論的放射モーメント・M1](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#m1-radiation-ja>)

  Gνを物質が受け取る四元力と定義した模式形。Rは放射の応力エネルギー、Pは放射圧テンソル。M1は角度モーメントの閉包で、放射分布全体を厳密に解くものではありません。文献解説のみ。
- [因果的な相対論的粘性流体](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#causal-viscous-ja>)

  下段はIsrael–Stewart型の緩和を示す模式式で、完全な構成則ではありません。追加緩和変数を使わないBDNKなどの一階理論と区別します。因果性の条件は理論・状態方程式に依存し、文献解説のみです。

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

章固有の対応は未登録です。全体一覧：[コード・入力・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja)
