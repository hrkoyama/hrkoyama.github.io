# Dirichlet境界の熱拡散 / Heat decay with Dirichlet boundaries

https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/

## 日本語

[共有図の左パネル：Dirichlet境界の熱拡散。右パネルは別のPoisson境界問題。](https://hrkoyama.github.io/numerical-methods-atlas/assets/diffusion-boundaries.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#heat-dirichlet)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja)

$$
\partial_tu=\nu\nabla^2u
$$

一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。

### 厳密解・参照解

零Dirichlet境界でのsin(πx)の指数減衰と格子収束を確認します。周期境界・平均値1の参照解一覧の熱モードとは別条件です。

#### [熱拡散／Fourierモードの減衰](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-heat)

解析解 · 関連モデルの参照

u = 1 + 0.25 sin(2πx) exp[−0.02(2π)²t]

単位区間の周期境界、拡散係数0.02。

こちらは零Dirichlet・sin(πx)、参照カードは周期境界・1+0.25sin(2πx)・ν=0.02です。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [前進Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [後退Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Crank–Nicolson法](https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Thomas法／三重対角消去](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

#### [code/numerical-methods-atlas/2026-11-21/tests/test_linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_diffusion_matches_exact_and_refines`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_linear.py -k test_diffusion_matches_exact_and_refines
```

## English

[Shared figure, left: Dirichlet heat decay. Right: separate Poisson boundary problems.](https://hrkoyama.github.io/numerical-methods-atlas/assets/diffusion-boundaries.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#heat-dirichlet-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en)

$$
\partial_tu=\nu\nabla^2u
$$

A representative constant-diffusivity form: mode decay, time integration and boundaries.

### Exact and reference solutions

Check exponential decay of sin(πx) with zero Dirichlet endpoints and mesh refinement. The library heat mode instead has periodic boundaries and mean one.

#### [Heat / Fourier-mode decay](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-heat)

Analytic reference · Related-model reference

u = 1 + 0.25 sin(2πx) exp[−0.02(2π)²t]

Periodic unit interval; viscosity 0.02.

This test has zero Dirichlet endpoints and sin(πx); the card has periodic boundaries, 1+0.25sin(2πx) and ν=0.02.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Forward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Backward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Crank–Nicolson](https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Thomas tridiagonal elimination](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.

#### [code/numerical-methods-atlas/2026-11-21/tests/test_linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_diffusion_matches_exact_and_refines`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_linear.py -k test_diffusion_matches_exact_and_refines
```
