# ALEピストン・球面輸送・SPH/GSPHの限定検証

所与ALEの有限圧力ピストン、限定球面輸送と軸対称釣合い、実GSPHとSPH対照を固定入力で検証します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## Saltzman型の歪み格子ピストン：2次元EulerとALE

2023年版の歪み格子と有限初期圧力を明示した、所与の格子移動による2次元Eulerピストン計算。

**使用手法**

- [ALE一様状態・幾何保存モデル](https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=ja) (`ale`)
- [Rusanov／局所Lax–Friedrichs流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja) (`rusanov`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=ja#saltzman-ale-piston-ja-algorithm)

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

Tan–Lv–Zhu (2023) Example 8 の e0=10^-4 を明示した有限圧力版。所与のアフィンALE格子を使う2D Euler/Rusanov例で、物質追従格子、WENO、remapや1985原報の全面再現ではありません。


**問題の図**

![Saltzman型の歪み格子ピストン：2次元EulerとALE：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/saltzman-ale-piston.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Saltzman型の歪み格子ピストン：2次元EulerとALE](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=ja) (`saltzman-ale-piston`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=ja#saltzman-ale-piston-ja-validation)

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

- [Saltzman型の歪み格子ピストン：2次元EulerとALE](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-saltzman-ale-piston-ja) (`saltzman-ale-piston`; 同じ問題の参照 · 解析参照)

固定入力の式・参照・図と実行コードを対応付けます。 Tan–Lv–Zhu (2023) Example 8 の e0=10^-4 を明示した有限圧力版。所与のアフィンALE格子を使う2D Euler/Rusanov例で、物質追従格子、WENO、remapや1985原報の全面再現ではありません。
### 前提・単位・境界

2023年版の歪み格子と有限初期圧力を明示した、所与の格子移動による2次元Eulerピストン計算。 固定入力の条件・境界・参照の範囲はinputs.jsonを参照。

**編集上の補足**

Tan–Lv–Zhu (2023) Example 8 の e0=10^-4 を明示した有限圧力版。所与のアフィンALE格子を使う2D Euler/Rusanov例で、物質追従格子、WENO、remapや1985原報の全面再現ではありません。

### 採用した計算法

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

$$
U=(\rho,\rho u,\rho v,E)^{\mathsf T},\quad p=(\gamma-1)\left[E-\frac{\rho}{2}(u^2+v^2)\right]
$$

$$
\frac{d}{dt}(|K|\overline U_K)=-\sum_{f\subset\partial K}|f|\widehat F_{\mathrm{ALE}}(U_f^-,U_f^+;\mathbf n_f,w_{n,f})
$$

$$
F_{\mathrm{ALE}}(U;\mathbf n,w_n)=(u_n-w_n)U+p(0,n_x,n_y,u_n)^{\mathsf T},\quad u_n=\mathbf u\cdot\mathbf n
$$

$$
\widehat F_{\mathrm{ALE}}=\frac{F_{\mathrm{ALE}}(U_L)+F_{\mathrm{ALE}}(U_R)}{2}-\frac{a_{\max}}{2}(U_R-U_L),\quad a_{\max}=\max_{s=L,R}(|u_{n,s}-w_n|+c_s)
$$

$$
x(t)=t+(1-t)x_0,\quad y(t)=y_0,\quad\mathbf w=(1-x_0,0)
$$

数式の編集補足：凍結配布版のコードと登録済み方程式に基づく記述です。配布版・計算・受入条件・保存結果は変更しません。 所与のアフィン格子運動と2次元ALE/Rusanov流束の式で、物質追従格子やremapの式ではありません。

### 比較・検証

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

### 確認の限界

限定した教育用モデルです。元論文の全条件・全アルゴリズムや一般的な性能の再現ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "finest": {
      "grid": [
        80,
        8
      ],
      "density_error": 0.03966960674770006,
      "shock_error": 0.009071663139626374,
      "plateau_density_error": 0.060142667838002595,
      "plateau_pressure_error": 0.07005129077711092,
      "max_transverse": 0.08502093161153988,
      "mass_defect": 4.1551145858098734e-16,
      "momentum_defect": 1.3877787807814449e-15,
      "energy_defect": 3.5023519269671693e-15,
      "GCL": 3.7705883405261993e-17,
      "steps": 1333,
      "minimum_density": 0.9999999999997568,
      "minimum_pressure": 6.66666666666505e-05
    }
  },
  "checks": {
    "positive": true,
    "conservation": true,
    "GCL": true,
    "density": true,
    "refinement": true,
    "shock": true,
    "plateau": true,
    "transverse": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. https://arxiv.org/pdf/astro-ph/0206401; review_level=selected-original-author-paper-sections-and-equations
- New Third-Order Finite Volume Unequal-Sized WENO Lagrangian Schemes for Solving Euler Equations. https://www.mdpi.com/2227-7390/11/23/4842; review_level=selected-publisher-fulltext-example-8
- Second Order Corner Coupled Upwind Transport Methods for Lagrangian Hydrodynamics. https://www.osti.gov/servlets/purl/15005665; review_level=secondary-bibliographic-identity-original-report-unread
- A standard test set for numerical approximations to the shallow water equations in spherical geometry. https://digital.library.unt.edu/ark:/67531/metadc1069483/; review_level=author-report-bibliography-and-abstract-original-formulas-unread
- Cascade interpolation for semi-Lagrangian advection over the sphere. https://www.image.ucar.edu/staff/rnair/qj99_sph.pdf; review_level=selected-author-hosted-formulas-and-publisher-bibliography

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Williamson型の球面固体回転輸送：傾いた軸と極通過

所与の固体回転速度で球面上のcosine bellを輸送し、傾いた軸・極通過・1周後の誤差を調べる限定例。

**使用手法**

- [セミラグランジュ法：所与球面回転の限定例](https://hrkoyama.github.io/numerical-methods-atlas/methods/semi-lagrangian/?lang=ja) (`semi-lagrangian`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=ja#williamson-sphere-transport-ja-algorithm)

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

- [球面上の所与速度スカラー移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#sphere-scalar-advection-ja) (`sphere-scalar-advection`)

単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。


**問題の図**

![Williamson型の球面固体回転輸送：傾いた軸と極通過：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Williamson型の球面固体回転輸送：傾いた軸と極通過](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=ja) (`williamson-sphere-transport`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=ja#williamson-sphere-transport-ja-validation)

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

- [Williamson型の球面固体回転輸送：傾いた軸と極通過](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-williamson-sphere-transport-ja) (`williamson-sphere-transport`; 同じ問題の参照 · 解析参照)

固定入力の式・参照・図と実行コードを対応付けます。 単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。
### 前提・単位・境界

所与の固体回転速度で球面上のcosine bellを輸送し、傾いた軸・極通過・1周後の誤差を調べる限定例。 固定入力の条件・境界・参照の範囲はinputs.jsonを参照。

**編集上の補足**

単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。

### 採用した計算法

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

$$
q_t+\mathbf v\cdot\nabla_{\mathbb S^2}q=0,\quad q(\mathbf r,t)=q_0(R_{\mathbf n}(-2\pi t/T)\mathbf r)
$$

$$
\mathbf n=(-\sin\alpha,0,\cos\alpha),\quad q_0(r)=\tfrac12[1+\cos(\pi r/R)]\ (r<R),\quad q_0=0\ (r\ge R)
$$

数式の編集補足：凍結配布版のコードと登録済み方程式に基づく記述です。配布版・計算・受入条件・保存結果は変更しません。

### 比較・検証

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

### 確認の限界

限定した教育用モデルです。元論文の全条件・全アルゴリズムや一般的な性能の再現ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "fine_L1": [
      0.17228372801445835,
      0.1983012829411487
    ]
  },
  "checks": {
    "error": true,
    "refinement": true,
    "mass": true,
    "bounds": true,
    "sphere_area": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. https://arxiv.org/pdf/astro-ph/0206401; review_level=selected-original-author-paper-sections-and-equations
- New Third-Order Finite Volume Unequal-Sized WENO Lagrangian Schemes for Solving Euler Equations. https://www.mdpi.com/2227-7390/11/23/4842; review_level=selected-publisher-fulltext-example-8
- Second Order Corner Coupled Upwind Transport Methods for Lagrangian Hydrodynamics. https://www.osti.gov/servlets/purl/15005665; review_level=secondary-bibliographic-identity-original-report-unread
- A standard test set for numerical approximations to the shallow water equations in spherical geometry. https://digital.library.unt.edu/ark:/67531/metadc1069483/; review_level=author-report-bibliography-and-abstract-original-formulas-unread
- Cascade interpolation for semi-Lagrangian advection over the sphere. https://www.image.ucar.edu/staff/rnair/qj99_sph.pdf; review_level=selected-author-hosted-formulas-and-publisher-bibliography

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 球面浅水波の軸対称定常釣合いを時間積分

球面浅水波の軸対称な無次元定常状態を実際に時間積分し、釣合い残差と格子依存を分ける。

**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=ja#sphere-zonal-balance-ja-algorithm)

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

- [球面浅水波の軸対称部分問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#spherical-shallow-water-ja) (`spherical-shallow-water`)

a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。


**問題の図**

![球面浅水波の軸対称定常釣合いを時間積分：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sphere-zonal-balance.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[球面浅水波の軸対称定常釣合いを時間積分](https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/?lang=ja) (`sphere-zonal-balance`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=ja#sphere-zonal-balance-ja-validation)

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

- [球面浅水波の軸対称定常釣合いを時間積分](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sphere-zonal-balance-ja) (`sphere-zonal-balance`; 同じ問題の参照 · 解析参照)

固定入力の式・参照・図と実行コードを対応付けます。 a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。
### 前提・単位・境界

球面浅水波の軸対称な無次元部分問題です。運動量の原始変数は子午線方向の中心差分、質量は緯度帯の面流束による有限体積形で離散化し、RK4で時間積分します。極の質量流束をゼロとし、平衡残差の差し引きや補正は行いません。固定入力・境界・参照の範囲はinputs.jsonを参照。

**編集上の補足**

a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。

### 採用した計算法

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

$$
h_t+\frac{\partial_\phi(hv\cos\phi)}{a\cos\phi}=0,\quad u_t+\frac va u_\phi-(2\Omega\sin\phi+u\tan\phi/a)v=0
$$

$$
v_t+\frac va v_\phi+(2\Omega\sin\phi+u\tan\phi/a)u+\frac ga h_\phi=0
$$

$$
u=u_0\cos\phi,\quad v=0,\quad h=h_0-\frac{a\Omega u_0+u_0^2/2}{g}\sin^2\phi
$$

数式の編集補足：凍結配布版のコードと登録済み方程式に基づく記述です。配布版・計算・受入条件・保存結果は変更しません。

### 比較・検証

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

### 確認の限界

限定した教育用モデルです。元論文の全条件・全アルゴリズムや一般的な性能の再現ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "finest": {
      "grid": 64,
      "h_error": 0.00010108962138506427,
      "initial_balance_residual": 0.0018041320580228781,
      "analytic_force_residual": 0.0,
      "mass_defect": 0.0,
      "minimum_h": 8.87466665967074,
      "steps": 129
    }
  },
  "checks": {
    "analytic_balance": true,
    "balance_order": true,
    "height": true,
    "refinement": true,
    "mass": true,
    "positive": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. https://arxiv.org/pdf/astro-ph/0206401; review_level=selected-original-author-paper-sections-and-equations
- New Third-Order Finite Volume Unequal-Sized WENO Lagrangian Schemes for Solving Euler Equations. https://www.mdpi.com/2227-7390/11/23/4842; review_level=selected-publisher-fulltext-example-8
- Second Order Corner Coupled Upwind Transport Methods for Lagrangian Hydrodynamics. https://www.osti.gov/servlets/purl/15005665; review_level=secondary-bibliographic-identity-original-report-unread
- A standard test set for numerical approximations to the shallow water equations in spherical geometry. https://digital.library.unt.edu/ark:/67531/metadc1069483/; review_level=author-report-bibliography-and-abstract-original-formulas-unread
- Cascade interpolation for semi-Lagrangian advection over the sphere. https://www.image.ucar.edu/staff/rnair/qj99_sph.pdf; review_level=selected-author-hosted-formulas-and-publisher-bibliography

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Gaussian畳込みGSPHによるSod型粒子衝撃管

Gaussian畳込みの線形比体積近似と対称な可変平滑化長を使う、限定GSPH粒子流体計算。

**使用手法**

- [Godunov SPH／GSPH](https://hrkoyama.github.io/numerical-methods-atlas/methods/gsph/?lang=ja) (`gsph`)
- [SPHカーネル再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/sph/?lang=ja) (`sph`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=ja#gsph-sod-ja-algorithm)

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

Gaussianの線形比体積畳み込み、対称な可変h、独立な対Riemann解と反対称な全エネルギー交換を持つGSPHです。通常SPHへp*を代入する代用ではありません。一次再構成に限定し、論文のcubic/MUSCLや一般精度を主張しません。


**問題の図**

![Gaussian畳込みGSPHによるSod型粒子衝撃管：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/gsph-sod.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Sod衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja) (`sod`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=ja#gsph-sod-ja-validation)

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

- [Euler／Sod問題](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-sod-ja) (`euler-sod`; 関連モデルの参照 · 半解析参照)

γ=1.4、左右(ρ,u,p)=(1,0,1)/(0.125,0,0.1)、x0=0.5、[0,1]、t=0.2が一致します。点値・保存セル平均・誤差ノルムは別に確認します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

- [Gaussian畳込みGSPHによるSod型粒子衝撃管](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gsph-sod-ja) (`gsph-sod`; 同じ問題の参照 · 半解析参照)

固定入力の式・参照・図と実行コードを対応付けます。 Gaussianの線形比体積畳み込み、対称な可変h、独立な対Riemann解と反対称な全エネルギー交換を持つGSPHです。通常SPHへp*を代入する代用ではありません。一次再構成に限定し、論文のcubic/MUSCLや一般精度を主張しません。
### 前提・単位・境界

Gaussian畳込みの線形比体積近似と対称な可変平滑化長を使う、限定GSPH粒子流体計算。 固定入力の条件・境界・参照の範囲はinputs.jsonを参照。

**編集上の補足**

Gaussianの線形比体積畳み込み、対称な可変h、独立な対Riemann解と反対称な全エネルギー交換を持つGSPHです。通常SPHへp*を代入する代用ではありません。一次再構成に限定し、論文のcubic/MUSCLや一般精度を主張しません。

### 採用した計算法

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

数式の編集補足：凍結配布版のコードと登録済み方程式に基づく記述です。配布版・計算・受入条件・保存結果は変更しません。

### 比較・検証

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

### 確認の限界

限定した教育用モデルです。元論文の全条件・全アルゴリズムや一般的な性能の再現ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "finest_GSPH": {
      "method": "gsph",
      "right_particles": 32,
      "rho_error": 0.03789937718353325,
      "pressure_error": 0.040752681798075875,
      "shock_error": 0.011271366170524794,
      "defect": [
        0.0,
        2.220446049250313e-16,
        0.0
      ],
      "h_change": 1.5560167029698944,
      "steps": 518,
      "h_residual": 9.994160761956033e-11,
      "Riemann_residual": 1.5300261058115439e-15
    },
    "pair_swap_force_residual": 0.0,
    "pair_swap_energy_residual": 1.1102230246251565e-16,
    "oracle_pressure_root": 0.30313017805063625,
    "oracle_root_diagnostics": {
      "iterations": 45,
      "log_bracket_width": 1.3078427230084344e-13,
      "wave_residual": -5.773159728050814e-14
    }
  },
  "checks": {
    "pair_swap_force": true,
    "pair_swap_energy": true,
    "conservation": true,
    "rho": true,
    "pressure": true,
    "refinement": true,
    "shock": true,
    "h_solve": true,
    "Riemann": true,
    "adaptive_h": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. https://arxiv.org/pdf/astro-ph/0206401; review_level=selected-original-author-paper-sections-and-equations
- New Third-Order Finite Volume Unequal-Sized WENO Lagrangian Schemes for Solving Euler Equations. https://www.mdpi.com/2227-7390/11/23/4842; review_level=selected-publisher-fulltext-example-8
- Second Order Corner Coupled Upwind Transport Methods for Lagrangian Hydrodynamics. https://www.osti.gov/servlets/purl/15005665; review_level=secondary-bibliographic-identity-original-report-unread
- A standard test set for numerical approximations to the shallow water equations in spherical geometry. https://digital.library.unt.edu/ark:/67531/metadc1069483/; review_level=author-report-bibliography-and-abstract-original-formulas-unread
- Cascade interpolation for semi-Lagrangian advection over the sphere. https://www.image.ucar.edu/staff/rnair/qj99_sph.pdf; review_level=selected-author-hosted-formulas-and-publisher-bibliography

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 一様圧力と線形音波：SPH/GSPHの粒子配置依存

規則・摂動粒子の一様圧力と小振幅音波について、初期カーネル誤差と時間発展誤差を区別する。

**使用手法**

- [Godunov SPH／GSPH](https://hrkoyama.github.io/numerical-methods-atlas/methods/gsph/?lang=ja) (`gsph`)
- [SPHカーネル再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/sph/?lang=ja) (`sph`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=ja#sph-pressure-acoustics-ja-algorithm)

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。


**問題の図**

![一様圧力と線形音波：SPH/GSPHの粒子配置依存：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[一様圧力と線形音波：SPH/GSPHの粒子配置依存](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=ja) (`sph-pressure-acoustics`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=ja#sph-pressure-acoustics-ja-validation)

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

- [一様圧力と線形音波：SPH/GSPHの粒子配置依存](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sph-pressure-acoustics-ja) (`sph-pressure-acoustics`; 同じ問題の参照 · 解析参照)

固定入力の式・参照・図と実行コードを対応付けます。 GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。
### 前提・単位・境界

規則・摂動粒子の一様圧力と小振幅音波について、初期カーネル誤差と時間発展誤差を区別する。 固定入力の条件・境界・参照の範囲はinputs.jsonを参照。

**編集上の補足**

GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。

### 採用した計算法

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

数式の編集補足：凍結配布版のコードと登録済み方程式に基づく記述です。配布版・計算・受入条件・保存結果は変更しません。

### 比較・検証

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

### 確認の限界

限定した教育用モデルです。元論文の全条件・全アルゴリズムや一般的な性能の再現ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "profiles": 16,
    "linearization_remainder_scale": 1e-06
  },
  "checks": {
    "regular_static_force": true,
    "jittered_static_velocity": true,
    "acoustic_phase": true,
    "acoustic_amplitude": true,
    "conservation": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. https://arxiv.org/pdf/astro-ph/0206401; review_level=selected-original-author-paper-sections-and-equations
- New Third-Order Finite Volume Unequal-Sized WENO Lagrangian Schemes for Solving Euler Equations. https://www.mdpi.com/2227-7390/11/23/4842; review_level=selected-publisher-fulltext-example-8
- Second Order Corner Coupled Upwind Transport Methods for Lagrangian Hydrodynamics. https://www.osti.gov/servlets/purl/15005665; review_level=secondary-bibliographic-identity-original-report-unread
- A standard test set for numerical approximations to the shallow water equations in spherical geometry. https://digital.library.unt.edu/ark:/67531/metadc1069483/; review_level=author-report-bibliography-and-abstract-original-formulas-unread
- Cascade interpolation for semi-Lagrangian advection over the sphere. https://www.image.ucar.edu/staff/rnair/qj99_sph.pdf; review_level=selected-author-hosted-formulas-and-publisher-bibliography

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
