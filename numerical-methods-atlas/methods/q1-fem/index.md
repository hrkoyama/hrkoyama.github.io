# Q1 FEM for mapped-coordinate vector BVP / Q1有限要素法（曲線座標ベクトルBVP）

Status: educational-example

Approximate two Cartesian velocity components with bilinear(r,theta) basis functions for an annular variable-viscosity stress BVP. Assemble the exact polar Jacobian,physical gradients and coupled strain weak form.

極座標(r,θ)の双線形基底でCartesian速度2成分を近似し、円環の可変粘性応力発散BVPを解く。正確なrのJacobian、物理勾配、結合したひずみ弱形式を組み立てる。

Mapped Q1 vector BVP on this annulus only; not P1,general quadrilaterals,an r0 axis,pressure/incompressibility or nonlinear Navier–Stokes. FixedNr8/16/32,Ntheta2Nr checks are not broad certification.

Other names: Q1 FEM, bilinear finite elements, 双線形有限要素法, mapped Q1, Q1有限要素法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mesh-boundary/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mesh-boundary/



- Reference: https://mfem.org/examples/ — Example2 stress sigma=lambda div(u)I+mu(grad(u)+grad(u)^T), weak formulation and traction conventions inspected. Use lambda0 as a linear vector viscous BVP; manufactured fields are derived here. MFEM not executed or copied.

## Small fixed-input validation supplements

Mapped polarQ1 couples both Cartesian components of variable-viscosity stress. Fixed cases check exact curved geometry,inner/outer physical traction,nonzero net force,work and MMS errors.

円環の極座標Q1でCartesian2成分の可変粘性応力を結合。正確な曲線Jacobian、内外の物理牽引力、非零全境界力、仕事と製造解誤差を固定入力で比較します。

- Annular variable-viscosity vector PDE MMS: https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json

Common execution records: [{"id": "annular-viscous-mms", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [可変粘性のベクトル応力境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#variable-viscosity-vector-ja) (`variable-viscosity-vector`; annular-viscous-mms)

#### 問題の図 (`method-problems-ja`)

##### [環状領域の可変粘性・真2DベクトルMMS](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja) (`annular-viscous-mms`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms-preview.png)

polarのmapped Q1にCartesian速度2成分を置き、r dr dthetaで2mu epsilonの弱形式を4×4 Gauss積分してblock疎解法。円周faceにはr dthetaと外向き法線を使う。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja#code-ja)

- [環状領域の可変粘性・真2DベクトルMMS](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja) (`annular-viscous-mms`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

軸を除く円環で可変粘性の応力発散方程式を実際に解き、速度・歪み・境界tractionと仕事を照合します。


#### 厳密解・参照解 (`method-references-ja`)

##### [環状領域の可変粘性・真2DベクトルMMS](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja#references-ja) (`annular-viscous-mms`)

- [環状粘性ベクトルMMS：独立応力微分で外力を確認](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-annular-viscous-mms-ja) (`annular-viscous-mms`; 同じ問題の参照; 製造解)

線形vector粘性BVPです。divfree拘束・圧力・非線形Navier–Stokesは含めません。原点なしのr>0であり、軸stencil検証ではありません。

[既存の参照図](/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja#annular-viscous-mms-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mesh-boundary/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 環状領域の可変粘性・真2DベクトルMMS (`annular-viscous-mms`)

[環状領域の可変粘性・真2DベクトルMMS](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

軸を除く円環で可変粘性の応力発散方程式を実際に解き、速度・歪み・境界tractionと仕事を照合します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

円環の極座標Q1でCartesian2成分の可変粘性応力を結合。正確な曲線Jacobian、内外の物理牽引力、非零全境界力、仕事と製造解誤差を固定入力で比較します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-23/mesh-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/run.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/annulus.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/annulus.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/fem.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/boundary.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/experiments.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Variable-viscosity vector stress boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#variable-viscosity-vector-en) (`variable-viscosity-vector`; annular-viscous-mms)

#### Problem figures (`method-problems-en`)

##### [Annular variable-viscosity vector PDE MMS](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en) (`annular-viscous-mms`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms-preview.png)

Mapped polar Q1 with two Cartesian velocity components;4×4 Gauss integration of2mu epsilon uses exact r dr dtheta metric, followed by a block sparse solve. Circular traction uses r dtheta and outward normals.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en#code-en)

- [Annular variable-viscosity vector PDE MMS](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en) (`annular-viscous-mms`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

Actually solve variable-viscosity stress divergence on an annulus; check velocity, strain, physical traction and work.


#### Exact / reference solutions (`method-references-en`)

##### [Annular variable-viscosity vector PDE MMS](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en#references-en) (`annular-viscous-mms`)

- [Annular vector-viscous MMS: force qualified by independent stress differentiation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-annular-viscous-mms-en) (`annular-viscous-mms`; Same-problem reference; Manufactured solution)

A linear vector viscous BVP, without divergence-free constraint, pressure or nonlinear Navier–Stokes. r>0 only; no axis stencil certification.

[Existing reference profile](/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en#annular-viscous-mms-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mesh-boundary/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Annular variable-viscosity vector PDE MMS (`annular-viscous-mms`)

[Annular variable-viscosity vector PDE MMS](https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

Actually solve variable-viscosity stress divergence on an annulus; check velocity, strain, physical traction and work.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Mapped polarQ1 couples both Cartesian components of variable-viscosity stress. Fixed cases check exact curved geometry,inner/outer physical traction,nonzero net force,work and MMS errors.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

###### Related source

- [/code/validated-examples/2026-11-23/mesh-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/run.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/annulus.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/annulus.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/fem.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/boundary.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/experiments.py)

###### Package tests

- [/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
