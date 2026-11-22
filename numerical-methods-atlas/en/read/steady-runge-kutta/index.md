# Damping Runge–Kutta iterations for steady solutions

Interpret multistage pseudo-time iterations as smoothers for a steady residual. A Jameson–Schmidt–Turkel-family example connects stage coefficients, stability polynomials, nonlinear order, high-frequency damping and preconditioning.

## The target is R(U)=0, not a physical-time trajectory

For a discrete steady Euler/Navier–Stokes residual R, iterate an artificial ODE in pseudo time τ toward its root. Here R is the conservative residual divided by cell volume. The step is a pseudo-time step; the aim is an adequately converged residual and steady observables, not an accurate physical transient.

The following base-state recurrence forms every stage from the same U^(0), unlike chaining forward-Euler increments from the preceding stage. Compare coefficients only after matching residual sign, cell-volume scaling and any preconditioning action.

$$
\frac{dU}{d\tau}=-R(U),\quad U^{(0)}=U^n,\quad U^{(k)}=U^{(0)}-\alpha_k\Delta\tau R(U^{(k-1)}),\quad U^{n+1}=U^{(s)}.
$$

## A representative Jameson-family four-stage iteration

Consider these coefficients with the same autonomous residual reevaluated at every stage. For R(U)=AU, the stability polynomial equals classical RK4. The simplified recurrence is not a complete specification of the original fluxes, artificial dissipation and dissipation-update schedule.

Equality of linear stability polynomials does not establish nonlinear fourth-order physical-time accuracy. This base-state recurrence is generally second order for nonlinear autonomous ODEs: it fails the third-order condition bᵀ(c⊙c)=1/3. Distinguish its steady-solver purpose and nonlinear order conditions from classical RK4.

$$
(\alpha_1,\alpha_2,\alpha_3,\alpha_4)=(1/4,1/3,1/2,1),\qquad z=-\Delta\tau\lambda,\quad \mathcal R_4(z)=1+z+z^2/2+z^3/6+z^4/24.
$$

$$
b^Tc=\tfrac12,\qquad b^T(c\odot c)=\tfrac14\ne\tfrac13\quad\text{for the stated base-state four-stage recurrence}.
$$

## Stability and high-frequency damping are different

For linearized residual modes, the iteration multiplier is a stability polynomial. |ℛ|≤1 prevents growth, but |ℛ| near one barely damps error. A multigrid smoother seeks small maximum amplification μ on frequencies H not representable on the coarse grid.

For a purely decaying z=−2 mode, this four-stage polynomial gives ℛ=1/3, while near-zero low-frequency modes decay slowly. Pushing the step to a stability boundary does not maximize damping or minimize time to convergence. Advection and diffusion occupy different spectral regions.

$$
e^{n+1}=\mathcal R_s(-\Delta\tau A)e^n,\qquad\mu=\max_{\theta\in\mathcal H}\left|\mathcal R_s(-\Delta\tau\lambda_h(\theta))\right|.
$$

## Residual smoothing, preconditioning and multigrid

Residual smoothing is a separate spatial filtering operation, not the choice of RK stage coefficients. With dimensionless centered D₂ on a uniform periodic grid and ε≥0, the example below attenuates high-frequency residuals. An invertible filter retains the residual root but changes the iteration spectrum.

Low-Mach preconditioning changes acoustic/convective scales, local stepping changes per-cell iteration increments, and coarse correction treats errors poorly reduced by the smoother. Combined iterations still require boundary/variable-coefficient/nonnormality analysis and must be distinguished from physical-time integration.

$$
(I-\varepsilon D_2)\overline r=r,\qquad \widehat D_2(\theta)=-4\sin^2(\theta/2),\quad \widehat{\overline r}(\theta)=\frac{\widehat r(\theta)}{1+4\varepsilon\sin^2(\theta/2)}.
$$

## Measure residuals, steady observables and work

Measure Fourier-mode damping on a manufactured Poisson-type problem and compare with μ. For compressible flow track true residuals scaled by conservative component and steady quantities such as forces, mass flow and conservation balances. When smoothing residuals, also display the original unsmoothed residual.

Report residual evaluations and linear-solve work, final errors and termination reasons, not only stage/cycle counts. Compare methods at the same steady solution and tolerance. This chapter supplies algorithmic reading, not a dedicated Jameson solver or new flow-validation results.

## Publication scope

This is reading on steady multistage RK iteration. Existing classical RK4, dual-time and multigrid examples do not implement or validate a complete Jameson-type compressible solver. No dedicated solver or new measured results are added.

## Sources

- A. JAMESON and WOLFGANG SCHMIDT and ELI TURKEL (1981). Numerical solution of the Euler equations by finite volume methods using Runge Kutta time stepping schemes. https://doi.org/10.2514/6.1981-1259
- Jameson, Antony (1991). Time dependent calculations using multigrid, with applications to unsteady flows past airfoils and wings. https://doi.org/10.2514/6.1991-1596
- J. C. Butcher (1963). Coefficients for the study of Runge-Kutta integration processes. https://doi.org/10.1017/S1446788700027932
