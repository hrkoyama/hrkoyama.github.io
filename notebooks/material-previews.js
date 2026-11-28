(() => {
  'use strict';
  const records = window.NOTEBOOK_MATERIAL_PREVIEWS || {};
  const english = () => {
    const selected = document.querySelector('[data-site-lang][aria-current="page"]');
    const requested = selected?.dataset.siteLang || new URL(location.href).searchParams.get('lang');
    if (requested === 'ja' || requested === 'en') return requested === 'en';
    try { return localStorage.getItem('hrkoyama.home.language') === 'en'; } catch { return false; }
  };
  const words = value => english() ? value.en : value.ja;
  const node = (tag, className, text) => {
    const result = document.createElement(tag);
    if (className) result.className = className;
    if (text) result.textContent = text;
    return result;
  };
  function localized(tag, className, value) {
    const result = node(tag, className, words(value));
    result.dataset.uiJa = value.ja; result.dataset.uiEn = value.en;
    return result;
  }
  const imagePath = value => /^assets\/material-previews\/b\d{3}(?:-[a-z0-9]+)*-first-page\.png$/.test(value);
  const buttonLabel = record => english() ? `Enlarge the cover / title preview of ${record.title}` : `${record.title}の表紙・表題画像を拡大`;

  // Used by notebook pages; bibliography figures are generated from the same
  // public metadata so their titles remain available without JavaScript.
  function create(id) {
    const record = records[id];
    if (!record) return null;
    const preview = record.preview;
    const container = node(preview.image ? 'figure' : 'div', preview.image ? `material-preview material-preview-${preview.mode === 'cover' ? 'cover' : 'title'}` : 'material-preview-empty');
    if (preview.image && imagePath(preview.image)) {
      const button = node('button', 'material-preview-button'); button.type = 'button';
      button.dataset.materialPreview = id; button.setAttribute('aria-label', buttonLabel(record));
      const image = node('img'); image.src = preview.image; image.alt = words(preview.alt);
      image.width = preview.width; image.height = preview.height; image.loading = 'lazy';
      button.append(image, localized('span', 'material-preview-action', {ja:'画像を拡大',en:'Enlarge preview'}));
      container.append(button);
    }
    const caption = node(preview.image ? 'figcaption' : 'div', 'material-preview-description');
    caption.append(localized('span', 'material-preview-label', preview.label), localized('p', 'material-preview-caption', preview.caption));
    if (preview.year_label) caption.append(localized('p', 'material-preview-date', preview.year_label));
    container.append(caption);
    return container;
  }
  window.NotebookMaterialPreviews = Object.freeze({create});

  let dialog;
  function show(id) {
    const record = records[id];
    if (!record?.preview.image || !imagePath(record.preview.image)) return;
    if (!dialog) {
      dialog = node('dialog', 'material-preview-dialog'); dialog.id = 'material-preview-dialog';
      dialog.setAttribute('aria-labelledby', 'material-preview-title');
      document.body.append(dialog);
      dialog.addEventListener('click', event => {
        if (event.target !== dialog) return;
        const bounds = dialog.getBoundingClientRect();
        if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
      });
    }
    const top = node('div', 'material-preview-dialog-top');
    const title = node('h2', '', record.title); title.id = 'material-preview-title';
    const close = localized('button', '', {ja:'閉じる',en:'Close'}); close.type = 'button';
    close.addEventListener('click', () => dialog.close()); top.append(title, close);
    const creator = node('p', 'material-preview-creator', record.creator || '');
    const image = node('img'); image.src = record.preview.image; image.alt = words(record.preview.alt);
    image.width = record.preview.width; image.height = record.preview.height;
    const caption = localized('p', 'material-preview-caption', record.preview.caption);
    const scope = localized('p', 'material-preview-scope', {ja:'表紙・表題の確認済み部分のみです。講師・著者名を残し、資料の本文・問題・連絡先を除いています。',en:'Only the reviewed cover / title portions are shown. Instructor and author names are retained; document bodies, questions and contact details are excluded.'});
    dialog.replaceChildren(top, creator, caption, image, scope);
    dialog.showModal();
  }
  document.addEventListener('click', event => {
    const button = event.target.closest('button[data-material-preview]');
    if (button) show(button.dataset.materialPreview);
  });
  function language() {
    document.querySelectorAll('button[data-material-preview]').forEach(button => {
      const record = records[button.dataset.materialPreview];
      if (record) {
        button.setAttribute('aria-label', buttonLabel(record));
        const image = button.querySelector('img');
        if (image) image.alt = words(record.preview.alt);
      }
    });
  }
  document.addEventListener('archive-language-change', language);
  language();
})();
