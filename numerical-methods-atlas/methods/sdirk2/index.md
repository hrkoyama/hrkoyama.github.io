# L-stable SDIRK2 / L安定なSDIRK2

Status: educational-example

A two-stage second-order implicit Runge–Kutta method for stiff ODE decay. The release uses stiffly accurate L-stable SDIRK with γ=1−1/√2 and Newton stage solves; a separate wrapper adds step-doubling local-error control. Additional fixed examples: Robertson kinetics: initial stiffness and actual error, Van der Pol: an early stiffness transition. See each release for assumptions and checked scope. Fixed educational executions: Enzyme conservation and QSSA.

硬い常微分方程式の減衰を扱う2段2次の陰的Runge–Kutta法。公開版はγ=1−1/√2のstiffly accurateなL安定SDIRKで、各段階にNewton法を用い、別のラッパーでステップ倍化による局所誤差制御を行う。 追加固定例：Robertson反応系の初期剛性と実誤差、van der Polの短時間剛性遷移。条件と検証範囲は各配布版で確認してください。 固定した教育用実行例：酵素反応の保存と準定常近似。

L-stability concerns the linear test equation with accurate stage solves; it guarantees neither large-step accuracy, nonlinear convergence nor positivity. A Newton failure raises in the fixed version and rejects a trial in the adaptive wrapper. Adaptivity uses step doubling, not an embedded pair; rtol/atol control a local error scale, not a guaranteed final global error. General DAEs, mass matrices and events are not implemented. The preceding limitations describe earlier editions. This additional release: Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound. This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope.

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
L安定性は正確な段階解を前提とする線形試験方程式の性質であり、大刻みの精度・非線形収束・正値性を保証しない。Newton失敗時は固定版が例外、適応版が試行棄却を行う。埋込み対ではなくステップ倍化で、rtol/atolは局所誤差尺度であり最終大域誤差の保証ではない。一般DAE、質量行列、イベント処理は未実装。 上記の制限は既存配布版の範囲です。今回の追加配布版：保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。 測定後の報告範囲変更で、数値的な修復ではありません。初回誤差4.535633779e-5は元目標2e-5を超えます。局所rtolは大域誤差を保証せず、報告検証の合格は全元目標の達成ではありません。大μ全周期は対象外です。
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
L-stability concerns the linear test equation with accurate stage solves; it guarantees neither large-step accuracy, nonlinear convergence nor positivity. A Newton failure raises in the fixed version and rejects a trial in the adaptive wrapper. Adaptivity uses step doubling, not an embedded pair; rtol/atol control a local error scale, not a guaranteed final global error. General DAEs, mass matrices and events are not implemented. The preceding limitations describe earlier editions. This additional release: Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound. This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope.
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

## Small fixed-input validation supplements

Additional fixed examples: Robertson kinetics: initial stiffness and actual error, Van der Pol: an early stiffness transition. See each release for assumptions and checked scope. Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound. This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope.

追加固定例：Robertson反応系の初期剛性と実誤差、van der Polの短時間剛性遷移。条件と検証範囲は各配布版で確認してください。 保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。 測定後の報告範囲変更で、数値的な修復ではありません。初回誤差4.535633779e-5は元目標2e-5を超えます。局所rtolは大域誤差を保証せず、報告検証の合格は全元目標の達成ではありません。大μ全周期は対象外です。

- Robertson kinetics: initial stiffness and actual error: https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/
- Van der Pol: an early stiffness transition: https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json

- Enzyme conservation and QSSA: https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json

Common execution records: [{"id": "stiff-cosine", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#stiff-cosine-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#stiff-cosine-en"}}, {"id": "robertson-stiff-kinetics", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "van-der-pol-stiff-transition", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "enzyme-qssa", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Robertson反応系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#robertson-kinetics-ja) (`robertson-kinetics`; robertson-stiff-kinetics)
- [半陽的index-1 DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#index-one-dae-ja) (`index-one-dae`; robertson-stiff-kinetics)
- [van der Pol振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#van-der-pol-ja) (`van-der-pol`; van-der-pol-stiff-transition)
- [Michaelis–Mentenと完全酵素反応系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-enzyme-ja) (`bio-enzyme`; enzyme-qssa)

#### 問題の図 (`method-problems-ja`)

##### [硬い余弦追従ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=ja) (`stiff-cosine`)

![保存済みの硬い余弦追従ODEの固定刻み誤差。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/stiff-cosine.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=ja#code-ja)

- [硬い余弦追従ODE：SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=ja) (`stiff-cosine`) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

既存のL安定2段SDIRK2でy′=−1000(y−cos t)−sin t、y(0)=1をt=1まで解く。解析解、固定刻み細分化、別の強減衰1段問題を検査。

##### [有理関数を厳密解に持つ非線形・非自律ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=ja) (`nonlinear-rational-ode`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-ode.png)

公開検査に後退Euler・BDF2・SDIRK2・IMEX Eulerがあり、保存プレビューはSDIRK2です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja) (`robertson-stiff-kinetics`)

![短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。 保存済みの数値場と参照を用いた図です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

BDF2は同格子BE開始。SDIRK2の非線形段階は重み付き最大残差で判定し、同じ段階内だけJacobian因子を再利用。適応法はRMS倍分割誤差と2半刻みを採用。 解析Jacobian付き固定BE/Newtonを使い、質量の投影・濃度クリップはしません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#code-ja)

- [Robertson反応系の初期剛性と実誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja) (`robertson-stiff-kinetics`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。

##### [van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja) (`van-der-pol-stiff-transition`)

![保存済みの固定刻み比較と局所/大域誤差の区別。初回208/209で、μ=1適応法の大域目標2e-5は未達のまま保持します。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition-preview.png)

BDF2/SDIRK2と倍分割適応法。解析Jacobian・段階内だけの因子再利用・失敗時の候補保存を実装します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja#code-ja)

- [van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja) (`van-der-pol-stiff-transition`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

局所制御と大域誤差を分離します。初回は元209目標中208達成で、μ=1の厳しい適応設定は大域目標2e-5に未達でした。

##### [酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja) (`enzyme-qssa`)

![全4状態と準定常近似を比較し、初期層と積分誤差を分けます。 保存値だけを描画します。 時間・濃度・個体数の軸は空間次元ではありません。率は教育用で疾病・実験予測ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa-preview.png)

全4状態をSDIRK2のstep doublingで積分し、各段のNewton法では同じ重み付きL∞残差とArmijo条件を使います。縮約Michaelis–Menten式はθ上の別RK4計算で求め、全系の積分誤差と近似モデル誤差を混同しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja#code-ja)

- [酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja) (`enzyme-qssa`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

全4状態と準定常近似を比較し、初期層と積分誤差を分けます。


#### 厳密解・参照解 (`method-references-ja`)

##### [硬い余弦追従ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=ja#references-ja) (`stiff-cosine`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [有理関数を厳密解に持つ非線形・非自律ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=ja#references-ja) (`nonlinear-rational-ode`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#references-ja) (`robertson-stiff-kinetics`)

- [Robertson反応系の初期剛性と実誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-stiff-kinetics-ja) (`robertson-stiff-kinetics`; 同じ問題の参照; 有限格子の数値参照)

保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja#robertson-stiff-kinetics-ja-measurements)

- [Robertson保存制約DAEと公式IDA保存値](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-conservation-dae-ja) (`robertson-conservation-dae`; 同じ問題の参照; 有限格子の数値参照)

公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja#robertson-conservation-dae-ja-measurements)

##### [van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja#references-ja) (`van-der-pol-stiff-transition`)

- [van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-van-der-pol-stiff-transition-ja) (`van-der-pol-stiff-transition`; 同じ問題の参照; 有限格子の数値参照)

測定後の報告範囲変更で、数値的な修復ではありません。初回誤差4.535633779e-5は元目標2e-5を超えます。局所rtolは大域誤差を保証せず、報告検証の合格は全元目標の達成ではありません。大μ全周期は対象外です。

[既存の参照図](/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja#van-der-pol-stiff-transition-ja-measurements)

##### [酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja#references-ja) (`enzyme-qssa`)

- [酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-enzyme-qssa-ja) (`enzyme-qssa`; 同じ問題の参照; 有限格子の数値参照)

2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。

[既存の参照図](/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja#enzyme-qssa-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 硬い余弦追従ODE：SDIRK2 (`stiff-cosine`)

[硬い余弦追従ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/stiff-cosine.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

既存のL安定2段SDIRK2でy′=−1000(y−cos t)−sin t、y(0)=1をt=1まで解く。解析解、固定刻み細分化、別の強減衰1段問題を検査。

##### Robertson反応系の初期剛性と実誤差 (`robertson-stiff-kinetics`)

[Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。

##### van der Polの短時間剛性遷移 (`van-der-pol-stiff-transition`)

[van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

局所制御と大域誤差を分離します。初回は元209目標中208達成で、μ=1の厳しい適応設定は大域目標2e-5に未達でした。

##### 酵素反応の保存と準定常近似 (`enzyme-qssa`)

[酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

全4状態と準定常近似を比較し、初期層と積分誤差を分けます。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/stiff.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py)
- [/code/validated-examples/2026-11-25/small-models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/run.py)
- [/code/validated-examples/2026-11-25/small-models/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/experiments.py)
- [/code/validated-examples/2026-11-25/small-models/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/io_utils.py)
- [/code/validated-examples/2026-11-25/small-models/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/biology.py)
- [/code/validated-examples/2026-11-25/small-models/pinn.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/pinn.py)
- [/code/validated-examples/2026-11-25/small-models/fno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/fno.py)
- [/code/validated-examples/2026-11-25/small-models/data_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/data_family.py)
- [/code/validated-examples/2026-11-25/small-models/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/oracles.py)
- [/code/validated-examples/2026-11-25/small-models/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/qualify.py)
- [/code/validated-examples/2026-11-25/small-models/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/reference_models.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)
- [/code/validated-examples/2026-11-25/small-models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/test_models.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_new_models.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Robertson chemical kinetics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#robertson-kinetics-en) (`robertson-kinetics`; robertson-stiff-kinetics)
- [Semi-explicit index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#index-one-dae-en) (`index-one-dae`; robertson-stiff-kinetics)
- [Van der Pol oscillator](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#van-der-pol-en) (`van-der-pol`; van-der-pol-stiff-transition)
- [Michaelis–Menten and full enzyme kinetics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-enzyme-en) (`bio-enzyme`; enzyme-qssa)

#### Problem figures (`method-problems-en`)

##### [Stiff cosine-tracking ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=en) (`stiff-cosine`)

![Stored fixed-step errors for the stiff cosine-tracking ODE.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/stiff-cosine.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=en#code-en)

- [Stiff cosine-tracking ODE: SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=en) (`stiff-cosine`) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Use the existing two-stage L-stable SDIRK2 for y'=-1000(y-cos(t))-sin(t), y(0)=1 up to t=1. Check its analytic solution, fixed-step refinement and a separate very stiff one-step decay.

##### [Nonlinear nonautonomous ODE with rational exact solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=en) (`nonlinear-rational-ode`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-ode.png)

Public checks include backward Euler, BDF2, SDIRK2 and IMEX Euler; the saved preview uses SDIRK2.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en) (`robertson-stiff-kinetics`)

![Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references. This preview reads saved numerical fields and references only. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

BDF2 starts with backward Euler on the same grid. SDIRK2 stages use a weighted maximum residual and reuse Jacobian factors only within one stage. Adaptive steps use an RMS step-doubling estimate and accept the two-half-step result. Use fixed BE/Newton with analytic Jacobians and no mass projection or concentration clipping.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#code-en)

- [Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en) (`robertson-stiff-kinetics`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references.

##### [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en) (`van-der-pol-stiff-transition`)

![Saved fixed-step comparisons and the local/global error distinction. The first study met 208/209 targets; the unmet mu = 1 adaptive global goal of 2e-5 remains recorded. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition-preview.png)

Use actual BDF2, SDIRK2 and adaptive step doubling, analytic Jacobians, factor reuse within each implicit stage, and retained candidates on failure.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en#code-en)

- [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en) (`van-der-pol-stiff-transition`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

Separate local control from global error. The first study met 208 of 209 original targets; the mu = 1 tight adaptive run missed the 2e-5 global goal.

##### [Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en) (`enzyme-qssa`)

![Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism. This figure reads saved data only. Time, concentrations and populations do not define a spatial dimension. The rates are educational, not disease or experimental predictions.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa-preview.png)

Integrate all four states with SDIRK2 step doubling, using the same weighted L∞ residual for Newton convergence and Armijo backtracking. Evolve the reduced Michaelis–Menten equation separately with RK4 in θ, keeping integration error distinct from model-reduction error.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en#code-en)

- [Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en) (`enzyme-qssa`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism.


#### Exact / reference solutions (`method-references-en`)

##### [Stiff cosine-tracking ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=en#references-en) (`stiff-cosine`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Nonlinear nonautonomous ODE with rational exact solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=en#references-en) (`nonlinear-rational-ode`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#references-en) (`robertson-stiff-kinetics`)

- [Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-stiff-kinetics-en) (`robertson-stiff-kinetics`; Same-problem reference; Finite-grid numerical reference)

Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound.

[Existing reference profile](/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en#robertson-stiff-kinetics-en-measurements)

- [Robertson conservation DAE and stored official IDA values](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-conservation-dae-en) (`robertson-conservation-dae`; Same-problem reference; Finite-grid numerical reference)

Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.

[Existing reference profile](/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en#robertson-conservation-dae-en-measurements)

##### [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en#references-en) (`van-der-pol-stiff-transition`)

- [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-van-der-pol-stiff-transition-en) (`van-der-pol-stiff-transition`; Same-problem reference; Finite-grid numerical reference)

This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope.

[Existing reference profile](/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en#van-der-pol-stiff-transition-en-measurements)

##### [Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en#references-en) (`enzyme-qssa`)

- [Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-enzyme-qssa-en) (`enzyme-qssa`; Same-problem reference; Finite-grid numerical reference)

These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction.

[Existing reference profile](/numerical-methods-atlas/validation/enzyme-qssa/?lang=en#enzyme-qssa-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/stiff-integration/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Stiff cosine-tracking ODE: SDIRK2 (`stiff-cosine`)

[Stiff cosine-tracking ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/stiff-cosine.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Use the existing two-stage L-stable SDIRK2 for y'=-1000(y-cos(t))-sin(t), y(0)=1 up to t=1. Check its analytic solution, fixed-step refinement and a separate very stiff one-step decay.

##### Robertson kinetics: initial stiffness and actual error (`robertson-stiff-kinetics`)

[Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references.

##### Van der Pol: an early stiffness transition (`van-der-pol-stiff-transition`)

[Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

Separate local control from global error. The first study met 208 of 209 original targets; the mu = 1 tight adaptive run missed the 2e-5 global goal.

##### Enzyme conservation and QSSA (`enzyme-qssa`)

[Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/stiff.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py)
- [/code/validated-examples/2026-11-25/small-models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/run.py)
- [/code/validated-examples/2026-11-25/small-models/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/experiments.py)
- [/code/validated-examples/2026-11-25/small-models/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/io_utils.py)
- [/code/validated-examples/2026-11-25/small-models/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/biology.py)
- [/code/validated-examples/2026-11-25/small-models/pinn.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/pinn.py)
- [/code/validated-examples/2026-11-25/small-models/fno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/fno.py)
- [/code/validated-examples/2026-11-25/small-models/data_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/data_family.py)
- [/code/validated-examples/2026-11-25/small-models/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/oracles.py)
- [/code/validated-examples/2026-11-25/small-models/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/qualify.py)
- [/code/validated-examples/2026-11-25/small-models/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/reference_models.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)
- [/code/validated-examples/2026-11-25/small-models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/test_models.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_new_models.py
```
