# slab-ewald

Fixed lightweight original scientific source, currently pre-run/unexecuted.

```sh
python -W error -m pytest -q -p no:cacheprovider
python -W error run.py --input inputs.json --output fresh-results
python plot.py --results fresh-results/result.json --output fresh-results
```

Three exact direct dependency pins; Matplotlib is plotting-only. Pytest plus all fixed inputs share one120second deadline. Runner requires unchanged frozen input/source and fresh output. Partial case/checkpoints and available failed candidates are retained. No tolerance repair or hidden state floor. Every successful case writes nonempty finite CSV and the strict public result envelope. NPZs retain full actual arrays. Plotting reads saved arrays only. Source read depth and original-paper access limits are explicit under references/. No external numerical package is required.

- neutral-slab-yb: Coulomb1, lateral1×1.25, extendedLz1.5/3/6,4neutral charges±1,physical-z dipole.34 andalpha3/4. Neutral fixed4charge Cartesian-z slab only. YB is a finite-gap approximation, not exact2P at arbitrary vacuum. Original Yeh full text not inspected.

First frozen execution passed17/17 tests and42/42 gates in1.067seconds combined; actual public result/CSV checker passed. No numerical failure/revision or criterion change. Saved-array PNG/SVG/PDF/preview rendered separately.
