# Particle-in-cell / PIC

Plasma PIC represents a distribution by computational particles and self-consistent fields by a mesh. Its smoothing, collisionality and sampling error differ from direct all-pairs Coulomb dynamics.

## Problem and representative equations

Start with nonrelativistic electrostatic Vlasov–Poisson. Computational particle p has weight wₚ, charge qₚ and position xₚ. Dimensionless shape weights Sᵢ sum to one, and Vᵢ is cell volume. Deposit ρ, solve Poisson with the stated boundary conditions, and use E=−∇φ.

$$
\rho_i=\frac1{V_i}\sum_p w_pq_pS_i(\mathbf x_p),\qquad -\nabla_h^2\phi_i=\rho_i/\epsilon_0,\qquad \dot{\mathbf v}_p=(q_p/m_p)\mathbf E_h(\mathbf x_p).
$$

## Algorithm

Repeat charge deposition, field solution, particle gathering and particle pushing; include background ions in ρ. Electromagnetic PIC additionally needs current deposition and Maxwell updates consistent with discrete continuity. Dawson’s sheet model is a historical particle-plasma example, not the definition of every PIC discretization.

## Conditions and pitfalls

Explicit electrostatic PIC must examine plasma-frequency time scales and Debye-length resolution. Exact restrictions depend on the particle pusher, shape and field solver. Separate sampling convergence in particle count from grid/time convergence, and check self-force and finite-grid heating.

## What to check

Begin with single-particle self-force, a uniform neutral distribution, and small-amplitude plasma oscillations or Landau damping. Report charge, energy drift, particle-count dependence and independent random realizations. Compare damping rates only within the linear-amplitude regime used by the theory.

## Publication scope

Reading, representative equations and sources are published. Dedicated code and numerical verification remain planned. The suggested checks above are not measured results, and code/results of other methods are not presented as validation of this method.

## Sources

- John Dawson (1962). One-Dimensional Plasma Model. https://doi.org/10.1063/1.1706638
- Hockney, R. W. and Eastwood, J. W. (1981). Computer Simulation Using Particles. https://doi.org/10.1201/9780367806934
