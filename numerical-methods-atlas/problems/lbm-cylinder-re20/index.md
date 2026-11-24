# LBMの実円柱Re20：Schäfer–Turek形状と明示出口 / Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet

https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/

## 日本語

[固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-lbm-curved-boundary/#lbm-cylinder-re20) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#lbm-cylinder-re20)

### 方程式・問題の定義

[0,2.2]x[0,.41]、中心(.2,.2)、R.05、ν.001、rho1、平均流速.2/最大.3/Re20。dx.01/.005、x wet nodes221/441、y halfway nodes41/82、dt=dx/6、T30、18k/36ksteps。入口parabola、出口はrho1と隣接内点poststream速度による全9成分NEE。

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

#### LBMの実円柱Re20：Schäfer–Turek形状と明示出口

補助実行例 · 実行例の定義・検証式

$$
\mathrm{Re}=\overline U D/\nu=20,\quad C_D=2F_x/(\rho\overline U^2D),\quad C_L=2F_y/(\rho\overline U^2D)
$$

$$
\Delta p=p(.15,.2)-p(.25,.2),\quad L_a=x_{reattach}-.25
$$

$$
f_{i,b}=f_i^{eq}(1,u_a)+f_{i,a}-f_i^{eq}(\rho_a,u_a),\quad i=0,\ldots,8
$$

標準2D-1の全長channelと偏心円柱を実際に発展し、抗力・揚力・表面圧力差・再循環長と定常性を2格子で検査します。

### 厳密解・参照解

群28pytest、円柱33判定。原典表3の推定範囲からの距離を別の事前粗格子公差で判定（CD5%、CL絶対.01、dp10%、La絶対.025）。26/28/30で場・力・dpの定常性、2格子差・Ma・wall/open収支も確認します。 元の出口不安定も保存し、境界式の別87成分資格と主計算を区別します。

#### [実LBMのRe20円柱流：Schäfer–Turek形状と明示した流出境界](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja#lbm-cylinder-re20-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

Re=Umean D/nu=20; CD=2Fx/(rho Umean^2 D); CL=2Fy/(rho Umean^2 D); delta p=p(.15,.2)-p(.25,.2).

[0,2.2]x[0,.41]、中心(.2,.2)、R.05、ν.001、rho1、平均流速.2/最大.3/Re20。dx.01/.005、x wet nodes221/441、y halfway nodes41/82、dt=dx/6、T30、18k/36ksteps。入口parabola、出口はrho1と隣接内点poststream速度による全9成分NEE。

原典p3/p7は出口を選択可。採用NEEは独立導出した有限reservoirで、原著NEE全文の同一実装やFEATflow do-nothingと偽りません。Nabh高精度値は同BCの厳密値ではなく、原典範囲も厳密誤差区間ではありません。線形/Zou–He旧試行はstep265出口近傍で不合格として保持。有限Mach/境界/曲面差を含み一般精度保証なし。

#### LBMの実円柱Re20：Schäfer–Turek形状と明示出口

群28pytest、円柱33判定。原典表3の推定範囲からの距離を別の事前粗格子公差で判定（CD5%、CL絶対.01、dp10%、La絶対.025）。26/28/30で場・力・dpの定常性、2格子差・Ma・wall/open収支も確認します。 元の出口不安定も保存し、境界式の別87成分資格と主計算を区別します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja)

### 計算法

標準BGK、真円交点の2次補間、半格子channel壁、非周期open streaming。出口全9成分にfeq(1,ua)+fa−feq(rhoa,ua)を設定し、既知6成分を含む変化量を収支へ記録。初期Poiseuille圧力guessから円柱摂動を実発展し、実運動量交換を平均流速基準の力係数へ換算します。

- [D2Q9–BGK衝突・並進](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja)

補助実行例

標準2D-1の全長channelと偏心円柱を実際に発展し、抗力・揚力・表面圧力差・再循環長と定常性を2格子で検査します。

[0,2.2]x[0,.41]、中心(.2,.2)、R.05、ν.001、rho1、平均流速.2/最大.3/Re20。dx.01/.005、x wet nodes221/441、y halfway nodes41/82、dt=dx/6、T30、18k/36ksteps。入口parabola、出口はrho1と隣接内点poststream速度による全9成分NEE。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/atlas-lbm-curved-boundary-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

原典p3/p7は出口を選択可。採用NEEは独立導出した有限reservoirで、原著NEE全文の同一実装やFEATflow do-nothingと偽りません。Nabh高精度値は同BCの厳密値ではなく、原典範囲も厳密誤差区間ではありません。線形/Zou–He旧試行はstep265出口近傍で不合格として保持。有限Mach/境界/曲面差を含み一般精度保証なし。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/lbm-curved-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/run.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/native.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/test_lbm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/test_lbm.py)

## English

[Actual saved2Dfields anddiagnostics fromfixedinputs; reference,boundary anderror scopesaredeclaredinthecase.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-lbm-curved-boundary/#lbm-cylinder-re20) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#lbm-cylinder-re20-en)

### Equations and problem definitions

[0,2.2]x[0,.41],center(.2,.2),R.05,nu.001,rho1,mean.2/peak.3/Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18k/36ksteps. Parabolic inlet;all-nine poststream NEE outletwithrho1andadjacent-interiorvelocity.

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

#### Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet

Supplementary execution example · Example definition or validation formula

$$
\mathrm{Re}=\overline U D/\nu=20,\quad C_D=2F_x/(\rho\overline U^2D),\quad C_L=2F_y/(\rho\overline U^2D)
$$

$$
\Delta p=p(.15,.2)-p(.25,.2),\quad L_a=x_{reattach}-.25
$$

$$
f_{i,b}=f_i^{eq}(1,u_a)+f_{i,a}-f_i^{eq}(\rho_a,u_a),\quad i=0,\ldots,8
$$

Evolve the full-length original2D-1channel andoff-center cylinder on twogrids,checking drag,lift,surface pressure difference,recirculation length andstationarity.

### Exact and reference solutions

Group28pytest;33cylinder gates. Score distance fromoriginalTable3estimated ranges usingseparate frozen coarse-grid tolerances:CD5%,CLabsolute.01,dp10%,Laabsolute.025. Check26/28/30field/force/dp stationarity,twogrid difference,Ma andwall/open budgets. Retain prior outletinstability anddistinguish the87boundarycomponent qualifiers frommain acceptance.

#### [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en#lbm-cylinder-re20-en-measurements)

Finite-grid numerical reference · Reference for the same problem

Re=Umean D/nu=20; CD=2Fx/(rho Umean^2 D); CL=2Fy/(rho Umean^2 D); delta p=p(.15,.2)-p(.25,.2).

[0,2.2]x[0,.41],center(.2,.2),R.05,nu.001,rho1,mean.2/peak.3/Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18k/36ksteps. Parabolic inlet;all-nine poststream NEE outletwithrho1andadjacent-interiorvelocity.

Originalpp3/7allow selectingoutflow. AdoptedNEEis independently derived finite reservoir,not claimed exactunread authorimplementation orFEATflowdo-nothing. Nabhvaluesarenotexact adopted-BCtruth andoriginalrangesarenotrigorousenclosures. Retain failedlinear/Zou–Heattempt(outlet-nearstep265). FiniteMach/BC/curveerrors;nogeneralaccuracyguarantee.

#### Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet

Group28pytest;33cylinder gates. Score distance fromoriginalTable3estimated ranges usingseparate frozen coarse-grid tolerances:CD5%,CLabsolute.01,dp10%,Laabsolute.025. Check26/28/30field/force/dp stationarity,twogrid difference,Ma andwall/open budgets. Retain prior outletinstability anddistinguish the87boundarycomponent qualifiers frommain acceptance.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en)

### Numerical methods

StandardBGK,true-circle quadratic links,halfwaychannelwalls,nonperiodic openstreaming. Setall9outlet populations tofeq(1,ua)+fa−feq(rhoa,ua); ledgerchanges include theknown6. Evolve fromaPoiseuille pressureguess; normalizeactual momentumexchange bymean speed.

- [D2Q9–BGK collision and streaming](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en)

Supplementary execution example

Evolve the full-length original2D-1channel andoff-center cylinder on twogrids,checking drag,lift,surface pressure difference,recirculation length andstationarity.

[0,2.2]x[0,.41],center(.2,.2),R.05,nu.001,rho1,mean.2/peak.3/Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18k/36ksteps. Parabolic inlet;all-nine poststream NEE outletwithrho1andadjacent-interiorvelocity.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/atlas-lbm-curved-boundary-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Originalpp3/7allow selectingoutflow. AdoptedNEEis independently derived finite reservoir,not claimed exactunread authorimplementation orFEATflowdo-nothing. Nabhvaluesarenotexact adopted-BCtruth andoriginalrangesarenotrigorousenclosures. Retain failedlinear/Zou–Heattempt(outlet-nearstep265). FiniteMach/BC/curveerrors;nogeneralaccuracyguarantee.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/lbm-curved-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/run.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/native.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/test_lbm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/test_lbm.py)
