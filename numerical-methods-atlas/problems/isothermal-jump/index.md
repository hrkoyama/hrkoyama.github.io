# 等温流体の密度ジャンプ / Isothermal density jump

https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/

## 日本語

[保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isothermal-jump.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#isothermal-jump)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [等温流体方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#isothermal-ja)

$$
\rho_t+(\rho u)_x=0
$$

$$
(\rho u)_t+(\rho u^2+c_s^2\rho)_x=0
$$

一定の等温音速cₛを用いる1次元の代表形。密度ジャンプの参照解へ。

### 厳密解・参照解

音速1、静止した左右密度1と0.125の等温Riemann解が半解析的な基準です。Eulerのエネルギー方程式を含むSodとは別モデルです。

#### [等温流／密度跳躍](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=isothermal-jump)

半解析解 · 関連モデルの参照

U(x,t) = R((x−x0)/t)

p = c_s² rho、一定の音速c_s。初期密度は厳密に正とし、真空状態とエネルギー方程式はありません。

p=ρ、音速1、左右密度(1,0.125)・速度0、x0=0.5が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

#### [code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_benchmark_default_horizon_smoke`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_numerics.py -k test_benchmark_default_horizon_smoke
```

## English

[Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isothermal-jump.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#isothermal-jump-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Isothermal flow equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#isothermal-en)

$$
\rho_t+(\rho u)_x=0
$$

$$
(\rho u)_t+(\rho u^2+c_s^2\rho)_x=0
$$

A one-dimensional form with constant isothermal sound speed cₛ. Follow the density-jump reference solution.

### Exact and reference solutions

Use the semi-analytic isothermal Riemann solution with sound speed one and stationary densities 1 and 0.125. This differs from Sod with an Euler energy equation.

#### [Isothermal / density jump](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=isothermal-jump)

Semi-analytic reference · Related-model reference

U(x,t) = R((x−x0)/t)

p = c_s² rho; constant c_s; strictly positive initial density; no vacuum state or energy equation.

p=ρ, sound speed one, densities (1,0.125), zero velocities and x0=0.5 match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.

#### [code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_benchmark_default_horizon_smoke`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_numerics.py -k test_benchmark_default_horizon_smoke
```
