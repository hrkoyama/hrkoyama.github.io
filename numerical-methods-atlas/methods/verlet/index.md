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
