# 小型学習モデルと生物ODEの独立検証

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-small-models/

この章に登録された手法・問題・実行例の関連資料です。 Poisson PINN・周期熱FNOと、酵素・捕食被食・SEIRを固定予算で調べます。学習/近似の元精度目標と再現検査を区別します。

## 手法

- [L安定なSDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja>)

  全4状態をSDIRK2のstep doublingで積分し、各段のNewton法では同じ重み付きL∞残差とArmijo条件を使います。縮約Michaelis–Menten式はθ上の別RK4計算で求め、全系の積分誤差と近似モデル誤差を混同しません。
- [適応SDIRK2／ステップ倍分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=ja>)

  全4状態をSDIRK2のstep doublingで積分し、各段のNewton法では同じ重み付きL∞残差とArmijo条件を使います。縮約Michaelis–Menten式はθ上の別RK4計算で求め、全系の積分誤差と近似モデル誤差を混同しません。
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)

  全4状態をSDIRK2のstep doublingで積分し、各段のNewton法では同じ重み付きL∞残差とArmijo条件を使います。縮約Michaelis–Menten式はθ上の別RK4計算で求め、全系の積分誤差と近似モデル誤差を混同しません。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  全4状態をSDIRK2のstep doublingで積分し、各段のNewton法では同じ重み付きL∞残差とArmijo条件を使います。縮約Michaelis–Menten式はθ上の別RK4計算で求め、全系の積分誤差と近似モデル誤差を混同しません。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  固定400/800/1600ステップの古典RK4で物理状態を積分します。独立参照はlog x・log yの変数でRadau/BDFを実行し、主計算には対数変数や保存量の射影を導入しません。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  全4状態を固定400/800/1600ステップのRK4で積分。独立非線形参照は偏差をηで尺度化してRadau/BDFで求め、早期のE・I線形化は2×2行列指数の両モードを使います。
- [PINN・ニューラル演算子](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/?lang=ja>)
- [Thomas法／三重対角消去](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja>)
- [L安定なSDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja>)
- [適応SDIRK2／ステップ倍分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=ja>)
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

## 方程式

- [Michaelis–Mentenと完全酵素反応系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-enzyme-ja>)

  酵素・基質・複合体の反応と飽和速度則。完全反応系、迅速平衡近似、準定常近似の違いは解説先へ。 限定した実行例：2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。 閉鎖反応E+S⇌C→E+Pを無次元化し、k₁=10、k₋₁=k₂=1、S₀=1、C₀=P₀=0、E₀=0.01/0.002。Kₘ=0.2、ε=E₀/(Kₘ+S₀)=1/120,1/600、θ=E₀t∈[0,0.5]です。
- [Lotka–Volterra捕食・被食](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-lotka-volterra-ja>)

  捕食・被食の結合ODE。位相平面と長時間積分を考えるためのモデルです。 限定した実行例：1初期値・有限時間の固定比較です。連続系の閉軌道を引き込み極限周期とは呼びません。RK4の厳密な不変量保存、任意刻みでの正値性、長時間の構造保存は保証しません。 無次元の捕食者・被食者系x′=x(1−y)、y′=y(x−1)、初期値(1.2,0.8)、0≤t≤20。正の象限で不変量H=x−log x+y−log yを評価します。
- [閉鎖SEIR区画モデル](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#seir-compartment-ja>)

  出生死亡なし・全人口一定の教育用率です。初期過渡は2×2行列指数に比較し、感染症予測には使いません。 閉鎖人口S+E+I+R=1、β=0.6、σ=0.3、γ=0.2。η=10⁻⁴/5×10⁻⁵に対し(S,E,I,R)(0)=(1−2η,η,η,0)、0≤t≤20。出生・死亡・外部流入はありません。
- [閉鎖SEIR区画モデル](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#seir-compartment-ja>)

  出生死亡なし・全人口一定の教育用率です。初期過渡は2×2行列指数に比較し、感染症予測には使いません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=ja#pinn-poisson-ja-algorithm>)

  x(1−x)を掛けて境界値を厳密に組み込むtanhネットワークを、解析的な全パラメータJacobian付きTRF最小二乗法で学習します。固定予算後の全モデルを保存し、31/63/127未知数の2次中心差分とThomas法も計算します。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja#fno-periodic-heat-ja-algorithm>)

  入力(u₀,ν)を幅2へ写し、局所線形項・DCと1–4モードの複素Fourier項・tanhからなる2ブロックを適用します。L-BFGS-Bの固定予算で学習し、同じ重みをN=32/64へ転送。非線形項は各格子上で評価しdealiasingしません。
- [熱・拡散方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja>)

  一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja#enzyme-qssa-ja-algorithm>)

  全4状態をSDIRK2のstep doublingで積分し、各段のNewton法では同じ重み付きL∞残差とArmijo条件を使います。縮約Michaelis–Menten式はθ上の別RK4計算で求め、全系の積分誤差と近似モデル誤差を混同しません。
- [Michaelis–Mentenと完全酵素反応系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-enzyme-ja>)

  酵素・基質・複合体の反応と飽和速度則。完全反応系、迅速平衡近似、準定常近似の違いは解説先へ。 限定した実行例：2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=ja#lotka-volterra-ja-algorithm>)

  固定400/800/1600ステップの古典RK4で物理状態を積分します。独立参照はlog x・log yの変数でRadau/BDFを実行し、主計算には対数変数や保存量の射影を導入しません。
- [Lotka–Volterra捕食・被食](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-lotka-volterra-ja>)

  捕食・被食の結合ODE。位相平面と長時間積分を考えるためのモデルです。 限定した実行例：1初期値・有限時間の固定比較です。連続系の閉軌道を引き込み極限周期とは呼びません。RK4の厳密な不変量保存、任意刻みでの正値性、長時間の構造保存は保証しません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=ja#seir-linearization-ja-algorithm>)

  全4状態を固定400/800/1600ステップのRK4で積分。独立非線形参照は偏差をηで尺度化してRadau/BDFで求め、早期のE・I線形化は2×2行列指数の両モードを使います。

## 問題の図

- [酵素反応の保存と準定常近似](<https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa-preview.png
- [Lotka–Volterra不変量と正値性](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra-preview.png
- [SEIR保存則と初期線形化](<https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization-preview.png
- [1D Poisson PINNと独立格子誤差](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/pinn-poisson.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/pinn-poisson.png
- [小型FNOの問題単位検証](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/fno-periodic-heat.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/fno-periodic-heat.png
- [酵素反応の保存と準定常近似](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa.png
- [Lotka–Volterra不変量と正値性](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra.png
- [SEIR保存則と初期線形化](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization.png
- [1次元Poisson・Dirichlet製造解](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja>)

  Poisson PINN・周期熱FNOと、酵素・捕食被食・SEIRを固定予算で調べます。学習/近似の元精度目標と再現検査を区別します。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-dirichlet.png
- [周期Fourierモードの熱拡散](<https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja>)

  Poisson PINN・周期熱FNOと、酵素・捕食被食・SEIRを固定予算で調べます。学習/近似の元精度目標と再現検査を区別します。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png

## 厳密解・参照解

- [酵素反応の保存と準定常近似：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja#references-ja>)

  独立な全系Radau/BDF参照、縮約式の陰的スカラー恒等式、E+C=E₀とS+C+P=1、正値性、実際の採用・棄却・Newton作業を照合。初期層を含む全時間と、事前指定θ≥0.02の近似誤差を別保存します。
- [酵素反応の保存と準定常近似](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-enzyme-qssa-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 閉鎖反応E+S⇌C→E+Pを無次元化し、k₁=10、k₋₁=k₂=1、S₀=1、C₀=P₀=0、E₀=0.01/0.002。Kₘ=0.2、ε=E₀/(Kₘ+S₀)=1/120,1/600、θ=E₀t∈[0,0.5]です。 2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。
- [Lotka–Volterra不変量と正値性：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/?lang=ja#references-ja>)

  独立参照との状態誤差、Hのドリフト、保存された軌道の最小値を別々に測定。参照側では解析Jacobian、Radau/BDF差、刻み精度、Hの時間微分の恒等式を事前資格しています。
- [Lotka–Volterra不変量と正値性](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lotka-volterra-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 無次元の捕食者・被食者系x′=x(1−y)、y′=y(x−1)、初期値(1.2,0.8)、0≤t≤20。正の象限で不変量H=x−log x+y−log yを評価します。 1初期値・有限時間の固定比較です。連続系の閉軌道を引き込み極限周期とは呼びません。RK4の厳密な不変量保存、任意刻みでの正値性、長時間の構造保存は保証しません。
- [SEIR保存則と初期線形化：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/?lang=ja#references-ja>)

  t≤20の全ODE積分誤差・人口保存・非負性と、0≤t≤1の201参照点での線形化モデル誤差を分けます。参照では両ηの尺度付きJacobian、Radau/BDF差とη²に対する余裕、解析的な全行列指数を別資格しています。
- [SEIR保存則と初期線形化](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-seir-linearization-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 閉鎖人口S+E+I+R=1、β=0.6、σ=0.3、γ=0.2。η=10⁻⁴/5×10⁻⁵に対し(S,E,I,R)(0)=(1−2η,η,η,0)、0≤t≤20。出生・死亡・外部流入はありません。 2つの小初期感染量による固定係数の整合性比較です。早期線形化をt=20全体の厳密解と見なさず、単一の優勢モードで両モードを置き換えません。実流行の予測・統計的被覆・任意人口への一般保証は行いません。
- [1D Poisson PINNと独立格子誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pinn-poisson-ja>)
  reference_kind: manufactured

  製造解 無次元区間[0,1]で −uₓₓ=π²sin(πx)、u(0)=u(1)=0。中間層16素子・49実パラメータ、固定seed 8401–8403、学習64点と独立評価257点を用います。
- [小型FNOの問題単位検証](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fno-periodic-heat-ja>)
  reference_kind: analytic

  解析解 周期区間[0,2π)、uₜ=νuₓₓ、T=0.25。同じ関数の点を分散させず、全46問題を学習24・検証6・未見ID8・νのOOD4・周波数のOOD4に分けます。2固定seed、93実パラメータです。
- [酵素反応の保存と準定常近似](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-enzyme-qssa-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 閉鎖反応E+S⇌C→E+Pを無次元化し、k₁=10、k₋₁=k₂=1、S₀=1、C₀=P₀=0、E₀=0.01/0.002。Kₘ=0.2、ε=E₀/(Kₘ+S₀)=1/120,1/600、θ=E₀t∈[0,0.5]です。
- [Lotka–Volterra不変量と正値性](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lotka-volterra-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 無次元の捕食者・被食者系x′=x(1−y)、y′=y(x−1)、初期値(1.2,0.8)、0≤t≤20。正の象限で不変量H=x−log x+y−log yを評価します。
- [SEIR保存則と初期線形化](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-seir-linearization-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 閉鎖人口S+E+I+R=1、β=0.6、σ=0.3、γ=0.2。η=10⁻⁴/5×10⁻⁵に対し(S,E,I,R)(0)=(1−2η,η,η,0)、0≤t≤20。出生・死亡・外部流入はありません。
- [1D Poisson PINNと独立格子誤差：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=ja#pinn-poisson-ja-validation>)

  全49列の残差Jacobianと損失勾配、空間微分を別資格段階で独立照合。解析解sin(πx)に対する独立点誤差、PDE残差、境界値、FD誤差を別に保存します。収束・精度目標の実際の真偽を残し、正常な予算終了を収束と呼びません。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 単一sin(πx)の共通固定入力とは一致しますが、保存比較図は複合正弦製造解も含みます。同じ零Dirichletでも全ソースが同一ではありません。
- [1D Poisson PINNと独立格子誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pinn-poisson-ja>)
  relation: related-model
  reference_kind: manufactured

  製造解 無次元区間[0,1]で −uₓₓ=π²sin(πx)、u(0)=u(1)=0。中間層16素子・49実パラメータ、固定seed 8401–8403、学習64点と独立評価257点を用います。 1つの滑らかなPoisson問題と3seedの固定予算実験です。小さい学習損失だけで独立点精度の達成や一般的なPINN学習成功を保証しません。未達目標も表示します。
- [小型FNOの問題単位検証：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja#fno-periodic-heat-ja-validation>)

  全93実座標の損失勾配を2つの固定差分幅で照合し、Fourierブロックを直接DFTと比較。解析的な熱モード減衰に対する絶対・相対誤差、格子制限差、ID/OODを分離します。参照RMS≤10⁻¹²では相対誤差をNAとし、ゼロ・微小振幅では絶対誤差を保存します。
- [熱拡散／Fourierモードの減衰](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 単位区間の周期境界、拡散係数0.02。 保存ギャラリーの周期[0,1]、1+0.25sin(2πx)、ν=0.02、最終時刻1が一致します。別周波数のコード検査への一致は意味しません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。
- [小型FNOの問題単位検証](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fno-periodic-heat-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 周期区間[0,2π)、uₜ=νuₓₓ、T=0.25。同じ関数の点を分散させず、全46問題を学習24・検証6・未見ID8・νのOOD4・周波数のOOD4に分けます。2固定seed、93実パラメータです。 固定された小型離散作用素の比較で、任意の解像度・分布に対する一般化やOOD精度を保証しません。N=64から32への差には非線形aliasingが含まれ、連続体離散化誤差とは呼びません。最適化収束と固定予算終了は別です。
- [酵素反応の保存と準定常近似：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja#enzyme-qssa-ja-validation>)

  独立な全系Radau/BDF参照、縮約式の陰的スカラー恒等式、E+C=E₀とS+C+P=1、正値性、実際の採用・棄却・Newton作業を照合。初期層を含む全時間と、事前指定θ≥0.02の近似誤差を別保存します。
- [酵素反応の保存と準定常近似](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-enzyme-qssa-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 閉鎖反応E+S⇌C→E+Pを無次元化し、k₁=10、k₋₁=k₂=1、S₀=1、C₀=P₀=0、E₀=0.01/0.002。Kₘ=0.2、ε=E₀/(Kₘ+S₀)=1/120,1/600、θ=E₀t∈[0,0.5]です。 2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。
- [Lotka–Volterra不変量と正値性：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=ja#lotka-volterra-ja-validation>)

  独立参照との状態誤差、Hのドリフト、保存された軌道の最小値を別々に測定。参照側では解析Jacobian、Radau/BDF差、刻み精度、Hの時間微分の恒等式を事前資格しています。
- [Lotka–Volterra不変量と正値性](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lotka-volterra-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 無次元の捕食者・被食者系x′=x(1−y)、y′=y(x−1)、初期値(1.2,0.8)、0≤t≤20。正の象限で不変量H=x−log x+y−log yを評価します。 1初期値・有限時間の固定比較です。連続系の閉軌道を引き込み極限周期とは呼びません。RK4の厳密な不変量保存、任意刻みでの正値性、長時間の構造保存は保証しません。
- [SEIR保存則と初期線形化：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=ja#seir-linearization-ja-validation>)

  t≤20の全ODE積分誤差・人口保存・非負性と、0≤t≤1の201参照点での線形化モデル誤差を分けます。参照では両ηの尺度付きJacobian、Radau/BDF差とη²に対する余裕、解析的な全行列指数を別資格しています。
- [SEIR保存則と初期線形化](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-seir-linearization-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 閉鎖人口S+E+I+R=1、β=0.6、σ=0.3、γ=0.2。η=10⁻⁴/5×10⁻⁵に対し(S,E,I,R)(0)=(1−2η,η,η,0)、0≤t≤20。出生・死亡・外部流入はありません。 2つの小初期感染量による固定係数の整合性比較です。早期線形化をt=20全体の厳密解と見なさず、単一の優勢モードで両モードを置き換えません。実流行の予測・統計的被覆・任意人口への一般保証は行いません。
- [1次元Poisson・Dirichlet製造解：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja#references-ja>)

  Poisson PINN・周期熱FNOと、酵素・捕食被食・SEIRを固定予算で調べます。学習/近似の元精度目標と再現検査を区別します。 零Dirichlet境界の製造正弦解、複合正弦の比較例、および離散残差で確認します。単一sin(πx)の参照カードが全ソース条件を表すわけではありません。 全49列の残差Jacobianと損失勾配、空間微分を別資格段階で独立照合。解析解sin(πx)に対する独立点誤差、PDE残差、境界値、FD誤差を別に保存します。収束・精度目標の実際の真偽を残し、正常な予算終了を収束と呼びません。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  Poisson PINN・周期熱FNOと、酵素・捕食被食・SEIRを固定予算で調べます。学習/近似の元精度目標と再現検査を区別します。 製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 単一sin(πx)の共通固定入力とは一致しますが、保存比較図は複合正弦製造解も含みます。同じ零Dirichletでも全ソースが同一ではありません。
- [1D Poisson PINNと独立格子誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pinn-poisson-ja>)
  relation: related-model
  reference_kind: manufactured

  Poisson PINN・周期熱FNOと、酵素・捕食被食・SEIRを固定予算で調べます。学習/近似の元精度目標と再現検査を区別します。 製造解 無次元区間[0,1]で −uₓₓ=π²sin(πx)、u(0)=u(1)=0。中間層16素子・49実パラメータ、固定seed 8401–8403、学習64点と独立評価257点を用います。 1つの滑らかなPoisson問題と3seedの固定予算実験です。小さい学習損失だけで独立点精度の達成や一般的なPINN学習成功を保証しません。未達目標も表示します。
- [周期Fourierモードの熱拡散：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#references-ja>)

  Poisson PINN・周期熱FNOと、酵素・捕食被食・SEIRを固定予算で調べます。学習/近似の元精度目標と再現検査を区別します。 周期区間の単一Fourierモードの指数減衰が解析基準です。保存図の振幅0.25・粘性0.02の条件を、別周波数のコード検査と区別します。 全93実座標の損失勾配を2つの固定差分幅で照合し、Fourierブロックを直接DFTと比較。解析的な熱モード減衰に対する絶対・相対誤差、格子制限差、ID/OODを分離します。参照RMS≤10⁻¹²では相対誤差をNAとし、ゼロ・微小振幅では絶対誤差を保存します。
- [熱拡散／Fourierモードの減衰](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja>)
  relation: related-model
  reference_kind: analytic

  Poisson PINN・周期熱FNOと、酵素・捕食被食・SEIRを固定予算で調べます。学習/近似の元精度目標と再現検査を区別します。 解析解 単位区間の周期境界、拡散係数0.02。 保存ギャラリーの周期[0,1]、1+0.25sin(2πx)、ν=0.02、最終時刻1が一致します。別周波数のコード検査への一致は意味しません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。
- [小型FNOの問題単位検証](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fno-periodic-heat-ja>)
  relation: related-model
  reference_kind: analytic

  Poisson PINN・周期熱FNOと、酵素・捕食被食・SEIRを固定予算で調べます。学習/近似の元精度目標と再現検査を区別します。 解析解 周期区間[0,2π)、uₜ=νuₓₓ、T=0.25。同じ関数の点を分散させず、全46問題を学習24・検証6・未見ID8・νのOOD4・周波数のOOD4に分けます。2固定seed、93実パラメータです。 固定された小型離散作用素の比較で、任意の解像度・分布に対する一般化やOOD精度を保証しません。N=64から32への差には非線形aliasingが含まれ、連続体離散化誤差とは呼びません。最適化収束と固定予算終了は別です。

## コード・検証

- [酵素反応の保存と準定常近似](<https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja>)
  availability: run

  全4状態と準定常近似を比較し、初期層と積分誤差を分けます。
- [Lotka–Volterra不変量と正値性](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=ja>)
  availability: run

  正の軌道を独立な対数座標参照と比較します。
- [SEIR保存則と初期線形化](<https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=ja>)
  availability: run

  人口保存と2モードの初期線形化を別々に検査します。
- [1D Poisson PINNと独立格子誤差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=ja>)
  availability: run

  3固定seedの49パラメータPINNを解析解・FDと比較します。
- [小型FNOの問題単位検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja>)
  availability: run

  同じ重みで32/64点・未見関数・OODを分けて評価します。
- [1次元Poisson・Dirichlet製造解：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja#code-ja>)
  availability: source

  Poisson PINN・周期熱FNOと、酵素・捕食被食・SEIRを固定予算で調べます。学習/近似の元精度目標と再現検査を区別します。 対応する公開検査と配布版の条件を確認できます。
- [周期Fourierモードの熱拡散：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#code-ja>)
  availability: source

  Poisson PINN・周期熱FNOと、酵素・捕食被食・SEIRを固定予算で調べます。学習/近似の元精度目標と再現検査を区別します。 対応する公開検査と配布版の条件を確認できます。
