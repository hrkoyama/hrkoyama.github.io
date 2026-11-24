# Separate independent-reference qualification

The public primary runner uses the bundled cache and never regenerates it. The reference qualifier has no imports of primary operators, Newton, Krylov, time-adjoint or distributed-VJP modules.

For a separately authorized reference run with the pinned dependencies:

```sh
python -B -W error qualify_references.py --source . --output reference-output
```

Use a fresh output directory and enforce the reviewed30s external deadline around the whole reference process. The private qualification wrapper additionally checks pins/source hashes and retains its source snapshot, logs, raw completed oracle output, partial checkpoint and receipt. The public command does not itself recreate that private process-group wrapper or imply an uncapped runtime guarantee.

Only a qualification.json with exactly67 native true decisions, the current input/acceptance/source digests and both cache digests may be installed. Keep the old cache, raw output and qualification receipt; do not overwrite historical evidence. An exception, unmet check or deadline is a failed attempt. A new source/input revision requires a separate pre-run review; no hidden rerun or threshold relaxation.

The two caches hold high-precision scalar values as decimal strings. Decimal50/80 agreement is qualified finite arithmetic, not interval enclosure. Modal recurrence is checked against separate finite geometric formulas. Discrete shooting uses the original finite-difference recurrence and is checked against separately implemented Decimal Thomas-Newton, plus the exact n1 discrete fold. It is not a continuum-fold reference. The assembled banded solver is qualified on fixed symmetric and nonsymmetric dyadic systems against independent Decimal elimination.
