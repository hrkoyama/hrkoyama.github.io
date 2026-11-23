# Noh on an actual two-dimensional Cartesian grid

Original educational Euler code, edition 2026-11-23-r2, group noh-cartesian.
One case uses three small full-square grids:32x32,64x64,128x128. It is the
same physical Noh problem as the older radial examples, not a new physical
problem in the Atlas count. No old scientific distribution is replaced.

## Reproduce offline

Python 3.10+, then install requirements.txt (numpy/scipy/pytest pinned).

    python -m pip install -r requirements.txt
    python -m pytest -q
    python run.py --input inputs.json --output output

Use a new empty output directory. The run writes result.json, a small summary
CSV, compressed full 2D conserved fields and references (NPZ), and time histories.
Plotting saved arrays separately needs requirements-plotting.txt:

    python -m pip install -r requirements-plotting.txt
    python plot.py --results output/result.json --output figures

No network/private checkout/ChatGPT/API is required after dependency setup.

## Physical problem and method

Square[-.5,.5]^2, gamma=5/3,rho0=1,inward speed1,p0=0 exactly,T=.6.
Two momentum components and both Cartesian flux directions evolve without a
radial source, radial reduction, quadrant boundary or symmetry projection.
Initial conserved states are cell-center cold samples; these are not exact
initial momentum averages over a cell. All four outer boundaries impose the
cold supersonic physical inflow rho=1+t/r, velocity=(-x/r,-y/r). The numerical
algorithm is piecewise-constant Rusanov plus unsplit SSPRK2/Heun, CFL.35.
No pressure/state floor, seed, updated-cell repair or hidden retry is used.
Each predictor/update is checked. Invalid stages retain their raw state.

Cold outer face fluxes are integrated analytically along each Cartesian face.
They are affine in time, so Heun integrates their inflow exactly. For this full
square, M=4R^2+8Rt*asinh(1)+pi*t^2, Etotal=M/2. Discrete component budgets are
checked separately. This differs from the spherical radial boundary dt^3 bias.

## References and quadrature

For the cylindrical Noh state rho2=16,p2=16/3,shock radius=t/3; ahead,
rho=1+t/r. Density reference means integrate over Cartesian cells, splitting
at the shock circle and using x=rs*sin(theta) Gauss64 quadrature. Gauss128 and
the independent analytic total mass/area check the reference integration.
These are quadrature references, not closed-form exact cell means. Stored
physical pressure averages differ from pressure recovered from conserved means
inside a mixed shock cell. Density errors use all cells, including origin and
shock. Ray graphs label an analytic point profile separately.

The existing independently executed LANL ExactPack d=2 point snapshot is reused
(commit9bacc477eb791e959c9621e771fc7a725db755fa), away from the jump. No new
ExactPack execution or independent 2D PDE engine is claimed. See exactpack-reuse.json.
Noh(1987), JCP72,78-120, DOI10.1016/0021-9991(87)90074-X is the original
problem/heating-error source (publisher metadata/abstract checked; full paper
not accessed). Also cite Thrussell & Ferguson(2023), SoftwareX24,101560,
DOI10.1016/j.softx.2023.101560 and official https://github.com/lanl/ExactPack .
All evolution/reference integration here is original Atlas code; no ExactPack
source or third-party figure is copied into this package.

## Measured limits

Pre-run source/input/criteria hashes and archived source are retained. The first
attempt passed 19 tests and 49 gates on all three grids. Full density L1 decreases
.29608 -> .17955 -> .09981. Finest core L1=.12231, axis shock error=.968dx,
diagonal=1.469dx. Maximum relative discrete-budget residual~4.6e-15.
Center maximum internal-energy excess remains~14%. Axis/diagonal radius
difference=.501dx at 128² and is NOT monotone over these three grids. D4 parity
is a code symmetry check, not proof of continuous rotational invariance.
No general perturbation stability, shifted origin, rotated mesh, 3D Cartesian
or higher-order result is established. All maximum errors remain reported.

The unpublished first package omitted the public verifier completion flag. Revision r2 adds only the result envelope termination field and improves prose spacing. Pre-run-envelope-contract.json records the change; all numerical criteria, inputs, test functions and solver/reference code remain unchanged.
