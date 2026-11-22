# 周期矩形波の線形移流 / Periodic square-wave advection

https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/

## 日本語

[保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-square.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/limiters/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#advection-square)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [線形移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja)

$$
\partial_t u+a\,\partial_xu=0
$$

一定速度aによる輸送。波形の移動、数値拡散、安定性へ。

### 厳密解・参照解

矩形波を周期的に平行移動した不連続解が基準です。参照解一覧の正弦波は同じ移流モデルの別初期値です。

#### [移流／正弦波の平行移動](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-advection)

解析解 · 関連モデルの参照

u = 1 + 0.25 sin[2π(x−t)]

単位区間の周期境界、一定移流速度1。

方程式と周期輸送は共通ですが、参照カードは滑らかな正弦初期値であり、この矩形初期値の参照値ではありません。

### 計算法

保存済みCIPおよびリミター比較の矩形波ケースで使われる手法です。

- [3次Hermite CIP](https://hrkoyama.github.io/numerical-methods-atlas/methods/cip/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Superbee](https://hrkoyama.github.io/numerical-methods-atlas/methods/superbee/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [単調中心勾配制限／MC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Van Leer勾配制限](https://hrkoyama.github.io/numerical-methods-atlas/methods/van-leer/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [切り詰めたVan Albada勾配制限](https://hrkoyama.github.io/numerical-methods-atlas/methods/van-albada/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [TVB修正minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/tvb/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

## English

[Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-square.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/limiters/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#advection-square-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Linear advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en)

$$
\partial_t u+a\,\partial_xu=0
$$

Transport at constant speed a: translation, numerical diffusion and stability.

### Exact and reference solutions

The standard is periodic translation of the discontinuous square profile. The library sine wave uses different initial data for the same transport model.

#### [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-advection)

Analytic reference · Related-model reference

u = 1 + 0.25 sin[2π(x−t)]

Periodic unit interval; constant advection speed 1.

The equation and periodic transport are shared, but the reference uses smooth sine initial data and is not a numerical reference for this square profile.

### Numerical methods

Methods used by the stored square-wave CIP and limiter comparisons.

- [Cubic-Hermite CIP](https://hrkoyama.github.io/numerical-methods-atlas/methods/cip/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Superbee](https://hrkoyama.github.io/numerical-methods-atlas/methods/superbee/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Monotonized central / MC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Van Leer limiter](https://hrkoyama.github.io/numerical-methods-atlas/methods/van-leer/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Clipped Van Albada limiter](https://hrkoyama.github.io/numerical-methods-atlas/methods/van-albada/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [TVB modified minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/tvb/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.
