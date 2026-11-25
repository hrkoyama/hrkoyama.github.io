# Berendsen weak-coupling thermostat / Berendsen弱結合サーモスタット

Status: educational-example

Relax the temperature difference over a chosen coupling time using velocity scaling. Fluctuations are suppressed, so this is not a correct canonical sampler.

目標温度との差を緩和時間で減衰させる速度スケーリング。温度の揺らぎが抑制され、正しい正準分布の生成器にはならない。

This authored splitting is not a full LAMMPS/MKT reproduction. Time20does not prove mixing/equilibration; correct mean temperature alone does not establish canonical sampling or general ergodicity.

Other names: ベルンゼン, Berendsen thermostat, weak coupling

Comparison notes: Treat as a historical relaxation method; do not assume correct NVT fluctuations or response properties.

歴史的な温度緩和法として扱い、NVTでの揺らぎ・応答の測定にはそのまま使わない。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/thermostats/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/thermostats/



- Reference: https://doi.org/10.1063/1.448118 — Bibliographic entry and introductory comparison; full derivation and numerical reproduction have not been audited.
- Reference: https://manual.gromacs.org/current/reference-manual/algorithms/molecular-dynamics.html — Bibliographic entry and introductory comparison; full derivation and numerical reproduction have not been audited.

## Small fixed-input validation supplements

Compare distributions,fluctuations and correlations as well as mean temperature on the same two-mode systems.

同じ2モード系で、温度平均に加えて分布・揺らぎ・相関を比べます。

- NH,chains,weak coupling and fixed-speed contrasts: https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json

Common execution records: [{"id": "deterministic-thermostat-contrasts", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Maintain the fixed educational case and retain unmet statistical/correlation goals.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/berendsen-thermostat/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`; thermostatted-quartic)
- [2モードの決定論的温度浴](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-mode-thermostat-model-ja) (`finite-mode-thermostat-model`; thermostatted-quartic)

#### 問題の図 (`method-problems-ja`)

##### [非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja) (`thermostatted-quartic`)

![弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja#code-ja)

- [NH・chain・弱結合・速度固定の比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=ja) (`deterministic-thermostat-contrasts`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip)

同じ2モード系で、温度平均に加えて分布・揺らぎ・相関を比べます。


#### 厳密解・参照解 (`method-references-ja`)

##### [非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja#references-ja) (`thermostatted-quartic`)

- [NH・chain・弱結合・速度固定の比較](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-deterministic-thermostat-contrasts-ja) (`deterministic-thermostat-contrasts`; 同じ問題の参照; 半解析参照)

同じ2モード四次系と調和対照。決定論的浴の短時間・有限標本比較。

[既存の参照図](/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=ja#deterministic-thermostat-contrasts-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/thermostats/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### NH・chain・弱結合・速度固定の比較 (`deterministic-thermostat-contrasts`)

[非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json)

同じ2モード系で、温度平均に加えて分布・揺らぎ・相関を比べます。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

同じ2モード系で、温度平均に加えて分布・揺らぎ・相関を比べます。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/run.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/common.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/deterministic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/deterministic.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/constrained.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/constrained.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/test_models.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`; thermostatted-quartic)
- [Two-mode deterministic thermostat model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-mode-thermostat-model-en) (`finite-mode-thermostat-model`; thermostatted-quartic)

#### Problem figures (`method-problems-en`)

##### [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en) (`thermostatted-quartic`)

![Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en#code-en)

- [NH,chains,weak coupling and fixed-speed contrasts](https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=en) (`deterministic-thermostat-contrasts`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip)

Compare distributions,fluctuations and correlations as well as mean temperature on the same two-mode systems.


#### Exact / reference solutions (`method-references-en`)

##### [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en#references-en) (`thermostatted-quartic`)

- [NH,chains,weak coupling and fixed-speed contrasts](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-deterministic-thermostat-contrasts-en) (`deterministic-thermostat-contrasts`; Same-problem reference; Semi-analytic reference)

Same two-mode quartic system plus a harmonic control; short-time and finite-sample deterministic-bath comparisons.

[Existing reference profile](/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=en#deterministic-thermostat-contrasts-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/thermostats/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### NH,chains,weak coupling and fixed-speed contrasts (`deterministic-thermostat-contrasts`)

[Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json)

Compare distributions,fluctuations and correlations as well as mean temperature on the same two-mode systems.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Compare distributions,fluctuations and correlations as well as mean temperature on the same two-mode systems.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json)

###### Related source

- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/run.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/common.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/deterministic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/deterministic.py)
- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/constrained.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/constrained.py)

###### Package tests

- [/code/validated-examples/2026-11-25/thermostat-constraint-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/test_models.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
