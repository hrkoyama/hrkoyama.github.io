# Wall heating：Noh問題と反射壁の数値的な過熱

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/wall-heating/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Rusanov／局所Lax–Friedrichs流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja>)
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja>)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja>)
  availability: run

  初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。
- [Noh問題：実際の2次元Cartesian Euler計算](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja>)
  availability: run

  正方形の全域で密度・2成分運動量・全エネルギーを更新する、小型の2次元Euler有限体積計算です。32²・64²・128²の3格子で厳密Noh状態からの誤差・保存収支・格子方向の影響を測ります。図は実際の2次元保存配列で、1D半径解の回転表示ではありません。
- [Sedov–Taylor点爆発：球対称の軽量検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja>)
  availability: run

  球対称Euler方程式を半径方向の有限体積法で解く軽量例です。固定した半径0.03の領域に総エネルギー1を与え、128・256・512セルで点爆発の相似参照からの差と保存収支を測ります。図は1次元球対称データの断面表示で、2次元Cartesian計算ではありません。
- [2D吸収影と保存的M1輸送](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja>)
  availability: run

  実際の円形吸収体の影を、特性線の円弦減衰・角度輸送・M1で比較します。
- [2D反向beamとM1閉包の情報損失](<https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja>)
  availability: run

  保存した反向packetの実進行からM1の限界を示し、別の閉M1MMSで数値実装を検証します。
- [Saltzman型の歪み格子ピストン：2次元EulerとALE](<https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=ja>)
  availability: run

  2023年版の歪み格子と有限初期圧力を明示した、所与の格子移動による2次元Eulerピストン計算。
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
- [Shu–Osher：独立参照と格子収束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=ja>)
  availability: run

  衝撃波と密度正弦波の相互作用を、同じPython実装の細格子ではなく、別に実行したAthena++の参照と照合します。
- [Euler二重膨張波：段階ごとの正値性](<https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja>)
  availability: run

  既存の強い二重希薄波を128/256/512セルで計算し、平均保存型の正値性スケーリングをMUSCL・大域LF流束・SSPRK(3,3)へ接続します。各前進Euler段と各SSP凸結合の密度・圧力・境界保存収支を記録します。
- [低Mach等エントロピー渦：前処理Roe流束の軽量検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja>)
  availability: run

  同じ非線形2次元Euler渦をN=16/32/64、背景Mach数.1/.01でT=.1まで進め、通常RoeとMiczek型の空間流束前処理を比較します。全12計算で、速度・動圧スケールの圧力誤差、保存収支、音響刻み、実段状態を調べます。
- [Brio–Wu：HLLDと保存的に粗視化した数値参照](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/brio-wu/?lang=ja>)
  availability: run

  γ=2、Bx=0.75の1次元理想MHD衝撃波管をt=0.1まで計算。HLLD＋MC＋SSPRK2の64/128セルを512セルの数値参照と比較し、密度・圧力・縦磁場・保存収支・切替回数を記録する。
- [Zalesak型2D回転輸送：保存・有界性・形状誤差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja>)
  availability: run

  スロット付き円盤を実際の2次元有限体積法で一回転させ、donor-cellとminmod MUSCLを比較します。3格子と、半セルの中心ずらし・45度の初期向きを含む8計算で、保存・各SSP段の有界性・形状誤差とスロットの埋まりを測ります。
- [SRHDの対称二衝撃波衝突](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja>)
  availability: run

  相対論的な対称衝突を、独立なTaub関係から得る厳密な保存量セル平均と比較し、実際の1D時空間場を保存します。
- [SRMHDの有限振幅円偏極Alfvén波](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja>)
  availability: run

  完全な磁気応力と誘導を含むSRMHDで非線形有限振幅波を1周期進め、厳密セル平均、位相、振幅と細分化を検査します。
- [Rusanov／局所Lax–Friedrichs流束：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Heun法／SSPRK(2,2)：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [MUSCL再構成：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Minmod：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
