# Velocity Verlet / particle leapfrog / 速度Verlet／粒子leapfrog法

Status: educational-example

Existing releases: A second-order reversible symplectic method using half kick, drift and half kick for position-dependent forces. Released unit-mass harmonic/quartic oscillators illustrate why energy error and geometric structure preservation are different properties. Additional fixed examples: Unsoftened Kepler two-body time error, Short-time32body dynamics from a cold Plummer-density sample. See each release for assumptions and checked scope. Additional fixed examples: Warm PIC linear Landau damping, Warm PIC two-stream initial growth. See each release for assumptions and checked scope. Additional fixed examples: Independently coded PIC spatial pipeline. See each release for assumptions and checked scope. Additional fixed examples: Kepler eccentricity and time-step controls, Coupled frequencies and finite-window resonance. See each release for assumptions and checked scope.

既存配布版：位置だけに依存する力を、半分のkick・drift・半分のkickで進める2次の可逆・シンプレクティック法。公開例は単位質量の調和/四次振動子で、エネルギー誤差と構造保存が同じでないことを確かめる。 追加固定例：無軟化Kepler二体の時間誤差、冷たいPlummer密度由来32粒子の短時間力学。条件と検証範囲は各配布版で確認してください。 追加固定例：温かいPICの線形Landau減衰、温かいPICの二流初期成長。条件と検証範囲は各配布版で確認してください。 追加固定例：PIC空間演算の独立実装照合。条件と検証範囲は各配布版で確認してください。 追加固定例：離心率を変えたKepler軌道と時間刻み、結合した2周波数系と共鳴の有限窓。条件と検証範囲は各配布版で確認してください。

Limits of existing releases: The original Hamiltonian is not exactly preserved at each step. A symplectic map can still be unstable at large steps; for the ω=1 harmonic oscillator, |h|<2 is the interior stability interval. Velocity-dependent forces, friction/thermostats, constraints, generic variable steps and nonseparable Hamiltonians require different treatment. This function is not a general molecular-dynamics solver. Additional fixed examples: One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference. Cold finite-N initial value,not an equilibrium Plummer DF or exact continuum orbit. No general BH reciprocity/global symplecticity claim. Additional fixed examples: Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established. Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established. Additional fixed examples: Independent coding check of discrete spatial operators. It does not change the time integrator/continuum model, establish continuum convergence, or reproduce the cold-plasma oscillation reference. A related supplement of cold-plasma-pic; the finite warm velocity spread is explicit. The preceding limitations describe earlier editions. This additional release: Small invariant errors do not establish phase accuracy. No canonical symplectic-defect measurement is claimed for the variable-step map, and fixed-h properties are not transferred automatically. R1 resolution was revised to R2 using pre-execution asymptotic planning, not measured calibration. The central actual floating map remains unresolved; ideal-pi Jordan structure is not transferred to it. Results concern 64-step amplification and small fixed inputs, not a scanned resonance diagram, general stability or a universal long-time error theorem.

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
既存配布版の制約：元のHamiltonianを各ステップで厳密保存するわけではない。シンプレクティックでも大刻みは不安定になり得て、ω=1の調和振動子では|h|<2が安定域の内部。速度依存力、摩擦・サーモスタット、拘束、一般の可変刻みや非分離Hamiltonianでは、同じ性質をそのまま保証できない。公開関数は一般分子動力学solverではない。 今回の追加固定例：1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。 冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。 今回の追加固定例：1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。 1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。 今回の追加固定例：離散演算の独立したコーディング照合です。時間積分法や連続方程式を変えた独立エンジン、連続極限の収束、冷たいプラズマの振動参照の再現を意味しません。既存cold-plasma-picの関連補助検証として扱い、温かい初期速度の軌道を冷たい解と同一視しません。 上記の制限は既存配布版の範囲です。今回の追加配布版：保存量の小さい誤差から位相精度を推論しません。変動刻み写像の正準symplectic defectは測定せず、固定hの性質をそのまま移しません。初期解像度R1は数値実行前の漸近解析でR2へ改訂。 中心の実浮動係数写像はunresolvedとし、理想πのJordan性を移しません。64刻み増幅と小さい固定入力の観測であり、走査した共鳴図・一般安定性・長時間の普遍誤差定理は主張しません。
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
Limits of existing releases: The original Hamiltonian is not exactly preserved at each step. A symplectic map can still be unstable at large steps; for the ω=1 harmonic oscillator, |h|<2 is the interior stability interval. Velocity-dependent forces, friction/thermostats, constraints, generic variable steps and nonseparable Hamiltonians require different treatment. This function is not a general molecular-dynamics solver. Additional fixed examples: One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference. Cold finite-N initial value,not an equilibrium Plummer DF or exact continuum orbit. No general BH reciprocity/global symplecticity claim. Additional fixed examples: Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established. Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established. Additional fixed examples: Independent coding check of discrete spatial operators. It does not change the time integrator/continuum model, establish continuum convergence, or reproduce the cold-plasma oscillation reference. A related supplement of cold-plasma-pic; the finite warm velocity spread is explicit. The preceding limitations describe earlier editions. This additional release: Small invariant errors do not establish phase accuracy. No canonical symplectic-defect measurement is claimed for the variable-step map, and fixed-h properties are not transferred automatically. R1 resolution was revised to R2 using pre-execution asymptotic planning, not measured calibration. The central actual floating map remains unresolved; ideal-pi Jordan structure is not transferred to it. Results concern 64-step amplification and small fixed inputs, not a scanned resonance diagram, general stability or a universal long-time error theorem.
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

## Small fixed-input validation supplements

Additional fixed examples: Unsoftened Kepler two-body time error, Short-time32body dynamics from a cold Plummer-density sample. See each release for assumptions and checked scope. Additional fixed examples: Warm PIC linear Landau damping, Warm PIC two-stream initial growth. See each release for assumptions and checked scope. Additional fixed examples: Independently coded PIC spatial pipeline. See each release for assumptions and checked scope.

追加固定例：無軟化Kepler二体の時間誤差、冷たいPlummer密度由来32粒子の短時間力学。条件と検証範囲は各配布版で確認してください。 追加固定例：温かいPICの線形Landau減衰、温かいPICの二流初期成長。条件と検証範囲は各配布版で確認してください。 追加固定例：PIC空間演算の独立実装照合。条件と検証範囲は各配布版で確認してください。

- Unsoftened Kepler two-body time error: https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/
- Short-time32body dynamics from a cold Plummer-density sample: https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/result.json

- Warm PIC linear Landau damping: https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/
- Warm PIC two-stream initial growth: https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/result.json

- Independently coded PIC spatial pipeline: https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/results/result.json

- Kepler eccentricity and time-step controls: https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/
- Coupled frequencies and finite-window resonance: https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json

- A two-state BO / CP-type model with a short nuclear thermostat coupling: https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json

Common execution records: [{"id": "harmonic-oscillator", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#harmonic-oscillator-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#harmonic-oscillator-en"}}, {"id": "gravity-kepler", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "gravity-plummer-short", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "thermal-landau-damping", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "thermal-two-stream", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "pic-independent-spatial", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "kepler-eccentricity", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "multifrequency-resonance", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "two-state-bo-cp-ou", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`; harmonic-oscillator, quartic-oscillator, gravity-kepler, multifrequency-resonance)
- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; cold-plasma-pic)
- [静電Vlasov–Poisson方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#vlasov-poisson-ja) (`vlasov-poisson`; cold-plasma-pic, thermal-landau-damping, thermal-two-stream)
- [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja) (`particle-gravity`; gravity-kepler, gravity-plummer-short)
- [Kepler二体問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kepler-two-body-ja) (`kepler-two-body`; gravity-kepler)
- [二周波数の結合調和振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#coupled-harmonic-oscillators-ja) (`coupled-harmonic-oscillators`; multifrequency-resonance)
- [2準位電子角と核のBO/CP型模型](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#two-state-bo-cp-model-ja) (`two-state-bo-cp-model`; two-state-bo-cp-model)

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

##### [CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja) (`cold-plasma-pic`)

![1次元周期・振幅0.001の冷たい電子プラズマ。CIC静電PICの変位モードとcos(t)、別々の格子・時間刻み走査の保存誤差を表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#code-ja)

- [PIC空間演算の独立実装照合](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja) (`pic-independent-spatial`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip)

ベクトル化CIC/FFTと、別に書いた粒子ループCIC・密なDFTを、それぞれが自己無撞着な場を毎kick計算する軌道全体で照合します。

##### [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja) (`gravity-kepler`)

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

位置のみの力でkick半分→drift→kick半分。独立のbracketed Kepler rootと解析速度を使用。 独自の中心力KDK Verlet。固定・保存刻み再生・再生成刻みを区別し、cubic Hermite軌道の正の放射速度交差をbrentqで局在化。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja#code-ja)

- [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja) (`gravity-kepler`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

非等質量二体をKDKで1周し、独立Kepler方程式の位置・速度とエネルギー/角運動量を照合。

- [離心率を変えたKepler軌道と時間刻み](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja) (`kepler-eccentricity`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

e=0.1/0.7の16固定軌道で、保存量と同時刻の位相誤差、実際の近日点時刻と逆積分を比較します。

##### [冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja) (`gravity-plummer-short`)

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short-preview.png)

直接KDK20/40/80steps、最細でtheta0/.35/.6のfull second-moment BH。独立scalar対力+DOP853を2許容値で資格確認。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja#code-ja)

- [冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja) (`gravity-plummer-short`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

同じ軟化有限N ODEで時間誤差と木近似誤差を分け、独立DOP853・直接力と収支を比較。

##### [温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja) (`thermal-landau-damping`)

![実際に動かした粒子の初期(x,v)に対する速度変化δv/α。空間2D流体図ではなく1D1V位相空間の応答です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping-preview.png)

正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja#code-ja)

- [温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja) (`thermal-landau-damping`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

熱速度1のMaxwell分布を自己無撞着に動かし、減衰率・周波数・符号付き場の履歴を独立した線形参照で調べます。

##### [温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja) (`thermal-two-stream`)

![実粒子のT40での速度変化δv/αを初期(x,v)に表示。1D1V位相空間の後期診断で、成長率を検証する固定窓\[12,20\]とは分けます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream-preview.png)

正のGauss速度重みと密度CDF逆写像で共同(x,v)分布を作り、CIC電荷配置→FFT Poisson→同じCIC補間を各kickで再計算するvelocity-Verlet法。Z関数の分散根を枝追跡で確認し、別導出のVolterra初期値問題を刻み半減して固定窓の過渡偏りを検査します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja#code-ja)

- [温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja) (`thermal-two-stream`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

温度を持つ対向Maxwell二流を時間発展し、固定した線形窓の成長率と過渡を分散式・Volterra参照から分けて検査します。

##### [結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja) (`multifrequency-resonance`)

![保存した最細impulse軌道の実q1–q2座標と物理時刻。これは走査相図ではなく、結合した1軌道です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png)

全ポテンシャルVerletと、B半kick・A厳密flow・B半kickのStrang impulse。Aには高速調和振動子と低速自由流、Bには低速位置項と結合を含めます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja#code-ja)

- [結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja) (`multifrequency-resonance`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

2自由度の実結合系で、12の64刻みprobeと6の精度軌道を使い、真のモード、座標間交換、離散写像と丸めを分けます。

##### [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja) (`two-state-bo-cp-model`)

![電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。 長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png)

解析BO力とCP型作用の式をVerlet/BAOABで積分し、核熱と架空電子運動エネルギーを分けます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja#code-ja)

- [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja) (`two-state-bo-cp-ou`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [調和振動子（複素ODE表示も統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=ja#references-ja) (`harmonic-oscillator`)

- [調和振動子：Verletの位相誤差とエネルギー](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-harmonic-oscillator-exact-ja) (`harmonic-oscillator-exact`; 同じ問題の参照; 解析参照)

既存の固定入力・保存結果に対応する解析参照カードを追加。解析式、点・時刻・動径の標本化、配布版SHAと実行コードを相互に辿れます。過去の計算を再実行した記録ではありません。 既存ギャラリーはt≤10、共通固定入力は終端20です。

[既存の参照図](/numerical-methods-atlas/problems/harmonic-oscillator/?lang=ja)

##### [4次ポテンシャルの非線形振動子](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja#references-ja) (`quartic-oscillator`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#references-ja) (`cold-plasma-pic`)

- [PIC空間演算の独立実装照合](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pic-independent-spatial-ja) (`pic-independent-spatial`; 関連モデルの参照; 有限格子の数値参照)

周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。

[既存の参照図](/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja#pic-independent-spatial-ja-measurements)

##### [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja#references-ja) (`gravity-kepler`)

- [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-kepler-ja) (`gravity-kepler`; 同じ問題の参照; 解析参照)

1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。

[既存の参照図](/numerical-methods-atlas/validation/gravity-kepler/?lang=ja#gravity-kepler-ja-measurements)

- [離心率を変えたKepler軌道と時間刻み](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kepler-eccentricity-ja) (`kepler-eccentricity`; 同じ問題の参照; 半解析参照)

保存量の小さい誤差から位相精度を推論しません。変動刻み写像の正準symplectic defectは測定せず、固定hの性質をそのまま移しません。初期解像度R1は数値実行前の漸近解析でR2へ改訂。

[既存の参照図](/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja#kepler-eccentricity-ja-measurements)

##### [冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja#references-ja) (`gravity-plummer-short`)

- [冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-plummer-short-ja) (`gravity-plummer-short`; 同じ問題の参照; 有限格子の数値参照)

冷たい有限N初期値で平衡Plummer分布/連続球厳密軌道ではありません。BHの一般相反性・大域symplectic性は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja#gravity-plummer-short-ja-measurements)

##### [温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja#references-ja) (`thermal-landau-damping`)

- [温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-thermal-landau-damping-ja) (`thermal-landau-damping`; 同じ問題の参照; 半解析参照)

1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。

[既存の参照図](/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja#thermal-landau-damping-ja-measurements)

##### [温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja#references-ja) (`thermal-two-stream`)

- [温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-thermal-two-stream-ja) (`thermal-two-stream`; 同じ問題の参照; 半解析参照)

1D1V・固定イオン・無衝突の小規模例です。正のGauss速度重みのfull-f粒子を全て動かします。4シードのSEとt区間は静かな空間シフトに条件付けられ、i.i.d.粒子雑音やN^(-1/2)収束の証明ではありません。速度積分の偏りは別の倍増計算で検査。線形参照は独立した連続モデルの導出で、独立非線形Vlasovエンジンではありません。二流の後期は診断表示で飽和値を合否に用いません。偶数格子のNyquist電荷を別記し、そのモードまでGauss則を満たすとは表示しません。 4シフトのStudent-t区間は名目上の条件付き要約で、真の率に対する被覆率や全誤差を検証したものではありません。

[既存の参照図](/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja#thermal-two-stream-ja-measurements)

##### [結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja#references-ja) (`multifrequency-resonance`)

- [結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-multifrequency-resonance-ja) (`multifrequency-resonance`; 同じ問題の参照; 半解析参照)

中心の実浮動係数写像はunresolvedとし、理想πのJordan性を移しません。64刻み増幅と小さい固定入力の観測であり、走査した共鳴図・一般安定性・長時間の普遍誤差定理は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja#multifrequency-resonance-ja-measurements)

##### [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja#references-ja) (`two-state-bo-cp-model`)

- [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-two-state-bo-cp-ou-ja) (`two-state-bo-cp-ou`; 同じ問題の参照; 半解析参照)

長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。

[既存の参照図](/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja#two-state-bo-cp-ou-ja-measurements)

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

##### PIC空間演算の独立実装照合 (`pic-independent-spatial`)

[CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/verification.json)

ベクトル化CIC/FFTと、別に書いた粒子ループCIC・密なDFTを、それぞれが自己無撞着な場を毎kick計算する軌道全体で照合します。

##### 無軟化Kepler二体の時間誤差 (`gravity-kepler`)

[無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json)

非等質量二体をKDKで1周し、独立Kepler方程式の位置・速度とエネルギー/角運動量を照合。

##### 離心率を変えたKepler軌道と時間刻み (`kepler-eccentricity`)

[無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)

e=0.1/0.7の16固定軌道で、保存量と同時刻の位相誤差、実際の近日点時刻と逆積分を比較します。

##### 冷たいPlummer密度由来32粒子の短時間力学 (`gravity-plummer-short`)

[冷たいPlummer密度由来32粒子の短時間力学](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json)

同じ軟化有限N ODEで時間誤差と木近似誤差を分け、独立DOP853・直接力と収支を比較。

##### 温かいPICの線形Landau減衰 (`thermal-landau-damping`)

[温かいPICの線形Landau減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/verification.json)

熱速度1のMaxwell分布を自己無撞着に動かし、減衰率・周波数・符号付き場の履歴を独立した線形参照で調べます。

##### 温かいPICの二流初期成長 (`thermal-two-stream`)

[温かいPICの二流初期成長](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/verification.json)

温度を持つ対向Maxwell二流を時間発展し、固定した線形窓の成長率と過渡を分散式・Volterra参照から分けて検査します。

##### 結合した2周波数系と共鳴の有限窓 (`multifrequency-resonance`)

[結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)

2自由度の実結合系で、12の64刻みprobeと6の精度軌道を使い、真のモード、座標間交換、離散写像と丸めを分けます。

##### 2準位模型のBO/CP型連成と短い核熱浴 (`two-state-bo-cp-ou`)

[2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

追加固定例：無軟化Kepler二体の時間誤差、冷たいPlummer密度由来32粒子の短時間力学。条件と検証範囲は各配布版で確認してください。 追加固定例：温かいPICの線形Landau減衰、温かいPICの二流初期成長。条件と検証範囲は各配布版で確認してください。 追加固定例：PIC空間演算の独立実装照合。条件と検証範囲は各配布版で確認してください。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/run.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/dynamics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/dynamics.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/references/exact.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/experiments.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/protocol.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/protocol.py)
- [/code/validated-examples/2026-11-23/warm-pic/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/run.py)
- [/code/validated-examples/2026-11-23/warm-pic/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/primary.py)
- [/code/validated-examples/2026-11-23/warm-pic/loading.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/loading.py)
- [/code/validated-examples/2026-11-23/warm-pic/references/linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/references/linear.py)
- [/code/validated-examples/2026-11-23/warm-pic/references/estimate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/references/estimate.py)
- [/code/validated-examples/2026-11-23/warm-pic/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/experiments.py)
- [/code/validated-examples/2026-11-23/pic-spatial/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/run.py)
- [/code/validated-examples/2026-11-23/pic-spatial/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/primary.py)
- [/code/validated-examples/2026-11-23/pic-spatial/references/scalar_pic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/references/scalar_pic.py)
- [/code/validated-examples/2026-11-24/geometric-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/run.py)
- [/code/validated-examples/2026-11-24/geometric-controls/physics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/physics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py)
- [/code/validated-examples/2026-11-24/geometric-controls/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/io_utils.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/qualify.py)
- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/coupled_md.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/coupled_md.py)
- [/code/validated-examples/2026-11-25/quantum-small/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/io_utils.py)
- [/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py)
- [/code/validated-examples/2026-11-25/quantum-small/molecules.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/molecules.py)
- [/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py)
- [/code/validated-examples/2026-11-25/quantum-small/plot_results.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/plot_results.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/test_dynamics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/test_dynamics.py)
- [/code/validated-examples/2026-11-23/warm-pic/test_pic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/test_pic.py)
- [/code/validated-examples/2026-11-23/pic-spatial/test_spatial.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/test_spatial.py)
- [/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_hamiltonian.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`; harmonic-oscillator, quartic-oscillator, gravity-kepler, multifrequency-resonance)
- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; cold-plasma-pic)
- [Electrostatic Vlasov–Poisson equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#vlasov-poisson-en) (`vlasov-poisson`; cold-plasma-pic, thermal-landau-damping, thermal-two-stream)
- [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en) (`particle-gravity`; gravity-kepler, gravity-plummer-short)
- [Kepler two-body problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kepler-two-body-en) (`kepler-two-body`; gravity-kepler)
- [Coupled two-frequency harmonic oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#coupled-harmonic-oscillators-en) (`coupled-harmonic-oscillators`; multifrequency-resonance)
- [Two-state electronic-angle/nuclear BO and CP-type model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#two-state-bo-cp-model-en) (`two-state-bo-cp-model`; two-state-bo-cp-model)

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

##### [Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) (`cold-plasma-pic`)

![One-dimensional periodic cold electrons, amplitude 0.001: stored CIC electrostatic-PIC displacement versus cos(t), with separate grid and timestep error sweeps.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#code-en)

- [Independently coded PIC spatial pipeline](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en) (`pic-independent-spatial`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip)

Compare vectorized CIC/FFT with separately authored scalar-particle CIC/dense DFT; each trajectory sources its own field at every kick.

##### [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en) (`gravity-kepler`)

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

Position-only kick-half/drift/kick-half; separate bracketed Kepler root and analytic velocities. Original central-force KDK Verlet. Fixed, replayed and regenerated schedules are distinct. Positive radial crossings of cubic Hermite trajectories are localized by brentq.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en#code-en)

- [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en) (`gravity-kepler`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

Advance an unequal-mass binary for one orbit with KDK and compare independent Kepler positions/velocities and conservation.

- [Kepler eccentricity and time-step controls](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en) (`kepler-eccentricity`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

Sixteen fixed evolutions at e=0.1/0.7 compare invariants, same-time phase error, physical periapsis times and reversal.

##### [Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en) (`gravity-plummer-short`)

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short-preview.png)

Direct KDK20/40/80steps; finest-dt full second-moment BHtheta0/.35/.6; qualify independent scalar-pair DOP853 at two tolerances.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en#code-en)

- [Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en) (`gravity-plummer-short`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

Separate time and tree-force errors for the same softened finite-N ODE with independent DOP853/direct-force references and budgets.

##### [Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en) (`thermal-landau-damping`)

![Actual evolved particle velocity change delta-v/alpha against initial(x,v); a1D1V phase-space response, not a2D physical-space flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping-preview.png)

Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en#code-en)

- [Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en) (`thermal-landau-damping`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

Advance thermal Maxwellian full-f particles and compare damping rate, frequency and signed-field history with qualified independent linear references.

##### [Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en) (`thermal-two-stream`)

![Actual particle delta-v/alpha atT40against initial(x,v). This1D1Vphase-space image is a late diagnostic; growth rates are validated only over\[12,20\].](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream-preview.png)

Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en#code-en)

- [Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en) (`thermal-two-stream`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

Evolve counter-streaming warm Maxwellians; distinguish fixed-window growth and transients using dielectric and Volterra references.

##### [Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en) (`multifrequency-resonance`)

![Saved q1–q2 coordinates of the finest impulse trajectory, colored by physical time. This is one coupled trajectory, not a scanned phase diagram. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png)

Full-potential Verlet and a Strang impulse composition: half B kick, exact A flow, half B kick. A contains the fast oscillator and slow free drift; B contains the slow potential and the coupling.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en#code-en)

- [Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en) (`multifrequency-resonance`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

A genuinely coupled two-degree-of-freedom system uses twelve 64-step probes and six accuracy trajectories to separate normal modes, coordinate exchange, discrete maps and roundoff.

##### [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en) (`two-state-bo-cp-model`)

![Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath. Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png)

Use analytic BO forces and the declared CP-type action with Verlet/BAOAB; record nuclear heat and fictitious electronic kinetic energy separately.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en#code-en)

- [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en) (`two-state-bo-cp-ou`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath.


#### Exact / reference solutions (`method-references-en`)

##### [Harmonic oscillator, including complex-ODE form](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=en#references-en) (`harmonic-oscillator`)

- [Harmonic oscillator: Verlet phase error and energy](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-harmonic-oscillator-exact-en) (`harmonic-oscillator-exact`; Same-problem reference; Analytic reference)

An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution. The existing gallery shows t≤10; the common fixed input ends at20.

[Existing reference profile](/numerical-methods-atlas/problems/harmonic-oscillator/?lang=en)

##### [Nonlinear quartic-potential oscillator](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en#references-en) (`quartic-oscillator`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en#references-en) (`cold-plasma-pic`)

- [Independently coded PIC spatial pipeline](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pic-independent-spatial-en) (`pic-independent-spatial`; Related-model reference; Finite-grid numerical reference)

Periodic[0,2pi],256particles,grids8/16/32,seeds35001/35002,dt.02,T.24. Uniform random positions,v=.2Normal+.1sin(x). Six pairs mean twelve separately evolved trajectories.

[Existing reference profile](/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en#pic-independent-spatial-en-measurements)

##### [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en#references-en) (`gravity-kepler`)

- [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-kepler-en) (`gravity-kepler`; Same-problem reference; Analytic reference)

One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.

[Existing reference profile](/numerical-methods-atlas/validation/gravity-kepler/?lang=en#gravity-kepler-en-measurements)

- [Kepler eccentricity and time-step controls](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kepler-eccentricity-en) (`kepler-eccentricity`; Same-problem reference; Semi-analytic reference)

Small invariant errors do not establish phase accuracy. No canonical symplectic-defect measurement is claimed for the variable-step map, and fixed-h properties are not transferred automatically. R1 resolution was revised to R2 using pre-execution asymptotic planning, not measured calibration.

[Existing reference profile](/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en#kepler-eccentricity-en-measurements)

##### [Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en#references-en) (`gravity-plummer-short`)

- [Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-plummer-short-en) (`gravity-plummer-short`; Same-problem reference; Finite-grid numerical reference)

Cold finite-N initial value,not an equilibrium Plummer DF or exact continuum orbit. No general BH reciprocity/global symplecticity claim.

[Existing reference profile](/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en#gravity-plummer-short-en-measurements)

##### [Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en#references-en) (`thermal-landau-damping`)

- [Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-thermal-landau-damping-en) (`thermal-landau-damping`; Same-problem reference; Semi-analytic reference)

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.

[Existing reference profile](/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en#thermal-landau-damping-en-measurements)

##### [Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en#references-en) (`thermal-two-stream`)

- [Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-thermal-two-stream-en) (`thermal-two-stream`; Same-problem reference; Semi-analytic reference)

Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.

[Existing reference profile](/numerical-methods-atlas/validation/thermal-two-stream/?lang=en#thermal-two-stream-en-measurements)

##### [Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en#references-en) (`multifrequency-resonance`)

- [Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-multifrequency-resonance-en) (`multifrequency-resonance`; Same-problem reference; Semi-analytic reference)

The central actual floating map remains unresolved; ideal-pi Jordan structure is not transferred to it. Results concern 64-step amplification and small fixed inputs, not a scanned resonance diagram, general stability or a universal long-time error theorem.

[Existing reference profile](/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en#multifrequency-resonance-en-measurements)

##### [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en#references-en) (`two-state-bo-cp-model`)

- [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-two-state-bo-cp-ou-en) (`two-state-bo-cp-ou`; Same-problem reference; Semi-analytic reference)

Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.

[Existing reference profile](/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en#two-state-bo-cp-ou-en-measurements)

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

##### Independently coded PIC spatial pipeline (`pic-independent-spatial`)

[Cold-plasma oscillation with electrostatic CIC PIC](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/verification.json)

Compare vectorized CIC/FFT with separately authored scalar-particle CIC/dense DFT; each trajectory sources its own field at every kick.

##### Unsoftened Kepler two-body time error (`gravity-kepler`)

[Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json)

Advance an unequal-mass binary for one orbit with KDK and compare independent Kepler positions/velocities and conservation.

##### Kepler eccentricity and time-step controls (`kepler-eccentricity`)

[Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)

Sixteen fixed evolutions at e=0.1/0.7 compare invariants, same-time phase error, physical periapsis times and reversal.

##### Short-time32body dynamics from a cold Plummer-density sample (`gravity-plummer-short`)

[Short-time32body dynamics from a cold Plummer-density sample](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-plummer-short/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json)

Separate time and tree-force errors for the same softened finite-N ODE with independent DOP853/direct-force references and budgets.

##### Warm PIC linear Landau damping (`thermal-landau-damping`)

[Warm PIC linear Landau damping](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/verification.json)

Advance thermal Maxwellian full-f particles and compare damping rate, frequency and signed-field history with qualified independent linear references.

##### Warm PIC two-stream initial growth (`thermal-two-stream`)

[Warm PIC two-stream initial growth](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/atlas-warm-pic-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/verification.json)

Evolve counter-streaming warm Maxwellians; distinguish fixed-window growth and transients using dielectric and Volterra references.

##### Coupled frequencies and finite-window resonance (`multifrequency-resonance`)

[Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)

A genuinely coupled two-degree-of-freedom system uses twelve 64-step probes and six accuracy trajectories to separate normal modes, coordinate exchange, discrete maps and roundoff.

##### A two-state BO / CP-type model with a short nuclear thermostat coupling (`two-state-bo-cp-ou`)

[A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Additional fixed examples: Unsoftened Kepler two-body time error, Short-time32body dynamics from a cold Plummer-density sample. See each release for assumptions and checked scope. Additional fixed examples: Warm PIC linear Landau damping, Warm PIC two-stream initial growth. See each release for assumptions and checked scope. Additional fixed examples: Independently coded PIC spatial pipeline. See each release for assumptions and checked scope.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/run.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/dynamics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/dynamics.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/references/exact.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/experiments.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/protocol.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/protocol.py)
- [/code/validated-examples/2026-11-23/warm-pic/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/run.py)
- [/code/validated-examples/2026-11-23/warm-pic/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/primary.py)
- [/code/validated-examples/2026-11-23/warm-pic/loading.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/loading.py)
- [/code/validated-examples/2026-11-23/warm-pic/references/linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/references/linear.py)
- [/code/validated-examples/2026-11-23/warm-pic/references/estimate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/references/estimate.py)
- [/code/validated-examples/2026-11-23/warm-pic/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/experiments.py)
- [/code/validated-examples/2026-11-23/pic-spatial/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/run.py)
- [/code/validated-examples/2026-11-23/pic-spatial/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/primary.py)
- [/code/validated-examples/2026-11-23/pic-spatial/references/scalar_pic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/references/scalar_pic.py)
- [/code/validated-examples/2026-11-24/geometric-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/run.py)
- [/code/validated-examples/2026-11-24/geometric-controls/physics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/physics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py)
- [/code/validated-examples/2026-11-24/geometric-controls/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/io_utils.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/qualify.py)
- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/coupled_md.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/coupled_md.py)
- [/code/validated-examples/2026-11-25/quantum-small/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/io_utils.py)
- [/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py)
- [/code/validated-examples/2026-11-25/quantum-small/molecules.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/molecules.py)
- [/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py)
- [/code/validated-examples/2026-11-25/quantum-small/plot_results.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/plot_results.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)
- [/code/validated-examples/2026-11-23/gravity-dynamics/test_dynamics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/test_dynamics.py)
- [/code/validated-examples/2026-11-23/warm-pic/test_pic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/test_pic.py)
- [/code/validated-examples/2026-11-23/pic-spatial/test_spatial.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/test_spatial.py)
- [/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_hamiltonian.py
```
