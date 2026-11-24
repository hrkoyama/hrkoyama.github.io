# RATTLE constrained integration / RATTLE拘束積分

Status: educational-example

A Verlet-type discrete map enforces position and velocity constraints. Newton residuals, time reversal and time-discretization error are measured separately.

位置と速度の拘束をVerlet型の段階で満たす離散写像です。Newton残差、時間反転、時間離散誤差を分けて測ります。

Geometric structure concerns the map on the constraint manifold. This does not imply exact energy conservation or a guarantee for arbitrary constraints and solver tolerances. Numerical Jacobians provide a limited diagnostic.

Other names: RATTLE, RATTLE algorithm

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/symplectic/



- Reference: https://www.unige.ch/~hairer/poly-sde-mani.pdf — Author-hosted lecture notes, selected printed page50, SectionV.5, equations5.1–5.3 and Theorem5.1 statement, rendered and visually read. Centered SHAKE momentum and RATTLE final tangency are explicit. The original1977 SHAKE and1983 RATTLE articles remain full-text unread; no full proof review is claimed. Source date: 2011 (date displayed on lecture notes); this is not asserted as the publication year.
- Reference: https://www.unige.ch/~hairer/poly_geoint/week2.pdf — Author-hosted course notes, selected rendered printed pages2,12–13: Verlet kick/drift form, symplectic statement, Lie and symmetric Strang compositions. This does not qualify every state-dependent step rule or the authored coupled resonance experiment. Source date: 2010 (displayed course date); this is not asserted as the publication year.
- Reference: https://dlmf.nist.gov/22.4 — Official Table22.4.1 selected real periods: sn and cn have4K, dn has2K. Version date is not an initial publication date. Common-period reduction and direct-library periodicity qualification are separate from the independent angular DOP853 state comparison. Source date: 2026 (version); this is not asserted as the publication year.

## Small fixed-input validation supplements

Additional fixed examples: SHAKE and RATTLE: constraints and momentum ownership. See each release for assumptions and checked scope. Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency.

追加固定例：SHAKEとRATTLE：拘束と運動量の違い。条件と検証範囲は各配布版で確認してください。 原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。

- SHAKE and RATTLE: constraints and momentum ownership: https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json

Common execution records: [{"id": "shake-rattle-pendulum", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/rattle/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [拘束付き平面振り子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#constrained-pendulum-ja) (`constrained-pendulum`; high-index-pendulum)
- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`; high-index-pendulum)

#### 問題の図 (`method-problems-ja`)

##### [拘束付き振り子](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja) (`high-index-pendulum`)

![位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。 保存配列から作図。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png)

指数低減ODEと臨界拘束誤差拡張を固定RK4で積分し、拘束仕事も同じ段で積分します。 独自のスカラーNewton位置拘束、RATTLE終端接線impulse、SHAKE位置対。SHAKEの運動量は内部点だけで中心化し、端点を作りません。 SHAKEのsolves列はeta、eta/h^2、位置残差、Newton更新数です。列1は一律にeta/h^2ですが、初回半刻みの物理乗数は2eta/h^2、以後の位置Verletではeta/h^2です。逆位置対はすべて後者です。判定と図はこの列1を使いません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#code-ja)

- [SHAKEとRATTLE：拘束と運動量の違い](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja) (`shake-rattle-pendulum`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

単振り子の10固定軌道で、位置拘束、全時刻の接線運動量と内部点の中心化運動量を区別します。


#### 厳密解・参照解 (`method-references-ja`)

##### [拘束付き振り子](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#references-ja) (`high-index-pendulum`)

- [振り子の指数低減・拘束ドリフト・明示安定化](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-high-index-pendulum-ja) (`high-index-pendulum`; 同じ問題の参照; 半解析参照)

投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。

[既存の参照図](/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja#high-index-pendulum-ja-measurements)

- [SHAKEとRATTLE：拘束と運動量の違い](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shake-rattle-pendulum-ja) (`shake-rattle-pendulum`; 同じ問題の参照; 半解析参照)

原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。

[既存の参照図](/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja#shake-rattle-pendulum-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### SHAKEとRATTLE：拘束と運動量の違い (`shake-rattle-pendulum`)

[拘束付き振り子](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)

単振り子の10固定軌道で、位置拘束、全時刻の接線運動量と内部点の中心化運動量を区別します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-24/geometric-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/run.py)
- [/code/validated-examples/2026-11-24/geometric-controls/physics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/physics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py)
- [/code/validated-examples/2026-11-24/geometric-controls/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/io_utils.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/qualify.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#constrained-pendulum-en) (`constrained-pendulum`; high-index-pendulum)
- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`; high-index-pendulum)

#### Problem figures (`method-problems-en`)

##### [Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en) (`high-index-pendulum`)

![Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts. Drawn from saved arrays. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png)

Advance the index-reduced ODE and a critical constraint-error extension with fixed RK4, integrating constraint work at the same stages. Original scalar Newton position constraints, RATTLE final tangent impulses and SHAKE position pairs. SHAKE momentum is centered only at interior nodes; endpoint momenta are absent. SHAKE solves columns are eta, eta/h^2, position residual and Newton updates. Column1 uses the uniform recurrence normalization eta/h^2. For the first constrained half-step startup, the physical multiplier is 2*eta/h^2; later full position-Verlet steps use eta/h^2. Reverse-pair steps all use the later recurrence convention. RATTLE has its separate five-column normalization. No scientific gate or plot uses SHAKE column1.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#code-en)

- [SHAKE and RATTLE: constraints and momentum ownership](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en) (`shake-rattle-pendulum`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

Ten fixed pendulum evolutions distinguish position constraints, full-time tangent momentum and interior centered momentum.


#### Exact / reference solutions (`method-references-en`)

##### [Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#references-en) (`high-index-pendulum`)

- [Index reduction, constraint drift and explicit stabilization for a pendulum](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-high-index-pendulum-en) (`high-index-pendulum`; Same-problem reference; Semi-analytic reference)

No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.

[Existing reference profile](/numerical-methods-atlas/validation/high-index-pendulum/?lang=en#high-index-pendulum-en-measurements)

- [SHAKE and RATTLE: constraints and momentum ownership](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shake-rattle-pendulum-en) (`shake-rattle-pendulum`; Same-problem reference; Semi-analytic reference)

Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency.

[Existing reference profile](/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en#shake-rattle-pendulum-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/symplectic/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### SHAKE and RATTLE: constraints and momentum ownership (`shake-rattle-pendulum`)

[Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)

Ten fixed pendulum evolutions distinguish position constraints, full-time tangent momentum and interior centered momentum.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)

###### Related source

- [/code/validated-examples/2026-11-24/geometric-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/run.py)
- [/code/validated-examples/2026-11-24/geometric-controls/physics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/physics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py)
- [/code/validated-examples/2026-11-24/geometric-controls/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/io_utils.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/qualify.py)

###### Package tests

- [/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
