# Analytic reference and independent small-matrix oracle

These files contain new reference evaluators written for this example. They do
not import the primary flux or Numart operators, execute a third-party PDE engine,
or reuse an independently computed Euler trajectory. The cited papers remain
under their respective copyright; no paper PDF or third-party source is bundled.

`analytic_vortex.py` evaluates a translating, whole-plane isentropic Euler vortex.
The background velocity is `(1,.5)`, beta is3, gamma is1.4 and the box length is20.
The background density is1 and

```
p_inf = (1^2+.5^2)/(gamma*M_inf^2)
a = beta/(2*pi) * exp((1-X^2-Y^2)/2)
theta = 1 - (gamma-1)*beta^2/(8*gamma*pi^2*p_inf)*exp(1-X^2-Y^2)
rho = theta^(1/(gamma-1)); p = p_inf*theta^(gamma/(gamma-1))
u = 1-a*Y; v = .5+a*X
```

`M_inf` is the background Mach number, not the maximum local Mach number of the
swirling flow. At `p_inf=1`, the formula recovers the historical KEEP vortex.
Changing the background pressure alone while retaining its old density field
would not give this family of exact solutions.

The field uses minimum-image coordinates on the finite periodic box. The
continuous, translating field is a whole-plane solution; its nonzero Gaussian
tails mean this is not a globally exact smooth periodic nonlinear solution.
The box and short time reduce that qualification; they do not remove it.
Spiegel, Huynh and DeBonis discuss finite-periodic vortex interactions and shear
layers. No long-time or full-period validation is inferred here.

Tensor Gauss quadrature yields cell means of all four **conserved** variables.
Order8 and16 are compared. The resulting velocity and pressure are obtained by
converting the mean conserved state, which differs from averaging primitive
velocity or pressure. `analytic_euler_residual` uses hand-derived point gradients
and the physical flux equations; `analytic_local_balance` exposes the radial
centripetal/pressure balance. `conserved_time_derivative` and
`cell_means_time_derivative` give the physical translation derivative, allowing a
true initial truncation residual against the finite-volume operator. They do not
pretend that a translating vortex is a steady numerical solve.

`miczek_matrix.py` is a direct matrix-assembly/eigendecomposition oracle for a few
fixed diagnostic states. It is separate from the primary closed-polynomial
diffusion action. It assembles the physical primitive Euler Jacobian `A` and the
Miczek modifying matrix `P`, then computes `D=P^-1 |P A|`. Exact primitive to
conservative Jacobians provide the corresponding conservative matrices.

The papers distinguish the pressure-rescaling reference Mach parameter from the
actual flow Mach number. Here standard Euler fluxes have no explicit `1/M_r^2`
pressure factor, so their formulas are expressed with `M_r=1`; low Mach enters
through the actual pressure and sound speed. This does not set `M_inf=1`.
The modifying parameter is
`delta=1/mu-1`, `mu=min(1,max(local_speed/sound_speed,M_cut))`.

Miczek etal(2015), Section8 Eq56, and Barsukow etal(2017), Section3 Eqs21/32,
provide the matrix and its place in the numerical diffusion. Physical-time Euler
equations and the central physical flux are retained. This is spatial flux
preconditioning, not a pseudo-time PDE solver or an acceleration result for an
inner nonlinear solve.

Barsukow etal's Section5 explicitly warns that forward Euler has a more
restrictive low-Mach stability condition. The selected SSPRK(3,3) integrator is
checked using the stated full two-dimensional Fourier amplification matrices and
actual admissible stage states. A finite sampled linear diagnostic is not a
general nonlinear stability proof. The name SSPRK does not imply that this flux
is TVD/SSP: the SSP theorem assumes a suitable forward-Euler strong-stability
property, as stated by Gottlieb, Shu and Tadmor(2001).

`energy_scaling` defines the diagnostic norm explicitly by mapping conservative
perturbations to pressure/sound, velocity and entropy perturbations. Its power
norm checks do not measure enormous background internal-energy units as velocity
errors, and they do not prove bounds for arbitrary nonlinear solutions.

`definition.json` records the mathematical field and qualifications;
`citations.json` records source roles and exactly what was checked. Code is MIT
under `REFERENCE-LICENSE.txt`.
