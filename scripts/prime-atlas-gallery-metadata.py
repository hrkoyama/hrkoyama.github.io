#!/usr/bin/env python3
"""Prime saved gallery metadata before strict reverse resource routes.

Inputs are source catalogs, the prior preview manifest and immutable canonical
packet files. No plotting, solver or generated release registry, execution
route, problem hub or test-case index is used. Prior image records and bytes
are preserved; newly declared canonical PNGs are checked before registration.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import struct
import zlib


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(path):
    result = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            result.update(block)
    return result.hexdigest()


def read(path):
    return json.loads(path.read_text())


def local(root, name):
    part = PurePosixPath(name)
    require(name == part.as_posix() and not part.is_absolute() and
            '..' not in part.parts, 'Unsafe saved-image member')
    path = root / name
    require(path.is_file() and not path.is_symlink() and
            path.resolve().is_relative_to(root), 'Missing/unsafe saved file: ' + name)
    return path


def png_size(path):
    """Check saved PNG chunks/CRC/EOF without decoding or drawing an image."""
    raw = path.read_bytes()
    require(len(raw) >= 24 and raw[:8] == b'\x89PNG\r\n\x1a\n', 'Invalid saved PNG')
    offset, data_seen, end_seen = 8, False, False
    while offset < len(raw):
        require(offset + 12 <= len(raw), 'Truncated saved PNG chunk')
        length = int.from_bytes(raw[offset:offset + 4], 'big')
        end = offset + 12 + length
        require(end <= len(raw), 'Truncated saved PNG payload')
        kind = raw[offset + 4:offset + 8]
        require(re.fullmatch(rb'[A-Za-z]{4}', kind), 'Invalid saved PNG chunk type')
        require(int.from_bytes(raw[end - 4:end], 'big') ==
                zlib.crc32(raw[offset + 4:end - 4]) & 0xffffffff,
                'Invalid saved PNG CRC')
        require((offset == 8 and kind == b'IHDR' and length == 13) or
                (offset > 8 and kind != b'IHDR'), 'Invalid saved PNG header')
        data_seen |= kind == b'IDAT' and length > 0
        if kind == b'IEND':
            require(length == 0 and end == len(raw), 'Invalid saved PNG ending')
            end_seen = True
        offset = end
    require(data_seen and end_seen, 'Incomplete saved PNG')
    width, height = struct.unpack('>II', raw[16:24])
    require(min(width, height) > 0, 'Empty saved image dimensions')
    return width, height


def canonical_picture_binding(metadata, expansion, ident, member):
    """Bind one registered problem to its declared canonical saved image.

    Legacy extra figures keep their original caption-plus-note-suffix contract.
    Standard primary figures use the immutable case summary plus the explicitly
    authored case_note; this is display provenance, not a claimed plot caption.
    """
    candidates = [case for case in metadata
                  if expansion['case_problem_ids'].get(case['id']) == ident
                  and member == 'results/' + case.get('gallery_figure', case['id'] + '.png')]
    require(len(candidates) == 1,
            'Saved image needs one explicit canonical case/problem/member binding')
    case = candidates[0]
    notes = expansion['case_notes'][case['id']]
    require(isinstance(notes, dict) and all(isinstance(notes.get(language), str)
            and notes[language].strip() for language in ['ja', 'en']),
            'Saved image needs an explicit bilingual case note')
    expected_caption = {}
    if 'gallery_figure' in case:
        captions = [extra['caption'] for extra in case['additional_figures']
                    if extra['file'] == case['gallery_figure']]
        require(len(captions) == 1, 'Saved case needs one gallery caption')
        for language in ['ja', 'en']:
            original_limits = case['limits'][language]
            require(notes[language].startswith(original_limits),
                    'Source case notes lost the canonical limits prefix')
            expected_caption[language] = captions[0][language] + notes[language][len(original_limits):]
        contract = 'pre-run-contract.json'
    else:
        require(case.get('plot', case['id'] + '.png') == case['id'] + '.png',
                'Declared standard primary plot differs')
        for language in ['ja', 'en']:
            summary = case['summary'][language]
            require(isinstance(summary, str) and summary.strip(),
                    'Primary image needs a canonical bilingual case summary')
            expected_caption[language] = summary + ' ' + notes[language]
        contract = 'freeze.json'
    return case, expected_caption, contract


def assemble(root, *, load_group=None):
    """Return a metadata-only append; no writes, numerical imports or renders."""
    root = Path(root).resolve(strict=True)
    if load_group is None:
        # Strict standard canonical loader: all files, complete ZIP, actual
        # numerical result/input flags, independent rerun and PNG CRCs. It does
        # not invoke a solver. Injection below is for thin metadata unit tests.
        from atlas_depth_release import load_depth_group
        load_group = load_depth_group
    gallery = root / 'numerical-methods-atlas/gallery'
    previous = read(gallery / 'preview-manifest.json')
    result = deepcopy(previous)
    catalog = read(root / 'catalog/atlas-gallery.json')
    problems = read(root / 'catalog/atlas-test-problems.json')['problems']
    expansion = read(root / 'catalog/atlas-depth-expansion.json')
    rows, old = catalog['items'], previous['items']
    identifiers = [row['id'] for row in rows]
    old_ids = [row['id'] for row in old]
    require(len(identifiers) == len(set(identifiers)) and
            len(old_ids) == len(set(old_ids)), 'Duplicate picture identity')
    require(set(identifiers) == {row['id'] for row in problems},
            'Source gallery/problem identities differ')
    require(identifiers[:len(old_ids)] == old_ids,
            'Existing saved-picture order/identities must stay a prefix')
    require(previous['calculations_sha256'] == sha(gallery / 'calculations.json'),
            'The historical calculation receipt changed')
    inputs = {row['id']: row for row in rows}
    for row in old:
        item = inputs[row['id']]
        require(isinstance(row['image'], str) and row['image'].startswith('/') and
                not row['image'].startswith('//'), 'Unsafe existing image URL')
        image = local(root, row['image'][1:])
        require(sha(image) == row['image_sha256'] and
                min(row['width'], row['height']) > 0, 'Stale existing saved image')
        if image.suffix == '.png':
            require(png_size(image) == (row['width'], row['height']),
                    'Existing PNG dimensions differ')
        else:
            with image.open('rb') as stream:
                signature = stream.read(12)
            require(image.suffix == '.webp' and signature[:4] == b'RIFF' and
                    signature[8:12] == b'WEBP', 'Existing image type changed')
        require(row['caption'] == item['caption'],
                'Changing an existing picture caption needs explicit authoring: ' + row['id'])
        if item['kind'] == 'image':
            source = item['source']
            expected = source if source.startswith('/') else '/numerical-methods-atlas/' + source
            require(row['image'] == expected, 'Existing picture URL changed: ' + row['id'])

    receipts = result['source_sha256']

    def bind(name, expected=None):
        path = local(root, name)
        digest = sha(path)
        require(expected is None or expected == digest, 'Packet member SHA differs: ' + name)
        require(name not in receipts or receipts[name] == digest,
                'Existing picture provenance changed: ' + name)
        receipts[name] = digest
        return path

    additions, loaded_groups = [], {}
    for item in rows[len(old_ids):]:
        ident = item['id']
        require(item['kind'] == 'image',
                'New computed/stored plots need separate scientific authoring: ' + ident)
        source = item['source']
        require(isinstance(source, str) and source.startswith('/code/validated-examples/'),
                'Only immutable canonical image sources may be primed')
        matches = []
        for group in expansion['groups']:
            edition = group.get('edition', expansion['edition'])
            prefix = 'code/validated-examples/' + edition + '/' + group['id'] + '/'
            if source.startswith('/' + prefix):
                matches.append((group, edition, prefix))
        require(len(matches) == 1, 'Saved picture needs exactly one source release')
        group, edition, prefix = matches[0]
        base = root / prefix
        key = (group['id'], edition)
        if key not in loaded_groups:
            loaded_groups[key] = load_group(root, *key)
        qualified = loaded_groups[key]
        manifest = qualified['manifest']
        verification = qualified['verification']
        require(verification.get('passed') is True and
                verification.get('all_cases_rerun') is True and
                all(verification.get(key) == 0 for key in ['failures', 'errors', 'skipped']),
                'Unqualified canonical release: ' + group['id'])
        require(manifest.get('group') == group['id'] and
                manifest.get('version') == edition and
                verification.get('group') == group['id'] and
                verification.get('edition') == edition and
                verification['source_manifest_sha256'] == sha(base / 'source-manifest.json'),
                'Canonical packet identity differs')
        files = manifest['files']
        metadata = qualified['metadata']
        member = source.removeprefix('/' + prefix)
        case, expected_caption, contract = canonical_picture_binding(
            metadata, expansion, ident, member)
        require(expected_caption == item['caption'], 'Saved case/gallery caption differs')
        for name in ['cases.json', 'inputs.json', 'acceptance.json',
                     contract, 'results/result.json',
                     'results/' + case['id'] + '.png', member]:
            require(name in files and re.fullmatch('[a-f0-9]{64}', files[name]),
                    'Missing immutable member SHA')
            bind(prefix + name, files[name])
        bind(prefix + 'source-manifest.json')
        bind(prefix + 'verification.json')
        archive = verification['archive']
        bind(prefix + archive['file'], archive['sha256'])
        image = local(root, prefix + member)
        width, height = png_size(image)
        result['items'].append(dict(id=ident, image=source, image_sha256=files[member],
                                   width=width, height=height, source_kind='existing-figure',
                                   caption=deepcopy(item['caption'])))
        additions.append(ident)

    # These reviewed source catalogs now contain the added saved-picture
    # graph. Do not refresh arbitrary historical scientific file bindings.
    changed = {}
    for name in ['catalog/atlas-gallery.json', 'catalog/atlas-test-problems.json',
                 'catalog/atlas-depth-expansion.json', 'scripts/prime-atlas-gallery-metadata.py']:
        value = sha(local(root, name))
        if receipts.get(name) != value:
            changed[name] = dict(before=receipts.get(name), after=value)
        receipts[name] = value
    if additions or changed:
        require(re.fullmatch(r'\d{4}-\d{2}-\d{2}', catalog['reviewed_on']),
                'Source catalog needs its reviewed date')
        result.setdefault('metadata_updates', []).append(dict(
            on=catalog['reviewed_on'], date_role='Source catalog reviewed_on; not execution time.',
            scope='Register already qualified canonical PNG metadata before reverse routes; '
                  'retain all prior picture records/images and original numerical-preview receipts.',
            primary_item_count_before=len(old), primary_item_count_after=len(rows),
            added_primary_ids=additions,
            changed_catalog_bindings={name: value for name, value in changed.items()
                                      if name.startswith('catalog/')},
            producer=dict(path='scripts/prime-atlas-gallery-metadata.py',
                          sha256=receipts['scripts/prime-atlas-gallery-metadata.py']),
            historical_primary_records_unchanged=True, scientific_preview_execution=False,
            historical_figures_rerendered=False))
    require(result['items'][:len(old)] == old and
            [row['id'] for row in result['items']] == identifiers,
            'Metadata-only append did not preserve exact existing records')
    return result, additions


def prime(root):
    root = Path(root).resolve(strict=True)
    destination = root / 'numerical-methods-atlas/gallery/preview-manifest.json'
    before = destination.read_bytes()
    result, additions = assemble(root)
    encoded = (json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode()
    if encoded != before:
        temporary = destination.with_name(destination.name + '.metadata.tmp')
        with temporary.open('xb') as stream:
            stream.write(encoded)
        require(destination.read_bytes() == before, 'Picture metadata changed during priming')
        temporary.replace(destination)
    print('Primed existing canonical PNG metadata: ' + str(len(additions)) +
          ' additions; no images/calculations/verification rewritten.')


def main():
    prime(Path(__file__).resolve().parents[1])


if __name__ == '__main__':
    main()
