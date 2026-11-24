# LBM curved walls and a Re20 cylinder

Advance actual Re20 cylinder flow with curved walls and an open outlet; compare forces,pressure difference and wake with independent numerical benchmarks.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet

Evolve the full-length original2D-1channel andoff-center cylinder on twogrids,checking drag,lift,surface pressure difference,recirculation length andstationarity.

**Methods used**

- [D2Q9–BGK collision and streaming](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en) (`d2q9-bgk`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en#lbm-cylinder-re20-en-algorithm)

StandardBGK,true-circle quadratic links,halfwaychannelwalls,nonperiodic openstreaming. Setall9outlet populations tofeq(1,ua)+fa−feq(rhoa,ua); ledgerchanges include theknown6. Evolve fromaPoiseuille pressureguess; normalizeactual momentumexchange bymean speed.

$$
\mathrm{Re}=\overline U D/\nu=20,\quad C_D=2F_x/(\rho\overline U^2D),\quad C_L=2F_y/(\rho\overline U^2D)
$$

$$
\Delta p=p(.15,.2)-p(.25,.2),\quad L_a=x_{reattach}-.25
$$

$$
f_{i,b}=f_i^{eq}(1,u_a)+f_{i,a}-f_i^{eq}(\rho_a,u_a),\quad i=0,\ldots,8
$$

- [Isothermal lattice BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en) (`bgk`)

[0,2.2]x[0,.41],center(.2,.2),R.05,nu.001,rho1,mean.2/peak.3/Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18k/36ksteps. Parabolic inlet;all-nine poststream NEE outletwithrho1andadjacent-interiorvelocity.

- [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en) (`navier-stokes`)

[0,2.2]x[0,.41],center(.2,.2),R.05,nu.001,rho1,mean.2/peak.3/Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18k/36ksteps. Parabolic inlet;all-nine poststream NEE outletwithrho1andadjacent-interiorvelocity.


**Problem figure**

![Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en) (`lbm-cylinder-re20`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en#lbm-cylinder-re20-en-validation)

Group28pytest;33cylinder gates. Score distance fromoriginalTable3estimated ranges usingseparate frozen coarse-grid tolerances:CD5%,CLabsolute.01,dp10%,Laabsolute.025. Check26/28/30field/force/dp stationarity,twogrid difference,Ma andwall/open budgets. Retain prior outletinstability anddistinguish the87boundarycomponent qualifiers frommain acceptance.

- [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cylinder-re20-en) (`lbm-cylinder-re20`; Same-problem reference · Finite-grid numerical reference)

Originalpp3/7allow selectingoutflow. AdoptedNEEis independently derived finite reservoir,not claimed exactunread authorimplementation orFEATflowdo-nothing. Nabhvaluesarenotexact adopted-BCtruth andoriginalrangesarenotrigorousenclosures. Retain failedlinear/Zou–Heattempt(outlet-nearstep265). FiniteMach/BC/curveerrors;nogeneralaccuracyguarantee.
### Assumptions, units and boundaries

[0,2.2]x[0,.41],center(.2,.2),R.05,nu.001,rho1,mean.2/peak.3/Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18k/36ksteps. Parabolic inlet;all-nine poststream NEE outletwithrho1andadjacent-interiorvelocity.

**Editorial clarification**

Originalpp3/7allow selectingoutflow. AdoptedNEEis independently derived finite reservoir,not claimed exactunread authorimplementation orFEATflowdo-nothing. Nabhvaluesarenotexact adopted-BCtruth andoriginalrangesarenotrigorousenclosures. Retain failedlinear/Zou–Heattempt(outlet-nearstep265). FiniteMach/BC/curveerrors;nogeneralaccuracyguarantee.

### Adopted numerical method

StandardBGK,true-circle quadratic links,halfwaychannelwalls,nonperiodic openstreaming. Setall9outlet populations tofeq(1,ua)+fa−feq(rhoa,ua); ledgerchanges include theknown6. Evolve fromaPoiseuille pressureguess; normalizeactual momentumexchange bymean speed.

$$
\mathrm{Re}=\overline U D/\nu=20,\quad C_D=2F_x/(\rho\overline U^2D),\quad C_L=2F_y/(\rho\overline U^2D)
$$

$$
\Delta p=p(.15,.2)-p(.25,.2),\quad L_a=x_{reattach}-.25
$$

$$
f_{i,b}=f_i^{eq}(1,u_a)+f_{i,a}-f_i^{eq}(\rho_a,u_a),\quad i=0,\ldots,8
$$

### References and validation

Group28pytest;33cylinder gates. Score distance fromoriginalTable3estimated ranges usingseparate frozen coarse-grid tolerances:CD5%,CLabsolute.01,dp10%,Laabsolute.025. Check26/28/30field/force/dp stationarity,twogrid difference,Ma andwall/open budgets. Retain prior outletinstability anddistinguish the87boundarycomponent qualifiers frommain acceptance.

### Limits

Originalpp3/7allow selectingoutflow. AdoptedNEEis independently derived finite reservoir,not claimed exactunread authorimplementation orFEATflowdo-nothing. Nabhvaluesarenotexact adopted-BCtruth andoriginalrangesarenotrigorousenclosures. Retain failedlinear/Zou–Heattempt(outlet-nearstep265). FiniteMach/BC/curveerrors;nogeneralaccuracyguarantee.

### Stored measurements and decisions

```json
{
  "metrics": {
    "finest": {
      "dx": 0.005,
      "dt": 0.0008333333333333334,
      "tau": 0.6,
      "steps": 36000,
      "time": 30.000000000000004,
      "Re": 20,
      "CD": 5.644519321602302,
      "CL": 0.011096755643135437,
      "stationarity": 0.0002032789456526155,
      "drag_drift": 0.000151098422030169,
      "lift_drift": 3.478689810392302e-06,
      "pressure_drift": 1.863260540397613e-06,
      "pressure_difference": 0.11872124659802585,
      "recirculation_length": 0.08386681527452555,
      "mass_drift": 0.0004002747565754678,
      "mass_ledger": 3.339112580809518e-12,
      "momentum_ledger": 3.37499434539968e-12,
      "max_mach": 0.1536578006651768,
      "min_rho": 0.9010633065006105,
      "max_rho": 1.1123850424542971,
      "min_population": 0.020454450201225206,
      "wall_mass_exchange": 16.570402727464682,
      "open_mass_exchange": -2.2019060198153952,
      "final_lattice_momentum_x": 1213.6393581371472,
      "final_lattice_momentum_y": 0.17207763765525091
    },
    "reference_scope": "Schäfer-Turek1996 Table3 estimated numerical-comparison ranges, not exact or rigorous enclosures. Original pp3/7 allow user-selected outflow. This source uses a declared all-nine poststream NEE pressure reservoir, not later FEATflow do-nothing; exact original-author NEE implementation is not claimed. Coarse LBM acceptance separately fixed before execution.",
    "outlet": "All-nine poststream NEE: rho1,adjacent-poststream velocity; finite reservoir,not later FEATflow do-nothing",
    "initial_pressure": "Straight Poiseuille-gradient guess, not a cylinder reference or imposed interior field"
  },
  "checks": {
    "original source definitions and interval anchors": true,
    "0.01 finite arrays": true,
    "0.01 positive density": true,
    "0.01 actual maximum Mach": true,
    "0.01 mass ledger": true,
    "0.01 wall-open momentum ledger": true,
    "0.01 all fixed integer steps": true,
    "0.01 declared physical endpoint": true,
    "0.01 velocity stationarity": true,
    "0.01 drag late block drift": true,
    "0.01 lift late block drift": true,
    "0.01 pressure late drift": true,
    "0.01 positive downstream drag": true,
    "0.01 pressure front exceeds back": true,
    "0.005 finite arrays": true,
    "0.005 positive density": true,
    "0.005 actual maximum Mach": true,
    "0.005 mass ledger": true,
    "0.005 wall-open momentum ledger": true,
    "0.005 all fixed integer steps": true,
    "0.005 declared physical endpoint": true,
    "0.005 velocity stationarity": true,
    "0.005 drag late block drift": true,
    "0.005 lift late block drift": true,
    "0.005 pressure late drift": true,
    "0.005 positive downstream drag": true,
    "0.005 pressure front exceeds back": true,
    "finest original range distance CD": true,
    "finest original range distance CL": true,
    "finest original range distance pressure_difference": true,
    "finest original range distance recirculation_length": true,
    "two-grid drag sensitivity": true,
    "both prescribed actual full-domain cylinder grids": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/index.json

![Actual saved2Dfields anddiagnostics fromfixedinputs; reference,boundary anderror scopesaredeclaredinthecase.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20-preview.png)

Actual saved2Dfields anddiagnostics fromfixedinputs; reference,boundary anderror scopesaredeclaredinthecase.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/atlas-lbm-curved-boundary-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Qisu Zou and Xiaoyi He (1996). On pressure and velocity flow boundary conditions and bounceback for the lattice Boltzmann BGK model. https://arxiv.org/abs/comp-gas/9611001; review_level=primary-selected-extracted-text
Selected primary equations and flat-boundary/corner/compressibility discussion read; special d2q9i successes are not borrowed.

- Pierre Lallemand and Li-Shi Luo (2003). Lattice Boltzmann method for moving boundaries. https://doi.org/10.1016/S0021-9991(02)00022-0; review_level=primary-selected-text-via-mirror
Read selected original Eq12–15 on quadratic links,wall correction,momentum exchange andmassnonconservation; qualify by a generic-Lagrange scalar oracle. No2001fulltext orlocalPDFsymbol audit.

- M. Schäfer and S. Turek (1996). Benchmark Computations of Laminar Flow Around a Cylinder. https://kent-and.github.io/mek4250/2021/SchaeferTurek1996.pdf; review_level=primary-selected-extracted-text
Read original geometry/definitions/user-selected outflow/Table3estimated intervals via a disclosed course mirror after official404s.

- FEATflow benchmark project (2026). DFG flow around cylinder benchmark2D-1, Re20. https://wwwold.mathematik.tu-dortmund.de/~featflow/en/benchmarks/cfdbenchmarking/flow/dfg_benchmark1_re20.html; review_level=official-benchmark-page
Official BC/definitions/Nabh attribution read; Nabh original unread and values not labelled exact adopted-outlet truth.

- Zhaoli Guo,Chuguang Zheng and Baochang Shi (2002). Non-equilibrium extrapolation method for velocity and pressure boundary conditions in the lattice Boltzmann method. https://cpb.iphy.ac.cn/en/article/doi/10.1088/1009-1963/11/4/310; review_level=primary-official-abstract-only
Official primary abstract only. Full equations unread; adopted all-nine poststream pressure reservoir is independently derived and qualified.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
