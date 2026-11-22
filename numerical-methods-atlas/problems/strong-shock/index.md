# 1次元の強い圧力ジャンプ / One-dimensional strong pressure jump

https://hrkoyama.github.io/numerical-methods-atlas/problems/strong-shock/

## 日本語

[完了したPPM計算の保存密度。停止した他の変種とは区別しています。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/strong-shock.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/shock-expansion/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#strong-shock)

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

この強い圧力段差の初期値を使った半解析的Riemann参照を保存しています。参照解一覧の標準Sodとは初期値が異なります。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [制限付きPPM再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/ppm/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [HLLC](https://hrkoyama.github.io/numerical-methods-atlas/methods/hllc/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [HLLE／Einfeldt波速](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [AUSM系列の流束分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/ausm/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

## English

[Stored density from a completed PPM run, distinct from variants that stopped.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/strong-shock.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/shock-expansion/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#strong-shock-en)

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

A semi-analytic Riemann reference is stored for this strong pressure jump. Its initial states differ from the library's standard Sod problem.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [Limited PPM reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/ppm/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [HLLC](https://hrkoyama.github.io/numerical-methods-atlas/methods/hllc/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [HLLE / Einfeldt wave speeds](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [AUSM-family flux splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/ausm/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.
