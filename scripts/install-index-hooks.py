#!/usr/bin/env python3
"""Install the opt-in index hook in this authorized public worktree only."""
from pathlib import Path
import os
import re
import subprocess
import sys


def git(*args, required=True):
    result = subprocess.run(['git', *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if required and result.returncode:
        raise RuntimeError('git '+args[0]+' failed: '+result.stderr.strip())
    return result.stdout.strip() if not result.returncode else ''


def install():
    if sys.version_info < (3, 10):
        raise RuntimeError('Run this installer with the Python 3.10+ interpreter used to build the site.')
    root = Path(git('rev-parse', '--show-toplevel'))
    os.chdir(root)
    accepted = re.compile(r'(?:https://github[.]com/|git@github[.]com:|ssh://git@github[.]com/)hrkoyama/hrkoyama[.]github[.]io(?:[.]git)?/?\Z')
    fetch = git('remote', 'get-url', 'origin')
    pushes = git('remote', 'get-url', '--push', '--all', 'origin').splitlines()
    if not accepted.fullmatch(fetch) or not pushes or not all(accepted.fullmatch(url) for url in pushes):
        raise RuntimeError('Install only in the public hrkoyama/hrkoyama.github.io repository; origin does not match.')
    if git('config', '--get', 'extensions.worktreeConfig', required=False) != 'true':
        raise RuntimeError('Worktree-specific Git configuration must be enabled before installing this hook.')
    hook = root/'.githooks/pre-commit'
    if not hook.is_file() or not os.access(hook, os.X_OK):
        raise RuntimeError('The versioned .githooks/pre-commit file is missing or is not executable.')
    existing = git('config', '--get', 'core.hooksPath', required=False)
    if existing and (root/existing).resolve() != hook.parent.resolve():
        raise RuntimeError('An existing core.hooksPath is configured; it was preserved. Integrate its hooks before installing.')
    default_hooks = Path(git('rev-parse', '--git-path', 'hooks'))
    active = sorted(path.name for path in default_hooks.iterdir()
                    if not path.name.endswith('.sample') and path.is_file() and os.access(path, os.X_OK)) if default_hooks.is_dir() else []
    if not existing and active:
        raise RuntimeError('Existing default hooks were preserved ('+', '.join(active)+'). Integrate them before installing.')
    git('config', '--worktree', 'atlas.indexPython', sys.executable)
    git('config', '--worktree', 'core.hooksPath', '.githooks')
    print('Installed the opt-in index hook for this hrkoyama public worktree.')
    print('Normal commits skip refresh. Before publishing run scripts/prepare-indexes.py explicitly.')
    print('Optional commit-time refresh: ATLAS_REFRESH_INDEXES_ON_COMMIT=1 git commit ...')
    print('Build interpreter: '+sys.executable)


if __name__ == '__main__':
    try:
        install()
    except (RuntimeError, OSError) as exc:
        print('Index hook installation: '+str(exc), file=sys.stderr)
        raise SystemExit(1)
