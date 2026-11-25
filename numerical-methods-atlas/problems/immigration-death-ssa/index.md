# 移入–死亡SSA：有限時刻の厳密分布 / Immigration–death SSA: exact transient laws

https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/

## 日本語

[1本の軌跡と12,288本の固定アンサンブルを分けて検証します。 有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology-ode-controls/#immigration-death-ssa) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#immigration-death-ssa)

### 方程式・問題の定義

移入率6、粒子ごとの死亡率1、時刻0/0.5/2/4。初期0・5・名目上のPoisson(6)定常標本を2seedずつ、各2,048本で比較します。

#### [化学マスター方程式とGillespie SSA](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-chemical-master-ja)

$$
\partial_t P(\boldsymbol n,t)=\sum_j\left[a_j(\boldsymbol n-\boldsymbol\nu_j)P(\boldsymbol n-\boldsymbol\nu_j,t)-a_j(\boldsymbol n)P(\boldsymbol n,t)\right]
$$

整数分子数n、反応ジャンプνj、傾向関数ajの確率モデル。Gillespie SSAは軌道を標本化する解法で、反応網自体とは区別します。 全モデル族の実装ではありません。今回の固定例：移入–死亡SSA：有限時刻の厳密分布

#### [移入–死亡反応と厳密過渡法則](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#immigration-death-model-ja)

$$
\varnothing\xrightarrow{6}N,\qquad N\xrightarrow{N} \varnothing
$$

$$
N(t)\overset d=\mathrm{Bin}(n_0,e^{-t})+\mathrm{Pois}(6(1-e^{-t}))
$$

有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。

#### 移入–死亡SSA：有限時刻の厳密分布

補助実行例 · 実行例の定義・検証式

$$
\varnothing\xrightarrow{6}N,\qquad N\xrightarrow{N} \varnothing
$$

$$
N(t)\overset d=\mathrm{Bin}(n_0,e^{-t})+\mathrm{Pois}(6(1-e^{-t}))
$$

1本の軌跡と12,288本の固定アンサンブルを分けて検証します。

### 厳密解・参照解

Binomial＋Poissonの厳密過渡法則を、80/120桁の有向区間・尾部上界で照合。20個のDKW目標と20個の厳密和平均目標を名目union bound0.01にまとめ、分散の5SE目標は別に残します。

#### [移入–死亡SSA：有限時刻の厳密分布](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=ja#immigration-death-ssa-ja-measurements)

解析解 · 同じ問題の参照

\varnothing\xrightarrow{6}N,\qquad N\xrightarrow{N} \varnothing;\quad N(t)\mid N(0)=n_0\;\overset d=\mathrm{Bin}(n_0,e^{-t})+\mathrm{Pois}(6(1-e^{-t}))

移入率6、粒子ごとの死亡率1、観測時刻0/0.5/2/4。初期値0・5・名目上の定常Poisson(6)を各2seed、各記録2,048軌跡で比較します。粒子数は非負整数、時間単位を固定し、N=0では死亡propensityが零になります。

有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。

#### 移入–死亡SSA：有限時刻の厳密分布

Binomial＋Poissonの厳密過渡法則を、80/120桁の有向区間・尾部上界で照合。20個のDKW目標と20個の厳密和平均目標を名目union bound0.01にまとめ、分散の5SE目標は別に残します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=ja)

### 計算法

Gillespie direct SSAで、次の事象時刻を観測点の間で保持します。生のPCG64から開区間一様数を作り、初期Poissonの有限格子逆CDFと全ストリームを記録します。

- [Gillespie直接確率シミュレーション（SSA）](https://hrkoyama.github.io/numerical-methods-atlas/methods/gillespie-ssa/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [移入–死亡SSA：有限時刻の厳密分布](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=ja)

補助実行例

1本の軌跡と12,288本の固定アンサンブルを分けて検証します。

移入率6、粒子ごとの死亡率1、時刻0/0.5/2/4。初期0・5・名目上のPoisson(6)定常標本を2seedずつ、各2,048本で比較します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/biology-ode-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/test_models.py)

## English

[Separate one displayed path from12,288fixed ensemble paths. Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology-ode-controls/#immigration-death-ssa) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#immigration-death-ssa-en)

### Equations and problem definitions

Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record.

#### [Chemical master equation and Gillespie SSA](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-chemical-master-en)

$$
\partial_t P(\boldsymbol n,t)=\sum_j\left[a_j(\boldsymbol n-\boldsymbol\nu_j)P(\boldsymbol n-\boldsymbol\nu_j,t)-a_j(\boldsymbol n)P(\boldsymbol n,t)\right]
$$

Integer molecule counts, reaction jumps νj and propensities aj; SSA samples paths of this continuous-time Markov model. The 1977 paper is a foundational SSA reference, not a priority claim for all master equations. SSA is a solver; the reaction network is the model. A seed documents a trajectory, not an ensemble validation. Not implementation of the entire model family. Fixed cases: Immigration–death SSA: exact transient laws

#### [Immigration–death reaction and exact transient law](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#immigration-death-model-en)

$$
\varnothing\xrightarrow{6}N,\qquad N\xrightarrow{N} \varnothing
$$

$$
N(t)\overset d=\mathrm{Bin}(n_0,e^{-t})+\mathrm{Pois}(6(1-e^{-t}))
$$

Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.

#### Immigration–death SSA: exact transient laws

Supplementary execution example · Example definition or validation formula

$$
\varnothing\xrightarrow{6}N,\qquad N\xrightarrow{N} \varnothing
$$

$$
N(t)\overset d=\mathrm{Bin}(n_0,e^{-t})+\mathrm{Pois}(6(1-e^{-t}))
$$

Separate one displayed path from12,288fixed ensemble paths.

### Exact and reference solutions

Qualify exact Binomial-plus-Poisson transients with directed80/120digit intervals and tail bounds. Combine20DKW and20exact-sum mean goals under nominal union bound0.01; retain five-SE variance goals separately.

#### [Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=en#immigration-death-ssa-en-measurements)

Analytic reference · Reference for the same problem

\varnothing\xrightarrow{6}N,\qquad N\xrightarrow{N} \varnothing;\quad N(t)\mid N(0)=n_0\;\overset d=\mathrm{Bin}(n_0,e^{-t})+\mathrm{Pois}(6(1-e^{-t}))

Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record. Integer particle counts and a fixed time unit; death rate 1 per particle and immigration rate 6. Nonnegative integer counts; death propensity vanishes at N=0.

Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.

#### Immigration–death SSA: exact transient laws

Qualify exact Binomial-plus-Poisson transients with directed80/120digit intervals and tail bounds. Combine20DKW and20exact-sum mean goals under nominal union bound0.01; retain five-SE variance goals separately.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=en)

### Numerical methods

Use direct GillespieSSA with pending event times preserved across observations. Draw open-grid uniforms from rawPCG64; record finite-grid Poisson initialization and all RNG streams.

- [Gillespie direct stochastic simulation (SSA)](https://hrkoyama.github.io/numerical-methods-atlas/methods/gillespie-ssa/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=en)

Supplementary execution example

Separate one displayed path from12,288fixed ensemble paths.

Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/biology-ode-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/test_models.py)
