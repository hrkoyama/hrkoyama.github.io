# Rebuilding the atlas introduction assets

From the site repository root, use a Python environment with Pillow:

```sh
python -m pip install -r numerical-methods-atlas/share/render-requirements.txt
python scripts/build-atlas-sharing.py
```

Use `--font /path/to/Japanese-capable-font.ttf` when automatic Hiragino/Noto CJK detection does not apply. Font binaries are not redistributed. The recorded font hash, Pillow/FreeType versions and source hashes are in build.json. SVG and PNG use the same text and flat drawing instructions; PNG text widths are checked before output. Unchanged PNGs are reused only after their render-input hash, file hash and 1200×630 dimensions match, so an ordinary unchanged refresh needs only the Python standard library and no locally installed Japanese font. Changed graphics require Pillow; failures are explicit and stale images are not silently accepted.

These are introduction graphics, not new scientific results. Counts come from the shared catalogs and coverage inventory. Existing rights apply: https://hrkoyama.github.io/rights/
