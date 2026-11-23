# Reference scope and independence

The references implement exact formulas independently of `relativistic.py`.
`tensor_state` constructs the four-dimensional stress-energy tensor rather than
copying the production three-vector flux. Units are c=1 and 4π=1; Minkowski
signature is (−,+,+,+). Total energy E includes rest-mass energy.

For the restricted symmetric collision, the upstream states have identical
thermodynamics and opposite normal velocities. The downstream gas is at rest.
Rezzolla–Zanotti (2001) §3 equation3.1 gives the invariant relative shock velocity;
§4 equation4.5 gives the positive-root Taub enthalpy quadratic. A scalar pressure
root, Taub mass flux and downstream-rest-frame shock speed yield two moving
discontinuities. Exact cell overlaps provide conserved cell means, including cut
cells. This is not a general exact relativistic Riemann solver or a reproduction
of the numerical inputs of Martí–Müller (1994).

For the nonlinear circularly polarized Alfvén wave, Del Zanna et al. (2007) §4.1
equations82–85 give the speed and primitive fields. We use their physical
normalization rho=p=B0=eta=1 and gamma=4/3, but map the original length2π to a unit
period. One numerical crossing time is 1/vA. D, Sx and E are constant; transverse
momentum and induction fields are exact sinusoidal cell integrals. The primitive
recovery of a conserved cell average need not equal the average primitive field.
All evolution errors therefore compare conserved averages.

Before the six runs, `qualify` checks the Taub adiabat, prescribed relative
velocity, tensor Rankine–Hugoniot jump, nonlinear dispersion, independent
12-point Gauss integration of tensor-based means, and complex-step differentiation
of the full tensor conservation law at non-grid coordinates. Separate tests and
the actual collision outputs compare the B→0 production solver with an independent
scalar-pressure SRHD recovery and flux.

`source-review.json` records precisely which primary-source portions were read.
The original ECHO preprint pages9–10 were rendered and visually inspected; the
original journal version §4.1 was also read through the university repository.
No third-party paper PDF is redistributed. Font (2008) equations68–69 were read
for the recovery identities, not for a claim of a complete GRMHD implementation.
