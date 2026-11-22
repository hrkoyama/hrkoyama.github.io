# 減衰Newton法による3次方程式の求根 / Damped Newton root of a cubic equation

https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/

## 日本語

[公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/cubic-root.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sparse-nonlinear/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#cubic-root)

### 方程式・問題の定義

スカラー代数方程式x³-1=0。非線形境界値問題Bratuとは別の検証です。

### 厳密解・参照解

x³-1=0の既知の実根x=1と残差を用い、Armijo減衰Newtonの収束を確認します。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

#### [code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_damped_newton_backtracks_and_reports_failure`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_sparse_fem.py -k test_damped_newton_backtracks_and_reports_failure
```

## English

[Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/cubic-root.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/sparse-nonlinear/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#cubic-root-en)

### Equations and problem definitions

Scalar algebraic equation x³-1=0, a distinct test from the nonlinear Bratu boundary-value problem.

### Exact and reference solutions

Use the known real root x=1 of x³-1=0 and its residual to check Armijo-damped Newton convergence.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.

#### [code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_damped_newton_backtracks_and_reports_failure`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_sparse_fem.py -k test_damped_newton_backtracks_and_reports_failure
```
