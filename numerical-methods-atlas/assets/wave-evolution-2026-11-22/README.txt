Matched-time wave evolution: scalar linear advection

Reproduce in an absent or empty output folder (Python 3.9 or later):
  python -m pip install -r requirements.txt
  python generate-wave-evolution.py --output generated

The script refuses to overwrite a nonempty output directory. NumPy and
Matplotlib are the only direct dependencies. requirements.txt records the
versions used; it is not a lock file for transitive dependencies. The recorded
execution used Python 3.12.14. result.json records the exact runtime versions.

Equation and common inputs:
  u_t + a*u_x = 0, periodic domain [0,1), a=1
  N=127 points, h=1/127, C=a*dt/h=0.8, dt=0.8/127
  u(x,0)=exp(60*(cos(2*pi*(x-0.25))-1))
  steps 0..160; playback saves every second step (81 frames)
  one crossing period is 1; final time is 1.007874015748... periods

All four curves start from the identical sampled positive smooth bump, with
the same time and fixed shared vertical scale. An odd N avoids the ambiguous
real Nyquist mode under a fractional exact spectral translation.

For theta=2*pi*m/N, each interval dt multiplies Fourier coefficients by:
  exact: exp(-i*C*theta)
  A damping_only: abs(1-C+C*exp(-i*theta))*exp(-i*C*theta)
  B dispersion_only: exp(-i*C*sin(theta))
  C lax_wendroff: 1-i*C*sin(theta)+C^2*(cos(theta)-1)

A is an artificial amplitude-only diagnostic: it combines upwind gain with
exact advection phase. It is not claimed to be an ordinary stencil scheme.
B is the exactly evolved semidiscrete centered-difference equation. It has
unit Fourier gain, so discrete L2 is preserved; its phase is inaccurate.
There is no RK4 or other time-integrator error in B. A conserved L2 does not
imply a conserved peak: Fourier phases can redistribute the profile and
produce negative lobes. C is the actual fully discrete Lax-Wendroff update;
both amplitude and phase differ from exact advection.

The exact curve translates the initial N-point trigonometric interpolant.
verification.json quantifies its difference from the analytic shifted bump
over all 161 times and 127 grid points (about 1.3e-14 in this run). It also
reports an oversampled numerical Fourier-tail estimate, which includes
floating-point noise and is not an analytic rigorous bound.

Files in generated/:
  frames.json: compact schema_version=1 data for shared-time playback
    x: 127 coordinates rounded to 10 decimal places
    steps, time, time_in_periods: 81 aligned entries
    series: exact, damping_only, dispersion_only, lax_wendroff;
      each is an array [frame][grid point], amplitudes rounded to 7 decimals
    parameters, labels, fixed y_limits, snapshot_steps
  overview.png: 3 diagnostics by 3 matched times, common axes and exact overlay
  snapshots.csv: initial, step40, step80, step160 data at 16 significant digits
  result.json: parameters, formulas, versions, fingerprints, mass/L2/extrema
  verification.json: direct real-space LW iteration; every-mode upwind,
    centered-derivative and LW stencil checks; reality; mean conservation;
    A/LW nonincreasing L2; B conserved L2; physical-reference and rounding
    errors; SHA-256 hashes of generated result files and the generator

Scientific checks use unrounded float64 data at all 161 steps. The JSON
amplitude rounding error is at most 5e-8; x/time rounding at most 5e-11.
The CSV preserves higher precision for independent checks. SHA-256 identifies
the canonical fixed-input JSON and initial little-endian float64 samples.

Scope: an explanatory variant of the existing scalar linear-advection atlas
problem. No new atlas problem count; no shock data or nonlinear KEEP result.

New script: original implementation code, MIT; see LICENSE. Preserve the
copyright and full license notice. Figures and numerical data retain the
existing item-specific site terms; this README adds no blanket license.
Site rights: https://hrkoyama.github.io/rights/
