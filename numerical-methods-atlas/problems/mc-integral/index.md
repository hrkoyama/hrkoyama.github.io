# Monte Carlo：256 seedの積分誤差と区間被覆 / Monte Carlo: integral errors and interval coverage across 256 seeds

https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/

## 日本語

[公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/mc-integral/preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/monte-carlo/#publication-scope) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#mc-integral)

### 方程式・問題の定義

一様乱数による積分の統計推定問題です。既存一覧の物理方程式を解く例ではありません。

#### Monte Carlo：256 seedの積分誤差と区間被覆

共通実行例 · 問題の式

$$
\int_0^1 x^2\,dx=\tfrac13,\qquad\operatorname{Var}(U^2)=\tfrac4{45}
$$

$$
\operatorname{RMS}(\hat I_N)=\sqrt{4/(45N)}
$$

U[0,1]でx²を積分。256の独立seedで解析積分・分散と比較し、Nの平方根に反比例するRMS誤差と区間被覆を確認。MCMC・希少事象は対象外。

### 厳密解・参照解

既知の積分値を基準に256 seedの誤差・標準誤差・区間被覆を確認します。個々の乱数軌道の決定論的な解との比較ではありません。

#### Monte Carlo：256 seedの積分誤差と区間被覆

U[0,1]でx²を積分。256の独立seedで解析積分・分散と比較し、Nの平方根に反比例するRMS誤差と区間被覆を確認。MCMC・希少事象は対象外。

- [保存結果](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/mc-integral/result.json)
- [保存結果](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/mc-integral/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/mc-integral/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [Monte Carlo積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Monte Carlo：256 seedの積分誤差と区間被覆](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/mc-integral/?lang=ja)

共通実行例

U[0,1]でx²を積分。256の独立seedで解析積分・分散と比較し、Nの平方根に反比例するRMS誤差と区間被覆を確認。MCMC・希少事象は対象外。

U[0,1]でx²を積分。256の独立seedで解析積分・分散と比較し、Nの平方根に反比例するRMS誤差と区間被覆を確認。MCMC・希少事象は対象外。

[コード / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/mc-integral.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run.py --input inputs/mc-integral.json --output output
python -m pytest -q test_models.py
```

U[0,1]でx²を積分。256の独立seedで解析積分・分散と比較し、Nの平方根に反比例するRMS誤差と区間被覆を確認。MCMC・希少事象は対象外。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/model-benchmarks/2026-11-22/run.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/run.py)
- [/code/model-benchmarks/2026-11-22/test_models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py)

#### [code/model-benchmarks/2026-11-22/test_models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_fixed_case`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

作業フォルダ：model-benchmarks-2026-11-22/

```sh
python -m pytest -q test_models.py -k test_fixed_case
```

## English

[The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/mc-integral/preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/monte-carlo/#publication-scope) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#mc-integral-en)

### Equations and problem definitions

Statistical integral estimation with uniform random samples, not a solve of one of the registry’s physical equations.

#### Monte Carlo: integral errors and interval coverage across 256 seeds

Common execution example · Problem definition

$$
\int_0^1 x^2\,dx=\tfrac13,\qquad\operatorname{Var}(U^2)=\tfrac4{45}
$$

$$
\operatorname{RMS}(\hat I_N)=\sqrt{4/(45N)}
$$

Integrate x² under U[0,1]. Compare 256 independent seeds with analytic integral and variance, checking N^-1/2 RMS scaling and interval coverage. Excludes MCMC and rare events.

### Exact and reference solutions

Check errors, standard errors and interval coverage across 256 seeds against the known integral. This does not compare individual random realizations with a deterministic trajectory.

#### Monte Carlo: integral errors and interval coverage across 256 seeds

Integrate x² under U[0,1]. Compare 256 independent seeds with analytic integral and variance, checking N^-1/2 RMS scaling and interval coverage. Excludes MCMC and rare events.

- [Saved result](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/mc-integral/result.json)
- [Saved result](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/mc-integral/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/mc-integral/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [Monte Carlo integration](https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Monte Carlo: integral errors and interval coverage across 256 seeds](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/mc-integral/?lang=en)

Common execution example

Integrate x² under U[0,1]. Compare 256 independent seeds with analytic integral and variance, checking N^-1/2 RMS scaling and interval coverage. Excludes MCMC and rare events.

Integrate x² under U[0,1]. Compare 256 independent seeds with analytic integral and variance, checking N^-1/2 RMS scaling and interval coverage. Excludes MCMC and rare events.

[Code / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/mc-integral.json)

[File manifest and hashes](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run.py --input inputs/mc-integral.json --output output
python -m pytest -q test_models.py
```

Integrate x² under U[0,1]. Compare 256 independent seeds with analytic integral and variance, checking N^-1/2 RMS scaling and interval coverage. Excludes MCMC and rare events.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/model-benchmarks/2026-11-22/run.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/run.py)
- [/code/model-benchmarks/2026-11-22/test_models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py)

#### [code/model-benchmarks/2026-11-22/test_models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_fixed_case`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

Working directory: model-benchmarks-2026-11-22/

```sh
python -m pytest -q test_models.py -k test_fixed_case
```
