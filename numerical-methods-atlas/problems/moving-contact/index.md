# 移動接触不連続 / Moving contact discontinuity

https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/

## 日本語

[保存したEuler密度波形（1つの手法を代表表示）。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/moving-contact.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reconstruction/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#moving-contact)

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

一定圧力・速度の周期接触不連続の解析的な平行移動が基準です。Sodの波構造全体を代用しません。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [制限付きPPM再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/ppm/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [WENO5-JS](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [有限差分WENO5-Z](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Eulerの特性変数再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/characteristic-reconstruction/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

## English

[Stored Euler density profile, showing one representative method.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/moving-contact.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reconstruction/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#moving-contact-en)

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

The standard is analytic translation of a periodic contact discontinuity at constant pressure and velocity. The complete Sod wave pattern is not a substitute.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Limited PPM reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/ppm/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [WENO5-JS](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [FD WENO5-Z](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Euler characteristic reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/characteristic-reconstruction/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.
