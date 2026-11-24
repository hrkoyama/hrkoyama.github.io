# 曲面LBMの環状Couette制御：速度・圧力・torque / Curved LBM annular Couette control: velocity,pressure andtorque

https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/

## 日本語

[固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-lbm-annulus/#lbm-annular-couette-control) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#lbm-annular-couette-control)

### 方程式・問題の定義

Rin.2/Rout.4、中心(.5,.5)、内壁接線速度.02、外壁静止、ν.01。N80/160/240、tau.7、T4、整数3840/15360/34560steps、両境界法計6runs。初期は解析場の平衡分布。

#### [等温格子BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja)

$$
f_q(\boldsymbol x+\boldsymbol c_q,t+1)=f_q(\boldsymbol x,t)-\frac{f_q-f_q^{\rm eq}}{\tau}+S_q
$$

格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。

#### [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja)

$$
\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\rho^{-1}\nabla p+\nu\nabla^2\boldsymbol u
$$

$$
\nabla\cdot\boldsymbol u=0
$$

一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。

#### 曲面LBMの環状Couette制御：速度・圧力・torque

補助実行例 · 実行例の定義・検証式

$$
u_\theta=Ar+B/r,\quad A=-U_iR_i/(R_o^2-R_i^2),\quad B=U_iR_iR_o^2/(R_o^2-R_i^2)
$$

$$
p=\tfrac12A^2r^2+2AB\log r-\tfrac12B^2/r^2+C,\quad T_{inner}=-4\pi\rho\nu B
$$

実円弧交点の2次Lagrange補間とstair-halfwayを、回転内壁の解析Navier–Stokes場に比較します。円柱wakeとは別の追加制御です。

### 厳密解・参照解

群28pytest、環状80判定。独立半径/Cartesian微分7資格、最細速度.03・全点圧力ゲージ.08・torque相対.05、定常性・細分化・stair差・壁込み収支。別の87成分資格に合格済みですが主計算合格とは分けます。 新160/240格子の別29成分資格に合格。

#### [曲面LBMの環状Couette制御：速度・圧力・トルク](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja#lbm-annular-couette-control-ja-measurements)

解析解 · 同じ問題の参照

u_theta=Ar+B/r; p=A^2r^2/2+2AB log(r)-B^2/(2r^2)+C; T_inner=-4pi rho nu B.

Rin.2/Rout.4、中心(.5,.5)、内壁接線速度.02、外壁静止、ν.01。N80/160/240、tau.7、T4、整数3840/15360/34560steps、両境界法計6runs。初期は解析場の平衡分布。

固定円弧と低速回転のみ。2次補間は負係数を含み一般の正値性や安定性を保証しません。補間mass非保存は実値を記録。以前の線形版は圧力.617757>.08で不合格として保存し、半径平均への置換なし。移動solidの拓撲変化や円柱の代用ではありません。 2次版旧N80の圧力.352758>.08も不合格として保持し、Ui/tau/Tを変えず両境界を固定細分化します。

#### 曲面LBMの環状Couette制御：速度・圧力・torque

群28pytest、環状80判定。独立半径/Cartesian微分7資格、最細速度.03・全点圧力ゲージ.08・torque相対.05、定常性・細分化・stair差・壁込み収支。別の87成分資格に合格済みですが主計算合格とは分けます。 新160/240格子の別29成分資格に合格。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja)

### 計算法

円弧交点qから反射特性上の3点2次補間を行います。q<.5はoutgoingの内側2点、q>.5はincomingの内側1点を使用し、q=.5はhalfway。移動壁補正、実force/torqueと非零wall massを台帳化し、floorやmass補正をしません。

- [D2Q9–BGK衝突・並進](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja)

補助実行例

実円弧交点の2次Lagrange補間とstair-halfwayを、回転内壁の解析Navier–Stokes場に比較します。円柱wakeとは別の追加制御です。

Rin.2/Rout.4、中心(.5,.5)、内壁接線速度.02、外壁静止、ν.01。N80/160/240、tau.7、T4、整数3840/15360/34560steps、両境界法計6runs。初期は解析場の平衡分布。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/atlas-lbm-annulus-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

固定円弧と低速回転のみ。2次補間は負係数を含み一般の正値性や安定性を保証しません。補間mass非保存は実値を記録。以前の線形版は圧力.617757>.08で不合格として保存し、半径平均への置換なし。移動solidの拓撲変化や円柱の代用ではありません。 2次版旧N80の圧力.352758>.08も不合格として保持し、Ui/tau/Tを変えず両境界を固定細分化します。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/lbm-annulus/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/run.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-annulus/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/native.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/test_lbm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/test_lbm.py)

## English

[Actual saved2Dfields anddiagnostics fromfixedinputs; reference,boundary anderror scopesaredeclaredinthecase.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-lbm-annulus/#lbm-annular-couette-control) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#lbm-annular-couette-control-en)

### Equations and problem definitions

Rin.2/Rout.4,center(.5,.5),inner tangential speed.02,stationary outerwall,nu.01. N80/160/240,tau.7,T4,integer3840/15360/34560steps; both boundaries give sixruns. Initialize equilibrium moments of the analytic field.

#### [Isothermal lattice BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en)

$$
f_q(\boldsymbol x+\boldsymbol c_q,t+1)=f_q(\boldsymbol x,t)-\frac{f_q-f_q^{\rm eq}}{\tau}+S_q
$$

Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow.

#### [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en)

$$
\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\rho^{-1}\nabla p+\nu\nabla^2\boldsymbol u
$$

$$
\nabla\cdot\boldsymbol u=0
$$

Representative constant-density/viscosity flow. In addition to periodic2D MAC projection/Taylor–Green, a separate release verifies a pressure-eliminated nonperiodic Re100 cavity.

#### Curved LBM annular Couette control: velocity,pressure andtorque

Supplementary execution example · Example definition or validation formula

$$
u_\theta=Ar+B/r,\quad A=-U_iR_i/(R_o^2-R_i^2),\quad B=U_iR_iR_o^2/(R_o^2-R_i^2)
$$

$$
p=\tfrac12A^2r^2+2AB\log r-\tfrac12B^2/r^2+C,\quad T_{inner}=-4\pi\rho\nu B
$$

Compare true-circle quadratic Lagrange link interpolation andstair halfway against analytic rotating-inner-wall Navier–Stokes flow; anadditional control distinct fromcylinderwake.

### Exact and reference solutions

Group28pytest;80annular gates. Sevenindependent radial/Cartesian qualifiers,finest velocity.03,fullpointwise pressure-gauge.08,torque relative.05,stationarity/refinement/stair comparison andwallinclusive budgets. Separate87component qualifiers passed; this doesnot imply main success. Separate29newmeshcomponentqualifierspassed.

#### [Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en#lbm-annular-couette-control-en-measurements)

Analytic reference · Reference for the same problem

u_theta=Ar+B/r; p=A^2r^2/2+2AB log(r)-B^2/(2r^2)+C; T_inner=-4pi rho nu B.

Rin.2/Rout.4,center(.5,.5),inner tangential speed.02,stationary outerwall,nu.01. N80/160/240,tau.7,T4,integer3840/15360/34560steps; both boundaries give sixruns. Initialize equilibrium moments of the analytic field.

Fixedcircles andslowrotation only. Negative quadratic coefficients preclude a general positivity/stability guarantee; report actual interpolation massnonconservation. Prior linear attemptfailed pressure.617757>.08 andisretained; no radial-average substitution. No changing-solid topology orsubstitute forcylinderflow. Retain the failedquadraticN80pressure.352758>.08;refinebothboundariesatfixedUi/tau/T.

#### Curved LBM annular Couette control: velocity,pressure andtorque

Group28pytest;80annular gates. Sevenindependent radial/Cartesian qualifiers,finest velocity.03,fullpointwise pressure-gauge.08,torque relative.05,stationarity/refinement/stair comparison andwallinclusive budgets. Separate87component qualifiers passed; this doesnot imply main success. Separate29newmeshcomponentqualifierspassed.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en)

### Numerical methods

Three-point quadratic interpolation on the reflected characteristic: twointerior outgoing samples forq<.5,oneinterior incoming sample forq>.5,exacthalfway atq=.5. Record movingwall correction,actual force/torque andnonzero wallmass; nofloor ormassrepair.

- [D2Q9–BGK collision and streaming](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en)

Supplementary execution example

Compare true-circle quadratic Lagrange link interpolation andstair halfway against analytic rotating-inner-wall Navier–Stokes flow; anadditional control distinct fromcylinderwake.

Rin.2/Rout.4,center(.5,.5),inner tangential speed.02,stationary outerwall,nu.01. N80/160/240,tau.7,T4,integer3840/15360/34560steps; both boundaries give sixruns. Initialize equilibrium moments of the analytic field.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/atlas-lbm-annulus-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Fixedcircles andslowrotation only. Negative quadratic coefficients preclude a general positivity/stability guarantee; report actual interpolation massnonconservation. Prior linear attemptfailed pressure.617757>.08 andisretained; no radial-average substitution. No changing-solid topology orsubstitute forcylinderflow. Retain the failedquadraticN80pressure.352758>.08;refinebothboundariesatfixedUi/tau/T.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/lbm-annulus/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/run.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-annulus/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/native.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/test_lbm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/test_lbm.py)
