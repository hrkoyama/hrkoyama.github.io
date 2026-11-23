# Slab electrostatics and 2D-periodic Ewald

Interfaces often require periodicity in two directions and isolation in the normal direction. Elongating a triply periodic cell is not identical to evaluating the genuinely two-periodic Green function.

## Problem and representative equations

For a neutral cell of volume V, normal z and unit Coulomb prefactor, the Yeh–Berkowitz correction adds a dipole contribution to a specified three-periodic Ewald baseline. Its coordinate derivative gives the normal force correction. The formula assumes neutrality and a conducting-boundary 3D reference.

$$
M_z=\sum_iq_i z_i,\qquad \Delta E=\frac{2\pi}{V}M_z^2,\qquad \Delta F_{i,z}=-\frac{4\pi}{V}q_iM_z.
$$

## Algorithm

Place slabs in an elongated cell with vacuum, converge the 3D sums, and add the dipole correction. Increase the vacuum height to assess residual image interactions. At finite vacuum height, this is not a claim of exact equivalence to a fully two-periodic summation.

## Conditions and pitfalls

Charged slabs, other external dielectric conditions, electrodes and imposed fields require additional formulations. Keep self and k=0 conventions distinct from this correction. Neutral-cell M_z is invariant under an origin shift; net charge destroys that property.

## What to check

Use neutral charge pairs or a dipole layer and vary vacuum height independently of reciprocal/mesh cutoffs. Compare with an independent two-periodic reference when available, and finite-difference the energy for normal forces. Agreement with an uncorrected 3D calculation cannot establish zero slab error.

## Publication scope

Links lead to existing educational code and dated verification records. This reading/translation update changes no scientific code or historical measurements and does not claim reproduction of an entire paper.

## Sources

- In-Chul Yeh and Max L. Berkowitz (1999). Ewald summation for systems with slab geometry. https://doi.org/10.1063/1.479595
- Ewald, P. P. (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304
