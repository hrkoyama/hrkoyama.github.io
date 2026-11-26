# Variable Eddington factors and tensors: closing moments with angular transport

VEF obtains an Eddington closure from angular transport and iterates it with a separate moment system. It uses a scalar factor f in one dimension and a tensor D in multiple dimensions. VET denotes this tensor form, rather than an unrelated physical model.

## Distinguishing grey models, diffusion and M1

The grey approximation integrates over frequency. VEF/VET instead obtains the pressure closure from an angular distribution. Being grey does not select diffusion, M1 or VEF.

Use a static medium, constant total extinction sigma_t and isotropic scattering sigma_s, and a positive isotropic source q. With angular measure dOmega/(4pi) and c=1, E, H and K are normalized energy, flux and pressure moments. Restore the common 4pi factor for unnormalized angular integrals.

$$
\boldsymbol\Omega\cdot\nabla I+\sigma_tI=\sigma_sE+q,\quad E=\langle I\rangle,\quad\langle g\rangle=\frac{1}{4\pi}\int_{S^2}g\,d\Omega
$$

$$
\mathsf D=\frac{\langle\boldsymbol\Omega\boldsymbol\Omega^{\mathsf T}I\rangle}{E},\quad\mathsf K=\mathsf DE,\quad f= D_{xx}
$$

$$
\nabla\cdot\boldsymbol H+\sigma_aE=q,\quad\sigma_t\boldsymbol H+\nabla\cdot(\mathsf DE)=0,\quad\sigma_a=\sigma_t-\sigma_s
$$

## Iterating angular transport and moments

Form q+sigma_s E from the current moment solution, solve directional transport, and calculate D from the resulting intensities. Solve a separately discretized moment system and feed the new E back to transport. Merely plotting D is not this coupled iteration.

The formal solver here uses a periodic Fourier representation. The low-order system uses finite differences with shared face fluxes, retaining the cross derivatives from Dxy. This is not a reproduction of the papers' short-characteristics or high-order mixed finite-element implementations.

Check the inner linear residual separately from the outer E and D updates. Because the spatial discretizations differ, exact agreement between the transport and moment E at a fixed mesh is not a stopping condition.

$$
\sigma_t\sigma_aE-\sum_{i,j}\partial_i\partial_j(D_{ij}E)=\sigma_tq
$$

## 1D VEF: a periodic scattering field

Fix q=1+0.3cos(2pi x), sigma_t=4 and sigma_s=3 on a unit-period domain. Obtain f(x)=Kxx/E from I(x,mu), then compare the separate scalar moment solution with an analytic reference.

The heatmap's mu coordinate is an angular cosine, not a second spatial dimension. Keep the fixed f=1/3 control distinct, and store spatial and angular comparisons as separate rows.

[1D VEF: figure, fixed input, analytic reference and code](/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en)

## 2D VET: nonparallel source modes

Fix q=1+0.3cos(2pi x)+0.2sin(2pi(x+y)) on a periodic unit square. Two nonparallel modes produce nonzero Dxy and spatially changing principal axes.

Although space is two-dimensional, the angular measure is the sphere S2. Retain the full 3x3 tensor, including Dzz, and check symmetry, trace one, positivity and angular realizability. An M1 tensor formed from local E and H is only a diagnostic comparison; no time-evolving M1 solver is implemented in this example.

[2D VET: figure, fixed input, analytic reference and code](/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en)

## An independent analytic reference

Specify the positive isotropic source first and derive the reference from the continuum angular integral of each Fourier mode. This is not a manufactured solution obtained by choosing an intensity or closure and reverse-engineering the forcing. The primary solver does not use the analytic reference to construct D.

Align the polar axis with the wave vector and integrate 1/(sigma_t+i k mu) to obtain R(k)=atan(k/sigma_t)/k. A separate module evaluates E, H and K using the scattering-coupled amplitude A. Compare the complex phase of sine modes too, so a constant background cannot conceal mode errors.

$$
R(k)=\frac{\tan^{-1}(k/\sigma_t)}{k},\quad A_m=\frac{b_m}{1-\sigma_sR(|\boldsymbol k_m|)},\quad E_{\rm ref}=\frac{q_0}{\sigma_a}+\operatorname{Re}\sum_m A_mR(|\boldsymbol k_m|)e^{i\boldsymbol k_m\cdot\boldsymbol x}
$$

## Checked scope and limitations

The two fixed problems are limited to static grey transfer, linear isotropic scattering, constant coefficients and periodic boundaries. They do not validate inflow boundary factors, vacuum boundaries, absorber shadows, crossing beams, gas coupling, time evolution, multiple frequencies or relativistic transport.

Selected passages of the original papers support the equations, closure and iteration. These examples do not reproduce Athena or all paper experiments, establish universal convergence or speedups, or certify fixed-grid asymptotic preservation in the diffusion limit.

## How to check the results

Check positive intensity and E, tensor trace and eigenvalues, and face-flux balance first. Then inspect the linear residual and outer iteration, and compare fields, source-mode amplitudes and phases with the analytic reference.

Keep spatial and angular rows separate, retaining the mesh-dependent HO/LO gap. Constant solutions, cross-derivative signs, omitted scattering feedback and a fixed one-third closure provide controls, so a small residual alone does not pass. Consult the execution entries and release ZIP records below for measured values and decisions.

## Fixed-input examples and diagnostic controls

Distinguish the scope established by acceptance checks from a general mathematical guarantee; preserve historical inputs, measurements and criteria.

### Variable Eddington factor: a periodic 1D scattering-source control

Fixed-target computation

Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference.

Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.

[Input, results and acceptance](/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-variable-eddington-controls/#vef-fourier-scattering1d) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/run.py) · [Code primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py) · [Code analytic_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py) · [Tests test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py) · [ZIP](/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip) · [Results](/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)

### Variable Eddington tensor: a periodic 2D nonparallel-source control

Fixed-target computation

Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference.

Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.

[Input, results and acceptance](/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-variable-eddington-controls/#vet-fourier-source2d) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/run.py) · [Code primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py) · [Code analytic_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py) · [Tests test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py) · [ZIP](/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip) · [Results](/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)

## Publication scope

One group contains two lightweight fixed verification cases. VEF and VET are related scalar/tensor forms; mesh, angle and control rows do not add independent physical problems.

## Sources

- L. H. Auer and Dimitri Mihalas (1970). On the Use of Variable Eddington Factors in Non-LTE Stellar Atmospheres Computations. https://doi.org/10.1093/mnras/149.1.65
- Samuel Olivier and Terry S. Haut (2023). High-Order Mixed Finite Element Variable Eddington Factor Methods. https://arxiv.org/pdf/2301.04758
- Samuel Olivier and Will Pazner and Terry S. Haut and Ben C. Yee (2023). A Family of Independent Variable Eddington Factor Methods with Efficient Preconditioned Iterative Solvers. https://doi.org/10.1016/j.jcp.2022.111747
- Yan-Fei Jiang and James M. Stone and Shane W. Davis (2012). A Godunov Method for Multidimensional Radiation Magnetohydrodynamics based on a variable Eddington tensor. https://doi.org/10.1088/0067-0049/199/1/14
- Shane W. Davis and James M. Stone and Yan-Fei Jiang (2012). A Radiation Transfer Solver for Athena using Short Characteristics. https://arxiv.org/pdf/1201.2222
- M. Aaron Skinner and Eve C. Ostriker (2013). A Two-moment Radiation Hydrodynamics Module in Athena Using a Time-explicit Godunov Method. https://doi.org/10.1088/0067-0049/206/2/21
