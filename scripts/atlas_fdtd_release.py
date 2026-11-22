"""Resolve the immutable, independently extracted 2D TMz FDTD supplement."""
import hashlib
import json
import re
from pathlib import Path

ORIGIN = 'https://hrkoyama.github.io'


def fdtd_release_record(root, method):
    config = method['fdtd_release']
    assert method['id'] == 'fdtd' and method['status'] == 'educational-example'
    assert not method['code_modules'] and not method['test_files']
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}(?:-r\d+)?', config['edition'])
    base = config['base']
    assert base == '/code/fdtd/' + config['edition'] + '/'
    directory = root / base.lstrip('/')
    assert directory.resolve().is_relative_to(root.resolve())

    def file(name):
        path = Path(name)
        assert name and not path.is_absolute() and '..' not in path.parts
        target = directory / path
        assert target.resolve().is_relative_to(directory.resolve()) and target.is_file()
        return target

    digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
    manifest = json.loads(file(config['manifest']).read_text())
    receipt = json.loads(file(config['verification']).read_text())
    assert manifest.get('version', manifest.get('edition')) == config['edition']
    assert manifest['family'] == 'fdtd' and manifest['public_base_url'] == ORIGIN + base
    cases = ['periodic-wave', 'pec-cavity']
    required = {'solver.py', 'run.py', 'test_fdtd.py', 'README.md', 'requirements.txt', 'LICENSE'}
    for case in cases:
        required.add('inputs/' + case + '.json')
        required.update('results/' + case + '/' + name for name in
                        ['result.json', 'summary.png', 'convergence.csv', 'energy.csv', 'solution.csv'])
    assert required <= manifest['files'].keys()
    for name, expected in manifest['files'].items():
        assert digest(file(name)) == expected, name
    for case in cases:
        evidence = json.loads(file('results/' + case + '/result.json').read_text())
        assert evidence['case'] == case and evidence['passed'] is True
        assert evidence['termination'] == 'fixed_budget_completed'
        assert evidence['checks'] and all(value is True for value in evidence['checks'].values())
        assert evidence['input_sha256'] == digest(file('inputs/' + case + '.json'))
    archive = receipt['archive']
    assert archive['file'] == config['archive']
    assert file(config['archive']).stat().st_size == archive['bytes']
    assert digest(file(config['archive'])) == archive['sha256'] == receipt['archive_sha256']
    assert receipt['returncode'] == 0 and receipt['passed_tests'] > 0
    assert receipt['tests'] == receipt['passed_tests']
    assert receipt['failures'] == receipt['errors'] == receipt['skipped'] == 0
    assert receipt['source_manifest_sha256'] == digest(file(config['manifest']))
    return dict(code_base=ORIGIN + base, code_edition=config['edition'],
                code_urls=[ORIGIN + base + name for name in ['solver.py', 'run.py']],
                test_urls=[ORIGIN + base + 'test_fdtd.py'],
                run_commands=['python -m pytest -q test_fdtd.py'] +
                    ['python run.py --input inputs/' + case + '.json --output rerun-' + case for case in cases],
                run_from='Extracted 2D TMz FDTD supplement directory',
                code_download=ORIGIN + base + config['archive'],
                code_manifest=ORIGIN + base + config['manifest'],
                code_verification=ORIGIN + base + config['verification'],
                code_archive_sha256=archive['sha256'],
                results=ORIGIN + base + 'results/periodic-wave/result.json',
                result_urls={case: ORIGIN + base + 'results/' + case + '/result.json' for case in cases},
                passed_tests=receipt['passed_tests'])
