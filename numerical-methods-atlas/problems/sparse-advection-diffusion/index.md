# 非対称移流拡散離散系の製造解 / Nonsymmetric advection-diffusion discrete manufactured system

https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/

## 日本語

[保存済み非対称離散系の真の残差履歴。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sparse-advection-diffusion.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sparse-nonlinear/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#sparse-advection-diffusion)

### 方程式・問題の定義

定常の離散移流拡散行列です。リンク先は移流項と拡散項の基礎であり、各単独式がこの行列問題全体を表すわけではありません。

#### [線形移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja)

$$
\partial_t u+a\,\partial_xu=0
$$

一定速度aによる輸送。波形の移動、数値拡散、安定性へ。

#### [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja)

$$
\partial_tu=\nu\nabla^2u
$$

一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。

### 厳密解・参照解

既知の離散ベクトルからb=A xを構成する製造系で、真の残差と解誤差を確認します。連続移流拡散方程式の厳密解を使った検証とは区別します。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [再始動GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [BiCGSTAB](https://hrkoyama.github.io/numerical-methods-atlas/methods/bicgstab/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Jacobi／対角前処理](https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobi-preconditioner/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [ピボット選択なしILU(0)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ilu0/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

#### [code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_nonsymmetric_solve_true_residual_and_error`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_sparse_fem.py -k test_nonsymmetric_solve_true_residual_and_error
```

## English

[Stored true-residual histories of the nonsymmetric discrete system.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sparse-advection-diffusion.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/sparse-nonlinear/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#sparse-advection-diffusion-en)

### Equations and problem definitions

This is a steady discrete advection-diffusion matrix. Linked entries explain its transport and diffusion components; neither alone represents the complete matrix problem.

#### [Linear advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en)

$$
\partial_t u+a\,\partial_xu=0
$$

Transport at constant speed a: translation, numerical diffusion and stability.

#### [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en)

$$
\partial_tu=\nu\nabla^2u
$$

A representative constant-diffusivity form: mode decay, time integration and boundaries.

### Exact and reference solutions

Use a manufactured discrete system b=A x from a known vector to check true residual and solution error. Distinguish this from verification against an exact continuum advection-diffusion solution.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [Restarted GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [BiCGSTAB](https://hrkoyama.github.io/numerical-methods-atlas/methods/bicgstab/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Jacobi / diagonal preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobi-preconditioner/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Unpivoted ILU(0)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ilu0/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.

#### [code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_nonsymmetric_solve_true_residual_and_error`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_sparse_fem.py -k test_nonsymmetric_solve_true_residual_and_error
```
