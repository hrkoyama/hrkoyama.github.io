# Small quantum models and saved-reference cards

Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## A two-state BO / CP-type model with a short nuclear thermostat coupling

Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath.

**Methods used**

- [Born–Oppenheimer molecular dynamics / BOMD](https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=en) (`born-oppenheimer-md`)
- [Car–Parrinello molecular dynamics / CPMD](https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=en) (`car-parrinello-md`)
- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en) (`langevin-thermostat`)
- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en#two-state-bo-cp-ou-en-algorithm)

Use analytic BO forces and the declared CP-type action with Verlet/BAOAB; record nuclear heat and fictitious electronic kinetic energy separately.

$$
H(Q)=\frac{kQ^2}{2}I+\begin{pmatrix}-\Delta&gQ\\gQ&\Delta\end{pmatrix},\quad\psi=(\cos\theta,\sin\theta)^T
$$

$$
E(Q,\theta)=\frac{kQ^2}{2}-\Delta\cos(2\theta)+gQ\sin(2\theta),\quad E_-(Q)=\frac{kQ^2}{2}-\sqrt{\Delta^2+g^2Q^2}
$$

$$
M\ddot Q=-kQ-g\sin(2\theta),\quad\mu\ddot\theta=-2\Delta\sin(2\theta)-2gQ\cos(2\theta)
$$

$$
V^+=aV^-+\sqrt{(T/M)(1-a^2)}\,\xi,\quad a=e^{-\gamma h},\quad Q_{\rm bath}=\sum\Delta K_{\rm nuclear}
$$

- [Two-state electronic-angle/nuclear BO and CP-type model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#two-state-bo-cp-model-en) (`two-state-bo-cp-model`)

Actual coupled normalized electronic angle and nuclear coordinate, short NVE plus one nuclear OU trajectory. No first-principles/long NVE/canonical sampling/production CPMD. BO and mu.04 state comparisons use fixed4096/8192 RK4 companions; mu.01 receives energy checks only. Authored dimensionless model units with M=20 and angular fictitious mass mu=.04/.01; these are not cp.x emass units.


**Problem figure**

![A two-state BO / CP-type model with a short nuclear thermostat coupling: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en) (`two-state-bo-cp-model`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en#two-state-bo-cp-ou-en-validation)

Check energy gradients, fixed4096/8192 RK4 sensitivity, extended energy, OU heat bookkeeping and conditional temperature variance.

- [A two-state BO / CP-type model with a short nuclear thermostat coupling](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-two-state-bo-cp-ou-en) (`two-state-bo-cp-ou`; Same-problem reference · Semi-analytic reference)

Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.
### Assumptions, units and boundaries

Actual coupled normalized electronic angle and nuclear coordinate, short NVE plus one nuclear OU trajectory. No first-principles/long NVE/canonical sampling/production CPMD. BO and mu.04 state comparisons use fixed4096/8192 RK4 companions; mu.01 receives energy checks only. Authored dimensionless model units with M=20 and angular fictitious mass mu=.04/.01; these are not cp.x emass units.

**Editorial clarification**

Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.

### Adopted numerical method

Use analytic BO forces and the declared CP-type action with Verlet/BAOAB; record nuclear heat and fictitious electronic kinetic energy separately.

$$
H(Q)=\frac{kQ^2}{2}I+\begin{pmatrix}-\Delta&gQ\\gQ&\Delta\end{pmatrix},\quad\psi=(\cos\theta,\sin\theta)^T
$$

$$
E(Q,\theta)=\frac{kQ^2}{2}-\Delta\cos(2\theta)+gQ\sin(2\theta),\quad E_-(Q)=\frac{kQ^2}{2}-\sqrt{\Delta^2+g^2Q^2}
$$

$$
M\ddot Q=-kQ-g\sin(2\theta),\quad\mu\ddot\theta=-2\Delta\sin(2\theta)-2gQ\cos(2\theta)
$$

$$
V^+=aV^-+\sqrt{(T/M)(1-a^2)}\,\xi,\quad a=e^{-\gamma h},\quad Q_{\rm bath}=\sum\Delta K_{\rm nuclear}
$$

### References and validation

Check energy gradients, fixed4096/8192 RK4 sensitivity, extended energy, OU heat bookkeeping and conditional temperature variance.

### Limits

Long first-principles NVE and general electronic/nuclear thermostat equilibration remain deferred. No material prediction, multi-orbital CPMD or canonical/ergodic sampling certificate.

### Stored measurements and decisions

```json
{
  "metrics": {
    "95 bo-0 NVE extended energy drift": 4.54374582403716e-08,
    "95 bo-1 NVE extended energy drift": 1.135934568630148e-08,
    "95 bo-2 NVE extended energy drift": 2.8398352558411943e-09,
    "95 cp-mu004-0 NVE extended energy drift": 4.543430420778094e-08,
    "95 cp-mu004-1 NVE extended energy drift": 1.1358568974273453e-08,
    "95 cp-mu004-2 NVE extended energy drift": 2.839641743968002e-09,
    "95 cp-mu001 NVE extended energy drift": 2.8397284523862254e-09,
    "95 bo finest RK4 state comparison": 5.443721431889809e-09,
    "95 cp-mu004 finest RK4 state comparison": 9.898870595217574e-08,
    "95 bo fixed RK4 companion sensitivity": 2.5547594848822963e-15,
    "95 cp-mu004 fixed RK4 companion sensitivity": 1.2252872249276024e-15,
    "95 OU extended energy minus measured heat": 4.47292801061816e-09,
    "95 OU conditional temperature variance identity": 0.0,
    "95 normalized orbital": 2.220446049250313e-16
  },
  "checks": {
    "95 bo-0 NVE extended energy drift": true,
    "95 bo-1 NVE extended energy drift": true,
    "95 bo-2 NVE extended energy drift": true,
    "95 cp-mu004-0 NVE extended energy drift": true,
    "95 cp-mu004-1 NVE extended energy drift": true,
    "95 cp-mu004-2 NVE extended energy drift": true,
    "95 cp-mu001 NVE extended energy drift": true,
    "95 bo finest RK4 state comparison": true,
    "95 cp-mu004 finest RK4 state comparison": true,
    "95 bo fixed RK4 companion sensitivity": true,
    "95 cp-mu004 fixed RK4 companion sensitivity": true,
    "95 OU extended energy minus measured heat": true,
    "95 OU conditional temperature variance identity": true,
    "95 normalized orbital": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Unified Approach for Molecular Dynamics and Density-Functional Theory [accessed 2026-11-25]. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.2471; review_level=abstract-and-metadata
Publisher title/authors/date/DOI and abstract only. Full PDF/equations not read; this is not a reproduction of the silicon calculation.

- Quantum ESPRESSO cp.x input description [accessed 2026-11-25]. https://www.quantum-espresso.org/Doc/INPUT_CP.html; review_level=selected-official-documentation
Selected emass/orthogonalization and CP context. Its physical mass conventions are not silently assigned to the authored dimensionless angle mass.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Hydrogenic formulas and immutable finite-basis helium reference cards

Map existing H/He formulas and saved finite-basis references to units, normalization and model limits.

**Methods used**

- [Schrodinger eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en) (`schrodinger`)
- [Hartree–Fock](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en) (`hartree-fock`)
- [Kohn–Sham density functional theory / DFT](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en) (`kohn-sham-dft`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en#atomic-reference-cards-en-algorithm)

Audit existing formulas and three stored energy rows; distinguish radial from volume density and orbital from total energy.

$$
E_n=-\frac{Z^2}{2n^2},\quad H_lu=-\frac12u^{\prime\prime}+\left[\frac{l(l+1)}{2r^2}-\frac Zr\right]u
$$

$$
\Psi=u(r)Y_{lm}/r,\quad\int|u|^2\,dr=1,\quad p_{\rm He}(r)=2|u|^2,\quad n_{\rm He}(r)=\frac{p_{\rm He}(r)}{4\pi r^2}
$$

$$
\int p_{\rm He}(r)\,dr=\int n_{\rm He}(\mathbf r)\,d^3r=2,\quad E_x^{\rm HF}=-E_H/2\ \text{one-orbital restricted Hartree--Fock He only}
$$

- [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en) (`stationary-schrodinger`)

Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows.

- [Closed-shell Hartree–Fock equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en) (`hartree-fock-model`)

Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows.

- [Local Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en) (`kohn-sham-model`)

Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows.


**Problem figure**

![Hydrogenic formulas and immutable finite-basis helium reference cards: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/atomic-reference-cards.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Helium ground state: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en) (`helium-ground-state`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en#atomic-reference-cards-en-validation)

Each of three saved rows uses40 uncontracted functions. Check exact values and electron counts without rerunning SCF or independent references.

- [Hydrogenic formulas and immutable finite-basis helium reference cards](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-atomic-reference-cards-en) (`atomic-reference-cards`; Same-problem reference · Finite-grid numerical reference)

Curation and saved-value audit only: zero new SCF/independent-reference runs. No correlated-exact He, complete-basis limit or full orbital rerun claim.
### Assumptions, units and boundaries

Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows.

**Editorial clarification**

Curation and saved-value audit only: zero new SCF/independent-reference runs. No correlated-exact He, complete-basis limit or full orbital rerun claim.

### Adopted numerical method

Audit existing formulas and three stored energy rows; distinguish radial from volume density and orbital from total energy.

$$
E_n=-\frac{Z^2}{2n^2},\quad H_lu=-\frac12u^{\prime\prime}+\left[\frac{l(l+1)}{2r^2}-\frac Zr\right]u
$$

$$
\Psi=u(r)Y_{lm}/r,\quad\int|u|^2\,dr=1,\quad p_{\rm He}(r)=2|u|^2,\quad n_{\rm He}(r)=\frac{p_{\rm He}(r)}{4\pi r^2}
$$

$$
\int p_{\rm He}(r)\,dr=\int n_{\rm He}(\mathbf r)\,d^3r=2,\quad E_x^{\rm HF}=-E_H/2\ \text{one-orbital restricted Hartree--Fock He only}
$$

### References and validation

Each of three saved rows uses40 uncontracted functions. Check exact values and electron counts without rerunning SCF or independent references.

### Limits

No new SCF, external-reference regeneration, complete-basis or correlated-exact helium claim.

### Stored measurements and decisions

```json
{
  "metrics": {
    "96 selected saved row count": 0.0,
    "96 saved energy literal 0": 0.0,
    "96 basis functions 0": 0.0,
    "96 saved electron count 0": 1.7763568394002505e-15,
    "96 saved energy literal 1": 0.0,
    "96 basis functions 1": 0.0,
    "96 saved electron count 1": 3.1086244689504383e-15,
    "96 saved energy literal 2": 0.0,
    "96 basis functions 2": 0.0,
    "96 saved electron count 2": 3.1086244689504383e-15
  },
  "checks": {
    "96 selected saved row count": true,
    "96 saved energy literal 0": true,
    "96 basis functions 0": true,
    "96 saved electron count 0": true,
    "96 saved energy literal 1": true,
    "96 basis functions 1": true,
    "96 saved electron count 1": true,
    "96 saved energy literal 2": true,
    "96 basis functions 2": true,
    "96 saved electron count 2": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- NIST DLMF18.39 Applications in the Physical Sciences [accessed 2026-11-25]. https://dlmf.nist.gov/18.39; review_level=selected-official-documentation
Earlier same-session R3 selected E7–8,E13–15,E24–35; oscillator/Coulomb normalization and measure. Full chapter/books not audited.

- PySCF Self-consistent field methods [accessed 2026-11-25]. https://pyscf.org/user/scf.html; review_level=selected-official-documentation
FC=SCe, mean-field orbital/determinant ansatz, stability vs stationarity, RHF/UHF spin symmetry and overlap orthogonalization selected passages. No PySCF execution.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Small 1D box and quantum harmonic-oscillator eigenpairs

Compare low stationary eigenpairs of a1D box and harmonic oscillator, with finite-domain and mesh sensitivity.

**Methods used**

- [Schrodinger eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en) (`schrodinger`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=en#quantum-box-ho-en-algorithm)

Use centered differences and eight full NumPy eigensolves, saving824 native pairs before selecting24 low pairs.

$$
H_h=-\frac12D_{xx}+V,\quad V_{\rm box}=0,\quad V_{\rm HO}=x^2/2
$$

$$
E_j^{\rm box}=\frac{(j\pi)^2}{2},\quad u_j=\sqrt2\sin(j\pi x),\quad\lambda_{h,j}=2h^{-2}\sin^2\left(\frac{j\pi}{2M}\right),\ h=1/M
$$

$$
E_n^{\rm HO}=n+\frac12,\quad u_n(x)=\frac{H_n(x)e^{-x^2/2}}{\pi^{1/4}\sqrt{2^nn!}},\quad u_h=v_h/\sqrt h
$$

- [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en) (`stationary-schrodinger`)

Finite Dirichlet boxes and central differences; whole-line HO formulas do not isolate finite-wall error. Node counts diagnostic until forward sign qualification. Atomic model units hbar=m=1 and HO omega=1. The box[0,1] and finite HO[-L,L] domains both use homogeneous Dirichlet conditions.


**Problem figure**

![Small 1D box and quantum harmonic-oscillator eigenpairs: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/quantum-box-ho.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Small 1D box and quantum harmonic-oscillator eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=en) (`quantum-box-ho`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=en#quantum-box-ho-en-validation)

Compare a stable Decimal box spectrum, continuum profiles, native normalization, orthogonality, residuals and reflection parity; report nodes and tail signs separately.

- [Small 1D box and quantum harmonic-oscillator eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-quantum-box-ho-en) (`quantum-box-ho`; Same-problem reference · Analytic reference)

Eight full solves save824raw pairs; qualification applies to24selected pairs. Thresholded nodes/phase are diagnostics. HO0.003 is a met fixed-case goal, not a proved bound; finite-wall/mesh sensitivities do not certify separate errors.
### Assumptions, units and boundaries

Finite Dirichlet boxes and central differences; whole-line HO formulas do not isolate finite-wall error. Node counts diagnostic until forward sign qualification. Atomic model units hbar=m=1 and HO omega=1. The box[0,1] and finite HO[-L,L] domains both use homogeneous Dirichlet conditions.

**Editorial clarification**

Eight full solves save824raw pairs; qualification applies to24selected pairs. Thresholded nodes/phase are diagnostics. HO0.003 is a met fixed-case goal, not a proved bound; finite-wall/mesh sensitivities do not certify separate errors.

### Adopted numerical method

Use centered differences and eight full NumPy eigensolves, saving824 native pairs before selecting24 low pairs.

$$
H_h=-\frac12D_{xx}+V,\quad V_{\rm box}=0,\quad V_{\rm HO}=x^2/2
$$

$$
E_j^{\rm box}=\frac{(j\pi)^2}{2},\quad u_j=\sqrt2\sin(j\pi x),\quad\lambda_{h,j}=2h^{-2}\sin^2\left(\frac{j\pi}{2M}\right),\ h=1/M
$$

$$
E_n^{\rm HO}=n+\frac12,\quad u_n(x)=\frac{H_n(x)e^{-x^2/2}}{\pi^{1/4}\sqrt{2^nn!}},\quad u_h=v_h/\sqrt h
$$

### References and validation

Compare a stable Decimal box spectrum, continuum profiles, native normalization, orthogonality, residuals and reflection parity; report nodes and tail signs separately.

### Limits

No separate certified finite-wall/mesh decomposition for HO; raw nodal count is a diagnostic. HO0.003 is the fixed-input study target, not a proved finite-h bound.

### Stored measurements and decisions

```json
{
  "metrics": {
    "97 box-M32 native_norm_error": 9.992007221626409e-16,
    "97 box-M32 physical_norm_error": 9.992007221626409e-16,
    "97 box-M32 orthogonality_error": 9.992007221626409e-16,
    "97 box-M32 state1 residual": 2.6534314217337773e-16,
    "97 box-M32 state1 same-grid oracle": 2.521780905296546e-15,
    "97 box-M32 state2 residual": 2.6489743749213535e-16,
    "97 box-M32 state2 same-grid oracle": 1.6250574155051521e-15,
    "97 box-M32 state3 residual": 2.3939284948881844e-16,
    "97 box-M32 state3 same-grid oracle": 2.2560444050504554e-15,
    "97 box-M64 native_norm_error": 4.440892098500626e-16,
    "97 box-M64 physical_norm_error": 4.440892098500626e-16,
    "97 box-M64 orthogonality_error": 5.729429494880433e-16,
    "97 box-M64 state1 residual": 3.628867495606101e-16,
    "97 box-M64 state1 same-grid oracle": 1.5283589494924628e-13,
    "97 box-M64 state2 residual": 3.5175380832319105e-16,
    "97 box-M64 state2 same-grid oracle": 2.5578063468007826e-14,
    "97 box-M64 state3 residual": 3.511156850072398e-16,
    "97 box-M64 state3 same-grid oracle": 9.295888967353658e-15,
    "97 box-M128 native_norm_error": 1.3322676295501878e-15,
    "97 box-M128 physical_norm_error": 8.881784197001252e-16,
    "97 box-M128 orthogonality_error": 1.1102230246251565e-15,
    "97 box-M128 state1 residual": 3.7340644105619856e-16,
    "97 box-M128 state1 same-grid oracle": 7.066470719683718e-13,
    "97 box-M128 state2 residual": 3.901829244394146e-16,
    "97 box-M128 state2 same-grid oracle": 1.6885756120423205e-13,
    "97 box-M128 state3 residual": 4.0863269302611023e-16,
    "97 box-M128 state3 same-grid oracle": 7.042499776870415e-14,
    "97 HO-L8-h0.25 native_norm_error": 1.1102230246251565e-15,
    "97 HO-L8-h0.25 physical_norm_error": 1.1102230246251565e-15,
    "97 HO-L8-h0.25 orthogonality_error": 1.1102230246251565e-15,
    "97 HO-L8-h0.25 state0 residual": 1.384362487647675e-16,
    "97 HO-L8-h0.25 state0 reflection parity": 9.906146009304781e-16,
    "97 HO-L8-h0.25 state1 residual": 1.549514541364104e-16,
    "97 HO-L8-h0.25 state1 reflection parity": 2.169025096981292e-15,
    "97 HO-L8-h0.25 state2 residual": 1.26030926507246e-16,
    "97 HO-L8-h0.25 state2 reflection parity": 5.378632453105551e-15,
    "97 HO-L8-h0.125 native_norm_error": 1.1102230246251565e-15,
    "97 HO-L8-h0.125 physical_norm_error": 8.881784197001252e-16,
    "97 HO-L8-h0.125 orthogonality_error": 8.881784197001252e-16,
    "97 HO-L8-h0.125 state0 residual": 3.9740329134654874e-16,
    "97 HO-L8-h0.125 state0 reflection parity": 1.489799852793317e-14,
    "97 HO-L8-h0.125 state1 residual": 4.0343427613151107e-16,
    "97 HO-L8-h0.125 state1 reflection parity": 3.32819383816502e-14,
    "97 HO-L8-h0.125 state2 residual": 3.816857166136067e-16,
    "97 HO-L8-h0.125 state2 reflection parity": 3.1052104675910025e-14,
    "97 HO-L8-h0.0625 native_norm_error": 1.1102230246251565e-15,
    "97 HO-L8-h0.0625 physical_norm_error": 1.1102230246251565e-15,
    "97 HO-L8-h0.0625 orthogonality_error": 1.3322676295501878e-15,
    "97 HO-L8-h0.0625 state0 residual": 5.118810100977104e-16,
    "97 HO-L8-h0.0625 state0 reflection parity": 1.0562240570035153e-14,
    "97 HO-L8-h0.0625 state1 residual": 5.6425322872051155e-16,
    "97 HO-L8-h0.0625 state1 reflection parity": 3.3151730411536006e-14,
    "97 HO-L8-h0.0625 state2 residual": 4.424438066999679e-16,
    "97 HO-L8-h0.0625 state2 reflection parity": 3.9175195970046425e-14,
    "97 HO-L4-h0.125 native_norm_error": 8.881784197001252e-16,
    "97 HO-L4-h0.125 physical_norm_error": 6.661338147750939e-16,
    "97 HO-L4-h0.125 orthogonality_error": 6.661338147750939e-16,
    "97 HO-L4-h0.125 state0 residual": 2.8638408377792463e-16,
    "97 HO-L4-h0.125 state0 reflection parity": 5.622962058212243e-15,
    "97 HO-L4-h0.125 state1 residual": 2.7780454534440377e-16,
    "97 HO-L4-h0.125 state1 reflection parity": 1.3088888066254994e-14,
    "97 HO-L4-h0.125 state2 residual": 3.13657233698048e-16,
    "97 HO-L4-h0.125 state2 reflection parity": 1.5345752054778173e-14,
    "97 HO-L6-h0.125 native_norm_error": 6.661338147750939e-16,
    "97 HO-L6-h0.125 physical_norm_error": 4.440892098500626e-16,
    "97 HO-L6-h0.125 orthogonality_error": 1.0478097465287758e-15,
    "97 HO-L6-h0.125 state0 residual": 2.3361979300913016e-16,
    "97 HO-L6-h0.125 state0 reflection parity": 1.654208719984383e-15,
    "97 HO-L6-h0.125 state1 residual": 3.0895334790910436e-16,
    "97 HO-L6-h0.125 state1 reflection parity": 3.966086461776309e-15,
    "97 HO-L6-h0.125 state2 residual": 3.0577186768266187e-16,
    "97 HO-L6-h0.125 state2 reflection parity": 9.059939709541788e-15,
    "97 box finest relative continuum 0": 5.019839662078447e-05,
    "97 box reduction lower (0, 0)": 3.99903629835137,
    "97 box reduction upper (0, 0)": 3.99903629835137,
    "97 box reduction lower (0, 1)": 3.9997589977320964,
    "97 box reduction upper (0, 1)": 3.9997589977320964,
    "97 box finest relative continuum 1": 0.0002007814885717256,
    "97 box reduction lower (1, 0)": 3.996146764158027,
    "97 box reduction upper (1, 0)": 3.996146764158027,
    "97 box reduction lower (1, 1)": 3.999036298147065,
    "97 box reduction upper (1, 1)": 3.999036298147065,
    "97 box finest relative continuum 2": 0.00045171299567713406,
    "97 box reduction lower (2, 0)": 3.9913360615376745,
    "97 box reduction upper (2, 0)": 3.9913360615376745,
    "97 box reduction lower (2, 1)": 3.9978320428851237,
    "97 box reduction upper (2, 1)": 3.9978320428851237,
    "97 HO finest total error 0": 0.0001221001366430441,
    "97 HO finest total error 1": 0.0006106201113647014,
    "97 HO finest total error 2": 0.0015879589598619681
  },
  "checks": {
    "97 box-M32 native_norm_error": true,
    "97 box-M32 physical_norm_error": true,
    "97 box-M32 orthogonality_error": true,
    "97 box-M32 state1 residual": true,
    "97 box-M32 state1 same-grid oracle": true,
    "97 box-M32 state2 residual": true,
    "97 box-M32 state2 same-grid oracle": true,
    "97 box-M32 state3 residual": true,
    "97 box-M32 state3 same-grid oracle": true,
    "97 box-M64 native_norm_error": true,
    "97 box-M64 physical_norm_error": true,
    "97 box-M64 orthogonality_error": true,
    "97 box-M64 state1 residual": true,
    "97 box-M64 state1 same-grid oracle": true,
    "97 box-M64 state2 residual": true,
    "97 box-M64 state2 same-grid oracle": true,
    "97 box-M64 state3 residual": true,
    "97 box-M64 state3 same-grid oracle": true,
    "97 box-M128 native_norm_error": true,
    "97 box-M128 physical_norm_error": true,
    "97 box-M128 orthogonality_error": true,
    "97 box-M128 state1 residual": true,
    "97 box-M128 state1 same-grid oracle": true,
    "97 box-M128 state2 residual": true,
    "97 box-M128 state2 same-grid oracle": true,
    "97 box-M128 state3 residual": true,
    "97 box-M128 state3 same-grid oracle": true,
    "97 HO-L8-h0.25 native_norm_error": true,
    "97 HO-L8-h0.25 physical_norm_error": true,
    "97 HO-L8-h0.25 orthogonality_error": true,
    "97 HO-L8-h0.25 state0 residual": true,
    "97 HO-L8-h0.25 state0 reflection parity": true,
    "97 HO-L8-h0.25 state1 residual": true,
    "97 HO-L8-h0.25 state1 reflection parity": true,
    "97 HO-L8-h0.25 state2 residual": true,
    "97 HO-L8-h0.25 state2 reflection parity": true,
    "97 HO-L8-h0.125 native_norm_error": true,
    "97 HO-L8-h0.125 physical_norm_error": true,
    "97 HO-L8-h0.125 orthogonality_error": true,
    "97 HO-L8-h0.125 state0 residual": true,
    "97 HO-L8-h0.125 state0 reflection parity": true,
    "97 HO-L8-h0.125 state1 residual": true,
    "97 HO-L8-h0.125 state1 reflection parity": true,
    "97 HO-L8-h0.125 state2 residual": true,
    "97 HO-L8-h0.125 state2 reflection parity": true,
    "97 HO-L8-h0.0625 native_norm_error": true,
    "97 HO-L8-h0.0625 physical_norm_error": true,
    "97 HO-L8-h0.0625 orthogonality_error": true,
    "97 HO-L8-h0.0625 state0 residual": true,
    "97 HO-L8-h0.0625 state0 reflection parity": true,
    "97 HO-L8-h0.0625 state1 residual": true,
    "97 HO-L8-h0.0625 state1 reflection parity": true,
    "97 HO-L8-h0.0625 state2 residual": true,
    "97 HO-L8-h0.0625 state2 reflection parity": true,
    "97 HO-L4-h0.125 native_norm_error": true,
    "97 HO-L4-h0.125 physical_norm_error": true,
    "97 HO-L4-h0.125 orthogonality_error": true,
    "97 HO-L4-h0.125 state0 residual": true,
    "97 HO-L4-h0.125 state0 reflection parity": true,
    "97 HO-L4-h0.125 state1 residual": true,
    "97 HO-L4-h0.125 state1 reflection parity": true,
    "97 HO-L4-h0.125 state2 residual": true,
    "97 HO-L4-h0.125 state2 reflection parity": true,
    "97 HO-L6-h0.125 native_norm_error": true,
    "97 HO-L6-h0.125 physical_norm_error": true,
    "97 HO-L6-h0.125 orthogonality_error": true,
    "97 HO-L6-h0.125 state0 residual": true,
    "97 HO-L6-h0.125 state0 reflection parity": true,
    "97 HO-L6-h0.125 state1 residual": true,
    "97 HO-L6-h0.125 state1 reflection parity": true,
    "97 HO-L6-h0.125 state2 residual": true,
    "97 HO-L6-h0.125 state2 reflection parity": true,
    "97 box finest relative continuum 0": true,
    "97 box reduction lower (0, 0)": true,
    "97 box reduction upper (0, 0)": true,
    "97 box reduction lower (0, 1)": true,
    "97 box reduction upper (0, 1)": true,
    "97 box finest relative continuum 1": true,
    "97 box reduction lower (1, 0)": true,
    "97 box reduction upper (1, 0)": true,
    "97 box reduction lower (1, 1)": true,
    "97 box reduction upper (1, 1)": true,
    "97 box finest relative continuum 2": true,
    "97 box reduction lower (2, 0)": true,
    "97 box reduction upper (2, 0)": true,
    "97 box reduction lower (2, 1)": true,
    "97 box reduction upper (2, 1)": true,
    "97 HO finest total error 0": true,
    "97 HO finest total error 1": true,
    "97 HO finest total error 2": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- NIST DLMF18.39 Applications in the Physical Sciences [accessed 2026-11-25]. https://dlmf.nist.gov/18.39; review_level=selected-official-documentation
Earlier same-session R3 selected E7–8,E13–15,E24–35; oscillator/Coulomb normalization and measure. Full chapter/books not audited.

- NumPy2.0 numpy.linalg.eigh [accessed 2026-11-25]. https://numpy.org/doc/2.0/reference/generated/numpy.linalg.eigh.html; review_level=selected-official-documentation
Signature, Hermitian lower-triangle handling, all ascending eigenvalues/normalized columns, LinAlgError and LAPACK syevd/heevd notes.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI

Compare RHF, broken-spin UHF and finite-basis FCI for H2 at two fixed geometries in the same minimal basis.

**Methods used**

- [Hartree–Fock](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en) (`hartree-fock`)
- [Configuration interaction / CI](https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=en) (`configuration-interaction`)
- [Self-consistent field iteration / SCF](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en) (`scf`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en#h2-rhf-uhf-fci-en-algorithm)

Run fixed SCF and diagonalize the4x4 two-electron Hamiltonian using the unchanged explicit H STO-3G contraction.

$$
F^\sigma=h+J[P^\alpha+P^\beta]-K[P^\sigma],\quad F^\sigma C^\sigma=SC^\sigma\varepsilon^\sigma
$$

$$
\langle S^2\rangle_{1\alpha,1\beta}=1-|c_\alpha^\dagger S c_\beta|^2
$$

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs),\quad E_{\rm tot}=E_{\rm el}+E_{NN}
$$

- [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en) (`stationary-schrodinger`)

Explicit unchanged STO-3G s contraction, R1.4/3.0bohr, finite-basis FCI and broken-spin UHF; not exact continuum chemistry. Distances1.4/3.0bohr and total energies in hartree. Two electrons in2AOs, each an explicitly supplied three-primitive contracted Hs function.

- [Closed-shell Hartree–Fock equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en) (`hartree-fock-model`)

Explicit unchanged STO-3G s contraction, R1.4/3.0bohr, finite-basis FCI and broken-spin UHF; not exact continuum chemistry. Distances1.4/3.0bohr and total energies in hartree. Two electrons in2AOs, each an explicitly supplied three-primitive contracted Hs function.

- [Unrestricted HF in a minimal two-electron model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#unrestricted-hartree-fock-model-en) (`unrestricted-hartree-fock-model`)

Explicit unchanged STO-3G s contraction, R1.4/3.0bohr, finite-basis FCI and broken-spin UHF; not exact continuum chemistry. Distances1.4/3.0bohr and total energies in hartree. Two electrons in2AOs, each an explicitly supplied three-primitive contracted Hs function.


**Problem figure**

![Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h2-rhf-uhf-fci.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en) (`h2-rhf`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en#h2-rhf-uhf-fci-en-validation)

Check two saved PySCF RHF energies, an analytic paired g/u variational polynomial, the even2x2 FCI block and independent fermion assembly.

- [Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-h2-rhf-uhf-fci-en) (`h2-rhf-uhf-fci`; Same-problem reference · Semi-analytic reference)

Only2fixed distances. Finite-basis FCI is not continuum exactness, and UHF stationarity is not a general global-minimum guarantee. Angular/complete-basis convergence and a broad dissociation curve remain untested.
### Assumptions, units and boundaries

Explicit unchanged STO-3G s contraction, R1.4/3.0bohr, finite-basis FCI and broken-spin UHF; not exact continuum chemistry. Distances1.4/3.0bohr and total energies in hartree. Two electrons in2AOs, each an explicitly supplied three-primitive contracted Hs function.

**Editorial clarification**

Only2fixed distances. Finite-basis FCI is not continuum exactness, and UHF stationarity is not a general global-minimum guarantee. Angular/complete-basis convergence and a broad dissociation curve remain untested.

### Adopted numerical method

Run fixed SCF and diagonalize the4x4 two-electron Hamiltonian using the unchanged explicit H STO-3G contraction.

$$
F^\sigma=h+J[P^\alpha+P^\beta]-K[P^\sigma],\quad F^\sigma C^\sigma=SC^\sigma\varepsilon^\sigma
$$

$$
\langle S^2\rangle_{1\alpha,1\beta}=1-|c_\alpha^\dagger S c_\beta|^2
$$

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs),\quad E_{\rm tot}=E_{\rm el}+E_{NN}
$$

### References and validation

Check two saved PySCF RHF energies, an analytic paired g/u variational polynomial, the even2x2 FCI block and independent fermion assembly.

### Limits

Only two H2 geometries and two contracted s orbitals; no complete-basis dissociation curve. UHF is spin contaminated; FCI exactness is finite-basis only.

### Stored measurements and decisions

```json
{
  "metrics": {
    "98 R1.4 saved PySCF RHF": 1.7319479184152442e-14,
    "98 R1.4 UHF analytic paired ansatz": 1.3322676295501878e-15,
    "98 R1.4 finite-basis FCI analytic": 4.440892098500626e-16,
    "98 R1.4 independent fermion assembly": 1.1102230246251565e-16,
    "98 R1.4 FCI residual": 1.510066572755813e-15,
    "98 R1.4 UHF <= RHF": 0.0,
    "98 R1.4 FCI <= UHF": -0.02056161860694994,
    "98 R1.4 RHF electron count": 1.3322676295501878e-15,
    "98 R1.4 RHF orbital norm": 9.992007221626409e-16,
    "98 R1.4 RHF SCF residual": 4.739336526991705e-16,
    "98 R1.4 UHF electron count": 1.3322676295501878e-15,
    "98 R1.4 UHF orbital norm": 9.992007221626409e-16,
    "98 R1.4 UHF SCF residual": 3.031599154361081e-11,
    "98 R3.0 saved PySCF RHF": 8.659739592076221e-15,
    "98 R3.0 UHF analytic paired ansatz": 0.0,
    "98 R3.0 finite-basis FCI analytic": 6.661338147750939e-16,
    "98 R3.0 independent fermion assembly": 1.1102230246251565e-16,
    "98 R3.0 FCI residual": 6.798699777552591e-16,
    "98 R3.0 UHF <= RHF": -0.06574294870227004,
    "98 R3.0 FCI <= UHF": -0.03413887592482623,
    "98 R3.0 RHF electron count": 8.881784197001252e-16,
    "98 R3.0 RHF orbital norm": 6.661338147750939e-16,
    "98 R3.0 RHF SCF residual": 1.0881821476711805e-16,
    "98 R3.0 UHF electron count": 4.440892098500626e-16,
    "98 R3.0 UHF orbital norm": 7.771561172376096e-16,
    "98 R3.0 UHF SCF residual": 1.610351596292876e-11,
    "98 stretched UHF energy lowering": 0.06574294870227004,
    "98 stretched UHF spin contamination": 0.7742403321308335
  },
  "checks": {
    "98 R1.4 saved PySCF RHF": true,
    "98 R1.4 UHF analytic paired ansatz": true,
    "98 R1.4 finite-basis FCI analytic": true,
    "98 R1.4 independent fermion assembly": true,
    "98 R1.4 FCI residual": true,
    "98 R1.4 UHF <= RHF": true,
    "98 R1.4 FCI <= UHF": true,
    "98 R1.4 RHF electron count": true,
    "98 R1.4 RHF orbital norm": true,
    "98 R1.4 RHF SCF residual": true,
    "98 R1.4 UHF electron count": true,
    "98 R1.4 UHF orbital norm": true,
    "98 R1.4 UHF SCF residual": true,
    "98 R3.0 saved PySCF RHF": true,
    "98 R3.0 UHF analytic paired ansatz": true,
    "98 R3.0 finite-basis FCI analytic": true,
    "98 R3.0 independent fermion assembly": true,
    "98 R3.0 FCI residual": true,
    "98 R3.0 UHF <= RHF": true,
    "98 R3.0 FCI <= UHF": true,
    "98 R3.0 RHF electron count": true,
    "98 R3.0 RHF orbital norm": true,
    "98 R3.0 RHF SCF residual": true,
    "98 R3.0 UHF electron count": true,
    "98 R3.0 UHF orbital norm": true,
    "98 R3.0 UHF SCF residual": true,
    "98 stretched UHF energy lowering": true,
    "98 stretched UHF spin contamination": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- PySCF Self-consistent field methods [accessed 2026-11-25]. https://pyscf.org/user/scf.html; review_level=selected-official-documentation
FC=SCe, mean-field orbital/determinant ansatz, stability vs stationarity, RHF/UHF spin symmetry and overlap orthogonalization selected passages. No PySCF execution.

- PySCF Configuration interaction (CISD and FCI) [accessed 2026-11-25]. https://pyscf.org/user/ci.html; review_level=selected-official-documentation
Introduction and FCI/spin-sector examples: all determinants within a finite symmetry sector, diagonalization, Nalpha/Nbeta. Not full chapter or full package source.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## A tiny three-center H3+ RHF / MP2 / FCI example

Demonstrate RHF, MP2 and finite-basis FCI for a tiny fixed three-center H3+ molecule.

**Methods used**

- [Hartree–Fock](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en) (`hartree-fock`)
- [MP2 perturbation theory](https://hrkoyama.github.io/numerical-methods-atlas/methods/mp2/?lang=en) (`mp2`)
- [Configuration interaction / CI](https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=en) (`configuration-interaction`)
- [Self-consistent field iteration / SCF](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en) (`scf`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en#h3plus-mp2-fci-en-algorithm)

Canonicalize RHF, evaluate the two-electron MP2 correction and9x9 FCI, and render the saved occupied-orbital density slice.

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs)
$$

$$
E_{\rm MP2}=E_{\rm RHF}+\sum_{a,b\in\mathrm{virt}}\frac{(0a|0b)^2}{2\varepsilon_0-\varepsilon_a-\varepsilon_b},\quad E_{\rm FCI}=\lambda_{\min}(H)+E_{NN}
$$

- [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en) (`stationary-schrodinger`)

Two electrons/3 explicit s orbitals, one fixed non-symmetric triangle. Molecular DFT, CC and general multireference/large molecules remain unimplemented tails. One H3+ geometry[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr, charge+1,2electrons/3s orbitals; energies in hartree.

- [Closed-shell Hartree–Fock equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en) (`hartree-fock-model`)

Two electrons/3 explicit s orbitals, one fixed non-symmetric triangle. Molecular DFT, CC and general multireference/large molecules remain unimplemented tails. One H3+ geometry[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr, charge+1,2electrons/3s orbitals; energies in hartree.


**Problem figure**

![A tiny three-center H3+ RHF / MP2 / FCI example: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en) (`h3plus-minimal`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en#h3plus-mp2-fci-en-validation)

Check independent signed-fermion assembly, determinant perturbation MP2, electron number, SCF stationarity and FCI variational ordering.

- [A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-h3plus-mp2-fci-en) (`h3plus-mp2-fci`; Same-problem reference · Finite-grid numerical reference)

Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.
### Assumptions, units and boundaries

Two electrons/3 explicit s orbitals, one fixed non-symmetric triangle. Molecular DFT, CC and general multireference/large molecules remain unimplemented tails. One H3+ geometry[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr, charge+1,2electrons/3s orbitals; energies in hartree.

**Editorial clarification**

Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.

### Adopted numerical method

Canonicalize RHF, evaluate the two-electron MP2 correction and9x9 FCI, and render the saved occupied-orbital density slice.

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs)
$$

$$
E_{\rm MP2}=E_{\rm RHF}+\sum_{a,b\in\mathrm{virt}}\frac{(0a|0b)^2}{2\varepsilon_0-\varepsilon_a-\varepsilon_b},\quad E_{\rm FCI}=\lambda_{\min}(H)+E_{NN}
$$

### References and validation

Check independent signed-fermion assembly, determinant perturbation MP2, electron number, SCF stationarity and FCI variational ordering.

### Limits

General molecular DFT, CC, large bases and general multireference methods remain unimplemented. Independent operator assembly is not an independent external chemistry-engine scalar reference.

### Stored measurements and decisions

```json
{
  "metrics": {
    "99 operator assembly": 4.440892098500626e-16,
    "99 FCI residual": 2.0196960871277348e-16,
    "99 singlet spatial symmetry": 1.821725679363684e-16,
    "99 MP2 determinant perturbation oracle": 0.0,
    "99 MP2 minimum denominator": 2.27228160503523,
    "99 FCI <= RHF": -0.02394188636845218,
    "99 RHF electron count": 0.0,
    "99 RHF SCF residual": 4.7552933164260536e-12
  },
  "checks": {
    "99 operator assembly": true,
    "99 FCI residual": true,
    "99 singlet spatial symmetry": true,
    "99 MP2 determinant perturbation oracle": true,
    "99 MP2 minimum denominator": true,
    "99 FCI <= RHF": true,
    "99 RHF electron count": true,
    "99 RHF SCF residual": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- PySCF Self-consistent field methods [accessed 2026-11-25]. https://pyscf.org/user/scf.html; review_level=selected-official-documentation
FC=SCe, mean-field orbital/determinant ansatz, stability vs stationarity, RHF/UHF spin symmetry and overlap orthogonalization selected passages. No PySCF execution.

- PySCF Second-order Moller-Plesset perturbation theory [accessed 2026-11-25]. https://pyscf.org/user/mp.html; review_level=selected-official-documentation
Introduction/total vs correlation energy/spin symmetry selected passages.

- PySCF official mp2 module source [accessed 2026-11-25]. https://pyscf.org/_modules/pyscf/mp/mp2.html; review_level=selected-official-documentation
Selected kernel lines53–87 and energy lines167–178: canonical occupied/virtual denominators and direct/exchange contractions. Source read for convention; code not copied into this packet and no fresh PySCF reference.

- PySCF Configuration interaction (CISD and FCI) [accessed 2026-11-25]. https://pyscf.org/user/ci.html; review_level=selected-official-documentation
Introduction and FCI/spin-sector examples: all determinants within a finite symmetry sector, diagonalization, Nalpha/Nbeta. Not full chapter or full package source.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Immutable periodic-helium energy and force reference audit

Map saved periodic-He energies and six-coordinate forces to unchanged independent references and criteria.

**Methods used**

- [Kohn–Sham density functional theory / DFT](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en) (`kohn-sham-dft`)
- [Pseudopotentials and PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=en) (`pseudopotentials`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en#periodic-he-reference-cards-en-algorithm)

Audit arithmetic of saved energy differences, analytic forces and Gaussian/PW comparisons under the original bounds.

$$
F_{A\alpha}=-\frac{\partial E}{\partial R_{A\alpha}},\quad F^{\rm FD}_{A\alpha}=-\frac{E(R_{A\alpha}+\delta)-E(R_{A\alpha}-\delta)}{2\delta}
$$

- [Local Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en) (`kohn-sham-model`)

Audit saved six-coordinate FD and Gaussian/PW comparisons; source versions, local-only He GTH, XC/units/cell/electron count fixed. No new k/basis/cutoff scans. Artificial He2,4electrons,5bohr cell. Stored geometry/localGTH version/LDA_X+VWN/Libxc/PySCF/DFTK versions remain fixed in saved-data/periodic-he-reference.json. Energy hartree; force hartree/bohr.


**Problem figure**

![Immutable periodic-helium energy and force reference audit: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-he-reference-cards.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en) (`periodic-he-forces`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en#periodic-he-reference-cards-en-validation)

Run zero electronic calculations. Preserve cell, units, local-only GTH, XC, electron counts and engine-version provenance; identify shared Libxc formulas.

- [Immutable periodic-helium energy and force reference audit](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-he-reference-cards-en) (`periodic-he-reference-cards`; Same-problem reference · Finite-grid numerical reference)

Audit of stored6force components, energy differences and Gaussian/PW comparisons; zero new electronic solves. No new basis/k/cutoff scans, materials, metals or longMD claim.
### Assumptions, units and boundaries

Audit saved six-coordinate FD and Gaussian/PW comparisons; source versions, local-only He GTH, XC/units/cell/electron count fixed. No new k/basis/cutoff scans. Artificial He2,4electrons,5bohr cell. Stored geometry/localGTH version/LDA_X+VWN/Libxc/PySCF/DFTK versions remain fixed in saved-data/periodic-he-reference.json. Energy hartree; force hartree/bohr.

**Editorial clarification**

Audit of stored6force components, energy differences and Gaussian/PW comparisons; zero new electronic solves. No new basis/k/cutoff scans, materials, metals or longMD claim.

### Adopted numerical method

Audit arithmetic of saved energy differences, analytic forces and Gaussian/PW comparisons under the original bounds.

$$
F_{A\alpha}=-\frac{\partial E}{\partial R_{A\alpha}},\quad F^{\rm FD}_{A\alpha}=-\frac{E(R_{A\alpha}+\delta)-E(R_{A\alpha}-\delta)}{2\delta}
$$

### References and validation

Run zero electronic calculations. Preserve cell, units, local-only GTH, XC, electron counts and engine-version provenance; identify shared Libxc formulas.

### Limits

No new SCF/DFTK/PySCF run, no basis/k/cutoff scans; preserve all old values and criteria. The He GTH is local-only, so its saved success does not test nonlocal projectors.

### Stored measurements and decisions

```json
{
  "metrics": {
    "100 saved FD arithmetic 0": 0.0,
    "100 unchanged FD science bound 0": 8.486369273974503e-09,
    "100 saved FD arithmetic 1": 0.0,
    "100 unchanged FD science bound 1": 1.4108486323660685e-08,
    "100 saved FD arithmetic 2": 0.0,
    "100 unchanged FD science bound 2": 2.1580722472935854e-08,
    "100 saved FD arithmetic 3": 0.0,
    "100 unchanged FD science bound 3": 1.1233197302895626e-08,
    "100 saved FD arithmetic 4": 0.0,
    "100 unchanged FD science bound 4": 1.818304432021911e-08,
    "100 saved FD arithmetic 5": 0.0,
    "100 unchanged FD science bound 5": 2.3223412720652092e-08,
    "100 unchanged Gaussian/PW force basis-gth-qzv3p": 7.28156560618684e-05,
    "100 unchanged Gaussian/PW energy basis-gth-qzv3p": 7.395629375217538e-05,
    "100 unchanged Gaussian/PW force basis-k2-gth-qzv3p": 7.538249895754426e-05,
    "100 unchanged Gaussian/PW energy basis-k2-gth-qzv3p": 0.00017168416810697806
  },
  "checks": {
    "100 saved FD arithmetic 0": true,
    "100 unchanged FD science bound 0": true,
    "100 saved FD arithmetic 1": true,
    "100 unchanged FD science bound 1": true,
    "100 saved FD arithmetic 2": true,
    "100 unchanged FD science bound 2": true,
    "100 saved FD arithmetic 3": true,
    "100 unchanged FD science bound 3": true,
    "100 saved FD arithmetic 4": true,
    "100 unchanged FD science bound 4": true,
    "100 saved FD arithmetic 5": true,
    "100 unchanged FD science bound 5": true,
    "100 unchanged Gaussian/PW force basis-gth-qzv3p": true,
    "100 unchanged Gaussian/PW energy basis-gth-qzv3p": true,
    "100 unchanged Gaussian/PW force basis-k2-gth-qzv3p": true,
    "100 unchanged Gaussian/PW energy basis-k2-gth-qzv3p": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- DFTK Pseudopotentials [accessed 2026-11-25]. https://docs.dftk.org/stable/examples/pseudopotentials/; review_level=selected-official-documentation
Official separable Kleinman-Bylander/norm-conserving/GTH formats and approximation limits introduction. Our rank-one kernel is authored and is not an element-fitted norm-conserving potential.

- PySCF Self-consistent field methods [accessed 2026-11-25]. https://pyscf.org/user/scf.html; review_level=selected-official-documentation
FC=SCe, mean-field orbital/determinant ansatz, stability vs stationarity, RHF/UHF spin symmetry and overlap orthogonalization selected passages. No PySCF execution.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## A three-wave periodic projector and Fermi-occupation model

Show a genuine rank-one nonlocal kernel and finite-temperature occupations in a three-wave periodic educational model.

**Methods used**

- [Schrodinger eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en) (`schrodinger`)
- [Pseudopotentials and PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=en) (`pseudopotentials`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en#periodic-projector-occupations-en-algorithm)

Solve3x3 Hermitian blocks, determine fixed-N Fermi occupations and differentiate Helmholtz free energy including entropy.

$$
H_{GG\prime}(k,R)=\tfrac12(G+k)^2\delta_{GG\prime}+V_{GG\prime}+\eta\beta_G\beta_{G\prime}^*,\quad\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R}
$$

$$
f_{kn}=\frac{2}{1+e^{(\varepsilon_{kn}-\mu)/T}},\quad\sum_{kn}w_kf_{kn}=1.5
$$

$$
F=\sum_{kn}w_kf_{kn}\varepsilon_{kn}-TS,\quad F_R=-\sum_{kn}w_kf_{kn}\langle u_{kn}|\partial_RH_k|u_{kn}\rangle
$$

- [Three-wave nonlocal kernel and mean Fermi occupations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-projector-fermi-model-en) (`finite-projector-fermi-model`)

Authored rank-one periodic linear model and finite-N Helmholtz forces. No real metal/element pseudopotential/norm conservation/Hartree-XC/long MD claim. N=1.5 is a mean independent-particle Fermi occupation count, not an integer-N canonical many-body ensemble. Dimensionless G=-1,0,1,p=G+k,k=±.25 with equal.5weights,T=.05,mean electron countN=1.5 and spin factor2. No physical lattice-constant or metal mapping.


**Problem figure**

![A three-wave periodic projector and Fermi-occupation model: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en) (`finite-projector-fermi`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en#periodic-projector-occupations-en-validation)

Check an independent cubic spectral oracle, Hermiticity, electron number, entropy, analytic force and fixed-N free-energy differences.

- [A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-projector-occupations-en) (`periodic-projector-occupations`; Same-problem reference · Semi-analytic reference)

Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.
### Assumptions, units and boundaries

Authored rank-one periodic linear model and finite-N Helmholtz forces. No real metal/element pseudopotential/norm conservation/Hartree-XC/long MD claim. N=1.5 is a mean independent-particle Fermi occupation count, not an integer-N canonical many-body ensemble. Dimensionless G=-1,0,1,p=G+k,k=±.25 with equal.5weights,T=.05,mean electron countN=1.5 and spin factor2. No physical lattice-constant or metal mapping.

**Editorial clarification**

Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.

### Adopted numerical method

Solve3x3 Hermitian blocks, determine fixed-N Fermi occupations and differentiate Helmholtz free energy including entropy.

$$
H_{GG\prime}(k,R)=\tfrac12(G+k)^2\delta_{GG\prime}+V_{GG\prime}+\eta\beta_G\beta_{G\prime}^*,\quad\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R}
$$

$$
f_{kn}=\frac{2}{1+e^{(\varepsilon_{kn}-\mu)/T}},\quad\sum_{kn}w_kf_{kn}=1.5
$$

$$
F=\sum_{kn}w_kf_{kn}\varepsilon_{kn}-TS,\quad F_R=-\sum_{kn}w_kf_{kn}\langle u_{kn}|\partial_RH_k|u_{kn}\rangle
$$

### References and validation

Check an independent cubic spectral oracle, Hermiticity, electron number, entropy, analytic force and fixed-N free-energy differences.

### Limits

The authored rank-one kernel is not an element-fitted norm-conserving pseudopotential. No self-consistent Hartree/XC, real metal, general material or long-time MD success.

### Stored measurements and decisions

```json
{
  "metrics": {
    "101 Hermiticity 0": 3.58464566598299e-18,
    "101 residual 0": 2.751670084160633e-16,
    "101 independent cubic 0": 2.7755575615628914e-16,
    "101 fixed-case cubic clamp activation 0": 0.0,
    "101 Hermiticity 1": 3.58464566598299e-18,
    "101 residual 1": 2.7503882064100795e-16,
    "101 independent cubic 1": 2.7755575615628914e-16,
    "101 fixed-case cubic clamp activation 1": 0.0,
    "101 fixed electron number": 6.661338147750939e-16,
    "101 lower occupation": 4.6784131873466673e-05,
    "101 upper occupation": 1.4444120001743874,
    "101 nonnegative entropy": 1.4360712457901055,
    "101 finest free-energy force difference": 1.721169318180671e-10
  },
  "checks": {
    "101 Hermiticity 0": true,
    "101 residual 0": true,
    "101 independent cubic 0": true,
    "101 fixed-case cubic clamp activation 0": true,
    "101 Hermiticity 1": true,
    "101 residual 1": true,
    "101 independent cubic 1": true,
    "101 fixed-case cubic clamp activation 1": true,
    "101 fixed electron number": true,
    "101 lower occupation": true,
    "101 upper occupation": true,
    "101 nonnegative entropy": true,
    "101 finest free-energy force difference": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- DFTK periodic problems and plane-wave discretisations [accessed 2026-11-25]. https://docs.dftk.org/stable/guide/periodic_problems/; review_level=selected-official-documentation
Selected displayed Bloch/periodic operator/plane-wave basis context; no material calculations reproduced.

- DFTK Pseudopotentials [accessed 2026-11-25]. https://docs.dftk.org/stable/examples/pseudopotentials/; review_level=selected-official-documentation
Official separable Kleinman-Bylander/norm-conserving/GTH formats and approximation limits introduction. Our rank-one kernel is authored and is not an element-fitted norm-conserving potential.

- DFTK Temperature and metallic systems [accessed 2026-11-25]. https://docs.dftk.org/stable/examples/metallic_systems/; review_level=selected-official-documentation
Selected Fermi-Dirac smearing temperature, partial occupations, explicit unconverged fast-example warning and energy Entropy term. No magnesium run, no new k/basis/cutoff scans.

- NumPy2.0 numpy.linalg.eigh [accessed 2026-11-25]. https://numpy.org/doc/2.0/reference/generated/numpy.linalg.eigh.html; review_level=selected-official-documentation
Signature, Hermitian lower-triangle handling, all ascending eigenvalues/normalized columns, LinAlgError and LAPACK syevd/heevd notes.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
