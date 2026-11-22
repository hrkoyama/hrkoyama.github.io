#!/usr/bin/env python3
"""Refresh generated public navigation and indexes in dependency order."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
for command in [
    [sys.executable, 'scripts/build-notebook-bibliography.py'],
    [sys.executable, 'scripts/build-public-resources.py'],
    [sys.executable, 'scripts/build-atlas-execution-examples.py'],
    [sys.executable, 'scripts/update-atlas-ci-pins.py'],
    [sys.executable, 'scripts/build-quantum-examples.py'],
    [sys.executable, 'scripts/build-atlas-method-sources.py'],
    [sys.executable, 'scripts/build-atlas-fdtd.py'],
    [sys.executable, 'scripts/build-atlas-detailed-reading.py'],
    [sys.executable, 'scripts/build-atlas-depth-examples.py'],
    [sys.executable, 'scripts/update-depth-ci-pins.py'],
    [sys.executable, 'scripts/build-atlas-h2.py'],
    [sys.executable, 'scripts/build-atlas-periodic.py'],
    [sys.executable, 'scripts/build-atlas-forces.py'],
    [sys.executable, 'scripts/build-atlas-quantum.py'],
    [sys.executable, 'scripts/build-atlas-resources.py'],
    [sys.executable, 'scripts/build-atlas-autodiff.py'],
    [sys.executable, 'scripts/build-atlas-execution-guide.py'],
    [sys.executable, 'scripts/build-atlas-execution-entries.py'],
    [sys.executable, 'scripts/build-atlas-ci-page.py'],
    [sys.executable, 'scripts/build-thermostat-reading.py'],
    [sys.executable, 'scripts/build-atlas-keep.py'],
    [sys.executable, 'scripts/build-atlas-stability.py'],
    [sys.executable, 'scripts/build-atlas-test-problems.py'],
    [sys.executable, 'scripts/build-atlas-equations.py'],
    [sys.executable, 'scripts/build-atlas-gallery.py'],
    [sys.executable, 'scripts/build-atlas-goals.py'],
    [sys.executable, 'scripts/build-atlas-depth.py'],
    [sys.executable, 'scripts/build-atlas-crossovers.py'],
    [sys.executable, 'scripts/build-atlas-reading-index.py'],
    [sys.executable, 'scripts/build-atlas-search.py'],
    [sys.executable, 'scripts/build-atlas-sharing.py'],
    [sys.executable, 'scripts/build-atlas-purpose.py'],
    ['node', 'scripts/build-site-chrome.mjs'],
    [sys.executable, 'scripts/build-sitemap.py'],
    [sys.executable, 'scripts/build-guide.py', '--local-site', '.'],
    [sys.executable, 'scripts/build-search.py'],
    [sys.executable, 'scripts/check-site.py'],
]:
    subprocess.run(command, cwd=ROOT, check=True)
