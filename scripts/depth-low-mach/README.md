# Low-Mach isentropic vortex: spatially preconditioned Roe

A small, standalone nonlinear two-dimensional ideal-gas Euler example.
The current revision uses the SAME unlimited centered primitive-MUSCL
reconstruction with ordinary Roe and Miczek spatially preconditioned Roe
fluxes. Both use physical-time SSPRK(3,3), with acoustic CFL=0.2.

## Reproduce the fixed comparison

Use Python3.12 and the three pinned runtime dependencies. No C++ compiler,
private checkout, external Euler library, plotting library or network is
needed after obtaining the package and installing these dependencies.

```sh
python -m pip install -r requirements.txt
python -m pytest -q -p no:cacheprovider
python -W error run.py --input inputs.json --output output
```

The output directory must be new or empty. All twelve fixed runs execute;
there are no hidden retries, state/pressure floors or repaired states.
The current run takes about4.4 seconds on the original Mac; this is a
measured platform-specific time, not a performance guarantee.

Optional saved-data plotting uses the separately pinned requirements:

```sh
python -m pip install -r requirements-plot.txt
python plot.py --results output/result.json --output figures
```

The plotter evaluates no PDE. It verifies saved field/history/source hashes
and also reads the retained original failed trial. Nine files (three figures
in PNG/SVG/PDF) include that trial's full-domain pressure map.

## Physical problem and analytic qualification

- Full periodic Cartesian box [-10,10] squared, gamma1.4.
- Mean density1, mean velocity(1,0.5), vortex beta3.
- Background Mach numbers0.1 and0.01, retaining the SAME flow speed and
  vortex strength. Pressure is |U_infinity|^2/(gamma*M_infinity^2).
- Three grids16²/32²/64², both flux variants, physical final time0.1.
- The local maximum Mach varies and is about1.4 times the background Mach
  on the finest grid. The named Mach parameter is not maximum local Mach.

This family rescales the existing KEEP whole-plane isentropic vortex.
The finite periodic box uses minimum-image coordinates; the Gaussian seam
is a stated model approximation. Its velocity jump bound is about9.24e-21
for this short horizon. The analytic reference is independently evaluated
from physical equations, with hand-derived q_t and Euler residual checks.

Initial and final comparison states are CONSERVED cell averages from
eight-point tensor Gauss quadrature, qualified against order16. The largest
dynamic-scale difference is about4.08e-11, below the frozen2e-7 criterion.
This is not a closed-form exact cell mean. Pressure/velocity comparisons
evaluate primitive variables FROM those cell means, consistently on both
numerical and reference states; they are not averages of primitive values.

## Actual spatial preconditioning and time stepping

Only the Roe numerical dissipation changes, through P^-1|P A| with the
Miczek matrix in primitive variables and conservative-variable Jacobians.
Papers and exact variable conventions are in references/definition.json.
The cutoff uses the local Roe TOTAL speed Mach with a floor equal to the
selected background Mach. Physical sound speed and Euler time derivative
are unchanged. This is not an implicit or dual-time solver.

The matrix absolute value is applied by its degree-two characteristic
polynomial. A separately written dense eigendecomposition oracle checks
the matrix and the Roe jump/physical-flux difference identities.

Both variants reconstruct unlimited centered primitive slopes. This is
appropriate only to the selected smooth inputs. It is not a limiter/TVD
method or general positivity guarantee. Each reconstructed face and each
actual RK stage must have finite positive density and pressure. Failure
retains raw states, raw reconstructed faces when applicable, context and
completed history, then stops. Each run has a20000-step budget.

The initial truncation diagnostic is R_h(q_exact_means)-q_t_exact_means.
It measures error for a translating physical solution; it is NOT evidence
of a converged steady solution or accelerated steady residual.

## Forward Euler is not certified by the SSPRK name

The chosen spatial operators have a forward-Euler amplification counterexample
at the actual acoustic step, including ordinary Roe with unlimited MUSCL.
No conditional SSP/TVD/nonlinear theorem is borrowed by naming SSPRK(3,3).

We separately check all17² sampled Fourier modes for each of two background
Mach values and two flux variants. The EXACT linearization of the centered
primitive-MUSCL spatial operator uses

- advection coefficient sin(k)*(3-cos(k))/2;
- dissipation coefficient (1-cos(k))²/2.

A finite-difference Jacobian of the actual reconstructed RHS is checked
against independently assembled dense physical matrices. The sampled
SSPRK3 spectral-radius maximum is1.0. Matrix powers1/10/100 have maximum
2-norm1.0 in the explicitly stated physical acoustic-energy/entropy
variables. The low-Mach preconditioned forward-Euler maximum is1.03560.
These are sampled uniform-state checks, not an all-wave-number or nonlinear
stability proof. Actual twelve-run stage checks provide separate evidence.

## Measured results and retained limitations

The current revision passes35 tests and all143 frozen numerical gates.
The largest relative periodic residual among all four conserved quantities
is4.24e-14. This checks total conserved energy, not kinetic-energy invariance.

At N64, M_infinity=0.01:

- Velocity relative L1: ordinary Roe0.0741088; preconditioned0.0184687.
- Whole-domain pressure L1 / (rho_infinity*|U_infinity|²):
  ordinary0.0119411; preconditioned0.0126041.
- Pressure in the fixed radius3 core: ordinary0.0487105;
  preconditioned0.000632485.
- Cell-mean perturbation-kinetic-energy ratios to analytic cell means:
  ordinary0.945626; preconditioned0.997324.

Velocity error divides by the norm of the analytic VORTEX perturbation, not
the larger background flow. Pressure divides by the fixed dynamic scale
rho_infinity*|U_infinity|²=1.25, not the large thermodynamic pressure.
The fixed-core pressure diagnostic does not replace the whole-domain norm.

At M_infinity=0.1 the finest velocity errors are0.0124030/0.0111110
(preconditioned/Roe ratio0.8958), a modest benefit. Whole-domain pressure
errors are0.000665253/0.000673656. Thus global pressure is slightly WORSE
with preconditioning at both finest cases, despite improved velocity/core
pressure. Its error also grows when Mach is reduced. Do not claim universal
pressure improvement or Mach-independent pressure accuracy. The full
pressure maps, including current box-wide waves, remain visible.

The convective time steps in the results are diagnostics, not time steps
used in the runs. The explicit acoustic restriction remains. T=0.1 is only
about0.56 percent of a box crossing at the mean speed. No full vortex
period, long-time preservation, steady convergence acceleration, shocks,
general meshes or arbitrary Mach numbers are verified here.

## Original failed trial is part of the record

The original piecewise-constant spatial trial passed32 unit tests and142
of143 gates. At M_infinity=0.01,N64 its preconditioned whole-domain pressure
error0.1653667632 exceeded the predeclared0.1 criterion. attempts/01 retains
the original source, contract, logs, twelve full2D fields and failed result.
The additional figure displays the FULL pressure field, not a core crop.

Revision2 changes BOTH variants to unlimited centered primitive MUSCL,
consistent with the smooth unlimited reconstruction discussed in Miczek
etal(2015), Section6. It adds reconstructed-face failure guards and three
regression checks, and uses the exact corresponding Fourier symbol.
Original physical inputs, grid/Mach/time/CFL and acceptance.json are
BYTE-IDENTICAL. The old contract is contract-first-order.json; the revised
pre-run-contract.json was frozen before revision2 execution. The failed
result is never changed to a success.

## Sources and terms

Citations distinguish the original Miczek2015 matrix, Barsukow2017 stability
analysis, NASA's analytic-vortex/boundary discussion, and SSPRK coefficients
versus their conditional stability theorem. See references/citations.json
and references/README.md for the exact selected portions reviewed. No
Gresho/NASA solver execution, independent PDE engine, full-paper audit or
third-party figure reproduction is claimed.

Original software is MIT. Prose, figures and numerical input/output data
have separate conditions; see LICENSE and the public licensing policy.
