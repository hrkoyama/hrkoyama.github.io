# 磁場ループの移流 / Magnetic field-loop advection

https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/

## 日本語

[保存済み磁場ループ移流の計算場。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mhd/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#magnetic-loop)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [理想MHD](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#mhd-ja)

$$
\rho_t+\nabla\cdot(\rho\boldsymbol v)=0
$$

$$
(\rho\boldsymbol v)_t+\nabla\cdot[\rho\boldsymbol v\otimes\boldsymbol v+(p+B^2/2)I-\boldsymbol B\otimes\boldsymbol B]=0
$$

$$
E_t+\nabla\cdot[(E+p+B^2/2)\boldsymbol v-(\boldsymbol v\cdot\boldsymbol B)\boldsymbol B]=0
$$

$$
\boldsymbol B_t=\nabla\times(\boldsymbol v\times\boldsymbol B),\quad\nabla\cdot\boldsymbol B=0
$$

透磁率を1とする理想MHDの代表形。Eは熱・運動・磁場を含む全エネルギー密度。解説でCT・GLMと発散の測り方、HLLDテストへ進めます。

### 厳密解・参照解

弱磁場ループが1周期で戻る初期場との誤差、磁気エネルギー、配置固有の磁場発散を確認します。任意強度のMHDループの厳密解を主張しません。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [GLM発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [HLLDのMHDリーマン解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [HLLE／Einfeldt波速](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

## English

[Stored computed fields for magnetic-loop advection.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/mhd/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#magnetic-loop-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Ideal magnetohydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en)

$$
\rho_t+\nabla\cdot(\rho\boldsymbol v)=0
$$

$$
(\rho\boldsymbol v)_t+\nabla\cdot[\rho\boldsymbol v\otimes\boldsymbol v+(p+B^2/2)I-\boldsymbol B\otimes\boldsymbol B]=0
$$

$$
E_t+\nabla\cdot[(E+p+B^2/2)\boldsymbol v-(\boldsymbol v\cdot\boldsymbol B)\boldsymbol B]=0
$$

$$
\boldsymbol B_t=\nabla\times(\boldsymbol v\times\boldsymbol B),\quad\nabla\cdot\boldsymbol B=0
$$

Representative ideal MHD with magnetic permeability set to one. E is total thermal, kinetic and magnetic energy density. Follow CT/GLM, divergence conventions and HLLD tests.

### Exact and reference solutions

Check return error against the initial weak-field loop, magnetic energy and layout-specific divergence after one transit. No exact solution is claimed for arbitrary finite-strength MHD loops.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [GLM divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [HLLD MHD Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [HLLE / Einfeldt wave speeds](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.
