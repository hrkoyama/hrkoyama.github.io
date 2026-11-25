The optional row_literal_encoding scalar-bijection-v1 stores a single complete
Unicode-scalar alphabet for strings in packed rows, the row pool, shape keys and
detail-key references. The table is ordered by descending literal frequency,
then original code point. Safe scalar codes use the existing 93 JSON-safe ASCII
characters followed by code points from U+0080. Decoding is one pass.

The decoder restores literals before the existing pool, shape and string stages.
It preserves the complete old decoded API, vocabulary IDs, ranking, routes,
detail files and full AI exports. The two new storage headers are consumed.
Unknown, orphaned and malformed modes are rejected.

Before reconstructing roots or strings, the marked subset checks scalar
bijection/canonical counts, dense arrays, finite values and resource bounds.
Its combined raw traversal is intentionally stricter: one million nodes,
depth 64 and 16.4 million restored UTF-16 units, in addition to existing
pool/schema limits. The writer leaves the exact old unmarked representation
when this optional subset or the 8,192-scalar table is unsuitable. Existing
unmarked formats and their original validation remain supported.

These are storage changes only. The raw and gzip-level-9 browser budgets are
unchanged. Adoption requires the separately retained source-bound whole-corpus
and search-result qualifications; a prototype measurement alone is insufficient.
