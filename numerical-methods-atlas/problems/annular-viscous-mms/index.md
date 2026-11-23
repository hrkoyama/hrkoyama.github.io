# 環状領域の可変粘性・真2DベクトルMMS / Annular variable-viscosity vector PDE MMS

https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/

## 日本語

[実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mesh-boundary/#annular-viscous-mms) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#annular-viscous-mms)

### 方程式・問題の定義

1≤r≤2、theta周期、mu=1+.2r²、lambda=0、両円でu=0。A(s)=(s−1)(4−s)、u=(A(1+xy),A(x²−y²)/2)。Nr8/16/32、Ntheta=2Nr。

#### [可変粘性のベクトル応力境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#variable-viscosity-vector-ja)

$$
-\nabla\cdot\boldsymbol\tau=\boldsymbol f,\quad \boldsymbol\tau=2\mu\boldsymbol\varepsilon(\boldsymbol u),\quad \boldsymbol\varepsilon(\boldsymbol u)=\tfrac12(\nabla\boldsymbol u+\nabla\boldsymbol u^T)
$$

$$
1<r<2,\quad \mu=1+r^2/5,\quad A=(r^2-1)(4-r^2),\quad \boldsymbol u_\star=A(1+xy,(x^2-y^2)/2)^T
$$

$$
\int_\Omega2\mu\,\boldsymbol\varepsilon(\boldsymbol u_h):\boldsymbol\varepsilon(\boldsymbol v_h)\,dA=\int_\Omega\boldsymbol f\cdot\boldsymbol v_h\,dA
$$

Cartesianの2成分を結合した線形応力発散BVPです。極座標内のQ1基底と正確な曲線Jacobianを使い、可変μの勾配と剪断応力を含みます。圧力・非圧縮拘束・対流項はありません。

#### 環状領域の可変粘性・真2DベクトルMMS

補助実行例 · 実行例の定義・検証式

$$
-\nabla\cdot(2\mu\epsilon(u))=f,\quad\mu=1+0.2r^2
$$

$$
\int 2\mu\epsilon(u):\epsilon(v)\,r\,dr\,d\theta=\int f\cdot v\,r\,dr\,d\theta
$$

$$
dS=r\,d\theta,\quad t=(2\mu\epsilon(u))n
$$

軸を除く円環で可変粘性の応力発散方程式を実際に解き、速度・歪み・境界tractionと仕事を照合します。

### 厳密解・参照解

独自解析外力を別のCartesian応力差分で資格確認。L2速度/歪み/traction細分化、反力/体積外力と物理tractionの収支、粘性散逸と外力仕事を別々に測定。 体積外力の解析積分(756pi/5,0)も別に照合。

#### [環状粘性ベクトルMMS：独立応力微分で外力を確認](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja#annular-viscous-mms-ja-measurements)

製造解 · 同じ問題の参照

s=x*x+y*y; A=(s-1)*(4-s); u=(A*(1+x*y),A*(x*x-y*y)/2); mu=1+.2*s; f=-div(2*mu*epsilon(u)).

1≤r≤2、theta周期、mu=1+.2r²、lambda=0、両円でu=0。A(s)=(s−1)(4−s)、u=(A(1+xy),A(x²−y²)/2)。Nr8/16/32、Ntheta=2Nr。s=x²+y²、A=(s−1)(4−s)のCartesianベクトル場から応力と外力を解析的に導き、別のCartesian差分応力微分で確認します。体積外力の独立積分(756π/5,0)も照合します。

線形vector粘性BVPです。divfree拘束・圧力・非線形Navier–Stokesは含めません。原点なしのr>0であり、軸stencil検証ではありません。

#### 環状領域の可変粘性・真2DベクトルMMS

独自解析外力を別のCartesian応力差分で資格確認。L2速度/歪み/traction細分化、反力/体積外力と物理tractionの収支、粘性散逸と外力仕事を別々に測定。 体積外力の解析積分(756pi/5,0)も別に照合。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja)

### 計算法

polarのmapped Q1にCartesian速度2成分を置き、r dr dthetaで2mu epsilonの弱形式を4×4 Gauss積分してblock疎解法。円周faceにはr dthetaと外向き法線を使う。

- [Q1有限要素法（曲線座標ベクトルBVP）](https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [環状領域の可変粘性・真2DベクトルMMS](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja)

補助実行例

軸を除く円環で可変粘性の応力発散方程式を実際に解き、速度・歪み・境界tractionと仕事を照合します。

1≤r≤2、theta周期、mu=1+.2r²、lambda=0、両円でu=0。A(s)=(s−1)(4−s)、u=(A(1+xy),A(x²−y²)/2)。Nr8/16/32、Ntheta=2Nr。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

線形vector粘性BVPです。divfree拘束・圧力・非線形Navier–Stokesは含めません。原点なしのr>0であり、軸stencil検証ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/mesh-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/run.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/annulus.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/annulus.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py)

## English

[Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mesh-boundary/#annular-viscous-mms) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#annular-viscous-mms-en)

### Equations and problem definitions

1≤r≤2, periodic angle, mu=1+.2r², lambda0 and zero velocity on both circles. A(s)=(s−1)(4−s), u=(A(1+xy),A(x²−y²)/2). Nr8/16/32,Ntheta2Nr.

#### [Variable-viscosity vector stress boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#variable-viscosity-vector-en)

$$
-\nabla\cdot\boldsymbol\tau=\boldsymbol f,\quad \boldsymbol\tau=2\mu\boldsymbol\varepsilon(\boldsymbol u),\quad \boldsymbol\varepsilon(\boldsymbol u)=\tfrac12(\nabla\boldsymbol u+\nabla\boldsymbol u^T)
$$

$$
1<r<2,\quad \mu=1+r^2/5,\quad A=(r^2-1)(4-r^2),\quad \boldsymbol u_\star=A(1+xy,(x^2-y^2)/2)^T
$$

$$
\int_\Omega2\mu\,\boldsymbol\varepsilon(\boldsymbol u_h):\boldsymbol\varepsilon(\boldsymbol v_h)\,dA=\int_\Omega\boldsymbol f\cdot\boldsymbol v_h\,dA
$$

Linear stress-divergence BVP coupling two Cartesian components. Q1 basis functions in polar coordinates use the exact curved Jacobian and include variable-mu gradients and shear. There is no pressure,incompressibility constraint or advective term.

#### Annular variable-viscosity vector PDE MMS

Supplementary execution example · Example definition or validation formula

$$
-\nabla\cdot(2\mu\epsilon(u))=f,\quad\mu=1+0.2r^2
$$

$$
\int 2\mu\epsilon(u):\epsilon(v)\,r\,dr\,d\theta=\int f\cdot v\,r\,dr\,d\theta
$$

$$
dS=r\,d\theta,\quad t=(2\mu\epsilon(u))n
$$

Actually solve variable-viscosity stress divergence on an annulus; check velocity, strain, physical traction and work.

### Exact and reference solutions

Qualify the derived force by separate Cartesian stress differentiation. Measure velocity/strain/traction refinement, reactions versus volume-force/physical traction budgets, and viscous dissipation versus force work. Also check the independently integrated body force (756pi/5,0).

#### [Annular vector-viscous MMS: force qualified by independent stress differentiation](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en#annular-viscous-mms-en-measurements)

Manufactured solution · Reference for the same problem

s=x*x+y*y; A=(s-1)*(4-s); u=(A*(1+x*y),A*(x*x-y*y)/2); mu=1+.2*s; f=-div(2*mu*epsilon(u)).

1≤r≤2, periodic angle, mu=1+.2r², lambda0 and zero velocity on both circles. A(s)=(s−1)(4−s), u=(A(1+xy),A(x²−y²)/2). Nr8/16/32,Ntheta2Nr. Derive stress/force from the Cartesian vector field with s=x²+y²,A=(s-1)(4-s), then qualify force by separate Cartesian stress finite differentiation. Also check independent integrated body force(756pi/5,0).

A linear vector viscous BVP, without divergence-free constraint, pressure or nonlinear Navier–Stokes. r>0 only; no axis stencil certification.

#### Annular variable-viscosity vector PDE MMS

Qualify the derived force by separate Cartesian stress differentiation. Measure velocity/strain/traction refinement, reactions versus volume-force/physical traction budgets, and viscous dissipation versus force work. Also check the independently integrated body force (756pi/5,0).

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en)

### Numerical methods

Mapped polar Q1 with two Cartesian velocity components;4×4 Gauss integration of2mu epsilon uses exact r dr dtheta metric, followed by a block sparse solve. Circular traction uses r dtheta and outward normals.

- [Q1 FEM for mapped-coordinate vector BVP](https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Annular variable-viscosity vector PDE MMS](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en)

Supplementary execution example

Actually solve variable-viscosity stress divergence on an annulus; check velocity, strain, physical traction and work.

1≤r≤2, periodic angle, mu=1+.2r², lambda0 and zero velocity on both circles. A(s)=(s−1)(4−s), u=(A(1+xy),A(x²−y²)/2). Nr8/16/32,Ntheta2Nr.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

A linear vector viscous BVP, without divergence-free constraint, pressure or nonlinear Navier–Stokes. r>0 only; no axis stencil certification.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/mesh-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/run.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/annulus.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/annulus.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py)
