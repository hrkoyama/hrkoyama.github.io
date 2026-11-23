# DFTから原子間力へ：有限差分・独立参照・力の収束とBOMDへの接続

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/periodic-forces/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Kohn–Sham密度汎関数法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [電子状態計算の基底](<https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [自己無撞着場反復（SCF）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [LDA・GGA・hybrid汎関数](<https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [擬ポテンシャル・PAW](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [周期電子状態とk点](<https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [Kohn–Sham密度汎関数法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja>)
- [電子状態計算の基底](<https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=ja>)
- [自己無撞着場反復（SCF）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja>)
- [LDA・GGA・hybrid汎関数](<https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=ja>)
- [擬ポテンシャル・PAW](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=ja>)
- [周期電子状態とk点](<https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=ja>)

## 方程式

- [局所Kohn–Sham DFT](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja>)

  密度汎関数の局所KS代表形です。公開例は、球対称Heのスピン非偏極・Dirac交換のみLDAと、固定した周期He／He₂セルのLDA交換＋VWN5相関です。原子の動径実装と周期PySCFワークフローは別系列で、基底・境界条件・参照も異なります。各例の範囲は下の固定入力・検証記録で確認してください。GGA・hybrid・一般物質・励起状態まで検証した意味ではありません。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-periodic-he-forces-ja>)

  非対称な2原子He周期セル・局所GTH・LDA交換＋VWN5。PySCFの解析力（Gaussian基底の微分を含む）を全6座標のエネルギー有限差分とDFTK平面波参照で照合し、力の基底・k点・SCF・FFT収束を分離。BOMDの力供給と短い刻み比較に限定し、長時間NVE・CPMD・一般物質は未検証。
- [局所Kohn–Sham DFT](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja>)

  密度汎関数の局所KS代表形です。公開例は、球対称Heのスピン非偏極・Dirac交換のみLDAと、固定した周期He／He₂セルのLDA交換＋VWN5相関です。原子の動径実装と周期PySCFワークフローは別系列で、基底・境界条件・参照も異なります。各例の範囲は下の固定入力・検証記録で確認してください。GGA・hybrid・一般物質・励起状態まで検証した意味ではありません。

## 問題の図

- [周期He₂の原子間力：解析力・有限差分・BOMD接続](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/preview.png

## 厳密解・参照解

- [周期He₂の原子間力：解析力・有限差分・BOMD接続：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja#references-ja>)

  固定He₂配置のエネルギー有限差分と解析力、独立DFTK参照と保存された収束検査を区別します。長時間の第一原理MD精度を認定するものではありません。
- [周期He₂の原子間力：解析力・有限差分・BOMD接続：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=ja#periodic-he-forces-ja-validation>)

  独立DFTK平面波計算：Γ／2³の解析力、8カットオフ設定、全6座標のエネルギー有限差分。共通Libxcと異なる有限基底の制約を明記。

## コード・検証

- [周期He₂の原子間力：解析力・有限差分・BOMD接続](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=ja>)
  availability: run

  非対称な2原子He周期セル・局所GTH・LDA交換＋VWN5。PySCFの解析力（Gaussian基底の微分を含む）を全6座標のエネルギー有限差分とDFTK平面波参照で照合し、力の基底・k点・SCF・FFT収束を分離。BOMDの力供給と短い刻み比較に限定し、長時間NVE・CPMD・一般物質は未検証。
- [周期He₂の原子間力：解析力・有限差分・BOMD接続：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
