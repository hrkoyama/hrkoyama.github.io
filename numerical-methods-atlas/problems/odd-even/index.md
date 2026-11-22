# 定常平面衝撃波のodd–even診断 / Stationary-shock odd–even diagnostic

https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/

## 日本語

[保存済み定常平面衝撃波のodd–even診断。](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-methods/planar-128-0.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/carbuncle/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#odd-even)

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

Mach-6定常垂直衝撃波の解析的下流状態と、種を与えた行デカップリング指標・無擾乱対照を比較します。一般的な横方向不安定性全体の検証ではありません。

### 計算法

保存された垂直衝撃波診断の流束とRoe音響エントロピー平滑化です。圧力センサー混合法をRotated-RHLLと同一視しません。

- [Roe法](https://hrkoyama.github.io/numerical-methods-atlas/methods/roe/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Roe音響波のエントロピー修正](https://hrkoyama.github.io/numerical-methods-atlas/methods/entropy-fix/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [HLLE／Einfeldt波速](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [AUSM系列の流束分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/ausm/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

## English

[Stored odd–even diagnostic for a stationary planar shock.](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-methods/planar-128-0.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/carbuncle/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#odd-even-en)

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

Compare analytic downstream states of a stationary Mach-6 normal shock with seeded row-decoupling diagnostics and unperturbed controls. This is not validation of every transverse instability.

### Numerical methods

Fluxes and Roe acoustic entropy smoothing used in the stored normal-shock diagnostic. The pressure-sensor blend is not identified as Rotated-RHLL.

- [Roe](https://hrkoyama.github.io/numerical-methods-atlas/methods/roe/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Acoustic Roe entropy correction](https://hrkoyama.github.io/numerical-methods-atlas/methods/entropy-fix/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [HLLE / Einfeldt wave speeds](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [AUSM-family flux splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/ausm/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.
