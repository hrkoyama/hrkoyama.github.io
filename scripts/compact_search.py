"""Small browser indexes; keep the existing detailed public corpora and URLs."""
from copy import deepcopy
import hashlib
import json
import re
import unicodedata

GROUPS = ('methods', 'equations', 'figures', 'references', 'code')


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, separators=(',', ':'))+'\n').encode()


def vocabulary(text):
    text = re.sub('[‐‑‒–—−-]', ' ', unicodedata.normalize('NFKC', text).lower())
    return list(dict.fromkeys(text.split()))


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
        return result

    for row in rows:
        values = row['search_terms']
        row['search_terms'] = ({language: deltas(indices) for language, indices in values.items()}
                               if isinstance(values, dict) else deltas(values))
    source_path = 'numerical-methods-atlas/home-search-index.json' if kind == 'atlas' else 'search/index.json'
    payload = {
        'format': 'compact-search-v1', 'kind': kind, field: rows, 'terms': ordered,
        'term_encoding': 'sorted-delta',
        'source_index': {'url': '/'+source_path,
                         'sha256': hashlib.sha256((root/source_path).read_bytes()).hexdigest()},
        'details': {'directory': '/search/details/', 'keys': sorted(references)},
        'scope': 'Same public search terms; original text and explicit navigation are loaded from fixed public files as needed. Search queries are never transmitted.',
    }
    path = root/'search'/('atlas-query-index.json' if kind == 'atlas' else 'query-index.json')
    path.write_bytes(encoded(payload))
    return path
