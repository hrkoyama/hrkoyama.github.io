# 周期移動等エントロピー渦 / Periodic moving isentropic vortex

https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/

## 日本語

[保存したKEEP移動渦の最終フレーム。](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/keep-vortex/frame-080.webp)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/keep/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#isentropic-vortex)

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

滑らかな周期等エントロピー渦の解析的移動解と格子・時間刻みの収束を確認します。非圧縮Taylor–Green渦の参照式とは別問題です。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [直交座標の原KEEP分割流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/keep/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

## English

[Stored final frame of the KEEP moving vortex.](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/keep-vortex/frame-080.webp)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/keep/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#isentropic-vortex-en)

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

Check analytic transport of a smooth periodic isentropic vortex with space/time refinement. This differs from the incompressible Taylor–Green reference.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [Original Cartesian KEEP split flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/keep/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.
