# 冷たいPlummer密度由来32粒子の短時間力学 / Short-time32body dynamics from a cold Plummer-density sample

https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/

## 日本語

[固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-gravity-dynamics/#gravity-plummer-short) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#gravity-plummer-short)

### 方程式・問題の定義

固定32等質量・切断r3の密度由来反対称座標、初速0、epsilon.05、T.2。密度尺度a1とは別。

#### [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja)

$$
\boldsymbol a_i=-G\sum_{j\ne i}m_j\frac{\boldsymbol x_i-\boldsymbol x_j}{(|\boldsymbol x_i-\boldsymbol x_j|^2+\epsilon^2)^{3/2}}
$$

$$
\nabla^2\phi=4\pi G(\rho-\overline\rho)\quad\text{(periodic)}
$$

孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。

#### 冷たいPlummer密度由来32粒子の短時間力学

補助実行例 · 実行例の定義・検証式

$$
a_i=-\sum_{j\ne i}Gm_jr_{ij}/(r_{ij}^2+\epsilon^2)^{3/2}
$$

$$
U=-\sum_{i<j}Gm_im_j/\sqrt{r_{ij}^2+\epsilon^2}
$$

同じ軟化有限N ODEで時間誤差と木近似誤差を分け、独立DOP853・直接力と収支を比較。

### 厳密解・参照解

非零の固定尺度、同一座標上の力、同期E/P/L/COM、theta0対照、非対称静的probe。

#### [冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja#gravity-plummer-short-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

a_i=-sum_{j!=i}G*m_j*r_ij/(r_ij^2+eps^2)^(3/2); U=-sum_{i<j}G*m_i*m_j/sqrt(r_ij^2+eps^2).

固定32等質量・切断r3の密度由来反対称座標、初速0、epsilon.05、T.2。密度尺度a1とは別。 非零の固定尺度、同一座標上の力、同期E/P/L/COM、theta0対照、非対称静的probe。 冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。

冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。

#### 冷たいPlummer密度由来32粒子の短時間力学

非零の固定尺度、同一座標上の力、同期E/P/L/COM、theta0対照、非対称静的probe。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja)

### 計算法

直接KDK20/40/80steps、最細でtheta0/.35/.6のfull second-moment BH。独立scalar対力+DOP853を2許容値で資格確認。

- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Barnes–Hut八分木](https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja)

補助実行例

同じ軟化有限N ODEで時間誤差と木近似誤差を分け、独立DOP853・直接力と収支を比較。

固定32等質量・切断r3の密度由来反対称座標、初速0、epsilon.05、T.2。密度尺度a1とは別。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/gravity-dynamics/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/run.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/dynamics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/dynamics.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/references/exact.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/test_dynamics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/test_dynamics.py)

## English

[Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-gravity-dynamics/#gravity-plummer-short) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#gravity-plummer-short-en)

### Equations and problem definitions

Fixed32equal masses,antipodal truncatedr3 density-derived positions,zero velocity,epsilon.05,T.2; density scalea1 differs from pair softening.

#### [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en)

$$
\boldsymbol a_i=-G\sum_{j\ne i}m_j\frac{\boldsymbol x_i-\boldsymbol x_j}{(|\boldsymbol x_i-\boldsymbol x_j|^2+\epsilon^2)^{3/2}}
$$

$$
\nabla^2\phi=4\pi G(\rho-\overline\rho)\quad\text{(periodic)}
$$

Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution.

#### Short-time32body dynamics from a cold Plummer-density sample

Supplementary execution example · Example definition or validation formula

$$
a_i=-\sum_{j\ne i}Gm_jr_{ij}/(r_{ij}^2+\epsilon^2)^{3/2}
$$

$$
U=-\sum_{i<j}Gm_im_j/\sqrt{r_{ij}^2+\epsilon^2}
$$

Separate time and tree-force errors for the same softened finite-N ODE with independent DOP853/direct-force references and budgets.

### Exact and reference solutions

Nonzero fixed scales,same-position force comparison,synchronizedE/P/L/COM,theta0 control and asymmetric static probe.

#### [Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en#gravity-plummer-short-en-measurements)

Finite-grid numerical reference · Reference for the same problem

a_i=-sum_{j!=i}G*m_j*r_ij/(r_ij^2+eps^2)^(3/2); U=-sum_{i<j}G*m_i*m_j/sqrt(r_ij^2+eps^2).

Fixed32equal masses,antipodal truncatedr3 density-derived positions,zero velocity,epsilon.05,T.2; density scalea1 differs from pair softening.

Cold finite-N initial value,not an equilibrium Plummer DF or exact continuum orbit. No general BH reciprocity/global symplecticity claim.

#### Short-time32body dynamics from a cold Plummer-density sample

Nonzero fixed scales,same-position force comparison,synchronizedE/P/L/COM,theta0 control and asymmetric static probe.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en)

### Numerical methods

Direct KDK20/40/80steps; finest-dt full second-moment BHtheta0/.35/.6; qualify independent scalar-pair DOP853 at two tolerances.

- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Barnes–Hut octree](https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en)

Supplementary execution example

Separate time and tree-force errors for the same softened finite-N ODE with independent DOP853/direct-force references and budgets.

Fixed32equal masses,antipodal truncatedr3 density-derived positions,zero velocity,epsilon.05,T.2; density scalea1 differs from pair softening.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Cold finite-N initial value,not an equilibrium Plummer DF or exact continuum orbit. No general BH reciprocity/global symplecticity claim.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/gravity-dynamics/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/run.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/dynamics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/dynamics.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/references/exact.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/test_dynamics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/test_dynamics.py)
