The production and reference use Coulomb1/r, not the1/(4pi r) PDE fundamental solution.
Production3P uses V=Lx Ly Lz and the full nonzero reciprocal lattice:
Erec=(2pi/V) sum exp(-k²/(4alpha²)) |rho_k|²/k²,
Eself=-alpha/sqrt(pi) sum(q²). Real sums exclude only self/zero image.
The neutral YB energy is+2pi Mz²/V and its force is-4pi qi Mz/V.
Mz is evaluated using physical, unwrapped z. The lateral box is1 by1.25.

The independent2P evaluator has only x/y image translations. Its full-lattice
nonzero-mode potential has prefactor pi/A multiplying
sum_j,k qj cos(k.rhoij)[exp(kz)erfc(k/(2alpha)+alpha z)
+exp(-kz)erfc(k/(2alpha)-alpha z)]/k.
Let B(z)=z erf(alpha z)+exp(-alpha²z²)/(alpha sqrt(pi)).
The zero-mode potential is-2pi/A sum_j qj B(zij), including j=i;
its vertical electric field is+2pi/A sum_j qj erf(alpha zij).
The potential self subtraction is-2alpha qi/sqrt(pi), separate from zero mode.
Particle forces equal qi times the electric field; total energy=.5sum(qi phi_i).
At plus/minus infinity the selected gauge is plus/minus2pi Mz/A.
This convention is from Lindbo--Tornberg Eq4/AppendixA, not a3P extrapolation.

In the two erfc terms, Gaussian derivative contributions cancel in dH/dz,
leaving k(Aplus-Aminus). Screened products use erfcx for nonnegative
arguments and the non-growing original exponential for negative arguments.
This avoids overflow without suppressing warnings. All implementations are
original code, with scalar-reference versus vector-production accumulation.
Selected-source access depths, including the unavailable original Yeh paper,
remain explicit in source-review.json. No external package was executed.
