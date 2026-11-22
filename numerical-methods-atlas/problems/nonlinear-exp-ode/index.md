# 指数関数を厳密解に持つ非線形・非自律ODE / Nonlinear nonautonomous ODE with exponential exact solution

https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/

## 日本語

[公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-exp-ode.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/runge-kutta/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#nonlinear-exp-ode)

### 方程式・問題の定義

非自律スカラーODE y′=-y²+exp(2t)+exp(t)。既存46項目に対応する専用モデル式はありません。

### 厳密解・参照解

非自律非線形方程式y′=-y²+exp(2t)+exp(t)、y(0)=1の製造厳密解y=exp(t)と時間収束を確認します。

### 計算法

公開の全陽的RK tableauに対する非自律・非線形製造解の検査です。保存プレビューはRK4を使います。

- [前進Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [陽的中点RK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/explicit-midpoint/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Ralston RK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/ralston/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Kutta RK3](https://hrkoyama.github.io/numerical-methods-atlas/methods/kutta3/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [SSPRK(4,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk43/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [SSPRK(5,4)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk54/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

#### [code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_rk_order_conditions_and_manufactured_nonlinear_time_dependence`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_runge_kutta.py -k test_rk_order_conditions_and_manufactured_nonlinear_time_dependence
```

## English

[Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-exp-ode.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/runge-kutta/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#nonlinear-exp-ode-en)

### Equations and problem definitions

Nonautonomous scalar ODE y′=-y²+exp(2t)+exp(t); no dedicated model in the existing 46-entry equation registry.

### Exact and reference solutions

Check temporal refinement against the manufactured exact solution y=exp(t) for y′=-y²+exp(2t)+exp(t), y(0)=1.

### Numerical methods

Public nonautonomous/nonlinear manufactured-solution checks exercise every explicit RK tableau; the saved preview uses RK4.

- [Forward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Explicit midpoint RK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/explicit-midpoint/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Ralston RK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/ralston/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Kutta RK3](https://hrkoyama.github.io/numerical-methods-atlas/methods/kutta3/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [SSPRK(4,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk43/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [SSPRK(5,4)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk54/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.

#### [code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_rk_order_conditions_and_manufactured_nonlinear_time_dependence`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_runge_kutta.py -k test_rk_order_conditions_and_manufactured_nonlinear_time_dependence
```
