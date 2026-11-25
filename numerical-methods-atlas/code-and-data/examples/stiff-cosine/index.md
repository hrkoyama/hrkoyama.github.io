# Stiff cosine-tracking ODE: SDIRK2 / 硬い余弦追従ODE：SDIRK2

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: stiff-cosine

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json

## ja

硬い余弦追従問題の解析解と刻み細分化を比べ、別の強減衰問題でL安定な応答を確認する。

**使用手法**

- [L安定なSDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja) (`sdirk2`)

**方程式**

[この固定入力の問題式と条件](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-stiff-cosine-ja)

既存2段SDIRK2を使う時間初期値問題。主問題はt=1、1000/2000/4000刻み。46モデル台帳とは別の実行例の式で、熱PDEや汎用硬い系の新規モデルとして数えない。

$$
y'=-1000(y-\cos t)-\sin t,\qquad y(0)=1,\qquad y_{\rm ref}(t)=\cos t
$$

$$
z'=-10^8z,\qquad z(0)=1\quad\text{(separate one-step decay check)}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![保存済みの硬い余弦追従ODEの固定刻み誤差。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/stiff-cosine.png)

この問題の代表図です。格子・時刻・初期値などは、この実行例の固定入力と異なる場合があります。

[硬い余弦追従ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=ja) (`stiff-cosine`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=ja#stiff-cosine-ja-validation)

CSVは最細刻みの数値解・解析解・絶対誤差。観測次数は全時刻最大誤差から計算。旧保存例の粗格子で約1台になる挙動と、今回の解像した刻みでの次数を混同しない。

- [硬い余弦追従ODE：SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-stiff-cosine-exact-ja) (`stiff-cosine-exact`; 同じ問題の参照 · 解析参照)

既存の固定入力・保存結果に対応する解析参照カードを追加。解析式、点・時刻・動径の標本化、配布版SHAと実行コードを相互に辿れます。過去の計算を再実行した記録ではありません。


### scope

既存のL安定2段SDIRK2でy′=−1000(y−cos t)−sin t、y(0)=1をt=1まで解く。解析解、固定刻み細分化、別の強減衰1段問題を検査。

### assumptions

rate=1000、1000/2000/4000ステップでrate*h=1,0.5,0.25。固定γ=1−1/√2と既存Newton段階解法を使用。別の減衰はy′=−10⁸y、y(0)=1、h=1。適応刻み法ではない。

### units

無次元時間と状態。rateの次元は逆時間、rate*hは無次元。

### boundaries

初期値問題で空間境界なし。終端時刻を必ず含む等間隔列。

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/stiff-cosine.json
Input SHA-256: 53efd235fef8241ed7774f37696b97ef466217ae3244afa1430389c6fa23cd30
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/stiff-cosine.json --output output-stiff-cosine
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/stiff-cosine/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/stiff-cosine/solution.csv

CSVは最細刻みの数値解・解析解・絶対誤差。観測次数は全時刻最大誤差から計算。旧保存例の粗格子で約1台になる挙動と、今回の解像した刻みでの次数を混同しない。

### Numerical acceptance

- analytic-error / 細かい固定刻みの全時刻で解析解と比較。: /metrics/maximum_error; value ≤ 1e-06
- resolved-refinement / 指定した細分化で観測次数を調べる。硬い粗格子で一律2次とは仮定しない。: /metrics/minimum_observed_order; value ≥ 1.7
- bounded-state / この初期値の余弦追従解が有界。: /metrics/maximum_state_magnitude; value ≤ 1.01
- stiff-decay / 別の強減衰1段問題を解析的指数減衰と比較。: /metrics/stiff_decay_error; value ≤ 1e-06
- final-time / 指定した終端時刻に到達。: /metrics/final_time_error; value ≤ 1e-14
- all-criteria / 全数値条件の判定: /checks; all values = true
- input-provenance / 実行した固定入力のSHA-256: /input_sha256; value = 53efd235fef8241ed7774f37696b97ef466217ae3244afa1430389c6fa23cd30
- case-passed / 入力に記載した条件の合格: /passed; value = true

### Failure and scope

方式違い、非有限入力、非正の率や刻み数、倍増でない列を拒否。Newton段階失敗は例外のまま伝える。粗い硬い刻みで一律2次収束を主張せず、今回の細分化で測定する。L安定でも正値を厳密に保つとは限らない。一般DAE・硬いPDEの検証ではない。

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/

### References

- CSVは最細刻みの数値解・解析解・絶対誤差。観測次数は全時刻最大誤差から計算。旧保存例の粗格子で約1台になる挙動と、今回の解像した刻みでの次数を混同しない。: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/stiff-cosine/result.json
- 解析解y=cos t+(y₀−1)e^(−rate*t)。別の同次減衰も指数関数を参照。: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/
- 既存SDIRK2項目にあるDIRKの原論文。選んだ係数・Newton設定は公開実装に固定。: https://doi.org/10.1137/0714068

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Compare stiff cosine tracking with its analytic solution under step refinement, plus a separate strongly damped problem.

**Methods used**

- [L-stable SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en) (`sdirk2`)

**Equations**

[This fixed-input problem and its conditions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-stiff-cosine-en)

Temporal initial-value problems using the existing two-stage SDIRK2. Main case: t=1 and 1000/2000/4000 steps. These example formulas are separate from the 46-model inventory, not new heat-PDE or general stiff-system entries.

$$
y'=-1000(y-\cos t)-\sin t,\qquad y(0)=1,\qquad y_{\rm ref}(t)=\cos t
$$

$$
z'=-10^8z,\qquad z(0)=1\quad\text{(separate one-step decay check)}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Stored fixed-step errors for the stiff cosine-tracking ODE.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/stiff-cosine.png)

A representative figure for the problem. Its grid, time and initial data may differ from this execution’s fixed input.

[Stiff cosine-tracking ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=en) (`stiff-cosine`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=en#stiff-cosine-en-validation)

CSV contains finest-grid time, numerical/analytic state and absolute error. Orders use maximum-in-time errors. Distinguish the older coarse-step order reduction from the resolved refinement here.

- [Stiff cosine-tracking ODE: SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-stiff-cosine-exact-en) (`stiff-cosine-exact`; Same-problem reference · Analytic reference)

An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution.


### scope

Use the existing two-stage L-stable SDIRK2 for y'=-1000(y-cos(t))-sin(t), y(0)=1 up to t=1. Check its analytic solution, fixed-step refinement and a separate very stiff one-step decay.

### assumptions

rate=1000; 1000/2000/4000 steps give rate*h=1,0.5,0.25. Uses fixed gamma=1-1/sqrt(2) and the existing Newton stage solver. Separate decay: y'=-1e8*y, y(0)=1, h=1. No adaptive stepping.

### units

Dimensionless time/state; rate has inverse-time units and rate*h is dimensionless.

### boundaries

Initial-value problem with no spatial boundaries; an equal-step sequence includes the final time.

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/stiff-cosine.json
Input SHA-256: 53efd235fef8241ed7774f37696b97ef466217ae3244afa1430389c6fa23cd30
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/stiff-cosine.json --output output-stiff-cosine
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/stiff-cosine/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/stiff-cosine/solution.csv

CSV contains finest-grid time, numerical/analytic state and absolute error. Orders use maximum-in-time errors. Distinguish the older coarse-step order reduction from the resolved refinement here.

### Numerical acceptance

- analytic-error / Compare the finest fixed-step trajectory with the analytic solution at all times.: /metrics/maximum_error; value ≤ 1e-06
- resolved-refinement / Check observed order on the supplied refinement; do not assume uniform second order on coarse stiff steps.: /metrics/minimum_observed_order; value ≥ 1.7
- bounded-state / Bounded cosine tracking for this supplied initial condition.: /metrics/maximum_state_magnitude; value ≤ 1.01
- stiff-decay / Compare a separate very stiff one-step decay with analytic exponential decay.: /metrics/stiff_decay_error; value ≤ 1e-06
- final-time / Reach the specified final time.: /metrics/final_time_error; value ≤ 1e-14
- all-criteria / All numerical acceptance flags: /checks; all values = true
- input-provenance / SHA-256 of the executed fixed input: /input_sha256; value = 53efd235fef8241ed7774f37696b97ef466217ae3244afa1430389c6fa23cd30
- case-passed / Acceptance conditions in the input passed: /passed; value = true

### Failure and scope

Reject other methods, nonfinite inputs, nonpositive rates/counts and non-doubling levels. Propagate implicit-stage failures. Do not claim uniform second order on coarse stiff steps; measure this supplied refinement. L-stability does not imply exact positivity. Not validation of general DAEs or stiff PDEs.

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/stiff-integration/

### References

- CSV contains finest-grid time, numerical/analytic state and absolute error. Orders use maximum-in-time errors. Distinguish the older coarse-step order reduction from the resolved refinement here.: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/stiff-cosine/result.json
- Analytic y=cos(t)+(y0-1)*exp(-rate*t); the separate homogeneous decay also uses an exponential reference.: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/
- DIRK paper already cited by the SDIRK2 record; selected coefficients/Newton settings are fixed by the released implementation.: https://doi.org/10.1137/0714068

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
