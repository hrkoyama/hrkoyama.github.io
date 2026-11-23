# Spectral elements and flux reconstruction: two small reproducible examples

Run the complete two-case fixed input in a new/empty output directory:

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

The runtime dependencies are only the three reviewed pins. Matplotlib is optional:
install `requirements-plotting.txt` and run
`python plot.py --results output/result.json --output output` to redraw saved data.
Plotting never executes a PDE solver. Both examples are dimensionless and bounded
by a 90-second runner budget; the public independent verification also limits each
group's tests plus execution. These are small educational implementations.

## SEM: 2D Poisson and the existing triangle P1 FEM

Solve `-Delta u=2 pi^2 sin(pi x)sin(pi y)` on the unit square, with zero Dirichlet
data and exact `u=sin(pi x)sin(pi y)`. Continuous tensor-product Qp Lagrange
elements use Legendre Gauss-Lobatto nodes and GLL stiffness/load quadrature.
The sparse assembled system is solved with SciPy. The diagonal GLL quadrature
mass is not the exactly integrated mass for every polynomial product.

At p=2, refine 2/4/8 square elements per axis. Compare the unmodified published
P1 triangle FEM at 4/8/16 subdivisions: 9/49/225 free unknowns respectively are
matched across the methods, but element type, quadrature and algebraic solver
differ. This is an error/space comparison, not a runtime or universal superiority
benchmark. Separately fix 2x2 elements and vary p=1..6. Continuous L2 and H1
seminorm errors are integrated with higher-order Gauss points, not merely sampled
at the GLL nodes. Save the actual 2D SEM field and P1 nodes/triangles/field in NPZ.

## FR: 1D periodic advection and the existing modal DG

Solve `u_t+u_x=0` on [0,1), with initial `0.4+sin(2 pi x)` and T=0.25. Use p=1/2,
8/16/32 cells, Gauss solution points, upwind interface flux and Radau corrections.
The corrections recover DG for this constant linear flux on affine intervals.
SSPRK(3,3), the initial L2 projection rule and timestep policy match the unchanged
published modal Legendre DG, which is actually executed for every configuration.
The schemes' final polynomials are compared at the same Gauss points.

Continuous errors use additional Gauss points. Each RK stage's weighted mass and
each completed step's quadratic energy are checked. A matrix exponential of the
same FR spatial operator measures the RK3 time error separately; it is a distinct
time propagator, not an independent spatial PDE implementation. Courant halving
checks that time error. The main h/dt refinement alone is a coupled observed order.
No limiter, shock, nonlinear flux, arbitrary correction family or multidimensional
FR verification is included. All initial/final/reference nodal arrays, histories,
CSV, input hashes, decisions and baseline provenance are retained.

## Related production implementations

- PyFR: https://www.pyfr.org/ — FR-based flow software.
- Nek5000: https://nek5000.github.io/NekDoc/theory.html — spectral-element methods.
- nekRS: https://github.com/Nek5000/nekRS — CPU/GPU spectral-element flow solver.

These are related implementations described from their official documentation;
none is installed, invoked, benchmarked or certified by this distribution.
The seven files under `legacy/` are byte-identical original code from the atlas's
published Numart 2026-11-22 edition. `baseline-provenance.json` gives every public
source URL and hash. Only the named P1 FEM and scalar modal-DG paths are exercised;
the other dependency functions are not newly validated here.

Original code is MIT. Text, figures, inputs, numerical data and third-party material
retain the separate terms stated in LICENSE and the site's LICENSING.md.
