#!/usr/bin/env python3
"""Build the verified lightweight-release registry and bind its no-checkout workflow."""
import hashlib
import json
from pathlib import Path
import re
from atlas_depth_release import GROUPS, load_depth_group, read_json
from depth_verifier_assets import render_depth_verifier

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = 'numerical-methods-atlas/validation/releases.json'
WORKFLOW_PATH = '.github/workflows/atlas-depth-linux.yml'
VERIFIER_PATH = 'scripts/verify-depth-public.py'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_registry(root):
    root = Path(root)
    config = read_json(root / 'catalog/atlas-depth-expansion.json')
    assert [g['id'] for g in config['groups']] == list(GROUPS), 'Review every group in its canonical order'
    editions = {group['id']: group.get('edition', config['edition']) for group in config['groups']}
    records = []
    for group in GROUPS:
        data = load_depth_group(root, group, editions[group])
        directory = data['directory']
        receipt = data['verification']
        records.append({'group': group, 'edition': data['edition'],
            'base': 'https://hrkoyama.github.io' + data['base'],
            'archive': receipt['archive']['file'],
            'archive_sha256': receipt['archive']['sha256'],
            'manifest_sha256': digest(directory / 'source-manifest.json'),
            'verification_sha256': digest(directory / 'verification.json'),
            'requirements_sha256': digest(directory / 'requirements.txt'),
            'case_ids': sorted(case['id'] for case in data['metadata']),
            'tests': receipt['tests']})
    ids = [ident for release in records for ident in release['case_ids']]
    assert len(ids) == len(set(ids)) > 0, 'Review nonempty, unique case inventory explicitly'
    return {'schema_version': 1, 'edition': config['edition'], 'case_count': len(ids), 'releases': records}


def render_registry(registry):
    return (json.dumps(registry, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode('utf-8')


def bind_workflow(root, payload):
    """Bind existing registry bytes and the rendered verifier without rebuilding ZIP metadata."""
    root = Path(root)
    workflow = root / WORKFLOW_PATH
    text = workflow.read_text()
    pins = {'ATLAS_DEPTH_BOOTSTRAP_SHA256': digest(root / VERIFIER_PATH),
            'ATLAS_DEPTH_REGISTRY_SHA256': hashlib.sha256(payload).hexdigest()}
    for key, expected in pins.items():
        text, count = re.subn(r"(" + re.escape(key) + r": ')[0-9a-f]{64}(')",
                              lambda match: match[1] + expected + match[2], text)
        assert count == 1, 'Expected exactly one workflow pin: ' + key
    workflow.write_text(text)
    return pins


def build():
    render_depth_verifier(ROOT)
    payload = render_registry(build_registry(ROOT))
    bind_workflow(ROOT, payload)
    target = ROOT / REGISTRY_PATH
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(payload)
    print('Built',len(json.loads(payload)['releases']),'reviewed public releases with',json.loads(payload)['case_count'],'cases; bound two SHA-256 workflow pins.')


if __name__ == '__main__':
    build()
