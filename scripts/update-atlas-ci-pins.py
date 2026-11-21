#!/usr/bin/env python3
"""Bind the no-checkout workflow to the reviewed public tool and registry bytes."""
from pathlib import Path
import hashlib
import re

ROOT=Path(__file__).resolve().parents[1]
WORKFLOW=ROOT/'.github/workflows/atlas-public-linux.yml'
INPUTS={
    'ATLAS_BOOTSTRAP_SHA256':'scripts/run-atlas-public-ci.py',
    'ATLAS_VERIFIER_SHA256':'scripts/verify-atlas-execution-examples.py',
    'ATLAS_BUILDER_SHA256':'scripts/build-atlas-execution-examples.py',
    'ATLAS_REGISTRY_SHA256':'numerical-methods-atlas/code-and-data/examples.json',
}

def build():
    text=WORKFLOW.read_text()
    for key,path in INPUTS.items():
        value=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
        text,count=re.subn(r"("+re.escape(key)+r": ')[0-9a-f]{64}(')",lambda m:m[1]+value+m[2],text)
        if count!=1:raise ValueError('Expected exactly one workflow pin: '+key)
    WORKFLOW.write_text(text)
    print('Bound public Linux workflow to four reviewed SHA-256 values.')

if __name__=='__main__':build()
