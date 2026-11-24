# Centered spatial difference / 空間中心差分

Status: educational-example

Read about Centered spatial difference, follow the original references and inspect related educational code and checks. Additional fixed examples: Crossing the Bratu fold with pseudo-arclength continuation, Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products. See each release for assumptions and checked scope. Additional fixed examples: Bratu sensitivity near the discrete fold, Matrix-free VJP for distributed Bratu coefficients. See each release for assumptions and checked scope.

「空間中心差分」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。 追加固定例：擬似弧長継続でBratuのfoldを越える、解析・中央差分・方向ADによるJacobian不要Newton–Krylov。条件と検証範囲は各配布版で確認してください。 追加固定例：離散fold近傍のBratu感度、分布係数Bratuの行列非形成VJP。条件と検証範囲は各配布版で確認してください。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers. Additional fixed examples: A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim. An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee. The preceding limitations describe earlier editions. This additional release: The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved. Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

Other names: 中心差分, 中心差分法, 中央差分, central difference, central finite difference

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stability/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/stability/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py

- Reference: https://doi.org/10.1007/BF01448839 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1002/cpa.3160070112 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1002/cpa.3160130205 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

Reaction-diffusion: separate second-order space and fourth-order time: Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions. Turing instability: linear growth and small-amplitude patterns: Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode. Finite-amplitude Schnakenberg transient: nonlinearity and independent reference: Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics. Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence: Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual. Solve a Re100 lid-driven cavity and manufactured flow with a nonperiodic wall-bounded2D vorticity/streamfunction method. Compare original finite-grid Ghia tables, wall shear and grid refinement, keeping a separate pressure-Poisson/gradient manufactured problem distinct. Additional periodic2D KH/RT initial growth uses maintained smooth bases and independent linear IVPs; actual centered conservative face fluxes and Heun evolve vorticity/buoyancy with pressure eliminated. Additional2D cell-centered Poisson uses actual five-point face differences and half-cell Robin elimination; check Neumann compatibility/mean gauge and continuous boundary-flux error. Additional actual2D linear rotating-SWE C-grid uses staggered gradients/divergence and adjoint four-point Coriolis interpolation; separate continuous and discrete-symbol references.

反応拡散：空間2次と時間4次を分けて測る: 線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。 Turing不安定性：線形成長率と小振幅パターン: Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。 Schnakenberg有限振幅過渡：非線形性と独立参照: t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。 Schnakenberg飽和パターン：近定常性と格子・時間収束: t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。 非周期壁面の2D渦度・流れ関数法でRe100蓋駆動キャビティと製造流れを解きます。Ghia原著の有限格子数値表、壁剪断と格子収束を比較し、独立した圧力Poisson・勾配製造問題を区別します。 追加の周期2D KH/RT初期成長は、維持した滑らかな基底と独立線形IVPを使用。中央の保存面流束とHeunで渦度/浮力を実際に進め、圧力は消去します。 追加は2Dセル中心PoissonのNeumann/Robin境界。実際の五点面流束と半セルRobin消去、適合条件・平均ゲージ・境界流束誤差を確認します。 追加は実際の2D線形回転浅水C-grid。staggered勾配・発散・随伴な4点Coriolis補間を使い、連続波と離散記号を分けて比較します。

- Reaction-diffusion: separate second-order space and fourth-order time: https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/
- Turing instability: linear growth and small-amplitude patterns: https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json

- Finite-amplitude Schnakenberg transient: nonlinearity and independent reference: https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/
- Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence: https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/result.json

- Re100 lid-driven cavity: Ghia centerline comparison: https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/
- Nonperiodic wall MMS: velocity, shear and pressure operator: https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/result.json

- KH initial growth in a smooth periodic shear layer: https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/
- RT initial growth in smooth Boussinesq double layers: https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/result.json

- Pure Neumann compatibility and mean gauge: https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/
- 2D mixed Robin MMS and boundary flux: https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json

- Actual2D C-grid rotating shallow-water time advance: https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/result.json

- Crossing the Bratu fold with pseudo-arclength continuation: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/
- Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/result.json

- Bratu sensitivity near the discrete fold: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/
- Matrix-free VJP for distributed Bratu coefficients: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json

Common execution records: [{"id": "reaction-diffusion-fourier", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "turing-schnakenberg", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "schnakenberg-nonlinear", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "schnakenberg-pattern", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "cavity-ghia-re100", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "wall-manufactured", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "kh-initial-growth", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "rt-initial-growth", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "poisson-neumann", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "poisson-robin", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "cgrid-rotating-wave", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "bratu-fold-continuation", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "bratu-matrix-free-jfnk", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "bratu-fold-sensitivity", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "bratu-distributed-vjp", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`; heat-periodic, heat-dirichlet, reaction-diffusion-fourier)
- [Schnakenberg反応拡散](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-schnakenberg-ja) (`bio-schnakenberg`; turing-schnakenberg)
- [Turing反応拡散の枠組み](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-turing-ja) (`bio-turing`; turing-schnakenberg)
- [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja) (`navier-stokes`; lid-driven-cavity)
- [等温格子BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja) (`bgk`; lid-driven-cavity)
- [外力付き非圧縮流と壁面製造解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-incompressible-ja) (`forced-incompressible`; wall-manufactured)
- [維持されたせん断層の強制渦度系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-vorticity-ja) (`forced-vorticity`; kh-initial-growth)
- [能動浮力を伴うBoussinesq渦度系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#boussinesq-buoyancy-ja) (`boussinesq-buoyancy`; rt-initial-growth)
- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; poisson-neumann, poisson-robin)
- [線形回転浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-rotating-shallow-water-ja) (`linear-rotating-shallow-water`; cgrid-rotating-wave)
- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`; bratu-fold-continuation, bratu-matrix-free-jfnk, bratu-fold-sensitivity, bratu-distributed-vjp)

#### 問題の図 (`method-problems-ja`)

##### [周期Fourierモードの熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja) (`heat-periodic`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Dirichlet境界の熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja) (`heat-dirichlet`)

![共有図の左パネル：Dirichlet境界の熱拡散。右パネルは別のPoisson境界問題。](https://hrkoyama.github.io/numerical-methods-atlas/assets/diffusion-boundaries.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja) (`reaction-diffusion-fourier`)

![周期Fourierモードの線形反応拡散。16/32/64格子の連続解誤差と、固定格子での半離散厳密解に対する時間誤差を分けた保存収束図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja#code-ja)

- [反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja) (`reaction-diffusion-fourier`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。

##### [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`)

![a=0.1,b=0.9、拡散係数0.01/1のSchnakenberg型。行列指数に対する線形誤差・成長率と、t=4の小振幅非線形初期パターンを保存値から表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#code-ja)

- [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。

- [Schnakenberg有限振幅過渡：非線形性と独立参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja) (`schnakenberg-nonlinear`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。

- [Schnakenberg飽和パターン：近定常性と格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja) (`schnakenberg-pattern`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。

##### [Re100の蓋駆動キャビティ](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja) (`lid-driven-cavity`)

![保存した最細Re100計算の流線と速さ。赤点は格子上の主渦、白抜き点はGhia表Vの主渦位置です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

ωt+uωx+vωy=νΔωを中央差分とHeun法で進め、各段で−Δhψ=ωを非周期Dirichlet DSTで解きます。u=ψy,v=−ψx。局所一次のThom壁渦度を使用し、原著のCSI-MGと高次壁公式は実装していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#code-ja)

- [Re=100蓋駆動キャビティ：Ghia中心線との比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja) (`cavity-ghia-re100`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

非周期・粘性非圧縮の実際の2D計算を17/33/65点格子で定常化し、Ghia原著の速度中心線と比較します。流線・渦中心・真の残差と発散を同時に保存します。

##### [非周期壁面の製造非圧縮流](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja) (`wall-manufactured`)

![実計算した最細の製造流れの流線と速度誤差。厳密壁渦度を注入せず、キャビティと同じThom閉鎖を使います。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured-preview.png)

共通の中央差分・Heun・非周期Dirichlet DST Poissonを使用します。多項式の明示微分と、独立な係数行列の微分を照合します。別途p=x²+y²+sinπx sinπyの非零Dirichlet Poisson問題を解き、内部中央差分・壁上の二次片側差分勾配を検査します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja#code-ja)

- [非周期壁面の製造解：速度・剪断・圧力演算子](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja) (`wall-manufactured`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

キャビティと同じ壁条件付き2Dソルバーに解析外力を与え、速度と流れ関数の格子収束、壁渦度・壁剪断の誤差を測ります。別の非零Dirichlet圧力製造解でPoisson・勾配の境界演算子も検査します。

##### [KHの初期成長：滑らかな周期せん断層](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=ja) (`kh-initial-growth`)

![保存した2D摂動渦度をεで規格化。色の尺度を明記し、線形参照と成長を比較します。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth-preview.png)

点値の渦度・浮力摂動を共有面の中央流束とHeun法で進め、5点差分PoissonをFFTで解きます。u=ψy,v=−ψxなので中央差分発散は整合します。基底場を解析的に差し引き、層そのものの離散ドリフトと微小摂動を分離します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=ja#code-ja)

- [KHの初期成長：滑らかな周期せん断層](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja) (`kh-initial-growth`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip)

実際の非線形2D渦度方程式を解き、独立Fourier–Galerkin線形初期値問題と有限時間の成長・格子誤差を比較します。

##### [RTの初期成長：滑らかなBoussinesq二層](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=ja) (`rt-initial-growth`)

![保存した2D浮力摂動をεで規格化。滑らかな二層の初期変位で、乱流混合の図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth-preview.png)

点値の渦度・浮力摂動を共有面の中央流束とHeun法で進め、5点差分PoissonをFFTで解きます。u=ψy,v=−ψxなので中央差分発散は整合します。基底場を解析的に差し引き、層そのものの離散ドリフトと微小摂動を分離します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=ja#code-ja)

- [RTの初期成長：滑らかなBoussinesq二層](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja) (`rt-initial-growth`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip)

密度差を浮力だけに残す2D Boussinesq系を時間発展し、不安定な滑らかな層の初期成長を独立線形参照で調べます。

##### [純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja) (`poisson-neumann`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png)

共有面差分で特異行列を組み、体積重み平均のLagrange拘束付き疎直接法とcompatible CGを照合。物理的な不適合外力の平均を勝手に引かない。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja#code-ja)

- [純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja) (`poisson-neumann`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

特異な2D Poissonを互換条件と指定平均込みで解き、不適合な外力を拒否します。

##### [2D混合Robinの製造解と境界流束](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja) (`poisson-robin`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin-preview.png)

半セル距離を用いてRobin境界値を消去し、外向きgradientの面積積分を離散式と同じ重みで評価。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja#code-ja)

- [2D混合Robinの製造解と境界流束](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja) (`poisson-robin`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

2D PoissonのNeumann/Robin面を実際に組み、連続製造解と境界fluxを照合します。

##### [2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja) (`cgrid-rotating-wave`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave-preview.png)

セルeta・法線face u/vの差分と4点Coriolis補間を2Dで評価しRK4更新。3×3行列指数は参照だけで、PDE場の更新には使いません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja#code-ja)

- [2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja) (`cgrid-rotating-wave`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

実際の2D staggered場を時間積分し、連続波と離散symbolの参照を分けて比較します。

##### [擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja) (`bratu-fold-continuation`)

![保存した分岐曲線、λ=2の上下枝、Jacobianの最小特異値、3格子のfold誤差を示す縮小図。擬似弧長stepは物理時間ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png)

hΣdu²+dλ²の重み付き単位接線、予測点と接線超平面によるNewton補正。別の拡大系でfoldと正規化null vectorを解きます。このcaseは疎Jacobianを明示的に組み立てます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja#code-ja)

- [擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja) (`bratu-fold-continuation`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

同じ1次元Bratu境界値問題の下枝から上枝までを追跡し、接線・fold・独立解析族との空間誤差を調べます。

##### [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja) (`bratu-matrix-free-jfnk`)

![保存したN=127のNewton残差、上枝の解と解析参照、Jv誤差、実評価回数を示す縮小図。run indexは保存CSVに対応します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png)

解析Jv、残差2評価の中央差分、または方向1本のforward ADを使います。PoissonのThomas右前処理、2回の再直交化とGivensによるGMRES。η0=.3、その後η=clamp(.9(Fk/Fk−1)^1.5,.001,.5)。これはEW Choice 2型の明示的な変形で、原著のsafeguard全体やPETSc既定値ではありません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja#code-ja)

- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja) (`bratu-matrix-free-jfnk`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。

##### [離散fold近傍のBratu感度](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja) (`bratu-fold-sensitivity`)

![離散fold近傍のBratu感度。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity-preview.png)

解析Jv、Poisson-Thomas右前処理、固定GMRES本体で接線と随伴を解きます。全rtol・最終候補・true residual・終了状態・丸めscaleを保存します。shootingと別の高精度Thomas-Newtonで離散参照を資格します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja#code-ja)

- [離散fold近傍のBratu感度](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja) (`bratu-fold-sensitivity`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

離散Bratuのfoldへ近づく6固定点で、状態誤差と線形許容差の影響を分け、独立shooting勾配と照合します。

##### [分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja) (`bratu-distributed-vjp`)

![分布係数Bratuの行列非形成VJP。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png)

Bvは局所gather、B転置はscatter-add。一次実装はn×m行列を作らずJvで解き、同一状態の1/3目的関数で実際に1個のPoisson因子を共有します。別の参照期間のみdense hatとm本の接線RHSを許可します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja#code-ja)

- [分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja) (`bratu-distributed-vjp`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

2重みだけの局所hat作用で8/16/32個の空間係数を表し、目的関数ごとの随伴VJPを全感度参照と比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期Fourierモードの熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#references-ja) (`heat-periodic`)

- [熱拡散／Fourierモードの減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja) (`sine-heat`; 関連モデルの参照; 解析参照)

保存ギャラリーの周期[0,1]、1+0.25sin(2πx)、ν=0.02、最終時刻1が一致します。別周波数のコード検査への一致は意味しません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-heat)

##### [Dirichlet境界の熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja#references-ja) (`heat-dirichlet`)

- [熱拡散／Fourierモードの減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja) (`sine-heat`; 関連モデルの参照; 解析参照)

こちらは零Dirichlet・sin(πx)、参照カードは周期境界・1+0.25sin(2πx)・ν=0.02です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-heat)

##### [反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja#references-ja) (`reaction-diffusion-fourier`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#references-ja) (`turing-schnakenberg`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Re100の蓋駆動キャビティ](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#references-ja) (`lid-driven-cavity`)

- [Ghia Re100：原著の有限格子速度中心線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ghia-re100-ja) (`ghia-re100`; 同じ問題の参照; 有限格子の数値参照)

Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。

[既存の参照図](/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja#cavity-ghia-re100-ja-measurements)

- [LBMのRe100キャビティ：実2D場とGhia中心線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-cavity-re100-ja) (`lbm-cavity-re100`; 関連モデルの参照; 有限格子の数値参照)

物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。

[既存の参照図](/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja#lbm-cavity-re100-ja-measurements)

##### [非周期壁面の製造非圧縮流](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja#references-ja) (`wall-manufactured`)

- [壁面製造解：多項式速度と独立した圧力演算子](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-wall-mms-ja) (`wall-mms`; 同じ問題の参照; 製造解)

Thomの壁渦度局所打切りは一次で、壁剪断の二次精度は主張せず観測次数を示します。流れ関数の発展では圧力を消去するためゲージは該当しません。圧力診断は独立した演算子製造問題であり、キャビティの圧力・応力境界やMAC射影の検証ではありません。多項式の別微分は独立な流体ソルバーとの比較とは区別します。

[既存の参照図](/numerical-methods-atlas/validation/wall-manufactured/?lang=ja#wall-manufactured-ja-measurements)

##### [KHの初期成長：滑らかな周期せん断層](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=ja#references-ja) (`kh-initial-growth`)

- [KH初期成長：独立した線形Fourier–Galerkin参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kh-initial-growth-ja) (`kh-initial-growth`; 同じ問題の参照; 有限格子の数値参照)

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。

[既存の参照図](/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja#kh-initial-growth-ja-measurements)

##### [RTの初期成長：滑らかなBoussinesq二層](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=ja#references-ja) (`rt-initial-growth`)

- [RT初期成長：Boussinesq二層の線形IVP参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rt-initial-growth-ja) (`rt-initial-growth`; 同じ問題の参照; 有限格子の数値参照)

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。

[既存の参照図](/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja#rt-initial-growth-ja-measurements)

##### [純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja#references-ja) (`poisson-neumann`)

- [純Neumann：解析場・互換条件・平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-neumann-ja) (`poisson-neumann`; 同じ問題の参照; 製造解)

同じ半離散系の別線形解法は独立PDE参照ではありません。既存Dirichlet MGの成功や2D任意境界へ一般化しません。

[既存の参照図](/numerical-methods-atlas/validation/poisson-neumann/?lang=ja#poisson-neumann-ja-measurements)

##### [2D混合Robinの製造解と境界流束](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja#references-ja) (`poisson-robin`)

- [混合Robin：2次元解析場と独立な法線流束](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-robin-ja) (`poisson-robin`; 同じ問題の参照; 製造解)

Robin問題は一意なので平均ゲージを重ねません。境界条件の代数残差と物理flux精度を区別します。

[既存の参照図](/numerical-methods-atlas/validation/poisson-robin/?lang=ja#poisson-robin-ja-measurements)

##### [2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja#references-ja) (`cgrid-rotating-wave`)

- [C-grid：連続Fourier解と離散記号の行列指数](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-cgrid-rotating-wave-ja) (`cgrid-rotating-wave`; 同じ問題の参照; 解析参照)

線形・平面・周期squareの限定例。非線形浅水、PV・球面格子・全球dynamical coreやWilliamsonは未実装の後続課題。

[既存の参照図](/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja#cgrid-rotating-wave-ja-measurements)

##### [擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja#references-ja) (`bratu-fold-continuation`)

- [擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-fold-continuation-ja) (`bratu-fold-continuation`; 同じ問題の参照; 解析参照)

小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。

[既存の参照図](/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja#bratu-fold-continuation-ja-measurements)

##### [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja#references-ja) (`bratu-matrix-free-jfnk`)

- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-matrix-free-jfnk-ja) (`bratu-matrix-free-jfnk`; 同じ問題の参照; 解析参照)

小1次元BVP向けの教育実装です。ADは四則・exp・境界paddingの方向微分に限ります。小Hessenberg行列と基底は保持します。ηの固定下限があるため、原著EWの漸近収束定理、一般AD/PETScとの同等性、速度向上や大域収束は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja#bratu-matrix-free-jfnk-ja-measurements)

##### [離散fold近傍のBratu感度](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja#references-ja) (`bratu-fold-sensitivity`)

- [離散fold近傍のBratu shooting・接線・随伴参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-fold-sensitivity-ja) (`bratu-fold-sensitivity`; 同じ問題の参照; 有限格子の数値参照)

連続foldは離散foldではありません。rtol1e-4/1e-8は達成必須、requested1e-12は観測のみで未達を収束と表示しません。返却候補の独立勾配精度は別判定。最小固有値/丸めscaleは浮動小数点の診断で保証区間ではありません。BratuのJは対称であり、非対称転置は別の演算子対照です。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

[既存の参照図](/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja#bratu-fold-sensitivity-ja-measurements)

##### [分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja#references-ja) (`bratu-distributed-vjp`)

- [分布Bratu係数の独立dense感度と行列不要VJP](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-distributed-vjp-ja) (`bratu-distributed-vjp`; 同じ問題の参照; 有限格子の数値参照)

同じ離散状態の微分検証で、独立した物理PDE解の証明や一般ADではありません。保存arrayと固定Krylov workspaceの記録はRSS測定ではありません。m=2のθ端点は[a-b-2,a+b-2]で、物理係数端点[a-b,a+b]と区別します。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

[既存の参照図](/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja#bratu-distributed-vjp-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stability/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 反応拡散：空間2次と時間4次を分けて測る (`reaction-diffusion-fourier`)

[反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。

##### Turing不安定性：線形成長率と小振幅パターン (`turing-schnakenberg`)

[Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。

##### Schnakenberg有限振幅過渡：非線形性と独立参照 (`schnakenberg-nonlinear`)

[Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json)

t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。

##### Schnakenberg飽和パターン：近定常性と格子・時間収束 (`schnakenberg-pattern`)

[Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json)

t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。

##### Re=100蓋駆動キャビティ：Ghia中心線との比較 (`cavity-ghia-re100`)

[Re100の蓋駆動キャビティ](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json)

非周期・粘性非圧縮の実際の2D計算を17/33/65点格子で定常化し、Ghia原著の速度中心線と比較します。流線・渦中心・真の残差と発散を同時に保存します。

##### 非周期壁面の製造解：速度・剪断・圧力演算子 (`wall-manufactured`)

[非周期壁面の製造非圧縮流](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json)

キャビティと同じ壁条件付き2Dソルバーに解析外力を与え、速度と流れ関数の格子収束、壁渦度・壁剪断の誤差を測ります。別の非零Dirichlet圧力製造解でPoisson・勾配の境界演算子も検査します。

##### KHの初期成長：滑らかな周期せん断層 (`kh-initial-growth`)

[KHの初期成長：滑らかな周期せん断層](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/verification.json)

実際の非線形2D渦度方程式を解き、独立Fourier–Galerkin線形初期値問題と有限時間の成長・格子誤差を比較します。

##### RTの初期成長：滑らかなBoussinesq二層 (`rt-initial-growth`)

[RTの初期成長：滑らかなBoussinesq二層](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/verification.json)

密度差を浮力だけに残す2D Boussinesq系を時間発展し、不安定な滑らかな層の初期成長を独立線形参照で調べます。

##### 純Neumannの互換条件と平均値ゲージ (`poisson-neumann`)

[純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

特異な2D Poissonを互換条件と指定平均込みで解き、不適合な外力を拒否します。

##### 2D混合Robinの製造解と境界流束 (`poisson-robin`)

[2D混合Robinの製造解と境界流束](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

2D PoissonのNeumann/Robin面を実際に組み、連続製造解と境界fluxを照合します。

##### 2D C-grid回転浅水波の実時間発展 (`cgrid-rotating-wave`)

[2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json)

実際の2D staggered場を時間積分し、連続波と離散symbolの参照を分けて比較します。

##### 擬似弧長継続でBratuのfoldを越える (`bratu-fold-continuation`)

[擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json)

同じ1次元Bratu境界値問題の下枝から上枝までを追跡し、接線・fold・独立解析族との空間誤差を調べます。

##### 解析・中央差分・方向ADによるJacobian不要Newton–Krylov (`bratu-matrix-free-jfnk`)

[解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json)

非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。

##### 離散fold近傍のBratu感度 (`bratu-fold-sensitivity`)

[離散fold近傍のBratu感度](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

離散Bratuのfoldへ近づく6固定点で、状態誤差と線形許容差の影響を分け、独立shooting勾配と照合します。

##### 分布係数Bratuの行列非形成VJP (`bratu-distributed-vjp`)

[分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

2重みだけの局所hat作用で8/16/32個の空間係数を表し、目的関数ごとの随伴VJPを全感度参照と比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

反応拡散：空間2次と時間4次を分けて測る: 線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。 Turing不安定性：線形成長率と小振幅パターン: Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。 Schnakenberg有限振幅過渡：非線形性と独立参照: t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。 Schnakenberg飽和パターン：近定常性と格子・時間収束: t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。 非周期壁面の2D渦度・流れ関数法でRe100蓋駆動キャビティと製造流れを解きます。Ghia原著の有限格子数値表、壁剪断と格子収束を比較し、独立した圧力Poisson・勾配製造問題を区別します。 追加の周期2D KH/RT初期成長は、維持した滑らかな基底と独立線形IVPを使用。中央の保存面流束とHeunで渦度/浮力を実際に進め、圧力は消去します。 追加は2Dセル中心PoissonのNeumann/Robin境界。実際の五点面流束と半セルRobin消去、適合条件・平均ゲージ・境界流束誤差を確認します。 追加は実際の2D線形回転浅水C-grid。staggered勾配・発散・随伴な4点Coriolis補間を使い、連続波と離散記号を分けて比較します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)
- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/models.py)
- [/code/validated-examples/2026-11-22/biology/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/run.py)
- [/code/validated-examples/2026-11-22/biology/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/biology.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/run.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/wall_flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/wall_flow.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/references/qualify_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/references/qualify_reference.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/run.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/flow.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/references/linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/references/linear.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/history/reference-attempt-01/references/linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/history/reference-attempt-01/references/linear.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/run.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/boundary.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/fem.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/annulus.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/annulus.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/experiments.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py)
- [/code/validated-examples/2026-11-23/moving-waves/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/run.py)
- [/code/validated-examples/2026-11-23/moving-waves/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/transport.py)
- [/code/validated-examples/2026-11-23/moving-waves/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/references/exact.py)
- [/code/validated-examples/2026-11-23/moving-waves/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/experiments.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py)
- [/code/validated-examples/2026-11-24/adjoint/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/run.py)
- [/code/validated-examples/2026-11-24/adjoint/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/operators.py)
- [/code/validated-examples/2026-11-24/adjoint/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/newton.py)
- [/code/validated-examples/2026-11-24/adjoint/fold_study.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/fold_study.py)
- [/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py)
- [/code/validated-examples/2026-11-24/adjoint/balanced_operator.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/balanced_operator.py)
- [/code/validated-examples/2026-11-24/adjoint/state_linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_linear.py)
- [/code/validated-examples/2026-11-24/adjoint/state_expansion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_expansion.py)
- [/code/validated-examples/2026-11-24/adjoint/state_krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/state_jacobian.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_jacobian.py)
- [/code/validated-examples/2026-11-24/adjoint/distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/time_adjoint.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/time_adjoint.py)
- [/code/validated-examples/2026-11-24/adjoint/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/io_contract.py)
- [/code/validated-examples/2026-11-24/adjoint/qualify_references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/qualify_references.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/conftest.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/conftest.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)
- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)
- [/code/validated-examples/2026-11-22/biology/test_biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/test_biology.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_result_envelope.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_result_envelope.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_serialization.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_wall_flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_wall_flow.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/test_instability.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/test_instability.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py)
- [/code/validated-examples/2026-11-23/moving-waves/test_moving.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/test_moving.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_time.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_time.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_numerics.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`; heat-periodic, heat-dirichlet, reaction-diffusion-fourier)
- [Schnakenberg reaction–diffusion](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-schnakenberg-en) (`bio-schnakenberg`; turing-schnakenberg)
- [Turing reaction–diffusion framework](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-turing-en) (`bio-turing`; turing-schnakenberg)
- [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en) (`navier-stokes`; lid-driven-cavity)
- [Isothermal lattice BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en) (`bgk`; lid-driven-cavity)
- [Forced incompressible flow and wall manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-incompressible-en) (`forced-incompressible`; wall-manufactured)
- [Forced vorticity about a maintained shear layer](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-vorticity-en) (`forced-vorticity`; kh-initial-growth)
- [Boussinesq vorticity with active buoyancy](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#boussinesq-buoyancy-en) (`boussinesq-buoyancy`; rt-initial-growth)
- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; poisson-neumann, poisson-robin)
- [Linear rotating shallow-water equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-rotating-shallow-water-en) (`linear-rotating-shallow-water`; cgrid-rotating-wave)
- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`; bratu-fold-continuation, bratu-matrix-free-jfnk, bratu-fold-sensitivity, bratu-distributed-vjp)

#### Problem figures (`method-problems-en`)

##### [Periodic Fourier-mode heat decay](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en) (`heat-periodic`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Heat decay with Dirichlet boundaries](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en) (`heat-dirichlet`)

![Shared figure, left: Dirichlet heat decay. Right: separate Poisson boundary problems.](https://hrkoyama.github.io/numerical-methods-atlas/assets/diffusion-boundaries.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en) (`reaction-diffusion-fourier`)

![Stored linear periodic Fourier reaction–diffusion refinement separates continuum errors on 16/32/64 grids from temporal errors against a fixed-grid semidiscrete exact solution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en#code-en)

- [Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en) (`reaction-diffusion-fourier`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.

##### [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

![Schnakenberg-type a=0.1,b=0.9 and diffusivities 0.01/1: stored linear errors/growth against a matrix exponential and a small nonlinear onset pattern at t=4.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

- [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en) (`turing-schnakenberg`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.

- [Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en) (`schnakenberg-nonlinear`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.

- [Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en) (`schnakenberg-pattern`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.

##### [Re100 lid-driven cavity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en) (`lid-driven-cavity`)

![Saved finest Re100 streamlines and speed. Red dot: computed grid primary vortex; hollow dot: original Ghia TableV location.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

Advance vorticity transport with centered differences and Heun. Each stage solves−Delta_h psi=omega using a nonperiodic Dirichlet DST, then formsu=psi_y,v=−psi_x. Use local first-order Thom wall vorticity; this is an independent method, not Ghia CSI-MG or its higher-order wall formula.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#code-en)

- [Re100 lid-driven cavity: Ghia centerline comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en) (`cavity-ghia-re100`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

March a real nonperiodic 2D viscous incompressible solver to steady state on 17/33/65 node grids and compare against original Ghia centerlines. Retain streamlines, grid vortex center, true PDE residual and discrete divergence.

##### [Manufactured incompressible flow with nonperiodic walls](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en) (`wall-manufactured`)

![Computed finest manufactured-flow streamlines and velocity error, using the same Thom closure as the cavity without exact wall-vorticity injection.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured-preview.png)

Use the shared centered FD/Heun/nonperiodic Dirichlet DST solver. Qualify explicit analytic derivatives against independently differentiated tensor coefficients. Separately solve nonzero-Dirichlet Poisson forp=x²+y²+sin(pi*x)sin(pi*y), checking central interior and second-order one-sided boundary gradients.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en#code-en)

- [Nonperiodic wall MMS: velocity, shear and pressure operator](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en) (`wall-manufactured`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

Apply analytic forcing to the same wall-bounded2D solver, measuring grid convergence of velocity/streamfunction and actual wall-vorticity/shear errors. A separate nonzero-Dirichlet manufactured pressure verifies Poisson and boundary-gradient operators.

##### [KH initial growth in a smooth periodic shear layer](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en) (`kh-initial-growth`)

![Saved actual2D perturbation vorticity normalized by epsilon; color scale and linear-reference growth are explicit.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth-preview.png)

Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en#code-en)

- [KH initial growth in a smooth periodic shear layer](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en) (`kh-initial-growth`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip)

Evolve the actual nonlinear2D vorticity PDE and compare finite-time growth and spatial errors with an independent continuous Fourier–Galerkin linear IVP.

##### [RT initial growth in smooth Boussinesq double layers](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en) (`rt-initial-growth`)

![Saved actual2D buoyancy perturbation normalized by epsilon; an early smooth-layer displacement, not turbulent mixing.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth-preview.png)

Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en#code-en)

- [RT initial growth in smooth Boussinesq double layers](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en) (`rt-initial-growth`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip)

Advance the actual2D Boussinesq vorticity/active-buoyancy system and compare smooth unstable-layer growth with a separately derived linear IVP.

##### [Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en) (`poisson-neumann`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png)

Shared-face differences, weighted-mean augmented solve and compatible CG comparison; no physical RHS mean projection.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en#code-en)

- [Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en) (`poisson-neumann`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

Solve singular2D Poisson with compatibility/gauge and reject incompatible source.

##### [2D mixed Robin MMS and boundary flux](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en) (`poisson-robin`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin-preview.png)

Eliminate Robin trace at half-cell distance, using the same outward-gradient face weights in the discrete PDE and budget.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en#code-en)

- [2D mixed Robin MMS and boundary flux](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en) (`poisson-robin`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

Assemble actual2D Neumann/Robin faces and compare the manufactured field and boundary flux.

##### [Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en) (`cgrid-rotating-wave`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave-preview.png)

Actual2D cell-height/face-velocity differences and four-point Coriolis interpolation use RK4. The3×3 matrix exponential is reference-only, never the PDE update.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en#code-en)

- [Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en) (`cgrid-rotating-wave`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

Time-advance actual2D staggered fields and distinguish continuous-wave references from semidiscrete symbols.

##### [Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en) (`bratu-fold-continuation`)

![Preview of the stored branch,lambda=2 profiles,smallest Jacobian singular value and three-grid fold error. Arclength steps are not physical time.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png)

Use a unit tangent in h-sum(du squared)+d-lambda squared, a predictor and a tangent-hyperplane Newton corrector. A separate augmented system locates the fold and a normalized null vector. This case deliberately assembles sparse Jacobians.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en#code-en)

- [Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en) (`bratu-fold-continuation`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

Follow the lower and upper branches of the same one-dimensional Bratu boundary-value problem; check tangents, the fold and spatial error against an independent analytic family.

##### [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en) (`bratu-matrix-free-jfnk`)

![Preview of stored N=127 Newton residuals,upper-branch field/reference,Jv errors and actual evaluation counts. Run indices match the saved CSV.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png)

Use analytic Jv, a two-residual central difference, or one-direction forward AD. Apply a Poisson Thomas right preconditioner with two-pass reorthogonalized GMRES/Givens. Start eta=.3, then clamp .9*(Fk/Fk-1)^1.5 to [.001,.5]. This is an explicit EW Choice2-style variant, not the paper’s full safeguards or PETSc defaults.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en#code-en)

- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en) (`bratu-matrix-free-jfnk`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

Solve both Bratu branches with three Jv choices without assembling the nonlinear Jacobian; retain forcing, actual residuals and evaluation counts.

##### [Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en) (`bratu-fold-sensitivity`)

![Bratu sensitivity near the discrete fold. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity-preview.png)

Analytic Jv, Poisson-Thomas right preconditioning and the preserved GMRES body solve tangents/adjoints. Save every rtol, returned candidate, true residual, termination and roundoff scale. Qualify the discrete oracle through shooting and separate high-precision Thomas-Newton. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en#code-en)

- [Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en) (`bratu-fold-sensitivity`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

At six fixed points approaching the discrete Bratu fold, separate state error from linear-solve tolerance and compare against independent shooting gradients.

##### [Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en) (`bratu-distributed-vjp`)

![Matrix-free VJP for distributed Bratu coefficients. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png)

Bv uses local gather and B transpose scatter-add. Primary solves use Jv without an n-by-m matrix. One shared Poisson factor serves the one/three-objective runs on the same state. Dense hats and m tangent RHS are allowed only in the separate reference window. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en#code-en)

- [Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en) (`bratu-distributed-vjp`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

Represent8/16/32 spatial controls with two local hat weights per node; compare objective-wise adjoint VJPs with a separate full-sensitivity reference.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic Fourier-mode heat decay](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#references-en) (`heat-periodic`)

- [Heat / Fourier-mode decay](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-heat-en) (`sine-heat`; Related-model reference; Analytic reference)

The saved gallery matches periodic [0,1], 1+0.25sin(2πx), ν=0.02 and final time one; this does not assert a match to separate-frequency code checks. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-heat)

##### [Heat decay with Dirichlet boundaries](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en#references-en) (`heat-dirichlet`)

- [Heat / Fourier-mode decay](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-heat-en) (`sine-heat`; Related-model reference; Analytic reference)

This test has zero Dirichlet endpoints and sin(πx); the card has periodic boundaries, 1+0.25sin(2πx) and ν=0.02.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-heat)

##### [Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en#references-en) (`reaction-diffusion-fourier`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#references-en) (`turing-schnakenberg`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Re100 lid-driven cavity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#references-en) (`lid-driven-cavity`)

- [Ghia Re100: original finite-grid velocity centerlines](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ghia-re100-en) (`ghia-re100`; Same-problem reference; Finite-grid numerical reference)

Educational Re100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed.

[Existing reference profile](/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en#cavity-ghia-re100-en-measurements)

- [LBM Re100 cavity: actual2D fields and Ghia centerlines](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cavity-re100-en) (`lbm-cavity-re100`; Related-model reference; Finite-grid numerical reference)

Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest.

[Existing reference profile](/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en#lbm-cavity-re100-en-measurements)

##### [Manufactured incompressible flow with nonperiodic walls](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en#references-en) (`wall-manufactured`)

- [Wall manufactured solution: polynomial velocity and separate pressure operator](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-wall-mms-en) (`wall-mms`; Same-problem reference; Manufactured solution)

Thom wall vorticity has first-order local truncation; publish observed shear rates without promising second order. Pressure is eliminated from streamfunction evolution, so a pressure gauge is inapplicable. The separate operator MMS does not verify cavity pressure, traction boundaries or MAC projection. Independent polynomial differentiation is distinct from comparison with an independent flow solver.

[Existing reference profile](/numerical-methods-atlas/validation/wall-manufactured/?lang=en#wall-manufactured-en-measurements)

##### [KH initial growth in a smooth periodic shear layer](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en#references-en) (`kh-initial-growth`)

- [KH initial growth: independent linear Fourier-Galerkin reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kh-initial-growth-en) (`kh-initial-growth`; Same-problem reference; Finite-grid numerical reference)

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.

[Existing reference profile](/numerical-methods-atlas/validation/kh-initial-growth/?lang=en#kh-initial-growth-en-measurements)

##### [RT initial growth in smooth Boussinesq double layers](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en#references-en) (`rt-initial-growth`)

- [RT initial growth: linear Boussinesq double-layer IVP reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rt-initial-growth-en) (`rt-initial-growth`; Same-problem reference; Finite-grid numerical reference)

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.

[Existing reference profile](/numerical-methods-atlas/validation/rt-initial-growth/?lang=en#rt-initial-growth-en-measurements)

##### [Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en#references-en) (`poisson-neumann`)

- [Pure Neumann: analytic field, compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-neumann-en) (`poisson-neumann`; Same-problem reference; Manufactured solution)

A different linear solver of the same matrix is not an independent PDE discretization; no general boundary/MG claim.

[Existing reference profile](/numerical-methods-atlas/validation/poisson-neumann/?lang=en#poisson-neumann-en-measurements)

##### [2D mixed Robin MMS and boundary flux](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en#references-en) (`poisson-robin`)

- [Mixed Robin: 2D analytic field and independent normal flux](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-robin-en) (`poisson-robin`; Same-problem reference; Manufactured solution)

The unique Robin problem has no additional mean gauge. Algebraic boundary satisfaction differs from physical flux accuracy.

[Existing reference profile](/numerical-methods-atlas/validation/poisson-robin/?lang=en#poisson-robin-en-measurements)

##### [Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en#references-en) (`cgrid-rotating-wave`)

- [C-grid: continuous Fourier solution and discrete-symbol exponential](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-cgrid-rotating-wave-en) (`cgrid-rotating-wave`; Same-problem reference; Analytic reference)

Linear planar periodic square only. Nonlinear SWE,PV,spherical dynamics and Williamson tests remain future work.

[Existing reference profile](/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en#cgrid-rotating-wave-en-measurements)

##### [Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en#references-en) (`bratu-fold-continuation`)

- [Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-fold-continuation-en) (`bratu-fold-continuation`; Same-problem reference; Analytic reference)

A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.

[Existing reference profile](/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en#bratu-fold-continuation-en-measurements)

##### [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en#references-en) (`bratu-matrix-free-jfnk`)

- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-matrix-free-jfnk-en) (`bratu-matrix-free-jfnk`; Same-problem reference; Analytic reference)

An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee.

[Existing reference profile](/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en#bratu-matrix-free-jfnk-en-measurements)

##### [Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en#references-en) (`bratu-fold-sensitivity`)

- [Discrete Bratu shooting, tangent and adjoint references near a fold](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-fold-sensitivity-en) (`bratu-fold-sensitivity`; Same-problem reference; Finite-grid numerical reference)

The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

[Existing reference profile](/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en#bratu-fold-sensitivity-en-measurements)

##### [Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en#references-en) (`bratu-distributed-vjp`)

- [Independent dense sensitivities and matrix-free VJPs for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-distributed-vjp-en) (`bratu-distributed-vjp`; Same-problem reference; Finite-grid numerical reference)

Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

[Existing reference profile](/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en#bratu-distributed-vjp-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/stability/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Reaction-diffusion: separate second-order space and fourth-order time (`reaction-diffusion-fourier`)

[Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.

##### Turing instability: linear growth and small-amplitude patterns (`turing-schnakenberg`)

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.

##### Finite-amplitude Schnakenberg transient: nonlinearity and independent reference (`schnakenberg-nonlinear`)

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json)

Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.

##### Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence (`schnakenberg-pattern`)

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json)

Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.

##### Re100 lid-driven cavity: Ghia centerline comparison (`cavity-ghia-re100`)

[Re100 lid-driven cavity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json)

March a real nonperiodic 2D viscous incompressible solver to steady state on 17/33/65 node grids and compare against original Ghia centerlines. Retain streamlines, grid vortex center, true PDE residual and discrete divergence.

##### Nonperiodic wall MMS: velocity, shear and pressure operator (`wall-manufactured`)

[Manufactured incompressible flow with nonperiodic walls](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json)

Apply analytic forcing to the same wall-bounded2D solver, measuring grid convergence of velocity/streamfunction and actual wall-vorticity/shear errors. A separate nonzero-Dirichlet manufactured pressure verifies Poisson and boundary-gradient operators.

##### KH initial growth in a smooth periodic shear layer (`kh-initial-growth`)

[KH initial growth in a smooth periodic shear layer](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/verification.json)

Evolve the actual nonlinear2D vorticity PDE and compare finite-time growth and spatial errors with an independent continuous Fourier–Galerkin linear IVP.

##### RT initial growth in smooth Boussinesq double layers (`rt-initial-growth`)

[RT initial growth in smooth Boussinesq double layers](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/verification.json)

Advance the actual2D Boussinesq vorticity/active-buoyancy system and compare smooth unstable-layer growth with a separately derived linear IVP.

##### Pure Neumann compatibility and mean gauge (`poisson-neumann`)

[Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

Solve singular2D Poisson with compatibility/gauge and reject incompatible source.

##### 2D mixed Robin MMS and boundary flux (`poisson-robin`)

[2D mixed Robin MMS and boundary flux](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

Assemble actual2D Neumann/Robin faces and compare the manufactured field and boundary flux.

##### Actual2D C-grid rotating shallow-water time advance (`cgrid-rotating-wave`)

[Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json)

Time-advance actual2D staggered fields and distinguish continuous-wave references from semidiscrete symbols.

##### Crossing the Bratu fold with pseudo-arclength continuation (`bratu-fold-continuation`)

[Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json)

Follow the lower and upper branches of the same one-dimensional Bratu boundary-value problem; check tangents, the fold and spatial error against an independent analytic family.

##### Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products (`bratu-matrix-free-jfnk`)

[Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json)

Solve both Bratu branches with three Jv choices without assembling the nonlinear Jacobian; retain forcing, actual residuals and evaluation counts.

##### Bratu sensitivity near the discrete fold (`bratu-fold-sensitivity`)

[Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

At six fixed points approaching the discrete Bratu fold, separate state error from linear-solve tolerance and compare against independent shooting gradients.

##### Matrix-free VJP for distributed Bratu coefficients (`bratu-distributed-vjp`)

[Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

Represent8/16/32 spatial controls with two local hat weights per node; compare objective-wise adjoint VJPs with a separate full-sensitivity reference.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Reaction-diffusion: separate second-order space and fourth-order time: Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions. Turing instability: linear growth and small-amplitude patterns: Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode. Finite-amplitude Schnakenberg transient: nonlinearity and independent reference: Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics. Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence: Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual. Solve a Re100 lid-driven cavity and manufactured flow with a nonperiodic wall-bounded2D vorticity/streamfunction method. Compare original finite-grid Ghia tables, wall shear and grid refinement, keeping a separate pressure-Poisson/gradient manufactured problem distinct. Additional periodic2D KH/RT initial growth uses maintained smooth bases and independent linear IVPs; actual centered conservative face fluxes and Heun evolve vorticity/buoyancy with pressure eliminated. Additional2D cell-centered Poisson uses actual five-point face differences and half-cell Robin elimination; check Neumann compatibility/mean gauge and continuous boundary-flux error. Additional actual2D linear rotating-SWE C-grid uses staggered gradients/divergence and adjoint four-point Coriolis interpolation; separate continuous and discrete-symbol references.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)
- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/models.py)
- [/code/validated-examples/2026-11-22/biology/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/run.py)
- [/code/validated-examples/2026-11-22/biology/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/biology.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/run.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/wall_flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/wall_flow.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/references/qualify_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/references/qualify_reference.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/run.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/flow.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/references/linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/references/linear.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/history/reference-attempt-01/references/linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/history/reference-attempt-01/references/linear.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/run.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/boundary.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/fem.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/annulus.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/annulus.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/experiments.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py)
- [/code/validated-examples/2026-11-23/moving-waves/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/run.py)
- [/code/validated-examples/2026-11-23/moving-waves/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/transport.py)
- [/code/validated-examples/2026-11-23/moving-waves/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/references/exact.py)
- [/code/validated-examples/2026-11-23/moving-waves/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/experiments.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py)
- [/code/validated-examples/2026-11-24/adjoint/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/run.py)
- [/code/validated-examples/2026-11-24/adjoint/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/operators.py)
- [/code/validated-examples/2026-11-24/adjoint/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/newton.py)
- [/code/validated-examples/2026-11-24/adjoint/fold_study.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/fold_study.py)
- [/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py)
- [/code/validated-examples/2026-11-24/adjoint/balanced_operator.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/balanced_operator.py)
- [/code/validated-examples/2026-11-24/adjoint/state_linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_linear.py)
- [/code/validated-examples/2026-11-24/adjoint/state_expansion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_expansion.py)
- [/code/validated-examples/2026-11-24/adjoint/state_krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/state_jacobian.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_jacobian.py)
- [/code/validated-examples/2026-11-24/adjoint/distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/time_adjoint.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/time_adjoint.py)
- [/code/validated-examples/2026-11-24/adjoint/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/io_contract.py)
- [/code/validated-examples/2026-11-24/adjoint/qualify_references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/qualify_references.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/conftest.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/conftest.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)
- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)
- [/code/validated-examples/2026-11-22/biology/test_biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/test_biology.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_result_envelope.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_result_envelope.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_serialization.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_wall_flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_wall_flow.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/test_instability.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/test_instability.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py)
- [/code/validated-examples/2026-11-23/moving-waves/test_moving.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/test_moving.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_time.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_time.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_numerics.py
```
