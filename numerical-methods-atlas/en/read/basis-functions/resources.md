# Orthogonal polynomials and mesh basis functions

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/basis-functions/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Legendre modal basis / orthonormal scaling](<https://hrkoyama.github.io/numerical-methods-atlas/methods/legendre-basis/?lang=en>)
- [Lagrange nodal basis / GLL collocation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nodal-basis/?lang=en>)
- [Legendre modal basis / orthonormal scaling](<https://hrkoyama.github.io/numerical-methods-atlas/methods/legendre-basis/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Lagrange nodal basis / GLL collocation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nodal-basis/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Legendre modal basis / orthonormal scaling](<https://hrkoyama.github.io/numerical-methods-atlas/methods/legendre-basis/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Lagrange nodal basis / GLL collocation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nodal-basis/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

## Equations

- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-smooth-function-projection-en>)

  Unit-weight interval projection and GLL interpolation, not a PDE. The 32-point projection is checked by a separate Legendre recurrence and 64/96-point rules; example formulas do not add to the 46 model entries.

## Problem figures

- [Polynomial interpolation and projection of a smooth function](<https://hrkoyama.github.io/numerical-methods-atlas/problems/smooth-function-projection/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/smooth-function-projection.png
- [Polynomial interpolation and projection of a jump function](<https://hrkoyama.github.io/numerical-methods-atlas/problems/jump-function-projection/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/jump-function-projection.png

## Exact / reference solutions

- [Polynomial interpolation and projection of a smooth function — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/smooth-function-projection/?lang=en#references-en>)

  Compare Legendre-projection and nodal-interpolation errors against known values of the specified smooth function. These data do not solve a governing equation.
- [Polynomial interpolation and projection of a jump function — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/jump-function-projection/?lang=en#references-en>)

  Compare with known values of the specified jump function to inspect projection/interpolation oscillations and convergence, separately from smooth-function error behavior.
- [Smooth function: Legendre projection and GLL interpolation — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/smooth-function-projection/?lang=en#smooth-function-projection-en-validation>)

  CSV provides 201 aligned projection/interpolation/exp(x) rows per degree. JSON records degree-wise L2 errors, coefficient differences, orthogonality and 64/96-point quadrature agreement.

## Code and validation

- [Smooth function: Legendre projection and GLL interpolation](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/smooth-function-projection/?lang=en>)
  availability: run

  L2-project exp(x) at degrees 2/4/6/8 and compare GLL interpolation at the same degrees. Check coefficients, orthogonality and errors using separate 64/96-point rules and an independent Legendre recurrence, versus 32-point projection quadrature.
- [Legendre modal basis / orthonormal scaling — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/legendre-basis/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Lagrange nodal basis / GLL collocation — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nodal-basis/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
