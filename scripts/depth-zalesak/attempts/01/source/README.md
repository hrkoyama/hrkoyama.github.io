# Zalesak-type two-dimensional rotation

This standalone educational example evolves a slotted scalar disk with real
two-dimensional conservative finite volumes. It compares donor-cell and
directional-minmod MUSCL, both with SSPRK(3,3), on32²/64²/128² cells for one
full turn. Two64² MUSCL probes translate the rotation/body center by half a
cell and rotate the initial body by45 degrees. It is not an implementation of
Zalesak's flux-corrected-transport algorithm.

Use Python3.10 or newer. The public lightweight verifier deliberately requires
the three reviewed direct dependency pins in requirements.txt. Matplotlib is
optional and only needed for rendering already-saved fields.

```sh
python -m pip install -r requirements.txt
python -W error -m pytest -q -p no:cacheprovider
python -W error run.py --input inputs.json --output new-output
```

Use a new/empty output directory. `run.py` rejects any change to the scientific
files bound by `pre-run-contract.json`, including inputs and acceptance. To
develop a different method or input, create and label a new scientific edition
with a new contract instead of presenting modified results as this release.

The scientific protocol fixes26 tests, eight runs and158 numerical decisions
before execution; all pytest plus the runner share120 seconds in the public
verifier. The acceptance file is not adjusted after looking at output. Failed
states and the completed stage history are retained if an evolution fails.

## Physical and boundary definition

The unit square contains a unit-height disk centered at(.5,.75), radius.15,
with the lower-open slot x in(.475,.525), y<.85 removed. The rotation center
is(.5,.5), velocity is(.5-y,x-.5), angular speed1 and T=2pi. The shape/velocity
coordinates follow the official Firedrake demo's slotted-cylinder component.
This example isolates that0–1 component and uses periodic boundaries; it does
not reproduce the original1979 paper's grid/BC or the full Firedrake demo.

Opposing normal face velocities agree exactly and the discrete divergence
vanishes. The periodic extension has a tangential-velocity seam. The exact
compact body stays within radius.4 of the rotation center, away from that
seam. Numerical diffusion can reach it; the mass fraction in a fixed.05-wide
boundary band is reported instead of assuming it is zero.

## Conditional bound and conservation

Each interface has one upwind flux, shared by its two periodic neighbor cells.
Four face midpoint reconstructions average to the original cell mean. With
minmod all four faces stay in the neighboring range. An individual outgoing
face Courant no larger than1/4 makes the FE mean a convex combination with
nonnegative coefficients summing to one when the discrete divergence is zero.
The chosen value is.20. SSPRK(3,3) is a convex combination of these FE updates.

Every reconstructed face, FE candidate and SSP convex mean is checked against
the fixed[0,1] roundoff band5e-13. Raw values are retained. No transported
state clipping/floor, step rejection or retry exists. This limited condition
is not a theorem for arbitrary meshes, velocities or reconstruction families.

## Exact geometric reference and error meaning

`references/geometry.py` integrates the rigidly rotated indicator over each
cell using circle/convex-polygon areas. It does not evolve a PDE or rasterize
a picture. Its area, true first moments, quarter/full-turn mapping and fixed
cut cells are cross-checked with separately implemented vertical-slice SciPy
quadrature. Tiny geometric roundoff corrections are counted separately from
the absence of PDE-state clipping. See references/README.md and source-review
records for sources and the actual inspected scope.

The final and all intermediate quarter-turn references are conservative cell
means. The code checks errors and discrete centroids at the intermediate
times so that a wrong rotation direction or doubled angular speed cannot pass
solely because the body returns after an integer number of turns.

The slot probe area-weights piecewise-constant cell means over a fixed inner
rectangle. Even the exact cell projection gives a nonzero probe baseline on
coarse grids. The result stores that baseline, numerical value and excess
separately; these are not the exact continuum integral inside an empty slot.
Center/orientation probes are two finite diagnostics, not a universal
isotropy guarantee or a promise of perfect shape preservation.

## Saved output and optional figures

Each run saves a full2D field NPZ with final/initial/reference arrays, five
quarter-turn snapshots and their references. The stage NPZ stores all FE and
SSP min/max, mean preservation, mass residual and Courant measurements as a
numeric table with named columns. Arrays contain no pickle/object payloads.

```sh
python -m pip install -r requirements-plot.txt
python plot.py --results new-output/result.json --output new-output
```

The renderer validates hashes and reads saved arrays only. Its PNG/SVG/PDF
figures are scientific plots of actual2D computed fields. Original software
code is MIT; prose, figures, inputs/data and third-party material retain the
separate conditions described by LICENSE and the public licensing page.
