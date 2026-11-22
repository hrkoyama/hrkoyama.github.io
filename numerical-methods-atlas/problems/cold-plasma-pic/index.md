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

#### CIC静電PICの冷たいプラズマ振動

補助実行例 · 実行例の定義・検証式

$$
\dot x_i=v_i,\quad\dot v_i=-E_h(x_i),\quad-\phi_{xx}=\rho,\quad E=-\phi_x
$$

$$
A(t)/A(0)\simeq\cos(\omega_pt),\qquad\omega_p=1
$$

1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。

### 厳密解・参照解

小振幅の冷たいプラズマの線形変位cos(t)と比較し、電荷整合性・Poisson残差・自己力、格子系列と時間刻み系列を確認します。一般の非線形PIC軌道の厳密解という主張ではありません。

#### CIC静電PICの冷たいプラズマ振動

32・64・128格子の系列と、別の512格子上の時間刻み系列を分けます。変位モードを連続線形理論のcos(t)と比較し、全電荷・Poissonポテンシャル残差・単一粒子の自己力を検査します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [Particle-in-Cell（PIC）](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

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

#### Cold-plasma oscillation with electrostatic CIC PIC

Supplementary execution example · Example definition or validation formula

$$
\dot x_i=v_i,\quad\dot v_i=-E_h(x_i),\quad-\phi_{xx}=\rho,\quad E=-\phi_x
$$

$$
A(t)/A(0)\simeq\cos(\omega_pt),\qquad\omega_p=1
$$

Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.

### Exact and reference solutions

Compare with linear cold-plasma displacement cos(t); check charge compatibility, Poisson residual, self force, and separate grid/timestep series. This is not an exact reference for general nonlinear PIC trajectories.

#### Cold-plasma oscillation with electrostatic CIC PIC

Separate a 32/64/128-grid sweep from timestep refinement on a 512 grid. Compare displacement amplitude with continuum linear cos(t), and check charge compatibility, potential-Poisson residual and single-particle self force.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

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
