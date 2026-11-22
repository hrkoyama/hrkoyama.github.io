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
