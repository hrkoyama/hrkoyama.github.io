# Fixed interpolation, spline and Haar controls

This educational group contains three dimensionless approximation problems, not
three discretizations of a new physical PDE. All inputs and acceptance decisions
are fixed in `inputs.json` and `acceptance.json`. The reference operations below
are included in the same 120-second pytest-plus-main budget. Runtime has not been
measured before the first reviewed execution.

```
python -m pytest -q -W error test_approximation.py
python -B -W error run.py --input inputs.json --output fresh-results
python plot.py --results fresh-results/result.json --output fresh-results
```

The plot command also accepts a results directory. It reads saved arrays and does
not recompute an interpolant, spline fit or transform. Matplotlib is only imported
by `plot.py`; it is not part of the public Linux scientific-run dependency set.
The three direct pins are NumPy 2.0.2, SciPy 1.14.1 and pytest 8.3.5. A separate
plotting environment needs Matplotlib. No automatic installation is performed.

## 81: nodes, stored representations and evaluation

The functions are `1/(1+25*x*x)` and `abs(x)` on [-1,1], with degrees 8, 16 and
32 and 2048 fixed dyadic midpoint probes. This gives twelve interpolation rows
and six finite Chebyshev coefficient sets. The positive cosine-node table is
supplied as decimal literals in the input, reflected exactly, and qualified by a
bounded Decimal110 Machin/Taylor calculation. The actual binary64 values, not
ideal real cosine nodes, define the numerical experiment.

Four objects remain distinct:

* `P_stored`: the exact polynomial through the stored nodes and stored data,
  evaluated independently with Fraction Lagrange products at seventeen probes.
* `R_closed`: the exact rational barycentric expression using the supplied
  closed weights. Those weights need not be exact inverse-product weights for
  rounded Lobatto nodes. Its difference from `P_stored` is a representation error.
* `C_stored`: the exact Chebyshev series with the stored computed coefficients,
  evaluated by a separate Fraction forward basis recurrence. The finite
  Lobatto-inspired coefficient transform uses the actual rounded nodes; ideal
  discrete orthogonality is not asserted for them.
* `f_exact`: the mathematical Runge or absolute-value target at each probe.
  Fraction target values are rounded once for the displayed full-field error.

The barycentric and Clenshaw rounding defects at the seventeen certificate
probes are checked against operation-graph bounds, not one empirical epsilon.
Conditioning, denominator guard ratios, representation defects and actual
sampled function errors are saved separately. The fixed Runge comparison asks
only that the degree-32 equispaced sampled error exceed degree 16, while the
Lobatto-like error decreases. It does not assert monotone convergence for every
function, nor a continuous maximum-norm theorem from a finite probe grid.

## 82: C2 continuity versus shape preservation

Three fixed data sets (a flat-to-flat monotone plateau, a cubic and a line) are
fit by natural cubic splines, clamped cubic splines and PCHIP: nine fit records.
The primary C2 path solves a B-spline collocation system, then evaluates with de
Boor recursion. The independent reference solves the exact rational system for
nodal second derivatives and evaluates the resulting piecewise cubics. The
PCHIP path uses harmonic interior slopes and one-sided endpoint limiting;
independent Fraction formulas and SciPy 1.14.1 are comparisons. SciPy is a
secondary companion, not the only oracle.

Seven left-endpoint fixtures and their seven reversed right-endpoint versions,
plus one two-point fixture, make fifteen records, sixteen scalar outputs and
thirteen distinct data sets. Actual inputs and endpoint values are retained in
`endpoint-reference-records.json`.

The plateau uses `a=float(0.01)`, `b=float(1.01)`. Its independent witnesses at
x=1.5 are `a-9*(b-a)/88` for the natural spline and `a-15*(b-a)/152` for the
zero-clamped spline. Fraction converts the actual binary64 a and b, which differ
from the ideal decimal fractions 1/100 and 101/100. The PCHIP plateau is
`a+(b-a)*(3*s*s-2*s*s*s)` on [2,3], with constant exterior plateaux. The abbreviated
ideal-decimal expression is not used as the stored-input oracle. Natural and
clamped overshoot is a documented result, not a failure of interpolation.

## 83: finite Haar boundaries and shifts

Six input records (smooth32, step32, ramp17, step17, shifted step32 and shifted
step17) and two boundary rules make twelve three-level analyses. No threshold,
hard threshold and soft threshold make thirty-six reconstructions. The shifted
steps are cyclic one-sample shifts of their unshifted inputs; shift-back errors
are recorded separately. No shift-invariance pass criterion is imposed.

At each odd-length level, periodic extension appends the first sample and
half-sample symmetric extension appends the last sample. Synthesis crops to the
saved preceding length. This explicitly defined finite Haar layout is not a
claim of exact coefficient-layout compatibility with an external package.
Independent analysis and synthesis matrices plus exact unnormalized Fraction
pair sums with Decimal80 normalization qualify the primary pair kernels.

All `l2_squared` fields mean **sum of squares**, without square root or averaging.
For length 32, the square orthogonal transform preserves squared energy and the
squared reconstruction error equals the squared coefficient-change norm.
Length 17 produces twenty coefficients: the transform is redundant. Each level
instead records `energy_after = energy_before + appended_sample**2`. The cropped
reconstruction error is not forced to equal the redundant coefficient error.

## Saved evidence and scope

Each case has nonempty scalar metrics and actual record CSVs. NPZ files contain
the full sampled fields, nodes, weights, coefficients, derivative arrays,
independent matrices, references and error ledgers. JSON records contain no NaN
or infinity. Candidate arrays are retained before downstream reference work;
exceptions preserve a failed candidate and completed case/row checkpoints.
Source hashes use the explicit pre-run source inventory and never recursively
hash prior results from an extracted public ZIP.

`source-reading.json` records selected primary/official reading and unread
originals. Documentation publication dates that were not established remain
unknown; version numbers and access dates are separate. The unavailable de Boor
article, unread Berrut–Trefethen and Fritsch–Butland full texts are not claimed as
full-paper reviews. `DESIGN.md` gives the independently derived formulas.

## 日本語の要点

無次元の固定入力3例です。81は格納節点の補間多項式・閉重み有理式・格納係数級数・
目標関数を区別し、条件数と丸めを分けます。82はC2補間とPCHIPの形状保存を比較し、
実binary64を有理数化した独立式で平坦部の負値を確認します。83はHaarの境界処理・
1標本シフト・閾値を分離します。17点の対称拡張に正規直交エネルギー保存を強制しません。
参照計算を含めpytestとmainを共有120秒で行い、図は保存配列のみから作ります。
原入力・判定値・失敗履歴は実行後に緩和・上書きしません。
