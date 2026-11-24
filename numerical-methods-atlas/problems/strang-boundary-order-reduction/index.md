# Dirichlet境界でのStrang次数低下と補正 / Strang splitting: Dirichlet boundary order reduction and correction

https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/

## 日本語

[実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。 保存済みの数値場と参照を用いた図です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-ode-adaptivity/#strang-boundary-order-reduction) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#strang-boundary-order-reduction)

### 方程式・問題の定義

u_t=u_xx+u、[0,1]、両端u=1、解析定常解+.1正弦摂動、T=.1。内部31/63/127点・8/16/32/64刻みとLie対照4run、計28run。

#### [非同次境界を持つ線形反応拡散](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#inhomogeneous-reaction-diffusion-ja)

$$
u_t=u_{xx}+u,\quad0<x<1,\quad u(0,t)=u(1,t)=1
$$

同じ非周期有限差分系に対する時間誤差と、連続厳密解に対する空間誤差を分けます。

#### [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja)

$$
\partial_tu=\nu\nabla^2u
$$

一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。

#### Dirichlet境界でのStrang次数低下と補正

補助実行例 · 実行例の定義・検証式

$$
u_t=u_{xx}+u,\quad u(0,t)=u(1,t)=1,\quad w=u-1
$$

$$
A_{\rm raw}(w)=L_hw,\ B_{\rm raw}(w)=w+1;\quad A_{\rm corr}(w)=L_hw+1,\ B_{\rm corr}(w)=w
$$

実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。

### 厳密解・参照解

独立疎affine指数作用と別記述の正弦和を先に資格。同FD時間誤差・解析連続解との差・固定格子/刻み領域の観測次数を判定。

#### [Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja#strang-boundary-order-reduction-ja-measurements)

半解析解 · 同じ問題の参照

u_t=u_{xx}+u,\quad u(0,t)=u(1,t)=1,\quad w=u-1;\quad A_{\rm raw}(w)=L_hw,\ B_{\rm raw}(w)=w+1;\quad A_{\rm corr}(w)=L_hw+1,\ B_{\rm corr}(w)=w

u_t=u_xx+u、[0,1]、両端u=1、解析定常解+.1正弦摂動、T=.1。内部31/63/127点・8/16/32/64刻みとLie対照4run、計28run。

原著の線形特殊例で非線形数値表の再現ではありません。非自律/一般境界や普遍的な次数低下は主張せず、Lie終端の反応trace不整合も別表示します。

#### Dirichlet境界でのStrang次数低下と補正

独立疎affine指数作用と別記述の正弦和を先に資格。同FD時間誤差・解析連続解との差・固定格子/刻み領域の観測次数を判定。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja)

### 計算法

w=u−1で未補正(Lw,w+1)、補正(Lw+1,w)に分割。実DirichletDST-I指数流を合成し、反応の境界不整合を保持します。

- [Strang分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Lie–Trotter分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja)

補助実行例

実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。

u_t=u_xx+u、[0,1]、両端u=1、解析定常解+.1正弦摂動、T=.1。内部31/63/127点・8/16/32/64刻みとLie対照4run、計28run。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

原著の線形特殊例で非線形数値表の再現ではありません。非自律/一般境界や普遍的な次数低下は主張せず、Lie終端の反応trace不整合も別表示します。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)

## English

[Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization. This preview reads saved numerical fields and references only.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-ode-adaptivity/#strang-boundary-order-reduction) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#strang-boundary-order-reduction-en)

### Equations and problem definitions

Solve u_t = u_xx + u on [0, 1] with both boundary values equal to 1, an analytic steady state plus a 0.1 sine perturbation, and T = 0.1. Use 31, 63 and 127 interior nodes with 8, 16, 32 and 64 steps, plus four Lie controls: 28 runs.

#### [Linear reaction-diffusion with inhomogeneous boundaries](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#inhomogeneous-reaction-diffusion-en)

$$
u_t=u_{xx}+u,\quad0<x<1,\quad u(0,t)=u(1,t)=1
$$

Separate temporal errors relative to the same nonperiodic finite-difference system from spatial errors relative to the continuous exact family.

#### [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en)

$$
\partial_tu=\nu\nabla^2u
$$

A representative constant-diffusivity form: mode decay, time integration and boundaries.

#### Strang splitting: Dirichlet boundary order reduction and correction

Supplementary execution example · Example definition or validation formula

$$
u_t=u_{xx}+u,\quad u(0,t)=u(1,t)=1,\quad w=u-1
$$

$$
A_{\rm raw}(w)=L_hw,\ B_{\rm raw}(w)=w+1;\quad A_{\rm corr}(w)=L_hw+1,\ B_{\rm corr}(w)=w
$$

Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization.

### Exact and reference solutions

First qualify an independent sparse affine exponential action against separately written sine sums. Then separate temporal error against the same finite-difference system, spatial error against the analytic continuum field, and observed order in the fixed regime.

#### [Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en#strang-boundary-order-reduction-en-measurements)

Semi-analytic reference · Reference for the same problem

u_t=u_{xx}+u,\quad u(0,t)=u(1,t)=1,\quad w=u-1;\quad A_{\rm raw}(w)=L_hw,\ B_{\rm raw}(w)=w+1;\quad A_{\rm corr}(w)=L_hw+1,\ B_{\rm corr}(w)=w

Solve u_t = u_xx + u on [0, 1] with both boundary values equal to 1, an analytic steady state plus a 0.1 sine perturbation, and T = 0.1. Use 31, 63 and 127 interior nodes with 8, 16, 32 and 64 steps, plus four Lie controls: 28 runs.

This is an authored linear specialization, not a reproduction of the original nonlinear tables. It makes no general claim for nonautonomous boundaries or universal order loss. The final reaction-trace mismatch of Lie splitting is disclosed separately.

#### Strang splitting: Dirichlet boundary order reduction and correction

First qualify an independent sparse affine exponential action against separately written sine sums. Then separate temporal error against the same finite-difference system, spatial error against the analytic continuum field, and observed order in the fixed regime.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en)

### Numerical methods

For w = u - 1, use the unmodified split (Lw, w + 1) or the corrected split (Lw + 1, w). Compose actual Dirichlet DST-I flows and retain the reaction boundary mismatch.

- [Strang splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Lie–Trotter splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en)

Supplementary execution example

Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization.

Solve u_t = u_xx + u on [0, 1] with both boundary values equal to 1, an analytic steady state plus a 0.1 sine perturbation, and T = 0.1. Use 31, 63 and 127 interior nodes with 8, 16, 32 and 64 steps, plus four Lie controls: 28 runs.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This is an authored linear specialization, not a reproduction of the original nonlinear tables. It makes no general claim for nonautonomous boundaries or universal order loss. The final reaction-trace mismatch of Lie splitting is disclosed separately.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)
