"""Decide whether public numerical ZIPs need a fresh full Linux execution.

Only explicit prose/identity changes may reuse a previous *actual* full run.
The baseline is never a successful workflow whose numerical job was skipped.
This module performs no network, numerical execution, or Git operation on import.
"""
from __future__ import annotations

import base64
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
import math
from pathlib import PurePosixPath
import re
import time
from urllib.parse import parse_qs, quote, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener


REPOSITORY = "hrkoyama/hrkoyama.github.io"
API = "https://api.github.com/repos/" + REPOSITORY
WORKFLOW = "atlas-depth-linux.yml"
SCIENTIFIC_JOB = "public-supplements"
EXECUTION_STEP = "Install three pinned wheel dependencies and verify public ZIPs"
RUNS_ENDPOINT = "/actions/workflows/" + WORKFLOW + "/runs?branch=main&status=completed&per_page=100"
FAILURE_STATUSES = ("failure", "cancelled", "timed_out")
SHA = re.compile(r"[0-9a-f]{40}\Z")
MAX_COMPARE_FILES = 300
MAX_HTML_FILES = 24
MAX_HTML_FILE_BYTES = 1024 * 1024
MAX_HTML_TOTAL_BYTES = 4 * 1024 * 1024
NUMERIC_TOKENS = re.compile(r"[+-]?(?:(?:\d+\.\d*|\.\d+|\d+)(?:[eE][+-]?\d+)?)")
IDENTITY_FILES = {"catalog/atlas-identities.json", "catalog/atlas-identity-history.json"}
COPY_CATALOGS = {"catalog/" + name for name in (
    "atlas-home.json", "atlas-purpose.json", "atlas-goals.json", "atlas-reading-index.json",
    "atlas-detailed-reading.json", "atlas-test-problems.json", "atlas-methods.json",
)}
DERIVED_SEARCH_METADATA = {"search/" + name for name in (
    "index.json", "atlas-navigation.json", "atlas-query-index.json", "query-index.json", "asset-manifest.json",
)}
HASH_DETAIL = re.compile(r"search/details/([0-9a-f]{64})\.json\Z")
VETTED_PRESENTATION_BLOBS = {
    "site.js": "ec3543ea7b3ea20e3fc1b7b11d8f9868d6103bea",
    "numerical-methods-atlas/reading.js": "5235acb15f3c67886f1aac73c78a896f7b95a957",
    "numerical-methods-atlas/reading-index.mjs": "9b3846482036e7604a7ca1a8671f183346fe3311",
    "numerical-methods-atlas/books.js": "44c0ab95d62e039c985725cef33f33836650cb9b",
}
PRESENTATION_CLOSURES = {
    "site.js": ("site.js",),
    "numerical-methods-atlas/reading.js": ("numerical-methods-atlas/reading.js", "numerical-methods-atlas/books.js"),
    "numerical-methods-atlas/reading-index.mjs": ("numerical-methods-atlas/reading-index.mjs",),
}
NONEXECUTABLE_SCRIPT_TYPES = {"application/json", "application/ld+json", "application/mathml+xml", "text/plain", "math/tex", "math/tex; mode=display"}
SENSITIVE_WORDS = re.compile(r"(?:^|[/_.-])(?:inputs?|references?|reference-values|acceptance|tolerances?|golden|expected|results?|verification|requirements)(?:$|[/_.-])", re.I)
CRITICAL_CATALOG = re.compile(r"catalog/(?:atlas-depth[^/]*|atlas-registration|atlas-execution-examples|atlas-quantum-examples|atlas-reference-supplements|atlas-[^/]*supplements|atlas-legacy-reference[^/]*|atlas-ci|site-build-pipeline|atlas-agent-kits|atlas-rkdg-pilot)\.json\Z")
SENSITIVE_PROSE_KEYS = re.compile(r"(?:^|[_-])(?:ids?|keys?|code|paths?|urls?|href|src|refs?|references?|sha256|hash|commands?|scripts?|inputs?|acceptance|tolerances?|requirements?|formulas?|equations?|boundary|conditions?|models?|algorithms?|units?|parameters?|seeds?|grids?|basis|kpoints?)(?:$|[_-])", re.I)
PROSE_ANCESTORS = {"name", "title", "summary", "description", "note", "label", "caption", "text"}


class ScopeError(ValueError):
    """Uncertain API/history/diff; a fresh numerical execution is required."""


class InvalidEvent(ValueError):
    """The event cannot safely identify the checked public-main commit."""


def require(value, reason):
    if not value:
        raise ScopeError(reason)


def canonical_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def git_blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def strict_json(raw):
    def pairs(rows):
        result = {}
        for key, value in rows:
            require(key not in result, "duplicate-json-key")
            result[key] = value
        return result
    def floating(value):
        number = float(value)
        require(math.isfinite(number), "nonfinite-json-number")
        return number
    def constant(_):
        raise ScopeError("nonfinite-json-number")
    return json.loads(raw, object_pairs_hook=pairs, parse_float=floating, parse_constant=constant)


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args):
        return None


class Client:
    """Read-only, fixed-repository API; credentials and exception URLs are not logged."""
    def __init__(self, token):
        self.token = token
        self.opener = build_opener(_NoRedirect())
        self.deadline = time.monotonic() + 150
        self.total_bytes = 0
        self.html_bytes = 0

    def get(self, endpoint):
        require(isinstance(endpoint, str) and endpoint.startswith(("/actions/", "/compare/", "/contents/", "/git/ref/heads/main")), "unsupported-api-endpoint")
        require("\n" not in endpoint and "\r" not in endpoint and self.token, "api-credential-or-endpoint-unavailable")
        remaining = self.deadline - time.monotonic()
        require(remaining > 0, "api-deadline-exhausted")
        request = Request(API + endpoint, headers={
            "Authorization": "Bearer " + self.token,
            "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "Atlas-public-Linux-scope", "Cache-Control": "no-cache",
        })
        try:
            with self.opener.open(request, timeout=min(20, remaining)) as response:
                require(response.status == 200 and response.geturl() == API + endpoint, "unexpected-api-response")
                raw = response.read(8 * 1024 * 1024 + 1)
        except Exception as exc:
            raise ScopeError("api-read-failed") from None
        self.total_bytes += len(raw)
        require(len(raw) <= 8 * 1024 * 1024 and self.total_bytes <= 32 * 1024 * 1024, "api-response-budget-exceeded")
        return strict_json(raw)

    def blob(self, path, revision):
        require(safe_path(path) and SHA.fullmatch(revision or ""), "invalid-immutable-content-request")
        value = self.get("/contents/" + quote(path, safe="/") + "?ref=" + revision)
        require(isinstance(value, dict) and value.get("type") == "file" and value.get("encoding") == "base64", "unsupported-content-response")
        size = value.get("size")
        require(type(size) is int and 0 <= size <= MAX_HTML_FILE_BYTES, "html-file-budget-exceeded")
        try:
            raw = base64.b64decode("".join(value["content"].split()), validate=True)
        except Exception:
            raise ScopeError("invalid-content-encoding") from None
        require(len(raw) == size, "content-size-mismatch")
        require(git_blob_sha(raw) == value.get("sha"), "content-git-identity-mismatch")
        self.html_bytes += size
        require(self.html_bytes <= MAX_HTML_TOTAL_BYTES, "html-total-budget-exceeded")
        return raw


def safe_path(path):
    return isinstance(path, str) and bool(path) and "\\" not in path and not any(ord(c) < 32 for c in path) and not PurePosixPath(path).is_absolute() and all(p not in {"", ".", ".."} for p in path.split("/"))


def _generated_document(path):
    return bool(re.fullmatch(r"numerical-methods-atlas/(?:(?:ja|en)/read|methods|problems)/[^/]+/index\.(?:json|md|html)", path))


def _generated_json_document(path):
    return _generated_document(path) and path.endswith(".json") or bool(re.fullmatch(
        r"numerical-methods-atlas/(?:(?:ja|en)/read|methods|problems)/index\.json", path))


def _presentation_script(source):
    if source.startswith("/") and not source.startswith("//"):
        source = "https://hrkoyama.github.io" + source
    parsed = urlsplit(source)
    require(parsed.scheme == "https" and parsed.netloc == "hrkoyama.github.io" and not parsed.fragment,
            "unknown-external-presentation-script")
    require(set(parse_qs(parsed.query, keep_blank_values=True)) <= {"v"}, "unknown-script-query")
    path = parsed.path.lstrip("/")
    require(path in PRESENTATION_CLOSURES, "unknown-external-presentation-script")
    return path


class _HTMLSignature(HTMLParser):
    """Preserve behavior-bearing markup; only ordinary prose text is omitted."""
    protected = {"script", "style", "textarea", "option", "pre", "code", "template"}
    voids = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.events = []
        self.stack = []
        self.scripts = set()
        self.external_script = False

    def _check_active(self, tag, attrs):
        require(not any(name.startswith("on") for name, _ in attrs), "inline-event-handler")
        require(not any(isinstance(value, str) and re.sub(r"\s+", "", value).lower().startswith("javascript:") for _, value in attrs), "inline-javascript-url")
        require(tag not in {"iframe", "object", "embed"}, "unknown-active-html-content")
        if tag == "script":
            values = dict(attrs)
            if values.get("src"):
                self.scripts.add(_presentation_script(values["src"]))
                self.external_script = True
            else:
                require(values.get("type", "").strip().lower() in NONEXECUTABLE_SCRIPT_TYPES,
                        "inline-executable-script")
                self.external_script = False

    def handle_starttag(self, tag, attrs):
        require(len({name for name, _ in attrs}) == len(attrs), "duplicate-html-attribute")
        self._check_active(tag, attrs)
        self.events.append(["start", tag, sorted(attrs, key=lambda x: (x[0], str(x[1])))])
        if tag not in self.voids:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        require(len({name for name, _ in attrs}) == len(attrs), "duplicate-html-attribute")
        self._check_active(tag, attrs)
        self.events.append(["empty", tag, sorted(attrs, key=lambda x: (x[0], str(x[1])))])

    def handle_endtag(self, tag):
        self.events.append(["end", tag])
        if tag in self.stack:
            self.stack = self.stack[:len(self.stack) - 1 - self.stack[::-1].index(tag)]
        if tag == "script":
            self.external_script = False

    def handle_data(self, data):
        if self.stack and self.stack[-1] == "script" and self.external_script:
            require(not data.strip(), "inline-executable-script-with-src")
        if set(self.stack).intersection(self.protected):
            self.events.append(["data", data])
        else:
            # Mixed prose such as "dx=0.01" may contain a parameter consumed
            # by unchanged browser code. Preserve every numeric token.
            numbers = NUMERIC_TOKENS.findall(data)
            if numbers:
                self.events.append(["numbers", numbers])

    def handle_entityref(self, name):
        self.events.append(["entity", name])

    def handle_charref(self, name):
        self.events.append(["charref", name])

    def handle_comment(self, data):
        self.events.append(["comment", data])

    def handle_decl(self, decl):
        self.events.append(["decl", decl])

    def handle_pi(self, data):
        self.events.append(["pi", data])


def html_signature(raw):
    require(isinstance(raw, bytes) and len(raw) <= MAX_HTML_FILE_BYTES, "html-file-budget-exceeded")
    parser = _HTMLSignature()
    parser.feed(raw.decode("utf-8"))
    parser.close()
    return canonical_digest(parser.events)


def html_presentation_scripts(raw):
    parser = _HTMLSignature()
    parser.feed(raw.decode("utf-8"))
    parser.close()
    return set(parser.scripts)


def catalog_prose_signature(raw):
    """Ignore only bounded JA/EN prose wording, retaining JSON structure and data."""
    require(isinstance(raw, bytes) and len(raw) <= MAX_HTML_FILE_BYTES, "catalog-file-budget-exceeded")
    def project(value, path=()):
        if isinstance(value, dict):
            return ["object", [[key, project(item, path + (key,))] for key, item in sorted(value.items())]]
        if isinstance(value, list):
            return ["array", [project(item, path + (index,)) for index, item in enumerate(value)]]
        if isinstance(value, str):
            prose = path and path[-1] in {"ja", "en"} and any(part in PROSE_ANCESTORS for part in path[:-1]) and not any(
                isinstance(part, str) and SENSITIVE_PROSE_KEYS.search(part) for part in path[:-1])
            # A localized URL or code/path field is still an execution reference.
            reference = bool(re.search(r"(?:https?://|^/|(?:^|\s)(?:code|scripts|inputs|references)/)", value))
            if prose and not reference:
                require(not re.search(r"<\s*script\b", value, re.I), "catalog-active-markup")
                return ["prose", NUMERIC_TOKENS.findall(value), html_signature(value.encode("utf-8"))]
            return ["string", value]
        return [type(value).__name__, value]
    return canonical_digest(project(strict_json(raw)))


def validate_derived_detail(raw, path):
    require(isinstance(raw, bytes) and len(raw) <= MAX_HTML_FILE_BYTES, "derived-detail-budget-exceeded")
    match = HASH_DETAIL.fullmatch(path)
    require(match and hashlib.sha256(raw).hexdigest() == match[1], "derived-detail-content-address-mismatch")
    value = strict_json(raw)
    require(isinstance(value, dict) and set(value) == {"text"}, "invalid-derived-detail-schema")
    text = value["text"]
    require(isinstance(text, str) or isinstance(text, dict) and text and set(text) <= {"ja", "en"} and all(isinstance(v, str) and bool(v) for v in text.values()), "invalid-derived-detail-text")


def classify_change(file, before=None, after=None):
    """Return explicit safe/critical classification for one cumulative difference."""
    path, status = file.get("filename"), file.get("status")
    if not safe_path(path):
        return {"safe": False, "reason": "invalid-path"}
    if status not in {"modified", "added"}:
        return {"safe": False, "reason": "removed-renamed-or-unknown-status"}
    lower = path.lower()
    if path.startswith(("code/", "scripts/", ".github/", "tests/", "numart/", "validation/", "agent-kits/", "experiments/")) or lower.endswith(".zip"):
        return {"safe": False, "reason": "critical-code-verifier-or-distribution"}
    if CRITICAL_CATALOG.fullmatch(path) or lower.endswith(".schema.json"):
        return {"safe": False, "reason": "critical-catalog-or-schema"}
    if not _generated_document(path) and SENSITIVE_WORDS.search(lower):
        return {"safe": False, "reason": "critical-input-reference-or-criteria"}
    if path in IDENTITY_FILES or re.fullmatch(r"catalog/identity-snapshots/NMA-P-[0-9]{6,}/[0-9A-F]{2,}\.json", path):
        return {"safe": True, "reason": "identity-metadata"}
    if HASH_DETAIL.fullmatch(path):
        if after is None:
            return {"safe": False, "reason": "derived-detail-comparison-required"}
        validate_derived_detail(after, path)
        return {"safe": True, "reason": "content-addressed-derived-text"}
    if status == "added":
        return {"safe": False, "reason": "unclassified-new-file"}
    if path in {"README.md", "MAINTENANCE.md"} or (path.startswith("docs/") and lower.endswith(".md")) or re.fullmatch(r"guide/packs/[^/]+\.md", path) or (_generated_document(path) and lower.endswith(".md")):
        return {"safe": True, "reason": "prose-document"}
    if path in COPY_CATALOGS or _generated_json_document(path):
        if before is None or after is None:
            return {"safe": False, "reason": "catalog-prose-comparison-required"}
        if catalog_prose_signature(before) == catalog_prose_signature(after):
            return {"safe": True, "reason": "catalog-formatting-or-prose-only"}
        return {"safe": False, "reason": "critical-catalog-semantic-change"}
    if path == "guide/index.json" or path in DERIVED_SEARCH_METADATA or path == "numerical-methods-atlas/home-search-index.json":
        return {"safe": True, "reason": "presentation-metadata"}
    if path == "site.css" or re.fullmatch(r"styles/[^/]+\.css", path) or path in {"search/search.css", "search/navigation.css", "search/methods.css"}:
        return {"safe": True, "reason": "presentation-stylesheet"}
    if lower.endswith(".html"):
        if not (_generated_document(path) or re.fullmatch(r"numerical-methods-atlas/(?:ja|en)/read/index\.html", path)):
            return {"safe": False, "reason": "unclassified-html-source"}
        if before is None or after is None:
            return {"safe": False, "reason": "html-content-comparison-required"}
        if html_signature(before) == html_signature(after):
            return {"safe": True, "reason": "html-prose-only"}
        return {"safe": False, "reason": "critical-html-behavior-or-parameters"}
    return {"safe": False, "reason": "unclassified-change"}


def _event_target(event_name, event, sha, ref, repo, run_id):
    if repo != REPOSITORY or ref != "refs/heads/main" or not SHA.fullmatch(sha or "") or not isinstance(run_id, (str, int)) or not str(run_id).isdigit():
        raise InvalidEvent("unsupported-repository-ref-or-sha")
    if event_name == "workflow_run":
        run = event.get("workflow_run", {})
        if run.get("head_repository", {}).get("full_name") != REPOSITORY or run.get("head_branch") != "main" or run.get("conclusion") != "success" or run.get("head_sha") != sha:
            raise InvalidEvent("untrusted-or-superseded-workflow-run")
    elif event_name not in {"workflow_dispatch", "schedule"}:
        raise InvalidEvent("unsupported-event")


def _baseline(client, current_run_id):
    listing = client.get(RUNS_ENDPOINT)
    runs = listing.get("workflow_runs")
    require(isinstance(runs, list) and len(runs) <= 100, "invalid-history-list")
    # The ordinary history is created-order paginated. A recent retry of an
    # ancient run can therefore be absent, even though its full attempt failed
    # after our apparent baseline. Read complete bounded failure lists as well.
    runs = list(runs)
    for status in FAILURE_STATUSES:
        failed = client.get("/actions/workflows/" + WORKFLOW + "/runs?branch=main&status=" + status + "&per_page=100")
        rows = failed.get("workflow_runs")
        require(isinstance(rows, list) and type(failed.get("total_count")) is int and failed["total_count"] == len(rows) <= 100,
                "incomplete-failure-history")
        require(all(isinstance(row, dict) and row.get("status") == "completed" and row.get("conclusion") == status for row in rows),
                "invalid-filtered-failure-history")
        runs.extend(rows)
    unique = {}
    for run in runs:
        require(isinstance(run, dict) and type(run.get("id")) is int and type(run.get("run_attempt")) is int and run["run_attempt"] > 0,
                "invalid-history-run")
        key = (run["id"], run["run_attempt"])
        if key not in unique or str(run.get("updated_at", "")) > str(unique[key].get("updated_at", "")):
            unique[key] = run
    def order(run):
        require(isinstance(run, dict) and type(run.get("id")) is int and run["id"] > 0, "invalid-history-run")
        stamp = run.get("updated_at")
        require(isinstance(stamp, str), "missing-history-timestamp")
        return datetime.fromisoformat(stamp.replace("Z", "+00:00")), run["id"]
    for run in sorted(unique.values(), key=order, reverse=True):
        if str(run["id"]) == str(current_run_id):
            continue
        require(run.get("head_branch") == "main" and run.get("head_repository", {}).get("full_name") == REPOSITORY and run.get("status") == "completed", "untrusted-history-run")
        require(SHA.fullmatch(run.get("head_sha", "")) and type(run.get("run_attempt")) is int and run["run_attempt"] > 0, "invalid-history-identity")
        require(run.get("html_url") == f'https://github.com/{REPOSITORY}/actions/runs/{run["id"]}', "invalid-history-url")
        jobs_value = client.get(f'/actions/runs/{run["id"]}/attempts/{run["run_attempt"]}/jobs?per_page=100')
        jobs = jobs_value.get("jobs")
        require(isinstance(jobs, list) and type(jobs_value.get("total_count")) is int and jobs_value["total_count"] == len(jobs) < 100, "incomplete-job-history")
        scientific = [job for job in jobs if job.get("name") == SCIENTIFIC_JOB]
        require(len(scientific) == 1, "missing-or-ambiguous-scientific-job")
        job = scientific[0]
        require(job.get("run_id") == run["id"] and job.get("head_sha") == run["head_sha"], "scientific-job-identity-mismatch")
        if job.get("conclusion") == "skipped" and run.get("conclusion") == "success":
            continue
        require(run.get("conclusion") == "success" and job.get("status") == "completed" and job.get("conclusion") == "success", "latest-full-attempt-not-successful")
        steps = [step for step in job.get("steps", []) if step.get("name") == EXECUTION_STEP]
        require(len(steps) == 1 and steps[0].get("status") == "completed" and steps[0].get("conclusion") == "success", "missing-successful-full-execution-step")
        require(type(job.get("id")) is int and job["id"] > 0, "invalid-scientific-job-id")
        return {"run_id": run["id"], "run_attempt": run["run_attempt"], "sha": run["head_sha"],
                "job_id": job["id"], "url": run["html_url"], "completed_at": run["updated_at"],
                "actual_full_execution": True}
    raise ScopeError("no-full-success-baseline-in-history-window")


def plan(event_name, event, sha, ref, repo, run_id, client):
    """Plan fresh full verification or evidenced reuse; uncertainty always runs full."""
    _event_target(event_name, event, sha, ref, repo, run_id)
    result = {"schema_version": 1, "mode": "full", "run_full": True, "target_sha": sha,
              "event": event_name, "reason": "full-by-default", "reasons": [], "baseline": None,
              "changed_files": [], "comparison_sha256": None, "science_execution": "scheduled-full",
              "created_at_utc": datetime.now(timezone.utc).isoformat(), "repository": REPOSITORY,
              "history_window": 100, "numerical_execution_performed_by_planner": False}
    def full(reason):
        result.update(reason=reason, reasons=[reason])
        return result
    if event_name in {"workflow_dispatch", "schedule"}:
        return full("manual-always-full" if event_name == "workflow_dispatch" else "weekly-always-full")
    try:
        current = client.get("/git/ref/heads/main")
        current_sha = current.get("object", {}).get("sha")
        require(isinstance(current_sha, str) and SHA.fullmatch(current_sha), "invalid-main-ref-response")
        if current_sha != sha:
            raise InvalidEvent("target-is-not-current-main")
        baseline = _baseline(client, run_id)
        result["baseline"] = baseline
        comparison = client.get(f'/compare/{baseline["sha"]}...{sha}?per_page=1&page=1')
        require(comparison.get("status") in {"ahead", "identical"} and comparison.get("merge_base_commit", {}).get("sha") == baseline["sha"], "non-ancestral-comparison")
        files = comparison.get("files")
        require(isinstance(files, list) and len(files) < MAX_COMPARE_FILES, "missing-or-truncated-comparison")
        names, pending_content = set(), []
        for file in files:
            require(isinstance(file, dict) and safe_path(file.get("filename")) and file["filename"] not in names and SHA.fullmatch(file.get("sha", "")), "invalid-comparison-file")
            names.add(file["filename"])
            check = classify_change(file)
            row = {key: file[key] for key in ("filename", "status", "sha")}
            row.update(check)
            result["changed_files"].append(row)
            if check["reason"] in {"html-content-comparison-required", "catalog-prose-comparison-required", "derived-detail-comparison-required"}:
                pending_content.append((file, row))
        result["comparison_sha256"] = canonical_digest(result["changed_files"])
        critical = [r for r in result["changed_files"] if not r["safe"] and r["reason"] not in {"html-content-comparison-required", "catalog-prose-comparison-required", "derived-detail-comparison-required"}]
        if critical:
            return full("critical-or-unclassified-change")
        require(len(pending_content) <= MAX_HTML_FILES, "semantic-comparison-count-exceeded")
        html_bytes = 0
        verified_scripts = {}
        for file, row in pending_content:
            detail = bool(HASH_DETAIL.fullmatch(file["filename"]))
            before = None if detail else client.blob(file["filename"], baseline["sha"])
            after = client.blob(file["filename"], sha)
            require(git_blob_sha(after) == file["sha"], "target-content-git-identity-mismatch")
            html_bytes += (len(before) if before is not None else 0) + len(after)
            require(html_bytes <= MAX_HTML_TOTAL_BYTES, "semantic-total-budget-exceeded")
            if detail:
                row.update(classify_change(file, after=after), after_blob_sha=git_blob_sha(after),
                           after_sha256=hashlib.sha256(after).hexdigest(), after_bytes=len(after))
                continue
            signature = html_signature if file["filename"].endswith(".html") else catalog_prose_signature
            row.update(before_blob_sha=git_blob_sha(before), after_blob_sha=git_blob_sha(after),
                       before_semantic_signature=signature(before), after_semantic_signature=signature(after),
                       before_bytes=len(before), after_bytes=len(after))
            row.update(classify_change(file, before, after))
            if row["safe"] and file["filename"].endswith(".html"):
                scripts = html_presentation_scripts(before) | html_presentation_scripts(after)
                paths = sorted({p for script in scripts for p in PRESENTATION_CLOSURES[script]})
                for path in paths:
                    if path not in verified_scripts:
                        raw = client.blob(path, sha)
                        html_bytes += len(raw)
                        require(html_bytes <= MAX_HTML_TOTAL_BYTES, "semantic-total-budget-exceeded")
                        require(git_blob_sha(raw) == VETTED_PRESENTATION_BLOBS[path], "unvetted-presentation-script-content")
                        verified_scripts[path] = {"path": path, "git_blob_sha": git_blob_sha(raw), "bytes": len(raw)}
                row["vetted_script_paths"] = paths
        result["vetted_presentation_scripts"] = [verified_scripts[path] for path in sorted(verified_scripts)]
        result["semantic_content_bytes"] = html_bytes
        result["comparison_sha256"] = canonical_digest(result["changed_files"])
        if any(not row["safe"] for row in result["changed_files"]):
            return full("critical-html-or-catalog-content")
        result.update(mode="reuse", run_full=False, reason="only-reviewed-prose-or-identity-changes",
                      reasons=["only-reviewed-prose-or-identity-changes"],
                      science_execution="not-rerun-reused-proof")
        return result
    except InvalidEvent:
        raise
    except Exception as error:
        result["error_type"] = type(error).__name__
        return full(str(error) if isinstance(error, ScopeError) and re.fullmatch(r"[a-z0-9-]+", str(error)) else "api-or-history-error")
