# Checkerboard and rotated tensor diffusion

Two educational2D boundary-value examples distinguish continuum error, algebraic forward/energy error and independently recomputed residual. No claim of universal MG/AMG robustness or performance.

Python3.12. Install `requirements.txt`; run `python -W error -m pytest -q -p no:cacheprovider`, then `python -W error run.py --input inputs.json --output results`. All fixed primary and independent P1 reference solves run in main. Their combined scientific budget is120seconds. Plot separately with `requirements-plot.txt`: `python plot.py --results results/result.json --output results`.

Checkerboard: unit square, homogeneous Dirichlet, source1, quadrant coefficients100/1. FV point values at cell centres use shared harmonic fluxes; independently assembled aligned triangular P1 grids128/192 provide reference sensitivity, not exact solutions or certified error bounds. No singular convergence order is assumed.

Rotated tensor: Q1 full weak form, eigenvalues1/.01, anglepi/6, exact sine solution with independently derived nonzero cross-derivative source. The affine patch and u=xy,f=-2Kxy patch detect gradient, boundary and tensor errors.

Geometric and educational matrix-only SA hierarchies use identical matrices and right-hand sides, zero initial corrections, symmetric2/2weighted Jacobi, safe omega=.5/rowbound, Galerkin coarse matrices and terminal Cholesky. See DESIGN.md for the SPD argument and implementation probes. Existing old SA data/implementation are untouched. The new aggregate rule is adapted with attribution in source-provenance.json.

The small PCG driver is scoped to these fixed nonzero right-hand sides; arbitrary zero-RHS or indefinite systems are outside this packet.

All array fields, CSR matrices, face fluxes, reference fields, true residual histories, finite CSV records and strict result.json are saved. Source/input/acceptance SHA identities are checked before execution. Failed attempts and all original contracts are retained; acceptance thresholds are never fitted to outputs.

Source review: DuMux official TPFA derivation (scalar aligned transmissibilities and K-orthogonality restriction); hypre official symmetric smoother requirement for CG. No DuMux/hypre software is executed. Vanek et al.1996 publisher abstract only; full paper/proof unread. This is an original educational implementation, not BoomerAMG.
