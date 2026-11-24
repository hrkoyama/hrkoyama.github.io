# 2D反向beamとM1閉包の情報損失 / Opposing beams and information loss in the M1 closure

https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/

## 日本語

[保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-radiation-geometry/#opposing-beams2d) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#opposing-beams2d)

### 方程式・問題の定義

2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。

#### [静止媒質の灰色放射輸送・散乱・線形交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja)

$$
\epsilon\partial_t I+\boldsymbol\Omega\cdot\nabla I+(\kappa_a+\kappa_s)I=\kappa_sJ+\kappa_aV+Q
$$

$$
J=\langle I\rangle_\Omega,\quad\partial_t V=\kappa_a(J-V)\quad(\mathrm{linear\ exchange})
$$

正規化した角度平均を使います。物質交換は1997輸送例と周期Fourier比較で進めます。1997の光学座標では係数1、物理座標の比較ではκを放射・物質の両交換項に掛けます。

#### [静止媒質・平坦時空の灰色M1モーメント](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-m1-ja)

$$
E_t+\nabla\cdot\boldsymbol F=-\kappa E+S_E,\quad\boldsymbol F_t+\nabla\cdot\mathsf P=-\kappa\boldsymbol F+\boldsymbol S_F
$$

$$
\mathsf P=E[(1-\chi)\mathsf I_3/2+(3\chi-1)\boldsymbol n\boldsymbol n^T/2]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\boldsymbol F|/E
$$

c=1、2D空間で3D圧力のPzzを保持。等方・真空分岐、閉じたPDEの製造解、角度法とのビーム差を区別し、相対論的放射流体とは扱いません。

#### 2D反向beamとM1閉包の情報損失

補助実行例 · 実行例の定義・検証式

$$
\partial_tE+\nabla\cdot\mathbf F=-\kappa_aE,\quad\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa_a\mathbf F
$$

$$
\mathbf P=E\left[\frac{1-\chi}{2}\mathbf I_3+\frac{3\chi-1}{2}\mathbf n\otimes\mathbf n\right]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\mathbf F|/E,\quad P_{xx}+P_{yy}+P_{zz}=E
$$

保存した反向packetの実進行からM1の限界を示し、別の閉M1MMSで数値実装を検証します。

### 厳密解・参照解

独立な特性cell平均と閉M1強制項の複素step検査191項目がmain前に合格。全step収支・cone・正値、別時間probe、MMSとx/y実進行の収束を検査します。 新fluxの762固定成分判定がPDE改訂前に合格。旧17pytestを維持し方向別fluxの5回帰を追加した22pytestと、元24計算・166科学判定を同じ120秒上限で再検査します。

#### [反向伝播packetの特性線参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja#opposing-beams2d-ja-measurements)

解析解 · 同じ問題の参照

Iplus(x,y,t)=6G(x-t,y;.25); Iminus(x,y,t)=6G(x+t,y;.75); E=Gplus+Gminus,Fx=Gplus-Gminus,Fy=0; Pxx=E,Pyy=Pzz=0.

2D空間に3D角度測度を用い、c=1の軸に整列した光線を扱います。実際の符号付き角度輸送と非線形の閉じたM1方程式をともに進めます。解析特性線の参照はRTE/S_Nに適用し、M1解全体の厳密参照とはしません。

6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。

#### 2D反向beamとM1閉包の情報損失

独立な特性cell平均と閉M1強制項の複素step検査191項目がmain前に合格。全step収支・cone・正値、別時間probe、MMSとx/y実進行の収束を検査します。 新fluxの762固定成分判定がPDE改訂前に合格。旧17pytestを維持し方向別fluxの5回帰を追加した22pytestと、元24計算・166科学判定を同じ120秒上限で再検査します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja)

### 計算法

風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。

- [放射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Rusanov／局所Lax–Friedrichs流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja)

補助実行例

保存した反向packetの実進行からM1の限界を示し、別の閉M1MMSで数値実装を検証します。

2D空間と3D角度測度、c1、静止吸収体。実S_Nと非線形M1を24/48/96格子で進め、同一solverの変動方向MMS・x/y交差packet controlを保持。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/radiation-geometry/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/run.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/geometry.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/mms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/mms.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/wavespeeds.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/wavespeeds.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/test_directional.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/test_directional.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/test_geometry.py)

## English

[Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-geometry/#opposing-beams2d) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#opposing-beams2d-en)

### Equations and problem definitions

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.

#### [Static grey radiative transfer,scattering and linear exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en)

$$
\epsilon\partial_t I+\boldsymbol\Omega\cdot\nabla I+(\kappa_a+\kappa_s)I=\kappa_sJ+\kappa_aV+Q
$$

$$
J=\langle I\rangle_\Omega,\quad\partial_t V=\kappa_a(J-V)\quad(\mathrm{linear\ exchange})
$$

Use a normalized angular mean. Material exchange is evolved in the1997 transport example and periodic Fourier controls. The1997 optical coordinates give a unit exchange coefficient; physical-coordinate controls multiply both exchange terms by kappa.

#### [Static grey M1 moments in flat spacetime](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-m1-en)

$$
E_t+\nabla\cdot\boldsymbol F=-\kappa E+S_E,\quad\boldsymbol F_t+\nabla\cdot\mathsf P=-\kappa\boldsymbol F+\boldsymbol S_F
$$

$$
\mathsf P=E[(1-\chi)\mathsf I_3/2+(3\chi-1)\boldsymbol n\boldsymbol n^T/2]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\boldsymbol F|/E
$$

c=1,2D space with full3D pressure including Pzz. Separate isotropic/vacuum branches,closed-PDE MMS and beam defects against angular transport; no relativistic-fluid claim.

#### Opposing beams and information loss in the M1 closure

Supplementary execution example · Example definition or validation formula

$$
\partial_tE+\nabla\cdot\mathbf F=-\kappa_aE,\quad\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa_a\mathbf F
$$

$$
\mathbf P=E\left[\frac{1-\chi}{2}\mathbf I_3+\frac{3\chi-1}{2}\mathbf n\otimes\mathbf n\right]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\mathbf F|/E,\quad P_{xx}+P_{yy}+P_{zz}=E
$$

Show the M1 limitation in actual opposing-packet evolution; validate the same closed M1 solver independently with a manufactured solution.

### Exact and reference solutions

The independent characteristic cell averages and manufactured M1 forcing passed191reference/component checks before any PDE main. Check all-step budgets, realizability and positivity, spatial refinement, a separate half-step probe, and actual x/y evolution. Opposing-beam closure error is distinguished from numerical error. The new general flux passed762fixed component checks before this revised PDE main. Retain the17old tests and add5directional regressions=22tests; all24fixed runs and166scientific gates remain unchanged under the same120second limit.

#### [Counterpropagating packet characteristic reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en#opposing-beams2d-en-measurements)

Analytic reference · Reference for the same problem

Iplus(x,y,t)=6G(x-t,y;.25); Iminus(x,y,t)=6G(x+t,y;.75); E=Gplus+Gminus,Fx=Gplus-Gminus,Fy=0; Pxx=E,Pyy=Pzz=0.

2Dspace with3Dangular measure,c1. Pure aligned rays; actual signed-angle transport and nonlinear closed M1 both evolved. The analytic characteristic reference applies to RTE/S_N,not to the entire M1 solution.

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

#### Opposing beams and information loss in the M1 closure

The independent characteristic cell averages and manufactured M1 forcing passed191reference/component checks before any PDE main. Check all-step budgets, realizability and positivity, spatial refinement, a separate half-step probe, and actual x/y evolution. Opposing-beam closure error is distinguished from numerical error. The new general flux passed762fixed component checks before this revised PDE main. Retain the17old tests and add5directional regressions=22tests; all24fixed runs and166scientific gates remain unchanged under the same120second limit.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en)

### Numerical methods

Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en)

Supplementary execution example

Show the M1 limitation in actual opposing-packet evolution; validate the same closed M1 solver independently with a manufactured solution.

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/radiation-geometry/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/run.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/geometry.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/mms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/mms.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/wavespeeds.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/wavespeeds.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/test_directional.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/test_directional.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/test_geometry.py)
