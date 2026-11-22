# Small particle and transport verification examples / 小規模な粒子・輸送の検証

These are original educational implementations, not wrappers around production
Ewald, FMM, plasma, gas-flow or radiative-transfer solvers. All six cases use
small fixed inputs and declared acceptance criteria in `inputs.json`. They need
NumPy, SciPy and pytest only; no quantum-chemistry calculation, network access,
reference download or external program is used at runtime.

```sh
python -m pip install -r requirements.txt
python -W error -m pytest -q -p no:cacheprovider test_particles.py
python -W error run.py --input inputs.json --output output
```

`result.json` records every decision, measured value, refinement series, input
SHA-256 and elapsed time. Per-case CSVs contain the same measured records.
Exit 0 means all declared checks passed; exit 1 means a numerical criterion
failed; exit 2 means unsupported/invalid input or an I/O error. The CLI deliberately
limits particle counts, grids and steps to the small educational budget. A caller
must choose a new output folder when retaining a prior result.

## Implementations and independent/analytic checks

1. **3D Ewald**: neutral cubic periodic charges, Coulomb constant one and conducting
   (tin-foil) boundary. Both real and reciprocal sums plus the self correction are
   implemented. Changing the split parameter and both cutoffs checks convergence.
   All 24 forces are checked by central energy differences. An independent 1D
   Jacobi-theta integral checks the NaCl Madelung constant; it does not call the
   3D Ewald routine. The asymmetric test cell is distinct from the NaCl lattice.
2. **B-spline smooth PME (SPME)**: orders 4/6 and meshes 16/24/40; tensor-product
   cardinal B-spline assignment, exact nodal-spline structure-factor correction,
   FFT convolution and analytic derivatives of the mesh energy. The reciprocal
   representation is compared with direct Ewald sums; both paths share the real
   sum and self correction. This is the Essmann (1995) smooth-PME variant, not an
   implementation of Darden (1993)'s original Lagrange interpolation. Finite-mesh
   aliasing permits a small nonzero net force for this energy-gradient variant;
   that diagnostic is reported. Exact momentum conservation is not claimed.
3. **2D free-space Laplace FMM**: kernel `phi=-sum(q log(r))` with `E=-grad(phi)`.
   The uniform quadtree has P2M, upward M2M, interaction-list M2L, downward L2L,
   local evaluation and exact near-field P2P. Orders 2/4/8/12 are compared with
   independent all-pairs potential and field sums. It is not Barnes–Hut, a 3D
   Coulomb solver, a periodic FMM, an adaptive tree, or a measured scaling study.
4. **1D electrostatic PIC**: periodic CIC charge deposition and identical field
   gathering, spectral Poisson solve, quiet-start cold electrons with a stationary
   neutralizing ion background, velocity Verlet. Spatial and temporal sweeps are
   separate and compare a small-amplitude mode with `cos(omega_p t)`, `omega_p=1`.
   Nonzero-mean charge is rejected (up to scaled roundoff). Charge compatibility,
   Poisson-potential residual and single-particle self force
   are checked. The real spectral derivative discards the Nyquist field mode.
   The continuum linear reference has a finite-amplitude/particle-noise floor;
   no nonlinear instability, collisional plasma or electromagnetic PIC is tested.
5. **Homogeneous DSMC collision component**: equal masses and isotropic,
   constant-rate Maxwell-molecule pair scattering. Each round randomly matches
   particles once, preserves pair momentum and kinetic energy and randomizes the
   relative direction. A two-beam ensemble is compared with Maxwellian component
   moments, the Gamma(3/2,1) energy CDF and the exact expected anisotropy factor
   `(N-2)/(2(N-1))` per round. Three particle budgets and sixteen seeds (7919 through 7934) are stored.
   Each seed has fixed zero total momentum and fixed energy, so finite-N
   equilibrium is microcanonical. Its component fourth moment is
   `3-6/(3*N-1)`; Maxwell/Gamma are thermodynamic-limit references. The
   finite-particle offset is distinct from across-seed sampling uncertainty.
   For `D=<vx^2-(vy^2+vz^2)/2>`, a uniformly chosen partner gives the
   center-of-mass anisotropy factor `(N-2)/(2*(N-1))`; the isotropic
   postcollision relative direction has zero expected anisotropy.
   This is a collision-only component test: rounds are not calibrated physical
   time. Streaming, collision cells, hard-sphere rate selection, transport
   coefficients and real-gas-flow solutions are outside this example.
6. **1D pure-absorption discrete ordinates**: Gauss–Legendre positive hemispheric
   directions and first-order upstream spatial transport; compare every ray with
   Beer–Lambert attenuation. Discrete flux balance and positivity are checked.
   The recorded angular error uses the analytic-ray quadrature and excludes
   spatial error; a separate total-flux-error column includes both. Separate
   angular refinement uses exact exponential propagation per constant
   cell and compares exit flux with `2*pi*E_3(tau)`. No scattering, emission,
   frequency redistribution, radiation–fluid coupling or full DISORT reproduction
   is claimed.

## References and provenance

Primary-paper and official-reference URLs, bibliography and actual review scope
are in `cases.json`. Equations and code are independently written for these
fixed examples. No paper, textbook, library source or third-party dataset is
copied into the package. The NaCl scalar reference is recomputed by a Jacobi-theta
integral; its quadrature error estimate is stored. Statistical DSMC acceptance
applies to the recorded seeds/budgets rather than all possible random samples.

NumPy/SciPy functions provide array arithmetic, FFTs, `erfc`, independent scalar
quadrature/special-function references and distribution diagnostics. They are
not implementations of the Ewald/FMM/PIC/collision/ray-marching algorithms here.
Their licenses remain separate from the MIT license of this original code.

The MIT label applies only to the original Python code. Prose, figures, input
parameters, numerical data and third-party material retain separate conditions;
consult https://hrkoyama.github.io/LICENSING.md and
https://hrkoyama.github.io/rights/. This supplement adds no blanket permission
for those materials. Runtime plotting is optional and uses saved results only.

## 日本語での範囲

6例とも小さな固定入力・判定基準・収束系列・終了理由を保存します。Ewaldは中性の3次元周期セル、SPMEはBスプラインを使うsmooth PMEです。1993年のLagrange型PMEやスラブ補正を実装したとは表示しません。FMMは2次元自由空間の対数核で、M2M/M2L/L2Lと近傍の直接和を実装しています。

PICは1次元静電場・冷たい電子の微小振動に限定します。DSMCはMaxwell分子の等質な衝突部分だけで、衝突roundを実ガス流の時間へ換算しません。放射輸送は散乱と放射を含まない純吸収の平板です。各例の成功を3次元実物質・実プラズマ・実ガス・一般の放射流体の検証へ広げません。

誤差を小さく見せるために判定幅を変更せず、入力とそのSHAを結果へ残します。統計検査では固定seedでの結果と一般的な保証を区別します。詳細な日英説明・式・一次文献・実際の閲覧範囲は `cases.json` にあります。


Optional plots, without rerunning the science:

```sh
python -m pip install -r requirements-plotting.txt
python plot.py --results output/result.json --output output
```

MITは独自のPythonコードだけに適用します。本文・図・入力・数値データ・第三者資料の条件はサイトのLICENSING.mdとrightsを参照し、この配布で一括の利用許諾を追加しません。
