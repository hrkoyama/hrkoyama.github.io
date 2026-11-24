# 周期Taylor–Green渦 / Periodic Taylor–Green vortex

https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/

## 日本語

[保存済みTaylor–Green渦の速度と圧力。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/incompressible/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#taylor-green)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja)

$$
\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\rho^{-1}\nabla p+\nu\nabla^2\boldsymbol u
$$

$$
\nabla\cdot\boldsymbol u=0
$$

一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。

#### [等温格子BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja)

$$
f_q(\boldsymbol x+\boldsymbol c_q,t+1)=f_q(\boldsymbol x,t)-\frac{f_q-f_q^{\rm eq}}{\tau}+S_q
$$

格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。

#### 周期Taylor–Green渦：速度・散逸・発散

共通実行例 · 問題の式

$$
\boldsymbol u_t+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\nabla p+\nu\nabla^2\boldsymbol u,\qquad\nabla\cdot\boldsymbol u=0
$$

$$
\boldsymbol u_{\rm ref}(x,y,t)=\begin{pmatrix}\sin x\cos y\\-\cos x\sin y\end{pmatrix}e^{-2\nu t},\qquad\nu=0.1
$$

[0,2π)²周期、t=0.5、16/32/64格子のMAC圧力射影。保存すべき定数エネルギーではなく粘性減衰を調べる。空間と安定刻みの同時細分化と、同一格子の刻み感度を区別する。

#### LBM Taylor–Green渦：格子・刻み・Machの結合感度

補助実行例 · 実行例の定義・検証式

$$
u=U\sin x\cos y\,e^{-2\nu t},\quad v=-U\cos x\sin y\,e^{-2\nu t}
$$

$$
p=\frac{U^2}{4}(\cos2x+\cos2y)e^{-4\nu t},\quad\langle K\rangle=\frac{U^2}{4}e^{-4\nu t}
$$

周期2Dの非線形渦を実際に時間発展し、連続解析場への速度・圧力・エネルギー誤差を保存します。amplitude感度と同格子のcoupled刻み感度も分けて示します。

### 厳密解・参照解

2次元周期Taylor–Green渦の速度・圧力の解析解、粘性減衰と離散発散を確認します。参照解一覧の表示はy=π/4の断面であり、2次元計算全体のデータではありません。

#### [粘性流／2次元Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=taylor-green)

解析解 · 関連モデルの参照

(u,v)=(sin x cos y,−cos x sin y)e^(−2νt); p=(cos 2x+cos 2y)e^(−4νt)/4

周期領域[0,2π]²、単位密度、動粘性係数0.1、圧力平均ゼロ。Webではy=π/4のx方向断面を表示します。

同じν=0.1・周期[0,2π]²の解析モデルですが、参照カードはy=π/4のx断面表示です。2次元速度・圧力場や格子誤差の配列とは一致しません。

#### [LBMのTaylor–Green渦：格子・時間・Mach数が結び付く感度](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja#lbm-taylor-green-ja-measurements)

解析解 · 関連モデルの参照

u=U sin(x)cos(y) exp(-2nu t), v=-U cos(x)sin(y) exp(-2nu t); p=U^2 exp(-4nu t)[cos(2x)+cos(2y)]/4.

[0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。

[0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。

#### 周期Taylor–Green渦：速度・散逸・発散

CSVは(i,j)をC順に並べ、u面・v面・圧力中心それぞれの座標、数値解と解析解を別列に保存。MAC速度を同じ位置の成分と誤解しない。JSONにエネルギー履歴と時間感度を保存。

- [CSVは(i,j)をC順に並べ、u面・v面・圧力中心それぞれの座標、数値解と解析解を別列に保存。MAC速度を同じ位置の成分と誤解しない。JSONにエネルギー履歴と時間感度を保存。](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/taylor-green/result.json)
- [u=sin x cos y e^(−2νt)、v=−cos x sin y e^(−2νt)、p=(cos2x+cos2y)e^(−4νt)/4。平均運動エネルギーはe^(−4νt)/4。](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/incompressible/)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/taylor-green/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/taylor-green/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=ja)

#### LBM Taylor–Green渦：格子・刻み・Machの結合感度

22pytestと79判定、6固定発展。最細速度相対L2.03、圧力.08、combined速度次数1.5以上、エネルギー.03、発散・周期質量・平均運動量を判定。解析PDE5資格を区別して保存します。 最粗N16の初回エネルギー誤差5.0018%未達を保持し、同じ3%基準へ最粗だけN24へ細分化。次数は最細32/64対だけで評価します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [MAC圧力射影法](https://hrkoyama.github.io/numerical-methods-atlas/methods/projection/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [D2Q9–BGK衝突・並進](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [周期Taylor–Green渦：速度・散逸・発散](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=ja)

共通実行例

既存の2次元MAC投影法・中心対流項・明示SSPRK2を使用。16²/32²/64²で解析的減衰渦と比較し、最細格子はCFL半減でも確認。

単位密度、[0,2π)²、ν=0.1、T=0.5。u₀=sin x cos y、v₀=−cos x sin y。既存ソルバーの移流・拡散安定性に基づくCFL=0.2、時間感度検査は0.1。

[コード / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/taylor-green.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/taylor-green.json --output output-taylor-green
python -m pytest -q tests/test_recipes.py
```

非正粘性・終端時刻、CFL範囲外、倍増でない格子を拒否。安定時間刻みも変わる格子細分化は空間のみの次数証明ではない。固定格子のCFL半減は時間感度であり厳密誤差上界ではない。壁境界・乱流・任意Reynolds数への検証ではない。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [LBM Taylor–Green渦：格子・刻み・Machの結合感度](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja)

補助実行例

周期2Dの非線形渦を実際に時間発展し、連続解析場への速度・圧力・エネルギー誤差を保存します。amplitude感度と同格子のcoupled刻み感度も分けて示します。

[0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

拡散尺度では格子・時間・Machが結合し、amplitude変更はReも変えます。純空間/純時間/純Mach次数や有限Machの厳密非圧縮性を主張しません。平衡初期化のkinetic startupも実誤差へ含めます。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/lbm-taylor-green/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/run.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/test_lbm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/test_lbm.py)

## English

[Stored Taylor–Green velocity and pressure fields.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/incompressible/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#taylor-green-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en)

$$
\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\rho^{-1}\nabla p+\nu\nabla^2\boldsymbol u
$$

$$
\nabla\cdot\boldsymbol u=0
$$

Representative constant-density/viscosity flow. In addition to periodic2D MAC projection/Taylor–Green, a separate release verifies a pressure-eliminated nonperiodic Re100 cavity.

#### [Isothermal lattice BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en)

$$
f_q(\boldsymbol x+\boldsymbol c_q,t+1)=f_q(\boldsymbol x,t)-\frac{f_q-f_q^{\rm eq}}{\tau}+S_q
$$

Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow.

#### Periodic Taylor–Green vortex: velocity, decay and divergence

Common execution example · Problem definition

$$
\boldsymbol u_t+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\nabla p+\nu\nabla^2\boldsymbol u,\qquad\nabla\cdot\boldsymbol u=0
$$

$$
\boldsymbol u_{\rm ref}(x,y,t)=\begin{pmatrix}\sin x\cos y\\-\cos x\sin y\end{pmatrix}e^{-2\nu t},\qquad\nu=0.1
$$

Periodic [0,2π)², t=0.5, MAC pressure projection on 16/32/64 grids. Check viscous decay rather than constant energy. Combined space/stable-step refinement is separated from fixed-grid time-step sensitivity.

#### LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity

Supplementary execution example · Example definition or validation formula

$$
u=U\sin x\cos y\,e^{-2\nu t},\quad v=-U\cos x\sin y\,e^{-2\nu t}
$$

$$
p=\frac{U^2}{4}(\cos2x+\cos2y)e^{-4\nu t},\quad\langle K\rangle=\frac{U^2}{4}e^{-4\nu t}
$$

Evolve a nonlinear periodic2D vortex and save velocity/pressure/energy errors against the continuous analytic field. Distinguish amplitude probes from a fixed-grid coupled-step probe.

### Exact and reference solutions

Check analytic 2D periodic Taylor–Green velocity/pressure, viscous decay and discrete divergence. The library display is a y=π/4 slice rather than the full 2D computed field.

#### [Viscous flow / 2D Taylor–Green](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=taylor-green)

Analytic reference · Related-model reference

(u,v)=(sin x cos y,−cos x sin y)e^(−2νt); p=(cos 2x+cos 2y)e^(−4νt)/4

Periodic [0,2π]²; unit density; viscosity 0.1; zero mean pressure. Web profile is an x-slice at y=π/4.

The analytic model shares ν=0.1 and periodic [0,2π]², but the card displays an x-slice at y=π/4, not full 2D velocity/pressure or mesh-error arrays.

#### [LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en#lbm-taylor-green-en-measurements)

Analytic reference · Related-model reference

u=U sin(x)cos(y) exp(-2nu t), v=-U cos(x)sin(y) exp(-2nu t); p=U^2 exp(-4nu t)[cos(2x)+cos(2y)]/4.

Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.

Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.

#### Periodic Taylor–Green vortex: velocity, decay and divergence

CSV uses C-order (i,j) rows with separate coordinates and numerical/analytic values for u faces, v faces and pressure centers; the components are not collocated. JSON includes energy histories and temporal sensitivity.

- [CSV uses C-order (i,j) rows with separate coordinates and numerical/analytic values for u faces, v faces and pressure centers; the components are not collocated. JSON includes energy histories and temporal sensitivity.](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/taylor-green/result.json)
- [u=sin(x)cos(y)e^(-2nu*t), v=-cos(x)sin(y)e^(-2nu*t), p=(cos(2x)+cos(2y))e^(-4nu*t)/4; mean kinetic energy e^(-4nu*t)/4.](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/incompressible/)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/taylor-green/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/taylor-green/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=en)

#### LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity

22pytest and79gates,sixfixed evolutions. Require finest velocity relativeL2.03,pressure.08,combined velocity order≥1.5,energy.03anddivergence/periodic mass/mean momentum. Save five analyticPDEqualifiers distinctly. Retain the initial N16energy failure5.0018%; refine only thatcoarsegrid to24against the unchanged3%gate. Report order only for thefinest32/64pair.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [MAC pressure projection](https://hrkoyama.github.io/numerical-methods-atlas/methods/projection/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [D2Q9–BGK collision and streaming](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Periodic Taylor–Green vortex: velocity, decay and divergence](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=en)

Common execution example

Use existing two-dimensional MAC projection, centered convection and explicit SSPRK2. Compare analytic decaying vortex on 16²/32²/64² grids and halve CFL on the finest grid.

Unit density, [0,2*pi)², nu=0.1 and T=0.5. u0=sin(x)cos(y), v0=-cos(x)sin(y). CFL=0.2 uses the solver's combined advection/diffusion stability estimate; temporal sensitivity uses 0.1.

[Code / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/taylor-green.json)

[File manifest and hashes](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/taylor-green.json --output output-taylor-green
python -m pytest -q tests/test_recipes.py
```

Reject nonpositive viscosity/final time, invalid CFL and nondoubling grids. Grid refinement also changes the stable time step and is not a pure spatial-order proof. Fixed-grid CFL reduction measures sensitivity, not a rigorous error bound. No validation of walls, turbulence or arbitrary Reynolds number.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en)

Supplementary execution example

Evolve a nonlinear periodic2D vortex and save velocity/pressure/energy errors against the continuous analytic field. Distinguish amplitude probes from a fixed-grid coupled-step probe.

Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Diffusive scaling couples grid,time andMach; amplitude changesRe. No isolated spatial/time/Mach order or exact incompressibility atfiniteMach. Kinetic equilibrium-startup transients remain part of the measured errors.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/lbm-taylor-green/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/run.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/test_lbm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/test_lbm.py)
