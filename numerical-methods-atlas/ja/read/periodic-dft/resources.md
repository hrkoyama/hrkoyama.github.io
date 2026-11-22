# 周期DFT：Γ点・k点積分・基底・SCFと独立参照

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/periodic-dft/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Born–Oppenheimer分子動力学（BOMD）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=ja>)
- [カー–パリネロ法（CPMD）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=ja>)
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

  密度汎関数の局所KS代表形。実行例は球対称He・スピン非偏極Dirac交換のみLDA。相関・GGA・hybrid・一般化KS・周期系は未実装。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-periodic-he-dft-ja>)

  3次元周期・固定HeセルのKS-LDA。BZ積分メッシュとバンド経路、数値収束と物理近似を区別。
- [局所Kohn–Sham DFT](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja>)

  密度汎関数の局所KS代表形。実行例は球対称He・スピン非偏極Dirac交換のみLDA。相関・GGA・hybrid・一般化KS・周期系は未実装。

## 問題の図

- [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/preview.png

## 厳密解・参照解

- [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja#references-ja>)

  固定した小周期Heセルの独立DFTK参照・SCF・基底・k点の保存検査を使います。擬ポテンシャルと交換のみLDAのモデル範囲に限定します。
- [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=ja#periodic-he-dft-ja-validation>)

  別実行のDFTK平面波KS-LDA。Γ／2³で同一モデルを比較し、平面波打切り収束を保存。異なる有限軌道基底のため機械精度一致は要求しない。

## コード・検証

- [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=ja>)
  availability: run

  固定した1原子単純立方Heセル（格子定数4 bohr、価電子2、非偏極LDA_X＋VWN5、局所GTH）。PySCFを使う実行・検証ワークフロー。11設定でk点・Gaussian軌道基底・FFT補助格子・SCFを別々に比較し、Γ／2³は独立DFTK平面波参照と照合。平衡He結晶・完全基底・金属・一般物質は未検証。
- [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
