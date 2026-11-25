# Exact checkpoint packaging

The numerical runner writes the full native checkpoint set on every reproduction.
This saved result contains 1344 original files (7671358 original bytes). To keep the
distribution below its archive-entry limit, 19 primary result/measurement/figure
files are stored directly and 1325 raw JSON checkpoints are preserved in the one
`results/native-checkpoints.jsonl` file. No numerical input, criterion, seed or original text was changed.

The bundle is UTF-8 JSON Lines. Its first line is the version-1
`atlas-exact-utf8-checkpoints` header. Each following line is an independent JSON
envelope with `record="file"`, the original `path` relative to `results/`, original
`bytes`, SHA-256 `sha256`, and `text`. The text field is the EXACT original UTF-8
file text, including whitespace and final newlines; checkpoint numbers were never
parsed and reserialized during packaging. JSON envelope escapes such as `\n` must
be decoded once by a JSON reader. Re-encode `text` as UTF-8 to recover the original
bytes, then verify length and SHA-256 before writing a fresh safe relative path.
Do not execute the text. Reject absolute/traversal paths, duplicates and mismatches.

All direct files and every bundled entry were byte-compared against their full
original outputs. The complete original and logically recovered inventory digests
are identical: `98b895717df73b90e50643476e2adb28e68fc36ccd31131186a8de7a6ff9bfd5`.

The ordinary `result.json`, full case result records, `checks.json`, `summary.json`,
`execution-context.json`, measurement CSV, plot manifest and seven PNGs remain
directly accessible. Native eigensolver returns, input matrices, SCF candidates
and trajectory checkpoints remain available losslessly in the bundle. Running
the included scientific code still generates all native files in a fresh output
directory; it does not consume this bundle or omit intermediate returns. The
archive-member limit applies to the distributed ZIP, not to regenerated outputs.
