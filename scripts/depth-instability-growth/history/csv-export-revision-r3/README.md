# Preserved successful revision3 before additive CSV export

Revision3 passed22 pytest checks,10 nonlinear runs and74 case decisions, and its original2026-11-23 immutable package remains untouched. A later full public-verifier fixture found that the runner generated NPZ and JSON but no CSV. This is an output-contract omission, not a numerical failure. The archived contract SHA is1420a6a48028cfb3fb64e8f7d70b7a324675f44efe647dd56b4371c359f77f49; run.py.txt is the exact old runner.

Root authorized an additive per-case five-run scalar CSV summary in run.py only, unchanged equations/inputs/acceptance/22tests and74decisions, followed by an honest revision4 contract and packaging as new2026-11-23-r2. All reference/solver code and old immutable files remain unchanged. Static review checks that only a standard-library csv import and serialization block were added. The packager is the only newly executed empirical path; NPZ arrays and decisions are compared with the original package afterward.
