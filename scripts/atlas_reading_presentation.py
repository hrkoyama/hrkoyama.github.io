"""Run historical body checks on original bytes, retaining the input layout.

The navigation generator owns the reversible presentation transform. Reuse its
pure functions without invoking navigation/index generation or changing prose.
"""
from functools import lru_cache
import importlib.util
from pathlib import Path


@lru_cache(maxsize=1)
def _navigation():
    path = Path(__file__).with_name('build-atlas-reading-navigation.py')
    spec = importlib.util.spec_from_file_location('_reading_presentation_navigation', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def original_reading_document(document):
    opening_first = 'data-reading-layout="opening-first"' in document
    return (_navigation().restore_legacy_article(document) if opening_first else document), opening_first


def retain_reading_presentation(document, opening_first):
    return _navigation().legacy_reading_layout(document) if opening_first else document


def specialized_reading_layout(nav, toc, body, opening, language, *, plain_toc=False):
    """Move the captured title/lead/scope ahead of existing reading utilities."""
    if language not in ('ja', 'en') or not opening or not body.startswith(opening):
        raise ValueError('Expected the original captured reading opening')
    if not opening.startswith('<h1>') or not opening.endswith('</aside>'):
        raise ValueError('Expected the title, introduction and visible scientific scope')
    if '<!-- chapter-resource-position -->' in body:
        raise ValueError('Reading body already has an opening boundary')
    parent_label = '解説章の目次' if language == 'ja' else 'Reading contents'
    parent = '<a href="/numerical-methods-atlas/' + language + '/read/">' + parent_label + '</a>'
    nav_prefix = '<nav class="resource-nav">' + parent + ' · '
    if not nav.startswith(nav_prefix) or not nav.endswith('</nav>'):
        raise ValueError('Expected the existing parent and resource navigation')
    resources = '<nav class="resource-nav">' + nav[len(nav_prefix):]
    toc_label = 'この章の目次' if language == 'ja' else 'On this page'
    if plain_toc:
        if not toc.startswith('<nav aria-label="' + toc_label + '">') or not toc.endswith('</nav>') or '<details' in toc:
            raise ValueError('Expected the original plain chapter contents')
        toc = '<details class="specialized-reading-toc"><summary>' + toc_label + '</summary>' + toc + '</details>'
    elif not toc.startswith('<details class="periodic-toc">') or not toc.endswith('</details>'):
        raise ValueError('Expected the existing closed periodic contents')
    return ('<nav class="prose specialized-reading-parent">' + parent + '</nav>'
            '<div class="prose specialized-reading-opening" data-chapter-opening lang="' + language + '">' + opening + '</div>'
            '<!-- chapter-resource-position -->'
            '<div class="prose specialized-reading-tools">' + resources + toc + '</div>'
            '<article class="prose" lang="' + language + '">' + body[len(opening):] + '</article>')
