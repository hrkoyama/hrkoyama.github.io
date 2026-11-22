# Band symmetry groups and irreducible representations / バンド計算の対称群・既約表現

Status: reading-only

Distinguish space/little groups, nonsymmorphic symmetry, SOC double groups, time reversal and Kramers pairing.

空間群、小群、非共型対称性、SOCの二重群、時間反転とKramers縮退を区別する。

Introductory group concepts, representative equations and primary sources are available. No dedicated implementation or verified band-irrep assignment is provided yet. This is an introduction to concepts, conditions and their computational use. Complete character tables, automatic irrep assignment to computed wavefunctions and symmetry-based topology classification are not implemented.

Other names: 対称群, 群論, space group, point group, little group, 小群, 既約表現, irreps, バンド計算, 対称性, Kramers, 二重群, double group, nonsymmorphic, glide, screw, SOC, TRIM, Bilbao, SeeK-path

Comparison notes: This is an introduction to concepts, conditions and their computational use. Complete character tables, automatic irrep assignment to computed wavefunctions and symmetry-based topology classification are not implemented.

ここで提供するのは群の概念・条件・計算での使い方の導入です。全空間群の指標表や、実計算の波動関数への既約表現の自動割当て、対称性によるトポロジー判定は未実装です。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#band-symmetry
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#band-symmetry



- Reference: https://doi.org/10.1107/S0108767305040286 — Primary source for band-symmetry concepts and conventions. Introductory review; no atlas band-structure calculation or irrep assignment has been numerically reproduced.
- Reference: https://doi.org/10.1016/j.commatsci.2016.10.015 — Primary source for band-symmetry concepts and conventions. Introductory review; no atlas band-structure calculation or irrep assignment has been numerically reproduced.
- Reference: https://doi.org/10.1107/S1600576717011712 — Primary source for band-symmetry concepts and conventions. Introductory review; no atlas band-structure calculation or irrep assignment has been numerically reproduced.
- Reference: https://doi.org/10.1103/PhysRevB.76.045302 — Primary source for band-symmetry concepts and conventions. Introductory review; no atlas band-structure calculation or irrep assignment has been numerically reproduced.

Next: Maintain the reading, primary sources and links to existing small examples. Consider a dedicated implementation only when needed, starting with a small educational case; routine work excludes heavy convergence sweeps, reference regeneration and long MD.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/band-symmetry/
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

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#band-symmetry)


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

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#band-symmetry)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

No related source, tests or code-edition links are registered for this method.
