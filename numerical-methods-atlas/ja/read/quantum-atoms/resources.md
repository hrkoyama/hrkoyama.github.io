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

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [Schrödinger固有値問題](<https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja>)
- [Hartree–Fock法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja>)
- [Kohn–Sham密度汎関数法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja>)
- [自己無撞着場反復（SCF）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja>)
- [Coulomb・Hartreeポテンシャル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-poisson/?lang=ja>)
- [LDA・GGA・hybrid汎関数](<https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=ja>)

## 方程式

- [電子の定常Schrödinger方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja>)

  固定核・非相対論の電子固有値問題。核間反発は電子Hamiltonianの外に加える。従来の水素型動径例を保持し、追加は1次元の箱/HOと3AO以下の2電子FCIに限定する。一般多電子系の直接解法や連続空間の厳密分子解の検証ではない。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [閉殻Hartree–Fock方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja>)

  閉殻RHFの占有空間軌道の式で、非局所交換を含む。既存のHe局所還元とH2のRHF例を保持する。追加は固定H2/H3+の最小2電子模型で、UHF式は別の対応模型に明示する。一般多中心分子、開殻の大域安定性、完全基底や一般相関法の保証ではない。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [局所Kohn–Sham DFT](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja>)

  密度汎関数の局所KS代表形です。公開例は、球対称Heのスピン非偏極・Dirac交換のみLDAと、固定した周期He／He₂セルのLDA交換＋VWN5相関です。原子の動径実装と周期PySCFワークフローは別系列で、基底・境界条件・参照も異なります。各例の範囲は下の固定入力・検証記録で確認してください。GGA・hybrid・一般物質・励起状態まで検証した意味ではありません。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [電子の定常Schrödinger方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja>)

  固定核・非相対論の電子固有値問題。核間反発は電子Hamiltonianの外に加える。従来の水素型動径例を保持し、追加は1次元の箱/HOと3AO以下の2電子FCIに限定する。一般多電子系の直接解法や連続空間の厳密分子解の検証ではない。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-hydrogenic-atoms-ja>)

  原子単位の1電子・定常動径問題。計算は有限半径箱の零Dirichlet境界を使い、無限領域の水素型解析解と比較する。一般多電子・分子・周期系の解法を意味しない。
- [電子の定常Schrödinger方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja>)

  固定核・非相対論の電子固有値問題。核間反発は電子Hamiltonianの外に加える。従来の水素型動径例を保持し、追加は1次元の箱/HOと3AO以下の2電子FCIに限定する。一般多電子系の直接解法や連続空間の厳密分子解の検証ではない。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-helium-ground-state-ja>)

  孤立・球対称・閉殻1s²に限定した原子単位の動径式。RHFのvH/2は2電子同一空間軌道に特有。LDAは交換のみで相関なし。UHF、GGA、hybrid、一般分子・周期DFTの実行例ではない。
- [閉殻Hartree–Fock方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja>)

  閉殻RHFの占有空間軌道の式で、非局所交換を含む。既存のHe局所還元とH2のRHF例を保持する。追加は固定H2/H3+の最小2電子模型で、UHF式は別の対応模型に明示する。一般多中心分子、開殻の大域安定性、完全基底や一般相関法の保証ではない。
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

  水素型原子の解析的な固有エネルギー・軌道と比較し、有限半径打切りと格子誤差を分けます。既存の固定入力・保存結果を参照します。 既存の固定入力・保存結果に対応する解析参照カードを追加。解析式、点・時刻・動径の標本化、配布版SHAと実行コードを相互に辿れます。過去の計算を再実行した記録ではありません。
- [水素型原子：解析解と格子収束](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-hydrogenic-coulomb-reference-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 非相対論・無限質量の点核。核電荷Z=1,2。縮約動径軌道を一様格子の2次中心差分で離散化。 既存の固定入力・保存結果に対応する解析参照カードを追加。解析式、点・時刻・動径の標本化、配布版SHAと実行コードを相互に辿れます。過去の計算を再実行した記録ではありません。
- [H/Heの式・密度・固定参照カード](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-atomic-reference-cards-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。 参照カードの整備・保存値照合であり、新SCF/新独立参照は0回。相関込み厳密He、完全基底極限、全軌道の再実行は主張しません。
- [He基底状態：閉殻HF・交換のみLDA：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#references-ja>)

  閉殻HF・交換のみLDAの独立参照、SCF残差・電子数・格子収束を確認します。近似汎関数の解を厳密なHe多体解とは呼びません。
- [H/Heの式・密度・固定参照カード](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-atomic-reference-cards-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。 参照カードの整備・保存値照合であり、新SCF/新独立参照は0回。相関込み厳密He、完全基底極限、全軌道の再実行は主張しません。
- [水素型原子：解析解と格子収束](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-hydrogenic-coulomb-reference-ja>)
  reference_kind: analytic

  解析解 非相対論・無限質量の点核。核電荷Z=1,2。縮約動径軌道を一様格子の2次中心差分で離散化。
- [水素型原子：解析解と格子収束：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=ja#hydrogenic-atoms-ja-validation>)

  E_n=−Z²/(2n²)とLaguerre動径解。有限格子の誤差と箱の誤差を分ける。
- [水素型原子：解析解と格子収束](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-hydrogenic-coulomb-reference-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 非相対論・無限質量の点核。核電荷Z=1,2。縮約動径軌道を一様格子の2次中心差分で離散化。 既存の固定入力・保存結果に対応する解析参照カードを追加。解析式、点・時刻・動径の標本化、配布版SHAと実行コードを相互に辿れます。過去の計算を再実行した記録ではありません。
- [H/Heの式・密度・固定参照カード](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-atomic-reference-cards-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。 参照カードの整備・保存値照合であり、新SCF/新独立参照は0回。相関込み厳密He、完全基底極限、全軌道の再実行は主張しません。
- [He：閉殻HF・交換のみLDA：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=ja#helium-ground-state-ja-validation>)

  PySCF 2.11.0 / LibxcのGaussian基底参照。外挿値・有限格子値・参照を区別。参照scriptの再実行は今回の共通runnerの測定に含まない。
- [H/Heの式・密度・固定参照カード](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-atomic-reference-cards-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。 参照カードの整備・保存値照合であり、新SCF/新独立参照は0回。相関込み厳密He、完全基底極限、全軌道の再実行は主張しません。

## コード・検証

- [水素型原子：解析解と格子収束](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=ja>)
  availability: run

  孤立した1電子のH・He⁺について、1s・2s・2p・3dのエネルギーと動径軌道を解析解と比較します。多電子原子や分子の直接解法ではありません。
- [He：閉殻HF・交換のみLDA](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=ja>)
  availability: run

  Heの球対称1s²・閉殻HFとスピン非偏極Dirac交換のみLDAを比較します。電子相関・分子・周期系は含みません。
- [H/Heの式・密度・固定参照カード](<https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja>)
  availability: run

  既存H/Heの式と保存参照を、単位・規格化・模型の限界とともに示します。
- [水素型原子の動径固有値問題：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
- [He基底状態：閉殻HF・交換のみLDA：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
