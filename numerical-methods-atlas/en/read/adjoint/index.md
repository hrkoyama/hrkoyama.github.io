# Implicit differentiation and adjoints: Bratu parameter sensitivity

Implicit differentiation and adjoints: Bratu parameter sensitivity


Compute how a converged numerical solution responds to a changing coefficient. Implement implicit state sensitivities and a discrete adjoint gradient for Bratu’s equation, then check them against an exact continuous family, re-solved parameter differences and spatial refinement.


Differentiate the converged equation


Consider a state u defined by an equation depending on parameters θ rather than by an explicit formula. For n states and m parameters, denote residual partial derivatives by J and B. All gradients below are column vectors.



$$
F(u(\theta),\theta)=0,\qquad J=F_u\in\mathbb R^{n\times n},\qquad B=F_\theta\in\mathbb R^{n\times m}.
$$

If F is continuously differentiable near the solution and J is nonsingular, the implicit function theorem defines a local derivative of the solution. Applying the chain rule gives a sensitivity equation. This does not establish global uniqueness or automatically select one branch among several roots.


Implicit differentiation: solve the sensitivity equation



$$
J S+B=0,\qquad S=\frac{du}{d\theta},\qquad J s_v=-Bv,\qquad s_v=S v.
$$

S is the state Jacobian with respect to all parameters. If only one direction v is needed, solve one linear system with right-hand side −Bv. Do not explicitly form an inverse of J. Analytic expressions, AD or appropriately checked finite differences can supply J and B.


The example first solves the primal problem using the existing Newton method, then assembles residual partial derivatives at the computed state. AD evaluates local derivatives of the residual. The implementation does not differentiate an unrolled finite sequence of Newton iterations.


Discrete adjoints: obtain an objective gradient


Observation fitting and design often need the total derivative of a scalar objective rather than every state sensitivity. Separate the partial derivative r at fixed state from the contribution Sᵀq due to the changing state.



$$
\widehat L(\theta)=L(u(\theta),\theta),\qquad q=\nabla_uL,\quad r=\nabla_\theta L,\qquad \nabla_\theta\widehat L=r+S^Tq.
$$

Solving a transpose system gives the same gradient without storing every column of S. The Lagrangian convention used here subtracts the residual term, so the term involving B has a minus sign.



$$
J^Tp=q,\qquad \boxed{\nabla_\theta\widehat L=r-B^Tp}.
$$


$$
\mathcal L(u,\theta,p)=L(u,\theta)-p^TF(u,\theta),\qquad \nabla_u\mathcal L=q-J^Tp=0.
$$

With many parameters and few objectives, adjoint solves per objective can replace sensitivity solves per parameter. Factorizations can be shared across right-hand sides, and a VJP can evaluate Bᵀp. This one-parameter, one-objective example has one right-hand side for either method and makes no speed claim. The implementation assembles and solves small dense matrices.


The same Bratu discretization and branch


Use the same Bratu equation on [0,1] with zero Dirichlet data as in the AD chapter. Here n counts interior unknowns. Coordinates, state, parameter and objective are dimensionless in this educational model. The grid and boundary data are independent of the parameter.



$$
-u^{\prime\prime}-\lambda e^u=0,\quad 0The continuous problem has an exact family parameterized by α. The point α=1 uses the same parameter as the earlier Bratu example. The verification uses α=1 and 2, both corresponding to the smaller-solution branch reached from zero initial data.



$$
u_\alpha(x)=-2\log\!\frac{\cosh(\alpha(x-1/2))}{\cosh(\alpha/2)},\qquad \lambda(\alpha)=\frac{2\alpha^2}{\cosh^2(\alpha/2)},
$$


$$
\frac{d\lambda}{d\alpha}=\lambda\left(\frac2\alpha-\tanh\frac\alpha2\right),\qquad s_*(x)=\frac{\tanh(\alpha/2)-2(x-1/2)\tanh(\alpha(x-1/2))}{d\lambda/d\alpha}.
$$

Evaluate s_* at the grid nodes as an independent reference for the discrete sensitivity s. The continuous solution is not assumed to be an exact root of the discrete equations. Sensitivity can diverge at a fold where dλ/dα vanishes. Branch switching, passage through singular points and continuation of the upper branch are outside the verified scope.


Retain the objective’s explicit parameter dependence



$$
L_h(u,\lambda)=\frac h2\sum_{i=1}^{n}u_i^2+\frac\beta2\lambda^2,\qquad \beta=0.05,\qquad q=h u,\quad r=\beta\lambda.
$$

The first term is a trapezoidal approximation of the integral of half the squared state. Zero endpoint values leave only interior contributions. The second term deliberately retains explicit parameter dependence, so dropping βλ can be detected separately from the state-mediated contribution. This is a defined derivative-check objective, not a fit to observational data.



$$
J^Tp=h u,\qquad g_{\mathrm{direct}}=\beta\lambda+h u^T s,\qquad g_{\mathrm{adjoint}}=\beta\lambda+p^T e^u.
$$

Here p is a discrete adjoint in the Euclidean inner product; the quadrature weight h is included in q=h u. Do not identify p directly with nodal values of a continuous PDE adjoint defined in an L² inner product. Nonuniform grids, finite elements and parameter-dependent quadrature require consistent treatment of mass matrices and weights.


Verification: separate sensitivities, gradients and spatial error




The [saved measurements and source hashes](/numerical-methods-atlas/assets/bratu-sensitivity.json) record controls, tested points, residuals and errors.


Residual partial derivatives. Treat state and parameter as independent inputs; compare AD evaluations of J and F_λ with analytic expressions. A parameter-only seed holds u fixed.

Sensitivity and adjoint equations. Use the same converged state and recompute each linear-system residual. Compare direct and adjoint gradients, including the explicit βλ term.

Parameter differences. Solve the nonlinear problem again at λ+ε and λ−ε before differencing the objective. Perturbing λ while holding the state fixed does not test the total derivative.

Spatial refinement. For n=15, 31 and 63 compare discrete sensitivity with the exact continuous s_* in the maximum nodal norm. Direct–adjoint agreement alone does not establish spatial accuracy.


Saved measurements. The points α=1 and 2 have λ≈1.5728955 and 3.3597947. All six regular cases start at zero with an absolute primal residual Euclidean tolerance of 10⁻¹⁰ and at most 40 updates. Direct and adjoint gradients differ by less than 1.4×10⁻¹⁵. Primal residuals are at most 5.3×10⁻¹¹; the relative sensitivity and adjoint residuals defined below are at most 2.3×10⁻¹³ and 1.9×10⁻¹³, respectively.


For n=15, 31 and 63, maximum nodal sensitivity errors are approximately 3.0015×10⁻⁴, 7.4860×10⁻⁵ and 1.8704×10⁻⁵ at α=1; at α=2 they are 2.6708×10⁻², 6.4898×10⁻³ and 1.6112×10⁻³. Halving h reduces errors by about four; the coarser α=2 grid shows a larger departure from the asymptotic regime. These are spatial sensitivity errors, not direct–adjoint discrepancies.



$$
g_{\mathrm{FD}}(\varepsilon)=\frac{L_h(u(\lambda+\varepsilon),\lambda+\varepsilon)-L_h(u(\lambda-\varepsilon),\lambda-\varepsilon)}{2\varepsilon}.
$$

The n=31 difference check uses 17 perturbations ε from 10⁻¹ to 10⁻⁹. In this saved run, agreement is good near ε=10⁻⁵, where the absolute gradient difference for α=2 is about 4.0×10⁻¹¹. At ε=10⁻⁹ it grows to about 1.3×10⁻⁶. Making perturbations ever smaller does not give an ever more accurate gradient.



The parameter perturbation ε and spatial mesh spacing h are different quantities. Sweep ε and vary the nonlinear solve tolerance to expose regimes dominated by truncation, incomplete convergence or roundoff. Finite differences provide an independent check, not a uniformly optimal reference at every perturbation.


The Bratu Jacobian here is symmetric, so replacing Jᵀ incorrectly by J would escape detection on this problem alone. A separate manufactured implicit system with a nonsymmetric matrix and multiple parameters therefore independently checks direct sensitivities and adjoint gradients. That test checks transposition, signs and shapes; it does not validate another physical model.


A separate α=2, n=31 sweep uses primal tolerances 10⁻², 10⁻⁶ and 10⁻¹⁰. At ε=10⁻⁴, absolute finite-difference gradient error decreases from about 3.2×10⁻⁵ for the loose 10⁻² solve to about 3.5×10⁻⁸ for the two tighter settings. The 10⁻⁶ and 10⁻¹⁰ controls accept the same Newton iterates, so their curves overlap. Do not interpret every tolerance tightening as a distinct result or a strict monotonic improvement.


Incomplete solves, conditioning and unrolled iterations



$$
r_F=\|F(u,\lambda)\|_2,\qquad \rho_s=\frac{\|Js+F_\lambda\|_2}{\|F_\lambda\|_2},\qquad \rho_p=\frac{\|J^Tp-q\|_2}{\|q\|_2}.
$$

Primal, sensitivity and adjoint equations have separate residuals. A small linear residual does not repair an unconverged state: derivatives are then evaluated at an approximate state rather than an exact root. An ill-conditioned J can amplify small primal errors into state or gradient errors. Conditioning also depends on scaling and grid size, so cross-grid condition numbers are not algorithm rankings.


Differentiating finitely many iterations gives the derivative of a map depending on the initial state and executed updates. Implicit differentiation targets the equations defining a local converged solution. State that distinction when differentiating through stopping criteria, line searches or adaptive decisions. A computed gradient alone establishes neither inverse-problem identifiability nor optimizer convergence.


Continuous sensitivities and applicability



$$
-s^{\prime\prime}-\lambda e^u s=e^u,\qquad s(0)=s(1)=0.
$$

Differentiating the continuous Bratu equation with respect to λ gives this boundary-value problem. Here centered differences also provide its natural discretization, and refinement can be checked against s_* from the exact family. In general, discretizing a continuous adjoint and differentiating a discrete residual need not agree on a finite mesh. Include parameter dependence of boundaries, grids, observation operators and quadrature weights.


Verified scope is a specified smooth steady Bratu branch and a small nonsymmetric manufactured system. It does not cover shocks, limiters, contacts/events, transient adjoints, singular bifurcation points or inverse fitting to real observations. Read discretization error, derivative implementation and physical-model validity separately.


A separate continuous reference is also provided for the objective gradient. Integrate the exact-family u_α and s_* and compare 96- and 192-point Gauss quadrature.



$$
g_* =\beta\lambda+\int_0^1 u_\alpha(x)s_*(x)\,dx.
$$

The references are about 0.1027083914 at α=1 and 0.5823748758 at α=2. The n=31 discrete adjoint gradients are about 0.1027218294 and 0.5857608186, respectively. Spatial error remains despite near-machine-precision direct–adjoint agreement. The two quadrature orders differ by less than 4.4×10⁻¹⁵ in both cases; their difference is a convergence diagnostic rather than a rigorous quadrature error bound.


Run and inspect the fixed release


Extract the [dated release ZIP](/code/bratu-sensitivity/2026-11-22/bratu-sensitivity-2026-11-22.zip) and follow its [README](/code/bratu-sensitivity/2026-11-22/README.md) in a new Python environment. The earlier AD supplement and other releases are not overwritten.


python -m pip install -r requirements.txt
python scripts/build_bratu_sensitivity.py
python -m pytest tests/test_bratu_sensitivity.py

Inspect the [sensitivity/adjoint source](/code/bratu-sensitivity/2026-11-22/numart/bratu_sensitivity.py), [figure and evidence builder](/code/bratu-sensitivity/2026-11-22/scripts/build_bratu_sensitivity.py), [test source](/code/bratu-sensitivity/2026-11-22/tests/test_bratu_sensitivity.py), [file inventory and SHA-256 hashes](/code/bratu-sensitivity/2026-11-22/source-manifest.json), and [independent-extraction verification record](/code/bratu-sensitivity/2026-11-22/verification.json).


The existing AD foundation chapter explains how residual derivatives are obtained. Blondel et al. (2022), Section 2.1, and the official JAXopt references provide further discussion of root derivatives and their JVP/VJP constructions. This independent example uses NumPy and adds neither a JAX/JAXopt dependency nor a performance comparison with those libraries.


[Automatic differentiation foundation](/numerical-methods-atlas/en/read/automatic-differentiation/) · [Newton and conditioning](/numerical-methods-atlas/en/read/sparse-nonlinear/)


The nine dedicated tests are rerun from an independently extracted copy of the release. The verification receipt also records checks of numerical evidence, the rebuilt figure and file hashes.

## Publication scope

An educational implementation verifies implicit state sensitivity and a discrete adjoint gradient on a specified smaller-solution Bratu branch, with a separate nonsymmetric multiparameter manufactured transpose test. State, derivative, mesh and parameter-perturbation errors are separated. Scope is small steady dense systems; it does not provide general reverse-mode AD, transient adjoints, singular-point continuation or a real-data inverse solver.

## Sources

- Antony Jameson (1988). Aerodynamic design via control theory. https://doi.org/10.1007/bf01061285
- Seppo Linnainmaa (1976). Taylor expansion of the accumulated rounding error. https://doi.org/10.1007/bf01931367
- Mathieu Blondel, Quentin Berthet, Marco Cuturi, Roy Frostig, Stephan Hoyer, Felipe Llinares-López, Fabian Pedregosa and Jean-Philippe Vert (2022). Efficient and Modular Implicit Differentiation. https://doi.org/10.52202/068431-0378
- The JAXopt authors (2026). Implicit differentiation; root_jvp and root_vjp. https://jaxopt.github.io/stable/implicit_diff.html
