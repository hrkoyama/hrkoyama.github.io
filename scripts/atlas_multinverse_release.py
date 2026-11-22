"""Resolve the immutable multi-parameter Bratu inverse supplement for method pages."""
import hashlib
import json
from pathlib import Path

ORIGIN = 'https://hrkoyama.github.io'
_VERIFIED = {}


def multinverse_release_record(root, method):
    config = method['multi_inverse_release']
    assert method['id'] == 'optimization' and method['status'] == 'educational-example'
    assert not method['code_modules'] and not method['test_files']
    key = (str(root.resolve()), json.dumps(config, sort_keys=True))
    if key in _VERIFIED:
        return _VERIFIED[key]
    base = config['base']
    assert base.startswith('/code/bratu-multinverse/') and base.endswith('/') and '..' not in base
    directory = root / base.lstrip('/')

    def file(name):
        path = Path(name)
        assert name and not path.is_absolute() and '..' not in path.parts
        target = directory / path
        assert target.resolve().is_relative_to(directory.resolve()) and target.is_file()
        return target

    digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
    manifest = json.loads(file(config['manifest']).read_text())
    receipt = json.loads(file(config['verification']).read_text())
    assert manifest['version'] == config['edition']
    assert manifest['family'] == 'bratu-multinverse' and manifest['public_base_url'] == ORIGIN + base
    required = {'numart/bratu_multinverse.py', 'numart/bratu_inverse.py', 'numart/bratu_sensitivity.py',
                'numart/autodiff.py', 'numart/krylov.py',
                'scripts/build_bratu_multinverse.py', 'tests/test_bratu_multinverse.py',
                'README.md', 'requirements.txt', 'LICENSE', 'LICENSING.md', config['evidence']}
    assert required <= manifest['files'].keys()
    for name, expected in manifest['files'].items():
        assert digest(file(name)) == expected, name
    archive = receipt['archive']
    assert archive['file'] == config['archive']
    assert file(config['archive']).stat().st_size == archive['bytes']
    assert digest(file(config['archive'])) == archive['sha256'] == receipt['archive_sha256']
    assert receipt['returncode'] == 0 and receipt['passed_tests'] > 0
    assert receipt['failures'] == receipt['errors'] == 0
    assert receipt['source_manifest_sha256'] == digest(file(config['manifest']))
    record = dict(code_base=ORIGIN + base, code_edition=config['edition'],
                  code_urls=[ORIGIN + base + name for name in
                             ['numart/bratu_multinverse.py', 'numart/bratu_inverse.py', 'numart/bratu_sensitivity.py',
                              'numart/autodiff.py', 'numart/krylov.py',
                              'scripts/build_bratu_multinverse.py']],
                  test_urls=[ORIGIN + base + 'tests/test_bratu_multinverse.py'],
                  run_commands=['python -m pytest -q tests/test_bratu_multinverse.py',
                                'python scripts/build_bratu_multinverse.py'],
                  run_from='Extracted multi-parameter Bratu inverse supplement directory',
                  code_download=ORIGIN + base + config['archive'],
                  code_manifest=ORIGIN + base + config['manifest'],
                  code_verification=ORIGIN + base + config['verification'],
                  code_archive_sha256=archive['sha256'],
                  results=ORIGIN + base + config['evidence'],
                  passed_tests=receipt['passed_tests'])
    _VERIFIED[key] = record
    return record
