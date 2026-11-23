#!/usr/bin/env python3
"""Refresh the declared, validated public build pipeline in dependency order."""
from pathlib import Path
import subprocess
from site_pipeline import commands

ROOT = Path(__file__).resolve().parents[1]
for command in commands(ROOT):
    subprocess.run(command, cwd=ROOT, check=True)
