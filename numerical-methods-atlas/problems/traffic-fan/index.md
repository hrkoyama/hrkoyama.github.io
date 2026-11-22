# 交通流の希薄化波 / Traffic clearing fan

https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/

## 日本語

[保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-fan.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/equation-gallery/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#traffic-fan)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [LWR交通流モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#traffic-ja)

$$
\partial_t\rho+\partial_x[\rho(1-\rho)]=0
$$

無次元化した代表流束。渋滞の上流伝播と希薄化を調べる。

### 厳密解・参照解

密度0.9と0.1のRiemann問題に対する解析的なエントロピー希薄波が基準です。

#### [交通流／渋滞解消の膨張波](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=traffic-fan)

解析解 · 関連モデルの参照

rho_t + [rho(1−rho)]_x = 0

全直線上のスカラーRiemann問題のエントロピー解。端点の外側は一定値で継続します。

流束ρ(1-ρ)、左右密度(0.9,0.1)、段差位置0.5が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [Godunov型有限体積法](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

## English

[Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-fan.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/equation-gallery/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#traffic-fan-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [LWR traffic model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#traffic-en)

$$
\partial_t\rho+\partial_x[\rho(1-\rho)]=0
$$

A representative nondimensional flux: upstream jams and clearing fans.

### Exact and reference solutions

The standard is the analytic entropy rarefaction for Riemann densities 0.9 and 0.1.

#### [Traffic / clearing fan](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=traffic-fan)

Analytic reference · Related-model reference

rho_t + [rho(1−rho)]_x = 0

Entropy solution of a scalar whole-line Riemann problem; constant endpoint continuation.

Flux ρ(1-ρ), left/right densities (0.9,0.1) and jump position 0.5 match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [Godunov-type finite volumes](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.
