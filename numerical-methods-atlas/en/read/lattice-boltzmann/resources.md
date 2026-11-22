# Lattice Boltzmann: collide, stream, recover fluid motion

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/lattice-boltzmann/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [D2Q9–BGK collision and streaming](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en>)
- [Guo forcing](<https://hrkoyama.github.io/numerical-methods-atlas/methods/guo/?lang=en>)
- [Half-way bounce-back](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bounce-back/?lang=en>)
- [D2Q9–BGK collision and streaming](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [D2Q9–BGK collision and streaming](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Guo forcing](<https://hrkoyama.github.io/numerical-methods-atlas/methods/guo/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Half-way bounce-back](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bounce-back/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

## Equations

- [Isothermal lattice BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en>)

  Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow. Lattice BGK is the computed model; incompressible Navier–Stokes supplies the low-Mach macroscopic decay comparison.
- [Incompressible Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en>)

  A representative constant-density, constant-viscosity form. Public examples use periodic 2D MAC projection and a Taylor–Green vortex. Lattice BGK is the computed model; incompressible Navier–Stokes supplies the low-Mach macroscopic decay comparison.
- [Isothermal lattice BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en>)

  Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow. Links the lattice-BGK/body-force/halfway-wall calculation to its macroscopic steady incompressible channel solution.
- [Incompressible Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en>)

  A representative constant-density, constant-viscosity form. Public examples use periodic 2D MAC projection and a Taylor–Green vortex. Links the lattice-BGK/body-force/halfway-wall calculation to its macroscopic steady incompressible channel solution.
- [Isothermal lattice BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en>)

  Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow.

## Problem figures

- [Viscous decay of a periodic shear wave](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/lbm-shear.png
- [Plane Poiseuille channel flow](<https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/channel-poiseuille.png

## Exact / reference solutions

- [Viscous decay of a periodic shear wave — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=en#references-en>)

  For a low-Mach periodic shear wave, infer viscosity from Fourier decay and check refinement. The heat reference card is a related scalar decay model.
- [Heat / Fourier-mode decay](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-heat-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Periodic unit interval; viscosity 0.02. Linear viscous shear decay and scalar heat modes have the same form, but LBM lattice units, wavenumber and viscosity differ from the card’s ν=0.02.
- [Plane Poiseuille channel flow — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en#references-en>)

  The analytic standard is the lattice-unit parabola with halfway bounce-back walls and Guo body forcing. The library unit-width channel with G=1 uses a different length and drive.
- [Viscous channel / Poiseuille](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poiseuille-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Fully developed planar steady channel, no slip, unit density; −dp/dx=G or body acceleration G. Both have parabolic profiles, but the computation uses lattice height ny and forcing for peak speed 0.01; the card uses unit width, G=1 and ν=0.1.

## Code and validation

- [D2Q9–BGK collision and streaming — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Guo forcing — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/guo/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Half-way bounce-back — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bounce-back/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Viscous decay of a periodic shear wave — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
- [Plane Poiseuille channel flow — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
