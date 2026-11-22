# Bratu inverse problem: estimate λ from synthetic observations with adjoint gradients

Bratu inverse problem: estimate λ from synthetic observations with adjoint gradients


A forward problem computes a state from a coefficient; an inverse problem estimates that coefficient from observations of the state. Fit one Bratu parameter λ to five observations and use the previous chapter’s discrete adjoint gradient in the actual optimization updates. The model, boundary conditions and observation positions are known in this small synthetic problem.

Specify the known inputs and the unknown parameter

State u, coordinate x and coefficient λ are dimensionless in this educational model. The grid, interval [0,1], zero Dirichlet boundary conditions, observation operator H and weights W are fixed. Only λ is unknown; model form and boundary values are not inferred simultaneously. Use centered differences with n interior unknowns and re-solve the nonlinear equation at each trial parameter.


$$
-u^{\prime\prime}-\lambda e^u=0,\quad u(0)=u(1)=0,\qquad F_h(u,\lambda)=D_hu-\lambda e^u=0,\quad D_h=h^{-2}\operatorname{tridiag}(-1,2,-1),\quad h=(n+1)^{-1}.
$$

$$
u_\alpha(x)=-2\log\!\frac{\cosh(\alpha(x-1/2))}{\cosh(\alpha/2)},\quad\lambda(\alpha)=\frac{2\alpha^2}{\cosh^2(\alpha/2)},\qquad\alpha_*=1.5,\quad\lambda_*\approx2.684636137266.
$$
The generating values are α*=1.5 and λ*≈2.684636137266. Restrict λ to [0.2,3.4] and start every state solve at zero to target the smaller-solution branch. Numerical branch selection is part of the problem specification. Fitting on the upper branch or continuing through a fold is not verified.

Observation operators and weighted least squares


$$
x_{\rm obs}=(1/8,1/4,1/2,3/4,7/8),\qquad r_h(\lambda)=H_hu_h(\lambda)-d,\quad W=\operatorname{diag}(w_j),\quad w_j=1/5.
$$
Five sensors lie at x=0.125, 0.25, 0.5, 0.75, 0.875. They coincide with grid nodes for n=15,31,63,127, so H selects interior state entries; no interpolation error is introduced. A row observing a fixed zero endpoint is zero. Save the observations d before optimization and keep them fixed rather than regenerating them for each trial λ.


$$
\Phi_h(\lambda)=\frac12 r_h(\lambda)^TWr_h(\lambda)+\frac\gamma2(\lambda-\lambda_{\rm prior})^2,\qquad\gamma\ge0,\quad\ell=0.2\le\lambda\le b=3.4.
$$
All published experiments use γ=0 and wⱼ=1/5, making the objective half the mean squared observation residual. The implementation also accepts positive nonuniform weights and γ≥0, with separate tests for the weights and explicit prior term. Interpreting W as an inverse error covariance would require a specified probability model; none is assumed here.

Build an adjoint gradient from observation residuals


$$
J=F_u=D_h-\lambda\operatorname{diag}(e^u),\quad F_\lambda=-e^u,\quad q=H_h^TWr_h,\qquad J^Tp=q.
$$

$$
\frac{d\Phi_h}{d\lambda}=\underbrace{\gamma(\lambda-\lambda_{\rm prior})}_{\text{explicit parameter term}}-p^TF_\lambda=\gamma(\lambda-\lambda_{\rm prior})+p^Te^u.
$$
The state partial derivative q includes both the transpose of H and the observation weights. With the Lagrangian convention Φ−pᵀF, subtract pᵀF_λ from the explicit parameter derivative. Since F_λ=−exp(u), the Bratu state-mediated term has a plus sign. Setting γ=0 removes the explicit term, not the state-mediated term.

Assemble J at the converged primal state and solve Jᵀp=q using the existing implicit-differentiation linear algebra. Do not differentiate an unrolled Newton iteration sequence. This Bratu J is symmetric: an independent nonsymmetric manufactured problem tests transposition in the previous release, while the new dedicated tests check the observation operator, nonuniform weights and regularization.

There is one parameter and one objective, so a direct sensitivity solve Js=exp(u) also has one right-hand side. This example demonstrates no adjoint speed advantage. It checks a construction that can extend to many parameters on a small inverse problem.

Run a gradient method with box constraints


$$
\Pi_{[\ell,b]}(z)=\min(b,\max(\ell,z)),\qquad\lambda_{\rm trial}=\Pi_{[\ell,b]}(\lambda_k-a g_k),\quad\Delta\lambda=\lambda_{\rm trial}-\lambda_k.
$$

$$
\Phi_h(\lambda_{\rm trial})\le\Phi_h(\lambda_k)+c g_k\Delta\lambda,\qquad c=10^{-4},\quad a=10\,2^{-j},\quad j=0,1,\ldots .
$$
Update λ using its current adjoint gradient g and project into the interval. Restart the step length at a=10 on each iteration and halve it until the sufficient-decrease inequality holds. Use the actual displacement after projection in gΔλ. Accepted and rejected trial evaluations use the same primal controls. A failed state solve stops the calculation rather than supplying a valid objective value.


$$
G(\lambda)=\lambda-\Pi_{[\ell,b]}(\lambda-g(\lambda)),\qquad |G(\lambda)|\le10^{-10}.
$$
The stopping measure is the absolute projected-gradient mapping with a unit step. It equals the ordinary gradient at an interior solution where projection is inactive; at an active bound a nonzero g can satisfy constrained stationarity. Save every accepted point, step length, backtrack count, primal/adjoint residual and termination reason, with at most 300 updates and 50 line-search trials. A small objective change alone is not the convergence test.

Armijo (1966) provides the sufficient-decrease and variable-step idea; this implementation applies it to the projected displacement. The original unconstrained convergence theorem is not cited as a global-convergence guarantee for this nonlinear inverse problem. This is also not an implementation of BFGS or a general constrained-optimization library.

Keep three synthetic data regimes distinct


$$
d^{\rm disc}=H_hu_h(\lambda_*),\qquad d^{\rm cont}_j=u_{\alpha_*}(x_j),\qquad d^{\rm noisy}=d^{\rm cont}+10^{-3}(1,-0.6,0.4,-1,0.3)^T.
$$
Noiseless data from the same discretization. Generate d with the n=31 forward solver and invert with that same discretization. Recovering λ* is an inverse crime: it checks consistency among data generation, observations, gradient and optimizer, not accuracy for the continuous problem or real measurements.

Noiseless data from the independent continuous family. Fix the closed-form u_α values at the observation points. Refine the inverse grid through n=15,31,63,127 to examine discretization bias in the difference from the generating parameter.

Data with a fixed perturbation. Add the displayed deterministic vector once to the same continuous observations. No random draw or known noise distribution is assumed, and no resampling occurs. The published perturbed-data fit uses n=63. A best fit displaced from λ* need not indicate optimizer failure.

Verification: gradients, optimization, grids and observations



The [saved measurements and input data](/numerical-methods-atlas/assets/bratu-inverse.json) record figure values, controls, residuals and termination reasons.


$$
g_{\rm FD}(\varepsilon)=\frac{\Phi_h(\lambda+\varepsilon)-\Phi_h(\lambda-\varepsilon)}{2\varepsilon},\qquad F_h(u_h(\lambda\pm\varepsilon),\lambda\pm\varepsilon)=0.
$$
Check gradients away from stationary points. Re-solve the state at λ±ε for several λ and compare objective-only central differences with adjoint gradients. Do not rely only on both gradients being nearly zero at an optimum.

Use an independent scalar reference. Compare the adjoint-gradient fit with objective-only golden-section search. Golden section assumes a unimodal objective; sampled objective landscapes are also saved. Agreement is not a proof of global optimality across all branches.

Use three starting values. Compare accepted updates, objective decrease, projected gradients and termination reasons from 0.5,1.5,3.2.

Vary the data generation and grid separately. Record same-discretization consistency, mesh error for continuous data and the shift in best fit under the fixed perturbation.

Saved measurements 1: gradient checks. At n=31 and λ=0.8,1.8,3.0, central differences with ε=10⁻⁵ differ from adjoint gradients by approximately 1.31×10⁻¹², 2.81×10⁻¹² and 1.79×10⁻¹². The maximum absolute direct-sensitivity/adjoint gradient difference is below 1.4×10⁻¹⁷. The JSON also saves a perturbation sweep. These check derivatives of the implemented discrete objective.


Measurements 2: same-discretization recovery. For n=31, starts λ=0.5,1.5,3.2 take 33,30,25 accepted updates. Absolute errors from λ* are approximately 1.48×10⁻⁹, 1.10×10⁻⁹ and 1.65×10⁻⁹. All three projected gradients are at most 10⁻¹⁰ and data RMS residuals below 3.9×10⁻¹⁰. Read this close agreement as a same-discretization consistency check.


Measurements 3: mesh dependence for continuous data. For n=15,31,63,127, fitted λ values are approximately 2.6816989071, 2.6839024768, 2.6844527616, 2.6845902950. Absolute errors from λ* are approximately 2.9372×10⁻³, 7.3366×10⁻⁴, 1.8338×10⁻⁴, 4.5842×10⁻⁵, decreasing by about four as h halves. Observed orders are 2.0013, 2.0003, 2.0001. The optimizer converges while finite-mesh bias remains.


Measurements 4: a fixed perturbation shifts the best fit. At n=63 the fitted λ≈2.6841620622 shifts by about −2.9070×10⁻⁴ from the unperturbed optimum on the same grid. Absolute error from λ* is about 4.7408×10⁻⁴, data RMS residual about 7.1942×10⁻⁴ and objective about 2.5878×10⁻⁷. The projected gradient is about 6.39×10⁻¹¹, so the departure from truth is not explained simply by unfinished optimization.


The four continuous-data fits and the fixed-perturbation fit agree with the objective-only golden-section reference to within 2.1×10⁻⁹ in λ. The reference’s final interval width is below about 8.65×10⁻⁹; it is not a certificate of an exact optimum. Primal residuals at the eight final fits above are at most 1.4×10⁻¹¹. Judge derivative agreement, optimizer stopping and closeness to the generating parameter separately.

Observations that can and cannot identify λ


$$
J s=e^u,\qquad \frac{d(H_hu_h)}{d\lambda}=H_hs,\qquad \|W^{1/2}H_hs\|_2>0\ \text{is a local sensitivity diagnostic}.
$$
A response of the interior observations to λ is a useful local sensitivity diagnostic in this scalar problem. A weak response can amplify small data changes into large parameter changes. Local sensitivity alone does not prove global uniqueness. Changing the branch, sensor positions or admissible interval changes the inverse problem.

For a counterexample, observe only x=0,1. Their fixed Dirichlet values vanish independently of λ, so H=0 and Hs=0. With γ=0, the objective is independent of λ and the data cannot identify it. Dedicated tests check this property, and the fitting function rejects this setting as uninformative. A regularization term could select a parameter but would not make the boundary observations informative.

The fixed-perturbation experiment supplies no statistical confidence intervals. Real observations, unknown model discrepancy, optimal sensor placement and identifiability of many parameters are outside the verified scope.

Separate parameter error from optimization error


$$
e_\lambda=|\widehat\lambda_h-\lambda_*|,\qquad r_{\rm data}=\sqrt{\frac15\sum_{j=1}^5(H_hu_h-d)_j^2},\qquad r_F=\|F_h(u_h,\lambda)\|_2,\quad r_p=\|J^Tp-q\|_2.
$$
Error from the generating λ*, observation residual, primal residual, adjoint residual and projected gradient are different quantities. A small projected gradient checks stationarity for the chosen grid, observations and constraints; it does not guarantee truth recovery or a zero observation residual. Conversely, continuous/discrete mismatch or fixed observation perturbations can move a well-converged optimum away from λ*.

Primal solves use an unscaled Euclidean residual tolerance of 10⁻¹⁰ and at most 40 updates. Adjoint systems use small dense matrices. Finite-difference gradient checks balance perturbation truncation, roundoff and inner-solve error. Mesh refinement, tighter optimizer stopping and improvement of a physical model address different errors.

This release is an educational scalar, box-constrained fit on a specified Bratu branch. It is not a general inverse-problem library, quasi-Newton implementation, transient adjoint, singular-point continuation method, model-selection procedure or validation of a physical model with experimental data.

Run the fixed release and inspect its inputs

Extract the [dated release ZIP](/code/bratu-inverse/2026-11-22/bratu-inverse-2026-11-22.zip) and follow the [README](/code/bratu-inverse/2026-11-22/README.md). The earlier AD and sensitivity supplements remain separate, fixed releases; this synthetic inverse example has its own package.

python -m pip install -r requirements.txt
python scripts/build_bratu_inverse.py
python -m pytest tests/test_bratu_inverse.py
Inspect the [objective, adjoint and optimizer source](/code/bratu-inverse/2026-11-22/numart/bratu_inverse.py), [figure and evidence builder](/code/bratu-inverse/2026-11-22/scripts/build_bratu_inverse.py), [dedicated tests](/code/bratu-inverse/2026-11-22/tests/test_bratu_inverse.py), [independent-extraction verification record](/code/bratu-inverse/2026-11-22/verification.json) and [file inventory and SHA-256 hashes](/code/bratu-inverse/2026-11-22/source-manifest.json). JSON inputs include positions, generating parameter, fixed perturbation, weights, starts and stopping controls.

Blondel et al. (2022), Section 2.1, and the official JAXopt documentation discuss root derivatives built from residual derivatives and linear solves; Jameson (1988) gives historical context for adjoints in design. This NumPy educational implementation does not claim to reproduce their paper experiments or JAXopt’s implementation or performance.

[Implicit differentiation and Bratu sensitivity](/numerical-methods-atlas/en/read/adjoint/) · [Automatic differentiation foundation](/numerical-methods-atlas/en/read/automatic-differentiation/) · [General gradient and quasi-Newton reading](/numerical-methods-atlas/en/read/optimization/)

## Publication scope

An educational box-constrained adjoint-gradient implementation estimates one Bratu coefficient λ from synthetic observations. Measured checks cover same-discretization consistency, mesh dependence for independent continuous-family data, fixed observation perturbations, gradient differences and an objective-only reference search. Scope is a specified smaller-solution branch, fixed observations and small dense matrices. It does not validate BFGS or optimization methods generally, all-branch uniqueness, real data, statistical uncertainty or unknown model discrepancy.

## Sources

- Larry Armijo (1966). Minimization of functions having Lipschitz continuous first partial derivatives. https://doi.org/10.2140/pjm.1966.16.1
- Antony Jameson (1988). Aerodynamic design via control theory. https://doi.org/10.1007/bf01061285
- Mathieu Blondel, Quentin Berthet, Marco Cuturi, Roy Frostig, Stephan Hoyer, Felipe Llinares-López, Fabian Pedregosa and Jean-Philippe Vert (2022). Efficient and Modular Implicit Differentiation. https://doi.org/10.52202/068431-0378
- The JAXopt authors (2026). Implicit differentiation; root_jvp and root_vjp. https://jaxopt.github.io/stable/implicit_diff.html
