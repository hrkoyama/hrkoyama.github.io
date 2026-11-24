# Sparse and nonlinear systems: measure the actual residual

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/sparse-nonlinear/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Restarted GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en>)
- [BiCGSTAB](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bicgstab/?lang=en>)
- [Jacobi / diagonal preconditioning](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobi-preconditioner/?lang=en>)
- [Unpivoted ILU(0)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ilu0/?lang=en>)
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)
- [Newton–Krylov with assembled Jacobian](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton-krylov/?lang=en>)
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)

  The common example solves the forward boundary-value problem with damped Newton. Related method pages lead to separate editions for automatic differentiation, sensitivities, adjoints and coefficient fitting. Sensitivity and inverse problems with one or two coefficients have separate inputs and acceptance checks; they are not added to the common forward execution entry.
- [Automatic differentiation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en>)

  The common example solves the forward boundary-value problem with damped Newton. Related method pages lead to separate editions for automatic differentiation, sensitivities, adjoints and coefficient fitting. Sensitivity and inverse problems with one or two coefficients have separate inputs and acceptance checks; they are not added to the common forward execution entry.
- [Implicit differentiation and adjoint methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en>)

  The common example solves the forward boundary-value problem with damped Newton. Related method pages lead to separate editions for automatic differentiation, sensitivities, adjoints and coefficient fitting. Sensitivity and inverse problems with one or two coefficients have separate inputs and acceptance checks; they are not added to the common forward execution entry.
- [Gradient and quasi-Newton optimization](<https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en>)

  The common example solves the forward boundary-value problem with damped Newton. Related method pages lead to separate editions for automatic differentiation, sensitivities, adjoints and coefficient fitting. Sensitivity and inverse problems with one or two coefficients have separate inputs and acceptance checks; they are not added to the common forward execution entry.
- [Restarted GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [BiCGSTAB](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bicgstab/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Jacobi / diagonal preconditioning](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobi-preconditioner/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Unpivoted ILU(0)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ilu0/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

## Equations

- [Bratu nonlinear boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en>)

  The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Linear advection](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en>)

  Transport at constant speed a: translation, numerical diffusion and stability. This is a steady discrete advection-diffusion matrix. Linked entries explain its transport and diffusion components; neither alone represents the complete matrix problem.
- [Heat / diffusion equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en>)

  A representative constant-diffusivity form: mode decay, time integration and boundaries. This is a steady discrete advection-diffusion matrix. Linked entries explain its transport and diffusion components; neither alone represents the complete matrix problem.
- [Bratu nonlinear boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en>)

  The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-bratu-en>)

  31/63/127 interior nodes and a zero initial guess select the lower branch with βtanh(β/2)<2; no upper-branch or bifurcation tracking.

## Problem figures

- [One-dimensional Bratu boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png
- [Nonsymmetric advection-diffusion discrete manufactured system](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sparse-advection-diffusion.png
- [Damped Newton root of a cubic equation](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/cubic-root.png

## Exact / reference solutions

- [One-dimensional Bratu boundary-value problem — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#references-en>)

  Check a hyperbolic-function continuum solution on the lower branch and mesh refinement. Follow-on sensitivity/inverse examples validate derivatives and objectives separately; Bratu has no card in the 18-case reference library.
- [Nonsymmetric advection-diffusion discrete manufactured system — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=en#references-en>)

  Use a manufactured discrete system b=A x from a known vector to check true residual and solution error. Distinguish this from verification against an exact continuum advection-diffusion solution.
- [Damped Newton root of a cubic equation — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/?lang=en#references-en>)

  Use the known real root x=1 of x³-1=0 and its residual to check Armijo-damped Newton convergence.
- [1D Bratu: Newton–GMRES on the lower branch — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/?lang=en#bratu-en-validation>)

  CSV carries finest-grid numerical/analytic values and absolute error. JSON retains each mesh's nonlinear residual, Newton iteration count and minimum damping length.

## Code and validation

- [Symmetric saddle systems and Schur preconditioning](<https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en>)
  availability: run

  MINRES and GMRES use the same original-system residual criterion and are checked against the ideal Schur three-point spectrum.
- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en>)
  availability: run

  Solve both Bratu branches with three Jv choices without assembling the nonlinear Jacobian; retain forcing, actual residuals and evaluation counts.
- [Bratu sensitivity near the discrete fold](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en>)
  availability: run

  At six fixed points approaching the discrete Bratu fold, separate state error from linear-solve tolerance and compare against independent shooting gradients.
- [Matrix-free VJP for distributed Bratu coefficients](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en>)
  availability: run

  Represent8/16/32 spatial controls with two local hat weights per node; compare objective-wise adjoint VJPs with a separate full-sensitivity reference.
- [1D Bratu: Newton–GMRES on the lower branch](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/?lang=en>)
  availability: run

  Solve the lower branch of −u''=λexp(u), with β=1 and λ=2β²/cosh²(β/2), starting at zero. Check the analytic solution, recomputed nonlinear residual and second-order refinement on 31/63/127 interior nodes.
- [Crossing the Bratu fold with pseudo-arclength continuation](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en>)
  availability: run

  Follow the lower and upper branches of the same one-dimensional Bratu boundary-value problem; check tangents, the fold and spatial error against an independent analytic family.
- [Line search and trust regions from the same difficult starts](<https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en>)
  availability: run

  Compare Newton, Armijo and dogleg from identical fixed starts, distinguishing roots from stationary nonroots and budget exhaustion.
- [Robertson kinetics: initial stiffness and actual error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en>)
  availability: run

  Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references.
- [Robertson conservation DAE and stored official IDA values](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en>)
  availability: run

  Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. The first retained run missed four original time-accuracy and refinement goals.
- [Van der Pol: an early stiffness transition](<https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en>)
  availability: run

  Separate local control from global error. The first study met 208 of 209 original targets; the mu = 1 tight adaptive run missed the 2e-5 global goal.
- [Consistent initialization and discrete residuals for an index-one DAE](<https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en>)
  availability: run

  Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch.
- [Enzyme conservation and QSSA](<https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en>)
  availability: run

  Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism.
- [Restarted GMRES — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [BiCGSTAB — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bicgstab/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Jacobi / diagonal preconditioning — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobi-preconditioner/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Unpivoted ILU(0) — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ilu0/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Armijo-damped Newton — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Newton–Krylov with assembled Jacobian — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton-krylov/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [One-dimensional Bratu boundary-value problem — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
- [Nonsymmetric advection-diffusion discrete manufactured system — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
- [Damped Newton root of a cubic equation — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
