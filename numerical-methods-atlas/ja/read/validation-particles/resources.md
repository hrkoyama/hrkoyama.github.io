# 粒子・静電場・運動論・放射輸送

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-particles/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Ewald法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [Particle Mesh Ewald（PME）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [Smooth PME（SPME）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [高速多重極法の移動演算](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [Particle-in-Cell（PIC）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [DSMC・運動論輸送](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [放射輸送・モーメント法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [Ewald法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=ja>)
- [Particle Mesh Ewald（PME）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/?lang=ja>)
- [Smooth PME（SPME）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=ja>)
- [高速多重極法の移動演算](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=ja>)
- [Particle-in-Cell（PIC）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja>)
- [DSMC・運動論輸送](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja>)
- [放射輸送・モーメント法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja>)

## 方程式

- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 リンクは静電Poisson/Laplace場です。中性周期Coulomb電荷のEwald/PME問題であり、重力の質量・符号・境界を流用しません。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 2次元Poisson/Laplaceの対数Green核を用いる粒子和です。3次元軟化重力1/rモデルとは区別します。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 Poissonへのリンクは自己無撞着な静電場の部分です。粒子の運動・CIC補間を結合したPIC全体の式が一覧に揃っているわけではありません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=ja#ewald-ja-algorithm>)

  erfcで減衰する実空間和、Gaussian係数を持つ構造因子の逆格子和、−alpha/sqrt(pi) sum(q²)を加えます。力は各項の位置微分から求め、24成分を中心エネルギー差分と比較します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=ja#spme-ja-algorithm>)

  4次または6次のcardinal Bスプラインのテンソル積で電荷を格子化し、節点スプラインの離散構造因子補正、Gaussian Green関数、3次元FFTを組み合わせます。格子エネルギーを重みの位置微分で解析的に微分します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=ja#fmm-ja-algorithm>)

  葉でP2M、上向きのM2M、相互作用リスト上のM2L、下向きのL2L、局所多項式の評価と近接P2Pを実装します。遠方を粒子ごとに開くBarnes–Hutへ置き換えず、移動演算回数と近接対数を記録します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja#pic-ja-algorithm>)

  CIC電荷割当てと同じ重みの場補間、ゼロ平均のスペクトルPoisson解、速度Verletを組み合わせます。実数の奇微分の規約により、電場のNyquistモードはゼロにします。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=ja#dsmc-ja-algorithm>)

  対の重心速度と相対速度の大きさを保持し、相対速度の方向を球面上で一様に選びます。roundは物理時刻ではなく衝突演算の回数です。 D=<vx²−(vy²+vz²)/2>と置くと、ランダムな相方の平均で重心の異方性が(N−2)/(2(N−1))倍になり、散乱後の相対方向の異方性期待値はゼロになるため、保存した期待減衰率が得られます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja#radiation-transport-ja-algorithm>)

  正のGauss–Legendre離散方向と1次風上有限体積の空間行進を使います。角度誤差だけを分ける系列では、一定セル内を指数関数で正確に伝播します。

## 問題の図

- [中性周期点電荷：Ewald・smooth PME](<https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/ewald.png
- [2次元対数核のM2M・M2L・L2Lを持つFMM](<https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png
- [CIC静電PICの冷たいプラズマ振動](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png
- [等質DSMC衝突成分の保存則・Maxwell分布](<https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/dsmc.png
- [純吸収平板の離散座標放射輸送](<https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png
- [中性周期セルのEwald和と独立theta積分](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/ewald.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/ewald.png
- [Bスプラインsmooth PMEの格子・次数収束](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/spme.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/spme.png
- [2次元対数核のM2M・M2L・L2Lを持つFMM](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png
- [CIC静電PICの冷たいプラズマ振動](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png
- [等質DSMC衝突成分の保存則・Maxwell分布](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/dsmc.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/dsmc.png
- [純吸収平板の離散座標放射輸送](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png

## 厳密解・参照解

- [中性周期点電荷：Ewald・smooth PME：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja#references-ja>)

  同じ中性周期電荷・規約の収束したEwald和、力の有限差分とカットオフ・格子収束を確認します。孤立重力粒子の直接和とは境界・相互作用が異なります。 追加版は同じ中性8点電荷・立方体・tin-foil規約のエネルギーと全粒子力を、別実装theta積分と参照自身の細分化に照合します。SPMEはB-splineのエネルギー勾配型であり、原Lagrange PMEや厳密運動量保存を主張しません。
- [2次元対数核のM2M・M2L・L2Lを持つFMM：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/?lang=ja#references-ja>)

  同じ2次元対数核と粒子配置の直接和を数値基準に、多重極の次数・階層変換・力誤差を確認します。3次元1/r核の基準は流用しません。 追加版ではCartesian直接和と解析配置を別の基準にし、展開次数と木深さを分離します。深さに対する単調収束や3次元Coulomb核の精度・計算量を保証しません。
- [CIC静電PICの冷たいプラズマ振動：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#references-ja>)

  小振幅の冷たいプラズマの線形変位cos(t)と比較し、電荷整合性・Poisson残差・自己力、格子系列と時間刻み系列を確認します。一般の非線形PIC軌道の厳密解という主張ではありません。 追加版は静止イオン背景のまま、電荷・運動量・粒子と場のエネルギーを軌道誤差と分けます。小振幅線形参照であり、熱的Landau減衰や電磁PICの根拠ではありません。
- [等質DSMC衝突成分の保存則・Maxwell分布：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=ja#references-ja>)

  等質衝突成分の運動量・エネルギー保存、異方性緩和と分布モーメントを確認します。有限粒子数の平衡はmicrocanonicalで、Maxwell/Gamma分布は大粒子数極限の基準です。空間輸送を含むBoltzmann方程式全体の厳密解検証ではありません。 追加版は固定運動量・エネルギー球面の有限粒子数モーメントを導出し、独立な射影正規標本と複数seedで比較します。衝突roundは物理時間ではなく、hard-sphere空間輸送へ対応を広げません。
- [純吸収平板の離散座標放射輸送：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja#references-ja>)

  純吸収・指定流入の平板に対する各方向の解析的な指数減衰と離散座標解を比較します。相対論的M1モーメント閉包とは別の放射モデルです。 追加版は解析rayと連続角度参照を保持し、固定角度の空間誤差と厳密rayの角度誤差、流入・流出・体積吸収の収支を分けます。散乱や多次元閉包へ拡張しません。
- [中性周期セルのEwald和と独立theta積分：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=ja#ewald-ja-validation>)

  分割alphaを3点、実空間打切りを3点、逆空間打切りを4点で確認。NaClのMadelung定数は3次元和を呼ばない独立な1次元Jacobi-theta積分と照合し、求積の誤差推定も保存します。
- [Bスプラインsmooth PMEの格子・次数収束：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=ja#spme-ja-validation>)

  16³・24³・40³格子と2つの次数で、直接Ewald逆空間和との差を記録します。Ewaldと実空間項・自己項を共有する部分も明示。最細格子の力はエネルギー差分とも比較し、全電荷の保持を確認します。
- [2次元対数核のM2M・M2L・L2Lを持つFMM：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=ja#fmm-ja-validation>)

  固定seedの128粒子で次数2・4・8・12を走査し、別の全対直接和とポテンシャル・電場の全成分を照合します。2点の符号、順序不変性、ポテンシャル微分も検査します。
- [CIC静電PICの冷たいプラズマ振動：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja#pic-ja-validation>)

  32・64・128格子の系列と、別の512格子上の時間刻み系列を分けます。変位モードを連続線形理論のcos(t)と比較し、全電荷・Poissonポテンシャル残差・単一粒子の自己力を検査します。
- [等質DSMC衝突成分の保存則・Maxwell分布：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=ja#dsmc-ja-validation>)

  粒子512・2048・8192、16 seedで、運動量・運動エネルギー、Maxwellの2次/4次モーメント、Gamma(3/2,1)のエネルギーCDFを比較。異方性の期待減衰率(N−2)/(2(N−1))も独立に照合します。 有限Nの成分4次モーメントは3−6/(3N−1)であり、Maxwell値3との有限N偏りとseed間の標本誤差を区別します。
- [純吸収平板の離散座標放射輸送：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja#radiation-transport-ja-validation>)

  32〜512セルで全方向の強度誤差・空間フラックス誤差・正値性・離散吸収収支を確認。4〜32方向の別系列は、出射フラックス2pi E3(tau)の解析表示と比較します。

## コード・検証

- [中性周期セルのEwald和と独立theta積分](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=ja>)
  availability: run

  3次元周期Coulomb相互作用の実空間和・逆空間和・自己項を実装し、分割パラメータと打切りを変えて検証します。
- [Bスプラインsmooth PMEの格子・次数収束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=ja>)
  availability: run

  電荷をBスプラインで格子へ割り当て、FFTでEwald逆空間項を評価するsmooth PME（SPME）の小規模例です。
- [Ewald：非対称周期セルのエネルギー・力と独立theta積分](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=ja>)
  availability: run

  中性8電荷の全エネルギーと24力成分を、別実装のGaussian/theta積分と比較。分割・実空間・逆空間の打切り、保存則と不変性を分けて測定します。
- [SPME：格子・補間次数・格子位相と保存則](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=ja>)
  availability: run

  BスプラインSPMEを同じ独立theta参照へ照合し、格子・次数・位相への依存、電荷の保持、エネルギー勾配と合力を測ります。
- [2次元対数核のM2M・M2L・L2Lを持つFMM](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=ja>)
  availability: run

  自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。
- [FMM：直接和・解析配置と展開次数・木の深さ](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=ja>)
  availability: run

  96粒子の2次元対数核を別の全対直接和と照合し、展開次数・木の深さ、回転・平行移動、合力の近似誤差を測ります。
- [CIC静電PICの冷たいプラズマ振動](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja>)
  availability: run

  1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。
- [PIC：格子・時間収束、保存量と粒子雑音](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=ja>)
  availability: run

  冷たい1次元周期プラズマのquiet-start収束と、独立seedでの初期粒子雑音を分け、電荷・運動量・Gauss則・エネルギー誤差を保存します。
- [等質DSMC衝突成分の保存則・Maxwell分布](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=ja>)
  availability: run

  等質なMaxwell分子のランダム二体衝突で、保存則と平衡分布への緩和を検証します。
- [DSMC衝突成分：有限N平衡・保存則・統計誤差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=ja>)
  availability: run

  有限粒子数の平衡をMaxwell極限と区別し、独立な球面標本、解析的異方性減衰、seed間誤差と比較します。
- [純吸収平板の離散座標放射輸送](<https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja>)
  availability: run

  純吸収の定常放射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。
- [放射輸送：空間・角度収束と光子統計](<https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=ja>)
  availability: run

  純吸収平板で特性解・独立適応求積・光子生存率を比較し、離散収支と標本誤差・区間被覆を別々に測ります。
