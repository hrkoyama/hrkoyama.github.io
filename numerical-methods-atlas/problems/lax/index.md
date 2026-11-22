# Lax衝撃波管 / Lax shock tube

https://hrkoyama.github.io/numerical-methods-atlas/problems/lax/

## 日本語

[共有図の左パネル：Lax衝撃波管。右は別のエントロピー波収束計算。](https://hrkoyama.github.io/numerical-methods-atlas/assets/lax-entropy.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#lax)

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

左右状態(0.445,0.698,3.528)と(0.5,0,0.571)、γ=1.4の半解析的Riemann解が基準です。

#### [Euler／Lax問題](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-lax)

半解析解 · 関連モデルの参照

U(x,t) = R((x−x0)/t)

比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。

γ=1.4、左右(0.445,0.698,3.528)/(0.5,0,0.571)、[-5,5]、x0=0、t=1.3が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [HLLC](https://hrkoyama.github.io/numerical-methods-atlas/methods/hllc/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

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

#### [code/numerical-methods-atlas/2026-11-21/tests/test_reference_solutions.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_reference_solutions.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_euler_matches_existing_independent_reference`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_reference_solutions.py -k test_euler_matches_existing_independent_reference
```

## English

[Shared figure, left: Lax shock tube. Right: a separate entropy-wave refinement study.](https://hrkoyama.github.io/numerical-methods-atlas/assets/lax-entropy.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#lax-en)

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

Use the semi-analytic Riemann solution for primitive states (0.445,0.698,3.528) and (0.5,0,0.571), γ=1.4.

#### [Euler / Lax](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-lax)

Semi-analytic reference · Related-model reference

U(x,t) = R((x−x0)/t)

Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity.

γ=1.4, states (0.445,0.698,3.528)/(0.5,0,0.571), [-5,5], x0=0 and t=1.3 match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [HLLC](https://hrkoyama.github.io/numerical-methods-atlas/methods/hllc/?lang=en) — Related explanation; Method-registry status: Educational example / related code

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

#### [code/numerical-methods-atlas/2026-11-21/tests/test_reference_solutions.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_reference_solutions.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_euler_matches_existing_independent_reference`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_reference_solutions.py -k test_euler_matches_existing_independent_reference
```
