# 円柱前面の弓形衝撃波 / Cylinder-forebody bow shock

https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-forebody/

## 日本語

[保存済み円柱前面の密度比較。有限時刻の結果で、定常収束の認定ではありません。](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-expansion/forebody-48-0-density.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/shock-expansion/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#cylinder-forebody)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja)

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。

### 厳密解・参照解

曲面適合格子上の保存済み数値場、壁面圧力、2格子・擾乱ありなしの履歴が基準資料です。定常収束やカーバンクル消失の認定ではありません。

### 計算法

保存された曲面前方衝撃波の流束比較です。Rotated項目は方向別HLLE/Roeの教育用実験で、最適化Rotated-RHLLの完成検証ではありません。

- [Roe法](https://hrkoyama.github.io/numerical-methods-atlas/methods/roe/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [HLLE／Einfeldt波速](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [AUSM系列の流束分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/ausm/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [回転ハイブリッド・リーマンソルバー](https://hrkoyama.github.io/numerical-methods-atlas/methods/rotated-hybrid/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

## English

[Stored finite-time forebody density comparison; not steady-state certification.](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-expansion/forebody-48-0-density.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/shock-expansion/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#cylinder-forebody-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en)

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.

### Exact and reference solutions

Reference material consists of stored body-fitted fields, wall pressure and histories for two grids with and without perturbations. It certifies neither a steady state nor elimination of carbuncles.

### Numerical methods

Flux comparisons stored for the body-fitted bow shock. The rotated entry is the educational directional HLLE/Roe experiment, not completed validation of optimized Rotated-RHLL.

- [Roe](https://hrkoyama.github.io/numerical-methods-atlas/methods/roe/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [HLLE / Einfeldt wave speeds](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [AUSM-family flux splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/ausm/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Rotated-hybrid Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/methods/rotated-hybrid/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.
