# Godunov smoothed particle hydrodynamics (GSPH)

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/gsph/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Godunov SPH / GSPH](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gsph/?lang=en>)

## Equations

No chapter-specific association is registered. Atlas-wide index: [Equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en)

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Sod-type particle shock tube with Gaussian-convolution GSPH](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=en>)
  availability: run

  ActualInutsuka-linear-overlap variablehGSPH approximation withfirstorderpair states, comparedwithdistinctstandardSPHcontrol. Periodictwointerfaces; centralwindowbeforeouterwaves. Not cubic/MUSCLpaperreproduction or plainSPH-pressure-star surrogate.
- [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=en>)
  availability: run

  Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.
- [Godunov SPH / GSPH — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gsph/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
