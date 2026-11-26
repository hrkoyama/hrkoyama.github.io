import { readFile, writeFile, readdir } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { decorateSite, immutablePresentations } from './site-chrome.mjs';
const root = new URL('../', import.meta.url);
// Each archive keeps its own design; changed viewing assets must reach readers
// even when their browser has cached the previous stylesheet or module.
const archiveAssets = /^(?:astronomy-step-by-step|notebooks|academic-roots|guide|gordon-bell|the-art-of-thermal-instability)\/|^styles\/home\.css$/;
const assetVersions = new Map();
async function versionViewingAssets(html, pageUrl) {
  const refs = [...html.matchAll(/\b(?:href|src)="([^"#]+\.(?:css|js|mjs)(?:\?[^"#]*)?)"/g)];
  for (const match of refs) {
    const original = match[1];
    if (/^(?:[a-z]+:|\/\/)/i.test(original)) continue;
    const assetUrl = original.startsWith('/') ? new URL(original.slice(1), root) : new URL(original, pageUrl);
    const path = decodeURIComponent(assetUrl.pathname.slice(root.pathname.length));
    if (!assetUrl.pathname.startsWith(root.pathname) || !archiveAssets.test(path)) continue;
    if (!assetVersions.has(path)) {
      const bytes = await readFile(new URL(path, root));
      assetVersions.set(path, createHash('sha256').update(bytes).digest('hex').slice(0, 12));
    }
    const [pathname, query = ''] = original.split('?');
    const params = new URLSearchParams(query.replaceAll('&amp;', '&'));
    params.set('v', assetVersions.get(path));
    const updated = pathname + '?' + params.toString().replaceAll('&', '&amp;');
    html = html.replaceAll('="' + original + '"', '="' + updated + '"');
  }
  return html;
}
async function walk(dir) {
  for (const entry of await readdir(dir, {withFileTypes:true})) {
    if (entry.name.startsWith('.')) continue;
    const url = new URL(entry.name + (entry.isDirectory() ? '/' : ''), dir);
    if (entry.isDirectory()) await walk(url);
    else if (entry.name.endsWith('.html')) {
      const path = decodeURIComponent(url.pathname.slice(root.pathname.length));
      const reading = /^numerical-methods-atlas\/(en|ja)\/read\//.exec(path);
      const fixed = reading ? reading[1] : path === 'academic-roots/index.html' || path.startsWith('notebooks/') ? 'ja' : path.startsWith('gordon-bell/') || path.startsWith('the-art-of-thermal-instability/') ? 'en' : '';
      const decorated = decorateSite(await readFile(url,'utf8'), {contentLanguage:fixed, pagePath:path});
      const completed = await versionViewingAssets(decorated, url);
      const immutable = immutablePresentations.get(path);
      if (immutable && createHash('sha256').update(completed).digest('hex') !== immutable.sha256) {
        throw Error('Immutable presentation differs: ' + path);
      }
      await writeFile(url, completed);
    }
  }
}
await walk(root);
// Keep viewing-asset receipts in sync when shared navigation changes notebook HTML.
const manifestUrl = new URL('notebooks/public-manifest.json',root);
const manifest = JSON.parse(await readFile(manifestUrl,'utf8'));
for (const file of manifest.files) {
  const bytes = await readFile(new URL('notebooks/' + file.path,root));
  const sha256 = createHash('sha256').update(bytes).digest('hex');
  if (file.sha256 !== sha256 && !/\.(html|md|js|css)$/.test(file.path)) throw Error('Unexpected viewing asset change: ' + file.path);
  file.bytes = bytes.length; file.sha256 = sha256;
}
await writeFile(manifestUrl, JSON.stringify(manifest,null,2)+'\n');
console.log('Built shared bilingual navigation, rights notices and AI discovery links.');
