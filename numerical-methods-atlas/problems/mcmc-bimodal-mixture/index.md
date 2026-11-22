# 多峰性MCMC：峰への閉じ込め・偽の安心・大域提案 / Multimodal MCMC: trapping, false reassurance and a global proposal

https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/

## 日本語

[同じ2峰密度を、分散初期値の局所MH・同じ峰からの局所MH・対称reflectionを混ぜるMHで比較。期待した混合不良の検出と、実際の峰間移動を分けて検証します。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-multimodal-mixing.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mcmc/#mcmc-multimodal-mixing) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#mcmc-bimodal-mixture)

### 方程式・問題の定義

2峰Gaussian混合分布を標的とするMarkov連鎖の標本化問題です。既存の方程式一覧には専用項目がありません。

#### 多峰性MCMC：峰への閉じ込め・偽の安心・大域提案

補助実行例 · 実行例の定義・検証式

$$
\pi(x)=\tfrac12\phi(x+6)+\tfrac12\phi(x-6),\quad E[X]=0,\quad\operatorname{Var}X=37
$$

$$
F(x)=\tfrac12\Phi(x+6)+\tfrac12\Phi(x-6),\quad P(X>0)=\tfrac12
$$

$$
q(y\mid x)=(1-p)\phi_s(y-x)+p\phi_s(y+x)=q(x\mid y),\quad s=.8,\ p=.1
$$

$$
\alpha(x,y)=\min\{1,\pi(y)/\pi(x)\},\quad I_n=\mathbf1\{X_n>0\}
$$

同じ2峰密度を、分散初期値の局所MH・同じ峰からの局所MH・対称reflectionを混ぜるMHで比較。期待した混合不良の検出と、実際の峰間移動を分けて検証します。

### 厳密解・参照解

既知の2峰Gaussian混合の解析的な密度・モーメント・指定点CDF・正側占有と照合し、診断量は独立ArviZ参照で確認します。峰への閉じ込めと多鎖診断の限界を区別し、局所診断の良さを全体混合の保証にしません。

#### 多峰性MCMC：峰への閉じ込め・偽の安心・大域提案

解析平均・分散・CDFの指定7点・正側占有と照合。各鎖の占有率と峰間遷移、rank/folded split Rhat、bulk/tail/mean・modeindicator ESS、鎖内だけのACF/ESSを記録。分散trapped鎖はpooled分布が良くてもRhat/多鎖ESSで失敗、same-mode鎖はRhatが良くても既知標的に失敗する対照です。scenario passはこの期待失敗を検出できた意味です。CDF差は指定点最大でKS全域距離・IID検定p値ではありません。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [Markov連鎖Monte Carlo](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [多峰性MCMC：峰への閉じ込め・偽の安心・大域提案](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=ja)

補助実行例

同じ2峰密度を、分散初期値の局所MH・同じ峰からの局所MH・対称reflectionを混ぜるMHで比較。期待した混合不良の検出と、実際の峰間移動を分けて検証します。

無次元1D標的p=.5N(−6,1)+.5N(6,1)、平均0/分散37/正側占有.5。3固定seed・4鎖、burn1024、保持16384標本/鎖。prefix1024/4096/16384は入れ子で独立再試行ではありません。棄却と自己遷移を保持します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

固定seed・有限予算の教育用実験です。局所Gaussian RWも理論上は既約なMHであり、有限時間のtrappingを非エルゴードなアルゴリズムとは呼びません。小さいRhat・大きいESS・プールCDFの一致は未発見の峰を除外せず、既知対称性のreflection提案も一般多峰ソルバーではありません。量子計算は追加しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/mcmc/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/run.py)
- [/code/validated-examples/2026-11-22/mcmc/sampler.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/sampler.py)
- [/code/validated-examples/2026-11-22/mcmc/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/diagnostics.py)
- [/code/validated-examples/2026-11-22/mcmc/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/experiments.py)
- [/code/validated-examples/2026-11-22/mcmc/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/fixtures.py)
- [/code/validated-examples/2026-11-22/mcmc/test_mcmc.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/test_mcmc.py)

## English

[Compare dispersed local MH, same-mode local MH and symmetry-informed reflection/local MH on the same bimodal target. Separate detecting expected mixing failures from successful finite-budget mode exploration.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-multimodal-mixing.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mcmc/#mcmc-multimodal-mixing) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#mcmc-bimodal-mixture-en)

### Equations and problem definitions

Markov-chain sampling of a bimodal Gaussian-mixture target; the equation registry has no dedicated entry.

#### Multimodal MCMC: trapping, false reassurance and a global proposal

Supplementary execution example · Example definition or validation formula

$$
\pi(x)=\tfrac12\phi(x+6)+\tfrac12\phi(x-6),\quad E[X]=0,\quad\operatorname{Var}X=37
$$

$$
F(x)=\tfrac12\Phi(x+6)+\tfrac12\Phi(x-6),\quad P(X>0)=\tfrac12
$$

$$
q(y\mid x)=(1-p)\phi_s(y-x)+p\phi_s(y+x)=q(x\mid y),\quad s=.8,\ p=.1
$$

$$
\alpha(x,y)=\min\{1,\pi(y)/\pi(x)\},\quad I_n=\mathbf1\{X_n>0\}
$$

Compare dispersed local MH, same-mode local MH and symmetry-informed reflection/local MH on the same bimodal target. Separate detecting expected mixing failures from successful finite-budget mode exploration.

### Exact and reference solutions

Compare with the known bimodal Gaussian mixture’s analytic density, moments, declared CDF points and positive occupancy, and check diagnostics against independent ArviZ references. Distinguish trapping from diagnostic limitations; reassuring local diagnostics do not guarantee global mixing.

#### Multimodal MCMC: trapping, false reassurance and a global proposal

Compare with analytic moments, seven declared CDF points and positive occupancy. Record per-chain occupancies/transitions, rank/folded split Rhat, bulk/tail/mean and mode-indicator ESS, and within-only ACF/ESS. Dispersed trapped chains can have a good pooled distribution yet fail between-chain diagnostics; same-mode chains can have reassuring Rhat yet fail the known target. A control scenario passes when its intended failure is detected. CDF error is a declared-point maximum, not whole-line KS distance or an IID-test p-value.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [Markov-chain Monte Carlo / MCMC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Multimodal MCMC: trapping, false reassurance and a global proposal](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=en)

Supplementary execution example

Compare dispersed local MH, same-mode local MH and symmetry-informed reflection/local MH on the same bimodal target. Separate detecting expected mixing failures from successful finite-budget mode exploration.

Dimensionless1D target p=.5N(−6,1)+.5N(6,1), mean0/variance37/positive occupancy.5. Three fixed seeds, four chains,1024 warmup and16384 retained draws/chain. Prefixes1024/4096/16384 are nested, not independent replications. Rejections/self-transitions are retained.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

An educational fixed-seed, finite-budget experiment. The local Gaussian RW is theoretically irreducible MH; finite-time trapping is not called a nonergodic algorithm. Small Rhat, large ESS and pooled-CDF agreement cannot rule out undiscovered modes. Symmetry-informed reflection is not a generic multimodal solver. No quantum calculations.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/mcmc/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/run.py)
- [/code/validated-examples/2026-11-22/mcmc/sampler.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/sampler.py)
- [/code/validated-examples/2026-11-22/mcmc/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/diagnostics.py)
- [/code/validated-examples/2026-11-22/mcmc/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/experiments.py)
- [/code/validated-examples/2026-11-22/mcmc/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/fixtures.py)
- [/code/validated-examples/2026-11-22/mcmc/test_mcmc.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/test_mcmc.py)
