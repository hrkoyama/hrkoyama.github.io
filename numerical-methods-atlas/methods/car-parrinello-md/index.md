# Car–Parrinello molecular dynamics / CPMD / カー–パリネロ法（CPMD）

Status: reading-only

Assign fictitious inertia to orbitals and propagate an orthonormality-constrained extended system with the nuclei.

電子軌道に仮想質量を与え、直交制約付きの拡張系で核と同時に進める。

Reading only. Adiabatic separation, fictitious-to-nuclear energy transfer and long trajectories are unvalidated.

Other names: CPMD, Car Parrinello, Car–Parrinello, Car Parrinello MD, カー・パリネロ法, カーパリネロ法, 第一原理分子動力学

Comparison notes: Reading only. Adiabatic separation, fictitious-to-nuclear energy transfer and long trajectories are unvalidated.

解説のみ。仮想電子運動の断熱性、エネルギー移動、長時間軌道は未検証です。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/periodic-dft/#first-principles-md
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/periodic-dft/#first-principles-md



- Reference: https://doi.org/10.1103/PhysRevLett.55.2471 — Publisher bibliography/abstract and original equations (3)–(5) and discussion of fictitious electronic motion near the BO surface consulted. The paper’s silicon dynamics have not been numerically reproduced.

Next: Maintain the reading, primary sources and links to existing small examples. Consider a dedicated implementation only when needed, starting with a small educational case; routine work excludes heavy convergence sweeps, reference regeneration and long MD.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
