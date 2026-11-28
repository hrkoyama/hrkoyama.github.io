"""Exercise the public/private boundary using a processed public PNG fixture."""
import copy
import hashlib
import json
import os
import shutil
import struct
import tempfile
import unittest
import zlib
from pathlib import Path

from notebook_previews import validate_previews

ROOT = Path(__file__).resolve().parents[1]


class PreviewBoundary(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=os.environ.get('NOTEBOOK_TEST_TMPDIR'))
        self.site = Path(self.temp.name)
        bibliography = json.loads((ROOT/'notebooks/bibliography.json').read_text())
        self.entry = copy.deepcopy(next(e for e in bibliography['entries'] if e['id']=='b109'))
        source = json.loads((ROOT/'notebooks/material-preview-manifest.json').read_text())
        self.manifest = {**source, 'images':[copy.deepcopy(next(e for e in source['images'] if e['id']=='b109'))]}
        self.path = self.site/self.entry['preview']['image']
        self.path.parent.mkdir(parents=True)
        shutil.copyfile(ROOT/'notebooks'/self.entry['preview']['image'],self.path)
        self.save()

    def tearDown(self):
        self.temp.cleanup()

    def save(self):
        (self.site/'material-preview-manifest.json').write_text(json.dumps(self.manifest))

    def rehash(self, content):
        self.path.write_bytes(content)
        self.manifest['images'][0].update(bytes=len(content),sha256=hashlib.sha256(content).hexdigest())
        self.save()

    def test_processed_public_title_image_is_valid(self):
        self.assertEqual(set(validate_previews(self.site,[self.entry])),{'b109'})

    def test_private_original_reference_is_rejected_even_with_a_manifest_entry(self):
        self.entry['preview']['image']='private/originals/source.pdf'
        self.manifest['images'][0]['image']=self.entry['preview']['image'];self.save()
        with self.assertRaises(AssertionError):validate_previews(self.site,[self.entry])

    def test_ocr_metadata_is_rejected_even_after_rehashing(self):
        payload=b'Comment\x00unpublished OCR fixture'
        kind=b'tEXt'
        chunk=struct.pack('>I',len(payload))+kind+payload+struct.pack('>I',zlib.crc32(kind+payload)&0xffffffff)
        content=self.path.read_bytes()
        self.rehash(content[:-12]+chunk+content[-12:])
        with self.assertRaisesRegex(AssertionError,'metadata'):validate_previews(self.site,[self.entry])

    def test_trailing_unpublished_data_is_rejected_after_rehashing(self):
        self.rehash(self.path.read_bytes()+b'unpublished text fixture')
        with self.assertRaisesRegex(AssertionError,'Trailing'):validate_previews(self.site,[self.entry])

    def test_unlisted_document_in_public_preview_folder_is_rejected(self):
        (self.path.parent/'original.pdf').write_bytes(b'Unpublished document fixture')
        with self.assertRaises(AssertionError):validate_previews(self.site,[self.entry])


if __name__=='__main__':unittest.main()
