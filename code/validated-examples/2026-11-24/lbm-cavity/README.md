# lbm-cavity: fixed-input educational LBM

日本語: lbm-cavity-re100。事前契約・固定入力・原典閲読範囲をこのsourceに保持します。実際の合否・実測時間は`results/result.json`と独立ZIPの`verification.json`で確認し、ソースを読んだだけで成功と解釈しません。既存配布版や他手法の成功を流用しません。

English: actual2D kinetic evolutions for `lbm-cavity-re100`. The pre-run contract fixes source, inputs, references and gates. Actual outcome/runtime live in `results/result.json` and independent-ZIP `verification.json`; source inspection alone is not a pass.

## Execution / 実行

Requires Python3.12 with exactly numpy2.0.2, scipy1.14.1, pytest8.3.5 plus a systemC++17compiler (`c++`, or explicit CXX). No native binary is shipped. `native.py` compiles `kernel.cpp` under TMPDIR with `-O2 -std=c++17 -ffp-contract=off -fPIC -Wall -Wextra -Werror`; nofastmath, no compiler install/network. Shared library/objects never enter generated scientific results. Both pytest's compilation and main's separate compilation count toward the same externally enforced120s per group. Compiler timeout15s is explicit; stdout/stderr/command/failure are retained.

```sh
python -B -W error -m pytest -q -p no:cacheprovider --junitxml=FRESH_RECEIPT/tests.xml
python -B -W error run.py --input inputs.json --output FRESH_RESULTS
python plot.py --results FRESH_RESULTS --output FRESH_RESULTS
```

Plotting additionally uses matplotlib3.9.4. Plotting is separate from the scientific120s and reads only saved arrays; it never reruns physics. All3groups use one native/source algorithm; each packet is self-contained.

## Inputs, units, boundaries / 入力・単位・境界

`inputs.json`, `acceptance.json` and `DESIGN.md` specify actual lattice/physical scales, integer counts, initialization and boundaries. Latticecs²=1/3, nu_lattice=(tau-.5)/3; u_physical=u_lattice*dx/dt, p_physical=(rho-meanrho)/3*(dx/dt)². Pressure gauges are explicitly removed only for comparison, without population/density repair. No observed-speed normalization, field reset after initialization, clipping, dynamic timestep/endpoint extension, adaptive convergence stop, sample selection or retry.

Flat moving walls use an independently signed halfway reflection. Curved boundaries use independently derived2point linear link interpolation; shortqrequires the declared interior point and fails if missing. Wall andopen mass/momentum are actual outgoing/incomingpopulation ledgers. Curved interpolation can change totalmass, which is reported separately from exact ledger closure. 

For cylinder2D-1, source printed3/7permits a user-selectedoutlet; the adoptedwet-nodeZou-He rho1withprevious-interiortangentialvelocity is **not** laterFEATflowdo-nothing. OriginalTable3ranges are author-estimated numerical intervals, not rigorous bounds. Separate frozen coarse-LBM tolerances, Ma, stationarity and2grid sensitivity bound this finite case. MeanU.2,D.1,nu.001defineRe20 and force coefficients; no peak-speed substitution. Initial straight-Poiseuille pressure is only a guess, not an imposed cylinderreference. The annular control does not replace cylinder flow.

TGV diffusive refinement couples grid/time/Mach, amplitude changesRe, and the half-step probe also changestau/Mach; no puretime-order claim. Ghia is an independent rounded incompressible reference, not exact or anotherLBMexecution.

## Fixed acceptance and reference scope / 事前判定と参照

This group freezes22meaningfulpytestchecks, 3actualmainkinetic evolutions and37casegates. Closed-formTGV/annulus references are independently qualified byFourier orCartesian/radial differentiation; these are continuum references,not exact finite-Mach kinetic solutions. Originalbenchmarktable attribution and actualselectedreading depth are in `references/source-review.json` and `cases.json`. Original2001BFLfulltext/Nabh1998report are not claimed read; no originalauthor code copied.

A separately authorized native component study actually passed58/58checks once, compilerincluded4.183360s. It qualified finiteone-step scalar/native outputs, movingwall sign, q/algebra/openmoments andledgers. Its reset-one-step timing projects workload only; it is not mainruntime or a scientific benchmark pass. Exactoriginalinput/source/protocol/reviews, two unexecutedpreflightrevisions andactualreceipt/results are retained under`qualification/`. Those58checks are not added to this packet's22pytest or37casegates.

## Saved science and failure retention / 保存・失敗保持

Each run saves its full compactfluid populations, density, velocity, geometry/linkfractions, allnative-step mass/momentum/force ledgers, exactintegerstep/time table anddeclaredcheckpointstates inNPZ. LedgerCSV andsummaryCSV have headers andfinite numericrows. `*-active.npz`, `active-stage.json` andstreamedledgerCSV persist through each1000step chunk; exceptions save availablecandidatearrays/traceback andpartialcaseJSON. Result success requires everyfixedcase/run/gate; abnormal termination remains failure.

The pre-run snapshot is never silently rewritten after output. Any failure/revision must preserve fullsource/contract/input/criteria/logs/results and require separate review before another run. Runtime estimates do not loosen120s orscientificcriteria. PNG/SVG/PDF main/previewfigures come fromtheactualsavedfields aftersuccess. Nativecompiler files/temporaryenvironment are excluded from output.


## R2 explicit resource lifecycle / 明示的終了処理

R1cavityexecuted22numericaltestbodies,allpassed;sessionteardownResourceWarningfailedQA,main0. R1ofthisgroupisthatfailedcavityattempt. Input,acceptance,kernel,geometry,scalarreference andall22scientifictestbodies are unchanged. Native.close,sessionfixturefinally andmainfinally now explicitly remove their compiler temporarydirectory; no warning is suppressed. Originalsource/contracts/logs/JUnit are retained. Main run has not been attempted at this pre-run revision.
