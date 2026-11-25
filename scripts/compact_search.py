"""Small browser indexes; keep the existing detailed public corpora and URLs."""
from copy import deepcopy
from collections import Counter
import math
import base64
import hashlib
import json
import re
import unicodedata

GROUPS = ('methods', 'equations', 'figures', 'references', 'code')

ENCODING = 'shared-raw-strings-v1'
PREFIX = '~s:'
MIN_CHARS = 4
MAX_POOL = 50000
MAX_POOL_UNITS = 8200000
MAX_STRING_UNITS = 1000000
MAX_EXPANDED_UNITS = 16400000
MAX_NODES = 1000000
MAX_DEPTH = 64


def encode_row_strings(data):
    if data.get('format') != 'compact-search-v1' or data.get('kind') not in ['atlas', 'site']:
        raise ValueError('Expected a compact atlas/site index')
    if 'row_string_encoding' in data or 'row_strings' in data:
        raise ValueError('Already encoded or reserved header fields')
    field = 'entries' if data['kind'] == 'atlas' else 'documents'
    if not isinstance(data.get(field), list) or len(data[field]) > 2000:
        raise ValueError('Invalid rows')
    counts = Counter()
    nodes, units = 0, 0

    def charge(text):
        nonlocal units
        length = len(text.encode('utf-16-le')) // 2
        units += length
        if units > MAX_EXPANDED_UNITS:
            raise ValueError('Expanded row strings exceed limit')

    def visit(value, depth=0):
        nonlocal nodes
        nodes += 1
        if nodes > MAX_NODES or depth > MAX_DEPTH:
            raise ValueError('Row structure exceeds limit')
        if isinstance(value, str):
            charge(value)
            if len(value) >= MIN_CHARS:
                counts[value] += 1
        elif isinstance(value, list):
            for item in value:
                visit(item, depth + 1)
        elif isinstance(value, dict):
            for key, item in value.items():
                if not isinstance(key, str):
                    raise ValueError('Non-JSON object key')
                charge(key)
                visit(item, depth + 1)
        elif value is not None and not isinstance(value, (bool, int, float)):
            raise ValueError('Non-JSON row value')
        elif isinstance(value, float) and not math.isfinite(value):
            raise ValueError('Nonfinite row value')

    for row in data[field]:
        if not isinstance(row, dict):
            raise ValueError('Rows must be records')
        visit(row)
    details = data.get('details')
    if details is not None and not isinstance(details, dict):
        raise ValueError('Invalid details header')
    keys = details.get('keys') if details is not None else None
    if keys is not None:
        if not isinstance(keys, list) or any(not isinstance(key, str) for key in keys):
            raise ValueError('Invalid details keys')
        visit(keys)
    pool = sorted(text for text, count in counts.items() if count > 1)
    if not pool:
        return data  # Preserve the old format if pooling cannot help.
    if len(pool) > MAX_POOL or sum(len(v.encode('utf-16-le')) // 2 for v in pool) > MAX_POOL_UNITS:
        raise ValueError('String pool exceeds limit')
    if any(len(v.encode('utf-16-le')) // 2 > MAX_STRING_UNITS for v in pool):
        raise ValueError('String pool entry exceeds limit')

    def base36(number):
        if number == 0:
            return '0'
        digits = ''
        while number:
            number, remainder = divmod(number, 36)
            digits = '0123456789abcdefghijklmnopqrstuvwxyz'[remainder] + digits
        return digits

    positions = {text: PREFIX + base36(i) for i, text in enumerate(pool)}

    def encode(value):
        if isinstance(value, str):
            if value in positions:
                return positions[value]
            return PREFIX + '~' + value[len(PREFIX):] if value.startswith(PREFIX) else value
        if isinstance(value, list):
            return [encode(item) for item in value]
        if isinstance(value, dict):
            return {key: encode(item) for key, item in value.items()}
        return value

    result = {**data, field: [encode(row) for row in data[field]],
              'row_string_encoding': ENCODING, 'row_strings': pool}
    if keys is not None:
        result['details'] = {**details, 'keys': encode(keys)}
    return result


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, separators=(',', ':'))+'\n').encode()


def vocabulary(text):
    text = re.sub('[‐‑‒–—−-]', ' ', unicodedata.normalize('NFKC', text).lower())
    return list(dict.fromkeys(text.split()))


def pack_vocabulary(words):
    """Lossless Unicode-code-point prefix lengths and suffixes, in ID order."""
    packed, previous = [], ''
    for word in words:
        common = 0
        while common < min(len(previous), len(word)) and previous[common] == word[common]:
            common += 1
        packed.extend((common, word[common:]))
        previous = word
    return packed


VOCABULARY_ALPHABET_ENCODING = 'unicode-prefix-alphabet-v1'
MAX_VOCABULARY_ALPHABET = 8192
MAX_VOCABULARY_TERMS = 500000
MAX_VOCABULARY_UNITS = 8200000
_ALPHABET_ASCII = ''.join(chr(i) for i in range(32, 127) if i not in (34, 92))


def encode_vocabulary_alphabet(data):
    """Lossless scalar substitution AFTER fixed term IDs/code-point prefixes.

    Frequency ties use original scalar order. An oversized or empty alphabet
    retains the existing wire format; no public term/expansion cap is increased.
    """
    if data.get('format') != 'compact-search-v1' or data.get('kind') not in ['atlas', 'site']:
        raise ValueError('Expected compact atlas/site vocabulary')
    if 'vocabulary_alphabet' in data or data.get('vocabulary_encoding') != 'unicode-prefix-flat-v1':
        raise ValueError('Reserved or unsupported vocabulary header')
    terms = data.get('terms')
    if not isinstance(terms, list) or len(terms) % 2 or len(terms) > 2 * MAX_VOCABULARY_TERMS:
        raise ValueError('Invalid search vocabulary')
    counts, previous, units, oversized = Counter(), '', 0, False
    for prefix, suffix in zip(terms[::2], terms[1::2]):
        if type(prefix) is not int or not 0 <= prefix <= len(previous) or not isinstance(suffix, str):
            raise ValueError('Invalid vocabulary prefix/suffix')
        if any(0xD800 <= ord(c) <= 0xDFFF for c in suffix):
            raise ValueError('Non-scalar vocabulary suffix')
        suffix_units = len(suffix.encode('utf-16-le')) // 2
        if suffix_units > MAX_VOCABULARY_UNITS - units:
            raise ValueError('Expanded search vocabulary exceeds limit')
        word = previous[:prefix] + suffix
        units += len(word.encode('utf-16-le')) // 2
        if units > MAX_VOCABULARY_UNITS:
            raise ValueError('Expanded search vocabulary exceeds limit')
        previous = word
        if not oversized:
            for character in suffix:
                counts[character] += 1
                if len(counts) > MAX_VOCABULARY_ALPHABET:
                    counts.clear(); oversized = True; break
    if oversized or not counts:
        return data
    alphabet = sorted(counts, key=lambda c: (-counts[c], ord(c)))
    def symbol(index):
        return _ALPHABET_ASCII[index] if index < len(_ALPHABET_ASCII) else chr(128 + index - len(_ALPHABET_ASCII))
    translation = {ord(character): symbol(i) for i, character in enumerate(alphabet)}
    packed = [value.translate(translation) if isinstance(value, str) else value for value in terms]
    return {**data, 'terms': packed, 'vocabulary_encoding': VOCABULARY_ALPHABET_ENCODING,
            'vocabulary_alphabet': ''.join(alphabet)}


def pack_deltas(deltas):
    """Canonical unsigned LEB128 bytes; base64 keeps the JSON transport simple."""
    raw = bytearray()
    for value in deltas:
        while value >= 128:
            raw.append((value & 127) | 128)
            value >>= 7
        raw.append(value)
    return base64.b64encode(raw).decode('ascii')


def encode_row_pool(data):
    """Lossless code-point prefixes for the existing pool, with unchanged IDs."""
    if 'row_pool_encoding' in data or 'row_pool_prefixes' in data:
        raise ValueError('Reserved row pool header')
    if data.get('row_string_encoding') is None:
        if 'row_strings' in data:
            raise ValueError('Orphan row string pool')
        return data
    if (data.get('format') != 'compact-search-v1' or data.get('kind') not in ['atlas', 'site'] or
            data.get('row_string_encoding') != ENCODING):
        raise ValueError('Expected shared raw row string pool')
    pool = data.get('row_strings')
    if not isinstance(pool, list) or len(pool) > MAX_POOL:
        raise ValueError('Invalid row pool')
    previous, units, seen, prefixes, suffixes = '', 0, set(), [], []
    for text in pool:
        if (not isinstance(text, str) or any(0xD800 <= ord(c) <= 0xDFFF for c in text) or
                text in seen):
            raise ValueError('Invalid row pool string')
        size = len(text.encode('utf-16-le')) // 2
        units += size
        if size > MAX_STRING_UNITS or units > MAX_POOL_UNITS:
            raise ValueError('Row pool exceeds unchanged limits')
        seen.add(text)
        prefix = 0
        while prefix < min(len(previous), len(text)) and previous[prefix] == text[prefix]:
            prefix += 1
        prefixes.append(prefix)
        suffixes.append(text[prefix:])
        previous = text
    return {**data, 'row_strings': suffixes, 'row_pool_encoding': 'unicode-prefix-columns-v1',
            'row_pool_prefixes': pack_deltas(prefixes)}


def encode_vocabulary_columns(data):
    """Store the same alphabet suffixes with a separate canonical prefix stream."""
    if 'vocabulary_prefixes' in data:
        raise ValueError('Reserved vocabulary prefixes')
    if data.get('vocabulary_encoding') != VOCABULARY_ALPHABET_ENCODING:
        return data
    packed = data.get('terms')
    if not isinstance(packed, list) or len(packed) % 2 or len(packed) > 2 * MAX_VOCABULARY_TERMS:
        raise ValueError('Invalid vocabulary columns')
    previous, units = 0, 0
    for prefix, suffix in zip(packed[::2], packed[1::2]):
        if (type(prefix) is not int or not 0 <= prefix <= previous or
                not isinstance(suffix, str) or any(0xD800 <= ord(c) <= 0xDFFF for c in suffix)):
            raise ValueError('Invalid vocabulary columns')
        previous = prefix + len(suffix)
        units += previous
        if units > MAX_VOCABULARY_UNITS:
            raise ValueError('Expanded vocabulary exceeds limit')
    return {**data, 'terms': packed[1::2],
            'vocabulary_encoding': 'unicode-prefix-alphabet-columns-v1',
            'vocabulary_prefixes': pack_deltas(packed[::2])}


def encode_row_shapes(data):
    """Lossless in-place-order dictionary shapes; arrays have a distinct -1 tag."""
    if data.get('format') != 'compact-search-v1' or data.get('kind') not in ['atlas', 'site']:
        raise ValueError('Expected compact rows')
    if 'row_structure_encoding' in data or 'row_shapes' in data:
        raise ValueError('Reserved row shapes')
    field = 'entries' if data['kind'] == 'atlas' else 'documents'
    rows = data.get(field)
    if not isinstance(rows, list) or len(rows) > 2000 or any(not isinstance(r, dict) for r in rows):
        raise ValueError('Invalid rows')
    shapes, identifiers = [], {}
    nodes, units, schema_units, schema_keys = 0, 0, 0, 0
    def charge(text):
        nonlocal units
        if not isinstance(text, str) or any(0xD800 <= ord(c) <= 0xDFFF for c in text):
            raise ValueError('Invalid row string')
        units += len(text.encode('utf-16-le')) // 2
        if units > MAX_EXPANDED_UNITS:
            raise ValueError('Expanded row strings exceed limit')
    def visit(value, depth=0):
        nonlocal nodes, schema_units, schema_keys
        nodes += 1
        if nodes > MAX_NODES or depth > MAX_DEPTH:
            raise ValueError('Row structure exceeds limit')
        if isinstance(value, dict):
            keys = tuple(value)
            for key in keys: charge(key)
            if keys not in identifiers:
                schema_keys += len(keys)
                schema_units += sum(len(k.encode('utf-16-le')) // 2 for k in keys)
                if len(shapes) >= MAX_POOL or schema_keys > MAX_NODES or schema_units > MAX_POOL_UNITS:
                    raise ValueError('Row shapes exceed limit')
                identifiers[keys] = len(shapes)
                shapes.append(list(keys))
            return [identifiers[keys]] + [visit(child, depth + 1) for child in value.values()]
        if isinstance(value, list):
            return [-1] + [visit(child, depth + 1) for child in value]
        if isinstance(value, str): charge(value)
        elif value is not None and not isinstance(value, (bool, int, float)):
            raise ValueError('Non-JSON row value')
        elif isinstance(value, float) and not math.isfinite(value):
            raise ValueError('Nonfinite row value')
        return value
    packed = [visit(row) for row in rows]
    return {**data, field: packed, 'row_structure_encoding': 'key-shapes-v1', 'row_shapes': shapes}


ROW_LITERAL_ENCODING = 'scalar-bijection-v1'
MAX_ROW_LITERAL_ALPHABET = 8192


def encode_row_literals(data):
    """Optional scalar bijection of four literal roots; old valid inputs can fall back."""
    if 'row_literal_encoding' in data or 'row_literal_alphabet' in data:
        raise ValueError('Reserved row literal header')
    if data.get('format') != 'compact-search-v1' or data.get('kind') not in ('atlas', 'site'):
        raise ValueError('Expected compact atlas/site rows')
    if data.get('row_string_encoding') is None or data.get('row_structure_encoding') is None:
        return data
    if data['row_string_encoding'] != ENCODING or data['row_structure_encoding'] != 'key-shapes-v1':
        raise ValueError('Unknown row literal source stages')
    field = 'entries' if data['kind'] == 'atlas' else 'documents'
    details = data.get('details')
    if not isinstance(details, dict) or 'keys' not in details:
        return data
    roots = ((field, data.get(field)), ('row_strings', data.get('row_strings')),
             ('row_shapes', data.get('row_shapes')), ('details.keys', details['keys']))
    if any(not isinstance(value, list) for _, value in roots):
        raise ValueError('Invalid row literal roots')
    if len(data[field]) > 2000 or len(data['row_strings']) > MAX_POOL or len(data['row_shapes']) > MAX_POOL:
        raise ValueError('Existing row count limit exceeded')
    counts, nodes, total = Counter(), 0, 0
    root_units = Counter()

    class UnsupportedSubset(Exception):
        pass

    def scan(value, depth, root):
        nonlocal nodes, total
        nodes += 1
        if nodes > MAX_NODES or depth > MAX_DEPTH:
            raise UnsupportedSubset()
        if depth == 1 and root == field and not isinstance(value, list):
            raise ValueError('Expected shaped outer row')
        if root in ('row_strings', 'details.keys') and depth == 1 and not isinstance(value, str):
            raise ValueError('Expected row literal string')
        if root == 'row_shapes' and ((depth == 1 and not isinstance(value, list)) or
                                     (depth >= 2 and not isinstance(value, str))):
            raise ValueError('Expected row shape key strings')
        if isinstance(value, str):
            if any(0xD800 <= ord(c) <= 0xDFFF for c in value):
                raise ValueError('Non-scalar row literal')
            size = len(value.encode('utf-16-le')) // 2
            total += size
            root_units[root] += size
            if (total > MAX_EXPANDED_UNITS or
                    (root in ('row_strings', 'row_shapes') and root_units[root] > MAX_POOL_UNITS) or
                    (root == 'row_strings' and size > MAX_STRING_UNITS)):
                raise UnsupportedSubset()
            for c in value:
                counts[c] += 1
                if len(counts) > MAX_ROW_LITERAL_ALPHABET:
                    raise UnsupportedSubset()
        elif isinstance(value, list):
            if len(value) > MAX_NODES - nodes:
                raise UnsupportedSubset()
            for child in value:
                scan(child, depth + 1, root)
        elif value is not None and not isinstance(value, (bool, int, float)):
            raise ValueError('Non-JSON shaped literal')
        elif isinstance(value, float) and not math.isfinite(value):
            raise ValueError('Nonfinite shaped literal')

    try:
        for root, value in roots:
            scan(value, 0, root)
    except UnsupportedSubset:
        return data  # No partial mapping: retain the exact original old wire.
    if not counts:
        return data
    alphabet = sorted(counts, key=lambda c: (-counts[c], ord(c)))
    translation = {ord(c): (_ALPHABET_ASCII[i] if i < len(_ALPHABET_ASCII)
                            else chr(128 + i - len(_ALPHABET_ASCII))) for i, c in enumerate(alphabet)}

    def mapped(value):
        if isinstance(value, str):
            return value.translate(translation)
        if isinstance(value, list):
            return [mapped(child) for child in value]
        return value

    out = {**data, field: mapped(data[field]), 'row_strings': mapped(data['row_strings']),
           'row_shapes': mapped(data['row_shapes']),
           'details': {**details, 'keys': mapped(details['keys'])}}
    return {**out, 'row_literal_encoding': ROW_LITERAL_ENCODING,
            'row_literal_alphabet': ''.join(alphabet)}


def pack_term_memberships(rows, term_count):
    """Transpose sorted term IDs, sharing identical posting lists losslessly.

    A channel is one row's text (or one language in a bilingual row). Class
    IDs are unsigned varints, NOT deltas; each class contains delta channel IDs.
    The public vocabulary and each channel's ascending term order are unchanged.
    """
    if type(term_count) is not int or not 0 <= term_count <= 500000 or len(rows) > 2000:
        raise ValueError('Invalid term vocabulary or rows')
    members = [[] for _ in range(term_count)]
    projected, channels, expanded = [], 0, 0
    for row in rows:
        values = row['search_terms']
        mapping = isinstance(values, dict)
        refs = {}
        for language, indices in (values.items() if mapping else [(None, values)]):
            if channels >= 8000 or not isinstance(indices, list):
                raise ValueError('Invalid term channels')
            previous = -1
            for index in indices:
                if type(index) is not int or not previous < index < term_count:
                    raise ValueError('Term IDs must be unique, sorted and in range')
                members[index].append(channels)
                previous = index
            expanded += len(indices)
            if expanded > 2000000:
                raise ValueError('Expanded term memberships exceed limit')
            refs[language] = channels
            channels += 1
        projected.append({**row, 'search_terms': refs if mapping else refs[None]})
    counts = Counter(tuple(posting) for posting in members)
    classes = sorted(counts, key=lambda posting: (-counts[posting], posting))
    positions = {posting: index for index, posting in enumerate(classes)}
    packed = [pack_deltas([channel - (posting[i-1] if i else 0)
                          for i, channel in enumerate(posting)]) for posting in classes]
    return projected, {
        'term_encoding': 'inverted-membership-varint-base64-v1',
        'term_channel_count': channels,
        'term_membership_ids': pack_deltas([positions[tuple(posting)] for posting in members]),
        'term_membership_classes': packed,
    }


def write_compact(root, source, kind):
    """Project source records without executing or changing any scientific asset."""
    directory = root/'search/details'
    directory.mkdir(parents=True, exist_ok=True)
    references = set()

    def detail(value):
        raw = encoded(value)
        key = hashlib.sha256(raw).hexdigest()
        path = directory/(key+'.json')
        if path.exists():
            assert path.read_bytes() == raw, 'Changed content-addressed search detail: '+key
        else:
            path.write_bytes(raw)
        references.add(key)
        return key

    def project(value):
        if isinstance(value, list):
            return [project(child) for child in value]
        if not isinstance(value, dict):
            return value
        if isinstance(value.get('groups'), dict) and set(value['groups']) == set(GROUPS) and any(value['groups'].values()):
            return {
                'kind': value['kind'], 'id': value['id'],
                'counts': {key: len(value['groups'][key]) for key in GROUPS},
                'groups': {key: [{k: v for k, v in value['groups'][key][0].items()
                                 if k in {'id', 'name', 'url', 'availability'}}]
                           if len(value['groups'][key]) == 1 else [] for key in GROUPS},
                'details_ref': detail({'search_navigation': value}),
            }
        return {key: project(child) for key, child in value.items()}

    field = 'entries' if kind == 'atlas' else 'documents'
    rows, words = [], {}

    def terms(text):
        indices = []
        for word in vocabulary(text):
            if word not in words:
                words[word] = len(words)
            indices.append(words[word])
        return indices

    for original in source[field]:
        row = project(deepcopy(original))
        if isinstance(row.get('method'), dict):
            for unused in ['run_commands', 'code_mapping_scope', 'reading_label']:
                row['method'].pop(unused, None)
        if isinstance(row.get('execution'), dict):
            row['execution'] = {key: value for key, value in row['execution'].items()
                                if key in {'id', 'title', 'focus_keywords', 'snippet'}}
        text = original.get('text', '')
        if isinstance(text, dict):
            row['search_terms'] = {language: terms(value) for language, value in text.items()}
            row['text'] = {language: value[:500] for language, value in text.items()}
            long = any(len(value) > 500 for value in text.values())
        else:
            row['search_terms'] = terms(text)
            row['text'] = text[:500]
            long = len(text) > 500
        if long:
            row['text_ref'] = detail({'text': text})
        rows.append(row)
    # Nearby terms share UTF-8 prefixes; ascending per-record IDs have small
    # deltas. This is a lossless set of normalized whitespace tokens, including
    # Japanese substrings, punctuation and scientific symbols.
    ordered = sorted(words)
    positions = {word: index for index, word in enumerate(ordered)}
    remap = {old: positions[word] for word, old in words.items()}

    for row in rows:
        values = row['search_terms']
        def ordered_ids(indices):
            return sorted(remap[index] for index in indices)
        row['search_terms'] = ({language: ordered_ids(indices) for language, indices in values.items()}
                               if isinstance(values, dict) else ordered_ids(values))
    rows, membership_header = pack_term_memberships(rows, len(ordered))
    source_path = 'numerical-methods-atlas/home-search-index.json' if kind == 'atlas' else 'search/index.json'
    payload = {
        'format': 'compact-search-v1', 'kind': kind, field: rows,
        'terms': pack_vocabulary(ordered),
        'vocabulary_encoding': 'unicode-prefix-flat-v1',
        **membership_header,
        'source_index': {'url': '/'+source_path,
                         'sha256': hashlib.sha256((root/source_path).read_bytes()).hexdigest()},
        'details': {'directory': '/search/details/', 'keys': sorted(references)},
        'scope': 'Same public search terms; original text and explicit navigation are loaded from fixed public files as needed. Search queries are never transmitted.',
    }
    path = root/'search'/('atlas-query-index.json' if kind == 'atlas' else 'query-index.json')
    path.write_bytes(encoded(encode_row_literals(encode_row_shapes(encode_row_pool(encode_vocabulary_columns(encode_vocabulary_alphabet(encode_row_strings(payload))))))))
    return path
