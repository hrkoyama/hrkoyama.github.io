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
