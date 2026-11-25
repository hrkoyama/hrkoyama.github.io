# 小さな量子模型と保存参照カード

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-quantum-small/

この章に登録された手法・問題・実行例の関連資料です。 固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。

## 手法

- [Born–Oppenheimer分子動力学（BOMD）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=ja>)

  解析BO力とCP型作用の式をVerlet/BAOABで積分し、核熱と架空電子運動エネルギーを分けます。
- [カー–パリネロ法（CPMD）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=ja>)

  解析BO力とCP型作用の式をVerlet/BAOABで積分し、核熱と架空電子運動エネルギーを分けます。
- [Langevinサーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja>)

  解析BO力とCP型作用の式をVerlet/BAOABで積分し、核熱と架空電子運動エネルギーを分けます。
- [速度Verlet／粒子leapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja>)

  解析BO力とCP型作用の式をVerlet/BAOABで積分し、核熱と架空電子運動エネルギーを分けます。
- [Schrödinger固有値問題](<https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja>)

  NumPyで8回全対角化し、native824固有対を保存して低24対を表示します。
- [Hartree–Fock法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja>)

  正準RHFから2電子MP2と9x9 FCIを求め、保存軌道から密度の2D断面を描画します。
- [MP2摂動論](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mp2/?lang=ja>)

  正準RHFから2電子MP2と9x9 FCIを求め、保存軌道から密度の2D断面を描画します。
- [配置間相互作用（CI）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=ja>)

  正準RHFから2電子MP2と9x9 FCIを求め、保存軌道から密度の2D断面を描画します。
- [自己無撞着場反復（SCF）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja>)

  正準RHFから2電子MP2と9x9 FCIを求め、保存軌道から密度の2D断面を描画します。
- [Schrödinger固有値問題](<https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja>)

  rank1核のHermitian行列を解き、固定NのFermi占有と自由エネルギーの力を計算します。
- [擬ポテンシャル・PAW](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=ja>)

  rank1核のHermitian行列を解き、固定NのFermi占有と自由エネルギーの力を計算します。
- [Born–Oppenheimer分子動力学（BOMD）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=ja>)
- [カー–パリネロ法（CPMD）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=ja>)
- [Langevinサーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja>)
- [速度Verlet／粒子leapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja>)
- [Schrödinger固有値問題](<https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja>)
- [Hartree–Fock法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja>)
- [Kohn–Sham密度汎関数法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja>)
- [配置間相互作用（CI）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=ja>)
- [自己無撞着場反復（SCF）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja>)
- [MP2摂動論](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mp2/?lang=ja>)
- [擬ポテンシャル・PAW](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=ja>)

## 方程式

- [2準位電子角と核のBO/CP型模型](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#two-state-bo-cp-model-ja>)

  長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。 無次元の核座標と規格化した1電子角。3固定刻み、2架空質量、1固定seedのOU熱浴です。 自作模型の無次元単位。Q,時間,電子角,温度を固定し、M=20、架空角質量μ=.04/.01。cp.xのemass規約とは別です。
- [電子の定常Schrödinger方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja>)

  固定核・非相対論の電子固有値問題。核間反発は電子Hamiltonianの外に加える。従来の水素型動径例を保持し、追加は1次元の箱/HOと3AO以下の2電子FCIに限定する。一般多電子系の直接解法や連続空間の厳密分子解の検証ではない。 原子単位、ゼロDirichlet端点、一様内点格子。箱[0,1]とHO[-L,L]です。 1次元模型の原子単位でℏ=m=1、HOはω=1。箱[0,1]とHOの有限区間[-L,L]はいずれも同次Dirichlet。
- [電子の定常Schrödinger方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja>)

  固定核・非相対論の電子固有値問題。核間反発は電子Hamiltonianの外に加える。従来の水素型動径例を保持し、追加は1次元の箱/HOと3AO以下の2電子FCIに限定する。一般多電子系の直接解法や連続空間の厳密分子解の検証ではない。 H核3個、電荷+1、2電子、3縮約s軌道の非対称三角形1個です。 H3+の固定3中心[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr、電荷+1、2電子/3s軌道。エネルギーhartree。
- [閉殻Hartree–Fock方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja>)

  閉殻RHFの占有空間軌道の式で、非局所交換を含む。既存のHe局所還元とH2のRHF例を保持する。追加は固定H2/H3+の最小2電子模型で、UHF式は別の対応模型に明示する。一般多中心分子、開殻の大域安定性、完全基底や一般相関法の保証ではない。 H核3個、電荷+1、2電子、3縮約s軌道の非対称三角形1個です。 H3+の固定3中心[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr、電荷+1、2電子/3s軌道。エネルギーhartree。
- [3平面波・非局所核と平均Fermi占有](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-projector-fermi-model-ja>)

  自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。 G=-1,0,1、k=±0.25、等重み、T=.05、電子数1.5の自作線形模型です。 無次元のG=-1,0,1、p=G+k、k=±.25、重み各.5、T=.05、平均電子数N=1.5、スピン係数2。実在格子定数や金属へ換算しません。
- [2準位電子角と核のBO/CP型模型](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#two-state-bo-cp-model-ja>)

  長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。
- [最小2電子模型のスピン非制限HF](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#unrestricted-hartree-fock-model-ja>)

  2固定距離のみ。有限基底FCIは連続空間の厳密解ではなく、UHF定常解の一般的な大域最小性は保証しません。角運動量・完全基底・広い解離曲線は未検証。
- [3平面波・非局所核と平均Fermi占有](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-projector-fermi-model-ja>)

  自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja#two-state-bo-cp-ou-ja-algorithm>)

  解析BO力とCP型作用の式をVerlet/BAOABで積分し、核熱と架空電子運動エネルギーを分けます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja#atomic-reference-cards-ja-algorithm>)

  pとn、軌道固有値と全エネルギーを区別し、既存の式と3保存行を照合します。
- [電子の定常Schrödinger方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja>)

  固定核・非相対論の電子固有値問題。核間反発は電子Hamiltonianの外に加える。従来の水素型動径例を保持し、追加は1次元の箱/HOと3AO以下の2電子FCIに限定する。一般多電子系の直接解法や連続空間の厳密分子解の検証ではない。
- [閉殻Hartree–Fock方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja>)

  閉殻RHFの占有空間軌道の式で、非局所交換を含む。既存のHe局所還元とH2のRHF例を保持する。追加は固定H2/H3+の最小2電子模型で、UHF式は別の対応模型に明示する。一般多中心分子、開殻の大域安定性、完全基底や一般相関法の保証ではない。
- [局所Kohn–Sham DFT](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja>)

  密度汎関数の局所KS代表形です。公開例は、球対称Heのスピン非偏極・Dirac交換のみLDAと、固定した周期He／He₂セルのLDA交換＋VWN5相関です。原子の動径実装と周期PySCFワークフローは別系列で、基底・境界条件・参照も異なります。各例の範囲は下の固定入力・検証記録で確認してください。GGA・hybrid・一般物質・励起状態まで検証した意味ではありません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=ja#quantum-box-ho-ja-algorithm>)

  NumPyで8回全対角化し、native824固有対を保存して低24対を表示します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja#h2-rhf-uhf-fci-ja-algorithm>)

  固定SCFでRHFと対称性を破ったUHFを求め、4x4二電子Hamiltonianを対角化します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja#h3plus-mp2-fci-ja-algorithm>)

  正準RHFから2電子MP2と9x9 FCIを求め、保存軌道から密度の2D断面を描画します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja#periodic-he-reference-cards-ja-algorithm>)

  保存エネルギー差分・解析力・Gaussian/PW比較の算術を再照合します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja#periodic-projector-occupations-ja-algorithm>)

  rank1核のHermitian行列を解き、固定NのFermi占有と自由エネルギーの力を計算します。

## 問題の図

- [2準位模型のBO/CP型連成と短い核熱浴](<https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png
- [1次元箱型井戸・量子調和振動子](<https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/quantum-box-ho.png
- [3中心H3+の小RHF/MP2/FCI模型](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png
- [3平面波の非局所projectorと有限温度占有](<https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png
- [2準位模型のBO/CP型連成と短い核熱浴](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png
- [H/Heの式・密度・固定参照カード](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/atomic-reference-cards.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/atomic-reference-cards.png
- [1次元箱型井戸・量子調和振動子](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/quantum-box-ho.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/quantum-box-ho.png
- [最小基底H2のRHF/UHF/FCI・2固定幾何](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h2-rhf-uhf-fci.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h2-rhf-uhf-fci.png
- [3中心H3+の小RHF/MP2/FCI模型](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png
- [保存周期Heエネルギー・力の参照台帳](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-he-reference-cards.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-he-reference-cards.png
- [3平面波の非局所projectorと有限温度占有](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png
- [He基底状態：閉殻HF・交換のみLDA](<https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja>)

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png
- [水素型原子の動径固有値問題](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja>)

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/hydrogenic.png
- [H₂分子RHF：独立参照・SCF・s型基底拡大](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja>)

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png
- [周期He₂の原子間力：解析力・有限差分・BOMD接続](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja>)

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/preview.png
- [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja>)

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/preview.png

## 厳密解・参照解

- [2準位模型のBO/CP型連成と短い核熱浴：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja#references-ja>)

  解析勾配、4096/8192段の固定RK4感度、拡張エネルギーとOU条件付き分散を照合します。
- [2準位模型のBO/CP型連成と短い核熱浴](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-two-state-bo-cp-ou-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 無次元の核座標と規格化した1電子角。3固定刻み、2架空質量、1固定seedのOU熱浴です。 自作模型の無次元単位。Q,時間,電子角,温度を固定し、M=20、架空角質量μ=.04/.01。cp.xのemass規約とは別です。 長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。
- [1次元箱型井戸・量子調和振動子：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=ja#references-ja>)

  Decimal箱スペクトル、連続解、native規格化・直交性・残差・parityを照合します。
- [1次元箱型井戸・量子調和振動子](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-quantum-box-ho-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 原子単位、ゼロDirichlet端点、一様内点格子。箱[0,1]とHO[-L,L]です。 1次元模型の原子単位でℏ=m=1、HOはω=1。箱[0,1]とHOの有限区間[-L,L]はいずれも同次Dirichlet。 8回の全固有対計算で824組をraw保存、規格化等の資格判定は選択24組です。節の閾値と位相は診断、HO0.003は固定例の達成目標で証明済み上界ではありません。有限壁と格子感度を相殺から独立に保証しません。
- [3中心H3+の小RHF/MP2/FCI模型：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja#references-ja>)

  独立fermion組立、MP2行列要素の摂動式、電子数・SCF残差・FCI変分性を確認します。
- [3中心H3+の小RHF/MP2/FCI模型](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-h3plus-mp2-fci-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 H核3個、電荷+1、2電子、3縮約s軌道の非対称三角形1個です。 H3+の固定3中心[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr、電荷+1、2電子/3s軌道。エネルギーhartree。 独立な演算子組立と2電子RS2恒等式で固定小模型を照合します。新しい外部PySCF参照はありません。一般分子DFT、CC、多参照法、精密エネルギー・最適化・化学精度は未実装/未検証。MP2は変分上界ではありません。
- [3平面波の非局所projectorと有限温度占有：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja#references-ja>)

  独立3次式固有値、Hermiticity・電子数・entropy・解析力と自由エネルギー差分を照合します。
- [3平面波の非局所projectorと有限温度占有](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-projector-occupations-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 G=-1,0,1、k=±0.25、等重み、T=.05、電子数1.5の自作線形模型です。 無次元のG=-1,0,1、p=G+k、k=±.25、重み各.5、T=.05、平均電子数N=1.5、スピン係数2。実在格子定数や金属へ換算しません。 自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。
- [2準位模型のBO/CP型連成と短い核熱浴](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-two-state-bo-cp-ou-ja>)
  reference_kind: semi-analytic

  半解析解 無次元の核座標と規格化した1電子角。3固定刻み、2架空質量、1固定seedのOU熱浴です。 自作模型の無次元単位。Q,時間,電子角,温度を固定し、M=20、架空角質量μ=.04/.01。cp.xのemass規約とは別です。
- [H/Heの式・密度・固定参照カード](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-atomic-reference-cards-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。
- [1次元箱型井戸・量子調和振動子](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-quantum-box-ho-ja>)
  reference_kind: analytic

  解析解 原子単位、ゼロDirichlet端点、一様内点格子。箱[0,1]とHO[-L,L]です。 1次元模型の原子単位でℏ=m=1、HOはω=1。箱[0,1]とHOの有限区間[-L,L]はいずれも同次Dirichlet。
- [最小基底H2のRHF/UHF/FCI・2固定幾何](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-h2-rhf-uhf-fci-ja>)
  reference_kind: semi-analytic

  半解析解 H-H距離1.4/3.0bohr、2電子、HごとにSTO-3G縮約s軌道を1個用います。 核間距離1.4/3.0bohr、全エネルギーhartree。各Hに同じ明示3primitiveのs型収縮を1つ置く2AO/2電子の固定部分空間。
- [3中心H3+の小RHF/MP2/FCI模型](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-h3plus-mp2-fci-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 H核3個、電荷+1、2電子、3縮約s軌道の非対称三角形1個です。 H3+の固定3中心[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr、電荷+1、2電子/3s軌道。エネルギーhartree。
- [保存周期Heエネルギー・力の参照台帳](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-he-reference-cards-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 人工2He・4電子・5bohrセル、局所のみのGTH、固定LDA_X+VWNとコード版です。 人工He2、4電子、5bohrセル。保存した幾何・局所GTH版・LDA_X+VWN/Libxc・PySCF/DFTK版をsaved-data/periodic-he-reference.jsonに固定。エネルギーhartree、力hartree/bohr。
- [3平面波の非局所projectorと有限温度占有](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-projector-occupations-ja>)
  reference_kind: semi-analytic

  半解析解 G=-1,0,1、k=±0.25、等重み、T=.05、電子数1.5の自作線形模型です。 無次元のG=-1,0,1、p=G+k、k=±.25、重み各.5、T=.05、平均電子数N=1.5、スピン係数2。実在格子定数や金属へ換算しません。
- [2準位模型のBO/CP型連成と短い核熱浴：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja#two-state-bo-cp-ou-ja-validation>)

  解析勾配、4096/8192段の固定RK4感度、拡張エネルギーとOU条件付き分散を照合します。
- [2準位模型のBO/CP型連成と短い核熱浴](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-two-state-bo-cp-ou-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 無次元の核座標と規格化した1電子角。3固定刻み、2架空質量、1固定seedのOU熱浴です。 自作模型の無次元単位。Q,時間,電子角,温度を固定し、M=20、架空角質量μ=.04/.01。cp.xのemass規約とは別です。 長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。
- [H/Heの式・密度・固定参照カード：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja#atomic-reference-cards-ja-validation>)

  選択3行は各40基底関数です。保存値・電子数・出典を照合し、新SCFは実行しません。
- [H/Heの式・密度・固定参照カード](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-atomic-reference-cards-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。 参照カードの整備・保存値照合であり、新SCF/新独立参照は0回。相関込み厳密He、完全基底極限、全軌道の再実行は主張しません。
- [1次元箱型井戸・量子調和振動子：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=ja#quantum-box-ho-ja-validation>)

  Decimal箱スペクトル、連続解、native規格化・直交性・残差・parityを照合します。
- [1次元箱型井戸・量子調和振動子](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-quantum-box-ho-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 原子単位、ゼロDirichlet端点、一様内点格子。箱[0,1]とHO[-L,L]です。 1次元模型の原子単位でℏ=m=1、HOはω=1。箱[0,1]とHOの有限区間[-L,L]はいずれも同次Dirichlet。 8回の全固有対計算で824組をraw保存、規格化等の資格判定は選択24組です。節の閾値と位相は診断、HO0.003は固定例の達成目標で証明済み上界ではありません。有限壁と格子感度を相殺から独立に保証しません。
- [最小基底H2のRHF/UHF/FCI・2固定幾何：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja#h2-rhf-uhf-fci-ja-validation>)

  保存PySCF RHF2値、独立g/u変分多項式・FCI閉形式・fermion組立と照合します。
- [最小基底H2のRHF/UHF/FCI・2固定幾何](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-h2-rhf-uhf-fci-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 H-H距離1.4/3.0bohr、2電子、HごとにSTO-3G縮約s軌道を1個用います。 核間距離1.4/3.0bohr、全エネルギーhartree。各Hに同じ明示3primitiveのs型収縮を1つ置く2AO/2電子の固定部分空間。 2固定距離のみ。有限基底FCIは連続空間の厳密解ではなく、UHF定常解の一般的な大域最小性は保証しません。角運動量・完全基底・広い解離曲線は未検証。
- [3中心H3+の小RHF/MP2/FCI模型：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja#h3plus-mp2-fci-ja-validation>)

  独立fermion組立、MP2行列要素の摂動式、電子数・SCF残差・FCI変分性を確認します。
- [3中心H3+の小RHF/MP2/FCI模型](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-h3plus-mp2-fci-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 H核3個、電荷+1、2電子、3縮約s軌道の非対称三角形1個です。 H3+の固定3中心[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr、電荷+1、2電子/3s軌道。エネルギーhartree。 独立な演算子組立と2電子RS2恒等式で固定小模型を照合します。新しい外部PySCF参照はありません。一般分子DFT、CC、多参照法、精密エネルギー・最適化・化学精度は未実装/未検証。MP2は変分上界ではありません。
- [保存周期Heエネルギー・力の参照台帳：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja#periodic-he-reference-cards-ja-validation>)

  元の数値・基準・履歴を保持し、単位・電子数・幾何・共有Libxcの独立性限界を明記します。
- [保存周期Heエネルギー・力の参照台帳](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-he-reference-cards-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 人工2He・4電子・5bohrセル、局所のみのGTH、固定LDA_X+VWNとコード版です。 人工He2、4電子、5bohrセル。保存した幾何・局所GTH版・LDA_X+VWN/Libxc・PySCF/DFTK版をsaved-data/periodic-he-reference.jsonに固定。エネルギーhartree、力hartree/bohr。 既存の6力成分・エネルギー差分・Gaussian/PW比較の保存値照合です。電子計算の追加0回。新しい基底/k/カットオフ走査、一般物質、金属、長時間MDへ拡張しません。
- [3平面波の非局所projectorと有限温度占有：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja#periodic-projector-occupations-ja-validation>)

  独立3次式固有値、Hermiticity・電子数・entropy・解析力と自由エネルギー差分を照合します。
- [3平面波の非局所projectorと有限温度占有](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-projector-occupations-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 G=-1,0,1、k=±0.25、等重み、T=.05、電子数1.5の自作線形模型です。 無次元のG=-1,0,1、p=G+k、k=±.25、重み各.5、T=.05、平均電子数N=1.5、スピン係数2。実在格子定数や金属へ換算しません。 自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。
- [He基底状態：閉殻HF・交換のみLDA：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#references-ja>)

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 閉殻HF・交換のみLDAの独立参照、SCF残差・電子数・格子収束を確認します。近似汎関数の解を厳密なHe多体解とは呼びません。
- [H/Heの式・密度・固定参照カード](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-atomic-reference-cards-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 有限格子の数値参照 Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。 参照カードの整備・保存値照合であり、新SCF/新独立参照は0回。相関込み厳密He、完全基底極限、全軌道の再実行は主張しません。
- [水素型原子の動径固有値問題：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=ja#references-ja>)

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 水素型原子の解析的な固有エネルギー・軌道と比較し、有限半径打切りと格子誤差を分けます。既存の固定入力・保存結果を参照します。 既存の固定入力・保存結果に対応する解析参照カードを追加。解析式、点・時刻・動径の標本化、配布版SHAと実行コードを相互に辿れます。過去の計算を再実行した記録ではありません。
- [水素型原子：解析解と格子収束](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-hydrogenic-coulomb-reference-ja>)
  relation: same-problem
  reference_kind: analytic

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 解析解 非相対論・無限質量の点核。核電荷Z=1,2。縮約動径軌道を一様格子の2次中心差分で離散化。 既存の固定入力・保存結果に対応する解析参照カードを追加。解析式、点・時刻・動径の標本化、配布版SHAと実行コードを相互に辿れます。過去の計算を再実行した記録ではありません。
- [H/Heの式・密度・固定参照カード](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-atomic-reference-cards-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 有限格子の数値参照 Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。 参照カードの整備・保存値照合であり、新SCF/新独立参照は0回。相関込み厳密He、完全基底極限、全軌道の再実行は主張しません。
- [H₂分子RHF：独立参照・SCF・s型基底拡大：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#references-ja>)

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 小さな固定H₂モデルの独立RHF参照とSCF・s型基底の検査を使います。有限基底RHFの一致は完全な電子相関を含む厳密分子解の一致ではありません。
- [最小基底H2のRHF/UHF/FCI・2固定幾何](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-h2-rhf-uhf-fci-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 半解析解 H-H距離1.4/3.0bohr、2電子、HごとにSTO-3G縮約s軌道を1個用います。 核間距離1.4/3.0bohr、全エネルギーhartree。各Hに同じ明示3primitiveのs型収縮を1つ置く2AO/2電子の固定部分空間。 2固定距離のみ。有限基底FCIは連続空間の厳密解ではなく、UHF定常解の一般的な大域最小性は保証しません。角運動量・完全基底・広い解離曲線は未検証。
- [周期He₂の原子間力：解析力・有限差分・BOMD接続：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja#references-ja>)

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 固定He₂配置のエネルギー有限差分と解析力、独立DFTK参照と保存された収束検査を区別します。長時間の第一原理MD精度を認定するものではありません。
- [保存周期Heエネルギー・力の参照台帳](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-he-reference-cards-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 有限格子の数値参照 人工2He・4電子・5bohrセル、局所のみのGTH、固定LDA_X+VWNとコード版です。 人工He2、4電子、5bohrセル。保存した幾何・局所GTH版・LDA_X+VWN/Libxc・PySCF/DFTK版をsaved-data/periodic-he-reference.jsonに固定。エネルギーhartree、力hartree/bohr。 既存の6力成分・エネルギー差分・Gaussian/PW比較の保存値照合です。電子計算の追加0回。新しい基底/k/カットオフ走査、一般物質、金属、長時間MDへ拡張しません。
- [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja#references-ja>)

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 固定した小周期Heセルの独立DFTK参照・SCF・基底・k点の保存検査を使います。擬ポテンシャルと交換のみLDAのモデル範囲に限定します。
- [保存周期Heエネルギー・力の参照台帳](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-he-reference-cards-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 有限格子の数値参照 人工2He・4電子・5bohrセル、局所のみのGTH、固定LDA_X+VWNとコード版です。 人工He2、4電子、5bohrセル。保存した幾何・局所GTH版・LDA_X+VWN/Libxc・PySCF/DFTK版をsaved-data/periodic-he-reference.jsonに固定。エネルギーhartree、力hartree/bohr。 既存の6力成分・エネルギー差分・Gaussian/PW比較の保存値照合です。電子計算の追加0回。新しい基底/k/カットオフ走査、一般物質、金属、長時間MDへ拡張しません。

## コード・検証

- [2準位模型のBO/CP型連成と短い核熱浴](<https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja>)
  availability: run

  電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。
- [1次元箱型井戸・量子調和振動子](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=ja>)
  availability: run

  1次元の箱と量子調和振動子で、低3固有対と有限領域・格子の影響を比較します。
- [3中心H3+の小RHF/MP2/FCI模型](<https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja>)
  availability: run

  固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。
- [3平面波の非局所projectorと有限温度占有](<https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja>)
  availability: run

  3平面波の小周期模型で、非局所projectorと有限温度占有・力を示します。
- [H/Heの式・密度・固定参照カード](<https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja>)
  availability: run

  既存H/Heの式と保存参照を、単位・規格化・模型の限界とともに示します。
- [最小基底H2のRHF/UHF/FCI・2固定幾何](<https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja>)
  availability: run

  同じ最小基底H2の2固定幾何で、RHF/UHF/有限基底FCIとスピン対称性を比較します。
- [保存周期Heエネルギー・力の参照台帳](<https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja>)
  availability: run

  既存周期Heのエネルギーと6座標力を、保存参照と元の受入基準へ対応付けます。
- [He基底状態：閉殻HF・交換のみLDA：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#code-ja>)
  availability: source

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 対応する公開検査と配布版の条件を確認できます。
- [H₂分子RHF：独立参照・SCF・s型基底拡大：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#code-ja>)
  availability: source

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 対応する公開検査と配布版の条件を確認できます。
- [周期He₂の原子間力：解析力・有限差分・BOMD接続：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja#code-ja>)
  availability: source

  固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。 対応する公開検査と配布版の条件を確認できます。
