"""Verify immutable lightweight validation supplements without executing solvers."""
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import re
import zipfile
import zlib

ORIGIN = 'https://hrkoyama.github.io'
GROUPS = ('foundations', 'models', 'particles', 'mhd', 'thermostats', 'biology', 'mcmc', 'mhd-convergence', 'foundations-conditioning', 'particle-transport', 'splitting', 'noh', 'noh-cartesian', 'sedov', 'double-mach', 'forward-step', 'low-mach', 'guderley', 'euler-positivity')
EDITION_PATTERN = r'\d{4}-\d{2}-\d{2}(?:-r\d+)?'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _object(pairs):
    result = {}
    for key, value in pairs:
        assert key not in result, 'Duplicate JSON key: '+key
        result[key] = value
    return result


def read_json(path):
    def invalid(value):
        raise ValueError('Nonfinite JSON constant: '+value)
    return json.loads(path.read_text(), object_pairs_hook=_object, parse_constant=invalid)


def _finite(value):
    if isinstance(value, float):
        assert math.isfinite(value), 'Nonfinite stored measurement'
    elif isinstance(value, dict):
        for child in value.values():
            _finite(child)
    elif isinstance(value, list):
        for child in value:
            _finite(child)


def _code_order(names, cases):
    preferred = ['run.py']
    for case in cases:
        for name in case.get('code_files', []):
            assert name in names, 'Unknown case-specific algorithm file: '+name
            preferred.append(name)
    preferred += [name for name in names if '/' not in name]
    preferred += names
    return list(dict.fromkeys(preferred))


def depth_additional_figures(directory, manifest, case):
    """Resolve optional, hash-bound saved PNGs without executing a renderer."""
    rows = case.get('additional_figures', [])
    assert isinstance(rows, list), 'Additional figures must be a list'
    directory = Path(directory).resolve()
    figures, seen = [], set()
    for row in rows:
        assert isinstance(row, dict), 'Additional figure must be a record'
        name = row.get('file')
        assert isinstance(name, str) and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*\.png', name), \
            'Additional figure must name a PNG directly inside results/'
        assert name not in seen and name != case['id']+'.png', 'Repeated additional figure'
        seen.add(name)
        caption = row.get('caption')
        assert isinstance(caption, dict) and all(
            isinstance(caption.get(language), str) and caption[language].strip()
            for language in ['ja', 'en']), 'Additional figure needs both captions'
        relative = 'results/'+name
        expected = manifest['files'].get(relative)
        assert isinstance(expected, str) and re.fullmatch(r'[0-9a-f]{64}', expected), \
            'Additional figure is absent from the source manifest'
        path = directory/relative
        assert path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(directory), \
            'Missing or unsafe additional figure'
        raw = path.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == expected, 'Changed additional figure'
        assert len(raw) >= 24 and raw[:8] == b'\x89PNG\r\n\x1a\n' and raw[12:16] == b'IHDR', \
            'Additional figure is not a saved PNG'
        offset, image_data, image_end = 8, False, False
        while offset < len(raw):
            assert offset+12 <= len(raw), 'Truncated additional PNG chunk'
            length = int.from_bytes(raw[offset:offset+4], 'big')
            end = offset+12+length
            assert end <= len(raw), 'Truncated additional PNG data'
            kind = raw[offset+4:offset+8]
            assert re.fullmatch(rb'[A-Za-z]{4}', kind), 'Invalid additional PNG chunk'
            assert int.from_bytes(raw[end-4:end], 'big') == zlib.crc32(raw[offset+4:end-4]) & 0xffffffff, \
                'Invalid additional PNG checksum'
            assert (offset == 8 and kind == b'IHDR' and length == 13) or (offset > 8 and kind != b'IHDR'), \
                'Invalid additional PNG header'
            image_data |= kind == b'IDAT' and length > 0
            if kind == b'IEND':
                assert length == 0 and end == len(raw), 'Invalid additional PNG ending'
                image_end = True
            offset = end
        assert image_data and image_end, 'Incomplete additional PNG'
        width, height = int.from_bytes(raw[16:20], 'big'), int.from_bytes(raw[20:24], 'big')
        assert width > 0 and height > 0, 'Additional figure has invalid dimensions'
        figures.append({'file': name, 'caption': dict(caption), 'width': width, 'height': height})
    return figures


def depth_gallery_figure(directory, manifest, case):
    """Opt in to one already verified extra figure, preserving primary pictures."""
    if 'gallery_figure' not in case:
        return None
    name = case['gallery_figure']
    assert isinstance(name, str), 'Gallery figure must name an additional PNG'
    figures = depth_additional_figures(directory, manifest, case)
    matches = [row for row in figures if row['file'] == name]
    assert len(matches) == 1, 'Gallery figure must be a hash-bound additional figure'
    row = matches[0]
    return {**row, 'sha256': manifest['files']['results/'+name]}


def load_depth_group(root, group, edition):
    """Strictly validate files, archive, numerical flags and independent-rerun receipt.

    No process or network is started. There is intentionally no stale-file cache:
    editing a previously checked file must be rejected on the next call.
    """
    root = Path(root).resolve()
    assert group in GROUPS and re.fullmatch(EDITION_PATTERN, edition)
    base = '/code/validated-examples/'+edition+'/'+group+'/'
    directory = (root/base.lstrip('/')).resolve()
    assert directory.is_relative_to(root) and directory.is_dir()

    def file(name):
        relative = PurePosixPath(name)
        assert name and not relative.is_absolute() and '..' not in relative.parts
        assert relative.as_posix() == name and '\\' not in name
        target = (directory/relative).resolve()
        assert target.is_relative_to(directory) and target.is_file(), 'Missing/unsafe release file: '+name
        return target

    manifest = read_json(file('source-manifest.json'))
    receipt = read_json(file('verification.json'))
    assert manifest['family'] == 'depth-'+group and manifest['group'] == group
    assert manifest['version'] == edition and manifest['public_base_url'] == ORIGIN+base
    assert isinstance(manifest['files'], dict) and manifest['files']
    required = {'run.py', 'inputs.json', 'cases.json', 'requirements.txt',
                'README.md', 'LICENSE', 'results/result.json'}
    assert required <= manifest['files'].keys()
    for name, expected in manifest['files'].items():
        assert isinstance(expected, str) and re.fullmatch(r'[0-9a-f]{64}', expected)
        assert digest(file(name)) == expected, 'Changed immutable file: '+name

    metadata = read_json(file('cases.json'))
    if isinstance(metadata, dict):
        metadata = metadata['cases']
    assert isinstance(metadata, list) and metadata
    indexed = {case['id']: case for case in metadata}
    assert len(indexed) == len(metadata), 'Repeated metadata case ID'
    assert all(re.fullmatch(r'[a-z][a-z0-9-]+', ident) for ident in indexed)
    for case in metadata:
        assert case['method_ids'] and len(case['method_ids']) == len(set(case['method_ids']))
        for field in ['title', 'summary', 'assumptions', 'algorithm', 'validation', 'limits']:
            assert all(isinstance(case[field][language], str) and case[field][language].strip()
                       for language in ['ja', 'en']), (case['id'], field)
        assert case['references'] and all(reference.get('review_level') for reference in case['references'])
        assert 'results/'+case['id']+'.png' in manifest['files'], 'Missing stored figure: '+case['id']
        depth_additional_figures(directory, manifest, case)
        depth_gallery_figure(directory, manifest, case)

    results = read_json(file('results/result.json'))
    _finite(results)
    assert results['passed'] is True and results['checks']
    assert all(value is True for value in results['checks'].values())
    assert results['input_sha256'] == digest(file('inputs.json'))
    measured = {case['id']: case for case in results['cases']}
    assert len(measured) == len(results['cases']) and measured.keys() == indexed.keys()
    assert set(manifest['case_ids']) == set(indexed) and len(manifest['case_ids']) == len(indexed)
    for case in measured.values():
        assert case['passed'] is True and case['checks']
        assert all(value is True for value in case['checks'].values()), case['id']
        assert isinstance(case['metrics'], dict) and case['metrics']
        assert isinstance(case.get('records'), (list, dict)) and case['records']

    assert receipt['group'] == group and receipt['edition'] == edition
    assert receipt['passed'] is True and receipt['all_cases_rerun'] is True
    assert type(receipt['tests']) is int and receipt['tests'] == receipt['passed_tests'] > 0
    assert receipt['failures'] == receipt['errors'] == receipt['skipped'] == 0
    assert receipt['returncode'] == 0
    assert set(receipt['case_ids']) == set(indexed) and len(receipt['case_ids']) == len(indexed)
    assert receipt['source_manifest_sha256'] == digest(file('source-manifest.json'))
    assert math.isfinite(receipt['independent_rerun_seconds']) and receipt['independent_rerun_seconds'] >= 0
    archive = receipt['archive']
    expected_archive = 'atlas-'+group+'-'+edition+'.zip'
    prefix = 'atlas-'+group+'-'+edition
    assert archive['file'] == expected_archive and archive['archive_directory'] == prefix
    assert archive['bytes'] == file(expected_archive).stat().st_size
    assert archive['sha256'] == digest(file(expected_archive))
    if 'archive_sha256' in receipt:
        assert archive['sha256'] == receipt['archive_sha256']
    with zipfile.ZipFile(file(expected_archive)) as zipped:
        expected_names = {prefix+'/'+name for name in [*manifest['files'], 'source-manifest.json']}
        assert set(zipped.namelist()) == expected_names and len(zipped.namelist()) == len(expected_names)
        for name, expected in manifest['files'].items():
            assert hashlib.sha256(zipped.read(prefix+'/'+name)).hexdigest() == expected, 'Changed ZIP member: '+name
        assert hashlib.sha256(zipped.read(prefix+'/source-manifest.json')).hexdigest() == digest(file('source-manifest.json'))

    # Failed, archived revisions remain in the manifest/ZIP, not active code links.
    python_files = sorted(name for name in manifest['files']
                          if name.endswith('.py') and 'attempts' not in PurePosixPath(name).parts)
    tests = [name for name in python_files if PurePosixPath(name).name.startswith('test_')]
    code = [name for name in python_files if name not in tests and PurePosixPath(name).name not in ('plot.py', '__init__.py')]
    assert 'run.py' in code and tests
    code = _code_order(code, metadata)
    sources = {base.lstrip('/')+'source-manifest.json': digest(file('source-manifest.json')),
               base.lstrip('/')+'verification.json': digest(file('verification.json')),
               base.lstrip('/')+'cases.json': digest(file('cases.json')),
               base.lstrip('/')+'results/result.json': digest(file('results/result.json')),
               base.lstrip('/')+expected_archive: archive['sha256']}
    return {'group': group, 'edition': edition, 'base': base, 'directory': directory,
            'manifest': manifest, 'verification': receipt, 'metadata': metadata,
            'results': results, 'source_sha256': sources, 'code_files': code,
            'code_urls': [ORIGIN+base+name for name in code],
            'test_urls': [ORIGIN+base+name for name in tests]}


def _depth_release_record(root, method, config):
    assert method['status'] == 'educational-example'
    assert set(config) >= {'group', 'edition', 'case_ids'}
    data = load_depth_group(root, config['group'], config['edition'])
    selected = config['case_ids']
    assert isinstance(selected, list) and selected and len(selected) == len(set(selected))
    metadata = {case['id']: case for case in data['metadata']}
    measured = {case['id']: case for case in data['results']['cases']}
    assert set(selected) <= metadata.keys()
    assert all(method['id'] in metadata[ident]['method_ids'] for ident in selected), 'Unrelated validation borrowed by method'
    examples = [{**metadata[ident], 'measured': measured[ident],
                 'entry': ORIGIN+'/numerical-methods-atlas/validation/'+ident+'/',
                 'reading': {language: ORIGIN+'/numerical-methods-atlas/'+language+'/read/validation-'+data['group']+'/#'+ident
                             for language in ['ja', 'en']}}
                for ident in selected]
    base = ORIGIN+data['base']
    return {'group': data['group'], 'case_ids': selected,
            'code_base': base, 'code_edition': data['edition'],
            'code_urls': depth_code_urls(data, selected), 'test_urls': data['test_urls'],
            'run_commands': ['python -m pytest -q', 'python run.py --input inputs.json --output output'],
            'run_from': data['verification']['archive']['archive_directory'],
            'code_download': base+data['verification']['archive']['file'],
            'code_manifest': base+'source-manifest.json', 'code_verification': base+'verification.json',
            'code_archive_sha256': data['verification']['archive']['sha256'],
            'results': base+'results/result.json', 'passed_tests': data['verification']['passed_tests'],
            'examples': examples}


def depth_release_record(root, method):
    """Resolve the primary release, retaining the original public API."""
    return _depth_release_record(root, method, method['depth_release'])


def depth_release_records(root, method):
    """Resolve separately verified editions without replacing earlier evidence."""
    configs = [method['depth_release'], *method.get('depth_additional_releases', [])]
    identities = [(item['group'], item['edition']) for item in configs]
    assert len(identities) == len(set(identities)), 'Repeated supplement release'
    records = [_depth_release_record(root, method, config) for config in configs]
    identifiers = [ident for record in records for ident in record['case_ids']]
    assert len(identifiers) == len(set(identifiers)), 'Repeated supplement case across releases'
    return records


def depth_code_urls(data, case_ids):
    """Put the selected cases' algorithm files before unrelated group modules."""
    metadata = {case['id']: case for case in data['metadata']}
    assert case_ids and set(case_ids) <= metadata.keys()
    files = _code_order(data['code_files'], [metadata[ident] for ident in case_ids])
    return [ORIGIN+data['base']+name for name in files]
