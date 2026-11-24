# Damping Runge–Kutta iterations for steady solutions

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/steady-runge-kutta/

Resources explicitly registered to the methods, problems and executions of this chapter. Reading on Jameson-family steady multistage RK iterations. The existing detailed-chapter catalog's related_methods links identify related method definitions only. Existing classical RK4, dual-time, low-Mach preconditioning and multigrid examples do not implement or validate a complete Jameson-type compressible solver. No dedicated solver, fixed-input execution or new measured result is added for this chapter.

## Methods

- [Jameson-type steady multistage Runge–Kutta](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jameson-steady-rk/?lang=en>)
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)
- [Dual time stepping](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dual-time/?lang=en>)
- [Low-Mach PDE preconditioning](<https://hrkoyama.github.io/numerical-methods-atlas/methods/low-mach-preconditioning/?lang=en>)
- [Geometric multigrid V-cycle](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en>)

## Equations

No chapter-specific association is registered. Atlas-wide index: [Equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en)

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Real-space mode damping with steady multistage RK](<https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=en>)
  availability: run

  Apply four steady residual stages on a periodic grid, separating damping, neutrality and amplification of discrete modes. The retained first run missed the original absolute residual goal in the expanding control.
- [Jameson-type steady multistage Runge–Kutta — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jameson-steady-rk/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
