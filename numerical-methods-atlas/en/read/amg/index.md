# Algebraic multigrid / AMG

AMG constructs a multilevel hierarchy and interpolation from a matrix. Smooth error means error that relaxation removes poorly, rather than only geometrically long-wavelength error.

## Problem and representative equations

For Au=b, use residual r=b−Au, restriction R and interpolation P. The Galerkin coarse operator is A_c=RAP. Correct the fine approximation using a coarse residual solve. The inverse in the formula expresses the principle; a multilevel cycle normally approximates that solve recursively.

$$
A_c=RAP,\qquad r=b-Au,\qquad u\leftarrow u+P A_c^{-1}Rr.
$$

## Algorithm

A cycle applies pre-relaxation, computes/restricts the residual, corrects on the coarse space and post-relaxes. Classical AMG uses strength connections and C/F splitting; aggregation variants group unknowns. Near-nullspace information, such as rigid motions for elasticity, must be represented by interpolation.

## Conditions and pitfalls

Success on a scalar elliptic problem does not ensure robustness for nonsymmetric advection, saddle points or strong anisotropy. CG preconditioning requires compatible symmetry/positive-definiteness properties. A pure-Neumann problem still has a constant nullspace and a right-hand-side compatibility condition.

Condition number alone does not determine AMG performance. Anisotropy direction, strength selection, the near-nullspace represented by interpolation and relaxation all affect convergence, even for positive-definite systems. Fixed isotropic/anisotropic matrix controls do not certify arbitrary elliptic problems or large parallel calculations.

## What to check

Use manufactured Poisson solutions while varying mesh size and coefficient contrast. Measure true residuals, solution errors and per-cycle reduction; record hierarchy sizes and nonzero counts. Few iterations do not establish small discretization error.

Preserve the historical manufactured-Poisson example. The additional release forms right-hand sides from known algebraic solutions and compares linear solves with an independent sparse direct solver and discrete-sine-transform diagonalization, also checking the analytic discrete spectrum. Record true relative residual, relative solution error, iteration history and hierarchy complexity separately while varying matrix size, anisotropy and conditioning at fixed residual tolerance and iteration budget. This added case is an algebraic conditioning diagnostic; it does not establish mesh convergence or accuracy against the continuous Poisson solution.

## Fixed-input examples and diagnostic controls

Distinguish the scope established by acceptance checks from a general mathematical guarantee; preserve historical inputs, measurements and criteria.

### Matrix-based AMG: distinguish residual and solution error

Fixed-target computation

Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution.

Only three fixed scalar grids are checked. Large coefficient jumps, strong anisotropy, elasticity, arbitrary unstructured meshes, optimal complexity and mesh-independent convergence are not certified. A small residual alone does not prove a small solution error.

[Input, results and acceptance](/numerical-methods-atlas/validation/sa-amg/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-foundations/#sa-amg) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py) · [Code solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/solvers.py) · [Tests test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py) · [ZIP](/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/foundations/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/foundations/verification.json)

### AMG: conditioning, anisotropy, residual and forward error

Diagnostic control; no physical-problem increment

Separate condition number from anisotropy on SPD systems of 49, 225 and 961 unknowns. Compare analytic spectra, independent sparse direct solutions and DST diagonalization, and measure how residual translates to forward error.

Only a small constant-coefficient family is checked. Arbitrary coefficient jumps, unstructured grids, indefinite systems, optimal complexity and uniform convergence are outside scope. No claim that anisotropy necessarily increases κ₂ or monotonically worsens convergence.

[Input, results and acceptance](/numerical-methods-atlas/validation/amg-conditioning/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-foundations-conditioning/#amg-conditioning) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py) · [Code experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py) · [Code fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py) · [Code mpmath_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py) · [Code solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py) · [Tests test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py) · [ZIP](/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/foundations-conditioning/verification.json)

## Publication scope

Historical inputs, measurements and tolerances are preserved. Additional conditioning, residual and convergence checks have a separate scoped release. Passing a diagnostic control can mean that its intended limitation was observed; it does not establish general success or reproduction of an entire paper.

## Sources

- J. W. Ruge and K. Stüben (1987). 4. Algebraic Multigrid. https://doi.org/10.1137/1.9781611971057.ch4
- P. Vaněk, M. Brezina, J. Mandel (2001). Convergence of algebraic multigrid based on smoothed aggregation. https://doi.org/10.1007/s002110000226
