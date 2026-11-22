KEEP chapter: a small linear analysis, not a nonlinear Euler verification

Reproduce the analytic figures and data in a new output folder:
  python -m pip install -r requirements.txt
  python analyse-keep.py --output generated

The script refuses to overwrite a nonempty output directory. NumPy and
Matplotlib are the only direct dependencies. Python 3.9 or later is supported.
The recorded execution used Python 3.12; exact environment versions are in
result.json. Installation of transitive dependencies is not a full lock file.

Optional check against the unchanged published 2026-11-21 code edition:
  python analyse-keep.py --output generated-with-keep --keep-code PATH/TO/atlas-code-2026-11-21

Obtain that version from the public code-and-data guide and verify its published
ZIP/manifest hashes first. The optional probe additionally verifies keep.py's
expected SHA-256. It reads the package but does not edit it. It estimates a
directional derivative about one uniform Euler state with four decreasing
perturbations, and projects a single entropy characteristic onto a Fourier
mode. It is a small linearization check, not a finite-amplitude guarantee.
Without --keep-code, that optional result is omitted; the two analytic figures
and their CSV data do not depend on the package.

Files:
  spatial-dispersion.csv/.png: centered-difference modified wavenumber,
    phase-speed and group-speed ratios for a scalar characteristic mode.
  rk4-response.csv/.png: per-step gain and continuous phase for R(-i*xi),
    including the pure-imaginary-axis stability boundary 2*sqrt(2).
  result.json: fixed inputs, formulas, direct stencil/stage checks, residuals,
    versions and hashes, plus the optional frozen-KEEP linearization check.

Scope:
  sin(theta)/h is the result for uniform-state linearization / a linear scalar
  characteristic mode. It is not the modified wavenumber of nonlinear split
  products. The Nyquist nullspace statement belongs to that centered linear
  stencil, not every nonlinear KEEP interaction. Each semidiscrete Fourier
  mode has constant amplitude in this linear analysis. The fully discrete
  RK4 solution has a generally non-unit gain and a phase error. RK4 phase can
  lag or lead; its plotted phase branch is unwrapped continuously from xi=0.
  The 2*sqrt(2) bound is only for a purely imaginary linear eigenvalue. It is
  not a global nonlinear Euler CFL, positivity or entropy-preservation bound.

New script: original implementation code, MIT; see LICENSE. Preserve the
copyright and full license notice. Figures and numerical data
retain the existing item-specific site terms; this README adds no blanket
license. Site rights: https://hrkoyama.github.io/rights/
