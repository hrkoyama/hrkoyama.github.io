"""Shared, static entrances to the atlas's cross-field connections."""
import hashlib
import json
from html import escape


BASE = '/numerical-methods-atlas/connections/'


def crossover_assets(root, interactive=False):
    """Return content-versioned assets; homepage cards need only the stylesheet."""
    css = '/styles/atlas-crossovers.css'
    version = hashlib.sha256((root / css.lstrip('/')).read_bytes()).hexdigest()[:12]
    assets = '<link rel="stylesheet" href="' + css + '?v=' + version + '">'
    if interactive:
        script = '/numerical-methods-atlas/crossovers.mjs'
        version = hashlib.sha256((root / script.lstrip('/')).read_bytes()).hexdigest()[:12]
        assets += '<script type="module" src="' + script + '?v=' + version + '"></script>'
    return assets


def crossover_teaser(root, lang):
    """Render three direct, bilingual path entrances without inferring validation."""
    data = json.loads((root / 'catalog/atlas-crossovers.json').read_text())
    ja = lang == 'ja'
    heading = data.get('home', {}).get('title', data['title'])[lang]
    intro = data.get('home', {}).get('description', data['intro'])[lang]
    body = '<aside class="atlas-crossover-teaser"><h2>' + heading + '</h2><p>' + intro + '</p><div class="crossover-teaser-grid">'
    for route in data['routes']:
        url = BASE + '?lang=' + lang + '#' + route['id'] + '-' + lang
        body += '<article><h3><a href="' + escape(url, quote=True) + '">' + escape(route['title'][lang]) + '</a></h3><p>' + escape(route.get('teaser', route['summary'])[lang]) + '</p></article>'
    action = data.get('home', {}).get('action', {'ja': '分野をつなぐ入口へ', 'en': 'Explore the crossovers'})[lang]
    body += '</div><p><a href="' + BASE + '?lang=' + lang + '">' + escape(action) + '</a></p><p class="crossover-teaser-note">' + ('個々の実行例と、分野間を連成した計算の検証を区別して表示します。' if ja else 'Component execution examples and validation of a coupled calculation are shown separately.') + '</p></aside>'
    return body
