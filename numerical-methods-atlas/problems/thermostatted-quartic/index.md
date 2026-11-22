# 非調和CSVRとLangevin：Boltzmann求積との分布比較 / Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature

https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/

## 日本語

[弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-thermostats/#csvr-langevin-quartic) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#thermostatted-quartic)

### 方程式・問題の定義

Hamilton系へのリンクは非調和ポテンシャルの力学部分です。確率温度浴を加えたCSVR・Langevinの分布検証を行います。

#### [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja)

$$
\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}
$$

$$
H=\frac{p^2}{2}+V(q)
$$

正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。

#### 非調和CSVRとLangevin：Boltzmann求積との分布比較

補助実行例 · 実行例の定義・検証式

$$
U(q)=\sum_{i=1}^2\left(\frac{\omega_i^2q_i^2}{2}+\frac{\lambda q_i^4}{4}\right),\quad\rho(q)=Z^{-1}e^{-U(q)/T}
$$

$$
F_H(E)=\int_{U(q)\le E}\rho(q)\left[1-e^{-(E-U(q))/T}\right]dq,\qquad N_f=2
$$

$$
\mathbb E H=\mathbb E K+\mathbb E U,\quad\operatorname{Var}H=\operatorname{Var}K+\operatorname{Var}U
$$

弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。

### 厳密解・参照解

非調和ポテンシャルのBoltzmann分布を独立数値求積し、CSVR・Langevinの有限刻み分布とモーメントを比較します。厳密な確率軌道の比較ではありません。

#### 非調和CSVRとLangevin：Boltzmann求積との分布比較

座標の正規化・CDF・Uの平均/分散を1D求積、HのCDFをKの指数分布と2D座標Boltzmann密度の畳込み積分で得ます。求積公差2e−10と2e−12の差を保存し、独立棄却集団でもH分布を検査。q,p,K,Hの相関には複製間の標準誤差を併記し、刻み差と標本誤差を混同しません。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [確率的速度リスケーリング（CSVR）](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Langevinサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja)

補助実行例

弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。

m=kB=T=1、ω=(1,1.7)、λ=0.2、U=Σ(ω²q²/2+λq⁴/4)。正準8192複製、温度摂動4096複製、t=20、τ=0.25/1、h=0.1/0.05、lag=0/0.5/1/2/4。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

特定の分離可能な四次2自由度・固定seedだけの小さな例です。Hを調和系のGamma分布と扱いません。全系相関には独立な厳密動力学参照がなく、相関一致や統計誤差に隠れる時間次数を合格主張しません。成熟分子系・輸送係数・量子・第一原理MDの検証ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/thermostats/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/run.py)
- [/code/validated-examples/2026-11-22/thermostats/thermostats.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/thermostats.py)
- [/code/validated-examples/2026-11-22/thermostats/test_thermostats.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/test_thermostats.py)

## English

[Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-thermostats/#csvr-langevin-quartic) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#thermostatted-quartic-en)

### Equations and problem definitions

The Hamiltonian link identifies the anharmonic mechanical part; validation concerns distributions with added stochastic CSVR/Langevin heat baths.

#### [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en)

$$
\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}
$$

$$
H=\frac{p^2}{2}+V(q)
$$

Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity.

#### Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature

Supplementary execution example · Example definition or validation formula

$$
U(q)=\sum_{i=1}^2\left(\frac{\omega_i^2q_i^2}{2}+\frac{\lambda q_i^4}{4}\right),\quad\rho(q)=Z^{-1}e^{-U(q)/T}
$$

$$
F_H(E)=\int_{U(q)\le E}\rho(q)\left[1-e^{-(E-U(q))/T}\right]dq,\qquad N_f=2
$$

$$
\mathbb E H=\mathbb E K+\mathbb E U,\quad\operatorname{Var}H=\operatorname{Var}K+\operatorname{Var}U
$$

Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.

### Exact and reference solutions

Independently integrate the anharmonic Boltzmann distribution and compare finite-step CSVR/Langevin distributions and moments, not exact stochastic trajectories.

#### Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature

Obtain coordinate normalizers/CDFs and U moments by 1D quadrature, and the H CDF by convolving exponential K with the 2D positional Boltzmann density. Save the difference between quadrature tolerances 2e−10 and 2e−12; a separate rejection ensemble also checks H. Report independent-replica standard errors for q,p,K,H correlations, keeping step differences distinct from sampling noise.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [Stochastic velocity rescaling (CSVR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en)

Supplementary execution example

Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.

m=kB=T=1, omega=(1,1.7), lambda=0.2, U=sum(omega²q²/2+lambda q⁴/4). Use 8192 canonical and 4096 heated replicas, t=20, tau=0.25/1, h=0.1/0.05, lags 0/0.5/1/2/4.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

A small example for one separable two-mode quartic potential and fixed seeds. H is not treated as harmonic Gamma. No independent exact full-system dynamical reference is claimed, and neither matching correlations nor time order hidden by sampling noise is an acceptance claim. Molecular transport, quantum and ab initio MD are outside scope.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/thermostats/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/run.py)
- [/code/validated-examples/2026-11-22/thermostats/thermostats.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/thermostats.py)
- [/code/validated-examples/2026-11-22/thermostats/test_thermostats.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/test_thermostats.py)
