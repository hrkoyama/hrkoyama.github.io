# 非周期壁面の製造非圧縮流 / Manufactured incompressible flow with nonperiodic walls

https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/

## 日本語

[実計算した最細の製造流れの流線と速度誤差。厳密壁渦度を注入せず、キャビティと同じThom閉鎖を使います。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-wall-flow/#wall-manufactured) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#wall-manufactured)

### 方程式・問題の定義

単位正方形、ν=.01、17/33/65点、ψ=8f(x)f(y),f(z)=z²(1−z)²。全壁で非浸透・滑りなし。渦度外力は連続方程式から解析的に導出し、全壁にキャビティと同じThom条件を使用します。厳密壁渦度は注入しません。

#### [外力付き非圧縮流と壁面製造解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-incompressible-ja)

$$
\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\nabla p+\nu\Delta\boldsymbol u+\boldsymbol f,\qquad\nabla\cdot\boldsymbol u=0
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+s,\quad s=(\nabla\times\boldsymbol f)_z,\quad-\Delta\psi=\omega,\quad(u,v)=(\psi_y,-\psi_x)
$$

$$
\psi_\star=8x^2(1-x)^2y^2(1-y)^2,\quad s=\boldsymbol u_\star\cdot\nabla\omega_\star-\nu\Delta\omega_\star
$$

$$
-\Delta p_{\mathrm{op},\star}=-4+2\pi^2\sin(\pi x)\sin(\pi y),\quad p_{\mathrm{op},\star}=x^2+y^2+\sin(\pi x)\sin(\pi y)
$$

一定密度1の外力付き非圧縮系です。実際の流れは外力のcurlを使う渦度・流れ関数形で圧力を消去します。p_opは独立の非零Dirichlet Poisson・勾配演算子の製造問題で、流れと結合した圧力場やキャビティ圧力ではありません。

#### 非周期壁面の製造解：速度・剪断・圧力演算子

補助実行例 · 実行例の定義・検証式

$$
f(z)=z^2(1-z)^2,\quad \psi_\star=8f(x)f(y),\quad u_\star=\partial_y\psi_\star,\quad v_\star=-\partial_x\psi_\star,\quad\omega_\star=-\Delta\psi_\star
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+s,\quad s=u_\star\partial_x\omega_\star+v_\star\partial_y\omega_\star-\nu\Delta\omega_\star
$$

$$
p_\star=x^2+y^2+\sin(\pi x)\sin(\pi y),\quad -\Delta p_\star=-4+2\pi^2\sin(\pi x)\sin(\pi y),\quad p|_{\partial\Omega}=p_\star
$$

$$
\tau_{xy}/\mu=\partial_y u\quad\text{on stationary horizontal walls},\qquad p_{\mathrm{obs}}=\log_2(E_h/E_{h/2})
$$

キャビティと同じ壁条件付き2Dソルバーに解析外力を与え、速度と流れ関数の格子収束、壁渦度・壁剪断の誤差を測ります。別の非零Dirichlet圧力製造解でPoisson・勾配の境界演算子も検査します。

### 厳密解・参照解

ψと速度の最細刻み対の次数≥1.7、誤差減少・絶対誤差、実際の壁渦度と速度勾配剪断の誤差減少を検査します。圧力演算子はp次数≥1.8、全体と境界の勾配次数≥1.7。独立多項式照合5項目、全壁値、真の定常残差、非周期Poisson残差も記録します。

#### [壁面製造解：多項式速度と独立した圧力演算子](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja#wall-manufactured-ja-measurements)

製造解 · 同じ問題の参照

psi*=8 f(x)f(y),f(z)=z²(1−z)²; s=u*omega*_x+v*omega*_y−nu*Delta omega*. Separate: p_op=x²+y²+sin(pi*x)sin(pi*y).

単位正方形・ν.01・滑りなし、ψ*=8x²(1−x)²y²(1−y)²、u*=ψ*y、v*=−ψ*x、ω*=−Δψ*。連続の渦度式からs=u*ω*x+v*ω*y−νΔω*を構成し、独立の係数行列微分と照合します。PDE計算の壁渦度はキャビティと同じThom式で、厳密値を注入しません。p_op=x²+y²+sinπx sinπyの非零Dirichlet Poisson・勾配は別の演算子問題で、流れに結合した圧力やキャビティ圧力ではありません。

Thomの壁渦度局所打切りは一次で、壁剪断の二次精度は主張せず観測次数を示します。流れ関数の発展では圧力を消去するためゲージは該当しません。圧力診断は独立した演算子製造問題であり、キャビティの圧力・応力境界やMAC射影の検証ではありません。多項式の別微分は独立な流体ソルバーとの比較とは区別します。

#### 非周期壁面の製造解：速度・剪断・圧力演算子

ψと速度の最細刻み対の次数≥1.7、誤差減少・絶対誤差、実際の壁渦度と速度勾配剪断の誤差減少を検査します。圧力演算子はp次数≥1.8、全体と境界の勾配次数≥1.7。独立多項式照合5項目、全壁値、真の定常残差、非周期Poisson残差も記録します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja)

### 計算法

共通の中央差分・Heun・非周期Dirichlet DST Poissonを使用します。多項式の明示微分と、独立な係数行列の微分を照合します。別途p=x²+y²+sinπx sinπyの非零Dirichlet Poisson問題を解き、内部中央差分・壁上の二次片側差分勾配を検査します。

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [非周期壁面の製造解：速度・剪断・圧力演算子](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja)

補助実行例

キャビティと同じ壁条件付き2Dソルバーに解析外力を与え、速度と流れ関数の格子収束、壁渦度・壁剪断の誤差を測ります。別の非零Dirichlet圧力製造解でPoisson・勾配の境界演算子も検査します。

単位正方形、ν=.01、17/33/65点、ψ=8f(x)f(y),f(z)=z²(1−z)²。全壁で非浸透・滑りなし。渦度外力は連続方程式から解析的に導出し、全壁にキャビティと同じThom条件を使用します。厳密壁渦度は注入しません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Thomの壁渦度局所打切りは一次で、壁剪断の二次精度は主張せず観測次数を示します。流れ関数の発展では圧力を消去するためゲージは該当しません。圧力診断は独立した演算子製造問題であり、キャビティの圧力・応力境界やMAC射影の検証ではありません。多項式の別微分は独立な流体ソルバーとの比較とは区別します。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23-r2/wall-flow/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/run.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/wall_flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/wall_flow.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/references/qualify_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/references/qualify_reference.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_result_envelope.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_result_envelope.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_serialization.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_wall_flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_wall_flow.py)

## English

[Computed finest manufactured-flow streamlines and velocity error, using the same Thom closure as the cavity without exact wall-vorticity injection.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-wall-flow/#wall-manufactured) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#wall-manufactured-en)

### Equations and problem definitions

Unit square, viscosity.01,17/33/65nodes,psi8f(x)f(y), f(z)=z²(1−z)². All walls are impermeable/no-slip. Derive the curl forcing from the continuous PDE and use the same actual Thom closure as the cavity on every wall; never inject exact wall vorticity.

#### [Forced incompressible flow and wall manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-incompressible-en)

$$
\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\nabla p+\nu\Delta\boldsymbol u+\boldsymbol f,\qquad\nabla\cdot\boldsymbol u=0
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+s,\quad s=(\nabla\times\boldsymbol f)_z,\quad-\Delta\psi=\omega,\quad(u,v)=(\psi_y,-\psi_x)
$$

$$
\psi_\star=8x^2(1-x)^2y^2(1-y)^2,\quad s=\boldsymbol u_\star\cdot\nabla\omega_\star-\nu\Delta\omega_\star
$$

$$
-\Delta p_{\mathrm{op},\star}=-4+2\pi^2\sin(\pi x)\sin(\pi y),\quad p_{\mathrm{op},\star}=x^2+y^2+\sin(\pi x)\sin(\pi y)
$$

Constant-density-one forced incompressible flow. The actual solver uses the curl forcing in a pressure-eliminated vorticity/streamfunction form. p_op is a separate nonzero-Dirichlet Poisson/gradient manufactured operator problem, not a coupled flow pressure or cavity pressure.

#### Nonperiodic wall MMS: velocity, shear and pressure operator

Supplementary execution example · Example definition or validation formula

$$
f(z)=z^2(1-z)^2,\quad \psi_\star=8f(x)f(y),\quad u_\star=\partial_y\psi_\star,\quad v_\star=-\partial_x\psi_\star,\quad\omega_\star=-\Delta\psi_\star
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+s,\quad s=u_\star\partial_x\omega_\star+v_\star\partial_y\omega_\star-\nu\Delta\omega_\star
$$

$$
p_\star=x^2+y^2+\sin(\pi x)\sin(\pi y),\quad -\Delta p_\star=-4+2\pi^2\sin(\pi x)\sin(\pi y),\quad p|_{\partial\Omega}=p_\star
$$

$$
\tau_{xy}/\mu=\partial_y u\quad\text{on stationary horizontal walls},\qquad p_{\mathrm{obs}}=\log_2(E_h/E_{h/2})
$$

Apply analytic forcing to the same wall-bounded2D solver, measuring grid convergence of velocity/streamfunction and actual wall-vorticity/shear errors. A separate nonzero-Dirichlet manufactured pressure verifies Poisson and boundary-gradient operators.

### Exact and reference solutions

Require finest-pair psi/velocity orders≥1.7, decreasing and bounded errors, and decreasing actual wall-vorticity/velocity-gradient shear errors. Separate pressure orders must be≥1.8 forp and≥1.7 for full/boundary gradients. Record five independent polynomial-reference checks, four-wall values, true steady residual and nonperiodic Poisson residual.

#### [Wall manufactured solution: polynomial velocity and separate pressure operator](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en#wall-manufactured-en-measurements)

Manufactured solution · Reference for the same problem

psi*=8 f(x)f(y),f(z)=z²(1−z)²; s=u*omega*_x+v*omega*_y−nu*Delta omega*. Separate: p_op=x²+y²+sin(pi*x)sin(pi*y).

Unit square,viscosity.01,no-slip,psi*=8x²(1−x)²y²(1−y)²,u*=psi*_y,v*=−psi*_x,omega*=−Delta psi*. Construct s=u*omega*_x+v*omega*_y−nu*Delta omega* from the continuous vorticity PDE, qualified by independent tensor-coefficient differentiation. PDE wall vorticity uses the same Thom closure as the cavity without exact injection. Nonzero-Dirichlet Poisson/gradient for p_op=x²+y²+sin(pi*x)sin(pi*y) is a separate operator problem, not coupled flow or cavity pressure.

Thom wall vorticity has first-order local truncation; publish observed shear rates without promising second order. Pressure is eliminated from streamfunction evolution, so a pressure gauge is inapplicable. The separate operator MMS does not verify cavity pressure, traction boundaries or MAC projection. Independent polynomial differentiation is distinct from comparison with an independent flow solver.

#### Nonperiodic wall MMS: velocity, shear and pressure operator

Require finest-pair psi/velocity orders ≥1.7, decreasing and bounded errors, and decreasing actual wall-vorticity/velocity-gradient shear errors. Separate pressure orders must be≥1.8 for p and≥1.7 for full/boundary gradients. Record five independent polynomial-reference checks, four-wall values, true steady residual and nonperiodic Poisson residual.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en)

### Numerical methods

Use the shared centered FD/Heun/nonperiodic Dirichlet DST solver. Qualify explicit analytic derivatives against independently differentiated tensor coefficients. Separately solve nonzero-Dirichlet Poisson forp=x²+y²+sin(pi*x)sin(pi*y), checking central interior and second-order one-sided boundary gradients.

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Nonperiodic wall MMS: velocity, shear and pressure operator](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en)

Supplementary execution example

Apply analytic forcing to the same wall-bounded2D solver, measuring grid convergence of velocity/streamfunction and actual wall-vorticity/shear errors. A separate nonzero-Dirichlet manufactured pressure verifies Poisson and boundary-gradient operators.

Unit square, viscosity .01,17/33/65nodes,psi8f(x)f(y), f(z)=z²(1−z)². All walls are impermeable/no-slip. Derive the curl forcing from the continuous PDE and use the same actual Thom closure as the cavity on every wall; never inject exact wall vorticity.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Thom wall vorticity has first-order local truncation; publish observed shear rates without promising second order. Pressure is eliminated from streamfunction evolution, so a pressure gauge is inapplicable. The separate operator MMS does not verify cavity pressure, traction boundaries or MAC projection. Independent polynomial differentiation is distinct from comparison with an independent flow solver.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23-r2/wall-flow/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/run.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/wall_flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/wall_flow.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/references/qualify_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/references/qualify_reference.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_result_envelope.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_result_envelope.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_serialization.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_wall_flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_wall_flow.py)
