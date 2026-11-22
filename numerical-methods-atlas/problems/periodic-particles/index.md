# 周期PM粒子群の質量・内力 / Periodic PM particle mass and internal force

https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/

## 日本語

[共有図の周期PM部分。孤立ツリーの比較は別問題です。](https://hrkoyama.github.io/numerical-methods-atlas/assets/particle-gravity.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#periodic-particles)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja)

$$
\boldsymbol a_i=-G\sum_{j\ne i}m_j\frac{\boldsymbol x_i-\boldsymbol x_j}{(|\boldsymbol x_i-\boldsymbol x_j|^2+\epsilon^2)^{3/2}}
$$

$$
\nabla^2\phi=4\pi G(\rho-\overline\rho)\quad\text{(periodic)}
$$

孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。

#### [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。

#### 周期PM粒子群：質量・内力・格子場

共通実行例 · 問題の式

$$
\nabla^2\phi=4\pi(\rho-\overline\rho),\qquad\widehat\phi_{\boldsymbol0}=0,\qquad\boldsymbol a=-\nabla\phi
$$

$$
\widehat\phi_{\boldsymbol k}=-\frac{4\pi}{k^2}\widehat\rho_{\boldsymbol k}\quad(\boldsymbol k\ne0),\qquad G=1
$$

3次元周期箱L=1、24³格子、同じCIC配置・補間と連続k²のFourier記号。孤立直接和・Ewald・PME・SPMEではない。正弦密度の解析格子解は粒子近接力全体の精度保証ではない。

### 厳密解・参照解

質量保存・質量重み付き内力と、格子PoissonのFourier製造解を確認します。一般の周期粒子直接和との力比較を行ったという意味ではありません。

#### 周期PM粒子群：質量・内力・格子場

CSVは粒子ごとの座標・質量・加速度・力。正弦密度の独立解析場検査はJSONの集計値に保存。PM格子細分化を粒子力の解析誤差として誤表示しない。

- [CSVは粒子ごとの座標・質量・加速度・力。正弦密度の独立解析場検査はJSONの集計値に保存。PM格子細分化を粒子力の解析誤差として誤表示しない。](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/periodic-particles/result.json)
- [別入力密度ρ=ρ₀+A cos(kx)に対するφ=−4πGA cos(kx)/k²、a_x=−4πGA sin(kx)/k。粒子群の厳密な周期力参照ではない。](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/periodic-particles/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/periodic-particles/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [Cloud-in-cellの割当てと補間](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [FFT粒子格子力](https://hrkoyama.github.io/numerical-methods-atlas/methods/pm/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [周期PM粒子群：質量・内力・格子場](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=ja)

共通実行例

入力JSONに保存した19粒子の周期CIC–FFT–CIC計算。質量、内力和、単粒子自己力、整数箱長移動を確認し、別の正弦密度の解析的周期Poisson場と照合。

3次元立方周期箱L=1、G=1、24³格子、正の質量で総和1。座標・質量は全値を入力に保存し、実行時の乱数生成はない。連続k²のFFT逆演算と同じCIC配置・補間を用いる。

[コード / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/periodic-particles.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/periodic-particles.json --output output-periodic-particles
python -m pytest -q tests/test_recipes.py
```

非正質量、非有限入力、G≠1、不適切な格子・正弦モード、非整数箱長移動を拒否。質量・内力和・自己力の一致だけでは個々の粒子力の精度を保証しない。周期直接和、短距離補正、Ewald・P3M・PME・SPME、粒子時間発展は実装しない。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_pm_self_force_and_total_internal_force_with_matched_cic`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_particle_gravity.py -k test_pm_self_force_and_total_internal_force_with_matched_cic
```

## English

[Periodic-PM part of a shared figure; isolated-tree comparisons are a separate problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/particle-gravity.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#periodic-particles-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en)

$$
\boldsymbol a_i=-G\sum_{j\ne i}m_j\frac{\boldsymbol x_i-\boldsymbol x_j}{(|\boldsymbol x_i-\boldsymbol x_j|^2+\epsilon^2)^{3/2}}
$$

$$
\nabla^2\phi=4\pi G(\rho-\overline\rho)\quad\text{(periodic)}
$$

Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution.

#### [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.

#### Periodic PM particles: mass, internal force and mesh field

Common execution example · Problem definition

$$
\nabla^2\phi=4\pi(\rho-\overline\rho),\qquad\widehat\phi_{\boldsymbol0}=0,\qquad\boldsymbol a=-\nabla\phi
$$

$$
\widehat\phi_{\boldsymbol k}=-\frac{4\pi}{k^2}\widehat\rho_{\boldsymbol k}\quad(\boldsymbol k\ne0),\qquad G=1
$$

3D periodic L=1 box and 24³ grid, matched CIC and continuum-k² Fourier symbol. Not isolated summation, Ewald, PME or SPME. The analytic sinusoidal mesh check does not certify all close-pair particle forces.

### Exact and reference solutions

Check mass conservation, mass-weighted internal force and a manufactured Fourier solution of mesh Poisson. This does not establish force accuracy against a general periodic particle direct sum.

#### Periodic PM particles: mass, internal force and mesh field

CSV stores each particle's coordinates, mass, acceleration and force. Independent sinusoidal-field diagnostics are JSON metrics. No mesh refinement is misrepresented as analytic particle-force error.

- [CSV stores each particle's coordinates, mass, acceleration and force. Independent sinusoidal-field diagnostics are JSON metrics. No mesh refinement is misrepresented as analytic particle-force error.](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/periodic-particles/result.json)
- [For separate rho=rho0+A*cos(k*x), phi=-4*pi*G*A*cos(k*x)/k² and ax=-4*pi*G*A*sin(k*x)/k. Not an exact periodic particle-force reference.](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/periodic-particles/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/periodic-particles/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [Cloud-in-cell assignment and interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [FFT particle–mesh forces](https://hrkoyama.github.io/numerical-methods-atlas/methods/pm/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Periodic PM particles: mass, internal force and mesh field](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=en)

Common execution example

Periodic CIC–FFT–CIC calculation for 19 particles stored explicitly in input JSON. Check mass, net internal force, single-particle self-force and integer-box translation; separately compare a sinusoidal density with analytic periodic Poisson fields.

Three-dimensional periodic cube L=1, G=1, 24³ mesh and positive masses summing to one. All positions/masses are stored explicitly; no runtime random generation. Continuum-k² FFT inversion with matched CIC assignment/interpolation.

[Code / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/periodic-particles.json)

[File manifest and hashes](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/periodic-particles.json --output output-periodic-particles
python -m pytest -q tests/test_recipes.py
```

Reject nonpositive masses, nonfinite inputs, G!=1, invalid grids/sinusoidal modes and noninteger box shifts. Mass/net-force/self-force consistency alone does not establish individual particle-force accuracy. No periodic pair-sum reference, short-range correction, Ewald/P3M/PME/SPME or particle evolution.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_pm_self_force_and_total_internal_force_with_matched_cic`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_particle_gravity.py -k test_pm_self_force_and_total_internal_force_with_matched_cic
```
