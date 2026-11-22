# Burgers衝撃波 / Burgers shock

https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/

## 日本語

[保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-shock.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/equation-gallery/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#burgers-shock)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [非粘性Burgers方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#burgers-ja)

$$
\partial_tu+\partial_x(u^2/2)=0
$$

非線形のスカラー保存則。衝撃波と膨張波を比較する。

### 厳密解・参照解

左右状態1と0、x=0.5の段差から生じるエントロピー衝撃波の解析解と比較します。有限体積誤差では点値とセル平均を区別します。

#### [Burgers／衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=burgers-shock)

解析解 · 関連モデルの参照

u_t + (u²/2)_x = 0

全直線上のスカラーRiemann問題のエントロピー解。端点の外側は一定値で継続します。

左右状態(1,0)、段差位置0.5、端点継続が一致します。点値とセル平均の評価は区別します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [Godunov型有限体積法](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

## English

[Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-shock.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/equation-gallery/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#burgers-shock-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Inviscid Burgers equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#burgers-en)

$$
\partial_tu+\partial_x(u^2/2)=0
$$

A nonlinear scalar conservation law: compare shocks and rarefactions.

### Exact and reference solutions

Compare with the analytic entropy shock for states 1 and 0 separated at x=0.5. Distinguish point values from conserved cell averages in finite-volume errors.

#### [Burgers / shock](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=burgers-shock)

Analytic reference · Related-model reference

u_t + (u²/2)_x = 0

Entropy solution of a scalar whole-line Riemann problem; constant endpoint continuation.

States (1,0), jump position 0.5 and endpoint continuation match; distinguish point and cell-average evaluation. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [Godunov-type finite volumes](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.
