# 球面浅水波の軸対称定常釣合いを時間積分 / Time evolution of axisymmetric spherical shallow-water balance

https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/

## 日本語

[球面浅水波の軸対称な無次元定常状態を実際に時間積分し、釣合い残差と格子依存を分ける。 a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sphere-zonal-balance.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-continuum-particle-controls/#sphere-zonal-balance) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#sphere-zonal-balance)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [球面浅水波の軸対称部分問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#spherical-shallow-water-ja)

$$
h_t+\frac{\partial_\phi(hv\cos\phi)}{a\cos\phi}=0,\quad u_t+\frac va u_\phi-(2\Omega\sin\phi+u\tan\phi/a)v=0
$$

$$
v_t+\frac va v_\phi+(2\Omega\sin\phi+u\tan\phi/a)u+\frac ga h_\phi=0
$$

$$
u=u_0\cos\phi,\quad v=0,\quad h=h_0-\frac{a\Omega u_0+u_0^2/2}{g}\sin^2\phi
$$

a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。

### 厳密解・参照解

固定入力の式・参照・図と実行コードを対応付けます。 a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。

#### [球面浅水波の軸対称定常釣合いを時間積分](https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=ja#sphere-zonal-balance-ja-measurements)

解析解 · 同じ問題の参照

h_t+\frac{\partial_\phi(hv\cos\phi)}{a\cos\phi}=0,\quad u_t+\frac va u_\phi-(2\Omega\sin\phi+u\tan\phi/a)v=0; v_t+\frac va v_\phi+(2\Omega\sin\phi+u\tan\phi/a)u+\frac ga h_\phi=0; u=u_0\cos\phi,\quad v=0,\quad h=h_0-\frac{a\Omega u_0+u_0^2/2}{g}\sin^2\phi

a=g=1、Ω=2、u0=0.5、h0=10の無次元軸対称部分問題です。中心差分のprimitive運動量、有限体積の質量、RK4で実際に時間発展させます。標準地球パラメータ、多次元の全球浅水コア、離散厳密釣合い、渦位保存の主張は含みません。

固定入力の式・参照・図と実行コードを対応付けます。 a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。

#### 球面浅水波の軸対称定常釣合いを時間積分

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=ja)

### 計算法

a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [球面浅水波の軸対称定常釣合いを時間積分](https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=ja)

補助実行例

球面浅水波の軸対称な無次元定常状態を実際に時間積分し、釣合い残差と格子依存を分ける。

球面浅水波の軸対称な無次元部分問題です。運動量の原始変数は子午線方向の中心差分、質量は緯度帯の面流束による有限体積形で離散化し、RK4で時間積分します。極の質量流束をゼロとし、平衡残差の差し引きや補正は行いません。固定入力・境界・参照の範囲はinputs.jsonを参照。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

限定した教育用モデルです。元論文の全条件・全アルゴリズムや一般的な性能の再現ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/run.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py)

## English

[NondimensionalWilliamson2-type axisymmetricsubproblem. Analyticstaticstatevsactualtimeintegration; not fullglobaldynamicalcore/PVclaim. Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sphere-zonal-balance.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-continuum-particle-controls/#sphere-zonal-balance) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#sphere-zonal-balance-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Axisymmetric spherical shallow-water subproblem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#spherical-shallow-water-en)

$$
h_t+\frac{\partial_\phi(hv\cos\phi)}{a\cos\phi}=0,\quad u_t+\frac va u_\phi-(2\Omega\sin\phi+u\tan\phi/a)v=0
$$

$$
v_t+\frac va v_\phi+(2\Omega\sin\phi+u\tan\phi/a)u+\frac ga h_\phi=0
$$

$$
u=u_0\cos\phi,\quad v=0,\quad h=h_0-\frac{a\Omega u_0+u_0^2/2}{g}\sin^2\phi
$$

Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.

### Exact and reference solutions

Bind the fixed-input formula, reference, figure and executable code. Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.

#### [Time evolution of axisymmetric spherical shallow-water balance](https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=en#sphere-zonal-balance-en-measurements)

Analytic reference · Reference for the same problem

h_t+\frac{\partial_\phi(hv\cos\phi)}{a\cos\phi}=0,\quad u_t+\frac va u_\phi-(2\Omega\sin\phi+u\tan\phi/a)v=0; v_t+\frac va v_\phi+(2\Omega\sin\phi+u\tan\phi/a)u+\frac ga h_\phi=0; u=u_0\cos\phi,\quad v=0,\quad h=h_0-\frac{a\Omega u_0+u_0^2/2}{g}\sin^2\phi

Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.

Bind the fixed-input formula, reference, figure and executable code. Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.

#### Time evolution of axisymmetric spherical shallow-water balance

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=en)

### Numerical methods

Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Time evolution of axisymmetric spherical shallow-water balance](https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=en)

Supplementary execution example

NondimensionalWilliamson2-type axisymmetricsubproblem. Analyticstaticstatevsactualtimeintegration; not fullglobaldynamicalcore/PVclaim.

Nondimensional axisymmetric spherical SWE subproblem. Hybrid centered meridional differences for primitive momentum and latitude-band finite-volume face fluxes for mass, advanced by RK4. Pole mass flux is zero; no equilibrium residual subtraction or correction. Fixed inputs, boundaries and reference scope are specified in inputs.json.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

NondimensionalWilliamson2-type axisymmetricsubproblem. Analyticstaticstatevsactualtimeintegration; not fullglobaldynamicalcore/PVclaim.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/run.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py)
