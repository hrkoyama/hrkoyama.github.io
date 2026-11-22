# Radiation transport and moment methods

Radiation transport resolves intensity in space, direction and frequency. Moment methods reduce the angular dimension but require closure for information removed by integration.

## Problem and representative equations

Use frequency-integrated grey intensity I in a static medium, with isotropic emissivity η and absorption coefficient κ of inverse-length units; omit scattering here. Define E=(1/c)∫I dΩ, F=∫nI dΩ and P=(1/c)∫nnI dΩ. Moment equations for E and F require a prescription for P.

$$
\frac1c\partial_t I+\mathbf n\cdot\nabla I=\eta-\kappa I,\qquad\partial_t E+\nabla\cdot\mathbf F=4\pi\eta-c\kappa E,\qquad c^{-2}\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa\mathbf F/c.
$$

## Algorithm

Discrete ordinates discretizes angle directly; moment methods close P=D E. M1 obtains D locally from E and F, while flux-limited diffusion instead approximates F from the gradient of E. Check optically thick and free-streaming limits and couple matter exchange through a consistent energy balance.

## Conditions and pitfalls

M1 generally cannot propagate crossing beams independently. FLD ties flux to the energy gradient, limiting shadows and strongly anisotropic fields. A reduced light speed changes transport/relaxation scales and must be justified against the physical time scales of interest.

## What to check

Test exponential absorption, isotropic diffusion, free streaming/shadows and crossing beams separately. Check E≥0, |F|≤cE, matter-plus-radiation energy and angular/spatial/time convergence. Distinguish closure error from discretization error.

## Publication scope

Reading, representative equations and sources are published. Dedicated code and numerical verification remain planned. The suggested checks above are not measured results, and code/results of other methods are not presented as validation of this method.

## Sources

- C.D. Levermore (1984). Relating Eddington factors to flux limiters. https://doi.org/10.1016/0022-4073(84)90112-2
