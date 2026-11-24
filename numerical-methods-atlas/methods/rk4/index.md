# Classical RK4 / 古典的RK4

Status: educational-example

Classical four-stage Runge–Kutta advances smooth nonstiff ODEs with fourth-order accuracy. Released examples compare order conditions, stability functions and nonlinear/time-dependent problems while distinguishing accuracy from SSP and symplectic properties. Additional fixed examples: Index reduction, constraint drift and explicit stabilization for a pendulum. See each release for assumptions and checked scope.

滑らかな非硬い常微分方程式を4回の右辺評価で4次精度に進める古典Runge–Kutta法。公開例では次数条件、安定関数、非線形・時刻依存問題を比較し、SSP性やシンプレクティック性とは区別する。 追加固定例：振り子の指数低減・拘束ドリフト・明示安定化。条件と検証範囲は各配布版で確認してください。

Explicit RK4 is neither A-stable nor L-stable and may require small steps for stiff decay. It has no positive general nonlinear SSP coefficient; fourth-order accuracy implies neither positivity, TVD, energy conservation nor symplecticity. The released rk_step is a fixed-step component without an embedded error estimator or adaptive controller. The preceding limitations describe earlier editions. This additional release: No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.

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
陽解法でA安定・L安定ではなく、硬い減衰では小さい刻みを要する。一般の非線形問題に正のSSP係数を持たず、正値性・TVD性・エネルギー保存・シンプレクティック性を4次精度から導くことはできない。このrk_stepは固定刻みの部品で、埋込み誤差推定や自動刻み調整を持たない。 上記の制限は既存配布版の範囲です。今回の追加配布版：投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。
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
Explicit RK4 is neither A-stable nor L-stable and may require small steps for stiff decay. It has no positive general nonlinear SSP coefficient; fourth-order accuracy implies neither positivity, TVD, energy conservation nor symplecticity. The released rk_step is a fixed-step component without an embedded error estimator or adaptive controller. The preceding limitations describe earlier editions. This additional release: No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.
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

## Small fixed-input validation supplements

Reaction-diffusion: separate second-order space and fourth-order time: Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions. Turing instability: linear growth and small-amplitude patterns: Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode. FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference: Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853. Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects. Additional actual2D C-grid linear rotating-SWE fields use RK4. A matrix exponential of the same semidiscrete operator is reference-only; separate continuous spatial and fixed-N temporal errors.

反応拡散：空間2次と時間4次を分けて測る: 線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。 Turing不安定性：線形成長率と小振幅パターン: Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。 FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照: 2変数の膜興奮縮約ODEを電流パルスで励起し、DOP853との全出力時刻の誤差・時間収束・回復を確認します。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。 追加は実際の2D C-grid線形回転浅水場をRK4で時間発展。同じ離散作用素の行列指数を参照にし、連続波の空間誤差と固定N時間細分化を区別します。

- Reaction-diffusion: separate second-order space and fourth-order time: https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/
- Turing instability: linear growth and small-amplitude patterns: https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/
- FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference: https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json

- WENO-JS/Z: fixed critical-point and epsilon comparison: https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/results/result.json

- Actual2D C-grid rotating shallow-water time advance: https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/result.json

- Index reduction, constraint drift and explicit stabilization for a pendulum: https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json

Common execution records: [{"id": "logistic-growth", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#logistic-growth-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#logistic-growth-en"}}, {"id": "sir-epidemic", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#sir-epidemic-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#sir-epidemic-en"}}, {"id": "reaction-diffusion-fourier", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "turing-schnakenberg", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "fitzhugh-nagumo", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "weno-critical-epsilon", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "cgrid-rotating-wave", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "high-index-pendulum", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [線形移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja) (`linear-advection`; advection-sine)
- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; isentropic-vortex)
- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`; quartic-oscillator, high-index-pendulum)
- [ロジスティック個体群増殖](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-logistic-ja) (`bio-logistic`; logistic-growth)
- [SIR・SEIR区画モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-sir-ja) (`bio-sir`; sir-epidemic)
- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`; reaction-diffusion-fourier)
- [Schnakenberg反応拡散](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-schnakenberg-ja) (`bio-schnakenberg`; turing-schnakenberg)
- [Turing反応拡散の枠組み](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-turing-ja) (`bio-turing`; turing-schnakenberg)
- [FitzHugh–Nagumoの興奮と回復](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-fitzhugh-nagumo-ja) (`bio-fitzhugh-nagumo`; fitzhugh-nagumo)
- [線形回転浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-rotating-shallow-water-ja) (`linear-rotating-shallow-water`; cgrid-rotating-wave)
- [拘束付き平面振り子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#constrained-pendulum-ja) (`constrained-pendulum`; high-index-pendulum)

#### 問題の図 (`method-problems-ja`)

##### [周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) (`advection-sine`)

![保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。 p+1個のGauss解点、上流数値流束、Legendre多項式によるRadau左右補正、SSPRK(3,3)。初期L2射影・上流流束・時間刻み規約をバイト一致の既存modal DGと揃えます。スケールしたCourant数(2p+1)|a|Δt/h≤.15。最後にp2/N32で刻みを半減。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#code-ja)

- [WENO-JS／Z：臨界点とεの固定比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja) (`weno-critical-epsilon`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip)

同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。

##### [周期移動等エントロピー渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja) (`isentropic-vortex`)

![M∞=.01、64²、T=.1の実際の2次元Euler計算。全\[-10,10\]²領域から中心\[-3,3\]²を拡大し、保存速度から差分で求めた渦度と背景流を引いた速度矢印で、MUSCL付き通常Roe／前処理Roeを比較します。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex-preview.png)

従来のKEEP/RK4固定例を保持し、新しい低Mach比較にRoe・数値散逸の前処理・無制限中心primitive MUSCL・SSPRK(3,3)を対応付けます。個々の実行例が使う手法は実行ページで区別します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [4次ポテンシャルの非線形振動子](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja) (`quartic-oscillator`)

![保存済みのt≤10の正準位相軌道。手法違いは同一問題の比較。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/quartic-oscillator.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [指数関数を厳密解に持つ非線形・非自律ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja) (`nonlinear-exp-ode`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-exp-ode.png)

公開の全陽的RK tableauに対する非自律・非線形製造解の検査です。保存プレビューはRK4を使います。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [有理減衰ODE（y′ = −y²）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja) (`nonlinear-rational-decay`)

![保存済み有理減衰ODEの時間刻み収束（代表3手法）。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-decay.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [ロジスティック増殖：解析解と刻み幅の収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=ja) (`logistic-growth`)

![公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/logistic-growth/preview.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=ja#code-ja)

- [ロジスティック増殖：解析解と刻み幅の収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=ja) (`logistic-growth`) · [コードZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。

##### [SIR：独立DOP853参照・人口保存・収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=ja) (`sir-epidemic`)

![公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/preview.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=ja#code-ja)

- [SIR：独立DOP853参照・人口保存・収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=ja) (`sir-epidemic`) · [コードZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。

##### [反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja) (`reaction-diffusion-fourier`)

![周期Fourierモードの線形反応拡散。16/32/64格子の連続解誤差と、固定格子での半離散厳密解に対する時間誤差を分けた保存収束図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja#code-ja)

- [反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja) (`reaction-diffusion-fourier`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。

##### [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`)

![a=0.1,b=0.9、拡散係数0.01/1のSchnakenberg型。行列指数に対する線形誤差・成長率と、t=4の小振幅非線形初期パターンを保存値から表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#code-ja)

- [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。

##### [FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=ja) (`fitzhugh-nagumo`)

![無次元の2変数FHN型ODEにt=10〜20の電流パルス。DOP853参照とRK4の興奮・回復、刻み0.1/0.05/0.025の収束と全出力点の差を保存結果から表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=ja#code-ja)

- [FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja) (`fitzhugh-nagumo`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

2変数の膜興奮縮約ODEを電流パルスで励起し、DOP853との全出力時刻の誤差・時間収束・回復を確認します。

##### [2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja) (`cgrid-rotating-wave`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave-preview.png)

セルeta・法線face u/vの差分と4点Coriolis補間を2Dで評価しRK4更新。3×3行列指数は参照だけで、PDE場の更新には使いません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja#code-ja)

- [2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja) (`cgrid-rotating-wave`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

実際の2D staggered場を時間積分し、連続波と離散symbolの参照を分けて比較します。

##### [拘束付き振り子](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja) (`high-index-pendulum`)

![位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。 保存配列から作図。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png)

指数低減ODEと臨界拘束誤差拡張を固定RK4で積分し、拘束仕事も同じ段で積分します。 独自のスカラーNewton位置拘束、RATTLE終端接線impulse、SHAKE位置対。SHAKEの運動量は内部点だけで中心化し、端点を作りません。 SHAKEのsolves列はeta、eta/h^2、位置残差、Newton更新数です。列1は一律にeta/h^2ですが、初回半刻みの物理乗数は2eta/h^2、以後の位置Verletではeta/h^2です。逆位置対はすべて後者です。判定と図はこの列1を使いません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#code-ja)

- [振り子の指数低減・拘束ドリフト・明示安定化](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja) (`high-index-pendulum`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#references-ja) (`advection-sine`)

- [移流／正弦波の平行移動](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja) (`sine-advection`; 関連モデルの参照; 解析参照)

同じ周期・速度1の正弦移流モデルです。参照一覧は振幅0.25、共通固定入力は0.2で、DG・CIP等の表現や時間も異なります。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-advection)

- [WENO臨界点：多項式セル平均と解析的周期輸送](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-weno-critical-profile-ja) (`weno-critical-profile`; 関連モデルの参照; 解析参照)

同じ一定速度の周期移流に対する追加参照ですが、cos+.1sin³のセル平均と局所臨界多項式は、従来の単一正弦・CIP表示と異なります。

[既存の参照図](/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja#weno-critical-epsilon-ja-measurements)

- [FRとDGの周期正弦移流：平均0.4・T=.25の解析参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fr-periodic-advection-ja) (`fr-periodic-advection`; 同じ問題の参照; 解析参照)

全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。

[既存の参照図](/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja)

##### [周期移動等エントロピー渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja#references-ja) (`isentropic-vortex`)

- [等エントロピー渦：低Mach比較に用いるEuler解析場](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isentropic-vortex-ja) (`isentropic-vortex`; 同じ問題の参照; 解析参照)

同じ等エントロピー移動渦族の解析場です。保存量をGauss求積してから圧力・速度を算出し、周期の継ぎ目に残るGaussianの裾と求積誤差を明記します。

[既存の参照図](/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja#low-mach-vortex-ja-measurements)

##### [4次ポテンシャルの非線形振動子](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja#references-ja) (`quartic-oscillator`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [指数関数を厳密解に持つ非線形・非自律ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja#references-ja) (`nonlinear-exp-ode`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [有理減衰ODE（y′ = −y²）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja#references-ja) (`nonlinear-rational-decay`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [ロジスティック増殖：解析解と刻み幅の収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=ja#references-ja) (`logistic-growth`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [SIR：独立DOP853参照・人口保存・収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=ja#references-ja) (`sir-epidemic`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja#references-ja) (`reaction-diffusion-fourier`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#references-ja) (`turing-schnakenberg`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=ja#references-ja) (`fitzhugh-nagumo`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja#references-ja) (`cgrid-rotating-wave`)

- [C-grid：連続Fourier解と離散記号の行列指数](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-cgrid-rotating-wave-ja) (`cgrid-rotating-wave`; 同じ問題の参照; 解析参照)

線形・平面・周期squareの限定例。非線形浅水、PV・球面格子・全球dynamical coreやWilliamsonは未実装の後続課題。

[既存の参照図](/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja#cgrid-rotating-wave-ja-measurements)

##### [拘束付き振り子](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#references-ja) (`high-index-pendulum`)

- [振り子の指数低減・拘束ドリフト・明示安定化](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-high-index-pendulum-ja) (`high-index-pendulum`; 同じ問題の参照; 半解析参照)

投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。

[既存の参照図](/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja#high-index-pendulum-ja-measurements)

- [SHAKEとRATTLE：拘束と運動量の違い](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shake-rattle-pendulum-ja) (`shake-rattle-pendulum`; 同じ問題の参照; 半解析参照)

原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。

[既存の参照図](/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja#shake-rattle-pendulum-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### WENO-JS／Z：臨界点とεの固定比較 (`weno-critical-epsilon`)

[周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/verification.json)

同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。

##### ロジスティック増殖：解析解と刻み幅の収束 (`logistic-growth`)

[ロジスティック増殖：解析解と刻み幅の収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/logistic-growth.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。

##### SIR：独立DOP853参照・人口保存・収束 (`sir-epidemic`)

[SIR：独立DOP853参照・人口保存・収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/sir-epidemic.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。

##### 反応拡散：空間2次と時間4次を分けて測る (`reaction-diffusion-fourier`)

[反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。

##### Turing不安定性：線形成長率と小振幅パターン (`turing-schnakenberg`)

[Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。

##### FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照 (`fitzhugh-nagumo`)

[FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

2変数の膜興奮縮約ODEを電流パルスで励起し、DOP853との全出力時刻の誤差・時間収束・回復を確認します。

##### 2D C-grid回転浅水波の実時間発展 (`cgrid-rotating-wave`)

[2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json)

実際の2D staggered場を時間積分し、連続波と離散symbolの参照を分けて比較します。

##### 振り子の指数低減・拘束ドリフト・明示安定化 (`high-index-pendulum`)

[拘束付き振り子](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

反応拡散：空間2次と時間4次を分けて測る: 線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。 Turing不安定性：線形成長率と小振幅パターン: Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。 FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照: 2変数の膜興奮縮約ODEを電流パルスで励起し、DOP853との全出力時刻の誤差・時間収束・回復を確認します。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。 追加は実際の2D C-grid線形回転浅水場をRK4で時間発展。同じ離散作用素の行列指数を参照にし、連続波の空間誤差と固定N時間細分化を区別します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)
- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/models.py)
- [/code/validated-examples/2026-11-23/weno-critical/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/run.py)
- [/code/validated-examples/2026-11-23/weno-critical/weno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/weno.py)
- [/code/validated-examples/2026-11-23/weno-critical/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/references/analytic.py)
- [/code/validated-examples/2026-11-23/moving-waves/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/run.py)
- [/code/validated-examples/2026-11-23/moving-waves/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/transport.py)
- [/code/validated-examples/2026-11-23/moving-waves/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/references/exact.py)
- [/code/validated-examples/2026-11-23/moving-waves/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/experiments.py)
- [/code/validated-examples/2026-11-24/dae-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/run.py)
- [/code/validated-examples/2026-11-24/dae-controls/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/models.py)
- [/code/validated-examples/2026-11-24/dae-controls/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/newton.py)
- [/code/validated-examples/2026-11-24/dae-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/experiments.py)
- [/code/validated-examples/2026-11-24/dae-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/io_contract.py)
- [/code/validated-examples/2026-11-24/dae-controls/references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/references.py)
- [/code/validated-examples/2026-11-24/dae-controls/reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/reporting.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)
- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)
- [/code/validated-examples/2026-11-23/weno-critical/test_weno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/test_weno.py)
- [/code/validated-examples/2026-11-23/moving-waves/test_moving.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/test_moving.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_cases.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_serialization.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_runge_kutta.py tests/test_hamiltonian.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Linear advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en) (`linear-advection`; advection-sine)
- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; isentropic-vortex)
- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`; quartic-oscillator, high-index-pendulum)
- [Logistic population growth](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-logistic-en) (`bio-logistic`; logistic-growth)
- [SIR and SEIR compartment models](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-sir-en) (`bio-sir`; sir-epidemic)
- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`; reaction-diffusion-fourier)
- [Schnakenberg reaction–diffusion](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-schnakenberg-en) (`bio-schnakenberg`; turing-schnakenberg)
- [Turing reaction–diffusion framework](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-turing-en) (`bio-turing`; turing-schnakenberg)
- [FitzHugh–Nagumo excitation and recovery](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-fitzhugh-nagumo-en) (`bio-fitzhugh-nagumo`; fitzhugh-nagumo)
- [Linear rotating shallow-water equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-rotating-shallow-water-en) (`linear-rotating-shallow-water`; cgrid-rotating-wave)
- [Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#constrained-pendulum-en) (`constrained-pendulum`; high-index-pendulum)

#### Problem figures (`method-problems-en`)

##### [Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) (`advection-sine`)

![Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions. Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects. p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#code-en)

- [WENO-JS/Z: fixed critical-point and epsilon comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en) (`weno-critical-epsilon`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip)

Compare WENO5 JS and Z power-two weights from the same cell means, then evolve actual periodic transport. Retain three regularity classes, three epsilon choices, fixed grids and separate halved-time-step diagnostics.

##### [Periodic moving isentropic vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en) (`isentropic-vortex`)

![Actual 2D Euler evolution at M∞=.01, 64² and T=.1. A central \[-3,3\]² crop of the full \[-10,10\]² computation compares ordinary and preconditioned Roe with MUSCL. Vorticity is derived by finite differences of saved velocity; arrows show velocity minus the background flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex-preview.png)

Retain the historical KEEP/RK4 fixed case and connect Roe, dissipation preconditioning, unlimited central primitive MUSCL and SSPRK(3,3) to the additional low-Mach comparison. Each execution page states its own methods.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Nonlinear quartic-potential oscillator](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en) (`quartic-oscillator`)

![Stored canonical phase orbits for t≤10; methods remain variants of one problem.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/quartic-oscillator.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Nonlinear nonautonomous ODE with exponential exact solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en) (`nonlinear-exp-ode`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-exp-ode.png)

Public nonautonomous/nonlinear manufactured-solution checks exercise every explicit RK tableau; the saved preview uses RK4.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Rational-decay ODE (y′ = −y²)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en) (`nonlinear-rational-decay`)

![Stored time-refinement errors for rational decay, showing three methods.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-decay.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Logistic growth: analytic solution and time refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=en) (`logistic-growth`)

![The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/logistic-growth/preview.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=en#code-en)

- [Logistic growth: analytic solution and time refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=en) (`logistic-growth`) · [Code ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.

##### [SIR: independent DOP853 reference, conservation and convergence](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=en) (`sir-epidemic`)

![The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/preview.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=en#code-en)

- [SIR: independent DOP853 reference, conservation and convergence](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=en) (`sir-epidemic`) · [Code ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.

##### [Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en) (`reaction-diffusion-fourier`)

![Stored linear periodic Fourier reaction–diffusion refinement separates continuum errors on 16/32/64 grids from temporal errors against a fixed-grid semidiscrete exact solution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en#code-en)

- [Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en) (`reaction-diffusion-fourier`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.

##### [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

![Schnakenberg-type a=0.1,b=0.9 and diffusivities 0.01/1: stored linear errors/growth against a matrix exponential and a small nonlinear onset pattern at t=4.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

- [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en) (`turing-schnakenberg`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.

##### [FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=en) (`fitzhugh-nagumo`)

![A dimensionless two-variable FHN-type ODE with a t=10..20 current pulse: stored RK4/DOP853 excitation and recovery, steps 0.1/0.05/0.025 and all-output-time differences.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=en#code-en)

- [FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en) (`fitzhugh-nagumo`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853.

##### [Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en) (`cgrid-rotating-wave`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave-preview.png)

Actual2D cell-height/face-velocity differences and four-point Coriolis interpolation use RK4. The3×3 matrix exponential is reference-only, never the PDE update.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en#code-en)

- [Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en) (`cgrid-rotating-wave`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

Time-advance actual2D staggered fields and distinguish continuous-wave references from semidiscrete symbols.

##### [Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en) (`high-index-pendulum`)

![Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts. Drawn from saved arrays. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png)

Advance the index-reduced ODE and a critical constraint-error extension with fixed RK4, integrating constraint work at the same stages. Original scalar Newton position constraints, RATTLE final tangent impulses and SHAKE position pairs. SHAKE momentum is centered only at interior nodes; endpoint momenta are absent. SHAKE solves columns are eta, eta/h^2, position residual and Newton updates. Column1 uses the uniform recurrence normalization eta/h^2. For the first constrained half-step startup, the physical multiplier is 2*eta/h^2; later full position-Verlet steps use eta/h^2. Reverse-pair steps all use the later recurrence convention. RATTLE has its separate five-column normalization. No scientific gate or plot uses SHAKE column1.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#code-en)

- [Index reduction, constraint drift and explicit stabilization for a pendulum](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en) (`high-index-pendulum`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#references-en) (`advection-sine`)

- [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en) (`sine-advection`; Related-model reference; Analytic reference)

Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-advection)

- [WENO critical points: polynomial cell means and analytic periodic transport](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en) (`weno-critical-profile`; Related-model reference; Analytic reference)

An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.

[Existing reference profile](/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en#weno-critical-epsilon-en-measurements)

- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en) (`fr-periodic-advection`; Same-problem reference; Analytic reference)

Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.

[Existing reference profile](/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en)

##### [Periodic moving isentropic vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en#references-en) (`isentropic-vortex`)

- [Isentropic vortex: analytic Euler field for low-Mach comparisons](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isentropic-vortex-en) (`isentropic-vortex`; Same-problem reference; Analytic reference)

Analytic field for the same translating isentropic-vortex family. Pressure and velocity are evaluated after Gauss integration of conserved variables; finite-periodic Gaussian tails and quadrature error remain explicit.

[Existing reference profile](/numerical-methods-atlas/validation/low-mach-vortex/?lang=en#low-mach-vortex-en-measurements)

##### [Nonlinear quartic-potential oscillator](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en#references-en) (`quartic-oscillator`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Nonlinear nonautonomous ODE with exponential exact solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en#references-en) (`nonlinear-exp-ode`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Rational-decay ODE (y′ = −y²)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en#references-en) (`nonlinear-rational-decay`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Logistic growth: analytic solution and time refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=en#references-en) (`logistic-growth`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [SIR: independent DOP853 reference, conservation and convergence](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=en#references-en) (`sir-epidemic`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en#references-en) (`reaction-diffusion-fourier`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#references-en) (`turing-schnakenberg`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=en#references-en) (`fitzhugh-nagumo`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en#references-en) (`cgrid-rotating-wave`)

- [C-grid: continuous Fourier solution and discrete-symbol exponential](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-cgrid-rotating-wave-en) (`cgrid-rotating-wave`; Same-problem reference; Analytic reference)

Linear planar periodic square only. Nonlinear SWE,PV,spherical dynamics and Williamson tests remain future work.

[Existing reference profile](/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en#cgrid-rotating-wave-en-measurements)

##### [Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#references-en) (`high-index-pendulum`)

- [Index reduction, constraint drift and explicit stabilization for a pendulum](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-high-index-pendulum-en) (`high-index-pendulum`; Same-problem reference; Semi-analytic reference)

No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.

[Existing reference profile](/numerical-methods-atlas/validation/high-index-pendulum/?lang=en#high-index-pendulum-en-measurements)

- [SHAKE and RATTLE: constraints and momentum ownership](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shake-rattle-pendulum-en) (`shake-rattle-pendulum`; Same-problem reference; Semi-analytic reference)

Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency.

[Existing reference profile](/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en#shake-rattle-pendulum-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### WENO-JS/Z: fixed critical-point and epsilon comparison (`weno-critical-epsilon`)

[Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/verification.json)

Compare WENO5 JS and Z power-two weights from the same cell means, then evolve actual periodic transport. Retain three regularity classes, three epsilon choices, fixed grids and separate halved-time-step diagnostics.

##### Logistic growth: analytic solution and time refinement (`logistic-growth`)

[Logistic growth: analytic solution and time refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/logistic-growth.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.

##### SIR: independent DOP853 reference, conservation and convergence (`sir-epidemic`)

[SIR: independent DOP853 reference, conservation and convergence](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/sir-epidemic.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.

##### Reaction-diffusion: separate second-order space and fourth-order time (`reaction-diffusion-fourier`)

[Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.

##### Turing instability: linear growth and small-amplitude patterns (`turing-schnakenberg`)

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.

##### FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference (`fitzhugh-nagumo`)

[FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853.

##### Actual2D C-grid rotating shallow-water time advance (`cgrid-rotating-wave`)

[Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json)

Time-advance actual2D staggered fields and distinguish continuous-wave references from semidiscrete symbols.

##### Index reduction, constraint drift and explicit stabilization for a pendulum (`high-index-pendulum`)

[Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Reaction-diffusion: separate second-order space and fourth-order time: Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions. Turing instability: linear growth and small-amplitude patterns: Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode. FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference: Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853. Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects. Additional actual2D C-grid linear rotating-SWE fields use RK4. A matrix exponential of the same semidiscrete operator is reference-only; separate continuous spatial and fixed-N temporal errors.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)
- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/models.py)
- [/code/validated-examples/2026-11-23/weno-critical/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/run.py)
- [/code/validated-examples/2026-11-23/weno-critical/weno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/weno.py)
- [/code/validated-examples/2026-11-23/weno-critical/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/references/analytic.py)
- [/code/validated-examples/2026-11-23/moving-waves/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/run.py)
- [/code/validated-examples/2026-11-23/moving-waves/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/transport.py)
- [/code/validated-examples/2026-11-23/moving-waves/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/references/exact.py)
- [/code/validated-examples/2026-11-23/moving-waves/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/experiments.py)
- [/code/validated-examples/2026-11-24/dae-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/run.py)
- [/code/validated-examples/2026-11-24/dae-controls/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/models.py)
- [/code/validated-examples/2026-11-24/dae-controls/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/newton.py)
- [/code/validated-examples/2026-11-24/dae-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/experiments.py)
- [/code/validated-examples/2026-11-24/dae-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/io_contract.py)
- [/code/validated-examples/2026-11-24/dae-controls/references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/references.py)
- [/code/validated-examples/2026-11-24/dae-controls/reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/reporting.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)
- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)
- [/code/validated-examples/2026-11-23/weno-critical/test_weno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/test_weno.py)
- [/code/validated-examples/2026-11-23/moving-waves/test_moving.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/test_moving.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_cases.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_serialization.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_runge_kutta.py tests/test_hamiltonian.py
```
