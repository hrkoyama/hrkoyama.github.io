# Neutral slabs: corrected3P and genuine2P references

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-slab-ewald/

Resources explicitly registered to the methods, problems and executions of this chapter. Freeze rectangular boxes and the nonperiodic-z branch; compare the Yeh–Berkowitz correction with a genuine2P reference including self and zero modes.

## Methods

- [Ewald summation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=en>)

  Full±3D reciprocal sum/self term and2pi Mz²/V correction; independent2P retains zero/self terms and stable exp-erfc evaluation.
- [Slab electrostatics and 2D-periodic Ewald](<https://hrkoyama.github.io/numerical-methods-atlas/methods/slab-ewald/?lang=en>)

  Full±3D reciprocal sum/self term and2pi Mz²/V correction; independent2P retains zero/self terms and stable exp-erfc evaluation.
- [Ewald summation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=en>)
- [Slab electrostatics and 2D-periodic Ewald](<https://hrkoyama.github.io/numerical-methods-atlas/methods/slab-ewald/?lang=en>)

## Equations

- [Coulomb electrostatics with mixed periodic boundaries](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#coulomb-electrostatics-en>)

  Neutral system,Coulomb constant1. Distinguish genuine2P references from finite-vacuum3P plus correction. Coulomb1, lateral1×1.25, extendedLz1.5/3/6,4neutral charges±1,physical-z dipole.34 andalpha3/4.
- [Coulomb electrostatics with mixed periodic boundaries](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#coulomb-electrostatics-en>)

  Neutral system,Coulomb constant1. Distinguish genuine2P references from finite-vacuum3P plus correction.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en#neutral-slab-yb-en-algorithm>)

  Full±3D reciprocal sum/self term and2pi Mz²/V correction; independent2P retains zero/self terms and stable exp-erfc evaluation.

## Problem figures

- [Neutral rectangular slab: genuine2P reference and YB](<https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb-preview.png
- [Neutral rectangular slab: genuine2P reference and YB](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb.png

## Exact / reference solutions

- [Neutral rectangular slab: genuine2P reference and YB — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=en#references-en>)

  Separate reference cutoff/splitting qualification, energy gradients, vacuum error, all forces, zero-mode control/far gauge and neutral translations.
- [Neutral rectangular slab: genuine2P reference and YB](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-neutral-slab-yb-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Coulomb1, lateral1×1.25, extendedLz1.5/3/6,4neutral charges±1,physical-z dipole.34 andalpha3/4. Neutral fixed4charge Cartesian-z slab only. YB is a finite-gap approximation, not exact2P at arbitrary vacuum. Original Yeh full text not inspected.
- [Neutral rectangular slab: genuine2P reference and YB](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-neutral-slab-yb-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Coulomb1, lateral1×1.25, extendedLz1.5/3/6,4neutral charges±1,physical-z dipole.34 andalpha3/4.
- [Neutral rectangular slab: genuine2P reference and YB — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en#neutral-slab-yb-en-validation>)

  Separate reference cutoff/splitting qualification, energy gradients, vacuum error, all forces, zero-mode control/far gauge and neutral translations.
- [Neutral rectangular slab: genuine2P reference and YB](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-neutral-slab-yb-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Coulomb1, lateral1×1.25, extendedLz1.5/3/6,4neutral charges±1,physical-z dipole.34 andalpha3/4. Neutral fixed4charge Cartesian-z slab only. YB is a finite-gap approximation, not exact2P at arbitrary vacuum. Original Yeh full text not inspected.

## Code and validation

- [Neutral rectangular slab: genuine2P reference and YB](<https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en>)
  availability: run

  Compare corrected orthorhombic3P Ewald energy/all forces against a separately implemented genuine2P series.
