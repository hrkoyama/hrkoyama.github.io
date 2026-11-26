# Radiation transport and moment methods / 輻射輸送・モーメント法

Status: educational-example

Discrete-ordinate radiation transport through an absorbing slab: Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux. Radiation transport: space/angle convergence and photon statistics: Compare characteristics, independent adaptive integration and photon survival in a pure-absorption slab; separate discrete balance, sampling error and interval coverage. Additional fixed examples: Isotropic scattering in a finite slab. See each release for assumptions and checked scope. Additional fixed examples: Su–Olson1996 non-equilibrium diffusion, Su–Olson transport with an independently published analytical table. See each release for assumptions and checked scope. Additional fixed examples: Two-dimensional absorber shadow and M1 transport, Opposing beams and information loss in the M1 closure. See each release for assumptions and checked scope.

純吸収平板の離散座標輻射輸送: 純吸収の定常輻射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。 輻射輸送：空間・角度収束と光子統計: 純吸収平板で特性解・独立適応求積・光子生存率を比較し、離散収支と標本誤差・区間被覆を別々に測ります。 追加固定例：等方散乱平板の反射・透過・吸収。条件と検証範囲は各配布版で確認してください。 追加固定例：Su–Olson1996非平衡拡散、Su–Olson1997角度輸送の独立公開表比較。条件と検証範囲は各配布版で確認してください。 追加固定例：2D吸収影と保存的M1輸送、2D反向beamとM1閉包の情報損失。条件と検証範囲は各配布版で確認してください。

Discrete-ordinate radiation transport through an absorbing slab: Multiple scattering, thermal emission, frequency redistribution, moving media and radiation–fluid coupling are unimplemented. This does not reproduce full DISORT functionality/stabilization. Radiation transport: space/angle convergence and photon statistics: Coverage is observed over finite fixed seeds; neither exactly 95% empirical coverage nor all-seed success is guaranteed. Keep deterministic quadrature error separate from statistical error. Multiple scattering, frequency dependence, thermal emission and radiation hydrodynamics are unvalidated. Additional fixed examples: Limited to fourfixedisotropic slabs;noMC,generalphase-function/DISORT reproduction,universalorder or rigorouscontinuumerrorbound. Additional fixed examples: This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units. No direct original1997fulltext/tablecomparison claim. TheauthorREADMEdoesnotstate transcriptionversusregeneration. Source-offprofiles,generalscattering,globalcontinuumerrorandangularorderarenotcertified. The addition is a resolved N~kappa^2 semidiscrete periodic control,not fixed-grid AP or an SSPRK2 diffusion-time order certificate. Initial F0 versus nonzero Fick flux is retained;limit gates use final s=.25 only. SciPy sparse expm_multiply is shared;DOP853 qualifies the reference propagator. Additional fixed examples: Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented. Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

Other names: 放射輸送法, radiative transfer, radiation transport, 放射モーメント法, 輻射輸送法, 輻射モーメント法, 放射輸送・モーメント法, グレー近似, 灰色近似, grey approximation, gray approximation, 輻射拡散近似, 放射拡散近似, radiation diffusion approximation

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/radiation-transport/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/radiation-transport/



- Reference: https://doi.org/10.1016/0022-4073(84)90112-2 — Method-specific source; see the detailed reading for source role and actual review depth.

## Small fixed-input validation supplements

Discrete-ordinate radiation transport through an absorbing slab: Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux. Radiation transport: space/angle convergence and photon statistics: Compare characteristics, independent adaptive integration and photon survival in a pure-absorption slab; separate discrete balance, sampling error and interval coverage.

純吸収平板の離散座標輻射輸送: 純吸収の定常輻射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。 輻射輸送：空間・角度収束と光子統計: 純吸収平板で特性解・独立適応求積・光子生存率を比較し、離散収支と標本誤差・区間被覆を別々に測ります。

- Discrete-ordinate radiation transport through an absorbing slab: https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json

- Radiation transport: space/angle convergence and photon statistics: https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json

- Isotropic scattering in a finite slab: https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/result.json

- Su–Olson1996 non-equilibrium diffusion: https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/
- Su–Olson transport with an independently published analytical table: https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/result.json

- Two-dimensional absorber shadow and M1 transport: https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/
- Opposing beams and information loss in the M1 closure: https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/result.json

Common execution records: [{"id": "radiation-transport", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "radiation-convergence", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "isotropic-scattering-slab", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "su-olson-diffusion1996", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "su-olson-transport1997", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "shadow-absorber2d", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "opposing-beams2d", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [静止媒質の灰色輻射輸送・散乱・線形交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja) (`static-grey-transfer`; isotropic-scattering-slab, su-olson-transport1997, shadow-absorber2d, opposing-beams2d)
- [Su–Olson1996の非平衡拡散・物質交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#non-equilibrium-diffusion-exchange-ja) (`non-equilibrium-diffusion-exchange`; su-olson-diffusion1996)
- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`; su-olson-transport1997)
- [静止媒質・平坦時空の灰色M1モーメント](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-m1-ja) (`static-grey-m1`; shadow-absorber2d, opposing-beams2d)

#### 問題の図 (`method-problems-ja`)

##### [純吸収平板の離散座標輻射輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja) (`absorbing-slab`)

![光学的厚さ0.7の純吸収平板。32〜512セルのBeer–Lambert参照への空間誤差と、厳密セル内伝播を使う4〜32方向の角度誤差を分けた保存図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja#code-ja)

- [純吸収平板の離散座標輻射輸送](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja) (`radiation-transport`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

純吸収の定常輻射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。

- [輻射輸送：空間・角度収束と光子統計](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=ja) (`radiation-convergence`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

純吸収平板で特性解・独立適応求積・光子生存率を比較し、離散収支と標本誤差・区間被覆を別々に測ります。

##### [等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja) (`isotropic-scattering-slab`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab-preview.png)

保存的風上FVの全方向source結合を離散sweep応答で解きます。半球ごとの正重みGaussにより入射流束πを正規化し、吸収は体積sourceから独立積算します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja#code-ja)

- [等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja) (`isotropic-scattering-slab`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip)

正負の角度を結合した実際の定常輸送を解き、独立な連続角Fredholm参照とR/T/Aを比較します。

##### [Su–Olson1996非平衡拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja) (`su-olson-diffusion1996`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996-preview.png)

保存的FVと後退Euler。輻射物質の反対sourceを同じSchur補元で結合し、Robinのβ+h/2半セル抵抗を用います。ε.25/2の同じ交換operatorも解析検査します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja#code-ja)

- [Su–Olson1996非平衡拡散](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja) (`su-olson-diffusion1996`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

実際の輻射・物質2場とMarshak境界を進め、固定版ExactPackの独立積分参照と比較します。

##### [Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja) (`su-olson-transport1997`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-preview.png)

全方向の風上FVとSSPRK2でIとVを実進行。I=2U、E=半角積分、εE+Vの収支を追跡し、拡散への置換はしません。 厚い極限制御だけは同じ風上演算子を実cos/sin応答から構成し、単一モードを行列指数で時間厳密に進めます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja#code-ja)

- [Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja) (`su-olson-transport1997`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

物質交換を含む実際の正負角度輸送を進め、2023原著者公開の解析benchmark表と比較します。

##### [2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja) (`shadow-absorber2d`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d-preview.png)

風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja#code-ja)

- [2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja) (`shadow-absorber2d`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

実際の円形吸収体の影を、特性線の円弦減衰・角度輸送・M1で比較します。

##### [2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja) (`opposing-beams2d`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d-preview.png)

風上角度FV／M1のRusanovとSSPRK2。吸収は保存ledger付き指数分割。6軸重み1/6、単位beamのnodal強度6、Pzzと全3Dtraceを保持。floor/projectionはしません。 旧c1 Rusanovの横拡散による3不合格を保持し、一般状態の方向別Jacobian固有値・LF円錐分割・法線flux比の最大を一面係数に採用。全ghost面と台帳へ同じfluxを使い、真空と既存許容丸め域の速度だけ1へ拡張して回数・最大超過を記録します。U/Pの投影や純beam特例branchはありません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja#code-ja)

- [2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja) (`opposing-beams2d`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

保存した反向packetの実進行からM1の限界を示し、別の閉M1MMSで数値実装を検証します。


#### 厳密解・参照解 (`method-references-ja`)

##### [純吸収平板の離散座標輻射輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja#references-ja) (`absorbing-slab`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja#references-ja) (`isotropic-scattering-slab`)

- [等方散乱平板：連続角Fredholm流束参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isotropic-scattering-slab-ja) (`isotropic-scattering-slab`; 同じ問題の参照; 半解析参照)

有限の4平板に限定。MC、一般角度phase関数、DISORT再現、普遍的次数や厳密連続体誤差境界は認証しません。

[既存の参照図](/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja#isotropic-scattering-slab-ja-measurements)

##### [Su–Olson1996非平衡拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja#references-ja) (`su-olson-diffusion1996`)

- [Su–Olson1996拡散：固定版の独立積分評価関数](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-su-olson-diffusion1996-ja) (`su-olson-diffusion1996`; 同じ問題の参照; 半解析参照)

1996拡散であり1997角度輸送とは別です。原典本文は未読、公式ソフトの選択値を資格。物理単位の質量opacity解釈は使わず無次元関数を直接参照します。

[既存の参照図](/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja#su-olson-diffusion1996-ja-measurements)

##### [Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja#references-ja) (`su-olson-transport1997`)

- [Su–Olson輸送：2023著者公開の独立解析ベンチマーク表](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-su-olson-transport1997-ja) (`su-olson-transport1997`; 同じ問題の参照; 有限格子の数値参照)

原1997本文・原表と直接照合したとはしません。公開表の転記か再生成かは著者READMEに未記載。source停止後、一般散乱、全時空間の連続体誤差や角度次数は未認証です。 この追加はκhを解像したN∝κ²の半離散周期制御で、固定格子AP性や主SSPRK2の拡散時間次数を認証しません。初期F0と非零Fick流束の初期層を保持し、極限判定は最終s=.25のみ。両行列伝播にSciPy sparse expm_multiplyを共有し、DOP853照合は参照伝播器の資格です。

[既存の参照図](/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja#su-olson-transport1997-ja-measurements)

##### [2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja#references-ja) (`shadow-absorber2d`)

- [円形吸収体の特性線参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shadow-absorber2d-ja) (`shadow-absorber2d`; 同じ問題の参照; 解析参照)

6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。

[既存の参照図](/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja#shadow-absorber2d-ja-measurements)

##### [2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja#references-ja) (`opposing-beams2d`)

- [反向伝播packetの特性線参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-opposing-beams2d-ja) (`opposing-beams2d`; 同じ問題の参照; 解析参照)

6軸は整列beam用で一般角度収束ではありません。反向beamのM1差はモデル情報損失として示し、角度輸送への収束を要求しません。相対論・気体流体・多周波RHDではありません。

[既存の参照図](/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja#opposing-beams2d-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/radiation-transport/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 純吸収平板の離散座標輻射輸送 (`radiation-transport`)

[純吸収平板の離散座標輻射輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

純吸収の定常輻射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。

##### 輻射輸送：空間・角度収束と光子統計 (`radiation-convergence`)

[純吸収平板の離散座標輻射輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json)

純吸収平板で特性解・独立適応求積・光子生存率を比較し、離散収支と標本誤差・区間被覆を別々に測ります。

##### 等方散乱平板の反射・透過・吸収 (`isotropic-scattering-slab`)

[等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/verification.json)

正負の角度を結合した実際の定常輸送を解き、独立な連続角Fredholm参照とR/T/Aを比較します。

##### Su–Olson1996非平衡拡散 (`su-olson-diffusion1996`)

[Su–Olson1996非平衡拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json)

実際の輻射・物質2場とMarshak境界を進め、固定版ExactPackの独立積分参照と比較します。

##### Su–Olson1997角度輸送の独立公開表比較 (`su-olson-transport1997`)

[Su–Olson1997角度輸送の独立公開表比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json)

物質交換を含む実際の正負角度輸送を進め、2023原著者公開の解析benchmark表と比較します。

##### 2D吸収影と保存的M1輸送 (`shadow-absorber2d`)

[2D吸収影と保存的M1輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json)

実際の円形吸収体の影を、特性線の円弦減衰・角度輸送・M1で比較します。

##### 2D反向beamとM1閉包の情報損失 (`opposing-beams2d`)

[2D反向beamとM1閉包の情報損失](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json)

保存した反向packetの実進行からM1の限界を示し、別の閉M1MMSで数値実装を検証します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

純吸収平板の離散座標輻射輸送: 純吸収の定常輻射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。 輻射輸送：空間・角度収束と光子統計: 純吸収平板で特性解・独立適応求積・光子生存率を比較し、離散収支と標本誤差・区間被覆を別々に測ります。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py)
- [/code/validated-examples/2026-11-22/particles/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py)
- [/code/validated-examples/2026-11-22/particles/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py)
- [/code/validated-examples/2026-11-22/particle-transport/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py)
- [/code/validated-examples/2026-11-22/particle-transport/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/run.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/slab.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/slab.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/io_contract.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/references/fredholm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/references/fredholm.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/run.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/diffusion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/diffusion.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/transport.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/thick_limit.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/thick_limit.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/thick_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/thick_reference.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/analytic.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify_thick.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify_thick.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/run.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/geometry.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/mms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/mms.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/wavespeeds.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/wavespeeds.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/io_contract.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/references/analytic.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/references/qualify.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/test_scattering.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/test_scattering.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/test_matter.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/test_matter.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/test_thick_limit.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/test_thick_limit.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/test_directional.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/test_directional.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/test_geometry.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Static grey radiative transfer,scattering and linear exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en) (`static-grey-transfer`; isotropic-scattering-slab, su-olson-transport1997, shadow-absorber2d, opposing-beams2d)
- [Su–Olson1996 non-equilibrium diffusion and material exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#non-equilibrium-diffusion-exchange-en) (`non-equilibrium-diffusion-exchange`; su-olson-diffusion1996)
- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`; su-olson-transport1997)
- [Static grey M1 moments in flat spacetime](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-m1-en) (`static-grey-m1`; shadow-absorber2d, opposing-beams2d)

#### Problem figures (`method-problems-en`)

##### [Discrete-ordinate radiation transport through an absorbing slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en) (`absorbing-slab`)

![Pure-absorption slab of optical depth 0.7: stored 32–512-cell spatial errors versus Beer–Lambert and a separate 4–32-ordinate angular sweep using exact cell propagation.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/radiation-transport.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en#code-en)

- [Discrete-ordinate radiation transport through an absorbing slab](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en) (`radiation-transport`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux.

- [Radiation transport: space/angle convergence and photon statistics](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=en) (`radiation-convergence`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

Compare characteristics, independent adaptive integration and photon survival in a pure-absorption slab; separate discrete balance, sampling error and interval coverage.

##### [Isotropic scattering in a finite slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en) (`isotropic-scattering-slab`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab-preview.png)

Conservative upwind FV with the full discrete angular source coupling solved by sweep-response elimination. Positive hemisphere Gauss weights normalize incoming fluxpi;absorption is independently accumulated from the volume source.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en#code-en)

- [Isotropic scattering in a finite slab](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en) (`isotropic-scattering-slab`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip)

Solve genuinely coupled signed-angle steady transport and compare R/T/A with an independent continuum-angle Fredholm reference.

##### [Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en) (`su-olson-diffusion1996`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996-preview.png)

Conservative FV/backwardEuler with opposite exchange sources coupled by a shared Schur complement and Robin half-cell resistance beta+h/2. Analytic nonunitepsilon.25/2controls exercise the same exchange operators.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en#code-en)

- [Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en) (`su-olson-diffusion1996`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

Advance actual radiation/material fields with the Marshak boundary and compare with independently qualified pinned ExactPack integrals.

##### [Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en) (`su-olson-transport1997`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-preview.png)

Full signed-angle upwind FV/SSPRK2 advancesIandV. WithI=2U,E=halfangularintegral,the weightedbudgetisepsilonE+V;nodiffusionsubstitution. Only the thick-limit control constructs the same upwind operator from actual real cos/sin responses and evolves one Fourier mode by an exact-time matrix exponential.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en#code-en)

- [Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en) (`su-olson-transport1997`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

Evolve actual signed-angle transport/material exchange and compare with pinned analytical benchmark tables provided by the2023primary author.

##### [Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en) (`shadow-absorber2d`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d-preview.png)

Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en#code-en)

- [Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en) (`shadow-absorber2d`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

Compare the actual evolved circular-absorber shadow with characteristic chord attenuation, signed-angle transport and nonlinear M1.

##### [Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en) (`opposing-beams2d`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d-preview.png)

Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en#code-en)

- [Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en) (`opposing-beams2d`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

Show the M1 limitation in actual opposing-packet evolution; validate the same closed M1 solver independently with a manufactured solution.


#### Exact / reference solutions (`method-references-en`)

##### [Discrete-ordinate radiation transport through an absorbing slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en#references-en) (`absorbing-slab`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Isotropic scattering in a finite slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en#references-en) (`isotropic-scattering-slab`)

- [Isotropically scattering slab: continuous-angle Fredholm flux reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isotropic-scattering-slab-en) (`isotropic-scattering-slab`; Same-problem reference; Semi-analytic reference)

Limited to fourfixedisotropic slabs;noMC,generalphase-function/DISORT reproduction,universalorder or rigorouscontinuumerrorbound.

[Existing reference profile](/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en#isotropic-scattering-slab-en-measurements)

##### [Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en#references-en) (`su-olson-diffusion1996`)

- [Su–Olson1996 diffusion: pinned independent integral evaluator](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-su-olson-diffusion1996-en) (`su-olson-diffusion1996`; Same-problem reference; Semi-analytic reference)

This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units.

[Existing reference profile](/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en#su-olson-diffusion1996-en-measurements)

##### [Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en#references-en) (`su-olson-transport1997`)

- [Su–Olson transport: primary2023author-provided analytical benchmark data](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-su-olson-transport1997-en) (`su-olson-transport1997`; Same-problem reference; Finite-grid numerical reference)

No direct original1997fulltext/tablecomparison claim. TheauthorREADMEdoesnotstate transcriptionversusregeneration. Source-offprofiles,generalscattering,globalcontinuumerrorandangularorderarenotcertified. The addition is a resolved N~kappa^2 semidiscrete periodic control,not fixed-grid AP or an SSPRK2 diffusion-time order certificate. Initial F0 versus nonzero Fick flux is retained;limit gates use final s=.25 only. SciPy sparse expm_multiply is shared;DOP853 qualifies the reference propagator.

[Existing reference profile](/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en#su-olson-transport1997-en-measurements)

##### [Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en#references-en) (`shadow-absorber2d`)

- [Circular-absorber characteristic reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shadow-absorber2d-en) (`shadow-absorber2d`; Same-problem reference; Analytic reference)

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

[Existing reference profile](/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en#shadow-absorber2d-en-measurements)

##### [Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en#references-en) (`opposing-beams2d`)

- [Counterpropagating packet characteristic reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-opposing-beams2d-en) (`opposing-beams2d`; Same-problem reference; Analytic reference)

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

[Existing reference profile](/numerical-methods-atlas/validation/opposing-beams2d/?lang=en#opposing-beams2d-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/radiation-transport/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Discrete-ordinate radiation transport through an absorbing slab (`radiation-transport`)

[Discrete-ordinate radiation transport through an absorbing slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux.

##### Radiation transport: space/angle convergence and photon statistics (`radiation-convergence`)

[Discrete-ordinate radiation transport through an absorbing slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/absorbing-slab/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json)

Compare characteristics, independent adaptive integration and photon survival in a pure-absorption slab; separate discrete balance, sampling error and interval coverage.

##### Isotropic scattering in a finite slab (`isotropic-scattering-slab`)

[Isotropic scattering in a finite slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/verification.json)

Solve genuinely coupled signed-angle steady transport and compare R/T/A with an independent continuum-angle Fredholm reference.

##### Su–Olson1996 non-equilibrium diffusion (`su-olson-diffusion1996`)

[Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json)

Advance actual radiation/material fields with the Marshak boundary and compare with independently qualified pinned ExactPack integrals.

##### Su–Olson transport with an independently published analytical table (`su-olson-transport1997`)

[Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json)

Evolve actual signed-angle transport/material exchange and compare with pinned analytical benchmark tables provided by the2023primary author.

##### Two-dimensional absorber shadow and M1 transport (`shadow-absorber2d`)

[Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json)

Compare the actual evolved circular-absorber shadow with characteristic chord attenuation, signed-angle transport and nonlinear M1.

##### Opposing beams and information loss in the M1 closure (`opposing-beams2d`)

[Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json)

Show the M1 limitation in actual opposing-packet evolution; validate the same closed M1 solver independently with a manufactured solution.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Discrete-ordinate radiation transport through an absorbing slab: Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux. Radiation transport: space/angle convergence and photon statistics: Compare characteristics, independent adaptive integration and photon survival in a pure-absorption slab; separate discrete balance, sampling error and interval coverage.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

###### Related source

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py)
- [/code/validated-examples/2026-11-22/particles/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py)
- [/code/validated-examples/2026-11-22/particles/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py)
- [/code/validated-examples/2026-11-22/particle-transport/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py)
- [/code/validated-examples/2026-11-22/particle-transport/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/run.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/slab.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/slab.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/io_contract.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/references/fredholm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/references/fredholm.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/run.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/diffusion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/diffusion.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/transport.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/thick_limit.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/thick_limit.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/thick_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/thick_reference.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/analytic.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify_thick.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify_thick.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/run.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/geometry.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/mms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/mms.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/wavespeeds.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/wavespeeds.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/io_contract.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/references/analytic.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/references/qualify.py)

###### Package tests

- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)
- [/code/validated-examples/2026-11-24/radiation-scattering/test_scattering.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/test_scattering.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/test_matter.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/test_matter.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/test_thick_limit.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/test_thick_limit.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/test_directional.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/test_directional.py)
- [/code/validated-examples/2026-11-24/radiation-geometry/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/test_geometry.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
