"""Offline regressions for the public-ZIP execution selector, without science."""
import copy
import base64
from contextlib import redirect_stdout
import importlib.util
import hashlib
import io
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest import mock

from atlas_depth_scope import Client, InvalidEvent, ScopeError, plan


REPO = 'hrkoyama/hrkoyama.github.io'
BASE = 'a' * 40
TARGET = 'b' * 40
MID = 'c' * 40
RUNS = '/actions/workflows/atlas-depth-linux.yml/runs?branch=main&status=completed&per_page=100'
FAILURE_RUNS = {status: RUNS.replace('status=completed', 'status='+status)
                for status in ['failure', 'cancelled', 'timed_out']}
STEP = 'Install three pinned wheel dependencies and verify public ZIPs'
PUBLIC_RUN = '/actions/runs/999'
PUBLIC_JOBS = '/actions/runs/999/attempts/1/jobs?per_page=100'
FRESHNESS_STEP = 'Regenerate every index and reject stale generated files'
DETAIL_REFERENCES = {
    'site': ('search/detail-references.json', 'search/query-index.json'),
    'atlas': ('search/atlas-detail-references.json', 'search/atlas-query-index.json'),
}


def run_record(identifier=100, sha=BASE, conclusion='success', when='2026-11-26T12:00:00Z'):
    return {'id': identifier, 'run_number': identifier, 'run_attempt': 1,
            'status': 'completed', 'conclusion': conclusion, 'head_sha': sha,
            'head_branch': 'main', 'head_repository': {'full_name': REPO},
            'html_url': f'https://github.com/{REPO}/actions/runs/{identifier}',
            'updated_at': when}


def job_record(identifier=1000, conclusion='success', run_id=100, head_sha=BASE):
    return {'id': identifier, 'name': 'public-supplements', 'status': 'completed',
            'conclusion': conclusion, 'run_id': run_id, 'head_sha': head_sha, 'steps': [
                {'name': STEP, 'status': 'completed', 'conclusion': conclusion}]}


def public_run_record():
    value = run_record(999, TARGET)
    value.update(name='Public site checks', path='.github/workflows/site-checks.yml', event='push')
    return value


def public_job_records():
    return [{'id': 9000 + index, 'name': name, 'status': 'completed',
             'conclusion': 'success', 'run_id': 999, 'head_sha': TARGET,
             'steps': [{'name': FRESHNESS_STEP, 'status': 'completed', 'conclusion': 'success'}]
                      if name == 'check' else []}
            for index, name in enumerate(['check', 'logic', 'browser-smoke'])]


def changed(path, status='modified'):
    return {'filename': path, 'status': status, 'sha': 'd' * 40}


def git_blob_sha(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


class FakeClient:
    """Only fixtures are reachable; an unexpected API request fails the test."""
    def __init__(self):
        self.calls = []
        self.responses = {
            '/git/ref/heads/main': {'object': {'sha': TARGET}},
            PUBLIC_RUN: public_run_record(),
            PUBLIC_JOBS: {'total_count': 3, 'jobs': public_job_records()},
            RUNS: {'total_count': 1, 'workflow_runs': [run_record()]},
            '/actions/runs/100/attempts/1/jobs?per_page=100':
                {'total_count': 1, 'jobs': [job_record()]},
            f'/compare/{BASE}...{TARGET}?per_page=1&page=1': {
                'status': 'ahead', 'merge_base_commit': {'sha': BASE},
                'files': [changed('catalog/atlas-identities.json')]},
        }
        self.blobs = {}
        self.tree_entries = {}
        for status in ['queued', 'in_progress', 'waiting', 'pending', 'requested']:
            self.responses[RUNS.replace('status=completed', 'status='+status)] = {'total_count': 0, 'workflow_runs': []}
        for endpoint in FAILURE_RUNS.values():
            self.responses[endpoint] = {'total_count': 0, 'workflow_runs': []}

    def get(self, endpoint):
        self.calls.append(endpoint)
        value = self.responses[endpoint]
        if isinstance(value, BaseException):
            raise value
        return copy.deepcopy(value)

    def blob(self, path, sha):
        self.calls.append(('blob', path, sha))
        value = self.blobs[(path, sha)]
        if isinstance(value, BaseException):
            raise value
        return value

    def tree_entry(self, path, revision):
        self.calls.append(('tree_entry', path, revision))
        if (path, revision) in self.tree_entries:
            value = self.tree_entries[(path, revision)]
            if isinstance(value, BaseException):
                raise value
            return copy.deepcopy(value)
        raw = self.blobs.get((path, revision))
        if isinstance(raw, bytes):
            sha = git_blob_sha(raw)
        else:
            files = self.responses[f'/compare/{BASE}...{TARGET}?per_page=1&page=1'].get('files', [])
            sha = next((file['sha'] for file in files if file.get('filename') == path), 'd' * 40)
        return {'mode': '100644', 'type': 'blob', 'sha': sha}


class ScopeTests(unittest.TestCase):
    def setUp(self):
        self.client = FakeClient()
        self.event = {'workflow_run': public_run_record()}

    def choose(self, **kwargs):
        args = dict(event_name='workflow_run', event=self.event, sha=TARGET,
                    ref='refs/heads/main', repo=REPO, run_id=10000, client=self.client)
        args.update(kwargs)
        return plan(**args)

    def compare(self):
        return self.client.responses[f'/compare/{BASE}...{TARGET}?per_page=1&page=1']

    def set_blob_change(self, path, before, after):
        def encode(value):
            return value if isinstance(value, bytes) else json.dumps(value, ensure_ascii=False).encode()
        before, after = encode(before), encode(after)
        self.compare()['files'] = [changed(path)]
        self.compare()['files'][0]['sha'] = git_blob_sha(after)
        self.client.blobs[(path, BASE)] = before; self.client.blobs[(path, TARGET)] = after

    def configure_active_detail(self, path=None, kind='site'):
        """Bind an optional detail key to two small, regenerated query manifests."""
        key = path.removeprefix('search/details/').removesuffix('.json') if path else None
        if key is not None:
            self.assertRegex(key, r'\A[0-9a-f]{64}\Z')
        for owner, (manifest_path, index_path) in DETAIL_REFERENCES.items():
            index_raw = json.dumps({'kind': owner, 'docs': []}, sort_keys=True).encode()
            index_sha = git_blob_sha(index_raw)
            self.client.tree_entries[(index_path, TARGET)] = {
                'mode': '100644', 'type': 'blob', 'sha': index_sha}
            manifest = {'schema_version': 1, 'kind': owner, 'index_path': index_path,
                        'index_git_blob_sha': index_sha,
                        'index_sha256': hashlib.sha256(index_raw).hexdigest(),
                        'detail_keys': [key] if key is not None and owner == kind else []}
            self.client.blobs[(manifest_path, TARGET)] = json.dumps(manifest, sort_keys=True).encode()

    def add_detail_change(self):
        raw = b'{"text":"Read the current reference and its error bounds."}'
        path = 'search/details/' + hashlib.sha256(raw).hexdigest() + '.json'
        self.compare()['files'] = [changed(path, 'added')]
        self.compare()['files'][0]['sha'] = git_blob_sha(raw)
        self.client.blobs[(path, TARGET)] = raw
        return path

    def full(self):
        value = self.choose()
        self.assertEqual(value['mode'], 'full', value)
        self.assertIs(value['run_full'], True, value)
        return value

    def reuse(self):
        value = self.choose()
        self.assertEqual(value['mode'], 'reuse', value)
        self.assertIs(value['run_full'], False, value)
        self.assertEqual(value['target_sha'], TARGET)
        self.assertEqual(value['baseline']['sha'], BASE)
        self.assertEqual(value['baseline']['run_id'], 100)
        return value

    def test_metadata_reuses_real_full_success_and_links_its_identity(self):
        result = self.reuse()
        self.assertIn('comparison_sha256', result)
        self.assertIn('/actions/runs/100/attempts/1/jobs?per_page=100', self.client.calls)
        self.assertEqual(self.client.calls.count(f'/compare/{BASE}...{TARGET}?per_page=1&page=1'), 1)

    def test_reuse_checks_the_exact_successful_public_workflow_attempt_and_freshness_job(self):
        self.reuse()
        self.assertIn(PUBLIC_RUN, self.client.calls)
        self.assertIn(PUBLIC_JOBS, self.client.calls)

    def test_public_workflow_identity_and_success_are_required_for_reuse(self):
        mutations = [('id', 998), ('head_sha', MID), ('head_branch', 'candidate'),
                     ('head_repository', {'full_name': 'other/repository'}),
                     ('name', 'Unrelated check'), ('path', '.github/workflows/other.yml'),
                     ('event', 'pull_request'), ('status', 'in_progress'),
                     ('conclusion', 'failure'), ('run_attempt', 0), ('run_attempt', True)]
        for key, value in mutations:
            with self.subTest(key=key, value=value):
                self.client = FakeClient()
                self.client.responses[PUBLIC_RUN][key] = value
                self.full()

    def test_public_workflow_retry_requires_its_own_jobs_and_freshness_step(self):
        self.event['workflow_run']['run_attempt'] = 2
        self.client.responses[PUBLIC_RUN]['run_attempt'] = 2
        second_jobs = '/actions/runs/999/attempts/2/jobs?per_page=100'
        self.client.responses[second_jobs] = {'total_count': 3, 'jobs': public_job_records()}
        self.reuse()
        self.assertIn(second_jobs, self.client.calls)
        self.assertNotIn(PUBLIC_JOBS, self.client.calls)
        self.client.responses[second_jobs]['jobs'][0]['steps'] = []
        self.full()

    def test_public_jobs_and_regeneration_must_be_complete_unique_and_successful(self):
        for mutation in ['truncated', 'missing_job', 'duplicate_job', 'unknown_job',
                         'job_failed', 'job_running', 'wrong_run', 'wrong_sha',
                         'missing_regeneration', 'duplicate_regeneration',
                         'regeneration_failed', 'regeneration_running']:
            with self.subTest(mutation=mutation):
                self.client = FakeClient()
                listing = self.client.responses[PUBLIC_JOBS]
                check = listing['jobs'][0]
                if mutation == 'truncated': listing['total_count'] += 1
                if mutation == 'missing_job': listing['jobs'].pop(); listing['total_count'] -= 1
                if mutation == 'duplicate_job': listing['jobs'][2] = copy.deepcopy(check)
                if mutation == 'unknown_job': listing['jobs'][2]['name'] = 'unrelated-job'
                if mutation == 'job_failed': check['conclusion'] = 'failure'
                if mutation == 'job_running': check['status'] = 'in_progress'
                if mutation == 'wrong_run': check['run_id'] = 998
                if mutation == 'wrong_sha': check['head_sha'] = MID
                if mutation == 'missing_regeneration': check['steps'] = []
                if mutation == 'duplicate_regeneration': check['steps'] *= 2
                if mutation == 'regeneration_failed': check['steps'][0]['conclusion'] = 'failure'
                if mutation == 'regeneration_running': check['steps'][0]['status'] = 'in_progress'
                self.full()

    def test_changed_files_require_regular_immutable_tree_entries_at_both_revisions(self):
        path = 'catalog/atlas-identities.json'
        self.reuse()
        self.assertIn(('tree_entry', path, BASE), self.client.calls)
        self.assertIn(('tree_entry', path, TARGET), self.client.calls)
        for revision in [BASE, TARGET]:
            for entry in [None, {}, {'mode': '120000', 'type': 'blob', 'sha': 'd' * 40},
                          {'mode': '100755', 'type': 'blob', 'sha': 'd' * 40},
                          {'mode': '040000', 'type': 'tree', 'sha': 'd' * 40},
                          {'mode': '160000', 'type': 'commit', 'sha': 'd' * 40},
                          RuntimeError('private-tree-token-must-not-leak')]:
                with self.subTest(revision=revision, entry=entry):
                    self.client = FakeClient()
                    self.client.tree_entries[(path, revision)] = entry
                    result = self.full()
                    self.assertNotIn('private-tree-token-must-not-leak', str(result))

    def test_tree_target_blob_must_match_the_complete_compare_record(self):
        path = 'catalog/atlas-identities.json'
        self.client.tree_entries[(path, TARGET)] = {'mode': '100644', 'type': 'blob', 'sha': MID}
        self.full()

    def test_all_explicit_prose_and_id_changes_are_eligible(self):
        for path in ['README.md', 'MAINTENANCE.md', 'docs/atlas-identities.md',
                     'catalog/atlas-identities.json', 'catalog/atlas-identity-history.json',
                     'catalog/identity-snapshots/NMA-P-000004/00.json',
                     'catalog/atlas-home.json', 'guide/index.json',
                     'site.css', 'styles/atlas-resources.css',
                     'search/atlas-query-index.json']:
            with self.subTest(path=path):
                self.compare()['files'] = [changed(path)]
                if path in {'README.md', 'MAINTENANCE.md', 'docs/atlas-identities.md'}:
                    self.set_blob_change(path, b'Old wording', b'New wording')
                if path == 'catalog/atlas-home.json':
                    self.set_blob_change(path, {'landing':{'ja':{'description':'Old text'}}},
                                         {'landing':{'ja':{'description':'New text'}}})
                self.reuse()

    def test_document_prose_changes_cannot_hide_numerical_values_or_relative_references(self):
        for before, after in [(b'Reference 1e-8', b'Reference 1e-2'),
                              (b'[source](../code/old.py)', b'[source](../code/new.py)'),
                              (b'Use `solver_old.py`', b'Use `solver_new.py`'),
                              (b'Equation $a+b$', b'Equation $a-b$'),
                              (b'See ftp://example.org/old', b'See ftp://example.org/new'),
                              (b'See data/old.dat', b'See data/new.dat'),
                              (b'Formula a+b', b'Formula a-b')]:
            with self.subTest(before=before, after=after):
                self.client = FakeClient()
                self.set_blob_change('docs/notes.md', before, after)
                self.full()

    def test_known_copy_catalogs_preserve_url_schemes_data_paths_and_inline_formulas(self):
        path = 'catalog/atlas-reading-index.json'
        self.set_blob_change(path, {'id': 'reading', 'description': {'ja': 'Old wording'}},
                             {'id': 'reading', 'description': {'ja': 'New wording'}})
        self.reuse()
        for before, after in [('See ftp://example.org/old', 'See ftp://example.org/new'),
                              ('See data/old.dat', 'See data/new.dat'),
                              ('Formula a+b', 'Formula a-b')]:
            with self.subTest(before=before, after=after):
                self.client = FakeClient()
                self.set_blob_change(path, {'id': 'reading', 'description': {'ja': before}},
                                     {'id': 'reading', 'description': {'ja': after}})
                self.full()

    def test_wildcard_generated_documents_need_active_owner_proof(self):
        for path in ['guide/packs/unknown.md',
                     'numerical-methods-atlas/ja/read/unknown/index.md',
                     'numerical-methods-atlas/en/read/unknown/index.json',
                     'numerical-methods-atlas/methods/unknown/index.html',
                     'numerical-methods-atlas/problems/unknown/index.json',
                     'numerical-methods-atlas/ja/read/index.html']:
            with self.subTest(path=path):
                self.client = FakeClient()
                self.set_blob_change(path, b'Old wording', b'New wording')
                self.full()

    def test_added_id_snapshot_can_be_metadata_only(self):
        path = 'catalog/identity-snapshots/NMA-P-000004/00.json'
        self.compare()['files'] = [changed(path, 'added')]
        self.reuse()
        self.assertIn(('tree_entry', path, TARGET), self.client.calls)
        self.assertNotIn(('tree_entry', path, BASE), self.client.calls)
        self.client.tree_entries[(path, TARGET)] = {'mode': '120000', 'type': 'blob', 'sha': 'd' * 40}
        self.full()

    def test_science_inputs_references_tolerances_and_source_always_run(self):
        paths = ['code/validated-examples/2026-11-25/quantum-small/eigenpairs.py',
                 'code/validated-examples/2026-11-25/quantum-small/inputs.json',
                 'code/validated-examples/2026-11-25/quantum-small/acceptance.json',
                 'code/validated-examples/2026-11-25/quantum-small/README.md',
                 'data/reference-values.json', 'data/observations.csv',
                 'docs/reference-values.md', 'docs/inputs.md', 'docs/tolerance.md',
                 'downloads/scientific-example.zip', 'results/golden.npz',
                 'numerical-methods-atlas/validation/releases.json',
                 'numerical-methods-atlas/cip.json', 'catalog/atlas-depth-expansion.json',
                 'catalog/atlas-registration.json', 'scripts/verify-depth-public.py',
                 'scripts/templates/verify-depth-public.py.tmpl',
                 'scripts/atlas_identities.py', 'scripts/check-atlas-identities.py',
                 'catalog/schemas/atlas-identities.schema.json',
                 'scripts/atlas_depth_scope.py', 'scripts/plan-atlas-depth-ci.py',
                 '.github/workflows/atlas-depth-linux.yml', 'requirements.txt',
                 'package-lock.json', 'frontend/new-solver.js', 'new-science/new_solver.cpp']
        for path in paths:
            with self.subTest(path=path):
                self.compare()['files'] = [changed(path)]
                self.full()

    def test_unknown_files_fail_closed(self):
        for path in ['catalog/new-source.json', 'unknown/new-kind.xyz', 'science.config', 'simulator.css']:
            with self.subTest(path=path):
                self.compare()['files'] = [changed(path)]
                self.full()

    def test_catalog_prose_requires_unchanged_numbers_identity_paths_and_shape(self):
        original = {'id':'home','landing':{'ja':{'description':'Old overview'},
                                         'en':{'description':'Atlas'}},
            'count':3,'acceptance':{'tol':1e-8},'path':'/numerical-methods-atlas/'}
        revised = copy.deepcopy(original); revised['landing']['ja']['description'] = 'New overview'
        self.set_blob_change('catalog/atlas-home.json', original, revised)
        self.reuse()
        for mutation in ['count','tolerance','id','path','shape']:
            with self.subTest(mutation=mutation):
                revised = copy.deepcopy(original)
                if mutation == 'count': revised['count'] = 4
                if mutation == 'tolerance': revised['acceptance']['tol'] = 1e-4
                if mutation == 'id': revised['id'] = 'different'
                if mutation == 'path': revised['path'] = '/other/'
                if mutation == 'shape': revised['added'] = 'extra'
                self.client = FakeClient(); self.set_blob_change('catalog/atlas-home.json', original, revised)
                self.full()

    def test_problem_catalog_title_copy_is_prose_but_numeric_literals_are_not(self):
        original = {'problems':[{'id':'sine','name':{'ja':'Old 1D sine','en':'Sine'},
            'note':{'ja':'tolerance=1e-8'}}]}
        revised = copy.deepcopy(original); revised['problems'][0]['name']['ja'] = 'New 1D wording'
        self.set_blob_change('catalog/atlas-test-problems.json', original, revised)
        self.reuse()
        revised['problems'][0]['note']['ja'] = 'tolerance=1e-4'
        self.set_blob_change('catalog/atlas-test-problems.json', original, revised)
        self.full()

    def test_critical_catalog_configs_remain_full_even_for_copy_changes(self):
        for name in ['atlas-depth.json','atlas-depth-expansion.json','atlas-registration.json',
                     'atlas-execution-examples.json','atlas-quantum-examples.json',
                     'atlas-reference-supplements.json','atlas-legacy-reference-contracts-2026-11-25.json',
                     'atlas-ci.json','site-build-pipeline.json','atlas-agent-kits.json','atlas-rkdg-pilot.json']:
            with self.subTest(name=name):
                self.client = FakeClient()
                self.set_blob_change('catalog/'+name, {'title':{'ja':'Old'}}, {'title':{'ja':'New'}})
                self.full()

    def test_localized_scientific_conditions_are_not_treated_as_prose(self):
        for path in ['catalog/new-model.json', 'catalog/atlas-home.json']:
            with self.subTest(path=path):
                self.client = FakeClient()
                self.set_blob_change(path, {'boundary':{'ja':'periodic'}},
                    {'boundary':{'ja':'dirichlet'}})
                self.full()

    def test_generated_problem_descriptor_requires_owner_proof_even_for_just_title_copy(self):
        path = 'numerical-methods-atlas/problems/advection-sine/index.json'
        original = {'id':'advection-sine','name':{'ja':'Old title','en':'Sine'},
                    'conditions':{'nx':64}}
        revised = copy.deepcopy(original); revised['name']['ja'] = 'New wording'
        self.set_blob_change(path, original, revised); self.full()
        revised['conditions']['nx'] = 128
        self.set_blob_change(path, original, revised); self.full()

    def test_added_content_addressed_search_detail_is_verified_as_text(self):
        raw = json.dumps({'text':{'ja':'Current reading','en':'Reference'}},
                         separators=(',',':')).encode()
        path = 'search/details/'+hashlib.sha256(raw).hexdigest()+'.json'
        self.compare()['files'] = [changed(path, 'added')]
        self.compare()['files'][0]['sha'] = git_blob_sha(raw)
        self.client.blobs[(path, TARGET)] = raw
        self.configure_active_detail(path)
        result = self.reuse()
        self.assertEqual(result['changed_files'][0]['after_sha256'], hashlib.sha256(raw).hexdigest())

    def test_details_reuse_only_when_an_active_site_or_atlas_query_owns_the_key(self):
        for kind in DETAIL_REFERENCES:
            with self.subTest(kind=kind):
                self.client = FakeClient()
                path = self.add_detail_change()
                self.configure_active_detail(path, kind)
                result = self.reuse()
                self.assertEqual(len(result['active_detail_references']), 2)
                for manifest_path, index_path in DETAIL_REFERENCES.values():
                    self.assertIn(('blob', manifest_path, TARGET), self.client.calls)
                    self.assertIn(('tree_entry', index_path, TARGET), self.client.calls)

    def test_only_the_two_exact_regenerated_detail_manifest_paths_are_eligible(self):
        for status in ['modified', 'added']:
            with self.subTest(status=status):
                self.client = FakeClient()
                self.configure_active_detail()
                self.compare()['files'] = []
                for manifest_path, _ in DETAIL_REFERENCES.values():
                    record = changed(manifest_path, status)
                    record['sha'] = git_blob_sha(self.client.blobs[(manifest_path, TARGET)])
                    self.compare()['files'].append(record)
                self.reuse()
        self.client = FakeClient()
        self.compare()['files'] = [changed('search/unknown-detail-references.json')]
        self.full()

    def test_realistic_root_copy_diff_includes_active_manifests_query_indexes_and_new_detail(self):
        detail_path = self.add_detail_change()
        detail_record = copy.deepcopy(self.compare()['files'][0])
        self.configure_active_detail(detail_path)
        before = (Path(__file__).resolve().parents[1] / 'index.html').read_bytes()
        pattern = re.compile(
            rb'(<div class="home-feature-copy"><h3><a href="/numerical-methods-atlas/\?lang=en">[^<>]*</a></h3><p>)([^<>]*)(</p>)')
        after, replacements = pattern.subn(lambda match: match[1] + match[2] + b' Read the evidence.' + match[3], before)
        self.assertEqual(replacements, 1)
        self.set_blob_change('index.html', before, after)
        self.compare()['files'].append(detail_record)
        expected_paths = {'index.html', detail_path}
        for manifest_path, index_path in DETAIL_REFERENCES.values():
            manifest_record = changed(manifest_path)
            manifest_record['sha'] = git_blob_sha(self.client.blobs[(manifest_path, TARGET)])
            index_record = changed(index_path)
            index_record['sha'] = self.client.tree_entries[(index_path, TARGET)]['sha']
            self.compare()['files'].extend([manifest_record, index_record])
            expected_paths.update([manifest_path, index_path])
        result = self.reuse()
        self.assertEqual({row['filename'] for row in result['changed_files']}, expected_paths)
        self.assertTrue(all(row['safe'] for row in result['changed_files']))

    def test_an_orphan_detail_cannot_use_its_own_valid_content_hash_as_ownership_proof(self):
        self.add_detail_change()
        self.configure_active_detail()
        result = self.full()
        self.assertEqual(result['reason'], 'unreferenced-derived-detail')

    def test_detail_reference_manifests_require_the_exact_bounded_schema(self):
        for mutation in ['missing_field', 'extra_field', 'schema', 'boolean_schema', 'kind',
                         'index_path', 'git_hash', 'sha256', 'keys_type', 'invalid_key',
                         'duplicate_keys', 'unsorted_keys', 'too_many_keys', 'duplicate_json']:
            with self.subTest(mutation=mutation):
                self.client = FakeClient()
                path = self.add_detail_change()
                self.configure_active_detail(path)
                manifest_path, _ = DETAIL_REFERENCES['site']
                value = json.loads(self.client.blobs[(manifest_path, TARGET)])
                key = value['detail_keys'][0]
                if mutation == 'missing_field': del value['index_sha256']
                if mutation == 'extra_field': value['unreviewed'] = True
                if mutation == 'schema': value['schema_version'] = 2
                if mutation == 'boolean_schema': value['schema_version'] = True
                if mutation == 'kind': value['kind'] = 'other'
                if mutation == 'index_path': value['index_path'] = 'search/other-index.json'
                if mutation == 'git_hash': value['index_git_blob_sha'] = 'not-a-git-hash'
                if mutation == 'sha256': value['index_sha256'] = 'not-a-sha256'
                if mutation == 'keys_type': value['detail_keys'] = key
                if mutation == 'invalid_key': value['detail_keys'] = [key.upper()]
                if mutation == 'duplicate_keys': value['detail_keys'] = [key, key]
                if mutation == 'unsorted_keys': value['detail_keys'] = sorted([key, '0' * 64], reverse=True)
                if mutation == 'too_many_keys': value['detail_keys'] = [format(index, '064x') for index in range(5001)]
                raw = json.dumps(value, sort_keys=True).encode()
                if mutation == 'duplicate_json': raw = raw[:-1] + b',"schema_version":1}'
                self.client.blobs[(manifest_path, TARGET)] = raw
                self.full()

    def test_detail_manifest_and_query_must_be_regular_files_with_matching_git_identities(self):
        for owner, (manifest_path, index_path) in DETAIL_REFERENCES.items():
            for mutation in ['manifest_unavailable', 'manifest_hash', 'manifest_mode',
                             'missing_manifest_mode', 'query_hash', 'query_mode', 'query_unavailable']:
                with self.subTest(owner=owner, mutation=mutation):
                    self.client = FakeClient()
                    path = self.add_detail_change()
                    self.configure_active_detail(path)
                    if mutation == 'manifest_unavailable':
                        self.client.blobs[(manifest_path, TARGET)] = RuntimeError('private-manifest-token-must-not-leak')
                    if mutation in {'manifest_hash', 'manifest_mode', 'missing_manifest_mode'}:
                        entry = {'mode': '100644', 'type': 'blob',
                                 'sha': git_blob_sha(self.client.blobs[(manifest_path, TARGET)])}
                        if mutation == 'manifest_hash': entry['sha'] = MID
                        if mutation == 'manifest_mode': entry['mode'] = '120000'
                        if mutation == 'missing_manifest_mode': del entry['mode']
                        self.client.tree_entries[(manifest_path, TARGET)] = entry
                    if mutation in {'query_hash', 'query_mode', 'query_unavailable'}:
                        entry = self.client.tree_entries[(index_path, TARGET)]
                        if mutation == 'query_hash': entry['sha'] = MID
                        if mutation == 'query_mode': entry['mode'] = '100755'
                        if mutation == 'query_unavailable':
                            self.client.tree_entries[(index_path, TARGET)] = RuntimeError('private-query-token-must-not-leak')
                    result = self.full()
                    self.assertNotIn('private-manifest-token-must-not-leak', str(result))
                    self.assertNotIn('private-query-token-must-not-leak', str(result))

    def test_search_detail_wrong_hash_schema_or_unknown_name_requires_full(self):
        for scenario in ['filename_hash', 'schema', 'unknown_name']:
            with self.subTest(scenario=scenario):
                self.client = FakeClient()
                value = {'text':'Reading'} if scenario != 'schema' else {'text':'Reading','dt':0.01}
                raw = json.dumps(value).encode()
                content_hash = '0'*64 if scenario == 'filename_hash' else hashlib.sha256(raw).hexdigest()
                path = 'search/new-science.json' if scenario == 'unknown_name' else 'search/details/'+content_hash+'.json'
                self.compare()['files'] = [changed(path, 'added')]
                self.compare()['files'][0]['sha'] = git_blob_sha(raw)
                self.client.blobs[(path, TARGET)] = raw
                if scenario != 'unknown_name': self.configure_active_detail(path)
                self.full()

    def test_derived_search_data_and_new_details_cannot_bypass_public_freshness_proof(self):
        raw = b'{"text":"Current reading"}'
        detail_path = 'search/details/' + hashlib.sha256(raw).hexdigest() + '.json'
        for path in ['search/index.json', 'search/query-index.json',
                     'search/atlas-query-index.json', 'search/asset-manifest.json',
                     'numerical-methods-atlas/home-search-index.json', detail_path]:
            with self.subTest(path=path):
                self.client = FakeClient()
                self.compare()['files'] = [changed(path, 'added' if path == detail_path else 'modified')]
                if path == detail_path:
                    self.compare()['files'][0]['sha'] = git_blob_sha(raw)
                    self.client.blobs[(path, TARGET)] = raw
                    self.configure_active_detail(path)
                self.client.responses[PUBLIC_JOBS]['jobs'][0]['steps'] = []
                self.full()

    def test_unknown_or_scientific_change_stays_full_alongside_proven_safe_presentation(self):
        for path in ['code/fixed-input.json', 'data/reference-values.json',
                     'catalog/atlas-depth.json', 'downloads/existing.ZIP',
                     'scripts/verify-depth-public.py', 'unknown/science.dat']:
            with self.subTest(path=path):
                self.client = FakeClient()
                self.compare()['files'] = [changed('site.css'), changed(path)]
                self.full()

    def cache_import_change(self):
        path = 'numerical-methods-atlas/home-navigation.mjs'
        dependency = 'numerical-methods-atlas/atlas-home-data.js'
        before = (b"import {homeAreas} from './home-overview-data.js?v=111111111111';\n"
                  b"import {homeNavigationData} from './atlas-home-data.js?v=222222222222';\n"
                  b'export const choose=()=>true;\n')
        dependency_before = b'export const homeNavigationData={"label":"Old wording"};\n'
        dependency_after = b'export const homeNavigationData={"label":"New wording"};\n'
        version = hashlib.sha256(dependency_after).hexdigest()[:12].encode()
        after = before.replace(b'222222222222', version)
        self.set_blob_change(path, before, after)
        return path, dependency, dependency_before, dependency_after

    def test_unaccompanied_cache_token_edits_cannot_reuse_a_full_run(self):
        self.cache_import_change()
        result = self.full()
        self.assertEqual(result['reason'], 'unproven-presentation-cache-version')

    def test_cache_change_needs_its_declared_generated_dependency_and_unchanged_source_owner(self):
        path, dependency, before, after = self.cache_import_change()
        record = changed(dependency)
        record['sha'] = git_blob_sha(after)
        self.compare()['files'].append(record)
        self.client.blobs[(dependency, BASE)] = before
        self.client.blobs[(dependency, TARGET)] = after
        result = self.reuse()
        cache = next(row for row in result['changed_files'] if row['filename'] == path)
        self.assertIn(dependency, [item['path'] for item in cache['presentation_cache_dependencies']])
        self.assertIn(PUBLIC_JOBS, self.client.calls)
        self.compare()['files'].append(changed('frontend/atlas/app.js'))
        self.full()

    def test_shared_site_css_and_js_cache_group_requires_a_safe_stylesheet_change(self):
        root = Path(__file__).resolve().parents[1]
        before = (root / 'index.html').read_bytes()
        css_before = (root / 'site.css').read_bytes()
        css_after = css_before + b'\n.home-main { outline-offset: 0; }\n'
        script_before = (root / 'site.js').read_bytes()
        version = hashlib.sha256(css_after + script_before).hexdigest()[:12].encode()
        pattern = re.compile(rb'((?:href|src)="/site\.(?:css|js)\?v=)([0-9a-f]{12})(")')
        after, replacements = pattern.subn(lambda match: match[1] + version + match[3], before)
        self.assertEqual(replacements, 2, 'site.css and site.js share their actual combined asset version')
        self.set_blob_change('index.html', before, after)
        self.full()
        css_record = changed('site.css')
        css_record['sha'] = git_blob_sha(css_after)
        self.compare()['files'].append(css_record)
        self.client.blobs[('site.css', BASE)] = css_before
        self.client.blobs[('site.css', TARGET)] = css_after
        self.reuse()
        script_after = script_before + b'\nwindow.unreviewedScopeFixture = true;\n'
        script_record = changed('site.js')
        script_record['sha'] = git_blob_sha(script_after)
        self.compare()['files'].append(script_record)
        self.client.blobs[('site.js', BASE)] = script_before
        self.client.blobs[('site.js', TARGET)] = script_after
        self.full()

    def test_actual_root_copy_and_search_main_query_cache_change_reuse_with_derived_query(self):
        root = Path(__file__).resolve().parents[1]
        root_before = (root / 'index.html').read_bytes()
        copy_changes = [
            ('ja', '人が式・条件・図・参照値から根拠を読み、AIも同じ公開条件で実行・検証できる、数値計算テスト問題ライブラリです。',
             '人が式・条件・図・参照値を読んで確かめ、AIも同じ公開条件で実行・検証できる、数値計算テスト問題ライブラリです。'),
            ('en', 'A numerical test-problem library where people can inspect equations, conditions, figures and references, and AI agents can run and verify code under the same published conditions.',
             'A numerical test-problem library where people can read and check equations, conditions, figures and references, and AI agents can run and verify code under the same published conditions.'),
        ]
        # Preserve the actual DOM while choosing fixture text independently of
        # whatever legitimate introduction wording is currently published.
        slots = []
        for language, old, new in copy_changes:
            pattern = re.compile(
                rb'(<div class="home-feature-copy"><h3><a href="/numerical-methods-atlas/\?lang='
                + language.encode() + rb'">[^<>]*</a></h3><p>)([^<>]*)(</p>)')
            root_before, replacements = pattern.subn(
                lambda match: match[1] + old.encode() + match[3], root_before)
            self.assertEqual(replacements, 1, 'retain exactly one actual NaN introduction DOM per language')
            slots.append((pattern, new.encode()))
        root_after = root_before
        for pattern, new in slots:
            root_after, replacements = pattern.subn(lambda match: match[1] + new + match[3], root_after)
            self.assertEqual(replacements, 1)
        query_path = 'search/query-index.json'
        query_after = b'{"kind":"site","fixture_label":"Read and check the evidence"}'
        version = hashlib.sha256(query_after).hexdigest()[:12].encode()
        search_path = 'search/index.html'
        search_before = (root / search_path).read_bytes()
        self.assertIn(b'<main class="profile-main search-main"', search_before)
        pattern = re.compile(rb'(data-search-index="/search/query-index.json\?v=)([0-9a-f]{12})(")')
        search_after, replacements = pattern.subn(lambda match: match[1] + version + match[3], search_before)
        self.assertEqual(replacements, 1, 'use the actual search main query-index attribute')
        self.set_blob_change('index.html', root_before, root_after)
        for path, before, after in [(query_path, None, query_after), (search_path, search_before, search_after)]:
            record = changed(path)
            record['sha'] = git_blob_sha(after)
            self.compare()['files'].append(record)
            self.client.blobs[(path, TARGET)] = after
            if before is not None:
                self.client.blobs[(path, BASE)] = before
        result = self.reuse()
        self.assertEqual({row['filename'] for row in result['changed_files']},
                         {'index.html', query_path, search_path})
        safe_records = copy.deepcopy(self.compare()['files'])
        count_changed, counts = re.subn(rb'(data-search-count=")([0-9]+)(")',
            lambda match: match[1] + str(int(match[2]) + 1).encode() + match[3], search_after, count=1)
        self.assertEqual(counts, 1)
        for mutation, invalid in [
                ('query_url', search_after.replace(b'data-search-index="/search/query-index.json?',
                                                   b'data-search-index="/search/unreviewed-index.json?', 1)),
                ('count', count_changed),
                ('script', search_after.replace(b'src="/search/search.js?',
                                                b'src="/search/unreviewed-search.js?', 1))]:
            with self.subTest(mutation=mutation):
                self.assertNotEqual(invalid, search_after)
                self.compare()['files'] = copy.deepcopy(safe_records)
                record = next(item for item in self.compare()['files'] if item['filename'] == search_path)
                record['sha'] = git_blob_sha(invalid)
                self.client.blobs[(search_path, TARGET)] = invalid
                self.full()

    def test_actual_root_intro_copy_is_reusable_until_a_scientific_change_is_mixed_in(self):
        path = 'index.html'
        before = (Path(__file__).resolve().parents[1] / path).read_bytes()
        pattern = re.compile(
            rb'(<div class="home-feature-copy"><h3><a href="/numerical-methods-atlas/\?lang=en">[^<>]*</a></h3><p>)([^<>]*)(</p>)')
        after, replacements = pattern.subn(lambda match: match[1] + match[2] + b' Read the evidence.' + match[3], before)
        self.assertEqual(replacements, 1, 'use the actual existing atlas introduction on the root page')
        self.set_blob_change(path, before, after)
        self.reuse()
        root_record = copy.deepcopy(self.compare()['files'][0])
        for critical in ['code/fixed-input.json', 'data/reference-values.json',
                         'catalog/atlas-depth.json', 'downloads/existing.ZIP',
                         'scripts/verify-depth-public.py', 'unknown/science.dat']:
            with self.subTest(critical=critical):
                self.compare()['files'] = [root_record, changed(critical)]
                self.full()

    def test_mixed_science_and_metadata_since_full_cannot_be_laundered_by_skip(self):
        skipped = run_record(200, MID, when='2026-11-26T12:10:00Z')
        self.client.responses[RUNS] = {'total_count': 2, 'workflow_runs': [skipped, run_record()]}
        self.client.responses['/actions/runs/200/attempts/1/jobs?per_page=100'] = {
            'total_count': 1, 'jobs': [job_record(2000, 'skipped', 200, MID)]}
        self.compare()['files'] += [changed('code/new-input.json')]
        self.full()
        self.assertIn(f'/compare/{BASE}...{TARGET}?per_page=1&page=1', self.client.calls)
        self.assertNotIn(f'/compare/{MID}...{TARGET}?per_page=1&page=1', self.client.calls)

    def test_latest_full_failure_is_a_barrier_even_with_older_success(self):
        for conclusion in ['failure', 'cancelled', 'timed_out']:
            with self.subTest(conclusion=conclusion):
                self.client = FakeClient()
                failed = run_record(200, BASE, conclusion, '2026-11-26T12:10:00Z')
                self.client.responses[RUNS] = {'workflow_runs': [failed, run_record()]}
                self.client.responses['/actions/runs/200/attempts/1/jobs?per_page=100'] = {
                    'total_count': 1, 'jobs': [job_record(2000, conclusion, 200)]}
                self.full()
                self.assertNotIn('/actions/runs/100/attempts/1/jobs?per_page=100', self.client.calls)

    def test_successful_job_inside_failed_workflow_is_not_reusable(self):
        self.client.responses[RUNS]['workflow_runs'][0]['conclusion'] = 'failure'
        self.full()

    def test_success_without_real_execution_step_is_not_a_full_baseline(self):
        self.client.responses['/actions/runs/100/attempts/1/jobs?per_page=100']['jobs'][0]['steps'] = []
        self.full()

    def test_old_failure_does_not_poison_later_full_success(self):
        older = run_record(50, MID, 'failure', '2026-11-25T12:00:00Z')
        self.client.responses[RUNS]['workflow_runs'].append(older)
        self.reuse()

    def test_rerun_updated_time_not_run_number_determines_latest_full_attempt(self):
        retried_failure = run_record(50, BASE, 'failure', '2026-11-26T13:00:00Z')
        retried_failure['run_attempt'] = 2
        retried_failure['run_number'] = 50
        good = run_record(); good['run_number'] = 100
        self.client.responses[RUNS] = {'workflow_runs': [good, retried_failure]}
        self.client.responses['/actions/runs/50/attempts/2/jobs?per_page=100'] = {
            'total_count': 1, 'jobs': [job_record(500, 'failure', 50)]}
        self.full()
        self.assertIn('/actions/runs/50/attempts/2/jobs?per_page=100', self.client.calls)
        self.assertNotIn('/actions/runs/100/attempts/1/jobs?per_page=100', self.client.calls)

    def test_recent_failed_ancient_rerun_outside_general_window_blocks_reuse(self):
        self.client.responses[RUNS] = {'total_count': 500,
            'workflow_runs': [run_record(identifier) for identifier in range(100,200)]}
        failed = run_record(1, BASE, 'failure', '2026-11-26T13:00:00Z'); failed['run_attempt'] = 2
        self.client.responses[FAILURE_RUNS['failure']] = {'total_count':1,'workflow_runs':[failed]}
        self.client.responses['/actions/runs/1/attempts/2/jobs?per_page=100'] = {
            'total_count':1,'jobs':[job_record(10,'failure',1)]}
        result = self.full()
        self.assertEqual(result['reason'], 'latest-full-attempt-not-successful')
        self.assertIn('/actions/runs/1/attempts/2/jobs?per_page=100', self.client.calls)
        self.assertNotIn('/actions/runs/100/attempts/1/jobs?per_page=100', self.client.calls)

    def test_filtered_failure_history_must_be_complete_and_available(self):
        for status, endpoint in FAILURE_RUNS.items():
            for scenario in ['truncated','api_error','wrong_conclusion']:
                with self.subTest(status=status, scenario=scenario):
                    self.client = FakeClient()
                    if scenario == 'truncated':
                        self.client.responses[endpoint] = {'total_count':1,'workflow_runs':[]}
                    elif scenario == 'api_error':
                        self.client.responses[endpoint] = RuntimeError('secret-value-must-not-leak')
                    else:
                        self.client.responses[endpoint] = {'total_count':1,'workflow_runs':[run_record()]}
                    result = self.full()
                    self.assertNotIn('secret-value-must-not-leak', str(result))

    def test_no_history_and_all_skips_require_full(self):
        self.client.responses[RUNS] = {'workflow_runs': []}
        self.full()
        self.client = FakeClient()
        self.client.responses['/actions/runs/100/attempts/1/jobs?per_page=100']['jobs'][0]['conclusion'] = 'skipped'
        self.full()

    def test_incomplete_or_ambiguous_jobs_require_full(self):
        for mutate in ['partial', 'duplicate', 'incomplete']:
            with self.subTest(mutate=mutate):
                self.client = FakeClient()
                jobs = self.client.responses['/actions/runs/100/attempts/1/jobs?per_page=100']
                if mutate == 'partial': jobs['total_count'] = 2
                if mutate == 'duplicate':
                    jobs['jobs'].append(job_record(1001)); jobs['total_count'] = 2
                if mutate == 'incomplete': jobs['jobs'][0]['status'] = 'in_progress'
                self.full()

    def test_retry_attempt_does_not_reuse_an_earlier_attempts_scientific_job(self):
        self.client.responses[RUNS]['workflow_runs'][0]['run_attempt'] = 2
        self.client.responses['/actions/runs/100/attempts/2/jobs?per_page=100'] = {
            'total_count': 1, 'jobs': [{'id': 1002, 'name': 'classify-changes',
                'status': 'completed', 'conclusion': 'success', 'steps': []}]}
        self.full()
        self.assertIn('/actions/runs/100/attempts/2/jobs?per_page=100', self.client.calls)
        self.assertNotIn('/actions/runs/100/attempts/1/jobs?per_page=100', self.client.calls)

    def test_baseline_job_must_belong_to_the_selected_run_and_commit(self):
        for key, value in [('run_id', 101), ('head_sha', MID)]:
            with self.subTest(key=key):
                self.client = FakeClient()
                self.client.responses['/actions/runs/100/attempts/1/jobs?per_page=100']['jobs'][0][key] = value
                self.full()

    def test_incomplete_or_wrong_history_requires_full(self):
        for mutation in ['missing', 'in_progress', 'other_repository', 'other_branch']:
            with self.subTest(mutation=mutation):
                self.client = FakeClient()
                run = self.client.responses[RUNS]['workflow_runs'][0]
                if mutation == 'missing': del run['head_sha']
                if mutation == 'in_progress': run['status'] = 'in_progress'
                if mutation == 'other_repository': run['head_repository']['full_name'] = 'elsewhere/project'
                if mutation == 'other_branch': run['head_branch'] = 'other'
                self.full()

    def test_compare_at_300_file_cap_requires_full(self):
        self.compare()['files'] = [changed(f'docs/page-{n}.md') for n in range(300)]
        self.full()

    def test_compare_must_be_ancestral_and_complete(self):
        for mutate in ['diverged', 'wrong_base', 'no_files', 'malformed_file']:
            with self.subTest(mutate=mutate):
                self.client = FakeClient()
                value = self.compare()
                if mutate == 'diverged': value['status'] = 'diverged'
                if mutate == 'wrong_base': value['merge_base_commit']['sha'] = MID
                if mutate == 'no_files': del value['files']
                if mutate == 'malformed_file': value['files'][0]['sha'] = 'not-a-sha'
                self.full()

    def test_api_failures_cannot_produce_reuse(self):
        for endpoint in ['/git/ref/heads/main', PUBLIC_RUN, PUBLIC_JOBS, RUNS,
                         '/actions/runs/100/attempts/1/jobs?per_page=100',
                         f'/compare/{BASE}...{TARGET}?per_page=1&page=1']:
            with self.subTest(endpoint=endpoint):
                self.client = FakeClient(); self.client.responses[endpoint] = RuntimeError('private-token-must-not-leak')
                result = self.full()
                self.assertNotIn('private-token-must-not-leak', str(result))

    def test_malformed_main_reference_requires_full_instead_of_reuse(self):
        self.client.responses['/git/ref/heads/main'] = {}
        self.full()

    def test_retry_is_full_even_if_its_prior_failed_attempt_disappears_from_listing(self):
        # GitHub lists the latest in-progress attempt; the previous attempt's
        # scientific failure may no longer appear under status=completed/failure.
        value = self.choose(run_attempt=2)
        self.assertEqual(value['mode'], 'full')
        self.assertTrue(value['run_full'])
        self.assertEqual(value['reason'], 'workflow-retry-always-full')
        self.assertEqual(value['run_attempt'], 2)
        self.assertNotIn(RUNS, self.client.calls)
        self.client.responses['/git/ref/heads/main']['object']['sha'] = MID
        with self.assertRaises(InvalidEvent):
            self.choose(run_attempt=2)

    def test_invalid_run_attempt_does_not_authorize_reuse(self):
        for attempt in [0, -1, True, '2']:
            with self.subTest(attempt=attempt), self.assertRaises(InvalidEvent):
                self.choose(run_attempt=attempt)

    def test_missing_current_attempt_is_full_instead_of_assuming_first_attempt(self):
        value = self.choose(run_attempt=None)
        self.assertEqual(value['mode'], 'full')
        self.assertEqual(value['reason'], 'missing-current-run-attempt')
        code, value, output = self.run_cli(run_attempt=None)
        self.assertEqual(code, 0)
        self.assertEqual(value['reason'], 'missing-current-run-attempt')
        self.assertIn('run_full=true', output)

    def test_other_queued_or_active_retry_cannot_hide_its_prior_full_failure(self):
        for status in ['queued', 'in_progress', 'waiting', 'pending', 'requested']:
            with self.subTest(status=status):
                self.client = FakeClient()
                retry = run_record(50, MID); retry.update(status=status, conclusion=None, run_attempt=2)
                endpoint = RUNS.replace('status=completed', 'status='+status)
                self.client.responses[endpoint] = {'total_count': 1, 'workflow_runs': [retry]}
                self.assertEqual(self.full()['reason'], 'concurrent-retry-history-uncertain')

    def test_first_attempt_active_history_is_complete_and_stable_before_reuse(self):
        endpoint = RUNS.replace('status=completed', 'status=queued')
        fresh = run_record(200, MID); fresh.update(status='queued', conclusion=None)
        self.client.responses[endpoint] = {'total_count': 1, 'workflow_runs': [fresh]}
        self.reuse()
        for scenario in ['incomplete', 'unavailable', 'unknown_attempt']:
            with self.subTest(scenario=scenario):
                self.client = FakeClient()
                value = {'total_count': 1, 'workflow_runs': [fresh]}
                if scenario == 'incomplete': value['workflow_runs'] = []
                if scenario == 'unavailable': value = RuntimeError('private-token-must-not-leak')
                if scenario == 'unknown_attempt':
                    value = copy.deepcopy(value); value['workflow_runs'][0].pop('run_attempt')
                self.client.responses[endpoint] = value
                result = self.full(); self.assertNotIn('private-token-must-not-leak', str(result))
        self.client = FakeClient(); get = self.client.get; reads = []
        def changing_get(path):
            if path == endpoint:
                reads.append(path)
                if len(reads) == 2:
                    return {'total_count': 1, 'workflow_runs': [fresh]}
            return get(path)
        with mock.patch.object(self.client, 'get', side_effect=changing_get):
            self.assertEqual(self.full()['reason'], 'active-history-changed-during-classification')

    def test_manual_and_weekly_events_always_execute_full(self):
        for event in ['workflow_dispatch', 'schedule']:
            with self.subTest(event=event):
                result = self.choose(event_name=event, event={})
                self.assertTrue(result['run_full']); self.assertEqual(result['mode'], 'full')

    def test_untrusted_event_and_mismatched_checked_commit_are_errors(self):
        cases = [{'repo': 'koyamarium/project'}, {'ref': 'refs/heads/other'},
                 {'event_name': 'push'}, {'sha': 'bad'}, {'sha': MID}]
        for kwargs in cases:
            with self.subTest(kwargs=kwargs), self.assertRaises(InvalidEvent):
                self.choose(**kwargs)
        for key, value in [('conclusion', 'failure'), ('head_branch', 'other'),
                           ('head_repository', {'full_name': 'other/project'})]:
            event = copy.deepcopy(self.event); event['workflow_run'][key] = value
            with self.subTest(key=key), self.assertRaises(InvalidEvent): self.choose(event=event)

    def test_superseded_main_cannot_be_claimed_as_verified(self):
        self.client.responses['/git/ref/heads/main']['object']['sha'] = MID
        with self.assertRaises(InvalidEvent): self.choose()

    def test_prose_only_generated_html_still_requires_an_active_owner(self):
        path = 'numerical-methods-atlas/ja/read/example/index.html'
        before = b'<main><h1>Old heading</h1><p>Old prose</p></main>'
        after = before.replace(b'Old', b'New')
        self.compare()['files'] = [changed(path)]
        self.compare()['files'][0]['sha'] = git_blob_sha(after)
        self.client.blobs[(path, BASE)] = before
        self.client.blobs[(path, TARGET)] = after
        self.full()

    def test_known_ui_scripts_do_not_prove_a_generated_html_owner(self):
        path = 'numerical-methods-atlas/ja/read/example/index.html'
        for script in ['site.js','numerical-methods-atlas/reading.js','numerical-methods-atlas/reading-index.mjs']:
            with self.subTest(script=script):
                self.client = FakeClient()
                before = ('<main><h1>Old heading</h1><script src="/'+script+'?v=known"></script></main>').encode()
                self.set_blob_change(path, before, before.replace(b'Old',b'New'))
                self.full()

    def test_html_with_inline_dom_reader_or_unknown_external_script_requires_full(self):
        path = 'numerical-methods-atlas/index.html'
        pairs = [
            (b'<div id="boundary">periodic</div><script>let boundary=document.querySelector("#boundary").textContent;</script>',
             b'<div id="boundary">dirichlet</div><script>let boundary=document.querySelector("#boundary").textContent;</script>'),
            (b'<h1>Old heading</h1><script src="/unknown-solver.js"></script>',
             b'<h1>New heading</h1><script src="/unknown-solver.js"></script>'),
            (b'<h1>Old heading</h1><script src="https://other.example/solver.js"></script>',
             b'<h1>New heading</h1><script src="https://other.example/solver.js"></script>'),
        ]
        for before, after in pairs:
            with self.subTest(before=before):
                self.client = FakeClient(); self.set_blob_change(path, before, after); self.full()

    def test_html_parameters_code_and_event_handlers_trigger_full(self):
        pairs = [
            (b'<script>let a=1;</script>', b'<script>let a=2;</script>'),
            (b'<input value="1">', b'<input value="2">'),
            (b'<div data-cfl=".2">text</div>', b'<div data-cfl=".3">text</div>'),
            (b'<button onclick="f(1)">go</button>', b'<button onclick="f(2)">go</button>'),
            (b'<textarea>1</textarea>', b'<textarea>2</textarea>'),
            (b'<select><option>1</option></select>', b'<select><option>2</option></select>'),
            (b'<script type="application/json">{"dt":1}</script>', b'<script type="application/json">{"dt":2}</script>'),
            (b'<div id="dx">dx=0.01</div>', b'<div id="dx">dx=0.02</div>'),
            (b'<input value="1" value="2">', b'<input value="2" value="1">'),
        ]
        path = 'numerical-methods-atlas/index.html'
        for before, after in pairs:
            with self.subTest(before=before):
                self.client = FakeClient(); self.compare()['files'] = [changed(path)]
                self.compare()['files'][0]['sha'] = git_blob_sha(after)
                self.client.blobs[(path, BASE)] = before; self.client.blobs[(path, TARGET)] = after
                self.full()

    def test_html_blob_unavailable_requires_full(self):
        self.compare()['files'] = [changed('numerical-methods-atlas/index.html')]
        self.full()

    def test_known_spa_intro_copy_can_change_with_numerical_content_kept_exact(self):
        path = 'numerical-methods-atlas/index.html'
        before = b'<main><h1 id="home-landing-title-en">Old description</h1><p>dx=0.01 and 64 cells</p></main>'
        after = before.replace(b'Old description', b'New wording')
        self.compare()['files'] = [changed(path)]; self.compare()['files'][0]['sha'] = git_blob_sha(after)
        self.client.blobs[(path, BASE)] = before; self.client.blobs[(path, TARGET)] = after
        self.reuse()

    def test_unknown_html_and_wrong_target_blob_are_not_reusable(self):
        for path in ['about/index.html', 'numerical-methods-atlas/index.html']:
            with self.subTest(path=path):
                self.client = FakeClient(); self.compare()['files'] = [changed(path)]
                self.client.blobs[(path, BASE)] = b'<p>old</p>'
                self.client.blobs[(path, TARGET)] = b'<p>new</p>'
                self.full()

    def test_renames_deletions_and_unsafe_paths_require_full(self):
        for status in ['renamed', 'removed', 'copied', 'unknown']:
            with self.subTest(status=status):
                self.compare()['files'] = [changed('docs/copy.md', status)]
                self.full()
        for path in ['docs/../../code/source.md', '/docs/copy.md', 'docs\\copy.md']:
            with self.subTest(path=path):
                self.compare()['files'] = [changed(path)]
                self.full()

    def run_cli(self, *, api_error=False, sha=TARGET, run_attempt=1):
        spec = importlib.util.spec_from_file_location('atlas_scope_cli_test',
            Path(__file__).with_name('plan-atlas-depth-ci.py'))
        cli = importlib.util.module_from_spec(spec); spec.loader.exec_module(cli)
        if api_error:
            self.client.responses[RUNS] = RuntimeError('secret-value-must-not-leak')
        with tempfile.TemporaryDirectory(prefix='atlas-depth-scope-cli-') as directory:
            root = Path(directory)
            event_path = root/'event.json'; event_path.write_text(json.dumps(self.event))
            report_path, output_path = root/'plan.json', root/'github-output'
            environment = {'GITHUB_EVENT_NAME':'workflow_run','GITHUB_EVENT_PATH':str(event_path),
                'GITHUB_SHA':sha,'GITHUB_REF':'refs/heads/main','GITHUB_REPOSITORY':REPO,
                'GITHUB_RUN_ID':'10000','GITHUB_RUN_ATTEMPT':str(run_attempt),
                'GITHUB_TOKEN':'secret-value-must-not-leak'}
            if run_attempt is None:
                environment.pop('GITHUB_RUN_ATTEMPT')
            with mock.patch.dict(os.environ, environment, clear=True), \
                 mock.patch.object(cli, 'Client', return_value=self.client), \
                 mock.patch.object(sys, 'argv', ['plan-atlas-depth-ci.py','--output',str(report_path),'--github-output',str(output_path)]), \
                 redirect_stdout(io.StringIO()):
                code = cli.main()
            return code, json.loads(report_path.read_text()), output_path.read_text()

    def test_cli_emits_reuse_and_exact_target_without_running_science(self):
        code, report, output = self.run_cli()
        self.assertEqual(code, 0); self.assertEqual(report['mode'], 'reuse')
        self.assertEqual(dict(line.split('=',1)for line in output.splitlines()),
            {'run_full':'false','mode':'reuse','target_sha':TARGET})
        self.assertFalse(report['numerical_execution_performed_by_planner'])

    def test_cli_passes_the_real_workflow_attempt_to_the_fail_closed_retry_gate(self):
        code, report, output = self.run_cli(run_attempt=2)
        self.assertEqual(code, 0)
        self.assertEqual(report['mode'], 'full')
        self.assertEqual(report['reason'], 'workflow-retry-always-full')
        self.assertIn('run_full=true', output)
        code, report, output = self.run_cli(run_attempt=0)
        self.assertEqual(code, 1)
        self.assertEqual(report['mode'], 'blocked')

    def test_cli_uncertain_api_emits_full_and_sanitizes_private_error(self):
        code, report, output = self.run_cli(api_error=True)
        self.assertEqual(code, 0); self.assertTrue(report['run_full'])
        self.assertIn('run_full=true', output)
        self.assertNotIn('secret-value-must-not-leak', str(report)+output)

    def test_cli_rejects_invalid_target_without_github_output_injection(self):
        code, report, output = self.run_cli(sha=TARGET+'\nrun_full=true')
        self.assertEqual(code, 1); self.assertEqual(report['mode'], 'blocked')
        parsed = dict(line.split('=',1)for line in output.splitlines())
        self.assertEqual(parsed['run_full'], 'false'); self.assertEqual(parsed['mode'], 'blocked')
        self.assertEqual(parsed.get('target_sha', ''), '')


class ClientBudgetTests(unittest.TestCase):
    """Exercise the real transport's bounds with an in-memory opener only."""
    endpoint = '/git/ref/heads/main'

    def client(self, raw=b'{}', *, status=200, response_url=None):
        client = Client('test-token-never-transmitted')
        self.requests = []
        requests = self.requests
        endpoint = self.endpoint

        class Response:
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def geturl(self): return response_url or 'https://api.github.com/repos/' + REPO + endpoint
            def read(self, count): return raw[:count]

        class Opener:
            def open(self, request, timeout):
                requests.append((request.full_url, timeout))
                self_response = Response()
                self_response.status = status
                return self_response

        client.opener = Opener()
        return client

    def test_deadline_stops_api_access_before_opening_a_connection(self):
        client = self.client()
        client.deadline = 0
        with self.assertRaises(ScopeError): client.get(self.endpoint)
        self.assertEqual(self.requests, [])

    def test_individual_and_cumulative_response_budgets_reject_oversize_data(self):
        client = self.client(b' ' * (8 * 1024 * 1024 + 1))
        with self.assertRaises(ScopeError): client.get(self.endpoint)
        client = self.client()
        client.total_bytes = 32 * 1024 * 1024
        with self.assertRaises(ScopeError): client.get(self.endpoint)

    def test_wrong_http_identity_and_nonfinite_or_duplicate_json_are_rejected(self):
        for options in [{'status': 206}, {'response_url': 'https://other.example/private-token'},
                        {'raw': b'{"key":1,"key":2}'}, {'raw': b'{"x":NaN}'},
                        {'raw': b'{"x":1e999}'}]:
            with self.subTest(options=options):
                client = self.client(**options)
                with self.assertRaises(ValueError) as caught: client.get(self.endpoint)
                self.assertNotIn('test-token-never-transmitted', str(caught.exception))

    def tree_client(self):
        client = Client('test-token-never-transmitted')
        root_sha, directory_sha = 'e' * 40, 'f' * 40
        responses = {
            '/git/commits/' + BASE: {'sha': BASE, 'tree': {'sha': root_sha}},
            '/git/trees/' + root_sha: {'sha': root_sha, 'truncated': False, 'tree': [
                {'path': 'catalog', 'mode': '040000', 'type': 'tree', 'sha': directory_sha}]},
            '/git/trees/' + directory_sha: {'sha': directory_sha, 'truncated': False, 'tree': [
                {'path': 'atlas-identities.json', 'mode': '100644', 'type': 'blob', 'sha': 'd' * 40}]},
        }
        calls = []

        def get(endpoint):
            calls.append(endpoint)
            return copy.deepcopy(responses[endpoint])

        client.get = get
        return client, responses, calls

    def test_tree_walk_uses_immutable_nonrecursive_bounded_responses(self):
        client, _, calls = self.tree_client()
        path = 'catalog/atlas-identities.json'
        expected = {'mode': '100644', 'type': 'blob', 'sha': 'd' * 40}
        self.assertEqual(client.tree_entry(path, BASE), expected)
        self.assertEqual(client.tree_entry(path, BASE), expected)
        self.assertEqual(len(calls), 3, 'cached immutable ancestors need not be acquired again')
        self.assertFalse(any('recursive' in endpoint for endpoint in calls))

    def test_tree_walk_rejects_truncation_ambiguity_missing_paths_and_request_exhaustion(self):
        for mutation in ['truncated', 'missing_truncated', 'wrong_commit', 'wrong_tree',
                         'duplicate', 'missing_path', 'symlink_ancestor', 'budget']:
            with self.subTest(mutation=mutation):
                client, responses, _ = self.tree_client()
                root = responses['/git/trees/' + 'e' * 40]
                if mutation == 'truncated': root['truncated'] = True
                if mutation == 'missing_truncated': del root['truncated']
                if mutation == 'wrong_commit': responses['/git/commits/' + BASE]['sha'] = MID
                if mutation == 'wrong_tree': root['sha'] = MID
                if mutation == 'duplicate': root['tree'] *= 2
                if mutation == 'missing_path': root['tree'] = []
                if mutation == 'symlink_ancestor': root['tree'][0].update(mode='120000', type='blob')
                if mutation == 'budget': client.trees = {str(index): {} for index in range(64)}
                with self.assertRaises(ScopeError): client.tree_entry('catalog/atlas-identities.json', BASE)

    def test_content_acquisition_rejects_dereferenced_links_wrong_identity_and_budget_overruns(self):
        raw = b'Known content'
        original = {'type': 'file', 'encoding': 'base64', 'size': len(raw),
                    'content': base64.b64encode(raw).decode(), 'sha': git_blob_sha(raw)}
        for mutation in ['symlink', 'encoding', 'base64', 'size', 'boolean_size',
                         'blob_sha', 'individual_budget', 'total_budget']:
            with self.subTest(mutation=mutation):
                client = Client('test-token-never-transmitted')
                response = copy.deepcopy(original)
                if mutation == 'symlink': response['type'] = 'symlink'
                if mutation == 'encoding': response['encoding'] = 'none'
                if mutation == 'base64': response['content'] = 'invalid!!!'
                if mutation == 'size': response['size'] += 1
                if mutation == 'boolean_size': response['size'] = True
                if mutation == 'blob_sha': response['sha'] = MID
                if mutation == 'individual_budget': response['size'] = 1024 * 1024 + 1
                if mutation == 'total_budget': client.html_bytes = 4 * 1024 * 1024
                client.get = lambda endpoint: copy.deepcopy(response)
                with self.assertRaises(ScopeError): client.blob('catalog/atlas-home.json', BASE)


if __name__ == '__main__':
    unittest.main()
