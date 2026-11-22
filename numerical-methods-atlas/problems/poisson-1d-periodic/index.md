# 1次元周期Poisson・擬似時間による定常解 / 1D periodic Poisson / pseudo-time steady solution

https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-periodic/

## 日本語

[保存済み擬似時間定常解の誤差・格子収束。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-periodic.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/hyperbolic-diffusion/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#poisson-1d-periodic)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。

#### [補助的な双曲型拡散系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hyperbolic-diffusion-ja)

$$
\partial_\tau u-\nu\partial_xp=f
$$

$$
\partial_\tau p-T_r^{-1}\partial_xu=-p/T_r
$$

τは擬似時間、Trは緩和時間。定常でp=uₓ、−νuₓₓ=fを回復します。物理時間の熱拡散とは区別します。

### 厳密解・参照解

周期正弦製造解に向かう補助双曲系の擬似時間残差、零平均と格子収束を確認します。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [1次の双曲型拡散ベースライン](https://hrkoyama.github.io/numerical-methods-atlas/methods/hyperbolic-diffusion/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

#### [code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_hyperbolic_diffusion_steady_refinement_and_failure`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_new_models.py -k test_hyperbolic_diffusion_steady_refinement_and_failure
```

## English

[Stored error refinement of the pseudo-time steady solution.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-periodic.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/hyperbolic-diffusion/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#poisson-1d-periodic-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.

#### [Auxiliary hyperbolic diffusion system](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hyperbolic-diffusion-en)

$$
\partial_\tau u-\nu\partial_xp=f
$$

$$
\partial_\tau p-T_r^{-1}\partial_xu=-p/T_r
$$

τ is pseudo-time and Tr a relaxation time. At steady state p=uₓ and −νuₓₓ=f are recovered; this is distinct from physical-time heat diffusion.

### Exact and reference solutions

Check pseudo-time residual, zero mean and mesh refinement toward the periodic sine manufactured solution of the auxiliary hyperbolic system.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [First-order hyperbolic diffusion baseline](https://hrkoyama.github.io/numerical-methods-atlas/methods/hyperbolic-diffusion/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.

#### [code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_hyperbolic_diffusion_steady_refinement_and_failure`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_new_models.py -k test_hyperbolic_diffusion_steady_refinement_and_failure
```
