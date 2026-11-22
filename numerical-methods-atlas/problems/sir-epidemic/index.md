# SIR：独立DOP853参照・人口保存・収束 / SIR: independent DOP853 reference, conservation and convergence

https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/

## 日本語

[公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#05-1927-sir-and-seir-compartment-models) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#sir-epidemic)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [SIR・SEIR区画モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-sir-ja)

$$
\dot s=-\beta si
$$

$$
\dot i=\beta si-\gamma i
$$

$$
\dot r=\gamma i
$$

$$
s+i+r=1
$$

閉じた一様混合集団の規格化SIR系。SEIRは曝露区画を追加します。人数と割合ではβの定義が異なります。 限定した実行例：閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。

#### SIR：独立DOP853参照・人口保存・収束

共通実行例 · 問題の式

$$
\dot S=-\beta SI,\quad\dot I=\beta SI-\gamma I,\quad\dot R=\gamma I
$$

$$
S+I+R=1
$$

閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。

### 厳密解・参照解

同一入力の独立DOP853数値参照、人口保存、非負性と時間収束を確認します。一般的な閉形式SIR解の提供ではありません。

#### SIR：独立DOP853参照・人口保存・収束

別実装DOP853と2段階許容誤差の比較。解析解ではありません。

- [別実装DOP853と2段階許容誤差の比較。解析解ではありません。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/references/sir.json)
- [保存結果](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/result.json)
- [保存結果](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [SIR：独立DOP853参照・人口保存・収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=ja)

共通実行例

閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。

閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。

[コード / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/sir-epidemic.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run.py --input inputs/sir-epidemic.json --output output
python -m pytest -q test_models.py
```

閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。

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

[The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#05-1927-sir-and-seir-compartment-models) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#sir-epidemic-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [SIR and SEIR compartment models](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-sir-en)

$$
\dot s=-\beta si
$$

$$
\dot i=\beta si-\gamma i
$$

$$
\dot r=\gamma i
$$

$$
s+i+r=1
$$

Closed, well-mixed normalized population fractions. SEIR adds an exposed compartment and a progression rate. The original general epidemic framework is broader than this SIR specialization. Population-count and fraction conventions give different β definitions. Scoped executed example: Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.

#### SIR: independent DOP853 reference, conservation and convergence

Common execution example · Problem definition

$$
\dot S=-\beta SI,\quad\dot I=\beta SI-\gamma I,\quad\dot R=\gamma I
$$

$$
S+I+R=1
$$

Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.

### Exact and reference solutions

Check an independent DOP853 numerical reference for identical inputs, population conservation, nonnegativity and time refinement. This is not a general closed-form SIR solution.

#### SIR: independent DOP853 reference, conservation and convergence

Separately implemented DOP853 with two-tolerance agreement; not an analytic solution.

- [Separately implemented DOP853 with two-tolerance agreement; not an analytic solution.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/references/sir.json)
- [Saved result](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/result.json)
- [Saved result](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [SIR: independent DOP853 reference, conservation and convergence](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=en)

Common execution example

Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.

Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.

[Code / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/sir-epidemic.json)

[File manifest and hashes](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run.py --input inputs/sir-epidemic.json --output output
python -m pytest -q test_models.py
```

Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.

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
