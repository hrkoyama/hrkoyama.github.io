# 孤立粒子群の軟化重力（ツリー・直接和） / Isolated softened particle gravity: tree versus direct sum

https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/

## 日本語

[保存済みツリー力と直接和の相対誤差。開き角・展開次数を比較。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isolated-particles.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#isolated-particles)

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

#### Barnes–Hut：192粒子と直接和の比較

共通実行例 · 近似・離散化の式

$$
\boldsymbol a_i=-\sum_{j\ne i}m_j\frac{\boldsymbol r_{ij}}{(r_{ij}^{2}+\epsilon^{2})^{3/2}},\qquad G=1,\quad \epsilon=0.03
$$

$$
\boldsymbol a_{\rm cell}\simeq-\frac{M\boldsymbol r}{s^3}+\frac{3\mathbf S\boldsymbol r}{s^5}-\frac{15(\boldsymbol r^{\mathsf T}\mathbf S\boldsymbol r)\boldsymbol r}{2s^7}+\frac{3\operatorname{tr}(\mathbf S)\boldsymbol r}{2s^5}
$$

$$
s^2=r^2+\epsilon^2,\qquad \mathbf S=\sum_jm_j\boldsymbol\delta_j\boldsymbol\delta_j^{\mathsf T}
$$

孤立Plummer核。rᵢⱼ=xᵢ−xⱼ、セルのrは対象点と質量中心の差、δは質量中心からの偏差。order=2では同じ軟化核の完全二次項を使い、trace項を残す。周期重力や軌道計算ではない。

### 厳密解・参照解

同一粒子・同一Plummer軟化の直接対和が数値基準です。ツリー開き角と多重極次数ごとの力誤差を比較します。

#### Barnes–Hut：192粒子と直接和の比較

同じPlummer核の直接和。完全に開いたツリーとの一致と近似力の誤差を分ける。

- [同じPlummer核の直接和。完全に開いたツリーとの一致と近似力の誤差を分ける。](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/forces.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/barnes-hut/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [Barnes–Hut八分木](https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Barnes–Hut：192粒子と直接和の比較](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/barnes-hut/?lang=ja)

共通実行例

孤立・軟化重力の静的な力の比較。軌道計算・周期系・実行速度の比較ではありません。

正の質量を持つ固定192粒子。Plummer軟化、traceを含む完全な二次モーメント項を使い、同じ核の直接和を参照。

[コード / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/input.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python examples/barnes-hut/run.py --input examples/barnes-hut/input.json --output output
python -m pytest -q tests/test_particle_gravity.py
```

孤立・軟化重力の静的な力の比較。軌道計算・周期系・実行速度の比較ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/run.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/run.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py)

## English

[Stored relative tree/direct-sum force errors versus opening angle and expansion order.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isolated-particles.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#isolated-particles-en)

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

#### Barnes–Hut: 192 particles against direct summation

Common execution example · Approximation or discretization

$$
\boldsymbol a_i=-\sum_{j\ne i}m_j\frac{\boldsymbol r_{ij}}{(r_{ij}^{2}+\epsilon^{2})^{3/2}},\qquad G=1,\quad \epsilon=0.03
$$

$$
\boldsymbol a_{\rm cell}\simeq-\frac{M\boldsymbol r}{s^3}+\frac{3\mathbf S\boldsymbol r}{s^5}-\frac{15(\boldsymbol r^{\mathsf T}\mathbf S\boldsymbol r)\boldsymbol r}{2s^7}+\frac{3\operatorname{tr}(\mathbf S)\boldsymbol r}{2s^5}
$$

$$
s^2=r^2+\epsilon^2,\qquad \mathbf S=\sum_jm_j\boldsymbol\delta_j\boldsymbol\delta_j^{\mathsf T}
$$

Isolated Plummer kernel: rᵢⱼ=xᵢ−xⱼ, cell r is target minus center of mass, and δ is the central offset. order=2 retains the softened kernel's full second-moment term, including its trace. No periodic gravity or trajectories.

### Exact and reference solutions

Direct pair summation with identical particles and Plummer softening is the numerical standard. Compare force errors by tree opening angle and multipole order.

#### Barnes–Hut: 192 particles against direct summation

Same-Plummer-kernel direct sum, distinguishing fully opened tree agreement from approximation error.

- [Same-Plummer-kernel direct sum, distinguishing fully opened tree agreement from approximation error.](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/forces.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/barnes-hut/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [Barnes–Hut octree](https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Barnes–Hut: 192 particles against direct summation](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/barnes-hut/?lang=en)

Common execution example

Static isolated softened-gravity force comparison, not orbital integration, periodic gravity or a timing benchmark.

192 fixed particles with positive masses; Plummer softening and the complete second-moment term including its trace, compared with direct summation using the identical kernel.

[Code / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/input.json)

[File manifest and hashes](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python examples/barnes-hut/run.py --input examples/barnes-hut/input.json --output output
python -m pytest -q tests/test_particle_gravity.py
```

Static isolated softened-gravity force comparison, not orbital integration, periodic gravity or a timing benchmark.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/run.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/run.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py)
