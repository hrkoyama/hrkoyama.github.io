# Lightweight numerical foundations / 軽量な数値計算基盤

Four small fixed-input examples join original educational implementations to
analytic and separate SciPy/LAPACK references. They cover matrix-based smoothed
aggregation AMG, Householder QR and one-sided Jacobi SVD, Lanczos/Arnoldi, and
Gauss–Legendre/adaptive Simpson quadrature.

## Run

Use Python 3.12 and the pinned dependencies in `requirements.txt`:

```sh
python -m pip install -r requirements.txt
python -m pytest -q test_foundations.py
python run.py --input inputs.json --output output
```

Choose a new or empty output directory. A completed run writes `result.json`,
one CSV for each case, and `amg-residuals.csv`. The JSON records fixed-input SHA,
environment versions, numerical checks, metrics, every comparison record, and
termination reasons. Exit status 0 means every fixed acceptance check passed;
1 means a completed scientific check failed. Invalid input/output usage prints
an explicit diagnostic and returns 2. `duration_seconds` measures the
calculation and CSV generation after imports, not environment installation.

The local source test run passed 29 tests. A single-thread run of all four cases
took about 0.03 seconds after imports on the development Mac; CLI wall time was
about 0.6 seconds. These are observations for this small input, not a portable
performance guarantee.

Plotting is optional and reads only previously stored JSON/CSV:

```sh
python -m pip install -r requirements-plotting.txt
python plot.py --results output/result.json --output output
```

This creates one `<case-id>.png` per case. The scientific runner and ordinary
tests do not import Matplotlib or regenerate figures.

## What is implemented and compared

- **SA AMG:** Hierarchy setup consumes only an SPD coefficient matrix. A
  row-relative strength graph, greedy star aggregates, smoothed interpolation,
  Galerkin coarse operators, and Jacobi-smoothed V-cycles are implemented here.
  Only the small terminal matrix is solved densely. Three zero-Dirichlet
  Poisson grids (49/225/961 unknowns) compare with separate `scipy.sparse.linalg.spsolve`,
  the analytic discrete sine mode, and the continuum manufactured solution.
  A permuted-node test checks that setup does not use geometric coordinates.
  Stored quantities distinguish residual, solution error, PDE discretization
  order, and operator complexity. A zero cycle budget reports nonconvergence.
- **QR/SVD:** Householder QR and cyclic one-sided Jacobi SVD are original code.
  Normal, column-scaled, deficient-rank and zero matrices test reconstruction,
  orthogonality, rank, and least-squares stationarity. References are independent
  SciPy/LAPACK `gesdd`, `gelsd`, and `gelsy`. SVD factors are compact: columns
  below the fixed relative rank threshold are omitted. QR has no column
  pivoting and makes no rank-revealing claim.
- **Krylov eigenvalues:** Lanczos uses a three-term recurrence plus full
  reorthogonalization; Arnoldi uses two-pass modified Gram–Schmidt. NumPy solves
  only the small projected eigenproblem. Separate SciPy dense eigensolvers
  supply the reference for 32/48-dimensional symmetric and mildly nonnormal
  matrices. Dimensions 4/8/16 measure residual and eigenvalue error. Tests
  include complex Arnoldi Ritz pairs, happy breakdown and exhausted budgets.
- **Quadrature:** Golub–Welsch builds Legendre nodes and weights using a small
  Jacobi-matrix eigensolve, independently compared with `roots_legendre`.
  Polynomial moments through degree `2*n-1` and an exponential are checked.
  Original adaptive Simpson integrates an exponential and a Lorentzian peak
  against analytic formulas and independent QUADPACK (`scipy.integrate.quad`).
  Evaluation/depth exhaustion and nonfinite integrands are explicit failures.

`cases.json` supplies bilingual assumptions, algorithm descriptions, measured
validation scope, limitations, formulas and primary references.
`source-review.json` states which publisher metadata/abstracts/first-page
excerpts were checked. No paywalled-paper full-text audit is claimed.

## Limits

This is a small educational supplement, not a replacement for production AMG,
LAPACK, ARPACK or QUADPACK. The AMG input is scalar SPD; it does not establish
mesh-independent convergence, arbitrary-coefficient robustness or optimal
complexity. The SVD uses a numerical-rank convention, not exact algebraic rank.
The eigenvalue examples use separated extreme eigenpairs, not interior or
clustered eigenvalues. The adaptive Simpson estimate is heuristic for general
functions; it is not a certified error bound or a safeguard against every
oscillatory/singular integrand. A zero reported quadrature difference can mean
roundoff agreement rather than exact real-arithmetic integration.

The small dense contractions in the Krylov code use explicit NumPy `einsum`
operations. This avoids spurious floating-point flags observed in the pinned
NumPy/Apple BLAS combination for finite small matrix products; it does not
disable warnings or alter numerical acceptance criteria.

## 日本語

4つの固定例で、解説・自作コード・独立参照・収束・終了理由をつなぎます。
実行コマンドは上記と共通です。`inputs.json` に入力と受入基準を固定し、
出力には入力SHA、Python/依存版、各判定、実測値、CSVを保存します。

- **AMG:** 行列係数だけから強度グラフと集約を作り、補間を平滑化し、
  `PᵀAP` で粗演算子を作ります。幾何学的粗格子を使う手法とは区別します。
  独立疎行列直接解・離散正弦解・連続製造解を別々に比較し、残差と解誤差、
  格子次数、operator complexityを記録します。任意の不定値・異方性・係数不連続は未検証です。
- **QR/SVD:** Householder反射と片側Jacobi回転を実装し、LAPACKの別アルゴリズムと照合します。
  階数落ちでは数値的に零の方向を除くcompact SVDを使います。数学的厳密階数や
  あらゆるスケーリングに対する相対高精度を保証しません。
- **固有値:** 全再直交化を持つLanczos/Arnoldiで射影し、小さい投影行列だけを密に解きます。
  元行列全体の密固有値計算は独立参照側です。32/48次の固定行列で次元4/8/16を比較し、
  固有対残差と直交性を測ります。非再始動の教材であり、内部固有値や強い非正規性は対象外です。
- **求積:** Gauss–Legendreの多項式厳密次数と非多項式の収束、適応Simpsonの公差走査を確認します。
  Simpson推定は任意の関数の厳密誤差上界ではありません。評価予算・深さ・非有限値を検査します。

29テストが合格し、全4例は開発Macでimport後約0.03秒、CLI全体で約0.6秒でした。
この固定入力での観測であり、他環境の実行時間を保証する値ではありません。
一次文献の確認範囲は `source-review.json` に記載し、書誌確認と全文監査を区別します。
原著コードを転載していません。`LICENSE` はここにあるオリジナルPythonコードに適用し、
依存ライブラリ、第三者論文、サイト本文・図・データの利用条件はそれぞれ区別します。

MIT applies to original code only. Text, figures, fixed inputs and numerical
data retain the separate site conditions in
[LICENSING.md](https://hrkoyama.github.io/LICENSING.md) and
[Rights & AI policy](https://hrkoyama.github.io/rights/).
No blanket Creative Commons or other new permission is granted for these
non-code materials or third-party sources.

MITはオリジナルコードのみです。本文・図・固定入力・数値データは上記の
`LICENSING.md` と `/rights/` にある個別条件を参照してください。
これらや第三者資料へ、新しい一括許諾を追加しません。
