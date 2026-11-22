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

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

対応する方程式一覧の項目は未登録です。

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


#### 厳密解・参照解 (`method-references-ja`)

##### [硬い余弦追従ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=ja#references-ja) (`stiff-cosine`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [有理関数を厳密解に持つ非線形・非自律ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=ja#references-ja) (`nonlinear-rational-ode`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

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

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/stiff.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/stiff.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_new_models.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

No corresponding equation-registry entry is registered.

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


#### Exact / reference solutions (`method-references-en`)

##### [Stiff cosine-tracking ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=en#references-en) (`stiff-cosine`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Nonlinear nonautonomous ODE with rational exact solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=en#references-en) (`nonlinear-rational-ode`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

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

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/stiff.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/stiff.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_new_models.py
```
