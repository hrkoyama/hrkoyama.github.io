# Born–Oppenheimer molecular dynamics / BOMD / Born–Oppenheimer分子動力学（BOMD）

Status: reading-only

Converge the electronic ground state at each nuclear configuration and propagate classical nuclei with its forces.

核配置ごとに電子基底状態を収束させ、得られた力で核の古典運動を進める。

Overall BOMD remains reading only. The separate force release’s short Verlet interface check does not validate long trajectories or thermostats.

Other names: BOMD, Born Oppenheimer MD, Born–Oppenheimer MD, ボルンオッペンハイマー法, ボルン–オッペンハイマー法, ボルン・オッペンハイマー分子動力学

Comparison notes: Overall BOMD remains reading only. The separate force release’s short Verlet interface check does not validate long trajectories or thermostats.

BOMD全体の状態は解説のみ。別の力配布版で行った短いVerlet接続確認を、長時間軌道・温度制御の検証として数えません。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/periodic-dft/#first-principles-md
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/periodic-dft/#first-principles-md



- Reference: https://doi.org/10.1002/andp.19273892002 — Publisher bibliography and DOI checked. Cited for the historical basis of Born–Oppenheimer separation, without claiming a full-text audit or reproduction of a modern MD implementation.
- Reference: https://doi.org/10.1103/PhysRevLett.55.2471 — Publisher bibliography/abstract and original equations (3)–(5) and discussion of fictitious electronic motion near the BO surface consulted. The paper’s silicon dynamics have not been numerically reproduced.

Next: Maintain the reading, primary sources and links to existing small examples. Consider a dedicated implementation only when needed, starting with a small educational case; routine work excludes heavy convergence sweeps, reference regeneration and long MD.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/
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

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/periodic-dft/#first-principles-md)


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

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/periodic-dft/#first-principles-md)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

No related source, tests or code-edition links are registered for this method.
