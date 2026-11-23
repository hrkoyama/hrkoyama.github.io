# Guderley converging shock: lightweight spherical radial verification

The fixed example evolves a pre-collapse inward shock with an independently
written, one-dimensional spherical finite-volume Euler solver. It compares
three radial grids against the semi-analytic Guderley branch evaluated by
actual pinned LANL ExactPack eigenvalue and ODE routines. The reference
adapter, original-source provenance, licenses and selected bibliography are
in `references/`. The adapter is not claimed as an independently derived ODE.

## Reproduce the fixed runs

Use Python 3.12 and the three pinned dependencies:

```sh
python -m pip install -r requirements.txt
python -m pytest -q -p no:cacheprovider
python -W error run.py --input inputs.json --output output
```

Use a fresh or empty output directory. All three fixed grids execute, and
the reference exponent/branch are numerically evaluated once per process.
No private checkout, network service, C++ compiler or plotting library is
needed to run the scientific code after installing the dependencies.

Saved-data plotting has separate pinned requirements:

```sh
python -m pip install -r requirements-plot.txt
python plot.py --results output/result.json --output figures
```

The renderer validates source and saved-array hashes and evaluates no Euler
or similarity ODE. Its six files are PNG/SVG/PDF for the main verification
figure and the gallery preview. Two-dimensional circles map the saved
radial shell means onto a meridional plane. They are **not Cartesian 2D
simulations**, and interpolation does not create additional spatial data.

## Recorded fixed-input result

The original Mac run passed 33 unit tests and all 55 numerical gates. The
three PDE refinements, including the similarity eigenvalue calculation,
took about 44.6 seconds; this is a platform-specific observation rather
than a runtime guarantee. Steps were 71, 142 and 285 for the three grids.

- Full-volume density relative L1: 0.02345, 0.01339, 0.007722.
- Full-volume pressure relative L1: 0.03277, 0.01743, 0.009477.
- Active-region density relative L1: 0.02414, 0.01378, 0.007948.
- Finest shock radius: 0.530273 versus reference 0.533989.
- Maximum scaled three-component discrete budget residual: 8.85e-16.
- Minimum raw internal energy: zero. Sound-only roundoff guards: zero.

Shock error in cells is **not monotonic**: 1.13, 2.27 and 2.54 cells. Its
absolute radius error is approximately 0.00665 on the first two grids and
0.00372 on the finest. Density Linf differences are 0.258/0.271/0.266 and
pressure Linf differences 0.492/0.494/0.466; these do not decrease
monotonically either. L1 improvement does not imply pointwise resolution
of the jump or convergence at the collapse singularity.

## Fixed physical scope

- Ideal gas gamma 1.4, spherical symmetry (three spatial dimensions).
- Radius `[0,0.75]`, with 128, 256 and 512 spherical shells.
- Similarity time `t=-1` to `t=-0.85`, well before collapse at zero.
- Shock normalization `Rs(-1)=0.6`, `Rs(t)=0.6*(-t)**alpha`.
- The nonlinear eigenvalue lambda is computed by pinned ExactPack;
  `alpha=1/lambda`, approximately 0.7171745012.
- Ahead of the inward shock, the inner gas is exactly density 1,
  velocity 0 and pressure 0. The outer initial domain already contains
  the shocked self-similar field, not the same cold uniform state.

The initial conserved state is integrated with 16-point Gauss quadrature
over spherical shell volume, splitting exactly at the analytic shock.
Order 32 qualifies both initial and final comparison means. Pressure
is computed **from the conserved mean** on both sides of the comparison.
It differs from a mean of pointwise primitive pressure in a shock cell.

## Actual finite-volume method and budgets

The spatial method is first-order HLL with shared face fluxes. Face areas
are `4*pi*r**2`, volumes are `4*pi*delta(r**3)/3`, and the radial-momentum
geometric source is `p_i*delta(area)/volume`. The center uses a reflected
ghost state with face area zero. The outer ghost state is evaluated from
the similarity field at **both actual Heun stage times**. CFL is 0.4 using
the spherical volume-to-face-area length.

The actual outer HLL flux and the geometric pressure source are integrated
with the same Heun weights as the state. Mass, radial momentum including
its source, and energy are checked separately. Radial momentum is not a
Cartesian globally conserved component and its source is not omitted.

There is no pressure/density floor, state repair or hidden retry. Every
stage must have positive density and finite conserved components. Cold
upstream pressure can be zero. A fixed **absolute internal-energy-density
cancellation band of 64 machine epsilons** (about 1.42e-14 in these fixed
nondimensional units) is permitted without changing the raw state or
raw pressure. The sound-speed square root alone treats negative values
within that band as zero. The number of such face/CFL evaluations and
their minimum raw pressure are stored separately from state repairs;
repeated evaluations of one cell count repeatedly. Larger negative
internal energy causes an explicit failure with raw state/context/history.

## Predetermined checks and limits

The main contract binds numerical sources, inputs and criteria before
the first primary test/PDE execution. The lightweight unit checks cover
independent physical/geometric identities and explicit failure paths.
The fixed calculations additionally check the moving strong-shock jump,
finite-difference Euler substitution of the smooth reference field,
quadrature, actual budgets and shock position from a pressure-gradient
peak inside the predetermined `[0.8 Rs,1.2 Rs]` window.

Volume-weighted density/pressure L1 errors are reported for the entire
sphere and for the predetermined `r >= 0.8 Rs` shock/nonzero-flow region.
The latter prevents a cold inner region from hiding active errors.
Maximum density/pressure errors and the sampled shock trajectory are
retained without asserting that each maximum must converge monotonically.
Three-grid slopes are finite-resolution diagnostics, not a proof of an
asymptotic order at a discontinuity.

No calculation reaches the singular collapse, follows a reflected shock,
changes gamma/geometry, or applies a nonradial perturbation. Success here
does not establish general robustness or multidimensional stability.
The reference is numerical ODE integration plus quadrature, not a
closed-form exact cell average. `references/qualification.json`
records separate pinned-original-code and reference qualification work.
