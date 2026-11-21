#!/usr/bin/env python3
"""Offline release checks for public links, source receipts and generated indexes."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse, unquote
import hashlib
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://hrkoyama.github.io'
subprocess.run([sys.executable, str(ROOT / 'scripts/check-notebook-material-links.py')], cwd=ROOT, check=True)
errors = []
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def local(url):
    path = (ROOT / unquote(urlparse(url).path).lstrip('/')).resolve()
    if not path.is_relative_to(ROOT): raise ValueError('Path outside public tree: ' + url)
    return path / 'index.html' if path.is_dir() else path
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.canonical = []; self.ids = set()
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.links.extend(a[k] for k in ['href', 'src', 'poster'] if a.get(k))
        if a.get('id'): self.ids.add(a['id'])
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical.append(a.get('href'))

pages = {}; canonicals = set(); link_count = 0
for parent, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in {'node_modules', 'scripts', 'docs'}]
    for name in files:
        if not name.endswith('.html') or name.startswith('google'): continue
        path = Path(parent) / name; relative = path.relative_to(ROOT).as_posix()
        text = path.read_text(); page = Page(); page.feed(text); pages[path.resolve()] = page
        if len(page.canonical) != 1: errors.append(relative + ': expected one canonical URL')
        else: canonicals.add(page.canonical[0])
        if any(text.count('<!-- ' + marker + ' -->') != 1 for marker in ['site-head', 'site-top', 'site-bottom']): errors.append(relative + ': missing or duplicate shared navigation')
        if '/using/' not in text: errors.append(relative + ': missing usage/citation link')
        if re.search(r'koyam(?:arium|ahr)@gmail\.com', text, re.I): errors.append(relative + ': maintainer email restored')
        for href in page.links:
            u = urlparse(urljoin(ORIGIN + '/' + relative, href))
            if u.scheme not in ['https', 'http']: continue
            if u.netloc == 'koyamarium.github.io': errors.append(relative + ': retired site link: ' + href)
            if relative.startswith('the-art-of-thermal-instability/') and u.netloc == 'github.com' and u.path.startswith('/koyamarium/the-art-of-thermal-instability'): errors.append(relative + ': private source dependency: ' + href)
            if relative.startswith('numerical-methods-atlas/') and u.netloc == 'github.com' and re.match(r'/koyamarium/(numerical-methods-atlas|the-art-of-numerical-algorithms)(/|$)', u.path): errors.append(relative + ': private numerical source dependency: ' + href)
            if u.netloc != 'hrkoyama.github.io': continue
            link_count += 1
            if not local(u.geturl()).is_file(): errors.append(relative + ': missing public target: ' + href)

sitemap = [e.text for e in ET.parse(ROOT / 'sitemap.xml').findall('.//{*}loc')]
if len(sitemap) != len(set(sitemap)): errors.append('Duplicate root sitemap URL')
if set(sitemap) != canonicals: errors.append('Root sitemap differs from published canonical pages')
for url in sitemap:
    if not url.startswith(ORIGIN + '/') or not local(url).is_file(): errors.append('Invalid sitemap target: ' + url)

guide = json.loads((ROOT / 'guide/index.json').read_text())
for source in guide['pages']:
    path = local(source['url'])
    if digest(path) != source['sha256']: errors.append('Stale Research Compass source: ' + source['url'])
for record in guide['records']:
    path = local(record['url']); fragment = unquote(urlparse(record['url']).fragment)
    if not path.is_file() or (fragment and fragment not in pages[path.resolve()].ids): errors.append('Invalid Research Compass citation: ' + record['url'])

search = json.loads((ROOT / 'search/index.json').read_text())
if not search.get('sourceSha256'): errors.append('Search freshness receipts missing; run refresh-site.py')
for relative, expected in search.get('sourceSha256', {}).items():
    path = ROOT / relative
    if not path.is_file() or digest(path) != expected: errors.append('Stale site search input: ' + relative)

manifest = json.loads((ROOT / 'notebooks/public-manifest.json').read_text())
for entry in manifest['files']:
    path = ROOT / 'notebooks' / entry['path']
    if not path.is_file() or path.stat().st_size != entry['bytes'] or digest(path) != entry['sha256']: errors.append('Notebook viewing asset differs: ' + entry['path'])
for name, project in json.loads((ROOT / 'research-imports.json').read_text())['projects'].items():
    for relative, expected in project['binarySha256'].items():
        if digest(ROOT / name / relative) != expected: errors.append('Reviewed research asset differs: ' + name + '/' + relative)
for relative in ['the-art-of-thermal-instability/ki-2002/reproduce.py', 'the-art-of-thermal-instability/ki-2002/requirements.txt', 'the-art-of-thermal-instability/field-1965/reproduce.py', 'using/citations.json', 'google0b2aef3d9ae4b856.html']:
    if not (ROOT / relative).is_file(): errors.append('Required public resource missing: ' + relative)
print(json.dumps({'pages': len(pages), 'internal_references': link_count, 'guide_sources': len(guide['pages']), 'notebook_assets': len(manifest['files']), 'errors': errors}, ensure_ascii=False, indent=2))
if errors: raise SystemExit(1)
