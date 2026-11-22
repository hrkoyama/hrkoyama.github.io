# 1次元Eulerエントロピー波 / One-dimensional Euler entropy wave

https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-1d/

## 日本語

[保存済みの1次元エントロピー波の密度誤差・格子収束。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/entropy-1d.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/experiments/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#entropy-1d)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja)

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。

### 厳密解・参照解

一定速度・圧力のもとで正弦状密度を運ぶEulerエントロピー波の解析解と比較します。専用の参照解一覧カードは未収録です。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [WENO5-JS](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

## English

[Stored density-error refinement for a 1D entropy wave.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/entropy-1d.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/experiments/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#entropy-1d-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en)

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.

### Exact and reference solutions

Compare with analytic translation of a sinusoidal Euler entropy wave at constant velocity and pressure. No dedicated card is included in the reference-solution library.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [WENO5-JS](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.
