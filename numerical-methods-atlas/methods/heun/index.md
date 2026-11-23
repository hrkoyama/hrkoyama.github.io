# Heun / SSPRK(2,2) / Heun法／SSPRK(2,2)

Status: educational-example

Read about Heun / SSPRK(2,2), follow the original references and inspect related educational code and checks.

「Heun法／SSPRK(2,2)」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: ホイン法, SSPRK22, SSPRK2, SSP RK2, explicit trapezoidal method, 陽的台形則

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py

- Reference: https://doi.org/10.1175/2009MWR2724.1 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity. The additional2D Cartesian Noh edition updates both x/y fluxes and both momenta on a full square. The additional spherical Sedov blast measures grid and finite deposition-radius effects separately. The additional forward-step example verifies actual 2D finite-volume flow with reflecting walls including the step faces. The additional Guderley example evolves a zero-upstream-pressure spherical converging shock only before collapse and compares a semi-analytic similarity reference. Solve a Re100 lid-driven cavity and manufactured flow with a nonperiodic wall-bounded2D vorticity/streamfunction method. Compare original finite-grid Ghia tables, wall shear and grid refinement, keeping a separate pressure-Poisson/gradient manufactured problem distinct. Additional periodic2D KH/RT initial growth uses maintained smooth bases and independent linear IVPs; actual centered conservative face fluxes and Heun evolve vorticity/buoyancy with pressure eliminated. Additional full-state1D CP wave and actual2D magnetic-loop/Orszag–Tang use HLLD,MC-MUSCL and Heun. Count HLLD-to-HLLE fallback and face positivity scaling,with no cell floor or PDE retry. Additional ALE scalar advances face positions and mass with the same two-stage Heun weights,checking boundary budgets,GCL and an independent time reference.

初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。 追加の2D Cartesian Noh版は正方形全域のx/y流束と2成分運動量を更新する軽量例です。 Sedov球対称爆発の追加例では、有限半径へのエネルギー投入と格子の影響を分けて測ります。 追加の前向きステップ例は段差面を含む反射壁境界の実2D有限体積計算を検証します。 追加のGuderley例は、圧力ゼロの上流へ進む球対称収束衝撃波を原点到達前だけ計算し、半解析的な相似参照と比較します。 非周期壁面の2D渦度・流れ関数法でRe100蓋駆動キャビティと製造流れを解きます。Ghia原著の有限格子数値表、壁剪断と格子収束を比較し、独立した圧力Poisson・勾配製造問題を区別します。 追加の周期2D KH/RT初期成長は、維持した滑らかな基底と独立線形IVPを使用。中央の保存面流束とHeunで渦度/浮力を実際に進め、圧力は消去します。 追加の全成分1D円偏波と実際の2D磁場ループ/Orszag–TangでHLLD・MC-MUSCL・Heunを使用。HLLD→HLLE代替と面の正値性スケーリングを数え、セルfloorや再試行は行いません。 追加ALEスカラーは面位置と質量を同じ2段Heunで更新し、同じ段重みの境界収支・GCLと独立時間参照を比較します。

- Noh shocks: zero-pressure planar, cylindrical and spherical flow: https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/result.json

- Noh problem: an actual 2D Cartesian Euler calculation: https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/result.json

- Sedov–Taylor point blast: lightweight spherical-radial validation: https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/atlas-sedov-2026-11-23-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/results/result.json

- Double Mach reflection: lightweight grid verification: https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/atlas-double-mach-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/result.json

- Mach3 forward step: wall budgets and grid verification: https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/atlas-forward-step-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/result.json

- Guderley converging shock: lightweight spherical-radial verification: https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/atlas-guderley-2026-11-23-r3.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/result.json

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

- Circular Alfven wave: full-state refinement: https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/
- Magnetic loop: independent 2D reference and refinement: https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/
- Late Orszag-Tang: independent reference and compression structure: https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/result.json

- ALE scalar transport on genuinely nonuniform moving cells: https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/result.json

Common execution records: [{"id": "noh-shock", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "noh-cartesian-2d", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "sedov-blast", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "double-mach-reflection", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "forward-step-m3", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "guderley-implosion", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "cavity-ghia-re100", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "wall-manufactured", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "kh-initial-growth", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "rt-initial-growth", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "circular-alfven-refinement", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "magnetic-loop-independent", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "postshock-orszag-tang", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "ale-nonuniform-transport", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; double-mach, forward-step, noh, sedov, guderley)
- [理想MHD](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#mhd-ja) (`mhd`; orszag-tang, circular-alfven, magnetic-loop)
- [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja) (`navier-stokes`; lid-driven-cavity)
- [外力付き非圧縮流と壁面製造解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-incompressible-ja) (`forced-incompressible`; wall-manufactured)
- [維持されたせん断層の強制渦度系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-vorticity-ja) (`forced-vorticity`; kh-initial-growth)
- [能動浮力を伴うBoussinesq渦度系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#boussinesq-buoyancy-ja) (`boussinesq-buoyancy`; rt-initial-growth)
- [移動セル上のALEスカラー保存式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#ale-scalar-transport-ja) (`ale-scalar-transport`; ale-nonuniform-transport)

#### 問題の図 (`method-problems-ja`)

##### [二重Mach反射](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja) (`double-mach`)

![実際の2次元Euler計算の密度場。Mach10、γ=1.4、T=.2、256×64セル。保存済みの別実装FV参照への差とwall jet診断を示します。細い噴流・渦構造の収束を保証する図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection-preview.png)

既存のGodunov/HLL像と、新しい区分定数HLL＋Heunの固定入力を区別します。各実行例にはその計算で実際に使う手法だけを結びます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#code-ja)

- [Double Mach反射：多格子の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja) (`double-mach-reflection`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/atlas-double-mach-2026-11-23.zip)

既存のDouble Mach反射と同じ初期値・境界を使い、64×16・128×32・256×64の実2D Euler有限体積計算をT=.2まで実行します。別実装の有限格子参照との差、実際の境界流束収支、上部の入射衝撃位置と壁近傍を比較します。

##### [Mach 3前向きステップ](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja) (`forward-step`)

![実際の2次元Euler計算の密度場。Mach 3、γ=1.4、T=4、240×80セル。固体段差を除いて描きます。角のエントロピー補正は使わず、微細なすべり線・渦の収束を保証する図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png)

従来のHLL・MUSCLと勾配制限の比較データを保持し、追加の軽量例は区分定数HLL＋Heunを使います。参照実装の手法は参照の出典と条件で区別します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#code-ja)

- [Mach 3前向きステップ：壁面収支と多格子検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja) (`forward-step-m3`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/atlas-forward-step-2026-11-23.zip)

実際の2次元Euler有限体積計算を60×20・120×40・240×80でT=4まで行い、別実装のMUSCL有限格子参照と比較します。段差の垂直面・上面を含む実際の数値流束から4保存量の収支を評価し、角のエントロピー補正を加えない変種として図とコードを公開します。

##### [Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja) (`orszag-tang`)

![CT・GLMを統合した1問題のうち、CTの保存フレームを代表表示。](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#code-ja)

- [後期Orszag–Tang：独立参照と圧縮構造](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja) (`postshock-orszag-tang`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip)

圧縮性理想MHDのOrszag–TangをT=.2まで進め、相互作用する圧縮・衝撃波構造の密度と圧力を独立有限格子参照で検査します。

##### [円偏波Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja) (`circular-alfven`)

![保存済み円偏波Alfvén波の誤差・収束比較。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja#code-ja)

- [円偏波Alfvén波：全成分の格子収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja) (`circular-alfven-refinement`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip)

全8保存変数を進め、非零のBz・vzを含む円偏波を解析セル平均と比較します。

##### [磁場ループの移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja) (`magnetic-loop`)

![保存済み磁場ループ移流の計算場。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#code-ja)

- [磁場ループ：独立2次元参照と細分化](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja) (`magnetic-loop-independent`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip)

実際の2次元磁場ループ輸送を、別実装Athena++の空間・時間感度を検査した終端保存場と比較します。

##### [指数関数を厳密解に持つ非線形・非自律ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja) (`nonlinear-exp-ode`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-exp-ode.png)

公開の全陽的RK tableauに対する非自律・非線形製造解の検査です。保存プレビューはRK4を使います。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [有理減衰ODE（y′ = −y²）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja) (`nonlinear-rational-decay`)

![保存済み有理減衰ODEの時間刻み収束（代表3手法）。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-decay.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Noh問題：冷たい収束流と外向き衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) (`noh`)

![実際の2次元Cartesian Euler計算の密度場。正方形全域128²セル、初期圧力ゼロ、γ=5/3、t=.6。白破線は厳密衝撃円。軸・対角方向の差と原点過熱を残し、1D半径例にも辿れます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d-preview.png)

RusanovとHeunは1D半径例と新2D Cartesian例で使用。MUSCL/minmodは旧球対称系列に限定され、新2D版は区分定数です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#code-ja)

- [Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja) (`noh-shock`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip)

初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。

- [Noh問題：実際の2次元Cartesian Euler計算](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja) (`noh-cartesian-2d`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip)

正方形の全域で密度・2成分運動量・全エネルギーを更新する、小型の2次元Euler有限体積計算です。32²・64²・128²の3格子で厳密Noh状態からの誤差・保存収支・格子方向の影響を測ります。図は実際の2次元保存配列で、1D半径解の回転表示ではありません。

##### [Sedov–Taylorの点爆発](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja) (`sedov`)

![1次元球対称Eulerの保存済み半径密度を中心断面に表示。γ=5/3、E=ρ0=1、p0=0、t=.05、512球殻、有限投入半径.03。半解析的な点源参照との違いと衝撃層の誤差を残した図で、実2D Cartesian計算ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/results/sedov-blast-preview.png)

区分定数のRusanov有限体積流束とSSPRK2/Heunを使う限定した球半径例です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja#code-ja)

- [Sedov–Taylor点爆発：球対称の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja) (`sedov-blast`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/atlas-sedov-2026-11-23-r2.zip)

球対称Euler方程式を半径方向の有限体積法で解く軽量例です。固定した半径0.03の領域に総エネルギー1を与え、128・256・512セルで点爆発の相似参照からの差と保存収支を測ります。図は1次元球対称データの断面表示で、2次元Cartesian計算ではありません。

##### [Guderleyの収束衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja) (`guderley`)

![1次元球対称Eulerの保存済み半径密度を子午面に表示。γ=1.4、512球殻、r∈\[0,.75\]、R_s(−1)=.6、t=−.85。圧力ゼロの静止上流へ進む収束前の衝撃波を半解析参照と比較します。2D Cartesianや原点反射後の計算ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/guderley-implosion-preview.png)

球殻の面積・体積と幾何学的な圧力源を使う区分定数HLL有限体積流束、物理時間のHeun更新による限定例です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja#code-ja)

- [Guderley収束衝撃波：球対称の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja) (`guderley-implosion`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/atlas-guderley-2026-11-23-r3.zip)

冷たい静止気体へ内向きに進む球対称Guderley衝撃波を、128/256/512個の球殻でt=−1から−.85まで計算します。HLL流束とHeun法を、相似指数の固有値・半解析場・衝撃位置・保存収支と照合する軽量例です。

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

##### [非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja) (`ale-nonuniform-transport`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png)

実セル質量の上流相対流束(a−w)qと実面位置を同じHeun predictor/correctorで進め、各段体積・面Courant数を記録。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja#code-ja)

- [非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja) (`ale-nonuniform-transport`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

質量と格子面位置を同じHeun段で更新し、一様GCLだけでなく非一様な解析波を運びます。


#### 厳密解・参照解 (`method-references-ja`)

##### [二重Mach反射](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#references-ja) (`double-mach`)

- [Double Mach反射：保存済み独立有限格子数値参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-double-mach-ja) (`double-mach`; 同じ問題の参照; 有限格子の数値参照)

以前に独立実行した2格子の有限体積参照を保存量制限で比較します。有限格子数値参照であり、厳密2D解や誤差上界ではありません。

[既存の参照図](/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja#double-mach-reflection-ja-measurements)

##### [Mach 3前向きステップ](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#references-ja) (`forward-step`)

- [Mach 3前向きステップ：独立C++有限格子数値参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-forward-step-ja) (`forward-step`; 同じ問題の参照; 有限格子の数値参照)

新しく独立実行したC++17のMUSCL/HLL/Heun参照を保存量制限で比較します。同じHLL族・Heunと角無補正条件を共有する有限格子数値参照であり、全場の厳密解や誤差上界ではありません。

[既存の参照図](/numerical-methods-atlas/validation/forward-step-m3/?lang=ja#forward-step-m3-ja-measurements)

##### [Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#references-ja) (`orszag-tang`)

- [後期Orszag–Tang：独立有限格子の密度・圧力参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-postshock-orszag-tang-ja) (`postshock-orszag-tang`; 関連モデルの参照; 有限格子の数値参照)

γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。

[既存の参照図](/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja#postshock-orszag-tang-ja-measurements)

##### [円偏波Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja#references-ja) (`circular-alfven`)

- [円偏波Alfvén波：全保存変数の解析セル平均](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-circular-alfven-refinement-ja) (`circular-alfven-refinement`; 関連モデルの参照; 解析参照)

γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。

[既存の参照図](/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja#circular-alfven-refinement-ja-measurements)

##### [磁場ループの移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#references-ja) (`magnetic-loop`)

- [磁場ループ：固定Athena++の独立終端参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-magnetic-loop-independent-ja) (`magnetic-loop-independent`; 関連モデルの参照; 有限格子の数値参照)

[-1,1]×[-.5,.5]周期、ρ=p=1、Az=.001max(.3−r,0)、T=1、(Nx,Ny)=(16,8),(32,16),(64,32)。変更していない公式生成器と同じv=(2,1,2)で、古いvz=0設定とは区別します。

[既存の参照図](/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja#magnetic-loop-independent-ja-measurements)

##### [指数関数を厳密解に持つ非線形・非自律ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja#references-ja) (`nonlinear-exp-ode`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [有理減衰ODE（y′ = −y²）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja#references-ja) (`nonlinear-rational-decay`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Noh問題：冷たい収束流と外向き衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#references-ja) (`noh`)

- [Nohの冷たい流入衝撃波：平面・円筒・球対称](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja) (`noh`; 同じ問題の参照; 解析参照)

同じNoh問題の解析参照。1Dは保存量の厳密体積平均、2Dは衝撃円で分割した密度の求積セル平均を使用します。点値とセル平均、p(平均U)と平均pを区別します。

[既存の参照図](/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-measurements)

##### [Sedov–Taylorの点爆発](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja#references-ja) (`sedov`)

- [Sedov–Taylorの点爆発：エネルギー正規化した球対称自己相似解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sedov-ja) (`sedov`; 同じ問題の参照; 半解析参照)

エネルギー正規化した球対称の自己相似参照。相似ODEの数値積分・球殻平均の求積を含む半解析解で、閉形式の厳密セル平均とは区別します。有限半径の投入初期値は理想点爆発の特異初期値と一致しません。 固定した有限の投入半径で点源の自己相似参照と比べるため、誤差曲線には投入モデルの差も含まれ、純粋な空間精度の収束次数ではありません。同じ最細格子で投入半径を変える比較は感度診断であり、連続極限の投入誤差とPDE離散化誤差を完全に分離する検証ではありません。

[既存の参照図](/numerical-methods-atlas/validation/sedov-blast/?lang=ja#sedov-blast-ja-measurements)

##### [Guderleyの収束衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja#references-ja) (`guderley`)

- [Guderley収束衝撃波：固有値と球対称の半解析参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-guderley-ja) (`guderley`; 同じ問題の参照; 半解析参照)

γ=1.4・冷たい一様な上流を持つ球対称Guderley相似解の収束前分岐です。相似指数の固有値探索・相似ODE積分・衝撃位置で分割した球殻求積を含む半解析参照で、閉形式の厳密セル平均ではありません。通常追試は保存済みの資格確認で求めたλを再利用して相似ODEと求積を再実行し、固有値探索と元ExactPack点照合の再生成は別の明示コマンドとします。参照は固定ExactPackに基づくアダプターであり、独立に実装した相似解との照合とは扱いません。原点での収束、反射後の衝撃波、一般のEOSは今回の範囲外です。

[既存の参照図](/numerical-methods-atlas/validation/guderley-implosion/?lang=ja#guderley-implosion-ja-measurements)

##### [Re100の蓋駆動キャビティ](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#references-ja) (`lid-driven-cavity`)

- [Ghia Re100：原著の有限格子速度中心線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ghia-re100-ja) (`ghia-re100`; 同じ問題の参照; 有限格子の数値参照)

Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。

[既存の参照図](/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja#cavity-ghia-re100-ja-measurements)

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

##### [非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja#references-ja) (`ale-nonuniform-transport`)

- [ALE：実際の移動セル上の解析積分と時間参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ale-nonuniform-transport-ja) (`ale-nonuniform-transport`; 同じ問題の参照; 解析参照)

1D指定格子運動の第一段階です。図のx–tは2D物理計算ではなく、Euler Lagrange/remapやSaltzmanピストンは未実装の後続課題。

[既存の参照図](/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja#ale-nonuniform-transport-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Double Mach反射：多格子の軽量検証 (`double-mach-reflection`)

[二重Mach反射](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/atlas-double-mach-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/verification.json)

既存のDouble Mach反射と同じ初期値・境界を使い、64×16・128×32・256×64の実2D Euler有限体積計算をT=.2まで実行します。別実装の有限格子参照との差、実際の境界流束収支、上部の入射衝撃位置と壁近傍を比較します。

##### Mach 3前向きステップ：壁面収支と多格子検証 (`forward-step-m3`)

[Mach 3前向きステップ](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/atlas-forward-step-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/verification.json)

実際の2次元Euler有限体積計算を60×20・120×40・240×80でT=4まで行い、別実装のMUSCL有限格子参照と比較します。段差の垂直面・上面を含む実際の数値流束から4保存量の収支を評価し、角のエントロピー補正を加えない変種として図とコードを公開します。

##### 後期Orszag–Tang：独立参照と圧縮構造 (`postshock-orszag-tang`)

[Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/verification.json)

圧縮性理想MHDのOrszag–TangをT=.2まで進め、相互作用する圧縮・衝撃波構造の密度と圧力を独立有限格子参照で検査します。

##### 円偏波Alfvén波：全成分の格子収束 (`circular-alfven-refinement`)

[円偏波Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/verification.json)

全8保存変数を進め、非零のBz・vzを含む円偏波を解析セル平均と比較します。

##### 磁場ループ：独立2次元参照と細分化 (`magnetic-loop-independent`)

[磁場ループの移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/verification.json)

実際の2次元磁場ループ輸送を、別実装Athena++の空間・時間感度を検査した終端保存場と比較します。

##### Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算 (`noh-shock`)

[Noh問題：冷たい収束流と外向き衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/verification.json)

初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。

##### Noh問題：実際の2次元Cartesian Euler計算 (`noh-cartesian-2d`)

[Noh問題：冷たい収束流と外向き衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/verification.json)

正方形の全域で密度・2成分運動量・全エネルギーを更新する、小型の2次元Euler有限体積計算です。32²・64²・128²の3格子で厳密Noh状態からの誤差・保存収支・格子方向の影響を測ります。図は実際の2次元保存配列で、1D半径解の回転表示ではありません。

##### Sedov–Taylor点爆発：球対称の軽量検証 (`sedov-blast`)

[Sedov–Taylorの点爆発](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/atlas-sedov-2026-11-23-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/verification.json)

球対称Euler方程式を半径方向の有限体積法で解く軽量例です。固定した半径0.03の領域に総エネルギー1を与え、128・256・512セルで点爆発の相似参照からの差と保存収支を測ります。図は1次元球対称データの断面表示で、2次元Cartesian計算ではありません。

##### Guderley収束衝撃波：球対称の軽量検証 (`guderley-implosion`)

[Guderleyの収束衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/atlas-guderley-2026-11-23-r3.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/verification.json)

冷たい静止気体へ内向きに進む球対称Guderley衝撃波を、128/256/512個の球殻でt=−1から−.85まで計算します。HLL流束とHeun法を、相似指数の固有値・半解析場・衝撃位置・保存収支と照合する軽量例です。

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

##### 非一様移動格子で実際に運ぶALEスカラー (`ale-nonuniform-transport`)

[非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json)

質量と格子面位置を同じHeun段で更新し、一様GCLだけでなく非一様な解析波を運びます。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。 追加の2D Cartesian Noh版は正方形全域のx/y流束と2成分運動量を更新する軽量例です。 Sedov球対称爆発の追加例では、有限半径へのエネルギー投入と格子の影響を分けて測ります。 追加の前向きステップ例は段差面を含む反射壁境界の実2D有限体積計算を検証します。 追加のGuderley例は、圧力ゼロの上流へ進む球対称収束衝撃波を原点到達前だけ計算し、半解析的な相似参照と比較します。 非周期壁面の2D渦度・流れ関数法でRe100蓋駆動キャビティと製造流れを解きます。Ghia原著の有限格子数値表、壁剪断と格子収束を比較し、独立した圧力Poisson・勾配製造問題を区別します。 追加の周期2D KH/RT初期成長は、維持した滑らかな基底と独立線形IVPを使用。中央の保存面流束とHeunで渦度/浮力を実際に進め、圧力は消去します。 追加の全成分1D円偏波と実際の2D磁場ループ/Orszag–TangでHLLD・MC-MUSCL・Heunを使用。HLLD→HLLE代替と面の正値性スケーリングを数え、セルfloorや再試行は行いません。 追加ALEスカラーは面位置と質量を同じ2段Heunで更新し、同じ段重みの境界収支・GCLと独立時間参照を比較します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)
- [/code/validated-examples/2026-11-23-r5/noh/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/run.py)
- [/code/validated-examples/2026-11-23-r5/noh/noh_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/noh_solver.py)
- [/code/validated-examples/2026-11-23-r5/noh/noh_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/noh_reference.py)
- [/code/validated-examples/2026-11-23-r5/noh/generate_exactpack_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/generate_exactpack_reference.py)
- [/code/validated-examples/2026-11-23-r5/noh/plot_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/plot_noh.py)
- [/code/validated-examples/2026-11-23-r2/noh-cartesian/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/run.py)
- [/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_solver.py)
- [/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_reference.py)
- [/code/validated-examples/2026-11-23-r2/sedov/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/run.py)
- [/code/validated-examples/2026-11-23-r2/sedov/sedov_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/sedov_solver.py)
- [/code/validated-examples/2026-11-23-r2/sedov/reference_sedov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/reference_sedov.py)
- [/code/validated-examples/2026-11-23-r2/sedov/exactpack-generate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/exactpack-generate.py)
- [/code/validated-examples/2026-11-23-r2/sedov/reference-development/ode01-source.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/reference-development/ode01-source.py)
- [/code/validated-examples/2026-11-23/double-mach/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/run.py)
- [/code/validated-examples/2026-11-23/double-mach/dm_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/dm_solver.py)
- [/code/validated-examples/2026-11-23/double-mach/references/reference-source.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/references/reference-source.py)
- [/code/validated-examples/2026-11-23/forward-step/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/run.py)
- [/code/validated-examples/2026-11-23/forward-step/fs_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/fs_solver.py)
- [/code/validated-examples/2026-11-23/forward-step/references/convert.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/references/convert.py)
- [/code/validated-examples/2026-11-23/forward-step/references/run-reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/references/run-reference.py)
- [/code/validated-examples/2026-11-23-r3/guderley/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/run.py)
- [/code/validated-examples/2026-11-23-r3/guderley/guderley_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/guderley_solver.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/precollapse.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/precollapse.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/EXACTPACK-test_guderley.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/EXACTPACK-test_guderley.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/eexp.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/eexp.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/guderley.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/guderley.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/interp_laz.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/interp_laz.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/original_init.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/original_init.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/ramsey.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/ramsey.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/qualify_cached_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/qualify_cached_reference.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/qualify_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/qualify_reference.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/run.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/wall_flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/wall_flow.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/references/qualify_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/references/qualify_reference.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/run.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/flow.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/references/linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/references/linear.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/history/reference-attempt-01/references/linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/history/reference-attempt-01/references/linear.py)
- [/code/validated-examples/2026-11-23/mhd-transport/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/run.py)
- [/code/validated-examples/2026-11-23/mhd-transport/solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/solver.py)
- [/code/validated-examples/2026-11-23/mhd-transport/hlld.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/hlld.py)
- [/code/validated-examples/2026-11-23/mhd-transport/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/references/analytic.py)
- [/code/validated-examples/2026-11-23/mhd-transport/references/qualify_saved.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/references/qualify_saved.py)
- [/code/validated-examples/2026-11-23/mhd-transport/references/generate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/references/generate.py)
- [/code/validated-examples/2026-11-23/mhd-transport/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/references/qualify.py)
- [/code/validated-examples/2026-11-23/moving-waves/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/run.py)
- [/code/validated-examples/2026-11-23/moving-waves/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/transport.py)
- [/code/validated-examples/2026-11-23/moving-waves/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/references/exact.py)
- [/code/validated-examples/2026-11-23/moving-waves/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/experiments.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)
- [/code/validated-examples/2026-11-23-r5/noh/test_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/test_noh.py)
- [/code/validated-examples/2026-11-23-r2/noh-cartesian/test_cartesian.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/test_cartesian.py)
- [/code/validated-examples/2026-11-23-r2/sedov/test_sedov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/test_sedov.py)
- [/code/validated-examples/2026-11-23/double-mach/test_dm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/test_dm.py)
- [/code/validated-examples/2026-11-23/forward-step/test_fs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/test_fs.py)
- [/code/validated-examples/2026-11-23-r3/guderley/test_guderley.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/test_guderley.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_result_envelope.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_result_envelope.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_serialization.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_wall_flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_wall_flow.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/test_instability.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/test_instability.py)
- [/code/validated-examples/2026-11-23/mhd-transport/test_mhd.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/test_mhd.py)
- [/code/validated-examples/2026-11-23/moving-waves/test_moving.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/test_moving.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_runge_kutta.py tests/test_hamiltonian.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; double-mach, forward-step, noh, sedov, guderley)
- [Ideal magnetohydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en) (`mhd`; orszag-tang, circular-alfven, magnetic-loop)
- [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en) (`navier-stokes`; lid-driven-cavity)
- [Forced incompressible flow and wall manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-incompressible-en) (`forced-incompressible`; wall-manufactured)
- [Forced vorticity about a maintained shear layer](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-vorticity-en) (`forced-vorticity`; kh-initial-growth)
- [Boussinesq vorticity with active buoyancy](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#boussinesq-buoyancy-en) (`boussinesq-buoyancy`; rt-initial-growth)
- [ALE scalar conservation on moving cells](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#ale-scalar-transport-en) (`ale-scalar-transport`; ale-nonuniform-transport)

#### Problem figures (`method-problems-en`)

##### [Double Mach reflection](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en) (`double-mach`)

![Density from the actual 2D Euler calculation: Mach 10, gamma = 1.4, T = 0.2, 256 × 64 cells. Differences from a saved reference computed with a separate FV implementation and wall-jet diagnostics remain visible. The picture does not establish convergence of thin jets or vortices.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection-preview.png)

Distinguish the existing Godunov/HLL view from new piecewise-constant HLL plus Heun fixed inputs. Each execution links only the methods actually used in that computation.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#code-en)

- [Double Mach reflection: lightweight grid verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en) (`double-mach-reflection`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/atlas-double-mach-2026-11-23.zip)

Full 2D Euler finite volumes evolve the existing Double Mach initial/boundary data to T=.2 on64x16,128x32 and256x64 cells. Compare a separately written finite-grid reference, actual boundary-flux budgets, an upper incident-front position and a fixed near-wall region.

##### [Mach-3 forward-facing step](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en) (`forward-step`)

![Density from the actual 2D Euler computation: Mach3,gamma=1.4,T=4,240×80 cells. The solid step is masked. No corner entropy correction is used; the picture does not establish convergence of fine slip lines or vortices.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png)

Retain the earlier HLL/MUSCL and slope-limiter comparisons; the additional lightweight example uses piecewise-constant HLL plus Heun. Methods belonging to the reference implementation are identified separately with its source and conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#code-en)

- [Mach3 forward step: wall budgets and grid verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en) (`forward-step-m3`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/atlas-forward-step-2026-11-23.zip)

Actual2D Euler finite volumes evolve60x20,120x40 and240x80 meshes toT4, comparing separately implemented MUSCL finite-grid references. Actual numerical wall fluxes, including the vertical and horizontal step faces, close all four conserved budgets. Figures and code explicitly use the variant without corner entropy correction.

##### [Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) (`orszag-tang`)

![Stored CT frame representing the merged CT/GLM problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#code-en)

- [Late Orszag-Tang: independent reference and compression structure](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en) (`postshock-orszag-tang`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip)

Evolve compressible ideal-MHD Orszag-Tang to T.2 and check density/pressure in interacting compression/shock structure against an independent finite-grid reference.

##### [Circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en) (`circular-alfven`)

![Stored circularly polarized Alfvén-wave comparison.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en#code-en)

- [Circular Alfven wave: full-state refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en) (`circular-alfven-refinement`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip)

Evolve all eight conserved variables and compare circular polarization, including nonzero Bz/vz, against analytic cell means.

##### [Magnetic field-loop advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en) (`magnetic-loop`)

![Stored computed fields for magnetic-loop advection.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#code-en)

- [Magnetic loop: independent 2D reference and refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en) (`magnetic-loop-independent`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip)

Compare genuine 2D magnetic-loop transport with final conserved fields from independent Athena++, qualified in space and time.

##### [Nonlinear nonautonomous ODE with exponential exact solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en) (`nonlinear-exp-ode`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-exp-ode.png)

Public nonautonomous/nonlinear manufactured-solution checks exercise every explicit RK tableau; the saved preview uses RK4.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Rational-decay ODE (y′ = −y²)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en) (`nonlinear-rational-decay`)

![Stored time-refinement errors for rational decay, showing three methods.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-decay.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) (`noh`)

![Density from an actual2D Cartesian Euler computation:full square128²,p0=0,gamma5/3,t=.6. White dashed circle is the exact shock. Axis/diagonal differences and origin heating remain visible, with links to earlier1D radial examples.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d-preview.png)

Rusanov/Heun are used in both radial1D and new Cartesian2D runs. MUSCL/minmod apply only to the earlier spherical series; the new2D reconstruction is piecewise constant.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#code-en)

- [Noh shocks: zero-pressure planar, cylindrical and spherical flow](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en) (`noh-shock`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip)

An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.

- [Noh problem: an actual 2D Cartesian Euler calculation](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en) (`noh-cartesian-2d`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip)

A small 2D Euler finite-volume calculation evolves density, both momenta and total energy over the full square. Three grids,32²/64²/128², measure Noh-reference errors, budgets and grid orientation effects. The picture shows the actual evolved 2D array.

##### [Sedov–Taylor point blast](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en) (`sedov`)

![A central-section view of saved one-dimensional spherical-radial Euler density:gamma5/3,E=rho0=1,p0=0,t=.05,512 shells and finite deposition radius.03. Point-source reference differences and shock errors remain visible; this is not an actual2D Cartesian computation.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/results/sedov-blast-preview.png)

A scoped spherical-radial example using piecewise-constant Rusanov finite-volume fluxes and SSPRK2/Heun.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en#code-en)

- [Sedov–Taylor point blast: lightweight spherical-radial validation](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en) (`sedov-blast`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/atlas-sedov-2026-11-23-r2.zip)

A lightweight spherical-radial Euler finite-volume example deposits unit energy inside fixed radius0.03. Three grids of128/256/512 radial cells measure differences from a point-blast similarity reference and conservation budgets. The picture is a section display of1D spherical data, not a2D Cartesian calculation.

##### [Guderley converging shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en) (`guderley`)

![A meridional-section display of saved one-dimensional spherical-radial Euler density: gamma=1.4, 512 shells, r in \[0,0.75\], Rs(-1)=0.6, t=-0.85. Compare the pre-collapse shock entering stationary zero-pressure upstream gas with a semi-analytic reference. This is not 2D Cartesian or post-collapse evolution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/guderley-implosion-preview.png)

A scoped spherical-shell example with piecewise-constant HLL finite-volume fluxes, shell areas/volumes, the geometric pressure source and physical-time Heun updates.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en#code-en)

- [Guderley converging shock: lightweight spherical-radial verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en) (`guderley-implosion`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/atlas-guderley-2026-11-23-r3.zip)

An inward spherical Guderley shock in cold stationary gas is evolved from t=-1 to -0.85 on 128/256/512 radial shells. HLL fluxes and Heun steps are checked against a similarity eigenvalue/field, shock trajectory and discrete conservation budgets.

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

##### [ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en) (`ale-nonuniform-transport`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png)

Upwind relative flux(a-w)q advances actual masses with identical predictor/corrector face geometry; record stage volumes and Courant numbers.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en#code-en)

- [ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en) (`ale-nonuniform-transport`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

Advance cell integrals and face positions with identical Heun stages, transporting a nonuniform analytic wave beyond a uniform GCL check.


#### Exact / reference solutions (`method-references-en`)

##### [Double Mach reflection](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#references-en) (`double-mach`)

- [Double Mach reflection: saved independent finite-grid numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-double-mach-en) (`double-mach`; Same-problem reference; Finite-grid numerical reference)

Compare against two previously independently executed finite-volume reference grids using conservative restriction. This is a finite-grid numerical reference, not an exact2D solution or error bound.

[Existing reference profile](/numerical-methods-atlas/validation/double-mach-reflection/?lang=en#double-mach-reflection-en-measurements)

##### [Mach-3 forward-facing step](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#references-en) (`forward-step`)

- [Mach-3 forward-facing step: independent C++ finite-grid numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-forward-step-en) (`forward-step`; Same-problem reference; Finite-grid numerical reference)

Conservatively restrict newly independently executed C++17 MUSCL/HLL/Heun reference data. The finite-grid numerical reference shares the HLL family,Heun and the uncorrected corner; it is not an exact full-field solution or error bound.

[Existing reference profile](/numerical-methods-atlas/validation/forward-step-m3/?lang=en#forward-step-m3-en-measurements)

##### [Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#references-en) (`orszag-tang`)

- [Late Orszag-Tang: independent finite-grid density/pressure reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-postshock-orszag-tang-en) (`postshock-orszag-tang`; Related-model reference; Finite-grid numerical reference)

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.

[Existing reference profile](/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en#postshock-orszag-tang-en-measurements)

##### [Circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en#references-en) (`circular-alfven`)

- [Circular Alfven wave: analytic full-state conserved cell means](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-circular-alfven-refinement-en) (`circular-alfven-refinement`; Related-model reference; Analytic reference)

gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure.

[Existing reference profile](/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en#circular-alfven-refinement-en-measurements)

##### [Magnetic field-loop advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#references-en) (`magnetic-loop`)

- [Magnetic loop: pinned independent Athena++ final-field reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-magnetic-loop-independent-en) (`magnetic-loop-independent`; Related-model reference; Finite-grid numerical reference)

Periodic[-1,1]x[-.5,.5],rho=p1,Az=.001max(.3-r,0),T1,(Nx,Ny)=(16,8),(32,16),(64,32). Use unchanged official-generator v=(2,1,2), explicitly distinct from old vz0 inputs.

[Existing reference profile](/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en#magnetic-loop-independent-en-measurements)

##### [Nonlinear nonautonomous ODE with exponential exact solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en#references-en) (`nonlinear-exp-ode`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Rational-decay ODE (y′ = −y²)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en#references-en) (`nonlinear-rational-decay`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#references-en) (`noh`)

- [Noh cold-inflow shock: planar, cylindrical and spherical symmetry](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en) (`noh`; Same-problem reference; Analytic reference)

Analytic reference for the same Noh problem.1D uses exact conserved-volume means;2D uses density means from shock-split Cartesian cell quadrature. Distinguish points/cell means and p(mean U)/mean p.

[Existing reference profile](/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-measurements)

##### [Sedov–Taylor point blast](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en#references-en) (`sedov`)

- [Sedov–Taylor point blast: energy-normalized spherical similarity solution](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sedov-en) (`sedov`; Same-problem reference; Semi-analytic reference)

An energy-normalized spherical similarity reference. Numerical integration of similarity ODEs and shell quadrature make this semi-analytic, not closed-form exact cell means. Finite-radius deposition is distinct from the singular ideal point-blast initial data. At fixed finite deposition radius, comparison with the point-source similarity reference includes deposition-model discrepancy; its refinement slope is not a pure spatial order. Changing deposition radius on the same finest grid is a sensitivity diagnostic, not a complete separation of continuum deposition and PDE-discretization errors.

[Existing reference profile](/numerical-methods-atlas/validation/sedov-blast/?lang=en#sedov-blast-en-measurements)

##### [Guderley converging shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en#references-en) (`guderley`)

- [Guderley converging shock: eigenvalue and spherical semi-analytic reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-guderley-en) (`guderley`; Same-problem reference; Semi-analytic reference)

The pre-collapse branch of the spherical Guderley similarity solution at gamma=1.4 with a cold uniform upstream state. Eigenvalue shooting, similarity-ODE integration and shock-split shell quadrature make it semi-analytic rather than closed-form exact cell means. Routine replay reuses lambda from the retained qualification, freshly integrating the similarity ODE and quadrature; recomputing the eigenvalue and original ExactPack probes is a separate explicit command. This is an adapter to pinned ExactPack, not an independently implemented similarity evaluator. Collapse at the origin, the reflected shock and general equations of state remain outside this example.

[Existing reference profile](/numerical-methods-atlas/validation/guderley-implosion/?lang=en#guderley-implosion-en-measurements)

##### [Re100 lid-driven cavity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#references-en) (`lid-driven-cavity`)

- [Ghia Re100: original finite-grid velocity centerlines](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ghia-re100-en) (`ghia-re100`; Same-problem reference; Finite-grid numerical reference)

Educational Re100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed.

[Existing reference profile](/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en#cavity-ghia-re100-en-measurements)

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

##### [ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en#references-en) (`ale-nonuniform-transport`)

- [ALE: analytic moving-cell integrals and separate time reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ale-nonuniform-transport-en) (`ale-nonuniform-transport`; Same-problem reference; Analytic reference)

First-stage1D prescribed mesh motion. The x–t image is not2D physics; Euler Lagrange/remap and Saltzman piston remain future work.

[Existing reference profile](/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en#ale-nonuniform-transport-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Double Mach reflection: lightweight grid verification (`double-mach-reflection`)

[Double Mach reflection](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/atlas-double-mach-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/verification.json)

Full 2D Euler finite volumes evolve the existing Double Mach initial/boundary data to T=.2 on64x16,128x32 and256x64 cells. Compare a separately written finite-grid reference, actual boundary-flux budgets, an upper incident-front position and a fixed near-wall region.

##### Mach3 forward step: wall budgets and grid verification (`forward-step-m3`)

[Mach-3 forward-facing step](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/atlas-forward-step-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/verification.json)

Actual2D Euler finite volumes evolve60x20,120x40 and240x80 meshes toT4, comparing separately implemented MUSCL finite-grid references. Actual numerical wall fluxes, including the vertical and horizontal step faces, close all four conserved budgets. Figures and code explicitly use the variant without corner entropy correction.

##### Late Orszag-Tang: independent reference and compression structure (`postshock-orszag-tang`)

[Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/verification.json)

Evolve compressible ideal-MHD Orszag-Tang to T.2 and check density/pressure in interacting compression/shock structure against an independent finite-grid reference.

##### Circular Alfven wave: full-state refinement (`circular-alfven-refinement`)

[Circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/verification.json)

Evolve all eight conserved variables and compare circular polarization, including nonzero Bz/vz, against analytic cell means.

##### Magnetic loop: independent 2D reference and refinement (`magnetic-loop-independent`)

[Magnetic field-loop advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/verification.json)

Compare genuine 2D magnetic-loop transport with final conserved fields from independent Athena++, qualified in space and time.

##### Noh shocks: zero-pressure planar, cylindrical and spherical flow (`noh-shock`)

[Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/verification.json)

An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.

##### Noh problem: an actual 2D Cartesian Euler calculation (`noh-cartesian-2d`)

[Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/verification.json)

A small 2D Euler finite-volume calculation evolves density, both momenta and total energy over the full square. Three grids,32²/64²/128², measure Noh-reference errors, budgets and grid orientation effects. The picture shows the actual evolved 2D array.

##### Sedov–Taylor point blast: lightweight spherical-radial validation (`sedov-blast`)

[Sedov–Taylor point blast](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/atlas-sedov-2026-11-23-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/verification.json)

A lightweight spherical-radial Euler finite-volume example deposits unit energy inside fixed radius0.03. Three grids of128/256/512 radial cells measure differences from a point-blast similarity reference and conservation budgets. The picture is a section display of1D spherical data, not a2D Cartesian calculation.

##### Guderley converging shock: lightweight spherical-radial verification (`guderley-implosion`)

[Guderley converging shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/atlas-guderley-2026-11-23-r3.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/verification.json)

An inward spherical Guderley shock in cold stationary gas is evolved from t=-1 to -0.85 on 128/256/512 radial shells. HLL fluxes and Heun steps are checked against a similarity eigenvalue/field, shock trajectory and discrete conservation budgets.

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

##### ALE scalar transport on genuinely nonuniform moving cells (`ale-nonuniform-transport`)

[ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json)

Advance cell integrals and face positions with identical Heun stages, transporting a nonuniform analytic wave beyond a uniform GCL check.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity. The additional2D Cartesian Noh edition updates both x/y fluxes and both momenta on a full square. The additional spherical Sedov blast measures grid and finite deposition-radius effects separately. The additional forward-step example verifies actual 2D finite-volume flow with reflecting walls including the step faces. The additional Guderley example evolves a zero-upstream-pressure spherical converging shock only before collapse and compares a semi-analytic similarity reference. Solve a Re100 lid-driven cavity and manufactured flow with a nonperiodic wall-bounded2D vorticity/streamfunction method. Compare original finite-grid Ghia tables, wall shear and grid refinement, keeping a separate pressure-Poisson/gradient manufactured problem distinct. Additional periodic2D KH/RT initial growth uses maintained smooth bases and independent linear IVPs; actual centered conservative face fluxes and Heun evolve vorticity/buoyancy with pressure eliminated. Additional full-state1D CP wave and actual2D magnetic-loop/Orszag–Tang use HLLD,MC-MUSCL and Heun. Count HLLD-to-HLLE fallback and face positivity scaling,with no cell floor or PDE retry. Additional ALE scalar advances face positions and mass with the same two-stage Heun weights,checking boundary budgets,GCL and an independent time reference.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)
- [/code/validated-examples/2026-11-23-r5/noh/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/run.py)
- [/code/validated-examples/2026-11-23-r5/noh/noh_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/noh_solver.py)
- [/code/validated-examples/2026-11-23-r5/noh/noh_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/noh_reference.py)
- [/code/validated-examples/2026-11-23-r5/noh/generate_exactpack_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/generate_exactpack_reference.py)
- [/code/validated-examples/2026-11-23-r5/noh/plot_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/plot_noh.py)
- [/code/validated-examples/2026-11-23-r2/noh-cartesian/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/run.py)
- [/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_solver.py)
- [/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_reference.py)
- [/code/validated-examples/2026-11-23-r2/sedov/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/run.py)
- [/code/validated-examples/2026-11-23-r2/sedov/sedov_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/sedov_solver.py)
- [/code/validated-examples/2026-11-23-r2/sedov/reference_sedov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/reference_sedov.py)
- [/code/validated-examples/2026-11-23-r2/sedov/exactpack-generate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/exactpack-generate.py)
- [/code/validated-examples/2026-11-23-r2/sedov/reference-development/ode01-source.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/reference-development/ode01-source.py)
- [/code/validated-examples/2026-11-23/double-mach/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/run.py)
- [/code/validated-examples/2026-11-23/double-mach/dm_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/dm_solver.py)
- [/code/validated-examples/2026-11-23/double-mach/references/reference-source.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/references/reference-source.py)
- [/code/validated-examples/2026-11-23/forward-step/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/run.py)
- [/code/validated-examples/2026-11-23/forward-step/fs_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/fs_solver.py)
- [/code/validated-examples/2026-11-23/forward-step/references/convert.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/references/convert.py)
- [/code/validated-examples/2026-11-23/forward-step/references/run-reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/references/run-reference.py)
- [/code/validated-examples/2026-11-23-r3/guderley/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/run.py)
- [/code/validated-examples/2026-11-23-r3/guderley/guderley_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/guderley_solver.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/precollapse.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/precollapse.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/EXACTPACK-test_guderley.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/EXACTPACK-test_guderley.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/eexp.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/eexp.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/guderley.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/guderley.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/interp_laz.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/interp_laz.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/original_init.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/original_init.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/ramsey.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/exactpack_guderley/ramsey.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/qualify_cached_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/qualify_cached_reference.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/qualify_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/qualify_reference.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/run.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/wall_flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/wall_flow.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/references/qualify_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/references/qualify_reference.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/run.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/flow.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/references/linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/references/linear.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/history/reference-attempt-01/references/linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/history/reference-attempt-01/references/linear.py)
- [/code/validated-examples/2026-11-23/mhd-transport/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/run.py)
- [/code/validated-examples/2026-11-23/mhd-transport/solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/solver.py)
- [/code/validated-examples/2026-11-23/mhd-transport/hlld.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/hlld.py)
- [/code/validated-examples/2026-11-23/mhd-transport/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/references/analytic.py)
- [/code/validated-examples/2026-11-23/mhd-transport/references/qualify_saved.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/references/qualify_saved.py)
- [/code/validated-examples/2026-11-23/mhd-transport/references/generate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/references/generate.py)
- [/code/validated-examples/2026-11-23/mhd-transport/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/references/qualify.py)
- [/code/validated-examples/2026-11-23/moving-waves/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/run.py)
- [/code/validated-examples/2026-11-23/moving-waves/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/transport.py)
- [/code/validated-examples/2026-11-23/moving-waves/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/references/exact.py)
- [/code/validated-examples/2026-11-23/moving-waves/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/experiments.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)
- [/code/validated-examples/2026-11-23-r5/noh/test_noh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/test_noh.py)
- [/code/validated-examples/2026-11-23-r2/noh-cartesian/test_cartesian.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/test_cartesian.py)
- [/code/validated-examples/2026-11-23-r2/sedov/test_sedov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/test_sedov.py)
- [/code/validated-examples/2026-11-23/double-mach/test_dm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/test_dm.py)
- [/code/validated-examples/2026-11-23/forward-step/test_fs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/test_fs.py)
- [/code/validated-examples/2026-11-23-r3/guderley/test_guderley.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/test_guderley.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_result_envelope.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_result_envelope.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_serialization.py)
- [/code/validated-examples/2026-11-23-r2/wall-flow/test_wall_flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/test_wall_flow.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/test_instability.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/test_instability.py)
- [/code/validated-examples/2026-11-23/mhd-transport/test_mhd.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/test_mhd.py)
- [/code/validated-examples/2026-11-23/moving-waves/test_moving.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/test_moving.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_runge_kutta.py tests/test_hamiltonian.py
```
