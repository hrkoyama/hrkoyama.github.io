# HLL / HLL

Status: educational-example

Read about HLL, follow the original references and inspect related educational code and checks.

「HLL」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: HLL法, HLL流束, HLLリーマンソルバー, Harten-Lax-van Leer

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/equations.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py

- Reference: https://doi.org/10.1016/0021-9991(78)90023-2 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/0021-9991(89)90222-2 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/0021-9991(91)90211-3 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1017/CBO9780511791253 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

Three-grid 2D Double Mach verification using HLL and Heun compares a separately written finite-grid numerical reference, boundary-flux budgets, shock position and unresolved near-wall structure. The additional forward-step example verifies actual 2D finite-volume flow with reflecting walls including the step faces. The additional Guderley example evolves a zero-upstream-pressure spherical converging shock only before collapse and compares a semi-analytic similarity reference. Check shallow-water bed sources and hydrostatic reconstruction with wet/emerged lakes and a SWASHES steady Bernoulli flow. A separate flat-bed Ritter dam break tests genuinely dry states, conservation budgets and a fixed-depth front. Additional lightweight1D SRHD symmetric collision/SRMHD finite-amplitude CP wave use the shared full7-variable stress/induction,MUSCL-minmod,causalHLL±1,SSPRK33 and Z recovery; no generic Riemann,GR or extreme-speed claim.

既存のHLL流束・Heunによる2D Double Mach反射を3格子で検証し、別実装の有限格子数値参照との差、境界流束収支、衝撃位置と未解像の壁近傍構造を示します。 追加の前向きステップ例は段差面を含む反射壁境界の実2D有限体積計算を検証します。 追加のGuderley例は、圧力ゼロの上流へ進む球対称収束衝撃波を原点到達前だけ計算し、半解析的な相似参照と比較します。 浅水系の地形源項と静水再構成を、全湿潤・露出床の静止湖とSWASHESの定常Bernoulli流で検査します。別の平坦床Ritter破堤は、真の乾燥状態・保存収支・固定水深の前縁を確認します。 追加の軽量1D SRHD対称衝突/SRMHD有限振幅円偏極波は、同じ完全7量の応力/誘導、MUSCL-minmod、因果的HLL±1、SSPRK33とZ回復を使用。一般Riemann・GR・極端速度の認証ではありません。

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

- SWASHES topographic flow: lakes and nonzero steady discharge: https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/
- Dry-bed dam break: actual wetting and dry states: https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/result.json

- SRHD symmetric two-shock collision: https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/
- SRMHD finite-amplitude circularly polarized Alfvén wave: https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/result.json

Common execution records: [{"id": "double-mach-reflection", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "forward-step-m3", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "guderley-implosion", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "swashes-topography", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "dry-bed-dam-break", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "srhd-collision", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "srmhd-alfven", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-ja) (`shallow-water`; dam-break, dry-bed-dam-break)
- [等温流体方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#isothermal-ja) (`isothermal`; isothermal-jump)
- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; double-mach, nasa-wedge, forward-step, entropy-2d, odd-even, guderley)
- [地形源項付き浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-bed-ja) (`shallow-water-bed`; swashes-topography)
- [特殊相対論的流体（SRHD）](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srhd-ja) (`srhd`; srhd-collision)
- [特殊相対論的理想MHD（SRMHD）](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srmhd-ja) (`srmhd`; srmhd-alfven)

#### 問題の図 (`method-problems-ja`)

##### [湿潤床ダム崩壊](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja) (`dam-break`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/dam-break.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [等温流体の密度ジャンプ](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja) (`isothermal-jump`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isothermal-jump.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [二重Mach反射](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja) (`double-mach`)

![実際の2次元Euler計算の密度場。Mach10、γ=1.4、T=.2、256×64セル。保存済みの別実装FV参照への差とwall jet診断を示します。細い噴流・渦構造の収束を保証する図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection-preview.png)

既存のGodunov/HLL像と、新しい区分定数HLL＋Heunの固定入力を区別します。各実行例にはその計算で実際に使う手法だけを結びます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#code-ja)

- [Double Mach反射：多格子の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja) (`double-mach-reflection`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/atlas-double-mach-2026-11-23.zip)

既存のDouble Mach反射と同じ初期値・境界を使い、64×16・128×32・256×64の実2D Euler有限体積計算をT=.2まで実行します。別実装の有限格子参照との差、実際の境界流束収支、上部の入射衝撃位置と壁近傍を比較します。

##### [15度楔の斜め衝撃波（Mach数の違いを統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja) (`nasa-wedge`)

![同一問題に統合したMach数違いのうち、Mach 2の保存図を代表表示。](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/wedge-m2-mc.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Mach 3前向きステップ](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja) (`forward-step`)

![実際の2次元Euler計算の密度場。Mach 3、γ=1.4、T=4、240×80セル。固体段差を除いて描きます。角のエントロピー補正は使わず、微細なすべり線・渦の収束を保証する図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png)

従来のHLL・MUSCLと勾配制限の比較データを保持し、追加の軽量例は区分定数HLL＋Heunを使います。参照実装の手法は参照の出典と条件で区別します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#code-ja)

- [Mach 3前向きステップ：壁面収支と多格子検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja) (`forward-step-m3`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/atlas-forward-step-2026-11-23.zip)

実際の2次元Euler有限体積計算を60×20・120×40・240×80でT=4まで行い、別実装のMUSCL有限格子参照と比較します。段差の垂直面・上面を含む実際の数値流束から4保存量の収支を評価し、角のエントロピー補正を加えない変種として図とコードを公開します。

##### [2次元の滑らかなEulerエントロピー波](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja) (`entropy-2d`)

![保存済み2次元エントロピー波の格子収束。](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/smooth-refinement.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [定常平面衝撃波のodd–even診断](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja) (`odd-even`)

![保存済み定常平面衝撃波のodd–even診断。](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-methods/planar-128-0.png)

保存された垂直衝撃波診断の流束とRoe音響エントロピー平滑化です。圧力センサー混合法をRotated-RHLLと同一視しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Guderleyの収束衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja) (`guderley`)

![1次元球対称Eulerの保存済み半径密度を子午面に表示。γ=1.4、512球殻、r∈\[0,.75\]、R_s(−1)=.6、t=−.85。圧力ゼロの静止上流へ進む収束前の衝撃波を半解析参照と比較します。2D Cartesianや原点反射後の計算ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/guderley-implosion-preview.png)

球殻の面積・体積と幾何学的な圧力源を使う区分定数HLL有限体積流束、物理時間のHeun更新による限定例です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja#code-ja)

- [Guderley収束衝撃波：球対称の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja) (`guderley-implosion`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/atlas-guderley-2026-11-23-r3.zip)

冷たい静止気体へ内向きに進む球対称Guderley衝撃波を、128/256/512個の球殻でt=−1から−.85まで計算します。HLL流束とHeun法を、相似指数の固有値・半解析場・衝撃位置・保存収支と照合する軽量例です。

##### [SWASHES地形上の静止湖・定常浅水流](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja) (`swashes-topography`)

![保存した有限体積配列から描いた地形・水面と定常誤差のプレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png)

非負な静水圧再構成、共有HLL流束と左右の圧力補正で地形源項を離散化します。前進Euler、面Courant数.4。静水は反射壁。亜臨界流は上流で流量・下流で水深のみを指定し他変数を外挿します。floor・clip・retryはありません。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja#code-ja)

- [SWASHES地形流：静水と非零流量の定常解](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja) (`swashes-topography`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

水没・露出した隆起上の静水と、非零流量の亜臨界定常解を別々に検査します。静水の保存と、動く定常流に残る離散化誤差を区別します。

##### [乾燥床へのRitter破堤流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja) (`dry-bed-dam-break`)

![実際の1次元浅水計算の保存配列による水深・流量と乾湿前線のプレビュー。時空間図は1次元の5保存時刻です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png)

同じ有限体積ソルバーが乾状態h=q=0を直接扱います。片側乾床HLL波速はu−c,u+2c（反対向きも同様）。面Courant数.4で前進Euler更新し、状態の切上げなしに全更新後の非負性と共有流束収支を記録します。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja#code-ja)

- [乾いた河床のダム破壊：実際のwetting/drying](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja) (`dry-bed-dam-break`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

右半分を厳密にh=q=0として開始する浅水方程式を解き、実際の乾湿前線の進行と保存をRitter解析解と比較します。

##### [SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja) (`srhd-collision`)

![最細格子の実際の保存密度Dの1D x–t図。5保存時刻を使用し、2D流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png)

同じ7保存量RMHD演算子をB=0で使い、MUSCL/minmod・因果的HLL波速±1・SSPRK33で進めます。Z=ρhW²の物理根を保護付きNewton法で復元し、残差と保存量往復を確認します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja#code-ja)

- [SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja) (`srhd-collision`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

相対論的な対称衝突を、独立なTaub関係から得る厳密な保存量セル平均と比較し、実際の1D時空間場を保存します。

##### [SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja) (`srmhd-alfven`)

![最細格子の実際の横磁場Byの1D x–t図。5保存時刻を使い、計算は完全な磁気結合を含みます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png)

D・運動量3成分・全エネルギー・横磁場2成分の全7変数を同じMUSCL/minmod–HLL–SSPRK33で進めます。磁場は動的に結合し、完全なRMHDのZ根で原始変数へ復元します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja#code-ja)

- [SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja) (`srmhd-alfven`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

完全な磁気応力と誘導を含むSRMHDで非線形有限振幅波を1周期進め、厳密セル平均、位相、振幅と細分化を検査します。


#### 厳密解・参照解 (`method-references-ja`)

##### [湿潤床ダム崩壊](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja#references-ja) (`dam-break`)

- [浅水流／水深が正のダム崩壊](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swe-dam-break-ja) (`swe-dam-break`; 関連モデルの参照; 半解析参照)

湿潤河床、g=1、左右水深(2,1)・速度0、x0=0.5が一致します。乾燥河床例への対応ではありません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=swe-dam-break)

##### [等温流体の密度ジャンプ](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja#references-ja) (`isothermal-jump`)

- [等温流／密度跳躍](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isothermal-jump-ja) (`isothermal-jump`; 関連モデルの参照; 半解析参照)

p=ρ、音速1、左右密度(1,0.125)・速度0、x0=0.5が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=isothermal-jump)

##### [二重Mach反射](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#references-ja) (`double-mach`)

- [Double Mach反射：保存済み独立有限格子数値参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-double-mach-ja) (`double-mach`; 同じ問題の参照; 有限格子の数値参照)

以前に独立実行した2格子の有限体積参照を保存量制限で比較します。有限格子数値参照であり、厳密2D解や誤差上界ではありません。

[既存の参照図](/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja#double-mach-reflection-ja-measurements)

##### [15度楔の斜め衝撃波（Mach数の違いを統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=ja#references-ja) (`nasa-wedge`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Mach 3前向きステップ](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#references-ja) (`forward-step`)

- [Mach 3前向きステップ：独立C++有限格子数値参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-forward-step-ja) (`forward-step`; 同じ問題の参照; 有限格子の数値参照)

新しく独立実行したC++17のMUSCL/HLL/Heun参照を保存量制限で比較します。同じHLL族・Heunと角無補正条件を共有する有限格子数値参照であり、全場の厳密解や誤差上界ではありません。

[既存の参照図](/numerical-methods-atlas/validation/forward-step-m3/?lang=ja#forward-step-m3-ja-measurements)

##### [2次元の滑らかなEulerエントロピー波](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja#references-ja) (`entropy-2d`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [定常平面衝撃波のodd–even診断](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=ja#references-ja) (`odd-even`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Guderleyの収束衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja#references-ja) (`guderley`)

- [Guderley収束衝撃波：固有値と球対称の半解析参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-guderley-ja) (`guderley`; 同じ問題の参照; 半解析参照)

γ=1.4・冷たい一様な上流を持つ球対称Guderley相似解の収束前分岐です。相似指数の固有値探索・相似ODE積分・衝撃位置で分割した球殻求積を含む半解析参照で、閉形式の厳密セル平均ではありません。通常追試は保存済みの資格確認で求めたλを再利用して相似ODEと求積を再実行し、固有値探索と元ExactPack点照合の再生成は別の明示コマンドとします。参照は固定ExactPackに基づくアダプターであり、独立に実装した相似解との照合とは扱いません。原点での収束、反射後の衝撃波、一般のEOSは今回の範囲外です。

[既存の参照図](/numerical-methods-atlas/validation/guderley-implosion/?lang=ja#guderley-implosion-ja-measurements)

##### [SWASHES地形上の静止湖・定常浅水流](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja#references-ja) (`swashes-topography`)

- [静止湖：表現した床の上の湿潤・露出平衡](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lake-at-rest-bed-ja) (`lake-at-rest-bed`; 同じ問題の参照; 解析参照)

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。

[既存の参照図](/numerical-methods-atlas/validation/swashes-topography/?lang=ja#swashes-topography-ja-measurements)

- [SWASHES定常流：非射流Bernoulli根](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swashes-bernoulli-ja) (`swashes-bernoulli`; 同じ問題の参照; 半解析参照)

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。

[既存の参照図](/numerical-methods-atlas/validation/swashes-topography/?lang=ja#swashes-topography-ja-measurements)

##### [乾燥床へのRitter破堤流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja#references-ja) (`dry-bed-dam-break`)

- [Ritter乾燥床破堤：g9.81の専用セル平均参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ritter-dry-bed-ja) (`ritter-dry-bed`; 同じ問題の参照; 解析参照)

前線診断はセル平均の.001m等深線で、厳密な支持端を別に保存します。非負性は固定実行の実測です。初期乾セルの濡れを検査し、後退汀線・周期的な再乾燥、実地洪水、摩擦や地形上の移動前線は検証しません。 初回100/200/400セル・[−5,5]mでは28検査と105/109判定が合格し、乾セル残存3判定と前線誤差.3960>.25mが不合格でした。元の全記録を保持し、許容条件を変えず領域・格子を細分化しました。 領域・格子だけを変えた第2回は微小な裾のbinary64 underflowで停止しました。第3回は同じHLL更新の水量packetによる代数的評価を導入し、元の28検査に3検査を追加します。

[既存の参照図](/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja#dry-bed-dam-break-ja-measurements)

- [浅水／乾床への膨張波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swe-dry-bed-ja) (`swe-dry-bed`; 関連モデルの参照; 解析参照)

既存の乾燥床浅水参照は元の重力・領域・時刻を保持します。今回のg9.81・[-10,10]・t.5は専用Ritter参照で照合します。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=swe-dry-bed)

##### [SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja#references-ja) (`srhd-collision`)

- [相対論的対称衝突：特殊化した二衝撃波Taub参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-srhd-collision-ja) (`srhd-collision`; 同じ問題の参照; 半解析参照)

独自の穏やかな対称入力で、接触面は同じ静止状態へ退化します。一般三波Riemann解、高Lorentz因子、原著の数値入力は検証しません。Eは静止質量を含み、保存量の厳密セル平均と比較します。

[既存の参照図](/numerical-methods-atlas/validation/srhd-collision/?lang=ja#srhd-collision-ja-measurements)

##### [SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja#references-ja) (`srmhd-alfven`)

- [SRMHD円偏波：有限振幅厳密族と独立テンソル積分](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-srmhd-alfven-ja) (`srmhd-alfven`; 同じ問題の参照; 解析参照)

原著の厳密解族を独立な低次法で計算し、ECHO法や原著誤差表は再現しません。一般RMHD衝撃波、極端な磁化・Lorentz因子、GR、抵抗MHD、多次元磁場発散制御は対象外。図は実際の1D時空間場です。

[既存の参照図](/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja#srmhd-alfven-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/)


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

##### Guderley収束衝撃波：球対称の軽量検証 (`guderley-implosion`)

[Guderleyの収束衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/atlas-guderley-2026-11-23-r3.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/verification.json)

冷たい静止気体へ内向きに進む球対称Guderley衝撃波を、128/256/512個の球殻でt=−1から−.85まで計算します。HLL流束とHeun法を、相似指数の固有値・半解析場・衝撃位置・保存収支と照合する軽量例です。

##### SWASHES地形流：静水と非零流量の定常解 (`swashes-topography`)

[SWASHES地形上の静止湖・定常浅水流](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json)

水没・露出した隆起上の静水と、非零流量の亜臨界定常解を別々に検査します。静水の保存と、動く定常流に残る離散化誤差を区別します。

##### 乾いた河床のダム破壊：実際のwetting/drying (`dry-bed-dam-break`)

[乾燥床へのRitter破堤流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json)

右半分を厳密にh=q=0として開始する浅水方程式を解き、実際の乾湿前線の進行と保存をRitter解析解と比較します。

##### SRHDの対称二衝撃波衝突 (`srhd-collision`)

[SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json)

相対論的な対称衝突を、独立なTaub関係から得る厳密な保存量セル平均と比較し、実際の1D時空間場を保存します。

##### SRMHDの有限振幅円偏極Alfvén波 (`srmhd-alfven`)

[SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json)

完全な磁気応力と誘導を含むSRMHDで非線形有限振幅波を1周期進め、厳密セル平均、位相、振幅と細分化を検査します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

既存のHLL流束・Heunによる2D Double Mach反射を3格子で検証し、別実装の有限格子数値参照との差、境界流束収支、衝撃位置と未解像の壁近傍構造を示します。 追加の前向きステップ例は段差面を含む反射壁境界の実2D有限体積計算を検証します。 追加のGuderley例は、圧力ゼロの上流へ進む球対称収束衝撃波を原点到達前だけ計算し、半解析的な相似参照と比較します。 浅水系の地形源項と静水再構成を、全湿潤・露出床の静止湖とSWASHESの定常Bernoulli流で検査します。別の平坦床Ritter破堤は、真の乾燥状態・保存収支・固定水深の前縁を確認します。 追加の軽量1D SRHD対称衝突/SRMHD有限振幅円偏極波は、同じ完全7量の応力/誘導、MUSCL-minmod、因果的HLL±1、SSPRK33とZ回復を使用。一般Riemann・GR・極端速度の認証ではありません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/solvers.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/riemann.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/equations.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/equations.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)
- [/code/validated-examples/2026-11-23/double-mach/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/run.py)
- [/code/validated-examples/2026-11-23/double-mach/dm_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/dm_solver.py)
- [/code/validated-examples/2026-11-23/double-mach/references/reference-source.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/references/reference-source.py)
- [/code/validated-examples/2026-11-23/forward-step/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/run.py)
- [/code/validated-examples/2026-11-23/forward-step/fs_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/fs_solver.py)
- [/code/validated-examples/2026-11-23/forward-step/references/convert.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/references/convert.py)
- [/code/validated-examples/2026-11-23/forward-step/references/reference.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/references/reference.cpp)
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
- [/code/validated-examples/2026-11-23/shallow-water/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/run.py)
- [/code/validated-examples/2026-11-23/shallow-water/shallow_water.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/shallow_water.py)
- [/code/validated-examples/2026-11-23/shallow-water/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/references/analytic.py)
- [/code/validated-examples/2026-11-23/shallow-water/protocol-candidates/04-before-normalization/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/protocol-candidates/04-before-normalization/run.py)
- [/code/validated-examples/2026-11-23/relativistic/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/run.py)
- [/code/validated-examples/2026-11-23/relativistic/relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/relativistic.py)
- [/code/validated-examples/2026-11-23/relativistic/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/references/exact.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)
- [/code/validated-examples/2026-11-23/double-mach/test_dm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/test_dm.py)
- [/code/validated-examples/2026-11-23/forward-step/test_fs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/test_fs.py)
- [/code/validated-examples/2026-11-23-r3/guderley/test_guderley.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/test_guderley.py)
- [/code/validated-examples/2026-11-23/shallow-water/test_packet_arithmetic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/test_packet_arithmetic.py)
- [/code/validated-examples/2026-11-23/shallow-water/test_shallow_water.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/test_shallow_water.py)
- [/code/validated-examples/2026-11-23/relativistic/test_relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/test_relativistic.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_numerics.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Shallow-water equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-en) (`shallow-water`; dam-break, dry-bed-dam-break)
- [Isothermal flow equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#isothermal-en) (`isothermal`; isothermal-jump)
- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; double-mach, nasa-wedge, forward-step, entropy-2d, odd-even, guderley)
- [Shallow-water equations with bed source](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-bed-en) (`shallow-water-bed`; swashes-topography)
- [Special-relativistic hydrodynamics (SRHD)](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srhd-en) (`srhd`; srhd-collision)
- [Special-relativistic ideal MHD (SRMHD)](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srmhd-en) (`srmhd`; srmhd-alfven)

#### Problem figures (`method-problems-en`)

##### [Wet-bed dam break](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en) (`dam-break`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/dam-break.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Isothermal density jump](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en) (`isothermal-jump`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isothermal-jump.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Double Mach reflection](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en) (`double-mach`)

![Density from the actual 2D Euler calculation: Mach 10, gamma = 1.4, T = 0.2, 256 × 64 cells. Differences from a saved reference computed with a separate FV implementation and wall-jet diagnostics remain visible. The picture does not establish convergence of thin jets or vortices.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection-preview.png)

Distinguish the existing Godunov/HLL view from new piecewise-constant HLL plus Heun fixed inputs. Each execution links only the methods actually used in that computation.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#code-en)

- [Double Mach reflection: lightweight grid verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en) (`double-mach-reflection`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/atlas-double-mach-2026-11-23.zip)

Full 2D Euler finite volumes evolve the existing Double Mach initial/boundary data to T=.2 on64x16,128x32 and256x64 cells. Compare a separately written finite-grid reference, actual boundary-flux budgets, an upper incident-front position and a fixed near-wall region.

##### [15-degree wedge shock (Mach variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en) (`nasa-wedge`)

![Stored Mach-2 example from the merged wedge Mach variants.](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/wedge-m2-mc.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Mach-3 forward-facing step](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en) (`forward-step`)

![Density from the actual 2D Euler computation: Mach3,gamma=1.4,T=4,240×80 cells. The solid step is masked. No corner entropy correction is used; the picture does not establish convergence of fine slip lines or vortices.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png)

Retain the earlier HLL/MUSCL and slope-limiter comparisons; the additional lightweight example uses piecewise-constant HLL plus Heun. Methods belonging to the reference implementation are identified separately with its source and conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#code-en)

- [Mach3 forward step: wall budgets and grid verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en) (`forward-step-m3`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/atlas-forward-step-2026-11-23.zip)

Actual2D Euler finite volumes evolve60x20,120x40 and240x80 meshes toT4, comparing separately implemented MUSCL finite-grid references. Actual numerical wall fluxes, including the vertical and horizontal step faces, close all four conserved budgets. Figures and code explicitly use the variant without corner entropy correction.

##### [Smooth two-dimensional Euler entropy wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en) (`entropy-2d`)

![Stored refinement study for the 2D entropy wave.](https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/smooth-refinement.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Stationary-shock odd–even diagnostic](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=en) (`odd-even`)

![Stored odd–even diagnostic for a stationary planar shock.](https://hrkoyama.github.io/numerical-methods-atlas/assets/shock-methods/planar-128-0.png)

Fluxes and Roe acoustic entropy smoothing used in the stored normal-shock diagnostic. The pressure-sensor blend is not identified as Rotated-RHLL.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Guderley converging shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en) (`guderley`)

![A meridional-section display of saved one-dimensional spherical-radial Euler density: gamma=1.4, 512 shells, r in \[0,0.75\], Rs(-1)=0.6, t=-0.85. Compare the pre-collapse shock entering stationary zero-pressure upstream gas with a semi-analytic reference. This is not 2D Cartesian or post-collapse evolution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/guderley-implosion-preview.png)

A scoped spherical-shell example with piecewise-constant HLL finite-volume fluxes, shell areas/volumes, the geometric pressure source and physical-time Heun updates.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en#code-en)

- [Guderley converging shock: lightweight spherical-radial verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en) (`guderley-implosion`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/atlas-guderley-2026-11-23-r3.zip)

An inward spherical Guderley shock in cold stationary gas is evolved from t=-1 to -0.85 on 128/256/512 radial shells. HLL fluxes and Heun steps are checked against a similarity eigenvalue/field, shock trajectory and discrete conservation budgets.

##### [SWASHES lakes and steady shallow flow over topography](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en) (`swashes-topography`)

![Preview of represented bed, saved FV surfaces and moving-steady errors.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png)

Hydrostatic reconstruction, shared HLL flux and left/right pressure corrections discretize the bed source; forward Euler and face CFL .4. Lakes use reflecting walls. Moving subcritical boundaries impose upstream q and downstream h, extrapolating the other datum. No state floors, clipping or retries. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en#code-en)

- [SWASHES topographic flow: lakes and nonzero steady discharge](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en) (`swashes-topography`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

Check two lake equilibria separately from nonzero subcritical flow, distinguishing lake preservation from moving-flow discretization error.

##### [Ritter dam break onto a dry bed](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en) (`dry-bed-dam-break`)

![Preview from actual saved 1D shallow-water depth/discharge arrays. The space-time panel shows five saved times, not a 2D flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png)

The FV solver supports h=q=0 directly; one-sided dry HLL speeds use u-c/u+2c and their reflection. Forward Euler at face CFL .4 records every minimum and shared-flux budget without raising cell depths. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en#code-en)

- [Dry-bed dam break: actual wetting and dry states](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en) (`dry-bed-dam-break`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

Start the right half at exactly h=q=0 and compare wetting-front advance, conservation and conservative errors with the Ritter analytic solution.

##### [SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en) (`srhd-collision`)

![Actual finest-grid1D x–t conserved-density field from five stored times; not a two-dimensional flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png)

Use the shared seven-component RMHD operator at B=0 with primitive MUSCL/minmod, causal HLL bounds±1 and SSPRK33. Safeguarded Newton recovers the physical Z=rho h W² root; check residual and full conserved-state roundtrip.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en#code-en)

- [SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en) (`srhd-collision`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

Compare a relativistic symmetric collision with independent exact Taub-based conserved cell means; save actual1D x–t fields.

##### [SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en) (`srmhd-alfven`)

![Actual finest-grid transverse By in1D x–t from five stored times; the solver includes full magnetic coupling.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png)

Evolve all seven variables D,three momenta,total E and two transverse magnetic fields with the shared MUSCL/minmod–HLL–SSPRK33 operator. Magnetic dynamics are coupled; primitive recovery solves the full RMHD Z root.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en#code-en)

- [SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en) (`srmhd-alfven`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

Evolve a nonlinear finite-amplitude wave for one period with full SRMHD magnetic stress and induction; check exact cell means,phase,amplitude and refinement.


#### Exact / reference solutions (`method-references-en`)

##### [Wet-bed dam break](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en#references-en) (`dam-break`)

- [Shallow water / wet dam break](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swe-dam-break-en) (`swe-dam-break`; Related-model reference; Semi-analytic reference)

Wet bed, g=1, depths (2,1), zero velocities and x0=0.5 match; this is not a dry-bed correspondence. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=swe-dam-break)

##### [Isothermal density jump](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en#references-en) (`isothermal-jump`)

- [Isothermal / density jump](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isothermal-jump-en) (`isothermal-jump`; Related-model reference; Semi-analytic reference)

p=ρ, sound speed one, densities (1,0.125), zero velocities and x0=0.5 match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=isothermal-jump)

##### [Double Mach reflection](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#references-en) (`double-mach`)

- [Double Mach reflection: saved independent finite-grid numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-double-mach-en) (`double-mach`; Same-problem reference; Finite-grid numerical reference)

Compare against two previously independently executed finite-volume reference grids using conservative restriction. This is a finite-grid numerical reference, not an exact2D solution or error bound.

[Existing reference profile](/numerical-methods-atlas/validation/double-mach-reflection/?lang=en#double-mach-reflection-en-measurements)

##### [15-degree wedge shock (Mach variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nasa-wedge/?lang=en#references-en) (`nasa-wedge`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Mach-3 forward-facing step](https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#references-en) (`forward-step`)

- [Mach-3 forward-facing step: independent C++ finite-grid numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-forward-step-en) (`forward-step`; Same-problem reference; Finite-grid numerical reference)

Conservatively restrict newly independently executed C++17 MUSCL/HLL/Heun reference data. The finite-grid numerical reference shares the HLL family,Heun and the uncorrected corner; it is not an exact full-field solution or error bound.

[Existing reference profile](/numerical-methods-atlas/validation/forward-step-m3/?lang=en#forward-step-m3-en-measurements)

##### [Smooth two-dimensional Euler entropy wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=en#references-en) (`entropy-2d`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Stationary-shock odd–even diagnostic](https://hrkoyama.github.io/numerical-methods-atlas/problems/odd-even/?lang=en#references-en) (`odd-even`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Guderley converging shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en#references-en) (`guderley`)

- [Guderley converging shock: eigenvalue and spherical semi-analytic reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-guderley-en) (`guderley`; Same-problem reference; Semi-analytic reference)

The pre-collapse branch of the spherical Guderley similarity solution at gamma=1.4 with a cold uniform upstream state. Eigenvalue shooting, similarity-ODE integration and shock-split shell quadrature make it semi-analytic rather than closed-form exact cell means. Routine replay reuses lambda from the retained qualification, freshly integrating the similarity ODE and quadrature; recomputing the eigenvalue and original ExactPack probes is a separate explicit command. This is an adapter to pinned ExactPack, not an independently implemented similarity evaluator. Collapse at the origin, the reflected shock and general equations of state remain outside this example.

[Existing reference profile](/numerical-methods-atlas/validation/guderley-implosion/?lang=en#guderley-implosion-en-measurements)

##### [SWASHES lakes and steady shallow flow over topography](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en#references-en) (`swashes-topography`)

- [Lake at rest: wet and emerged equilibrium over represented bed](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lake-at-rest-bed-en) (`lake-at-rest-bed`; Same-problem reference; Analytic reference)

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.

[Existing reference profile](/numerical-methods-atlas/validation/swashes-topography/?lang=en#swashes-topography-en-measurements)

- [SWASHES steady flow: subcritical Bernoulli root](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swashes-bernoulli-en) (`swashes-bernoulli`; Same-problem reference; Semi-analytic reference)

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.

[Existing reference profile](/numerical-methods-atlas/validation/swashes-topography/?lang=en#swashes-topography-en-measurements)

##### [Ritter dam break onto a dry bed](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en#references-en) (`dry-bed-dam-break`)

- [Ritter dry-bed dam break: dedicated g9.81 cell-mean reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ritter-dry-bed-en) (`ritter-dry-bed`; Same-problem reference; Analytic reference)

The .001m mean-depth contour differs from the analytic support edge, which is reported separately. These fixed runs test wetting of initially dry cells. Retreating shorelines, re-drying cycles, real floods, friction and moving fronts over topography are outside scope. The initial100/200/400-cell [-5,5]m attempt passed28 tests and105/109 gates; three retained-dry-cell gates and the .3960m>.25m contour error failed. All original records remain archived; revision2 enlarges/refines the input without changing acceptance. Revision2 then stopped on a binary64 subnormal-tail dry-momentum artifact. Revision3 factors the same HLL update into water packets and adds three regression/equivalence tests; the original28 remain unchanged.

[Existing reference profile](/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en#dry-bed-dam-break-en-measurements)

- [Shallow water / dry-bed fan](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swe-dry-bed-en) (`swe-dry-bed`; Related-model reference; Analytic reference)

Retain the historical dry-bed reference gravity/domain/time unchanged. The new g9.81,[-10,10],t.5 computation uses its dedicated Ritter reference.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=swe-dry-bed)

##### [SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en#references-en) (`srhd-collision`)

- [Relativistic symmetric collision: specialized two-shock Taub reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srhd-collision-en) (`srhd-collision`; Same-problem reference; Semi-analytic reference)

Custom mild symmetric input; contact degenerates to identical resting states. No general three-wave Riemann,extreme-Lorentz-factor or original-paper numerical-input reproduction claim. E includes rest mass; compare exact conserved cell means.

[Existing reference profile](/numerical-methods-atlas/validation/srhd-collision/?lang=en#srhd-collision-en-measurements)

##### [SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en#references-en) (`srmhd-alfven`)

- [SRMHD circular wave: finite-amplitude exact family and independent tensor integration](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srmhd-alfven-en) (`srmhd-alfven`; Same-problem reference; Analytic reference)

Use the original exact family with an independent lower-order operator; no ECHO-algorithm or error-table reproduction. Generic RMHD shocks,extreme magnetization/Lorentz factors,GR,resistive MHD and multidimensional divergence control are outside scope. Figures show actual1D x–t fields.

[Existing reference profile](/numerical-methods-atlas/validation/srmhd-alfven/?lang=en#srmhd-alfven-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/)


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

##### Guderley converging shock: lightweight spherical-radial verification (`guderley-implosion`)

[Guderley converging shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/atlas-guderley-2026-11-23-r3.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/verification.json)

An inward spherical Guderley shock in cold stationary gas is evolved from t=-1 to -0.85 on 128/256/512 radial shells. HLL fluxes and Heun steps are checked against a similarity eigenvalue/field, shock trajectory and discrete conservation budgets.

##### SWASHES topographic flow: lakes and nonzero steady discharge (`swashes-topography`)

[SWASHES lakes and steady shallow flow over topography](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json)

Check two lake equilibria separately from nonzero subcritical flow, distinguishing lake preservation from moving-flow discretization error.

##### Dry-bed dam break: actual wetting and dry states (`dry-bed-dam-break`)

[Ritter dam break onto a dry bed](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json)

Start the right half at exactly h=q=0 and compare wetting-front advance, conservation and conservative errors with the Ritter analytic solution.

##### SRHD symmetric two-shock collision (`srhd-collision`)

[SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json)

Compare a relativistic symmetric collision with independent exact Taub-based conserved cell means; save actual1D x–t fields.

##### SRMHD finite-amplitude circularly polarized Alfvén wave (`srmhd-alfven`)

[SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json)

Evolve a nonlinear finite-amplitude wave for one period with full SRMHD magnetic stress and induction; check exact cell means,phase,amplitude and refinement.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Three-grid 2D Double Mach verification using HLL and Heun compares a separately written finite-grid numerical reference, boundary-flux budgets, shock position and unresolved near-wall structure. The additional forward-step example verifies actual 2D finite-volume flow with reflecting walls including the step faces. The additional Guderley example evolves a zero-upstream-pressure spherical converging shock only before collapse and compares a semi-analytic similarity reference. Check shallow-water bed sources and hydrostatic reconstruction with wet/emerged lakes and a SWASHES steady Bernoulli flow. A separate flat-bed Ritter dam break tests genuinely dry states, conservation budgets and a fixed-depth front. Additional lightweight1D SRHD symmetric collision/SRMHD finite-amplitude CP wave use the shared full7-variable stress/induction,MUSCL-minmod,causalHLL±1,SSPRK33 and Z recovery; no generic Riemann,GR or extreme-speed claim.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/solvers.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/riemann.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/equations.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/equations.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)
- [/code/validated-examples/2026-11-23/double-mach/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/run.py)
- [/code/validated-examples/2026-11-23/double-mach/dm_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/dm_solver.py)
- [/code/validated-examples/2026-11-23/double-mach/references/reference-source.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/references/reference-source.py)
- [/code/validated-examples/2026-11-23/forward-step/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/run.py)
- [/code/validated-examples/2026-11-23/forward-step/fs_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/fs_solver.py)
- [/code/validated-examples/2026-11-23/forward-step/references/convert.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/references/convert.py)
- [/code/validated-examples/2026-11-23/forward-step/references/reference.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/references/reference.cpp)
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
- [/code/validated-examples/2026-11-23/shallow-water/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/run.py)
- [/code/validated-examples/2026-11-23/shallow-water/shallow_water.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/shallow_water.py)
- [/code/validated-examples/2026-11-23/shallow-water/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/references/analytic.py)
- [/code/validated-examples/2026-11-23/shallow-water/protocol-candidates/04-before-normalization/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/protocol-candidates/04-before-normalization/run.py)
- [/code/validated-examples/2026-11-23/relativistic/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/run.py)
- [/code/validated-examples/2026-11-23/relativistic/relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/relativistic.py)
- [/code/validated-examples/2026-11-23/relativistic/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/references/exact.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)
- [/code/validated-examples/2026-11-23/double-mach/test_dm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/test_dm.py)
- [/code/validated-examples/2026-11-23/forward-step/test_fs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/test_fs.py)
- [/code/validated-examples/2026-11-23-r3/guderley/test_guderley.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/test_guderley.py)
- [/code/validated-examples/2026-11-23/shallow-water/test_packet_arithmetic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/test_packet_arithmetic.py)
- [/code/validated-examples/2026-11-23/shallow-water/test_shallow_water.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/test_shallow_water.py)
- [/code/validated-examples/2026-11-23/relativistic/test_relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/test_relativistic.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_numerics.py
```
