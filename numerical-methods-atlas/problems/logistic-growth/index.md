# ロジスティック増殖：解析解と刻み幅の収束 / Logistic growth: analytic solution and time refinement

https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/

## 日本語

[公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/logistic-growth/preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#01-1838-logistic-population-growth) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#logistic-growth)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [ロジスティック個体群増殖](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-logistic-ja)

$$
\dot N=rN(1-N/K)
$$

収容力Kを持つ密度依存の連続時間増殖モデル。離散ロジスティック写像とは区別します。 限定した実行例：無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。

#### ロジスティック増殖：解析解と刻み幅の収束

共通実行例 · 問題の式

$$
\dot y=r y(1-y/K)
$$

$$
y(t)=K/[1+(K/y_0-1)e^{-rt}]
$$

無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。

### 厳密解・参照解

指定r・K・初期値のロジスティック解析解と時間刻み収束が基準です。18件の参照解一覧とは別の固定入力で検証しています。

#### ロジスティック増殖：解析解と刻み幅の収束

無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。

- [保存結果](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/logistic-growth/result.json)
- [保存結果](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/logistic-growth/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [ロジスティック増殖：解析解と刻み幅の収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=ja)

共通実行例

無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。

無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。

[コード / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/logistic-growth.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run.py --input inputs/logistic-growth.json --output output
python -m pytest -q test_models.py
```

無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。

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

[The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/logistic-growth/preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#01-1838-logistic-population-growth) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#logistic-growth-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Logistic population growth](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-logistic-en)

$$
\dot N=rN(1-N/K)
$$

Density-limited growth with carrying capacity K. It is the simplest biological ODE baseline. The linked original is the later 1847 memoir; the 1838 note itself was not audited. The differential equation is not the discrete logistic map. Scoped executed example: One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.

#### Logistic growth: analytic solution and time refinement

Common execution example · Problem definition

$$
\dot y=r y(1-y/K)
$$

$$
y(t)=K/[1+(K/y_0-1)e^{-rt}]
$$

One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.

### Exact and reference solutions

Use the logistic analytic solution for the specified r, K and initial value and check time refinement. Validation uses its own fixed inputs outside the 18-case reference library.

#### Logistic growth: analytic solution and time refinement

One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.

- [Saved result](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/logistic-growth/result.json)
- [Saved result](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/logistic-growth/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Logistic growth: analytic solution and time refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=en)

Common execution example

One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.

One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.

[Code / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/logistic-growth.json)

[File manifest and hashes](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run.py --input inputs/logistic-growth.json --output output
python -m pytest -q test_models.py
```

One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.

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
