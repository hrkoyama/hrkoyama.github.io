# Guo forcing / Guo外力

Status: educational-example

Read about Guo forcing, follow the original references and inspect related educational code and checks.

「Guo外力」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: Guo forcing, Guo外力法, Guo forcing scheme

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/lattice-boltzmann/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/lattice-boltzmann/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/lattice_boltzmann.py

- Reference: https://doi.org/10.1103/PhysRev.94.511 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1209/0295-5075/17/6/001 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1103/PhysRevE.65.046308 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/guo/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [等温格子BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja) (`bgk`; channel-poiseuille)
- [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja) (`navier-stokes`; channel-poiseuille)

#### 問題の図 (`method-problems-ja`)

##### [平行平板Poiseuille流](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja) (`channel-poiseuille`)

![保存済み半格子壁Poiseuille速度分布と参照値。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/channel-poiseuille.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。


#### 厳密解・参照解 (`method-references-ja`)

##### [平行平板Poiseuille流](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja#references-ja) (`channel-poiseuille`)

- [粘性チャネル／Poiseuille流](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poiseuille-ja) (`poiseuille`; 関連モデルの参照; 解析参照)

放物線形は共通ですが、計算は格子幅ny・目標最大速度0.01に応じた体積力、カードは単位幅・G=1・ν=0.1です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poiseuille)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/lattice-boltzmann/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

この手法と問題図を対応付けた固定入力実行例は未登録です。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/lattice_boltzmann.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/lattice_boltzmann.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_new_models.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Isothermal lattice BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en) (`bgk`; channel-poiseuille)
- [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en) (`navier-stokes`; channel-poiseuille)

#### Problem figures (`method-problems-en`)

##### [Plane Poiseuille channel flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en) (`channel-poiseuille`)

![Stored half-way-wall Poiseuille velocity profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/channel-poiseuille.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.


#### Exact / reference solutions (`method-references-en`)

##### [Plane Poiseuille channel flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en#references-en) (`channel-poiseuille`)

- [Viscous channel / Poiseuille](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poiseuille-en) (`poiseuille`; Related-model reference; Analytic reference)

Both have parabolic profiles, but the computation uses lattice height ny and forcing for peak speed 0.01; the card uses unit width, G=1 and ν=0.1.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poiseuille)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/lattice-boltzmann/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/lattice_boltzmann.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/lattice_boltzmann.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_new_models.py
```
