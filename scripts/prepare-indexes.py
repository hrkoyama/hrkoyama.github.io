#!/usr/bin/env python3
"""Refresh derived public files from the active staged tree, without mixing edits."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import subprocess
import sys
import tempfile


class PreparationError(RuntimeError):
    pass


@dataclass(frozen=True)
class Entry:
    mode: str
    oid: str


class Repository:
    def __init__(self):
        initial = Path.cwd()
        self.env = os.environ.copy()
        self.env.update(GIT_NO_LAZY_FETCH='1', GIT_TERMINAL_PROMPT='0')
        if self.env.get('GIT_INDEX_FILE'):
            self.env['GIT_INDEX_FILE'] = str((initial/self.env['GIT_INDEX_FILE']).resolve())
        self.root = Path(self.git('rev-parse', '--show-toplevel', cwd=initial).decode().strip())
        git_dir = self.git('rev-parse', '--absolute-git-dir', cwd=initial).decode().strip()
        index = self.git('rev-parse', '--git-path', 'index', cwd=initial).decode().strip()
        self.index = (initial/index).resolve()
        self.env.update(GIT_DIR=git_dir, GIT_WORK_TREE=str(self.root), GIT_INDEX_FILE=str(self.index))
        self.algorithm = self.git('rev-parse', '--show-object-format').decode().strip()

    def git(self, *args, env=None, cwd=None, data=None):
        result = subprocess.run(['git', *args], cwd=cwd or getattr(self, 'root', Path.cwd()),
                                env=env or self.env, input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode:
            raise PreparationError('git '+args[0]+' failed: '+result.stderr.decode(errors='replace').strip())
        return result.stdout

    def entries(self, tree):
        result = {}
        for record in self.git('ls-tree', '-rz', '--full-tree', tree).split(b'\0'):
            if not record:
                continue
            metadata, raw_path = record.split(b'\t', 1)
            mode, kind, oid = metadata.decode().split()
            path = os.fsdecode(raw_path)
            if kind != 'blob' or mode not in {'100644', '100755', '120000'}:
                raise PreparationError('Unsupported staged entry: '+repr(path))
            if PurePosixPath(path).is_absolute() or '..' in PurePosixPath(path).parts:
                raise PreparationError('Invalid staged path: '+repr(path))
            result[path] = Entry(mode, oid)
        return result

    def export(self, entries, destination):
        # Raw blobs retain every staged path, including export-ignore files. No
        # checkout filter, working-tree contents, or network source is involved.
        process = subprocess.Popen(['git', 'cat-file', '--batch'], cwd=self.root, env=self.env,
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            for name, entry in entries.items():
                process.stdin.write(entry.oid.encode()+b'\n')
                process.stdin.flush()
                header = process.stdout.readline().split()
                if len(header) != 3 or header[1] != b'blob':
                    raise PreparationError('Could not export staged blob: '+repr(name))
                size = int(header[2])
                target = destination/name
                target.parent.mkdir(parents=True, exist_ok=True)
                if entry.mode == '120000':
                    value = process.stdout.read(size)
                    if len(value) != size:
                        raise PreparationError('Truncated staged symlink: '+repr(name))
                    link = PurePosixPath(os.fsdecode(value))
                    if link.is_absolute() or '..' in link.parts:
                        raise PreparationError('Snapshot symlink must stay inside its directory: '+repr(name))
                    target.symlink_to(os.fsdecode(value))
                else:
                    with target.open('wb') as output:
                        remaining = size
                        while remaining:
                            chunk = process.stdout.read(min(1024*1024, remaining))
                            if not chunk:
                                raise PreparationError('Truncated staged file: '+repr(name))
                            output.write(chunk)
                            remaining -= len(chunk)
                    target.chmod(0o755 if entry.mode == '100755' else 0o644)
                if process.stdout.read(1) != b'\n':
                    raise PreparationError('Invalid staged blob separator')
            process.stdin.close()
            if process.wait():
                raise PreparationError('Staged snapshot export failed')
        finally:
            if process.poll() is None:
                process.kill()
                process.wait()
            for stream in [process.stdin, process.stdout, process.stderr]:
                if stream and not stream.closed:
                    stream.close()


def file_entry(path, algorithm):
    try:
        info = path.lstat()
    except FileNotFoundError:
        return None
    if stat.S_ISLNK(info.st_mode):
        data = os.fsencode(os.readlink(path))
        digest = hashlib.new(algorithm, b'blob '+str(len(data)).encode()+b'\0'+data)
        return Entry('120000', digest.hexdigest())
    if not stat.S_ISREG(info.st_mode):
        raise PreparationError('Expected a regular file or symlink: '+str(path))
    digest = hashlib.new(algorithm, b'blob '+str(info.st_size).encode()+b'\0')
    with path.open('rb') as stream:
        for chunk in iter(lambda:stream.read(1024*1024), b''):
            digest.update(chunk)
    return Entry('100755' if info.st_mode & 0o111 else '100644', digest.hexdigest())


def snapshot_entries(directory, algorithm):
    entries = {}
    for parent, directories, files in os.walk(directory, followlinks=False):
        for name in list(directories):
            path = Path(parent)/name
            if path.is_symlink():
                files.append(name)
                directories.remove(name)
        for name in files:
            path = Path(parent)/name
            entries[path.relative_to(directory).as_posix()] = file_entry(path, algorithm)
    return entries


def index_bytes(repository):
    return repository.index.read_bytes() if repository.index.exists() else None


def verify_destinations(repository, paths, before, original_index):
    if index_bytes(repository) != original_index:
        raise PreparationError('The active Git index changed during generation; retry the commit.')
    conflicts = []
    for name in paths:
        target = repository.root/name
        for parent in target.parents:
            if parent == repository.root:
                break
            if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
                conflicts.append(name)
                break
        else:
            conflicts.append(name)
        try:
            if file_entry(target, repository.algorithm) != before.get(name):
                conflicts.append(name)
        except PreparationError:
            conflicts.append(name)
    if conflicts:
        raise PreparationError('Generated files have unstaged changes or path collisions; nothing was applied:\n'+
                               '\n'.join('  '+repr(name) for name in sorted(set(conflicts))))


def copy_entry(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix='.atlas-index-', dir=target.parent)
    os.close(descriptor)
    temporary = Path(temporary)
    try:
        if source.is_symlink():
            temporary.unlink()
            temporary.symlink_to(os.readlink(source))
        else:
            shutil.copy2(source, temporary)
        os.replace(temporary, target)
    finally:
        if temporary.exists() or temporary.is_symlink():
            temporary.unlink()


def apply_changes(repository, snapshot, temporary_index, paths, before, after, original_index, scratch):
    verify_destinations(repository, paths, before, original_index)
    env = {**repository.env, 'GIT_INDEX_FILE':str(temporary_index)}
    records = []
    for name in paths:
        entry = after.get(name)
        if entry is None:
            records.append(b'0 '+b'0'*(40 if repository.algorithm == 'sha1' else 64)+b'\t'+os.fsencode(name)+b'\0')
        else:
            source = snapshot/name
            if entry.mode == '120000':
                oid = repository.git('hash-object', '-w', '--stdin', data=os.fsencode(os.readlink(source))).strip()
            else:
                oid = repository.git('hash-object', '-w', '--no-filters', '--', str(source)).strip()
            records.append(entry.mode.encode()+b' '+oid+b'\t'+os.fsencode(name)+b'\0')
    repository.git('update-index', '-z', '--index-info', env=env, data=b''.join(records))
    backup = scratch/'backup'
    for name in paths:
        if before.get(name) is not None:
            copy_entry(repository.root/name, backup/name)
    lock = Path(str(repository.index)+'.lock')
    descriptor = None
    owned_lock = False
    applied = []
    try:
        try:
            descriptor = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
            owned_lock = True
        except FileExistsError as exc:
            raise PreparationError('The active Git index is locked; retry after the other Git operation finishes.') from exc
        with os.fdopen(descriptor, 'wb') as stream:
            descriptor = None
            stream.write(temporary_index.read_bytes())
            stream.flush()
            os.fsync(stream.fileno())
        verify_destinations(repository, paths, before, original_index)
        for name in paths:
            applied.append(name)
            target = repository.root/name
            if after.get(name) is None:
                target.unlink()
            else:
                copy_entry(snapshot/name, target)
        os.replace(lock, repository.index)
        owned_lock = False
    except BaseException:
        # Only previously clean derived paths were touched. Restore them if an
        # I/O error or interruption prevents the final atomic index replacement.
        for name in reversed(applied):
            target = repository.root/name
            if before.get(name) is None:
                if target.exists() or target.is_symlink():
                    target.unlink()
            else:
                copy_entry(backup/name, target)
        raise
    finally:
        if descriptor is not None:
            os.close(descriptor)
        if owned_lock:
            lock.unlink(missing_ok=True)


def prepare(check=False):
    repository = Repository()
    original_index = index_bytes(repository)
    base = os.environ.get('ATLAS_INDEX_SCRATCH') or os.environ.get('TMPDIR')
    if base:
        Path(base).mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='atlas-indexes-', dir=base) as temporary:
        scratch = Path(temporary)
        temporary_index = scratch/'index'
        env = {**repository.env, 'GIT_INDEX_FILE':str(temporary_index)}
        if original_index is None:
            repository.git('read-tree', '--empty', env=env)
        else:
            temporary_index.write_bytes(original_index)
        tree = repository.git('write-tree', env=env).decode().strip()
        before = repository.entries(tree)
        snapshot = scratch/'site'
        snapshot.mkdir()
        repository.export(before, snapshot)
        build_env = {key:value for key,value in os.environ.items() if not key.startswith('GIT_')}
        build_env.update(PYTHONDONTWRITEBYTECODE='1', GIT_NO_LAZY_FETCH='1', GIT_TERMINAL_PROMPT='0')
        result = subprocess.run([sys.executable, 'scripts/refresh-site.py'], cwd=snapshot, env=build_env)
        if result.returncode:
            raise PreparationError('Index refresh failed; the real working tree and Git index were not changed.')
        after = snapshot_entries(snapshot, repository.algorithm)
        paths = sorted(name for name in before.keys() | after.keys() if before.get(name) != after.get(name))
        for name in paths:
            print(('A' if name not in before else 'D' if name not in after else 'M')+' '+name)
        if index_bytes(repository) != original_index:
            raise PreparationError('The active Git index changed during generation; retry the commit.')
        if check:
            print('Generated indexes are stale.' if paths else 'Generated indexes are current.')
            return 1 if paths else 0
        if paths:
            apply_changes(repository, snapshot, temporary_index, paths, before, after, original_index, scratch)
        print('Automatically staged '+str(len(paths))+' generated file(s).')
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Report stale staged outputs without changing files or the active index')
    args = parser.parse_args()
    if sys.version_info < (3, 10):
        raise PreparationError('Python 3.10+ is required; rerun the installer with the site build interpreter.')
    return prepare(args.check)


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (PreparationError, OSError) as exc:
        print('Index preparation: '+str(exc), file=sys.stderr)
        raise SystemExit(1)
