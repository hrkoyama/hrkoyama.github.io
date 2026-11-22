# Particle mesh Ewald / PME

PME transfers the reciprocal Ewald calculation to a mesh and uses FFTs. Distinguish the original Lagrange-interpolation PME from the later B-spline construction of SPME.

## Problem and representative equations

For a neutral triply periodic Coulomb system, Qₘ is charge assigned to mesh point xₘ using weights Wₘ. The reciprocal operator Ĝₕ includes Ewald screening, mesh conventions and interpolation corrections. This schematic describes only the reciprocal contribution; real-space and self terms remain necessary.

$$
Q_{\mathbf m}=\sum_iq_iW_{\mathbf m}(\mathbf r_i),\qquad\phi_h=\mathcal F_h^{-1}\!\left[\widehat G_h\,\mathcal F_h Q\right].
$$

## Algorithm

Assign charges with local Lagrange polynomials, transform the mesh, apply the reciprocal convolution and transform back. Specify the differentiation and particle-gather rules together. A mesh-interpolated field and the derivative of the discrete energy need not give identical forces.

## Conditions and pitfalls

Separate mesh resolution, interpolation order, Ewald cutoffs and force differentiation in error studies. State FFT normalization, k=0 treatment and units. The usual O(N log N) description assumes an appropriate mesh-growth regime and is not an accuracy guarantee.

## What to check

Use a converged direct Ewald calculation for the identical neutral cell. Vary mesh size, interpolation order and screening; measure RMS/maximum energy and force errors and sensitivity to common translations. A gravity-PM test does not validate PME.

## Publication scope

Reading, representative equations and sources are published. Dedicated code and numerical verification remain planned. The suggested checks above are not measured results, and code/results of other methods are not presented as validation of this method.

## Sources

- Darden, Tom and York, Darrin and Pedersen, Lee (1993). Particle mesh Ewald: An N log(N) method for Ewald sums in large systems. https://doi.org/10.1063/1.464397
- Ewald, P. P. (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304
