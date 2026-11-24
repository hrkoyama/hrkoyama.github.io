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
MIN_CHARS = 32
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


def pack_deltas(deltas):
    """Canonical unsigned LEB128 bytes; base64 keeps the JSON transport simple."""
    raw = bytearray()
    for value in deltas:
        while value >= 128:
            raw.append((value & 127) | 128)
            value >>= 7
        raw.append(value)
    return base64.b64encode(raw).decode('ascii')


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

    def deltas(indices):
        result, previous = [], 0
        for index in sorted(remap[index] for index in indices):
            result.append(index-previous)
            previous = index
        return pack_deltas(result)

    for row in rows:
        values = row['search_terms']
        row['search_terms'] = ({language: deltas(indices) for language, indices in values.items()}
                               if isinstance(values, dict) else deltas(values))
    source_path = 'numerical-methods-atlas/home-search-index.json' if kind == 'atlas' else 'search/index.json'
    payload = {
        'format': 'compact-search-v1', 'kind': kind, field: rows,
        'terms': pack_vocabulary(ordered),
        'vocabulary_encoding': 'unicode-prefix-flat-v1',
        'term_encoding': 'sorted-delta-varint-base64',
        'source_index': {'url': '/'+source_path,
                         'sha256': hashlib.sha256((root/source_path).read_bytes()).hexdigest()},
        'details': {'directory': '/search/details/', 'keys': sorted(references)},
        'scope': 'Same public search terms; original text and explicit navigation are loaded from fixed public files as needed. Search queries are never transmitted.',
    }
    path = root/'search'/('atlas-query-index.json' if kind == 'atlas' else 'query-index.json')
    path.write_bytes(encoded(encode_row_strings(payload)))
    return path
