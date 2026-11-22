# Krylov eigenvalue solvers

Krylov eigensolvers approximate a few eigenpairs through a small subspace instead of diagonalizing a large matrix in full. Arnoldi, symmetric Lanczos and shift-invert require different assumptions.

## Problem and representative equations

Build Kₘ(A,v)=span{v,Av,…,Aᵐ⁻¹v}. Arnoldi gives an orthonormal Vₘ and upper-Hessenberg Hₘ. Solve Hₘy=θy and set x=Vₘy. The last Arnoldi vector and hₘ₊₁,ₘ give the Ritz residual.

$$
AV_m=V_mH_m+h_{m+1,m}v_{m+1}e_m^T,\qquad \|Ax-\theta x\|_2=|h_{m+1,m}e_m^Ty|\quad(\|y\|_2=1).
$$

## Algorithm

Expand the basis using matrix-vector products and orthogonalization, solve the projected eigenproblem and restart when needed. Hermitian matrices permit a Lanczos three-term recurrence. Shift-invert targets interior eigenvalues but each inverse action requires a linear solve.

## Conditions and pitfalls

Finite-precision loss of orthogonality can create ghost duplicates. For nonnormal matrices, a small residual need not imply a comparably small eigenvalue error. State B and the inner product in generalized problems Ax=λBx, and assess inner-solve tolerances for shift-invert.

## What to check

Check scaled residuals ∥Ax−θx∥/(∥A∥+|θ|), orthogonality, known eigenpairs and clustered/repeated eigenvalues. For symmetric cases compare Rayleigh quotients, and record restarts and initial-vector sensitivity.

## Publication scope

Reading, representative equations and sources are published. Dedicated code and numerical verification remain planned. The suggested checks above are not measured results, and code/results of other methods are not presented as validation of this method.

## Sources

- W. E. Arnoldi (1951). The principle of minimized iterations in the solution of the matrix eigenvalue problem. https://doi.org/10.1090/qam/42792
- C. Lanczos (1950). An iteration method for the solution of the eigenvalue problem of linear differential and integral operators. https://doi.org/10.6028/jres.045.026
