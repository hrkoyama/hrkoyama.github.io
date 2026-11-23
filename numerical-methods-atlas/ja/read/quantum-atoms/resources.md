# 水素型原子とHe：実行・検証例

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-atoms/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Schrödinger固有値問題](<https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [Hartree–Fock法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [Kohn–Sham密度汎関数法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [自己無撞着場反復（SCF）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [Coulomb・Hartreeポテンシャル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-poisson/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [LDA・GGA・hybrid汎関数](<https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [Schrödinger固有値問題](<https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja>)
- [Hartree–Fock法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja>)
- [Kohn–Sham密度汎関数法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja>)
- [自己無撞着場反復（SCF）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja>)
- [Coulomb・Hartreeポテンシャル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-poisson/?lang=ja>)
- [LDA・GGA・hybrid汎関数](<https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=ja>)

## 方程式

- [電子の定常Schrödinger方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja>)

  固定核・非相対論の電子多体固有値問題。核間反発は電子Hamiltonianの外に加える。実行例は1電子の孤立水素型原子に限定。一般の多電子直接解法は未実装。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [閉殻Hartree–Fock方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja>)

  閉殻RHFの占有空間軌道の式で、一般に非局所な交換を含みます。公開例は、球対称1s² Heの局所還元と、別の分子積分実装による固定入力のH₂ RHFです。原子例と分子例では基底・離散化・参照が異なります。各例の範囲は下の固定入力・検証記録で確認してください。一般多中心分子・開殻・相関を含む解法の検証ではありません。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [局所Kohn–Sham DFT](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja>)

  密度汎関数の局所KS代表形です。公開例は、球対称Heのスピン非偏極・Dirac交換のみLDAと、固定した周期He／He₂セルのLDA交換＋VWN5相関です。原子の動径実装と周期PySCFワークフローは別系列で、基底・境界条件・参照も異なります。各例の範囲は下の固定入力・検証記録で確認してください。GGA・hybrid・一般物質・励起状態まで検証した意味ではありません。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-hydrogenic-atoms-ja>)

  原子単位の1電子・定常動径問題。計算は有限半径箱の零Dirichlet境界を使い、無限領域の水素型解析解と比較する。一般多電子・分子・周期系の解法を意味しない。
- [電子の定常Schrödinger方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja>)

  固定核・非相対論の電子多体固有値問題。核間反発は電子Hamiltonianの外に加える。実行例は1電子の孤立水素型原子に限定。一般の多電子直接解法は未実装。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-helium-ground-state-ja>)

  孤立・球対称・閉殻1s²に限定した原子単位の動径式。RHFのvH/2は2電子同一空間軌道に特有。LDAは交換のみで相関なし。UHF、GGA、hybrid、一般分子・周期DFTの実行例ではない。
- [閉殻Hartree–Fock方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja>)

  閉殻RHFの占有空間軌道の式で、一般に非局所な交換を含みます。公開例は、球対称1s² Heの局所還元と、別の分子積分実装による固定入力のH₂ RHFです。原子例と分子例では基底・離散化・参照が異なります。各例の範囲は下の固定入力・検証記録で確認してください。一般多中心分子・開殻・相関を含む解法の検証ではありません。
- [局所Kohn–Sham DFT](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja>)

  密度汎関数の局所KS代表形です。公開例は、球対称Heのスピン非偏極・Dirac交換のみLDAと、固定した周期He／He₂セルのLDA交換＋VWN5相関です。原子の動径実装と周期PySCFワークフローは別系列で、基底・境界条件・参照も異なります。各例の範囲は下の固定入力・検証記録で確認してください。GGA・hybrid・一般物質・励起状態まで検証した意味ではありません。

## 問題の図

- [水素型原子の動径固有値問題](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/hydrogenic.png
- [He基底状態：閉殻HF・交換のみLDA](<https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png

## 厳密解・参照解

- [水素型原子の動径固有値問題：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja#references-ja>)

  水素型原子の解析的な固有エネルギー・軌道と比較し、有限半径打切りと格子誤差を分けます。既存の固定入力・保存結果を参照します。
- [He基底状態：閉殻HF・交換のみLDA：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#references-ja>)

  閉殻HF・交換のみLDAの独立参照、SCF残差・電子数・格子収束を確認します。近似汎関数の解を厳密なHe多体解とは呼びません。
- [水素型原子：解析解と格子収束：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=ja#hydrogenic-atoms-ja-validation>)

  E_n=−Z²/(2n²)とLaguerre動径解。有限格子の誤差と箱の誤差を分ける。
- [He：閉殻HF・交換のみLDA：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=ja#helium-ground-state-ja-validation>)

  PySCF 2.11.0 / LibxcのGaussian基底参照。外挿値・有限格子値・参照を区別。参照scriptの再実行は今回の共通runnerの測定に含まない。

## コード・検証

- [水素型原子：解析解と格子収束](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=ja>)
  availability: run

  孤立した1電子のH・He⁺について、1s・2s・2p・3dのエネルギーと動径軌道を解析解と比較します。多電子原子や分子の直接解法ではありません。
- [He：閉殻HF・交換のみLDA](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=ja>)
  availability: run

  Heの球対称1s²・閉殻HFとスピン非偏極Dirac交換のみLDAを比較します。電子相関・分子・周期系は含みません。
- [水素型原子の動径固有値問題：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
- [He基底状態：閉殻HF・交換のみLDA：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
