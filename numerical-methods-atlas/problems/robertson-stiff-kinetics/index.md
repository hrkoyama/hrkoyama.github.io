# Robertson反応系：ODEと保存則DAE / Robertson kinetics: ODE and conservation DAE

https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/

## 日本語

[短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。 保存済みの数値場と参照を用いた図です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-ode-adaptivity/#robertson-stiff-kinetics) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#robertson-stiff-kinetics)

### 方程式・問題の定義

無次元3成分、初期値(1,0,0)、T=.4。固定512/1024/2048刻みと2許容誤差の適応法で計8run。 モデル時間0から4。中間種と残差の尺度は1e-4。公式印字値の丸め幅と数値誤差を区別します。

#### [Robertson反応系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#robertson-kinetics-ja)

$$
\dot y_1=-0.04y_1+10^4y_2y_3,\quad\dot y_2=0.04y_1-10^4y_2y_3-3\times10^7y_2^2,\quad\dot y_3=3\times10^7y_2^2
$$

$$
y_1+y_2+y_3=1
$$

3成分の硬い反応ODEと、保存則を代数式に置き換えたindex-1 DAEを区別して比較します。

#### [半陽的index-1 DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#index-one-dae-ja)

$$
\dot y=f(t,y,z),\qquad0=g(t,y,z),\qquad\det g_z\ne0
$$

整合初期化と微分・代数残差を扱う小規模な固定例です。一般DAEソルバーの完成を意味しません。

#### Robertson反応系の初期剛性と実誤差

補助実行例 · 実行例の定義・検証式

$$
\dot y_1=-0.04y_1+10^4y_2y_3,\quad\dot y_2=-\dot y_1-3\!\times\!10^7y_2^2,\quad\dot y_3=3\!\times\!10^7y_2^2
$$

$$
\|r\|_{w,\infty}=\max_i|r_i|/w_i,\quad e_{\rm dbl}=(y_{h/2,h/2}-y_h)/3
$$

短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。

#### Robertson保存制約DAEと公式IDA保存値

補助実行例 · 実行例の定義・検証式

$$
F1=ydot1+0.04*y1-1e4*y2*y3; F2=ydot2-0.04*y1+1e4*y2*y3+3e7*y2^2; F3=y1+y2+y3-1
$$

$$
M=diag(1,1,0)
$$

Robertsonの保存制約DAEと全ODEを同じ固定時間格子で比較し、公式IDA保存値を別に照合します。 初回は元の時間精度・細分化目標4件が未達でした。

### 厳密解・参照解

22共通時刻の実誤差、全受理時刻の質量/最小値、真の段階残差、実RHS/Jacobian/因子/solve数を別判定します。 元39目標をすべて実測し、精度・細分化4目標の未達を変更せず研究結果として記録します。他35条件と独立参照・保存配列からの判定再計算は必須です。

#### [Robertson反応系の初期剛性と実誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja#robertson-stiff-kinetics-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

\dot y_1=-0.04y_1+10^4y_2y_3,\quad\dot y_2=-\dot y_1-3\!\times\!10^7y_2^2,\quad\dot y_3=3\!\times\!10^7y_2^2;\quad \|r\|_{w,\infty}=\max_i|r_i|/w_i,\quad e_{\rm dbl}=(y_{h/2,h/2}-y_h)/3

無次元3成分、初期値(1,0,0)、T=.4。固定512/1024/2048刻みと2許容誤差の適応法で計8run。

保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。

#### [Robertson保存制約DAEと公式IDA保存値](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja#robertson-conservation-dae-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

F1=ydot1+0.04*y1-1e4*y2*y3; F2=ydot2-0.04*y1+1e4*y2*y3+3e7*y2^2; F3=y1+y2+y3-1;\quad M=diag(1,1,0)

モデル時間0から4。中間種と残差の尺度は1e-4。公式印字値の丸め幅と数値誤差を区別します。

公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。

#### Robertson反応系の初期剛性と実誤差

22共通時刻の実誤差、全受理時刻の質量/最小値、真の段階残差、実RHS/Jacobian/因子/solve数を別判定します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja)

#### Robertson保存制約DAEと公式IDA保存値

元39目標をすべて実測し、精度・細分化4目標の未達を変更せず研究結果として記録します。他35条件と独立参照・保存配列からの判定再計算は必須です。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja)

### 計算法

BDF2は同格子BE開始。SDIRK2の非線形段階は重み付き最大残差で判定し、同じ段階内だけJacobian因子を再利用。適応法はRMS倍分割誤差と2半刻みを採用。 解析Jacobian付き固定BE/Newtonを使い、質量の投影・濃度クリップはしません。

- [BDF2](https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [L安定なSDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [適応SDIRK2／ステップ倍分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [微分代数方程式（DAE）](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [後退Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Robertson反応系の初期剛性と実誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja)

補助実行例

短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。

無次元3成分、初期値(1,0,0)、T=.4。固定512/1024/2048刻みと2許容誤差の適応法で計8run。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)

#### [Robertson保存制約DAEと公式IDA保存値](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja)

補助実行例

Robertsonの保存制約DAEと全ODEを同じ固定時間格子で比較し、公式IDA保存値を別に照合します。 初回は元の時間精度・細分化目標4件が未達でした。

モデル時間0から4。中間種と残差の尺度は1e-4。公式印字値の丸め幅と数値誤差を区別します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/dae-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/run.py)
- [/code/validated-examples/2026-11-24/dae-controls/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/models.py)
- [/code/validated-examples/2026-11-24/dae-controls/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/newton.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_cases.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_serialization.py)

## English

[Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references. This preview reads saved numerical fields and references only. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-ode-adaptivity/#robertson-stiff-kinetics) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#robertson-stiff-kinetics-en)

### Equations and problem definitions

A nondimensional three-species system starts at (1, 0, 0) and ends at T = 0.4. The fixed methods use 512, 1024 and 2048 steps; two adaptive tolerance settings bring the total to eight runs. Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct.

#### [Robertson chemical kinetics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#robertson-kinetics-en)

$$
\dot y_1=-0.04y_1+10^4y_2y_3,\quad\dot y_2=0.04y_1-10^4y_2y_3-3\times10^7y_2^2,\quad\dot y_3=3\times10^7y_2^2
$$

$$
y_1+y_2+y_3=1
$$

Distinguish the stiff three-species ODE from an index-one DAE obtained by replacing one equation with conservation.

#### [Semi-explicit index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#index-one-dae-en)

$$
\dot y=f(t,y,z),\qquad0=g(t,y,z),\qquad\det g_z\ne0
$$

Small fixed examples expose consistent initialization and separate differential/algebraic residuals; this is not a general-purpose DAE solver.

#### Robertson kinetics: initial stiffness and actual error

Supplementary execution example · Example definition or validation formula

$$
\dot y_1=-0.04y_1+10^4y_2y_3,\quad\dot y_2=-\dot y_1-3\!\times\!10^7y_2^2,\quad\dot y_3=3\!\times\!10^7y_2^2
$$

$$
\|r\|_{w,\infty}=\max_i|r_i|/w_i,\quad e_{\rm dbl}=(y_{h/2,h/2}-y_h)/3
$$

Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references.

#### Robertson conservation DAE and stored official IDA values

Supplementary execution example · Example definition or validation formula

$$
F1=ydot1+0.04*y1-1e4*y2*y3; F2=ydot2-0.04*y1+1e4*y2*y3+3e7*y2^2; F3=y1+y2+y3-1
$$

$$
M=diag(1,1,0)
$$

Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. The first retained run missed four original time-accuracy and refinement goals.

### Exact and reference solutions

Check actual errors at 22 common times, mass and minimum values at every accepted state, true stage residuals, and actual RHS, Jacobian, factorization and linear-solve counts separately. Evaluate all 39 original targets, retaining the four unmet accuracy/refinement goals as study outcomes. The other 35 requirements, independent references and faithful saved-array recomputation remain mandatory.

#### [Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en#robertson-stiff-kinetics-en-measurements)

Finite-grid numerical reference · Reference for the same problem

\dot y_1=-0.04y_1+10^4y_2y_3,\quad\dot y_2=-\dot y_1-3\!\times\!10^7y_2^2,\quad\dot y_3=3\!\times\!10^7y_2^2;\quad \|r\|_{w,\infty}=\max_i|r_i|/w_i,\quad e_{\rm dbl}=(y_{h/2,h/2}-y_h)/3

A nondimensional three-species system starts at (1, 0, 0) and ends at T = 0.4. The fixed methods use 512, 1024 and 2048 steps; two adaptive tolerance settings bring the total to eight runs.

Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound.

#### [Robertson conservation DAE and stored official IDA values](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en#robertson-conservation-dae-en-measurements)

Finite-grid numerical reference · Reference for the same problem

F1=ydot1+0.04*y1-1e4*y2*y3; F2=ydot2-0.04*y1+1e4*y2*y3+3e7*y2^2; F3=y1+y2+y3-1;\quad M=diag(1,1,0)

Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct.

Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.

#### Robertson kinetics: initial stiffness and actual error

Check actual errors at 22 common times, mass and minimum values at every accepted state, true stage residuals, and actual RHS, Jacobian, factorization and linear-solve counts separately.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en)

#### Robertson conservation DAE and stored official IDA values

Evaluate all 39 original targets, retaining the four unmet accuracy/refinement goals as study outcomes. The other 35 requirements, independent references and faithful saved-array recomputation remain mandatory.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en)

### Numerical methods

BDF2 starts with backward Euler on the same grid. SDIRK2 stages use a weighted maximum residual and reuse Jacobian factors only within one stage. Adaptive steps use an RMS step-doubling estimate and accept the two-half-step result. Use fixed BE/Newton with analytic Jacobians and no mass projection or concentration clipping.

- [BDF2](https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [L-stable SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Adaptive SDIRK2 / step doubling](https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Differential-algebraic equations / DAE](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Backward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en)

Supplementary execution example

Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references.

A nondimensional three-species system starts at (1, 0, 0) and ends at T = 0.4. The fixed methods use 512, 1024 and 2048 steps; two adaptive tolerance settings bring the total to eight runs.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)

#### [Robertson conservation DAE and stored official IDA values](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en)

Supplementary execution example

Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. The first retained run missed four original time-accuracy and refinement goals.

Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/dae-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/run.py)
- [/code/validated-examples/2026-11-24/dae-controls/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/models.py)
- [/code/validated-examples/2026-11-24/dae-controls/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/newton.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_cases.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_serialization.py)
