# 量子化学・DFT：何を近似し、何を解くか

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Schrödinger固有値問題](<https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja>)
- [電子状態計算の基底](<https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=ja>)
- [Hartree–Fock法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja>)
- [Kohn–Sham密度汎関数法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja>)
- [自己無撞着場反復（SCF）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja>)
- [Pulay / DIIS加速](<https://hrkoyama.github.io/numerical-methods-atlas/methods/diis/?lang=ja>)
- [Coulomb・Hartreeポテンシャル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-poisson/?lang=ja>)
- [LDA・GGA・hybrid汎関数](<https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=ja>)
- [擬ポテンシャル・PAW](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=ja>)
- [周期電子状態とk点](<https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=ja>)
- [バンド計算の対称群・既約表現](<https://hrkoyama.github.io/numerical-methods-atlas/methods/band-symmetry/?lang=ja>)
- [MP2摂動論](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mp2/?lang=ja>)
- [配置間相互作用（CI）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=ja>)
- [結合クラスター・CCSD(T)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/coupled-cluster/?lang=ja>)
- [CASSCF・多参照法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multireference/?lang=ja>)
- [時間依存DFT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/tddft/?lang=ja>)
- [量子Monte Carlo](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quantum-monte-carlo/?lang=ja>)
- [DMRG・テンソルネットワーク](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dmrg/?lang=ja>)

## 方程式

- [電子の定常Schrödinger方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja>)

  固定核・非相対論の電子固有値問題。核間反発は電子Hamiltonianの外に加える。従来の水素型動径例を保持し、追加は1次元の箱/HOと3AO以下の2電子FCIに限定する。一般多電子系の直接解法や連続空間の厳密分子解の検証ではない。
- [閉殻Hartree–Fock方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja>)

  閉殻RHFの占有空間軌道の式で、非局所交換を含む。既存のHe局所還元とH2のRHF例を保持する。追加は固定H2/H3+の最小2電子模型で、UHF式は別の対応模型に明示する。一般多中心分子、開殻の大域安定性、完全基底や一般相関法の保証ではない。
- [局所Kohn–Sham DFT](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja>)

  密度汎関数の局所KS代表形です。公開例は、球対称Heのスピン非偏極・Dirac交換のみLDAと、固定した周期He／He₂セルのLDA交換＋VWN5相関です。原子の動径実装と周期PySCFワークフローは別系列で、基底・境界条件・参照も異なります。各例の範囲は下の固定入力・検証記録で確認してください。GGA・hybrid・一般物質・励起状態まで検証した意味ではありません。
- [時間依存Kohn–Sham方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#time-dependent-kohn-sham-ja>)

  局所時間依存KSの代表形。初期状態、交換相関の記憶効果、断熱近似を区別する。実時間と線形応答の専用実装は未公開。

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [水素型原子：解析解と格子収束](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=ja>)
  availability: run

  孤立した1電子のH・He⁺について、1s・2s・2p・3dのエネルギーと動径軌道を解析解と比較します。多電子原子や分子の直接解法ではありません。
- [H/Heの式・密度・固定参照カード](<https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja>)
  availability: run

  既存H/Heの式と保存参照を、単位・規格化・模型の限界とともに示します。
- [1次元箱型井戸・量子調和振動子](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=ja>)
  availability: run

  1次元の箱と量子調和振動子で、低3固有対と有限領域・格子の影響を比較します。
- [3平面波の非局所projectorと有限温度占有](<https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja>)
  availability: run

  3平面波の小周期模型で、非局所projectorと有限温度占有・力を示します。
- [H₂分子RHF：独立参照・SCF・s型基底拡大](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=ja>)
  availability: run

  孤立・Born–Oppenheimer・非相対論・2電子閉殻H₂。3核間距離でSTO-3Gと入れ子s型Gaussian基底を比較。RHFの数値検証であり、分子DFT・周期系・完全基底極限や正しい解離を検証しない。
- [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=ja>)
  availability: run

  固定した1原子単純立方Heセル（格子定数4 bohr、価電子2、非偏極LDA_X＋VWN5、局所GTH）。PySCFを使う実行・検証ワークフロー。11設定でk点・Gaussian軌道基底・FFT補助格子・SCFを別々に比較し、Γ／2³は独立DFTK平面波参照と照合。平衡He結晶・完全基底・金属・一般物質は未検証。
- [周期He₂の原子間力：解析力・有限差分・BOMD接続](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=ja>)
  availability: run

  非対称な2原子He周期セル・局所GTH・LDA交換＋VWN5。PySCFの解析力（Gaussian基底の微分を含む）を全6座標のエネルギー有限差分とDFTK平面波参照で照合し、力の基底・k点・SCF・FFT収束を分離。BOMDの力供給と短い刻み比較に限定し、長時間NVE・CPMD・一般物質は未検証。
- [He：閉殻HF・交換のみLDA](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=ja>)
  availability: run

  Heの球対称1s²・閉殻HFとスピン非偏極Dirac交換のみLDAを比較します。電子相関・分子・周期系は含みません。
- [最小基底H2のRHF/UHF/FCI・2固定幾何](<https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja>)
  availability: run

  同じ最小基底H2の2固定幾何で、RHF/UHF/有限基底FCIとスピン対称性を比較します。
- [3中心H3+の小RHF/MP2/FCI模型](<https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja>)
  availability: run

  固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。
- [保存周期Heエネルギー・力の参照台帳](<https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja>)
  availability: run

  既存周期Heのエネルギーと6座標力を、保存参照と元の受入基準へ対応付けます。
- [Schrödinger固有値問題：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [電子状態計算の基底：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Hartree–Fock法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Kohn–Sham密度汎関数法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [自己無撞着場反復（SCF）：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Coulomb・Hartreeポテンシャル：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-poisson/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [LDA・GGA・hybrid汎関数：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [擬ポテンシャル・PAW：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [周期電子状態とk点：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [MP2摂動論：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mp2/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [配置間相互作用（CI）：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
