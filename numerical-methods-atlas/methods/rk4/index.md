# Classical RK4 / 古典的RK4

Status: educational-example

Classical four-stage Runge–Kutta advances smooth nonstiff ODEs with fourth-order accuracy. Released examples compare order conditions, stability functions and nonlinear/time-dependent problems while distinguishing accuracy from SSP and symplectic properties.

滑らかな非硬い常微分方程式を4回の右辺評価で4次精度に進める古典Runge–Kutta法。公開例では次数条件、安定関数、非線形・時刻依存問題を比較し、SSP性やシンプレクティック性とは区別する。

Explicit RK4 is neither A-stable nor L-stable and may require small steps for stiff decay. It has no positive general nonlinear SSP coefficient; fourth-order accuracy implies neither positivity, TVD, energy conservation nor symplecticity. The released rk_step is a fixed-step component without an embedded error estimator or adaptive controller.

Other names: RK4法, 古典的Runge-Kutta法, classical Runge-Kutta, classical fourth-order Runge-Kutta, 4次ルンゲクッタ法


## 条件と確認範囲 (ja)

problem: 滑らかな常微分方程式・空間離散後の系の初期値問題。

variant: runge_kutta.TABLEAUS['rk4']の古典4段4次とrk_step。Hamiltonian比較にも同じ古典係数のRK4がある。

use_when:
- 非硬い滑らかな問題で、誤差と刻み幅の関係を明快に調べたい。
- 4回の右辺評価を許容でき、固定刻みや別の刻み制御を管理できる。

avoid_when:
- 非常に硬い減衰やDAEを汎用に解く。
- SSP性・正値性や長時間のHamilton構造保存が必須。

assumptions [specified]:
- 対象は初期値問題y'=f(t,y)で、4次収束を期待する区間では右辺と解に十分な滑らかさがある。
- 採用係数はc=(0,1/2,1/2,1)、a21=1/2、a32=1/2、a43=1、b=(1,2,2,1)/6の古典4段4次。
- 時間刻みは呼び出し側が選び、空間離散したPDEではそのスペクトル・CFL制約にも従う。線形モードでは|R(hλ)|≤1を確認する。
公開tableauと非自律段階時刻を確認。

units [specified]:
時間hとtは同じ単位、f_iはy_i/時間の単位。状態成分の単位は問題が定め、RK4自体は固有の物理単位を持たない。hλは無次元。
y+h fという段階式から成分ごとに定義。

boundary_conditions [not-applicable]:
時間ステップ単体に空間境界条件は該当しない。PDEを進める場合、境界値やゴースト状態は各段階の右辺評価が正しく供給する必要がある。
rk_stepは右辺関数を受け取る時間積分部品。

limitations [specified]:
陽解法でA安定・L安定ではなく、硬い減衰では小さい刻みを要する。一般の非線形問題に正のSSP係数を持たず、正値性・TVD性・エネルギー保存・シンプレクティック性を4次精度から導くことはできない。このrk_stepは固定刻みの部品で、埋込み誤差推定や自動刻み調整を持たない。
線形安定性と非線形SSP性・幾何学的性質を区別。

Review: runge_kutta.pyのrk4係数・rk_step・安定関数を読んだ。test_runge_kutta.pyの4次条件、非自律非線形製造解、安定関数とSSP非成立の検査、およびHamiltonian比較の既存テストを確認。今回の再実行なし。

Not checked:
- Kuttaの歴史的原報の本文・優先権の調査。
- 新しい数値実行、任意の右辺・不連続時刻・硬いPDEへの検証。

Evidence:
- TABLEAUS['rk4']; rk_step; stability_polynomial; stability_function: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py
- classical RK4 comparison; canonical_step: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py
- test_rk_order_conditions_and_manufactured_nonlinear_time_dependence; test_linear_stability_matches_actual_stages_and_refinement; test_rk2_same_linear_factor_different_nonlinear_stages_and_ssp: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py
- test_map_jacobians_against_independent_differences_and_symplectic_form: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py

References:
- [formulation / primary-research] Butcher (1963). Coefficients for the study of Runge-Kutta integration processes. — https://doi.org/10.1017/S1446788700027932
  Runge–Kutta法の次数条件を定式化した一次文献。4次条件を扱う本文を確認したが、古典RK4の発明論文という意味では引用しない。
  full-text (2026-11-22); Runge–Kutta definitions and p. 196 fourth-order conditions; relevant portions read, not every proof.; https://www.cambridge.org/core/services/aop-cambridge-core/content/view/457E8B0413C29B9D7BBCD7D2A45A23D5/S1446788700027932a.pdf/div-class-title-coefficients-for-the-study-of-runge-kutta-integration-processes-div.pdf

## Conditions and review scope (en)

problem: Initial-value problems for smooth ODEs or semidiscrete systems.

variant: Classical four-stage fourth-order TABLEAUS['rk4'] and rk_step in runge_kutta.py; the Hamiltonian comparison also uses classical RK4 coefficients.

use_when:
- A smooth nonstiff problem needs a clear accuracy/step-size baseline.
- Four RHS evaluations per step are affordable, with fixed-step or external step control.

avoid_when:
- Very stiff decay or general DAEs must be handled.
- SSP/positivity guarantees or long-time Hamiltonian structure preservation are essential.

assumptions [specified]:
- The target is the initial-value problem y'=f(t,y), with sufficient smoothness of f and y for fourth-order convergence.
- The adopted classical tableau has c=(0,1/2,1/2,1), a21=1/2, a32=1/2, a43=1 and b=(1,2,2,1)/6.
- The caller selects the step. A semidiscrete PDE also imposes spatial spectral/CFL restrictions; linear modes require |R(hλ)|≤1.
Inspected the released tableau and nonautonomous stage times.

units [specified]:
h and t have the same time unit, and f_i has units y_i/time. State-component units belong to the problem; RK4 imposes no intrinsic physical unit. hλ is dimensionless.
Specified componentwise from stage updates of the form y+h f.

boundary_conditions [not-applicable]:
Spatial boundary conditions do not apply to the ODE step itself. For a PDE, each stage's RHS evaluation must supply the appropriate boundary values or ghost states.
rk_step is a time integrator that receives an RHS function.

limitations [specified]:
Explicit RK4 is neither A-stable nor L-stable and may require small steps for stiff decay. It has no positive general nonlinear SSP coefficient; fourth-order accuracy implies neither positivity, TVD, energy conservation nor symplecticity. The released rk_step is a fixed-step component without an embedded error estimator or adaptive controller.
Separates linear stability from nonlinear SSP and geometric properties.

Review: Read the RK4 tableau, rk_step and stability functions in runge_kutta.py. Inspected tests for fourth-order conditions, a manufactured nonautonomous nonlinear solution, stability functions, failure of general SSP conditions, and the Hamiltonian comparison. No rerun was performed.

Not checked:
- Historical Kutta full text and priority claims.
- New numerical runs or validation for arbitrary RHS functions, time discontinuities or stiff PDEs.

Evidence:
- TABLEAUS['rk4']; rk_step; stability_polynomial; stability_function: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py
- classical RK4 comparison; canonical_step: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py
- test_rk_order_conditions_and_manufactured_nonlinear_time_dependence; test_linear_stability_matches_actual_stages_and_refinement; test_rk2_same_linear_factor_different_nonlinear_stages_and_ssp: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py
- test_map_jacobians_against_independent_differences_and_symplectic_form: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py

References:
- [formulation / primary-research] Butcher (1963). Coefficients for the study of Runge-Kutta integration processes. — https://doi.org/10.1017/S1446788700027932
  Primary order-condition formulation, with the fourth-order discussion inspected. This is not presented as the historical invention paper for classical RK4.
  full-text (2026-11-22); Runge–Kutta definitions and p. 196 fourth-order conditions; relevant portions read, not every proof.; https://www.cambridge.org/core/services/aop-cambridge-core/content/view/457E8B0413C29B9D7BBCD7D2A45A23D5/S1446788700027932a.pdf/div-class-title-coefficients-for-the-study-of-runge-kutta-integration-processes-div.pdf


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py

- Reference: https://doi.org/10.1017/S1446788700027932 — Primary formulation of Runge–Kutta order conditions, including fourth-order conditions; not attributed as the historical invention of classical RK4.

## Small fixed-input validation supplement

Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions. Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode. Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853.

線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。 Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。 2変数の膜興奮縮約ODEを電流パルスで励起し、DOP853との全出力時刻の誤差・時間収束・回復を確認します。

- Reaction-diffusion: separate second-order space and fourth-order time: https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/
- Turing instability: linear growth and small-amplitude patterns: https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/
- FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference: https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json

Common execution records: [{"id": "logistic-growth", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#logistic-growth-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#logistic-growth-en"}}, {"id": "sir-epidemic", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#sir-epidemic-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#sir-epidemic-en"}}, {"id": "reaction-diffusion-fourier", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "turing-schnakenberg", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "fitzhugh-nagumo", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
