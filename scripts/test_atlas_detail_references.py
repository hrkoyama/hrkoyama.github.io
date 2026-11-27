"""Tiny isolated fixtures for active detail inventories, without site generation."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from compact_search import GROUPS, encoded, write_compact


def digest(value):
    return hashlib.sha256(encoded(value)).hexdigest()


def git_blob_sha(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


class DetailReferenceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='atlas-detail-references-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def build(self, kind, rows):
        field = 'entries' if kind == 'atlas' else 'documents'
        source = {field: rows}
        source_path = self.root / ('numerical-methods-atlas/home-search-index.json'
                                   if kind == 'atlas' else 'search/index.json')
        source_path.parent.mkdir(parents=True, exist_ok=True)
        source_path.write_bytes(encoded(source))
        index = write_compact(self.root, source, kind)
        manifest_path = self.root / 'search' / ('atlas-detail-references.json'
                                              if kind == 'atlas' else 'detail-references.json')
        return index, manifest_path, json.loads(manifest_path.read_bytes())

    def assert_binding(self, kind, index, manifest, keys):
        raw = index.read_bytes()
        self.assertEqual(manifest, {
            'schema_version': 1, 'kind': kind,
            'index_path': 'search/atlas-query-index.json' if kind == 'atlas' else 'search/query-index.json',
            'index_git_blob_sha': git_blob_sha(raw),
            'index_sha256': hashlib.sha256(raw).hexdigest(),
            'detail_keys': sorted(keys),
        })
        self.assertEqual(len(manifest['detail_keys']), len(set(manifest['detail_keys'])))
        for key in manifest['detail_keys']:
            self.assertRegex(key, r'\A[0-9a-f]{64}\Z')
            detail = self.root / 'search' / 'details' / (key + '.json')
            self.assertEqual(hashlib.sha256(detail.read_bytes()).hexdigest(), key)

    def test_both_indexes_bind_exact_active_text_and_navigation_keys(self):
        text = 'Read the fixed evidence. ' * 30
        navigation = {'kind': 'method', 'id': 'fixture',
                      'groups': {name: ([{'id': 'method-one', 'url': '/methods/one/'}]
                                        if name == 'methods' else []) for name in GROUPS}}
        localized = {'ja': '公開された根拠を読む。' * 60, 'en': 'Evidence to inspect. ' * 30}
        for kind in ('atlas', 'site'):
            with self.subTest(kind=kind):
                index, _, manifest = self.build(kind, [
                    {'id': 'one', 'text': text, 'search_navigation': navigation},
                    {'id': 'same-text', 'text': text},
                    {'id': 'localized', 'text': localized},
                    {'id': 'short', 'text': 'Short text'},
                ])
                keys = {digest({'text': text}), digest({'text': localized}),
                        digest({'search_navigation': navigation})}
                self.assert_binding(kind, index, manifest, keys)

    def test_regeneration_replaces_manifest_but_preserves_historical_and_orphan_details(self):
        for kind in ('atlas', 'site'):
            with self.subTest(kind=kind):
                old_text = 'Original evidence. ' * 40
                _, manifest_path, old_manifest = self.build(kind, [{'id': 'one', 'text': old_text}])
                old_key = digest({'text': old_text})
                historical = self.root / 'search' / 'details' / (old_key + '.json')
                historical_raw = historical.read_bytes()
                orphan_raw = encoded({'text': 'Unreferenced tolerance 1e-2 https://example.org/other'})
                orphan_key = hashlib.sha256(orphan_raw).hexdigest()
                orphan = historical.parent / (orphan_key + '.json')
                orphan.write_bytes(orphan_raw)
                manifest_path.write_bytes(encoded({'detail_keys': [orphan_key], 'forged': True}))
                new_text = 'Revised evidence. ' * 40
                index, _, manifest = self.build(kind, [{'id': 'one', 'text': new_text}])
                self.assert_binding(kind, index, manifest, {digest({'text': new_text})})
                self.assertNotEqual(manifest['index_git_blob_sha'], old_manifest['index_git_blob_sha'])
                self.assertNotIn(old_key, manifest['detail_keys'])
                self.assertNotIn(orphan_key, manifest['detail_keys'])
                self.assertEqual(historical.read_bytes(), historical_raw)
                self.assertEqual(orphan.read_bytes(), orphan_raw)

    def test_empty_reference_list_is_explicit_and_bound_to_actual_index(self):
        for kind in ('atlas', 'site'):
            with self.subTest(kind=kind):
                index, _, manifest = self.build(kind, [{'id': 'short', 'text': 'Short evidence'}])
                self.assert_binding(kind, index, manifest, set())

    def test_unchanged_source_has_identical_index_and_manifest_bytes(self):
        rows = [{'id': 'one', 'text': 'Stable evidence. ' * 40}]
        for kind in ('atlas', 'site'):
            with self.subTest(kind=kind):
                index, manifest_path, _ = self.build(kind, rows)
                before = (index.read_bytes(), manifest_path.read_bytes())
                self.build(kind, rows)
                self.assertEqual((index.read_bytes(), manifest_path.read_bytes()), before)

    def test_atlas_and_site_inventories_do_not_overwrite_each_other(self):
        _, atlas_path, atlas_manifest = self.build('atlas', [{'id': 'atlas', 'text': 'Atlas evidence. ' * 40}])
        atlas_raw = atlas_path.read_bytes()
        _, site_path, site_manifest = self.build('site', [{'id': 'site', 'text': 'Site evidence. ' * 40}])
        self.assertNotEqual(site_path, atlas_path)
        self.assertEqual(atlas_path.read_bytes(), atlas_raw)
        self.assertNotEqual(atlas_manifest['detail_keys'], site_manifest['detail_keys'])

    def test_unknown_kind_is_rejected(self):
        with self.assertRaises(ValueError):
            write_compact(self.root, {'documents': []}, 'unknown')


if __name__ == '__main__':
    unittest.main()
