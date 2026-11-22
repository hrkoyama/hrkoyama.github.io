# Smooth particle mesh Ewald / SPME

SPME approximates Ewald structure factors using smooth cardinal B-splines. Treat it as a specific interpolation-and-force construction rather than a synonym for every PME implementation.

## Problem and representative equations

Let uᵢ be particle coordinates in mesh units and Mₚ a cardinal B-spline of order p, not degree p. The product below is the local tensor assignment in three dimensions. Fourier structure factors require a correction for the spline response.

$$
Q_{m_xm_ym_z}=\sum_iq_i\prod_{d\in\{x,y,z\}}M_p(u_{id}-m_d),\qquad \deg M_p=p-1.
$$

## Algorithm

Spread charge over p neighboring mesh points in each direction, evaluate a corrected reciprocal mesh energy by FFT, and obtain forces using derivatives of the assignment in analytical differentiation. Record the spline order and mesh together with whether differentiation is analytical or in Fourier space.

## Conditions and pitfalls

Smooth assignment alone does not guarantee both energy consistency and exact net-force cancellation. Ewald neutrality, boundary and self-term conventions still apply. Comparisons with original PME should control error tolerance and differentiation rules, not merely the number of mesh points.

## What to check

Measure force errors against the same converged Ewald reference and check energy finite differences. Report common-translation mesh effects and total force separately. Ensure real-space truncation is not hiding the reciprocal-space convergence trend.

## Publication scope

Reading, representative equations and sources are published. Dedicated code and numerical verification remain planned. The suggested checks above are not measured results, and code/results of other methods are not presented as validation of this method.

## Sources

- Essmann, Ulrich and Perera, Lalith and Berkowitz, Max L. and Darden, Tom and Lee, Hsing and Pedersen, Lee G. (1995). A smooth particle mesh Ewald method. https://doi.org/10.1063/1.470117
- Darden, Tom and York, Darrin and Pedersen, Lee (1993). Particle mesh Ewald: An N log(N) method for Ewald sums in large systems. https://doi.org/10.1063/1.464397
