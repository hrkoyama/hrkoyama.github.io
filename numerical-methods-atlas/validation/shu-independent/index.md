# Shu–Osher：独立参照と格子収束

衝撃波と密度正弦波の相互作用を、同じPython実装の細格子ではなく、別に実行したAthena++の参照と照合します。

**使用手法**

- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=ja#shu-independent-ja-algorithm)

アトラス側はMC-MUSCL/HLLC/SSPRK3、Athena++側はPLM/HLLC/RK3。公式problem generatorの位置と正弦波の波数だけを合わせるpatchを保存し、solver本体は変更しません。

$$
\rho(x,0)=1+0.2\sin(5x)\quad(x\geq-4)
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Shu–Osher：独立参照と格子収束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/shu-independent.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Shu–Osher衝撃波・エントロピー波干渉](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja) (`shu-osher`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=ja#shu-independent-ja-validation)

100/200/400セルの密度L1誤差と改善率、正値性を測り、参照2048/4096/8192セルの差も事前幅と比較します。境界へ衝撃波が届かない固定時刻で比較します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

γ=1.4、[-5,5]、t=1.8。x<-4は(rho,u,p)=(3.857143,2.629369,10.33333)、右はrho=1+0.2sin5x,u=0,p=1。

## 採用した計算法

アトラス側はMC-MUSCL/HLLC/SSPRK3、Athena++側はPLM/HLLC/RK3。公式problem generatorの位置と正弦波の波数だけを合わせるpatchを保存し、solver本体は変更しません。

$$
\rho(x,0)=1+0.2\sin(5x)\quad(x\geq-4)
$$

## 比較・検証

100/200/400セルの密度L1誤差と改善率、正値性を測り、参照2048/4096/8192セルの差も事前幅と比較します。境界へ衝撃波が届かない固定時刻で比較します。

## 確認の限界

参照は厳密解ではなく独立した有限格子数値解です。異なる流束系列すべての優劣、WENOの一般的高次数、負圧防止の保証には広げません。 参照2048→4096のL1差0.005346は事前幅0.005を満たさず、8192へ細分しました。途中の未達記録も残します。

## 保存実測値と判定

```json
{
  "metrics": {
    "reference_last_pair_l1": 0.003374178434921656,
    "reference_finest_n": 8192,
    "finest_density_l1": 0.05377749991959067
  },
  "checks": {
    "independent_reference_refined": true,
    "density_error": true,
    "grid_improvement": true,
    "positive_states": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- J. M. Stone, K. Tomida, C. J. White and K. G. Felker (2020). The Athena++ Adaptive Mesh Refinement Framework: Design and Magnetohydrodynamic Solvers. https://doi.org/10.3847/1538-4365/ab929b; review_level=official-code-and-metadata; pinned source compiled and executed
- C.-W. Shu and S. Osher (1989). Efficient implementation of essentially non-oscillatory shock-capturing schemes, II. https://doi.org/10.1016/0021-9991(89)90222-2; review_level=bibliographic identity and official Athena problem generator

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Shu–Osher: independent reference and mesh refinement

Compare shock–density-wave interaction against separately executed Athena++ reference data rather than a finer grid of the same Python code.

**Methods used**

- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=en#shu-independent-en-algorithm)

Atlas uses MC-MUSCL/HLLC/SSPRK3; Athena++ uses PLM/HLLC/RK3. A saved problem-generator patch matches only shock location and sinusoid wavenumber; the independent solver is unchanged.

$$
\rho(x,0)=1+0.2\sin(5x)\quad(x\geq-4)
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Shu–Osher: independent reference and mesh refinement: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/shu-independent.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Shu–Osher shock/entropy interaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en) (`shu-osher`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=en#shu-independent-en-validation)

Measure density L1 error, refinement and positivity on 100/200/400 cells; also compare 2048/4096/8192 reference differences with a predeclared bound. The shock has not reached the boundaries at the fixed comparison time.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

gamma=1.4, [-5,5], t=1.8. For x<-4, (rho,u,p)=(3.857143,2.629369,10.33333); to the right rho=1+0.2sin5x,u=0,p=1.

## Adopted numerical method

Atlas uses MC-MUSCL/HLLC/SSPRK3; Athena++ uses PLM/HLLC/RK3. A saved problem-generator patch matches only shock location and sinusoid wavenumber; the independent solver is unchanged.

$$
\rho(x,0)=1+0.2\sin(5x)\quad(x\geq-4)
$$

## References and validation

Measure density L1 error, refinement and positivity on 100/200/400 cells; also compare 2048/4096/8192 reference differences with a predeclared bound. The shock has not reached the boundaries at the fixed comparison time.

## Limits

The reference is an independent finite-grid numerical solution, not an exact solution. No universal flux ranking, WENO-order claim or positivity guarantee is inferred. The 2048-to-4096 reference L1 increment0.005346 missed the predeclared0.005 bound, so8192 cells were added. The earlier miss remains recorded.

## Stored measurements and decisions

```json
{
  "metrics": {
    "reference_last_pair_l1": 0.003374178434921656,
    "reference_finest_n": 8192,
    "finest_density_l1": 0.05377749991959067
  },
  "checks": {
    "independent_reference_refined": true,
    "density_error": true,
    "grid_improvement": true,
    "positive_states": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- J. M. Stone, K. Tomida, C. J. White and K. G. Felker (2020). The Athena++ Adaptive Mesh Refinement Framework: Design and Magnetohydrodynamic Solvers. https://doi.org/10.3847/1538-4365/ab929b; review_level=official-code-and-metadata; pinned source compiled and executed
- C.-W. Shu and S. Osher (1989). Efficient implementation of essentially non-oscillatory shock-capturing schemes, II. https://doi.org/10.1016/0021-9991(89)90222-2; review_level=bibliographic identity and official Athena problem generator

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
