#!/usr/bin/env python3
"""Rebuild root and atlas sitemaps from current canonical HTML, without private files."""
from pathlib import Path
from html.parser import HTMLParser
import os
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://hrkoyama.github.io'
class Head(HTMLParser):
    def __init__(self):
        super().__init__(); self.canonical = None; self.blocked = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical = a.get('href')
        if tag == 'meta' and a.get('name') == 'robots' and 'noindex' in a.get('content', ''): self.blocked = True

def canonical_urls(root):
    urls = set()
    for parent, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in {'node_modules', 'scripts', 'docs'}]
        for name in files:
            if not name.endswith('.html') or name.startswith('google'):
                continue
            page = Path(parent) / name
            head = Head()
            head.feed(page.read_text())
            if head.blocked or not head.canonical:
                continue
            url = head.canonical
            if not url.startswith(ORIGIN + '/') or '?' in url or '#' in url:
                raise ValueError(url)
            urls.add(url)
    return urls


def write_sitemap(path, urls):
    ns = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    ET.register_namespace('', ns)
    tree = ET.Element('{'+ns+'}urlset')
    for url in sorted(urls):
        item = ET.SubElement(tree, 'url')
        ET.SubElement(item, 'loc').text = url
    ET.indent(tree)
    ET.ElementTree(tree).write(path, encoding='utf-8', xml_declaration=True)


def build(root=ROOT):
    urls = canonical_urls(root)
    write_sitemap(root/'sitemap.xml', urls)
    atlas = {url for url in urls if url.startswith(ORIGIN+'/numerical-methods-atlas/')}
    write_sitemap(root/'numerical-methods-atlas/sitemap.xml', atlas)
    print(f'Built canonical sitemaps: root {len(urls)} pages; atlas {len(atlas)} pages.')


if __name__ == '__main__':
    build()
