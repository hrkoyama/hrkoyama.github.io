# Yee finite-difference time-domain method

Yee FDTD advances Maxwell curl equations on a lattice staggered in both space and time. It is a specific arrangement, not simply centered differences with electric and magnetic fields collocated.

## Problem and representative equations

In a linear isotropic nondispersive medium with constant ε and μ, c=1/√(εμ). Store E at integer times and B at half times, with H=B/μ. curlₕ denotes the discrete curl compatible with the chosen spatial placement; J is electric current density.

$$
\begin{aligned}\mathbf B^{n+1/2}&=\mathbf B^{n-1/2}-\Delta t\,\operatorname{curl}_h\mathbf E^n,\\\mathbf E^{n+1}&=\mathbf E^n+\frac{\Delta t}{\epsilon}\left(\operatorname{curl}_h\mathbf H^{n+1/2}-\mathbf J^{n+1/2}\right).\end{aligned}
$$

## Algorithm

Update magnetic flux from electric circulation, then advance E from magnetic circulation and current. Initialize fields and boundaries at their staggered times. The compatible divₕ curlₕ identity helps preserve a magnetic constraint; electric charge conservation also requires a compatible current update.

## Conditions and pitfalls

For the standard uniform Cartesian constant-medium scheme, cΔt√(Δx⁻²+Δy⁻²+Δz⁻²)≤1. Dispersive materials, absorption layers and conduction terms need their own analysis. Stability does not eliminate phase error or staircase geometry error, and a PML setting does not imply zero reflection.

## What to check

Compare periodic-wave phase speed and grid convergence, conducting-cavity frequencies and interface reflection/transmission with analytic results. Track energy balance, magnetic divergence and Gauss-law residuals separately. Similarities with MHD constrained transport do not make their equations identical.

## Publication scope

Reading, representative equations and sources are published. Dedicated code and numerical verification remain planned. The suggested checks above are not measured results, and code/results of other methods are not presented as validation of this method.

## Sources

- Kane Yee (1966). Numerical solution of initial boundary value problems involving maxwell's equations in isotropic media. https://doi.org/10.1109/tap.1966.1138693
