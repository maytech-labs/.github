#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-REAL-1.0
"""Report the state of the maytech-labs org and where the profile and site have drifted from it.

Usage: scripts/org-status.py [--json] [--site PATH]

Reads the org's repos from the GitHub API (with $GITHUB_TOKEN or `gh auth token` when available,
anonymously otherwise), then checks each against profile/README.md and the website's index.html.
Exits 0 when everything is in sync, 1 when something has drifted, 2 when it could not run.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ORG = "maytech-labs"
ROOT = Path(__file__).resolve().parent.parent
PROFILE = ROOT / "profile" / "README.md"
DEFAULT_SITE = ROOT.parent / f"{ORG}.github.io" / "index.html"
# Repos that are the profile and the site themselves, not projects to list.
META = {".github", f"{ORG}.github.io"}


def token():
    if os.environ.get("GITHUB_TOKEN"):
        return os.environ["GITHUB_TOKEN"]
    try:
        out = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return out.stdout.strip() if out.returncode == 0 else None


def get(url, auth, raw=False):
    req = urllib.request.Request(url, headers={"User-Agent": f"{ORG}-org-status"})
    if auth:
        req.add_header("Authorization", f"Bearer {auth}")
    if raw and url.startswith("https://api.github.com/"):
        req.add_header("Accept", "application/vnd.github.raw+json")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read().decode()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise
    return body if raw else json.loads(body)


def fetch_repo(repo, auth):
    name, branch = repo["name"], repo["default_branch"]
    release = get(f"https://api.github.com/repos/{ORG}/{name}/releases/latest", auth)
    license_text = None
    for f in ("LICENSE.md", "LICENSE", "COPYING"):
        url = (f"https://api.github.com/repos/{ORG}/{name}/contents/{f}?ref={branch}" if repo["private"]
               else f"https://raw.githubusercontent.com/{ORG}/{name}/{branch}/{f}")
        license_text = get(url, auth if repo["private"] else None, raw=True)
        if license_text:
            break
    first = next((l for l in (license_text or "").splitlines() if l.strip()), "")
    return {
        "name": name,
        "description": repo["description"] or "",
        "archived": repo["archived"],
        "private": repo["private"],
        "pushed": repo["pushed_at"][:10],
        "release": version(release["tag_name"]) if release else None,
        "license": "REAL 1.0" if "Reciprocal Ethical AI License" in first and "1.0" in first
        else ("missing" if not license_text else "other"),
    }


def version(tag):
    """The version in a release tag: v1.2.3, godo-v1.2.3, and 1.2.3 all give 1.2.3."""
    m = re.search(r"(\d+(?:\.\d+)*(?:[-+][\w.]+)?)$", tag)
    return m.group(1) if m else tag


def mentions(text, name):
    return re.search(rf"(github\.com/{ORG}/|{ORG}\.github\.io/){re.escape(name)}(?![\w.-])", text) is not None


def site_badge(html, name):
    m = re.search(rf"<h3>{re.escape(name)}\s*<span class=\"badge\">([^<]+)</span>", html)
    return m.group(1).strip() if m else None


def check(repos, profile, site):
    drift = []
    names = {r["name"] for r in repos}
    for r in repos:
        n = r["name"]
        if n in META:
            continue
        if r["private"]:
            # Private repos aren't listed publicly; only their license is checked.
            if r["license"] != "REAL 1.0":
                drift.append(f"{n} (private): license is {r['license']}, not REAL 1.0")
            if mentions(profile, n) or (site is not None and mentions(site, n)):
                drift.append(f"{n}: private, but linked from the profile or site")
            continue
        if r["archived"]:
            if mentions(profile, n):
                drift.append(f"{n}: archived but still in profile/README.md")
            if site is not None and mentions(site, n):
                drift.append(f"{n}: archived but still on the site")
            continue
        if not r["description"]:
            drift.append(f"{n}: repo has no description")
        if r["license"] != "REAL 1.0":
            drift.append(f"{n}: license is {r['license']}, not REAL 1.0")
        if not mentions(profile, n):
            drift.append(f"{n}: not in profile/README.md")
        if site is not None:
            if not mentions(site, n):
                drift.append(f"{n}: not on the site")
            badge = site_badge(site, n)
            if r["release"] and badge and re.fullmatch(r"v?\d+(\.\d+)*", badge) and badge.lstrip("v") != r["release"]:
                drift.append(f"{n}: site badge says {badge}, latest release is {r['release']}")
            if r["release"] and badge == "pre-release":
                drift.append(f"{n}: site says pre-release, but {r['release']} is released")
    for text, where in ((profile, "profile/README.md"), (site or "", "the site")):
        for n in sorted(set(re.findall(rf"github\.com/{ORG}/([\w.-]+?)(?=[/)\"'#\s]|$)", text))):
            if n not in names:
                drift.append(f"{n}: linked from {where}, but no public repo has that name")
    return drift


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true", help="print JSON instead of a table")
    ap.add_argument("--site", type=Path, default=DEFAULT_SITE,
                    help=f"path to the site's index.html (default: {DEFAULT_SITE}); fetched from GitHub when missing")
    args = ap.parse_args()

    auth = token()
    if auth:
        try:
            get("https://api.github.com/rate_limit", auth)
        except urllib.error.HTTPError as e:
            if e.code != 401:
                raise
            print("org-status: GitHub token rejected; continuing anonymously", file=sys.stderr)
            auth = None
    try:
        listing = get(f"https://api.github.com/orgs/{ORG}/repos?per_page=100&type=all", auth)
        repos = sorted((fetch_repo(r, auth) for r in listing), key=lambda r: r["name"])
        site = args.site.read_text() if args.site.exists() else get(
            f"https://raw.githubusercontent.com/{ORG}/{ORG}.github.io/main/index.html", None, raw=True)
    except (urllib.error.URLError, OSError, ValueError) as e:
        print(f"org-status: could not run: {e}", file=sys.stderr)
        return 2
    drift = check(repos, PROFILE.read_text(), site)

    if args.json:
        print(json.dumps({"repos": repos, "drift": drift}, indent=2))
    else:
        cols = ("name", "release", "license", "pushed", "description")
        rows = [[r["name"] + (" (archived)" if r["archived"] else "") + (" (private)" if r["private"] else ""), r["release"] or "-",
                 r["license"], r["pushed"], r["description"][:60]] for r in repos]
        widths = [max(len(c), *(len(row[i]) for row in rows)) for i, c in enumerate(cols)]
        for row in [list(cols)] + rows:
            print("  ".join(v.ljust(w) for v, w in zip(row, widths)).rstrip())
        print()
        if not auth:
            print("note: no working GitHub token, so private repos aren't checked (set GITHUB_TOKEN or run gh auth login)")
        if site is None:
            print("note: site index.html not found locally or on GitHub; site checks skipped")
        print("\n".join(f"drift: {d}" for d in drift) if drift else "in sync: profile and site match the org")
    return 1 if drift else 0


if __name__ == "__main__":
    sys.exit(main())
