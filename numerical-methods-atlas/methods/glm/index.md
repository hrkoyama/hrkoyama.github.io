# GLM divergence cleaning / GLM発散クリーニング

Status: educational-example

Read about GLM divergence cleaning, follow the original references and inspect related educational code and checks.

「GLM発散クリーニング」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: GLM法, GLM divergence cleaning, divergence cleaning, 発散クリーニング, div cleaning

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

Orszag–Tang: CT, GLM and independent Athena++: Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++. GLM longitudinal mode: analytic damping: Compare a longitudinal magnetic Fourier mode of GLM cleaning with the continuous linear matrix-exponential solution. CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium: Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence. Orszag–Tang: matched CT/GLM and converged independent references: Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated. Initial-constraint preservation by CT and active GLM cleaning: nonphysical control: Intentionally begin with the same non-solenoidal cell B, checking that CT does not remove the initial defect and calibrating GLM’s B/psi response. This diagnostic adds no physical problem.

Orszag–Tang：CT・GLMと独立Athena++比較: 同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。 GLMの磁気単極子モード：解析的減衰: GLM cleaning単独の縦磁場Fourierモードを、連続線形方程式の行列指数解と比較します。 CT・GLM：移動する磁気静力学平衡の格子・時間収束: 非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。 Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束: 同じOT初期セル平均と同じdt列でCT/GLMを計算し、別に実行したAthena++の格子・時間感度を分離した参照と比較します。 CTの初期制約保持とGLMの能動的cleaning：非物理診断対照: 故意にdiv B≠0とした同じcell磁場で、CTが初期違反を除去しないこととGLMのB/ψ応答を確認します。物理問題数へ加算しない診断対照です。

- Orszag–Tang: CT, GLM and independent Athena++: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/
- GLM longitudinal mode: analytic damping: https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json

- CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/
- Orszag–Tang: matched CT/GLM and converged independent references: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/
- Initial-constraint preservation by CT and active GLM cleaning: nonphysical control: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/result.json

Common execution records: [{"id": "ct-glm-independent", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "glm-fourier-mode", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "ct-glm-smooth-convergence", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "ct-glm-ot-convergence", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "ct-glm-constraint-control", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [理想MHD](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#mhd-ja) (`mhd`; orszag-tang, magnetic-loop, advected-magnetostatic-equilibrium)

#### 問題の図 (`method-problems-ja`)

##### [Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja) (`orszag-tang`)

![CT・GLMを統合した1問題のうち、CTの保存フレームを代表表示。](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#code-ja)

- [Orszag–Tang：CT・GLMと独立Athena++比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja) (`ct-glm-independent`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。

- [Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja) (`ct-glm-ot-convergence`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip)

同じOT初期セル平均と同じdt列でCT/GLMを計算し、別に実行したAthena++の格子・時間感度を分離した参照と比較します。

##### [磁場ループの移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja) (`magnetic-loop`)

![保存済み磁場ループ移流の計算場。](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [CT・GLM：移動する磁気静力学平衡の格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=ja) (`advected-magnetostatic-equilibrium`)

![非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png)

この問題に明示的に対応するct-glm-smooth-convergence配布例のCTとGLMです。同じLLF係数と時間刻みを使っても、磁場配置・角電場平均・法線場の扱いが異なる離散系全体の比較です。この発散ゼロの物理例を、別の非物理制約対照で測った能動的なcleaning性能と同一視しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=ja#code-ja)

- [CT・GLM：移動する磁気静力学平衡の格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja) (`ct-glm-smooth-convergence`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip)

非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#references-ja) (`orszag-tang`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [磁場ループの移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=ja#references-ja) (`magnetic-loop`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [CT・GLM：移動する磁気静力学平衡の格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=ja#references-ja) (`advected-magnetostatic-equilibrium`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mhd/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Orszag–Tang：CT・GLMと独立Athena++比較 (`ct-glm-independent`)

[Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json)

同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。

##### Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束 (`ct-glm-ot-convergence`)

[Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json)

同じOT初期セル平均と同じdt列でCT/GLMを計算し、別に実行したAthena++の格子・時間感度を分離した参照と比較します。

##### CT・GLM：移動する磁気静力学平衡の格子・時間収束 (`ct-glm-smooth-convergence`)

[CT・GLM：移動する磁気静力学平衡の格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json)

非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。

##### 問題図との対応付けとは別の登録実行・検査例

- [glm-fourier-mode](https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=ja) (`glm-fourier-mode`)
- [ct-glm-constraint-control](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=ja) (`ct-glm-constraint-control`)

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Orszag–Tang：CT・GLMと独立Athena++比較: 同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。 GLMの磁気単極子モード：解析的減衰: GLM cleaning単独の縦磁場Fourierモードを、連続線形方程式の行列指数解と比較します。 CT・GLM：移動する磁気静力学平衡の格子・時間収束: 非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。 Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束: 同じOT初期セル平均と同じdt列でCT/GLMを計算し、別に実行したAthena++の格子・時間感度を分離した参照と比較します。 CTの初期制約保持とGLMの能動的cleaning：非物理診断対照: 故意にdiv B≠0とした同じcell磁場で、CTが初期違反を除去しないこととGLMのB/ψ応答を確認します。物理問題数へ加算しない診断対照です。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/mhd.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/mhd.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hlld.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hlld.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/mhd_tests.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/mhd_tests.py)
- [/code/validated-examples/2026-11-22/mhd/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/run.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/mhd.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/mhd.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/hlld.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/hlld.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/mhd_tests.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/mhd_tests.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/solvers.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/riemann.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/benchmarks.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/benchmarks.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/equations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/equations.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/limited.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/limited.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/limiters.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/limiters.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/snapshots.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/snapshots.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/run.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/solver.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/experiments.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_hlld.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hlld.py)
- [/code/validated-examples/2026-11-22/mhd/test_validation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/test_validation.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/test_convergence.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/test_convergence.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_hlld.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Ideal magnetohydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en) (`mhd`; orszag-tang, magnetic-loop, advected-magnetostatic-equilibrium)

#### Problem figures (`method-problems-en`)

##### [Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) (`orszag-tang`)

![Stored CT frame representing the merged CT/GLM problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#code-en)

- [Orszag–Tang: CT, GLM and independent Athena++](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en) (`ct-glm-independent`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++.

- [Orszag–Tang: matched CT/GLM and converged independent references](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en) (`ct-glm-ot-convergence`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip)

Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated.

##### [Magnetic field-loop advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en) (`magnetic-loop`)

![Stored computed fields for magnetic-loop advection.](https://hrkoyama.github.io/numerical-methods-atlas/assets/mhd-tests/field-loop.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=en) (`advected-magnetostatic-equilibrium`)

![Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png)

CT and GLM are explicitly bound by the ct-glm-smooth-convergence release example. Matching LLF coefficients and time steps still compares whole discretizations with different magnetic placement, corner EMF averaging and normal-field handling. This solenoidal physical example is distinct from active-cleaning measurements in the separate nonphysical constraint control.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=en#code-en)

- [CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en) (`ct-glm-smooth-convergence`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip)

Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence.


#### Exact / reference solutions (`method-references-en`)

##### [Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#references-en) (`orszag-tang`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Magnetic field-loop advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#references-en) (`magnetic-loop`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=en#references-en) (`advected-magnetostatic-equilibrium`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/mhd/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Orszag–Tang: CT, GLM and independent Athena++ (`ct-glm-independent`)

[Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json)

Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++.

##### Orszag–Tang: matched CT/GLM and converged independent references (`ct-glm-ot-convergence`)

[Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json)

Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated.

##### CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium (`ct-glm-smooth-convergence`)

[CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium](https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json)

Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence.

##### Registered executions and checks separate from problem-figure links

- [glm-fourier-mode](https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=en) (`glm-fourier-mode`)
- [ct-glm-constraint-control](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=en) (`ct-glm-constraint-control`)

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Orszag–Tang: CT, GLM and independent Athena++: Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++. GLM longitudinal mode: analytic damping: Compare a longitudinal magnetic Fourier mode of GLM cleaning with the continuous linear matrix-exponential solution. CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium: Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence. Orszag–Tang: matched CT/GLM and converged independent references: Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated. Initial-constraint preservation by CT and active GLM cleaning: nonphysical control: Intentionally begin with the same non-solenoidal cell B, checking that CT does not remove the initial defect and calibrating GLM’s B/psi response. This diagnostic adds no physical problem.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/mhd.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/mhd.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hlld.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hlld.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/mhd_tests.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/mhd_tests.py)
- [/code/validated-examples/2026-11-22/mhd/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/run.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/mhd.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/mhd.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/hlld.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/hlld.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/mhd_tests.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/mhd_tests.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/solvers.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/riemann.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/benchmarks.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/benchmarks.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/equations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/equations.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/limited.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/limited.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/limiters.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/limiters.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/snapshots.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/snapshots.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/run.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/solver.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/experiments.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_hlld.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hlld.py)
- [/code/validated-examples/2026-11-22/mhd/test_validation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/test_validation.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/test_convergence.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/test_convergence.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_hlld.py
```
