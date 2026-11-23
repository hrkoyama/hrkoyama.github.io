# fmm3d

Fixed lightweight original scientific source, currently pre-run/unexecuted.

```sh
python -W error -m pytest -q -p no:cacheprovider
python -W error run.py --input inputs.json --output fresh-results
python plot.py --results fresh-results/result.json --output fresh-results
```

Three exact direct dependency pins; Matplotlib is plotting-only. Pytest plus all fixed inputs share one120second deadline. Runner requires unchanged frozen input/source and fresh output. Partial case/checkpoints and available failed candidates are retained. No tolerance repair or hidden state floor. Every successful case writes nonempty finite CSV and the strict public result envelope. NPZs retain full actual arrays. Plotting reads saved arrays only. Source read depth and original-paper access limits are explicit under references/. No external numerical package is required.

- fmm3d-inverse-r: Isolated-Gm/r,G1,64equal masses,p3/5/7. Main levels forced; adaptive case alone usescapacity8/maxdepth3. Small-N uncompressed teaching example; reportp^6M2L cost. No SVD/spherical-harmonic/scaling or exact momentum-conservation claim.

First frozen execution passed19/19 tests and48/48 gates across8 FMM evaluations plus independent direct qualifications,within13.421seconds combined. Actual public result/finiteCSV checker passed. No numerical failure/revision or criterion change. Actual saved fields rendered separately.
