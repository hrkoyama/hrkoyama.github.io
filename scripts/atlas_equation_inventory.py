"""Merge new canonical model entries into the shared imported coverage inventory.

Imported records retain their metadata. Entries introduced by this module are
rebuilt from the equation catalog on each refresh, so they neither duplicate
nor survive removal from that catalog. No scientific computation is performed.
"""
from copy import deepcopy

ORIGIN = 'curated-equation-catalog'


def merge_catalog_equations(items, equations):
    identifiers = [row['id'] for row in equations]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError('Duplicate canonical equation identity')
    result = [deepcopy(row) for row in items if row.get('origin') != ORIGIN]
    existing = [row['id'] for row in result if row['kind'] == 'equation']
    if len(existing) != len(set(existing)):
        raise ValueError('Duplicate imported equation identity')
    for row in equations:
        if row['id'] not in existing:
            result.append({'kind': 'equation', 'id': row['id'],
                           'label': row['name']['en'], 'chapter': row['chapter'],
                           'status': row['status'], 'group': 'Physics & mathematical models',
                           'scope': row.get('coverage_scope', row['note']['en']),
                           'origin': ORIGIN})
    return result
