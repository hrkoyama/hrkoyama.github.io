# Steady multistage residual iteration

Run `python run.py --input inputs.json --output fresh-results`, then `python plot.py --results fresh-results/result.json --output fresh-results`. Plot input may also be the result directory. Scientific dependencies are the three exact requirements pins; rendering additionally uses Matplotlib 3.9.4. The fixed protocol is dimensionless. Main and pytest together share 120 seconds, including all numerical reference qualification; plotting is separate. No automatic retries or post-result threshold changes.

Inputs, acceptance, algorithm and reference scope are specified in `inputs.json`, `acceptance.json`, `cases.json`, `source-reading.json` and `DESIGN.md`. A passing public result requires the exact frozen input SHA and nonempty records, metrics and checks for every case. CSV rows are finite; unavailable state error for inconsistent pendulum controls is an empty cell in the explicitly labelled column, not NaN.

Raw paths are saved before later reference/error diagnostics. Ordinary exceptions retain the owned active candidate and completed path; a hard process kill cannot recover unwritten memory. No projection, clipping, floor, implicit fallback or altered time window is used. Pseudo-time in the steady example is not physical-time accuracy.

Stored official IDA values, where used, are approximate printed values from SUNDIALS v7.1.1; their rounding intervals do not bound true-solution error. No IDA program is compiled or executed here. Position-constrained pendulum equations are index three; the explicit underlying ODE and disclosed critical constraint-error extension are not general high-index solvers.
