# Preconditioning matrices, low Mach numbers, sonic points and entropy fixes

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/low-mach-preconditioning/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Acoustic Roe entropy correction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/entropy-fix/?lang=en>)
- [Low-Mach PDE preconditioning](<https://hrkoyama.github.io/numerical-methods-atlas/methods/low-mach-preconditioning/?lang=en>)

## Equations

No chapter-specific association is registered. Atlas-wide index: [Equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en)

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Low-Mach isentropic vortex: preconditioned Roe flux verification](<https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en>)
  availability: run

  The same nonlinear 2D Euler vortex is evolved to T=0.1 on N=16/32/64 at background Mach 0.1/0.01, comparing ordinary Roe with Miczek spatial flux preconditioning. Twelve fixed runs retain velocity and dynamically scaled pressure errors, conserved budgets, acoustic steps and actual stage states.
- [Acoustic Roe entropy correction — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/entropy-fix/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Low-Mach PDE preconditioning — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/low-mach-preconditioning/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
