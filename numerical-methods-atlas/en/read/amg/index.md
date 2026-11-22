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

## What to check

Use manufactured Poisson solutions while varying mesh size and coefficient contrast. Measure true residuals, solution errors and per-cycle reduction; record hierarchy sizes and nonzero counts. Few iterations do not establish small discretization error.

## Publication scope

Links lead to existing educational code and dated verification records. This reading/translation update changes no scientific code or historical measurements and does not claim reproduction of an entire paper.

## Sources

- J. W. Ruge and K. Stüben (1987). 4. Algebraic Multigrid. https://doi.org/10.1137/1.9781611971057.ch4
