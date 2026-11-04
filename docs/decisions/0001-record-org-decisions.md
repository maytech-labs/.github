# 0001. Record org-wide decisions here

- **Status:** Accepted
- **Date:** 2026-11-04

## Context

arm-tools, mochi-donut, and arm-lessons each keep decision records in `docs/decisions/`. Some choices span every repo (the license, the Homebrew tap, the website), and so far each repo has recorded its own copy of them, or none has.

## Decision

- Org-wide decisions live in this repo's `docs/decisions/`, in the same format as the project repos ([0000-template.md](0000-template.md)).
- A project repo that adopts an org decision links to it here rather than restating it.
- Project-specific decisions stay in the project's repo.

## Consequences

- One place to look for anything that applies across maytech-labs.
- New repos have a written baseline to follow.
- Older project records (arm-tools 0045, 0047; mochi-donut 0038, 0039) still describe org choices in their own words. They aren't rewritten; new ones link here.

## Alternatives considered

- **Keep recording in every repo.** Copies drift, and repos without records (real-check, real-license, homebrew-tap) have none.
- **A wiki.** Not reviewed in pull requests, and not versioned with the code.
