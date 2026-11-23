# Barnes–Hut octree / Barnes–Hut八分木

Status: educational-example

Existing releases: Approximate isolated 3D particle gravity with an octree. The public example uses G=1 and a Plummer-softened kernel, with a monopole or the same kernel's full second-moment term, compared with direct summation. Additional fixed examples: Short-time32body dynamics from a cold Plummer-density sample. See each release for assumptions and checked scope.

既存配布版：孤立した3次元粒子の重力加速度をoctreeで近似する。公開例はG=1のPlummer軟化核に対し、質量単極子または同じ軟化核の完全な二次モーメント項を使い、直接和と比較する。 追加固定例：冷たいPlummer密度由来32粒子の短時間力学。条件と検証範囲は各配布版で確認してください。

Limits of existing releases: A static-force educational example without time integration, expansion, periodic images or FMM. theta is not a rigorous error bound, and order=2 need not improve every configuration. Targetwise approximation does not guarantee exact action–reaction/total-momentum conservation. Interaction counts are not timings or empirical complexity guarantees for every distribution. Additional fixed examples: Cold finite-N initial value,not an equilibrium Plummer DF or exact continuum orbit. No general BH reciprocity/global symplecticity claim.

Other names: Barnes Hut, Barnes-Hut法, バーンズ・ハット法, Barnes Hut tree, BH tree


## 条件と確認範囲 (ja)

problem: 正質量粒子の孤立・Plummer軟化Newton重力加速度。

variant: Barnes–Hut octree、幾何開角s/d、単極子または軟化核の完全二次モーメント。theta=0で全て開く。

use_when:
- 孤立境界で静的な力と開角・近似次数の関係を調べるとき。
- 同じ位置・質量・軟化長で直接和と照合するとき。

avoid_when:
- 周期系を孤立直接和とそのまま比較したい場合。
- 近接衝突の非軟化力や厳密な対称相互作用を必要とする場合。

assumptions [specified]:
- 位置は有限の(N,3)配列、質量は正かつ有限、粒子数は1以上。softening=ε>0、theta≥0、orderは0または2。
- 節点の一辺s=2×half、質量中心までの距離dについて s/d<theta なら受理する。ただし対象粒子を含むセルは必ず開き、葉では自己項を除く。
- 加速度核は −m r/(r²+ε²)^(3/2)。order=2はS=Σmδδᵀの完全なTaylor項を加え、軟化された核に必要なtrace(S)項も保持する。
粒子入力、Plummer核、受理基準と二次項をコードで確認した。

units [specified]:
無次元のG=1。位置と軟化長は同じ長さ単位、質量には一貫した単位を使う。長さL₀・質量M₀で次元を戻す場合、加速度の尺度はGM₀/L₀²。
G=1と位置・質量・軟化の共通規約を固定例でも確認した。

boundary_conditions [specified]:
孤立境界で周期像を加えない。軟化核のポテンシャル −Gm/√(r²+ε²) は無限遠で零となる規約。周期PM・Ewald・TreePMとは異なる境界問題。
周期像なしの孤立直接和とtreeを同じ核で比較する。

limitations [specified]:
既存配布版の制約：静的な力の教育例で、時間積分・宇宙膨張・周期境界・FMMを含まない。thetaは厳密な誤差上限ではなく、order=2がすべての配置で常に改善する保証もない。対象ごとの近似なので厳密な作用反作用・全運動量保存は保証せず、相互作用回数は実時間や全分布でのO(N log N)の実測ではない。 今回の追加固定例：冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。
固定静的例とターゲット別の近似に限定した。

Review: tree_acceleration/direct_acceleration、自己項・theta=0・選択配置の二次項・重複位置の既存検査、192粒子の固定入力・実行部・保存済み2検査の結果を読んだ。保存結果の再実行は行っていない。

Not checked:
- 原論文本文にある開角・多重極の全詳細。
- 動的軌道、全粒子分布の誤差上限、実時間性能の新しい計算。

Evidence:
- tree_acceleration, _build, direct_acceleration: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py
- fully-open direct comparison, selected second moment and coincident-particle tests: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py
- fixed static direct-versus-tree runner: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/run.py
- 192-particle isolated G=1, ε=0.03, theta=0.6, order=2: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/input.json
- stored fixed force comparison; two recorded checks: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/result.json

References:
- [original-method / primary-research] Barnes, J. & Hut, P. (1986). A hierarchical O(N log N) force-calculation algorithm. — https://doi.org/10.1038/324446a0
  立方体を八分割する階層的な力計算の出典。今回確認した抄録から、軟化核や二次モーメント式の細部まで確認済みとはしない。
  abstract-and-metadata (2026-11-22); Publisher abstract and bibliographic metadata returned by web search; full article body not reviewed.; https://www.nature.com/articles/324446a0

## Conditions and review scope (en)

problem: Isolated Plummer-softened Newtonian acceleration from positive-mass particles.

variant: Barnes–Hut octree with geometric s/d opening, monopole or full softened second moment; theta=0 fully opens the tree.

use_when:
- Studying static isolated-force error versus opening angle and expansion order.
- Comparing against direct summation with identical positions, masses and softening.

avoid_when:
- Direct comparison of a periodic problem to isolated direct summation.
- Unsoftened close encounters or strictly symmetric pair interactions.

assumptions [specified]:
- Positions are finite (N,3), masses positive and finite, and N≥1; ε=softening>0, theta≥0 and order is 0 or 2.
- A node is accepted when s/d<theta, with s=2×half and d measured to its center of mass. Target-containing cells are always opened; leaves exclude self terms.
- The acceleration kernel is −m r/(r²+ε²)^(3/2). order=2 adds the full Taylor term from S=Σmδδᵀ, retaining trace(S) for the softened kernel.
Checked particle inputs, Plummer kernel, acceptance and second-order term in code.

units [specified]:
Dimensionless G=1. Positions and softening share a length unit and masses use one consistent unit. With scales L₀,M₀, acceleration is restored with GM₀/L₀².
Checked G=1 and common position/mass/softening conventions in the fixed example.

boundary_conditions [specified]:
Isolated boundaries without periodic images; the softened potential −Gm/√(r²+ε²) tends to zero at infinity. This is a different boundary problem from periodic PM, Ewald or TreePM.
The tree and isolated direct sum use the same kernel without periodic images.

limitations [specified]:
Limits of existing releases: A static-force educational example without time integration, expansion, periodic images or FMM. theta is not a rigorous error bound, and order=2 need not improve every configuration. Targetwise approximation does not guarantee exact action–reaction/total-momentum conservation. Interaction counts are not timings or empirical complexity guarantees for every distribution. Additional fixed examples: Cold finite-N initial value,not an equilibrium Plummer DF or exact continuum orbit. No general BH reciprocity/global symplecticity claim.
Scoped to static cases and targetwise approximation.

Review: Inspected tree_acceleration/direct_acceleration, existing self-exclusion/fully-open/selected second-moment/coincident-particle tests, and the 192-particle fixed input, runner and stored two-check result; no rerun.

Not checked:
- All original-paper opening/multipole details beyond the reviewed abstract.
- New trajectory, all-distribution error-bound or wall-clock performance calculations.

Evidence:
- tree_acceleration, _build, direct_acceleration: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py
- fully-open direct comparison, selected second moment and coincident-particle tests: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py
- fixed static direct-versus-tree runner: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/run.py
- 192-particle isolated G=1, ε=0.03, theta=0.6, order=2: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/input.json
- stored fixed force comparison; two recorded checks: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/result.json

References:
- [original-method / primary-research] Barnes, J. & Hut, P. (1986). A hierarchical O(N log N) force-calculation algorithm. — https://doi.org/10.1038/324446a0
  Supports hierarchical octree force evaluation; the reviewed abstract does not establish the atlas's softened second-moment formula.
  abstract-and-metadata (2026-11-22); Publisher abstract and bibliographic metadata returned by web search; full article body not reviewed.; https://www.nature.com/articles/324446a0


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py

- Reference: https://doi.org/10.1038/324446a0 — Octree hierarchical force evaluation; does not by itself document the atlas's full second-moment expansion of a Plummer-softened kernel.

## Small fixed-input validation supplements

Additional fixed examples: Short-time32body dynamics from a cold Plummer-density sample. See each release for assumptions and checked scope.

追加固定例：冷たいPlummer密度由来32粒子の短時間力学。条件と検証範囲は各配布版で確認してください。

- Short-time32body dynamics from a cold Plummer-density sample: https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/result.json

Common execution records: [{"id": "barnes-hut", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#barnes-hut-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#barnes-hut-en"}}, {"id": "gravity-plummer-short", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en"}, "kind": "dedicated-supplement"}]

Runnable example:

{
  "input": "https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/input.json",
  "runner": "https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/run.py",
  "reference": "https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/result.json",
  "forces": "https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/forces.csv",
  "command": "python examples/barnes-hut/run.py --input examples/barnes-hut/input.json --output output-barnes-hut",
  "working_directory": "Extracted code edition directory"
}

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja) (`particle-gravity`; isolated-particles, gravity-plummer-short)

#### 問題の図 (`method-problems-ja`)

##### [孤立粒子群の軟化重力（ツリー・直接和）](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=ja) (`isolated-particles`)

![保存済みツリー力と直接和の相対誤差。開き角・展開次数を比較。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isolated-particles.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=ja#code-ja)

- [Barnes–Hut：192粒子と直接和の比較](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/barnes-hut/?lang=ja) (`barnes-hut`) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

孤立・軟化重力の静的な力の比較。軌道計算・周期系・実行速度の比較ではありません。

##### [冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja) (`gravity-plummer-short`)

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short-preview.png)

直接KDK20/40/80steps、最細でtheta0/.35/.6のfull second-moment BH。独立scalar対力+DOP853を2許容値で資格確認。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja#code-ja)

- [冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja) (`gravity-plummer-short`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

同じ軟化有限N ODEで時間誤差と木近似誤差を分け、独立DOP853・直接力と収支を比較。


#### 厳密解・参照解 (`method-references-ja`)

##### [孤立粒子群の軟化重力（ツリー・直接和）](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=ja#references-ja) (`isolated-particles`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja#references-ja) (`gravity-plummer-short`)

- [冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-plummer-short-ja) (`gravity-plummer-short`; 同じ問題の参照; 有限格子の数値参照)

冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja#gravity-plummer-short-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Barnes–Hut：192粒子と直接和の比較 (`barnes-hut`)

[孤立粒子群の軟化重力（ツリー・直接和）](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/barnes-hut/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/input.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

孤立・軟化重力の静的な力の比較。軌道計算・周期系・実行速度の比較ではありません。

##### 冷たいPlummer密度由来32粒子の短時間力学 (`gravity-plummer-short`)

[冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json)

同じ軟化有限N ODEで時間誤差と木近似誤差を分け、独立DOP853・直接力と収支を比較。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

追加固定例：冷たいPlummer密度由来32粒子の短時間力学。条件と検証範囲は各配布版で確認してください。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/run.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/dynamics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/dynamics.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/references/exact.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/experiments.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/protocol.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/protocol.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/test_dynamics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/test_dynamics.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_particle_gravity.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en) (`particle-gravity`; isolated-particles, gravity-plummer-short)

#### Problem figures (`method-problems-en`)

##### [Isolated softened particle gravity: tree versus direct sum](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=en) (`isolated-particles`)

![Stored relative tree/direct-sum force errors versus opening angle and expansion order.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isolated-particles.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=en#code-en)

- [Barnes–Hut: 192 particles against direct summation](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/barnes-hut/?lang=en) (`barnes-hut`) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Static isolated softened-gravity force comparison, not orbital integration, periodic gravity or a timing benchmark.

##### [Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en) (`gravity-plummer-short`)

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short-preview.png)

Direct KDK20/40/80steps; finest-dt full second-moment BHtheta0/.35/.6; qualify independent scalar-pair DOP853 at two tolerances.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en#code-en)

- [Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en) (`gravity-plummer-short`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

Separate time and tree-force errors for the same softened finite-N ODE with independent DOP853/direct-force references and budgets.


#### Exact / reference solutions (`method-references-en`)

##### [Isolated softened particle gravity: tree versus direct sum](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=en#references-en) (`isolated-particles`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en#references-en) (`gravity-plummer-short`)

- [Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-plummer-short-en) (`gravity-plummer-short`; Same-problem reference; Finite-grid numerical reference)

Cold finite-N initial value,not an equilibrium Plummer DF or exact continuum orbit. No general BH reciprocity/global symplecticity claim.

[Existing reference profile](/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en#gravity-plummer-short-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Barnes–Hut: 192 particles against direct summation (`barnes-hut`)

[Isolated softened particle gravity: tree versus direct sum](https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/barnes-hut/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/input.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Static isolated softened-gravity force comparison, not orbital integration, periodic gravity or a timing benchmark.

##### Short-time32body dynamics from a cold Plummer-density sample (`gravity-plummer-short`)

[Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json)

Separate time and tree-force errors for the same softened finite-N ODE with independent DOP853/direct-force references and budgets.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Additional fixed examples: Short-time32body dynamics from a cold Plummer-density sample. See each release for assumptions and checked scope.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/particle_gravity.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/run.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/dynamics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/dynamics.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/references/exact.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/experiments.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/protocol.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/protocol.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_particle_gravity.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/test_dynamics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/test_dynamics.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_particle_gravity.py
```
