# Small two-dimensional level-set examples

Python3.10+; pinned NumPy/SciPy/pytest. No network or private checkout at runtime.
Use the complete fixed input and a new or empty output directory:

```sh
python -m pip install -r requirements.txt
python -W error -m pytest -q
python -W error run.py --input inputs.json --output output
```

Two nondimensional circle motions on [0,1]^2, radius0.15 and T=1: translation
with velocity(0.2,0.1), and off-center rigid rotation with angular speed2pi.
The phi<0 region is the interior. These are prescribed kinematics, not a fluid
calculation. Both modes use the SAME ENO2 one-sided derivatives and Heun RK2,
32/64/128 square cell-centered grids and |u|+|v| Courant number<=0.35.
Analytic exterior ghost values are imposed at every stage; interior values
are always numerically advanced. The unbounded-plane circle remains away
from the square boundary, whose data are explicitly prescribed.

Compare advection alone with ten calls to first-order Godunov redistancing,
every0.1 physical time unit, five pseudo-steps per call with dtau=0.3dx.
The smoothed sign is frozen at each call. This is a deliberately simple
redistancing example, not the constrained interface-preserving algorithm of
Sussman/Fatemi. No zero-contour projection, volume correction, state clipping,
adaptive retry, analytic interior reset or VOF algorithm is present.

At t=0,.25,.5,.75,1 record linearly interpolated grid-edge zero crossings,
their radial errors relative to the exact moving circle, and negative area
from an explicitly defined piecewise-linear triangulation. Radial samples
are NOT a Hausdorff distance. Compare geometric area with pi*r^2, retaining
the initial geometric sampling bias; phi itself is not a conserved fraction.
Distance quality is RMS(|grad(phi)|-1) in the band |phi_exact|<=2dx.
The reference is analytic rigid center motion, not an independently executed
PDE engine. Heun CFL-halving atN64 is a separate sensitivity check; refinement
of dx and dt together is not a pure spatial-order measurement. Redistancing
has no guaranteed improvement in area or interface accuracy.

Each case writes a CSV and a compressed NPZ containing full128x128 fields.
result.json contains every observation, sampled contour, individual
redistancing area jump, actual step/call count, checks and input hash.
The numerical run has a90-second cap; nonfinite/unbounded fields, lost
interfaces, invalid input or a pre-existing nonempty output fail explicitly.
An unsuccessful numerical acceptance returns exit1; input/runtime failure2.

Optional plots use saved fields only:

```sh
python -m pip install -r requirements-plotting.txt
python plot.py --results output/result.json --output output
```

VOF is discussed in the accompanying reading as an interface-volume-fraction
formulation; this release does not implement or benchmark VOF. It validates
neither topology-changing flow nor surface tension/curvature dynamics.
