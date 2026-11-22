# 不連続関数の多項式補間・射影 / Polynomial interpolation and projection of a jump function

https://hrkoyama.github.io/numerical-methods-atlas/problems/jump-function-projection/

## 日本語

[保存済み8次多項式の射影・補間と元の関数。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/jump-function-projection.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/basis-functions/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#jump-function-projection)

### 方程式・問題の定義

不連続な指定関数の射影・補間問題であり、移流方程式を進める問題ではありません。

### 厳密解・参照解

指定された段差関数の既知値と比較し、射影・補間の振動と収束を確認します。滑らかな関数の誤差評価とは区別します。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [Legendreモード基底・正規直交化](https://hrkoyama.github.io/numerical-methods-atlas/methods/legendre-basis/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Lagrange節点基底・GLL選点法](https://hrkoyama.github.io/numerical-methods-atlas/methods/nodal-basis/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

## English

[Stored degree-8 projection/interpolation and the original function.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/jump-function-projection.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/basis-functions/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#jump-function-projection-en)

### Equations and problem definitions

Projection/interpolation of a prescribed discontinuous function, rather than an advection evolution problem.

### Exact and reference solutions

Compare with known values of the specified jump function to inspect projection/interpolation oscillations and convergence, separately from smooth-function error behavior.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [Legendre modal basis / orthonormal scaling](https://hrkoyama.github.io/numerical-methods-atlas/methods/legendre-basis/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Lagrange nodal basis / GLL collocation](https://hrkoyama.github.io/numerical-methods-atlas/methods/nodal-basis/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.
