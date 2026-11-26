"""Offline regressions for the public-ZIP execution selector, without science."""
import copy
from contextlib import redirect_stdout
import importlib.util
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

from atlas_depth_scope import InvalidEvent, VETTED_PRESENTATION_BLOBS, classify_change, html_signature, plan


REPO = 'hrkoyama/hrkoyama.github.io'
BASE = 'a' * 40
TARGET = 'b' * 40
MID = 'c' * 40
RUNS = '/actions/workflows/atlas-depth-linux.yml/runs?branch=main&status=completed&per_page=100'
FAILURE_RUNS = {status: RUNS.replace('status=completed', 'status='+status)
                for status in ['failure', 'cancelled', 'timed_out']}
STEP = 'Install three pinned wheel dependencies and verify public ZIPs'


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
            RUNS: {'total_count': 1, 'workflow_runs': [run_record()]},
            '/actions/runs/100/attempts/1/jobs?per_page=100':
                {'total_count': 1, 'jobs': [job_record()]},
            f'/compare/{BASE}...{TARGET}?per_page=1&page=1': {
                'status': 'ahead', 'merge_base_commit': {'sha': BASE},
                'files': [changed('catalog/atlas-identities.json')]},
        }
        self.blobs = {}
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


class ScopeTests(unittest.TestCase):
    def setUp(self):
        self.client = FakeClient()
        self.event = {'workflow_run': {'id': 999, 'name': 'Public site checks',
            'head_sha': TARGET, 'head_branch': 'main', 'conclusion': 'success',
            'head_repository': {'full_name': REPO}}}

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

    def add_vetted_ui_blobs(self):
        for path, expected in VETTED_PRESENTATION_BLOBS.items():
            raw = (Path(__file__).resolve().parents[1]/path).read_bytes()
            self.assertEqual(git_blob_sha(raw), expected, 'UI fixture must use the reviewed immutable source')
            self.client.blobs[(path, TARGET)] = raw

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

    def test_all_explicit_prose_and_id_changes_are_eligible(self):
        for path in ['README.md', 'MAINTENANCE.md', 'docs/atlas-identities.md',
                     'catalog/atlas-identities.json', 'catalog/atlas-identity-history.json',
                     'catalog/identity-snapshots/NMA-P-000004/00.json',
                     'catalog/atlas-home.json', 'guide/index.json',
                     'site.css', 'styles/atlas-resources.css',
                     'search/atlas-query-index.json',
                     'numerical-methods-atlas/problems/advection-sine/index.json']:
            with self.subTest(path=path):
                self.compare()['files'] = [changed(path)]
                if path == 'catalog/atlas-home.json':
                    self.set_blob_change(path, {'title':{'ja':'Old text'}}, {'title':{'ja':'New text'}})
                if path == 'numerical-methods-atlas/problems/advection-sine/index.json':
                    self.set_blob_change(path, {'name':{'ja':'Old title'}}, {'name':{'ja':'New title'}})
                self.reuse()

    def test_added_id_snapshot_can_be_metadata_only(self):
        self.compare()['files'] = [changed('catalog/identity-snapshots/NMA-P-000004/00.json', 'added')]
        self.reuse()

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
        original = {'id':'home','title':{'ja':'Old overview','en':'Atlas'},
            'count':3,'acceptance':{'tol':1e-8},'path':'/numerical-methods-atlas/'}
        revised = copy.deepcopy(original); revised['title']['ja'] = 'New overview'
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

    def test_generated_problem_descriptor_preserves_numerical_parameters(self):
        path = 'numerical-methods-atlas/problems/advection-sine/index.json'
        original = {'id':'advection-sine','name':{'ja':'Old title','en':'Sine'},
                    'conditions':{'nx':64}}
        revised = copy.deepcopy(original); revised['name']['ja'] = 'New wording'
        self.set_blob_change(path, original, revised); self.reuse()
        revised['conditions']['nx'] = 128
        self.set_blob_change(path, original, revised); self.full()

    def test_added_content_addressed_search_detail_is_verified_as_text(self):
        raw = json.dumps({'text':{'ja':'Current reading','en':'Reference'}},
                         separators=(',',':')).encode()
        path = 'search/details/'+hashlib.sha256(raw).hexdigest()+'.json'
        self.compare()['files'] = [changed(path, 'added')]
        self.compare()['files'][0]['sha'] = git_blob_sha(raw)
        self.client.blobs[(path, TARGET)] = raw
        result = self.reuse()
        self.assertEqual(result['changed_files'][0]['after_sha256'], hashlib.sha256(raw).hexdigest())

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
        for endpoint in ['/git/ref/heads/main', RUNS,
                         '/actions/runs/100/attempts/1/jobs?per_page=100',
                         f'/compare/{BASE}...{TARGET}?per_page=1&page=1']:
            with self.subTest(endpoint=endpoint):
                self.client = FakeClient(); self.client.responses[endpoint] = RuntimeError('private-token-must-not-leak')
                result = self.full()
                self.assertNotIn('private-token-must-not-leak', str(result))

    def test_malformed_main_reference_requires_full_instead_of_reuse(self):
        self.client.responses['/git/ref/heads/main'] = {}
        self.full()

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

    def test_prose_only_html_requires_equal_executable_structure(self):
        path = 'numerical-methods-atlas/ja/read/example/index.html'
        before = b'<main><h1>Old heading</h1><p>Old prose</p></main>'
        after = before.replace(b'Old', b'New')
        self.compare()['files'] = [changed(path)]
        self.compare()['files'][0]['sha'] = git_blob_sha(after)
        self.client.blobs[(path, BASE)] = before
        self.client.blobs[(path, TARGET)] = after
        self.reuse()

    def test_vetted_ui_scripts_require_the_exact_reviewed_transitive_sources(self):
        path = 'numerical-methods-atlas/ja/read/example/index.html'
        for script in ['site.js','numerical-methods-atlas/reading.js','numerical-methods-atlas/reading-index.mjs']:
            with self.subTest(script=script):
                self.client = FakeClient()
                before = ('<main><h1>Old heading</h1><script src="/'+script+'?v=known"></script></main>').encode()
                self.set_blob_change(path, before, before.replace(b'Old',b'New'))
                self.add_vetted_ui_blobs()
                result = self.reuse()
                verified = {row['path'] for row in result['vetted_presentation_scripts']}
                self.assertIn(script, verified)
                if script.endswith('reading.js'):
                    self.assertIn('numerical-methods-atlas/books.js', verified)

    def test_modified_vetted_ui_dependency_requires_full(self):
        path = 'numerical-methods-atlas/ja/read/example/index.html'
        before = b'<h1>Old heading</h1><script src="/numerical-methods-atlas/reading.js"></script>'
        self.set_blob_change(path, before, before.replace(b'Old',b'New'))
        self.add_vetted_ui_blobs()
        self.client.blobs[('numerical-methods-atlas/books.js', TARGET)] += b'\n// unreviewed change'
        self.full()

    def test_html_with_inline_dom_reader_or_unknown_external_script_requires_full(self):
        path = 'numerical-methods-atlas/ja/read/example/index.html'
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
        path = 'numerical-methods-atlas/ja/read/example/index.html'
        for before, after in pairs:
            with self.subTest(before=before):
                self.client = FakeClient(); self.compare()['files'] = [changed(path)]
                self.compare()['files'][0]['sha'] = git_blob_sha(after)
                self.client.blobs[(path, BASE)] = before; self.client.blobs[(path, TARGET)] = after
                self.full()

    def test_html_blob_unavailable_requires_full(self):
        self.compare()['files'] = [changed('numerical-methods-atlas/ja/read/example/index.html')]
        self.full()

    def test_html_wording_may_change_only_when_numeric_literals_are_unchanged(self):
        path = 'numerical-methods-atlas/ja/read/example/index.html'
        before = b'<main><h1>Old description</h1><p>dx=0.01 and 64 cells</p></main>'
        after = before.replace(b'Old description', b'New wording')
        self.compare()['files'] = [changed(path)]; self.compare()['files'][0]['sha'] = git_blob_sha(after)
        self.client.blobs[(path, BASE)] = before; self.client.blobs[(path, TARGET)] = after
        self.reuse()

    def test_unknown_html_and_wrong_target_blob_are_not_reusable(self):
        for path in ['about/index.html', 'numerical-methods-atlas/ja/read/example/index.html']:
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

    def run_cli(self, *, api_error=False, sha=TARGET):
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
                'GITHUB_RUN_ID':'10000','GITHUB_TOKEN':'secret-value-must-not-leak'}
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


if __name__ == '__main__':
    unittest.main()
