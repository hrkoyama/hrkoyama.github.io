# 円偏波Alfvén波 / Circularly polarized Alfvén wave

https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/

## 日本語

[保存済み円偏波Alfvén波の誤差・収束比較。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mhd/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#circular-alfven)

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

円偏光Alfvén波の解析解を、一定の全エネルギーを含む保存変数セル平均で評価します。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [HLLDのMHDリーマン解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [HLLE／Einfeldt波速](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

## English

[Stored circularly polarized Alfvén-wave comparison.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/mhd/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#circular-alfven-en)

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

Evaluate the analytic circularly polarized Alfvén wave using conserved cell averages, including its constant total energy.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [HLLD MHD Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [HLLE / Einfeldt wave speeds](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlle/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.
