# 分野をつなぐ数値計算の入口

量子化学・分子動力学・反応拡散・生物・流体・重力を、受け渡す量と共通の数学からたどる。矢印ごとに必要な検証を示し、実行できる固定例、解説のみの段階、未実行の連成を区別する。

共通台帳の実行例と、独立展開した補助配布版の固定検証を分けて示します。Langevin振動子・反応拡散・Turing/膜興奮の限定例があっても、第一原理MDから熱浴まで、または反応・拡散・流体を結ぶ経路全体の検証には広げません。

## DFT → 第一原理MD → 温度制御

[HTML](https://hrkoyama.github.io/numerical-methods-atlas/connections/?lang=ja#dft-md-ja)

静的な電子状態から核の力、軌道、熱浴へ。固定Heの力と、別の古典系でのLangevin／CSVRの分布・揺らぎ・相関をたどり、第一原理MDとの連成に残る検証を確かめます。

この経路で確認できる範囲：静的Heと多原子He₂の力は実行可能で、BOMD接続は短い局所確認まで。Langevin／CSVRの調和・quartic分布と相関は、独立した古典補助例で検証します。BOMD／CPMDと熱浴を結ぶ経路全体は未実行です。

### 固定セルの周期He KS-LDA

実行可能：格子定数4 bohr、He 1原子・価電子2の固定セル。PySCFドライバーでLDA_X＋VWN5と局所GTHを用い、k点・Gaussian軌道基底・FFT補助格子・SCFを分けて比較する。Γ点と2³メッシュには別実行のDFTK参照がある。

段階の状態: fixed-input

- [周期DFTの固定モデル・測定結果](/numerical-methods-atlas/ja/read/periodic-dft/)
- [Kohn–Sham密度汎関数法](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja): educational-example
- [自己無撞着場反復（SCF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja): educational-example
- [電子状態計算の基底](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=ja): educational-example
- [LDA・GGA・hybrid汎関数](https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=ja): educational-example
- [擬ポテンシャル・PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=ja): educational-example
- [周期電子状態とk点](https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=ja): educational-example
- [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=ja): 固定した1原子単純立方Heセル（格子定数4 bohr、価電子2、非偏極LDA_X＋VWN5、局所GTH）。PySCFを使う実行・検証ワークフロー。11設定でk点・Gaussian軌道基底・FFT補助格子・SCFを別々に比較し、Γ／2³は独立DFTK平面波参照と照合。平衡He結晶・完全基底・金属・一般物質は未検証。

残る差: 静的な固定モデルの範囲。平衡He結晶の予測、一般物質、力・応力・MD軌道の検証は含まない。

### エネルギーから核の力へ

核座標Rに依存する収束済み電子エネルギーから F_I = −∂E_BO/∂R_I を求める段階。位置依存の基底ではPulay項、擬ポテンシャルではその力への寄与も整合させる。

段階の状態: fixed-input

- [DFTから原子間力へ：有限差分・独立参照・収束](/numerical-methods-atlas/ja/read/periodic-forces/)
- [Kohn–Sham密度汎関数法](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja): educational-example
- [電子状態計算の基底](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=ja): educational-example
- [自己無撞着場反復（SCF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja): educational-example
- [周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=ja): 非対称な2原子He周期セル・局所GTH・LDA交換＋VWN5。PySCFの解析力（Gaussian基底の微分を含む）を全6座標のエネルギー有限差分とDFTK平面波参照で照合し、力の基底・k点・SCF・FFT収束を分離。BOMDの力供給と短い刻み比較に限定し、長時間NVE・CPMD・一般物質は未検証。

残る差: 固定He₂・局所GTH・VWN5の数値検証に限定。他元素・非局所擬ポテンシャル・応力・金属・長時間MDは未検証。

### BOMD・Car–Parrinello MD

BOMDは各核配置で電子基底状態を十分に収束させて核を進める。力の配布版にはvelocity-Verletへの接続と1ステップ対2半ステップの局所確認がある。BOMD全体とCPMDは解説のみの状態を維持し、長時間NVEやCPの仮想質量・直交制約の検証と区別する。

段階の状態: reading

- [BOMDとCPMDの比較](/numerical-methods-atlas/ja/read/periodic-dft/#first-principles-md)
- [BOMDへの力の受け渡しと局所確認](/numerical-methods-atlas/ja/read/periodic-forces/#bomd-interface)
- [Born–Oppenheimer分子動力学（BOMD）](https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=ja): reading-only
- [カー–パリネロ法（CPMD）](https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=ja): reading-only

残る差: BOMDの長時間NVEドリフトと時間刻み・SCF公差の系統的収束、CPMDの専用実装は未公開。短い接続確認を軌道全体の検証として数えない。

### サーモスタットと分布の確認

12手法のうちLangevinとCSVRの2手法に専用実装。旧1自由度Langevin/BAOABの調和例を保持し、別版の同じOBABO分割で、非縮退2自由度の調和系とquartic係数λ=0.2の2自由度非調和系を比較します。CSVR単独の運動エネルギー核も検査。他の10手法は実装予定です。

段階の状態: scoped-supplement

- [温度制御と分布の比較](/numerical-methods-atlas/ja/read/thermostats/)
- [Langevin振動子：分布・相関・刻み幅の実測](/numerical-methods-atlas/ja/read/validation-models/#langevin-harmonic)
- [CSVRとLangevin：分布・揺らぎ・方法依存の相関](/numerical-methods-atlas/ja/read/validation-thermostats/)
- [Nosé–Hooverサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover/?lang=ja): planned
- [Nosé–Hoover chain](https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover-chains/?lang=ja): planned
- [Langevinサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja): educational-example
- [確率的速度リスケーリング（CSVR）](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja): educational-example

別管理の固定補助例: 旧1自由度の調和Langevin/BAOABと、新しい同OBABO分割の2自由度CSVR／Langevin比較（調和・quartic λ=0.2）、CSVR核の限定診断。BOMD／CPMDの核配置・原子間力は受け取らず、DFTと熱浴を連成した計算ではありません。
- [Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja): 調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。
  調和ポテンシャル・固定seedの分布検証です。位置分散が正確でも運動量には有限刻み偏りがあります。他のサーモスタット、一般分子系、長時間の第一原理MDへ検証を移しません。
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-models/#langevin-harmonic)
- [CSVRの厳密浴：条件付き分布・揺らぎ・運動エネルギー相関](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=ja): 自由度1・2・6のCSVR浴だけを実装し、厳密な条件付きモーメントと非心χ²分布、正準Gamma分布と運動エネルギー相関を照合します。
  浴の診断用ケースで独立した物理問題数へ加算しません。浴がKを正しく分布させてもglobal rescalingだけでは方向を熱化しません。exp(−t/τ)を力付きMDのK相関へ流用しません。固定seedと予算に対する統計判定で、一般の混合保証ではありません。
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-thermostats/#csvr-kinetic-kernel)
- [CSVRとLangevin：調和2自由度の分布・揺らぎ・相関](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja): 異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。
  global CSVRとlocal Langevinの運動相関が等しいとは要求しません。CDF差は指定5点の最大であり全実数上のKS距離ではありません。正準初期分布の保存と温度摂動からの有限時間確認は一般のエルゴード性証明ではなく、軸上の励起されない自由度が残る反例もテストします。分子・拘束・BOMDには外挿しません。
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-thermostats/#csvr-langevin-harmonic)
- [非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja): 弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。
  特定の分離可能な四次2自由度・固定seedだけの小さな例です。Hを調和系のGamma分布と扱いません。全系相関には独立な厳密動力学参照がなく、相関一致や統計誤差に隠れる時間次数を合格主張しません。成熟分子系・輸送係数・量子・第一原理MDの検証ではありません。
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-thermostats/#csvr-langevin-quartic)

残る差: 専用実装は2手法で、他10手法は未実装。新しい2自由度調和・quartic比較とCSVR核は別の古典要素例です。旧BAOABも保持します。平衡分布・揺らぎと、浴に依存する時間相関を区別し、一般多体系や第一原理MDとの連成へ証拠を移しません。

### 多原子セルでエネルギー微分と力を照合する

量を受け渡す接続

**受け渡す量:** 核配置R → 電子密度・E_BO(R) → 核の力F_I。

**共通する数理:** 同じKS/SCF問題を核配置ごとに解き、そのエネルギーの幾何微分を使う。電子計算の打切り誤差は力にも伝わる。

**異なる点:** スカラーの全エネルギー比較とベクトルの力の比較は別の検査。基底の位置依存性、擬ポテンシャル、イオン項とSCF未収束を微分に反映する。

**既存の要素根拠:** 1原子の静的例とは別に、periodic-he-forcesが非対称He₂の解析力・全6座標有限差分・独立DFTK参照と、基底/k点/SCF/FFT収束を保存。

**接続に必要な検証:** 対称性に守られない変位配置で力を中心有限差分のエネルギー勾配と比較し、変位幅・基底・補助格子・k点・SCF公差を独立に細かくする。

固定例で接続を検証：固定したHe₂モデルのエネルギーから力への接続を検証。一般物質やMD全体へは適用範囲を移さない。

### 力を時間発展へ渡す

量を受け渡す接続

**受け渡す量:** BOMD：各時刻のF_Iから核の位置・運動量を更新。CPMD：核と仮想電子自由度を直交制約付きで同時に更新。

**共通する数理:** 核の運動方程式は時間積分の問題。電子構造との連成では反復誤差・時間刻み・拘束誤差を同時に管理する。

**異なる点:** BOMDの電子最小化とCPMDの仮想軌道ダイナミクスは異なる。CPの仮想質量やエネルギーは物理的な電子温度・電子励起ではない。

**既存の要素根拠:** 周期He₂の力供給をvelocity-Verletへ接続し、各配置でSCFを解き直して1ステップと2半ステップを比較。CPMD実装や長時間NVEの証拠ではない。

**接続に必要な検証:** まずサーモスタットなしで、BOMDは物理的な核の運動＋BOエネルギーのNVEドリフトを時間刻み・SCF公差に対して測る。CPでは保存すべき拡張エネルギーと核＋BOエネルギーの交換を区別し、仮想質量/刻み幅、直交性、断熱分離とBO軌道への感度も調べる。

局所的な接続のみ確認：BOMDへの力の受け渡しを短い局所刻み比較で確認。長時間軌道・NVEドリフト・温度制御の検証は残る。

### 軌道から熱浴・統計へ

量を受け渡す接続

**受け渡す量:** 核の運動量・運動エネルギーと熱浴の摩擦/確率項を交換する。T = 2K/(f k_B)では拘束・重心運動を除いた有効自由度fを明記する。

**共通する数理:** 常微分/確率微分方程式と分布の標本化が重なる。有限時間刻みと熱浴結合時間は標本化と相関の両方に影響する。

**異なる点:** 平均温度の一致だけでは正準分布やエルゴード性を示さない。熱浴は拡散・速度相関を変え得る。CPでは核と仮想電子自由度の温度を混同しない。

**既存の要素根拠:** 旧BAOABと、新しい同OBABO分割のCSVR／Langevin調和・quartic比較、Gamma/CIRを参照するCSVR核診断が古典要素例として利用可能。温度・エネルギー分布、揺らぎ、方法依存の相関を確認します。第一原理MDの力供給APIとは独立で、両者を結んだ軌道は実行していません。

**接続に必要な検証:** 調和振動子・理想気体などで位置分布とKのχ²分布、自己相関、独立系列の不確かさを確認し、刻み幅と結合時間を変える。核MDとの連成前に小自由度の探索失敗も調べる。

連成実行：未実施。サーモスタット付き第一原理MDは未実行。

### 一次文献と確認した範囲

- W. Kohn and L. J. Sham (1965). [Self-Consistent Equations Including Exchange and Correlation Effects](https://doi.org/10.1103/PhysRev.140.A1133). 既存アトラスの原著書誌・DOIを確認。Kohn–Sham法の原著として引用し、論文全体の数値再現は主張しません。
- M. Born and R. Oppenheimer (1927). [Zur Quantentheorie der Molekeln](https://onlinelibrary.wiley.com/doi/10.1002/andp.19273892002). 出版社の書誌・DOIを確認。Born–Oppenheimer分離の歴史的基礎として引用し、原文全文の監査や現代のMD実装の再現は主張しません。
- R. Car and M. Parrinello (1985). [Unified Approach for Molecular Dynamics and Density-Functional Theory](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.2471). 出版社の書誌・抄録と公開原文の式(3)–(5)、BO面近傍の仮想電子運動の議論を参照。論文のSi動力学の数値再現は行っていません。
- William G. Hoover (1985). [Canonical dynamics: Equilibrium phase-space distributions](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.31.1695). 既存サーモスタット台帳の原著。今回出版社の書誌・抄録を確認し、拡張位相空間分布と調和振動子の例の範囲を参照。全文の監査・数値再現は未実施。
- B. Leimkuhler and C. Matthews (2013). [Rational Construction of Stochastic Numerical Methods for Molecular Sampling](https://arxiv.org/abs/1203.5428). 著者稿の抄録、Langevin式、付録のBAOAB更新式（印刷22ページ）を確認。一般分子の超収束や原著の長時間計算を再現したとは主張しません。
- G. Bussi, D. Donadio and M. Parrinello (2007). [Canonical sampling through velocity rescaling](https://arxiv.org/html/0803.4060v1). 著者稿のII.1–II.3、運動エネルギーSDE(7)と付録A(16)–(22)を確認。Gamma二乗和生成には著者の訂正も参照。

## 反応拡散 → 生物・流体の輸送

[HTML](https://hrkoyama.github.io/numerical-methods-atlas/connections/?lang=ja#reaction-transport-ja)

線形モード、有限振幅の非線形発展、成長後パターン、0次元の膜興奮では検証量が変わります。固定した1次元Schnakenberg系の独立参照・空間/時間収束から、流体と結ぶために残る検証をたどります。

この経路で確認できる範囲：固定した1次元周期Schnakenbergの非線形発展と成長後パターンを独立参照・空間/時間収束で、線形反応拡散と0次元FHNを各専用例で検証します。ロジスティック/SIR、移流、周期流体も別々の要素根拠です。反応・拡散・移流/流体を結ぶ経路全体は未実行です。

### 反応と拡散の枠組み

反応則・拡散・初期値・境界を指定し、線形Fourierモード、Schnakenbergの線形発現、有限振幅の非線形発展と成長後パターンを分けます。新しい固定1次元周期例は中心差分＋陰的中点反応のStrang分割を独立な脱エイリアスFourier–Galerkin/Radau参照へ照合します。

段階の状態: scoped-supplement

- [生物モデルと反応拡散の検証案](/numerical-methods-atlas/ja/read/biological-models/)
- [線形反応拡散の空間・時間収束](/numerical-methods-atlas/ja/read/validation-models/#reaction-diffusion-fourier)
- [非線形Schnakenbergと成長後パターンの独立参照・収束](/numerical-methods-atlas/ja/read/validation-biology/)
- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja): educational-example
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja): educational-example
- [陰的中点則](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja): educational-example

別管理の固定補助例: 旧線形モード例を保持し、固定した1次元周期Schnakenberg系の非線形解と成長後パターンの空間/時間誤差を分けて測定します。同じ差分半離散系のRadauは時間誤差用で、独立な連続PDE参照とは区別します。汎用の生物モデルや流体連成の認証ではありません。
- [反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja): 線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。
  線形・周期・滑らかな単一モードだけを検証します。非線形のFisher前線、複雑境界、空間生態系や一般の反応ネットワークの検証ではありません。
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-models/#reaction-diffusion-fourier)
- [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja): Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。
  1つの平衡近傍の発生段階です。原著係数や原著実験の再現、成熟模様、ランダム擾乱からの波数選択、実生物の較正は主張しません。
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-models/#turing-schnakenberg)
- [Schnakenberg有限振幅過渡：非線形性と独立参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja): t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。
  選択対称性を持つ1D教育用モデルで、乱数からの自由な波数選択・位相安定性・2D斑点・実生物の較正を検証しません。原著の係数や実験の再現ではありません。陰的midpointはA安定でもL安定・無条件正値ではなく、反応でu+vは保存しません。初回粗刻みは不合格で、受入基準を変えず時間解像度を強化した履歴を保持。量子計算は追加しません。
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology/#schnakenberg-nonlinear)
- [Schnakenberg飽和パターン：近定常性と格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja): t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。
  選択対称性を持つ1D教育用モデルで、乱数からの自由な波数選択・位相安定性・2D斑点・実生物の較正を検証しません。原著の係数や実験の再現ではありません。陰的midpointはA安定でもL安定・無条件正値ではなく、反応でu+vは保存しません。初回粗刻みは不合格で、受入基準を変えず時間解像度を強化した履歴を保持。量子計算は追加しません。 近飽和は参照の90→100の検査窓に対する判定で、厳密定常解・非線形安定性・長期吸引の証明ではありません。lateの巨大な線形差は線形化の破綻診断で、精度誤差ではありません。
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology/#schnakenberg-pattern)

残る差: 固定した1次元周期問題の範囲です。一般の反応則・非周期境界、Fisher–KPP前線、流れとの移流反応拡散は未検証です。拡散単体と反応拡散の結果を分けて示します。

### 生物：非線形模様形成・膜興奮と前線

Schnakenbergは1次元周期の線形発現・有限振幅発展・成長後パターンを、FitzHugh–Nagumoは0次元の刺激応答を検証します。非線形の独立参照と格子/時間収束を、生体組織への適合やFisher–KPP前線の検証へは転用しません。

段階の状態: scoped-supplement

- [Fisher–KPP前線](/numerical-methods-atlas/ja/read/biological-models/#06-1937-fisherkpp-invasion-front)
- [Turing型の模様発生](/numerical-methods-atlas/ja/read/biological-models/#09-1952-turing-reactiondiffusion-framework)
- [Schnakenbergの反応則](/numerical-methods-atlas/ja/read/biological-models/#17-1979-schnakenberg-reactiondiffusion)
- [Turing初期成長と独立参照](/numerical-methods-atlas/ja/read/validation-models/#turing-schnakenberg)
- [FitzHugh–Nagumoの0次元刺激応答](/numerical-methods-atlas/ja/read/validation-models/#fitzhugh-nagumo)
- [非線形Schnakenbergと成長後パターンの独立参照・収束](/numerical-methods-atlas/ja/read/validation-biology/)
- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja): educational-example
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja): educational-example
- [陰的中点則](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja): educational-example

別管理の固定補助例: 1次元Schnakenbergの線形発現・非線形発展・成長後パターンと、0次元FitzHugh–Nagumo刺激応答という別々の固定要素例です。独立参照と空間/時間誤差を区別し、膜の空間伝播へ広げません。
- [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja): Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。
  1つの平衡近傍の発生段階です。原著係数や原著実験の再現、成熟模様、ランダム擾乱からの波数選択、実生物の較正は主張しません。
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-models/#turing-schnakenberg)
- [FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja): 2変数の膜興奮縮約ODEを電流パルスで励起し、DOP853との全出力時刻の誤差・時間収束・回復を確認します。
  FHN/BVP型の縮約ODEの限定検証です。HH全イオンチャネル、空間軸索、患者データ、実測電気生理の再現を含みません。
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-models/#fitzhugh-nagumo)
- [Schnakenberg有限振幅過渡：非線形性と独立参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja): t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。
  選択対称性を持つ1D教育用モデルで、乱数からの自由な波数選択・位相安定性・2D斑点・実生物の較正を検証しません。原著の係数や実験の再現ではありません。陰的midpointはA安定でもL安定・無条件正値ではなく、反応でu+vは保存しません。初回粗刻みは不合格で、受入基準を変えず時間解像度を強化した履歴を保持。量子計算は追加しません。
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology/#schnakenberg-nonlinear)
- [Schnakenberg飽和パターン：近定常性と格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja): t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。
  選択対称性を持つ1D教育用モデルで、乱数からの自由な波数選択・位相安定性・2D斑点・実生物の較正を検証しません。原著の係数や実験の再現ではありません。陰的midpointはA安定でもL安定・無条件正値ではなく、反応でu+vは保存しません。初回粗刻みは不合格で、受入基準を変えず時間解像度を強化した履歴を保持。量子計算は追加しません。 近飽和は参照の90→100の検査窓に対する判定で、厳密定常解・非線形安定性・長期吸引の証明ではありません。lateの巨大な線形差は線形化の破綻診断で、精度誤差ではありません。
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology/#schnakenberg-pattern)

残る差: 固定した反射対称初期値と有限時間の1次元Schnakenbergです。一般初期値からの模様選択・2次元形態、伝播する膜パルス、Fisher前線速度、生物実験への較正と流体連成は未検証です。FHNは空間なしです。

### 実行できる反応のみの0次元例

ロジスティック増殖は単一個体群の解析解とRK4を比較。SIRは閉鎖・均質集団の割合をRK4と独立DOP853で比較し、人口保存・非負性・時間収束を調べる。どちらも空間を持たない。

段階の状態: fixed-input

- [ロジスティック増殖の固定例](/numerical-methods-atlas/ja/read/biological-models/#01-1838-logistic-population-growth)
- [閉鎖SIRの固定例](/numerical-methods-atlas/ja/read/biological-models/#05-1927-sir-and-seir-compartment-models)
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja): educational-example
- [ロジスティック増殖：解析解と刻み幅の収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=ja): 無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。
- [SIR：独立DOP853参照・人口保存・収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=ja): 閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。

残る差: 反応のみのODEの証拠。拡散・移流・空間伝播・SEIRの実装や、反応拡散連成の検証には使えない。

### 流れに運ばれる濃度・反応場

∂_t c + ∇·(u c) = ∇·(D∇c) + R(c) が一つの保存形。非圧縮なら∇·u=0の下で移流形にできる。与えた流速の受動スカラーと、濃度が密度・浮力などを介して流れへ戻る能動連成を分ける。

段階の状態: component-only

- [一定速度の移流部品](/numerical-methods-atlas/ja/read/stability/)
- [周期非圧縮流の部品](/numerical-methods-atlas/ja/read/incompressible/)
- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja): educational-example
- [MAC圧力射影法](https://hrkoyama.github.io/numerical-methods-atlas/methods/projection/?lang=ja): educational-example
- [周期正弦波の線形移流：風上法と解析解](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=ja): 長さ1の周期区間でq_t+a q_x=0を1周期進め、64/128点の1次風上法を平行移動した正弦波と比較する。計算値、解析値、誤差をCSVへ出す。
- [周期Taylor–Green渦：速度・散逸・発散](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=ja): 既存の2次元MAC投影法・中心対流項・明示SSPRK2を使用。16²/32²/64²で解析的減衰渦と比較し、最細格子はCFL半減でも確認。

残る差: 移流とTaylor–Green流れの実行例は別々の部品。濃度・反応・流体を結ぶ実行や分割誤差の測定はない。

### 同じPDE族から異なる生物の問いへ

モデルを適用する接続

**受け渡す量:** 反応則・拡散と境界を与え、前線位置または各空間モードの振幅を観測する。

**共通する数理:** 空間離散化した拡散と反応源の時間積分を共有し、反応JacobianとLaplacianのスペクトルが安定性に関わる。

**異なる点:** 前線速度の誤差とTuringの分散関係は別の検証量。生物の模様に似た画像でも機構やパラメータの妥当性は決まらない。

**既存の要素根拠:** Schnakenbergは旧線形発現に加え、固定した1次元周期・有限振幅初期値の非線形発展と成長後パターンを独立Fourier–Galerkin/Radau参照、空間・時間細分化で比較します。FHNは0次元DOP853照合、Fisher–KPP前線は未実行です。

**接続に必要な検証:** 前線は解析プロファイル/速度と比較し、有限領域の境界影響と空間/時間誤差を分ける。Turingはk=0の安定性を確かめ、境界が許す非零モードの初期成長をJ−k²Dおよび離散Laplacianの予測と比べる。

モデル族の対応全体の検証範囲：固定したSchnakenbergの空間例は独立した要素検証です。異なる生物モデル族への一般化、生体組織への妥当性確認、前線や流体へ接続する経路全体は実行していません。

### 空間項を外した反応の基準を調べる

要素計算との比較

**受け渡す量:** 空間一様・無輸送の極限では反応源R(c)がODEを与える。公開のロジスティック/SIRは各々の指定したRだけを検証する。

**共通する数理:** ODE積分器、局所誤差・時間収束、非負性の確認を反応更新の考え方に使える。

**異なる点:** ロジスティックは一変数の増殖、SIRは人口割合の区画間移行。全ての種が保存されるわけではなく、SIRの保存則を一般のRへ移せない。空間境界も持たない。

**既存の要素根拠:** logistic-growthとsir-epidemicは解析解または独立数値参照と比べた0次元の実行例。空間伝播の証拠はない。

**接続に必要な検証:** 連成する反応則そのものについて平衡・非負性・時間収束・源を含む収支を再確認する。ODE単体で合格しても、拡散や移流との分割後の非負性と収束は別に調べる。

要素例を参照する範囲：反応の部品を拡散・輸送と結合する実行は未実施。

### 移流を加え、流れとの受け渡しを決める

量を受け渡す接続

**受け渡す量:** 流体から濃度へ速度uを渡す。能動モデルなら濃度から浮力・密度・反応熱など、選んだ構成則に応じた量を流体へ返す。

**共通する数理:** 反応・移流・拡散の演算子を同じ時間軸上で組み合わせる。非圧縮の圧力投影は別途Poisson問題を必要とする。

**異なる点:** 保存形と移流形の同値には∇·u=0などの条件がある。移流CFL、拡散の刻み制限、反応の剛性、圧力境界は異なる。受動輸送と双方向連成の誤差も異なる。

**既存の要素根拠:** 線形/非線形Schnakenberg反応拡散と成長後パターン、周期移流、Taylor–Green流れは別々の要素検証です。反応・拡散のStrang誤差を測っても、濃度・移流・流体を結ぶ分割誤差を検証したことにはなりません。

**接続に必要な検証:** 境界流束と反応源を含む濃度収支、非負性、∇·u、空間/時間収束、分割順序・刻み依存を調べる。製造解または独立な連成参照を設け、能動連成では返す力/熱の収支も確認する。

連成実行：未実施。反応・拡散・移流または流体との能動連成は未実行。

### 一次文献と確認した範囲

- Pierre-François Verhulst (1847). [Sur la loi d’accroissement de la population (Deuxième mémoire)](https://www.persee.fr/doc/marb_0775-3225_1847_num_20_1_3457). 既存書誌の原文・書誌確認を継承。1847年の後期論文であり、1838年の最初の短報を監査したとはしない。今回の原文再監査は行っていない。
- W. O. Kermack and A. G. McKendrick (1927). [A contribution to the mathematical theory of epidemics](https://doi.org/10.1098/rspa.1927.0118). 既存生物モデル章と実行台帳の一次文献を継承。原論文の一般的な枠組みは公開例の閉鎖・均質SIRより広い。今回の全文再監査・論文全体の数値再現は行っていない。
- R. A. Fisher (1937). [The wave of advance of advantageous genes](https://doi.org/10.1111/j.1469-1809.1937.tb02153.x). 既存書誌の出版社書誌・原文抜粋の確認を継承。集団遺伝の前線の出典。独立のKPP原著の監査は未実施。今回の数値再現はない。
- Alan M. Turing (1952). [The Chemical Basis of Morphogenesis](https://www.damtp.cam.ac.uk/user/gold/pdfs/teaching/old_literature/Turing1952.pdf). 既存書誌にある大学公開原文のモデル設定・不安定性の前提の確認を継承。一般の2成分式を一意のTuring反応則とは扱わない。今回DOI先は取得不可で、追加の全文監査や数値再現は行っていない。
- Jürgen Schnakenberg (1979). [Simple chemical reaction systems with limit cycle behaviour](https://www.sciencedirect.com/science/article/pii/0022519379900420). 既存書誌の出版社書誌・抄録確認を継承。自己触媒反応系の出典であり、空間PDEや組織に較正したモデルの数値検証ではない。今回の全文再監査はない。
- Alexandre Joel Chorin (1968). [Numerical solution of the Navier-Stokes equations](https://math.berkeley.edu/~chorin/chorin68.pdf). 既存書誌の出版社書誌・著者公開原文の確認を継承。今回原文PDFへの到達を確認したが本文は抽出できず追加の全文監査はない。公開MAC/SSPRK2例は原論文の境界・時間法そのものではない。
- R. FitzHugh (1961). [Impulses and Physiological States in Theoretical Models of Nerve Membrane](https://pubmed.ncbi.nlm.nih.gov/19431309/). PubMedの原著抄録・書誌を確認。2変数の興奮・不応期の縮約という役割を参照し、HH全系や実測膜電位の再現とは区別します。
- J. Nagumo, S. Arimoto and S. Yoshizawa (1962). [An Active Pulse Transmission Line Simulating Nerve Axon](https://ieeexplore.ieee.org/abstract/document/4066548). IEEE出版社の抄録・巻号・頁・DOIを確認。縮約した膜興奮と回路の歴史的な原著として参照し、空間的な伝送線路や回路実験を今回再現したとは扱いません。

## Poisson演算子 → 圧力・Hartree・重力

[HTML](https://hrkoyama.github.io/numerical-methods-atlas/connections/?lang=ja#poisson-fields-ja)

同じLaplacianと線形代数の道具が複数分野に現れる。ただし右辺、符号、境界、平均モード、自己項が変われば、検証済みの一つの解法をそのまま物理へ移せない。

この経路で確認できる範囲：共通のPoisson演算子を、右辺・符号・境界・零モードの異なる物理問題で比較する。既存の周期Taylor–Green圧力投影、固定周期HeのDFT内Hartree項、静的周期PMには各々の範囲の検証がある。この対応は、それらを一つに連成する計画や実行ではなく、Dirichletや他の物理・境界の検証を一般に移せるという主張でもない。

### 製造解で調べるPoisson境界値問題

−∇²u=fの指定したDirichlet問題で、1DのThomas法と2DのCG・幾何多重格子・P1 FEMを比較できる。離散残差と連続解の誤差、FD/FEMの異なるノルムを区別する。

段階の状態: fixed-input

- [Poisson方程式と境界](/numerical-methods-atlas/ja/read/elliptic/)
- [P1有限要素による比較](/numerical-methods-atlas/ja/read/fem/)
- [Thomas法／三重対角消去](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja): educational-example
- [共役勾配法](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja): educational-example
- [幾何マルチグリッドVサイクル](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja): educational-example
- [連続P1 Galerkin有限要素法](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja): educational-example
- [1次元Poisson：Dirichlet正弦解と2次収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/?lang=ja): 既存Thomas解法で −u''=π²sin(πx) を15/31/63内部点で解き、解析解sin(πx)、独立な差分残差、格子幅半減の次数を別々に確認する。
- [2次元Poisson：CG・多重格子とP1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja): 単位正方形のsin(πx)sin(πy)を参照し、CG/MGは15/31/63内部点、P1 FEMは4/8/16分割で細分化。FDの最大誤差と真の残差、FEMの要素内L2誤差とH1半ノルムを独立に評価する。

残る差: 滑らかな固定Dirichlet製造解の範囲。小残差だけで連続解精度や他の境界を保証しない。単一正弦モードのCG反復数は一般性能ではない。

### 周期Taylor–Green渦の圧力投影

一定密度・非圧縮流で圧力補正が速度を発散なしへ投影する。公開例は周期MAC格子のTaylor–Green渦で、速度誤差・粘性減衰・発散を解析参照と調べる。

段階の状態: fixed-input

- [非圧縮流の投影法](/numerical-methods-atlas/ja/read/incompressible/)
- [MAC圧力射影法](https://hrkoyama.github.io/numerical-methods-atlas/methods/projection/?lang=ja): educational-example
- [周期Taylor–Green渦：速度・散逸・発散](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=ja): 既存の2次元MAC投影法・中心対流項・明示SSPRK2を使用。16²/32²/64²で解析的減衰渦と比較し、最細格子はCFL半減でも確認。

残る差: 固定した周期・粘性渦の範囲。壁境界、可変密度、乱流、他分野のPoisson場との連成は未検証。

### 周期DFTの中のHartree場

電子数密度nからHartreeポテンシャルエネルギーv_Hを作り、KS/SCFへ戻す。原子単位系の孤立形は∇²v_H=−4πn。周期DFTでは電子・イオンを含む中性セルと零モード/エネルギー規約を一体で扱う。

段階の状態: component-only

- [周期Heの静的DFTワークフロー](/numerical-methods-atlas/ja/read/periodic-dft/)
- [KSとHartree項](/numerical-methods-atlas/ja/read/quantum-chemistry/#kohn-sham-dft)
- [Kohn–Sham密度汎関数法](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja): educational-example
- [自己無撞着場反復（SCF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja): educational-example
- [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=ja): 固定した1原子単純立方Heセル（格子定数4 bohr、価電子2、非偏極LDA_X＋VWN5、局所GTH）。PySCFを使う実行・検証ワークフロー。11設定でk点・Gaussian軌道基底・FFT補助格子・SCFを別々に比較し、Γ／2³は独立DFTK平面波参照と照合。平衡He結晶・完全基底・金属・一般物質は未検証。

残る差: 周期HeはHartree項を含むDFT全体の部品証拠。独立した汎用Hartree Poissonソルバーや圧力/重力との連成の実行例ではない。

### 周期PM粒子群の静的重力場

周期PMは∇²φ=4πG(ρ−ρ̄)、a=−∇φを用い、CIC割当て・格子場・粒子への戻しを組み合わせる。公開例は質量・内力・自己力の整合性と独立正弦密度場を調べる。

段階の状態: fixed-input

- [粒子重力と周期PM](/numerical-methods-atlas/ja/read/particle-gravity/)
- [孤立・周期・混合境界の区別](/numerical-methods-atlas/ja/read/gravity-boundaries/)
- [Cloud-in-cellの割当てと補間](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja): educational-example
- [FFT粒子格子力](https://hrkoyama.github.io/numerical-methods-atlas/methods/pm/?lang=ja): educational-example
- [周期PM粒子群：質量・内力・格子場](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=ja): 入力JSONに保存した19粒子の周期CIC–FFT–CIC計算。質量、内力和、単粒子自己力、整数箱長移動を確認し、別の正弦密度の解析的周期Poisson場と照合。

残る差: 静的な力・格子場の範囲。全粒子力の独立な厳密周期参照、短距離補正、粒子時間発展、自己重力流体の連成はない。

### Poissonを速度の拘束条件へ使う

共通演算子の対応

**受け渡す量:** 予測速度u*の発散 → 圧力補正 → u^(n+1)=u*−(Δt/ρ)∇p。一定密度の代表形では∇²p=(ρ/Δt)∇·u*。

**共通する数理:** Laplacianの離散線形系を解く道具を共有する。周期/純Neumannでは定数零空間と右辺の適合条件を扱う。

**異なる点:** 基本形−∇²u=fと符号・スケーリングを合わせる。動圧かp/ρか、MAC配置、離散grad/divの組合せ、速度境界から導く圧力境界が重要になる。

**既存の要素根拠:** Poisson製造解の例と、別の周期Taylor–Green投影例がある。Dirichlet製造解の合格だけで投影全体を検証したとはしない。

**接続に必要な検証:** 圧力残差に加え投影後の離散発散と速度/圧力誤差を測り、圧力定数のゲージを合わせる。壁では境界条件を再導出し、時間刻みと空間格子を細かくする。

対応関係を比較する範囲：共通のPoisson演算子を比較する対応。周期Taylor–Greenの圧力投影は既存例の速度・減衰・発散の検証範囲で確認済み。Dirichlet製造解や他の境界の合格を周期投影へ移す一般化した橋の実行はない。

### Poissonを自己無撞着な電子場へ使う

共通演算子の対応

**受け渡す量:** 電子数密度n → v_H → KS軌道 → 新しいn。エネルギーはE_H=½∫n v_Hで二重計数を避ける。

**共通する数理:** 密度から楕円型方程式でポテンシャルを作る点を共有する。SCFではこの場の誤差が非線形反復に戻る。

**異なる点:** v_Hは電子の反発ポテンシャルエネルギーで、重力φとは符号・単位が違う。Hartreeの自己相互作用と交換相関、イオンEwald項、点電荷の自己項は別々の概念。周期零モードを中性セル全体の規約と整合させる。

**既存の要素根拠:** periodic-he-dftは固定中性Heセルの全エネルギー・再構成・SCFと別DFTK参照を持つ。一般のHartree境界値問題すべてを検証するものではない。

**接続に必要な検証:** 符号・単位・電子数・ポテンシャルのゲージを確認し、Hartree場とエネルギーを同じ境界の独立参照と比較する。補助格子収束とSCF収束を分け、全エネルギーの項別再構成も調べる。

対応関係を比較する範囲：共通のPoisson演算子を比較する対応。周期HeのHartree項は既存の固定中性セルDFT全体のエネルギー・再構成・SCFの検証範囲に含まれる。独立した汎用Hartree検証ではなく、Dirichletや他の境界の検証を移す一般化した橋の実行もない。

### Poissonを重力場と粒子へ使う

共通演算子の対応

**受け渡す量:** 粒子質量 → 格子密度ρ → φ → a=−∇φ → 粒子への補間。ここで公開するのは静的な受け渡しまで。

**共通する数理:** 同じLaplacianの反転やFFTを利用できるが、粒子割当て・微分・補間の組合せ全体が力を決める。

**異なる点:** 周期では平均密度を除く適合条件を用い、孤立では無限遠条件に合うGreen関数を使う。周期の背景/零モード、孤立の軟化、自己力や自己エネルギー補正を同一視しない。

**既存の要素根拠:** periodic-particlesには質量・内力等の整合性と独立正弦密度場の検査がある。粒子群の厳密な周期直接和参照や流体連成の結果はない。

**接続に必要な検証:** 同じ境界・核で製造解/独立参照を用い、残差、場/力の誤差、質量、内力和、自己力を個別に確認する。格子細分化だけで全粒子力の精度を主張せず、時間発展や自己重力流体は別に検証する。

対応関係を比較する範囲：共通のPoisson演算子を比較する対応。静的な周期PMは既存例の質量・内力・自己力の整合性と独立正弦密度場の範囲で確認済み。Dirichletや孤立境界の検証を周期粒子力へ移す一般化した橋の実行はない。

### 一次文献と確認した範囲

- Alexandre Joel Chorin (1968). [Numerical solution of the Navier-Stokes equations](https://math.berkeley.edu/~chorin/chorin68.pdf). 既存書誌の出版社書誌・著者公開原文の確認を継承。今回原文PDFへの到達を確認したが本文は抽出できず追加の全文監査はない。公開MAC/SSPRK2例は原論文の境界・時間法そのものではない。
- M. R. Hestenes and E. Stiefel (1952). [Methods of Conjugate Gradients for Solving Linear Systems](https://nvlpubs.nist.gov/nistpubs/jres/049/6/v49.n06.a08.pdf). 既存CG項目の確認範囲を継承：第2–3節、式(3:1)、410–411頁の丸め誤差の議論。実対称正定値系の反復の出典であり、各物理場の検証ではない。今回の再監査はない。
- W. Kohn and L. J. Sham (1965). [Self-Consistent Equations Including Exchange and Correlation Effects](https://doi.org/10.1103/PhysRev.140.A1133). 既存アトラスの原著書誌・DOIを確認。Kohn–Sham法の原著として引用し、論文全体の数値再現は主張しません。
- J. W. Eastwood and R. W. Hockney (1974). [Shaping the force law in two-dimensional particle-mesh models](https://www.sciencedirect.com/science/article/pii/0021999174900448). 既存PM項目の出版社抄録・書誌確認を継承。2次元の割当てと格子の力誤差の文献であり、公開3次元Green関数の導出・数値検証そのものではない。今回の全文再監査はない。

## 共通する数理

### 時間発展・演算子の分割

核の運動、反応、移流、拡散はいずれも離散化後の時間積分へつながる。安定性、剛性、保存量と分割誤差は対象ごとに確認する。

- [Runge–Kutta法](/numerical-methods-atlas/ja/read/runge-kutta/)

### 楕円型境界値問題・疎行列

Poisson型演算子は圧力投影、Hartree場、重力場に現れる。右辺・符号・境界・零空間・自己項が異なれば別の問題になる。

- [楕円型方程式](/numerical-methods-atlas/ja/read/elliptic/)

### 非線形反復・自己無撞着性

SCFや陰的反応更新では残差を減らす反復が必要になる。小さな代数残差、離散化の収束、物理モデルの妥当性を分ける。

- [疎行列・非線形方程式](/numerical-methods-atlas/ja/read/sparse-nonlinear/)

### 固有値・安定性・分散関係

固有値はKS軌道、反応平衡の安定性、拡散モードの減衰などに現れる。同じ固有値計算でも、固有値の物理的意味と検証する量は異なる。

- [安定性の基礎](/numerical-methods-atlas/ja/read/stability/)

### 確率分布・揺らぎ・標本化

熱浴やMCMCでは平均だけでなく分布・相関・有限標本誤差を調べます。不変密度の式、R-hat≈1、大きなESSだけでは有限時間の探索や輸送特性は保証されません。MCMCの診断対照をMDや熱浴の連成検証へ流用しません。

- [サーモスタットの比較](/numerical-methods-atlas/ja/read/thermostats/)
- [MCMC：不変分布・混合・診断の違い](/numerical-methods-atlas/ja/read/mcmc/)
- [2峰混合と独立診断比較の固定例](/numerical-methods-atlas/ja/read/validation-mcmc/)

根拠の出典: [Connection catalog](https://hrkoyama.github.io/catalog/atlas-crossovers.json) · [Method registry](https://hrkoyama.github.io/numerical-methods-atlas/methods/index.json) · [Common execution registry](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json) · [Common-registry rerun receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Supplement biology: [independently-extracted-supplement](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json); SHA-256=5cafaaef809f46e6ab01327107f7367113b8069931621fc92d446fbf142682bd

Supplement models: [independently-extracted-supplement](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json); SHA-256=f792796e62b62c7be4eaa2d36fa460481563ac3e535e10c838a0a2e4502af3b2

Supplement thermostats: [independently-extracted-supplement](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json); SHA-256=c14f55ac05d93269dbf8eef4a2a4042f75764d5228d06f8e41039d0b60351905

# Crossovers between numerical fields

Explore quantum chemistry, molecular dynamics, reaction–diffusion, biology, fluids and gravity through exchanged quantities and shared mathematics. Each connection states its validation needs and distinguishes runnable fixed examples, reading-only stages and unexecuted coupling.

Common-registry executions and fixed checks from independently extracted supplements are separate evidence. Scoped Langevin-oscillator, reaction–diffusion, Turing and excitability examples do not establish the complete first-principles-MD-to-heat-bath or reaction–diffusion–fluid route.

## DFT → first-principles MD → temperature control

[HTML](https://hrkoyama.github.io/numerical-methods-atlas/connections/?lang=en#dft-md-en)

Move from static electronic structure to nuclear forces, trajectories and a heat bath. Follow fixed-He forces and separate classical Langevin/CSVR distribution, fluctuation and correlation checks, then inspect the remaining first-principles-MD coupling requirements.

Evidence scope of this route: Static He and multiatom-He2 forces are runnable; the BOMD interface has only a short local check. Langevin/CSVR harmonic/quartic distributions and correlations are checked in separate classical supplements. The complete BOMD/CPMD-to-heat-bath route remains unexecuted.

### Fixed-cell periodic-He KS-LDA

Runnable: a fixed one-He, two-valence-electron cell with lattice constant 4 bohr. A PySCF driver uses LDA_X plus VWN5 and local GTH, separating k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF checks. Gamma and 2³ meshes have separately executed DFTK references.

Stage state: fixed-input

- [Periodic DFT: fixed model and measured results](/numerical-methods-atlas/en/read/periodic-dft/)
- [Kohn–Sham density functional theory / DFT](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en): educational-example
- [Self-consistent field iteration / SCF](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en): educational-example
- [Electronic-structure basis sets](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=en): educational-example
- [LDA, GGA and hybrid functionals](https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=en): educational-example
- [Pseudopotentials and PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=en): educational-example
- [Periodic electronic structure and k-point sampling](https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=en): educational-example
- [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=en): Fixed one-atom simple-cubic He cell (lattice constant 4 bohr, two valence electrons, unpolarized LDA_X plus VWN5, local GTH). A PySCF execution/validation workflow. Eleven settings separately compare k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF; Gamma and 2³ are compared with independent DFTK plane waves. Equilibrium helium, complete-basis, metals and general materials remain unvalidated.

Remaining gap: Limited to the static fixed model. It does not validate equilibrium helium, general materials, forces, stress or MD trajectories.

### From energy to nuclear forces

Obtain F_I = −∂E_BO/∂R_I from the converged electronic energy as a function of nuclear coordinates R. Position-dependent bases require Pulay terms, and pseudopotential force contributions must be consistent.

Stage state: fixed-input

- [From DFT to forces: finite differences, independent reference and refinement](/numerical-methods-atlas/en/read/periodic-forces/)
- [Kohn–Sham density functional theory / DFT](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en): educational-example
- [Electronic-structure basis sets](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=en): educational-example
- [Self-consistent field iteration / SCF](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en): educational-example
- [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=en): Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated.

Remaining gap: Validation is limited to fixed He₂, local GTH and VWN5. Other elements, nonlocal pseudopotentials, stress, metals and long MD trajectories remain unvalidated.

### BOMD and Car–Parrinello MD

BOMD advances nuclei after converging the electronic ground state at each geometry. The force package provides a velocity-Verlet interface and a one-step/two-half-step local check. Overall BOMD and CPMD records remain reading only; long NVE and CP fictitious-mass/orthogonality validation are separate.

Stage state: reading

- [BOMD and CPMD comparison](/numerical-methods-atlas/en/read/periodic-dft/#first-principles-md)
- [BOMD force interface and local check](/numerical-methods-atlas/en/read/periodic-forces/#bomd-interface)
- [Born–Oppenheimer molecular dynamics / BOMD](https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=en): reading-only
- [Car–Parrinello molecular dynamics / CPMD](https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=en): reading-only

Remaining gap: Long BOMD NVE drift and systematic timestep/SCF trajectory convergence, and a dedicated CPMD implementation, remain unpublished. The short interface check does not validate complete trajectories.

### Thermostats and distribution checks

Two of the 12 methods have dedicated implementations: Langevin and CSVR. Preserve the earlier one-degree-of-freedom harmonic Langevin/BAOAB case. A separate edition compares both baths with the same OBABO splitting for a nondegenerate two-degree harmonic system and a two-degree anharmonic system with quartic coefficient lambda=0.2, and checks the standalone CSVR kinetic-energy kernel. The other 10 methods remain planned.

Stage state: scoped-supplement

- [Temperature control and distribution comparisons](/numerical-methods-atlas/en/read/thermostats/)
- [Langevin oscillator: measured distributions, correlations and steps](/numerical-methods-atlas/en/read/validation-models/#langevin-harmonic)
- [CSVR and Langevin: distributions, fluctuations and method-dependent correlations](/numerical-methods-atlas/en/read/validation-thermostats/)
- [Nosé–Hoover thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover/?lang=en): planned
- [Nosé–Hoover chains](https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover-chains/?lang=en): planned
- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en): educational-example
- [Stochastic velocity rescaling (CSVR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en): educational-example

Separately managed fixed supplements: Retain the earlier one harmonic-oscillator degree of freedom with Langevin/BAOAB. Add separate two-degree CSVR/Langevin comparisons with the same OBABO splitting (harmonic and quartic lambda=0.2), plus a scoped CSVR-kernel diagnostic. They consume neither BOMD/CPMD nuclear geometries nor interatomic forces and do not couple DFT to a heat bath.
- [Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en): Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations.
  Distribution checks use a harmonic potential and fixed seeds. Exact position variance does not remove finite-step momentum bias. Evidence does not transfer to other thermostats, general molecules or long ab initio MD.
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-models/#langevin-harmonic)
- [Exact CSVR bath: conditional laws, fluctuations and kinetic correlation](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=en): Implement the bath-only CSVR update for 1, 2 and 6 degrees of freedom; compare exact conditional moments/noncentral-chi-square laws, canonical Gamma fluctuations and kinetic correlations.
  A bath diagnostic, not another independent physical problem. Correct K sampling does not thermalize momentum directions by global scaling alone. The bath-only exp(−t/tau) identity is not a full-MD kinetic ACF. Statistical decisions apply to fixed seeds/budgets, not general mixing guarantees.
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-thermostats/#csvr-kinetic-kernel)
- [CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en): Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations.
  Global-CSVR and local-Langevin dynamical correlations are not required to agree. CDF errors are maxima over five declared points, not whole-line KS distances. Canonical-start preservation and the heated-start finite-time check do not prove ergodicity; tests retain an invariant unexcited-axis counterexample. No extrapolation to molecules, constraints or BOMD.
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-thermostats/#csvr-langevin-harmonic)
- [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en): Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.
  A small example for one separable two-mode quartic potential and fixed seeds. H is not treated as harmonic Gamma. No independent exact full-system dynamical reference is claimed, and neither matching correlations nor time order hidden by sampling noise is an acceptance claim. Molecular transport, quantum and ab initio MD are outside scope.
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-thermostats/#csvr-langevin-quartic)

Remaining gap: Dedicated implementations cover two methods; the other 10 methods are unimplemented. The new two-degree harmonic/quartic comparisons and CSVR kernel are separate classical components, alongside the retained BAOAB case. Distinguish equilibrium distributions/fluctuations from bath-dependent correlations, without transferring evidence to general many-body or first-principles-MD coupling.

### Check energy derivatives against forces in a multiatom cell

Quantity handoff

**Exchanged quantity:** Nuclear geometry R → electronic density and E_BO(R) → nuclear forces F_I.

**Shared mathematics:** Solve a related KS/SCF problem at each geometry and differentiate its energy. Electronic truncation errors also affect forces.

**What differs:** Scalar total-energy agreement and vector force agreement are separate tests. Derivatives must account for basis motion, pseudopotentials, ionic terms and incomplete SCF convergence.

**Existing component evidence:** Separate from the one-atom static example, periodic-he-forces saves asymmetric-He₂ analytic forces, all-six-coordinate finite differences, independent DFTK references and basis/k/SCF/FFT refinement.

**Validation required:** Compare forces with centered finite-difference energy gradients at displaced geometries without symmetry-protected cancellation; refine displacement, basis, auxiliary grid, k sampling and SCF tolerance separately.

Connection validated for the fixed example: The energy-to-force connection is validated for the fixed He₂ model. This evidence does not transfer to general materials or complete MD.

### Pass forces into time evolution

Quantity handoff

**Exchanged quantity:** BOMD: update nuclear positions and momenta from F_I at each step. CPMD: evolve nuclei and fictitious electronic degrees together under orthogonality constraints.

**Shared mathematics:** Nuclear equations require time integration. Coupling to electronic structure introduces iteration, time-step and constraint errors.

**What differs:** Electronic minimization in BOMD differs from fictitious orbital dynamics in CPMD. CP mass and fictitious energy are not physical electronic temperature or excitation.

**Existing component evidence:** The periodic-He₂ force provider is connected to velocity-Verlet, reconverging SCF at each geometry and comparing one step with two half steps. This is not CPMD implementation or long-NVE evidence.

**Validation required:** First, without a thermostat, measure BOMD drift of physical nuclear kinetic plus BO energy versus step size and SCF tolerance. For CP, distinguish drift of the conserved extended energy from exchange in nuclear-plus-BO energy; also check fictitious mass/step size, orthogonality, adiabatic separation and sensitivity relative to BO trajectories.

Local interface check only: A short local step comparison checks the BOMD force interface. Long trajectories, NVE drift and thermostat validation remain to be done.

### From trajectories to a heat bath and statistics

Quantity handoff

**Exchanged quantity:** Exchange nuclear momentum/kinetic energy with heat-bath friction or stochastic terms. For T = 2K/(f k_B), specify active degrees f after constraints and removed center-of-mass motion.

**Shared mathematics:** ODE/SDE integration overlaps with distribution sampling. Step size and bath coupling time affect sampling and correlations.

**What differs:** Correct mean temperature establishes neither canonical sampling nor ergodicity. A bath can change diffusion and velocity correlations. Keep nuclear and fictitious electronic temperatures distinct in CP.

**Existing component evidence:** The earlier BAOAB case, new same-OBABO CSVR/Langevin harmonic/quartic comparisons and a CSVR-kernel Gamma/CIR diagnostic provide classical component evidence. They check temperature/energy distributions, fluctuations and method-dependent correlations. They are independent of the first-principles force API; no trajectory joins the two.

**Validation required:** Use oscillators/ideal gases to check position distributions and the chi-square distribution of kinetic energy, autocorrelations and independent-stream uncertainty; vary step size and coupling time. Include small-system sampling failures before coupling to nuclear MD.

Coupled execution: not performed. Thermostatted first-principles MD has not been executed.

### Primary references and scope of review

- W. Kohn and L. J. Sham (1965). [Self-Consistent Equations Including Exchange and Correlation Effects](https://doi.org/10.1103/PhysRev.140.A1133). Original bibliography and DOI checked against the existing Atlas. Cited as the Kohn–Sham source without claiming numerical reproduction of the entire paper.
- M. Born and R. Oppenheimer (1927). [Zur Quantentheorie der Molekeln](https://onlinelibrary.wiley.com/doi/10.1002/andp.19273892002). Publisher bibliography and DOI checked. Cited for the historical basis of Born–Oppenheimer separation, without claiming a full-text audit or reproduction of a modern MD implementation.
- R. Car and M. Parrinello (1985). [Unified Approach for Molecular Dynamics and Density-Functional Theory](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.2471). Publisher bibliography/abstract and original equations (3)–(5) and discussion of fictitious electronic motion near the BO surface consulted. The paper’s silicon dynamics have not been numerically reproduced.
- William G. Hoover (1985). [Canonical dynamics: Equilibrium phase-space distributions](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.31.1695). Existing thermostat-registry primary reference. Publisher metadata/abstract checked for extended phase-space distributions and the harmonic-oscillator example. No full-paper audit or numerical reproduction.
- B. Leimkuhler and C. Matthews (2013). [Rational Construction of Stochastic Numerical Methods for Molecular Sampling](https://arxiv.org/abs/1203.5428). Author manuscript abstract, Langevin equation and BAOAB update in the appendix (printed page 22) checked. The original long molecular runs and general-system superconvergence are not reproduced here.
- G. Bussi, D. Donadio and M. Parrinello (2007). [Canonical sampling through velocity rescaling](https://arxiv.org/html/0803.4060v1). Checked author-manuscript sections II.1–II.3, kinetic SDE (7), and appendix A (16)–(22); consult the author correction for Gamma-based squared-noise generation.

## Reaction–diffusion → biological and fluid transport

[HTML](https://hrkoyama.github.io/numerical-methods-atlas/connections/?lang=en#reaction-transport-en)

Linear modes, finite-amplitude nonlinear evolution, post-growth patterns and zero-dimensional excitability require different checks. Follow independent references and space/time refinement for fixed 1D Schnakenberg systems toward the additional validation needed for fluid coupling.

Evidence scope of this route: Fixed 1D periodic nonlinear Schnakenberg evolution/post-growth patterns have independent-reference and space/time refinement checks; linear reaction–diffusion and zero-dimensional FHN retain separate examples. Logistic/SIR, advection and periodic flow are also component evidence. The complete reaction–diffusion–advection/fluid route remains unexecuted.

### Reaction–diffusion framework

Specify kinetics, diffusion, initial data and boundaries; distinguish linear Fourier modes, linear Schnakenberg onset, finite-amplitude nonlinear evolution and post-growth patterns. New fixed 1D periodic cases compare centered-difference diffusion/implicit-midpoint reaction Strang splitting with independent dealiased Fourier–Galerkin/Radau references.

Stage state: scoped-supplement

- [Biological models and proposed reaction–diffusion checks](/numerical-methods-atlas/en/read/biological-models/)
- [Space/time refinement for linear reaction–diffusion](/numerical-methods-atlas/en/read/validation-models/#reaction-diffusion-fourier)
- [Nonlinear Schnakenberg/post-growth patterns: independent references and refinement](/numerical-methods-atlas/en/read/validation-biology/)
- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en): educational-example
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en): educational-example
- [Implicit midpoint](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en): educational-example

Separately managed fixed supplements: Preserve the earlier linear-mode examples and separate space/time errors for nonlinear solutions and post-growth patterns in a fixed 1D periodic Schnakenberg system. Radau on the same finite-difference semidiscretization isolates time error and is distinct from the independent continuum-PDE reference. No general biological-model or fluid-coupling certification.
- [Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en): Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.
  Only a linear, periodic, smooth single mode is verified. Nonlinear Fisher fronts, complex boundaries, spatial ecosystems and general reaction networks remain outside scope.
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-models/#reaction-diffusion-fourier)
- [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en): Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.
  One near-equilibrium onset experiment. No claim reproduces original-paper parameters/experiments, mature patterns, wavenumber selection from random noise or biological calibration.
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-models/#turing-schnakenberg)
- [Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en): Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.
  A selected-symmetry1D educational model: no test of free noise-driven wavenumber selection, phase stability,2D spots or biological calibration. Not an original-paper reproduction. Implicit midpoint is A-stable but not L-stable or unconditionally positive; reactions do not conserve u+v. The initial coarse protocol failed; temporal resolution was strengthened while retaining every acceptance threshold and the failed record. No quantum calculations.
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology/#schnakenberg-nonlinear)
- [Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en): Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.
  A selected-symmetry1D educational model: no test of free noise-driven wavenumber selection, phase stability,2D spots or biological calibration. Not an original-paper reproduction. Implicit midpoint is A-stable but not L-stable or unconditionally positive; reactions do not conserve u+v. The initial coarse protocol failed; temporal resolution was strengthened while retaining every acceptance threshold and the failed record. No quantum calculations. Near-saturation refers to the reference90→100 test window; it proves no exact steady state, nonlinear stability or long-term attractor. A huge late linearized difference diagnoses failure of linearization, not numerical error.
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology/#schnakenberg-pattern)

Remaining gap: Limited to fixed 1D periodic problems. General kinetics, nonperiodic boundaries, Fisher–KPP fronts and advective reaction–diffusion coupled to flow remain unvalidated. Diffusion-only and reaction–diffusion evidence are distinct.

### Biology: nonlinear patterns, excitability and fronts

Validate linear onset, finite-amplitude evolution and post-growth patterns for 1D periodic Schnakenberg, and zero-dimensional FitzHugh–Nagumo stimulus response. Independent nonlinear references and grid/time refinement do not establish tissue calibration or verification of Fisher–KPP fronts.

Stage state: scoped-supplement

- [Fisher–KPP front](/numerical-methods-atlas/en/read/biological-models/#06-1937-fisherkpp-invasion-front)
- [Turing pattern onset](/numerical-methods-atlas/en/read/biological-models/#09-1952-turing-reactiondiffusion-framework)
- [Schnakenberg kinetics](/numerical-methods-atlas/en/read/biological-models/#17-1979-schnakenberg-reactiondiffusion)
- [Initial Turing growth and independent references](/numerical-methods-atlas/en/read/validation-models/#turing-schnakenberg)
- [Zero-dimensional FitzHugh–Nagumo stimulus response](/numerical-methods-atlas/en/read/validation-models/#fitzhugh-nagumo)
- [Nonlinear Schnakenberg/post-growth patterns: independent references and refinement](/numerical-methods-atlas/en/read/validation-biology/)
- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en): educational-example
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en): educational-example
- [Implicit midpoint](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en): educational-example

Separately managed fixed supplements: Separate fixed components: 1D Schnakenberg linear onset, nonlinear evolution and post-growth patterns, and zero-dimensional FitzHugh–Nagumo stimulus response. Distinguish independent-reference and space/time errors; no spatial membrane-propagation claim.
- [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en): Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.
  One near-equilibrium onset experiment. No claim reproduces original-paper parameters/experiments, mature patterns, wavenumber selection from random noise or biological calibration.
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-models/#turing-schnakenberg)
- [FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en): Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853.
  Scoped verification of an FHN/BVP-style reduced ODE. It excludes full HH ion channels, spatial axons, patient data and experimental electrophysiology reproduction.
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-models/#fitzhugh-nagumo)
- [Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en): Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.
  A selected-symmetry1D educational model: no test of free noise-driven wavenumber selection, phase stability,2D spots or biological calibration. Not an original-paper reproduction. Implicit midpoint is A-stable but not L-stable or unconditionally positive; reactions do not conserve u+v. The initial coarse protocol failed; temporal resolution was strengthened while retaining every acceptance threshold and the failed record. No quantum calculations.
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology/#schnakenberg-nonlinear)
- [Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en): Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.
  A selected-symmetry1D educational model: no test of free noise-driven wavenumber selection, phase stability,2D spots or biological calibration. Not an original-paper reproduction. Implicit midpoint is A-stable but not L-stable or unconditionally positive; reactions do not conserve u+v. The initial coarse protocol failed; temporal resolution was strengthened while retaining every acceptance threshold and the failed record. No quantum calculations. Near-saturation refers to the reference90→100 test window; it proves no exact steady state, nonlinear stability or long-term attractor. A huge late linearized difference diagnoses failure of linearization, not numerical error.
  [Supplement receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json) · [Code/tests ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip) · [Detailed reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology/#schnakenberg-pattern)

Remaining gap: Schnakenberg checks use fixed reflection-symmetric initial data, finite times and one spatial dimension. General pattern selection, 2D morphology, propagating membrane pulses, Fisher front speeds, biological calibration and fluid coupling remain unvalidated. FHN has no spatial dimension.

### Runnable zero-dimensional reaction-only examples

Logistic growth compares RK4 with an analytic single-population solution. SIR compares RK4 with independent DOP853 for a closed well-mixed population, checking conservation, nonnegativity and time refinement. Neither has a spatial dimension.

Stage state: fixed-input

- [Fixed logistic-growth example](/numerical-methods-atlas/en/read/biological-models/#01-1838-logistic-population-growth)
- [Fixed closed-SIR example](/numerical-methods-atlas/en/read/biological-models/#05-1927-sir-and-seir-compartment-models)
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en): educational-example
- [Logistic growth: analytic solution and time refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=en): One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.
- [SIR: independent DOP853 reference, conservation and convergence](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=en): Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.

Remaining gap: Evidence for reaction-only ODEs. It establishes no diffusion, advection, spatial spread, SEIR implementation or coupled reaction–diffusion validation.

### Concentration and reaction fields carried by flow

One conservative form is ∂_t c + ∇·(u c) = ∇·(D∇c) + R(c). With ∇·u=0 it reduces to advective form. Separate a passive scalar in prescribed flow from active feedback through density, buoyancy or other constitutive relations.

Stage state: component-only

- [Constant-speed advection component](/numerical-methods-atlas/en/read/stability/)
- [Periodic incompressible-flow component](/numerical-methods-atlas/en/read/incompressible/)
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en): educational-example
- [MAC pressure projection](https://hrkoyama.github.io/numerical-methods-atlas/methods/projection/?lang=en): educational-example
- [Periodic sine advection: upwind and analytic transport](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=en): Advance q_t+a q_x=0 for one period on a unit periodic interval. Compare first-order upwind on 64/128 points with an analytically translated sine, exporting computed, analytic and error values.
- [Periodic Taylor–Green vortex: velocity, decay and divergence](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=en): Use existing two-dimensional MAC projection, centered convection and explicit SSPRK2. Compare analytic decaying vortex on 16²/32²/64² grids and halve CFL on the finest grid.

Remaining gap: Advection and Taylor–Green runs are separate components. No execution couples concentration, reaction and flow or measures their splitting error.

### One PDE family, different biological questions

Model application

**Exchanged quantity:** Specify kinetics, diffusion and boundaries, then observe front position or spatial-mode amplitudes.

**Shared mathematics:** Both integrate discretized diffusion and reaction sources; the reaction Jacobian and Laplacian spectrum govern stability.

**What differs:** Front-speed error differs from a Turing dispersion relation. Resemblance to a biological pattern establishes neither mechanism nor parameter validity.

**Existing component evidence:** Schnakenberg supplements extend the earlier linear onset to finite-amplitude nonlinear evolution and post-growth patterns from fixed 1D periodic data, with independent Fourier–Galerkin/Radau references and separate space/time refinement. FHN retains a zero-dimensional DOP853 comparison; Fisher–KPP fronts are unexecuted.

**Validation required:** For fronts, compare analytic profile/speed and separate finite-boundary, spatial and temporal errors. For Turing onset, establish k=0 stability and compare early growth of boundary-admissible nonzero modes with J−k²D and the discrete-Laplacian prediction.

Scope of the model-family correspondence: The fixed spatial Schnakenberg example is independent component validation. Generalization across biological-model families, tissue-level validity and the complete bridge to fronts or flow have not been executed.

### Inspect reaction baselines without spatial terms

Component comparison

**Exchanged quantity:** A spatially uniform no-transport limit gives the ODE from R(c). Released logistic/SIR runs verify only their own specified reaction laws.

**Shared mathematics:** ODE integration, temporal refinement and nonnegativity checks provide a starting point for reaction updates.

**What differs:** Logistic growth is scalar growth; SIR transfers population fractions between compartments. Individual species need not be conserved, SIR’s balance does not transfer to arbitrary R, and these examples have no spatial boundary.

**Existing component evidence:** logistic-growth and sir-epidemic are zero-dimensional executions compared with analytic or independent numerical references. They provide no spatial-spread evidence.

**Validation required:** Recheck equilibria, nonnegativity, temporal refinement and source-aware balances for the actual coupled kinetics. Passing an ODE test leaves positivity and convergence after splitting with diffusion/advection to be verified.

Scope of the component reference: Coupling the reaction components to diffusion or transport has not been executed.

### Add advection and define exchange with flow

Quantity handoff

**Exchanged quantity:** Pass velocity u from flow to concentration. An active model returns buoyancy, density, reaction heat or other quantities defined by its chosen constitutive law.

**Shared mathematics:** Combine reaction, advection and diffusion operators on one time axis. Incompressible pressure projection separately requires a Poisson solve.

**What differs:** Equivalence of conservative and advective forms requires conditions such as ∇·u=0. Advection CFL, diffusion step restrictions, reaction stiffness and pressure boundaries differ, as do passive and two-way coupling errors.

**Existing component evidence:** Linear/nonlinear Schnakenberg reaction–diffusion, post-growth patterns, periodic advection and Taylor–Green flow are separate component checks. Measured reaction/diffusion Strang error does not establish splitting error for coupled concentration, advection and flow.

**Validation required:** Check concentration balance with boundary fluxes and reaction sources, nonnegativity, ∇·u, space/time refinement and splitting order/step dependence. Use a manufactured or independent coupled reference; active coupling also requires force/heat balance checks.

Coupled execution: not performed. Reaction–diffusion–advection and active fluid coupling have not been executed.

### Primary references and scope of review

- Pierre-François Verhulst (1847). [Sur la loi d’accroissement de la population (Deuxième mémoire)](https://www.persee.fr/doc/marb_0775-3225_1847_num_20_1_3457). Inherits the existing bibliography’s original-text/metadata review. This is the later 1847 memoir; the original 1838 note remains unaudited. No fresh full-text audit was performed.
- W. O. Kermack and A. G. McKendrick (1927). [A contribution to the mathematical theory of epidemics](https://doi.org/10.1098/rspa.1927.0118). Inherits the biological-model chapter/execution-registry primary reference. The original framework is broader than the released closed well-mixed SIR specialization. No fresh full-text audit or reproduction of the whole paper.
- R. A. Fisher (1937). [The wave of advance of advantageous genes](https://doi.org/10.1111/j.1469-1809.1937.tb02153.x). Inherits existing publisher-metadata/original-excerpt checks. A population-genetic front source. The independent KPP original remains unaudited; no numerical reproduction is added.
- Alan M. Turing (1952). [The Chemical Basis of Morphogenesis](https://www.damtp.cam.ac.uk/user/gold/pdfs/teaching/old_literature/Turing1952.pdf). Inherits the existing university-hosted original-text review of model setting and instability premise. The general two-species form is not a unique Turing kinetic law. The DOI endpoint was inaccessible in this pass; no added full-text audit or numerical reproduction.
- Jürgen Schnakenberg (1979). [Simple chemical reaction systems with limit cycle behaviour](https://www.sciencedirect.com/science/article/pii/0022519379900420). Inherits existing publisher-metadata/abstract checks. An autocatalytic-kinetics source, not numerical validation of a spatial PDE or tissue-calibrated model. No fresh full-text audit.
- Alexandre Joel Chorin (1968). [Numerical solution of the Navier-Stokes equations](https://math.berkeley.edu/~chorin/chorin68.pdf). Inherits existing publisher/author-hosted-original checks. The original PDF was reachable in this pass but yielded no extracted body, so no fresh text audit was added. The released MAC/SSPRK2 example differs from the original boundary/time algorithm.
- R. FitzHugh (1961). [Impulses and Physiological States in Theoretical Models of Nerve Membrane](https://pubmed.ncbi.nlm.nih.gov/19431309/). Original-paper abstract and bibliography in PubMed checked. Supports the two-variable excitable/refractory reduction; no full HH or measured membrane-voltage reproduction is claimed.
- J. Nagumo, S. Arimoto and S. Yoshizawa (1962). [An Active Pulse Transmission Line Simulating Nerve Axon](https://ieeexplore.ieee.org/abstract/document/4066548). IEEE publisher abstract, volume, pages and DOI checked. Historical source for reduced excitation and its circuit analogue; no spatial transmission-line or hardware-experiment reproduction is claimed.

## Poisson operators → pressure, Hartree and gravity

[HTML](https://hrkoyama.github.io/numerical-methods-atlas/connections/?lang=en#poisson-fields-en)

Laplacians and linear-algebra tools recur across fields. Changing the source, sign, boundaries, mean mode or self terms requires fresh validation before transferring a solver into another physical model.

Evidence scope of this route: Compare a shared Poisson operator across physical problems with different sources, signs, boundaries and zero modes. Existing periodic Taylor–Green pressure projection, the Hartree term within fixed periodic-He DFT and static periodic PM each have validation in their own scope. This correspondence neither proposes nor executes their coupling, and does not transfer validation generally from Dirichlet or other physical/boundary settings.

### Poisson boundary problems with manufactured solutions

For specified Dirichlet problems −∇²u=f, compare 1D Thomas and 2D CG, geometric multigrid and P1 FEM. Separate discrete residuals from continuum error and distinguish FD/FEM norms.

Stage state: fixed-input

- [Poisson equations and boundaries](/numerical-methods-atlas/en/read/elliptic/)
- [P1 finite-element comparison](/numerical-methods-atlas/en/read/fem/)
- [Thomas tridiagonal elimination](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en): educational-example
- [Conjugate gradients](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en): educational-example
- [Geometric multigrid V-cycle](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en): educational-example
- [Continuous P1 Galerkin FEM](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en): educational-example
- [1D Poisson: Dirichlet sine solution and second-order refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/?lang=en): Use the existing Thomas kernel for −u''=π²sin(πx) with 15/31/63 interior nodes; separately check analytic sin(πx), a recomputed discrete residual and halving-grid refinement.
- [2D Poisson: CG, multigrid and P1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en): Reference sin(πx)sin(πy) on the unit square; refine CG/MG through 15/31/63 interior nodes and P1 FEM through 4/8/16 subdivisions. Independently evaluate FD maximum errors/true residuals and FEM element-interior L2/H1-seminorm errors.

Remaining gap: Limited to fixed smooth Dirichlet manufactured solutions. A small residual alone establishes neither continuum accuracy nor other boundaries. One-sine-mode CG iteration counts do not establish general performance.

### Pressure projection for a periodic Taylor–Green vortex

In constant-density incompressible flow, a pressure correction projects velocity toward a divergence-free field. The released periodic MAC Taylor–Green case checks velocity error, viscous decay and divergence against an analytic reference.

Stage state: fixed-input

- [Incompressible-flow projection](/numerical-methods-atlas/en/read/incompressible/)
- [MAC pressure projection](https://hrkoyama.github.io/numerical-methods-atlas/methods/projection/?lang=en): educational-example
- [Periodic Taylor–Green vortex: velocity, decay and divergence](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=en): Use existing two-dimensional MAC projection, centered convection and explicit SSPRK2. Compare analytic decaying vortex on 16²/32²/64² grids and halve CFL on the finest grid.

Remaining gap: Limited to the fixed periodic viscous vortex. Walls, variable density, turbulence and coupling to other-domain Poisson fields remain unvalidated.

### Hartree field inside periodic DFT

Build the Hartree potential energy v_H from electron number density n and return it to KS/SCF. Its isolated atomic-unit form is ∇²v_H=−4πn. Periodic DFT requires a neutral electron–ion cell and consistent zero-mode/energy conventions.

Stage state: component-only

- [Static periodic-He DFT workflow](/numerical-methods-atlas/en/read/periodic-dft/)
- [KS and the Hartree term](/numerical-methods-atlas/en/read/quantum-chemistry/#kohn-sham-dft)
- [Kohn–Sham density functional theory / DFT](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en): educational-example
- [Self-consistent field iteration / SCF](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en): educational-example
- [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=en): Fixed one-atom simple-cubic He cell (lattice constant 4 bohr, two valence electrons, unpolarized LDA_X plus VWN5, local GTH). A PySCF execution/validation workflow. Eleven settings separately compare k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF; Gamma and 2³ are compared with independent DFTK plane waves. Equilibrium helium, complete-basis, metals and general materials remain unvalidated.

Remaining gap: Periodic He provides component evidence from a full DFT calculation containing Hartree terms. It is no standalone general Hartree-Poisson solver or pressure/gravity coupling example.

### Static gravitational field of periodic PM particles

Periodic PM uses ∇²φ=4πG(ρ−ρ̄), a=−∇φ, combining CIC assignment, a mesh field and interpolation back to particles. The released example checks mass, net internal force, self-force consistency and a separate sinusoidal density field.

Stage state: fixed-input

- [Particle gravity and periodic PM](/numerical-methods-atlas/en/read/particle-gravity/)
- [Isolated, periodic and mixed boundaries](/numerical-methods-atlas/en/read/gravity-boundaries/)
- [Cloud-in-cell assignment and interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en): educational-example
- [FFT particle–mesh forces](https://hrkoyama.github.io/numerical-methods-atlas/methods/pm/?lang=en): educational-example
- [Periodic PM particles: mass, internal force and mesh field](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=en): Periodic CIC–FFT–CIC calculation for 19 particles stored explicitly in input JSON. Check mass, net internal force, single-particle self-force and integer-box translation; separately compare a sinusoidal density with analytic periodic Poisson fields.

Remaining gap: Limited to static forces and mesh fields. No independent exact periodic reference for every particle force, short-range correction, particle evolution or coupled self-gravitating fluid is provided.

### Use Poisson to enforce a velocity constraint

Shared operator correspondence

**Exchanged quantity:** Divergence of predicted velocity u* → pressure correction → u^(n+1)=u*−(Δt/ρ)∇p. A representative constant-density form is ∇²p=(ρ/Δt)∇·u*.

**Shared mathematics:** Shares linear-system tools for a discrete Laplacian. Periodic/pure-Neumann problems require a constant nullspace treatment and source compatibility.

**What differs:** Align the sign and scaling with −∇²u=f. Specify dynamic pressure versus p/ρ, MAC placement, matched discrete grad/div and pressure boundaries derived from velocity conditions.

**Existing component evidence:** Poisson manufactured examples and a separate periodic Taylor–Green projection example exist. Passing a Dirichlet solve alone does not validate a complete projection method.

**Validation required:** Measure post-projection discrete divergence and velocity/pressure errors as well as pressure residuals, with pressure gauges aligned. Re-derive wall boundaries and refine time step and mesh.

Scope of the operator correspondence: A correspondence through a shared Poisson operator. Periodic Taylor–Green pressure projection is already checked within the existing velocity, decay and divergence scope. No generalized bridge run transfers Dirichlet manufactured-solution or other-boundary validation to periodic projection.

### Use Poisson for a self-consistent electronic field

Shared operator correspondence

**Exchanged quantity:** Electron number density n → v_H → KS orbitals → updated n. E_H=½∫n v_H avoids double counting the pair contribution.

**Shared mathematics:** Both construct a potential from a source through an elliptic equation. In SCF, field error feeds back into nonlinear iteration.

**What differs:** v_H is an electron-repulsion potential energy, with signs/units different from gravitational φ. Hartree self-interaction and exchange-correlation, ionic Ewald terms and point-charge self terms are distinct concepts. Align periodic zero modes with the whole neutral-cell convention.

**Existing component evidence:** periodic-he-dft includes fixed neutral-He energy/reconstruction/SCF checks and a separate DFTK reference. It does not validate every Hartree boundary problem.

**Validation required:** Check signs, units, electron count and potential gauge; compare Hartree fields/energies against an independent reference with the same boundaries. Separate auxiliary-grid and SCF refinement and check component-wise total-energy reconstruction.

Scope of the operator correspondence: A correspondence through a shared Poisson operator. The periodic-He Hartree term belongs to the already checked energy, reconstruction and SCF scope of the full fixed neutral-cell DFT example. This is not standalone general Hartree validation, and no generalized bridge run transfers validation from Dirichlet or other boundaries.

### Use Poisson for gravity and particles

Shared operator correspondence

**Exchanged quantity:** Particle masses → mesh density ρ → φ → a=−∇φ → interpolation to particles. Released evidence stops at this static exchange.

**Shared mathematics:** Laplacian inversions or FFT tools can recur, while particle assignment, differentiation and interpolation together determine the force.

**What differs:** Periodic compatibility removes the mean density; isolated fields require a Green function with the far-field condition. Distinguish periodic background/zero modes, isolated softening, self-force and self-energy corrections.

**Existing component evidence:** periodic-particles supplies mass/net-force consistency and an independent sinusoidal-density field check. It has no exact periodic pair-sum reference for the particle set or fluid-coupling result.

**Validation required:** Use manufactured/independent references with matching boundaries and kernels; separately check residual, field/force error, mass, net force and self-force. Mesh refinement alone does not establish all particle-force errors; evolution and self-gravitating flow need separate validation.

Scope of the operator correspondence: A correspondence through a shared Poisson operator. Static periodic PM is already checked within its mass, net-force, self-force consistency and independent sinusoidal-density-field scope. No generalized bridge run transfers Dirichlet or isolated-boundary validation to periodic particle forces.

### Primary references and scope of review

- Alexandre Joel Chorin (1968). [Numerical solution of the Navier-Stokes equations](https://math.berkeley.edu/~chorin/chorin68.pdf). Inherits existing publisher/author-hosted-original checks. The original PDF was reachable in this pass but yielded no extracted body, so no fresh text audit was added. The released MAC/SSPRK2 example differs from the original boundary/time algorithm.
- M. R. Hestenes and E. Stiefel (1952). [Methods of Conjugate Gradients for Solving Linear Systems](https://nvlpubs.nist.gov/nistpubs/jres/049/6/v49.n06.a08.pdf). Inherits CG-record review: sections 2–3, (3:1), and rounding-error discussion on pp. 410–411. A real-SPD iteration source, not validation of each physical field. No fresh audit.
- W. Kohn and L. J. Sham (1965). [Self-Consistent Equations Including Exchange and Correlation Effects](https://doi.org/10.1103/PhysRev.140.A1133). Original bibliography and DOI checked against the existing Atlas. Cited as the Kohn–Sham source without claiming numerical reproduction of the entire paper.
- J. W. Eastwood and R. W. Hockney (1974). [Shaping the force law in two-dimensional particle-mesh models](https://www.sciencedirect.com/science/article/pii/0021999174900448). Inherits PM-record publisher-abstract/metadata checks. Concerns 2D assignment/mesh-force error, not derivation or numerical validation of the released 3D Green function. No fresh full-text audit.

## Shared mathematics

### Time evolution and operator splitting

Nuclear motion, reactions, advection and diffusion lead to time integration after discretization. Stability, stiffness, balances and splitting error require problem-specific checks.

- [Runge–Kutta methods](/numerical-methods-atlas/en/read/runge-kutta/)

### Elliptic boundary problems and sparse systems

Poisson-type operators appear in pressure projection, Hartree fields and gravity. Different sources, signs, boundaries, nullspaces and self terms define different problems.

- [Elliptic equations](/numerical-methods-atlas/en/read/elliptic/)

### Nonlinear iteration and self-consistency

SCF and implicit reaction updates require iterative residual reduction. Separate algebraic residuals, discretization convergence and physical-model validity.

- [Sparse and nonlinear systems](/numerical-methods-atlas/en/read/sparse-nonlinear/)

### Eigenvalues, stability and dispersion

Eigenvalues describe KS orbitals, reaction-equilibrium stability and diffusion-mode decay. Their physical interpretation and validation targets differ even when the algebra overlaps.

- [Stability foundations](/numerical-methods-atlas/en/read/stability/)

### Probability distributions, fluctuations and sampling

Thermostats and MCMC require distributions, correlations and finite-sample uncertainty as well as means. Invariant-density formulas, R-hat near one or large ESS do not guarantee finite-time exploration or transport properties. MCMC diagnostic controls do not establish MD/thermostat coupling.

- [Thermostat comparisons](/numerical-methods-atlas/en/read/thermostats/)
- [MCMC: invariance, mixing and diagnostic limits](/numerical-methods-atlas/en/read/mcmc/)
- [Fixed bimodal-mixture and independent-diagnostic comparisons](/numerical-methods-atlas/en/read/validation-mcmc/)

Evidence sources: [Connection catalog](https://hrkoyama.github.io/catalog/atlas-crossovers.json) · [Method registry](https://hrkoyama.github.io/numerical-methods-atlas/methods/index.json) · [Common execution registry](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json) · [Common-registry rerun receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Supplement biology: [independently-extracted-supplement](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json); SHA-256=5cafaaef809f46e6ab01327107f7367113b8069931621fc92d446fbf142682bd

Supplement models: [independently-extracted-supplement](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json); SHA-256=f792796e62b62c7be4eaa2d36fa460481563ac3e535e10c838a0a2e4502af3b2

Supplement thermostats: [independently-extracted-supplement](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json); SHA-256=c14f55ac05d93269dbf8eef4a2a4042f75764d5228d06f8e41039d0b60351905
