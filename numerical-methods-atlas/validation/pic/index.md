# CIC静電PICの冷たいプラズマ振動

1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。

## 前提・単位・境界

長さ2pi、電子の電荷質量比−1、静止イオン背景密度1、plasma frequency=1の無次元系。quiet startから振幅0.001の微小正弦変位を与えます。

## 採用した計算法

CIC電荷割当てと同じ重みの場補間、ゼロ平均のスペクトルPoisson解、速度Verletを組み合わせます。実数の奇微分の規約により、電場のNyquistモードはゼロにします。

$$
\dot x_i=v_i,\quad\dot v_i=-E_h(x_i),\quad-\phi_{xx}=\rho,\quad E=-\phi_x
$$

$$
A(t)/A(0)\simeq\cos(\omega_pt),\qquad\omega_p=1
$$

## 比較・検証

32・64・128格子の系列と、別の512格子上の時間刻み系列を分けます。変位モードを連続線形理論のcos(t)と比較し、全電荷・Poissonポテンシャル残差・単一粒子の自己力を検査します。

## 確認の限界

有限振幅・有限粒子数の誤差床があります。非線形不安定性、Landau減衰、衝突、電磁PIC、相対論粒子、境界流入出の検証ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "mode_error": 0.0008867237363958114,
    "time_mode_error": 0.0004385575782555884,
    "charge_error": 1.743934249004316e-16,
    "poisson_residual": 1.0587911840678754e-22,
    "self_force": 3.3306690738754696e-16,
    "grid_refinement_ratio": 0.05753235309401034,
    "time_refinement_ratio": 0.014260976320524699
  },
  "checks": {
    "mode_error": true,
    "charge_error": true,
    "poisson_residual": true,
    "self_force": true,
    "time_error": true,
    "grid_refines": true,
    "time_refines": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- R. W. Hockney and J. W. Eastwood (1988). Computer Simulation Using Particles. https://doi.org/10.1201/9780367806934; review_level=publisher-preview-and-metadata
  出版社配布プレビューの書誌・粒子モデルの導入と目次を確認。CICや冷たいプラズマの歴史的出典とし、全書の監査は主張しません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Cold-plasma oscillation with electrostatic CIC PIC

Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.

## Assumptions, units and boundaries

Dimensionless length 2pi, electron charge/mass −1, stationary ion density one and plasma frequency one. A quiet start receives a small sinusoidal displacement of amplitude 0.001.

## Adopted numerical method

Combine CIC deposition and matching field gathering, a mean-zero spectral Poisson solve and velocity Verlet. Set the field Nyquist mode to zero for a real skew-adjoint spectral derivative.

$$
\dot x_i=v_i,\quad\dot v_i=-E_h(x_i),\quad-\phi_{xx}=\rho,\quad E=-\phi_x
$$

$$
A(t)/A(0)\simeq\cos(\omega_pt),\qquad\omega_p=1
$$

## References and validation

Separate a 32/64/128-grid sweep from timestep refinement on a 512 grid. Compare displacement amplitude with continuum linear cos(t), and check charge compatibility, potential-Poisson residual and single-particle self force.

## Limits

Finite amplitude and finite particles leave an error floor. Nonlinear instabilities, Landau damping, collisions, electromagnetic/relativistic PIC and open particle boundaries are unvalidated.

## Stored measurements and decisions

```json
{
  "metrics": {
    "mode_error": 0.0008867237363958114,
    "time_mode_error": 0.0004385575782555884,
    "charge_error": 1.743934249004316e-16,
    "poisson_residual": 1.0587911840678754e-22,
    "self_force": 3.3306690738754696e-16,
    "grid_refinement_ratio": 0.05753235309401034,
    "time_refinement_ratio": 0.014260976320524699
  },
  "checks": {
    "mode_error": true,
    "charge_error": true,
    "poisson_residual": true,
    "self_force": true,
    "time_error": true,
    "grid_refines": true,
    "time_refines": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- R. W. Hockney and J. W. Eastwood (1988). Computer Simulation Using Particles. https://doi.org/10.1201/9780367806934; review_level=publisher-preview-and-metadata
  Publisher preview bibliography, introduction and contents checked; historical source for CIC/cold plasma, not a full-book audit.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
