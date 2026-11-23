"""Render browser search assets from editable templates, never patch their logic."""
import hashlib
import json
from pathlib import Path
import re

OUTPUTS = {
    'search/compact-index.mjs': 'compact-index.mjs',
    'search/navigation.mjs': 'navigation.mjs',
    'search/method-search.mjs': 'method-search.mjs',
    'search/engine.mjs': 'engine.mjs',
    'numerical-methods-atlas/home-search.js': 'home-search.js',
    'search/search.js': 'search.js',
}
TOKEN = re.compile(r'\{\{asset:([a-zA-Z0-9_./-]+)\}\}')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def render_templates(root, templates, generator='scripts/search_assets.py'):
    root = Path(root)
    rows, visiting, built = [], set(), {}

    def render(output):
        if output in built:
            return built[output]
        if output in visiting:
            raise ValueError('Cyclic search asset dependency: '+output)
        visiting.add(output)
        source = templates[output]
        template = (root/source).read_text()
        dependencies = {}

        def version(match):
            name = match[1]
            if name.startswith('/') or '..' in Path(name).parts:
                raise ValueError('Unsafe search asset dependency: '+name)
            value = render(name) if name in templates else digest(root/name)
            dependencies[name] = value
            return value[:12]

        text = '// Generated from '+source+' by '+generator+'. Edit the source template.\n'+TOKEN.sub(version, template)
        if '{{asset:' in text:
            raise ValueError('Invalid search asset token in '+source)
        path = root/output
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        built[output] = digest(path)
        rows.append({'source': source, 'output': output, 'source_sha256': digest(root/source),
                     'sha256': built[output], 'dependencies': dict(sorted(dependencies.items()))})
        visiting.remove(output)
        return built[output]

    for output in templates:
        render(output)
    return rows, built


def build_search_assets(root, page=True):
    root = Path(root)
    rows, built = render_templates(root, {output:'frontend/search/'+name for output,name in OUTPUTS.items()})
    # These parents own their UI logic. Only the declared import cache version
    # and HTML data attributes are configuration outputs of this renderer.
    parent = root/'numerical-methods-atlas/home-overview.js'
    text, count = re.subn(r"(from './home-search[.]js)(?:[?]v=[a-f0-9]+)?(')",
                         r'\1?v='+built['numerical-methods-atlas/home-search.js'][:12]+r'\2', parent.read_text())
    if count != 1:
        raise ValueError('Expected the declared home-search import in home-overview.js')
    parent.write_text(text)
    if page:
        target = root/'search/index.html'
        text = target.read_text()
        for name in ['search.js', 'search.css']:
            text, count = re.subn(r'(/search/'+re.escape(name)+r')(?:\?v=[a-f0-9]+)?',
                                 r'\1?v='+digest(root/'search'/name)[:12], text)
            if count != 1:
                raise ValueError('Expected one search-page asset: '+name)
        text = re.sub(r'\sdata-atlas-search-index="[^"]*"|\sdata-search-count="[^"]*"|\sdata-atlas-search-count="[^"]*"', '', text)
        home = root/'search/atlas-query-index.json'
        site = root/'search/query-index.json'
        counts = (len(json.loads(home.read_text())['entries']), len(json.loads(site.read_text())['documents']))
        attrs = ('data-atlas-search-index="/search/atlas-query-index.json?v='+digest(home)[:12]+
                 '" data-search-count="'+str(counts[1])+'" data-atlas-search-count="'+str(counts[0])+
                 '" data-search-index="/search/query-index.json?v='+digest(site)[:12]+'"')
        text, count = re.subn(r'data-search-index="[^"]*"', lambda _: attrs, text)
        if count != 1:
            raise ValueError('Expected one search-page index configuration')
        target.write_text(text)
    manifest = {'schema_version': 1, 'generator': 'scripts/search_assets.py',
                'modules': sorted(rows, key=lambda row: row['output']),
                'configuration_consumers': ['numerical-methods-atlas/home-overview.js', 'search/index.html']}
    (root/'search/asset-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    return manifest
