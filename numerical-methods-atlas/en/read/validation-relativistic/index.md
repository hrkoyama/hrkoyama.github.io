# SRHD collision and nonlinear SRMHD Alfven wave

Compare an SRHD head-on collision with a Taub two-shock solution and full7-state finite-amplitude SRMHD wave with independent tensor formulas/conserved means. Space is1D; x–t pictures are not2D flow.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## SRHD symmetric two-shock collision

Compare a relativistic symmetric collision with independent exact Taub-based conserved cell means; save actual1D x–t fields.

**Methods used**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) (`minmod`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en#srhd-collision-en-algorithm)

Use the shared seven-component RMHD operator at B=0 with primitive MUSCL/minmod, causal HLL bounds±1 and SSPRK33. Safeguarded Newton recovers the physical Z=rho h W² root; check residual and full conserved-state roundtrip.

$$
U=(D,S_x,S_y,S_z,E,B_y,B_z)^T,\quad D=\rho W,\quad W=(1-v^2)^{-1/2}
$$

$$
h_b^2-h_a^2=(p_b-p_a)(h_b/\rho_b+h_a/\rho_a)
$$

$$
v_0^2=\frac{(p_b-p_a)(e_b-e_a)}{(e_a+p_b)(e_b+p_a)},\quad e=\rho+\frac{p}{\Gamma-1}
$$

$$
j^2=-\frac{p_b-p_a}{h_b/\rho_b-h_a/\rho_a},\quad V_s^2=\frac{j^2}{\rho_b^2+j^2}
$$

- [Special-relativistic hydrodynamics (SRHD)](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srhd-en) (`srhd`)

c=1,gamma5/3,rho1,p.1,opposite normal v±.3,B0. Domain[0,1], initial jump .5,t=.3,96/192/384 cells. Constant extrapolation boundaries before shocks reach endpoints.


**Problem figure**

![SRHD symmetric two-shock collision: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en) (`srhd-collision`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en#srhd-collision-en-validation)

Predeclare25 pytest tests,six runs,110 group gates and six reference qualifiers. Check all-component boundary budgets, stage/face admissibility,D/E refinement,star pressure,shock positions and reflection. Compare actual final states with independent scalar-pressure SRHD recovery and flux.

- [Relativistic symmetric collision: specialized two-shock Taub reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srhd-collision-en) (`srhd-collision`; Same-problem reference · Semi-analytic reference)

Custom mild symmetric input; contact degenerates to identical resting states. No general three-wave Riemann,extreme-Lorentz-factor or original-paper numerical-input reproduction claim. E includes rest mass; compare exact conserved cell means.
### Assumptions, units and boundaries

c=1,gamma5/3,rho1,p.1,opposite normal v±.3,B0. Domain[0,1], initial jump .5,t=.3,96/192/384 cells. Constant extrapolation boundaries before shocks reach endpoints.

**Editorial clarification**

Custom mild symmetric input; contact degenerates to identical resting states. No general three-wave Riemann,extreme-Lorentz-factor or original-paper numerical-input reproduction claim. E includes rest mass; compare exact conserved cell means.

### Adopted numerical method

Use the shared seven-component RMHD operator at B=0 with primitive MUSCL/minmod, causal HLL bounds±1 and SSPRK33. Safeguarded Newton recovers the physical Z=rho h W² root; check residual and full conserved-state roundtrip.

$$
U=(D,S_x,S_y,S_z,E,B_y,B_z)^T,\quad D=\rho W,\quad W=(1-v^2)^{-1/2}
$$

$$
h_b^2-h_a^2=(p_b-p_a)(h_b/\rho_b+h_a/\rho_a)
$$

$$
v_0^2=\frac{(p_b-p_a)(e_b-e_a)}{(e_a+p_b)(e_b+p_a)},\quad e=\rho+\frac{p}{\Gamma-1}
$$

$$
j^2=-\frac{p_b-p_a}{h_b/\rho_b-h_a/\rho_a},\quad V_s^2=\frac{j^2}{\rho_b^2+j^2}
$$

### References and validation

Predeclare25 pytest tests,six runs,110 group gates and six reference qualifiers. Check all-component boundary budgets, stage/face admissibility,D/E refinement,star pressure,shock positions and reflection. Compare actual final states with independent scalar-pressure SRHD recovery and flux.

### Limits

Custom mild symmetric input; contact degenerates to identical resting states. No general three-wave Riemann,extreme-Lorentz-factor or original-paper numerical-input reproduction claim. E includes rest mass; compare exact conserved cell means.

### Stored measurements and decisions

```json
{
  "metrics": {
    "exact_star": {
      "pressure": 0.35473854747189193,
      "density": 2.036718245233174,
      "enthalpy": 1.4354290883166312,
      "speed": 0.3181655418651244,
      "relative_velocity": 0.3,
      "taub_residual": -3.3306690738754696e-16
    },
    "finest_D_l1": 0.0054242304454669415,
    "finest_E_l1": 0.005207375513692991,
    "exact_scope": "Symmetric identical thermodynamics, opposite normal velocities: two shocks and resting identical star states; no nontrivial contact or general three-wave certification."
  },
  "checks": {
    "n96: fixed final time": true,
    "n96: five saved times": true,
    "n96: four records per SSP step": true,
    "n96: all stored arrays finite": true,
    "n96: positive stage density": true,
    "n96: positive stage pressure": true,
    "n96: subluminal stages": true,
    "n96: positive reconstructed face density": true,
    "n96: positive reconstructed face pressure": true,
    "n96: subluminal reconstructed faces": true,
    "n96: conserved finite-volume boundary budget": true,
    "n96: physical root residual": true,
    "n96: full conserved primitive roundtrip": true,
    "n96: no state floor or retry": true,
    "n96: reflection symmetry": true,
    "n96: independent SRHD zero B flux and recovery": true,
    "n192: fixed final time": true,
    "n192: five saved times": true,
    "n192: four records per SSP step": true,
    "n192: all stored arrays finite": true,
    "n192: positive stage density": true,
    "n192: positive stage pressure": true,
    "n192: subluminal stages": true,
    "n192: positive reconstructed face density": true,
    "n192: positive reconstructed face pressure": true,
    "n192: subluminal reconstructed faces": true,
    "n192: conserved finite-volume boundary budget": true,
    "n192: physical root residual": true,
    "n192: full conserved primitive roundtrip": true,
    "n192: no state floor or retry": true,
    "n192: reflection symmetry": true,
    "n192: independent SRHD zero B flux and recovery": true,
    "n384: fixed final time": true,
    "n384: five saved times": true,
    "n384: four records per SSP step": true,
    "n384: all stored arrays finite": true,
    "n384: positive stage density": true,
    "n384: positive stage pressure": true,
    "n384: subluminal stages": true,
    "n384: positive reconstructed face density": true,
    "n384: positive reconstructed face pressure": true,
    "n384: subluminal reconstructed faces": true,
    "n384: conserved finite-volume boundary budget": true,
    "n384: physical root residual": true,
    "n384: full conserved primitive roundtrip": true,
    "n384: no state floor or retry": true,
    "n384: reflection symmetry": true,
    "n384: independent SRHD zero B flux and recovery": true,
    "finest D L1": true,
    "finest total E L1": true,
    "finest star pressure": true,
    "finest shock position": true,
    "collision component 0 refinement 1": true,
    "collision component 4 refinement 1": true,
    "collision component 0 refinement 2": true,
    "collision component 4 refinement 2": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/index.json

![Actual finest-grid1D x–t conserved-density field from five stored times; not a two-dimensional flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png)

Actual finest-grid1D x–t conserved-density field from five stored times; not a two-dimensional flow.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Luciano Rezzolla and Olindo Zanotti (2001). An Improved Exact Riemann Solver for Relativistic Hydrodynamics [accessed 2026-11-23]. https://arxiv.org/abs/gr-qc/0103005; review_level=primary-selected-mathematical-sections
Read original preprint sections2–4: EOS, relative-velocity equation3.1 and Taub quadratic4.5. Restricted symmetric two-shock specialization.

- José A. Font (2008). Numerical Hydrodynamics and Magnetohydrodynamics in General Relativity [accessed 2026-11-23]. https://link.springer.com/article/10.12942/lrr-2008-7; review_level=primary-author-review-selected-equations
Read official author-review sections3.1–3.2, stress tensor49–51 and recovery68–69; flat-spacetime use only.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## SRMHD finite-amplitude circularly polarized Alfvén wave

Evolve a nonlinear finite-amplitude wave for one period with full SRMHD magnetic stress and induction; check exact cell means,phase,amplitude and refinement.

**Methods used**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) (`minmod`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en#srmhd-alfven-en-algorithm)

Evolve all seven variables D,three momenta,total E and two transverse magnetic fields with the shared MUSCL/minmod–HLL–SSPRK33 operator. Magnetic dynamics are coupled; primitive recovery solves the full RMHD Z root.

$$
B_y=\eta B_0\cos[2\pi(x-v_At)],\quad B_z=\eta B_0\sin[2\pi(x-v_At)]
$$

$$
v_x=0,\quad (v_y,v_z)=-v_A(B_y,B_z)/B_0
$$

$$
K=\rho h+B_0^2(1+\eta^2),\quad v_A^2=\frac{2B_0^2}{K+\sqrt{K^2-4\eta^2B_0^4}}
$$

$$
\mathbf v=\frac{\mathbf S+(\mathbf S\cdot\mathbf B)\mathbf B/Z}{Z+B^2},\quad p=\frac{\Gamma-1}{\Gamma}(Z/W^2-\rho)
$$

$$
E=Z-p+\frac12\left[B^2(1+v^2)-\frac{(\mathbf S\cdot\mathbf B)^2}{Z^2}\right]
$$

- [Special-relativistic ideal MHD (SRMHD)](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srmhd-en) (`srmhd`)

Flat spacetime,c=4pi=1,gamma4/3,rho=p=Bx=eta1, exact-family vx0. Rescale the original2pi period to a unit domain;64/128/256 cells,periodic,t=1/vA. Normal Bx is fixed in1D.


**Problem figure**

![SRMHD finite-amplitude circularly polarized Alfvén wave: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en) (`srmhd-alfven`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en#srmhd-alfven-en-validation)

Qualify nonlinear dispersion,independent tensor Gauss means and complex-step PDE residuals. Predeclare all-seven-component conservation,stage admissibility,intermediate errors,finest relative L1≤.04,phase≤.03,amplitude≤.04 and observed order≥1.5.

- [SRMHD circular wave: finite-amplitude exact family and independent tensor integration](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srmhd-alfven-en) (`srmhd-alfven`; Same-problem reference · Analytic reference)

Use the original exact family with an independent lower-order operator; no ECHO-algorithm or error-table reproduction. Generic RMHD shocks,extreme magnetization/Lorentz factors,GR,resistive MHD and multidimensional divergence control are outside scope. Figures show actual1D x–t fields.
### Assumptions, units and boundaries

Flat spacetime,c=4pi=1,gamma4/3,rho=p=Bx=eta1, exact-family vx0. Rescale the original2pi period to a unit domain;64/128/256 cells,periodic,t=1/vA. Normal Bx is fixed in1D.

**Editorial clarification**

Use the original exact family with an independent lower-order operator; no ECHO-algorithm or error-table reproduction. Generic RMHD shocks,extreme magnetization/Lorentz factors,GR,resistive MHD and multidimensional divergence control are outside scope. Figures show actual1D x–t fields.

### Adopted numerical method

Evolve all seven variables D,three momenta,total E and two transverse magnetic fields with the shared MUSCL/minmod–HLL–SSPRK33 operator. Magnetic dynamics are coupled; primitive recovery solves the full RMHD Z root.

$$
B_y=\eta B_0\cos[2\pi(x-v_At)],\quad B_z=\eta B_0\sin[2\pi(x-v_At)]
$$

$$
v_x=0,\quad (v_y,v_z)=-v_A(B_y,B_z)/B_0
$$

$$
K=\rho h+B_0^2(1+\eta^2),\quad v_A^2=\frac{2B_0^2}{K+\sqrt{K^2-4\eta^2B_0^4}}
$$

$$
\mathbf v=\frac{\mathbf S+(\mathbf S\cdot\mathbf B)\mathbf B/Z}{Z+B^2},\quad p=\frac{\Gamma-1}{\Gamma}(Z/W^2-\rho)
$$

$$
E=Z-p+\frac12\left[B^2(1+v^2)-\frac{(\mathbf S\cdot\mathbf B)^2}{Z^2}\right]
$$

### References and validation

Qualify nonlinear dispersion,independent tensor Gauss means and complex-step PDE residuals. Predeclare all-seven-component conservation,stage admissibility,intermediate errors,finest relative L1≤.04,phase≤.03,amplitude≤.04 and observed order≥1.5.

### Limits

Use the original exact family with an independent lower-order operator; no ECHO-algorithm or error-table reproduction. Generic RMHD shocks,extreme magnetization/Lorentz factors,GR,resistive MHD and multidimensional divergence control are outside scope. Figures show actual1D x–t fields.

### Stored measurements and decisions

```json
{
  "metrics": {
    "alfven_speed": 0.3819660112501051,
    "period": 2.6180339887498953,
    "finest_transverse_relative_l1": 0.0032808347423469524,
    "observed_orders": [
      1.8810822553983044,
      1.8033064216647157
    ],
    "exact_scope": "Nonlinear finite-amplitude circular polarization; not linear passive transport or a generic RMHD Riemann reference."
  },
  "checks": {
    "n64: fixed final time": true,
    "n64: five saved times": true,
    "n64: four records per SSP step": true,
    "n64: all stored arrays finite": true,
    "n64: positive stage density": true,
    "n64: positive stage pressure": true,
    "n64: subluminal stages": true,
    "n64: positive reconstructed face density": true,
    "n64: positive reconstructed face pressure": true,
    "n64: subluminal reconstructed faces": true,
    "n64: conserved finite-volume boundary budget": true,
    "n64: physical root residual": true,
    "n64: full conserved primitive roundtrip": true,
    "n64: no state floor or retry": true,
    "n64: actual magnetic wave present": true,
    "n64: intermediate wave errors": true,
    "n128: fixed final time": true,
    "n128: five saved times": true,
    "n128: four records per SSP step": true,
    "n128: all stored arrays finite": true,
    "n128: positive stage density": true,
    "n128: positive stage pressure": true,
    "n128: subluminal stages": true,
    "n128: positive reconstructed face density": true,
    "n128: positive reconstructed face pressure": true,
    "n128: subluminal reconstructed faces": true,
    "n128: conserved finite-volume boundary budget": true,
    "n128: physical root residual": true,
    "n128: full conserved primitive roundtrip": true,
    "n128: no state floor or retry": true,
    "n128: actual magnetic wave present": true,
    "n128: intermediate wave errors": true,
    "n256: fixed final time": true,
    "n256: five saved times": true,
    "n256: four records per SSP step": true,
    "n256: all stored arrays finite": true,
    "n256: positive stage density": true,
    "n256: positive stage pressure": true,
    "n256: subluminal stages": true,
    "n256: positive reconstructed face density": true,
    "n256: positive reconstructed face pressure": true,
    "n256: subluminal reconstructed faces": true,
    "n256: conserved finite-volume boundary budget": true,
    "n256: physical root residual": true,
    "n256: full conserved primitive roundtrip": true,
    "n256: no state floor or retry": true,
    "n256: actual magnetic wave present": true,
    "n256: intermediate wave errors": true,
    "finest transverse L1": true,
    "finest wave phase": true,
    "finest wave amplitude": true,
    "minimum observed grid order": true,
    "wave refinement 1": true,
    "wave refinement 2": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/index.json

![Actual finest-grid transverse By in1D x–t from five stored times; the solver includes full magnetic coupling.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png)

Actual finest-grid transverse By in1D x–t from five stored times; the solver includes full magnetic coupling.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- L. Del Zanna, O. Zanotti, N. Bucciantini and P. Londrillo (2007). ECHO: a Eulerian Conservative High Order scheme for general relativistic magnetohydrodynamics and magnetodynamics [accessed 2026-11-23]. https://arxiv.org/abs/0704.3206; review_level=primary-original-selected-section-and-rendered-pages
Read original journal section4.1 equations82–85 via the university repository; rendered and visually inspected original preprint pages9–10, including normalization and period. No ECHO-algorithm reproduction.

- José A. Font (2008). Numerical Hydrodynamics and Magnetohydrodynamics in General Relativity [accessed 2026-11-23]. https://link.springer.com/article/10.12942/lrr-2008-7; review_level=primary-author-review-selected-equations
Read official author-review sections3.1–3.2, stress tensor49–51 and recovery68–69; flat-spacetime use only.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
