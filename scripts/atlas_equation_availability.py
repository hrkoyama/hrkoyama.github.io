"""Verify scoped equation-to-example links without executing scientific code."""
from hashlib import sha256
import json
from pathlib import Path
from urllib.parse import urlsplit

from atlas_goal_availability import load_supplemental_examples


def equation_evidence(root, equations, discovery):
    """Keep model-family labels separate from the particular verified example.

    Biological scope and IDs originate in the survey's implemented-subset data.
    Common examples retain their original registry/receipt; supplements retain
    their own independent-extraction receipts. Neither adds a physical problem.
    """
    root = Path(root)
    survey_path = root / 'numerical-methods-atlas/assets/biological-models.json'
    survey = {item['id']: item for item in json.loads(survey_path.read_text())['models']}
    common = {item['id']: [] for item in equations}
    for example in discovery['examples']:
        for ident in example['equation_ids']:
            assert ident in common, 'Unknown equation in common execution mapping'
            common[ident].append(example)
    identifiers = list(dict.fromkeys(ident for item in equations
                                    for ident in item.get('supplemental_examples', [])))
    supplements = {item['id']: item for item in load_supplemental_examples(root, identifiers)}
    supplemental = {}
    for item in equations:
        selected = item.get('supplemental_examples', [])
        assert len(selected) == len(set(selected)), 'Repeated supplemental binding'
        supplemental[item['id']] = [supplements[ident] for ident in selected]
        if item['group'] != 'biology':
            continue
        source = item['formula_source']
        assert source['path'] == 'numerical-methods-atlas/assets/biological-models.json'
        model = survey[source['model_id']]
        executed = model['status'] == 'scoped-educational-example'
        assert item['status'] == ('local-example' if executed else 'reading'), item['id']
        assert {x['id'] for x in common[item['id']]} == set(model.get('execution_examples', [])), item['id']
        assert selected == model.get('supplemental_examples', []), item['id']
        if executed:
            assert common[item['id']] or supplemental[item['id']], 'Missing verified example'
            assert item['execution_scope'] == model['implementation_scope'], item['id']
            assert all(item['execution_scope'].get(lang) for lang in ['ja', 'en'])
        else:
            assert not common[item['id']] and not supplemental[item['id']]
            assert not item.get('execution_scope'), 'Survey-only scope cannot borrow executions'

    registry_path = root / 'numerical-methods-atlas/code-and-data/examples.json'
    registry = json.loads(registry_path.read_text())
    receipt_url = urlsplit(registry['verification_receipt'])
    assert receipt_url.scheme == 'https' and receipt_url.netloc == 'hrkoyama.github.io'
    assert not receipt_url.query and not receipt_url.fragment
    receipt_path = (root / receipt_url.path.lstrip('/')).resolve()
    assert receipt_path.is_relative_to(root.resolve())
    receipt = json.loads(receipt_path.read_text())
    assert receipt['passed'] is True
    assert receipt['registry_sha256'] == sha256(registry_path.read_bytes()).hexdigest()
    receipts = {item['id']: item for item in receipt['examples']}
    assert all(receipts[item['id']]['passed'] is True for rows in common.values() for item in rows)
    paths = [survey_path, registry_path, receipt_path,
             root / 'catalog/atlas-equations.json',
             root / 'catalog/atlas-execution-discovery.json']
    sources = {path.relative_to(root.resolve()).as_posix(): sha256(path.read_bytes()).hexdigest()
               for path in [p.resolve() for p in paths]}
    for supplement in supplements.values():
        sources.update(supplement['source_sha256'])
    return {'common': common, 'supplemental': supplemental, 'source_sha256': sources,
            'supplemental_case_ids': sorted(supplements)}
