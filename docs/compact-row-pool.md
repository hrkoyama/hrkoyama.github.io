# Lossless row-string pool prefixes

The optional `row_pool_encoding: unicode-prefix-columns-v1` representation
stores each existing `row_strings` entry as a suffix and stores its common
Unicode-scalar prefix length with the preceding reconstructed entry in
`row_pool_prefixes`. Prefixes use canonical unsigned LEB128 and canonical base64.
Pool order, IDs, `~s:` references and literal-token escapes remain unchanged.

The decoder restores the pool before the existing row-shape/string decoders.
The complete unpacked object, property order, text, detail references, query
ranking, URLs and sections remain the same. AI JSON and Markdown are separate
public artifacts and are not changed by this storage encoding.

All existing limits remain in force: 50,000 pool strings, 8,200,000 aggregate
UTF16 units, 1,000,000 UTF16 units per reconstructed string, and the original
expanded-row, node, depth and row-count limits. Check prefixes and cumulative
lengths before reconstructing text. Reject malformed/overlong varints,
noncanonical base64, lone surrogates, duplicate strings, sparse arrays, unknown
modes, orphan headers and mismatched counts. Legacy formats remain readable.

Adoption requires fixed-corpus full object/property-order parity, unchanged
query results, malformed-input controls, and actual Node gzip level 9 savings
under the unchanged published decoded/gzip budgets. Browser asset hashes bind
the corresponding decoder; old decoders are not claimed to read new wires.
