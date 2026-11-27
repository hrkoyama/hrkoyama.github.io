"""Small, closed presentation proofs for the public numerical-Linux selector.

This module does not authorize reuse on its own.  The caller must prove a
complete ancestral diff, regular-file modes, a real successful full baseline,
and successful *same-SHA* Public site checks with the unchanged strict
``prepare-indexes.py --check`` pipeline.  Every other changed authoritative
source, scientific input/reference/criterion, distribution and verifier is FULL.

Ownership was checked against build-atlas-purpose.py, atlas_runtime_assets.py,
atlas_home_layout.py, build-atlas-sharing.py, build-atlas-search.py,
build-search.py, search_assets.py and prepare-indexes.py.  The finite generated
paths below are entirely rewritten by those generators.  In contrast,
home-overview.js, home-navigation.mjs, the SPA shell and search/index.html retain
handwritten source: only explicitly named copy/cache slots may differ there.
No PNG, SVG, scientific manifest, source bundle or ZIP is admitted here.
"""
from __future__ import annotations

import hashlib
from html import unescape
from html.parser import HTMLParser
import json
import math
import re


MAX_PRESENTATION_BYTES = 1024 * 1024
PRESENTATION_SOURCE_PATHS = frozenset({
    "catalog/atlas-home.json", "catalog/atlas-purpose.json",
    "catalog/atlas-sharing.json", "index.html",
})
CATALOG_PRESENTATION_PATHS = PRESENTATION_SOURCE_PATHS - {"index.html"}

# Explicit ownership, rather than an extension/directory-wide JS/JSON exemption.
# These paths still require the caller's exact-SHA freshness/owner proof.  A
# signature alone deliberately cannot approve any member of this set.
GENERATED_PRESENTATION_OWNERS = {
    "numerical-methods-atlas/app.js": "scripts/atlas_runtime_assets.py",
    "numerical-methods-atlas/atlas-runtime-data.mjs": "scripts/atlas_runtime_assets.py",
    "numerical-methods-atlas/runtime-asset-manifest.json": "scripts/atlas_runtime_assets.py",
    "numerical-methods-atlas/atlas-home-data.js": "scripts/build-atlas-purpose.py",
    "numerical-methods-atlas/atlas-purpose.js": "scripts/build-atlas-purpose.py",
    "numerical-methods-atlas/explore/index.html": "scripts/atlas_home_layout.py",
    "numerical-methods-atlas/home-search.js": "scripts/search_assets.py",
    "numerical-methods-atlas/home-search-index.json": "scripts/build-atlas-search.py",
    "search/atlas-navigation.json": "scripts/build-atlas-search.py",
    "search/atlas-query-index.json": "scripts/build-atlas-search.py",
    "search/index.json": "scripts/build-search.py",
    "search/query-index.json": "scripts/build-search.py",
    "search/asset-manifest.json": "scripts/search_assets.py",
    "search/detail-references.json": "scripts/compact_search.py",
    "search/atlas-detail-references.json": "scripts/compact_search.py",
    **{"numerical-methods-atlas/share/" + name: "scripts/build-atlas-sharing.py"
       for name in (
           "index.html", "ja/index.html", "en/index.html", "sharing.json", "build.json",
           "atlas-intro-ja.txt", "atlas-intro-en.txt",
           "atlas-intro-short-ja.txt", "atlas-intro-short-en.txt",
           "atlas-intro-paragraph-ja.txt", "atlas-intro-paragraph-en.txt",
       )},
}
GENERATED_PRESENTATION_PATHS = frozenset(GENERATED_PRESENTATION_OWNERS)

# The normalizer accepts only a complete static import line with an existing
# 12-lowercase-hex version, once per declared import.  Logic, imported names,
# module paths, query keys and every byte outside those version digits remain.
CACHE_IMPORTS = {
    "numerical-methods-atlas/home-overview.js": {
        "./atlas-home-data.js": "numerical-methods-atlas/atlas-home-data.js",
        "./home-search.js": "numerical-methods-atlas/home-search.js",
        "./home-overview-data.js": "numerical-methods-atlas/home-overview-data.js",
    },
    "numerical-methods-atlas/home-navigation.mjs": {
        "./home-overview-data.js": "numerical-methods-atlas/home-overview-data.js",
        "./atlas-home-data.js": "numerical-methods-atlas/atlas-home-data.js",
    },
}

_COMMON_HTML_CACHE = {
    "/site.css": "site.css", "/site.js": "site.js", "/favicon.svg": "favicon.svg",
}
HTML_CACHE_ASSETS = {
    "index.html": {**_COMMON_HTML_CACHE, "/styles/home.css": "styles/home.css"},
    "numerical-methods-atlas/index.html": {
        **_COMMON_HTML_CACHE,
        "app.js": "numerical-methods-atlas/app.js",
        "home-overview.css": "numerical-methods-atlas/home-overview.css",
        **{"/styles/" + name: "styles/" + name for name in (
            "atlas-goal-filters.css", "atlas-depth.css", "atlas-crossovers.css",
            "atlas-validation.css", "atlas-purpose.css", "atlas-discovery.css",
            "atlas-home-shell.css",
        )},
        "/numerical-methods-atlas/goal-filters.mjs": "numerical-methods-atlas/goal-filters.mjs",
        "/numerical-methods-atlas/styles/atlas-execution-navigation.css": "numerical-methods-atlas/styles/atlas-execution-navigation.css",
        "/numerical-methods-atlas/wave-evolution.css": "numerical-methods-atlas/wave-evolution.css",
    },
    "search/index.html": {
        **_COMMON_HTML_CACHE,
        "/search/search.css": "search/search.css", "/search/search.js": "search/search.js",
        "/search/query-index.json": "search/query-index.json",
        "/search/atlas-query-index.json": "search/atlas-query-index.json",
    },
}

_NUMBER = re.compile(r"[+-]?(?:(?:\d+\.\d*|\.\d+|\d+)(?:[eE][+-]?\d+)?)")
_REFERENCE = re.compile(
    r"[A-Za-z][A-Za-z0-9+.-]*:[^\s<>\"'`]+"
    r"|!?\[[^\]\n]*\]\([^\n)]*\)"
    r"|\[[^\]\n]+\]:[^\n]*"
    r"|(?:^|(?<=[\s(]))(?:\.{0,2}/)[^\s<>\"'`),;]+"
    r"|(?<![\w/])(?:[\w.@+-]+/)+[\w.@+%#?=&:/-]+"
    r"|(?<!\w)[\w.-]+\.(?:py|mjs|js|json|csv|txt|md|zip|npz|npy|toml|ya?ml|xml|f90|cpp|h|dat|h5|hdf5|nc)(?!\w)",
    re.I,
)
_PLACEHOLDER = re.compile(r"\{[^{}\n]*\}")
_ENTITY = re.compile(r"&(?:#[xX][0-9a-fA-F]+|#\d+|[A-Za-z][A-Za-z0-9]*);?")
# When a designated intro string itself contains code/formula syntax, keep the
# whole string exact instead of attempting to decide which symbols are prose.
_CODE_OR_FORMULA = re.compile(r"[`$<>=≤≥≠≈±×÷∂∇∫∑√]|\\(?:[A-Za-z]+|[()[\]])|\[[^\]\n]+\]\[[^\]\n]*\]")
_COMMAND_OR_EXPRESSION = re.compile(
    r"\b(?:python[23]?|node|bash|sh|make|cmake|pytest|pip[3]?|curl|wget|gcc|gfortran)\s+[-/\w.]"
    r"|--[A-Za-z][A-Za-z0-9_-]*"
    r"|\b[A-Za-z_]\w*\([^\n)]*\)"
    r"|\b[A-Za-z]\w*\s*[+*^]\s*[A-Za-z]\w*\b"
    r"|\b[A-Za-z]\s*-\s*[A-Za-z]\b|\b[A-Za-z]_[A-Za-z0-9]+\b"
    r"|[α-ωΑ-Ω]"
)
_PROTECTED_HTML = frozenset({
    "script", "style", "pre", "code", "textarea", "option", "template", "title", "svg", "math",
    "xmp", "plaintext", "noscript", "iframe", "noembed", "noframes",
})


def _require(value, reason):
    if not value:
        raise ValueError(reason)


def _digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def _decode(raw):
    _require(isinstance(raw, bytes) and len(raw) <= MAX_PRESENTATION_BYTES,
             "presentation-file-budget-exceeded")
    text = raw.decode("utf-8")
    _require(not any(ord(c) < 32 and c not in "\n\r\t" for c in text),
             "presentation-control-character")
    return text


def _strict_json(text):
    def pairs(rows):
        result = {}
        for key, item in rows:
            _require(key not in result, "duplicate-json-key")
            result[key] = item
        return result
    def floating(value):
        result = float(value)
        _require(math.isfinite(result), "nonfinite-json-number")
        return result
    def constant(_):
        raise ValueError("nonfinite-json-number")
    return json.loads(text, object_pairs_hook=pairs, parse_float=floating, parse_constant=constant)


def _prose(value):
    decoded = unescape(value)
    if _ENTITY.search(value) or _CODE_OR_FORMULA.search(decoded) or _COMMAND_OR_EXPRESSION.search(decoded):
        return ["exact-intro", value]
    return ["intro", _NUMBER.findall(value), _REFERENCE.findall(value), _PLACEHOLDER.findall(value)]


def prose_value_signature(value):
    """Share the strict protected prose projection with legacy copy selectors."""
    _require(isinstance(value, str), "invalid-presentation-prose-value")
    _decode(value.encode("utf-8"))
    return _digest(_prose(value))


def _copy_slot(path, keys):
    if path == "catalog/atlas-home.json":
        return (len(keys) == 3 and keys[:1] == ("landing",) and keys[1] in {"ja", "en"}
                and keys[2] in {"title", "description"}) or (
            len(keys) == 4 and keys[0] == "landing" and keys[1] in {"ja", "en"}
            and keys[2] == "introduction" and keys[3] in {
                "why", "connections", "ways", "ai", "feedback", "details_title"})
    if path == "catalog/atlas-purpose.json":
        return (len(keys) == 2 and keys[0] in {"ja", "en"}
                and keys[1] in {"title", "meta_description"}) or (
            len(keys) == 3 and keys[0] in {"ja", "en"} and keys[1] == "paragraphs"
            and type(keys[2]) is int)
    if path == "catalog/atlas-sharing.json":
        return len(keys) == 3 and keys[0] == "copy" and keys[1] in {"ja", "en"} and keys[2] in {
            "title", "headline", "lead", "short", "paragraph", "description"}
    return False


def _catalog(path, text):
    def project(value, keys=()):
        if isinstance(value, dict):
            return ["object", [[key, project(item, keys + (key,))] for key, item in sorted(value.items())]]
        if isinstance(value, list):
            return ["array", [project(item, keys + (index,)) for index, item in enumerate(value)]]
        if isinstance(value, str) and _copy_slot(path, keys):
            return _prose(value)
        return [type(value).__name__, value]
    value = _strict_json(text)
    _require(isinstance(value, dict), "invalid-presentation-catalog")
    return _digest(project(value))


def _import_versions(path, text):
    references = []
    for source, target in CACHE_IMPORTS[path].items():
        pattern = re.compile(r"(?m)^(import [^\n;]+ from '" + re.escape(source) + r"\?v=)([0-9a-f]{12})(';)$")
        matches = list(pattern.finditer(text))
        _require(len(matches) == 1, "missing-or-ambiguous-cache-import")
        references.append({"path": target, "version": matches[0][2]})
        text = pattern.sub(lambda match: match[1] + "<cache-version>" + match[3], text)
    return text, references


def _attribute_spans(token):
    """Lex actual attribute values without matching names inside quoted values.

    Malformed syntax has no proof.  In particular a suffix
    such as data-loader-src and a quoted string containing src= are not src.
    """
    _require(len(token) <= 16384, "presentation-tag-budget-exceeded")
    start = re.match(r'<[A-Za-z][A-Za-z0-9:-]*', token)
    if not start:
        raise ValueError("invalid-presentation-attribute-syntax")
    position, result = start.end(), []
    while position < len(token):
        _require(len(result) <= 128, "presentation-attribute-budget-exceeded")
        whitespace = re.match(r'\s*', token[position:])[0]
        position += len(whitespace)
        if token[position:] in {">", "/>"}:
            return result
        if not whitespace:
            raise ValueError("invalid-presentation-attribute-syntax")
        name = re.match(r'[A-Za-z_:][A-Za-z0-9_.:-]*', token[position:])
        if not name:
            raise ValueError("invalid-presentation-attribute-syntax")
        attribute = name[0].lower()
        position += len(name[0])
        name_end = position
        position += len(re.match(r'\s*', token[position:])[0])
        if position >= len(token):
            raise ValueError("invalid-presentation-attribute-syntax")
        if token[position] != "=":
            # A boolean attribute ends at its name; whitespace belongs to the
            # next iteration and must not be accidentally consumed here.
            position = name_end
            result.append((attribute, None, None))
            continue
        position += 1
        position += len(re.match(r'\s*', token[position:])[0])
        if position >= len(token):
            raise ValueError("invalid-presentation-attribute-syntax")
        if token[position] in {'"', "'"}:
            quote = token[position]
            left = position + 1
            right = token.find(quote, left)
            if right < 0:
                raise ValueError("invalid-presentation-attribute-syntax")
            result.append((attribute, left, right))
            position = right + 1
        else:
            unquoted = re.match(r'[^\s<>"\'=]+', token[position:])
            if not unquoted:
                raise ValueError("invalid-presentation-attribute-syntax")
            position += len(unquoted[0])
            result.append((attribute, None, None))
    raise ValueError("invalid-presentation-attribute-syntax")


def _unique_attributes(token):
    attributes = _attribute_spans(token)
    _require(len({row[0] for row in attributes}) == len(attributes),
             "duplicate-presentation-attribute")
    return attributes


def _copy_attributes(token, names, attributes=None):
    """Project only actual selected value spans, preserving all other bytes."""
    attributes = _unique_attributes(token) if attributes is None else attributes
    for attribute, left, right in reversed(attributes):
        if attribute in names:
            _require(left is not None, "unquoted-presentation-copy-attribute")
            token = token[:left] + "\x00intro:" + _digest(_prose(token[left:right])) + "\x00" + token[right:]
    return token


def _html_versions(path, text):
    references = []
    # Only real link/script tags and the exact search-main configuration own
    # cache attributes. Body attributes and arbitrary main elements stay exact;
    # strings in inline code, text, comments and download links stay exact.
    def tag(name, token):
        attributes = _unique_attributes(token)
        allowed = {"link": {"href"}, "script": {"src"},
                   "main": set()}[name]
        if name == "main" and path == "search/index.html":
            values = {attribute: token[left:right] if left is not None else None
                      for attribute, left, right in attributes}
            if values.get("class") == "profile-main search-main":
                allowed = {"data-search-index", "data-atlas-search-index"}
        replacements = []
        for attribute, left, right in attributes:
            if attribute not in allowed or left is None:
                continue
            value = token[left:right]
            for source, target in HTML_CACHE_ASSETS[path].items():
                match = re.fullmatch(re.escape(source) + r'\?v=([0-9a-f]{12})', value)
                if match:
                    references.append({"path": target, "version": match[1]})
                    replacements.append((left + match.start(1), left + match.end(1)))
        for left, right in reversed(replacements):
            token = token[:left] + "<cache-version>" + token[right:]
        return token
    class Tags(HTMLParser):
        # HTMLParser retains script/style bodies as data.  Do not accidentally
        # normalize a string such as '<link href="...?v=...">' inside code.
        def __init__(self):
            super().__init__(convert_charrefs=False)
            self.rows = []
            self.protected = []
            self.offsets = [0]
            for found in re.finditer("\n", text):
                self.offsets.append(found.end())
        def handle_starttag(self, name, attrs):
            if not self.protected and name in {"link", "script", "main"}:
                line, column = self.getpos()
                start = self.offsets[line - 1] + column
                self.rows.append((name, start, start + len(self.get_starttag_text())))
            if name in _PROTECTED_HTML:
                _require(len(self.protected) < 128, "presentation-nesting-budget-exceeded")
                self.protected.append(name)
        def handle_startendtag(self, name, attrs):
            # A slash does not close HTML raw-text elements (e.g. plaintext/).
            # Keeping foreign self-closing math/svg protected is conservative.
            self.handle_starttag(name, attrs)
        def handle_endtag(self, name):
            if "plaintext" in self.protected:
                return
            if name in self.protected:
                self.protected = self.protected[:len(self.protected) - 1 - self.protected[::-1].index(name)]
    parser = Tags()
    parser.feed(text)
    parser.close()
    for name, start, end in reversed(parser.rows):
        text = text[:start] + tag(name, text[start:end]) + text[end:]
    return text, sorted(references, key=lambda row: (row["path"], row["version"]))


def _plain_slot(match):
    return match[1] + "\x00intro:" + _digest(_prose(match[2])) + "\x00" + match[3]


def _sub_html_slots(pattern, replace, text):
    """Replace actual markup slots, never lookalikes in code or comments."""
    class Starts(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=False)
            self.starts, self.protected, self.offsets = set(), [], [0]
            for found in re.finditer("\n", text):
                self.offsets.append(found.end())
        def handle_starttag(self, name, attrs):
            if not self.protected:
                line, column = self.getpos()
                self.starts.add(self.offsets[line - 1] + column)
            if name in _PROTECTED_HTML:
                _require(len(self.protected) < 128, "presentation-nesting-budget-exceeded")
                self.protected.append(name)
        def handle_startendtag(self, name, attrs):
            self.handle_starttag(name, attrs)
        def handle_endtag(self, name):
            if "plaintext" in self.protected:
                return
            if name in self.protected:
                self.protected = self.protected[:len(self.protected) - 1 - self.protected[::-1].index(name)]
    parser = Starts()
    parser.feed(text)
    parser.close()
    return re.sub(pattern, lambda match: replace(match) if match.start() in parser.starts else match[0], text)


def _html(path, text):
    text, _ = _html_versions(path, text)
    if path == "index.html":
        # The first paragraph of the two existing NaN cards, not other projects,
        # resource notes, headings, navigation or arbitrary paragraphs.
        pattern = re.compile(
            r'(<div class="home-feature-copy"><h3><a href="/numerical-methods-atlas/\?lang=(?:ja|en)">[^<>]*</a></h3><p>)([^<>]*)(</p>)')
        text = _sub_html_slots(pattern, _plain_slot, text)
    elif path == "numerical-methods-atlas/index.html":
        patterns = (
            r'(<h1 id="home-landing-title-(?:ja|en)">)([^<>]*)(</h1>)',
            r'(<p class="landing-description">)([^<>]*)(</p>)',
            r'(<p class="landing-connections" data-home-purpose="connections">)([^<>]*)(</p>)',
            r'(<p class="page-width landing-ways">)([^<>]*)(</p>)',
            r'(<p data-home-purpose="(?:why|ai)">)([^<>]*)(</p>)',
            r'(<summary id="home-about-title-(?:ja|en)">)([^<>]*)(</summary>)',
            r'(<div class="page-width landing-feedback"><p>)([^<>]*)(</p></div>)',
        )
        for pattern in patterns:
            text = _sub_html_slots(pattern, _plain_slot, text)
        # Only title/description metadata, never image URLs, robots, counts,
        # canonical URLs, arbitrary data attributes or scientific parameters.
        def meta(match):
            token = match[0]
            attrs = _unique_attributes(token)
            values = {name: token[left:right] if left is not None else None for name, left, right in attrs}
            if values.get("name") == "description":
                names = {"content", "data-description-ja", "data-description-en"}
            elif values.get("name") in {"twitter:title", "twitter:description"} or values.get("property") in {"og:title", "og:description"}:
                names = {"content"}
            else:
                return token
            return _copy_attributes(token, names, attrs)
        text = _sub_html_slots(r'<meta\b[^<>]*>', meta, text)
        def title(match):
            opening = _copy_attributes(match[1], {"data-page-title-ja", "data-page-title-en"})
            return opening + "\x00intro:" + _digest(_prose(match[2])) + "\x00" + match[3]
        text = _sub_html_slots(r'(<title\b[^<>]*>)([^<>]*)(</title>)', title, text)
    return _digest(text)


def presentation_kind(path):
    """Return a finite proof category; unknown files remain FULL in the caller."""
    if not isinstance(path, str):
        return None
    if path in CATALOG_PRESENTATION_PATHS:
        return "catalog"
    if path in CACHE_IMPORTS:
        return "cache"
    if path in HTML_CACHE_ASSETS:
        return "html"
    if path in GENERATED_PRESENTATION_PATHS:
        return "derived"
    return None


def presentation_signature(path, raw):
    """Hash the protected projection, or raise when no bounded proof is defined."""
    kind = presentation_kind(path)
    _require(kind in {"catalog", "html", "cache"}, "unsupported-presentation-signature")
    text = _decode(raw)
    if kind == "catalog":
        return _catalog(path, text)
    if kind == "html":
        return _html(path, text)
    return _digest(_import_versions(path, text)[0])


def presentation_cache_references(path, raw):
    """Return exact declared cache dependencies for the caller's provenance proof."""
    text = _decode(raw)
    if path in CACHE_IMPORTS:
        return _import_versions(path, text)[1]
    if path in HTML_CACHE_ASSETS:
        return _html_versions(path, text)[1]
    raise ValueError("unsupported-presentation-cache-owner")


def cache_validation_group(path, dependency):
    """Name the exact source bytes that determine a declared cache token.

    site-chrome.mjs intentionally hashes site.css || site.js into their shared
    version.  Other admitted cache owners use a single dependency's SHA-256.
    The caller still requires a changed, independently safe group member and
    unchanged strict same-SHA generation; this is not a new source allowlist.
    """
    if path in HTML_CACHE_ASSETS and dependency in HTML_CACHE_ASSETS[path].values():
        if dependency in {"site.css", "site.js"}:
            return ("site.css", "site.js")
        return (dependency,)
    if path in CACHE_IMPORTS and dependency in CACHE_IMPORTS[path].values():
        return (dependency,)
    raise ValueError("unsupported-presentation-cache-dependency")
