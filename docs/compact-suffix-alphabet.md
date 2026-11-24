# Lossless compact vocabulary alphabet

The browser index can store front-coded vocabulary suffixes with
`vocabulary_encoding: "unicode-prefix-alphabet-v1"`. This changes only the
storage representation. Original word IDs, order, Unicode code-point prefix
lengths, normalized search terms, text, headings, routes and detail references
are restored before searching. Detailed public JSON and Markdown remain intact.

The `vocabulary_alphabet` header lists original Unicode scalar values in
descending suffix frequency, with ties ordered by their original scalar value.
Its positions map to the 93 printable ASCII characters excluding quotation mark
and backslash, followed by U+0080 upwards. Decoding substitutes one scalar for
one scalar exactly once. Original private-use characters and astral characters
are ordinary data, with no escape or recursive expansion meaning.

The producer retains the existing front-coded format for an empty alphabet or
more than 8192 distinct suffix scalars. The decoder also retains all earlier
compact formats. It consumes the alphabet header internally; the unpacked
record and header API stays unchanged. This is backward format support by the
updated decoder, not a claim that an old decoder understands the new encoding.

The decoder rejects missing or orphan headers, unknown modes, duplicate or
non-scalar alphabet entries, unused or noncanonical mappings and symbols outside
the declared alphabet. Quotation mark, backslash, DEL and C0 control characters are
not valid encoded symbols. Python and JavaScript both interpret prefix lengths
in Unicode code points. Restored characters are charged in UTF-16 units, so an
astral original character counts as two units even when its stored symbol uses
one. The existing 500000-term, 8200000-vocabulary-unit and row, string-pool,
membership, structure and response-size limits remain in force.

The alphabet is a public compression table, not encryption or query rewriting.
No external decompressor, runtime dependency or request is added. Cache identity
and already-unpacked inputs retain their existing behavior.

Validation must compare whole unpacked records and headers against the previous
decoder, including current and frozen older corpora, exact query/rank/URL/section
results, malformed input fixtures and both byte budgets. A successful gzip-size
prototype alone does not establish browser parity or publication readiness.
