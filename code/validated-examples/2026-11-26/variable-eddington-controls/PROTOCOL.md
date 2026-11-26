# Periodic variable Eddington factor and tensor controls

This is a bounded, dimensionless educational protocol for a steady transport-derived closure. The input and acceptance files define the fixed contract. A reviewed `freeze.json` and actual execution receipts establish which source version was run; this document alone makes no success claim.

## Models and normalization

Use the normalized angular measure `<g> = (1/4π) ∫S² g dΩ`. Define `E=<I>`, `H=<ΩI>` and `K=<ΩΩI>`, with `D=K/E`. In slab symmetry the measure reduces to `(1/2) ∫[-1,1] dμ`; transverse second moments are obtained by exact azimuthal symmetry, not by treating the angular domain as a one-dimensional beam.

The prescribed-source equation is

```
Ω·∇I + st I = ss E + q,
st=4, ss=3, sa=st-ss=1, c=1.
```

The steady moment equations are `div H + sa E=q` and `div K + st H=0`. With the full angular closure they give

```
A_D(E) = st*sa*E - dxx(Dxx E) - 2*dxy(Dxy E) - dyy(Dyy E) = st*q.
```

The y terms are absent only for the slab case. The 2D spatial problem retains a full 3D angular tensor, including `Dzz`, `Dxz` and `Dyz`.

## Fixed inputs

Spatial unknowns are **point values at `x_i=i/N`**, not exact cell averages. The domain is the periodic unit interval or square, with ij array indexing. A normal x-face is at `((i+1/2)/N,j/N)` and a y-face at `(i/N,(j+1/2)/N)`. Wrapped periodic dual cells use these same shared faces.

The two case IDs are:

- `vef-fourier-scattering1d`: `q=1+0.3 cos(2πx)`, with `(N,Gauss μ)=(33,32),(65,32),(65,64)`.
- `vet-fourier-source2d`: `q=1+0.3 cos(2πx)+0.2 sin(2π(x+y))`, with `(N,Gauss μz,uniform φ)=(17,12,48),(33,12,48),(33,16,64)`.

Each case also has one constant-source control at `N=9`, through the same solver, using its coarse angular rule. Thus there are six main/probe rows and two component rows. There are no parameter scans or adaptive row additions. The two-dimensional angular weights are positive and normalized on S², with `Ω=(sqrt(1-μz²)cosφ,sqrt(1-μz²)sinφ,μz)`.

Sources use `q=qmean+Re Σ b exp(2πi k·x)`. A sine of positive amplitude `a` is represented by `b=-ia`. The input JSON stores integer wave numbers and real/imaginary parts explicitly. NumPy FFT coefficients for a positive mode are `b/2`, with the conjugate negative mode; the code never inserts `b` into both modes.

## High-order transport and low-order feedback

The initial LO energy is uniform `qmean/sa=1`. At each outer iteration, the **actual current LO energy** supplies `S=q+ss E_LO`. The formal periodic angular solve is

```
I_hat(Ω,k)=FFT(S)/(st+i Ω·k).
```

The code evaluates all directions, measures imaginary inverse-FFT residue before accepting real fields, and requires strict positive finite intensity and energy. It forms `E_HO,H_HO,K_HO,D` by positive quadrature, not from the analytic reference. In the slab, `Dyy=Dzz=(1-Dxx)/2` follows azimuthal symmetry. In 2D every independent tensor entry is integrated; z parity is measured rather than silently imposed.

An independent finite-difference moment solve advances its own `E_LO` using this D. It uses a fixed Richardson iteration preconditioned by the exact periodic FFT inverse of `st*sa-Laplacian_h/3`. This is not a conjugate-gradient/SPD assumption for variable D. The inner cap is 200 iterations and the outer cap is 40. No observed-failure-based damping, extrapolation, clipping or fallback is present.

After the new LO state is computed, another formal solve supplies the next D. That angular result is carried into the next iteration. Stopping requires both LO and D update thresholds **and the true LO residual with the same final current D**. The HO/LO energy gap is recorded separately: two different spatial discretizations need not agree exactly at a fixed grid.

## Shared face ownership

For `Pij=Dij E_LO`, x-face flux is

```
Fx[i+1/2,j] = -(Pxx[i+1,j]-Pxx[i,j])/(h*st)
              -(Pxy[i+1,j+1]+Pxy[i,j+1]-Pxy[i+1,j-1]-Pxy[i,j-1])/(4*h*st).
```

The y-face is the corresponding transpose using Pyy and the x derivative of Pxy. The divergence of these **same shared faces** gives the three-point diagonal and four-corner mixed operator, including both mixed contributions. In particular,

```
st*(div_face F + sa E_LO - q) = A_D(E_LO)-st*q.
```

Face H errors use the independent analytic H at the exact normal-face coordinates. Averaging adjacent faces supplies `H_LO_center` for plotting and a pointwise realizability diagnostic; the divergence of that averaged field is never substituted for the conservation residual.

## Independent oracle and negative controls

`analytic_reference.py` evaluates the prescribed-source continuum angular integrals in closed form, independently of the primary FFT and difference solver. It receives only source coefficients, physical constants and evaluation coordinates. `primary.py` cannot import this module or obtain D, q or an initial state from it. `run.py` may call it only after solving, to evaluate errors.

The independent component tests qualify the analytic integrals with distinct numerical angular integration, and verify the mixed operator and face budget with direct Fourier/stencil algebra. Negative controls address incorrect sine phase, frozen scattering feedback, isotropic prescribed closure and missing/mis-signed cross terms. Their scope is stated in `test_cases.py`; they do not replace either variable-closure main case. Primary-source reading depth and unreviewed portions of the cited papers are recorded in `source-reading.json`.

## Declared acceptance and interpretation

All primary-case acceptance thresholds are in `acceptance.json`, fixed before a first numerical execution. Required checks include true residuals, strict I/E positivity without floors, realizability, full-tensor trace/symmetry/PSD and z parity, independent finest-grid energy/face-flux/tensor errors, **complex** source-mode coefficients, same-angle spatial refinement, separate angle probes, and nontrivial scalar/off-diagonal closure variation.

The complex coefficient error uses the predeclared 0.02 bound and includes phase; separate magnitude and phase errors are also reported. A constant background cannot make a failed source mode pass. Constant controls use absolute errors for zero flux and absent modes; no zero reference is assigned an artificial relative error. Root's strict-positivity instruction is an explicit pre-execution tightening of the research draft's tiny-negative-intensity allowance, not an adjustment after observing results.

The algebraic M1 tensor evaluated on reference E/H is a study-only closure diagnostic. No M1 PDE solver is executed by this package. Work counts, wall time, HO/LO gaps and error curves are reported without a speedup claim, an angular-order theorem or a fixed-grid AP assertion.

Independent component-oracle bounds are fixed in test_cases.py; their principal qualification limits are also recorded under component_qualification_checks in acceptance.json: adaptive scalar R/B/C/T and complex Fourier coefficients use absolute tolerance 2e-12, a separate 24-by-96 sphere rule at three prescribed points uses 2e-9, and the shared-face/nine-point operator and constant-tensor preconditioner use 2e-12. Exact algebraic identities have the tighter explicit bounds in the frozen tests. These declarations precede every solver, test and plotting execution.

## Reproduction and artifacts

Use the three exact direct pins in `requirements.txt` under Python 3.12. The plotting requirements are separate. An independently extracted package needs no repository checkout, callback or network service. Set all three numerical thread variables before executing:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  python run.py --input inputs.json --output fresh-results
```

The output directory must be new. The CLI verifies `freeze.json` before scientific imports and again before completion. Freeze entries are an explicit allowlist of relative public source filenames and SHA-256 values. Generated output directories are never recursively added to that source inventory.

The runner has a cooperative 90-second budget, with an external owned-process 120-second limit. Pytest has an external 120-second limit; saved-array plotting has a separate 45-second limit. Reaching a cap is a retained failure, never permission to add rows, relax criteria or repeat automatically.

`result.json` has exactly the two public case IDs, case decisions, per-case metrics and four records each. Every record has `row_id`, `role`, the executed row/source, array filename/hash, diagnostics, mandatory checks and actual iteration history. The roles are `coarse`, `fine`, `angle-probe` and `constant`. `measurements.csv` contains finite numeric measurements and explicitly marks a non-applicable relative constant-flux error.

Each `{caseid}--{rowid}.npz` contains point coordinates, q, actual I and angular weights/directions, HO E/H/K, current D, independent LO E and shared face fluxes, center flux, and the independent reference fields/normal face values. The gallery uses the saved `fine` row; the separate diagnostic figure shows coarse/fine/probe measurements and does not silently substitute an angular probe for the main image.

On a handled solver/reference/checkpoint failure, original active and failed-candidate arrays (including nonfinite values when present) are written to `failure-state.npz` **before** strict JSON. The failure record distinguishes its phase, last valid angular block and completed rows. Existing attempts are retained. A hard external kill or exhausted storage cannot guarantee a final flush; previously completed row files remain intact.

## Limits

This is steady, static-medium, periodic, grey, homogeneous-opacity transport with isotropic scattering and prescribed smooth positive sources. It has no frequency-resolved opacity test, matter-temperature evolution, gas coupling, radiation hydrodynamics, moving medium, relativity, inflow/vacuum/Marshak boundary closure, shadows, transient light front, reduced light speed, general AP certificate or reproduction of Athena/DISORT/high-order FEM. VEF is the slab reduction of a formal transport closure; VET uses the spatially varying full S² second moment. Neither is a hardcoded 1/3, local M1 or FLD closure in the main runs. Earlier published packets, results, figures, references and acceptance criteria are unchanged.
