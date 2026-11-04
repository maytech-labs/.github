# 0005. The org's state is checkable with one command

- **Status:** Accepted
- **Date:** 2026-11-04

## Context

The profile ([profile/README.md](../../profile/README.md)) and the website ([0004](0004-site-on-github-pages.md)) describe every project by hand: name, description, release status, and links. When a repo is added, renamed, archived, or released, nothing says they're out of date. Checking means visiting every repo.

## Decision

- [`scripts/org-status.py`](../../scripts/org-status.py) reports the org's state and where the profile and site have drifted from it. It's Python with no dependencies beyond the standard library.
- For each public repo it reports the latest release, the license (whether it's REAL 1.0, per [0002](0002-real-license.md)), the last push, and the description.
- It reports drift: a repo missing from the profile or the site, an archived repo still listed, a link to a repo that doesn't exist, a version badge that doesn't match the latest release, a repo marked pre-release that has a release, a repo with no description, or a license other than REAL 1.0.
- It exits 0 when in sync, 1 on drift, and 2 when it can't run, so it can run in CI.
- `--json` prints the same data for other tools to read.
- Run it before editing the profile or the site, and after any repo is created, archived, or released.
- If it outgrows a script (more checks, other orgs, or use by agents), it becomes a tool in its own repo under REAL 1.0, installed from the tap ([0003](0003-one-homebrew-tap.md)).

## Consequences

- Updating the profile and the site starts from a list of what's wrong instead of a tour of every repo.
- It reads public data, anonymously when no GitHub token works, so the anonymous rate limit (60 requests an hour) caps it at about 55 repos per run (one request per repo, plus one for the list). Set `GITHUB_TOKEN` past that.
- It checks whether a repo is listed and whether versions match, not whether descriptions are still accurate. Prose stays a human check.
- It looks only at a repo's top-level license file. A full license audit is `real-check check` in that repo.

## Alternatives considered

- **Generate the profile and site from the API.** No drift at all, but every description would come from a one-line repo description and the pages would lose their hand-written copy.
- **A scheduled GitHub Action that opens issues on drift.** Worth adding once the script has settled; it would run this same script.
- **Check by hand.** What happened until now, and the profile and site already missed a new repo and two releases.
