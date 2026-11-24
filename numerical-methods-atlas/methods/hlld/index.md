# HLLD MHD Riemann solver / HLLDのMHDリーマン解法

Status: educational-example

Read about HLLD MHD Riemann solver, follow the original references and inspect related educational code and checks.

「HLLDのMHDリーマン解法」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: HLLD法, HLLD流束, HLLD solver, HLLDリーマンソルバー

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mhd/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/mhd/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/mhd.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hlld.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/mhd_tests.py

- Reference: https://doi.org/10.1017/S002211207900210X — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1093/mnras/staa877 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1086/166684 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1006/jcph.2000.6519 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1006/jcph.2001.6961 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/j.jcp.2005.02.017 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1016/0021-9991(88)90120-9 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://arxiv.org/abs/0911.3410 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

Compare the published HLLD-MC finite-volume code with Brio–Wu reference data independently produced by Athena++ at a pinned commit. Additional full-state1D CP wave and actual2D magnetic-loop/Orszag–Tang use HLLD,MC-MUSCL and Heun. Count HLLD-to-HLLE fallback and face positivity scaling,with no cell floor or PDE retry.

公開HLLD-MC有限体積コードを、固定コミットから別に構築したAthena++のBrio–Wu参照と比較します。 追加の全成分1D円偏波と実際の2D磁場ループ/Orszag–TangでHLLD・MC-MUSCL・Heunを使用。HLLD→HLLE代替と面の正値性スケーリングを数え、セルfloorや再試行は行いません。

- Brio–Wu against an independent HLLD implementation: https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json

- Circular Alfven wave: full-state refinement: https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/
- Magnetic loop: independent 2D reference and refinement: https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/
- Late Orszag-Tang: independent reference and compression structure: https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/results/result.json

Common execution records: [{"id": "brio-wu", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#brio-wu-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#brio-wu-en"}}, {"id": "brio-independent", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "circular-alfven-refinement", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "magnetic-loop-independent", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "postshock-orszag-tang", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [理想MHD](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#mhd-ja) (`mhd`; orszag-tang, brio-wu, circular-alfven, magnetic-loop)

#### 問題の図 (`method-problems-ja`)

##### [Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja) (`orszag-tang`)

![CT・GLMを統合した1問題のうち、CTの保存フレームを代表表示。](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#code-ja)

- [後期Orszag–Tang：独立参照と圧縮構造](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja) (`postshock-orszag-tang`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

圧縮性理想MHDのOrszag–TangをT=.2まで進め、相互作用する圧縮・衝撃波構造の密度と圧力を独立有限格子参照で検査します。

##### [Brio–Wu衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=ja) (`brio-wu`)

![保存済みBrio–Wu衝撃波管の比較図。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/brio-wu.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=ja#code-ja)

- [Brio–Wu：HLLDと保存的に粗視化した数値参照](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/brio-wu/?lang=ja) (`brio-wu`) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

γ=2、Bx=0.75の1次元理想MHD衝撃波管をt=0.1まで計算。HLLD＋MC＋SSPRK2の64/128セルを512セルの数値参照と比較し、密度・圧力・縦磁場・保存収支・切替回数を記録する。

- [Brio–Wu：別実装HLLDとの照合](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=ja) (`brio-independent`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

公開HLLD-MC有限体積コードを、固定コミットから別に構築したAthena++のBrio–Wu参照と比較します。

##### [円偏波Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja) (`circular-alfven`)

![保存済み円偏波Alfvén波の誤差・収束比較。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja#code-ja)

- [円偏波Alfvén波：全成分の格子収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja) (`circular-alfven-refinement`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

全8保存変数を進め、非零のBz・vzを含む円偏波を解析セル平均と比較します。

##### [磁場ループの移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja) (`magnetic-loop`)

![保存済み磁場ループ移流の計算場。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#code-ja)

- [磁場ループ：独立2次元参照と細分化](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja) (`magnetic-loop-independent`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

実際の2次元磁場ループ輸送を、別実装Athena++の空間・時間感度を検査した終端保存場と比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#references-ja) (`orszag-tang`)

- [後期Orszag–Tang：独立有限格子の密度・圧力参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-postshock-orszag-tang-ja) (`postshock-orszag-tang`; 関連モデルの参照; 有限格子の数値参照)

γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。

[既存の参照図](/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja#postshock-orszag-tang-ja-measurements)

##### [Brio–Wu衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=ja#references-ja) (`brio-wu`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [円偏波Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja#references-ja) (`circular-alfven`)

- [円偏波Alfvén波：全保存変数の解析セル平均](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-circular-alfven-refinement-ja) (`circular-alfven-refinement`; 関連モデルの参照; 解析参照)

γ=5/3、[0,1]周期、ρ=1、p=.1、Bx=1、振幅.1、速度1、T=1、32/64/128セル。初期値と参照は保存変数の解析セル平均であり、セル平均から復元する圧力は点の定圧と区別します。

[既存の参照図](/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja#circular-alfven-refinement-ja-measurements)

##### [磁場ループの移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#references-ja) (`magnetic-loop`)

- [磁場ループ：固定Athena++の独立終端参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-magnetic-loop-independent-ja) (`magnetic-loop-independent`; 関連モデルの参照; 有限格子の数値参照)

[-1,1]×[-.5,.5]周期、ρ=p=1、Az=.001max(.3−r,0)、T=1、(Nx,Ny)=(16,8),(32,16),(64,32)。変更していない公式生成器と同じv=(2,1,2)で、古いvz=0設定とは区別します。

[既存の参照図](/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja#magnetic-loop-independent-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mhd/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 後期Orszag–Tang：独立参照と圧縮構造 (`postshock-orszag-tang`)

[Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/verification.json)

圧縮性理想MHDのOrszag–TangをT=.2まで進め、相互作用する圧縮・衝撃波構造の密度と圧力を独立有限格子参照で検査します。

##### Brio–Wu：HLLDと保存的に粗視化した数値参照 (`brio-wu`)

[Brio–Wu衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/brio-wu/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/brio-wu.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

γ=2、Bx=0.75の1次元理想MHD衝撃波管をt=0.1まで計算。HLLD＋MC＋SSPRK2の64/128セルを512セルの数値参照と比較し、密度・圧力・縦磁場・保存収支・切替回数を記録する。

##### Brio–Wu：別実装HLLDとの照合 (`brio-independent`)

[Brio–Wu衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json)

公開HLLD-MC有限体積コードを、固定コミットから別に構築したAthena++のBrio–Wu参照と比較します。

##### 円偏波Alfvén波：全成分の格子収束 (`circular-alfven-refinement`)

[円偏波Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/verification.json)

全8保存変数を進め、非零のBz・vzを含む円偏波を解析セル平均と比較します。

##### 磁場ループ：独立2次元参照と細分化 (`magnetic-loop-independent`)

[磁場ループの移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/verification.json)

実際の2次元磁場ループ輸送を、別実装Athena++の空間・時間感度を検査した終端保存場と比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

公開HLLD-MC有限体積コードを、固定コミットから別に構築したAthena++のBrio–Wu参照と比較します。 追加の全成分1D円偏波と実際の2D磁場ループ/Orszag–TangでHLLD・MC-MUSCL・Heunを使用。HLLD→HLLE代替と面の正値性スケーリングを数え、セルfloorや再試行は行いません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/mhd.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/mhd.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hlld.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hlld.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/mhd_tests.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/mhd_tests.py)
- [/code/validated-examples/2026-11-22/mhd/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/run.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/hlld.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/hlld.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/mhd_tests.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/mhd_tests.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/mhd.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/mhd.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/solvers.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/riemann.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/benchmarks.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/benchmarks.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/equations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/equations.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/limited.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/limited.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/limiters.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/limiters.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/snapshots.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/snapshots.py)
- [/code/validated-examples/2026-11-24/mhd-transport/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/run.py)
- [/code/validated-examples/2026-11-24/mhd-transport/solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/solver.py)
- [/code/validated-examples/2026-11-24/mhd-transport/hlld.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/hlld.py)
- [/code/validated-examples/2026-11-24/mhd-transport/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/references/analytic.py)
- [/code/validated-examples/2026-11-24/mhd-transport/references/qualify_saved.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/references/qualify_saved.py)
- [/code/validated-examples/2026-11-24/mhd-transport/references/generate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/references/generate.py)
- [/code/validated-examples/2026-11-24/mhd-transport/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/references/qualify.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_hlld.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hlld.py)
- [/code/validated-examples/2026-11-22/mhd/test_validation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/test_validation.py)
- [/code/validated-examples/2026-11-24/mhd-transport/test_mhd.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/test_mhd.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_hlld.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Ideal magnetohydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en) (`mhd`; orszag-tang, brio-wu, circular-alfven, magnetic-loop)

#### Problem figures (`method-problems-en`)

##### [Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) (`orszag-tang`)

![Stored CT frame representing the merged CT/GLM problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#code-en)

- [Late Orszag-Tang: independent reference and compression structure](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en) (`postshock-orszag-tang`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

Evolve compressible ideal-MHD Orszag-Tang to T.2 and check density/pressure in interacting compression/shock structure against an independent finite-grid reference.

##### [Brio–Wu shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=en) (`brio-wu`)

![Stored Brio–Wu shock-tube comparison.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/brio-wu.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=en#code-en)

- [Brio–Wu: HLLD and a conservatively restricted numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/brio-wu/?lang=en) (`brio-wu`) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Evolve the one-dimensional γ=2 ideal-MHD shock tube with Bx=0.75 to t=0.1. Compare 64/128-cell HLLD/MC/SSPRK2 with a 512-cell numerical reference, recording density, pressure, longitudinal field, balances and fallback counts.

- [Brio–Wu against an independent HLLD implementation](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=en) (`brio-independent`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

Compare the published HLLD-MC finite-volume code with Brio–Wu reference data independently produced by Athena++ at a pinned commit.

##### [Circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en) (`circular-alfven`)

![Stored circularly polarized Alfvén-wave comparison.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/alfven.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en#code-en)

- [Circular Alfven wave: full-state refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en) (`circular-alfven-refinement`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

Evolve all eight conserved variables and compare circular polarization, including nonzero Bz/vz, against analytic cell means.

##### [Magnetic field-loop advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en) (`magnetic-loop`)

![Stored computed fields for magnetic-loop advection.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#code-en)

- [Magnetic loop: independent 2D reference and refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en) (`magnetic-loop-independent`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

Compare genuine 2D magnetic-loop transport with final conserved fields from independent Athena++, qualified in space and time.


#### Exact / reference solutions (`method-references-en`)

##### [Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#references-en) (`orszag-tang`)

- [Late Orszag-Tang: independent finite-grid density/pressure reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-postshock-orszag-tang-en) (`postshock-orszag-tang`; Related-model reference; Finite-grid numerical reference)

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.

[Existing reference profile](/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en#postshock-orszag-tang-en-measurements)

##### [Brio–Wu shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=en#references-en) (`brio-wu`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en#references-en) (`circular-alfven`)

- [Circular Alfven wave: analytic full-state conserved cell means](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-circular-alfven-refinement-en) (`circular-alfven-refinement`; Related-model reference; Analytic reference)

gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure.

[Existing reference profile](/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en#circular-alfven-refinement-en-measurements)

##### [Magnetic field-loop advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#references-en) (`magnetic-loop`)

- [Magnetic loop: pinned independent Athena++ final-field reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-magnetic-loop-independent-en) (`magnetic-loop-independent`; Related-model reference; Finite-grid numerical reference)

Periodic[-1,1]x[-.5,.5],rho=p1,Az=.001max(.3-r,0),T1,(Nx,Ny)=(16,8),(32,16),(64,32). Use unchanged official-generator v=(2,1,2), explicitly distinct from old vz0 inputs.

[Existing reference profile](/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en#magnetic-loop-independent-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/mhd/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Late Orszag-Tang: independent reference and compression structure (`postshock-orszag-tang`)

[Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/verification.json)

Evolve compressible ideal-MHD Orszag-Tang to T.2 and check density/pressure in interacting compression/shock structure against an independent finite-grid reference.

##### Brio–Wu: HLLD and a conservatively restricted numerical reference (`brio-wu`)

[Brio–Wu shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/brio-wu/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/brio-wu.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Evolve the one-dimensional γ=2 ideal-MHD shock tube with Bx=0.75 to t=0.1. Compare 64/128-cell HLLD/MC/SSPRK2 with a 512-cell numerical reference, recording density, pressure, longitudinal field, balances and fallback counts.

##### Brio–Wu against an independent HLLD implementation (`brio-independent`)

[Brio–Wu shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json)

Compare the published HLLD-MC finite-volume code with Brio–Wu reference data independently produced by Athena++ at a pinned commit.

##### Circular Alfven wave: full-state refinement (`circular-alfven-refinement`)

[Circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/verification.json)

Evolve all eight conserved variables and compare circular polarization, including nonzero Bz/vz, against analytic cell means.

##### Magnetic loop: independent 2D reference and refinement (`magnetic-loop-independent`)

[Magnetic field-loop advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/atlas-mhd-transport-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/verification.json)

Compare genuine 2D magnetic-loop transport with final conserved fields from independent Athena++, qualified in space and time.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Compare the published HLLD-MC finite-volume code with Brio–Wu reference data independently produced by Athena++ at a pinned commit. Additional full-state1D CP wave and actual2D magnetic-loop/Orszag–Tang use HLLD,MC-MUSCL and Heun. Count HLLD-to-HLLE fallback and face positivity scaling,with no cell floor or PDE retry.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/mhd.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/mhd.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hlld.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hlld.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/mhd_tests.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/mhd_tests.py)
- [/code/validated-examples/2026-11-22/mhd/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/run.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/hlld.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/hlld.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/mhd_tests.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/mhd_tests.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/mhd.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/mhd.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/solvers.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/riemann.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/benchmarks.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/benchmarks.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/equations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/equations.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/limited.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/limited.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/limiters.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/limiters.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/snapshots.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/snapshots.py)
- [/code/validated-examples/2026-11-24/mhd-transport/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/run.py)
- [/code/validated-examples/2026-11-24/mhd-transport/solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/solver.py)
- [/code/validated-examples/2026-11-24/mhd-transport/hlld.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/hlld.py)
- [/code/validated-examples/2026-11-24/mhd-transport/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/references/analytic.py)
- [/code/validated-examples/2026-11-24/mhd-transport/references/qualify_saved.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/references/qualify_saved.py)
- [/code/validated-examples/2026-11-24/mhd-transport/references/generate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/references/generate.py)
- [/code/validated-examples/2026-11-24/mhd-transport/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/references/qualify.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_hlld.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hlld.py)
- [/code/validated-examples/2026-11-22/mhd/test_validation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/test_validation.py)
- [/code/validated-examples/2026-11-24/mhd-transport/test_mhd.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/mhd-transport/test_mhd.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_hlld.py
```
