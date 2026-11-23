# Full-state MHD transport and late Orszag–Tang

The first primary execution passed47 pytest checks (no skips),12/12 fixed PDE runs and125/125 numerical gates within43.8881156 seconds combined. It used the independently reviewed unchanged contract295cffb4e7d6cf09d7412b3f5405d544c42ca487376b296e848ada55aabdaad8. Logs, JUnit and actual combined receipt are in execution-receipts/attempt-01.

This small educational supplement has three cases, 12 fixed primary runs and 47 focused pytest cases. It reuses the prior public full-eight-state HLLD implementation without changes, with a new no-retry driver. Density, all three momentum components, total energy and all three magnetic components are retained. MC reconstruction can scale face slopes toward the original positive cell value; this is counted. Cell states are never floored or clipped. Invalid HLLD star states use the explicitly counted inherited HLLE fallback.

Run from this directory with the pinned Python environment:

```sh
python -W error -m pytest -q -p no:cacheprovider
python -W error run.py --input inputs.json --output /fresh/output
python plot.py --results /fresh/output/result.json --output /fresh/figures
```

The validation dependencies are pinned in requirements.txt; plotting additionally uses requirements-plotting.txt. Main pytest plus the full 12-run study has a shared 120-second limit, enforced by its execution harness, with an internal 115-second main guard. The measured main subprocess took43.34045 seconds; no optional reference regeneration or plotting is included in that combined main-validation measurement.

The aligned circular Alfvén wave has analytic conserved finite-volume cell means qualified using independent Gauss16 quadrature. It is a one-spatial-dimensional traveling wave, displayed as space and time; it is not a 2D oblique-propagation test. The loop and Orszag–Tang are genuinely two-dimensional spatial calculations using CT-contact corner electric fields and native face magnetic fields. Initial conditions explicitly match the pinned official Athena++ generator: discrete vector-potential curl and arithmetic face-to-cell B, with sampled fluid primitives. They are not exact continuum conserved-cell-average initializations.

Independent references come from unmodified official Athena++ commit1395e2f543f4368d448cb1a2cf92ba1f910e3416, archive SHA8a6cd8658217349fd913c03b549df8b88c2a2fe96cb4ea1b8ba4bf747c6af896, compiled locally with Apple clang++ -O3 and no fast-math/MPI/OpenMP/HDF5. The HLLD/PLM/RK2/native-upwind-CT reference uses loop Ny64/128 and OT128/256, with a finest-grid halved-CFL companion. All numerical comparisons use final conserved fields only; pressure is computed after conservative restriction, not averaged separately. Native Athena face divergence was not exported and is not claimed measured. A common centered Bcc divergence is reported for both engines, separately from primary native-face divergence.

The official unmodified loop has domain widths(2,1,2), vflow3 and therefore v=(2,1,2), an explicit 2.5D variant of the historical vz=0 loop. Gamma is5/3, rho=p=1, Az=.001max(.3-r,0) and T=1. Compressible ideal-MHD OT runs to T=.2; it differs from the original1979 incompressible viscous/resistive model. Density contrast is an observable compression diagnostic, not proof of a continuum shock.

Reference attempt01 completed six PDE runs in53.315s but failed six exact-intermediate-time gates (25/31). Athena writes the first step after each requested intermediate time. The failed result, original R2 source contract and qualifier are retained unchanged in references/history and the private output archive. Independently approved R3 qualification was declared AFTER these six PDE runs and BEFORE saved-field requalification/main. It preserves all five NPZ snapshots bit-for-bit, checks strictly ordered finite times within[0,T] plus exact initial/final times under the unchanged1e-14 tolerance, and records intermediate-time offsets. All physical/spatial/time-error bounds remain unchanged. Requalification passed31/31 without any PDE rerun. The original source-run contract and the later qualification contract are distinct files.

Only selected primary-source sections were inspected; references/source-review.json and per-reference review_level record exact scope. Original Miyoshi–Kusano full text was unavailable, and original OT publisher abstract/bibliography only was inspected. No full-paper claim, paper PDF redistribution, exact postshock solution or universal stability/order/positivity guarantee is made.

Saved result observations: wave transverse relative L2=.00304059, last observed order1.62943 and phase error.00121487rad; loop magnetic relative L1=.253088 with reference increment equal to47.44% of primary error; OT density/pressure relative L1=.0110806/.0182227 with reference increments30.81%/29.83% of primary error. These finite-grid reference sensitivities are material and are not precision error bounds. All12 runs used zero HLLE fallbacks and zero face slope scalings; degenerate zero-normal-field branches in the loop were counted separately. Cell clips/retries remained zero.
