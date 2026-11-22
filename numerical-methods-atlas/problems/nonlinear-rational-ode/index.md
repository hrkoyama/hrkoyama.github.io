# 有理関数を厳密解に持つ非線形・非自律ODE / Nonlinear nonautonomous ODE with rational exact solution

https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/

## 日本語

[公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-ode.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#nonlinear-rational-ode)

### 方程式・問題の定義

非自律スカラーODE y′=-y²+sin(t)[y-1/(1+t)]。方程式一覧に専用項目はありません。

### 厳密解・参照解

y′=-y²+sin(t)[y-1/(1+t)]、y(0)=1の製造厳密解1/(1+t)と時間収束を確認します。

### 計算法

公開検査に後退Euler・BDF2・SDIRK2・IMEX Eulerがあり、保存プレビューはSDIRK2です。

- [後退Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [BDF2](https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [L安定なSDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [IMEX Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/imex-euler/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

#### [code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_implicit_orders_on_nonautonomous_nonlinear_exact_solution`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_new_models.py -k test_implicit_orders_on_nonautonomous_nonlinear_exact_solution
```

## English

[Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-ode.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/stiff-integration/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#nonlinear-rational-ode-en)

### Equations and problem definitions

Nonautonomous scalar ODE y′=-y²+sin(t)[y-1/(1+t)]; no dedicated equation-registry entry.

### Exact and reference solutions

Check temporal refinement against the manufactured exact solution 1/(1+t) for y′=-y²+sin(t)[y-1/(1+t)], y(0)=1.

### Numerical methods

Public checks include backward Euler, BDF2, SDIRK2 and IMEX Euler; the saved preview uses SDIRK2.

- [Backward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [BDF2](https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [L-stable SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [IMEX Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/imex-euler/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.

#### [code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_implicit_orders_on_nonautonomous_nonlinear_exact_solution`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_new_models.py -k test_implicit_orders_on_nonautonomous_nonlinear_exact_solution
```
