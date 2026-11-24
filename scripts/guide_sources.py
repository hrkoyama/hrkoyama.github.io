"""Bound guide chapters to the reviewed reading catalog, independent of its size."""
import json
from pathlib import Path
import re
ORIGIN = 'https://hrkoyama.github.io'
BASE = '/numerical-methods-atlas/'


def reading_source_urls(root):
    root = Path(root)
    data = json.loads((root/'catalog/atlas-reading-index.json').read_text())
    ids = [ident for group in data['groups'] for ident in group['chapters']]
    if not ids or len(ids) != len(set(ids)) or any(not re.fullmatch(r'[a-z0-9]+(?:[.-][a-z0-9]+)*', ident) for ident in ids):
        raise ValueError('Invalid or repeated reviewed reading identity')
    urls = set()
    for ident in ids:
        editions = [lang for lang in ['ja', 'en']
                    if (root/BASE.lstrip('/')/lang/'read'/ident/'index.html').is_file()]
        if not editions:
            raise ValueError('Missing reviewed reading edition: '+ident)
        urls.update(ORIGIN+BASE+lang+'/read/'+ident+'/' for lang in editions)
    return urls


def validate_reading_source_urls(actual, reviewed):
    actual = set(actual)
    if actual != reviewed:
        raise ValueError('Reading sitemap must match reviewed catalog editions: missing='
                         +str(sorted(reviewed-actual))+'; extra='+str(sorted(actual-reviewed)))
