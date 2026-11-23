"""One current registration contract; never infer new scientific validation."""
from collections import Counter
import json
from pathlib import Path
import re

STATUSES = ('educational-example', 'reading-only', 'planned')
ID = re.compile(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*')
EDITION = re.compile(r'\d{4}-\d{2}-\d{2}(?:-r\d+)?')


def read_json(path):
    def unique(pairs):
        result = {}
        for key,value in pairs:
            if key in result:
                raise ValueError('Duplicate JSON key: '+key)
            result[key] = value
        return result
    return json.loads(path.read_text(), object_pairs_hook=unique)


def catalogs(root):
    """Validate this small JSON Schema contract with the standard library."""
    root = Path(root)
    contract = read_json(root/'catalog/atlas-registration.json')
    schema = read_json(root/'catalog/schemas/atlas-registration.schema.json')
    if set(contract) != set(schema['required']):
        raise ValueError('Invalid atlas registration fields')
    for key,rule in schema['properties'].items():
        value = contract[key]
        if ('const' in rule and (type(value) is not type(rule['const']) or value != rule['const'])) or \
           (rule.get('type') == 'string' and (not isinstance(value,str) or not value.strip())):
            raise ValueError('Invalid atlas registration field: '+key)
    return read_json(root/contract['methods_catalog']), read_json(root/contract['supplements_catalog'])


def identifiers(rows, label):
    if not isinstance(rows,list) or not rows:
        raise ValueError('Missing '+label)
    result = []
    for row in rows:
        ident = row.get('id') if isinstance(row,dict) else None
        if not isinstance(ident,str) or not ID.fullmatch(ident) or ident in result:
            raise ValueError('Invalid or duplicate '+label+' ID: '+repr(ident))
        result.append(ident)
    return result


def registered_groups(root):
    _, supplements = catalogs(root)
    groups = identifiers(supplements['groups'], 'supplement group')
    for row in supplements['groups']:
        edition = row.get('edition', supplements['edition'])
        if not isinstance(edition,str) or not EDITION.fullmatch(edition):
            raise ValueError('Invalid supplement edition: '+row['id'])
    return tuple(groups)


def inventory(root):
    root = Path(root)
    methods, supplements = catalogs(root)
    ids = identifiers(methods['methods'], 'method')
    fields = set(identifiers(methods['groups'], 'method field'))
    for row in methods['methods']:
        if row.get('status') not in STATUSES or row.get('group',{}).get('id') not in fields:
            raise ValueError('Unregistered method status or field: '+row['id'])
        for key in ['name','summary']:
            if not isinstance(row.get(key),dict) or not all(isinstance(row[key].get(lang),str) and row[key][lang].strip() for lang in ['ja','en']):
                raise ValueError('Missing bilingual method '+key+': '+row['id'])
    groups = registered_groups(root)
    cases, by_group = {}, {}
    for group in supplements['groups']:
        edition = group.get('edition', supplements['edition'])
        value = read_json(root/'code/validated-examples'/edition/group['id']/'cases.json')
        rows = value['cases'] if isinstance(value,dict) else value
        names = identifiers(rows, 'supplement case')
        by_group[group['id']] = (edition, {row['id']:row for row in rows})
        for row in rows:
            refs = row.get('method_ids')
            if row['id'] in cases or not isinstance(refs,list) or not refs or len(refs)!=len(set(refs)) or not set(refs)<=set(ids):
                raise ValueError('Duplicate case or unregistered method reference: '+row['id'])
            cases[row['id']] = row
    for row in methods['methods']:
        configs = ([row['depth_release']] if row.get('depth_release') else [])+row.get('depth_additional_releases',[])
        if len({(config['group'],config['edition']) for config in configs})!=len(configs):
            raise ValueError('Duplicate method release: '+row['id'])
        for config in configs:
            group = config.get('group')
            if group not in by_group or row['status']!='educational-example':
                raise ValueError('Unregistered or unavailable method supplement: '+row['id'])
            edition, members = by_group[group]
            selected = config.get('case_ids')
            if config.get('edition')!=edition or not isinstance(selected,list) or not selected or len(selected)!=len(set(selected)) or not set(selected)<=members.keys():
                raise ValueError('Invalid method supplement case or edition: '+row['id'])
            if any(row['id'] not in members[ident]['method_ids'] for ident in selected):
                raise ValueError('Unrelated supplement borrowed by method: '+row['id'])
    if not set(supplements['case_problem_ids']) <= cases.keys():
        raise ValueError('Unregistered supplement problem mapping')
    return {'method_ids': ids, 'method_status_counts': dict(Counter(row['status'] for row in methods['methods'])),
            'supplement_groups': list(groups), 'supplement_case_ids': list(cases)}


def validate_public_methods(root, rows):
    canonical, _ = catalogs(root)
    source = {row['id']:row for row in canonical['methods']}
    if set(identifiers(rows,'public method')) != source.keys():
        raise ValueError('Public method inventory differs from canonical IDs')
    for row in rows:
        if row['status'] != source[row['id']]['status']:
            raise ValueError('Public method status changed without canonical evidence: '+row['id'])
        if row['status']=='educational-example' and (not row.get('code_urls') or not row.get('test_urls')):
            raise ValueError('Educational method lacks published code/test evidence: '+row['id'])


def validate_case_references(root, rows):
    methods, _ = catalogs(root)
    allowed = set(identifiers(methods['methods'], 'method'))
    identifiers(rows, 'supplement case')
    for row in rows:
        refs = row.get('method_ids')
        if not isinstance(refs,list) or not refs or len(refs)!=len(set(refs)) or not set(refs)<=allowed:
            raise ValueError('Unregistered case method reference: '+row['id'])
