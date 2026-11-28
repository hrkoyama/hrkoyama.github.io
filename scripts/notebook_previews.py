"""Validate only the allowlisted, processed public cover/title PNGs."""
import hashlib
import json
import re
import struct
import zlib
from pathlib import Path


def png_dimensions(content):
    assert content[:8] == b'\x89PNG\r\n\x1a\n', 'Preview must be PNG'
    offset, chunks, dimensions = 8, [], None
    while offset < len(content):
        assert offset + 12 <= len(content), 'Truncated PNG chunk'
        size = struct.unpack('>I', content[offset:offset+4])[0]
        kind = content[offset+4:offset+8]
        end = offset + size + 12
        assert end <= len(content), 'Truncated PNG payload'
        payload = content[offset+8:offset+8+size]
        crc = struct.unpack('>I', content[offset+8+size:end])[0]
        assert zlib.crc32(kind+payload) & 0xffffffff == crc, 'PNG checksum mismatch'
        assert kind in {b'IHDR', b'IDAT', b'IEND'}, 'Preview has unapproved PNG metadata'
        if kind == b'IHDR':
            assert not chunks and size == 13
            width, height, depth, colour, compression, filtering, interlace = struct.unpack('>IIBBBBB', payload)
            assert depth == 8 and colour == 2 and compression == filtering == interlace == 0, 'Preview must be fresh non-interlaced RGB'
            assert 0 < width <= 2000 and 0 < height <= 2000
            dimensions = (width, height)
        if kind == b'IEND':
            assert size == 0 and end == len(content), 'Trailing PNG data'
        chunks.append(kind); offset = end
    assert chunks[0] == b'IHDR' and chunks[-1] == b'IEND' and b'IDAT' in chunks
    assert chunks.count(b'IHDR') == chunks.count(b'IEND') == 1
    return dimensions


def validate_previews(site, entries):
    materials = {entry['id']:entry for entry in entries}
    manifest = json.loads((site / 'material-preview-manifest.json').read_text())
    assert set(manifest) == {'schema_version', 'updated_on', 'images', 'scope'}
    images = {item['id']:item for item in manifest['images']}
    assert len(images) == len(manifest['images'])
    preview_keys = {'mode','label','caption','alt','year_label','image','width','height'}
    private_reference = re.compile(r'/Users/|/Volumes/|drive\.google\.com|private/|\.tar\.xz|[\w.+%-]+@[\w.-]+\.[A-Za-z]{2,}', re.I)
    for material_id, material in materials.items():
        assert material['holding_status'] == 'scan_verified'
        preview = material['preview']
        assert set(preview) <= preview_keys
        assert {'mode','label','caption','alt','year_label','image'} <= set(preview)
        assert preview['mode'] in {'cover','masked_first_page','metadata_only'}
        for key in ['label','caption','alt','year_label']:
            value = preview[key]
            if value is None:
                assert key == 'year_label'
                continue
            assert set(value) == {'ja','en'}
            assert all(isinstance(v,str) and len(v) <= 1000 for v in value.values())
        assert not private_reference.search(json.dumps(preview,ensure_ascii=False)), material_id
        image = preview['image']
        if not image:
            assert image is None and preview['mode'] == 'metadata_only' and material_id not in images
            assert not ({'width','height'} & set(preview))
            continue
        assert preview['mode'] != 'metadata_only'
        assert image == f'assets/material-previews/{material_id}-first-page.png'
        assert re.fullmatch(r'assets/material-previews/b\d{3}(?:-[a-z0-9]+)*-first-page\.png', image)
        item = images[material_id]
        assert set(item) == {'id','image','sha256','bytes','width','height'}
        assert item['image'] == image
        path = site / image
        assert not path.is_symlink() and path.is_file()
        content = path.read_bytes()
        assert len(content) == item['bytes']
        assert hashlib.sha256(content).hexdigest() == item['sha256'], material_id
        assert png_dimensions(content) == (preview['width'],preview['height']) == (item['width'],item['height'])
    assert set(images) == {material_id for material_id, m in materials.items() if m['preview']['image']}
    folder = site / 'assets/material-previews'
    assert {p.relative_to(site).as_posix() for p in folder.rglob('*') if p.is_file()} == {item['image'] for item in images.values()}
    return images
