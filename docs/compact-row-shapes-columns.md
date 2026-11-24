# Lossless row shapes and vocabulary prefix columns

The compact browser index uses two additional optional storage codecs. Detailed public JSON, Markdown, scientific inputs, results, citations and content-addressed detail files retain their content. Decoding restores the same complete record/header API, row order, object key order, term IDs and query/rank/URL/section results.

`row_structure_encoding: "key-shapes-v1"` declares `row_shapes`, a deduplicated list of ordered object-key arrays. An encoded object is `[shapeID, ...values]`; an encoded original array is `[-1, ...items]`. Every composite value is tagged, so original arrays beginning with integers remain unambiguous. Values retain the existing row-string codec and its one-pass literal escape. Restoration precedes row-string restoration, and storage headers are consumed internally. Object construction preserves own `__proto__` data keys.

The original row, node, depth, expanded UTF-16 and pool limits remain in force. Shape headers also use the existing pool-count/pool-unit/node limits. Decoding rejects duplicate keys/layouts, unused layouts, unknown/orphan headers, wrong tags/arity, sparse or nonplain arrays, non-scalar strings, nonfinite values and excessive expansion before building the corresponding record. The format contains neither references between shape nodes nor recursive token expansion.

`vocabulary_encoding: "unicode-prefix-alphabet-columns-v1"` keeps alphabet-coded suffixes in `terms` and places the original code-point prefix lengths in `vocabulary_prefixes`. This string contains canonical unsigned LEB128 bytes in canonical base64, with at most four bytes per prefix. The existing 500000-term and 8200000 restored UTF-16-unit limits remain unchanged. Prefix counts must match suffix counts; truncated, overlong, overflowing and noncanonical streams fail. Restoring the old interleaved representation feeds the same bounded vocabulary/alphabet decoder.

The updated loader accepts every earlier compact format and already-unpacked data. An older loader does not understand these new optional headers; the existing asset hashes bind the matching loader and wire files. The codecs add no network request, runtime dependency or external decompressor.

Qualification compares full restored records and header key order on four current/frozen corpora, all 120 paired search consumers and malformed inputs. Both original decoded/gzip-level9 budgets apply. CDN encoded bytes remain a separately observed measurement with the server's compression settings.
