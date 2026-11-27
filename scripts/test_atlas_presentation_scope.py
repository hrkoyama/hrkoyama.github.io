"""Offline safety regressions for the finite presentation-only source boundary.

No generated corpus, ZIP, network access or numerical execution is needed.
Derived outputs require the caller's separate, same-SHA generation proof.
"""
import copy
import json
import os
from pathlib import Path
import re
import subprocess
import unittest

from atlas_presentation_scope import (presentation_kind, presentation_signature,
                                      presentation_cache_references)


ROOT = Path(__file__).resolve().parents[1]
CATALOGS = (
    "catalog/atlas-home.json",
    "catalog/atlas-purpose.json",
    "catalog/atlas-sharing.json",
)


def encode(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False).encode("utf-8")


def catalog(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def actual_source_bytes(name):
    """Read the real page, using immutable local Git objects in sparse copies."""
    path = ROOT / name
    if path.is_file():
        return path.read_bytes()
    return subprocess.check_output(
        ["git", "show", "HEAD:" + name], cwd=ROOT,
        env={**os.environ, "GIT_NO_LAZY_FETCH": "1", "GIT_TERMINAL_PROMPT": "0"})


def set_leaf(value, path, replacement):
    result = copy.deepcopy(value)
    cursor = result
    for part in path[:-1]:
        cursor = cursor[part]
    cursor[path[-1]] = replacement
    return result


class PresentationScopeTests(unittest.TestCase):
    def signature(self, path, raw):
        result = presentation_signature(path, raw)
        self.assertIsInstance(result, str)
        self.assertRegex(result, r"\A[0-9a-f]{64}\Z")
        return result

    def equivalent(self, path, before, after):
        self.assertEqual(self.signature(path, before), self.signature(path, after))

    def protected(self, path, before, after):
        """A rejected payload or a changed signature must prevent reuse."""
        try:
            old = self.signature(path, before)
            new = self.signature(path, after)
        except ValueError:
            return
        self.assertNotEqual(old, new, path)

    def test_catalogs_have_the_actual_localized_shapes(self):
        home, purpose, sharing = [catalog(path) for path in CATALOGS]
        self.assertEqual(set(home["landing"]), {"ja", "en"})
        self.assertEqual(set(purpose), {"ja", "en"})
        self.assertEqual(set(sharing["copy"]), {"ja", "en"})
        for language in ("ja", "en"):
            self.assertIsInstance(home["landing"][language]["introduction"]["why"], str)
            self.assertIsInstance(purpose[language]["paragraphs"], list)
            self.assertTrue(purpose[language]["paragraphs"])
            self.assertIn("{execution_examples}", sharing["copy"][language]["short"])
        for path in CATALOGS:
            self.assertEqual(presentation_kind(path), "catalog")
            self.signature(path, encode(catalog(path)))

    def test_real_catalog_intro_slots_allow_wording_in_both_languages(self):
        slots = {
            CATALOGS[0]: [("landing", lang, *tail) for lang in ("ja", "en") for tail in (
                ("title",), ("description",), ("introduction", "why"),
                ("introduction", "connections"), ("introduction", "ai"),
                ("introduction", "feedback"), ("introduction", "details_title"))],
            CATALOGS[1]: [(lang, *tail) for lang in ("ja", "en") for tail in (
                ("title",), ("meta_description",), ("paragraphs", 0), ("paragraphs", 2))],
            CATALOGS[2]: [("copy", lang, key) for lang in ("ja", "en") for key in (
                "title", "headline", "lead", "short", "paragraph", "description")],
        }
        for path, paths in slots.items():
            before = catalog(path)
            for leaf in paths:
                old = before
                for part in leaf:
                    old = old[part]
                with self.subTest(path=path, leaf=leaf):
                    self.equivalent(path, encode(before), encode(set_leaf(before, leaf, old + " Read the evidence.")))

    def test_catalog_non_intro_content_identity_and_structure_are_protected(self):
        cases = [
            (CATALOGS[0], ("landing", "ja", "entries", 0, "href"), "/other/"),
            (CATALOGS[0], ("landing", "en", "entries", 0, "id"), "other"),
            (CATALOGS[0], ("landing", "en", "collection", "note"), "Other scope"),
            (CATALOGS[1], ("en", "browse", 0, "description"), "Other scope"),
            (CATALOGS[1], ("ja", "status_note"), "Other scope"),
            (CATALOGS[2], ("atlas_url",), "https://example.org/"),
            (CATALOGS[2], ("sharing_terms", "en"), "Other terms"),
            (CATALOGS[2], ("copy", "en", "image", "subtitle"), "Other image"),
            (CATALOGS[2], ("image", "width"), 1201),
            (CATALOGS[2], ("renderer", "dependency"), "Pillow==1.0.0"),
        ]
        for path, leaf, replacement in cases:
            with self.subTest(path=path, leaf=leaf):
                before = catalog(path)
                self.protected(path, encode(before), encode(set_leaf(before, leaf, replacement)))
        for path in CATALOGS:
            before = catalog(path)
            for key in ("acceptance", "references", "inputs", "tolerance"):
                after = copy.deepcopy(before)
                after[key] = {"value": 1e-8}
                with self.subTest(path=path, added=key):
                    self.protected(path, encode(before), encode(after))
            after = copy.deepcopy(before)
            del after[next(iter(after))]
            self.protected(path, encode(before), encode(after))
        before = catalog(CATALOGS[1])
        after = copy.deepcopy(before)
        after["en"]["paragraphs"].append("Another paragraph")
        self.protected(CATALOGS[1], encode(before), encode(after))

    def test_catalog_numeric_reference_placeholder_and_formula_changes_fail_closed(self):
        path = CATALOGS[0]
        original = catalog(path)
        leaf = ("landing", "en", "description")
        pairs = [
            ("Threshold 1e-8", "Threshold 1e-2"),
            ("Count 22", "Count 23"),
            ("Value -0.25", "Value +0.25"),
            ("See https://example.org/old", "See https://example.org/new"),
            ("See /code/old.py", "See /code/new.py"),
            ("[source](../code/old.py)", "[source](../code/new.py)"),
            ("[source](./old.json)", "[source](./new.json)"),
            ("Use {execution_examples} examples", "Use {test_problems} examples"),
            ("Formula $a+b$", "Formula $a-b$"),
            (r"Formula \(a+b\)", r"Formula \(a-b\)"),
            ("Use `old.py`", "Use `new.py`"),
            ("Read the evidence", '<script src="/other.js"></script>'),
            ("Read the evidence", '<a href="../code/changed.py">Read the evidence</a>'),
        ]
        for old, new in pairs:
            with self.subTest(before=old, after=new):
                self.protected(path, encode(set_leaf(original, leaf, old)),
                               encode(set_leaf(original, leaf, new)))
        path = CATALOGS[2]
        before = catalog(path)
        old = before["copy"]["en"]["short"]
        self.protected(path, encode(before), encode(set_leaf(before, ("copy", "en", "short"),
                           old.replace("{execution_examples}", "{test_problems}"))))

    def test_catalog_json_formatting_is_allowed_but_invalid_json_is_not(self):
        for path in CATALOGS:
            before = catalog(path)
            self.equivalent(path, encode(before), json.dumps(before, ensure_ascii=False, indent=4,
                            sort_keys=True, allow_nan=False).encode("utf-8"))
        for payload in (b'{"landing":{},"landing":{}}', b'{"x":NaN}', b'{"x":Infinity}',
                        b'{"x":1e999}', b'[]', b'null', b'{', b'\xff'):
            with self.subTest(payload=payload):
                with self.assertRaises(ValueError):
                    presentation_signature(CATALOGS[0], payload)

    def root_intro(self, raw, language):
        pattern = re.compile(rb'(<h3><a href="/numerical-methods-atlas/\?lang=' + language.encode() +
                             rb'">[^<]+</a></h3><p>)([^<]*)(</p>)')
        matches = list(pattern.finditer(raw))
        self.assertEqual(len(matches), 1, "The real root must retain exactly one NaN intro per language")
        return pattern, matches[0]

    def test_real_root_only_the_two_nan_intro_paragraphs_allow_wording(self):
        path = "index.html"
        self.assertEqual(presentation_kind(path), "html")
        before = (ROOT / path).read_bytes()
        self.signature(path, before)
        for language in ("ja", "en"):
            pattern, _ = self.root_intro(before, language)
            after, count = pattern.subn(lambda m: m[1] + m[2] + b" Read the evidence." + m[3], before)
            self.assertEqual(count, 1)
            self.equivalent(path, before, after)
        for old, new in [
            (b"RESEARCH, LEARNING & ARCHIVES", b"OTHER MATERIAL"),
            (b"/numerical-methods-atlas/?lang=ja", b"/other/?lang=ja"),
            (b"/numerical-methods-atlas/assets/particle-gravity.png", b"/other/figure.png"),
            (b'<html lang="ja">', b'<html lang="en">'),
        ]:
            with self.subTest(old=old):
                self.assertIn(old, before)
                self.protected(path, before, before.replace(old, new, 1))

    def test_root_intro_parameters_references_and_active_markup_are_protected(self):
        path = "index.html"
        original = (ROOT / path).read_bytes()
        pattern, _ = self.root_intro(original, "en")
        pairs = [
            (b"Value 1e-8", b"Value 1e-2"),
            (b"See ../code/old.py", b"See ../code/new.py"),
            (b"See https://example.org/old", b"See https://example.org/new"),
            (b"Formula $a+b$", b"Formula $a-b$"),
            (b"Read the evidence", b'<script src="/other.js"></script>'),
            (b"Read the evidence", b'<span onclick="run()">Read</span>'),
            (b"Read the evidence", b'<a href="/code/other.py">Read</a>'),
        ]
        for old, new in pairs:
            before = pattern.sub(lambda m: m[1] + old + m[3], original)
            after = pattern.sub(lambda m: m[1] + new + m[3], original)
            with self.subTest(before=old, after=new):
                self.protected(path, before, after)

    def test_root_intro_html_entities_cannot_hide_changed_numeric_meaning(self):
        original = (ROOT / "index.html").read_bytes()
        pattern, _ = self.root_intro(original, "en")
        for old, new in [
            (b"Threshold &minus;1", b"Threshold &plus;1"),
            (b"Value 1&period;0", b"Value 1&comma;0"),
        ]:
            with self.subTest(before=old, after=new):
                before = pattern.sub(lambda m: m[1] + old + m[3], original)
                after = pattern.sub(lambda m: m[1] + new + m[3], original)
                self.protected("index.html", before, after)

    def test_fake_cache_attributes_and_quoted_attribute_lookalikes_remain_exact(self):
        for path, before in [
            ("numerical-methods-atlas/index.html",
             b'<script data-loader-src="app.js?v=111111111111"></script>'),
            ("numerical-methods-atlas/index.html",
             b'<script data-unknown=\'src="app.js?v=111111111111"\'></script>'),
            ("search/index.html",
             b'<body data-unknown=\'data-search-index="/search/query-index.json?v=111111111111"\'></body>'),
            ("index.html", b'<script data-loader-src="/site.js?v=111111111111"></script>'),
        ]:
            with self.subTest(path=path, before=before):
                after = before.replace(b"111111111111", b"222222222222")
                self.protected(path, before, after)
                self.assertEqual(presentation_cache_references(path, before), [])
                self.assertEqual(presentation_cache_references(path, after), [])

    def test_root_cache_projection_never_hides_url_or_arbitrary_attribute_changes(self):
        path = "index.html"
        before = (ROOT / path).read_bytes()
        for asset in (b"/styles/home.css", b"/site.css", b"/site.js", b"/favicon.svg"):
            pattern = re.compile(rb'((?:src|href)="' + re.escape(asset) + rb'\?v=)([0-9a-f]{12})(")')
            self.assertEqual(len(pattern.findall(before)), 1)
            after = pattern.sub(lambda m: m[1] + b"abcdef012345" + m[3], before)
            with self.subTest(asset=asset):
                self.equivalent(path, before, after)
                self.protected(path, before, after.replace(asset, b"/other/asset", 1))
                self.protected(path, before, after.replace(b"abcdef012345", b"abcdef0123456", 1))
        self.protected(path, before, before.replace(b'<head>', b'<head data-version="abcdef012345">', 1))

    def test_actual_full_search_main_owns_both_query_cache_versions(self):
        path = "search/index.html"
        before = actual_source_bytes(path)
        self.assertEqual(before.count(b'<main class="profile-main search-main"'), 1)
        changed = before
        expected = {}
        for attribute, index, token in [
            (b"data-search-index", b"/search/query-index.json", b"abcdef012345"),
            (b"data-atlas-search-index", b"/search/atlas-query-index.json", b"fedcba543210"),
        ]:
            pattern = re.compile(rb'(' + attribute + rb'="' + re.escape(index) + rb'\?v=)([0-9a-f]{12})(")')
            self.assertEqual(len(pattern.findall(before)), 1)
            after = pattern.sub(lambda m: m[1] + token + m[3], before)
            with self.subTest(attribute=attribute):
                self.equivalent(path, before, after)
            changed = pattern.sub(lambda m: m[1] + token + m[3], changed)
            expected[index.decode().lstrip("/")] = token.decode()
        self.equivalent(path, before, changed)
        query_refs = {row["path"]: row["version"] for row in presentation_cache_references(path, changed)
                      if row["path"] in expected}
        self.assertEqual(query_refs, expected)

    def test_search_main_cache_does_not_hide_unknown_context_attributes_counts_or_urls(self):
        path = "search/index.html"
        before = actual_source_bytes(path)
        query = re.compile(rb'(data-search-index="/search/query-index\.json\?v=)([0-9a-f]{12})(")')
        self.assertEqual(len(query.findall(before)), 1)
        for opening in [
            b'<main class="profile-main search-main extra"',
            b'<main class="other-main"',
            b'<body class="profile-main search-main"',
            b'<div class="profile-main search-main"',
        ]:
            unknown = before.replace(b'<main class="profile-main search-main"', opening, 1)
            changed = query.sub(lambda m: m[1] + b"abcdef012345" + m[3], unknown)
            with self.subTest(opening=opening):
                self.protected(path, unknown, changed)
                self.assertFalse(any(row["path"] in {"search/query-index.json", "search/atlas-query-index.json"}
                                     for row in presentation_cache_references(path, unknown)))
        for attribute in (b"data-search-count", b"data-atlas-search-count"):
            pattern = re.compile(rb'(' + attribute + rb'=")([0-9]+)(")')
            self.assertEqual(len(pattern.findall(before)), 1)
            changed = pattern.sub(lambda m: m[1] + str(int(m[2]) + 1).encode() + m[3], before)
            with self.subTest(attribute=attribute):
                self.protected(path, before, changed)
        self.protected(path, before, before.replace(b"/search/query-index.json?v=", b"/other/query-index.json?v=", 1))
        self.protected(path, before, before.replace(b'<main class="profile-main search-main"',
                       b'<main data-unknown="changed" class="profile-main search-main"', 1))
        for unknown in [
            b'<main class="profile-main search-main" data-loader-data-search-index="/search/query-index.json?v=111111111111"></main>',
            b'<main class="profile-main search-main" data-unknown=\'data-search-index="/search/query-index.json?v=111111111111"\'></main>',
        ]:
            with self.subTest(unknown=unknown):
                changed = unknown.replace(b"111111111111", b"222222222222")
                self.protected(path, unknown, changed)
                self.assertEqual(presentation_cache_references(path, unknown), [])

    def test_handwritten_imports_allow_only_known_twelve_hex_cache_values(self):
        fixtures = {
            "numerical-methods-atlas/home-overview.js": (
                "import {homeLandingCopy,homeCollectionInventory} from './atlas-home-data.js?v=111111111111';\n"
                "import {homeSearchPage,wireHomeSearch} from './home-search.js?v=222222222222';\n"
                "import {t,currentLanguage} from './i18n.js';\n"
                "import {homeAreas,homeCopy,homePaths,homeReadingLanguages} from './home-overview-data.js?v=333333333333';\n"
                "export const choose=()=>true;\n"),
            "numerical-methods-atlas/home-navigation.mjs": (
                "import {homeAreas} from './home-overview-data.js?v=111111111111';\n"
                "import {homeNavigationData} from './atlas-home-data.js?v=222222222222';\n"
                "export const choose=()=>true;\n"),
        }
        for path, text in fixtures.items():
            self.assertEqual(presentation_kind(path), "cache")
            raw = text.encode()
            self.equivalent(path, raw, raw.replace(b"111111111111", b"abcdef012345"))
            for after in [
                raw.replace(b"()=>true", b"()=>false"),
                raw.replace(b"./atlas-home-data.js", b"./other-data.js"),
                raw.replace(b"111111111111", b"abcdef0123456"),
                raw.replace(b"111111111111", b"zzzzzzzzzzzz"),
                raw + b"fetch('/code/other.py');\n",
                raw + b"// v=111111111111\n",
            ]:
                with self.subTest(path=path, after=after):
                    self.protected(path, raw, after)

    def test_scientific_unknown_and_spoofed_paths_never_enter_the_allowlist(self):
        for path in [
            "code/validated-examples/2026-11-25/quantum-small/inputs.json",
            "scripts/verify-depth-public.py", "scripts/atlas_depth_scope.py",
            ".github/workflows/atlas-depth-linux.yml", "catalog/atlas-depth.json",
            "catalog/atlas-registration.json", "catalog/new-home.json",
            "numerical-methods-atlas/validation/releases.json", "frontend/atlas/app.js",
            "numerical-methods-atlas/unknown.js", "numerical-methods-atlas/other/index.html",
            "numerical-methods-atlas/share/other/index.html", "catalog/atlas-home.json/extra",
            "../catalog/atlas-home.json", "/catalog/atlas-home.json", "catalog/ATLAS-HOME.json",
            "catalog/atlas-home.json.zip", "downloads/example.zip", "new/science.txt",
        ]:
            with self.subTest(path=path):
                self.assertIsNone(presentation_kind(path))
                with self.assertRaises(ValueError):
                    presentation_signature(path, b"{}")

    def test_generated_classification_alone_cannot_authorize_a_payload(self):
        for path, raw in [
            ("numerical-methods-atlas/app.js", b"const reference=2;"),
            ("numerical-methods-atlas/atlas-runtime-data.mjs", b"export const tolerance=0.1;"),
            ("search/index.json", b'{"reference":2}'),
            ("numerical-methods-atlas/share/index.html", b"<p>Other scientific scope</p>"),
        ]:
            with self.subTest(path=path):
                self.assertEqual(presentation_kind(path), "derived")
                with self.assertRaises(ValueError):
                    presentation_signature(path, raw)

    def test_size_and_payload_type_limits_fail_closed(self):
        value = catalog(CATALOGS[0])
        value["landing"]["en"]["description"] = "x" * (1024 * 1024 + 1)
        for path, payload in [(CATALOGS[0], encode(value)), ("index.html", b"x" * (1024 * 1024 + 1))]:
            with self.subTest(path=path):
                with self.assertRaises(ValueError):
                    presentation_signature(path, payload)
        for payload in (None, "{}", bytearray(b"{}")):
            with self.subTest(payload_type=type(payload).__name__):
                with self.assertRaises(ValueError):
                    presentation_signature(CATALOGS[0], payload)


if __name__ == "__main__":
    unittest.main()
