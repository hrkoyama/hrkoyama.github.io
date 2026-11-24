# Long-time grazing PML in a dispersive medium

This is one small fixed educational example. The numerical inputs and all
acceptance criteria are bound before its first full execution. No parameters
or tolerances are selected from a successful result. NumPy 2.0.2, SciPy 1.14.1
and pytest 8.3.5 are the only required runtime/test dependencies.

```sh
python -m pytest -q
python run.py --input inputs.json --output fresh-results
python plot.py --results fresh-results/result.json --output fresh-figures
```

The plot command additionally uses Matplotlib and reads saved numerical data;
it never executes a solver. It accepts either result.json or its directory.
The public verifier provides the unchanged shared 120-second group deadline.
Every complete candidate is saved before reference diagnostics. Failures and
partial states are retained; output must be fresh and there is no retry loop.

Evolve a finite packet with an 80-degree central phase angle to T = 700, isolating boundary error against a no-PML reference on the same grid.

Use c = 1 and a homogeneous Lorentz medium with epsilon_inf = 1, delta_epsilon = 0.2 and omega_0 = 12 continuing through the PML. Main damping is gamma = 0, with a gamma = 0.005 companion. Length 64, PML thickness 12, peak 6, packet center 32, width 4 and carrier 6 are fixed.

Couple Yee and midpoint ADE updates to a trapezoidal derivative-memory filter at native times. Separate positive physical dissipation from signed numerical PML work, retaining all physical and auxiliary states.

Use five long trajectories: three grazing grids with 512/768/1024 cells, a normal control and a weakly damped companion. First compare periodic reference boxes of length 2048/4096 using an independent 5 × 5 Fourier update matrix; then check modified budgets, auxiliaries, residuals and boundary-field errors.

The central angle is 80 degrees; finite kx bandwidth gives neighboring angles. The no-PML reference shares the discretization and initialization to isolate boundary error from bulk dispersion. Small operator and finite-trajectory checks do not prove global stability for arbitrary angles and materials.



## 日本語

80度の中心位相角を持つ有限波束をT=700まで進め、境界誤差を同格子の無PML参照から分離します。

c=1、均質Lorentz媒質ε∞=1、Δε=0.2、ω0=12はPML内まで連続。主γ=0とγ=0.005対照。長さ64、PML幅12・peak6、中心32・幅4、carrier6です。

Yee・中点ADEに時刻配置を保った台形微分memoryを結合。正の物理散逸と符号付きPML数値仕事を区別し、補助場を含め全状態を保存します。

512/768/1024点の浅角度、垂直、弱減衰の5長時間計算。独立な5×5 Fourier更新行列の2048/4096周期box比較を先行し、修正収支・補助変数・残留と境界場誤差を検査します。

有限kx帯域の中心角が80度で、全成分が厳密に80度ではありません。無PML参照は同じ離散化・初期場を使い、伝播分散を除いた境界誤差用です。任意角度・材料での大域安定性証明ではありません。

The old r6 eight-input/108-test FDTD release and its scientific bytes are
unchanged. The earlier 165-component qualification is retained separately;
that result alone did not complete any of these three full candidates.
Primary-source URLs and the exact selected reading scope are in cases.json.
Original Yee, Berenger and Roden-Gedney papers are not claimed as read.

## Cached reference and visible generator

The public main consumes the fixed, separately qualified reference NPZ files.
The byte-identical qualified generator is included as
`references/isolated_reference.py` for inspection. It imports only NumPy and
SciPy, and is a library function rather than another main command. Reference
regeneration belongs to the separately reviewed qualification phase; it is
not silently repeated by the public main. The primary never calls this
spectral propagator for its actual field updates.

公開mainは固定・別資格済みの参照NPZを使います。同一byteの資格済み生成源を
references/isolated_reference.pyに同梱し、主計算が参照を再生成したり、
このスペクトル伝播器で主場を更新したりすることはありません。
