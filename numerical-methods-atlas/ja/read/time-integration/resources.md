# 時間積分とleapfrog法

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [前進Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja>)
- [後退Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja>)
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)
- [陽的中点RK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/explicit-midpoint/?lang=ja>)
- [Ralston RK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ralston/?lang=ja>)
- [Kutta RK3](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kutta3/?lang=ja>)
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja>)
- [SSPRK(4,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk43/?lang=ja>)
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)
- [SSPRK(5,4)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk54/?lang=ja>)
- [陰的中点則](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja>)
- [2ステップleapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=ja>)
- [速度Verlet／粒子leapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

## 方程式

- [Hamilton系・振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja>)

  正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [有限次元の線形発展系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-evolution-system-ja>)

  減衰回転の物理時刻と、定常残差を減衰させる擬似時間を例ごとに区別します。

## 問題の図

- [調和振動子（複素ODE表示も統合）](<https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/harmonic-oscillator.png

## 厳密解・参照解

- [調和振動子（複素ODE表示も統合）：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=ja#references-ja>)

  正弦・余弦の解析軌道（複素ODE表現を含む）と比較し、位相・エネルギー・写像の幾何学的性質を区別します。専用参照解カードは未収録です。

## コード・検証

- [SWASHES地形流：静水と非零流量の定常解](<https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja>)
  availability: run

  水没・露出した隆起上の静水と、非零流量の亜臨界定常解を別々に検査します。静水の保存と、動く定常流に残る離散化誤差を区別します。
- [乾いた河床のダム破壊：実際のwetting/drying](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja>)
  availability: run

  右半分を厳密にh=q=0として開始する浅水方程式を解き、実際の乾湿前線の進行と保存をRitter解析解と比較します。
- [Su–Olson1996非平衡拡散](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja>)
  availability: run

  実際の放射・物質2場とMarshak境界を進め、固定版ExactPackの独立積分参照と比較します。
- [時間離散拡散の随伴とcheckpoint](<https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja>)
  availability: run

  後退Eulerの離散写像を実際に逆伝播し、接線・独立高精度mode解・block replayと比較します。
- [Robertson保存制約DAEと公式IDA保存値](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja>)
  availability: run

  Robertsonの保存制約DAEと全ODEを同じ固定時間格子で比較し、公式IDA保存値を別に照合します。 初回は元の時間精度・細分化目標4件が未達でした。
- [index-1 DAEの整合初期化と離散残差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja>)
  availability: run

  既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。
- [Double Mach反射：多格子の軽量検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja>)
  availability: run

  既存のDouble Mach反射と同じ初期値・境界を使い、64×16・128×32・256×64の実2D Euler有限体積計算をT=.2まで実行します。別実装の有限格子参照との差、実際の境界流束収支、上部の入射衝撃位置と壁近傍を比較します。
- [Mach 3前向きステップ：壁面収支と多格子検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja>)
  availability: run

  実際の2次元Euler有限体積計算を60×20・120×40・240×80でT=4まで行い、別実装のMUSCL有限格子参照と比較します。段差の垂直面・上面を含む実際の数値流束から4保存量の収支を評価し、角のエントロピー補正を加えない変種として図とコードを公開します。
- [後期Orszag–Tang：独立参照と圧縮構造](<https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja>)
  availability: run

  圧縮性理想MHDのOrszag–TangをT=.2まで進め、相互作用する圧縮・衝撃波構造の密度と圧力を独立有限格子参照で検査します。
- [円偏波Alfvén波：全成分の格子収束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja>)
  availability: run

  全8保存変数を進め、非零のBz・vzを含む円偏波を解析セル平均と比較します。
- [磁場ループ：独立2次元参照と細分化](<https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja>)
  availability: run

  実際の2次元磁場ループ輸送を、別実装Athena++の空間・時間感度を検査した終端保存場と比較します。
- [Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja>)
  availability: run

  初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。
- [Noh問題：実際の2次元Cartesian Euler計算](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja>)
  availability: run

  正方形の全域で密度・2成分運動量・全エネルギーを更新する、小型の2次元Euler有限体積計算です。32²・64²・128²の3格子で厳密Noh状態からの誤差・保存収支・格子方向の影響を測ります。図は実際の2次元保存配列で、1D半径解の回転表示ではありません。
- [Sedov–Taylor点爆発：球対称の軽量検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja>)
  availability: run

  球対称Euler方程式を半径方向の有限体積法で解く軽量例です。固定した半径0.03の領域に総エネルギー1を与え、128・256・512セルで点爆発の相似参照からの差と保存収支を測ります。図は1次元球対称データの断面表示で、2次元Cartesian計算ではありません。
- [Guderley収束衝撃波：球対称の軽量検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja>)
  availability: run

  冷たい静止気体へ内向きに進む球対称Guderley衝撃波を、128/256/512個の球殻でt=−1から−.85まで計算します。HLL流束とHeun法を、相似指数の固有値・半解析場・衝撃位置・保存収支と照合する軽量例です。
- [Re=100蓋駆動キャビティ：Ghia中心線との比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja>)
  availability: run

  非周期・粘性非圧縮の実際の2D計算を17/33/65点格子で定常化し、Ghia原著の速度中心線と比較します。流線・渦中心・真の残差と発散を同時に保存します。
- [非周期壁面の製造解：速度・剪断・圧力演算子](<https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja>)
  availability: run

  キャビティと同じ壁条件付き2Dソルバーに解析外力を与え、速度と流れ関数の格子収束、壁渦度・壁剪断の誤差を測ります。別の非零Dirichlet圧力製造解でPoisson・勾配の境界演算子も検査します。
- [KHの初期成長：滑らかな周期せん断層](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja>)
  availability: run

  実際の非線形2D渦度方程式を解き、独立Fourier–Galerkin線形初期値問題と有限時間の成長・格子誤差を比較します。
- [RTの初期成長：滑らかなBoussinesq二層](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja>)
  availability: run

  密度差を浮力だけに残す2D Boussinesq系を時間発展し、不安定な滑らかな層の初期成長を独立線形参照で調べます。
- [非一様移動格子で実際に運ぶALEスカラー](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja>)
  availability: run

  質量と格子面位置を同じHeun段で更新し、一様GCLだけでなく非一様な解析波を運びます。
- [Su–Olson1997角度輸送の独立公開表比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja>)
  availability: run

  物質交換を含む実際の正負角度輸送を進め、2023原著者公開の解析benchmark表と比較します。
- [2D吸収影と保存的M1輸送](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja>)
  availability: run

  実際の円形吸収体の影を、特性線の円弦減衰・角度輸送・M1で比較します。
- [2D反向beamとM1閉包の情報損失](<https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja>)
  availability: run

  保存した反向packetの実進行からM1の限界を示し、別の閉M1MMSで数値実装を検証します。
- [Euler二重膨張波：段階ごとの正値性](<https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja>)
  availability: run

  既存の強い二重希薄波を128/256/512セルで計算し、平均保存型の正値性スケーリングをMUSCL・大域LF流束・SSPRK(3,3)へ接続します。各前進Euler段と各SSP凸結合の密度・圧力・境界保存収支を記録します。
- [低Mach等エントロピー渦：前処理Roe流束の軽量検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja>)
  availability: run

  同じ非線形2次元Euler渦をN=16/32/64、背景Mach数.1/.01でT=.1まで進め、通常RoeとMiczek型の空間流束前処理を比較します。全12計算で、速度・動圧スケールの圧力誤差、保存収支、音響刻み、実段状態を調べます。
- [Zalesak型2D回転輸送：保存・有界性・形状誤差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja>)
  availability: run

  スロット付き円盤を実際の2次元有限体積法で一回転させ、donor-cellとminmod MUSCLを比較します。3格子と、半セルの中心ずらし・45度の初期向きを含む8計算で、保存・各SSP段の有界性・形状誤差とスロットの埋まりを測ります。
- [SRHDの対称二衝撃波衝突](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja>)
  availability: run

  相対論的な対称衝突を、独立なTaub関係から得る厳密な保存量セル平均と比較し、実際の1D時空間場を保存します。
- [SRMHDの有限振幅円偏極Alfvén波](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja>)
  availability: run

  完全な磁気応力と誘導を含むSRMHDで非線形有限振幅波を1周期進め、厳密セル平均、位相、振幅と細分化を検査します。
- [WENO-JS／Z：臨界点とεの固定比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja>)
  availability: run

  同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。
- [ロジスティック増殖：解析解と刻み幅の収束](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=ja>)
  availability: run

  無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。
- [SIR：独立DOP853参照・人口保存・収束](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=ja>)
  availability: run

  閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。
- [反応拡散：空間2次と時間4次を分けて測る](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja>)
  availability: run

  線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。
- [Turing不安定性：線形成長率と小振幅パターン](<https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja>)
  availability: run

  Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。
- [FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja>)
  availability: run

  2変数の膜興奮縮約ODEを電流パルスで励起し、DOP853との全出力時刻の誤差・時間収束・回復を確認します。
- [2D C-grid回転浅水波の実時間発展](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja>)
  availability: run

  実際の2D staggered場を時間積分し、連続波と離散symbolの参照を分けて比較します。
- [振り子の指数低減・拘束ドリフト・明示安定化](<https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja>)
  availability: run

  位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。
- [酵素反応の保存と準定常近似](<https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja>)
  availability: run

  全4状態と準定常近似を比較し、初期層と積分誤差を分けます。
- [Lotka–Volterra不変量と正値性](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=ja>)
  availability: run

  正の軌道を独立な対数座標参照と比較します。
- [SEIR保存則と初期線形化](<https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=ja>)
  availability: run

  人口保存と2モードの初期線形化を別々に検査します。
- [Schnakenberg有限振幅過渡：非線形性と独立参照](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja>)
  availability: run

  t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。
- [Schnakenberg飽和パターン：近定常性と格子・時間収束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja>)
  availability: run

  t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。
- [Lorentz分散板へのs/p斜め入射](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja>)
  availability: run

  有限波束の実進行から複素r/t・R/T・直接散逸を求め、複素Fresnel参照と比較します。
- [分散媒質の浅い入射角と長時間PML](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja>)
  availability: run

  80度の中心位相角を持つ有限波束をT=700まで進め、境界誤差を同格子の無PML参照から分離します。
- [2D誘電体円柱のMie散乱幅](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja>)
  availability: run

  実際の2D散乱場を進め、閉曲線Poynting流束と独立な円柱級数を比較します。
- [調和振動子：Verletの位相誤差とエネルギー](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=ja>)
  availability: run

  既存の単位質量・単位角振動数の調和振動子をvelocity Verletで進める。20時間単位、200/400/800刻みの解析解比較、元のエネルギー偏差、時間反転を出力。
- [前進Euler法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [後退Euler法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Heun法／SSPRK(2,2)：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [陽的中点RK2：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/explicit-midpoint/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Ralston RK2：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ralston/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Kutta RK3：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kutta3/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [SSPRK(3,3)：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [SSPRK(4,3)：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk43/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [古典的RK4：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [SSPRK(5,4)：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk54/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [陰的中点則：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [2ステップleapfrog法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
