# 有理減衰ODE（y′ = −y²） / Rational-decay ODE (y′ = −y²)

https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/

## 日本語

[保存済み有理減衰ODEの時間刻み収束（代表3手法）。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-decay.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/runge-kutta/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#nonlinear-rational-decay)

### 方程式・問題の定義

非線形スカラーODE y′=-y²、y(0)=1。既存の方程式一覧には専用項目がありません。

### 厳密解・参照解

y′=-y²、y(0)=1の厳密解1/(1+t)を使い、複数の陽的Runge–Kutta法の非線形誤差と次数を確認します。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

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

## English

[Stored time-refinement errors for rational decay, showing three methods.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-decay.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/runge-kutta/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#nonlinear-rational-decay-en)

### Equations and problem definitions

Nonlinear scalar ODE y′=-y², y(0)=1; no dedicated equation-registry entry.

### Exact and reference solutions

Use the exact solution 1/(1+t) for y′=-y², y(0)=1, to check nonlinear errors and orders of several explicit Runge–Kutta methods.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

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
