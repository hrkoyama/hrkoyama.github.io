# Learn by field

Read the theory, derivations and worked examples by field, from foundations to related methods and verification.

## [Numerical foundations: a 19-chapter beginner course](https://hrkoyama.github.io/numerical-methods-atlas/learn/numerical-foundations/en/)

Matching English and Japanese Web/PDF courses with shared figures, small verified examples, and 38 review questions with answers.

## Foundations, error and time integration

Start with error and stability, then follow time integration and equations with constraints.

- [Differences, CFL, von Neumann analysis, and Lax](https://hrkoyama.github.io/numerical-methods-atlas/en/read/stability/)
- [A-stability, L-stability and error norms](https://hrkoyama.github.io/numerical-methods-atlas/en/read/accuracy-stability/)
- [Time integration and leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/)
- [Runge–Kutta families: stages, order, stability, and SSP](https://hrkoyama.github.io/numerical-methods-atlas/en/read/runge-kutta/)
- [Stiff integration: solve the stage, control the time error](https://hrkoyama.github.io/numerical-methods-atlas/en/read/stiff-integration/)
- [Operator splitting: Lie–Trotter and Strang](https://hrkoyama.github.io/numerical-methods-atlas/en/read/operator-splitting/)
- [Operator splitting: Lie–Trotter and Strang on the same reaction–diffusion problem](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-splitting/)
- [Symplectic integration: a canonical map, not an exact energy promise](https://hrkoyama.github.io/numerical-methods-atlas/en/read/symplectic/)
- [Differential-algebraic equations / DAE](https://hrkoyama.github.io/numerical-methods-atlas/en/read/dae/)

## Elliptic problems, linear algebra and approximation

Go from boundary-value problems and sparse solvers to eigenvalues, basis functions, interpolation and quadrature.

- [Diffusion, elliptic equations, boundary conditions, and iteration](https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/)
- [Nishikawa's hyperbolic diffusion: iterate a first-order system](https://hrkoyama.github.io/numerical-methods-atlas/en/read/hyperbolic-diffusion/)
- [Sparse and nonlinear systems: measure the actual residual](https://hrkoyama.github.io/numerical-methods-atlas/en/read/sparse-nonlinear/)
- [Algebraic multigrid / AMG](https://hrkoyama.github.io/numerical-methods-atlas/en/read/amg/)
- [QR, SVD and least squares](https://hrkoyama.github.io/numerical-methods-atlas/en/read/qr-svd/)
- [Krylov eigenvalue solvers](https://hrkoyama.github.io/numerical-methods-atlas/en/read/eigensolvers/)
- [Orthogonal polynomials and mesh basis functions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/basis-functions/)
- [Spline interpolation](https://hrkoyama.github.io/numerical-methods-atlas/en/read/splines/)
- [Gaussian and adaptive quadrature](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quadrature/)
- [Chebyshev approximation](https://hrkoyama.github.io/numerical-methods-atlas/en/read/chebyshev/)
- [Wavelets](https://hrkoyama.github.io/numerical-methods-atlas/en/read/wavelets/)
- [AMG, factorizations, eigenvalues and quadrature](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-foundations/)
- [Numerical foundations: conditioning, residuals, convergence and independent references](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-foundations-conditioning/)
- [MG/AMG for coefficient jumps and rotated anisotropy](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-coefficient-diffusion/)

## Differentiation, optimization and inverse problems

Distinguish derivatives of residuals and solutions, then connect objectives, observations and regularization.

- [Automatic differentiation: derivatives for numerical solvers](https://hrkoyama.github.io/numerical-methods-atlas/en/read/automatic-differentiation/)
- [Implicit differentiation and adjoints: Bratu parameter sensitivity](https://hrkoyama.github.io/numerical-methods-atlas/en/read/adjoint/)
- [Gradient and quasi-Newton optimization](https://hrkoyama.github.io/numerical-methods-atlas/en/read/optimization/)
- [Bratu inverse problem: estimate λ from synthetic observations with adjoint gradients](https://hrkoyama.github.io/numerical-methods-atlas/en/read/bratu-inverse/)
- [Multi-parameter Bratu inversion: regularization and identifiability](https://hrkoyama.github.io/numerical-methods-atlas/en/read/bratu-multi-inverse/)
- [PINNs and neural operators](https://hrkoyama.github.io/numerical-methods-atlas/en/read/pinn-operators/)

## Fluids, shocks and steady solvers

Read about reconstruction, limiting and shock robustness, followed by low-Mach conditions and steady iterations.

- [Euler reconstruction: PPM, characteristics, WENO-Z and AUSM](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reconstruction/)
- [Slope limiters: minmod, Superbee, MC, van Leer, and van Albada](https://hrkoyama.github.io/numerical-methods-atlas/en/read/limiters/)
- [Advanced limiters: TVB and positivity preservation](https://hrkoyama.github.io/numerical-methods-atlas/en/read/advanced-limiters/)
- [Euler double rarefaction: positivity at every stage](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-euler-positivity/)
- [Zalesak-type 2D rotation: conservation, bounds and shape error](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-zalesak/)
- [Level sets: moving interfaces and comparison with VOF](https://hrkoyama.github.io/numerical-methods-atlas/en/read/level-set/)
- [Level sets: 2D circle translation and rigid rotation](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-level-set/)
- [Rotated-hybrid Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/en/read/rotated-hybrid/)
- [Traced PPM, AUSM variants and curved bow shocks](https://hrkoyama.github.io/numerical-methods-atlas/en/read/shock-expansion/)
- [The carbuncle phenomenon](https://hrkoyama.github.io/numerical-methods-atlas/en/read/carbuncle/)
- [Double Mach Reflection](https://hrkoyama.github.io/numerical-methods-atlas/en/read/double-mach/)
- [Double Mach reflection: lightweight grid verification](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-double-mach/)
- [KEEP schemes: preserve the smooth-flow balance, test the limits](https://hrkoyama.github.io/numerical-methods-atlas/en/read/keep/)
- [Preconditioning, dual time stepping, and residual distribution](https://hrkoyama.github.io/numerical-methods-atlas/en/read/advanced/)
- [Preconditioning matrices, low Mach numbers, sonic points and entropy fixes](https://hrkoyama.github.io/numerical-methods-atlas/en/read/low-mach-preconditioning/)
- [Low-Mach isentropic vortex: preconditioned Roe flux verification](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-low-mach/)
- [Damping Runge–Kutta iterations for steady solutions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/steady-runge-kutta/)
- [NASA 2D verification and validation case catalog](https://hrkoyama.github.io/numerical-methods-atlas/en/read/nasa-2d/)
- [Mach-3 forward-facing step: lightweight 2D verification](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-forward-step/)
- [Noh shocks: exact reference, origin heating and refinement](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-noh/)
- [Noh:2D Cartesian flow and grid orientation error](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-noh-cartesian/)
- [Sedov–Taylor point blast: lightweight spherical-radial validation](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-sedov/)
- [Guderley converging shock: lightweight spherical-radial verification](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-guderley/)
- [WENO critical points and epsilon dependence](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-weno-critical/)
- [KH/RT initial growth and independent linear references](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-instability-growth/)
- [Independent MHD transport, waves and compression comparisons](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mhd-transport/)
- [SRHD collision and nonlinear SRMHD Alfven wave](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-relativistic/)

## Meshes, finite elements and coupled equations

Organize spatial discretization and coordinates, then examine incompressible flow, MHD and relativistic systems.

- [Structured, unstructured, and triangular meshes](https://hrkoyama.github.io/numerical-methods-atlas/en/read/meshes/)
- [Continuous finite elements: from weak form to sparse assembly](https://hrkoyama.github.io/numerical-methods-atlas/en/read/fem/)
- [Spectral elements: high-order finite elements and 2D Poisson](https://hrkoyama.github.io/numerical-methods-atlas/en/read/spectral-element/)
- [Flux reconstruction: flux correction, DG and 1D periodic advection](https://hrkoyama.github.io/numerical-methods-atlas/en/read/flux-reconstruction/)
- [Spectral elements and FR: small comparisons with existing FEM/DG](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-sem-fr/)
- [Arbitrary Lagrangian–Eulerian methods](https://hrkoyama.github.io/numerical-methods-atlas/en/read/ale/)
- [Polar and cylindrical coordinates: tensors and viscosity](https://hrkoyama.github.io/numerical-methods-atlas/en/read/coordinates-viscosity/)
- [Spherical meshes and Arakawa A, B and C grids](https://hrkoyama.github.io/numerical-methods-atlas/en/read/geophysical-grids/)
- [CIP: carry the value and the gradient](https://hrkoyama.github.io/numerical-methods-atlas/en/read/cip/)
- [Incompressible flow: project with compatible discrete operators](https://hrkoyama.github.io/numerical-methods-atlas/en/read/incompressible/)
- [MHD: constrained transport and divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/en/read/mhd/)
- [Relativistic hydrodynamics: SRHD, GRHD, and GRMHD](https://hrkoyama.github.io/numerical-methods-atlas/en/read/relativistic-hydrodynamics/)
- [Independent fluid/MHD comparisons and CT/GLM](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mhd/)
- [CT and GLM: matched controls, independent checks and grid/time convergence](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mhd-convergence/)
- [Shallow water: topography, lakes and dry beds](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-shallow-water/)
- [Nonperiodic walls: cavity and manufactured flow](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-wall-flow/)
- [Corner singularities, curved coordinates and Neumann/Robin boundaries](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mesh-boundary/)
- [Nonuniform ALE transport and2D rotating shallow-water waves](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-moving-waves/)

## Particles, kinetic methods and transport

Explore particle methods, distribution functions, long-range forces and transport equations.

- [Particle methods and smoothed particle hydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/en/read/particles-sph/)
- [Godunov smoothed particle hydrodynamics (GSPH)](https://hrkoyama.github.io/numerical-methods-atlas/en/read/gsph/)
- [Lattice Boltzmann: collide, stream, recover fluid motion](https://hrkoyama.github.io/numerical-methods-atlas/en/read/lattice-boltzmann/)
- [Chapman–Enskog expansion: from populations to transport](https://hrkoyama.github.io/numerical-methods-atlas/en/read/chapman-enskog/)
- [DSMC and kinetic transport](https://hrkoyama.github.io/numerical-methods-atlas/en/read/dsmc/)
- [Particle gravity: PM, P³M, Tree, multipoles, and multigrid](https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/)
- [Gravity kernels: isolated FFTs and a periodic slab](https://hrkoyama.github.io/numerical-methods-atlas/en/read/gravity-boundaries/)
- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/en/read/radiation-transport/)
- [Particles, electrostatics, kinetic and radiative transport](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-particles/)
- [Particles and transport: independent references, conservation and statistical error](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-particle-transport/)
- [3D1/r kernels: expansions,trees and force checks](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-fmm3d/)
- [Gravitational trajectories: Kepler and softened finite particles](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-gravity-dynamics/)
- [Warm PIC: Landau damping and two-stream instability](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-warm-pic/)
- [PIC checks against independent spatial kernels](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-pic-spatial/)
- [Finite-Knudsen Couette and Fourier flows](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-dsmc-wall/)
- [Mach2 planar shock with hard-sphere DSMC](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-dsmc-shock/)
- [LBM lid-driven cavity at Re100](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-lbm-cavity/)
- [LBM Taylor–Green vortex and finite-Mach errors](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-lbm-taylor-green/)
- [Annular Couette control for curved-wall LBM](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-lbm-annulus/)
- [LBM curved walls and a Re20 cylinder](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-lbm-curved-boundary/)
- [Isotropically scattering slabs and continuum-angle references](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-scattering/)
- [Non-equilibrium radiation: distinct diffusion and transport](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-matter/)
- [2D shadows,beams and M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-geometry/)

## Electromagnetic fields, electrostatics and electronic structure

Follow periodic electrostatics and electromagnetic fields, then atomic, molecular and periodic electronic-structure approximations.

- [Ewald summation](https://hrkoyama.github.io/numerical-methods-atlas/en/read/ewald/)
- [Particle mesh Ewald / PME](https://hrkoyama.github.io/numerical-methods-atlas/en/read/pme/)
- [Smooth particle mesh Ewald / SPME](https://hrkoyama.github.io/numerical-methods-atlas/en/read/spme/)
- [Slab electrostatics and 2D-periodic Ewald](https://hrkoyama.github.io/numerical-methods-atlas/en/read/slab-ewald/)
- [Yee FDTD: foundations and verified examples](https://hrkoyama.github.io/numerical-methods-atlas/en/read/fdtd/)
- [Particle-in-cell / PIC](https://hrkoyama.github.io/numerical-methods-atlas/en/read/pic/)
- [Quantum chemistry and DFT: approximations and equations](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/)
- [Hydrogenic atoms and helium: runnable validation examples](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-atoms/)
- [Closed-shell HF for H₂: independent references, SCF residuals and basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/en/read/h2-hf/)
- [Periodic DFT: Γ points, k-point integration, basis sets, SCF and an independent reference](https://hrkoyama.github.io/numerical-methods-atlas/en/read/periodic-dft/)
- [From DFT to atomic forces: finite differences, independent references, force convergence and the BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/en/read/periodic-forces/)
- [Neutral slabs: corrected3P and genuine2P references](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-slab-ewald/)

## Stochastic computation, biology and temperature control

Compare stochastic error, population models and temperature control through their respective verification quantities.

- [Monte Carlo integration](https://hrkoyama.github.io/numerical-methods-atlas/en/read/monte-carlo/)
- [Markov-chain Monte Carlo / MCMC](https://hrkoyama.github.io/numerical-methods-atlas/en/read/mcmc/)
- [Multimodal MCMC: independent checks of poor mixing and convergence diagnostics](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mcmc/)
- [Stochastic differential equations](https://hrkoyama.github.io/numerical-methods-atlas/en/read/sde/)
- [Biological model equations and numerical verification](https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/)
- [Independent validation of nonlinear reaction–diffusion and pattern formation](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology/)
- [Thermostats: temperature control and distributions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/thermostats/)
- [MCMC, temperature control and biological models](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-models/)
- [CSVR and Langevin: distributions, fluctuations and correlations](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-thermostats/)
- [Weak/strong SDE errors and sampling uncertainty](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-stochastic-accuracy/)
- [Importance sampling and correlated-Gaussian diagnostics](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-stochastic-estimation/)

## Verification problems and experiment guides

Choose equations and references, and distinguish exhibits, saved results and runnable examples.

- [Equation gallery: choose the equation before the algorithm](https://hrkoyama.github.io/numerical-methods-atlas/en/read/equation-gallery/)
- [Benchmark library](https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/)
- [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)
- [Interactive experiment guide](https://hrkoyama.github.io/numerical-methods-atlas/en/read/experiments/)
- [Time-dependent tests: movies and saved states](https://hrkoyama.github.io/numerical-methods-atlas/en/read/movies/)

## History, references and development records

Trace numerical methods and their sources, then consult textbooks, coverage and development records.

- [Historical atlas](https://hrkoyama.github.io/numerical-methods-atlas/en/read/history/)
- [References by original publication year](https://hrkoyama.github.io/numerical-methods-atlas/en/read/references/)
- [Textbooks: where to look next](https://hrkoyama.github.io/numerical-methods-atlas/en/read/textbooks/)
- [Remembering Philip L. Roe](https://hrkoyama.github.io/numerical-methods-atlas/en/read/roe-memorial/)
- [Site coverage and counting rules](https://hrkoyama.github.io/numerical-methods-atlas/en/read/site-coverage/)
- [Implementation roadmap](https://hrkoyama.github.io/numerical-methods-atlas/en/read/roadmap/)
- [v0.1.0 — First edition](https://hrkoyama.github.io/numerical-methods-atlas/en/read/release-notes-v0.1.0/)

