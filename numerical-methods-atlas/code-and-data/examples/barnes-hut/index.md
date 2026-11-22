# Barnes–Hut: 192 particles against direct summation / Barnes–Hut：192粒子と直接和の比較

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/barnes-hut/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: barnes-hut

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json

## ja

192粒子の木近似と直接和を比べ、力の誤差・全開極限・相互作用回数を確認する。

### scope

孤立・軟化重力の静的な力の比較。軌道計算・周期系・実行速度の比較ではありません。

### assumptions

正の質量を持つ固定192粒子。Plummer軟化、traceを含む完全な二次モーメント項を使い、同じ核の直接和を参照。

### units

無次元、G=1、軟化長0.03。入力の長さ・質量の規約を保持。

### boundaries

3次元孤立境界。周期境界ではない。

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/input.json
Input SHA-256: 28c1943856caba029f30fd344c5f790da8054b9028021ceddf935ed68c9e03f6
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip
Run from: atlas-code-2026-11-21

```sh
python -m pip install -r requirements.txt
python examples/barnes-hut/run.py --input examples/barnes-hut/input.json --output output
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/result.json
- forces.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/forces.csv

### Numerical acceptance

- particle-count / 粒子数: /particles; value = 192
- relative-force-error / 直接和に対する相対RMS力誤差: /relative_rms_force_error; value ≤ 0.05
- fully-opened-error / 完全に開いたツリーと直接和の最大差: /fully_opened_max_absolute_error; value ≤ 2e-13
- reported-checks / runnerの検証結果: /checks; all values = true
- input-provenance / 実行に用いた入力ハッシュ: /input_sha256; value = 28c1943856caba029f30fd344c5f790da8054b9028021ceddf935ed68c9e03f6

Reading: https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=ja

### References

- 同じPlummer核の直接和。完全に開いたツリーとの一致と近似力の誤差を分ける。: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/result.json
- 原法の文献：A hierarchical O(N log N) force-calculation algorithm (1986): https://doi.org/10.1038/324446a0

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Compare tree and direct forces for 192 particles; inspect force error, the fully opened limit and interaction counts.

### scope

Static isolated softened-gravity force comparison, not orbital integration, periodic gravity or a timing benchmark.

### assumptions

192 fixed particles with positive masses; Plummer softening and the complete second-moment term including its trace, compared with direct summation using the identical kernel.

### units

Dimensionless, G=1, softening 0.03; preserve input length and mass conventions.

### boundaries

3D isolated boundaries, not periodic.

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/input.json
Input SHA-256: 28c1943856caba029f30fd344c5f790da8054b9028021ceddf935ed68c9e03f6
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip
Run from: atlas-code-2026-11-21

```sh
python -m pip install -r requirements.txt
python examples/barnes-hut/run.py --input examples/barnes-hut/input.json --output output
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/result.json
- forces.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/forces.csv

### Numerical acceptance

- particle-count / Particle count: /particles; value = 192
- relative-force-error / Relative RMS force error against direct sum: /relative_rms_force_error; value ≤ 0.05
- fully-opened-error / Maximum fully-opened tree/direct difference: /fully_opened_max_absolute_error; value ≤ 2e-13
- reported-checks / Runner validation flags: /checks; all values = true
- input-provenance / Executed input hash: /input_sha256; value = 28c1943856caba029f30fd344c5f790da8054b9028021ceddf935ed68c9e03f6

Reading: https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=en

### References

- Same-Plummer-kernel direct sum, distinguishing fully opened tree agreement from approximation error.: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/examples/barnes-hut/reference/result.json
- Original method publication: A hierarchical O(N log N) force-calculation algorithm (1986): https://doi.org/10.1038/324446a0

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
