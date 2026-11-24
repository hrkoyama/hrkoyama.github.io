# Small fixed linear algebra and spectral examples (51–54)

The R4 scientific core covers four fixed cases, with 27 main records, 16
independent reference checks and 195 scientific decisions. Its primary validation
passed all 29 pytest tests and all fixed checks. The R5 overlay changes English
metadata, documentation and figure labels only. Read the actual result.json and
packaged verification.json for independent package verification. Source presence
and component qualification alone are not evidence of full scientific success.

Use Python 3.12 and exactly NumPy 2.0.2, SciPy 1.14.1 and pytest 8.3.5. Plotting
also uses Matplotlib 3.9.4. No compiler is needed. Pytest and the main driver share
a 120-second limit. Plotting is separate and uses saved arrays without running
a solver or regenerating a reference.

```
python -B -W error -m pytest -q -p no:cacheprovider
python -B -W error run.py --input inputs.json --output fresh-output
python plot.py --results fresh-output/result.json --output figures
```

The output directory must be fresh. Plot --results accepts result.json or its
directory. Full NPZ arrays, case-keyed checks, metrics and finite CSV summaries
are retained. Gallery previews show saved matrices or eigenvectors. No parameter
scan, warning suppression, numerical-state floor or tolerance relaxation is used. The
acceptance file is unchanged: its historical proposed label records the original
freeze and does not overwrite later execution history.

## Direct factorizations and refinement

Original partial-pivot LU, lower Cholesky and triangular solves use exactly five
refinement updates. Factors and correction solves use binary32; residuals and
accumulation use binary64. This differs from the same-precision RFS described in
the selected LAPACK Users Guide passage. Fixed inputs are an SPD tridiagonal
matrix, a nearly singular rank-one perturbation, Hilbert 5 and Wilkinson 12.

Exact Fraction elimination of the actual binary64 A and b and separate LAPACK
DGESV/DPOSV comparisons supply references. Infinity conditioning, forward error,
normwise and componentwise backward error, and pivot growth are distinct. Growth
is measured from a binary64 LU reconstruction, not the binary32 correction
factor. A small residual alone is not a forward-error certificate.

The saved `exact` vector is formed by solving the actual binary64 inputs with
exact Fraction arithmetic, then rounding each solution component to binary64.
Forward errors are differences from that rounded reference, not a high-precision
subtraction from the unrounded rational solution. In the direct-case logarithmic
history figure only, exact zero errors are displayed at `float64.tiny`
(approximately 2.225e-308) by the existing `maximum` display expression. This
marker does not change saved errors, solver states, acceptance decisions or any
positive error; it is not a nonzero measured error. The axis label and footnote
identify both conventions.

日本語: 保存参照は厳密Fraction解を成分ごとにbinary64へ丸めたものです。誤差はその
丸め済み参照との差であり、未丸め有理数解との高精度差分ではありません。直接解法の
対数履歴図だけは、ゼロ誤差をfloat64.tinyへ置いて表示します。保存値・解法・判定を
変える操作でも、非ゼロの測定誤差でもありません。

## Symmetric-indefinite saddle controls

Algebraic mixed-Poisson/Stokes-type blocks use velocity sizes 12 and 24; they are
not a full fluid PDE. Stored-basis Lanczos least squares with full
reorthogonalization is the educational MINRES variant, not compact production
Paige–Saunders MINRES. Full GMRES uses the same original-system stopping residual.
An SPD congruence applies a dense ideal-Schur preconditioner with exact spectrum
1, (1±sqrt(5))/2. A scalable approximate Schur preconditioner is not claimed. One
negative-curvature control does not imply that CG fails on every indefinite input.

The raw Schur block is saved before the guarded definition
Ssym=(Sraw+Sraw.T)/2. Strict symmetry and pivot checks remain. The internal target
min(1e-9, forward_limit/kappa_inf(A)) is shared by both methods and preconditioners.
For symmetric A, kappa2<=kappa_inf and relative forward error is bounded by
kappa2 times the relative residual in exact arithmetic. The matrix-only condition
estimate is not a certified interval and uses no reference solution. Independent
forward-error and original-residual gates of 2e-8 and 1e-9 remain unchanged.

## Explicit restarting and shift-invert

The fixed Dirichlet Laplacian of size 31 has a closed discrete sine spectrum.
Two-pass Arnoldi is explicitly restarted from one selected Ritz vector, using
restart lengths 8 and 16. No implicit restarting, Krylov-Schur, locking, or general
nonnormal or clustered-spectrum capability is claimed. The unshifted largest
pair and shifts 0 and 950 target endpoint or interior eigenpairs.

Shifted solves have fixed residual guards. Krylov applications, shifted-system
residual actions and original eigenproblem residual actions are counted
separately, not presented as elapsed time or flop counts. This is a fixed-matrix
comparison, not a continuum PDE grid-convergence study. Bibliography task 55 is
a separate reading record.

## Consistent-mass P1 string and actual LOBPCG

A unit string has unit tension and density, homogeneous Dirichlet endpoints and
15, 31 or 63 interior nodes. The first three eigenpairs are computed with an
original M-inner-product Krylov method on K^-1 M and actual SciPy 1.14.1 LOBPCG,
using exact-K-inverse preconditioning. Neither algorithm wraps the other.

Generalized LAPACK, closed discrete spectra and the continuum values (j*pi)^2
separate algebraic and discretization errors. Residual, M-orthogonality,
refinement ratios and action budgets remain distinct. Some reduced LAPACK
primitives are shared; exact spectra and rational arithmetic provide independent
algebraic checks.

LOBPCG starts from {1, x^3, x^6}. With K=h^-1 tridiag(-1,2,-1) and
M=h/6 tridiag(1,4,1), K^-1 M1=x(1-x)/2-h^2/6 lies in span{1,x,x^2}; that older
initial block lost a preconditioned direction. Degree-plus-two images of
{1,x^3,x^6} avoid the structural dependence. This R3 change is retained.

R4 changes only the same mass matrix's action inside SciPy: B is a LinearOperator
using the existing S.mv einsum matvec and matmat. No matrix, inner product,
solver, initial block, tolerance, iteration limit or action cap changes. Failed
mass-action arguments and original exceptions are retained before a library
handler can replace them. Unreturned internal SciPy iterates are not claimed to
be available. Inputs are saved before entry and returned arrays before diagnostics.

## Preserved failures and qualification scope

R2 passed 26 tests and 16 reference checks but missed two saddle forward-error
gates and stopped at LOBPCG. R3 passed 27 tests and 16 reference checks, completing
26 of 27 records and 186 of 195 gates, then stopped at the initial n63 B action
with None.shape. The underlying exception was lost. Old sources, inputs,
criteria, full partial fields and raw logs remain unchanged in persistent private
storage. This package does not claim to include every historical field or turn
those failed attempts into successes.

A separately frozen saved-n63 component ran once: 35 of 35 checks passed in
0.303385584 seconds, with no LOBPCG, eigenproblem or PDE execution. Three direct
dense products raised RuntimeWarning: divide by zero encountered in matmul under
-W error. Five existing-einsum and LinearOperator products qualified against
exact Fraction dot products. This observes a present operation failure, not the
identity of the historical lost exception or a guarantee of full-case success.
The compact references/mass-action-qualification.json records that scope; full
raw evidence and tracebacks remain in private storage.

Selected official LAPACK, SOL, SLEPc and SciPy documentation supports the limited
scope. The unchanged references/source-review.json retains its earlier reading
record and original-paper gaps. Later bibliography-only reading is a separate
record, not silently inserted into that historical source.

日本語: 固定4例の入力・独立参照・195判定を維持し、R4で同じ質量行列の作用経路だけ
を変更しました。旧27テストは不変、実一般化3固有対/質量自己共役性と例外保存の
2回帰を追加。旧R3は未完了で失敗を保持しています。R5は英語・図ラベルだけの表示
修正です。成分35判定は本計算の合格を代用しません。結果/検証JSONを参照し、
連続体・代数誤差、元残差、M直交性、作用回数を混同しません。

R7 changes only the direct-figure reference/zero-display disclosures in labels,
captions and this README. R6 source and successful package evidence are retained;
all 29 tests, 27 records, 16 reference checks and 195 scientific gates are unchanged.
