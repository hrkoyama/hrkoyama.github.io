# Conditioning and honest verification / 条件数と検証の限界

Four bounded experiments deepen the earlier AMG, QR/SVD, Krylov and quadrature
examples. They compare independent references while separating residual from
forward error, numerical rank from exact rank, and a heuristic stopping flag
from actual quadrature accuracy. The earlier release is retained unchanged.
No quantum calculations are added.

## Run / 実行

Use Python 3.12 and the three pinned routine dependencies:

```sh
python -m pip install -r requirements.txt
python -W error -m pytest -q -p no:cacheprovider
python -W error run.py --input inputs.json --output output
```

Use a new or empty output directory. The runner writes `result.json`, four case
JSON files, four measurement CSV files and `amg-residuals.csv`. The main report
contains input SHA, actual environment, every numerical check, measurement and
termination status. `passed` means all predeclared checks passed. **A passing
expected-failure control does not mean that its solver/integral converged.**
Completed checks return exit status 0 or 1; invalid inputs, overwritten output
or exhausted wall-time budget raise an explicit error and return nonzero.
Completed per-case evidence remains saved if a later case fails.

Inputs and acceptance criteria were saved before the first primary pilot or
high-precision reference calculation. The input SHA256 is
`142f7fdeb264f130c64d402f417eb34e0a64e269431137eba5b821e85484306f`.
This downloadable runner accepts this fixed recipe, rather than arbitrary
allocation sizes or user-modified acceptance widths. The post-import wall-time
budget is 105 seconds; it does not cover package installation or plotting.
The development run took approximately 0.14 seconds after imports (about one
second CLI wall time), and 49 scientific/provenance/CLI tests passed with
warnings treated as errors. These are observations, not portable performance
guarantees.

Optional plotting reads only stored data and never imports the solver:

```sh
python -m pip install -r requirements-plotting.txt
python plot.py --results output/result.json --output output
```

It produces one PNG named after each case ID. `cases.json` supplies Japanese
and English explanations, assumptions, equations, references and limitations.

## What is tested

- **AMG conditioning:** Scalar SPD systems `A=T⊗I+εI⊗T`, with square interior
  sizes 7/15/31 and anisotropies 1/.1/.01. At fixed square size, the analytic
  2-norm condition number is `cot²(π/(2(n+1)))` **independent of ε**. Grid size
  changes conditioning; anisotropy can change iterative behavior at the same
  condition number. Matrix-only smoothed aggregation, Jacobi smoothing,
  strength .08, tolerance `1e-10` and 180-cycle limit are fixed. References are
  separate sparse LU (`spsolve`), DST-I spectral diagonalization, analytic sine
  eigenvalues and a separate tridiagonal spectrum routine. We save true
  residual, forward error, condition-times-residual, complete cycle history
  and operator complexity. An extremal-mode RHS perturbation reproduces the
  exact relative gain κ. One-cycle nonconvergence is an expected control.
  All nine development solves converged. This is a **pure algebraic
  diagnostic**, not a new continuum PDE test; earlier Poisson refinement
  results remain separate.
- **QR/SVD conditioning:** A 16×4 dyadic Hadamard construction has exact
  binary64 entries and prescribed singular values `2^(-q*j)`, q=0/4/8/12.
  Condition numbers are 1,4096,16777216,68719476736. Original Householder QR,
  cyclic one-sided Jacobi SVD and triangular back substitution are checked
  against SciPy/LAPACK `gesdd`, `gelsd`, `gelsy` and separately generated
  high-precision results for the **actual binary inputs**. A known RHS
  perturbation `2^-40*u_min` has solution response `2^-40*κ`; the most
  conditioned response is .0625. Reconstruction and forward accuracy are
  distinct; development roundoff produced forward error about `4.92e-4`
  while reconstruction remained near machine precision. A more accurate
  platform result is allowed. Rank cutoffs `1e-8/1e-12/1e-14` are compared
  against the same truncated problem. An exact rank-two matrix and zero-sweep
  nonconvergence are separate controls. No normal-equations run is claimed.
- **Krylov conditioning:** Fully reorthogonalized Lanczos and two-pass MGS
  Arnoldi use dimensions 4/8/16/32 on 48-dimensional examples. Symmetric
  top-two gaps 1/.1/.01 are compared with actual-matrix dense eigenvalues and
  nominal analytic spectra within construction roundoff. Clusters use
  invariant-subspace projectors, not sign-sensitive individual vectors.
  Strongly nonnormal inputs are actual upper-triangular matrices with
  couplings 10/1000, so their diagonal eigenvalues remain known without a
  floating-point similarity construction. Left/right eigenvectors measure
  eigenvalue condition. A **separately constructed** 2×2 pseudoeigenpair has
  residual about `2.5e-8` but forward eigenvalue error .005 at coupling1000;
  this is not labelled a pair produced by a failing solver.
- **Quadrature conditioning:** Gauss–Legendre orders 8/16/32/64/128 and
  adaptive Simpson tolerances `1e-5/1e-7/1e-9` compare narrow off-center
  Lorentzians (width .1/.03/.01), a square-root endpoint, cancellation scales
  up to `2^36`, a zero integral and a compact bump. Analytic atan integrals,
  `2/3`, the exact bump integral `256*w/315`, `roots_legendre` and QUADPACK
  provide references. QUADPACK status, warning message, evaluation count and
  estimated error are retained. Direct sqrt at `1e-9` honestly reached the
  depth budget despite a small observed error; its `x=t²` companion resolves.
  The bump misses all five initial sample nodes, giving estimated error zero
  but actual error about .00812698. The known-support split companion resolves
  it. This is an **expected heuristic blind spot**, not successful accurate
  integration. Relative condition at exact zero integral is undefined/null;
  cancellation uses roundoff-aware absolute budgets. The L∞ input-sensitivity
  measure and the pointwise relative cancellation condition are kept distinct.

## Independent reference provenance

`reference.json` was actually generated in a **separate** pinned mpmath1.3.0
environment at 80 and 120 decimal digits. Ordinary execution needs only NumPy,
SciPy and pytest; it never imports mpmath or regenerates this reference.
`reference-input.json` stores each actual float as `float.hex`, together with
canonical little-endian binary64 array hashes. The generator converts each
float to an exact integer ratio before arbitrary-precision arithmetic. An
independent Fraction construction also verifies that every formed matrix
equals the prescribed dyadic recipe. All four singular spectra and both RHS
solutions agree across precisions; recorded comparisons include residuals and
analytic agreement. Source, protocol, package-wheel and implementation hashes
are recorded. The stored payload SHA is
`b8d4776330ee86843de225f6800a9dba180083e5af728a178f9f9670135d83e8`.

To **optionally regenerate** the reference, use a separate environment, record
the new installation, and choose a new output path:

```sh
python -m venv reference-env
reference-env/bin/python -m pip install --no-cache-dir --report reference-env/install-report.json -r requirements-reference.txt
reference-env/bin/python mpmath_reference.py --input reference-input.json --recipe fixtures.py --protocol inputs.json --install-report reference-env/install-report.json --output reference-regenerated.json
```

The copied `mpmath-install-report.json` documents only the original execution
and wheel hash. A fresh regeneration must use its own install report; its
timestamped reference payload has a different whole-file hash. Do not
replace the pinned reference automatically. Compare numerical records and
input/source bindings explicitly. Tests intentionally corrupt missing/extra
datasets, precision runs, scalar/vector values and hashes to ensure failure
cannot silently fall back to analytic values.

Independence has limits: mpmath SVD is a different implementation/algorithm
(bidiagonalization and QR iteration) from the educational Jacobi SVD. mpmath
least squares is a separate high-precision implementation of the same
Householder mathematical family. NumPy projected eigensolves and SciPy dense
references may share LAPACK infrastructure. They are not described as fully
independent backends; analytic construction and independent controls are used
alongside them.

## 日本語

条件数と異方性、残差と前進誤差、数学的階数と数値階数、誤差推定値と実誤差を
分ける4例です。実行方法は上記と共通です。入力・判定基準は最初の計算前に
保存し、公差の事後緩和はしていません。49テストは警告をエラーとして合格しました。
`result.json` とCSVには、参照との差、入力SHA、実行環境、全判定、予算終了理由を保存します。
量子化学の計算は追加していません。

- **AMG:** n=7/15/31でκ₂を変え、各nでε=1/.1/.01を比較します。
  正方格子のこの系列ではκ₂はεによらず一定であり、異方性との同一視を避けます。
  独立疎行列LU、DST対角化、既知正弦解、解析固有値を別々に照合します。
  これは代数的診断です。連続Poisson解への格子次数は以前の教材に保持します。
  開発環境の9例は収束しましたが、任意異方性への頑健性を保証しません。
- **QR/SVD:** 厳密な二進行列のκ₂を1〜2³⁶へ変え、解の摂動増幅と再構成誤差を測ります。
  固定右辺摂動の既知応答は最大.0625です。機械丸めによる解誤差の下限を要求せず、
  より高精度な環境を失敗扱いしません。階数閾値を変えた解は同じ切捨て規約の参照と比較します。
  厳密階数2・反復予算0も検査します。
- **Krylov固有値:** クラスターでは個別固有ベクトルの符号・回転によらない部分空間を比較します。
  非正規系は実際の上三角入力にして解析固有値を保持します。
  残差2.5×10⁻⁸と前進誤差.005の対照は独立に構成した擬固有対であり、反復法の失敗出力とは呼びません。
- **求積:** 狭いピーク、端点、相殺、零積分、見逃す局所bumpを扱います。
  相殺では丸め誤差の絶対予算、零積分では相対条件数未定義を使います。
  Simpsonの推定誤差0が真の精度を保証しない例を残します。
  既知支持区間や変数変換による対照は、任意関数への自動的な救済を保証しません。

80/120桁の高精度参照は、実際のbinary64入力を整数比へ変換して、別環境で生成済みです。
通常の配布版追試は保存参照の照合と固定4例の再実行です。任意入力の高精度再生成や
大規模収束検証とは区別します。両精度・全4入力・実行ソースと入力のSHAを検査し、
欠落・破損時に解析解へ黙って差し替えることはありません。

## Scope, sources and rights / 検証範囲と利用条件

These educational kernels are adapted from the earlier MIT-licensed Atlas solver;
`source-provenance.json` records its immutable source SHA. Original source is
not overwritten. This release is not a production AMG/LAPACK/ARPACK/QUADPACK
replacement. Large coefficient jumps, general unstructured/indefinite systems,
arbitrary ill-conditioned singular-value relative accuracy, restarted/interior
Krylov problems, and general oscillatory/singular certified quadrature remain
outside scope. No universal monotonic convergence is asserted.

`source-review.json` distinguishes original-paper/author-preprint excerpts,
publisher abstracts and official implementation documentation; a full-text
audit of every paper is not claimed. The cited AMG/Jacobi/quadrature papers
motivate theory and limitations; this small source does not reproduce every
algorithm or theorem in those papers. Small dense contractions use explicit
NumPy einsum as in the earlier educational solver, without disabling warnings.

MIT applies to original Python code only. Text, figures, fixed inputs and
numerical data retain the separate site conditions in
[LICENSING.md](https://hrkoyama.github.io/LICENSING.md) and
[Rights & AI policy](https://hrkoyama.github.io/rights/).
Dependency libraries and third-party papers retain their own terms. No new
blanket permission is granted for non-code materials or third-party sources.

MITはここにあるオリジナルPythonコードのみです。本文・図・固定入力・数値データは
上記サイトの個別条件を参照し、依存ライブラリ・第三者論文の条件とは区別します。
論文の全手法・定理の再現や、全文監査は主張しません。
