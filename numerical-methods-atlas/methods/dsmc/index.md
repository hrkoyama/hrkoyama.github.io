# DSMC and kinetic transport / DSMC・運動論輸送

Status: educational-example

Existing releases: Conservation and Maxwell relaxation in a homogeneous DSMC collision component: Test conservation and relaxation toward equilibrium through randomized pair collisions of homogeneous Maxwell molecules. DSMC collision component: finite-N equilibrium, invariants and statistical error: Distinguish finite-particle equilibrium from the Maxwell limit; compare independent sphere samples, analytic anisotropy decay and across-seed uncertainty. Additional fixed examples: Hard-sphere DSMC finite-Kn Couette flow, Hard-sphere DSMC finite-Kn Fourier heat conduction. See each release for assumptions and checked scope. Additional fixed examples: Hard-sphere DSMC Mach2 planar shock. See each release for assumptions and checked scope.

既存配布版：等質DSMC衝突成分の保存則・Maxwell分布: 等質なMaxwell分子のランダム二体衝突で、保存則と平衡分布への緩和を検証します。 DSMC衝突成分：有限N平衡・保存則・統計誤差: 有限粒子数の平衡をMaxwell極限と区別し、独立な球面標本、解析的異方性減衰、seed間誤差と比較します。 追加固定例：硬球DSMCの有限Kn Couette流、硬球DSMCの有限Kn Fourier熱伝導。条件と検証範囲は各配布版で確認してください。 追加固定例：硬球DSMCのMach2平面衝撃波。条件と検証範囲は各配布版で確認してください。

Limits of existing releases: Conservation and Maxwell relaxation in a homogeneous DSMC collision component: This is an educational DSMC collision component. No spatial streaming, collision cells, speed-dependent hard-sphere selection, measured transport coefficients/flow fields or every-seed guarantee. Bird’s original hard-sphere conditions are not reproduced. DSMC collision component: finite-N equilibrium, invariants and statistical error: Statistical diagnostics cover fixed 64-seed ensembles, not every seed. Conservation correlates particles within a seed; do not use IID KS p-values. No spatial streaming, collision cells, speed-dependent hard-sphere selection or transport coefficients. Additional fixed examples: Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow. Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow. Additional fixed examples: Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. RH validates far states/full fluxes,not an exact internal shock profile. Saved phase space is not a2D physical flow.

Other names: DSMC法, direct simulation Monte Carlo, 直接シミュレーションモンテカルロ法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/dsmc/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/dsmc/



- Reference: https://doi.org/10.1063/1.1710976 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://global.oup.com/academic/product/molecular-gas-dynamics-and-the-direct-simulation-of-gas-flows-9780198561958 — Method-specific source; see the detailed reading for source role and actual review depth.

## Small fixed-input validation supplements

Conservation and Maxwell relaxation in a homogeneous DSMC collision component: Test conservation and relaxation toward equilibrium through randomized pair collisions of homogeneous Maxwell molecules. DSMC collision component: finite-N equilibrium, invariants and statistical error: Distinguish finite-particle equilibrium from the Maxwell limit; compare independent sphere samples, analytic anisotropy decay and across-seed uncertainty.

等質DSMC衝突成分の保存則・Maxwell分布: 等質なMaxwell分子のランダム二体衝突で、保存則と平衡分布への緩和を検証します。 DSMC衝突成分：有限N平衡・保存則・統計誤差: 有限粒子数の平衡をMaxwell極限と区別し、独立な球面標本、解析的異方性減衰、seed間誤差と比較します。

- Conservation and Maxwell relaxation in a homogeneous DSMC collision component: https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json

- DSMC collision component: finite-N equilibrium, invariants and statistical error: https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json

- Hard-sphere DSMC finite-Kn Couette flow: https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/
- Hard-sphere DSMC finite-Kn Fourier heat conduction: https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/result.json

- Hard-sphere DSMC Mach2 planar shock: https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/atlas-dsmc-shock-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/results/result.json

Common execution records: [{"id": "dsmc", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "dsmc-statistics", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "dsmc-couette", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "dsmc-fourier", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "dsmc-planar-shock", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [剛体球Boltzmann輸送と壁・流入出](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hard-sphere-boltzmann-ja) (`hard-sphere-boltzmann`; dsmc-couette, dsmc-fourier, dsmc-planar-shock)

#### 問題の図 (`method-problems-ja`)

##### [等質DSMC衝突成分の保存則・Maxwell分布](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=ja) (`maxwell-collisions`)

![等質なMaxwell分子の衝突成分。512/2048/8192粒子・16seedの保存モーメント誤差・標本不確かさと、物理時刻ではない衝突roundごとの異方性緩和。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/dsmc.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=ja#code-ja)

- [等質DSMC衝突成分の保存則・Maxwell分布](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=ja) (`dsmc`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

等質なMaxwell分子のランダム二体衝突で、保存則と平衡分布への緩和を検証します。

- [DSMC衝突成分：有限N平衡・保存則・統計誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=ja) (`dsmc-statistics`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

有限粒子数の平衡をMaxwell極限と区別し、独立な球面標本、解析的異方性減衰、seed間誤差と比較します。

##### [硬球DSMCの有限Kn Couette流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=ja) (`dsmc-couette`)

![保存した実粒子の位置–速度ヒストグラム。1次元位置と分子速度の位相空間であり、2D物理流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette-preview.png)

セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=ja#code-ja)

- [硬球DSMCの有限Kn Couette流](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=ja) (`dsmc-couette`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip)

物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。

##### [硬球DSMCの有限Kn Fourier熱伝導](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=ja) (`dsmc-fourier`)

![保存した実粒子の位置–速度ヒストグラム。1次元位置と分子速度の位相空間であり、2D物理流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier-preview.png)

セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=ja#code-ja)

- [硬球DSMCの有限Kn Fourier熱伝導](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=ja) (`dsmc-fourier`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip)

物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。

##### [硬球DSMCのMach2平面衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=ja) (`dsmc-planar-shock`)

![保存した実粒子の位置–速度ヒストグラム。1次元位置と分子速度の位相空間であり、2D物理流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/results/dsmc-planar-shock-preview.png)

セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。 開境界のmacro粒子到着数は平均を保つfloor(平均)+Bernoulli(小数部)で分散を下げます。Poisson数揺らぎや熱揺らぎの再現は主張しません。 既存4seedを残して次の8連番seedを追加します。一様順列と安定整数sortは対選択法則を保ちますが、乱数消費と軌道のbit一致は主張しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=ja#code-ja)

- [硬球DSMCのMach2平面衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=ja) (`dsmc-planar-shock`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/atlas-dsmc-shock-2026-11-23.zip)

物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [等質DSMC衝突成分の保存則・Maxwell分布](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=ja#references-ja) (`maxwell-collisions`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [硬球DSMCの有限Kn Couette流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=ja#references-ja) (`dsmc-couette`)

- [硬球DSMCの有限Kn Couette流](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-couette-ja) (`dsmc-couette`; 同じ問題の参照; 有限格子の数値参照)

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。

[既存の参照図](/numerical-methods-atlas/validation/dsmc-couette/?lang=ja#dsmc-couette-ja-measurements)

##### [硬球DSMCの有限Kn Fourier熱伝導](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=ja#references-ja) (`dsmc-fourier`)

- [硬球DSMCの有限Kn Fourier熱伝導](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-fourier-ja) (`dsmc-fourier`; 同じ問題の参照; 有限格子の数値参照)

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。

[既存の参照図](/numerical-methods-atlas/validation/dsmc-fourier/?lang=ja#dsmc-fourier-ja-measurements)

##### [硬球DSMCのMach2平面衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=ja#references-ja) (`dsmc-planar-shock`)

- [硬球DSMCのMach2平面衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-planar-shock-ja) (`dsmc-planar-shock`; 同じ問題の参照; 有限格子の数値参照)

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。RHは遠方状態・流束だけの参照で、内部構造の厳密解ではありません。図は保存した粒子位相空間であり、2D物理流れではありません。

[既存の参照図](/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=ja#dsmc-planar-shock-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/dsmc/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 等質DSMC衝突成分の保存則・Maxwell分布 (`dsmc`)

[等質DSMC衝突成分の保存則・Maxwell分布](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

等質なMaxwell分子のランダム二体衝突で、保存則と平衡分布への緩和を検証します。

##### DSMC衝突成分：有限N平衡・保存則・統計誤差 (`dsmc-statistics`)

[等質DSMC衝突成分の保存則・Maxwell分布](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json)

有限粒子数の平衡をMaxwell極限と区別し、独立な球面標本、解析的異方性減衰、seed間誤差と比較します。

##### 硬球DSMCの有限Kn Couette流 (`dsmc-couette`)

[硬球DSMCの有限Kn Couette流](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/verification.json)

物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。

##### 硬球DSMCの有限Kn Fourier熱伝導 (`dsmc-fourier`)

[硬球DSMCの有限Kn Fourier熱伝導](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/verification.json)

物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。

##### 硬球DSMCのMach2平面衝撃波 (`dsmc-planar-shock`)

[硬球DSMCのMach2平面衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/atlas-dsmc-shock-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/verification.json)

物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

等質DSMC衝突成分の保存則・Maxwell分布: 等質なMaxwell分子のランダム二体衝突で、保存則と平衡分布への緩和を検証します。 DSMC衝突成分：有限N平衡・保存則・統計誤差: 有限粒子数の平衡をMaxwell極限と区別し、独立な球面標本、解析的異方性減衰、seed間誤差と比較します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py)
- [/code/validated-examples/2026-11-22/particles/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py)
- [/code/validated-examples/2026-11-22/particles/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py)
- [/code/validated-examples/2026-11-22/particle-transport/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py)
- [/code/validated-examples/2026-11-22/particle-transport/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/run.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/dsmc.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/dsmc.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/diagnostics.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/references/generate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/references/generate.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/references/qualify.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/run.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/dsmc.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/dsmc.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/diagnostics.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/references/generate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/references/generate.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/references/qualify.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/test_core.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/test_core.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/test_wall.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/test_wall.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/test_arrivals.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/test_arrivals.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/test_core.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/test_core.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/test_matching.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/test_matching.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/test_shock.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/test_shock.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Hard-sphere Boltzmann transport,walls and reservoirs](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hard-sphere-boltzmann-en) (`hard-sphere-boltzmann`; dsmc-couette, dsmc-fourier, dsmc-planar-shock)

#### Problem figures (`method-problems-en`)

##### [Conservation and Maxwell relaxation in a homogeneous DSMC collision component](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en) (`maxwell-collisions`)

![Homogeneous Maxwell-molecule collision component: stored moment errors/seed uncertainty for 512/2048/8192 particles over 16 seeds, and anisotropy per collision round, not physical time.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/dsmc.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en#code-en)

- [Conservation and Maxwell relaxation in a homogeneous DSMC collision component](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=en) (`dsmc`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

Test conservation and relaxation toward equilibrium through randomized pair collisions of homogeneous Maxwell molecules.

- [DSMC collision component: finite-N equilibrium, invariants and statistical error](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=en) (`dsmc-statistics`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

Distinguish finite-particle equilibrium from the Maxwell limit; compare independent sphere samples, analytic anisotropy decay and across-seed uncertainty.

##### [Hard-sphere DSMC finite-Kn Couette flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=en) (`dsmc-couette`)

![Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette-preview.png)

Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=en#code-en)

- [Hard-sphere DSMC finite-Kn Couette flow](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en) (`dsmc-couette`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip)

Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.

##### [Hard-sphere DSMC finite-Kn Fourier heat conduction](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en) (`dsmc-fourier`)

![Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier-preview.png)

Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en#code-en)

- [Hard-sphere DSMC finite-Kn Fourier heat conduction](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=en) (`dsmc-fourier`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip)

Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.

##### [Hard-sphere DSMC Mach2 planar shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=en) (`dsmc-planar-shock`)

![Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/results/dsmc-planar-shock-preview.png)

Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time. Open-reservoir macro counts use unbiased floor(mean)+Bernoulli(fraction) per face/species/half-stream to reduce artificial sampling variance; no Poisson number-fluctuation or thermodynamic-fluctuation reproduction claim. Retain the original four seeds and append the next eight consecutive seeds; uniform permutation/stable integer sorting preserves the ideal within-cell matching law,not RNG consumption or bit-identical trajectories.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=en#code-en)

- [Hard-sphere DSMC Mach2 planar shock](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=en) (`dsmc-planar-shock`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/atlas-dsmc-shock-2026-11-23.zip)

Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.


#### Exact / reference solutions (`method-references-en`)

##### [Conservation and Maxwell relaxation in a homogeneous DSMC collision component](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en#references-en) (`maxwell-collisions`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Hard-sphere DSMC finite-Kn Couette flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=en#references-en) (`dsmc-couette`)

- [Finite-Kn hard-sphere Couette flow](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-couette-en) (`dsmc-couette`; Same-problem reference; Finite-grid numerical reference)

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.

[Existing reference profile](/numerical-methods-atlas/validation/dsmc-couette/?lang=en#dsmc-couette-en-measurements)

##### [Hard-sphere DSMC finite-Kn Fourier heat conduction](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en#references-en) (`dsmc-fourier`)

- [Finite-Kn hard-sphere Fourier heat conduction](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-fourier-en) (`dsmc-fourier`; Same-problem reference; Finite-grid numerical reference)

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.

[Existing reference profile](/numerical-methods-atlas/validation/dsmc-fourier/?lang=en#dsmc-fourier-en-measurements)

##### [Hard-sphere DSMC Mach2 planar shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=en#references-en) (`dsmc-planar-shock`)

- [Mach2 planar hard-sphere shock](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-planar-shock-en) (`dsmc-planar-shock`; Same-problem reference; Finite-grid numerical reference)

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. RH validates far states/full fluxes,not an exact internal shock profile. Saved phase space is not a2D physical flow.

[Existing reference profile](/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=en#dsmc-planar-shock-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/dsmc/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Conservation and Maxwell relaxation in a homogeneous DSMC collision component (`dsmc`)

[Conservation and Maxwell relaxation in a homogeneous DSMC collision component](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

Test conservation and relaxation toward equilibrium through randomized pair collisions of homogeneous Maxwell molecules.

##### DSMC collision component: finite-N equilibrium, invariants and statistical error (`dsmc-statistics`)

[Conservation and Maxwell relaxation in a homogeneous DSMC collision component](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json)

Distinguish finite-particle equilibrium from the Maxwell limit; compare independent sphere samples, analytic anisotropy decay and across-seed uncertainty.

##### Hard-sphere DSMC finite-Kn Couette flow (`dsmc-couette`)

[Hard-sphere DSMC finite-Kn Couette flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/verification.json)

Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.

##### Hard-sphere DSMC finite-Kn Fourier heat conduction (`dsmc-fourier`)

[Hard-sphere DSMC finite-Kn Fourier heat conduction](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/verification.json)

Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.

##### Hard-sphere DSMC Mach2 planar shock (`dsmc-planar-shock`)

[Hard-sphere DSMC Mach2 planar shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/atlas-dsmc-shock-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/verification.json)

Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Conservation and Maxwell relaxation in a homogeneous DSMC collision component: Test conservation and relaxation toward equilibrium through randomized pair collisions of homogeneous Maxwell molecules. DSMC collision component: finite-N equilibrium, invariants and statistical error: Distinguish finite-particle equilibrium from the Maxwell limit; compare independent sphere samples, analytic anisotropy decay and across-seed uncertainty.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

###### Related source

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py)
- [/code/validated-examples/2026-11-22/particles/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py)
- [/code/validated-examples/2026-11-22/particles/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py)
- [/code/validated-examples/2026-11-22/particle-transport/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py)
- [/code/validated-examples/2026-11-22/particle-transport/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/run.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/dsmc.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/dsmc.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/diagnostics.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/references/generate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/references/generate.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/references/qualify.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/run.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/dsmc.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/dsmc.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/diagnostics.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/references/generate.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/references/generate.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/references/qualify.py)

###### Package tests

- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/test_core.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/test_core.py)
- [/code/validated-examples/2026-11-23/dsmc-wall/test_wall.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/test_wall.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/test_arrivals.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/test_arrivals.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/test_core.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/test_core.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/test_matching.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/test_matching.py)
- [/code/validated-examples/2026-11-23/dsmc-shock/test_shock.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/test_shock.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
