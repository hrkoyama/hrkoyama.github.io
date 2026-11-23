# Nonperiodic wall flow / 非周期の壁面流れ

Two fixed educational examples share a genuine 2D streamfunction/vorticity Navier–Stokes solver. Dependencies are the three exact pins in requirements.txt. No network, private checkout, API key, external solver, or heavy reference regeneration is needed.

```bash
python -m pip install -r requirements.txt
python -W error -m pytest -q -p no:cacheprovider
python -W error run.py --input inputs.json --output results
# Optional scientific figures, separate from the three-pin runtime:
python -m pip install -r requirements-plot.txt
python plot.py --results results/result.json --output results
```

`cavity-ghia-re100`: unit square, Re100, viscosity .01, moving top u=1, other wall velocities 0; corner velocities 0. Compare actual steady solutions on 17/33/65 nodes with manually transcribed original Ghia1982 TablesI/II at their printed coordinates. Report true steady transport residual, streamfunction Poisson residual, discrete divergence, centerline errors and grid primary-vortex center against TableV. Grids and residual stop/caps are frozen in inputs.json.

`wall-manufactured`: same numerical solver and actual Thom wall closure, homogeneous no-slip walls, psi=8x²(1−x)²y²(1−y)². Analytic curl forcing is evaluated from explicit derivatives; an independent tensor-polynomial evaluator qualifies it. Measure streamfunction/velocity grid order, actual wall-vorticity and velocity-gradient wall-shear errors. Thom's local vorticity approximation is only first-order; no second-order wall-shear promise is made. Exact wall vorticity is never imposed. The fully nonperiodic manufactured case exercises forcing, Poisson and wall closure, not a separate toy algebraic equation.

A separate manufactured p=x²+y²+sin(pi*x)sin(pi*y) exercises the same nonzero Dirichlet Poisson operator plus second-order interior/one-sided boundary gradient. It is an operator verification with an analytic reference, not a physical pressure field coupled to the cavity. Streamfunction evolution eliminates pressure, so there is no pressure gauge in either flow solve and cavity pressure is uncomputed.

22 meaningful pytest checks and94 numerical gates across six fixed flow grids are declared before execution in pre-run-contract.json; pytest and the full runner must share 120 seconds in public CI. Inputs, acceptance, scientific source, test and reference files are hash-bound. A convergence failure remains a failed result. No state clipping, retries or tolerance relaxation are implemented.

Outputs: result.json, two CSV tables, six NPZ files containing computed fields, full reference fields where applicable, residual/Courant history and separate manufactured pressure arrays. plot.py reads saved arrays and generates both main scientific figures and gallery previews as PNG/SVG/PDF. Plotting does not rerun the solver. Printed coordinates have4digits; Ghia data are numerical reference values, not an exact continuum solution. The cavity's singular lid corners limit global regularity; no high-Re/turbulence, cavity pressure, universal convergence proof, or reproduction of Ghia's CSI-MG method is claimed.

出力は実際に計算した速度・流れ関数・渦度・残差履歴を含みます。製造解にも同じThom壁条件を使い、厳密な壁渦度の注入で境界誤差を隠しません。圧力は別の非零Dirichlet製造問題だけを検査し、キャビティ圧力の検証とは区別します。原著の閲覧箇所・転記・数式の導出・利用条件はreferences/README.mdに記録しています。第三者論文PDFは配布しません。

Code: MIT (LICENSE). Newly constructed inputs/data/figures/documentation: CC BY4.0, except the limited attributed Ghia numeric facts; no license claim over the source article. Cite Ghia, Ghia & Shin1982, DOI10.1016/0021-9991(82)90058-4 and Salari & Knupp2000, DOI10.2172/759450 as described in references/source-review.json.

The initial attempt passed the original 20 pytest checks and completed all numerical fields, then failed final JSON serialization because one table qualifier returned a NumPy bool. Its full source, fields, CSV and failed logs remain in attempts/01; it has no fabricated result.json. Revision2 casts qualifier decisions to native bool and adds one separate serialization regression. Inputs, acceptance, solver, runner and the original 20-test file are byte-identical. The successful revision ran 21 checks and 94 gates in about 7.113 seconds; every array in all six saved NPZ files is bit-identical to the first attempt. The revised contract explicitly distinguishes the original declaration from creation of the revision after that failed run.

Revision3 repairs the public-verifier result envelope only: top-level checks name the two case IDs, the prior three diagnostic decisions are retained under summary_checks, termination is fixed_budget_completed and failure is null. Add one complete-envelope regression for22total tests; inputs, acceptance, solver, references and all21prior tests remain unchanged. The successful revision2 source/results/logs are preserved in attempts/02. This revision is declared after the earlier attempts and before its own execution.

The nested public attempts/02 archive retains every scientific source, JSON/CSV/NPZ and log. Only12duplicate PNG/SVG/PDF presentations are omitted there to respect the source archive format; hashes, exact persistent private-backup locations and the plot command are in attempts/02/presentation-omissions.json. No numerical data is omitted; current presentations are included normally.
