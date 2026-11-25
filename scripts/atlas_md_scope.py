"""Chapter-local He evidence and the separate fixed two-state MD example."""
from copy import deepcopy
MD_METHODS = ('born-oppenheimer-md', 'car-parrinello-md')
MD_CASE = 'two-state-bo-cp-ou'
MD_GROUP = 'quantum-small'
MD_EDITION = '2026-11-25'
ORIGIN = 'https://hrkoyama.github.io'


def chapter_md_scope(data, methods, packet):
    """Pure validation after the caller's strict immutable canonical loader."""
    assert data['reading_only_methods'] == list(MD_METHODS)
    assert data['reading_only_methods_scope'] == 'chapter-local'
    assert data['scoped_md_examples'] == [MD_CASE]
    assert data['example_id'] in ('periodic-he-dft', 'periodic-he-forces')
    assert not set(MD_METHODS).intersection(data['methods'])
    assert packet['group'] == MD_GROUP and packet['edition'] == MD_EDITION
    manifest, verification = packet['manifest'], packet['verification']
    assert manifest['group'] == verification['group'] == MD_GROUP
    assert manifest['version'] == verification['edition'] == MD_EDITION
    assert verification['passed'] is True and verification['all_cases_rerun'] is True
    assert verification['tests'] == verification['passed_tests'] == 18
    assert all(verification[key] == 0 for key in ['returncode', 'failures', 'errors', 'skipped'])
    selected = [case for case in packet['metadata'] if case['id'] == MD_CASE]
    measured = [case for case in packet['results']['cases'] if case['id'] == MD_CASE]
    assert len(selected) == len(measured) == 1 and measured[0]['passed'] is True
    case = selected[0]
    assert all(ident in case['method_ids'] for ident in MD_METHODS)
    assert 'coupled_md.py' in case['code_files']
    pointer = {'group': MD_GROUP, 'edition': MD_EDITION, 'case_ids': [MD_CASE]}
    for ident in MD_METHODS:
        method = methods[ident]
        assert method['status'] == 'educational-example' and method['depth_release'] == pointer
        assert not any(method.get(key) for key in ['periodic_examples', 'periodic_release', 'force_examples', 'force_release'])
        assert any(profile['release'] == pointer and profile['scope'] and profile['limits']
                   for profile in method['supplemental_scope_profiles'])
    base = '/code/validated-examples/' + MD_EDITION + '/' + MD_GROUP + '/'
    assert packet['base'] == base
    manifest_path = base.lstrip('/') + 'source-manifest.json'
    assert verification['source_manifest_sha256'] == packet['source_sha256'][manifest_path]
    return {'id': MD_CASE, 'scope': 'two-state-educational-model',
            'group': MD_GROUP, 'edition': MD_EDITION,
            'entry': ORIGIN + '/numerical-methods-atlas/validation/' + MD_CASE + '/',
            'source_manifest': ORIGIN + base + 'source-manifest.json',
            'source_manifest_sha256': verification['source_manifest_sha256'],
            'verification': ORIGIN + base + 'verification.json',
            'code': ORIGIN + base + 'coupled_md.py',
            'title': deepcopy(case['title']), 'assumptions': deepcopy(case['assumptions']),
            'limits': deepcopy(case['limits'])}
