# SRMHDの有限振幅円偏極Alfvén波 / SRMHD finite-amplitude circularly polarized Alfvén wave

https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/

## 日本語

[最細格子の実際の横磁場Byの1D x–t図。5保存時刻を使い、計算は完全な磁気結合を含みます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-relativistic/#srmhd-alfven) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#srmhd-alfven)

### 方程式・問題の定義

平坦時空、c=4π=1、γ=4/3、ρ=p=Bx=η=1、vx=0の厳密族。原著2π周期を単位区間へ写し、64/128/256セル、周期境界、t=1/vA。Bxは1次元で固定します。

#### [特殊相対論的理想MHD（SRMHD）](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srmhd-ja)

$$
\partial_\mu(\rho u^\mu)=0,\qquad \partial_\mu T^{\mu\nu}=0
$$

$$
T^{\mu\nu}=(\rho h+b^2)u^\mu u^\nu+(p+b^2/2)\eta^{\mu\nu}-b^\mu b^\nu
$$

$$
\partial_t\boldsymbol B-\nabla\times(\boldsymbol v\times\boldsymbol B)=0,\quad \nabla\cdot\boldsymbol B=0,\quad h=1+\frac{\Gamma p}{(\Gamma-1)\rho}
$$

$$
K=\rho h+B_0^2(1+\eta_A^2),\quad v_A^2=\frac{2B_0^2}{K+\sqrt{K^2-4\eta_A^2B_0^4}}
$$

c=4π=1、平坦時空・理想電気伝導・γ則EOSです。bμは流体静止系磁場4ベクトル。全磁気応力と誘導を含む7保存量を1Dで進め、原始変数は完全なRMHDのZ根で復元します。GRMHDとは区別します。

#### SRMHDの有限振幅円偏極Alfvén波

補助実行例 · 実行例の定義・検証式

$$
B_y=\eta B_0\cos[2\pi(x-v_At)],\quad B_z=\eta B_0\sin[2\pi(x-v_At)]
$$

$$
v_x=0,\quad (v_y,v_z)=-v_A(B_y,B_z)/B_0
$$

$$
K=\rho h+B_0^2(1+\eta^2),\quad v_A^2=\frac{2B_0^2}{K+\sqrt{K^2-4\eta^2B_0^4}}
$$

$$
\mathbf v=\frac{\mathbf S+(\mathbf S\cdot\mathbf B)\mathbf B/Z}{Z+B^2},\quad p=\frac{\Gamma-1}{\Gamma}(Z/W^2-\rho)
$$

$$
E=Z-p+\frac12\left[B^2(1+v^2)-\frac{(\mathbf S\cdot\mathbf B)^2}{Z^2}\right]
$$

完全な磁気応力と誘導を含むSRMHDで非線形有限振幅波を1周期進め、厳密セル平均、位相、振幅と細分化を検査します。

### 厳密解・参照解

非線形分散式、独立テンソルのGauss積分と複素段階PDE残差で参照を確認。全7量保存と全段物理性、途中誤差、最細相対L1≤.04、位相≤.03、振幅≤.04、観測次数≥1.5を事前固定します。

#### [SRMHD円偏波：有限振幅厳密族と独立テンソル積分](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja#srmhd-alfven-ja-measurements)

解析解 · 同じ問題の参照

K=rho*h+B0^2*(1+eta^2); vA^2=2*B0^2/(K+sqrt(K^2-4*eta^2*B0^4)); (By,Bz)=eta*B0*(cos(2*pi*(x-vA*t)),sin(2*pi*(x-vA*t))); (vy,vz)=-vA*(By,Bz)/B0.

平坦時空、c=4π=1、γ=4/3、ρ=p=Bx=η=1、vx=0の厳密族。原著2π周期を単位区間へ写し、64/128/256セル、周期境界、t=1/vA。Bxは1次元で固定します。非線形Alfvén速度の閉じた式を使い、点の原始変数から独立なストレステンソルで保存量と流束を作り、Gauss積分と複素段階PDE残差で確認します。原著の2π周期を単位区間へ移しています。

原著の厳密解族を独立な低次法で計算し、ECHO法や原著誤差表は再現しません。一般RMHD衝撃波、極端な磁化・Lorentz因子、GR、抵抗MHD、多次元磁場発散制御は対象外。図は実際の1D時空間場です。

#### SRMHDの有限振幅円偏極Alfvén波

非線形分散式、独立テンソルのGauss積分と複素段階PDE残差で参照を確認。全7量保存と全段物理性、途中誤差、最細相対L1≤.04、位相≤.03、振幅≤.04、観測次数≥1.5を事前固定します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja)

### 計算法

D・運動量3成分・全エネルギー・横磁場2成分の全7変数を同じMUSCL/minmod–HLL–SSPRK33で進めます。磁場は動的に結合し、完全なRMHDのZ根で原始変数へ復元します。

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja)

補助実行例

完全な磁気応力と誘導を含むSRMHDで非線形有限振幅波を1周期進め、厳密セル平均、位相、振幅と細分化を検査します。

平坦時空、c=4π=1、γ=4/3、ρ=p=Bx=η=1、vx=0の厳密族。原著2π周期を単位区間へ写し、64/128/256セル、周期境界、t=1/vA。Bxは1次元で固定します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

原著の厳密解族を独立な低次法で計算し、ECHO法や原著誤差表は再現しません。一般RMHD衝撃波、極端な磁化・Lorentz因子、GR、抵抗MHD、多次元磁場発散制御は対象外。図は実際の1D時空間場です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/relativistic/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/run.py)
- [/code/validated-examples/2026-11-23/relativistic/relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/relativistic.py)
- [/code/validated-examples/2026-11-23/relativistic/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/references/exact.py)
- [/code/validated-examples/2026-11-23/relativistic/test_relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/test_relativistic.py)

## English

[Actual finest-grid transverse By in1D x–t from five stored times; the solver includes full magnetic coupling.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-relativistic/#srmhd-alfven) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#srmhd-alfven-en)

### Equations and problem definitions

Flat spacetime,c=4pi=1,gamma4/3,rho=p=Bx=eta1, exact-family vx0. Rescale the original2pi period to a unit domain;64/128/256 cells,periodic,t=1/vA. Normal Bx is fixed in1D.

#### [Special-relativistic ideal MHD (SRMHD)](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srmhd-en)

$$
\partial_\mu(\rho u^\mu)=0,\qquad \partial_\mu T^{\mu\nu}=0
$$

$$
T^{\mu\nu}=(\rho h+b^2)u^\mu u^\nu+(p+b^2/2)\eta^{\mu\nu}-b^\mu b^\nu
$$

$$
\partial_t\boldsymbol B-\nabla\times(\boldsymbol v\times\boldsymbol B)=0,\quad \nabla\cdot\boldsymbol B=0,\quad h=1+\frac{\Gamma p}{(\Gamma-1)\rho}
$$

$$
K=\rho h+B_0^2(1+\eta_A^2),\quad v_A^2=\frac{2B_0^2}{K+\sqrt{K^2-4\eta_A^2B_0^4}}
$$

Flat spacetime,ideal conductivity,gamma-law EOS,c=4pi=1; b^mu is the comoving magnetic four-vector. The1D solver evolves seven conserved variables with full magnetic stress and induction, using coupled RMHD Z recovery. Distinguish it from GRMHD.

#### SRMHD finite-amplitude circularly polarized Alfvén wave

Supplementary execution example · Example definition or validation formula

$$
B_y=\eta B_0\cos[2\pi(x-v_At)],\quad B_z=\eta B_0\sin[2\pi(x-v_At)]
$$

$$
v_x=0,\quad (v_y,v_z)=-v_A(B_y,B_z)/B_0
$$

$$
K=\rho h+B_0^2(1+\eta^2),\quad v_A^2=\frac{2B_0^2}{K+\sqrt{K^2-4\eta^2B_0^4}}
$$

$$
\mathbf v=\frac{\mathbf S+(\mathbf S\cdot\mathbf B)\mathbf B/Z}{Z+B^2},\quad p=\frac{\Gamma-1}{\Gamma}(Z/W^2-\rho)
$$

$$
E=Z-p+\frac12\left[B^2(1+v^2)-\frac{(\mathbf S\cdot\mathbf B)^2}{Z^2}\right]
$$

Evolve a nonlinear finite-amplitude wave for one period with full SRMHD magnetic stress and induction; check exact cell means,phase,amplitude and refinement.

### Exact and reference solutions

Qualify nonlinear dispersion,independent tensor Gauss means and complex-step PDE residuals. Predeclare all-seven-component conservation,stage admissibility,intermediate errors,finest relative L1≤.04,phase≤.03,amplitude≤.04 and observed order≥1.5.

#### [SRMHD circular wave: finite-amplitude exact family and independent tensor integration](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en#srmhd-alfven-en-measurements)

Analytic reference · Reference for the same problem

K=rho*h+B0^2*(1+eta^2); vA^2=2*B0^2/(K+sqrt(K^2-4*eta^2*B0^4)); (By,Bz)=eta*B0*(cos(2*pi*(x-vA*t)),sin(2*pi*(x-vA*t))); (vy,vz)=-vA*(By,Bz)/B0.

Flat spacetime,c=4pi=1,gamma4/3,rho=p=Bx=eta1, exact-family vx0. Rescale the original2pi period to a unit domain;64/128/256 cells,periodic,t=1/vA. Normal Bx is fixed in1D. Use the closed nonlinear Alfven-speed formula. Independently form conserved quantities/fluxes from point primitives through the stress tensor; qualify Gauss integration and complex-step PDE residuals. Rescale the original2pi period to the unit interval.

Use the original exact family with an independent lower-order operator; no ECHO-algorithm or error-table reproduction. Generic RMHD shocks,extreme magnetization/Lorentz factors,GR,resistive MHD and multidimensional divergence control are outside scope. Figures show actual1D x–t fields.

#### SRMHD finite-amplitude circularly polarized Alfvén wave

Qualify nonlinear dispersion,independent tensor Gauss means and complex-step PDE residuals. Predeclare all-seven-component conservation,stage admissibility,intermediate errors,finest relative L1≤.04,phase≤.03,amplitude≤.04 and observed order≥1.5.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en)

### Numerical methods

Evolve all seven variables D,three momenta,total E and two transverse magnetic fields with the shared MUSCL/minmod–HLL–SSPRK33 operator. Magnetic dynamics are coupled; primitive recovery solves the full RMHD Z root.

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en)

Supplementary execution example

Evolve a nonlinear finite-amplitude wave for one period with full SRMHD magnetic stress and induction; check exact cell means,phase,amplitude and refinement.

Flat spacetime,c=4pi=1,gamma4/3,rho=p=Bx=eta1, exact-family vx0. Rescale the original2pi period to a unit domain;64/128/256 cells,periodic,t=1/vA. Normal Bx is fixed in1D.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Use the original exact family with an independent lower-order operator; no ECHO-algorithm or error-table reproduction. Generic RMHD shocks,extreme magnetization/Lorentz factors,GR,resistive MHD and multidimensional divergence control are outside scope. Figures show actual1D x–t fields.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/relativistic/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/run.py)
- [/code/validated-examples/2026-11-23/relativistic/relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/relativistic.py)
- [/code/validated-examples/2026-11-23/relativistic/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/references/exact.py)
- [/code/validated-examples/2026-11-23/relativistic/test_relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/test_relativistic.py)
