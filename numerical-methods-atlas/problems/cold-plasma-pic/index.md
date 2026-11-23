# CIC静電PICの冷たいプラズマ振動 / Cold-plasma oscillation with electrostatic CIC PIC

https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/

## 日本語

[1次元周期・振幅0.001の冷たい電子プラズマ。CIC静電PICの変位モードとcos(t)、別々の格子・時間刻み走査の保存誤差を表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-particles/#pic) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#cold-plasma-pic)

### 方程式・問題の定義

Poissonへのリンクは自己無撞着な静電場の部分です。粒子の運動・CIC補間を結合したPIC全体の式が一覧に揃っているわけではありません。

#### [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。

#### [静電Vlasov–Poisson方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#vlasov-poisson-ja)

$$
\partial_t f+v\partial_x f-E\partial_v f=0
$$

$$
\partial_x E=1-\int f\,dv,\quad\int E\,dx=0
$$

1D1V電子と固定中性化背景。重み付き全分布PICの粒子・格子・時間近似と、線形参照の範囲を分けます。

#### CIC静電PICの冷たいプラズマ振動

補助実行例 · 実行例の定義・検証式

$$
\dot x_i=v_i,\quad\dot v_i=-E_h(x_i),\quad-\phi_{xx}=\rho,\quad E=-\phi_x
$$

$$
A(t)/A(0)\simeq\cos(\omega_pt),\qquad\omega_p=1
$$

1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。

#### PIC：格子・時間収束、保存量と粒子雑音

補助実行例 · 実行例の定義・検証式

$$
\mathbb E[|\widehat\rho_1/n|^2]=\frac{2+\cos(2\pi/n)}{3N}
$$

$$
H_h=\frac{w}{2}\sum_iv_i^2+\frac{\Delta x}{2}\sum_jE_j^2
$$

冷たい1次元周期プラズマのquiet-start収束と、独立seedでの初期粒子雑音を分け、電荷・運動量・Gauss則・エネルギー誤差を保存します。

#### PIC空間演算の独立実装照合

補助実行例 · 実行例の定義・検証式

$$
\rho_j=1-\frac1h\sum_p w_p S_j(x_p),\quad a_p=-\sum_j S_j(x_p)E_j
$$

$$
\widehat E_m=\widehat\rho_m/(ik_m),\quad E_0=0,\quad E_{N/2}=0\ \text{(even N)}
$$

$$
\rho=-\tfrac12\cos2x\ \Longrightarrow\ E=-\tfrac14\sin2x,\quad a=+\tfrac14\sin2x
$$

ベクトル化CIC/FFTと、別に書いた粒子ループCIC・密なDFTを、それぞれが自己無撞着な場を毎kick計算する軌道全体で照合します。

### 厳密解・参照解

小振幅の冷たいプラズマの線形変位cos(t)と比較し、電荷整合性・Poisson残差・自己力、格子系列と時間刻み系列を確認します。一般の非線形PIC軌道の厳密解という主張ではありません。 追加版は静止イオン背景のまま、電荷・運動量・粒子と場のエネルギーを軌道誤差と分けます。小振幅線形参照であり、熱的Landau減衰や電磁PICの根拠ではありません。

#### [PIC空間演算の独立実装照合](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja#pic-independent-spatial-ja-measurements)

有限格子の数値参照 · 関連モデルの参照

rho=-.5cos(2x) => E=-.25sin(2x), electron a=+.25sin(2x); independent scalar CIC + dense DFT owns its self-consistent field every kick.

周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。 19 pytestと58/58固定判定が合格。6組＝12の自己無撞着軌道を13時刻全てで照合し、最大差は位置8.88e−16・速度3.33e−16・電場8.33e−16・電荷2.89e−15。pytest+mainは0.392秒。最初の小pytestは周期端点の添字不具合で17/18となり、元記録を保持して修正後に全計算を実行しました。 離散演算の独立したコーディング照合です。時間積分法や連続方程式を変えた独立エンジン、連続極限の収束、冷たいプラズマの振動参照の再現を意味しません。既存cold-plasma-picの関連補助検証として扱い、温かい初期速度の軌道を冷たい解と同一視しません。

周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。

#### CIC静電PICの冷たいプラズマ振動

32・64・128格子の系列と、別の512格子上の時間刻み系列を分けます。変位モードを連続線形理論のcos(t)と比較し、全電荷・Poissonポテンシャル残差・単一粒子の自己力を検査します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja)

#### PIC：格子・時間収束、保存量と粒子雑音

16/32/64格子とdt=.2/.1/.05を別に精密化し、線形cos(t)と時間参照の誤差を分離します。実数奇微分のNyquist零モードはGauss残差から分けて記録。時刻0の64seed・N=256/1024/4096のCICモード電力を解析期待値と比較します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=ja)

#### PIC空間演算の独立実装照合

19 pytestと58/58固定判定が合格。6組＝12の自己無撞着軌道を13時刻全てで照合し、最大差は位置8.88e−16・速度3.33e−16・電場8.33e−16・電荷2.89e−15。pytest+mainは0.392秒。最初の小pytestは周期端点の添字不具合で17/18となり、元記録を保持して修正後に全計算を実行しました。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [Particle-in-Cell（PIC）](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Cloud-in-cellの割当てと補間](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja)

補助実行例

1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。

長さ2pi、電子の電荷質量比−1、静止イオン背景密度1、plasma frequency=1の無次元系。quiet startから振幅0.001の微小正弦変位を与えます。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

有限振幅・有限粒子数の誤差床があります。非線形不安定性、Landau減衰、衝突、電磁PIC、相対論粒子、境界流入出の検証ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)

#### [PIC：格子・時間収束、保存量と粒子雑音](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=ja)

補助実行例

冷たい1次元周期プラズマのquiet-start収束と、独立seedでの初期粒子雑音を分け、電荷・運動量・Gauss則・エネルギー誤差を保存します。

長さ2pi、静止イオン密度1、電子q/m=−1、plasma frequency=1、微小正弦変位0.001、最終時刻1.6。格子系列は同じ2048粒子を使い、時間系列は同じ32格子・256粒子を使います。 w=2pi/Nは粒子重み、nは格子数です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

DOP853は独立PIC空間実装ではありません。電荷・運動量の保持とエネルギーの近似保存を区別し、初期雑音のNスケーリングを時間発展した熱プラズマの保証としません。Landau減衰・電磁PIC・相対論・衝突は未検証です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)

#### [PIC空間演算の独立実装照合](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja)

補助実行例

ベクトル化CIC/FFTと、別に書いた粒子ループCIC・密なDFTを、それぞれが自己無撞着な場を毎kick計算する軌道全体で照合します。

周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

離散演算の独立したコーディング照合です。時間積分法や連続方程式を変えた独立エンジン、連続極限の収束、冷たいプラズマの振動参照の再現を意味しません。既存cold-plasma-picの関連補助検証として扱い、温かい初期速度の軌道を冷たい解と同一視しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/pic-spatial/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/run.py)
- [/code/validated-examples/2026-11-23/pic-spatial/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/primary.py)
- [/code/validated-examples/2026-11-23/pic-spatial/references/scalar_pic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/references/scalar_pic.py)
- [/code/validated-examples/2026-11-23/pic-spatial/test_spatial.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/test_spatial.py)

## English

[One-dimensional periodic cold electrons, amplitude 0.001: stored CIC electrostatic-PIC displacement versus cos(t), with separate grid and timestep error sweeps.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-particles/#pic) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#cold-plasma-pic-en)

### Equations and problem definitions

Poisson identifies the self-consistent electrostatic field; the registry does not list the complete coupled particle-motion/CIC PIC system.

#### [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.

#### [Electrostatic Vlasov–Poisson equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#vlasov-poisson-en)

$$
\partial_t f+v\partial_x f-E\partial_v f=0
$$

$$
\partial_x E=1-\int f\,dv,\quad\int E\,dx=0
$$

1D1V electrons and fixed neutralizing background. Separate weighted full-f particle,mesh and time approximations from the linear-reference scope.

#### Cold-plasma oscillation with electrostatic CIC PIC

Supplementary execution example · Example definition or validation formula

$$
\dot x_i=v_i,\quad\dot v_i=-E_h(x_i),\quad-\phi_{xx}=\rho,\quad E=-\phi_x
$$

$$
A(t)/A(0)\simeq\cos(\omega_pt),\qquad\omega_p=1
$$

Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.

#### PIC: mesh/time convergence, invariants and particle noise

Supplementary execution example · Example definition or validation formula

$$
\mathbb E[|\widehat\rho_1/n|^2]=\frac{2+\cos(2\pi/n)}{3N}
$$

$$
H_h=\frac{w}{2}\sum_iv_i^2+\frac{\Delta x}{2}\sum_jE_j^2
$$

Separate quiet-start refinement of a cold 1D periodic plasma from independent-seed initial particle noise; record charge, momentum, Gauss diagnostics and energy error.

#### Independently coded PIC spatial pipeline

Supplementary execution example · Example definition or validation formula

$$
\rho_j=1-\frac1h\sum_p w_p S_j(x_p),\quad a_p=-\sum_j S_j(x_p)E_j
$$

$$
\widehat E_m=\widehat\rho_m/(ik_m),\quad E_0=0,\quad E_{N/2}=0\ \text{(even N)}
$$

$$
\rho=-\tfrac12\cos2x\ \Longrightarrow\ E=-\tfrac14\sin2x,\quad a=+\tfrac14\sin2x
$$

Compare vectorized CIC/FFT with separately authored scalar-particle CIC/dense DFT; each trajectory sources its own field at every kick.

### Exact and reference solutions

Compare with linear cold-plasma displacement cos(t); check charge compatibility, Poisson residual, self force, and separate grid/timestep series. This is not an exact reference for general nonlinear PIC trajectories. The companion retains stationary background ions and separates charge, momentum and particle/field-energy diagnostics from trajectory error. Its reference is small-amplitude linear theory, supplying no evidence for thermal Landau damping or electromagnetic PIC.

#### [Independently coded PIC spatial pipeline](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en#pic-independent-spatial-en-measurements)

Finite-grid numerical reference · Related-model reference

rho=-.5cos(2x) => E=-.25sin(2x), electron a=+.25sin(2x); independent scalar CIC + dense DFT owns its self-consistent field every kick.

Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.

Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.

#### Cold-plasma oscillation with electrostatic CIC PIC

Separate a 32/64/128-grid sweep from timestep refinement on a 512 grid. Compare displacement amplitude with continuum linear cos(t), and check charge compatibility, potential-Poisson residual and single-particle self force.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en)

#### PIC: mesh/time convergence, invariants and particle noise

Refine 16/32/64 grids and dt=.2/.1/.05 separately; distinguish continuum cos(t) from time-reference errors. Record the real odd derivative’s Nyquist null mode separately from Gauss residuals. Compare time-zero CIC mode power at 64 seeds and N=256/1024/4096 with its analytic expectation.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=en)

#### Independently coded PIC spatial pipeline

19pytest and58/58fixed gates passed. Compare six pairs=twelve self-consistent trajectories at all13states; maximum differences:x8.88e-16,v3.33e-16,E8.33e-16,rho2.89e-15. Shared pytest+main.392s. Initial small pytest retained17/18with a periodic-index failure; integer wrapping was corrected before the first fixed main batch.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Cloud-in-cell assignment and interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en)

Supplementary execution example

Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.

Dimensionless length 2pi, electron charge/mass −1, stationary ion density one and plasma frequency one. A quiet start receives a small sinusoidal displacement of amplitude 0.001.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Finite amplitude and finite particles leave an error floor. Nonlinear instabilities, Landau damping, collisions, electromagnetic/relativistic PIC and open particle boundaries are unvalidated.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)

#### [PIC: mesh/time convergence, invariants and particle noise](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=en)

Supplementary execution example

Separate quiet-start refinement of a cold 1D periodic plasma from independent-seed initial particle noise; record charge, momentum, Gauss diagnostics and energy error.

Length 2pi, stationary unit-density ions, electron q/m=−1, plasma frequency one, sinusoidal displacement 0.001 and final time 1.6. Mesh runs retain 2048 particles; time runs retain a 32-cell mesh and 256 particles. The particle weight is w=2pi/N and n is the grid count.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

DOP853 is not an independent PIC spatial implementation. Distinguish charge/momentum preservation from approximate energy conservation. Initial-noise N scaling does not validate evolved warm plasmas. Landau damping, electromagnetic/relativistic PIC and collisions remain unvalidated.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)

#### [Independently coded PIC spatial pipeline](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en)

Supplementary execution example

Compare vectorized CIC/FFT with separately authored scalar-particle CIC/dense DFT; each trajectory sources its own field at every kick.

Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Independent coding check of discrete spatial operators. It does not change the time integrator/continuum model, establish continuum convergence, or reproduce the cold-plasma oscillation reference. A related supplement of cold-plasma-pic; the finite warm velocity spread is explicit.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/pic-spatial/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/run.py)
- [/code/validated-examples/2026-11-23/pic-spatial/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/primary.py)
- [/code/validated-examples/2026-11-23/pic-spatial/references/scalar_pic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/references/scalar_pic.py)
- [/code/validated-examples/2026-11-23/pic-spatial/test_spatial.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/test_spatial.py)
