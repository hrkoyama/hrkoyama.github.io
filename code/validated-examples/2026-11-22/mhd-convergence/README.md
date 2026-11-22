# Matched CT/GLM convergence / 条件を揃えたCT・GLMの収束検証

Three small fixed-input cases deepen, and do not overwrite, the previous fluid/MHD release. The physical cases compare a constructed moving magnetostatic equilibrium and the existing short-time Orszag–Tang target. A deliberately invalid initial-constraint control is diagnostic only. One new physical target is added; different methods, resolutions, steps and damping rates are not counted as separate problems. No quantum calculation is run.

旧流体・MHD配布版を保持した追加検証です。構成厳密解である移動磁気静力学平衡を1つの新しい物理標的として追加し、既存OTを深めます。初期div B違反を故意に与える対照は診断だけで、物理問題には加算しません。量子計算は追加しません。

## Same declared conditions / 揃えた条件

Both primary methods solve planar ideal MHD, gamma=5/3, mu0=1, in a periodic unit square. Each uses piecewise constants, the **same fixed Rusanov/LLF speed alpha=3**, forward Euler, and exactly the same prescribed steps. GLM has ch=3 and the **fixed physical** damping rate kappa=2, independent of mesh size. The energy is physical thermal+kinetic+magnetic MHD energy: it has no psi-energy term. No Powell/EGLM terms, pressure/density floors, energy reset, adaptivity or timestep retries are hidden in the solver.

CT stores unique right/top face fields and applies the curl of one shared arithmetic corner EMF. Fluid mass, momentum and total energy evolve conservatively; cell B is reconstructed explicitly from faces at every RHS. GLM evolves cell B and psi. The exact initial fields are separable, so their analytic face averages reconstruct **identical initial cell states** in the two methods. Nevertheless, the staggered face treatment and cell GLM fluxes differ intrinsically: this is a comparison of two fully stated discretizations, not a causal attribution of every error difference to one constraint technique. This arithmetic flux-CT is not Athena's upwind CT or CTU.

周期単位正方形・同じ方程式・同じ初期セル状態・固定LLF速度3・前進Euler・同じ刻み列を使います。GLMのchとκは格子で変えません。CTは共有corner EMFの離散curlと面B、GLMはcell B/ψです。質量・物理的総Eを保存し、ψの補助ノルムと混同しません。face/cell表現を含む離散化全体の比較であり、CT/GLMという名前だけの一般的な優劣は結論しません。

## Constructed exact moving equilibrium / 構成した移動平衡

```
A = .05 [cos(2pi(x-.3t)) + cos(2pi(y-.2t))]
B = (A_y, -A_x), rho=1, v=(.3,.2)
p = .1 + (2pi)^2 A^2/2, t_final=.1.
```

This is an analytically constructed verification case, **not a claimed published standard test**. With Jz=-Laplacian(A)=(2pi)^2 A, J cross B=Jz grad(A)=grad(p). Uniform translation satisfies mass and induction, and the full total-energy residual reduces to v dot [grad(p)-J cross B]=0. The Lorentz force and pressure gradient are nonzero. Independent pointwise PDE/force checks and Gaussian quadrature verify the reference construction.

`exact_smooth` integrates the **conserved variables** over each cell using sine/cosine averages (sinc factors). In particular, averaged A² and averaged B² are integrated separately. Pressure recovered from the averaged conserved state is not identical to the exact primitive pressure average because of subcell magnetic variance. Positivity is measured using the recovered finite-volume pressure; it is not falsely compared with a pointwise exact pressure.

16²/32²/64² meshes all use384 steps, so dt is fixed during mesh refinement. Record per-component L1/L2/Linf errors and the observed order; the scheme is formally first order, while the finite grid observations need not equal1 exactly. Step doubling on64² must be at most.1 of the measured continuum error. This is an empirical contamination diagnostic, not a rigorous error bound.

保存変数を解析的にセル積分し、L1/L2/L∞と観測次数を測ります。p(保存変数平均)とp平均を同一視しません。空間走査では全格子でdtを固定し、最細格子の刻み倍増差を別に確認します。理論上1次の手法と有限格子で測った次数を区別します。

## Independent Orszag–Tang reference / 独立OT参照

The standard continuous OT data are rho=25/(36pi), p=5/(12pi), v=(-sin(2pi y),sin(2pi x)), B=(-sin(2pi y),sin(4pi x))/sqrt(4pi), t=.05. The primary16²/32²/64² meshes use192 identical steps. Initial momentum and energy are analytic cell averages.

Official Athena++ source commit **1395e2f543f4368d448cb1a2cf92ba1f910e3416** was separately built and actually executed with HLLD/PLM/RK2/upwind CT. The previously built, hashed OT binary was reused for the new reference runs; no new compilation is claimed in this revision. New256² and512² runs both useCFL=.15, and a further512²/CFL=.3 run isolates reference time sensitivity. Stored128²/CFL=.3 data remain historical context; the128→256 pair changes CFL and is **not** used to infer a pure spatial order. All new reference input files, execution times, binary/source/raw/numeric hashes and BSD terms are included. Raw tables and build evidence are retained separately; no executable or article PDF is redistributed.

Reference cell data are conservatively block-averaged, respecting Athena's x1-fastest ordering and the coordinate shift from[-.5,.5]^2 to[0,1]^2. Compare density and both magnetic components; the magnetic L1 norm is the mean across Bx and By, not By alone. Reference spatial and temporal increments must be small both absolutely and relative to the primary error. Athena's primitive/face initialization differs at finite resolution while representing the same continuous data. An independent finite-grid numerical reference is not an exact solution or rigorous error bound.

別のC++実装を実際に実行し、256²/512²の同じCFLで格子増分、512²の固定格子で時間増分を分離します。密度とBx/Byの誤差、保存量・正値性を確認します。参照自身の増分を主計算誤差と比べ、有限参照を厳密解とは呼びません。128²の旧記録は保持し、異なるCFLの組を純粋な格子収束に使いません。

## Temporal reference / 時間積分だけの独立参照

At fixed8² for the smooth case and16² for OT, run16/32/64/128 forward-Euler steps. The largest declared two-dimensional CFL sum is.3. Separately executed SciPy DOP853 integrates **the same spatial RHS** using two tolerances (rtol1e-10/2e-12,atol1e-12/2e-14) and maximum stepsT/64,T/128. Its increment must be at most.01 of the finest primary temporal error. This isolates temporal convergence; it does not make DOP853 a second independent spatial solver.

固定格子で前進Eulerの時間収束を、別実行のDOP853へ照合します。DOP853は空間RHSを共有するので「時間積分器が独立」と限定します。連続厳密解・独立Athena空間実装・共有RHSの別時間積分器という3つの役割を分けます。

## Why a third diagnostic is necessary / 能動的cleaningの別対照

With constant scalar LLF viscosity on a periodic collocated mesh, centered divergence commutes with the discrete curl and Laplacian. The GLM div=psi=0 subspace is invariant up to roundoff, even in the nonlinear physical cases. Their tiny divergence therefore **does not demonstrate active cleaning**, and it is not used to rank GLM above CT. Maximum psi and native/common divergence are reported. Native face CT divergence and centered cell divergence are different operators; the latter also has a checkerboard blind spot.

The third case intentionally initializes nonzero **native CT divergence**, using faceBx=.01cos[2pi(i+1)/32], By=0. Its adjacent-face average is assigned identically to GLM cellBx; rho=p=1, v=0, psi=0. This violates valid physical CT initial conditions. CT preserves its initial defect, as expected of a curl update, rather than acting as a projection/cleaning method. Passing this diagnostic means detecting that expected behavior; it does not recommend invalid CT initial data.

For y-invariant By=vy=0, GLM's Bx/psi subsystem decouples from fluid feedback even though the full MHD code is run. Independently construct the Fourier symbol

```
k_tilde = N sin(2pi/N), nu_h = alpha N [cos(2pi/N)-1]
M_h = [[nu_h, -i k_tilde],[-i ch^2 k_tilde, nu_h-kappa]].
```

Compare both Bx and psi with `(I+dt*M_h)^steps`; also report semidiscrete `expm(T*M_h)` and the continuum Fourier matrix separately. The finite-grid reference includes LLF numerical diffusion and forward-Euler time error. Bx reduction alone can be phase exchange with psi: use a matched **kappa=0** companion at the same alpha/dt, and compare the auxiliary wave norm `W=mean(Bx²+psi²/ch²)` between kappa2 and0. W is not the conserved physical total energy E. Positive fluid states and conserved E/mass are checked in all three runs. This diagnostic does not certify nonlinear shock/boundary cleaning.

定数LLF・周期中心演算子の構造だけでdiv=ψ=0が保たれるため、物理2例の小さいdivをcleaningの成功と呼びません。別の非物理対照でψを励起し、CTの初期違反保持とGLMの独立Fourier応答を検査します。κ0対照で、Bx/ψの位相交換・数値粘性と物理減衰を分けます。対照の合格は期待した現象の検出を意味します。

## Fixed protocol and reproducibility / 事前固定と追試

The original two-case input SHA was `274e3e30d1abfb15efaef12e1e53cdd8176d3bc7229a3a89bcd5fa9e3b67d67d`. Before **any numerical pilot**, algebraic review found the inactive-cleaning subspace and added the separate constraint control, then its kappa0 companion. The original input and intermediate revision remain in `inputs-initial.json`, `inputs-control-before-damping-pair.json` and `protocol-history.json`. No original physical-case input or criterion changed. The final pre-pilot SHA is **ef1066846f52a270af0ee89282843ef6ea39279bedac758a1e13a0970c639734**. The first complete3-case pilot passed without changing these inputs/criteria.

独立した事前の代数確認で診断不足が見つかったため、数値pilotを行う前に非物理対照とκ0比較を追加しました。旧入力・中間入力・理由・SHAを残し、元の物理2例の条件や公差は変えていません。最初の全3例計算から固定基準を満たしました。

Python3.12, three routine pinned dependencies only:

```
python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -W error -m pytest -q -p no:cacheprovider
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -W error run.py --input inputs.json --output NEW_EMPTY_DIRECTORY
```

Routine runs load pinned independent Athena values and execute every primary input and both DOP853 time references, without network/C++/private checkout. A total110-second failure guard and finite grid/CFL/allocation controls apply. Output must be new or empty. Tests include independent cell quadrature, exact GLM Fourier symbols, CT div-curl identities, conservation, input limits, tampering/missing-reference rejection and invalid initial-constraint behavior.

Optional figures use saved JSON/NPZ only and do not rerun a solver:

```
python -m pip install -r requirements-plotting.txt
python plot.py --results NEW_EMPTY_DIRECTORY/result.json --output FIGURES_DIRECTORY
```

## Optional independent Athena regeneration / 参照の別再生成

Obtain the official pinned source archive URL from `references/athena-ot-original-provenance.json`, check its SHA against `references/reference-manifest.json`, and verify it before extracting. In a **separate** source checkout/build directory:

```
python configure.py -b --prob=orszag_tang --flux=hlld --cxx=clang++
make clean
make -j2
bin/athena -i PATH_TO_SAVED_ATHINPUT
```

Use each saved `athinput-*` independently, preserving the t=.05 final table. Convert the numeric table without interpolation or alteration:

```
import numpy as np
np.savez_compressed('NEW_REFERENCE.npz', table=np.loadtxt('NEW_ATHENA_FINAL.tab'))
```

Keep newly regenerated outputs separate from the frozen release, record actual compiler/environment/input/binary/source/raw/NPZ hashes and time, and compare the new numeric tables with the stored values. A compiler/platform rebuild can change binary hashes without changing the intended numerical model; do not copy old execution metadata into a new receipt. Routine runs require no regeneration or native binary. No AMR or quantum sweep is added.

## Sources and rights / 原典と利用条件

`cases.json` gives bilingual review scope for Dedner et al.2002 (selected original GLM/EGLM equations), Gardiner–Stone2005 (selected face/corner CT equations), Tóth2000 (abstract/bibliographic identity), Stone et al.**2020** (paper metadata plus actual official Athena++ code execution), and versioned SciPy DOP853 documentation. The constructed equilibrium and chosen numerical acceptance criteria are original test design, not attributed to a standard published benchmark. No article PDF or external executable is bundled.

Original Python code: MIT (`LICENSE`), with earlier Atlas planar-solver inspiration recorded in `source-provenance.json`. Athena-derived numeric outputs, inputs and their official BSD-3-Clause notice are documented in `references/ATHENA-LICENSE.txt`. Text, translations, figures, numerical data/results and third-party materials follow the site's separate conditions: https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
