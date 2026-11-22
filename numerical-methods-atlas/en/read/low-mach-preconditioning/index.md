# Preconditioning matrices, low Mach numbers, sonic points and entropy fixes

Separate acoustic/convective preconditioning from transonic numerical-viscosity corrections. Connect a concrete Γ, a linear eigenvalue model, Mach cutoffs and dual time stepping with explicit variable conventions.

## Matrix-solve and PDE preconditioning

Left preconditioning P⁻¹Ax=P⁻¹b assists an iterative linear solve. Low-Mach PDE preconditioning instead changes pseudo-time mass matrices or characteristic numerical dissipation. Papers may use P for both; identify the operator being modified first.

At low Mach number, |u_n±a| is large compared with convection |u_n|, affecting steady iteration and low-speed flux accuracy. This is a different limit from a transonic characteristic u_n±a=0.

## Place Γ on pseudo time

Distinguish conservative U from primitive q and pseudo time τ from physical time t. Steady problems omit the physical-time term. Unsteady dual-time iterations retain the physically discretized term, such as BDF2, throughout the inner solve. Γ is not the same matrix as U_q.

For nonsingular Γ and unchanged R, a converged steady pseudo-time solve still satisfies R=0. Preconditioning spatial dissipation additionally changes the discrete residual construction. Indiscriminately preconditioning physical time changes the unsteady solution, including acoustics.

$$
\Gamma(q)\frac{\partial q}{\partial\tau}+\frac{\partial U(q)}{\partial t}+R(U(q))=0,\qquad q=(p,u,v,w,T)^T.
$$

## A concrete Weiss–Smith-type matrix

For a calorically perfect ideal gas, use q=(p,u,v,w,T), total specific enthalpy H=c_pT+(u²+v²+w²)/2, constant c_p, ρ_T=(∂ρ/∂T)_p and physical sound speed a. Θ replaces the usual pressure-density derivative. This ideal-gas specialization is not a general real-fluid formula.

Setting U_ref=a gives Θ=ρ/p and recovers the physical Jacobian U_q in this ordering. Reducing U_ref toward a convective scale changes pseudo-acoustic scales. Γ, its inverse and a conservative-variable P are not numerically identical matrices.

$$
\Gamma=\begin{pmatrix}\Theta&0&0&0&\rho_T\\\Theta u&\rho&0&0&\rho_Tu\\\Theta v&0&\rho&0&\rho_Tv\\\Theta w&0&0&\rho&\rho_Tw\\\Theta H-1&\rho u&\rho v&\rho w&\rho_TH+\rho c_p\end{pmatrix},\qquad\Theta=\frac1{U_{\rm ref}^2}-\frac{\rho_T}{\rho c_p},\quad\rho_T=-\frac\rho T.
$$

## Stagnation singularities and a Mach cutoff

A representative bounded parameter is shown below. Positive M_cut prevents U_ref=0 at stagnation; the upper bound recovers the physical system at supersonic speed. This is an illustrative choice, not a universal prescription: viscous, unsteady and boundary-aware variants use other reference scales.

The cutoff avoids degeneracy of the preconditioner near zero velocity; it does not remove physical Mach-1 flow from the domain. Too large a cutoff weakens low-Mach benefits; too small a value can impair robustness or boundary behavior.

$$
M=\frac{\|\mathbf u\|}{a},\quad\beta=\min(1,\max(M,M_{\rm cut})),\quad U_{\rm ref}=\beta a,\quad 0<M_{\rm cut}\le1.
$$

## How characteristic eigenvalues change

To expose the effect, linearize about constant density/sound speed and use pressure perturbation divided by ρ₀a, normal/tangential velocities and an advected entropy variable with fixed scaling. The following P is an illustrative pressure-row scaling, not the nonlinear Γ above.

For nonzero β comparable with Mach number, pseudo-acoustic eigenvalues become convective in scale. However, a matrix 2-norm condition number is a singular-value ratio, not generally an absolute-eigenvalue ratio. Examine normality, variable scaling, boundaries and discretization as well.

$$
A=\begin{pmatrix}u_n&a&0&0\\a&u_n&0&0\\0&0&u_n&0\\0&0&0&u_n\end{pmatrix},\quad P=\operatorname{diag}(\beta^2,1,1,1),\quad q_\tau+PAq_x=0.
$$

$$
\lambda_{\pm}=\frac{(1+\beta^2)u_n\pm\sqrt{(1-\beta^2)^2u_n^2+4\beta^2a^2}}2,\quad\lambda_0=u_n\ (\text{twice}),\quad\lambda_+\lambda_-=\beta^2(u_n^2-a^2).
$$

$$
\kappa_2(A)=\sigma_{\max}(A)/\sigma_{\min}(A),\qquad\chi_\lambda(A)=\max_i|\lambda_i|/\min_{\lambda_i\ne0}|\lambda_i|.
$$

## Preconditioning does not remove a physical sonic zero

The model has zero acoustic eigenvalue product when u_n²=a². More generally, multiplication by an invertible P cannot remove singularity of A. Do not claim that a preconditioning matrix eliminates physical sonic points. Sonic singularities of particular attempts at isotropic acoustic preconditioning also require formulation-specific discussion.

$$
\det(PA)=\det(P)\det(A),\qquad P\text{ nonsingular}.
$$

## Transonic rarefaction and an entropy fix

A Roe linearization can produce an unphysical expansion shock when a characteristic crosses zero through a rarefaction. A representative smoothing replaces |λ| in the numerical dissipation as below. δ has speed units; state-aware choices and fixed fractional cutoffs are different variants.

This modifies numerical viscosity rather than deleting the physical characteristic. The published acoustic quadratic smoothing is not claimed as a faithful reproduction of every Harten–Hyman construction. Entropy correction, HLLE low-density robustness, carbuncle control and low-Mach preconditioning address different problems.

$$
\psi_\delta(\lambda)=\begin{cases}|\lambda|,&|\lambda|\ge\delta,\\(\lambda^2+\delta^2)/(2\delta),&|\lambda|<\delta,\end{cases}\qquad\delta>0.
$$

## Checks that keep the mechanisms separate

Test spectra, recovery at β→1, low-Mach scaling and near-stagnation invertibility on small linear problems. Measure pseudo-time convergence separately from solution error due to changed spatial fluxes. Interior eigenvalue analysis alone cannot assess boundary reflection.

Use transonic Burgers/Euler rarefactions to examine expansion shocks, refinement and δ sensitivity. For unsteady problems separate physical-time convergence from inner pseudo-residual convergence. Low-Mach checks here are proposed work; existing Jacobi scaling or dual-time examples do not validate a dedicated low-Mach flow solver.

## Publication scope

Low-Mach PDE preconditioning is reading-only, without dedicated code or numerical verification. Existing educational acoustic Roe smoothing does not implement Γ or the Weiss–Smith method. Dated verification records are unchanged, and proposed preconditioning checks are not presented as executed results.

## Sources

- Turkel, Eli (1987). Preconditioned methods for solving the incompressible and low speed compressible equations. https://doi.org/10.1016/0021-9991(87)90084-2
- Jonathan M. Weiss and Wayne A. Smith (1995). Preconditioning applied to variable and constant density flows. https://doi.org/10.2514/3.12946
- David L. Darmofal and Pierre Moinier and Michael B. Giles (2000). Eigenmode Analysis of Boundary Conditions for the One-Dimensional Preconditioned Euler Equations. https://doi.org/10.1006/jcph.2000.6472
- Ami Harten (1983). High resolution schemes for hyperbolic conservation laws. https://doi.org/10.1016/0021-9991(83)90136-5
- Roe, Philip L. (1981). Approximate Riemann solvers, parameter vectors, and difference schemes. https://doi.org/10.1016/0021-9991(81)90128-5
