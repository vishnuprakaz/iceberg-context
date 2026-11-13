"""Collect pull requests, issues and review discussion from GitHub.

Runs in GitHub Actions with the default GITHUB_TOKEN. That token allows about 1,000 GraphQL points and
1,000 REST requests per hour, so each run does a bounded amount of work and saves a cursor. History is
filled in over successive runs, oldest update first; once caught up, a run only fetches what changed.
"""
from __future__ import annotations

import os
import re
import time
from pathlib import Path

import yaml

from icekb import state
from icekb.util import clean_text, extract_refs, http_json, sha, upsert

API = "https://api.github.com"
START = "2014-01-01T00:00:00Z"
BOT = re.compile(r"\[bot\]$|^(dependabot|github-actions|copilot|codecov|asf-ci)", re.I)
NOISE = re.compile(r"^This (pull request|issue) has been (marked as stale|closed due to)|^This PR has been automatically", re.I)

PR_FIELDS = """
  number title bodyText state isDraft merged mergedAt closedAt createdAt updatedAt url baseRefName
  additions deletions changedFiles
  author { login } mergedBy { login } milestone { title }
  labels(first: 12) { nodes { name } }
  comments { totalCount } reviewThreads { totalCount }
  reactions(content: THUMBS_UP) { totalCount }
  files(first: 80) { nodes { path } }
  reviews(first: 40) { nodes { author { login } state submittedAt } }
  closingIssuesReferences(first: 5) { nodes { number } }
  authorAssociation
  reviewRequests(first: 10) { nodes { requestedReviewer { ... on User { login } ... on Team { name } } } }
  commits(last: 1) { nodes { commit { committedDate } } }
"""
# Bump when PR_FIELDS gains a field: the next run re-reads every open pull request once to fill it in.
PR_FIELDS_VERSION = 2
ISSUE_FIELDS = """
  number title bodyText state stateReason closedAt createdAt updatedAt url
  author { login } milestone { title }
  labels(first: 12) { nodes { name } }
  comments { totalCount }
  reactions(content: THUMBS_UP) { totalCount }
"""
QUERY = """
query($q: String!, $n: Int!, $after: String) {
  search(query: $q, type: ISSUE, first: $n, after: $after) {
    nodes { __typename ... on PullRequest { PR_FIELDS } ... on Issue { ISSUE_FIELDS } }
    pageInfo { hasNextPage endCursor }
  }
  rateLimit { remaining cost }
}
""".replace("ISSUE_FIELDS", ISSUE_FIELDS).replace("PR_FIELDS", PR_FIELDS)


class Budget(Exception):
    """Raised when the run should stop and resume next time."""


class Client:
    def __init__(self, token: str, max_seconds: int):
        self.headers = {"Authorization": f"Bearer {token}", "X-GitHub-Api-Version": "2022-11-28"}
        self.deadline = time.time() + max_seconds
        self.graphql_left = 1000
        self.rest_left = 1000
        self.calls = 0

    def _tick(self) -> None:
        self.calls += 1
        if time.time() > self.deadline:
            raise Budget("time budget used")

    def graphql(self, query: str, variables: dict) -> dict:
        if self.graphql_left < 80:
            raise Budget("GraphQL rate limit nearly used")
        self._tick()
        body, _ = http_json(f"{API}/graphql", method="POST", payload={"query": query, "variables": variables},
                            headers=self.headers)
        if body.get("errors") and not body.get("data"):
            message = body["errors"][0].get("message", "GraphQL error")
            if "rate limit" in message.lower():
                raise Budget(message)
            raise RuntimeError(message)
        self.graphql_left = body["data"]["rateLimit"]["remaining"]
        return body["data"]

    def rest(self, path: str) -> list:
        if self.rest_left < 40:
            raise Budget("REST rate limit nearly used")
        self._tick()
        body, headers = http_json(f"{API}{path}", headers=self.headers)
        self.rest_left = int(headers.get("X-RateLimit-Remaining") or headers.get("x-ratelimit-remaining") or self.rest_left - 1)
        return body


def _login(node: dict | None) -> str | None:
    return (node or {}).get("login")


def item_record(repo: str, node: dict) -> dict:
    is_pr = node["__typename"] == "PullRequest"
    number = node["number"]
    body = clean_text(node.get("bodyText") or "", limit=4000)
    state_ = "merged" if node.get("merged") else node["state"].lower()
    meta = {
        "repo": repo, "number": number, "state": state_, "updated_at": node["updatedAt"], "closed_at": node.get("closedAt"),
        "labels": [n["name"] for n in node["labels"]["nodes"]], "milestone": (node.get("milestone") or {}).get("title"),
        "comments": node["comments"]["totalCount"] + (node.get("reviewThreads") or {}).get("totalCount", 0),
        "thumbs_up": node["reactions"]["totalCount"],
    }
    if is_pr:
        meta.update({
            "draft": node["isDraft"], "merged_at": node.get("mergedAt"), "merged_by": _login(node.get("mergedBy")),
            "base": node["baseRefName"], "additions": node["additions"], "deletions": node["deletions"],
            "n_files": node["changedFiles"], "files": [f["path"] for f in node["files"]["nodes"]],
            "reviews": [{"by": _login(r["author"]), "state": r["state"], "at": r["submittedAt"]}
                        for r in node["reviews"]["nodes"] if _login(r["author"]) and not BOT.search(_login(r["author"]))],
            "closes": [n["number"] for n in node["closingIssuesReferences"]["nodes"]],
            "association": node.get("authorAssociation"),
            "requested": [(r.get("requestedReviewer") or {}).get("login") or (r.get("requestedReviewer") or {}).get("name")
                          for r in (node.get("reviewRequests") or {}).get("nodes") or [] if r.get("requestedReviewer")],
            "last_commit": next((c["commit"]["committedDate"] for c in (node.get("commits") or {}).get("nodes") or []), None),
        })
    else:
        meta["state_reason"] = node.get("stateReason")
    author = _login(node.get("author"))
    return {
        "id": f"gh:{repo}#{number}",
        "source": "github",
        "type": "pr" if is_pr else "issue",
        "date": node["createdAt"],
        "url": node["url"],
        "people": [author] if author else [],
        "title": clean_text(node["title"]),
        "body": body,
        "refs": [r for r in extract_refs(node["title"] + "\n" + body, repo) if r != f"gh:{repo}#{number}"]
                + [f"gh:{repo}#{n}" for n in meta.get("closes", [])],
        "hash": sha(node["updatedAt"]),
        "meta": {k: v for k, v in meta.items() if v not in (None, [], "")},
    }


def collect_items(client: Client, root: Path, repo: str, kind: str, cursor: dict, page_size: int) -> int:
    """Walk pull requests or issues in order of last update, starting from the saved timestamp."""
    key = f"{kind}_updated"
    since = cursor.get(key) or START
    short = repo.split("/")[1]
    total = 0
    after = None
    while True:
        q = f"repo:{repo} is:{'pr' if kind == 'prs' else 'issue'} updated:>={since} sort:updated-asc"
        data = client.graphql(QUERY, {"q": q, "n": page_size, "after": after})
        nodes = [n for n in data["search"]["nodes"] if n.get("number")]
        if nodes:
            total += len(nodes)
            upsert(root, f"github/{short}/{kind}", [item_record(repo, n) for n in nodes])
            newest = max(n["updatedAt"] for n in nodes)
            if newest > since:
                since, after = newest, None  # restart the window at the newest update seen
            else:
                after = data["search"]["pageInfo"]["endCursor"]  # many items share one timestamp: page through them
            cursor[key] = since
        if len(nodes) < page_size and not (after and data["search"]["pageInfo"]["hasNextPage"]):
            cursor[f"{kind}_caught_up"] = True
            return total


def comment_record(repo: str, c: dict, kind: str) -> dict | None:
    user = (c.get("user") or {}).get("login") or ""
    body = clean_text(c.get("body") or "", limit=1200)
    if not user or BOT.search(user) or (c.get("user") or {}).get("type") == "Bot" or len(body) < 25 or NOISE.search(body):
        return None
    number = int((c.get("pull_request_url") or c.get("issue_url") or "/0").rsplit("/", 1)[1])
    meta = {"repo": repo, "number": number, "kind": kind}
    if c.get("path"):
        meta["path"] = c["path"]
    return {
        "id": f"gh:{repo}#{number}/c{c['id']}",
        "source": "github",
        "type": "comment",
        "date": c["created_at"],
        "url": c["html_url"],
        "people": [user],
        "title": f"{'Review comment' if kind == 'review' else 'Comment'} on {repo}#{number}" + (f" ({c['path']})" if c.get("path") else ""),
        "body": body,
        "refs": [f"gh:{repo}#{number}"] + [r for r in extract_refs(body, repo) if r != f"gh:{repo}#{number}"],
        "hash": sha(c["updated_at"]),
        "meta": meta,
    }


def collect_comments(client: Client, root: Path, repo: str, kind: str, cursor: dict, start: str) -> int:
    key = f"{kind}_comments_updated"
    since = cursor.get(key) or start
    endpoint = "pulls/comments" if kind == "review" else "issues/comments"
    short = repo.split("/")[1]
    total, page = 0, 1
    while True:
        batch = client.rest(f"/repos/{repo}/{endpoint}?sort=updated&direction=asc&per_page=100&since={since}&page={page}")
        records = [r for r in (comment_record(repo, c, kind) for c in batch) if r]
        if records:
            upsert(root, f"github/{short}/comments", records)
            total += len(records)
        newest = max((c["updated_at"] for c in batch), default=since)
        if newest > since:
            since, page = newest, 1  # restart the window at the newest update seen
        else:
            page += 1  # a full page with one timestamp: page through it
        cursor[key] = since
        if len(batch) < 100:
            cursor[f"{kind}_comments_caught_up"] = True
            return total


def refresh_open(client: Client, root: Path, repo: str, cursor: dict, page_size: int) -> int:
    """Re-read all open pull requests once after PR_FIELDS changes, so that fields new to the query are filled in
    for pull requests that have not been updated since."""
    if cursor.get("open_fields_version") == PR_FIELDS_VERSION:
        return 0
    short, total, after = repo.split("/")[1], 0, None
    while True:
        data = client.graphql(QUERY, {"q": f"repo:{repo} is:pr is:open sort:updated-desc", "n": page_size, "after": after})
        nodes = [n for n in data["search"]["nodes"] if n.get("number")]
        upsert(root, f"github/{short}/prs", [item_record(repo, n) for n in nodes])
        total += len(nodes)
        info = data["search"]["pageInfo"]
        if not info["hasNextPage"]:
            cursor["open_fields_version"] = PR_FIELDS_VERSION
            return total
        after = info["endCursor"]


def collect(root: Path, *, max_minutes: str | int = 25, page_size: str | int = 40, **_ignored) -> dict:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN is not set; this collector runs in the daily GitHub Action")
    cfg = yaml.safe_load((root / "data" / "sources.yaml").read_text())
    comments_start = str(cfg.get("github", {}).get("comments_since", "2026-01-01")) + "T00:00:00Z"
    client = Client(token, int(max_minutes) * 60)
    st = state.load(root, "github")
    cursor = dict(st.get("cursor") or {})
    counts = {"prs": 0, "issues": 0, "comments": 0}
    stopped = ""
    repos = [r["name"] for r in cfg["repos"] if r.get("depth") == "full"]
    try:
        for repo in repos:
            cur = cursor.setdefault(repo, {})
            if cur.get("prs_caught_up"):
                counts["prs"] += refresh_open(client, root, repo, cur, int(page_size))
            for kind in ("prs", "issues"):
                counts[kind] += collect_items(client, root, repo, kind, cur, int(page_size))
        for repo in repos:
            cur = cursor[repo]
            for kind in ("review", "issue"):
                counts["comments"] += collect_comments(client, root, repo, kind, cur, comments_start)
    except Budget as stop:
        stopped = str(stop)
    caught_up = all(cursor.get(r, {}).get(f"{k}_caught_up") for r in repos
                    for k in ("prs", "issues", "review_comments", "issue_comments"))
    state.save(root, "github", ok=True, cursor=cursor,
               counts={"last_prs": counts["prs"], "last_issues": counts["issues"], "last_comments": counts["comments"],
                       "backfill": "complete" if caught_up else "in progress", "api_calls": client.calls})
    return {**counts, "stopped": stopped or "caught up", "api_calls": client.calls}
