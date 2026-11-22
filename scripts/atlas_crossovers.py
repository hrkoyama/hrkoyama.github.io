"""Shared, static entrances to the atlas's cross-field connections."""
import hashlib
import json
from html import escape
from pathlib import Path


BASE = '/numerical-methods-atlas/connections/'
ORIGIN = 'https://hrkoyama.github.io'

# Explicit applicability prevents a useful solver/diagnostic in another field
# from being borrowed as evidence for this stage or for a complete coupled run.
SUPPLEMENT_STAGE_CASES = {
    'thermostat': {'langevin-harmonic', 'csvr-kinetic-kernel', 'csvr-langevin-harmonic', 'csvr-langevin-quartic'},
    'reaction-diffusion': {'reaction-diffusion-fourier', 'turing-schnakenberg'},
    'biological-fronts': {'turing-schnakenberg', 'fitzhugh-nagumo'},
}


def load_supplemental_evidence(root, case_ids):
    """Resolve separate, hash-checked component supplements without new executions."""
    if not case_ids:
        return {'cases': {}, 'source_sha256': {}, 'receipts': {}}
    from atlas_depth_release import GROUPS, depth_code_urls, digest, load_depth_group, read_json
    root = Path(root)
    catalog_path = root/'catalog/atlas-depth-expansion.json'
    catalog = read_json(catalog_path)
    by_id = {}
    for group in catalog['groups']:
        assert group['id'] in GROUPS
        directory = root/'code/validated-examples'/catalog['edition']/group['id']
        metadata = read_json(directory/'cases.json')
        metadata = metadata['cases'] if isinstance(metadata, dict) else metadata
        for case in metadata:
            assert case['id'] not in by_id, 'Duplicate supplemental case ID'
            by_id[case['id']] = group['id']
    assert set(case_ids) <= by_id.keys(), 'Unknown supplemental evidence ID'
    groups = {group: load_depth_group(root, group, catalog['edition'])
              for group in sorted({by_id[ident] for ident in case_ids})}
    sources = {'catalog/atlas-depth-expansion.json': digest(catalog_path)}
    receipts, cases = {}, {}
    for group, data in groups.items():
        sources.update(data['source_sha256'])
        receipts[group] = {'url': ORIGIN+data['base']+'verification.json',
                           'sha256': data['source_sha256'][data['base'].lstrip('/')+'verification.json'],
                           'passed_tests': data['verification']['passed_tests'],
                           'all_cases_rerun': data['verification']['all_cases_rerun'],
                           'source_mode': 'independently-extracted-supplement'}
        metadata = {case['id']: case for case in data['metadata']}
        measured = {case['id']: case for case in data['results']['cases']}
        for ident in sorted(set(case_ids) & metadata.keys()):
            case = metadata[ident]
            cases[ident] = {'id': ident, 'group': group, 'edition': catalog['edition'],
                'title': case['title'], 'scope': case['summary'], 'limits': case['limits'],
                'method_ids': case['method_ids'], 'domains': case.get('domains', []),
                'url': ORIGIN+'/numerical-methods-atlas/validation/'+ident+'/',
                'reading': {language: ORIGIN+'/numerical-methods-atlas/'+language+'/read/validation-'+group+'/#'+ident
                            for language in ['ja', 'en']},
                'code_download': ORIGIN+data['base']+data['verification']['archive']['file'],
                'code_urls': depth_code_urls(data, [ident]), 'test_urls': data['test_urls'],
                'input': ORIGIN+data['base']+'inputs.json',
                'results': ORIGIN+data['base']+'results/result.json',
                'source_manifest': ORIGIN+data['base']+'source-manifest.json',
                'verification_receipt': receipts[group],
                'numerical_checks_passed': measured[ident]['passed'],
                'checks': measured[ident]['checks'], 'metrics': measured[ident]['metrics'],
                'source_mode': 'independently-extracted-supplement'}
    return {'cases': cases, 'source_sha256': sources, 'receipts': receipts}


def crossover_assets(root, interactive=False):
    """Return content-versioned assets; homepage cards need only the stylesheet."""
    css = '/styles/atlas-crossovers.css'
    version = hashlib.sha256((root / css.lstrip('/')).read_bytes()).hexdigest()[:12]
    assets = '<link rel="stylesheet" href="' + css + '?v=' + version + '">'
    if interactive:
        script = '/numerical-methods-atlas/crossovers.mjs'
        version = hashlib.sha256((root / script.lstrip('/')).read_bytes()).hexdigest()[:12]
        assets += '<script type="module" src="' + script + '?v=' + version + '"></script>'
    return assets


def crossover_teaser(root, lang):
    """Render three direct, bilingual path entrances without inferring validation."""
    data = json.loads((root / 'catalog/atlas-crossovers.json').read_text())
    ja = lang == 'ja'
    heading = data.get('home', {}).get('title', data['title'])[lang]
    intro = data.get('home', {}).get('description', data['intro'])[lang]
    body = '<aside class="atlas-crossover-teaser"><h2>' + heading + '</h2><p>' + intro + '</p><div class="crossover-teaser-grid">'
    for route in data['routes']:
        url = BASE + '?lang=' + lang + '#' + route['id'] + '-' + lang
        body += '<article><h3><a href="' + escape(url, quote=True) + '">' + escape(route['title'][lang]) + '</a></h3><p>' + escape(route.get('teaser', route['summary'])[lang]) + '</p></article>'
    action = data.get('home', {}).get('action', {'ja': '分野をつなぐ入口へ', 'en': 'Explore the crossovers'})[lang]
    body += '</div><p><a href="' + BASE + '?lang=' + lang + '">' + escape(action) + '</a></p><p class="crossover-teaser-note">' + ('個々の実行例と、分野間を連成した計算の検証を区別して表示します。' if ja else 'Component execution examples and validation of a coupled calculation are shown separately.') + '</p></aside>'
    return body
