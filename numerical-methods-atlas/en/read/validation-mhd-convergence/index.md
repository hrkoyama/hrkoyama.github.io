# CT and GLM: matched controls, independent checks and grid/time convergence

Compare CT and GLM discretizations with a matched flux family, LLF coefficient, time steps and fixed physical damping. Use a constructed smooth exact solution and independent Athena++ results to separate spatial, time-integration and reference differences.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium

Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence.

**Methods used**

- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) (`ct`)
- [GLM divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en) (`glm`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en#ct-glm-smooth-convergence-en-algorithm)

Both use piecewise constants, the same fixed Rusanov speed alpha3 and forward Euler. CT uses face B/shared arithmetic corner EMFs; GLM uses cell B/psi with fixed ch3 and physical damping rate kappa2. All meshes use384 steps and identical CT/GLM dt sequences; initial reconstructed CT cell B matches GLM cell B.

$$
A=a[\cos k(x-ut)+\cos k(y-vt)],\quad\mathbf B=(A_y,-A_x),\quad J_z=-\Delta A=k^2A
$$

$$
p=p_0+\tfrac12k^2A^2,\qquad\nabla p=J_z\nabla A=\mathbf J\times\mathbf B
$$

$$
\bar{\mathbf U}_{ij}=\frac1{\Delta x\Delta y}\int_{K_{ij}}\mathbf U\,dx\,dy,\qquad p(\bar{\mathbf U})\ne\bar p
$$

$$
\mathbf U^{m+1}=\mathbf U^m+\Delta t\,L_h(\mathbf U^m),\qquad C_{\rm sum}=\alpha\Delta t(\Delta x^{-1}+\Delta y^{-1})
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=en) (`advected-magnetostatic-equilibrium`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en#ct-glm-smooth-convergence-en-validation)

Measure conserved-variable L1/L2/Linf errors and observed orders at16²/32²/64². Compare finest-grid step doubling with.1 of the spatial error. At fixed8², compare16/32/64/128 steps with doubly refined DOP853 tolerances/max steps. Record mass/E, positivity, native CT divergence, common cell divergence and psi.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Periodic unit square, gamma5/3, mu0=1, planar MHD. A=.05[cos2pi(x−.3t)+cos2pi(y−.2t)], B=(Ay,−Ax), rho1, v=(.3,.2), p=.1+(2pi)²A²/2 at t=.1. Compare analytic conserved cell averages. This is a constructed verification case, not a claimed published standard benchmark.

**Editorial clarification**

This translating smooth equilibrium is an exact solution constructed for the Atlas. Compare conserved cell averages, distinguishing pressure recovered from them from the exact cell average of pressure. A separate time integrator on the same spatial semidiscretization checks time error; it is not an independent PDE solver.

### Adopted numerical method

Both use piecewise constants, the same fixed Rusanov speed alpha3 and forward Euler. CT uses face B/shared arithmetic corner EMFs; GLM uses cell B/psi with fixed ch3 and physical damping rate kappa2. All meshes use384 steps and identical CT/GLM dt sequences; initial reconstructed CT cell B matches GLM cell B.

$$
A=a[\cos k(x-ut)+\cos k(y-vt)],\quad\mathbf B=(A_y,-A_x),\quad J_z=-\Delta A=k^2A
$$

$$
p=p_0+\tfrac12k^2A^2,\qquad\nabla p=J_z\nabla A=\mathbf J\times\mathbf B
$$

$$
\bar{\mathbf U}_{ij}=\frac1{\Delta x\Delta y}\int_{K_{ij}}\mathbf U\,dx\,dy,\qquad p(\bar{\mathbf U})\ne\bar p
$$

$$
\mathbf U^{m+1}=\mathbf U^m+\Delta t\,L_h(\mathbf U^m),\qquad C_{\rm sum}=\alpha\Delta t(\Delta x^{-1}+\Delta y^{-1})
$$

### References and validation

Measure conserved-variable L1/L2/Linf errors and observed orders at16²/32²/64². Compare finest-grid step doubling with.1 of the spatial error. At fixed8², compare16/32/64/128 steps with doubly refined DOP853 tolerances/max steps. Record mass/E, positivity, native CT divergence, common cell divergence and psi.

### Limits

With constant LLF viscosity and periodic centered operators, the GLM div=psi=0 subspace remains invariant up to roundoff. This tests coupled-MHD accuracy; a separate nonphysical control activates cleaning. p(q-average) is not the exact averaged p. DOP853 is independent in time only and shares the spatial RHS. Step differences are empirical contamination indicators, not rigorous bounds; face/cell representation differences remain part of the comparison.

### Stored measurements and decisions

```json
{
  "metrics": {
    "initial_cell_state_linf_difference": 0.0,
    "ct_finest_spatial_error": 0.030434862760674048,
    "ct_minimum_spatial_order": 0.8792002695252499,
    "ct_time_contamination_ratio": 0.00042240836130500326,
    "ct_finest_temporal_scaled_l2": 0.00028691666346522787,
    "ct_minimum_temporal_order": 1.003588237880181,
    "ct_time_reference_to_primary_ratio": 1.0480281669324549e-12,
    "glm_finest_spatial_error": 0.053272941712543334,
    "glm_minimum_spatial_order": 0.8519970902037858,
    "glm_time_contamination_ratio": 0.0002497746629066176,
    "glm_finest_temporal_scaled_l2": 0.0006005455648426271,
    "glm_minimum_temporal_order": 1.004074134741654,
    "glm_time_reference_to_primary_ratio": 4.049255315353574e-13
  },
  "checks": {
    "identical_initial_cell_states": true,
    "ct_native_constraint_n16": true,
    "ct_native_constraint_n32": true,
    "ct_native_constraint_n64": true,
    "ct_spatial_order": true,
    "ct_continuum_error": true,
    "ct_common_divergence_bounded": true,
    "ct_time_contamination_bounded": true,
    "ct_positive_states": true,
    "ct_conservative_mass_energy": true,
    "glm_spatial_order": true,
    "glm_continuum_error": true,
    "glm_common_divergence_bounded": true,
    "glm_time_contamination_bounded": true,
    "glm_positive_states": true,
    "glm_conservative_mass_energy": true,
    "ct_temporal_order": true,
    "ct_temporal_error": true,
    "ct_temporal_reference_resolved": true,
    "glm_temporal_order": true,
    "glm_temporal_error": true,
    "glm_temporal_reference_resolved": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs-initial.json

### Sources and review scope

- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; selected original equations 17–19 and 24, pp.650–651
Checked selected original GLM B/psi and damping equations, conserved physical energy, and the distinction from extra EGLM source terms; not a full-paper audit.

- T. A. Gardiner and J. M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport. https://arxiv.org/abs/astro-ph/0501557; review_level=author preprint; selected section2.2/equations13–20
Checked the face-average/shared-corner-EMF structure. The present arithmetic flux-CT is not identified with the paper’s upwind CT/CTU algorithm.

- G. Tóth (2000). The ∇·B=0 Constraint in Shock-Capturing Magnetohydrodynamics Codes. https://doi.org/10.1006/jcph.2000.6519; review_level=author paper abstract and bibliographic metadata
Confirmed the original comparison topic and bibliographic identity; not a source of this experiment’s criteria or constructed equilibrium.

- SciPy developers (2024). scipy.integrate.solve_ivp: DOP853. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official versioned API and actual independent time-integrator execution
Execute DOP853 as a separate time integrator; shared spatial RHS means it is not an independent spatial discretization.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Orszag–Tang: matched CT/GLM and converged independent references

Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated.

**Methods used**

- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) (`ct`)
- [GLM divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en) (`glm`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en#ct-glm-ot-convergence-en-algorithm)

Primary runs use fixed alpha=ch=3 Rusanov/forward Euler and grid-independent GLM kappa2. Independent C++ Athena++ uses HLLD/PLM/RK2/upwind CT. Continuous initial fields agree; Athena’s face/primitive discretization is not identical.

$$
F_{i+1/2}=\tfrac12[F(U_L)+F(U_R)-\alpha(U_R-U_L)],\qquad\alpha=3
$$

$$
(B_x)_t+\partial_x\psi+\partial_y(v_yB_x-v_xB_y)=0,\quad\psi_t+c_h^2\nabla\cdot\mathbf B=-\kappa\psi
$$

$$
D_h^{\rm face}\,\operatorname{curl}_h E=0,\qquad D_h^{\rm cell}\ne D_h^{\rm face}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Orszag–Tang: matched CT/GLM and converged independent references: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-ot-convergence.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) (`orszag-tang`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en#ct-glm-ot-convergence-en-validation)

Measure density/magnetic L1 error, mesh improvement, positivity, conservation and div/psi. Athena256²/512² both useCFL.15; fixed512² CFL.3/.15 checks reference time sensitivity, with increments compared against.1 of primary error. At fixed16², compare primary time refinement with separately executed DOP853 and check finest-grid step doubling.

- [Late Orszag-Tang: independent finite-grid density/pressure reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-postshock-orszag-tang-en) (`postshock-orszag-tang`; Related-model reference · Finite-grid numerical reference)

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.
### Assumptions, units and boundaries

Standard periodic OT: gamma5/3, rho25/(36pi), p5/(12pi), v=(−sin2piy,sin2pix), B=(−sin2piy,sin4pix)/sqrt(4pi), t=.05. Both methods share192 steps on16²/32²/64². This supplements the previous immutable release.

**Editorial clarification**

Match the flux family, signal bound, time steps and physical damping, while retaining intrinsic differences in face versus cell magnetic fields and normal-field treatment. Compare the whole discretizations; do not attribute every difference solely to divergence control. Report native CT face divergence separately from a common cell-centered divergence.

### Adopted numerical method

Primary runs use fixed alpha=ch=3 Rusanov/forward Euler and grid-independent GLM kappa2. Independent C++ Athena++ uses HLLD/PLM/RK2/upwind CT. Continuous initial fields agree; Athena’s face/primitive discretization is not identical.

$$
F_{i+1/2}=\tfrac12[F(U_L)+F(U_R)-\alpha(U_R-U_L)],\qquad\alpha=3
$$

$$
(B_x)_t+\partial_x\psi+\partial_y(v_yB_x-v_xB_y)=0,\quad\psi_t+c_h^2\nabla\cdot\mathbf B=-\kappa\psi
$$

$$
D_h^{\rm face}\,\operatorname{curl}_h E=0,\qquad D_h^{\rm cell}\ne D_h^{\rm face}
$$

### References and validation

Measure density/magnetic L1 error, mesh improvement, positivity, conservation and div/psi. Athena256²/512² both useCFL.15; fixed512² CFL.3/.15 checks reference time sensitivity, with increments compared against.1 of primary error. At fixed16², compare primary time refinement with separately executed DOP853 and check finest-grid step doubling.

### Limits

Short smooth OT, not certification of post-shock,3D or general cleaning behavior. Athena is a finite-grid numerical reference; increments are not error bounds. Historical128²/CFL.3 is not paired with256²/CFL.15 to infer a pure spatial order. Constant-LLF preservation of GLM div=psi=0 is not evidence of active cleaning. Native face and common centered divergences differ; centered checkerboard blind spots remain.

### Stored measurements and decisions

```json
{
  "metrics": {
    "initial_cell_state_linf_difference": 0.0,
    "ct_finest_spatial_error": 0.04131948399815993,
    "ct_minimum_spatial_order": 0.7441584435125685,
    "ct_time_contamination_ratio": 0.005452472133120275,
    "ct_finest_temporal_scaled_l2": 0.0006451024853786959,
    "ct_minimum_temporal_order": 1.0051663785429696,
    "ct_time_reference_to_primary_ratio": 4.610829174194673e-13,
    "glm_finest_spatial_error": 0.06851242841151672,
    "glm_minimum_spatial_order": 0.6819406396313236,
    "glm_time_contamination_ratio": 0.003289333276474019,
    "glm_finest_temporal_scaled_l2": 0.0007617954701608142,
    "glm_minimum_temporal_order": 1.0056569861410107,
    "glm_time_reference_to_primary_ratio": 3.179752402329314e-13
  },
  "checks": {
    "identical_initial_cell_states": true,
    "independent_reference_density_refinement": true,
    "independent_reference_magnetic_refinement": true,
    "independent_reference_time_refinement": true,
    "ct_native_constraint_n16": true,
    "ct_native_constraint_n32": true,
    "ct_native_constraint_n64": true,
    "ct_spatial_refinement": true,
    "ct_density_error": true,
    "ct_magnetic_error": true,
    "ct_independent_reference_resolved": true,
    "ct_time_contamination_bounded": true,
    "ct_positive_states": true,
    "ct_conservative_mass_energy": true,
    "glm_spatial_refinement": true,
    "glm_density_error": true,
    "glm_magnetic_error": true,
    "glm_independent_reference_resolved": true,
    "glm_time_contamination_bounded": true,
    "glm_positive_states": true,
    "glm_conservative_mass_energy": true,
    "ct_temporal_order": true,
    "ct_temporal_error": true,
    "ct_temporal_reference_resolved": true,
    "glm_temporal_order": true,
    "glm_temporal_error": true,
    "glm_temporal_reference_resolved": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs-initial.json

### Sources and review scope

- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; selected original equations 17–19 and 24, pp.650–651
Checked selected original GLM B/psi and damping equations, conserved physical energy, and the distinction from extra EGLM source terms; not a full-paper audit.

- T. A. Gardiner and J. M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport. https://arxiv.org/abs/astro-ph/0501557; review_level=author preprint; selected section2.2/equations13–20
Checked the face-average/shared-corner-EMF structure. The present arithmetic flux-CT is not identified with the paper’s upwind CT/CTU algorithm.

- G. Tóth (2000). The ∇·B=0 Constraint in Shock-Capturing Magnetohydrodynamics Codes. https://doi.org/10.1006/jcph.2000.6519; review_level=author paper abstract and bibliographic metadata
Confirmed the original comparison topic and bibliographic identity; not a source of this experiment’s criteria or constructed equilibrium.

- J. M. Stone, K. Tomida, C. J. White and K. G. Felker (2020). The Athena++ Adaptive Mesh Refinement Framework: Design and Magnetohydrodynamic Solvers. https://doi.org/10.3847/1538-4365/ab929b; review_level=official source at pinned commit actually compiled/executed; paper metadata
Executed new reference runs with the previously independently built, hashed official C++ commit1395e2f543f4368d448cb1a2cf92ba1f910e3416 binary, retaining input/output/binary/source hashes; not a full-paper audit.

- SciPy developers (2024). scipy.integrate.solve_ivp: DOP853. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official versioned API and actual independent time-integrator execution
Execute DOP853 as a separate time integrator; shared spatial RHS means it is not an independent spatial discretization.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Initial-constraint preservation by CT and active GLM cleaning: nonphysical control

Intentionally begin with the same non-solenoidal cell B, checking that CT does not remove the initial defect and calibrating GLM’s B/psi response. This diagnostic adds no physical problem.

**Methods used**

- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) (`ct`)
- [GLM divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en) (`glm`)

**Equations**

[This example’s diagnostic and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=en#ct-glm-constraint-control-en-algorithm)

Use the same fully coupled MHD code. With y-invariance andBy=vy=0, the GLM Bx/psi subsystem decouples from fluid feedback, allowing a separately constructed2x2 discrete Fourier symbol and forward-Euler matrix power. Compare kappa2/0 at identical dt and LLF viscosity, separating B/psi phase exchange from physical damping.

$$
\widehat{U}^{m+1}=(I+\Delta t M_h)\widehat{U}^{m},\quad M_h=\begin{pmatrix}\nu_h&-i\widetilde{k}\\-ic_h^2\widetilde{k}&\nu_h-\kappa\end{pmatrix}
$$

$$
\nu_h=\alpha N[\cos(2\pi/N)-1],\quad\widetilde{k}=N\sin(2\pi/N)
$$

$$
W=\langle B_x^2+\psi^2/c_h^2\rangle,\qquad W_{\kappa=2}/W_{\kappa=0}<0.95
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Initial-constraint preservation by CT and active GLM cleaning: nonphysical control: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-constraint-control.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

No separate physical test problem is assigned to this check or diagnostic. Its own diagnostic figure and validation material are provided.

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=en#ct-glm-constraint-control-en-validation)

Check preservation of the initial CT defect, nonzero GLM psi, independent FE agreement for bothBx/psi, positive density/pressure, and conserved physical E/mass. Test the kappa2/0 ratio of auxiliary wave energy W=mean(Bx²+psi²/ch²), separating FE, semidiscrete-exponential and continuum-Fourier references.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Periodic32² grid,t=.1,128 steps,rho=p=1,v=0,By=psi=0. CT faceBx=.01cos[2pi(i+1)/32]; GLM cellBx equals the adjacent-face average. The intentional nonzero native CT divergence violates valid physical CT initial data and is treated solely as a diagnostic.

**Editorial clarification**

This diagnostic deliberately violates the divergence constraint while giving both methods the same initial cell magnetic field. It is separate from legitimate divergence-free CT initial data and checks CT preservation of an existing constraint error. Compare GLM with an undamped control using magnetic-plus-psi wave energy, distinguishing wave phase and numerical diffusion from physical damping.

### Adopted numerical method

Use the same fully coupled MHD code. With y-invariance andBy=vy=0, the GLM Bx/psi subsystem decouples from fluid feedback, allowing a separately constructed2x2 discrete Fourier symbol and forward-Euler matrix power. Compare kappa2/0 at identical dt and LLF viscosity, separating B/psi phase exchange from physical damping.

$$
\widehat{U}^{m+1}=(I+\Delta t M_h)\widehat{U}^{m},\quad M_h=\begin{pmatrix}\nu_h&-i\widetilde{k}\\-ic_h^2\widetilde{k}&\nu_h-\kappa\end{pmatrix}
$$

$$
\nu_h=\alpha N[\cos(2\pi/N)-1],\quad\widetilde{k}=N\sin(2\pi/N)
$$

$$
W=\langle B_x^2+\psi^2/c_h^2\rangle,\qquad W_{\kappa=2}/W_{\kappa=0}<0.95
$$

### References and validation

Check preservation of the initial CT defect, nonzero GLM psi, independent FE agreement for bothBx/psi, positive density/pressure, and conserved physical E/mass. Test the kappa2/0 ratio of auxiliary wave energy W=mean(Bx²+psi²/ch²), separating FE, semidiscrete-exponential and continuum-Fourier references.

### Limits

Passing means correctly detecting expected CT non-removal and the calibrated GLM response, not recommending non-solenoidal CT physical initial data. W is an auxiliary diagnostic norm, distinct from conserved physical total energy E without psi. B decay includes phase exchange and LLF diffusion; damping is assessed with the kappa0 control. No general nonlinear,boundary or shock cleaning guarantee is claimed.

### Stored measurements and decisions

```json
{
  "metrics": {
    "damped_to_undamped_B_psi_wave_energy_ratio": 0.797707175433604,
    "ct_native_divergence_linf_change": 0.0,
    "ct_common_divergence_linf_change": 1.457167719820518e-16,
    "initial_common_divergence_l2": 0.04393133573771591,
    "initial_cell_state_difference": 4.7704895589362195e-18
  },
  "checks": {
    "ct_preserves_initial_constraint_defect": true,
    "ct_does_not_clean_common_initial_defect": true,
    "ct_initial_constraint_is_deliberately_nonzero": true,
    "damped_independent_discrete_fourier_agreement": true,
    "damped_positive_states": true,
    "damped_conservative_mass_energy": true,
    "damped_psi_is_activated": true,
    "glm_final_B_divergence_reduced": true,
    "undamped_independent_discrete_fourier_agreement": true,
    "undamped_positive_states": true,
    "undamped_conservative_mass_energy": true,
    "undamped_psi_is_activated": true,
    "physical_damping_separated_from_phase_and_LLF_viscosity": true,
    "ct_positive_states": true,
    "ct_conservative_mass_energy": true,
    "matched_initial_cell_states": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs-initial.json

### Sources and review scope

- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; selected original equations 17–19 and 24, pp.650–651
Checked selected original GLM B/psi and damping equations, conserved physical energy, and the distinction from extra EGLM source terms; not a full-paper audit.

- T. A. Gardiner and J. M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport. https://arxiv.org/abs/astro-ph/0501557; review_level=author preprint; selected section2.2/equations13–20
Checked the face-average/shared-corner-EMF structure. The present arithmetic flux-CT is not identified with the paper’s upwind CT/CTU algorithm.

- G. Tóth (2000). The ∇·B=0 Constraint in Shock-Capturing Magnetohydrodynamics Codes. https://doi.org/10.1006/jcph.2000.6519; review_level=author paper abstract and bibliographic metadata
Confirmed the original comparison topic and bibliographic identity; not a source of this experiment’s criteria or constructed equilibrium.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
