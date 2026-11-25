# 硬い余弦追従ODE / Stiff cosine-tracking ODE

https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/

## 日本語

[保存済みの硬い余弦追従ODEの固定刻み誤差。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/stiff-cosine.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#stiff-cosine)

### 方程式・問題の定義

硬い非自律スカラーODE y′=-1000(y-cos t)-sin t。既存の方程式一覧には専用項目がありません。

#### 硬い余弦追従ODE：SDIRK2

共通実行例 · 問題の式

$$
y'=-1000(y-\cos t)-\sin t,\qquad y(0)=1,\qquad y_{\rm ref}(t)=\cos t
$$

$$
z'=-10^8z,\qquad z(0)=1\quad\text{(separate one-step decay check)}
$$

既存2段SDIRK2を使う時間初期値問題。主問題はt=1、1000/2000/4000刻み。46モデル台帳とは別の実行例の式で、熱PDEや汎用硬い系の新規モデルとして数えない。

### 厳密解・参照解

y′=-1000(y-cos t)-sin t、y(0)=1の厳密解cos tと、固定刻み・適応刻みの誤差を確認します。 既存の固定入力・保存結果に対応する解析参照カードを追加。解析式、点・時刻・動径の標本化、配布版SHAと実行コードを相互に辿れます。過去の計算を再実行した記録ではありません。

#### [硬い余弦追従ODE：SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=ja)

解析解 · 同じ問題の参照

y(t)=cos(t)+(y0-1)exp(-rate*t); yprime=-rate*(y-cos(t))-sin(t)

rate=1000、1000/2000/4000ステップでrate*h=1,0.5,0.25。固定γ=1−1/√2と既存Newton段階解法を使用。別の減衰はy′=−10⁸y、y(0)=1、h=1。適応刻み法ではない。

既存の固定入力・保存結果に対応する解析参照カードを追加。解析式、点・時刻・動径の標本化、配布版SHAと実行コードを相互に辿れます。過去の計算を再実行した記録ではありません。

#### 硬い余弦追従ODE：SDIRK2

CSVは最細刻みの数値解・解析解・絶対誤差。観測次数は全時刻最大誤差から計算。旧保存例の粗格子で約1台になる挙動と、今回の解像した刻みでの次数を混同しない。

- [CSVは最細刻みの数値解・解析解・絶対誤差。観測次数は全時刻最大誤差から計算。旧保存例の粗格子で約1台になる挙動と、今回の解像した刻みでの次数を混同しない。](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/stiff-cosine/result.json)
- [解析解y=cos t+(y₀−1)e^(−rate*t)。別の同次減衰も指数関数を参照。](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/stiff-cosine/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/stiff-cosine/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [L安定なSDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [硬い余弦追従ODE：SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=ja)

共通実行例

既存のL安定2段SDIRK2でy′=−1000(y−cos t)−sin t、y(0)=1をt=1まで解く。解析解、固定刻み細分化、別の強減衰1段問題を検査。

rate=1000、1000/2000/4000ステップでrate*h=1,0.5,0.25。固定γ=1−1/√2と既存Newton段階解法を使用。別の減衰はy′=−10⁸y、y(0)=1、h=1。適応刻み法ではない。

[コード / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/stiff-cosine.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/stiff-cosine.json --output output-stiff-cosine
python -m pytest -q tests/test_recipes.py
```

方式違い、非有限入力、非正の率や刻み数、倍増でない列を拒否。Newton段階失敗は例外のまま伝える。粗い硬い刻みで一律2次収束を主張せず、今回の細分化で測定する。L安定でも正値を厳密に保つとは限らない。一般DAE・硬いPDEの検証ではない。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_stiff_decay_and_local_error_control`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_new_models.py -k test_stiff_decay_and_local_error_control
```

## English

[Stored fixed-step errors for the stiff cosine-tracking ODE.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/stiff-cosine.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/stiff-integration/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#stiff-cosine-en)

### Equations and problem definitions

Stiff nonautonomous scalar ODE y′=-1000(y-cos t)-sin t; the equation registry has no dedicated entry.

#### Stiff cosine-tracking ODE: SDIRK2

Common execution example · Problem definition

$$
y'=-1000(y-\cos t)-\sin t,\qquad y(0)=1,\qquad y_{\rm ref}(t)=\cos t
$$

$$
z'=-10^8z,\qquad z(0)=1\quad\text{(separate one-step decay check)}
$$

Temporal initial-value problems using the existing two-stage SDIRK2. Main case: t=1 and 1000/2000/4000 steps. These example formulas are separate from the 46-model inventory, not new heat-PDE or general stiff-system entries.

### Exact and reference solutions

Check fixed/adaptive-step errors against cos t for y′=-1000(y-cos t)-sin t with y(0)=1. An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution.

#### [Stiff cosine-tracking ODE: SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=en)

Analytic reference · Reference for the same problem

y(t)=cos(t)+(y0-1)exp(-rate*t); yprime=-rate*(y-cos(t))-sin(t)

rate=1000; 1000/2000/4000 steps give rate*h=1,0.5,0.25. Uses fixed gamma=1-1/sqrt(2) and the existing Newton stage solver. Separate decay: y'=-1e8*y, y(0)=1, h=1. No adaptive stepping.

An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution.

#### Stiff cosine-tracking ODE: SDIRK2

CSV contains finest-grid time, numerical/analytic state and absolute error. Orders use maximum-in-time errors. Distinguish the older coarse-step order reduction from the resolved refinement here.

- [CSV contains finest-grid time, numerical/analytic state and absolute error. Orders use maximum-in-time errors. Distinguish the older coarse-step order reduction from the resolved refinement here.](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/stiff-cosine/result.json)
- [Analytic y=cos(t)+(y0-1)*exp(-rate*t); the separate homogeneous decay also uses an exponential reference.](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/stiff-cosine/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/stiff-cosine/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [L-stable SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Stiff cosine-tracking ODE: SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=en)

Common execution example

Use the existing two-stage L-stable SDIRK2 for y'=-1000(y-cos(t))-sin(t), y(0)=1 up to t=1. Check its analytic solution, fixed-step refinement and a separate very stiff one-step decay.

rate=1000; 1000/2000/4000 steps give rate*h=1,0.5,0.25. Uses fixed gamma=1-1/sqrt(2) and the existing Newton stage solver. Separate decay: y'=-1e8*y, y(0)=1, h=1. No adaptive stepping.

[Code / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/stiff-cosine.json)

[File manifest and hashes](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/stiff-cosine.json --output output-stiff-cosine
python -m pytest -q tests/test_recipes.py
```

Reject other methods, nonfinite inputs, nonpositive rates/counts and non-doubling levels. Propagate implicit-stage failures. Do not claim uniform second order on coarse stiff steps; measure this supplied refinement. L-stability does not imply exact positivity. Not validation of general DAEs or stiff PDEs.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_stiff_decay_and_local_error_control`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_new_models.py -k test_stiff_decay_and_local_error_control
```
