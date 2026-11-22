# 中性周期点電荷：Ewald・smooth PME / Neutral periodic charges: Ewald and smooth PME

https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/

## 日本語

[中性立方セルの非対称8点電荷。Ewaldの実空間・逆空間打切りに対する力の差を保存値から表示。smooth PMEの格子・Bスプライン次数比較は同じ問題の補助例へ接続。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/ewald.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-particles/#ewald) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#neutral-periodic-charges)

### 方程式・問題の定義

リンクは静電Poisson/Laplace場です。中性周期Coulomb電荷のEwald/PME問題であり、重力の質量・符号・境界を流用しません。

#### [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。

#### 中性周期セルのEwald和と独立theta積分

補助実行例 · 実行例の定義・検証式

$$
E=\frac12\sum_{ij\mathbf n}^{\prime}q_iq_j\frac{\operatorname{erfc}(\alpha r_{ij\mathbf n})}{r_{ij\mathbf n}}+\frac{2\pi}{V}\sum_{\mathbf k\ne0}\frac{e^{-k^2/(4\alpha^2)}}{k^2}|S(\mathbf k)|^2-\frac{\alpha}{\sqrt\pi}\sum_iq_i^2
$$

$$
M_{\rm NaCl}=\frac2{\sqrt\pi}\int_0^\infty[1-\vartheta_4(0,e^{-u^2})^3]du
$$

3次元周期Coulomb相互作用の実空間和・逆空間和・自己項を実装し、分割パラメータと打切りを変えて検証します。

#### Bスプラインsmooth PMEの格子・次数収束

補助実行例 · 実行例の定義・検証式

$$
Q_{\mathbf j}=\sum_iq_i\prod_{a=1}^3M_p(u_{ia}-j_a+p/2)
$$

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

電荷をBスプラインで格子へ割り当て、FFTでEwald逆空間項を評価するsmooth PME（SPME）の小規模例です。

#### Ewald：非対称周期セルのエネルギー・力と独立theta積分

補助実行例 · 実行例の定義・検証式

$$
E=\frac{1}{\sqrt\pi}\int_0^\infty\left[\sum_{ij}q_iq_j\Theta(\mathbf r_i-\mathbf r_j,u)-\sum_iq_i^2\right]du
$$

$$
\mathbf F_i=-\nabla_iE
$$

中性8電荷の全エネルギーと24力成分を、別実装のGaussian/theta積分と比較。分割・実空間・逆空間の打切り、保存則と不変性を分けて測定します。

#### SPME：格子・補間次数・格子位相と保存則

補助実行例 · 実行例の定義・検証式

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

$$
\sum_j M_p(u-j)=1,\qquad\sum_j M_p^{\prime}(u-j)=0
$$

BスプラインSPMEを同じ独立theta参照へ照合し、格子・次数・位相への依存、電荷の保持、エネルギー勾配と合力を測ります。

### 厳密解・参照解

同じ中性周期電荷・規約の収束したEwald和、力の有限差分とカットオフ・格子収束を確認します。孤立重力粒子の直接和とは境界・相互作用が異なります。 追加版は同じ中性8点電荷・立方体・tin-foil規約のエネルギーと全粒子力を、別実装theta積分と参照自身の細分化に照合します。SPMEはB-splineのエネルギー勾配型であり、原Lagrange PMEや厳密運動量保存を主張しません。

#### 中性周期セルのEwald和と独立theta積分

分割alphaを3点、実空間打切りを3点、逆空間打切りを4点で確認。NaClのMadelung定数は3次元和を呼ばない独立な1次元Jacobi-theta積分と照合し、求積の誤差推定も保存します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=ja)

#### Bスプラインsmooth PMEの格子・次数収束

16³・24³・40³格子と2つの次数で、直接Ewald逆空間和との差を記録します。Ewaldと実空間項・自己項を共有する部分も明示。最細格子の力はエネルギー差分とも比較し、全電荷の保持を確認します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=ja)

#### Ewald：非対称周期セルのエネルギー・力と独立theta積分

参照の求積・theta/像の打切り・切替点をまとめて精密化し、上限32→40の感度を別に記録します。alpha3点、実空間4点・逆空間5点、平行移動・並べ替え、合力、エネルギー差分の3成分を比較。粗い打切りの不正確さを検出する対照も残します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=ja)

#### SPME：格子・補間次数・格子位相と保存則

独立thetaエネルギー・全力との差と、共有Ewald経路自体の誤差を明記します。分配の総和・導関数総和、電荷、エネルギー差分3成分、位相間の幅、有限格子の合力と粗い格子の対照を保存します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [Ewald法](https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Particle Mesh Ewald（PME）](https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Smooth PME（SPME）](https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [中性周期セルのEwald和と独立theta積分](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=ja)

補助実行例

3次元周期Coulomb相互作用の実空間和・逆空間和・自己項を実装し、分割パラメータと打切りを変えて検証します。

立方セル・全電荷ゼロ・Coulomb定数1・導体境界（tin foil）。主例は非対称な8点電荷で、NaClの8イオン配置は別の解析照合用です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

非中性セル、背景補正、非直交セル、誘電率が有限の表面項、スラブ補正、応力、物質固有の力場は扱いません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)

#### [Bスプラインsmooth PMEの格子・次数収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=ja)

補助実行例

電荷をBスプラインで格子へ割り当て、FFTでEwald逆空間項を評価するsmooth PME（SPME）の小規模例です。

Ewaldと同じ中性立方セルと実空間項を使います。PME族のうちEssmannらのBスプライン変種を採用し、Dardenらの原法のLagrange補間とは区別します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

有限格子のaliasingにより、エネルギー勾配型の合力は厳密にはゼロでなく、その診断量を保存します。運動量保存・長時間MD・原法PME・最適化P³M・スラブ補正の検証ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)

#### [Ewald：非対称周期セルのエネルギー・力と独立theta積分](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=ja)

補助実行例

中性8電荷の全エネルギーと24力成分を、別実装のGaussian/theta積分と比較。分割・実空間・逆空間の打切り、保存則と不変性を分けて測定します。

Coulomb定数1、単位立方体の3次元周期、全電荷0、tin-foil境界。旧版と同じ非対称配置です。独立参照も同じ零モードと自己項の規約を使います。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

固定した中性立方セルだけです。上限感度は厳密な全配置の裾誤差保証ではありません。theta参照は別定式化の自作実装であり、第三者計算パッケージや公表された参照数表ではありません。非中性・非直交・スラブ・応力・長時間MDは対象外です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)

#### [SPME：格子・補間次数・格子位相と保存則](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=ja)

補助実行例

BスプラインSPMEを同じ独立theta参照へ照合し、格子・次数・位相への依存、電荷の保持、エネルギー勾配と合力を測ります。

同じ中性周期8電荷、alpha=5.6、実空間像3。PME族のEssmann型SPMEであり、1993年のLagrange補間の原法とは区別します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

エネルギー勾配型では有限格子のaliasingにより合力は一般にゼロではありません。厳密な運動量保存や任意配置での同じ誤差、長時間MD、原法PME、SPME全変種の検証とはしません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)

## English

[Asymmetric eight-charge neutral cubic cell: saved force differences over Ewald real/reciprocal cutoffs. The same problem links to a smooth-PME mesh/B-spline-order supplement.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/ewald.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-particles/#ewald) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#neutral-periodic-charges-en)

### Equations and problem definitions

The link is the electrostatic Poisson/Laplace field. This is neutral periodic Coulomb Ewald/PME, not an interchange of gravitational masses, signs or boundaries.

#### [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.

#### Neutral-cell Ewald sums and an independent theta integral

Supplementary execution example · Example definition or validation formula

$$
E=\frac12\sum_{ij\mathbf n}^{\prime}q_iq_j\frac{\operatorname{erfc}(\alpha r_{ij\mathbf n})}{r_{ij\mathbf n}}+\frac{2\pi}{V}\sum_{\mathbf k\ne0}\frac{e^{-k^2/(4\alpha^2)}}{k^2}|S(\mathbf k)|^2-\frac{\alpha}{\sqrt\pi}\sum_iq_i^2
$$

$$
M_{\rm NaCl}=\frac2{\sqrt\pi}\int_0^\infty[1-\vartheta_4(0,e^{-u^2})^3]du
$$

Implement real-space, reciprocal-space and self Ewald terms for neutral 3D periodic Coulomb charges; vary splitting and cutoffs.

#### Mesh/order convergence of B-spline smooth PME

Supplementary execution example · Example definition or validation formula

$$
Q_{\mathbf j}=\sum_iq_i\prod_{a=1}^3M_p(u_{ia}-j_a+p/2)
$$

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

A small smooth-PME example assigns charge with B-splines and evaluates the Ewald reciprocal contribution by FFT.

#### Ewald: asymmetric-cell energies and forces versus independent theta integration

Supplementary execution example · Example definition or validation formula

$$
E=\frac{1}{\sqrt\pi}\int_0^\infty\left[\sum_{ij}q_iq_j\Theta(\mathbf r_i-\mathbf r_j,u)-\sum_iq_i^2\right]du
$$

$$
\mathbf F_i=-\nabla_iE
$$

Compare a neutral eight-charge cell energy and all 24 force components with a separately coded Gaussian/theta integral. Separate splitting and real/reciprocal truncation from invariants and conservation.

#### SPME: mesh, interpolation order, mesh phase and conservation

Supplementary execution example · Example definition or validation formula

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

$$
\sum_j M_p(u-j)=1,\qquad\sum_j M_p^{\prime}(u-j)=0
$$

Compare B-spline SPME with the same independent theta reference; measure mesh/order/phase effects, charge partition, energy gradients and net force.

### Exact and reference solutions

Check converged Ewald sums for identical neutral periodic charges/conventions, force finite differences and cutoff/mesh refinement. Boundaries and interactions differ from isolated gravitational direct sums. The companion compares energy and every force for the same neutral eight-charge cubic tin-foil cell against a separately implemented theta integral and its own refinement. SPME uses B-spline energy gradients; original Lagrange PME and exact momentum conservation are not claimed.

#### Neutral-cell Ewald sums and an independent theta integral

Three splitting parameters, three real cutoffs and four reciprocal cutoffs. Check the NaCl Madelung constant against a separately implemented 1D Jacobi-theta integral, storing its quadrature error estimate.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=en)

#### Mesh/order convergence of B-spline smooth PME

Meshes 16³/24³/40³ and two orders are compared with directly summed Ewald reciprocal terms. Shared real/self terms are stated. Check finest-grid force derivatives by energy differences and verify assigned total charge.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=en)

#### Ewald: asymmetric-cell energies and forces versus independent theta integration

Record combined refinement of reference quadrature/theta/image/switch controls and a separate upper-limit 32-to-40 sensitivity. Compare three alpha values, four real and five reciprocal cutoffs, translation/permutation, net force and three energy-difference derivatives. Retain an intentionally inaccurate coarse-cutoff control.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=en)

#### SPME: mesh, interpolation order, mesh phase and conservation

Report full energy/force errors against theta integration and explicitly check the shared Ewald path. Store assignment and derivative sums, charge, three finite-difference derivatives, phase spread, finite-mesh net force and a coarse-mesh control.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [Ewald summation](https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Particle mesh Ewald / PME](https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Smooth particle mesh Ewald / SPME](https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Neutral-cell Ewald sums and an independent theta integral](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/?lang=en)

Supplementary execution example

Implement real-space, reciprocal-space and self Ewald terms for neutral 3D periodic Coulomb charges; vary splitting and cutoffs.

Cubic cell, zero total charge, Coulomb constant one and conducting/tin-foil boundary. An asymmetric eight-charge case is distinct from the eight-ion NaCl reference cell.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

No charged-cell/background correction, triclinic cell, finite-dielectric surface term, slab correction, stress or material-specific force field.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)

#### [Mesh/order convergence of B-spline smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/?lang=en)

Supplementary execution example

A small smooth-PME example assigns charge with B-splines and evaluates the Ewald reciprocal contribution by FFT.

The neutral cubic cell and real-space term match the Ewald example. The adopted PME-family variant uses Essmann-type B-splines, distinct from Darden’s original Lagrange interpolation.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Finite-mesh aliasing permits nonzero net force for this energy-gradient variant; that diagnostic is reported. No exact momentum conservation, long MD, original PME, optimized P³M or slab validation is claimed.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)

#### [Ewald: asymmetric-cell energies and forces versus independent theta integration](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=en)

Supplementary execution example

Compare a neutral eight-charge cell energy and all 24 force components with a separately coded Gaussian/theta integral. Separate splitting and real/reciprocal truncation from invariants and conservation.

Coulomb constant one; unit cubic 3D periodic neutral cell with tin-foil boundary. The asymmetric configuration matches the earlier example; reference zero-mode and self conventions match the model.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

One fixed neutral cubic cell. Upper-limit sensitivity is not a rigorous tail bound for arbitrary configurations. The theta reference is an independently formulated original implementation, not an external package or published numerical table. Charged/triclinic/slab cells, stress and long MD are outside scope.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)

#### [SPME: mesh, interpolation order, mesh phase and conservation](https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=en)

Supplementary execution example

Compare B-spline SPME with the same independent theta reference; measure mesh/order/phase effects, charge partition, energy gradients and net force.

Same neutral periodic eight-charge cell, alpha=5.6 and three real-space image shells. This is Essmann-style SPME in the PME family, distinct from the original 1993 Lagrange interpolation.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Finite-mesh aliasing generally gives nonzero net force for this energy-gradient variant. No exact momentum conservation, arbitrary-configuration error bound, long MD, original PME or every SPME variant is certified.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)
