# 湿潤床ダム崩壊 / Wet-bed dam break

https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/

## 日本語

[保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/dam-break.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#dam-break)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-ja)

$$
h_t+(hu)_x=0
$$

$$
(hu)_t+(hu^2+gh^2/2)_x=0
$$

$$
u_t-fv=-g\eta_x,\quad v_t+fu=-g\eta_y
$$

$$
\eta_t+H(u_x+v_y)=0
$$

前2式は平坦床・摩擦なしの1次元系。後2行は水深Hまわりの線形回転系。非線形流れのテストと、回転系のFourier記号の検証を区別します。

### 厳密解・参照解

水深2と1、静止状態、g=1の湿潤河床Riemann解を半解析的に評価します。乾燥河床解の収録は、この有限体積コードの乾燥状態対応を意味しません。

#### [浅水流／水深が正のダム崩壊](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=swe-dam-break)

半解析解 · 関連モデルの参照

U(x,t) = R((x−x0)/t)

平坦な底面と一定の重力g。乾床は参照解のみの対応で、既存の有限体積ソルバーでは扱えません。

湿潤河床、g=1、左右水深(2,1)・速度0、x0=0.5が一致します。乾燥河床例への対応ではありません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

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

[Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/dam-break.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#dam-break-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Shallow-water equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-en)

$$
h_t+(hu)_x=0
$$

$$
(hu)_t+(hu^2+gh^2/2)_x=0
$$

$$
u_t-fv=-g\eta_x,\quad v_t+fu=-g\eta_y
$$

$$
\eta_t+H(u_x+v_y)=0
$$

The first two equations are 1D flat-bed, frictionless flow; the remaining lines are the linear rotating system about depth H. Distinguish nonlinear flow tests from rotating-system Fourier-symbol checks.

### Exact and reference solutions

Use the semi-analytic wet-bed Riemann solution for depths 2 and 1, initially at rest, g=1. Library dry-bed formulas do not establish dry-state support in this finite-volume code.

#### [Shallow water / wet dam break](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=swe-dam-break)

Semi-analytic reference · Related-model reference

U(x,t) = R((x−x0)/t)

Flat bottom; constant g; dry states allowed in the reference only, not the existing FV solver.

Wet bed, g=1, depths (2,1), zero velocities and x0=0.5 match; this is not a dry-bed correspondence. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

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
