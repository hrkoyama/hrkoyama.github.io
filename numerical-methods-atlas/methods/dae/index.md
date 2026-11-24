# Differential-algebraic equations / DAE / 微分代数方程式（DAE）

Status: educational-example

Small fixed examples compare backward Euler and Newton for index-one DAEs, consistent initialization, conservation and constraint drift. Additional fixed examples: Consistent initialization and discrete residuals for an index-one DAE, Robertson conservation DAE and stored official IDA values, Index reduction, constraint drift and explicit stabilization for a pendulum. See each release for assumptions and checked scope.

小規模な固定例で、index-1 DAEの後退Euler・Newton法、整合初期化、保存則と拘束ドリフトを比較します。 追加固定例：index-1 DAEの整合初期化と離散残差、Robertson保存制約DAEと公式IDA保存値、振り子の指数低減・拘束ドリフト・明示安定化。条件と検証範囲は各配布版で確認してください。

Scope is limited to small fixed systems and inputs. The coarse Robertson schedule does not meet the original temporal accuracy/refinement goals; those false decisions are retained and shown. Underlying ODEs based on differentiated constraints can drift from the original constraint. General index handling, large sparse DAEs and convergence for arbitrary inputs are unverified. The preceding limitations describe earlier editions. This additional release: One authored positive branch and fixed BE runs; no IDA execution or general DAE-solver qualification. Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule. No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.

Other names: DAE法, differential algebraic equation, 微分代数方程式法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/dae/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/dae/



- Reference: https://doi.org/10.1109/tct.1971.1083221 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://sundials.readthedocs.io/en/v7.1.1/ida/Mathematics_link.html — Residual form, BDF/Newton and consistent initialization sections selected. Section5.2 is not an IDA version. This authored MMS/BE solver is not IDA.
- Reference: https://github.com/LLNL/sundials/blob/v7.1.1/examples/ida/serial/idaRoberts_dns.c — Read residual/Jacobian, initialization, tolerances and print format. Own first two residual rows have opposite sign and the same zero set.
- Reference: https://github.com/LLNL/sundials/blob/v7.1.1/examples/ida/serial/idaRoberts_dns.out — Selected printed t=0.4 and4 values only, with Decimal rounding intervals. These approximate IDA values are not exact truth; no IDA run is performed here.
- Reference: https://dlmf.nist.gov/22.19 — Selected pendulum formulas, phase and modulus convention. Authored Cartesian conversion uses K-t; SciPy takes parameter m=k². No full chapter reading claimed.
- Reference: https://dlmf.nist.gov/19.8 — Selected AGM/K identity; independent Decimal Machin pi and sine with explicit finite remainders qualify a single fixed modulus.

## Small fixed-input validation supplements

Additional fixed examples: Consistent initialization and discrete residuals for an index-one DAE, Robertson conservation DAE and stored official IDA values, Index reduction, constraint drift and explicit stabilization for a pendulum. See each release for assumptions and checked scope. One authored positive branch and fixed BE runs; no IDA execution or general DAE-solver qualification. Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule. No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.

追加固定例：index-1 DAEの整合初期化と離散残差、Robertson保存制約DAEと公式IDA保存値、振り子の指数低減・拘束ドリフト・明示安定化。条件と検証範囲は各配布版で確認してください。 単一の製造正枝・固定BE計算です。IDA実行や一般DAEソルバーの検証ではありません。 公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。 投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。

- Consistent initialization and discrete residuals for an index-one DAE: https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/
- Robertson conservation DAE and stored official IDA values: https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/
- Index reduction, constraint drift and explicit stabilization for a pendulum: https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json

Common execution records: [{"id": "index1-dae-consistent-initialization", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "robertson-conservation-dae", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "high-index-pendulum", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Other models and larger systems require separately frozen inputs, references and criteria.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Robertson反応系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#robertson-kinetics-ja) (`robertson-kinetics`; robertson-stiff-kinetics)
- [半陽的index-1 DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#index-one-dae-ja) (`index-one-dae`; robertson-stiff-kinetics, index1-dae-consistent-initialization)
- [拘束付き平面振り子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#constrained-pendulum-ja) (`constrained-pendulum`; high-index-pendulum)
- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`; high-index-pendulum)

#### 問題の図 (`method-problems-ja`)

##### [Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja) (`robertson-stiff-kinetics`)

![短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。 保存済みの数値場と参照を用いた図です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

BDF2は同格子BE開始。SDIRK2の非線形段階は重み付き最大残差で判定し、同じ段階内だけJacobian因子を再利用。適応法はRMS倍分割誤差と2半刻みを採用。 解析Jacobian付き固定BE/Newtonを使い、質量の投影・濃度クリップはしません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#code-ja)

- [Robertson保存制約DAEと公式IDA保存値](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja) (`robertson-conservation-dae`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

Robertsonの保存制約DAEと全ODEを同じ固定時間格子で比較し、公式IDA保存値を別に照合します。 初回は元の時間精度・細分化目標4件が未達でした。

##### [index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja) (`index1-dae-consistent-initialization`)

![既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。 保存配列から作図。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-preview.png)

連立Newtonと同じ尺度のArmijo線探索を用い、特異な初期推測は修復せず記録します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja#code-ja)

- [index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja) (`index1-dae-consistent-initialization`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。

##### [拘束付き振り子](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja) (`high-index-pendulum`)

![位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。 保存配列から作図。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png)

指数低減ODEと臨界拘束誤差拡張を固定RK4で積分し、拘束仕事も同じ段で積分します。 独自のスカラーNewton位置拘束、RATTLE終端接線impulse、SHAKE位置対。SHAKEの運動量は内部点だけで中心化し、端点を作りません。 SHAKEのsolves列はeta、eta/h^2、位置残差、Newton更新数です。列1は一律にeta/h^2ですが、初回半刻みの物理乗数は2eta/h^2、以後の位置Verletではeta/h^2です。逆位置対はすべて後者です。判定と図はこの列1を使いません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#code-ja)

- [振り子の指数低減・拘束ドリフト・明示安定化](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja) (`high-index-pendulum`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#references-ja) (`robertson-stiff-kinetics`)

- [Robertson反応系の初期剛性と実誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-stiff-kinetics-ja) (`robertson-stiff-kinetics`; 同じ問題の参照; 有限格子の数値参照)

保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja#robertson-stiff-kinetics-ja-measurements)

- [Robertson保存制約DAEと公式IDA保存値](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-conservation-dae-ja) (`robertson-conservation-dae`; 同じ問題の参照; 有限格子の数値参照)

公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja#robertson-conservation-dae-ja-measurements)

##### [index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja#references-ja) (`index1-dae-consistent-initialization`)

- [index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-index1-dae-consistent-initialization-ja) (`index1-dae-consistent-initialization`; 同じ問題の参照; 製造解)

単一の製造正枝・固定BE計算です。IDA実行や一般DAEソルバーの検証ではありません。

[既存の参照図](/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja#index1-dae-consistent-initialization-ja-measurements)

##### [拘束付き振り子](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#references-ja) (`high-index-pendulum`)

- [振り子の指数低減・拘束ドリフト・明示安定化](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-high-index-pendulum-ja) (`high-index-pendulum`; 同じ問題の参照; 半解析参照)

投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。

[既存の参照図](/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja#high-index-pendulum-ja-measurements)

- [SHAKEとRATTLE：拘束と運動量の違い](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shake-rattle-pendulum-ja) (`shake-rattle-pendulum`; 同じ問題の参照; 半解析参照)

原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。

[既存の参照図](/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja#shake-rattle-pendulum-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/dae/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Robertson保存制約DAEと公式IDA保存値 (`robertson-conservation-dae`)

[Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

Robertsonの保存制約DAEと全ODEを同じ固定時間格子で比較し、公式IDA保存値を別に照合します。 初回は元の時間精度・細分化目標4件が未達でした。

##### index-1 DAEの整合初期化と離散残差 (`index1-dae-consistent-initialization`)

[index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。

##### 振り子の指数低減・拘束ドリフト・明示安定化 (`high-index-pendulum`)

[拘束付き振り子](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-24/dae-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/run.py)
- [/code/validated-examples/2026-11-24/dae-controls/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/models.py)
- [/code/validated-examples/2026-11-24/dae-controls/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/newton.py)
- [/code/validated-examples/2026-11-24/dae-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/experiments.py)
- [/code/validated-examples/2026-11-24/dae-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/io_contract.py)
- [/code/validated-examples/2026-11-24/dae-controls/references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/references.py)
- [/code/validated-examples/2026-11-24/dae-controls/reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/reporting.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-24/dae-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_cases.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_serialization.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Robertson chemical kinetics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#robertson-kinetics-en) (`robertson-kinetics`; robertson-stiff-kinetics)
- [Semi-explicit index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#index-one-dae-en) (`index-one-dae`; robertson-stiff-kinetics, index1-dae-consistent-initialization)
- [Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#constrained-pendulum-en) (`constrained-pendulum`; high-index-pendulum)
- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`; high-index-pendulum)

#### Problem figures (`method-problems-en`)

##### [Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en) (`robertson-stiff-kinetics`)

![Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references. This preview reads saved numerical fields and references only. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

BDF2 starts with backward Euler on the same grid. SDIRK2 stages use a weighted maximum residual and reuse Jacobian factors only within one stage. Adaptive steps use an RMS step-doubling estimate and accept the two-half-step result. Use fixed BE/Newton with analytic Jacobians and no mass projection or concentration clipping.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#code-en)

- [Robertson conservation DAE and stored official IDA values](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en) (`robertson-conservation-dae`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. The first retained run missed four original time-accuracy and refinement goals.

##### [Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en) (`index1-dae-consistent-initialization`)

![Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch. Drawn from saved arrays. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-preview.png)

Use coupled Newton with an Armijo search in the same scaled norm, retaining rather than repairing a singular initial guess.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en#code-en)

- [Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en) (`index1-dae-consistent-initialization`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch.

##### [Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en) (`high-index-pendulum`)

![Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts. Drawn from saved arrays. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png)

Advance the index-reduced ODE and a critical constraint-error extension with fixed RK4, integrating constraint work at the same stages. Original scalar Newton position constraints, RATTLE final tangent impulses and SHAKE position pairs. SHAKE momentum is centered only at interior nodes; endpoint momenta are absent. SHAKE solves columns are eta, eta/h^2, position residual and Newton updates. Column1 uses the uniform recurrence normalization eta/h^2. For the first constrained half-step startup, the physical multiplier is 2*eta/h^2; later full position-Verlet steps use eta/h^2. Reverse-pair steps all use the later recurrence convention. RATTLE has its separate five-column normalization. No scientific gate or plot uses SHAKE column1.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#code-en)

- [Index reduction, constraint drift and explicit stabilization for a pendulum](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en) (`high-index-pendulum`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts.


#### Exact / reference solutions (`method-references-en`)

##### [Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#references-en) (`robertson-stiff-kinetics`)

- [Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-stiff-kinetics-en) (`robertson-stiff-kinetics`; Same-problem reference; Finite-grid numerical reference)

Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound.

[Existing reference profile](/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en#robertson-stiff-kinetics-en-measurements)

- [Robertson conservation DAE and stored official IDA values](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-conservation-dae-en) (`robertson-conservation-dae`; Same-problem reference; Finite-grid numerical reference)

Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.

[Existing reference profile](/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en#robertson-conservation-dae-en-measurements)

##### [Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en#references-en) (`index1-dae-consistent-initialization`)

- [Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-index1-dae-consistent-initialization-en) (`index1-dae-consistent-initialization`; Same-problem reference; Manufactured solution)

One authored positive branch and fixed BE runs; no IDA execution or general DAE-solver qualification.

[Existing reference profile](/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en#index1-dae-consistent-initialization-en-measurements)

##### [Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#references-en) (`high-index-pendulum`)

- [Index reduction, constraint drift and explicit stabilization for a pendulum](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-high-index-pendulum-en) (`high-index-pendulum`; Same-problem reference; Semi-analytic reference)

No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.

[Existing reference profile](/numerical-methods-atlas/validation/high-index-pendulum/?lang=en#high-index-pendulum-en-measurements)

- [SHAKE and RATTLE: constraints and momentum ownership](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shake-rattle-pendulum-en) (`shake-rattle-pendulum`; Same-problem reference; Semi-analytic reference)

Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency.

[Existing reference profile](/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en#shake-rattle-pendulum-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/dae/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Robertson conservation DAE and stored official IDA values (`robertson-conservation-dae`)

[Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. The first retained run missed four original time-accuracy and refinement goals.

##### Consistent initialization and discrete residuals for an index-one DAE (`index1-dae-consistent-initialization`)

[Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch.

##### Index reduction, constraint drift and explicit stabilization for a pendulum (`high-index-pendulum`)

[Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

###### Related source

- [/code/validated-examples/2026-11-24/dae-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/run.py)
- [/code/validated-examples/2026-11-24/dae-controls/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/models.py)
- [/code/validated-examples/2026-11-24/dae-controls/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/newton.py)
- [/code/validated-examples/2026-11-24/dae-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/experiments.py)
- [/code/validated-examples/2026-11-24/dae-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/io_contract.py)
- [/code/validated-examples/2026-11-24/dae-controls/references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/references.py)
- [/code/validated-examples/2026-11-24/dae-controls/reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/reporting.py)

###### Package tests

- [/code/validated-examples/2026-11-24/dae-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_cases.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_serialization.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
