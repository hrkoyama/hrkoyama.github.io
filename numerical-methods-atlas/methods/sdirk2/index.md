# L-stable SDIRK2 / L安定なSDIRK2

Status: educational-example

A two-stage second-order implicit Runge–Kutta method for stiff ODE decay. The release uses stiffly accurate L-stable SDIRK with γ=1−1/√2 and Newton stage solves; a separate wrapper adds step-doubling local-error control.

硬い常微分方程式の減衰を扱う2段2次の陰的Runge–Kutta法。公開版はγ=1−1/√2のstiffly accurateなL安定SDIRKで、各段階にNewton法を用い、別のラッパーでステップ倍化による局所誤差制御を行う。

L-stability concerns the linear test equation with accurate stage solves; it guarantees neither large-step accuracy, nonlinear convergence nor positivity. A Newton failure raises in the fixed version and rejects a trial in the adaptive wrapper. Adaptivity uses step doubling, not an embedded pair; rtol/atol control a local error scale, not a guaranteed final global error. General DAEs, mass matrices and events are not implemented.

Other names: SDIRK2法, 2次SDIRK, L-stable SDIRK2


## 条件と確認範囲 (ja)

problem: 速い減衰モードと遅い変化が共存する常微分方程式の初期値問題。

variant: stiff.pyのsdirk2_step: γ=1−1/√2の2段2次stiffly accurate SDIRK。Newtonは許容値2×10^-12・最大25回。適応ラッパーは独立のステップ倍化。

use_when:
- 硬い減衰を抑えつつ2次精度で進め、右辺とJacobianを用意できる。
- 陰的段階の収束と、許容誤差を変えた結果の比較を管理できる。

avoid_when:
- Jacobianが不整合、またはNewtonが収束しない状態のまま解を採用する。
- DAE、厳密な正値性、イベント検出や保証付き大域誤差制御をこの実装だけで必要とする。

assumptions [specified]:
- 対象は実数の1次元配列で表すODE y'=f(t,y)。整合するJacobian ∂f/∂yを呼び出し側が与える。
- A=[[γ,0],[1−γ,γ]]、b=(1−γ,γ)、c=(γ,1)、γ=1−1/√2。最終段を次の解にするstiffly accurate版。
- 正確な段階解に対する安定関数はR(z)=[1+(1−2γ)z]/(1−γz)^2。このγではA安定かつ左半平面で|z|→∞のときR→0となる。
- 実装では各段階のNewton収束が必要。固定刻みintegrateと、(2半歩−1全歩)/3を使って2半歩の解を採用するadaptive_sdirk2を区別する。
GAMMA、2段の時刻・係数、Newton呼び出しを確認。

units [specified]:
hは時間、f_iはy_i/時間、Jacobian要素J_ijはy_i/(y_j×時間)。無次元化または成分尺度の調整が必要で、固定のNewton許容値2×10^-12は任意の物理単位に自動対応しない。適応版のatolは状態尺度、rtolは無次元。
成分ごとのODE/Jacobian単位と許容値尺度を指定。

boundary_conditions [not-applicable]:
ODE時間積分単体には空間境界条件は該当しない。PDEの半離散系に使う場合、境界条件とその時刻依存性を右辺とJacobianへ整合して組み込む。
時間積分器はfとjacを引数に取り、境界を設定しない。

limitations [specified]:
L安定性は正確な段階解を前提とする線形試験方程式の性質であり、大刻みの精度・非線形収束・正値性を保証しない。Newton失敗時は固定版が例外、適応版が試行棄却を行う。埋込み対ではなくステップ倍化で、rtol/atolは局所誤差尺度であり最終大域誤差の保証ではない。一般DAE、質量行列、イベント処理は未実装。
L安定性、反復収束、局所誤差制御の条件を分離。

Review: stiff.pyのGAMMA・_stage・sdirk2_step・integrate・adaptive_sdirk2を読んだ。test_new_models.pyの非自律非線形の2次収束、硬い減衰、許容誤差比較、試行上限での例外を確認。新規計算・再実行なし。

Not checked:
- Alexander原報全文の係数表・証明の照合。
- 今回の数値再実行、一般DAE、硬いPDEでの次数低下や任意系のNewton収束。

Evidence:
- GAMMA; _stage; sdirk2_step; integrate; adaptive_sdirk2: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/stiff.py
- test_implicit_orders_on_nonautonomous_nonlinear_exact_solution; test_stiff_decay_and_local_error_control: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py

References:
- [original-method / primary-research] Alexander (1977). Diagonally Implicit Runge–Kutta Methods for Stiff O.D.E.’s. — https://doi.org/10.1137/0714068
  2段2次の硬い系向けDIRK法の一次文献。採用γと安定関数は本サイトの係数および公式補足資料から特定し、原報全文確認とは区別する。
  abstract-and-metadata (2026-11-22); Publisher abstract and metadata; full-text tableau not reviewed.; https://epubs.siam.org/doi/10.1137/0714068
- [formulation / official-documentation] MOOSE. LStableDirk2. — https://mooseframework.inl.gov/source/timeintegrators/LStableDirk2.html
  Alexander法との関係と2段2次・L安定性を明記する公式実装資料。数式画像は今回のテキスト取得では読めておらず、係数はローカル実装を根拠にする。
  full-text (2026-11-22); LStableDirk2 description, Notes and References; equation images were not extracted by the text browser.; https://mooseframework.inl.gov/source/timeintegrators/LStableDirk2.html

## Conditions and review scope (en)

problem: ODE initial-value problems with rapidly decaying modes and slower evolution.

variant: sdirk2_step in stiff.py: two-stage second-order stiffly accurate SDIRK with γ=1−1/√2. Newton uses tolerance 2×10^-12 and at most 25 iterations. The separate adaptive wrapper uses step doubling.

use_when:
- Stiff decay must be damped with second-order stepping, and an RHS/Jacobian are available.
- Implicit-stage convergence and tolerance-refinement comparisons can be monitored.

avoid_when:
- The Jacobian is inconsistent or unconverged Newton stages would be accepted.
- This implementation alone must supply DAE support, strict positivity, event detection or guaranteed global-error control.

assumptions [specified]:
- The target is an ODE y'=f(t,y) represented by a real one-dimensional array, with a consistent Jacobian ∂f/∂y supplied by the caller.
- A=[[γ,0],[1−γ,γ]], b=(1−γ,γ), c=(γ,1), and γ=1−1/√2. This stiffly accurate form returns the last stage.
- With exact stage solves, R(z)=[1+(1−2γ)z]/(1−γz)^2. This γ gives A-stability and R→0 as |z|→∞ in the left half-plane.
- Newton convergence is required at each stage. Distinguish fixed-step integrate from adaptive_sdirk2, which estimates error from (two half steps−one full step)/3 and accepts the two-half-step solution.
Inspected GAMMA, both stage times/coefficients and Newton calls.

units [specified]:
h has time units, f_i has y_i/time, and J_ij has y_i/(y_j×time). Nondimensionalization or component scaling is needed: the fixed Newton tolerance 2×10^-12 does not automatically adapt to arbitrary physical units. Adaptive atol sets state scales and rtol is dimensionless.
Specified componentwise ODE/Jacobian units and tolerance scaling.

boundary_conditions [not-applicable]:
Spatial boundaries do not apply to the ODE time step itself. For semidiscrete PDEs, incorporate boundary conditions and their time dependence consistently into the RHS and Jacobian.
The integrator takes f and jac and does not impose boundaries.

limitations [specified]:
L-stability concerns the linear test equation with accurate stage solves; it guarantees neither large-step accuracy, nonlinear convergence nor positivity. A Newton failure raises in the fixed version and rejects a trial in the adaptive wrapper. Adaptivity uses step doubling, not an embedded pair; rtol/atol control a local error scale, not a guaranteed final global error. General DAEs, mass matrices and events are not implemented.
Separates L-stability, iterative convergence and local-error control.

Review: Read GAMMA, _stage, sdirk2_step, integrate and adaptive_sdirk2 in stiff.py. Inspected test_new_models.py for nonautonomous nonlinear second-order convergence, stiff decay, tolerance comparisons and failure at the trial limit. No new numerical run or rerun was performed.

Not checked:
- Alexander full-text coefficient tables and proofs.
- New runs, general DAEs, stiff-PDE order reduction or Newton convergence for arbitrary systems.

Evidence:
- GAMMA; _stage; sdirk2_step; integrate; adaptive_sdirk2: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/stiff.py
- test_implicit_orders_on_nonautonomous_nonlinear_exact_solution; test_stiff_decay_and_local_error_control: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py

References:
- [original-method / primary-research] Alexander (1977). Diagonally Implicit Runge–Kutta Methods for Stiff O.D.E.’s. — https://doi.org/10.1137/0714068
  Primary paper for two-stage second-order stiff DIRK formulae. The selected coefficient is separately identified from the code and official documentation.
  abstract-and-metadata (2026-11-22); Publisher abstract and metadata; full-text tableau not reviewed.; https://epubs.siam.org/doi/10.1137/0714068
- [formulation / official-documentation] MOOSE. LStableDirk2. — https://mooseframework.inl.gov/source/timeintegrators/LStableDirk2.html
  Official documentation identifies the two-stage second-order L-stable method and its Alexander reference. Equation images were not readable in the text extraction; local coefficients are the implementation evidence.
  full-text (2026-11-22); LStableDirk2 description, Notes and References; equation images were not extracted by the text browser.; https://mooseframework.inl.gov/source/timeintegrators/LStableDirk2.html


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/stiff-integration/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/stiff.py

- Reference: https://doi.org/10.1137/0714068 — Primary source for the two-stage second-order stiffly stable DIRK family; the selected gamma and stability function are established from the local tableau and official supplementary documentation.
- Reference: https://mooseframework.inl.gov/source/timeintegrators/LStableDirk2.html — Official implementation documentation relating the two-stage second-order L-stable DIRK method to Alexander (1977); supplementary to the primary paper, not a replacement for it.

Common execution records: [{"id": "stiff-cosine", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#stiff-cosine-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#stiff-cosine-en"}}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
