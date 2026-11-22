# 分野をつなぐ数値計算の入口

量子化学・分子動力学・反応拡散・生物・流体・重力を、受け渡す量と共通の数学からたどる。矢印ごとに必要な検証を示し、実行できる固定例、解説のみの段階、未実行の連成を区別する。

実行済みの要素例と、未検証の分野間接続を分けて示します。単独例の合格だけで、力・MD・温度制御・反応拡散などの連成を検証済みとはしません。

## DFT → 第一原理MD → 温度制御

[HTML](https://hrkoyama.github.io/numerical-methods-atlas/connections/?lang=ja#dft-md-ja)

静的な電子状態から核の力、軌道、熱浴へ。公開の周期Heエネルギー計算を出発点に、まだ検証されていない橋を明示する。

この経路で確認できる範囲：固定Heの静的エネルギー計算のみ実行可能。力・BOMD/CPMD・熱浴までを結ぶ第一原理MDの経路全体は未実行。

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

段階の状態: reading

- [力と第一原理MDへの未検証の接続](/numerical-methods-atlas/ja/read/periodic-dft/#first-principles-md)
- [Kohn–Sham密度汎関数法](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja): educational-example
- [電子状態計算の基底](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=ja): educational-example
- [自己無撞着場反復（SCF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja): educational-example

残る差: 力の実装・変位による有限差分照合・力の基底/SCF収束は未公開。1原子の対称位置でゼロ力を得るだけでは一般の力を検証できない。

### BOMD・Car–Parrinello MD

解説のみ。BOMDは各核配置で電子基底状態を十分に収束させて核を進める。CPMDは直交制約の下で仮想電子質量を持つ軌道と核を連成し、BO面近傍の断熱分離を管理する。CPMDの仮想電子運動は実時間TDDFTとは異なる。

段階の状態: reading

- [BOMDとCPMDの比較](/numerical-methods-atlas/ja/read/periodic-dft/#first-principles-md)
- [Born–Oppenheimer分子動力学（BOMD）](https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=ja): reading-only
- [カー–パリネロ法（CPMD）](https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=ja): reading-only

残る差: 両手法とも台帳はreading-only。核の時間発展、NVEエネルギードリフト、CPの仮想質量依存性の数値結果はない。

### サーモスタットと分布の確認

比較解説を公開し、実装は計画中。Nosé–Hoover、chains、Langevin、確率的速度再スケーリングなどを、平均温度・運動エネルギー分布・相関の観点で比較する。

段階の状態: planned

- [温度制御と分布の比較](/numerical-methods-atlas/ja/read/thermostats/)
- [Nosé–Hooverサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover/?lang=ja): planned
- [Nosé–Hoover chain](https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover-chains/?lang=ja): planned
- [Langevinサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja): planned
- [確率的速度リスケーリング（CSVR）](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja): planned

残る差: 各サーモスタットの台帳はplannedのまま。専用実行例、温度分布の測定、第一原理MDとの連成検証はない。

### 収束したエネルギーだけでは力は未検証

量を受け渡す接続

**受け渡す量:** 核配置R → 電子密度・E_BO(R) → 核の力F_I。

**共通する数理:** 同じKS/SCF問題を核配置ごとに解き、そのエネルギーの幾何微分を使う。電子計算の打切り誤差は力にも伝わる。

**異なる点:** スカラーの全エネルギー比較とベクトルの力の比較は別の検査。基底の位置依存性、擬ポテンシャル、イオン項とSCF未収束を微分に反映する。

**既存の要素根拠:** periodic-he-dftには固定Heセルのエネルギー・SCF・k点/基底等の証拠がある。力の検証値はない。

**接続に必要な検証:** 対称性に守られない変位配置で力を中心有限差分のエネルギー勾配と比較し、変位幅・基底・補助格子・k点・SCF公差を独立に細かくする。

連成実行：未実施。固定セルの静的実行例から力計算へ渡す接続は未実行・未検証。

### 力を時間発展へ渡す

量を受け渡す接続

**受け渡す量:** BOMD：各時刻のF_Iから核の位置・運動量を更新。CPMD：核と仮想電子自由度を直交制約付きで同時に更新。

**共通する数理:** 核の運動方程式は時間積分の問題。電子構造との連成では反復誤差・時間刻み・拘束誤差を同時に管理する。

**異なる点:** BOMDの電子最小化とCPMDの仮想軌道ダイナミクスは異なる。CPの仮想質量やエネルギーは物理的な電子温度・電子励起ではない。

**既存の要素根拠:** BOMD・CPMDの原文献と比較解説がある。固定Heの静的結果は力やMDの保存則の証拠にはならない。

**接続に必要な検証:** まずサーモスタットなしで、BOMDは物理的な核の運動＋BOエネルギーのNVEドリフトを時間刻み・SCF公差に対して測る。CPでは保存すべき拡張エネルギーと核＋BOエネルギーの交換を区別し、仮想質量/刻み幅、直交性、断熱分離とBO軌道への感度も調べる。

連成実行：未実施。力と核の積分器を結んだBOMD/CPMDのローカル実行例はない。

### 軌道から熱浴・統計へ

量を受け渡す接続

**受け渡す量:** 核の運動量・運動エネルギーと熱浴の摩擦/確率項を交換する。T = 2K/(f k_B)では拘束・重心運動を除いた有効自由度fを明記する。

**共通する数理:** 常微分/確率微分方程式と分布の標本化が重なる。有限時間刻みと熱浴結合時間は標本化と相関の両方に影響する。

**異なる点:** 平均温度の一致だけでは正準分布やエルゴード性を示さない。熱浴は拡散・速度相関を変え得る。CPでは核と仮想電子自由度の温度を混同しない。

**既存の要素根拠:** サーモスタットの比較解説と検証計画を公開。専用コード・分布の測定結果・MDとの連成結果はない。

**接続に必要な検証:** 調和振動子・理想気体などで位置分布とKのχ²分布、自己相関、独立系列の不確かさを確認し、刻み幅と結合時間を変える。核MDとの連成前に小自由度の探索失敗も調べる。

連成実行：未実施。サーモスタット付き第一原理MDは未実行。

### 一次文献と確認した範囲

- W. Kohn and L. J. Sham (1965). [Self-Consistent Equations Including Exchange and Correlation Effects](https://doi.org/10.1103/PhysRev.140.A1133). 既存アトラスの原著書誌・DOIを確認。Kohn–Sham法の原著として引用し、論文全体の数値再現は主張しません。
- M. Born and R. Oppenheimer (1927). [Zur Quantentheorie der Molekeln](https://onlinelibrary.wiley.com/doi/10.1002/andp.19273892002). 出版社の書誌・DOIを確認。Born–Oppenheimer分離の歴史的基礎として引用し、原文全文の監査や現代のMD実装の再現は主張しません。
- R. Car and M. Parrinello (1985). [Unified Approach for Molecular Dynamics and Density-Functional Theory](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.2471). 出版社の書誌・抄録と公開原文の式(3)–(5)、BO面近傍の仮想電子運動の議論を参照。論文のSi動力学の数値再現は行っていません。
- William G. Hoover (1985). [Canonical dynamics: Equilibrium phase-space distributions](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.31.1695). 既存サーモスタット台帳の原著。今回出版社の書誌・抄録を確認し、拡張位相空間分布と調和振動子の例の範囲を参照。全文の監査・数値再現は未実施。

## 反応拡散 → 生物・流体の輸送

[HTML](https://hrkoyama.github.io/numerical-methods-atlas/connections/?lang=ja#reaction-transport-ja)

反応源と拡散演算子を共有しても、侵入前線・模様・流れとの連成では検証量が変わる。0次元反応と輸送の部品例から、未実装の空間連成を見分ける。

この経路で確認できる範囲：0次元反応・移流・周期流体の例は別々の証拠。空間反応拡散や反応・拡散・流れを結ぶ経路全体は未実行。

### 反応と拡散の枠組み

∂_t c = ∇·(D∇c) + R(c)。反応則R、拡散係数/行列D、初期条件、空間境界を指定して初めて問題になる。台帳のFisher–KPP・Turing・Schnakenbergは解説のみ。

段階の状態: reading

- [生物モデルと反応拡散の検証案](/numerical-methods-atlas/ja/read/biological-models/)

残る差: 反応拡散の空間ソルバーや連成実行例は公開されていない。拡散だけの例を足しても連成の検証にはならない。

### 生物：侵入前線と模様形成

Fisher–KPPは増殖と拡散の前線、Turingは安定な反応平衡が空間モードで不安定化する枠組み。Schnakenbergは具体的な反応則の一例であり、Turing原論文の反応則や組織較正済みモデルと同一ではない。

段階の状態: reading

- [Fisher–KPP前線](/numerical-methods-atlas/ja/read/biological-models/#06-1937-fisherkpp-invasion-front)
- [Turing型の模様発生](/numerical-methods-atlas/ja/read/biological-models/#09-1952-turing-reactiondiffusion-framework)
- [Schnakenbergの反応則](/numerical-methods-atlas/ja/read/biological-models/#17-1979-schnakenberg-reactiondiffusion)

残る差: いずれもsurvey-onlyのモデル。前線速度・モード成長率の測定も、生物の実験データによる妥当性確認も未実施。

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

**既存の要素根拠:** 解説に前線・モードの検証案と一次文献がある。測定した反応拡散の結果はない。

**接続に必要な検証:** 前線は解析プロファイル/速度と比較し、有限領域の境界影響と空間/時間誤差を分ける。Turingはk=0の安定性を確かめ、境界が許す非零モードの初期成長をJ−k²Dおよび離散Laplacianの予測と比べる。

空間モデルの実行：未実施。反応拡散の生物モデルとしての空間実行は未実施。

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

**既存の要素根拠:** advection-sineは周期一定速度のスカラー移流、taylor-greenは周期粘性流と発散を別々に検証する。濃度や反応を含む連成結果はない。

**接続に必要な検証:** 境界流束と反応源を含む濃度収支、非負性、∇·u、空間/時間収束、分割順序・刻み依存を調べる。製造解または独立な連成参照を設け、能動連成では返す力/熱の収支も確認する。

連成実行：未実施。反応・拡散・移流または流体との能動連成は未実行。

### 一次文献と確認した範囲

- Pierre-François Verhulst (1847). [Sur la loi d’accroissement de la population (Deuxième mémoire)](https://www.persee.fr/doc/marb_0775-3225_1847_num_20_1_3457). 既存書誌の原文・書誌確認を継承。1847年の後期論文であり、1838年の最初の短報を監査したとはしない。今回の原文再監査は行っていない。
- W. O. Kermack and A. G. McKendrick (1927). [A contribution to the mathematical theory of epidemics](https://doi.org/10.1098/rspa.1927.0118). 既存生物モデル章と実行台帳の一次文献を継承。原論文の一般的な枠組みは公開例の閉鎖・均質SIRより広い。今回の全文再監査・論文全体の数値再現は行っていない。
- R. A. Fisher (1937). [The wave of advance of advantageous genes](https://doi.org/10.1111/j.1469-1809.1937.tb02153.x). 既存書誌の出版社書誌・原文抜粋の確認を継承。集団遺伝の前線の出典。独立のKPP原著の監査は未実施。今回の数値再現はない。
- Alan M. Turing (1952). [The Chemical Basis of Morphogenesis](https://www.damtp.cam.ac.uk/user/gold/pdfs/teaching/old_literature/Turing1952.pdf). 既存書誌にある大学公開原文のモデル設定・不安定性の前提の確認を継承。一般の2成分式を一意のTuring反応則とは扱わない。今回DOI先は取得不可で、追加の全文監査や数値再現は行っていない。
- Jürgen Schnakenberg (1979). [Simple chemical reaction systems with limit cycle behaviour](https://www.sciencedirect.com/science/article/pii/0022519379900420). 既存書誌の出版社書誌・抄録確認を継承。自己触媒反応系の出典であり、空間PDEや組織に較正したモデルの数値検証ではない。今回の全文再監査はない。
- Alexandre Joel Chorin (1968). [Numerical solution of the Navier-Stokes equations](https://math.berkeley.edu/~chorin/chorin68.pdf). 既存書誌の出版社書誌・著者公開原文の確認を継承。今回原文PDFへの到達を確認したが本文は抽出できず追加の全文監査はない。公開MAC/SSPRK2例は原論文の境界・時間法そのものではない。

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

熱浴を付けたMDでは平均温度だけでなく分布・相関・有限標本誤差を調べる。不変分布の式だけでは有限時間の探索や輸送特性は保証されない。

- [サーモスタットの比較](/numerical-methods-atlas/ja/read/thermostats/)

根拠の出典: [Connection catalog](https://hrkoyama.github.io/catalog/atlas-crossovers.json) · [Method registry](https://hrkoyama.github.io/numerical-methods-atlas/methods/index.json) · [Execution registry](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json) · [Rerun receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-periodic.json)

# Crossovers between numerical fields

Explore quantum chemistry, molecular dynamics, reaction–diffusion, biology, fluids and gravity through exchanged quantities and shared mathematics. Each connection states its validation needs and distinguishes runnable fixed examples, reading-only stages and unexecuted coupling.

Executed component examples and unvalidated cross-field connections are shown separately. A passing standalone case does not validate coupled forces, MD, thermostatting or reaction–diffusion.

## DFT → first-principles MD → temperature control

[HTML](https://hrkoyama.github.io/numerical-methods-atlas/connections/?lang=en#dft-md-en)

Move from static electronic structure to nuclear forces, trajectories and a heat bath. Start with the released periodic-He energy calculation and identify each unvalidated bridge.

Evidence scope of this route: Only the static fixed-He energy calculation is runnable. The complete first-principles-MD route through forces, BOMD/CPMD and a heat bath has not been executed.

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

Stage state: reading

- [Unvalidated bridge to forces and first-principles MD](/numerical-methods-atlas/en/read/periodic-dft/#first-principles-md)
- [Kohn–Sham density functional theory / DFT](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en): educational-example
- [Electronic-structure basis sets](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=en): educational-example
- [Self-consistent field iteration / SCF](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en): educational-example

Remaining gap: No published force implementation, displaced-geometry finite-difference comparison or force basis/SCF convergence. A zero force at a symmetric one-atom position would not validate general forces.

### BOMD and Car–Parrinello MD

Reading only. BOMD advances nuclei while sufficiently converging the electronic ground state at each geometry. CPMD couples nuclei and orbitals with fictitious electronic mass under orthogonality constraints and requires adiabatic separation near the BO surface. Its fictitious orbital motion is distinct from real-time TDDFT.

Stage state: reading

- [BOMD and CPMD comparison](/numerical-methods-atlas/en/read/periodic-dft/#first-principles-md)
- [Born–Oppenheimer molecular dynamics / BOMD](https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=en): reading-only
- [Car–Parrinello molecular dynamics / CPMD](https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=en): reading-only

Remaining gap: Both method records remain reading-only. There are no nuclear-trajectory, NVE-energy-drift or CP-fictitious-mass-dependence results.

### Thermostats and distribution checks

Comparative reading is available; implementations are planned. Compare Nosé–Hoover, chains, Langevin and stochastic velocity rescaling through mean temperature, kinetic-energy distributions and correlations.

Stage state: planned

- [Temperature control and distribution comparisons](/numerical-methods-atlas/en/read/thermostats/)
- [Nosé–Hoover thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover/?lang=en): planned
- [Nosé–Hoover chains](https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover-chains/?lang=en): planned
- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en): planned
- [Stochastic velocity rescaling (CSVR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en): planned

Remaining gap: Thermostat method records remain planned. There are no dedicated execution examples, measured temperature distributions or coupled first-principles-MD validations.

### Converged energy leaves forces unvalidated

Quantity handoff

**Exchanged quantity:** Nuclear geometry R → electronic density and E_BO(R) → nuclear forces F_I.

**Shared mathematics:** Solve a related KS/SCF problem at each geometry and differentiate its energy. Electronic truncation errors also affect forces.

**What differs:** Scalar total-energy agreement and vector force agreement are separate tests. Derivatives must account for basis motion, pseudopotentials, ionic terms and incomplete SCF convergence.

**Existing component evidence:** periodic-he-dft provides fixed-He energy, SCF, k-sampling and basis evidence. It contains no validated force values.

**Validation required:** Compare forces with centered finite-difference energy gradients at displaced geometries without symmetry-protected cancellation; refine displacement, basis, auxiliary grid, k sampling and SCF tolerance separately.

Coupled execution: not performed. The bridge from the static fixed-cell example to force evaluation has not been executed or validated.

### Pass forces into time evolution

Quantity handoff

**Exchanged quantity:** BOMD: update nuclear positions and momenta from F_I at each step. CPMD: evolve nuclei and fictitious electronic degrees together under orthogonality constraints.

**Shared mathematics:** Nuclear equations require time integration. Coupling to electronic structure introduces iteration, time-step and constraint errors.

**What differs:** Electronic minimization in BOMD differs from fictitious orbital dynamics in CPMD. CP mass and fictitious energy are not physical electronic temperature or excitation.

**Existing component evidence:** Primary references and comparative reading exist for BOMD/CPMD. Static fixed-He results provide no force or MD conservation evidence.

**Validation required:** First, without a thermostat, measure BOMD drift of physical nuclear kinetic plus BO energy versus step size and SCF tolerance. For CP, distinguish drift of the conserved extended energy from exchange in nuclear-plus-BO energy; also check fictitious mass/step size, orthogonality, adiabatic separation and sensitivity relative to BO trajectories.

Coupled execution: not performed. No local execution example couples nuclear integration with validated forces in BOMD or CPMD.

### From trajectories to a heat bath and statistics

Quantity handoff

**Exchanged quantity:** Exchange nuclear momentum/kinetic energy with heat-bath friction or stochastic terms. For T = 2K/(f k_B), specify active degrees f after constraints and removed center-of-mass motion.

**Shared mathematics:** ODE/SDE integration overlaps with distribution sampling. Step size and bath coupling time affect sampling and correlations.

**What differs:** Correct mean temperature establishes neither canonical sampling nor ergodicity. A bath can change diffusion and velocity correlations. Keep nuclear and fictitious electronic temperatures distinct in CP.

**Existing component evidence:** Thermostat comparisons and a validation plan are published. There are no dedicated code, measured distributions or coupled MD results.

**Validation required:** Use oscillators/ideal gases to check position distributions and the chi-square distribution of kinetic energy, autocorrelations and independent-stream uncertainty; vary step size and coupling time. Include small-system sampling failures before coupling to nuclear MD.

Coupled execution: not performed. Thermostatted first-principles MD has not been executed.

### Primary references and scope of review

- W. Kohn and L. J. Sham (1965). [Self-Consistent Equations Including Exchange and Correlation Effects](https://doi.org/10.1103/PhysRev.140.A1133). Original bibliography and DOI checked against the existing Atlas. Cited as the Kohn–Sham source without claiming numerical reproduction of the entire paper.
- M. Born and R. Oppenheimer (1927). [Zur Quantentheorie der Molekeln](https://onlinelibrary.wiley.com/doi/10.1002/andp.19273892002). Publisher bibliography and DOI checked. Cited for the historical basis of Born–Oppenheimer separation, without claiming a full-text audit or reproduction of a modern MD implementation.
- R. Car and M. Parrinello (1985). [Unified Approach for Molecular Dynamics and Density-Functional Theory](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.2471). Publisher bibliography/abstract and original equations (3)–(5) and discussion of fictitious electronic motion near the BO surface consulted. The paper’s silicon dynamics have not been numerically reproduced.
- William G. Hoover (1985). [Canonical dynamics: Equilibrium phase-space distributions](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.31.1695). Existing thermostat-registry primary reference. Publisher metadata/abstract checked for extended phase-space distributions and the harmonic-oscillator example. No full-paper audit or numerical reproduction.

## Reaction–diffusion → biological and fluid transport

[HTML](https://hrkoyama.github.io/numerical-methods-atlas/connections/?lang=en#reaction-transport-en)

Reaction sources and diffusion operators recur across fronts, patterns and flow coupling, while validation targets change. Separate zero-dimensional reaction and transport component examples from unimplemented spatial coupling.

Evidence scope of this route: Zero-dimensional reaction, advection and periodic-flow examples provide separate evidence. Spatial reaction–diffusion and the complete reaction–diffusion–flow route have not been executed.

### Reaction–diffusion framework

∂_t c = ∇·(D∇c) + R(c). A problem requires a reaction law R, diffusivity/matrix D, initial data and spatial boundaries. Catalogued Fisher–KPP, Turing and Schnakenberg entries provide reading only.

Stage state: reading

- [Biological models and proposed reaction–diffusion checks](/numerical-methods-atlas/en/read/biological-models/)

Remaining gap: No spatial reaction–diffusion solver or coupled execution example is released. Adding a separate diffusion example does not validate the combination.

### Biology: invasion fronts and pattern onset

Fisher–KPP concerns growth–diffusion fronts; Turing describes spatial-mode destabilization of a stable reaction equilibrium. Schnakenberg supplies one kinetic law, distinct from Turing’s original example and from a tissue-calibrated model.

Stage state: reading

- [Fisher–KPP front](/numerical-methods-atlas/en/read/biological-models/#06-1937-fisherkpp-invasion-front)
- [Turing pattern onset](/numerical-methods-atlas/en/read/biological-models/#09-1952-turing-reactiondiffusion-framework)
- [Schnakenberg kinetics](/numerical-methods-atlas/en/read/biological-models/#17-1979-schnakenberg-reactiondiffusion)

Remaining gap: All remain survey-only models. Front-speed and mode-growth measurements and validation against biological observations have not been performed.

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

**Existing component evidence:** Reading supplies front/mode verification plans and primary references. There are no measured reaction–diffusion results.

**Validation required:** For fronts, compare analytic profile/speed and separate finite-boundary, spatial and temporal errors. For Turing onset, establish k=0 stability and compare early growth of boundary-admissible nonzero modes with J−k²D and the discrete-Laplacian prediction.

Spatial-model execution: not performed. Spatial execution of these biological reaction–diffusion models has not been performed.

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

**Existing component evidence:** advection-sine checks scalar periodic constant-speed transport; taylor-green separately checks periodic viscous flow and divergence. Neither supplies concentration–reaction–flow results.

**Validation required:** Check concentration balance with boundary fluxes and reaction sources, nonnegativity, ∇·u, space/time refinement and splitting order/step dependence. Use a manufactured or independent coupled reference; active coupling also requires force/heat balance checks.

Coupled execution: not performed. Reaction–diffusion–advection and active fluid coupling have not been executed.

### Primary references and scope of review

- Pierre-François Verhulst (1847). [Sur la loi d’accroissement de la population (Deuxième mémoire)](https://www.persee.fr/doc/marb_0775-3225_1847_num_20_1_3457). Inherits the existing bibliography’s original-text/metadata review. This is the later 1847 memoir; the original 1838 note remains unaudited. No fresh full-text audit was performed.
- W. O. Kermack and A. G. McKendrick (1927). [A contribution to the mathematical theory of epidemics](https://doi.org/10.1098/rspa.1927.0118). Inherits the biological-model chapter/execution-registry primary reference. The original framework is broader than the released closed well-mixed SIR specialization. No fresh full-text audit or reproduction of the whole paper.
- R. A. Fisher (1937). [The wave of advance of advantageous genes](https://doi.org/10.1111/j.1469-1809.1937.tb02153.x). Inherits existing publisher-metadata/original-excerpt checks. A population-genetic front source. The independent KPP original remains unaudited; no numerical reproduction is added.
- Alan M. Turing (1952). [The Chemical Basis of Morphogenesis](https://www.damtp.cam.ac.uk/user/gold/pdfs/teaching/old_literature/Turing1952.pdf). Inherits the existing university-hosted original-text review of model setting and instability premise. The general two-species form is not a unique Turing kinetic law. The DOI endpoint was inaccessible in this pass; no added full-text audit or numerical reproduction.
- Jürgen Schnakenberg (1979). [Simple chemical reaction systems with limit cycle behaviour](https://www.sciencedirect.com/science/article/pii/0022519379900420). Inherits existing publisher-metadata/abstract checks. An autocatalytic-kinetics source, not numerical validation of a spatial PDE or tissue-calibrated model. No fresh full-text audit.
- Alexandre Joel Chorin (1968). [Numerical solution of the Navier-Stokes equations](https://math.berkeley.edu/~chorin/chorin68.pdf). Inherits existing publisher/author-hosted-original checks. The original PDF was reachable in this pass but yielded no extracted body, so no fresh text audit was added. The released MAC/SSPRK2 example differs from the original boundary/time algorithm.

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

Thermostatted MD requires distributions, correlations and finite-sample uncertainty as well as mean temperature. An invariant-density formula does not establish finite-time exploration or transport properties.

- [Thermostat comparisons](/numerical-methods-atlas/en/read/thermostats/)

Evidence sources: [Connection catalog](https://hrkoyama.github.io/catalog/atlas-crossovers.json) · [Method registry](https://hrkoyama.github.io/numerical-methods-atlas/methods/index.json) · [Execution registry](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json) · [Rerun receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-periodic.json)
