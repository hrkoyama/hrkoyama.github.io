# H₂分子の閉殻HF：独立参照・SCF残差・基底の収束

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/h2-hf/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Hartree–Fock法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [電子状態計算の基底](<https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [自己無撞着場反復（SCF）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [配置間相互作用（CI）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [Hartree–Fock法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja>)
- [電子状態計算の基底](<https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=ja>)
- [自己無撞着場反復（SCF）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja>)

## 方程式

- [閉殻Hartree–Fock方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja>)

  閉殻RHFの占有空間軌道の式で、非局所交換を含む。既存のHe局所還元とH2のRHF例を保持する。追加は固定H2/H3+の最小2電子模型で、UHF式は別の対応模型に明示する。一般多中心分子、開殻の大域安定性、完全基底や一般相関法の保証ではない。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [電子の定常Schrödinger方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja>)

  固定核・非相対論の電子固有値問題。核間反発は電子Hamiltonianの外に加える。従来の水素型動径例を保持し、追加は1次元の箱/HOと3AO以下の2電子FCIに限定する。一般多電子系の直接解法や連続空間の厳密分子解の検証ではない。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [最小2電子模型のスピン非制限HF](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#unrestricted-hartree-fock-model-ja>)

  2固定距離のみ。有限基底FCIは連続空間の厳密解ではなく、UHF定常解の一般的な大域最小性は保証しません。角運動量・完全基底・広い解離曲線は未検証。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-h2-rhf-ja>)

  孤立2電子RHF・有限s型Gaussian基底。数値収束とRHF近似の誤差は別。
- [閉殻Hartree–Fock方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja>)

  閉殻RHFの占有空間軌道の式で、非局所交換を含む。既存のHe局所還元とH2のRHF例を保持する。追加は固定H2/H3+の最小2電子模型で、UHF式は別の対応模型に明示する。一般多中心分子、開殻の大域安定性、完全基底や一般相関法の保証ではない。

## 問題の図

- [H₂分子RHF：独立参照・SCF・s型基底拡大](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png

## 厳密解・参照解

- [H₂分子RHF：独立参照・SCF・s型基底拡大：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#references-ja>)

  小さな固定H₂モデルの独立RHF参照とSCF・s型基底の検査を使います。有限基底RHFの一致は完全な電子相関を含む厳密分子解の一致ではありません。
- [最小基底H2のRHF/UHF/FCI・2固定幾何](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-h2-rhf-uhf-fci-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 H-H距離1.4/3.0bohr、2電子、HごとにSTO-3G縮約s軌道を1個用います。 核間距離1.4/3.0bohr、全エネルギーhartree。各Hに同じ明示3primitiveのs型収縮を1つ置く2AO/2電子の固定部分空間。 2固定距離のみ。有限基底FCIは連続空間の厳密解ではなく、UHF定常解の一般的な大域最小性は保証しません。角運動量・完全基底・広い解離曲線は未検証。
- [H₂分子RHF：独立参照・SCF・s型基底拡大：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=ja#h2-rhf-ja-validation>)

  教育用コードをimportしない独立PySCF。同一幾何・同一有限基底のRHFであり、相関を含む厳密解ではありません。
- [最小基底H2のRHF/UHF/FCI・2固定幾何](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-h2-rhf-uhf-fci-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 H-H距離1.4/3.0bohr、2電子、HごとにSTO-3G縮約s軌道を1個用います。 核間距離1.4/3.0bohr、全エネルギーhartree。各Hに同じ明示3primitiveのs型収縮を1つ置く2AO/2電子の固定部分空間。 2固定距離のみ。有限基底FCIは連続空間の厳密解ではなく、UHF定常解の一般的な大域最小性は保証しません。角運動量・完全基底・広い解離曲線は未検証。

## コード・検証

- [H₂分子RHF：独立参照・SCF・s型基底拡大](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=ja>)
  availability: run

  孤立・Born–Oppenheimer・非相対論・2電子閉殻H₂。3核間距離でSTO-3Gと入れ子s型Gaussian基底を比較。RHFの数値検証であり、分子DFT・周期系・完全基底極限や正しい解離を検証しない。
- [最小基底H2のRHF/UHF/FCI・2固定幾何](<https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja>)
  availability: run

  同じ最小基底H2の2固定幾何で、RHF/UHF/有限基底FCIとスピン対称性を比較します。
- [H₂分子RHF：独立参照・SCF・s型基底拡大：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
