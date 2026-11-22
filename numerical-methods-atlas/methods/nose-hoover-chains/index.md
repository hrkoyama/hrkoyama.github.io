# Nosé–Hoover chains / Nosé–Hoover chain

Status: planned

Couple heat-bath variables to further heat baths in a chain. This extension addresses sampling problems of a single thermostat.

熱浴変数にも別の熱浴を結合し、鎖状の拡張系を作る。単一熱浴での標本化の問題を改善するための発展形。

Comparative reading is available. No dedicated implementation or numerical verification result is provided yet.

Other names: ノセ・フーバー鎖, NHC, Nose-Hoover chain

Comparison notes: Chain length, masses and substeps matter. Adding a chain does not universally guarantee ergodicity.

鎖の長さ、質量、サブステップに依存する。鎖を加えるだけで任意の系のエルゴード性を保証するものではない。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/thermostats/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/thermostats/



- Reference: https://doi.org/10.1063/1.463940 — Bibliographic entry and introductory comparison; full derivation and numerical reproduction have not been audited.
- Reference: https://docs.lammps.org/fix_nh.html — Bibliographic entry and introductory comparison; full derivation and numerical reproduction have not been audited.

Next: Add a dedicated formulation and integration recipe, followed by explicit-input distribution and time-correlation checks with stated degrees of freedom, random seeds and step sizes.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover-chains/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

対応する方程式一覧の項目は未登録です。

#### 問題の図 (`method-problems-ja`)

この手法に対応付けられたテスト問題の図は未登録です。

#### 厳密解・参照解 (`method-references-ja`)

この手法の問題図に結び付く参照資料は未登録です。
##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/thermostats/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

この手法と問題図を対応付けた固定入力実行例は未登録です。

この手法に対応するソース・検査・配布版のリンクは未登録です。


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

No corresponding equation-registry entry is registered.

#### Problem figures (`method-problems-en`)

No test-problem figure is registered for this method.

#### Exact / reference solutions (`method-references-en`)

No reference context is registered for this method’s problem figures.
##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/thermostats/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

No related source, tests or code-edition links are registered for this method.
