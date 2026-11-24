# Geometric controls / 幾何積分の固定比較

Three independently authored educational cases contain 44 fixed primary evolutions and 282 scientific decisions: constrained pendulum(10/74), Kepler controls(16/92), and coupled frequencies(18/116). The 32 pytest operator/ownership tests are separate from those 44 evolutions. The initial local shared run actually passed all 32 tests, 44 evolutions and 282 decisions in 4.45745 seconds; this is not a universal runtime guarantee. The 67-check reference qualification is separate.

3例は拘束単振り子、離心率別Kepler軌道、結合2周波数系です。44主軌道・282判定と32 pytestを区別し、未実行を成功とは数えません。

## Running the fixed protocol

Use Python 3.12 with NumPy 2.0.2, SciPy 1.14.1 and pytest 8.3.5. Set OPENBLAS_NUM_THREADS, OMP_NUM_THREADS, MKL_NUM_THREADS and VECLIB_MAXIMUM_THREADS to 1. Run `python -B -W error -m pytest -q -p no:cacheprovider`, then `python -B -W error run.py --input inputs.json --output NEW_DIRECTORY`. Main requires the exact frozen input/source and qualified portable cache; it never regenerates the two independent angular DOP853 trajectories. Reference-first ordering applies to the 44 main evolutions; pytest has its own small operator trajectories. The combined public budget is 120 seconds, without automatic retries.

`python plot.py --results NEW_DIRECTORY/result.json --output FIGURE_DIRECTORY` reads saved arrays only. Plotting additionally uses Matplotlib 3.9.4. It writes a distinct main and gallery preview for every case, each as PNG/SVG/PDF.

## Scientific scope

SHAKE owns position pairs and reconstructs momentum only at interior nodes. RATTLE owns full-time q/p and enforces final tangency. The centered finite-C identity, reduced-map finite-difference proxy and full-state versus pair reversals have distinct scopes. The original 1977/1983 full articles remain unread; selected author lecture notes were actually rendered/read.

Kepler uses relative coordinates with no softening, e=0.1/0.7 and a=mu=1. Energy and angular momentum are distinct from full-state phase accuracy. A variable schedule regenerated from reversed states is explicitly a diagnostic without a time-symmetry assertion. No canonical symplectic-defect measurement is claimed for that variable map. Pre-execution R2 resolution uses 512/1024/2048 steps for one period and 2048 nominal steps per period for ten-period controls; asymptotic planning estimates were not rigorous error bounds.

The coupled system retains alpha=1 and both normal modes. Coordinate energies can exchange while continuum normal-mode energies are invariant. The ideal mathematical-pi map, stored binary64 coefficient map and rounded scalar trajectory are separate objects. Trigonometric values are never snapped. Actual central float maps are labelled unresolved near degeneracy; off-central ideal classes and finite-horizon actual spectra are reported separately. The roundoff allowance is a finite arithmetic construction, not a universal stability theorem.

## Retention and reference history

Completed full arrays are saved before any subsequent reference/diagnostic operation. Each trajectory owns accepted states and counts; a small checkpoint is written every 256 steps. Ordinary exceptions dump accepted prefixes and current candidates. SIGKILL can retain only the latest already written checkpoint, not an interrupted arithmetic operation. Final NPZ arrays and numeric CSV retain actual times and states; SHAKE endpoint momenta are absent rather than replaced with zeros or NaN. No hidden projection, solver retry, softening or norm-cap recovery is used.

The first independent qualification genuinely failed 63/64: direct ellipj at unwrapped arguments up to 100 gave a dn identity discrepancy 1.0136336214827679e-13, above the fixed 1e-13. All candidates, logs, source and the failed decision are retained privately by the author. R3 uses the exact common 4K period, preserving unwrapped/reduced arguments and winding; dn remains a direct ellipj output, never a repaired square root. All original 64 thresholds/samples remain unchanged and three separate direct period tests are added. This is a reference evaluator revision after a failure, not a first-ever execution contract or threshold relaxation. Actual current qualification and main outcomes live in their JSON receipts.

初回参照資格63/64の未達を保存し、周期性による引数縮約を別版として検証します。dnを恒等式から作り直さず、元64条件と時刻を維持します。実際の成否は保存JSONをご覧ください。

Official JPL documentation is cited only for the Kepler equation; publication date was not verified. NIST 2026 denotes DLMF version 1.2.8 (released 2026-09-15), not its initial publication. Hairer dates refer to dates displayed on the selected lecture notes. Access dates are 2026-11-24. No original paper body is bundled.

## Current-platform coefficient portability

The author-platform Decimal caches remain qualified algorithm/history evidence, not a promise that another platform produces identical libm sin/cos bits. Main saves its actual coefficient values and hexadecimal strings first. It then evaluates Decimal80 and Decimal120 actions for each of the twelve probes (24 actions) and Decimal80 for six accuracy trajectories (six actions). These 30 linear reference-map actions are separate from 44 primary evolutions and do not regenerate the two angular DOP853 evolutions or the 67-check qualification. The existing 1e-50 precision agreement is additionally required by each existing probe reference gate. All 282 gate IDs, physical inputs, windows, error limits and 120-second shared cap are preserved.

各probeは現在保存した係数hexからDecimal80/120を評価し、6精度軌道はDecimal80を用います。

## Multiplier column convention

SHAKE solves columns are eta, eta/h^2, position residual and Newton updates. Column1 uses the uniform recurrence normalization eta/h^2. For the first constrained half-step startup, the physical multiplier is 2*eta/h^2; later full position-Verlet steps use eta/h^2. Reverse-pair steps all use the later recurrence convention. RATTLE has its separate five-column normalization. No scientific gate or plot uses SHAKE column1.

SHAKEのsolves列はeta、eta/h^2、位置残差、Newton更新数です。列1は一律にeta/h^2ですが、初回半刻みの物理乗数は2eta/h^2、以後の位置Verletではeta/h^2です。逆位置対はすべて後者です。判定と図はこの列1を使いません。
