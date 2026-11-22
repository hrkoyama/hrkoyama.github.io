# Velocity Verlet / particle leapfrog / 速度Verlet／粒子leapfrog法

Status: educational-example

A second-order reversible symplectic method using half kick, drift and half kick for position-dependent forces. Released unit-mass harmonic/quartic oscillators illustrate why energy error and geometric structure preservation are different properties.

位置だけに依存する力を、半分のkick・drift・半分のkickで進める2次の可逆・シンプレクティック法。公開例は単位質量の調和/四次振動子で、エネルギー誤差と構造保存が同じでないことを確かめる。

The original Hamiltonian is not exactly preserved at each step. A symplectic map can still be unstable at large steps; for the ω=1 harmonic oscillator, |h|<2 is the interior stability interval. Velocity-dependent forces, friction/thermostats, constraints, generic variable steps and nonseparable Hamiltonians require different treatment. This function is not a general molecular-dynamics solver.

Other names: Verlet法, ベルレ法, 速度ベルレ法, velocity Verlet, particle leapfrog


## 条件と確認範囲 (ja)

problem: 位置依存ポテンシャルを持つHamilton系の軌道と長時間の幾何学的挙動。

variant: hamiltonian._verletのkick–drift–kick（velocity-Verlet形）。公開の対象は単位質量の1次元調和・四次振動子で、Verlet原報の位置漸化式とは表現を区別する。

use_when:
- 固定刻みで、分離Hamiltonianの可逆性・シンプレクティック性とエネルギー誤差を比較したい。
- 位置依存力の時間尺度を解像できる振動子の教材例が欲しい。

avoid_when:
- 速度依存力や摩擦、拘束を追加しても同じ構造保存が自動的に成り立つと期待する。
- 任意質量・多粒子系や適応刻みの汎用実装を必要とする。

assumptions [specified]:
- 公開例は1自由度、単位質量の自律・分離Hamiltonian H(q,p)=p²/2+V(q)。V=q²/2またはq²/2+q⁴/4。
- 力は−V'(q)で位置のみに依存する。p_half=p−h V'(q)/2、q_new=q+h p_half、p_new=p_half−h V'(q_new)/2を用いる。
- 可逆性とシンプレクティック性の説明は固定刻みの同じ写像に対するもの。精度と安定性のため力学的時間尺度を解像する。
_gradient・_verletと選択できる2ポテンシャルを確認。

units [specified]:
公開振動子は質量m=1、調和角振動数ω=1に無次元化している。一般の質量に転用する場合はdriftをh p/mとし、q・p・力・時間の尺度を整合させる必要があるが、その一般化はこの公開関数の入力では提供しない。
driftの係数1とポテンシャルからm=ω=1の尺度を明示。

boundary_conditions [not-applicable]:
この振動子の位相空間写像に空間境界条件は該当しない。原報の周期Lennard–Jones流体とは別の問題であり、粒子の周期境界や壁・拘束はこの実装にない。
有限次元の振動子写像で境界の入力はない。

limitations [specified]:
元のHamiltonianを各ステップで厳密保存するわけではない。シンプレクティックでも大刻みは不安定になり得て、ω=1の調和振動子では|h|<2が安定域の内部。速度依存力、摩擦・サーモスタット、拘束、一般の可変刻みや非分離Hamiltonianでは、同じ性質をそのまま保証できない。公開関数は一般分子動力学solverではない。
エネルギー誤差、写像の構造、刻みの安定性を分離。

Review: hamiltonian.pyの_gradient・_verlet・canonical_step・trajectoryを読んだ。既存test_hamiltonian.pyの2次収束、Jacobianのシンプレクティック条件、逆時間、元エネルギーの非厳密保存、大刻み不安定を確認。今回の再実行なし。

Not checked:
- 原報のLennard–Jones流体の再現、velocity-Verlet表現の歴史的優先権。
- 新しい数値実行、多粒子・拘束・速度依存力・適応刻み。

Evidence:
- _gradient; _verlet; canonical_step; trajectory; energy: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py
- test_canonical_oscillator_refinement_order; test_map_jacobians_against_independent_differences_and_symplectic_form; test_symmetric_maps_reverse_fixed_steps_for_nonlinear_system; test_energy_is_distinct_from_symplecticity; test_large_step_can_be_symplectic_and_unstable: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py

References:
- [original-method / primary-research] Verlet (1967). Computer “Experiments” on Classical Fluids. I. Thermodynamical Properties of Lennard-Jones Molecules. — https://doi.org/10.1103/PhysRev.159.98
  原報の位置Verlet漸化式を本文で確認。本サイトは単位質量の振動子に対するkick–drift–kick形であり、原報のLennard–Jones流体を再現する実装ではない。
  full-text (2026-11-22); Section II, p. 99, equation (4); relevant integration passage read.; https://journals.aps.org/pr/pdf/10.1103/PhysRev.159.98
- [formulation / primary-research] Hairer, Lubich & Wanner (2003). Geometric numerical integration illustrated by the Störmer–Verlet method. — https://doi.org/10.1017/S0962492902000144
  可逆性・シンプレクティック性と長時間挙動を整理する研究論文。抄録確認に限り、多様体・拘束系への拡張を本実装の機能とはしない。
  abstract-and-metadata (2026-11-22); Publisher abstract and metadata; author-hosted PDF was inaccessible.; https://www.cambridge.org/core/journals/acta-numerica/article/abs/geometric-numerical-integration-illustrated-by-the-stormerverlet-method/E55395D5DD7A4E0526D10EA74DA6C46B

## Conditions and review scope (en)

problem: Trajectories and long-time geometric behaviour of Hamiltonian systems with a position-dependent potential.

variant: Kick–drift–kick (velocity-Verlet form) in hamiltonian._verlet, restricted to unit-mass one-dimensional harmonic/quartic oscillators; distinguished from the original paper's position recurrence.

use_when:
- Compare fixed-step reversibility/symplecticity with energy error for a separable Hamiltonian.
- An oscillator teaching example with resolved position-dependent-force time scales is useful.

avoid_when:
- The same geometric guarantees are expected to survive added velocity forces, friction or constraints automatically.
- A general-mass, many-particle or adaptive-step implementation is required.

assumptions [specified]:
- The released example is an autonomous separable one-degree-of-freedom Hamiltonian H(q,p)=p²/2+V(q) with unit mass and V=q²/2 or q²/2+q⁴/4.
- The force is −V'(q), depending only on position. The update is p_half=p−h V'(q)/2, q_new=q+h p_half, p_new=p_half−h V'(q_new)/2.
- Reversibility and symplecticity refer to the same fixed-step map. Dynamical time scales must still be resolved for accuracy and stability.
Inspected _gradient, _verlet and both supported potentials.

units [specified]:
The released oscillator is nondimensional with m=1 and harmonic ω=1. A general-mass formulation would require drift h p/m and consistent position, momentum, force and time scales; that generalization is not an input feature of this released function.
Unit mass/frequency follow from the drift coefficient and potential.

boundary_conditions [not-applicable]:
Spatial boundary conditions do not apply to this oscillator phase-space map. It is a different problem from the original periodic Lennard-Jones fluid; particle periodicity, walls and constraints are not implemented here.
The finite-dimensional oscillator map has no boundary input.

limitations [specified]:
The original Hamiltonian is not exactly preserved at each step. A symplectic map can still be unstable at large steps; for the ω=1 harmonic oscillator, |h|<2 is the interior stability interval. Velocity-dependent forces, friction/thermostats, constraints, generic variable steps and nonseparable Hamiltonians require different treatment. This function is not a general molecular-dynamics solver.
Separates energy error, map geometry and step stability.

Review: Read _gradient, _verlet, canonical_step and trajectory in hamiltonian.py. Inspected existing tests for second-order convergence, the Jacobian symplectic condition, time reversal, non-exact original energy conservation and large-step instability. No rerun was performed.

Not checked:
- Reproduction of the original Lennard-Jones fluid or historical priority of the velocity-Verlet representation.
- New numerical runs, many-particle systems, constraints, velocity-dependent forces or adaptive steps.

Evidence:
- _gradient; _verlet; canonical_step; trajectory; energy: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py
- test_canonical_oscillator_refinement_order; test_map_jacobians_against_independent_differences_and_symplectic_form; test_symmetric_maps_reverse_fixed_steps_for_nonlinear_system; test_energy_is_distinct_from_symplecticity; test_large_step_can_be_symplectic_and_unstable: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py

References:
- [original-method / primary-research] Verlet (1967). Computer “Experiments” on Classical Fluids. I. Thermodynamical Properties of Lennard-Jones Molecules. — https://doi.org/10.1103/PhysRev.159.98
  The original position recurrence was inspected. The atlas adopts a kick–drift–kick oscillator form and does not reproduce the paper's Lennard-Jones experiment.
  full-text (2026-11-22); Section II, p. 99, equation (4); relevant integration passage read.; https://journals.aps.org/pr/pdf/10.1103/PhysRev.159.98
- [formulation / primary-research] Hairer, Lubich & Wanner (2003). Geometric numerical integration illustrated by the Störmer–Verlet method. — https://doi.org/10.1017/S0962492902000144
  Research treatment of geometric and long-time properties. Only the abstract was checked; its manifold and constrained-system extensions are outside the local implementation.
  abstract-and-metadata (2026-11-22); Publisher abstract and metadata; author-hosted PDF was inaccessible.; https://www.cambridge.org/core/journals/acta-numerica/article/abs/geometric-numerical-integration-illustrated-by-the-stormerverlet-method/E55395D5DD7A4E0526D10EA74DA6C46B


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/symplectic/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py

- Reference: https://doi.org/10.1103/PhysRev.159.98 — Original position-Verlet recurrence in molecular dynamics. The atlas implements its kick–drift–kick phase-space form for a unit-mass oscillator, not the paper's Lennard-Jones simulation.
- Reference: https://doi.org/10.1017/S0962492902000144 — Research exposition of the method's reversibility, symplecticity and long-time behaviour; no claim that all constrained/manifold extensions are implemented.

Common execution records: [{"id": "harmonic-oscillator", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#harmonic-oscillator-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#harmonic-oscillator-en"}}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`; harmonic-oscillator, quartic-oscillator)

#### 問題の図 (`method-problems-ja`)

##### [調和振動子（複素ODE表示も統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=ja) (`harmonic-oscillator`)

![保存済みのt≤10の正準位相軌道。手法違いは同一問題の比較。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/harmonic-oscillator.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=ja#code-ja)

- [調和振動子：Verletの位相誤差とエネルギー](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=ja) (`harmonic-oscillator`) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

既存の単位質量・単位角振動数の調和振動子をvelocity Verletで進める。20時間単位、200/400/800刻みの解析解比較、元のエネルギー偏差、時間反転を出力。

##### [4次ポテンシャルの非線形振動子](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja) (`quartic-oscillator`)

![保存済みのt≤10の正準位相軌道。手法違いは同一問題の比較。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/quartic-oscillator.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。


#### 厳密解・参照解 (`method-references-ja`)

##### [調和振動子（複素ODE表示も統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=ja#references-ja) (`harmonic-oscillator`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [4次ポテンシャルの非線形振動子](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja#references-ja) (`quartic-oscillator`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 調和振動子：Verletの位相誤差とエネルギー (`harmonic-oscillator`)

[調和振動子（複素ODE表示も統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/harmonic-oscillator.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

既存の単位質量・単位角振動数の調和振動子をvelocity Verletで進める。20時間単位、200/400/800刻みの解析解比較、元のエネルギー偏差、時間反転を出力。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_hamiltonian.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`; harmonic-oscillator, quartic-oscillator)

#### Problem figures (`method-problems-en`)

##### [Harmonic oscillator, including complex-ODE form](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=en) (`harmonic-oscillator`)

![Stored canonical phase orbits for t≤10; methods remain variants of one problem.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/harmonic-oscillator.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=en#code-en)

- [Harmonic oscillator: Verlet phase error and energy](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=en) (`harmonic-oscillator`) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Advance the existing unit-mass, unit-frequency harmonic oscillator with velocity Verlet. Compare analytic states over 20 time units at 200/400/800 steps, original-energy deviation and reversal.

##### [Nonlinear quartic-potential oscillator](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en) (`quartic-oscillator`)

![Stored canonical phase orbits for t≤10; methods remain variants of one problem.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/quartic-oscillator.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.


#### Exact / reference solutions (`method-references-en`)

##### [Harmonic oscillator, including complex-ODE form](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=en#references-en) (`harmonic-oscillator`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Nonlinear quartic-potential oscillator](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en#references-en) (`quartic-oscillator`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/symplectic/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Harmonic oscillator: Verlet phase error and energy (`harmonic-oscillator`)

[Harmonic oscillator, including complex-ODE form](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/harmonic-oscillator.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Advance the existing unit-mass, unit-frequency harmonic oscillator with velocity Verlet. Compare analytic states over 20 time units at 200/400/800 steps, original-energy deviation and reversal.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_hamiltonian.py
```
