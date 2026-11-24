# Long-time grazing PML in a dispersive medium

One small fixed educational case. Actual completion is recorded by the
immutable verification receipt and results/result.json, not by prototype
module labels. Historical UNEXECUTED docstrings remain byte-preserved where
the qualified original kernels are intentionally unchanged.

```sh
python -m pytest -q
python run.py --input inputs.json --output fresh-results
python plot.py --results fresh-results/result.json --output fresh-figures
```

Runtime/test pins: NumPy2.0.2, SciPy1.14.1 and pytest8.3.5 only. Plotting
additionally uses Matplotlib and reads saved fields; it never evolves them.
The shared public group deadline remains120seconds for pytest plus main.
Use fresh output; preserve failures and never retry or extend a window
automatically. All complete candidates are saved before later diagnostics.

Evolve a finite packet with an 80-degree central phase angle to T = 700, isolating boundary error against a no-PML reference on the same grid.

Use c = 1 and a homogeneous Lorentz medium with epsilon_inf = 1, delta_epsilon = 0.2 and omega_0 = 12 continuing through the PML. Joint refinement uses 512/768/1024 cells and peaks 6/9/12. The normal coarse control has peak 6; the damped fine companion has peak 12. Length 64, layer thickness 12, center 32, width 4 and carrier 6 are fixed.

Couple Yee and midpoint ADE updates to a trapezoidal derivative-memory filter at native times. Separate positive physical dissipation from signed numerical PML work, retaining all physical and auxiliary states.

Use five long trajectories: three joint grid/layer-strength resolutions, a normal control and a weakly damped companion. Reuse the byte-bound no-PML reference only after checking every unchanged reference argument. Retain the old 13 test bodies and add two parameter-policy/peak-12 work regressions; all original 44 long-trajectory gates remain unchanged.

The central angle is 80 degrees; finite kx bandwidth gives neighboring angles. The no-PML reference shares the discretization and initialization to isolate boundary error from bulk dispersion. Small operator and finite-trajectory checks do not prove global stability for arbitrary angles and materials. The joint family does not measure fixed-PML spatial order; the older 100 checks alone do not prove peak-12 global stability.

The first fixed-peak-6 experiment completed five evolutions with 42/44 gates passing. Preserve the unmet refinement ratios 1.00905 and 1.00306. The revised, predeclared peak proportional to N keeps peak times h fixed and targets the finite-layer/cap floor; every original gate and bound remains unchanged.

## 日本語

80度の中心位相角を持つ有限波束をT=700まで進め、境界誤差を同格子の無PML参照から分離します。

c=1、均質Lorentz媒質ε∞=1、Δε=0.2、ω0=12はPML内まで連続。512/768/1024点とpeak6/9/12を同時に細分化します。垂直粗格子はpeak6、弱減衰細格子対照はpeak12。長さ64、層幅12、中心32、幅4、carrier6は固定です。

Yee・中点ADEに時刻配置を保った台形微分memoryを結合。正の物理散逸と符号付きPML数値仕事を区別し、補助場を含め全状態を保存します。

3つの格子・層強度の同時細分化、垂直・弱減衰対照の5長時間計算。参照入力が全て不変なことを確認して同一byteの無PML参照を再利用します。旧13検査本体を保持し、policy・peak12直接仕事の2回帰を追加。全44長時間判定は不変です。

有限kx帯域の中心角が80度で、全成分が厳密に80度ではありません。無PML参照は同じ離散化・初期場を使い、伝播分散を除いた境界誤差用です。任意角度・材料での大域安定性証明ではありません。 固定PMLの空間次数を測る族ではなく、旧100検査だけでpeak12の大域安定性が証明されたとはしません。

初回の固定peak6は5進行を完了し44判定中42合格。細分化比1.00905/1.00306の未達を保持します。新しい事前固定のpeak=N比例の族はσpeak hを一定にし、有限層/cap反射床を減らす設計で、元の44判定と閾値を変更しません。

## References and retained first experiment

Primary-source URLs and exact selected reading scopes are in cases.json.
Original Yee, Berenger and Roden-Gedney papers are not claimed as read.
The existing r6 FDTD code/eight inputs/108 tests remain unchanged.
The old165-component result alone did not complete these full candidates.

history/first-full-main contains compact scientific results and old
changed-source texts. All complete original source and failed native NPZ
arrays remain in the retained private attempt. This compact public history
does not claim to contain every failed native field.

The independent, byte-exact qualified generator is visible as
references/isolated_reference.py. The public main uses the fixed NPZ cache;
it does not regenerate references or use spectral propagation for primary
updates. references/reuse-audit.json documents the unchanged call arguments.
The joint family is peak = 6N/512, not fixed-layer spatial order. Actual
peaks/rates are saved in records, CSV and NPZ; the normal control is peak6
and the damped fine companion is peak12.

## Documentation dates / 文書日付

Meep documentation: publication/revision date unverified; accessed 2026-11-24.
Meep文書の公開・改訂日は未確認で、2026-11-24は参照日です。

The original reading record and all scientific inputs, algorithms, references, tests and criteria are unchanged.
元の閲読記録と科学入力・数値アルゴリズム・参照データ・検査・受入基準は変更していません。
