# 調和振動子（複素ODE表示も統合） / Harmonic oscillator, including complex-ODE form

https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/

## 日本語

[保存済みのt≤10の正準位相軌道。手法違いは同一問題の比較。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/harmonic-oscillator.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#harmonic-oscillator)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja)

$$
\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}
$$

$$
H=\frac{p^2}{2}+V(q)
$$

正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。

#### 調和振動子：Verletの位相誤差とエネルギー

共通実行例 · 問題の式

$$
\dot q=p,\qquad\dot p=-q,\qquad H(q,p)=\frac{q^2+p^2}{2}
$$

$$
q(0)=1,\quad p(0)=0.2,\qquad q_{\rm ref}(t)=\cos t+0.2\sin t
$$

単位質量・単位角振動数、t=20。速度Verletで200/400/800刻み。時間反転の一致やシンプレクティック性は元のエネルギーの厳密保存を意味しない。

### 厳密解・参照解

正弦・余弦の解析軌道（複素ODE表現を含む）と比較し、位相・エネルギー・写像の幾何学的性質を区別します。 既存の固定入力・保存結果に対応する解析参照カードを追加。解析式、点・時刻・動径の標本化、配布版SHAと実行コードを相互に辿れます。過去の計算を再実行した記録ではありません。 既存ギャラリーはt≤10、共通固定入力は終端20です。

#### [調和振動子：Verletの位相誤差とエネルギー](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=ja)

解析解 · 同じ問題の参照

q(t)=q0 cos(t)+p0 sin(t),p(t)=p0 cos(t)-q0 sin(t)

H=(q²+p²)/2、(q₀,p₀)=(1,0.2)。固定刻み、非散逸1自由度。初期値・終端時刻・刻み数は入力に明記。最大刻みh=0.1はhω<2の安定域。

既存の固定入力・保存結果に対応する解析参照カードを追加。解析式、点・時刻・動径の標本化、配布版SHAと実行コードを相互に辿れます。過去の計算を再実行した記録ではありません。 既存ギャラリーはt≤10、共通固定入力は終端20です。

#### 調和振動子：Verletの位相誤差とエネルギー

CSVは最細刻みの時刻ごとに数値・解析のq,pとエネルギーを整列。観測次数は終端状態誤差から、エネルギー偏差は全保存時刻から計算。

- [CSVは最細刻みの時刻ごとに数値・解析のq,pとエネルギーを整列。観測次数は終端状態誤差から、エネルギー偏差は全保存時刻から計算。](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/harmonic-oscillator/result.json)
- [独立な解析式q=q₀cos t+p₀sin t、p=−q₀sin t+p₀cos t。数値解の細格子値を厳密解とは呼ばない。](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/harmonic-oscillator/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/harmonic-oscillator/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [調和振動子：Verletの位相誤差とエネルギー](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=ja)

共通実行例

既存の単位質量・単位角振動数の調和振動子をvelocity Verletで進める。20時間単位、200/400/800刻みの解析解比較、元のエネルギー偏差、時間反転を出力。

H=(q²+p²)/2、(q₀,p₀)=(1,0.2)。固定刻み、非散逸1自由度。初期値・終端時刻・刻み数は入力に明記。最大刻みh=0.1はhω<2の安定域。

[コード / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/harmonic-oscillator.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/harmonic-oscillator.json --output output-harmonic-oscillator
python -m pytest -q tests/test_recipes.py
```

hω≥2、非有限入力、不明な方式・系、倍増でない刻み一覧を拒否。反転が良くても長時間位相誤差や元のHamiltonianの厳密保存を保証しない。非線形振動子・多体系への検証ではない。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

## English

[Stored canonical phase orbits for t≤10; methods remain variants of one problem.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/harmonic-oscillator.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#harmonic-oscillator-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en)

$$
\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}
$$

$$
H=\frac{p^2}{2}+V(q)
$$

Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity.

#### Harmonic oscillator: Verlet phase error and energy

Common execution example · Problem definition

$$
\dot q=p,\qquad\dot p=-q,\qquad H(q,p)=\frac{q^2+p^2}{2}
$$

$$
q(0)=1,\quad p(0)=0.2,\qquad q_{\rm ref}(t)=\cos t+0.2\sin t
$$

Unit mass/frequency, t=20, velocity Verlet with 200/400/800 steps. Reversibility or symplecticity does not imply exact conservation of the original energy.

### Exact and reference solutions

Compare with analytic sine/cosine trajectories, including complex-ODE form, and distinguish phase, energy and geometric map properties. An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution. The existing gallery shows t≤10; the common fixed input ends at20.

#### [Harmonic oscillator: Verlet phase error and energy](https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=en)

Analytic reference · Reference for the same problem

q(t)=q0 cos(t)+p0 sin(t),p(t)=p0 cos(t)-q0 sin(t)

H=(q²+p²)/2 and (q0,p0)=(1,0.2); one nondissipative degree of freedom, fixed steps. Inputs explicitly provide initial state, final time and counts. Largest h=0.1 lies in h*omega<2.

An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution. The existing gallery shows t≤10; the common fixed input ends at20.

#### Harmonic oscillator: Verlet phase error and energy

CSV aligns numerical/analytic q,p and energy on the finest time grid. Observed order uses endpoint-state errors; energy deviation uses all recorded times.

- [CSV aligns numerical/analytic q,p and energy on the finest time grid. Observed order uses endpoint-state errors; energy deviation uses all recorded times.](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/harmonic-oscillator/result.json)
- [Independent analytic q=q0*cos(t)+p0*sin(t), p=-q0*sin(t)+p0*cos(t); no fine numerical solution is called exact.](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/harmonic-oscillator/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/harmonic-oscillator/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Harmonic oscillator: Verlet phase error and energy](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=en)

Common execution example

Advance the existing unit-mass, unit-frequency harmonic oscillator with velocity Verlet. Compare analytic states over 20 time units at 200/400/800 steps, original-energy deviation and reversal.

H=(q²+p²)/2 and (q0,p0)=(1,0.2); one nondissipative degree of freedom, fixed steps. Inputs explicitly provide initial state, final time and counts. Largest h=0.1 lies in h*omega<2.

[Code / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/harmonic-oscillator.json)

[File manifest and hashes](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/harmonic-oscillator.json --output output-harmonic-oscillator
python -m pytest -q tests/test_recipes.py
```

Reject h*omega>=2, nonfinite inputs, unknown method/system and non-doubling counts. Accurate reversal does not establish long-time phase accuracy or exact original-Hamiltonian conservation. Not validation of nonlinear oscillators or many-body systems.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)
