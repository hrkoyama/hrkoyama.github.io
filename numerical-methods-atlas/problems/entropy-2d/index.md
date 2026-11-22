# 2次元の滑らかなEulerエントロピー波 / Smooth two-dimensional Euler entropy wave

https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/

## 日本語

[保存済み2次元エントロピー波の格子収束。](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/smooth-refinement.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reconstruction/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#entropy-2d)

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

速度(0.7,0.3)・圧力一定の2次元周期正弦密度波について、解析的な保存変数セル平均と格子収束を確認します。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [単調中心勾配制限／MC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

#### [code/numerical-methods-atlas/2026-11-21/tests/test_muscl2d.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_muscl2d.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_smooth_2d_cell_average_refinement_and_periodic_conservation`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_muscl2d.py -k test_smooth_2d_cell_average_refinement_and_periodic_conservation
```

## English

[Stored refinement study for the 2D entropy wave.](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/smooth-refinement.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reconstruction/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#entropy-2d-en)

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

Check analytic conserved cell averages and mesh refinement for the 2D periodic sine-density wave with velocity (0.7,0.3) and constant pressure.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Monotonized central / MC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.

#### [code/numerical-methods-atlas/2026-11-21/tests/test_muscl2d.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_muscl2d.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_smooth_2d_cell_average_refinement_and_periodic_conservation`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_muscl2d.py -k test_smooth_2d_cell_average_refinement_and_periodic_conservation
```
