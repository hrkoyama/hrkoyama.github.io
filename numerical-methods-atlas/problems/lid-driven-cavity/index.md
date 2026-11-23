# Re100の蓋駆動キャビティ / Re100 lid-driven cavity

https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/

## 日本語

[保存した最細Re100計算の流線と速さ。赤点は格子上の主渦、白抜き点はGhia表Vの主渦位置です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-wall-flow/#cavity-ghia-re100) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#lid-driven-cavity)

### 方程式・問題の定義

無次元の単位正方形、ν=.01、蓋速度U=1、Re=100。上面の内部節点だけu=1、他壁と四隅の速度は0、全壁ψ=0。初期内部渦度は0。壁渦度はThom条件で各Heun段に再設定します。

#### [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja)

$$
\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\rho^{-1}\nabla p+\nu\nabla^2\boldsymbol u
$$

$$
\nabla\cdot\boldsymbol u=0
$$

一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。

#### Re=100蓋駆動キャビティ：Ghia中心線との比較

補助実行例 · 実行例の定義・検証式

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega,\quad -\Delta\psi=\omega,\quad (u,v)=(\psi_y,-\psi_x)
$$

$$
\mathrm{Re}=UL/\nu=100,\quad \psi|_{\partial\Omega}=0,\quad u(x,1)=1\ (0<x<1)
$$

$$
\omega_{\mathrm{top},i}=-2\psi_{J-1,i}/h^2-2U/h,\quad \omega_{\mathrm{stationary}}=-2\psi_{\mathrm{adj}}/h^2+O(h)
$$

$$
\omega^{(1)}=\omega^n+\Delta t L(\omega^n),\quad \omega^{n+1}=\tfrac12\omega^n+\tfrac12[\omega^{(1)}+\Delta t L(\omega^{(1)})]
$$

非周期・粘性非圧縮の実際の2D計算を17/33/65点格子で定常化し、Ghia原著の速度中心線と比較します。流線・渦中心・真の残差と発散を同時に保存します。

### 厳密解・参照解

21単体検査と群全体94判定を事前固定。原著の表I/II（印刷398–399頁）を直接確認して転記した17点ずつへ線形補間し、最細の各速度最大誤差≤.03、細分化で減少、定常残差≤1e−7を検査します。表Vの主渦位置・壁値・Poisson残差・離散発散も確認します。

#### [Ghia Re100：原著の有限格子速度中心線](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja#cavity-ghia-re100-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

u_ref(.5,y_j),v_ref(x_j,.5): original TablesI/II Re100; primary vortex(x,y)=(.6172,.7344): TableV.

単位正方形、Re100、蓋速度1、他壁静止。Ghia原著の表I/IIのRe100列から速度u(0.5,y)とv(x,0.5)各17点を直接確認して転記し、印刷された4桁座標を保持します。表Vの格子上の主渦位置(.6172,.7344)を別に比較します。丸めを含む有限格子数値表で、厳密な連続解でも今回のソルバー出力でもありません。

Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。

#### Re=100蓋駆動キャビティ：Ghia中心線との比較

22単体検査と群全体94判定を事前固定。原著の表I/II（印刷398–399頁）を直接確認して転記した17点ずつへ線形補間し、最細の各速度最大誤差≤.03、細分化で減少、定常残差≤1e−7を検査します。表Vの主渦位置・壁値・Poisson残差・離散発散も確認します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja)

### 計算法

ωt+uωx+vωy=νΔωを中央差分とHeun法で進め、各段で−Δhψ=ωを非周期Dirichlet DSTで解きます。u=ψy,v=−ψx。局所一次のThom壁渦度を使用し、原著のCSI-MGと高次壁公式は実装していません。

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Re=100蓋駆動キャビティ：Ghia中心線との比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja)

補助実行例

非周期・粘性非圧縮の実際の2D計算を17/33/65点格子で定常化し、Ghia原著の速度中心線と比較します。流線・渦中心・真の残差と発散を同時に保存します。

無次元の単位正方形、ν=.01、蓋速度U=1、Re=100。上面の内部節点だけu=1、他壁と四隅の速度は0、全壁ψ=0。初期内部渦度は0。壁渦度はThom条件で各Heun段に再設定します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23-r2/wall-flow/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/run.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/wall_flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/wall_flow.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/references/qualify_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/references/qualify_reference.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_result_envelope.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_result_envelope.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_serialization.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_wall_flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_wall_flow.py)

## English

[Saved finest Re100 streamlines and speed. Red dot: computed grid primary vortex; hollow dot: original Ghia TableV location.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-wall-flow/#cavity-ghia-re100) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#lid-driven-cavity-en)

### Equations and problem definitions

Dimensionless unit square, viscosity.01, lid speed1, Re100. Top interior nodes haveu1; other walls and all four corners have zero velocity. Psi0 on every wall; initial interior vorticity0. Reapply Thom wall vorticity at every Heun stage.

#### [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en)

$$
\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\rho^{-1}\nabla p+\nu\nabla^2\boldsymbol u
$$

$$
\nabla\cdot\boldsymbol u=0
$$

Representative constant-density/viscosity flow. In addition to periodic2D MAC projection/Taylor–Green, a separate release verifies a pressure-eliminated nonperiodic Re100 cavity.

#### Re100 lid-driven cavity: Ghia centerline comparison

Supplementary execution example · Example definition or validation formula

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega,\quad -\Delta\psi=\omega,\quad (u,v)=(\psi_y,-\psi_x)
$$

$$
\mathrm{Re}=UL/\nu=100,\quad \psi|_{\partial\Omega}=0,\quad u(x,1)=1\ (0<x<1)
$$

$$
\omega_{\mathrm{top},i}=-2\psi_{J-1,i}/h^2-2U/h,\quad \omega_{\mathrm{stationary}}=-2\psi_{\mathrm{adj}}/h^2+O(h)
$$

$$
\omega^{(1)}=\omega^n+\Delta t L(\omega^n),\quad \omega^{n+1}=\tfrac12\omega^n+\tfrac12[\omega^{(1)}+\Delta t L(\omega^{(1)})]
$$

March a real nonperiodic 2D viscous incompressible solver to steady state on 17/33/65 node grids and compare against original Ghia centerlines. Retain streamlines, grid vortex center, true PDE residual and discrete divergence.

### Exact and reference solutions

Freeze21 pytest checks and94group gates. Linearly interpolate to17points per velocity transcribed after direct visual reading of original TablesI/II, printed398–399. Require finest component maximum errors≤.03, refinement decrease and steady residual≤1e−7. Also check primary-vortex grid location from TableV, wall values, Poisson residual and discrete divergence.

#### [Ghia Re100: original finite-grid velocity centerlines](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en#cavity-ghia-re100-en-measurements)

Finite-grid numerical reference · Reference for the same problem

u_ref(.5,y_j),v_ref(x_j,.5): original TablesI/II Re100; primary vortex(x,y)=(.6172,.7344): TableV.

Unit square,Re100,unit top lid and stationary other walls. Transcribe17points each of u(.5,y) and v(x,.5) after direct inspection of original TablesI/II Re100 columns, preserving printed four-decimal coordinates. Separately compare the grid primary vortex(.6172,.7344) from TableV. These rounded finite-grid numerical tables are neither continuum exact values nor outputs from the present solver.

Educational Re100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed.

#### Re100 lid-driven cavity: Ghia centerline comparison

Freeze 22 pytest checks and 94 group gates. Linearly interpolate to 17 points per velocity transcribed after direct visual reading of original TablesI/II, printed 398–399. Require finest component maximum errors≤.03, refinement decrease and steady residual≤1e−7. Also check primary-vortex grid location from TableV, wall values, Poisson residual and discrete divergence.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en)

### Numerical methods

Advance vorticity transport with centered differences and Heun. Each stage solves−Delta_h psi=omega using a nonperiodic Dirichlet DST, then formsu=psi_y,v=−psi_x. Use local first-order Thom wall vorticity; this is an independent method, not Ghia CSI-MG or its higher-order wall formula.

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Re100 lid-driven cavity: Ghia centerline comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en)

Supplementary execution example

March a real nonperiodic 2D viscous incompressible solver to steady state on 17/33/65 node grids and compare against original Ghia centerlines. Retain streamlines, grid vortex center, true PDE residual and discrete divergence.

Dimensionless unit square, viscosity .01, lid speed1, Re=100. Top interior nodes have u=1; other walls and all four corners have zero velocity. Psi=0 on every wall; initial interior vorticity 0. Reapply Thom wall vorticity at every Heun stage.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Educational Re=100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23-r2/wall-flow/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/run.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/wall_flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/wall_flow.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/references/qualify_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/references/qualify_reference.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_result_envelope.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_result_envelope.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_serialization.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_wall_flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_wall_flow.py)
