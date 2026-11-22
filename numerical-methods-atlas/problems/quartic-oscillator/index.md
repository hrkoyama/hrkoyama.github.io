# 4次ポテンシャルの非線形振動子 / Nonlinear quartic-potential oscillator

https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/

## 日本語

[保存済みのt≤10の正準位相軌道。手法違いは同一問題の比較。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/quartic-oscillator.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#quartic-oscillator)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja)

$$
\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}
$$

$$
H=\frac{p^2}{2}+V(q)
$$

正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。

### 厳密解・参照解

非線形ポテンシャルの保存エネルギーと長時間の数値軌道・写像の性質を比較します。保存図を閉形式の厳密軌道と呼びません。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [シンプレクティックEuler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/symplectic-euler/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [吉田の4次合成法](https://hrkoyama.github.io/numerical-methods-atlas/methods/yoshida4/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [陰的中点則](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

## English

[Stored canonical phase orbits for t≤10; methods remain variants of one problem.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/quartic-oscillator.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/symplectic/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#quartic-oscillator-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en)

$$
\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}
$$

$$
H=\frac{p^2}{2}+V(q)
$$

Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity.

### Exact and reference solutions

Compare conserved energy and long-time numerical trajectories/map properties in the nonlinear potential. The stored figure is not labeled a closed-form exact trajectory.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [Symplectic Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/symplectic-euler/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Yoshida fourth-order composition](https://hrkoyama.github.io/numerical-methods-atlas/methods/yoshida4/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Implicit midpoint](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.
