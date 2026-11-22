# Biological model equations and numerical verification

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

## Equations

- [Logistic population growth](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-logistic-en>)

  Density-limited growth with carrying capacity K. It is the simplest biological ODE baseline. The linked original is the later 1847 memoir; the 1838 note itself was not audited. The differential equation is not the discrete logistic map. Scoped executed example: One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [SIR and SEIR compartment models](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-sir-en>)

  Closed, well-mixed normalized population fractions. SEIR adds an exposed compartment and a progression rate. The original general epidemic framework is broader than this SIR specialization. Population-count and fraction conventions give different β definitions. Scoped executed example: Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Logistic population growth](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-logistic-en>)

  Density-limited growth with carrying capacity K. It is the simplest biological ODE baseline. The linked original is the later 1847 memoir; the 1838 note itself was not audited. The differential equation is not the discrete logistic map. Scoped executed example: One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.
- [Michaelis–Menten and full enzyme kinetics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-enzyme-en>)

  Enzyme saturation; the full mass-action system resolves the transient complex C, while the rate law eliminates a fast variable. The 1913 rapid-equilibrium interpretation and the 1925 quasi-steady-state derivation must remain distinct. Literature-only.
- [Lotka–Volterra predator–prey](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-lotka-volterra-en>)

  Coupled prey growth and predation; a phase-plane and long-time integration test.  Literature-only.
- [McKendrick age-structured population](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-age-structure-en>)

  Individuals move through age a at unit speed; newborns enter through a nonlocal renewal boundary. This is the classical age-transport form; the later von Foerster lineage is acknowledged without treating its date as the first appearance. Literature-only.
- [SIR and SEIR compartment models](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-sir-en>)

  Closed, well-mixed normalized population fractions. SEIR adds an exposed compartment and a progression rate. The original general epidemic framework is broader than this SIR specialization. Population-count and fraction conventions give different β definitions. Scoped executed example: Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.
- [Fisher–KPP invasion front](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-fisher-kpp-en>)

  Spatial spread of an invading population or advantageous allele, represented by a reaction–diffusion front. Fisher–KPP is a conventional family name; the independent KPP 1937 original remains an archival follow-up. The exact special speed is not the minimal speed. Literature-only.
- [Monod growth and chemostat](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-monod-en>)

  Nutrient-limited biomass X, substrate S, yield Y and chemostat dilution d; d=0 gives a closed batch model. This writes one constant-yield extension of saturation growth, not a universal metabolic model. Literature-only.
- [Hodgkin–Huxley membrane dynamics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-hodgkin-huxley-en>)

  Voltage and gating variables z=m,h,n describe an ionic excitable membrane. A cable extension adds spatial axial current. The original squid-axon model is not a calibrated human cardiac model. No single rate parameter set is selected by this survey. Literature-only.
- [Turing reaction–diffusion framework](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-turing-en>)

  A framework for diffusion-driven pattern onset around a homogeneous reaction equilibrium, not a unique choice of f and g. A spot image or unequal diffusion coefficients alone do not establish a Turing mechanism. Boundary conditions determine the available modes. Scoped executed example: A 1D periodic Schnakenberg system of length 2pi, a=0.1, b=0.9 and diffusivities 0.01/1. Preserve the earlier linear-onset example and compare finite-amplitude nonlinear evolution and post-growth patterns from fixed reflection-symmetric data with independent Fourier–Galerkin/Radau references and separate spatial/temporal refinement. No general pattern selection, 2D, biological calibration or fluid-coupling claim.
- [FitzHugh–Nagumo excitation and recovery](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-fitzhugh-nagumo-en>)

  A normalized fast excitation/slow recovery model for pulses, refractoriness and spiral waves when extended in space. This is a common normalized variant; cubic coefficients, recovery signs and nondimensionalization differ between formulations. Scoped executed example: The executed case has D=0 and no spatial coordinate. Scoped verification of an FHN/BVP-style reduced ODE. It excludes full HH ion channels, spatial axons, patient data and experimental electrophysiology reproduction.
- [Keller–Segel chemotaxis](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-keller-segel-en>)

  Cell density n drifts up a chemoattractant gradient; τc=0 gives an elliptic chemical subproblem. This is a common two-field reduction of a more detailed original formulation. Blowup thresholds depend on dimension, domain, boundary and chemical dynamics. Literature-only.
- [Gierer–Meinhardt activator–inhibitor](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-gierer-meinhardt-en>)

  A representative simplified short-range activation/long-range inhibition model. Source densities, saturation and baseline production vary across the model family. This simplified formula is not a verbatim transcription of every original variant. Literature-only.
- [Fluid–elastic structure and immersed boundaries](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-immersed-boundary-en>)

  Fluid coupled to a deformable structure; biological examples include valves and membranes, once a force/constitutive law is supplied. Immersed boundary is a numerical coupling method, not itself a closed biological constitutive equation. The existing periodic MAC solver does not implement this coupling. Literature-only.
- [Chemical master equation and Gillespie SSA](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-chemical-master-en>)

  Integer molecule counts, reaction jumps νj and propensities aj; SSA samples paths of this continuous-time Markov model. The 1977 paper is a foundational SSA reference, not a priority claim for all master equations. SSA is a solver; the reaction network is the model. A seed documents a trajectory, not an ensemble validation. Literature-only.
- [Mackey–Glass delayed physiological feedback](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-mackey-glass-en>)

  Delayed feedback in a normalized physiological control model; delay can change stability and oscillatory behavior. A scalar initial value alone is insufficient. The delayed ODE is distinct from a spatial reaction–diffusion model. Literature-only.
- [Replicator evolutionary game dynamics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-replicator-en>)

  Strategy fractions reproduce according to relative payoff in a specified matrix game. No universal Lyapunov function or equivalence of fixed point and evolutionarily stable strategy is assumed. Literature-only.
- [Schnakenberg reaction–diffusion](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-schnakenberg-en>)

  A simple autocatalytic kinetic law extended in space, useful for reproducible Turing-onset tests. A mathematical chemical pattern model; matching a visual biological pattern does not calibrate it to a tissue. Scoped executed example: A 1D periodic Schnakenberg system of length 2pi, a=0.1, b=0.9 and diffusivities 0.01/1. Preserve the earlier linear-onset example and compare finite-amplitude nonlinear evolution and post-growth patterns from fixed reflection-symmetric data with independent Fourier–Galerkin/Radau references and separate spatial/temporal refinement. No general pattern selection, 2D, biological calibration or fluid-coupling claim.
- [Shigesada–Kawasaki–Teramoto cross-diffusion](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-skt-en>)

  Competition with density-dependent self- and cross-dispersal can produce spatial segregation. The displayed homogeneous-environment reduction omits the original environmental-potential terms. It is not equivalent to two independent scalar diffusion equations. Literature-only.
- [Gray–Scott spatial autocatalysis](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-gray-scott-en>)

  A chemical feed/decay model whose spatial extension supports diverse spot and wave patterns. 1983 is the well-mixed CSTR source; Pearson 1993 is the spatial pattern reference. Spot division does not by itself demonstrate cell division or a linear Turing instability. Literature-only.
- [Aliev–Panfilov cardiac excitation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-cardiac-en>)

  A reduced phenomenological excitation/recovery model for cardiac waves and restitution. Monodomain/bidomain tissue models add conductivity tensors and, for bidomain, an extracellular elliptic constraint. They are not automatically included by this two-variable model. Literature-only.
- [Repressilator mRNA–protein network](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-repressilator-en>)

  Three repressing genes form a cyclic network; retaining mRNA and protein gives six state variables. The six-variable form is distinct from a reduced three-protein oscillator; oscillations are parameter-dependent. Literature-only.
- [Genetic toggle switch](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-toggle-en>)

  Mutual repression produces a possible bistable genetic switch in a normalized model. Bistability is not guaranteed for arbitrary Hill exponents or production rates. Induction, mRNA dynamics and noise are additional model choices. Literature-only.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-logistic-growth-en>)

  One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-sir-epidemic-en>)

  Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.

## Problem figures

- [Logistic growth: analytic solution and time refinement](<https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/logistic-growth/preview.png
- [SIR: independent DOP853 reference, conservation and convergence](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/preview.png

## Exact / reference solutions

- [Logistic growth: analytic solution and time refinement — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=en#references-en>)

  Use the logistic analytic solution for the specified r, K and initial value and check time refinement. Validation uses its own fixed inputs outside the 18-case reference library.
- [SIR: independent DOP853 reference, conservation and convergence — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=en#references-en>)

  Check an independent DOP853 numerical reference for identical inputs, population conservation, nonnegativity and time refinement. This is not a general closed-form SIR solution.
- [Logistic growth: analytic solution and time refinement — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=en#logistic-growth-en-validation>)

  One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.
- [SIR: independent DOP853 reference, conservation and convergence — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=en#sir-epidemic-en-validation>)

  Separately implemented DOP853 with two-tolerance agreement; not an analytic solution.

## Code and validation

- [Logistic growth: analytic solution and time refinement](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=en>)
  availability: run

  One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.
- [SIR: independent DOP853 reference, conservation and convergence](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=en>)
  availability: run

  Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.
- [Logistic growth: analytic solution and time refinement — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
- [SIR: independent DOP853 reference, conservation and convergence — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
