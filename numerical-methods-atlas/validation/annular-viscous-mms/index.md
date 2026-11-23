# 環状領域の可変粘性・真2DベクトルMMS

軸を除く円環で可変粘性の応力発散方程式を実際に解き、速度・歪み・境界tractionと仕事を照合します。

**使用手法**

- [Q1有限要素法（曲線座標ベクトルBVP）](https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=ja) (`q1-fem`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja#annular-viscous-mms-ja-algorithm)

polarのmapped Q1にCartesian速度2成分を置き、r dr dthetaで2mu epsilonの弱形式を4×4 Gauss積分してblock疎解法。円周faceにはr dthetaと外向き法線を使う。

$$
-\nabla\cdot(2\mu\epsilon(u))=f,\quad\mu=1+0.2r^2
$$

$$
\int 2\mu\epsilon(u):\epsilon(v)\,r\,dr\,d\theta=\int f\cdot v\,r\,dr\,d\theta
$$

$$
dS=r\,d\theta,\quad t=(2\mu\epsilon(u))n
$$

- [可変粘性のベクトル応力境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#variable-viscosity-vector-ja) (`variable-viscosity-vector`)

1≤r≤2、theta周期、mu=1+.2r²、lambda=0、両円でu=0。A(s)=(s−1)(4−s)、u=(A(1+xy),A(x²−y²)/2)。Nr8/16/32、Ntheta=2Nr。


**問題の図**

![環状領域の可変粘性・真2DベクトルMMS：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[環状領域の可変粘性・真2DベクトルMMS](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja) (`annular-viscous-mms`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja#annular-viscous-mms-ja-validation)

独自解析外力を別のCartesian応力差分で資格確認。L2速度/歪み/traction細分化、反力/体積外力と物理tractionの収支、粘性散逸と外力仕事を別々に測定。 体積外力の解析積分(756pi/5,0)も別に照合。

- [環状粘性ベクトルMMS：独立応力微分で外力を確認](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-annular-viscous-mms-ja) (`annular-viscous-mms`; 同じ問題の参照 · 製造解)

線形vector粘性BVPです。divfree拘束・圧力・非線形Navier–Stokesは含めません。原点なしのr>0であり、軸stencil検証ではありません。
## 前提・単位・境界

1≤r≤2、theta周期、mu=1+.2r²、lambda=0、両円でu=0。A(s)=(s−1)(4−s)、u=(A(1+xy),A(x²−y²)/2)。Nr8/16/32、Ntheta=2Nr。

**編集上の補足**

線形vector粘性BVPです。divfree拘束・圧力・非線形Navier–Stokesは含めません。原点なしのr>0であり、軸stencil検証ではありません。

## 採用した計算法

polarのmapped Q1にCartesian速度2成分を置き、r dr dthetaで2mu epsilonの弱形式を4×4 Gauss積分してblock疎解法。円周faceにはr dthetaと外向き法線を使う。

$$
-\nabla\cdot(2\mu\epsilon(u))=f,\quad\mu=1+0.2r^2
$$

$$
\int 2\mu\epsilon(u):\epsilon(v)\,r\,dr\,d\theta=\int f\cdot v\,r\,dr\,d\theta
$$

$$
dS=r\,d\theta,\quad t=(2\mu\epsilon(u))n
$$

## 比較・検証

独自解析外力を別のCartesian応力差分で資格確認。L2速度/歪み/traction細分化、反力/体積外力と物理tractionの収支、粘性散逸と外力仕事を別々に測定。 体積外力の解析積分(756pi/5,0)も別に照合。

## 確認の限界

線形vector粘性BVPです。divfree拘束・圧力・非線形Navier–Stokesは含めません。原点なしのr>0であり、軸stencil検証ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "n": 32,
    "theta_cells": 64,
    "dofs": 3968,
    "relative_l2": 0.0022683900910951296,
    "relative_strain_l2": 0.05188955686190023,
    "relative_traction_l2": 0.07266006943162176,
    "residual": 1.0857981180834031e-13,
    "boundary_error": 0.0,
    "area_error": 3.552713678800501e-15,
    "reaction_balance": 1.736671818881876e-15,
    "traction_flux_balance": 0.042495559851796386,
    "exact_flux_balance": 5.984756355647655e-16,
    "analytic_force_error": 8.394500285269018e-16,
    "work_identity": 3.851517252670248e-15,
    "symmetry": 3.552713678800501e-15
  },
  "checks": {
    "annulus-n8 residual": true,
    "annulus-n8 boundary_error": true,
    "annulus-n8 area_error": true,
    "annulus-n8 reaction_balance": true,
    "annulus-n8 exact_flux_balance": true,
    "annulus-n8 analytic_force_error": true,
    "annulus-n8 work_identity": true,
    "annulus-n8 symmetry": true,
    "annulus-n16 residual": true,
    "annulus-n16 boundary_error": true,
    "annulus-n16 area_error": true,
    "annulus-n16 reaction_balance": true,
    "annulus-n16 exact_flux_balance": true,
    "annulus-n16 analytic_force_error": true,
    "annulus-n16 work_identity": true,
    "annulus-n16 symmetry": true,
    "annulus-n32 residual": true,
    "annulus-n32 boundary_error": true,
    "annulus-n32 area_error": true,
    "annulus-n32 reaction_balance": true,
    "annulus-n32 exact_flux_balance": true,
    "annulus-n32 analytic_force_error": true,
    "annulus-n32 work_identity": true,
    "annulus-n32 symmetry": true,
    "relative_l2 refinement 1": true,
    "relative_l2 refinement 2": true,
    "relative_strain_l2 refinement 1": true,
    "relative_strain_l2 refinement 2": true,
    "relative_traction_l2 refinement 1": true,
    "relative_traction_l2 refinement 2": true,
    "traction_flux_balance refinement 1": true,
    "traction_flux_balance refinement 2": true,
    "finest relative_l2": true,
    "finest relative_strain_l2": true,
    "finest relative_traction_l2": true,
    "finest traction_flux_balance": true,
    "analytic Cartesian stress/source identity": true,
    "analytic annulus no-slip trace": true,
    "analytic corner analytic gradient": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/index.json

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms-preview.png)

実際に保存した計算配列と固定入力の収束指標から描いた検証図。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/attempts/01/source/inputs.json

## 出典と確認範囲

- MFEM developers (n.d.). Example2: Linear Elasticity. https://mfem.org/examples/; review_level=selected-official-equations

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Annular variable-viscosity vector PDE MMS

Actually solve variable-viscosity stress divergence on an annulus; check velocity, strain, physical traction and work.

**Methods used**

- [Q1 FEM for mapped-coordinate vector BVP](https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=en) (`q1-fem`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en#annular-viscous-mms-en-algorithm)

Mapped polar Q1 with two Cartesian velocity components;4×4 Gauss integration of2mu epsilon uses exact r dr dtheta metric, followed by a block sparse solve. Circular traction uses r dtheta and outward normals.

$$
-\nabla\cdot(2\mu\epsilon(u))=f,\quad\mu=1+0.2r^2
$$

$$
\int 2\mu\epsilon(u):\epsilon(v)\,r\,dr\,d\theta=\int f\cdot v\,r\,dr\,d\theta
$$

$$
dS=r\,d\theta,\quad t=(2\mu\epsilon(u))n
$$

- [Variable-viscosity vector stress boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#variable-viscosity-vector-en) (`variable-viscosity-vector`)

1≤r≤2, periodic angle, mu=1+.2r², lambda0 and zero velocity on both circles. A(s)=(s−1)(4−s), u=(A(1+xy),A(x²−y²)/2). Nr8/16/32,Ntheta2Nr.


**Problem figure**

![Annular variable-viscosity vector PDE MMS: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Annular variable-viscosity vector PDE MMS](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en) (`annular-viscous-mms`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en#annular-viscous-mms-en-validation)

Qualify the derived force by separate Cartesian stress differentiation. Measure velocity/strain/traction refinement, reactions versus volume-force/physical traction budgets, and viscous dissipation versus force work. Also check the independently integrated body force (756pi/5,0).

- [Annular vector-viscous MMS: force qualified by independent stress differentiation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-annular-viscous-mms-en) (`annular-viscous-mms`; Same-problem reference · Manufactured solution)

A linear vector viscous BVP, without divergence-free constraint, pressure or nonlinear Navier–Stokes. r>0 only; no axis stencil certification.
## Assumptions, units and boundaries

1≤r≤2, periodic angle, mu=1+.2r², lambda0 and zero velocity on both circles. A(s)=(s−1)(4−s), u=(A(1+xy),A(x²−y²)/2). Nr8/16/32,Ntheta2Nr.

**Editorial clarification**

A linear vector viscous BVP, without divergence-free constraint, pressure or nonlinear Navier–Stokes. r>0 only; no axis stencil certification.

## Adopted numerical method

Mapped polar Q1 with two Cartesian velocity components;4×4 Gauss integration of2mu epsilon uses exact r dr dtheta metric, followed by a block sparse solve. Circular traction uses r dtheta and outward normals.

$$
-\nabla\cdot(2\mu\epsilon(u))=f,\quad\mu=1+0.2r^2
$$

$$
\int 2\mu\epsilon(u):\epsilon(v)\,r\,dr\,d\theta=\int f\cdot v\,r\,dr\,d\theta
$$

$$
dS=r\,d\theta,\quad t=(2\mu\epsilon(u))n
$$

## References and validation

Qualify the derived force by separate Cartesian stress differentiation. Measure velocity/strain/traction refinement, reactions versus volume-force/physical traction budgets, and viscous dissipation versus force work. Also check the independently integrated body force (756pi/5,0).

## Limits

A linear vector viscous BVP, without divergence-free constraint, pressure or nonlinear Navier–Stokes. r>0 only; no axis stencil certification.

## Stored measurements and decisions

```json
{
  "metrics": {
    "n": 32,
    "theta_cells": 64,
    "dofs": 3968,
    "relative_l2": 0.0022683900910951296,
    "relative_strain_l2": 0.05188955686190023,
    "relative_traction_l2": 0.07266006943162176,
    "residual": 1.0857981180834031e-13,
    "boundary_error": 0.0,
    "area_error": 3.552713678800501e-15,
    "reaction_balance": 1.736671818881876e-15,
    "traction_flux_balance": 0.042495559851796386,
    "exact_flux_balance": 5.984756355647655e-16,
    "analytic_force_error": 8.394500285269018e-16,
    "work_identity": 3.851517252670248e-15,
    "symmetry": 3.552713678800501e-15
  },
  "checks": {
    "annulus-n8 residual": true,
    "annulus-n8 boundary_error": true,
    "annulus-n8 area_error": true,
    "annulus-n8 reaction_balance": true,
    "annulus-n8 exact_flux_balance": true,
    "annulus-n8 analytic_force_error": true,
    "annulus-n8 work_identity": true,
    "annulus-n8 symmetry": true,
    "annulus-n16 residual": true,
    "annulus-n16 boundary_error": true,
    "annulus-n16 area_error": true,
    "annulus-n16 reaction_balance": true,
    "annulus-n16 exact_flux_balance": true,
    "annulus-n16 analytic_force_error": true,
    "annulus-n16 work_identity": true,
    "annulus-n16 symmetry": true,
    "annulus-n32 residual": true,
    "annulus-n32 boundary_error": true,
    "annulus-n32 area_error": true,
    "annulus-n32 reaction_balance": true,
    "annulus-n32 exact_flux_balance": true,
    "annulus-n32 analytic_force_error": true,
    "annulus-n32 work_identity": true,
    "annulus-n32 symmetry": true,
    "relative_l2 refinement 1": true,
    "relative_l2 refinement 2": true,
    "relative_strain_l2 refinement 1": true,
    "relative_strain_l2 refinement 2": true,
    "relative_traction_l2 refinement 1": true,
    "relative_traction_l2 refinement 2": true,
    "traction_flux_balance refinement 1": true,
    "traction_flux_balance refinement 2": true,
    "finest relative_l2": true,
    "finest relative_strain_l2": true,
    "finest relative_traction_l2": true,
    "finest traction_flux_balance": true,
    "analytic Cartesian stress/source identity": true,
    "analytic annulus no-slip trace": true,
    "analytic corner analytic gradient": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/index.json

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms-preview.png)

Validation preview from actual saved PDE arrays and fixed-input refinement measurements.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/attempts/01/source/inputs.json

## Sources and review scope

- MFEM developers (n.d.). Example2: Linear Elasticity. https://mfem.org/examples/; review_level=selected-official-equations

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
